# nginx configuration using puppet

exec { 'apt-get update':
    command => '/usr/bin/apt-get-update
}

package { 'nginx':
    ensure => installed
}

file {'/var/www//html/index.nginx-debian.html':
    content => 'Hello World!'
    require => Package['nginx']
}

file_line { 'redirection':
    path  => '/etc/nginx/sites-available/default',
    after => 'server_name_;',
    line  => "\n\tlocation /redirect_me {\n\t\treturn 301 https://www.hamidas-portfolio.webflow.io;\n\t}\n"
}

service { 'restart server':
    ensure  => running,
    enable  => true,
    require => Package['nginx'] 
}
