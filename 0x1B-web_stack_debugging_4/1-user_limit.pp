# Enable user holberton to login and open files without erros"

# Increase hard file limitfor holberton user

exec { 'increase-hard-limit':
  command => 'sed -i "/^holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

# Increase soft file limitfor holberton user

exec { 'increase-soft-limit':
  command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
