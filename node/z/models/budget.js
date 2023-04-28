const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const BudgetSchema = new Schema({
  user_id: {
    type: Number,
    required: true,
  },
  expected_salary: {
    type: Number,
    required: true,
  },
  weekly_budget: {
    type: Number,
    required: true,
  },
});

const Budget = mongoose.model("Budget", BudgetSchema);

module.exports = Budget;
