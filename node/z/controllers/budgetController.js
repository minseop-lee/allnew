const express = require("express");
const Budget = require("../models/budget");
const router = express.Router();

// 예산 관리 페이지
router.get("/", async (req, res) => {
  const budget = await Budget.findOne({ user_id: req.query.user_id });
  res.render("budget", { budget });
});

// 예산 정보 업데이트 처리
router.post("/", async (req, res) => {
  await Budget.findOneAndUpdate(
    { user_id: req.body.user_id },
    {
      expected_salary: req.body.expected_salary,
      weekly_budget: req.body.weekly_budget,
    },
    { upsert: true }
  );
  res.redirect("/budget");
});

module.exports = router;
