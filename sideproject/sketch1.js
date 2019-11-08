var mic, fft;
function setup() {
     createCanvas(710,400);
     
   noFill();
   text = createDiv('This is where I will put some werwerwer hopefully');
   text.position(50, 80);
   //pauseF = document.getElementById("pause");
   mic = new p5.AudioIn();
   mic.start();
   fft = new p5.FFT();
   fft.setInput(mic);
}

function draw() {
     background(204, 229, 255);

   var spectrum = fft.analyze();
   //if pauseF == 1
       beginShape();
       for (i = 0; i<spectrum.length; i++) {
        vertex(i, map(spectrum[i], 0, 255, height, 0) );
       }
       endShape();
}

