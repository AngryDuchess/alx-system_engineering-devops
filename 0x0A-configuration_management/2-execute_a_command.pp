exec { 'killmenow'
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/pgrep -f killmenow',
  path    => '/usr/bin',
  logoutput => true,
 }
