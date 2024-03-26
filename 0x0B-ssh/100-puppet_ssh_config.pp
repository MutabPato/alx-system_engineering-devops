file { '/etc/ssh/ssh_config':
ensure  => present,
content => "

Host*
	IdentifyFile ~/.ssh/school
	PaaswordAuthentication no
",
}
