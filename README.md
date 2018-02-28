# fun_with_docker
This project allows you to quickly set up ElasticSearch, Flask, MySQL, NGINX, Postgres, Redis and the DD-Agent containers (along with two "helper" containers)*

First and foremost - download Docker compose if you haven't already (If you've got Docker on Mac OS, it comes with compose)
https://docs.docker.com/compose/install/#install-compose

Then you'll want to clone this repo:
git clone https://github.com/szaporta/fun_with_docker.git

Then you'll want to update the docker-compose.yml file with your API and APP keys whereever it asks for them under the "environment" header, (otherwise, the dd-agent container, or the timeboard writer containers won't work).

Then, just sit back as the images pull, the metrics for the above containers start sending, and the ES, MySQL, PG, and Redis Timeboards are automatically created by the "api helper" container :) (the timeboards are super basic at the moment, sorry!)

Extra Note: There are sample data sets pre-loaded in the MySQL and PostGres database containers, so if you want to query stuff manually, and play around with rdbms containers without worrying about breaking something, this is a good way to start. (Editor's Note: I'll be adding Redis and ES data sets soon.)

* The helper containers are intended to perform a single function per container. The ubuntu_siege one utilizes Siege to stress test a web server container (in this repo's case, it's the NGINX one), and the ubuntu_mysql one queries the MySQL server container repeatedly to simulate SELECT statements going into the MySQL container on the same network as the ubuntu_mysql one.
This enables some activity in certain metrics, rather than just a boring flat line.

