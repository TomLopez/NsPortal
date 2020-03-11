FROM ubuntu:18.04

RUN apt-get update -y 
RUN apt-get -y install sudo

RUN apt-get install -y python3 
RUN apt-get install -y python3-pip 
RUN python3 -m pip install --upgrade pip setuptools
CMD sudo su
CMD curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
CMD curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
CMD exit
CMD sudo apt-get update

CMD sudo ACCEPT_EULA=Y apt-get install msodbcsql17
CMD echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
CMD echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
CMD source ~/.bashrc

RUN apt-get install libssl1.0.0 libssl-dev
RUN apt-get -y install unixodbc-dev
RUN pip install virtualenv

ADD . /code
WORKDIR /code

RUN virtualenv -p /usr/bin/python3 env
CMD source env/Scripts/activate
RUN python3 setup.py install



RUN pserve development.ini
