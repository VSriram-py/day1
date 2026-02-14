require("dotenv").config();
const express = require("express");
const app = express();

const PORT = process.env.PORT || 3000;
const APP_NAME = process.env.APP_NAME || "Demo";
const LOG_LEVEL = process.env.LOG_LEVEL;

app.get("/", (req, res) => {
  res.send(`${APP_NAME} running with log level ${LOG_LEVEL}`);
});

app.listen(PORT, () => console.log(APP_NAME + " started"));
