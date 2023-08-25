# This manifest kills a process named killmenow using pkill

exec { 'pkill -f killmenow':
  command => '/usr/bin/pkill -f killmenow'
}
