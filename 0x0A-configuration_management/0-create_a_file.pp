file { '/tmp/school':  # The resource name is file
  ensure => file,  # the ensure parameter is set to file
  mode => '0744',  # mode is set to specified value
  owner => 'www-data',  # owner is set to specified value
  group => 'www-data',  # group is set to specified value
  content => 'I love Puppet',  # content is set to string 'i love you'
}
