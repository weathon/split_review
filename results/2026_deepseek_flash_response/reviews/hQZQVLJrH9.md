Now I will produce the final consolidated review.

## Summary

This paper establishes a formal first-order equivalence between activation steering and influence functions for neural networks. It proves a closed-form duality (Theorem 4.2) showing that any steering vector can be represented as a signed influence weighting over training data and vice versa, introduces a principal-angle diagnostic $\gamma$ to quantify when steering can faithfully replace weight editing (Theorems 5.1, 6.2), derives a spectral optimality result for choosing steering directions (Theorem 5.3), and provides generalization bounds for low-rank steering (Theorem 6.1). Experiments on GPT-2 Medium detoxification and ResNet-50 ImageNet classification serve as illustrative validations.

## Strengths

- **Formal duality between activation steering and influence functions.** Theorem 4.2 provides a mathematically precise, closed-form equivalence: every steering vector induces a signed measure over training data reproducing the same first-order logit shift, and conversely any signed weighting admits a steering vector that realizes the same shift. Prior work treated these as "largely independent lines" (Section 1), making this unification the paper's central novel contribution.

- **Alignment diagnostic $\gamma$ with provable fidelity guarantees.** The paper introduces $\gamma(x)$ — the cosine of the smallest principal angle between the Jacobian subspaces — and proves that the relative logit error of the minimum-norm IAS vector is bounded by $\sqrt{1-\gamma^2}$ (Theorem 5.1). Theorem 6.2 further proves a no-free-lunch lower bound: when $\gamma \leq \rho < 1$, no activation-space edit can fully replace a parameter-space perturbation. No prior steering work provided a principled, computable criterion for when steering is sufficient or doomed.

- **Spectral optimality replacing heuristic steering directions.** Theorem 5.3 shows that, given an $\ell_2$ budget, the steering direction maximizing expected first-order logit change is the leading eigenvector of a Fisher-influence matrix. This offers a principled alternative to heuristic contrastive vectors (e.g., CAA). Figure 3 confirms the spectral direction is statistically significant (p=0.00498) on ResNet-50.

## Weaknesses

### Fatal
None.

### Major

1. **Unexplained slope of 1.5 in Figure 1 undermines the central empirical claim.** The paper reports (lines 239–245) that predicted vs. actual logit shifts have cosine 0.978 but slope **1.50** (the fitted line is y=1.5x, shown clearly in the figure against the dashed identity line y=x). If the IAS vector reproduces the *same* first-order shift as the influence update, the slope should be 1.0. A 50% systematic bias means the actual logit shift is substantially larger than the first-order prediction in a *directional* way, not just noise. The paper dismisses this with "consistent with the expected linear regime," but a slope of 1.5 is not consistent with a first-order equivalence claim — it indicates that either (a) the first-order approximation is inaccurate at the magnitudes used, (b) the derivation has a missing factor, or (c) the empirical setup does not instantiate the theory correctly. This directly affects the paper's core claim that the IAS vector "realizes the same first-order output shift" (Theorem 4.2's converse).

2. **The claimed data provenance workflow is never experimentally demonstrated.** The paper repeatedly promises a practical payoff: given a steering vector, one can compute $\rho_{\mathbf{s}}$ to identify the "most causal training documents" (lines 118, 130, 275; abstract point (i); Section 4.1). The experiments in Section 7 contain no such demonstration. There is no experiment where the authors take a steering vector, compute $\rho_{\mathbf{s}}$ over the training set, inspect the top-weighted examples, and validate their causal relevance. This is the most practically novel claim in the paper, and it is entirely unsupported by evidence.

### Minor

3. **Cost model overstatement.** The introduction and Section 2 (lines 32, 56) claim that "all quantities" require "only two backward passes per input." However, computing the spectral direction (Theorem 5.3) requires solving a linear system with the Hessian via power iteration over mini-batches (lines 176-178), which is substantially more expensive. The "two backward passes" claim accurately describes the basic IAS vector and $\gamma$ diagnostic, but overreaches when applied to the full workflow including spectral steering.

4. **Equation (2) contains a formula error in a critical equation.** Line 84 writes $\Delta h^* = \mathbf{J}_{h \rightarrow y}^\top \mathbf{J}_{\theta \rightarrow y} \Delta \theta$, but the correct expression (from the Lagrangian derivation and Theorem 5.2) is $\Delta h^* = \mathbf{J}_{h \rightarrow y}^\dagger \mathbf{J}_{\theta \rightarrow y} \Delta \theta$ — involving the Moore-Penrose pseudoinverse, not just the transpose. Theorem 5.2 states the correct formula, so this appears to be a presentation error, but it is confusing in the core derivation.

5. **Limited experimental scope for the claimed unification.** The experiments cover only one LM detoxification comparison (GPT-2 Medium), one linearity plot (same model, same task), one $\gamma$-vs-depth curve, and one spectral-significance test on one ImageNet class. For a paper that claims to unify two major research areas and offer a "single, efficient workflow" (line 34), there are no experiments on: larger models (e.g., Llama-scale), multi-layer steering, the data-attribution workflow, the generalization bound (Theorem 6.1), or the no-free-lunch regime (Theorem 6.2). The experiments serve as sanity checks but do not match the ambition of the claims.

### Trivial
None.

## Nice-to-Haves

- An ablation varying $\alpha$ to show whether the slope in Figure 1 approaches 1.0 as $\alpha \to 0$, which would clarify whether the discrepancy is due to second-order terms.
- Error bars or variance estimates on the detoxification numbers in Table 1.
- A brief discussion of how Basu et al. (2021)'s findings on influence function fragility relate to this framework.

## Removed Points

- The criticism about the abstract omitting a caveat about the residual — the abstract says "to first order," which is appropriate for the stated scope.
- The criticism about influence function fragility not being discussed — relevant but not a core weakness for a theory paper that transparently inherits this limitation.
- The criticism about missing related work — the related work section is brief but this is an observable fact, and the hard rules caution against claiming specific missing references.
- The criticism about Lemma 5.4 being "just an algebraic restatement" — the inequality is valid and the practical interpretation is directionally correct, though slightly imprecise as noted in weakness 5.
- The strength about "ℓ₁-minimal data attribution" — this is a theoretical corollary without experimental validation, which conflicts with verified weakness 2.
- Several generic strengths from the strength finder (e.g., "addressed an important problem," "targeted an interesting question") that lacked specific evidence.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one critical observation that the paper itself does not acknowledge: the slope discrepancy in Figure 1 (1.5 instead of 1.0) is not a minor calibration issue but a structural challenge to the paper's framing of "equivalence." The high cosine (0.978) confirms a strong *linear relationship*, but the slope reveals that the magnitudes are systematically off by 50%. This distinction between correlation and calibration — between "proportional" and "equal" — is precisely the gap the paper needs to close. If the rebuttal can show the slope approaching 1.0 at smaller $\alpha$, or provide a principled explanation for the scaling factor, the empirical foundation would be substantially stronger.

## Suggestions

1. **Explain the slope of 1.5** by running the Figure 1 experiment at progressively smaller $\alpha$ values to show the slope approaching 1.0, or identify the source of the systematic scaling factor. Without this, the central empirical claim is compromised.
2. **Add a data provenance experiment**: take a detoxification steering vector, compute $\rho_{\mathbf{s}}$ on the training set, inspect the top-weighted examples, and validate their causal relevance.
3. **Scale experiments** to at least one larger model (e.g., Llama-7B or GPT-2 XL) and one additional task to demonstrate practical applicability beyond a single toy setting.

## Score and Decision

**Calibration anchors (all rounds):**

*Round 1 (bracketing):*
- Low band (< 3.5): "Measuring Effects of Steered Representation" (3.00), "Local Control Networks" (3.00), "Hessian-Free Influence Functions" (3.00), "Influence-based Attributions can be Manipulated" (3.00)
- Middle band (3.5–7.5): "Steering Vectors to Conceptors" (5.00), "Improving Instruction-Following through Activation Steering" (7.00), "Enhancing Training Robustness through Influence Measure" (6.20), "Steering Language Models with Activation Engineering" (5.00)
- High band (> 7.5): "Sparse Feature Circuits" (8.00), "Exploring Activation Functions in Neural ODEs" (8.00), "Interpreting Emergent Planning" (8.00), "Capturing Temporal Dependence of Training Data Influence" (8.00)

*Round 2 (narrowing within bracket):*
- "Steering Vectors to Conceptors" (5.00) — Similar theory+steering paper; the current paper has stronger theoretical novelty but similarly limited experiments.
- "CONFST: Effectively Steer LLM" (5.50) — Theory-motivated steering method; comparable in having a gap between theoretical claims and empirical support.
- "NeurFlow" (6.50, Accept) — Stronger empirical validation but comparable theoretical depth; the current paper is weaker empirically.
- "Improving Instruction-Following" (7.00, Accept) — Much stronger empirical support across four models; the current paper is clearly below this anchor.

**Initial bracket:** 4.0–7.0 (clearly above weak anchors at 3.0, clearly below strong anchors at 8.0).

**Narrowing:** Compared within the bracket, the paper sits below empirically solid anchors like "Improving Instruction-Following" (7.00) and "NeurFlow" (6.50) due to the major weaknesses (unexplained slope discrepancy, absent data provenance experiment). It is somewhat stronger than "Conceptors" (5.00) and comparable to "CONFST" (5.50) — these have similar theory-experiment gaps.

**Final score:** 5.5. The theoretical contribution (steering–influence duality, $\gamma$ diagnostic, spectral optimality) is genuinely novel and mathematically sound. However, the two major weaknesses — the 50% slope discrepancy in the central empirical validation and the entirely undemonstrated data provenance workflow — prevent the paper from making a convincing case for its claimed practical impact.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>