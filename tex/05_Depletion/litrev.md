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


	
============

Interactions between particles are a fact of life that theory must
confront in attempts to phenomena. Modern experimental techniques allow
access to a large range of interaction strengths, sometimes within
otherwise identical systems. For example, optical lattices or Feshbach
resonances can be used to tune interaction parameters between extreme
values, from the so-called strongly correlated regime (of great interest
in itself) to extremely weak or even interaction-free (?) regimes. A
common element in many of these experiments is the use of Bose-Einstein
condensates (BECs) or degenerate Fermi gases as test systems for
theoretical descriptions of interacting gases.

The criterion for condensation is, roughly speaking, when most of the
particles in a dilute bosonic gas occupy the same quantum state. More
formally this is captured by the Penrose-Onsager criterion, wherein a
homogeneous gas is said to be condensed if there is a macroscopic
population of the ground-state eigenvalue of the ensemble density
matrix. Any particles not in the ground state are said to be part of the
depleted fraction. The depletion of the condensate is comprised of two
parts, the thermal depletion and the quantum depletion. The thermal
depletion is an artefact of the finite temperature of the condensate and
has a number distribution described by Bose-Einstein statistics. The
quantum depletion is a consequence of particle interactions/quantum
fluctuations?

What is quantum depletion? Why is quantum depletion interesting? What is
the state of current knowledge? What does this paper contribute? How did
we make our measurements? How do we interpret the results in context of
current research? What else should we measure to further understand?

Equilibration time scales
https://www.sciencedirect.com/science/article/pii/S037843710201350X
homogeneous trap https://arxiv.org/pdf/1607.06939.pdf !!
https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.77.5315
https://journals.aps.org/pra/pdf/10.1103/PhysRevA.54.R1753

estimating correlations

https://arxiv.org/pdf/astro-ph/0310831.pdf
https://arxiv.org/abs/1305.4613

Interacting BEC in harmonic trap =\> Penrose criterion not valid
Instead, depleted (/excited) fraction and condensate fraction coexist
Two different momentum density profiles, depletion driven by collision?

Applicability of Bogoliubov theory in optical lattices
https://www.nature.com/articles/nphys1476

From [@Makotyn]:
================

Strongly-interacting systems like neutron stars and High-T
superconductors are cool. Liquid Helium was the first discovered but
hard to probe, so ultracold gases have stepped up instead.

This paper did not observe the expected $k^{-4}$ tail, which would be
expected to arise from two-body short-range interactions. The amplitude
of this tail is the parameter known as the contact (ref 33); they do
concede the tail may exist below their sensitivity as their SNR is bad
at high momentum. The unitary experimental conditions might also lead to
three-body interactions affecting the tails.

Check: Did they observe in-trap or after release?

From [@PSText]:
===============

Quantum depletion in a harmonic trap given by
$$\frac{\delta N}{N_0} = \frac{5\sqrt{\pi}}{8} \sqrt{a^3 n(0)}$$ Which
is fixed by the gas parameter (number density) in the centre of the
trap. This conflicts with the result quoted below!

From [@Muller]:
===============

The authors explicitly compute the quantum depletion contribution to the
momentum distribution in external potentials. The so-called 'potential
depletion' is a small correction to the homogeneous depletion. The
Penrose-Onsager criterion is only relevant for homogeneous condensates,
hence this paper's use of Bogoliubov theory to determine the one-body
density matrix. This means writing the atom field as a mean-field plus
perturbation, which gives another criterion for condensation in
non-homogeneous condensates. The momentum distribution similarly splits
into
$n_\textbf{k} = |\Phi_{\textbf{k}}|^2 + \langle \delta \Psi_\textbf{k}^\dagger \delta \Psi_\textbf{k}\rangle = n_{c\textbf{k}} + \delta n_\textbf{k}$,
contributions from the condensed and non-condensed fraction
respectively. In section 4 of the paper, the quantum depletion is
computed. The authors note that, as shown here, the population of the
zero-momentum state is not a good indicator of BEC in homogeneous
systems. That is, the number of particles in a nonzero momentum state is
NOT a measure of the depletion; the integral of the momentum
fluctuations about the mean-field, however, is.

Quantum depletion of the condensate
-----------------------------------

The quantum depletion is a finite non-condensed fraction at zero
temperature, arising from quantum fluctuations around the mean-field
approximation to the condensate. The deformation of the condensate by
the mean-field term in the GP equation does not lead to depletion. The
authors comment that the depleted fraction may be *less*, and not *more*
quantum than the condensate. Nonetheless: the depletion that follows is
the quantum depletion as opposed to the thermal depletion: It is given
by integrating the momentum fluctuations
$$\delta n = L^{-d} \sum_{\textbf{k}} \delta n_{\textbf{k}}$$

The Bogoliubov approximation is justified whenever $n a_{s}^3$ is small,
i.e. low density or weak scattering, when the depleted fraction is
small. In this case, in three dimensions, the depleted fraction is
$8(n a_s ^3)^{1/2} / 3 \pi^{1/2}$ in terms of the s-wave scattering
length, or $n\xi^d >>1$, with the healing
length$\xi = \hbar/\sqrt{2mgn_c}$ and $g=4\pi \hbar^2 a_s/m$.

The potential depletion turns out to be (small and) proportional to the
homegenous depletion. The most relevant result here is the depleted
fraction expression given above - there are no results given for
potential depletion in a harmonic trap, although one could use their
methods to compute this.

N.B. This paper also computes the momentum distribution and depletion of
a condensate in a lattice, of interest to the upstairs experiment.

From [@Sirjean]:
================

The authors find that the ionization rate is almost solely responsible
for the decay of the confined condensate. They characterize the two- and
three-body contributions to the ionization loss rate, and find that
quantum depletion makes a significant contribution to the three-body
rate. The two- and three-body rates should be proportional to $a^2$ and
$a^3$ respectively. The two-body rate they found was well-fitted for the
by a quadratic, but the three-body rate was found to be
$L\approx L_{20} (\frac{a}{20})^3 (1-0.21\frac{a-20}{20})$, where they
assumed $a=20$nm (wrong), and it's not clear what the subscript 20 on
the L means. This paragraph is quite vague and has no citations, but if
correct suggests quantum depletion matters to collision rates. Their
fitted rates for two- and three-body collisions are of order 10E-14
cm$^3$/sec and 10E-26 cm$^6$/sec respectively. They state that their
assumed detector efficiency means a=10nm would require additional loss
mechanisms for half the losses, or imply an overestimate of the detector
efficiency. They quote an estimated 40%! So given the recent
measurements of scattering length, that seems very likely. (then again
they were detecting ions, not neutral atoms)

The atom number was measured by MCP. To avoid saturation, they lower the
MCP gain and record the signal in analog mode with a 400$\mu s$ time
constant. They also leave their RF knife on at the end of a sequence and
maintain a very low thermal fraction.

From [@Lopes]:
==============

The authors measure quantum depletion in a homogeneous condensate. By
using a Feshbach resonance to tune the interactions, they are able to
control the depleted fraction. They measure the condensed fraction by
Bragg momentum spectroscopy. The results are qualitatively similar to
theory, however the theory at T=0 predicts lower quantum depletion than
was observed at finite temperatures. The thermal depletion also
populates the high-momentum tails and is not scattered out by the Bragg
process Their measurements are consistent with a small nonzero
temperature, consistent with their trap depth but they do not quote
doing actual thermometry. 15% and 20% statistical and systematic error.

In theory referenced, depletion of a homogeneous condensate is found to
be proportional to $\sqrt{na^3}$ and valid for $na^3<\approx 10^-3$.
Refs 15-17 measure depletion by using lattices to increase interactions,
and through expansion of dilute gas in 18 (i.e. the paper we are
concerned with)

Authors use K-39 BEC and separate the BEC from high-momentum components
by Bragg two-photon process. Demonstrated dependence on scattering
length by Feshbach resonance and showed that depleted fraction depends
(reversibly) on scattering length.

See refs 8, 9, for a connection to superconducitivity, superfluidity and
condensation. Side note: Connection of superfluidity to BEC was proposed
by Londin and Tisza.

From [@Qu]:
===========

Theoretical study of time dependence of density and momentum
distribution of expanding gases, includding Bose case. They show that
the $k^{-4}$ tal vanishes for large expansion times, in conflict with
the work of Chang et al.

Suggestive links between short-range wavefunction behaviour and
thermodynamics via Tan contact (ref 1-7). Ref 1 for Tan defn. Ref 11-12,
measure momentum tail after expansion by tuning out interactions.

Claim: Momentum distribution affected by interactions during expansion,
which is expected from the ballistic relation given the momentum
distribution. Expansion dynamics of momenta smaller than the inverse
healing length are well studied (by scaling relations or hydrodynamic
approx) but higher momentum not so. Section II and the conclusion are
the only interesting parts.

Many-body interacting systems b) weakly repulsive Bose gas
----------------------------------------------------------

The contact evolves as
$C(t) = \int d\textbf{r} (16\pi ^2 \rho^2(\textbf{r},t)a^2)$ where $a$
is the s-wave scattering length and the integrand is the local contact
density at equilibrium (from Bogoliubov theory). They use the scaling
transformation from hydrodynamic theory to examine the evolution of the
contact, which shows it decays with $C_0 /(\omega{ho} t)^3$, where $C_0$
is the initial contact. They open their argument with "The adiabatic
ansatz is expected to hold" - seems dodgy.

The fourth-power tail is observed in the section on Fermi gases, but is
ruled out by arguing that it implies infrared divergence. (Recall
Stringari comment - you have a natural cutoff which prevents this? But
this is in thermodynamic limit maybe?) - the fourth-power tail also
vanishes explicitly in the two-body case, but there's no strong result
here!