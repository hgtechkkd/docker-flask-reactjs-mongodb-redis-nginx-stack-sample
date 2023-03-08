# flask + reactjs + mongodb + redis + nginx

This is a sample flask-react-mongo application stack with docker files and docker compose.

This can be run with load balancing by using --scale option while running with docker.
<code> docker-compose up -d --build --scale backend=3 </code>

## more details

1. Install Docker (for windows optionally install Docker Desktop)

2. <code>gh repo clone hgtechkkd/docker-flask-reactjs-mongodb-redis-nginx-stack-sample</code>

3. run the following command:
   <code> docker-compose up -d --build --scale backend=3 </code>
   (Here 3 is number of relicas for backend server. You can change it accordingly.)

4. Open Github Desktop and check stack status.
   or run the following command:
   <code>docker ps</code>
