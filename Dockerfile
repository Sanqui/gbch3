FROM node:lts-alpine

# make the 'app' folder the current working directory
WORKDIR /app

COPY package.json yarn.lock ./

# install project dependencies
RUN yarn install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN yarn build

EXPOSE 3000
CMD [ "yarn", "start" ]