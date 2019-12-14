# Transition measurements	

## TODO
	Read: 
		Vassen 1557nm
		Martin 1960
		Luo et al (again) & refs
		Drake etc theory papers for outstanding differences
		Ketterle: Evaporative cooling of neutral atoms (for rough model)
	Calculate
		Stark shift
		Three-level model
		Evap toy model
		Anticrossings
	Figures
		Sequence diagram

This chapter describes two sets of measurements of electronic transition energies in Helium. First, I recount the method and used to measure the energy splittings between the 23P2 state and a collection of states in the n=5 manifold. Second, I describe two methods used to measure the splitting and the transition lifetime of the forbidden 23S1-33S1 transition. These measurements are accurate to a few hundred parts per billion, and their accuracy is limited by the absolute accuracy of the wavemeter we used as a reference for the laser lock. Within the accuracy stated by the manufacturer, these results are consistent with the predictions of QED.

## Gap, aim, and scope
	* Helium spectroscopy & outstanding differences.
	
Some of the 2P-5L transitions were observed by Martin in 1960, but his measurements are in stark disagreement with predictions made by Drake in 20xx. Further, in the NIST database, the transition energies to the 53D states are all identical. Indeed, in Martin's original paper, he only quotes measurements from 23P2-5D, indicating that his equipment did not have the resolving power to distinguish the lines from the 23P to the 53D states, and so obtained a weighted average of the energy splittings that I resolved individually for the first time. 
Martin was also unable to distinguish the 51D2 transition line, perhaps because of its proximity to the 53D lines. Even so, the transition rate is five orders of magnitude less than the n=5, L=3 transitions, so even if he had the resolving power he probably wouldn't have been able to detect the line? I wonder what the weakest line he found is.
Given the unerring accuracy of QED in most other arenas, it is prima facie not obvious that this disagreement points to a calculation error or a domain where QED is not valid. That said, the method for measuring excited-state transitions extends to the first observation of this singlet-triplet line, which is of interest given the outstanding disagreement on the singlet-triplet interval as constrained by the precision measurement by Vassen's group. 

The 1557nm transition was of particular interest because of its incredibly low transition rate. Predictions of these require corrections from QED. Later in this chapter I will discuss the first measurement of the 427nm transition, whose transition rate is XXX times slower than Vassen's, and a second method to measure the same transition from which we calculate the Einstein A coefficient of this transition. To our knowledge is the weakest transition observed in a neutral atom to date. 

## Contribution	

The table below displays the results of the measurements.

	Three methods, six lines
	Direct A measurement
		Other measurement methods of oscillator strengths
		Existing best precision & motivation
		Uh what do you learn from these?
	QED seems fine

## Method: 
n=5	
	To drive the transitions from the 23P2 state to the states in the n=5 manifold,	I use the probe beam to disturb the near-resonant optical molasses cooling stage of the experiment. This follows the MOT loading and precedes evaporative cooling, and operates with XYZ beam parameters for XXX ms, and then with ABC beam parameters for YYY ms. I calculate that during these stages, the excited-state population is ZZZ per cent, which are then susceptible to scattering photons from the probe beam. 
	
	I used the evaporative cooling sequence as a transducer between scattering-induced heating of the cloud and the final condensed number. I will present a quantitative sketch of the mechanism below, but one can also take a heuristic understanding from the following argument:

	The evaporative cooling we use to achieve Bose-Einstein condensation has stringent tolerances on initial phase space density, which increases with number and at lower temperatures. Tuning a radio chirp to the spin-flip transition from a trapped to an untrapped state and sweeping down to lower energies, higher-energy atoms are removed, the cloud rethermalizes at a lower temperature, and the phase space density increases.	Higher-energy atoms spend time further from the centre of a harmonic magnetic trap. So, scattering photons from the probe beam heat the cloud, leading widening the velocity distribution, which drives more of the atoms into resonance with the radio chirp. The final temperature is determined by the endpoint of the radio chirp. Resonance with the probe light manifests as a signal in a reduction of the final population of the condensate. 

	The measurements are taken at two different background field strengths. Therefore the detuning from cooling resonance is X and Y MHz in each stage, respectively. These values were calibrated independently by an RF spectroscopy technique. This allows empirical extrapolation to the field-free transition energy by correcting for the calculated Zeeman shift of the centre frequency of each measured line. 

	QUANTITATIVE MODELS
		Evaporative cooling
		Scattering rate and heating - can you determine the oscillator strength at all?

	The method therefore consists of alternating measurement trials with control trials, wherein the laser beam is blocked before the fibre coupler with a flipper mirror. At the moment I use an interpolation, but I might want to try using a model-based estimate of the atom number. Either way, there is going to be some error in the number estimation. It's probably small. The difference between the interpolated, unperturbed atom number and the detected number in the measurement trials is affected by the quantum efficiency and the introduced uncertainty in atom number. I show the 


	Overlap beam with atom cloud (How big is the MOT? Maybe run some calcs. How big is the beam?)

		How does evap affect temp? Use a simple model, though our sequence is bunk.
		Just need a heuristic explanation - hopefully theres a 'we can't determine exact relationship' in there somewhere. 
	Analysis
Forbidden	
	Theory & predicted SNR
	Sequences
	Analysis
## Issues	
	Power & curvature measurements
	instrumentation
	Didn't actually test QED
## Next?	
	Isotope shifts & better reference
	Different targets?

Link to next chapter