const express = require("express");
const LearningRecord = require("../models/learningRecord");
const router = express.Router();

// 학습일지 작성 페이지
router.get("/", (req, res) => {
  res.render("learning_record");
});

// 학습일지 작성 처리
router.post("/", async (req, res) => {
  await LearningRecord.create({
    user_id: req.body.user_id,
    subject: req.body.subject,
    content: req.body.content,
    date: new Date(),
  });
  res.redirect("/score");
});

module.exports = router;
