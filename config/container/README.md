#### Container Config (`config/container/`)
This directory contains configuration files for the Docker container created by [itzg/minecraft-server]. Use this directory to store any files that need to be accessed from the container, but don't need to be copied into the server's config directory. For example, we can put the server logo in this directory and with the following line in `docker-compose.yml`, the image will be converted into the correct format and placed in the server's root directory by the image: `ICON: /container/logo.png`.

[itzg/minecraft-server]: https://github.com/itzg/docker-minecraft-server
