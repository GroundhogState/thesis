# Many-body physics
	Section introduction	
		Statistical physics	
		Phase transitions	
			Thermal, quantum, dynamical, computable, semantic
		Emergent complexity	
5	Quantum depletion	
			Section intro 	
			BEC detail
				Bose einstein condensates are like really cool. 
				BEC was predictedby Bose then translated by Einstein but there's some historical controversy here.
				BEC is predicted by lookig at BE statistics and taking the temp to zero.
				This means that you get lots of bosons in the ground state - wow, loo kat that, they're all doing the same thing!
				BEC is actually a measure of disorder versus distinguishability maybe? Like you could condense at a higher temperature if the gap is really big.
				BEC is a coherent state and connected intimately to superfluidity - the superfluid part of a SF 
				BEC is actually, in practise, dependent on interactions between atoms. They need to thermalize as you cool the sample with evaporative cooling, although there are some folks who claim steady-state BEC by optical cooling which doens' t need th atoms to talk to ech other. But anyway, the meanfiled part of the condensate hamiltonian means your single particle states arent eigenstates
			Bogoliubov theory
		 Context & Gap	
			Contact measurements
				Probably about time to write a review paper on experiments, no?
			French disagreement
		Aim & scope	
			To reproduce the Palaiseau experiment
		Contribution	
			They were wrong. TBD just how wrong.
		Issues	
			Sys: Background
			Stat: Fitting power laws, weak signals
		Method	
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
		What next?	
			I guess it depends a bit on what the findings are, if any, from the correlation study. LIke, does it agree with theory, with the fit, or neither? What's going on here?
			Bragg spectroscopy?
		Link to next chapter	

6	Optical lattice	Section intro 	
			Strong interactions
			Simulation paradigms
			Implications for church turing?
			State of optical lattices

			The previous chapter would have dealt with the case where interactions between atoms were present but weak, and so were amenable to solution by perturbative or approximate methods. This means taking a solution for non-interacting systems and making small corrections. The information about the microscopic behaviour can in some sense be averaged out, or accounted for in aggregate, producing a simpler picture that can be mathematically more tractable. There are many instances where the solvability of models is no longer guaranteed even approximately. These so-called strongly correlated systems are ones where the actual evolution is completely different from the non-interacting case.

			Philosophica; digression: There is great power in mathematics, in teh ability to produce analytic results for a given model. That is, here is  a set of assumptions about a description of the world, and so I can use this to do smoe efficient computation and predict the future state of the world, or some part of it. Models are paradigmatic in physics for this reason, and they represent a great deal of compression, of abstraction of patterns out of context. In some ways they - mathematical models - could be thought of as the quantitative storytelling part of humanity, the things that make it unique - and so there's something really sublime about the exactness of the correspondence with the world, written extensively about in things like 'the unreasonable effectiveness of mathematics' and this correspondence is still explored in the problems of foundations of QM: what exactly does this mathematics say abotu the nature of the world? Why does it run this way? This deep inquiry will always be part of the human spirit, I think, but yeah.
			So, models are great. But you can only get them somtimes - if the algebra is nice, which is usually the case for simple, linear things, symmetric things, or where we can take the large-N limit as in the case of thermodynamics. But once things get more complex we may not have so-called closed form solutions. So we would need approximate methods. The modern incarnation of this is by algorithmic means - given boundary conditions we can solve DEs which are the foundational tool of physics. For probability distributions, rather than pointlike coordinates or vector evolution, things are more complex. That is, you need to worry about things like stochastic master equations and such which are very computationally expensive for quantum systems. There are analytic approximation methods too, using Feynman diagrams or computational tools inspired by them - but yeah that's way beyond scope here. Suffice to say they work - see LHC - but they're expensive I guess. 

			but the point I guess is that there is a wealth of methods that rely on the in-silico method: A digitized representation of the state of the system with some precision, and a method to evolve the state of the machine.
			THe problem is when you want to express a large - that is, many body and fairly strongly interacting - quantum system, and so the required memory is really big. That is, the state vector is exponentially large in the number of particles, and if you want to store the whole density matrix then things get much worse! And so we need other means. Approximations exist; consider only low-order correlations, for example, like the Gutzwiller methods, or find self-consistent solutions like in Hartree Fock. There are other methods of course - exact diagonalization is the best in the sense that it is, well, exact. And the scaling isn't *too* bad for matrix inversion, and once you're done you're done. The thing is you need the memory to store the matrix and thigns get bad pretty quick. And this is just for simulation of dynamics that evolve under a stationary hamiltionian. TIme-varying stuff is probably a lot worse - quenches are OK to model and correspond to strongly diabatic changes in stuff, but ya. The upshot is that using existing machines to simulate stuff is OK, but really limited. 

			Why is this a problem? Well, large-scale systems are ones we'd like to understand. Superconductors for example. Or big proteins/drugs. Or photosynthesis. So what's the problem? Well, quantum is paradoxically complex; a state vector requires so much infomaiton to describe, but only gives us a sliver of that when we measure it. And nature doesn't seem to have any worries runnign these quantum systems itself. So why not just use these analogies? Use a quantum system to represent a quantum system? You're still faced with the input and output challenge - state preparation is expensive, readout is expensive - but for some processes you mgiht not need big superpositions or massive entangled states, which are much harder to produce (look at some of these scaling results hey), but output is always gonna be an issue I guess. Unless you're really judicious with your output and manage to transform the states you care abotu into ones that are orthogonal in yuor measurement basis I guess. But that's another story.
			The idea is old; back to Feynman in, what, the 80s? So I guess it's not that old and took off really fast! Best to get a date on that one.

			So the posterchild for this kind of solution is the general quantum computer - one who can initialize a many-body quantum system in the ground state, then apply arbitrary unitary operations to it. This could include simulating time evolution or by using the quantum state vector as a superposition of computing states, to run calculations. So this would be more like quantum logic. In the end it's all the same. But building an arbitrary hamiltonian is beyond us rn. Fortunately it turns out that all you need is to be able to generate a basis of the lie algebra of transformations that you could peform. And some smart buggers proved that for large quanutm states you can do it with a universal gate set - for universal digital quantum computing at least, which is capable of enacting any unitary operation, and so this includes time evolution of quantum systems. I wuold like to check the equivalen t for time evolution - trotterization isn't quite this, as it boils down to some fairly complicated stuff. There's a whole swath of computing architecture out there right now, and several compilers that will take an operation and break it down into the gate set, so you can just write out your inifinitesimal unitary and go for gold. But yeah, approximation errors. So i think this cahpter needs a lot more focus. And I would like to better understand the problem classes that are within simulation - it's not quite the same as the complexity classes, I guess, but i wonder if you could phrase them as SAT problems if you're trying to make predictions? Tough to generalize exactly what people look for.

			Alternatively, well, quantum simulation. Thatis, analogue simulation. Thisidea is a bit less sophisticated than full quantum computing but turns out that there's a map the other way for example some lattice models ahve been shown to be universal, which means that for special choices of the coupling constants one can actualyl get full universal computation - simulating a digital quantum comptuer. Of course this is a completely other technical challenge, requires ptoentially long-range coupling, so your hardware gets really tricky especially for long-range entangling operations, et cetera. So yeah, not super easy. But in the case of specific problems, well, you might nnot do so badly. I wodner if you can scale problems from interacting graphs to equally-coupled models with on-site potential variations. Seems hard, as you'd rapidly increase the number of atoms yuo need, and probably some bizarre modulation on the lattce depth but something worth having a bit of a think about wen writing this chapter anyways. So yeah. Uhm. Im supposed to be writnig abotu quantum simulation; the analogy bbeing a wind tunnel, say, rather than building a digital sim. That said, now the task is usually done extensively in silico because it's *faster* and also because it's usually *cheaper* - human time is still expensive when you could use -perhaps more- energy in silico for suepr cheap thanks to the economies of scale. Of course, it's not clear when QCs will reach this kind of scaling,a s they need to be error-corrected which is not currently possible at any kind of practical sense, but it's still something people will shoot for. And actually this underscores the issues or the advantage of runniing quantum simulation ebcause well, yeah, there is noise, but for some kinds of noise one hopes that the contribution is someqhat gaussian, right? So you're still gonna try to monte-carlo your way aruond, except you're sampling from physical analogs. The first example of this was Greiner & Bloch, good on 'em. the idea was pitched by Zoller. IDK why they didn't go straight for fermions, but thats' how it went. This would be a good thing to cehck out, the historical reasons. And the key papers therein I guess. but why? For the sake of a good read, and well, yeah, they're kind of the seminal papers in the field! So best go get 'em. 
			Sho wat comes next? Um. I was on the tangetn about analog simulators, so there would be space for a survey of the field here. Starting without too much delving into specific models, but that would be a good look at the best in the world, or the first - various lattice geometries, magnetic lattices (how they doing?)
			And quantum gas microscopes - but then hey look ma, as we talked about in earlier chapters, they're not able to resolve single-bdoy momentum spectra. So this is why we would care about using BEC of He* - currently the best way to do this at scale. Some people have done few-fermion correlators recently (See the thermal correlator/dipolar fermion paper is it?) - but this would be really hard to scale, right? I wonder what the limitations are here. Or could you use a kind of torque to take longitudinal momentum into a lattice-free potential? LIke, use a different dimension of a 2D lattice for this.
			It's also worth talking about the state of the art of QMC - people have done 3D bose hubbard right, and done exceptionally well. DOes this sort of shoot the project in the foot? I wodner. Something to check out.
			BUt then yeah we get to talk a bit about the Bose HUbbard model.


		Gap	
			[If I don't get to it in the previous chapter re: Bogoliubov and quasiparticles, thsi woul dbe a good plcae to dig into why we would care about momenum correlations. ]. But then yea some extra goodies might be lifted/inspired by the french papers...
				1-body momentum measurements in optical lattices
				He*: start with bosons
			Bose-hubbard model
				Consdier a 2-well example; look at the quantum phase transition. Then what. Well, how abotu the 2-body momentum spectrum for BH coupled wells, huh? That'd be a nice illustration. There's probably room to talk about these as arrys of josephson junctions - a good chance to try and understand those if you want to. BUt that'd be an optional part I guess. Part of the survey. Maybe worth tracking down some of hte theses from the Greiner & Bloch labs. 
		Aim & scope	
			To build the dang lattice
		Contribution	
			Vacuum chamber
			Optics build inc dipole
				So when I started, we actually didn't have a working MOT. THere were the optis but they were dirty and eyah. So they didn't have light either. Had to build a few AO arms - everything except the collimator and zeeman slower I think, and the ZS was set up according to the old paper about that lab, right? THe 'optimized' one. Altough one could certainly design a chirped system to increase yield, but then I wonder what the density/number limits for a MOT are. How much could we actually obtain, given that we then have to push through the feed hold into another chamber?
				SO yeah. Two MOTs. Anythign exciting to write about? Maybe not - just ballpark the capture velocities maybe. 
				The dipole diagram and control woudl be worth describing. The theory of dipole trapping would belong here as it's not really relevant? Oh, no, I'll have to put it in the alignment chapter - well it realyl sits in the polz part of the tuneout chapter. So that'll cover that I guess. Look over the simulations of the dipole potential. Maybe some simulations of evaporative cooling in the dipole. Open source 'em of course. Would be a fun way to try some auto-optimization algorithms for path optimization. Another way to burn some time, I guess, there are a lot of things in here that are becoming big to-do items! Bu
			Imaging system
				Diagram, some example images and calculation of number
			Sequence up to evap & dipole
			Small simulations
		Progress meanwhile	
			New coils, solder catastrophe, new plates
		Issues/What next	
			Stability: Vibration, temp, vacuum
			Optics: Power, profile
			Automatic optimization
			Broad goals
				Fermions
				Quasirandom lattices
					Are these actually resources or what?
					Next generation laser tech? 
			
7	Conclusion	Revision of key findings		
		Outlook	
		Closing remarks/Afterword
			
