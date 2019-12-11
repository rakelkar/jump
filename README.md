# jump
jump pod with ssh to alllow me to jump around from a k8s cluster

```
# build and run
docker build . -t kcorer/jump
docker run -p 8888:8888 -it kcorer/jump

# curl it!
curl http://localhost:8888/
curl http://localhost:8888/echo/hey

# return status code
curl -v http://localhost:8888/echo?status=404
curl -v http://localhost:8888/echo?status=503


# deploy it 
kubectl apply -f jump.yaml
```
