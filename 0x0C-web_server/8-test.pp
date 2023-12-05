# nginx configuration using puppet

exec { 'apt-get update':
    command => 'apt-get update'
    path    => ['/usr/bin', '/usr/sbin']
}

package { 'nginx':
    ensure => installed
}

file { '/var/www//html/index.nginx-debian.html':
    ensure  => file,
    content => 'Hello World!',
    mode    => '0664',
    require => Package['nginx']
}

$line = '\n\tlocation /redirect_me {\n\t\treturn 301 https://www.hamidas-portfolio.webflow.io;\n\t}\n'

exec { 'redirection':
    command => "sudo sed -i 'server_name _;/a \\'${line}' /etc/nginx/sites-available/default",
    path    => '/usr/bin:bin/'
}'

service { 'restart server':
    ensure  => running,
    enable  => true,
    require => Package['nginx'] 
}
