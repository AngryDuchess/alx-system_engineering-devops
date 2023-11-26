# Creates a file school in a specified path and adds permisions
file { 'school':
  path    => '/tmp/school',
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744'
}
