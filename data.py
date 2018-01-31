import fastText
import json
import random

from singleton import Singleton


class Data(metaclass=Singleton):
    def __init__(self):
        self.answers = []
        self.fast_text_model = None

    def process(self, data_file):
        self.load_answers(data_file)
        self.create_labeled_questions_file(data_file, "fasttext_data.txt")
        self.fast_text_model = fastText.train_supervised("fasttext_data.txt")

    def create_labeled_questions_file(self, in_file_name, out_file_name):
        with open(in_file_name, "r", encoding="utf-8") as in_file:
            json_object = json.load(in_file)
            pairs = json_object["pairs"]

            with open(out_file_name, "w", encoding="utf-8") as out_file:
                for i, pair in enumerate(pairs):
                    questions = pair["question"]
                    for question in questions:
                        out_file.write("__label__" + str(i) + " " + question + "\n")

    def load_answers(self, in_file_name):
        with open(in_file_name, "r", encoding="utf-8") as in_file:
            json_object = json.load(in_file)
            pairs = json_object["pairs"]
            for pair in pairs:
                answers = pair["answer"]
                self.answers.append(answers)

    def get_answer(self, message):
        label = self.fast_text_model.predict(message)[0][0]
        answer_index = int(label.replace("__label__", ""))
        possible_answers = self.answers[answer_index]
        return random.choice(possible_answers)
