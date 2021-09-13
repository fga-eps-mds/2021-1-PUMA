const express = require('express');
const cors = require('cors');

var app = express()
app.use(cors())

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use('/', (req,res) =>{
    res.json({
        Project: "Puma",
        Service: "API Gateway"
    })
})

app.listen(3004)
