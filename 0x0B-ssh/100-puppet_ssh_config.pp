# This script sets up a client SSH configuration file so that you can connect to a server without typing a password.

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "Host *\nPasswordAuthentication no\nIdentityFile ~/.ssh/school\n"
}
