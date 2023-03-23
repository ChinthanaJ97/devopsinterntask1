Designed architecture is shown in image1
![image1](https://user-images.githubusercontent.com/125088387/227204595-d8f5542a-7282-4ace-8457-c965e6a82a39.png)

1.	Created an amazon ec2  ubuntu instance with a keypair
2.	Configured security group with allowing http, ssh, https and tcp(image2)
![40beeb05-45a8-43d2-bb0b-2310861e19a6](https://user-images.githubusercontent.com/125088387/227209096-1e65565b-1224-4c32-bd70-65f500a9ef9d.jpg)


4.	Connected to ec2 using private ip via Xshell
5.	Created a python file inside ec2 that display "hello world"
6.	Created a dockerfile to execute the python file
7.	Dockerfile builds docker image 
8.	Then docker image was pushed into my docker hub repo
9.	Then logged into my docker hub using username password through my ec2
10.	Then the docker container was run importing image from my docker repo
11.	Now it runs on ec2 localhost:8080 (myip.8080)
12.	Next Installation of apache server was done (Sudo apt-get intall apache2)
13.	Reached to /ect/appche2/sites-available
14.	Created a docker.conf file and configured reverse proxy and configured domain name into ec2 localhost:8080 , domain name was purchased from godaddy.com

        <Virtualhost *:80>
            ServerName        http://app.chinthanaa.com/
            ProxyRequests     Off
            ProxyPreserveHost On
            AllowEncodedSlashes NoDecode

            <Proxy http://localhost:8080/*>
              Order deny,allow
              Allow from all
            </Proxy>

            ProxyPass         /  http://localhost:8080/ nocanon
            ProxyPassReverse  /  http://localhost:8080/
            ProxyPassReverse  /  http://app.chinthanaa.com/

        </Virtualhost>


14.	Then created a public hosted zone in route 53 giving the godady domain name and then updated the four  NS record from the route 53 in the godaddy domain registry.(image3)
![44e3b51d-0f9e-417d-9bed-dbc215d946c3](https://user-images.githubusercontent.com/125088387/227209389-bbbdaee6-f0e3-452e-a1f3-14944b089294.jpg)


16.	Then added two name records in route 53 giving the subdomain as app and www(image4)
![1622c0bc-b355-4637-a944-beba85e6e79e](https://user-images.githubusercontent.com/125088387/227209596-7008591d-e272-4dd7-a8b9-3bc78db86936.jpg)


18.	Then after few hours my domain name is directly going to docker running port of my ec2 instance.
19.	Then obtained free ssl certification by ZeroSSL and did the configuration  part
20.     Downloaded zip file included 3 files (certificate.crt, ca_bundle.crt, private.key) 
21.     certificate.crt and ca_bundle.crt was added to /etc/ssl/    and private.key was added to private folder at /etc/ssl/private/ 

![image](https://user-images.githubusercontent.com/125088387/227219925-744ccad0-2d7b-4984-b091-d09e3479683c.png)

22.     Default certificates were then commented
![image](https://user-images.githubusercontent.com/125088387/227221140-385ac092-4fdc-4f54-b64a-317712c1d07e.png)



        <IfModule mod_ssl.c>
                <VirtualHost app.chinthanaa.com:443>
                        ServerAdmin chinthanapriy4@gmail.com
                        ServerName  app.chinthanaa.com
                        DocumentRoot /var/www/html

                        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
                        # error, crit, alert, emerg.
                        # It is also possible to configure the loglevel for particular
                        # modules, e.g.
                        #LogLevel info ssl:warn

                        ErrorLog ${APACHE_LOG_DIR}/error.log
                        CustomLog ${APACHE_LOG_DIR}/access.log combined

                        # For most configuration files from conf-available/, which are
                        # enabled or disabled at a global level, it is possible to
                        # include a line for only one particular virtual host. For example the
                        # following line enables the CGI configuration for this host only
                        # after it has been globally disabled with "a2disconf".
                        #Include conf-available/serve-cgi-bin.conf

                        #   SSL Engine Switch:
                        #   Enable/Disable SSL for this virtual host.
                        SSLEngine on

                        #   A self-signed (snakeoil) certificate can be created by installing
                        #   the ssl-cert package. See
                        #   /usr/share/doc/apache2/README.Debian.gz for more info.
                        #   If both key and certificate are stored in the same file, only the
                        #   SSLCertificateFile directive is needed.
                        SSLCertificateFile       /etc/ssl/certificate.crt
                        SSLCertificateKeyFile    /etc/ssl/private/private.key
                        SSLCertificateChainFile  /etc/ssl/ca_bundle.crt
                        #SSLCertificateFile      /etc/ssl/certs/ssl-cert-snakeoil.pem
                        #SSLCertificateKeyFile /etc/ssl/private/ssl-cert-snakeoil.key
                        SSLProxyEngine on
                        SSLProxyVerify none


                        #   Server Certificate Chain:
                        #   Point SSLCertificateChainFile at a file containing the
                        #   concatenation of PEM encoded CA certificates which form the
                        #   certificate chain for the server certificate. Alternatively
                        #   the referenced file can be the same as SSLCertificateFile
                        #   when the CA certificates are directly appended to the server
                        #   certificate for convinience.
                        #SSLCertificateChainFile /etc/apache2/ssl.crt/server-ca.crt

                        #   Certificate Authority (CA):
                        #   Set the CA certificate verification path where to find CA
                        #   certificates for client authentication or alternatively one
                        #   huge file containing all of them (file must be PEM encoded)
                        #   Note: Inside SSLCACertificatePath you need hash symlinks
                        #                to point to the certificate files. Use the provided
                        #                Makefile to update the hash symlinks after changes.
                        #SSLCACertificatePath /etc/ssl/certs/
                        #SSLCACertificateFile /etc/apache2/ssl.crt/ca-bundle.crt

                        #   Certificate Revocation Lists (CRL):
                        #   Set the CA revocation path where to find CA CRLs for client
                        #   authentication or alternatively one huge file containing all
                        #   of them (file must be PEM encoded)
                        #   Note: Inside SSLCARevocationPath you need hash symlinks
                        #                to point to the certificate files. Use the provided
                        #                Makefile to update the hash symlinks after changes.
                        #SSLCARevocationPath /etc/apache2/ssl.crl/
                        #SSLCARevocationFile /etc/apache2/ssl.crl/ca-bundle.crl

                        #   Client Authentication (Type):
                        #   Client certificate verification type and depth.  Types are
                        #   none, optional, require and optional_no_ca.  Depth is a
                        #   number which specifies how deeply to verify the certificate
                        #   issuer chain before deciding the certificate is not valid.
                        #SSLVerifyClient require
                        #SSLVerifyDepth  10

                        #   SSL Engine Options:
                        #   Set various options for the SSL engine.
                        #   o FakeBasicAuth:
                        #        Translate the client X.509 into a Basic Authorisation.  This means that
                        #        the standard Auth/DBMAuth methods can be used for access control.  The
                        #        user name is the `one line' version of the client's X.509 certificate.
                        #        Note that no password is obtained from the user. Every entry in the user
                        #        file needs this password: `xxj31ZMTZzkVA'.
                        #   o ExportCertData:
                        #        This exports two additional environment variables: SSL_CLIENT_CERT and
                        #        SSL_SERVER_CERT. These contain the PEM-encoded certificates of the
                        #        server (always existing) and the client (only existing when client
                        #        authentication is used). This can be used to import the certificates
                        #        into CGI scripts.
                        #   o StdEnvVars:
                        #        This exports the standard SSL/TLS related `SSL_*' environment variables.
                        #        Per default this exportation is switched off for performance reasons,
                        #        because the extraction step is an expensive operation and is usually
                        #        useless for serving static content. So one usually enables the
                        #        exportation for CGI and SSI requests only.
                        #   o OptRenegotiate:
                        #        This enables optimized SSL connection renegotiation handling when SSL
                        #        directives are used in per-directory context.
                        #SSLOptions +FakeBasicAuth +ExportCertData +StrictRequire
                        <FilesMatch "\.(cgi|shtml|phtml|php)$">
                                        SSLOptions +StdEnvVars
                        </FilesMatch>
                        <Directory /usr/lib/cgi-bin>
                                        SSLOptions +StdEnvVars
                        </Directory>
                        ProxyRequests Off
                        ProxyPreserveHost On
                        AllowEncodedSlashes NoDecode

                        <Proxy https://localhost:8080/*>
                           Order deny,allow
                         Allow from all
                        </Proxy>

                        ProxyPass         /  https://localhost:8080/ nocanon
                        ProxyPassReverse  /  https://localhost:8080/
                        ProxyPassReverse  /  https://app:chinthanaa.com/

                        RequestHeader set X-Forwarded-Proto "https"
                        RequestHeader set X-Forwarded-Port "443"
                        RequestHeader set X-Forwarded-Ssl on
                        #   SSL Protocol Adjustments:
                        #   The safe and default but still SSL/TLS standard compliant shutdown
                        #   approach is that mod_ssl sends the close notify alert but doesn't wait for
                        #   the close notify alert from client. When you need a different shutdown
                        #   approach you can use one of the following variables:
                        #   o ssl-unclean-shutdown:
                        #        This forces an unclean shutdown when the connection is closed, i.e. no
                        #        SSL close notify alert is send or allowed to received.  This violates
                        #        the SSL/TLS standard but is needed for some brain-dead browsers. Use
                        #        this when you receive I/O errors because of the standard approach where
                        #        mod_ssl sends the close notify alert.
                        #   o ssl-accurate-shutdown:
                        #        This forces an accurate shutdown when the connection is closed, i.e. a
                        #        SSL close notify alert is send and mod_ssl waits for the close notify
                        #        alert of the client. This is 100% SSL/TLS standard compliant, but in
                        #        practice often causes hanging connections with brain-dead browsers. Use
                        #        this only for browsers where you know that their SSL implementation
                        #        works correctly.
                        #   Notice: Most problems of broken clients are also related to the HTTP
                        #   keep-alive facility, so you usually additionally want to disable
                        #   keep-alive for those clients, too. Use variable "nokeepalive" for this.
                        #   Similarly, one has to force some clients to use HTTP/1.0 to workaround
                        #   their broken HTTP/1.1 implementation. Use variables "downgrade-1.0" and
                        #   "force-response-1.0" for this.
                        # BrowserMatch "MSIE [2-6]" \
                        #               nokeepalive ssl-unclean-shutdown \
                        #               downgrade-1.0 force-response-1.0

                </VirtualHost>
        </IfModule>
