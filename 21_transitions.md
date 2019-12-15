# Transition measurements	

## TODO
	Read: 
		Vassen 1557nm
		Martin 1960
		Luo et al & refs
		Drake etc theory papers for outstanding differences
		Ketterle: Evaporative cooling of neutral atoms (for rough model)
		Motivation & methods/state of the art for transition rate measurements
		Kieran's Forbidden code
		WTH actually drives forbidden transitions?
	Calculate
		Stark shift
		Three-level model
		Evap toy model
		Anticrossings
		Number unc
		Forbidden SNR redux
		Precision needed for isotope shift measurements?
	Figures
		Sequence diagram

This chapter describes two sets of measurements of electronic transition energies in Helium. First, I recount the method and used to measure the energy splittings between the 23P2 state and a collection of states in the n=5 manifold. Second, I describe two methods used to measure the splitting and the transition lifetime of the forbidden 23S1-33S1 transition. 

## Gap, aim, and scope
	
Some of the 2P-5L transitions were observed by Martin in 1960, but his measurements are in stark disagreement with predictions made by Drake in 20xx. Further, in the NIST database, the transition energies to the 53D states are all identical. Indeed, in Martin's original paper, he only quotes measurements from 23P2-5D, indicating that his equipment did not have the resolving power to distinguish the lines from the 23P to the 53D states, and so obtained a weighted average of the energy splittings that I resolved individually for the first time. 
Martin was also unable to distinguish the 51D2 transition line, perhaps because of its proximity to the 53D lines. Even so, the transition rate is five orders of magnitude less than the n=5, L=3 transitions, so even if he had the resolving power he probably wouldn't have been able to detect the line? I wonder what the weakest line he found is.
Given the unerring accuracy of QED in most other arenas, it is prima facie not obvious that this disagreement points to a calculation error or a domain where QED is not valid. That said, the method for measuring excited-state transitions extends to the first observation of this singlet-triplet line, which is of interest given the outstanding disagreement on the singlet-triplet interval as constrained by the precision measurement by Vassen's group. 

The 1557nm transition was of particular interest because of its incredibly low transition rate. Predictions of these require corrections from QED. Later in this chapter I will discuss the first measurement of the 427nm transition, whose transition rate is XXX times slower than Vassen's, and a second method to measure the same transition from which we calculate the Einstein A coefficient of this transition. To our knowledge is the weakest transition observed in a neutral atom to date. Include Lach and Pachucki comment.

## Contribution	

The table below displays the results of the measurements, including predicted linewidths. In the case of the 23S1-33S1, the measured Einstein A coefficient is also listed. These measurements are accurate to a few hundred parts per billion, and their accuracy is limited by the absolute accuracy of the wavemeter we used as a reference for the laser lock. Within the accuracy stated by the manufacturer, these results are consistent with the predictions of QED. Of the six lines measured, three have been resolved individually for the first time, and two have not been recorded elsewhere. The centre frequencies are obtained by fitting Lorentzian profiles to the atom loss spectra. Have a look at residuals; what are the expected broadening effects? What are the expected systematic errors?
Error budget goes here also.

## Method: 5L
	To drive the transitions from the 23P2 state to the states in the n=5 manifold,	I use the probe beam to disturb the near-resonant optical molasses cooling stage of the experiment. This follows the MOT loading and precedes evaporative cooling, and operates with XYZ beam parameters for XXX ms, and then with ABC beam parameters for YYY ms. I calculate that during these stages, the excited-state population is ZZZ per cent, which are then susceptible to scattering photons from the probe beam. 

	The beam was initially aligned by tuning the probe beam to the predicted value of the 53S1 transition and operating with the maximum available power. Although the uncertainy in wavemeter accuracy was larger than the transition linewidth, by operating well above the saturation intensity, the transition was broaded by tens of MHz and so the WM error was  less significant. When scanning the beam pointing across the expected target region, approximate alignment was signaled by a dramatic loss of atom number. When the signal saturated, the power was lowered until the signal was just above the noise floor, and then scanning resumed. This process iterated a few times until the maximum attainable signal was below saturation - that is, when for fixed power one could not completely destroy the trap. Notice there are three kinds of saturation here: Atomic population saturation, detector saturation, and signal saturation when you run out of atoms. perhaps the term 'dynamic range' would be more suited to the latter... Something to think about. 
	
	I used the evaporative cooling sequence as a transducer between scattering-induced heating of the cloud and the final condensed number. I will present a quantitative sketch of the mechanism below, but one can also take a heuristic understanding from the following argument:

	The evaporative cooling we use to achieve Bose-Einstein condensation has stringent tolerances on initial phase space density, which increases with number and at lower temperatures. Tuning a radio chirp to the spin-flip transition from a trapped to an untrapped state and sweeping down to lower energies, higher-energy atoms are removed, the cloud rethermalizes at a lower temperature, and the phase space density increases.	Higher-energy atoms spend time further from the centre of a harmonic magnetic trap. So, scattering photons from the probe beam heat the cloud, leading widening the velocity distribution, which drives more of the atoms into resonance with the radio chirp. The final temperature is determined by the endpoint of the radio chirp. Resonance with the probe light manifests as a signal in a reduction of the final population of the condensate. 

	The method therefore consists of alternating measurement trials with control trials, wherein the laser beam is blocked before the fibre coupler with a flipper mirror. At the moment I use an interpolation, but I might want to try using a model-based estimate of the atom number. Either way, there is going to be some error in the number estimation. It's probably small. The difference between the interpolated, unperturbed atom number and the detected number in the measurement trials is affected by the quantum efficiency and the introduced uncertainty in atom number.

	The polarization of the light was fixed with the waveplates before the chamber. Can you tell handedness just by relative angle of waveplates? We hypothesized that the initial state of the atoms during the cooling phase was in the m=2 state, as the optics are configured to drive with a sigma+ beam during the in-trap cooling stage. I verified this by driving with plane-polarized light (in the atom frame - put some trap sim in to show where the field points), which is a linear combination of sigma+ and sigma- light. If there were atoms in initial states other than the m=2, then when driving to the 53S1 state, one would observe multiple peaks. Instead, only one peak was observed, which vanished when the probe beam was set to sigma+ light. (I think check the data).

	The measurements are taken at two different background field strengths. Therefore the detuning from cooling resonance is X and Y MHz in each stage, respectively. These values were calibrated independently by an RF spectroscopy technique. This allows empirical extrapolation to the field-free transition energy by correcting for the calculated Zeeman shift of the centre frequency of each measured line. 

	QUANTITATIVE MODELS
		Evaporative cooling
		Scattering rate and heating - can you determine the oscillator strength at all?

	Analysis

## Method: Forbidden 1
	
	After our measurement of the 2P-5L transitions, our eyes turned to the 427nm transition. To our knowledge, nobody had measured it. We found that we required ten orders of magnitude greater sensitivity in order to detect this transition - a few mW over a few ms wasn't going to cut it. After discussion we decided that the most promising method might be to look for heating or loss by directly illuminating a BEC - having found previously that weak trap lifetimes can in fact be several minutes. However, before we embarked on the measurement, I performed some simple calculations to estimate the order of magnitude of the best signal-to-noise ratio we could expect.

	We determined that this SNR would be sufficient to warrant making an attempt at the measurement. 

	RECOUNT CALCULATION 
		3 level measurement
		Clebsch-gordan coefficients and net transition rates
		Collection efficiency monte carlo
	
	Sequence diagram
	
	For this measurement, the data processing methods were the similar to the 5L transitions - a drift model was created to predict the undisturbed atom number in a given shot, based on atom number measurements from the calibration shots. Wait - did the outcoupled fraction get used, counting the number dropped versus the number left in the trap? Were these things tried? Talk to Kieran.

	This method allows for the extraction of the line centre and width, which determines the state lifetime. However, the state lifetime is dominated by a fast decay to the 3P state, the oscillator strength of which is many orders of magnitude larger. The oscillator strength - which is proportional to the Einstein A coefficient - of the transition can be obtained by another method, described in the next section.

## Method: Forbidden 2

	We develop a second method to determine the Einstein A coefficient of the specific forbidden transition. We perform time-dependent thermometry of the a thermal cloud (above the critical temperature) while alternating shots with and without the probe beam blocked. During these sequences, we use RF pulses as per standard procedure (although in this case the term 'laser' is especially misleading as the source is incoherent) and fit a Gaussian profile to each pulse. During the 25 second hold time, the cloud heats at a rate of X K/sec. This is possibly due to: Penning ionization, magnetic field noise, background collisions, majorana leaks? How does it depend on number? Anyway. With the probe beam applied, the calculated scattering rate of up to Y Hz corresponds to a peak additional heating rate of Y J/sec. We fit the time evolution of the temperature of the thermal cloud with a linear model and obtain the change in heating rate with respect to the probe-free shots. We can then back-calculate via the specific heat of a harmonically trapped Bose gas to determine the energy transfer rate (which should just be proportional I think, when above the critical temperature?), hence the photon scattering rate. And so lo and behold we can determine the A coefficient, and look, it's really weak! What a great job we did.   I wonder whether Kieran's method is a bit sketch because does heassume a certain density distribution??

## Systematic effects

	Power & curvature measurements - what actually drives Quadrupole transitions?

## Next?	
	Isotope shifts & better reference
	Different target transitions?

Link to next chapter