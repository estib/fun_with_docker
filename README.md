# fun_with_docker
This project allows you to quickly set up MySQL, Redis, and the DD-Agent containers

First and foremost - download Docker compose if you haven't already (If you've got Docker on Mac OS, it comes with compose)
https://docs.docker.com/compose/install/#install-compose

Then you'll want to clone this repo

Then you'll want to update the docker-compose.yml file with your API and APP keys whereever it asks for them under the "environment" header, (otherwise, the dd-agent container, or the timeboard writer containers won't work).
