let mic, fft;

function setup() {
  createCanvas(710, 400);
  noFill();
  frameRate(30);
  mic = new p5.AudioIn();
  mic.start();
  fft = new p5.FFT();
  fft.setInput(mic);
}

function draw() {
  background(204, 229, 255);
  let spectrum = fft.analyze();
  beginShape();
  for (i = 0; i < spectrum.length; i++) {
    vertex(i, map(spectrum[i], 0, 255, height, 0));
  }
  endShape();
}

