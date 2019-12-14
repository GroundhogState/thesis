# Quantum depletion	
## Section intro 	
## BEC detail
	Bose einstein condensates are like really cool. 
	BEC was predictedby Bose then translated by Einstein but there's some historical controversy here.
	BEC is a coherent state and connected intimately to superfluidity - the superfluid part of a SF 
	BEC is predicted by lookig at BE statistics and taking the temp to zero.
	This means that you get lots of bosons in the ground state - wow, loo kat that, they're all doing the same thing!
	BEC is actually a measure of disorder versus distinguishability maybe? Like you could condense at a higher temperature if the gap is really big.
	BEC in a harmonic trap: Critical temperature, condensate fraction, chemical potential, peak density, thomas-fermi radius, momentum distribution, thermal fraction.
	BEC physics: Nonlinear Schrodinger equation approximated by GPE in the mean-field approximation
	BEC is actually, in practise, dependent on interactions between atoms. They need to thermalize as you cool the sample with evaporative cooling, although there are some folks who claim steady-state BEC by optical cooling which doens' t need th atoms to talk to ech other. But anyway, the meanfiled part of the condensate hamiltonian means your single particle states arent eigenstates
## Context & Gap	
	Bogoliubov theory & superfluidity
	Connecting contact, momentum distributions, and correlations.
	French disagreement
	Contact measurements
		Probably about time to write a review paper on experiments, no?
## Aim & scope	
	To reproduce the Palaiseau experiment.
## Contribution	& discussion.

## Issues	
	Sys: Background
	Stat: Fitting power laws, weak signals
## Method	
Sequence & Calibration stages
	Total number 

		Well this isn't anything new, I just use the pulsed atom laser in the same way as other chapters. Because I care more about number here I'd like to spend a bit of time thinknig about number errors that could crop up here which are perhaps less important to treat than they are in tuneout, which will be a busy chapter in its own right. 
	Raw profiles

		Centering algorithm to align BECs and compile to single shot.
		Create histogram in spherical coordinates.
		Compile and apply calibration corrections. 
		Do some fancy fitting - theory-driven pre guesses
		T from fits and consistnency 
	Trap leakage

		Trap leakage is surely number-dependent. Who knows what the law actually is - there is probably some combination of majorana and ??? - perhaps could ballpark what the leak rate should be, see if it squares with what I observe. But yeah it results in an increased flux rate, you can see it in the time trace. The best way to deal with it would be to extend the hold for ages, and then get heaps of statistics, but in the end I wound up using the 20-odd ms window of hold before drop in each case. This still gets to within ??? some margin of error when using all the data I have for a given run. Given the small count rate it isn;t at all obvious that I would be able to do this shot-for-shot; not sure what type of noise this is. 
	Background

		This one was easy. I just took the dark count rate from everywhere else; make a histogram displaced on the detector, assuming the dark counts and hotspots are time invariant. Are they? Worth a look I guess. But this is just like camera dark-fielding. That could be a great analogy actually! There are three channels, some background, and, well, the leakage but whatever let's sort of ignore that. Let's show it's Poissonian, maybe? Just to show that it really is uncorrelated events?
	Spin mixing

		Well, this one was OK, I just ran the experiment without the transfer. It shows up fine, I used the center found in the AVERAGE (I think) which might be worth looking at - should it be better to use the centre fixed from the proximate shots? idk. Depends on whether there's genuine drift or just jitter in BEC arrival position. Lol, I guess one could do an allan variance of this one also, that would tell you the best period to average across. Actually, yeah that is kind of cool. Perhaps including that much detail in the 'possible improvements' part. The origin of this isn't clear, hey. It is unlikely to be m=1 atoms, honestly, as they would probably be movable with the Z coil after the 'spray'. The spray moment suggests it's something in the fall path that seems to be an issue - one can control a little bit where it impacts by adjusting push coil timigns - but never quite entirely get rid of it. There is also the question of the m=-1 atoms floating around. But then, calibrating for that would involve using a different RF sequence, perhaps, and at the end of the day maybe the best thing to do would be to find a Rabi transfer setup that pushed everything into M=0 anyhow, and see whether the symmetry is a problem there. Something I'd like to do is to drop an entire BEC, center it very carefully and then reflect it in 3D, and subtract histograms. But that's a mini project for another time and might not really demonstrate much. I would need to include at this point an argument to gauge the systematic error, for example by spreading the entire population uniformly or worst-case just in the power law.  Then see how much a difference that woudl make.
	Transfer fraction calibration

		Verification that saturation is not a thing - also kinda pulls out the flux rate wehre saturation is a problem (could do this in 3D, obvs nonlinear but whatever, it's a ballpark)
		Verifies that m=0 halo is not distorted significantly in the transfer process
		Verifies that at least within the thermal part, no k-dependence of transfer
		Model of sweep - would it have been practical to get the max transfer without any momentum-dependences? - what is the doppler shift of the depleted atoms, anyhow? Not to mention the RF field is certainly not spatially coherent hey
		How accurately is this determined? 
	Illustration

		So I will probably include a diagram that shows these broken out - a master diagram of the full measreument stage, for example, and the time profiles that came from each section, and the calibration methods I used... Blah. So this is going to be like a very graphical section, as many of mine will be. 
Processing

	My general dream for these sections is a graph of the program or some kind of systems diagram, maybe nested screenshots or pseudocode would do the trick and then include the code as an appendix hey?

##What next?	
	I guess it depends a bit on what the findings are, if any, from the correlation study. Like, does it agree with theory, with the fit, or neither? What's going on here?
	Bragg spectroscopy?
Link to next chapter