# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|

  # Box settings
  config.vm.box = "ubuntu/focal64"

  # Provider settings
  config.vm.provider "virtualbox" do |vb|
    # vb.gui = true
    # Customize the amount of memory on the VM:
    vb.memory = "1024"
  end


  # Network settings
  config.vm.network "forwarded_port", guest: 80, host: 8080, auto_correct: true
  config.vm.network "forwarded_port", guest: 5000, host: 5050, host_ip: "127.0.0.1", auto_correct: true
  config.vm.network "forwarded_port", guest: 5001, host: 5001, host_ip: "127.0.0.1", auto_correct: true


  # config.vm.network "private_network", ip: "192.168.33.10"
  # config.vm.network "public_network"

  #Folder settings
  config.vm.synced_folder ".", "/root/"

  #Provision settings
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
end
