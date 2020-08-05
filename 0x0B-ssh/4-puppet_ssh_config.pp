#pass turn off pass
      file_Line { 'Turn off passwd auth':
      ensure => 'present',
      path   => '/etc/ssh/ssh_config',
      line   => '    PasswordAutentication no'
      }
      file_line { 'Declare identy file':
      ensure => 'present',
      path   => '/etc/ssh/ssh_config',
      line   => '    IdentityFile ~/.ssh/holberton'
      }