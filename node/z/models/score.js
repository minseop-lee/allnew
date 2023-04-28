const Sequelize = require("sequelize");
const sequelize = new Sequelize("testdb", "root", "1234", {
  host: "192.168.0.46",
  dialect: "mysql",
});

const Score = sequelize.define("Score", {
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
  points: {
    type: Sequelize.INTEGER,
    allowNull: false,
  },
});

module.exports = Score;
