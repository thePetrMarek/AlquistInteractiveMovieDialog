# Alquist Interactive Movie Dialog

## How to run
### The first time
```commandline
docker build -t alquist_interactive_movie_dialog_image .; docker run -d -p 5678:5678 --name alquist_interactive_movie_dialog_container alquist_interactive_movie_dialog_image
```

### Redeployment
```commandline
docker rm alquist_interactive_movie_dialog_container -f;docker build -t alquist_interactive_movie_dialog_image .;docker run -d -p 5678:5678 --name alquist_interactive_movie_dialog_container alquist_interactive_movie_dialog_image;
```

## API
Send GET with argument ``message``.