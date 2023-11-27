# using puppet to make changes to ssh config file

include stdlib

file_line { 'remove password authentication':
  ensure => 'present',
  path   => 'etc/ssh/ssh_config',
  line   => ['  PasswordAuthentication no']
}

file_line { 'new identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => ['  IdentityFile ~/.ssh/school']
}
