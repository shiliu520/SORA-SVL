FROM node

WORKDIR /app

ADD package.json /app
ADD package-lock.json /app

# RUN npm install
RUN npm install --registry=https://registry.npmmirror.com

COPY ./ /app

RUN npm run build --production

RUN npm install -g serve
CMD serve -s build

EXPOSE 3000
