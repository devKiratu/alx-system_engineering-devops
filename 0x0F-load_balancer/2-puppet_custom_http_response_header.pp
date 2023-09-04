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
    command => "/usr/bin/sed -i \"/http {/a\\${redirect_block}\" /etc/nginx/nginx.conf",
    require => Package['nginx']
  }

  # run nginx
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx']
  }
