#error 500

exec { 'FIX500':
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/',
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
}