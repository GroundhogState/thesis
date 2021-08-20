# Referee Comments on 2 3S1 - 3 3S1 paper
I have tried to distill the referee comments into actionable tasks (looking at you referee B) and assign them to (who I think is) the most relevant team member. Tell me if you think you can't do the task/ and or don't want to, or if there is an extra task you would like to do.

## Questions for Everyone
- [ ] Is there anything to be done about the comment? 
    > "In the conclusion the authors state that if they would use a frequency comb laser for calibration, sub-MHz accuracy could be achieved on the transition they measured. As 200 Hz has already been achieved on a transition in helium that is a lot narrower, it is clear that this is not the main strength of the paper, even though the measured transition is a nice addition for QED testing as the theoretical accuracy is at MHz level currently"
    - Bryce: maybe perhaps just parroting back their points but with a more positive spin
      - while our precision does not compare to the excellent work of [] as mentioned whcih we point out is the product of a xxx year campaign
	  - because of the lower signal level it its unlikey that this transition will usurp the most well measured transition in he. However the lack of line interference effects may be ease future sub-linewidth determination.
	  - the value of this determination is the sum of the transition strength, the novel approach and the transition frequency determination
      - while the theoretical uncertainty is small it is still comforting to see the agreement on a transition that have been outside the scope of previous comparison
	  
- [ ] Should we remove some of the thorium nulcear clock refs (we have 4 [27-30] in the previous version of the manuscript)
  - Bryce: yea, ref. B is not having much of the concept that our method could be usefull here. maybe 1 or 2 if they are mentioned seperately.
  
- [X] resolved (mention it briefly in a more historical/exemplar context) We are referring here to the 'Proton Radius Puzzle' without mentioning it. Should we mention it?
  - Bryce: maybe, this determination is so insensitive to it we should be careful to not give the impression that we will help directly.
  
- [ ] Does anyone know how the Stark shift effects line shape?
  - Bryce: nope, id expect it to be small isnt a line-shape change well within our total err budget
- [ ] How should we do frequency 'error bars' as bin limits is confusing apparently, is mentioning that error in frequency is small enough?
  - Bryce: com
    - i dont think its any more confusing than a histogram
	- could use double bars, capless for the limits and caped for the standard deviation
	- its so unimportant for the message from the plot
	- should maybe show in soms unbinned data
- [ ] What is sufficently Fourier Broadened, how short are we talking?
  - Bryce: com
    - as a first approx calculate the energy width of the BEC/thermal by converting the TF/themal energy into photon freq (of order khz)
	- given the pulse (top hat function) find the power spectral density (sinc function)
	- find the relative difference between the peak and offset by the photon freq earlier, hopefully this is within 10% or so
	- put those details in the paper
- [ ] How do we convincingly measure/derive the effective laser linewidth particuarly for the lifetime measurment?
  - Bryce: its hard
    - the time period that you need the linewidth for is the duration of the exp's that gave fig 3.
    - easiest way for medium term (integrated up to ~30s) linewidth is to get the width from the 2p cell scans
	  - should be easy enough to read them in and fit
	  - then make some approximations of how this translates to the blue
	- maybe you can get an effective linewidth over the total exp. peroid by 'stacking' all the 2p scans over the period of measurement
      - pretty convincing as a plot !
	- it may also be good to show the allan deviation of the wavemeter
      - we have measured (but not yet analyzed) by keeping the laser locked to the 2p cs ref
	  - wont be too complicated to analyze just feed wavemeter data into allan deviation calculator


## Bryce Requests
- [ ] Discuss briefly the tune-out measurment and how it compares/differes to this measurment and add a few references to manuscript about tune-out.
- [ ] Add some ideas why this alternative form of testing QED (transition strength) is important

## David Requests

## Jacob Requests
- [ ] Literature references, particularly about photon recoil heating in ions and weak spectroscopy. 

## Kieran To Do
### General
- [X] Change through out paper  
    - [X] 'scattered atoms" -> excited and decayed 
    - [X] later: "un-scattered" -> not excited
    - [X] "scattered to un-scattered" -> "excited to not excited" 
    - [X] "scattered fractions" -> "excited fractions"

### Abstract
Everyone seemed to think the abstract was good :)

### Intro
- [ ] In Intro add a line and some cites regarding previous 3He and 4He experiments specifically: 
    - [ ] better alpha fine structure determination; 
    - [ ] Lamb shift; 
    - [ ] generall QED tests in simple calculable system like He.
- [X] 1st page, second column, when referring to the 2 3S1 - 2 1S1 transition mention/cite (Rengelink et al., Nat.Phys. 14, 1132-1137 (2018)) and (Cancio et al., Phys. Rev. Lett. 108, 143001 (2012)) also
- [ ] Add references to literature on detection of an excitation by the heating effect by the photon recoil during excitation, already used for quite a while in ion spectroscopy and atomic clocks (see e.g. Nat. Commun. 5, 3096 (2014)).
- [X] added (there are still unknown factors and parameters, as shown by the recent "proton radius puzzle" that required a re-assessment of the proton radius \cite{Pohl2010,Antognini417,Bezginov1007,Xiong2019}) For "QED ... rigorously tested" it is not about ‘elements of QED’ that are not well constrained. It is about the proton radius and Rydberg constant. Cite also at least one paper by the group of Randolf Pohl as they displayed first that previous proton radius/Rydberg constant measurements could be wrong by 5 sigma.
- [X] changed (new to state of the art) page 2, first column: "new technologies” referring to atomic clocks. maybe recent or emerging or relevant technologies is better
- [X] Fig 1. caption: "is 427.7 nm”; probably "is at 427.7 nm" is better

### Direct/Heating Methods
- [X] changed (added a short paragraph explaining this point) In the heating method note that this detector only works for meta-stable helium because of its high internal energy; for other atoms one would have to use optical methods such as absorption imaging to determine the cloud temperature, which is far less sensitive.
- [X] 2nd page, bottom of first column: "small numbers of atoms that absorb the laser light": what is small?
- [X] 2nd page, second column: it is mentioned that the excitation is from the m=+1, but not that the sample is prepared in the m=+1 also to avoid Majorana spin flip losses (so mention it).
- [ ] 2nd page, last column: "This transfers all atoms into an atom laser": I understand what the authors mean, but for a general audience this is a bit cryptic (make this clear for non experts).
- [X] added (for further details on the beam shape and power in relation to the atom sample see \cite{SOMs}) Page 3, top first column: what is the laser power level at 427 m, and at what power density and beam size in relation to the atom sample? I could not find it in the manuscript or SOM. (Put these parameters into the SOMs and have ref to that in text)
- [X] added (While this effect is measurable, as it is small it should have a negligible effect on the line shape compared to the other sources of error) Just below the previous point: the probe beam deflects /changes the atom distribution due to Stark effect; how much does this change the line shape? (talk about how stark effects line shape)
- [ ] 3rd page 1st column, bottom, the discussion about the lifetime: see the remarks below about the SOM.
- [X] 3rd page 1st column "extremely well”: given the accuracy I would say "very well" (changed)
- [ ] Fig 3: The horizontal bars bars are apparently the limits of the bin. I find this very confusing, one would expect it to be the error in the frequency. The error taken for the horizontal scale is not mentioned here. (mention the error in the horizontal scale (and that it is negligable))
- [X] what i changed (time integrated power to applied energy) Fig 3, in the caption a "power" of 0.635 J is mentioned, but this should be “energy”
- [X] Fig 3 and 4: To avoid confusion I recommend that in the caption it is mentioned that the stated error bar for the transition frequency is purely statistical
- [ ] Page 3, second column: what do the authors mean with ‘sufficiently Fourier-broadened”? I presume that the pulse is short in time, and so has a wide spectrum? (how short / or how wide?)
- [X] Table 1: "vapor shift”: I think this is more commonly known as a pressure shift

### Conclusions
- [ ] reword “new extremely sensitive method for measuring and characterizing spectroscopic transitions” as too strong given what has been demonstrated with ions, and the requirements to make the method work (ultra-cold clouds and a very efficient detection scheme made possible by the high internal energy of meta-stable helium).
- [ ] reword “The high sensitivity…” and the one following about nuclear clocks as the presented method cannot so easily be applied to other atoms.
- [ ] Remove/ change the part where we compare Amin to the theoretical uncertainty
- [ ] Push the importance of alternative QED test more

### SOMs
- [ ] Expalin in more detail in section VI how we calculate the tansfer of energy Ep, specifically the monte carlo sim for the scattering rate as the atoms leave the BEC (ie. make it clear we do not assume full thermilisation)
- [ ] Make clear how the error in the Einstein A is calculated (probably in SOMs section VI)
- [X] Below Eq. 1: Zeeman effect: in text g_j, but should be g_j,g and g_j,e
- [ ] make BEC size and 427 nm beam size and power clear, as well as intensity of the laser interacting with the atoms, or how homogeneous the interaction with the atoms is.
- [ ] Expalin for figs S3 and S2 in relation to S1 that we are considering the laser linewidth over different time scales, hours for the full measurment, but only at most aminute for the calibration measurments.
- [ ] For the mean-field shift: In the low-excitation regime I would say the transition shift comes from i-i and e-i collisions, as can be seen in ref. [7] from eq. 2. So also the excited state can shift. Can the authors comment on this? (basically add e-i collisions to the mean-field shift equation)
- [ ] Does equation 14 assume borard band excitation (not seem to be a valid assumption as at least the short-term laser line width is much shorter than the transition.), I need some more clarification. How can I fix this if so?
- [ ] Fix the sensitivity metric (it doesn't really make sense right now) in addition to the concerns raised before, I had a hard time understanding the scaling of the sigma (signal to noise ratio) that is defined just above eq. 17. I would expect the signal to noise ratio to improve for bigger N, t or P, but according to the definition it goes down. That is not the behavior one needs for eq. 17, because then for increasing N, t or P the minimum detectable A goes up.
- [ ] It stands for Joules (What does the J stand for in the paragraph after formula 17 in the SOM?)
- [ ] How do we conviencly measure/derive the effective laser linewidth particuarly for the lifetime measurment, Part V: excited state lifetime, laser linewidth: I find it difficult to see how it is possible to make relative measurements as shown in S2 and S3 with sub MHz precision, and at the same time claim a laser linewidth of 2 MHz based on the wavemeter calibration Fig S.1. The variation in S1 does not have to come from the laser linewidth, and it does not have to be Gaussian either. The SolsTiS laser the authors use is marketed as one of the most stable lasers with a free running bandwidth of 50 kHz. Long-term drift is no doubt more than that, but to estimate a laser line width simply based on curve S1 might not be  correct (and it does influence the derived transition lifetime). S1 does not seem to have enough points for proper statistics. Can the authors explain this more?

