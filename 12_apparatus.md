# BEC recipe
## Tabula rasa: Vaccum system	
	
	Why vacuum?

		Physical models often make simplifying assumptions, like ignoring air resistance or friction, or collisions etc. Idealized models are only solvable in certain special cases, and introducing nonlinear effects like friction can make them mathematically intractable. This is partially resolved by sophisticated modelling these days, but the approximations will always remain. So when it came to studying microscopic systems, one would like to remove the background. so that the thing you are examining becomes not only the foreground, but the only thing in the image, and so your signal is not obfuscated. So people have tried to make vacuum for quite some time! Indeed this is one way atmospheric pressure was measured - Lavoisier used pumps from teh fire station to evacuate a chamber, and since then vacuum has advanced considerably. Vacuum manufacture is a massive industry now, and I wonder if I could find a history of vacuum pressures over time to track the best known vacua. In the case of ultracold atoms, one needs to maintain a vacuum because the forces that hold the atoms in their optical or magnetic traps are so frail that capturing particles from the atmosphere would be all but impossible - what fraction would have sufficiently low energy to capture, and how long would they last? So, yeah, yuo need vacuum, and the lighter your atoms, the more worried you should be about vacuum. It also provided benefits like making sure lines stay narrow to mitigate pressure broadening et cetera - trapping atoms in vacuum is in some sense the ideal tool for the physicist - to study things in almost perfect isolation, to extricate the subject of study with complete mastery over its environment. But nature abhors a vacuum, and so will find ways to ruin your day. So there are a ton of ways to get a chamber close to empty. Let's talk about a few of them. 
	Chamber architectures
	Scales
		Best vacua
		Mean free path & collision time

## Cooling and trapping	
	Metastable helium
		
	Optical methods & limits
		In this section I give a hueristic introduction to laser cooling. The detailed theory of atom-light interactions will be saved until the chapter on atomic transitions where the theory becomes necessary to understand the work.  If the next couple of secgtions aren;t sat leatst. 
		
		Consider a two level atom. It is probably possible to get away without using the word hamiltonian, so I would give a basic picture. Atoms can be thought aof as having two states: One where the electron is further away from the nuclers? state (as the sxcited state0) and that the energy level flips up or down with the adition of a photo. Oh ok so I would have to say why it is quantized perhaps, so there would be something to draw on in the chatper perfio previously, where I talk history of QM, which would probably include something about Planck's u idea of quantized areas phase space. But then again - there could well be a QM primer in the Moern er modern QM chapter - perhaps with the flag that 'this is the only math in the introduction chapter' but then there are things like the doppler cooling et cetera. I think perhaps a differnt structure would suffice: a non-technical summary at the top of each section/cahpter we with a digression into deeper and depper detail as you get towards the next section. Then people can tap out and push on to the next section whe 
	Magnetic traps & evaporative cooling
	Degenerate matter
		In this secion I will try to gvie a description of ultracold degnerate matter that even py a parents can understand! What a challenge. So I think it will be done in a cuple of parts. oNe where one considered a parabolic bucket with atoms rolling aroudn in it - at high energy they don't see each other. As they lose energy they get closer and clsoer to each other eeventually such that their interactions cant be ignored - they keep pinging off each other. They won't let the other balls take up ther space they are occupying. But there are two kinds of matter hey, there are bosons and fermoins. So at this pojt one would be able to intotduce the communtation relations in the technical part but fur the moment just accept: There is a wave-particle duality, you can see it with photon.s That would be a find introduction - well I guess it lives up in the itnro about when QM was born and all that. The double slit experiment would be a great example 0 maybe actualyl just the single slit, you know, that illustrates the diea of diffraction (does it?) and particles - depends what one is trying to show. I think yes the doule slit ecnompasses most of quantum (except entanglement lel) but hey. So yeah, I guess in this part would be something like a toy model, and then one can introduce the critical points like:
		That there is a ground state of traps, that the numbe rof particles in this state can be more than one when yuo are working with bosons, but not fermions. ANd they ahve to be cold - heuristically the picture could be that (because trying to avoid this idea of microstates) actually don't avoid them, but I really wonder how simple ane xplanation one can make here. But then again what's the idea behind going for simple? The're is the idea that someone will bea ble to read the thsis as a motivatedd undergrad, or as my parents so they sort of would be able to see what happened, or to new students in the lab, who could be able to read quickly but hey if you get to the point of joining th lab you must pbe pretty math-savvy. So. Yeah. What do we talk about? 
		HIstory of degenrate matterWell that was sorta covered in the super intro. Maybe that would just be
	Absolute limits of cooling
		Thermodynamic limits
		Modern methods
			Cooling fermions
			Prospects for feedback cooling?
			Quantized refrigerators
			Algorithmic cooling
			Other techniques: dilution fridges etc

## Diagnostics & detection	
	Ionization rates
		Penning ionization equation
		Density dependence
		Field dependence => Not a good absolute measure without calibration
		Historical uses: Measuring BEC transition
	Fluorescence
		Theory, some example plots
		Calculation of population from signal
			Precision
	Absorption imaging
		Theory
		Sure, it's a momentum measurement, but let's calculate its limits
			Limited resolution and sensitivity - make some reasonable assumptions
		There is also fluorescence imaging in gas microscopes but we don't have the optics for this
	Delay-line detector
		System diagram
			Signal pathways
		Resolution in TXY
		Field of view in K-space
		Optics analogy
		Dark counts
		Saturation
	Atom lasers: CW, Pulsed & trap freq
		CW 
			Sweep model
			temperature fitting?
			Correlations?
		Pulsed
			Outcoupling spectra
				Fourier broadening
			BCR
			'Weak' number measurements & single-shot precision
		Trap frequency measurements
			Compressed sensing
			Aliasing
			Optimal sampling methods?

## Laser systems	
	ECDL
		System diagram
		How dither locking works
		Experiment insertion
			Lattice build described in lattice chapter, stick to downstairs architecture to begin with
	TiS
		Seed & pump for 532nm
		TiSaf
			Cavity, crystal, etalon 
			Locking system
		Doubler
			Mechanism
			Locking
	Calibration
		Software lock loop
			MATLAB architecture - appendix?
		Wavemeter 
			How it works
		Cs crossover transition
		PMT setup - 
			dither lock
			Stability of lock
			Bounds on accuracy of calibration
	Alignment
		Camera/mirror setup 
			Reproducibility issues
		BEC slicing - did it work?
			Broken optic & weird structure in BEC - images?
		Atom trapping method
			Difference in beam pointing because of dispersion
		Trap frequency metho