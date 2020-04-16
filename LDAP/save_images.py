import os

# Enter your private Docker registry 
private_registry = "enter_url_here"

original_image = [
    "osixia/openldap:1.2.4",
    "osixia/phpldapadmin:0.8.0"
]

# Uncomment when pulling and tagging of images(while connected to Internet)
# for i in range(len(original_image)):
#     os.system("docker pull %s"%original_image[i])
#     os.system("docker tag %s %s"%(original_image[i],private_registry+"/"+original_image[i]))

# Uncomment when pushing to private Docker registry
# for i in range(len(original_image)):
#     os.system("docker push %s"%private_registry+"/"+original_image[i])