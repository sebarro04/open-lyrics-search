FROM node:20-alpine3.16

EXPOSE 3000

ENV NODE_ENV=production

WORKDIR /openlyrics_search

COPY ["package.json", "package-lock.json*", "./"]

RUN npm install --production

COPY . .

CMD ["npm", "start"]