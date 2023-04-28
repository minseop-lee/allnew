const express = require("express");
const Score = require("../models/score");
const router = express.Router();

// 성취도 확인 페이지
router.get("/", async (req, res) => {
  const scores = await Score.findAll({ where: { user_id: req.query.user_id } });
  res.render("score", { scores });
});

module.exports = router;
