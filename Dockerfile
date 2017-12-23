FROM fedora/apache
MAINTAINER Dan Kenigsberg <danken@gmail.com>
RUN dnf install -y hspell perl perl-CGI && dnf clean all
COPY hspell.cgi /var/www/cgi-bin
COPY hebrew.conf /etc/httpd/conf.d
