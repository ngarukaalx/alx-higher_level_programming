#!/usr/bin/node
// computes the number of tasks completed by user id.

// import request
const request = require('request');

// read command line arguments
const args = process.argv.slice(2);

// take the url argument
const url = args[0];
// make a Get request
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  // convert to javascript object
  const data = JSON.parse(body);

  // create map to store counts for each user Id
  const completedTasksByUser = new Map();

  // iterate through data
  data.forEach(task => {
    const userId = task.userId;

    // if the user id not in map initialize its value with zero
    if (!completedTasksByUser.has(userId)) {
      completedTasksByUser.set(userId, 0);
    }

    // increament value if task is completed
    if (task.completed) {
      completedTasksByUser.set(userId, completedTasksByUser.get(userId) + 1);
    }
  });

  const finalData = {};
  // log results
  completedTasksByUser.forEach((count, userId) => {
    if (count !== 0) {
      finalData[userId] = count;
    }
  });
  console.log(finalData);
});
