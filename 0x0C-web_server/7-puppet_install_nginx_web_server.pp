# nginx configuration using puppet

package { 'nginx':
    ensure => installed
}

file {'/var/www/index.nginx-debian.html':
    content => 'Hello World!'
}

file_line { 'redirection':
    path  => '/etc/nginx/sites-available/default',
    after => 'server_name_;',
    line  => "\n\tlocation /redirect_me {\n\t\treturn 301 https://www.hamidas-portfolio.webflow.io;\n\t}\n"
}

service { 'restart server':
    ensure    => running,
    subscribe => File_line['redirection'],
}
