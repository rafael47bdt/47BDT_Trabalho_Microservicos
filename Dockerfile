FROM mysql

MAINTAINER Rafael Marques <rafamds1942@gmail.com>

#ENV MYSQL_USER=root \
#    MYSQL_DATABASE=fiapdb \
#    MYSQL_ROOT_PASSWORD=senhaFiap

ADD ./aso.sql /docker-entrypoint-initdb.d
