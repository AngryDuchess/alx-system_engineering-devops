# Set nginx max open files limit

exec {'set hard limit':
    provider => 'shell',
    command  => "sed -i 's/nofile 5/nofile 50000/' /etc/security/limits.conf"
}

exec {'set soft limit':
    provider => 'shell',
    command  => "sed -i 's/nofile 4/nofile 40000/' /etc/security/limits.conf"
}
