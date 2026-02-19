import express from 'express';
import {twiml as Twiml} from 'twilio';

const app = express();

app.use(express.urlencoded({extended: false})); //twilio sends data as urlencoded form data

app.post("/voice/answer", (req, res) => {
    const vr = new Twiml.VoiceResponse();
    vr.say("Hello. I would like to refill my prescription.");
    vr.record({
        maxLength: 15,
        playBeep: true,
        action: "/voice/recorded",
        method: "POST"
    })
    //send xml back to twilio
    res.type("text/xml");
    res.send(vr.toString());
});

app.post("/voice/recorded", (req, res) => {
    const callSid = req.body.CallSid;
    const recordingUrl = req.body.RecordingUrl;
    const recordingURL = req.body.RecordingURL;

    console.log("Call SID:", callSid);
    console.log("Recording URL:", recordingUrl);

    const vr = new Twiml.VoiceResponse();
    vr.say("Thank you. Your prescription refill request has been received.");
    vr.hangup();
    res.type("text/xml");
    res.send(vr.toString());
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port http://localhost:${PORT}`);
});
