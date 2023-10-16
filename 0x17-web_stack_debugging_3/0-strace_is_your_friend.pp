# This script attempts to fix an Apache server that is returning a 500 error.

exec {'fix wordpress config':
  command => "/bin/sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
}

