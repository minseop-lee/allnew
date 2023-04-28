const express = require("express");
const mongoose = require("mongoose");
const mysql = require("mysql");
const bodyParser = require("body-parser");
const userController = require("./controllers/userController");
const learningRecordController = require("./controllers/learningRecordController");
const scoreController = require("./controllers/scoreController");
const budgetController = require("./controllers/budgetController");

const app = express();

// 데이터베이스 연결 설정 (MySQL)
const connection = mysql.createConnection({
  host: "192.168.1.198",
  user: "mysql",
  password: "1234",
  database: "testdb",
});

connection.connect();

// 데이터베이스 연결 설정 (MongoDB)
mongoose.connect("mongodb://192.168.1.198:27017/test", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

app.set("view engine", "html");
app.engine("html", require("ejs").renderFile);
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: false }));

// 라우터 설정
app.use("/", userController);
app.use("/learning_record", learningRecordController);
app.use("/score", scoreController);
app.use("/budget", budgetController);

app.listen(8000, () => {
  console.log("서버 실행 중...");
});
