Now I have a thorough understanding of the paper and the calibration anchors. Let me write the consolidated review.

---

## Summary

This paper establishes a first-order equivalence between activation steering and influence functions, showing that any activation steering vector can be represented as a signed re-weighting of training examples and vice versa. The framework yields an Influence-Aligned Steering (IAS) vector, an alignment diagnostic (γ) for certifying steering feasibility, a spectral recipe for optimal steering directions, and generalization bounds for low-rank interventions. The core mathematical results (Theorems 4.2, 5.1–5.3, 6.1, 6.2) form a coherent and novel theoretical contribution that genuinely unifies two previously disconnected interpretability paradigms.

## Strengths

- **Genuinely novel theoretical unification.** Theorem 4.2 provides an explicit closed-form construction mapping any steering vector to a signed influence measure over training data (Equation 4) and vice versa. This duality—absent from prior steering or influence literature—is the paper's core contribution and is properly proved. The alignment bound (Theorem 5.1), minimum-norm IAS (Theorem 5.2), and no-free-lunch result (Theorem 6.2) form a coherent package of diagnostic and impossibility results that give practitioners principled guidance on when steering can substitute for weight-space editing.

- **Convincing empirical validation of the first-order equivalence.** Figure 1 demonstrates near-perfect collinearity (cosine 0.978) between predicted and actual logit shifts for 5,000 prompt-token pairs on GPT-2 Medium. This directly validates the paper's central technical claim—that the linear approximation holds with high fidelity in the small-edit regime—and does so at a scale (GPT-2 Medium, 354M parameters) that is non-trivial.

- **Useful diagnostic tool with empirical support.** The alignment diagnostic γ is validated across layers (Figure 2), showing a monotonic increase from 0.64 at layer 0 to 0.94 at layer 11, giving practitioners a concrete, low-cost feasibility check backed by both theory and evidence.

- **Theoretical rigor with practical framing.** The generalization bound (Theorem 6.1) shows that low-rank IAS incurs excess Rademacher complexity vanishing with layer width and sample size—a reassuring result. The paper consistently translates theorems into actionable guidance (e.g., "prefer low ranks and small α unless γ is close to 1," "probe γ at a few candidate layers"), bridging theory and practice effectively.

## Weaknesses

### Major

- **Data-tracing capability—a central practical claim—is entirely unevaluated.** Corollary 1 and the "Practical payoff" paragraph state that ρₛ identifies the minimal set of training examples responsible for a steering intervention, and the text explicitly points readers to Section 7 ("see Section 7"). Yet Section 7 contains no data-tracing experiment: no examples of retrieved documents, no qualitative sanity check, no comparison to existing influence-based attribution methods. This is not a minor omission—the paper repeatedly frames data tracing as one of the framework's key practical deliverables (abstract: "a constructive algorithm for mapping undesired behaviors back to causal training examples"; introduction: "identify the responsible training examples"). A promised capability of this magnitude cannot go entirely undemonstrated without substantially weakening the paper's practical claims.

- **The detoxification experiment lacks essential detail and is under-explained.** Table 1 reports IAS (toxicity 0.0164, perplexity 13701) behind CAA (0.0150, 13291) on both metrics, yet the paper provides no description of what influence target Δθ IAS was constructed to match. Was the influence update derived from a toxicity-reduction objective? If so, which one? Without this information, the reader cannot assess whether the comparison is between methods solving the same problem or different problems. The paper also offers no diagnosis of why IAS underperforms CAA—does the gap arise from the choice of influence target, from imperfect first-order approximation at the chosen steering magnitude, or from the alignment residual? A single sentence contextualizing the result would substantially improve this section.

### Minor

- **The spectral optimality experiment (Section 7.4, Figure 3) validates a mathematical property rather than a practical use case.** It confirms that the top eigenvector of Σ lies far in the tail of a random-direction null distribution (p ≈ 0.005), which follows from the Rayleigh quotient and Theorem 5.3. What is missing is any demonstration that steering with this spectral direction actually produces meaningful behavioral changes—e.g., does it increase the horse classification rate on dog images? Does it outperform a hand-crafted steering vector on a downstream task? The experiment is a sanity check, not a validation of the claim that the "spectral recipe replaces hand-crafted vectors."

- **The slope in Figure 1 (1.50) is noted but not discussed.** A slope of 1.50 in the predicted-vs-actual regression implies systematic under-prediction of the actual logit shift by the first-order approximation. A brief note on whether this is due to second-order effects, the specific construction of the influence update, or something else would strengthen the analysis.

- **The paper says "see Section 7" for the data-tracing demonstration but Section 7 has none.** This appears to be a structural error in the manuscript (possibly an intended experiment that was not completed). At minimum, the cross-reference should be corrected.

### Trivial

- The "rule of thumb" about λ* (Section 3) is described as a practical diagnostic but is never operationalized in experiments—no λ* values are reported or used to guide a steering decision.

## Nice-to-Haves

- A concrete data-tracing demonstration: pick a simple steering intervention (e.g., a sentiment flip), compute ρₛ, and show the top-weighted training examples along with a brief qualitative analysis.
- End-to-end comparison of the spectral direction against a hand-crafted direction on a downstream task (classification change, not just logit magnitude).
- A brief complexity analysis for computing ρₛ at data-scale would ground the claim that the framework "scales to billion-parameter models."
- Discussion of how the detoxification IAS was constructed (what Δθ was used), and a brief diagnosis of the CAA-vs-IAS gap.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim that the detoxification result is "structural evidential problem" that "actively weakens the claim"**: REMOVED as overstated. The paper does not claim IAS is superior to CAA for detoxification; it claims IAS provides a principled mapping between steering and influence. The detoxification experiment demonstrates IAS can be applied, not that it is SOTA. The absence of detail on the IAS construction is a valid criticism (retained as Major above), but the result does not invalidate the theoretical framework.

- **Harsh critic's demand that IAS should beat CAA to be valid**: REMOVED. The IAS and CAA directions solve different problems—IAS matches a specific influence update while CAA uses a contrastive activation difference. Beating CAA is not required for the theory to hold.

- **Harsh critic's concern about Im(J_θ→y) ⊆ Im(J_h→y) being "rarely satisfied in practice"**: WEAKENED and moved to Nice-to-Haves. The paper explicitly addresses this with the alignment bound (Theorem 5.1) and the no-free-lunch result (Theorem 6.2), and Figure 2 shows γ can be high (0.94) at later layers. The framework accounts for imperfect alignment.

- **Harsh critic's demand for "more explicit comparison to prior work that has drawn loose connections between activation-space and weight-space interventions"**: REMOVED. The paper already positions itself relative to the steering (Turner et al., Subramani et al.) and influence (Koh & Liang, Pruthi et al.) literatures. Demanding specific comparisons to unnamed prior work is not actionable.

- **Harsh critic's characterization of the generalization bound as "does not add strong new constraints"**: REMOVED. This is a matter of judgment, not a factual error. The bound provides a formal guarantee that low-rank IAS is benign for generalization—a result with practical value.

- **Strength Finder: "The generalization bound... provides a theoretical safety guarantee"**: RETAINED but softened. The bound is a useful result but largely applies known techniques to the specific setting (as the paper acknowledges by citing Pinto et al. 2024).

- **Strength Finder: "The minimal-ℓ₁ data reweighting result... gives a principled debugging tool"**: RETAINED as a theoretical strength but noted as unevaluated in the Major weakness.

- **Strength Finder: "This paper establishes a first-order equivalence... demonstrating that the framework delivers on its core contribution"**: RETAINED for the theoretical aspects, but the claim about the framework being "practical" is softened due to missing empirical validation of the data-tracing workflow.

## Novel Insights

The core insight—that activation steering and influence functions are first-order projections of the same underlying sensitivity tensor, separated only by whether one propagates through J_{h→y} or J_{θ→y}—is genuinely elegant and not previously articulated in the literature. The alignment diagnostic γ (cosine of smallest principal angle between the two Jacobian subspaces) is a crisp, computable quantity that captures the entire feasibility question in a single scalar, and the empirical finding that γ increases monotonically with layer depth (Figure 2) is a practically useful observation that will inform steering practice regardless of whether one adopts IAS.

## Suggestions

1. **Add a data-tracing demonstration.** This is the single highest-impact improvement. Even a qualitative example—showing the top-k training documents retrieved by ρₛ for a simple steering intervention on a modest model—would transform the paper from "promising theory" to "validated workflow." An appendix section with a few examples would suffice.

2. **Specify the IAS construction for detoxification** (what Δθ was used, how it was derived) and add one sentence contextualizing the CAA comparison. If the IAS target was not specifically optimized for toxicity reduction, say so—this would explain the gap without undermining the theory.

3. **Upgrade the spectral experiment** to show an end-to-end behavioral change (e.g., percentage of dog images reclassified as horse after steering) rather than only a statistical significance test.

4. **Fix the "see Section 7" cross-reference** in the Practical payoff paragraph—either add the experiment or remove the reference.

## Score and Decision

**Round 1 bracket:** Based on comparing against anchors in the weak band (avg ~3.0: papers with significant methodological flaws), middle band (5.0–6.4: papers with genuine novelty but empirical limitations), and strong band (8.0: well-validated papers with clear contributions), this paper clearly sits in the middle band. It is substantially stronger than the 3.0 anchors (which have fundamental flaws) and weaker than the 8.0 anchors (which have thorough empirical validation).

**Round 2 narrowing:** Within the middle band, the closest comparators are:
- 9wjGUN65tY (5.00): "Conceptors" — also a theoretical framework for steering with limited experiments; the paper under review has stronger theoretical novelty but comparable empirical gaps.
- p85TNN62KD (5.50): "Versatile Influence Function" — extends influence functions to new loss classes with some empirical validation; comparable methodological contribution level.
- ZPkNrs6aNO (5.50): "Confident Directions" — a theoretical framework for steering with experiments.
- KjBG4JNOc2 (6.20): "Enhancing Training Robustness through Influence Measure" — stronger empirical validation than the paper under review.

**Anchor comparison summary:**
- 9wjGUN65tY (5.00, R1/R2): The paper under review has a more original theoretical insight (equivalence between two paradigms vs. applying conceptors to steering) but similar empirical limitations.
- p85TNN62KD (5.50, R1/R2): Comparable in contribution scope—both extend influence-function theory to a new domain, both have empirical gaps. The paper under review's theory is more elegant; VIF's experiments are more thorough.
- ZPkNrs6aNO (5.50, R2): Similar tier of theoretical steering work with experiments; comparable.
- KjBG4JNOc2 (6.20, R1/R2): Has more thorough empirical validation, earning a higher score.
- esYrEndGsr (8.00, R1): Far stronger empirical validation across multiple settings; the paper under review does not approach this level of experimental completeness.
- dTQmayPKMs (6.33, R2): Strong applied contribution with real-world validation (RLHF); the paper under review lacks this level of empirical grounding.

**Final placement:** The paper's theoretical contribution is genuinely novel and well-constructed, placing it above the bottom of the middle band. However, the missing data-tracing demonstration—a central claimed practical contribution—and the under-explained detoxification experiment prevent it from reaching the 6.0+ range where papers have more complete empirical validation. I place it at 5.5, comparable to other theoretically novel but empirically incomplete papers in this space.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>