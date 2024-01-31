




const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
var port = 4000; 

mongoose.connect('mongodb://127.0.0.1:27017/Userdatastore').then(() => {
  console.log("Connected to MongoDB");
}).catch((error) => {
  console.error("Error connecting to MongoDB:", error);
});

const userSchema = new mongoose.Schema({
  Username: String,
  lastName: String,
  dob: Date,
  email: String,
  mobile: String,
  password: Array,
});

const User = mongoose.model('User', userSchema);

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname,  'dregister.html'));
});
app.post('/submit', async (req, res) => {
  const { Fname, Lname, dob, emailInput, num, pass } = req.body;

  const newUser = new User({
    Username: Fname,
lastname:Lname,
email:emailInput,
mobile:num,
    password: pass,
  });

  try {
    const savedUser = await newUser.save();
    res.send(`Registration successful! User ID: ${savedUser._id}`);
  } catch (error) {
    console.error(error);
    res.status(500).send('Internal Server Error');
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
