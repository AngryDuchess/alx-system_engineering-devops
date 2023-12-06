# A puppet file to configure a new ubuntu machine with a custom http header response

$CONFIG_FILE="/etc/nginx/sites-available/default"
$HEADER="\n\tadd_header X-Served-By \$hostname;"

exec { 'update and install nginx':
    command  => 'sudo apt-get update -y && sudo apt-get install nginx -y',
    provider => shell,
}

exec { 'insert header':
    command  => 'sudo sed -i "/server_name _;/a\ $HEADER" "$CONFIG_FILE"' && sudo service nginx restart',
    provider => shell
    require  => Exec['update and install nginx']
}
