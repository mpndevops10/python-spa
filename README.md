# python-spa for Etech Engineers Only
## Steps to build your single page python Application
```
Run:
  docker build -t $imagename:$version .
```

## Make sure you have all the above files in the same directory(build context)
Run:
```
docker run --name $containername -dp host_port:container_port $imagename:$version
```
##Open the `host_port` above on the security group of your dockerhost
Access your app:
```
public_ip_dockerhost:$host_port
```
