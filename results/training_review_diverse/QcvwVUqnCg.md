Now I have thoroughly reviewed the paper. Let me compose the final consolidated review.

## Summary

This paper proposes a normative reinforcement learning model where Gaussian place fields are updated via TD error to maximize cumulative reward. Operating as an actor-critic with learnable field parameters (amplitude, center, width), the model reproduces three experimentally observed phenomena in hippocampal place field reorganization: (1) high field density at reward locations, (2) backward field elongation against the trajectory, and (3) representational drift with stable behavior. The paper further provides a perturbative analytical approximation linking field dynamics to critic weights, compares the model to the successor representation, and demonstrates a functional role for noise-induced drift in learning multiple new targets.

## Strengths

1. **Unification of three disparate phenomena under a single normative framework.** The model simultaneously reproduces reward-concentrated field density (Fig. 1B–D), backward elongation against the movement direction (Fig. 2A–B), and representational drift with stable behavior (Fig. 3B–C) using a single TD-learning objective with learnable Gaussian fields. Prior work explained each with separate mechanisms.

2. **Perturbative analytical approximation linking field dynamics to critic weights.** The derived approximation (Eq. 7, Section 4.1) provides a mechanistic prediction: field center shifts are proportional to the squared critic weight \(w_{v,i}^2\), explaining why fields near the reward shift fastest and why density emerges first at the reward and later at the start. This goes beyond pure simulation.

3. **Demonstration that noisy field updates improve learning of multiple new targets.** Fig. 4C shows that agents without noise fail to learn a changed target, while moderate noise substantially improves cumulative reward across repeated target shifts. This provides a concrete normative functional role for representational drift.

4. **Comparison with the successor representation (SR) revealing distinct learning dynamics.** The paper shows that RM and SR agents differ in the temporal correlation between mean firing rate and occupancy — RM fields are anti-correlated early and become positively correlated later, while SR fields are always positively correlated (Fig. 2C–E). This contrast yields testable predictions to distinguish the two normative accounts.

5. **Ablation experiments quantifying the contribution of each field parameter to policy convergence.** Optimizing width (\(\sigma\)) yields the greatest speedup, followed by amplitude (\(\alpha\)), while center optimization alone provides little benefit (Fig. 4A–B). This clarifies the relative importance of different degrees of representational flexibility and addresses parameter degeneracies.

## Weaknesses

### Fatal
None.

### Minor

1. **The mechanistic explanation for why reward maximization produces backward elongation is not provided.** The paper shows that the RM model recapitulates elongation and compares it to SR, but does not give an intuitive explanation for the mechanism. The SR explanation is clear (fields learn transition probabilities, naturally causing backward shift). For the RM model, the reader is left to infer why TD-error-driven updates cause fields to expand backward. A brief mechanistic paragraph would significantly deepen insight.

2. **The framing of drift conflates emergent phenomena with added mechanisms.** The paper is transparent about injecting Gaussian noise to produce drift (Section 4.3: "To drive larger variability in the representation, we introduced Gaussian noise"), and the no-noise baseline shows almost no drift (Fig. 3B blue). However, the abstract and contributions state that "reward maximization predicts drifting fields," which could be read as drift being emergent from the learning objective itself. The paper would benefit from explicitly distinguishing between phenomena that emerge from the RL objective (density, elongation) and those that require an additional mechanism (drift via noise). The functional role of noise for new-target learning is the genuine contribution and should be foregrounded as such.

3. **The 2D elongation claim could be more clearly quantified.** In 2D, the text claims "elongation of fields against the agent's direction of movement," while the figure caption describes elongation "along the trajectory." The concept of "backward against the trajectory" is well-defined in 1D (leftward when moving rightward) but less clearly defined in 2D. Given the corridor geometry, it is not obvious from the verbal description whether fields elongate backward (opposite to travel) or simply stretch along the corridor (which would be a different phenomenon). The quantitative summary statistics referenced in Sup. Fig. 6 should ideally resolve this, but the main text would benefit from clarifying what "against" means in the 2D setting.

4. **The "weak feature learning regime" explanation is stated but not rigorously justified.** The paper notes that increasing the number of fields reduces density because the agent enters a "weak feature learning regime" (Section 4.1), citing Sup. Fig. 4. This is an interesting observation, but the explanation is brief. A theoretical justification — even a sketch — of why additional fields in this regime do not contribute extra advantage would strengthen the claim.

### Trivial

- Equation 2 defines amplitude as \(\alpha_i^2\). The reason for the squaring (presumably to enforce non-negativity while allowing the gradient to pass through) is not stated and would be helpful to clarify briefly.

## Nice-to-Haves

- A per-field signed shift analysis (relative to movement direction) would provide a more quantitative test of the elongation claim in 1D, though the current average measure already captures the Mehta phenomenon.
- Formal statistical comparisons (e.g., permutation tests) for the ablation experiments would strengthen claims about "significant improvement," though the reported 95% CIs over 50 seeds already provide reasonable evidence.
- Exploration of how results generalize across different reward magnitudes and environments beyond those shown — though the paper already varies reward magnitude (Fig. 1D) and includes a 2D obstacle environment.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The perturbative analysis is relegated to Appendix B, which is not available."** — REMOVED per hard rule: the parser strips appendix sections, which exist in the original submission. The main text already gives the key prediction (Eq. 7) and its derivation steps, which is sufficient.

2. **"No statistical tests or error bars are reported for the ablation experiments (Fig. 4) beyond confidence intervals."** — WEAKENED to Nice-to-Have. The paper explicitly states "Shaded area is 95% CI over 50 seeds" for all relevant figures. Confidence intervals are standard; permutation tests are a wishlist item, not a missing requirement.

3. **Implication that the paper does not explore different reward magnitudes** — REMOVED as factually incorrect. Fig. 1D explicitly varies reward magnitude (r_max = 1, 5, 9) and reward location width.

4. **Critique about the biological plausibility of backpropagating TD error through the actor-critic** — The paper already acknowledges this limitation in the Discussion and cites biologically plausible learning rule alternatives. This is an acknowledged limitation of a normative model, not an unaddressed weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add a brief paragraph in Section 4.2 providing mechanistic intuition for why reward maximization produces backward elongation (e.g., fields expand to cover states with high-value correlates, shifting COM backward as they integrate predictive value signals).
- In the abstract and contributions, rephrase the drift claim to clearly distinguish the model component responsible (noise injection) from the learning objective, e.g., "Adding noise to field parameters during reward maximization produces drifting fields that..."
- In the 2D elongation description (Section 4.2), clarify what "against the movement direction" means operationally in 2D and provide a quantitative measure (e.g., signed elongation along the trajectory direction vs. orthogonal).
- Briefly justify the \(\alpha_i^2\) parameterization in Eq. 2.

## Score and Decision

This paper makes a meaningful contribution to computational neuroscience by demonstrating that a single reward-maximization framework can unify three well-known but previously disconnected phenomena. The modeling is clean, the perturbative analysis adds theoretical depth, the SR comparison yields testable predictions, and the functional role of noise for new-target learning is genuinely novel. The weaknesses are limited to framing and explanatory depth — none threaten the core claims. The paper is well above the acceptance threshold for a venue that values normative modeling contributions.

**Originality:** Good — first model to unify these three phenomena under reward maximization.  
**Importance:** High — addresses a long-standing question about why place fields reorganize the way they do.  
**Claims supported:** Yes, with minor framing concerns.  
**Soundness:** Good — simulations are thorough with confidence intervals and appropriate controls.  
**Clarity:** Good, though some framing could be more precise.  
**Value to community:** High — provides testable predictions and a framework for future work.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>