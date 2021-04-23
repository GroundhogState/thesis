# 2021-02-22

Technical introduction revisions
	Theory
		Atomic structure
			[] No longer hydrogenic -> Means we can still use them as a basis, and for the purposes of metastable state we can still think of hydrogenic orbitals quite well
			[] Clarify introduction of hydrogenlike orbitals - they are used to label energy states and to discuss transitions. 
			[] Why the spllitting of excited wfns? phase difference -> Different overlap, can find by putting into H, even without a functional form?
			[] Put level scheme diagram into atomic structure section
			[] Citations for series expansions, flag in last sentence reasons for dropping 1s term are discussed in next section
		Atoms and electromagnetic fields
			[] Heavy editing of this section required - start with atomic state (density matrix) and add electric field, then talk about transitions/spontaneous emission, dipole matrix coupling and polz dependence, then scattering and dipole forces, polarizability
			[] In Zeeman section, make plots of some He level splitting for studied transitions and the associated spectrum
			[] Dipole traps section -> Creation of BEC
			[] Better discussion of Stokes calculus or bin it, but useful for polarizability discussion and (maybe) compact notation re: atom-light state coupling
		Interactions between atoms
			[] Content complete but editing needed
		[] Consider breaking helium discussion out into separate section here
			may require He history, but could also go in introduction for simplicity of execution
			[] Surface ejection of eletrons are a two-step process; first the excited electron tunnels into a vacant state above the Fermi energy in the surface, and an electron from the metal tunnels into the hole state of the resulting ion, along with an excitation of a second electron which can be ejected from the surface \cite{Hotop H 1996 Detection of metastable atoms and molecules, in Atomic, Molecular, and Optical phyics: Atoms and Molecules, edited by F B Dunning and R G Hulet 191-215, doi:10.1016/s0076-695x(08)60793-0, and refs therein}
		Bose-Einstein condensation in dilute cases
			[] Heavy edits - just a disorganized pile of math right now
				Think: What are the key points you want to communicate here, and what is the minimum necessary background to put them together?
				Some plots: Critical temperature shifts, density-dependend effects, etc?
			[] Interaction-induced stuff (inc Thomas-Fermi and T_c shifts_  into effects of interactions) - or rename section 'collective effects'
			[] Bogoliubov dispersion plot, density dependence
		Creation of Bose-Einstein condensates
			Not content-complete at all
			[] Build back upon f_scatt, f_dipole part
			[] MOT, ZS, evap diagram
				Read: making probing understanding
	Experimental infrastructure
		[] Clarify structure of chapter - atm mostly describes downstairs machine, but includes AOM stuff from downstairs - note that it's included here for structural similarity and also because it's the one you actually built, relevant to chap X but shown here for completeness - what to do with the distinction between beamlines part?
		[] Get pictures, pressures, sequence timings from lab - tuesday night?
		Helium beamline
			[] Citations for ANU infrastructure pubs and their key primary refs
			[] BiQUIC coil diagram - field plots?
			[] Correct He source diagram
		Light sources
			[] Read Shin thesis for important info about main laser, lock system diagram if necessary
			[] Correct labels in cooling distro setup, add component labels
			[] Add single-beam level descriptions? probably just fine to make general statement and summarize in table
			[] MATLAB lock for spec laser
			[] Explain calibration system more carefully, esp in figure caption
			[] add 'to science chamber' in figure, tidy lines
		Detection of metastable helium atoms
			[] Consider moving ion detection part to earlier discussion of Penning ionization, focus on MCP-DLD and then introduce other sensors in lattice chapter
			[] Still need to include saturated fluorescence somehow
			[] MCP system diagram
			[] Atom laser part needs a bit of editing, plus a diagrams re ellipsoidal targeting and Fourier broadening, example plots (eg 'rabi' plot, )
			[] More detailed captions in each of MCP readout figures
			[] Additional diagram of PAL decay (From spectroscopy responses)
			[] Solving for (txy)->v transform
		Vacuum system integration
			[] Bake log pressure diagram
				[] Consider moving bakes etc down  to lattice section as that's where I actually build the system, in this section just flag the pumps and pressures, integration diagram
		Data acquisition & Control
			[] Fill in figure caption, show more of the captured diagnostics from this run? Or spectroscopy, that made more use of the analog logs

Stages of done-ness
	1: Content completion
	2: Edit 1: Concept ordering
	3: Edit 2: Self-consistent
	4: Edit 3: Integrated
	5: Citations and figures

# 2021-02-02

Who'd have thought I'd still be making additions to this logfile?

Well, I wouldn't be were it nor for having misplaced my little green journal. So this will suffice.
The point of this inquiry is to figure out a gameplan for the rest of the introduction chapter. I have how many days?
Thirteen days! Wow OK that is not as much as I thought. Let's make a comparison to the section headings. This gives us a sense of the number that need to be finished per day, on average. It's probably quite a lot.
Tallying them all up: 32. Thirty. Two. There are going to be ways to cut this down, but something has become clear: There is no room for the 'nice-to-haves' at this point. For sure, some of these sections will come together faster than others, but this comes down to more than two sections PER DAY, starting TODAY. One could well start at the top, but there are some that will be 'easier wins' and require much less detail and effort. 
For example: Ion detection, scattering, metastable helium background... 
Instead, let's try two things. One, reduce the redundancy, esp. in cooling and trapping, leave Contact discussion to the QD chapter, ditto collective excitations.
Done. That's not actuall too large a saving; we're down to 28. So let's identify the hardest
* Optical distribution systems will be hard if the diagrams are detailed cf Rispoli. They will be better if using Dutch-style ones, which are good to start. Let's leave the diagrams for later in the process so we can more accurately budget time.
* Atom lasers may be time consuming as I will need to look for more recent works using them (see BCR lit rev). 
* At the face of it nothing stands out as being especially harder than the others, except the laser systems for which I don't already have diagrams. It could be two days' work to get the diagrams done, let's account for that. Two and a half for safety margin. Then that's 11 calendar days, minus two or three for weekend activities, that's *eight* days. Back to three sections per day. Fuck, ok. 
Today, some 'easy' ones:
	* Scattering, penning ionization, and associated studies. 


# 2019-12-15

Bootcamp day 3. Things going ok. Still managing to find more words to plop out.

Taking Inger's advice and taking some stock of things I've been putting off talking about with supervisors:
## Things to talk to supervisors about
	* Content: Some expts (particularly the transitions) sorta feel like a sham. Bad scientific practise. This salesmanship feels dishonest, makes it hard to maintain motivation. There was no valuable contribution.
	* Didn't solve any interesting problems because of personal capacity of time to give - so in some senses a bit ashamed of the thesis in many levels, so far from goal/useful
	* What other writing blocks do I have? Obvs feeling like there are more crucial/urgent issues to work on outside of physics - feels like I had one good shot at something, missed, and now to pursue it would be counter to my values so there is a sense of loss here.
	* Exactly what goes in? For example, Kieran's derivation of the TO equation or Bryce's work on the fitting - they're essential to the project, so how much goes in? Should I make a full recount and then include a pre/post-amble about who contributed what to the project? 
	* What to include about the lattice?
	* why can't I shake the feeling that you just exploited my labour - the independence I've gained is almost despite you rather than because of you

1300-1400
	Basically nothing written. Fiddled with a few words. Growing discontent again. Considering the prospect that this would not be possible to put through, that it doesn't demonstrate sufficient work/smarts/number of problems solved in interesting/useful ways, just doing it for credibility & unlocking 'next thing' which might be all too late anyway, at least I feel a little proud of the effort/resilience expended but this hasn't seen me 'go rogue' in much sense, this is not hte physics i thought I wanted, this feels like staring at a wall, I'm blocked by something and maybe it's a ltitle too much coffee, maybe it's writing fatigue, maybe I overate, maybe I am genuinely running out of stuff to say in the thesis context, maybe need to read more, this was going to happen eventually but as soon as the flow state stops then the ugly head of self-doubt and self-criticism rears its head again. If I imagine speaking to myself, as another person say, what would I say? Mate you got ripped off for a couple of years then scraped through with a wooden fucking spoon no? Like this thesis is some kind of fucking consolation prize - of no consequence or use, I'll never be a cold atom physicist and I'll probably look back on the qualification as a silver fucking lining. Wow. I don't know whether this is anger or just exasperation. I'm dragging my feet it seems, petulantly whining about how its' not what I want it to be but there are real questions here about scientific integrity and intellectual honesty. I fell victim to a play by people who are good at the game but who share neither the curiosity nor the vision that I hoped to learn from. So what's left to learn here? Well, some quant methods, sure. I'll always be comparing myself to the leader and feeling like I'm falling behind. There

	Fuck this. I don't think I should keep ranting forever, go outside man this is beyond uncomfortable this is probably seriously counterproductive. Get some fresh air.
	

# 2019-12-12
Fleshed out Excel planner on ride home from ANZCOP
	Overview sheet, segment sheets, word tracker
	