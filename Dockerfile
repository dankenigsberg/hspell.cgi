FROM fedora/apache
MAINTAINER Dan Kenigsberg <danken@gmail.com>
RUN dnf install -y hspell perl perl-CGI && dnf clean all
RUN sed -i "s/^Listen 80$/Listen \${PORT}/;s/^User apache/User daemon/;s/^Group apache/Group daemon/" /etc/httpd/conf/httpd.conf
RUN echo RedirectMatch ^/$ /cgi-bin/hspell.cgi >> /etc/httpd/conf/httpd.conf
COPY hspell.cgi hspell.color.cgi color.pl /var/www/cgi-bin/
COPY hebrew.conf /etc/httpd/conf.d
COPY favicon.ico /var/www/html/
RUN chown -R daemon:daemon /var/log/httpd
RUN chown -R daemon:daemon /run/httpd
RUN chmod -R o+rwx /var/log/httpd
RUN chmod -R o+rwx /run/httpd
USER daemon
