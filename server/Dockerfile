FROM node:18
RUN mkdir /workdir
ADD package.json /workdir

WORKDIR /workdir

# RUN npm install
RUN npm install --registry=https://registry.npmmirror.com
ADD ./ /workdir

EXPOSE 3000
RUN ["npm", "run", "build"]
CMD [ "npm", "run", "start" ]