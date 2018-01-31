# Alquist Interactive Movie Dialog

## How to run
### The first time
```commandline
docker build -t AlquistInteractiveMovieDialogImage .; docker run -d --name AlquistInteractiveMovieDialogContainer AlquistInteractiveMovieDialogImage
```

### Redeployment
```commandline
docker rm AlquistInteractiveMovieDialogContainer -f;docker build -t AlquistInteractiveMovieDialogImage .;docker run -d --name AlquistInteractiveMovieDialogContainer AlquistInteractiveMovieDialogImage;
```