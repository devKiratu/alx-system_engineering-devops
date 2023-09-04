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
  file { '/var/www/html/index.html':
    content => "Hello World!\n",
    require => Package['nginx']
  }

  # set custom 404 page
  file { '/var/www/html/404.html':
    content => "Ceci n'est pas une page\n\n",
    require => Package['nginx']
  }

  # set redirection for route /redirect_me
  $redirect_block ="\\\n\\n\tadd_header X-Served-By ${hostname};\\n\\n\terror_page 404 \t/404.html;\\n\\n\tlocation /redirect_me {\\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\\n\t}\\n\\n"

  exec { 'configure_redirect_me':
    command => "/usr/bin/sed -i \"/server_name _;/a\\${redirect_block}\" /etc/nginx/sites-enabled/default",
    require => Package['nginx']
  }

  # run nginx
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx']
  }
