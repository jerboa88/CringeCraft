<!-- Project Header -->
<div align="center">
  <img class="projectLogo" src="config/container/logo.png" alt="Project logo" title="Project logo" width="256">

  <h1 class="projectName">CringeCraft MC Server</h1>

  <p class="projectBadges">
    <img src="https://img.shields.io/badge/type-Docker_Container-2196f3.svg" alt="Project type" title="Project type">
    <img src="https://img.shields.io/github/languages/top/jerboa88/CringeCraft.svg" alt="Language" title="Language">
    <img src="https://img.shields.io/github/repo-size/jerboa88/CringeCraft.svg" alt="Repository size" title="Repository size">
    <a href="LICENSE">
      <img src="https://img.shields.io/github/license/jerboa88/CringeCraft.svg" alt="Project license" title="Project license"/>
    </a>
  </p>

  <p class="projectDesc">
    A containerized PaperMC server that can be self-hosted using Docker & playit.gg
  </p>

  <br/>
</div>


## About
> Note that this project is configured for a specific use case so if you want to use this as a template for your own project, you'll need to change some things.

The goal of this project is to create a PaperMC server that is secure, portable, and easy to self-host.

It uses Docker Compose to build upon the awesome [itzg/minecraft-server] image. This allows us to run the server almost anywhere and lets us to deterministically set up the server with all relevant plugins and config. Please refer to that project for further configuration options and setup instructions.

The reverse proxy [playit.gg] is used so we can host the server on any machine without having to worry about port forwarding or DDNS.


## Installation
1. Install [Docker](https://www.docker.com/)
3. Download (and unzip) this repo
4. Make an account and tunnel on [playit.gg](https://playit.gg/).
   1. Create a new file called `playit_agent_secret.txt` in the `secrets/` directory
   2. Copy the agent secret and paste it into that file (see [Secrets](#secrets))
   3. Copy the port number given by and paste it into the `ports` section of `docker-compose.yml` (see [Docker Compose](#docker-compose])
5. Add all other required secrets to `secrets/` (see [Secrets](#secrets))
6. Profit!


## Usage
### Running the server
Run `docker compose up` in the top-most directory to run the server and `docker compose down` to stop it. You can also use `docker compose up -d` to run the server in the background.

### Configuration
#### Docker Compose (`docker-compose.yml`)
Docker Compose allows us to augment an existing Docker image with additional configuration. Everything defined in the `docker-compose.yml` file is used to build the container that runs the server. Since we are using [itzg/minecraft-server], please see that project for more details on the available configuration options. We will only cover the options that are relevant to this project here.

- `ports`: This maps the container's port 25565 to the host's port 22608. This is required so we can connect to the server from the outside world. Make sure that the second (outside) port is set to the port number given by [playit.gg]. The first (inside) port can be left as-is.
- `volumes`: This mounts our local `./config/minecraft` directory into the container's `/config` directory and mount our local `./config/container` directory into the container's `/container` directory. This is required so we can access our config files from the container. If you rename these directories, you'll need to update the `volumes` section accordingly.
- `secrets`: This tells Docker where to find our secret files. If you rename the `secrets` directory or the name of files in this directory, you'll need to update the `secrets` section accordingly.


#### Container Config (`config/container/`)
This directory contains configuration files for the Docker container created by [itzg/minecraft-server]. Use this directory to store any files that need to be accessed from the container, but don't need to be copied into the server's config directory. For example, we can put the server logo in this directory and with the following line in `docker-compose.yml`, the image will be converted into the correct format and placed in the server's root directory by the image: `ICON: /container/logo.png`.

#### Server Config (`config/minecraft/`)
This directory contains configuration files for the Minecraft server. Anything you put in this directory will be copied directly into the server's config directory. Note that will overwrite any existing files with the same name that are already in the container.

#### Secrets (`secrets/`)
Passwords and other sensitive information for the server are stored in the `secrets/` directory. These files are not tracked by git so you'll need to create them yourself when you first set up the project. Do not share these files with anyone.

By default, this project requires the following secret files to be added:
- `bstats_server_uuid.txt`: The UUID for the server on [bStats]. This is used to track server statistics.
- `playit_agent_secret.txt`: The secret for the server on [playit.gg]. This is used to authenticate the server with the reverse proxy.
- `rcon_password.txt`: The password for the RCON server. This is used to remotely control the server. Make sure this is set to something secure.

Each of these files should contain a single line with the relevant information. All of these secrets are loaded in `docker-compose.yml` and used to replace various placeholders in the server config files.


## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

The [itzg/minecraft-server] image is fetched at runtime by Docker Compose, but it is licensed under the Apache License 2.0.


[itzg/minecraft-server]: https://github.com/itzg/docker-minecraft-server
[playit.gg]: https://playit.gg/
[bStats]: https://bstats.org/
