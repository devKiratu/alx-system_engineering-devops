# This manifest perfoms what bash script '3-redirection' does

  # update package repository
  exec { 'update_packages':
    command => '/usr/bin/apt update'
  }

  # Install nginx
  package { 'nginx':
    ensure  => installed,
    require => Exec['update_packages']
  }

  # set homepage to return 'Hello World!'
  file { '/var/www/html/index.nginx-debian.html':
    content => "Hello World!\n",
    require => Package['nginx']
  }

  # run nginx
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx']
  }
