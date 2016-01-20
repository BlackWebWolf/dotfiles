from fabric.api import *
#playlists
def play_samon():
    local("mpsyt play eluveitie_samon")

#website tools
def nix_restart():
    local("sudo service nginx restart")

def domain_create():
    pass

def odin_eye(log="nginx/error.log"):
    command = "cat /var/log/%s" % log
    local(command)
def odin_watch(log="nginx/error.log"):
    command = "tail -f /var/log/%s" % log
    local(command)

