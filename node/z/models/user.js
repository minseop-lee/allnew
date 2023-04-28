const Sequelize = require("sequelize");
const sequelize = new Sequelize("testdb", "mysql", "1234", {
  host: "192.168.1.198",
  dialect: "mysql",
});

const User = sequelize.define("User", {
  id: {
    type: Sequelize.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  name: {
    type: Sequelize.STRING,
    allowNull: false,
  },
  email: {
    type: Sequelize.STRING,
    allowNull: false,
  },
  password: {
    type: Sequelize.STRING,
    allowNull: false,
  },
});

module.exports = User;
