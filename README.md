# pyqrcode-docker
Repo for creating arbitrary QR codes

## To use
You first need to create the container: `docker build -t bandi13/pyqrcode .`. Alternatively, you can just use the one from my DockerHub repository ([bandi13/pyqrcode](https://hub.docker.com/repository/docker/bandi13/pyqrcode/general)).

Then you can run it like so: `docker run --rm -it bandi13/pyqrcode "Hello world"`

There are various arguments you can add to change the output. This is done by passing `-e PYQRCODE_x` to the `docker run` command, where `x` is one of the following:
- ERROR: error correction level. One of 'L', 'M', 'Q', or 'H'
- VERSION: size and data capacity of the code. Integer between 1 and 40
- MODE: one of either 'numeric', 'alphanumeric', 'binary', or 'kanji'
- FGCOLOR: color of the terminal foreground
- BGCOLOR: color of the terminal background

This will also output the PNG image to the local directory if you pass in `-v $(pwd):/app`.

# Support
[<img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" height=36>](https://www.buymeacoff.ee/bandi13) or [<img src="https://storage.ko-fi.com/cdn/kofi2.png?v=3" height=36>](https://ko-fi.com/bandi13)
