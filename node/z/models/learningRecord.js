const Sequelize = require("sequelize");
const sequelize = new Sequelize("testdb", "root", "1234", {
  host: "192.168.0.46",
  dialect: "mysql",
});

const LearningRecord = sequelize.define("LearningRecord", {
  id: {
    type: Sequelize.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  user_id: {
    type: Sequelize.INTEGER,
    allowNull: false,
  },
  subject: {
    type: Sequelize.STRING,
    allowNull: false,
  },
  content: {
    type: Sequelize.TEXT,
    allowNull: false,
  },
  date: {
    type: Sequelize.DATE,
    allowNull: false,
  },
});

module.exports = LearningRecord;
