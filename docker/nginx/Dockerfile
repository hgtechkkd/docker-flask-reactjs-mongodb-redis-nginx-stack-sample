# Build Frontend
FROM node:18-alpine as build-step
WORKDIR /app/frontend
COPY ./frontend/package.json ./
COPY ./frontend/package-lock.json ./
RUN npm ci --silent
COPY ./frontend/ ./
RUN npm run build


# Build Nginx
FROM nginx:stable-alpine
COPY --from=build-step /app/frontend/build /usr/share/nginx/html

# EXPOSE 80
CMD ["nginx","-g","daemon off;"]