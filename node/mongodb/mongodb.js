const express = require("express");
const morgan = require("morgan");
const fs = require("fs");
const path = require("path");
const mongoClient = require("mongodb").MongoClient;
const app = express();

app.set("port", process.env.Port || 8000);
app.unsubscribe(morgan("dev"));

var db;
var databaseUrl = "mongodb://192.168.1.198:27017";

app.get("/", (req, res) => {
  res.send("Web server Started~!!");
});

app.get("/users", (req, res) => {
  mongoClient.connect(databaseUrl, function (err, database) {
    if (err != null) {
      res.json({ count: 0 });
    } else {
      db = database.db("test");
      db.collection("users")
        .find({})
        .toArray(function (err, result) {
          if (err) throw err;
          console.log("result : ");
          console.log(result);
          res.json(JSON.stringify(result));
        });
    }
  });
});

app.listen(app.get("port"), () => {
  console.log("8000 Port : Server Started~!!");
});
