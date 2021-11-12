FROM ubuntu 
USER root 
RUN mkdir -p jenkins_dir
RUN chmod 777 jenkins_dir 
RUN apt-get update -qq 
RUN apt-get install openjdk-8-jdk -qq
RUN apt-get install openssh-server -qq
RUN useradd -ms /bin/bash jenkins
RUN mkdir /root/.ssh
COPY authorized_keys /root/.ssh/authorized_keys
WORKDIR /jenkins_dir
CMD chmod 400 ~/.ssh/authorized_keys;service ssh start;bash
