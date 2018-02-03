import fastText
import json
import random

from expand_text import expand_text
from singleton import Singleton


class Data(metaclass=Singleton):
    def __init__(self):
        self.answers = []
        self.fast_text_model = None
        self._allCombinationsOfSinglePattern = []

    def process(self, data_file):
        json_object = self.load_json(data_file)
        json_object = self.replace_entities(json_object)
        self.load_answers(json_object)
        self.create_labeled_questions_file(json_object, "fasttext_data.txt")
        self.fast_text_model = fastText.train_supervised("fasttext_data.txt", epoch=50)

    def load_json(self, data_file):
        with open(data_file, "r", encoding="utf-8") as in_file:
            json_object = json.load(in_file)
        return json_object

    def replace_entities(self, json_object):
        for entity in json_object["entities"]:
            entity_name = entity["name"]
            entity_value = entity["value"]

            for i, entity2 in enumerate(json_object["entities"]):
                json_object["entities"][i]["value"] = entity2["value"].replace("$$" + entity_name + "$$", entity_value)

            for i, pair in enumerate(json_object["pairs"]):
                for j, question in enumerate(pair["question"]):
                    json_object["pairs"][i]["question"][j] = question.replace("$$" + entity_name + "$$", entity_value)
                for j, answer in enumerate(pair["answer"]):
                    json_object["pairs"][i]["answer"][j] = answer.replace("$$" + entity_name + "$$", entity_value)
        return json_object

    def create_labeled_questions_file(self, json_object, out_file_name):
        pairs = json_object["pairs"]
        with open(out_file_name, "w", encoding="utf-8") as out_file:
            for i, pair in enumerate(pairs):
                questions = pair["question"]
                for question in questions:
                    question_all_variants = expand_text(question)
                    for question_variant in question_all_variants:
                        question_variant = question_variant.lower()
                        out_file.write("__label__" + str(i) + " " + question_variant + "\n")

    def load_answers(self, json_object):
        pairs = json_object["pairs"]
        for pair in pairs:
            answers = pair["answer"]
            answers_all_variants = []
            for answer in answers:
                answers_all_variants += expand_text(answer)
            self.answers.append(answers_all_variants)


    def get_answer(self, message):
        message = message.lower()
        label = self.fast_text_model.predict(message)[0][0]
        answer_index = int(label.replace("__label__", ""))
        possible_answers = self.answers[answer_index]
        return random.choice(possible_answers)
