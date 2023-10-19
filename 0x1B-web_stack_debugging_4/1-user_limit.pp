# This script increases the limit of open files for user holberton

exec { 'fix_hard_limit':
  command => '/bin/sed -i "s/holberton hard nofile 5/holberton hard nofile 50/" /etc/security/limits.conf',
}

exec { 'fix_soft_limit':
  command => '/bin/sed -i "s/holberton soft nofile 4/holberton soft nofile 50/" /etc/security/limits.conf'
}
