# Introduction
1	Overview	Acknowledgements	
		Thesis structure	
			Layout 
			narrative,
			Audience
				The introduction is supposed to be readable by my parents!
			Scales
		Historical perspective	
			Democritus

				Ok so somewhere in here I wax lyrical. We tend to try to understand things. Why? Well. There is something advantageuos about being able to make predictions bout the world. This is something that has enhanced our survival prospects. But in humans something seems to be running on overdrive. And, sure, this isn't really relevant to the thesis, but you want to start from somewhere that naturally lreads to a framing of atomic theory. 
				Matter is inescapable. Except perhaps in the dream state - we are surrounded by substance. Some two or so thousand years ago, Democritus posited that there was a smallest thing. That one could break mountains down into boulders, boulders down to stones, stones to sand, and sand... To something indivisible. He called them, literally, atomos, for indivisible. This was astoundingly prescient: The atomic theory, as it came to be known, would not find empirical validation for another millenia or so. And, like all theories that prove to be correct, it too reached its point of failure a few hundred years thereafter. The atomic theory was outlandish at the time, breaking with the notion that things were ultimately continuous. The exploration of the atomic world eventualyl yielded a new kind of understanding of everyday matter. 
			Kinetic theory of gases, thermodynamics,  'absolute zero'

				The first profound successes were had with gases, laying the foundations for thermodynamics and the understanding of the extraction of energy from storage in chemical bonds, via heating a working fluid, say - and powering the steam revolution. Among the findings of the kinetic theory of gases was what later became known as an equation of state - an apparently universal relationship between macroscopic quantities - pressure, temperature, volume, and mass - expressing the balance of energy in gases. Among the findings that stem from this understanding was the notion of an absolute temperature scale: That if one could extract enough energy from a gas, by cooling it, then its internal energy would vanish. It would have no volume. It would be motionless. This prediction predated Einstein's formulation of the mass-energy equivalence, but even at the time, it was appreciated that gas molecules had to have a size. So they could not vanish simply by getting colder. This paradox took some years to resolve, and it was only possible by completely overturning the picture of the atom. While understanding thus far had stemmed from the investigation of matter, the first quantum revolution was to come from the study of light.
			Spectra & old quantum theory

				Spectra are typically obtained by taking a beam of light - say, from a pinhole or slit in a mask - and passing it through a medium, such as glass, which disperses the light according to its colour. In modern parlance, there is a difference between the momentum (direction of travel) of light with different energies (related to frequency). It was by WHO? that spectra were first resolved with enough detail to distinguish more or less intense lines against an apparent continuum. And in particular, that pure elemental sources created different colours. A standard prism and screen would show different results with different elements. Wait - but by this point, we must have had an understanding of electrons, right? Because there was this Bohr model, where the electrons were orbiting the nucleus. And there was an understanding that moving charges radiated light - this was post-Maxwell, surely. Better go revise that history. So the upshot I guess would be that, anyway, there was a finding that the lines of light - oh also, the photoelectric effect which predicts that light are particles and have energy proportional to their wavelength, hey. So, this is how people worked out the energy gaps between the internal states of atoms that were later found to be related to inverse ratios of square integers: That led to the positing of a classical model, with a 1/r potential, that was inspired by the knowledge that potential energy fell off like 1/r^2. But did we get this backwards? Would have to revise the classical mechanics too, yikes. But yeah. The wise thing to do would be to talk angular momentum, and then from spectra we introduce Planck's idea of supposing that it *comes in units*. And then we add in the postulate of de broglie - where was this first verified? - and the double slit experiment, then the whole world turns just about on its head. And so was born the old quantum theory. Or something like that, go read Born and that Disney book for starters.
			Modern QM, QFT?
				Presumably there will need to be some historical preamble, but the idea is now that we lay out the foundational pieces of quantum theory as we now understand it, or at least as it will be used in this thesis. This includes, and perhaps is motivated by an example, leading to a small exegesis of the thesis
					Hilbert spaces and quantum states
					Probability amplitudes
					Operators and observables
					Time evolution
					Composite systems
					Density matrices
					Interactions
					Correlations & Entanglement
				And a survey of the present state:
					Formulation of QED
						Lamb shift, Rydberg constant, etc etc?
					Extension to QFT
					Experimental successes
					Extension to condensed matter
					What's after the standard model? Unifying HEP/condensed matter/QI? Following the math doesn't seem to have worked for SUSY (and so one might take this as a cautionary tale for Everrett).
			Quantum technology
				Things that have changed the world
					Electronics
					Lasers
					NMR
				Nascent technologies
					Quantum optics
					Quantum information
					Quantum computing
				Ultracold atoms	
					A brief history
						Cooling and trapping - who, when, why?
						BEC - a complete surprise and experimental triumph

					Ultracold metrology
					Ultracold many-body physics

				A critical eye
				
					Technology evidently brings us great things. But let us not lose sight of the implicit 'right to know' - that we still embody the notion of a conquest over nature, of mastery of the other, the greater, the ultimately incomprehensible. Let us not fall victim to our own arrogances, and recall that in our turbulent times, our investigations come at cost. The nature of reality will, according to our ultimate foundations, remain. But the conditions of society in which we have the ability to pursue them are not guaranteed. One can never predict the outcomes of discoveries, or what miraculous things may be born of new technologies, but in the problem of allocating compute power from human wetware - which still retains a certain je ne sais quois that has not been replicated by industrial-scale algorithms running in silico - we should be mindful of the hubris of 

2	Getting to the ground state	
		Tabula rasa: Vaccum system	
			Why vacuum?
				Physical models often make simplifying assumptions, like ignoring air resistance or friction, or collisions etc. Idealized models are only solvable in certain special cases, and introducing nonlinear effects like friction can make them mathematically intractable. This is partially resolved by sophisticated modelling these days, but the approximations will always remain. So when it came to studying microscopic systems, one would like to remove the background. so that the thing you are examining becomes not only the foreground, but the only thing in the image, and so your signal is not obfuscated. So people have tried to make vacuum for quite some time! Indeed this is one way atmospheric pressure was measured - Lavoisier used pumps from teh fire station to evacuate a chamber, and since then vacuum has advanced considerably. Vacuum manufacture is a massive industry now, and I wonder if I could find a history of vacuum pressures over time to track the best known vacua. In the case of ultracold atoms, one needs to maintain a vacuum because the forces that hold the atoms in their optical or magnetic traps are so frail that capturing particles from the atmosphere would be all but impossible - what fraction would have sufficiently low energy to capture, and how long would they last? So, yeah, yuo need vacuum, and the lighter your atoms, the more worried you should be about vacuum. It also provided benefits like making sure lines stay narrow to mitigate pressure broadening et cetera - trapping atoms in vacuum is in some sense the ideal tool for the physicist - to study things in almost perfect isolation, to extricate the subject of study with complete mastery over its environment. But nature abhors a vacuum, and so will find ways to ruin your day. So there are a ton of ways to get a chamber close to empty. Let's talk about a few of them. 
			Producing vacuum: Pumps, bakes, NEGs, etc
			Chamber architectures
			Scales: Limits to vacuum

		Cooling and trapping	
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

		Diagnostics & detection	
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

		Laser systems	
			ECDL: Generation & Locking 
				System diagram
				How dither locking works
				Experiment insertion
					Lattice build described in lattice chapter, stick to downstairs architecture to begin with
			TiS: Generation & locking
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
				Trap frequency method


