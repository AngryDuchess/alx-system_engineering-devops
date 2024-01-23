# Increases the amount of traffic a  server can handle

exec {'fixing server traffic limit':
    provider => 'shell',
    command  => "sed -i 's/15/4096/' /etc/default/nginx"
}

exec {'restart nginx':
    provider => 'shell',
    command  => 'sudo service nginx restart'
}
