# file in /tmp

file {'/tmp/holberton':
     ensure => 'file',
     content => 'I love Puppet',
     path => '/tmp/holberton',
     owner => 'www-data',
     group => 'www-data',
     mode => '0744'
     }