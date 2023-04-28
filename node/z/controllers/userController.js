const express = require("express");
const User = require("../models/user");
const router = express.Router();

// 메인 페이지
router.get("/", (req, res) => {
  res.render("index");
});

// 로그인 페이지
router.get("/login", (req, res) => {
  res.render("login");
});

// 로그인 처리
router.post("/login", async (req, res) => {
  const user = await User.findOne({ where: { email: req.body.email } });
  if (user && user.password === req.body.password) {
    res.redirect("/learning_record");
  } else {
    res.send("로그인 실패");
  }
});

// 회원가입 페이지
router.get("/signup", (req, res) => {
  res.render("signup");
});

// 회원가입 처리
router.post("/signup", async (req, res) => {
  await User.create({
    name: req.body.name,
    email: req.body.email,
    password: req.body.password,
  });
  res.redirect("/login");
});

module.exports = router;
