const express = require("express");
const bwipjs = require("bwip-js");

const app = express();

app.get("/", async (req, res) => {
    const text = req.query.text || "Hello";

    try {
        const png = await bwipjs.toBuffer({
            bcid: "datamatrix",
            text: text,
            scale: 5,
            includetext: false
        });

        res.writeHead(200, {
            "Content-Type": "image/png"
        });

        res.end(png);
    } catch (err) {
        res.status(500).send(err.toString());
    }
});

app.listen(3000, () => {
    console.log("DataMatrix server running on port 3000");
});
