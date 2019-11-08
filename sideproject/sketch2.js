var mic, fft, waveform;
function setup() {
     createCanvas(710,400);
 
   noFill();
   frameRate(30);
   mic = new p5.AudioIn();
   mic.start();
   fft = new p5.FFT();
   fft.setInput(mic);
      text = createDiv('This is where I will put more options');
   text.position(50, 80);
   //pauseF = document.getElementById("pause");
}

function draw() {
     background(204, 229, 255);

   var waveform = fft.waveform();
  // if pauseF == 1
       beginShape();
       for (i = 0; i<waveform.length; i++) {
           var x = map(i, 0, waveform.length, 0, width);
           var y = map(waveform[i], -1, 1, 0, height);
           vertex(x, y);
       }
       endShape();
}