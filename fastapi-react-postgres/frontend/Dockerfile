# Stage 1: Build the React application
FROM node:22-alpine AS build

WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies (ci for more reproducible builds if package-lock is present)
RUN npm ci || npm install

# Copy the rest of the application code
COPY . .

# Build the app for production
RUN npm run build

# Stage 2: Serve the application with Nginx
FROM nginx:alpine

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the built React app from the previous stage
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]