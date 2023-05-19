FROM node:20-bullseye-slim

EXPOSE 3000

ENV NODE_ENV=production

WORKDIR /openlyrics_search

COPY openlyrics_search/package*.json .
RUN npm install

COPY openlyrics_search/. .

CMD ["npm", "start"]