# BEC recipe

## TODO
	Read up history of Bose - talk to Mukunda?


## Tabula rasa: Vaccum system	
	
	Why vacuum?

		Physical models often make simplifying assumptions, like ignoring air resistance or friction, or collisions etc. Idealized models are only solvable in certain special cases, and introducing nonlinear effects like friction can make them mathematically intractable. This is partially resolved by sophisticated modelling these days, but the approximations will always remain. So when it came to studying microscopic systems, one would like to remove the background. so that the thing you are examining becomes not only the foreground, but the only thing in the image, and so your signal is not obfuscated. So people have tried to make vacuum for quite some time! Indeed this is one way atmospheric pressure was measured - Lavoisier used pumps from teh fire station to evacuate a chamber, and since then vacuum has advanced considerably. Vacuum manufacture is a massive industry now, and I wonder if I could find a history of vacuum pressures over time to track the best known vacua. In the case of ultracold atoms, one needs to maintain a vacuum because the forces that hold the atoms in their optical or magnetic traps are so frail that capturing particles from the atmosphere would be all but impossible - what fraction would have sufficiently low energy to capture, and how long would they last? So, yeah, yuo need vacuum, and the lighter your atoms, the more worried you should be about vacuum. It also provided benefits like making sure lines stay narrow to mitigate pressure broadening et cetera - trapping atoms in vacuum is in some sense the ideal tool for the physicist - to study things in almost perfect isolation, to extricate the subject of study with complete mastery over its environment. But nature abhors a vacuum, and so will find ways to ruin your day. So there are a ton of ways to get a chamber close to empty. Let's talk about a few of them. 
	Chamber architectures
	Scales
		Best vacua
		Mean free path & collision time

## Cooling and trapping	
	
	Optical methods & limits
		In this section I give a hueristic introduction to laser cooling. The detailed theory of atom-light interactions will be saved until the chapter on atomic transitions where the theory becomes necessary to understand the work.  If the next couple of secgtions aren;t sat leatst. 
		
		Consider a two level atom. It is probably possible to get away without using the word hamiltonian, so I would give a basic picture. Atoms can be thought aof as having two states: One where the electron is further away from the nuclers? state (as the sxcited state0) and that the energy level flips up or down with the adition of a photo. Oh ok so I would have to say why it is quantized perhaps, so there would be something to draw on in the chatper perfio previously, where I talk history of QM, which would probably include something about Planck's u idea of quantized areas phase space. But then again - there could well be a QM primer in the Moern er modern QM chapter - perhaps with the flag that 'this is the only math in the introduction chapter' but then there are things like the doppler cooling et cetera. I think perhaps a differnt structure would suffice: a non-technical summary at the top of each section/cahpter we with a digression into deeper and depper detail as you get towards the next section. Then people can tap out and push on to the next section whe 
	Magnetic traps & evaporative cooling

	The Doppler limit means that, for Helium, optical cooling to the ground state is not possible. This is when the velocity selectivity of the cooling light matches the velocity width of the sample. To reach the condensation threshold at the recoil limit, how big or dense would your trap have to be? Not reliable. This threshold was the limit for cold atom experiments until the development of evaporative cooling and polarization gradient cooling, which enabled the first production of bose-einstein condensates and resulted in the awarding of the 2001 Nobel prize in physics. Polarization gradient cooling is unavailable in Helium-4 because the spinless nucleus means there is no hyperfine structure, but fortunately evaporative cooling can achieve the low temperatures required for condensation in experimentally feasible traps. See any number of cold atom textbooks for an introduction or Ketterle's paper for a great deal of detail. Here we provide a summary explanation only. Additional details are discussed in chapter 3, where the evaporative cooling process is part of the relevant experimental method. 

	Absolute limits of cooling
		Thermodynamic limits
			Third law & quantum proof
			Trap losses
	Modern methods
		Cooling fermions
		Prospects for feedback cooling?
		Quantized refrigerators
		Algorithmic cooling
		Other techniques: dilution fridges etc

	Degenerate matter
		In this secion I will try to gvie a description of ultracold degnerate matter that even py a parents can understand! What a challenge. So I think it will be done in a cuple of parts. oNe where one considered a parabolic bucket with atoms rolling aroudn in it - at high energy they don't see each other. As they lose energy they get closer and clsoer to each other eeventually such that their interactions cant be ignored - they keep pinging off each other. They won't let the other balls take up ther space they are occupying. But there are two kinds of matter hey, there are bosons and fermoins. So at this pojt one would be able to intotduce the communtation relations in the technical part but fur the moment just accept: There is a wave-particle duality, you can see it with photon.s That would be a find introduction - well I guess it lives up in the itnro about when QM was born and all that. The double slit experiment would be a great example 0 maybe actualyl just the single slit, you know, that illustrates the diea of diffraction (does it?) and particles - depends what one is trying to show. I think yes the doule slit ecnompasses most of quantum (except entanglement lel) but hey. So yeah, I guess in this part would be something like a toy model, and then one can introduce the critical points like:
		That there is a ground state of traps, that the numbe rof particles in this state can be more than one when yuo are working with bosons, but not fermions. ANd they ahve to be cold - heuristically the picture could be that (because trying to avoid this idea of microstates) actually don't avoid them, but I really wonder how simple ane xplanation one can make here. But then again what's the idea behind going for simple? The're is the idea that someone will bea ble to read the thsis as a motivatedd undergrad, or as my parents so they sort of would be able to see what happened, or to new students in the lab, who could be able to read quickly but hey if you get to the point of joining th lab you must pbe pretty math-savvy. So. Yeah. What do we talk about? 
		History of degenerate matter: Well that was sorta covered in the super intro. 

		Ok. Revising the content of this section. It will be the brief introduction to BEC. Consider a gas of non-interacting bosons in a harmonic oscillator potential. This can be treated in the grand canonical ensemble - plz clarify what the reservoir is - and so do you need to talk density matrix? I mean the Penrose-Onsager criterion is one way to do it. Seems relativistically fine - all good for the ground state biz but extends to nonzero momenta (moving frames). Blah. Bose-Einstein statistics. Bose enhancement re: scattering into the ground state. Point to references. Blah. No more words arriving. Let's fuck it I will see if I can get some formatting done here...

	BEC three ways

	The title is an illusion to Prithvi and my sketchy plan for pear, three ways. First, the heuristic.

	While the industry of European statistical physics was in its infancy, a young admirer of Einstein began asking questions would plant the seed of a flurry of work culminating in a technical triumph over the next seven decades. Satyendra Nath Bose made postulates about distinguishability - and noticed that such particles had dramatically fewer distinguishable microstates than they would if they were distinguishable. This, of course, has dramatic consequences for the statistical physics of systems constituted of these particles, which are now known as Bosons in his honour. Among the predictions that follow from postulating the indistinguishability of particles is that in the low-temperature limit, the velocity distribution diverges from the more familiar maxwell-boltzmann distribution. The threshold here can be thought of as the point where the intrinsic wavelike nature of particles becomes pronounced enough that the wavepackets of neighbouring particles begin to overlap, heralding a regime where the particle picture breaks down. Explicitly, Louis de Broglie's postulated that the relationship of momentum and wavelength of photons, \(\lambda_{dB} = h/p\), was exactly true for all particles. The reason we do not see particles interfere at everyday scales is that the so-called de Broglie wavelegth is smaller than the particles themselves. Taken in concert with the equipartition theorem, one can assign the (mean?) de Broglie wavelength of particles in a gas of temperature T, 

	\[\lambda_{T} = \frac{\hbar}{\sqrt{2\pi m k_B T}}\],

	and in three dimensions one can therefore ascribe a the particles a'quantum volume' of \(\lambda_T^3\). For a gas of density $n$, the volume per particle is $1/n$. From this argument, the quantum nature of gas particles cannot be ignored when \(\lambda_T^3 \approx 1/n\), or when \(n\lambda_T^3\approx 1\). The latter quantity is called the phase space density, referring to the concentration of the likely atomic states into a small region of phase space, consisting of the position-momentum conjugate variables (footnote: Phase space is not just x/p but could refer to any set of conjugate variables, mathematically speaking). Below this point, the distinguishability of particles becomes crucially important. 

	In the case of indistinguishable particles, at a given temperature the probability that a single particle will occupy a given state of energy E is given by the Bose-Einstein distribution. Another way to read this is the number of particles that occupy a given state, on average, is given by the BE statistics. Remarkably, as the temperature vanishes, the population of particles falls overwhelmingly into the lowest-energy state. The temperature at which a macroscopic fraction of the atoms occupy the ground state simultaneously is called the critical temperature, and coincides with the temperature given above. This heralds the phase transition from a 'normal' gas to quantum degenerate matter, or Bose-Einstein condensation.

	More formally, the critical temperature depends on the spectrum of the Hamiltonian, which must have a local minimum to allow for bound states. In this thesis, all experiments are performed in a magnetic trap which is described by a harmonic oscillator potential 

	\[V = \sum_i\frac{m\omega_{x_i} x_{i}^2}{2}\]

	for which the critical temperature for condensation is 
	\[k_B T_c = \hbar\omega_{ho} = \left(\N/\zeta(3)\right)^{1/3} = 0.94 \hbar\omega_{ho}N^{1/3}\],
	where \(\omega_{ho} = (\omega_x\omega_y\omega_z)^{1/3}\) is the geometric oscillator frequency and \(\zeta\) is the Riemann zeta function. The fraction of particles in the ground state, or the condnesate fraction, is given by 

	\[\frac{N_0}{N} = 1-\left(\frac{T}{T_c}\right)^3\] 

	when the gas is below the critical temperature. For the traps used in experiments in this thesis, the critical temperature is VERY LOW and the temperatures we reach are generally EVEN LOWER, producing condensate fractions about 95 per cent. 

	Condensation is a bona fide phase transition. The associated order parameter is sometimes known as the *mean field* and is defined as a complex parameter \(\sqrt{n_0(r)}e^{i\theta(r)}\), where $n$ and $\theta$ are the (potentially inhomogenous) ground state density and local phase of the macroscopic wavefunction. The imaginary part of the order parameter is nonzero probably because of stimulated scattering or something, so you wind up with constructively interfering particles. I guess. Either way, in this sense the BEC displays coherence at macroscopic scales - admittedly most condensates are only a few tens of microns across, but during our experiments they expand in freefall to an ellipsoidal volume of XXX - I wonder what the largest coherent volume is otherwise? How big is the biggest superconductor? Hm, I guess the magnets at CERN have us beat. 

	Macroscopic coherence is also manifest as off-diagonal long range order in the density matrix, as described by Penrose and Onsager (and leading to their definition of condensation in terms of the eigenvalues of the density matrix), and also has close analogies with Glauber's theory of optical coherence. Glauber's theory was extended by Sudarshan (?) to matter waves, which are distinct from the photonic case by ???. The theory of coherence makes predictions about the arrival-time correlations and distinguishes the g(2) function of the condensate (FUNCTION) from the thermal state (FUNCTION). These predictions were borne out by early experiments with metastable Helium, conducted in this laboratory using the same machine described in this thesis. For these reasons, the BEC is often referred to as a coherent state of matter, and the resulting pulses of atomic matter waves are called atom lasers in analogy with the coherent light sources, or lasers. 

	This, along with the various analogies between the optical propagator (the Huygens' equation) and the quantum mechanical one (the Schrodinger equation?), especially in the advent of techniques for reflection and dispersion of the momentum of coherent matter waves, led to the emergence of the term *atom optics*, and heralded a slew of experiments with matter waves that demonstrated the equivalence of optical and atomic systems, including matter wave interferometers and foundational experiments like Wheeler's delayed choice experiment. A distinguishing feature of atoms from light is that the atoms have intrinsic rest mass, and hence interact with each other gravitationally. This  is the root of ongoing experimental campaigns to harness this distinguishing feature for applications such as gravimetry, and also to probe the interface of quantum mechanics and gravity, a central outstanding problem in modern physics.


	

## Diagnostics & detection	
	Fluorescence
		Theory, some example plots
			Why the extension of lifetime? Off-resonant scattering rate lowered eh, plot curve vs wavelength?
		Calculation of population from signal
			Precision
	Absorption imaging
		Theory
		Sure, it's a momentum measurement, but let's calculate its limits
			Limited resolution and sensitivity - make some reasonable assumptions
		There is also fluorescence imaging in gas microscopes but we don't have the optics for this
	Delay-line detector
		System diagram
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
	Monitoring
		AI importing, intensity & SFP checks, WM lock check...
		Camera/mirror setup 
			Reproducibility issues