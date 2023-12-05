# nginx configuration using puppet

exec { 'update':
  command => 'apt-get update',
  path    => ['/usr/bin', '/usr/sbin'],
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  mode    => '0664',
  require => Package['nginx'],
}

$line = '\n\tlocation /redirect_me {\n\
        \treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\
        }'
exec { 'redirection':
  command => "sudo sed -i '/server_name _;/a \\ ${line}' /etc/nginx/sites-available/default",
  path    => '/usr/bin:/bin',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
