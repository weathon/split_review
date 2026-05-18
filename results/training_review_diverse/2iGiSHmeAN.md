Now I have a thorough understanding of the paper. Let me write the final consolidated review.

---

## Summary

This paper proposes BroGNet, a graph neural stochastic differential equation (SDE) framework for learning Brownian dynamics directly from trajectory data. The key innovations are (1) formulating the problem as a graph neural SDE that learns both the drift force and the stochastic diffusion term, (2) enforcing linear momentum conservation as a hard architectural constraint via Newton's third law in the message-passing scheme, and (3) demonstrating zero-shot generalization to unseen system sizes (up to 500 particles, trained on 5) and unseen temperatures. The method is evaluated on three systems (linear spring, nonlinear spring, binary linear spring) against six baselines including a soft-constraint variant (MIBDGNN).

## Strengths

- **First neural SDE + GNN framework for learning Brownian dynamics from trajectory.** The paper correctly identifies that prior work on learning physical dynamics focuses overwhelmingly on deterministic (ODE-governed) systems. The extension to the stochastic (SDE) setting is a genuine gap and the paper provides a concrete, working framework to fill it. The approach is principled: it factorizes learning into a deterministic drift term (via a GNN predicting pairwise forces) and a stochastic diffusion term (via an MLP predicting per-particle friction coefficients γ), then integrates via Euler-Maruyama.

- **Zero-shot generalizability to unseen system sizes and temperatures is convincingly demonstrated.** The inductive graph architecture allows the model trained on 5-particle systems to generalize to 50 and 500 particles (two orders of magnitude larger) without retraining (Figure 5a-c), and to temperatures T=10 and T=100 after training at T=1 (Figure 5e-f). This is a practically valuable property and is well-supported by the experimental results.

- **Well-designed ablation study isolating momentum conservation.** The paper proposes BDGNN (same architecture without Newton's third law) and MIBDGNN (soft-constraint via loss penalty) as direct ablations. The comparison cleanly separates the effects of graph representation, momentum conservation as inductive bias, and hard vs. soft constraint enforcement. This is a textbook experimental design that allows readers to attribute performance differences to specific design choices.

- **Systematic evaluation across three distinct physical systems.** The method is tested on linear spring, nonlinear spring (quartic force), and binary linear spring systems, spanning different interaction types and particle heterogeneity, lending confidence that the approach is not overfitted to a single toy system.

## Weaknesses

### Fatal
None. The paper's core contribution — a framework for learning Brownian dynamics from trajectory using graph neural SDEs — is valid and the experiments broadly support its feasibility and promise.

### Major

**1. The abstract and title overclaim BroGNet's superiority relative to MIBDGNN, creating a narrative mismatch with the paper's own results.**  
The abstract states: "We modify the architecture of BroGNet to enforce linear momentum conservation of the system, which, in turn, provides superior performance on learning dynamics as revealed empirically." However, Section 4.2 (line 192) explicitly states: "Interestingly, we observe that the MIBDGNN significantly outperforms BROGNET." MIBDGNN — the same architecture but with momentum conservation as a *soft* loss penalty rather than a hard architectural constraint — achieves better trajectory rollout error, Brownian error, and position error across all three benchmark systems (Figures 2–4). The paper acknowledges MIBDGNN's superiority in these metrics but the abstract's unqualified "superior performance" language does not reflect this. The conclusion (line 244) is more honest ("MIBDGNN exhibits superior performance in learning the dynamics... while BROGNET exhibits superior momentum conservation"), but the abstract, title, and introduction still frame the hard constraint as categorically superior. This mismatch undermines trust in the paper's narrative. The actual contribution — that *momentum conservation* (whether hard or soft) improves learning, with a trade-off between trajectory accuracy (soft better) and exact conservation (hard better) — is interesting and worth publishing, but needs to be stated upfront rather than buried in the conclusion.

**2. The training procedure is critically underspecified, making the loss function ambiguous and the method irreproducible.**  
The paper states (lines 112–126) that "the positions are derived using the Euler Maruyama integrator" and defines the loss as a Gaussian negative log-likelihood in Eq. 9. However, Eq. 10 (the Euler-Maruyama update) explicitly includes a noise term ΔΩₜ ~ 𝒩(0,1). It is never clarified whether:
- (a) The predicted position X̂_{i,t} used in the loss is the deterministic drift-only prediction (noise term omitted) or a sample from the full SDE step (noise included).
- (b) Training uses teacher forcing (ground-truth previous positions as input at each step) or full rollout from initial conditions.
- (c) The loss is evaluated per-step on ground-truth prefixes or on an entire predicted trajectory.

If X̂_{i,t} is a sample (including noise), then Eq. 9 is not a proper Gaussian NLL — the "predicted position" is a random variable whose variance includes both the learned σ̂ᵢ² and the sampling noise from ΔΩₜ, so the loss would conflate two sources of variance. If X̂_{i,t} is the deterministic mean, then the paper must state that the noise term is excluded during training and only added at evaluation time. Neither is specified. This ambiguity is the most actionable issue in the paper: it directly affects the mathematical validity of the training objective and prevents reproduction.

**3. No uncertainty quantification in any of the reported results.**  
All results are reported as geometric means (Figures 2–7) without error bars, standard deviations, or confidence intervals. The experimental setup generates ample information for computing variability: "1000 forward simulations from 100 initial conditions, each evaluated with 10 random seeds" (Figure 2 caption). Without uncertainty quantification, the reader cannot assess whether the reported differences between methods are statistically significant. For example, in Figure 2, MIBDGNN's trajectory error appears to be roughly an order of magnitude lower than BroGNet's — but if the variance across seeds is large, this difference may not be meaningful. Error bars are standard practice for any comparative evaluation and their absence is the weakest methodological decision in the paper.

### Minor

**1. The claim about data efficiency is ambiguous with respect to MIBDGNN.**  
Section 4.5 states: "BroGNet can learn efficiently from a small dataset size compared to the baselines... attributed to the momentum conservation bias." However, MIBDGNN also incorporates momentum conservation (as a soft constraint) and is one of the baselines in Figure 7. The text does not clarify whether BroGNet's advantage at small data sizes (e.g., 100 or 500 points) holds specifically *over MIBDGNN* or only over the non-momentum-conserving baselines (BFGN, BDGNN, BNequIP). If BroGNet and MIBDGNN perform similarly at small dataset sizes, the data efficiency benefit should be attributed to momentum conservation generally, not to the hard constraint specifically.

**2. No direct comparison of the learned force fields against ground-truth forces.**  
The paper evaluates only trajectory-level metrics (position error, trajectory rollout KL divergence, Brownian error). For a method that claims to learn the dynamics — and specifically the pairwise interaction forces — showing that the predicted F_{ij} matches the ground-truth F_{ij} (e.g., −kΔx for linear springs) would be far more direct and interpretable than rollout metrics. This is especially relevant for the zero-shot generalization results: a GNN that correctly predicts per-edge forces on 5-particle systems should maintain that accuracy on 500-particle systems, and a direct force comparison would confirm or refute this.

**3. The momentum conservation theorem (Theorem 1) is a description of the architecture, not a substantive theoretical result.**  
The theorem states that if internal forces sum to zero (as enforced by Eq. 8), linear momentum is conserved. This is immediate from the definition and does not constitute a theoretical contribution in the usual sense. This is not a flaw in the paper — many papers include such statements for completeness — but it should not be presented as a theoretical advance.

### Trivial

- The squareplus activation function is used throughout without justification or ablation in the main paper. (The paper references a ReLU comparison in Appendix Fig. L, which is good, but a brief justification in the main text would help.)
- The paper claims "no attempt has been made to learn the dynamics of Brownian systems... from their trajectory" (line 12) with the hedge "to the best of the authors' knowledge." The hedge is sufficient, but the statement could be softened to avoid appearing to overclaim novelty.

## Nice-to-Haves

- A systematic ablation on the number of message-passing layers L would be informative. The paper uses an unspecified number of layers, and given that the interaction is pairwise and linear, even a single layer might suffice.
- If the hard constraint provides better out-of-distribution generalization (to unseen temperatures or system sizes) than the soft constraint, this would substantially strengthen the paper. Currently Figures 5 and 7 show comparable performance between BroGNet and MIBDGNN in these settings, making it hard to argue for the hard constraint's superiority in generalization.
- The paper could be improved by reframing the contribution around hard vs. soft momentum constraints as a design space. The current framing ("BroGNet is superior") sets up expectations that the evidence does not meet, whereas a framing of "momentum conservation improves learning, and here is a study of the hard vs. soft trade-off" would be both accurate and novel.

## Removed Points

These points were raised by reviewers but are removed or downgraded per the filtering guidelines:
- *Criticism about directed edges for symmetric interactions* — Removed. The paper explains that edge weights are relative displacement vectors (directional by nature), making the directed formulation necessary.
- *"No attempt has been made" claim is overstated* — Removed. The paper uses the hedge "to the best of the authors' knowledge," and I cannot verify the related-work landscape externally.
- *Theorem 1 is trivial* — Downgraded to Minor. It is a straightforward guarantee but not a problem per se; the paper's value does not depend on theoretical depth.
- *Criticism about missing appendix details* — Removed. The parser strips appendix content; these exist in the original submission.

## Novel Insights

The most interesting empirical finding is that the soft-constraint variant (MIBDGNN) *outperforms* the hard-constraint variant (BroGNet) on trajectory prediction metrics, despite BroGNet achieving near-perfect momentum conservation. This suggests a trade-off that is counterintuitive from a physics perspective: adding momentum conservation as a differentiable loss penalty may provide a more flexible learning signal than a hard architectural constraint that zeros out the total force. The hard constraint, by forcing the sum of forces to zero at every step regardless of data, may limit the model's ability to fit the observed stochastic trajectories, whereas the soft constraint allows the model to decide how strongly to prioritize conservation vs. fitting. This tension, if explored further (e.g., by varying the penalty weight λ_MI in MIBDGNN), could yield insight into the design of physics-constrained neural SDEs more broadly.

## Suggestions

1. **Reframe the narrative.** Rewrite the abstract, introduction, and conclusion to present the paper as studying the effect of momentum conservation (both hard and soft) in neural SDEs for Brownian dynamics, rather than claiming BroGNet's categorical superiority. The contribution is the *framework* (graph neural SDE for BD) and the *finding* that momentum conservation improves learning, with different trade-offs for hard vs. soft enforcement.

2. **Clarify the training procedure.** Explicitly state: (a) whether X̂_{i,t} is computed with or without the noise term during training; (b) whether training uses teacher forcing or full rollout; (c) whether Eq. 9 is a proper NLL or an approximation. A short pseudocode or algorithm box would resolve all ambiguity in one paragraph.

3. **Add error bars / confidence intervals.** With 10 random seeds and 100 initial conditions, the data for computing standard deviations or 95% CIs is already collected — report them. This is the single most impactful addition for rigor.

4. **Add a force-field comparison.** For the spring systems, the ground-truth force per edge is known analytically (e.g., F_{ij} = −k(x_i − x_j) for linear springs). Compare the predicted per-edge forces against these ground-truth values (e.g., via RMSE or R²). This would directly validate whether the model has learned the correct physical law, and would strengthen the zero-shot generalization claims substantially.

## Score and Decision

The paper addresses a worthwhile problem and the core framework is sensible. The experimental design (ablations, multiple systems, zero-shot evaluation) is above average. However, the narrative mismatch between the abstract's "superior performance" claim and the results (MIBDGNN outperforms BroGNet), the underspecified training procedure that undermines reproducibility, and the absence of error bars in comparative evaluations are significant issues that prevent acceptance in the current form. The contribution could be rescued with a major reframing and the addition of missing details, but that requires substantive rewriting.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>