# Playing with Sound

Following a lecture today, it was suggested that us students sing in the shower and notice how the apparent intensity of the sound changes depending on the pitch. Of course, the goal of this was to find the resonant frequency of our shower. I thought this would be fun to quantify and it also gave me an idea for investigation:

> Can we estimate the dimensions of a shower based off the resonant frequencies?

Naively, I went about exploring this.

## Generating the Sweep

The first step was to create an audio file where all the frequencies are swept through in at a constant speed at a constant intensity. I did this in matlabb. My version of matlab (2015a) has a built-in function called [`chirp`](https://www.mathworks.com/help/signal/ref/chirp.html) that generates a swept-frequency cosine signal.

I decided to go through the frequenecy range [0, 1000] Hz, use the standard sampling rate of 44.1 kHz, and have the sweep take 15 seconds. The full command was:

```matlab
tot=15;   % sweep time (s)
fs=44100; % sampling frequency (hz)
t = 0:1/fs:tot;
y = chirp(t,0,tot,1000);
```
The output generated: 

<audio controls>
  <source src="/assets/freqSweep.wav" type="audio/wav">
Your browser does not support the audio element.
</audio>

Converting this to a spectrogram, we see a nice uniform sweep

![text](/assets/freqSweepSpec.png)

## Playing the Sound

Athough some experiments are in need, I thought I would jump to the chase: I happened to have a small bluetooth speaker around, so I used that to generate the sound. I also measured the dimensions of my shower to be about **57 x 22 inch**

<iframe width="1198" height="674" src="https://www.youtube.com/embed/5kJpnmpz_0Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Analyzing the Spectrum

Bringing the audio back into matlab and then looking at the spectrum, we see that the intensity is not uniform! A promising sign

![spectrum](/assets/bathroomSweep.png)

We can notice that there are two dominant frequencies that pop out, and then also their approximate harmonics!

![annotSpec](/assets/bathroomSweep_annot.png)

Two dominant frequencies that appear are **344 Hz** and **414.5 Hz**. We can now use this to estimate the shower dimensions.

## Estimating Dimensions

Using an estimated speed of sound (using the barometric pressure and temperature), we can plug and chug:

$$ c = 1123.32 \text{ ft/s} $$

$$ \lambbda = \frac{c}{\omega} $$

$$ \lambda \req .0402 \text{inches}$$

We can see that the resonant frequency has a pretty small associated wavelength. We might hope that this frequency is a *harmonic* of the fundamental. In this case, since the shower has a rectangular shape, we might expect two harmonic frequencies: one that corresponds to the length, and one that corresponds to the width. 

The powers that approximetaly put us in this range are 2^9 and 2^11 (respectivly).


```matlab
ss = 1123.32; % Speed of Sound

freq = 344.2;
(ss*12) / ((freq/(2^9))*1000)

freq = 414.5;
(ss*12) / ((freq/(2^11))*1000)
```

Generates:

```pre
20.0514

66.6024
```

Maybe??

I will point out, I think that is actually unlikely to be what we think it is, but it was cool none the less to see that our frequency response to the sweep was far from flat!

## Verifying Approach

In order to see if the results are sensible, I thought two experiments would be:

1. Placing speaker in a box of known dimension to estimate any correction factors
2. Play outside in open area to see how flat the frequency response is when no resonant frequencies are expected

These tasks are ongoing projects! 


