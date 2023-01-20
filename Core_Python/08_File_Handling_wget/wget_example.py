
import wget

path_source = 'ftp://ip_address'
path_destination = 'D:/'

print("Downloading file...")
wget.download(path_source, path_destination)
print("Downloading... Ok..")

