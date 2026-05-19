- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 3, 6, 8
Now I'll compose the final review.

## Summary

This paper develops a normative reinforcement learning model in which Gaussian radial basis function place fields (amplitude, center, width) are optimized alongside an actor-critic to maximize cumulative reward via TD error. The model reproduces three experimentally observed phenomena—high field density at reward locations, field elongation against the direction of travel, and representational drift with stable behavior—within a single reward-maximization framework. The paper also provides a perturbative theoretical analysis linking field-center shifts to critic-weight magnitude, compares the model's dynamics against the successor representation (SR), and shows that noisy field-parameter updates facilitate learning of new targets.

## Strengths

1. **Unification of three disparate place-field phenomena under a single normative objective.** Prior models addressed each phenomenon separately (e.g., SR for elongation, degenerate-subspace models for drift). This is the first model to reproduce all three—density at reward (Fig. 1B–F), backward elongation (Fig. 2A–B), and drift with stable behavior (Fig. 3B–C)—within one reward-maximization framework.

2. **Perturbative theoretical analysis linking field-center shifts to critic-weight magnitude.** Equation 7 provides an analytical prediction that fields at high-value locations (large critic weights) shift faster toward the reward. This approximation is validated against simulations in both 1D and 2D (Fig. 1E–F) and explains why reward-location density emerges before start-location density.

3. **Distinct dynamics from the successor representation, yielding testable predictions.** The paper shows that RM and SR firing-rate correlations change sign over learning (early anti-correlation → later positive correlation; Fig. 2D–E), and that RM fields elongate more strongly in a 2D obstacle environment (Fig. 2F). These differences offer experimentally distinguishable predictions.

4. **Systematic ablation isolating the contribution of each field parameter.** The ablation (Fig. 4A–B) establishes a clear ordering: width (σ) optimization provides the largest benefit, followed by amplitude (α), while center (λ) optimization alone provides negligible benefit. This clarifies which aspects of place-field plasticity most strongly support learning.

5. **Demonstration of a functional role for drift-like noise in new-target learning.** Agents with moderate noise (σ_noise = 0.0005) achieve higher cumulative reward and faster convergence when targets change repeatedly (Fig. 4C), establishing that representational instability can serve a computational purpose rather than being purely detrimental.

## Weaknesses

### Fatal

None.

### Major

1. **Representational drift is driven by externally injected noise, not emergent from the learning dynamics.**  
   The model without noise produces extremely stable population vectors (Fig. 3B, blue). To obtain drift the authors explicitly add Gaussian noise to field parameter updates ("To drive larger variability in the representation, we introduced Gaussian noise…"). The paper describes this as "recapitulating" drift (abstract, Section 4.3), but the model does not *explain* why biological systems drift — it shows that *if* you perturb the parameters with noise of a specific form, the fields change and behavior remains stable. This is a consistency check rather than a mechanistic account. The Discussion acknowledges biological noise sources, but the Results section presents the drift finding without sufficiently qualifying that it depends on an external noise injection whose biological origin is hypothesized, not derived. The paper would be strengthened by reframing this section as a "noise-driven drift hypothesis" rather than as a recapitulation.

### Minor

1. **The functional role of field center shifts is unclear and unreconciled with the ablation results.**  
   The ablation (Fig. 4A–B) shows that center (λ) optimization provides no benefit for single-target learning and even hurts when combined with amplitude optimization. Yet center shifts are the basis for two of the paper's three main phenomena (density increase at reward, field elongation). The paper does not reconcile why the model produces center shifts that are the most visually striking phenomenon but provide no measurable benefit for the reward-maximization objective in the single-target setting. The perturbative analysis (Eq. 7) shows centers shift as a side effect of critic-weight magnitude, but the paper does not discuss whether this makes them an epiphenomenon or whether they serve a different function (e.g., enabling relearning after reward relocation — a question partially addressed in Fig. 4C but not tied back to the ablation).

2. **The SR comparison tests a specific architectural variant that does not directly test the prevailing SR hypothesis.**  
   The SR agent uses fixed place fields for the actor-critic while learning successor features in a parallel pathway that does not influence behavior. In many hippocampal SR accounts (Stachenfeld et al., 2017), successor features serve as the state representation for both value and policy. The comparison is therefore between "place fields optimized for reward" and "place fields optimized for transition prediction given a fixed policy." This is a valid contrast for representation analysis, but it does not directly test whether TD learning of transitions *causes* field elongation in the way hypothesized by the SR literature. The paper should clarify what the comparison tests and what it does not.

3. **The mechanism by which noise improves new-target learning is not analyzed.**  
   The paper shows that moderate noise (σ_noise = 0.0005) improves relearning (Fig. 4C) but does not analyze how — e.g., does noise prevent parameter saturation, actively drive exploration of new feature geometries, or enable escape from local minima? A brief analysis of the mechanism would strengthen the claim.

4. **Several comparisons to experimental data remain qualitative.**  
   The paper states it "replicates" or "recapitulates" experimental findings, but comparisons are qualitative. For example, field elongation is shown as an average change in size and COM, but experimental papers (Mehta et al., 1997) also report specific asymmetry indices. Adding a quantitative metric would allow a more precise match and strengthen the claims.

5. **The noise benefit for new-target learning is shown for a single target sequence.**  
   The sequence of target locations in Fig. 4C is fixed (0.5 → 0.0 → 0.75 → -0.25 → 0.5). While a single sequence demonstrates feasibility, the generality of the noise benefit across different sequences is not tested.

### Trivial

None.

## Nice-to-Haves

- **Demonstrate drift without explicit noise injection.** If the stochastic policy alone, or degeneracy in the parameter space (e.g., with larger field counts), produced slowly decaying autocorrelations in field parameters, the paper would move from "consistent with drift" to "explains drift."
- **Sensitivity analysis for relative learning rates** of α, λ, σ parameters. The perturbative theory explicitly depends on separation of timescales; the results could change if different parameters learned at different rates.
- **Explore alternative noise models** (e.g., correlated or multiplicative noise) to assess biological plausibility.
- **Speculate on how noise magnitudes map onto experimental manipulations** (e.g., dopaminergic modulation, synaptic noise) to tighten the link to experiment.

## Removed Points

These points were removed from the main review; treat with caution:

1. "Does not discuss possibility of multiple learning objectives" — Scope creep; the paper is explicitly about a single reward-maximization objective.
2. "Does not test scenario where start location has high value" — Scope creep; the experiment is designed to match specific published experiments (Gauthier & Tank, 2018).
3. "Fig. 3F claims to replicate Qin et al. (2023) but effect is only at specific noise magnitudes" — The paper *explicitly* states which noise magnitudes replicate Qin et al. (2023), and at zero noise the trend reverses. This is correctly reported; no weakness exists.
4. "Missing statistical rigor" — The paper reports 95% CI over 10–50 seeds, which is standard for this type of work.
5. "Joint gradient sign could confuse readers" — The paper clearly states the objective structure (Eq. 6) and notes that the critic minimizes squared TD error while the actor/fields ascend the policy gradient. This is adequately explained.
6. "Related works missing X" — Not verifiable; do not mention missing references.
7. "Formatting/presentation nitpicks" — Parser artifacts, not author errors.
8. "Missing appendix content" — Parser strips appendix sections from all papers; they exist in the original submission.

## Novel Insights

Beyond the paper's own contributions, the most interesting insight from the review process is that the **tension between the ablation results (center optimization does not help) and the visual phenomena (center shifts are central)** is actually a feature, not a bug: the perturbative analysis reveals that center shifts arise as a *side effect* of value learning (proportional to w_v²) rather than as a directly optimized quantity. This suggests that some of the most visually salient neural phenomena may be epiphenomenal to the learning objective — a point that could be made more explicitly and could inform how experimentalists interpret field reorganization. Additionally, the finding that noise helps new-target learning but hurts at high magnitudes (inverted-U curve) provides a concrete computational hypothesis for why biological systems might maintain moderate drift rates rather than zero drift.

## Suggestions

1. **Reframe the drift section** to explicitly acknowledge that drift is noise-driven rather than emergent from the learning dynamics. Present it as "noise-induced drift is compatible with stable behavior under reward maximization" rather than as the model "recapitulating" drift.
2. **Add a brief discussion reconciling center shifts with the ablation results.** A few sentences explaining that center shifts are a consequence of value learning (per the perturbative analysis) rather than directly optimized for performance, and discussing whether they might serve other functions (e.g., facilitating relearning as hinted by Fig. 4C), would resolve the structural tension.
3. **Clarify the scope of the SR comparison** — explicitly state that the comparison is between reward-optimized and transition-prediction-optimized representations, not a direct test of the causal SR hypothesis for elongation.
4. **Add at least one quantitative metric** (e.g., asymmetry index from Mehta et al., 1997) to provide a more precise bridge between simulation and experiment.
