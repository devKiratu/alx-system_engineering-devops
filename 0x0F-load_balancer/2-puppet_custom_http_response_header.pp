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

  # add custom headers
  $redirect_block ="\\\n\\n\tadd_header X-Served-By ${hostname};\\n"

  exec { 'add_header':
    command => "/usr/bin/sed -i \"/server_name _;/a\\${redirect_block}\" /etc/nginx/sites-enabled/default",
    require => Package['nginx']
  }

  # run nginx
  exec { 'run_nginx':
    command => '/usr/sbin/service nginx restart',
    require => Package['nginx']
  }
