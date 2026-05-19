- Decision: Reject
- Avg Score: 3.60
- Scores: 3, 3, 6, 3, 3
## Summary

This paper proposes SwarMDP, a Swarm Markov Decision Process formulation for distributed Traffic Engineering, and introduces **eleganTE**, a training/evaluation framework built on the ns-3 discrete-event network simulator. The authors argue this is the first formulation meeting six identified requirements for general-purpose routing optimization (timeliness, compatibility, generality, robustness, scalability, realism). They implement MLP and GNN policies trained with PPO and benchmark them against OSPF and EIGRP across hand-crafted and random topologies. The paper's primary contribution is the framework and benchmark infrastructure, not a novel routing algorithm.

---

## Strengths

1. **First unified SwarMDP formulation satisfying all six requirements for general-purpose RO.** The paper formalizes distributed TE as a SwarMDP in Section 3, extending prior swarm-MDP frameworks to variable-sized action spaces per node (Equation 1). The related work section (Section 2) systematically maps prior approaches against the six requirements, making a concrete case for the gap being filled. This formal grounding provides a principled basis for future RL-based routing work.

2. **eleganTE framework coupling RL with faithful ns-3 simulation.** Section 4 describes a concrete, publicly available implementation that interfaces ns-3 via shared memory (ns3-ai), with custom modules for monitoring graphs (telemetry), demand-driven traffic generation, and a drop-in routing module. This directly addresses the reproducibility and realism deficits the paper identifies in prior work (e.g., REPETITA uses abstract graph computations rather than simulated networks). The framework is a genuine infrastructure contribution.

3. **Demonstrated outperformance over OSPF/EIGRP in a specific challenging scenario.** Figure 4 shows that both MLP and GNN policies achieve lower average packet delay than OSPF and EIGRP on the predef4s topology under both flat and peak traffic modes. This provides concrete evidence that the framework can surface failure modes of shortest-path heuristics and that learned policies can exploit them — directly supporting the paper's qualified claim ("including ones where").

4. **Versatile and reproducible benchmark design.** The synnet module (Section 4.1) supports both pre-defined and random topologies with gravity-model traffic matrices, temporal scaling, and perturbations. The paper reports results using the interquartile-mean methodology recommended by Agarwal et al. (2021), which is a rigour standard uncommon in networking RL papers.

---

## Weaknesses

### Fatal

None.

### Major

- **"Scalar continuous actions per edge" phrasing creates real ambiguity about the action implementation.** The paper states in Section 5.1: "We train the policies using PPO with scalar continuous actions per edge." Standing alone, this phrasing suggests one scalar per edge, which would indeed be incompatible with the formal action space (a per-destination distribution over neighbors, Equation 1). However, reading the full paragraph resolves this: the actor outputs $\mathbb{R}^{|V|\times|E|}$ values — one per (destination, edge) pair — and the assignment module $\psi$ maps these to gateway probabilities. The "per edge" wording is loose shorthand for "per edge-destination combination." This is not a fatal flaw, but it is a genuine presentation failure: the wording directly contradicts the formalism for any reader who skips the preceding sentences, and it has misled at least one reviewer. The paper must clarify this unambiguously (e.g., "scalar continuous actions per destination-edge pair") and explain how the assignment module converts sampled Gaussian values into valid probability simplices (e.g., softmax per destination over the incident edges of each node).

### Minor

- **High variance across seeds indicates training instability that is acknowledged but not analyzed.** Figures 3, 4, and 6 consistently show large interquartile ranges for learned policies, with the GNN on predef4s (Figure 4) spanning from near-zero delay to delays exceeding OSPF. The paper attributes this to "stability issues PPO is known for" (Section 7.1), but provides no learning curves, seed-level breakdowns, or diagnostic experiments (e.g., does the variance come from initialization sensitivity, reward scaling, or the action-space exploration strategy?). For a benchmark framework paper, documenting and characterizing this instability is itself valuable — it informs future method design. The current treatment is too superficial.

- **Conclusion framing modestly overstates the evidence.** The conclusion states policies "rival popular shortest-path RPs in many scenarios." In the small predefined scenarios (predef3, predef5, predef10) the policies are "on par with or worse than" OSPF/EIGRP (the paper's own §6.1 assessment). On 25- and 50-node networks (Figure 5), the GNN policy shows far worse delay and drop counts. The "many scenarios" claim — while technically supported by the predef4s and some random 10-node results — would be more accurately phrased as "some small hand-crafted scenarios and a subset of random 10-node topologies." The abstract's "including ones where the agents outperform" is carefully qualified and accurate; the conclusion's "rival... in many scenarios" is slightly looser than the evidence warrants.

- **The generalization experiment (GNN trained on 10 nodes, tested on 25/50) shows poor performance with no analysis of why.** Figure 5 clearly demonstrates that the GNN does not generalize to larger networks. This is presented as a finding, but the paper does not attempt to diagnose the failure mode: is it the distribution shift in graph structure, insufficient message-passing steps for larger diameters, a change in traffic dynamics, or a fundamental limitation of the GNN architecture used? Breaking this down would turn a negative result into an informative one for the community.

### Trivial

- The monitoring graph $M$ is referenced in the SwarMDP definition (Section 3) and briefly described in Section 4, but its full formalization is deferred to the appendix (§A.3). A one-sentence formal definition in the main text would help readability.

- Figure 4's y-axis scales make direct comparison of the MLP/GNN vs. OSPF/EIGRP performance differences harder to read at a glance.

---

## Nice-to-Haves

- **Including a prior RL-based routing method as a baseline** (e.g., the link-weight predictor of Stampa et al. 2017) would validate the framework's ability to reproduce existing work and help situate the SwarMDP formulation against earlier MDP formulations. This is not a requirement for acceptance — the paper's contribution is the framework, not a new algorithm — but it would make the benchmark substantially more informative.
- **An optimization-based upper bound** (e.g., solving for optimal flow splitting given a traffic matrix via linear programming) would calibrate the difficulty of each scenario.
- **Learning curves** showing reward over training steps across seeds would help diagnose whether the high variance reflects training failures or genuine multi-modality in the return landscape.

---

## Removed Points

These points were raised by the reviewers but are removed or demoted following the filtering rules:

1. **"Fundamental ambiguity in the action space — incompatible with the implementation" (Harsh Critic, Critical Issue 1).** The critic claims a single scalar per edge cannot specify a per-destination distribution. This is factually incorrect: the paper's actor outputs $\mathbb{R}^{|V|\times|E|}$ values (one per destination-edge pair), and the assignment module maps these to proper simplices. The phrase "scalar continuous actions per edge" is loose wording that should be fixed, but the formalism and implementation are compatible. *Reason for removal: factually wrong / misread of the paper.*

2. **"Observation function $\xi$ is incomplete — $M$ is not formally defined" (Section-by-section notes).** The paper explicitly references §A.3 for the full definition. The appendix exists in the original submission and was stripped by the PDF parser. *Reason for removal: missing appendix content (parser issue).*

3. **"Reproducibility details missing (ns-3 parameters)" (Missing parts section).** The paper references Section B for hyperparameter details. These are in the appendix, which was stripped. *Reason for removal: missing appendix content (parser issue).*

4. **"Introduction too dismissive of prior work" (Section-by-section notes).** This is a subjective opinion about rhetorical framing, not a verifiable weakness. *Reason for removal: subjective opinion / not a concrete weakness.*

5. **Strength: "Generalization to unseen topologies via GNN policy" (Strength Finder).** The claimed strength is that the GNN "can operate on larger networks than seen during training." However, Figure 5 shows generalization performance is very poor (far worse than OSPF). The fact that the policy produces *some* output on larger graphs is a technical property of the architecture, not a demonstrated strength. *Reason for removal: conflicts with evidence presented in the paper.*

6. **"The paper should discuss individual seed results" (various).** The paper follows Agarwal et al. (2021) interquartile-mean reporting, a standard ML methodology. Individual seed results for 5 seeds would add noise rather than signal. The critic's concern about high variance is valid and kept as a minor weakness, but the specific request for all individual seed points is a style preference. *Reason for removal: methodology preference, not a substantive flaw.*

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the high variance problem and the ambiguity in the action-description wording, but these are internal consistency issues rather than novel observations that reframe or extend the paper's claims. The central tension — a well-motivated framework with honest but preliminary results — is accurately captured by the paper's own limitations section.

---

## Suggestions

1. **Fix the action-description wording.** Replace "scalar continuous actions per edge" with "scalar continuous actions per (destination, edge) pair" throughout. Add 2–3 sentences explaining how the assignment module converts sampled Gaussian values into valid per-destination probability simplices via a (presumed) softmax over incident edges for each destination at each node. This resolves the single largest source of confusion.

2. **Add learning curves and a diagnostic section on variance.** Even 2–3 figures showing reward vs. training step across seeds for one or two scenarios would substantially strengthen the paper. Discuss whether variance stems from PPO hyperparameters, action-space exploration, or reward scaling.

3. **Provide a brief analysis of the generalization failure.** Classify whether the GNN's collapse on 25/50-node networks is due to distribution shift in graph spectra, insufficient message-passing depth for larger diameters, or a change in the traffic/topology ratio. This turns a negative result into actionable knowledge.

4. **Tighten the conclusion language.** Replace "rival popular shortest-path RPs in many scenarios" with something like "approach OSPF/EIGRP performance on several small topologies and exceed it on one hand-crafted scenario, while exhibiting high variance and poor generalization to larger networks."

---
