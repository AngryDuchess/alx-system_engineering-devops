# This script creates a file in /tmp with File permission,owner, group and content specified
file { '/tmp/school':
  ensure => file,
  mode => '0744',
  owner => 'www-data',
  group => 'www-data',
  content => 'I love Puppet',
}
