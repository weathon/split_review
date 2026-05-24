Now I have a thorough understanding of the paper and calibration anchors. Let me compose the final review.

---

## Summary

This paper develops a random matrix theory (RMT) framework for analyzing data curation (pruning) strategies in high-dimensional binary classification. It derives exact scaling laws for test error under both label-agnostic and label-aware curation rules, establishes a clean dichotomy (Theorem 2): aggressive "keep hard" pruning is optimal when the data generator is strong and data is abundant, while "keep easy" is optimal when the generator is weak. The framework is validated on synthetic data across a 2×2 grid of regimes, applied to explain recent LLM math reasoning results (LIMO/s1 vs. scaling), and demonstrated on ImageNet including model collapse prevention.

## Strengths

- **Clean theoretical contribution with an elegant core result.** Theorem 2 provides a precise, closed-form characterization of when "keep hard" vs. "keep easy" pruning is optimal, parametrized by generator quality ρ. The dichotomy (Part A: strong generator → keep hard; Part B: weak generator → keep easy) is non-obvious, falsifiable, and provides actionable guidance. The theory is internally consistent and mathematically rigorous.

- **Excellent synthetic validation matching theory precisely.** Figure 1's 2×2 grid (varying generator quality and data scale) shows solid theoretical predictions (lines) matching empirical results (dashed lines with error bars) across all four regimes. This provides convincing evidence that the RMT analysis is correct and that the "less is more" regime is real and precisely characterized.

- **Real-world ImageNet experiments confirming qualitative predictions.** Figure 2 demonstrates the crossover between "keep easy" (weak generator, 160K examples) and "keep hard" (strong generator, 1.2M examples) on a large-scale vision task, directly validating Theorem 2's predictions. Figure 3 shows that "keep hard valid" pruning prevents iterative model collapse from ~30% to ~52% error, stabilizing at ~30-32% across rounds.

- **Generality over prior work.** The label-aware curation setup (Equation 6) subsumes the label-verification settings of Feng et al. (2025) and Firdoussi et al. (2024) as special cases (Remark 1, q≡1), while adding the difficulty-based pruning dimension. This positions the contribution as a genuine generalization rather than a restatement.

## Weaknesses

### Fatal

None.

### Major

- **The LLM analysis (Section 4.2) overclaims: it provides a post-hoc qualitative narrative, not a principled prediction or test of the theory.** The paper's abstract claims the framework "provides a principled explanation for the contradictory curation strategies recently observed in LLM mathematical reasoning," and Section 4.2 states "Our theory resolves this cleanly." However, the entire Section 4.2 consists of re-narrating already-published results (Tables 1-2 from Muennighoff et al. 2025, Ye et al. 2025, Sun et al. 2025) through the lens of the theory: the base LLM is "strong" (high ρ) for average AIME → keep hard → LIMO wins; it is "weak" (low ρ) for hard AIME → keep all → scaling wins. This is an intuitive qualitative reinterpretation, not a derivation or prediction. The theory has no concept of question difficulty, chain-of-thought reasoning, or sequential token generation. Crucially, no procedure is offered or sketched for estimating ρ or ρ* in practice for an LLM. The mapping between theory and LLM practice is entirely hand-waved. If Section 4.2 were presented as a suggestive analogy rather than a "resolution," the paper would be more honest and arguably stronger. As written, this section undermines the paper's credibility by claiming explanatory power it does not deliver.

### Minor

- **Model collapse experiment (Figure 3) uses "keep hard valid" but Theorem 2 Part B predicts "keep easy" for weak generators — the paper does not clearly explain this tension.** The "hard valid" strategy combines label-aware pruning (removing mislabeled examples) with difficulty-based pruning (keeping hard examples). The theory predicts that for a *weak* generator, "keep easy" is optimal. The paper likely intends the label-verification component to effectively strengthen the generator, making "keep hard" then optimal — but this reasoning is never made explicit. The interaction between difficulty-based and label-based pruning in the collapse setting deserves theoretical analysis (which Theorem 3's machinery could provide) rather than just an empirical demonstration.

- **ImageNet experiments show qualitative agreement only; no theoretical curves are overlaid and no error bars are provided.** Figure 2 displays error rates vs. percentage of data kept but does not overlay the theoretical predictions from Theorem 1/Theorem 3. For a paper that emphasizes its theory's predictive power, this is a missed opportunity. Additionally, error bars/variance estimates are absent from Figure 2 (though they are present in the synthetic experiments of Figure 1), making it hard to assess the statistical significance of the modest differences between strategies (a few percentage points).

- **The ρ* → 1 assumption is strong and its effects are underexplored.** Theorem 2's main predictions assume both the pruner and generator have quality approaching perfection in their respective regimes. The paper states "In particular, for the main theoretical results (Theorem 2), we assume ρ* → 1." Real pruners are imperfect, and the effect of finite ρ* on the optimal strategy threshold is not characterized in the main text, though it presumably appears in the full formulas of Theorem 1 and the appendix.

### Trivial

None (formatting and style nitpicks excluded per policy).

## Nice-to-Haves

- Quantify or estimate ρ for a specific LLM on a specific task slice, showing that the estimated ρ predicts which curation strategy works better. This would transform Section 4.2 from interpretive to predictive.
- Overlay predicted scaling curves onto Figure 2 for the ImageNet experiments.
- Discuss the sensitivity of the crossover point (what fraction p to keep) to practical parameters like ρ* and ρ_g.
- Extend the model collapse analysis to explicitly handle the interaction between label-aware and difficulty-based pruning theoretically.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"The ImageNet experiments use a non-obvious setup"** — The critic flags that the pre-trained model serves as both generator and pruner using pseudo-labels, which differs from the theoretical assumptions. This is true but is a standard practical adaptation for connecting theory to vision experiments. The paper acknowledges the gap between theory and practice in its Limitations section. Removed as it is a known limitation of theory-to-practice bridging rather than an error.

- **"The LIMO/s1 tables are already published results, not novel experiments"** — While true that Tables 1-2 aggregate existing results, this is explicitly stated in the paper ("The following results are aggregated from existing literature"). The paper never claims to have run these experiments itself. This is not a weakness but a design choice for the interpretive section.

- **Strength Finder's claim #3: "Unified explanation of contradictory LLM math reasoning results"** — This conflicts with the verified major weakness that the LLM analysis is post-hoc and qualitative, not a principled resolution. Per the rules, when a strength and weakness disagree, the weakness wins.

- **Strength Finder's claim #4: "Principled model collapse prevention via pruning"** — Partially valid but the "hard valid" strategy used in Figure 3 does not cleanly match Theorem 2's prediction of "keep easy" for weak generators. Kept partially as a strength (the empirical result itself is real) but the "principled" claim is overstated.

## Novel Insights

The paper's central novel insight is the precise characterization of the "less is more" / "more is more" boundary in data curation: it is not about dataset size alone, but about the interplay between generator quality ρ and data scale n. This insight, formalized in Theorem 2, unifies seemingly contradictory empirical findings (LIMO, s1, classical scaling laws) under a single framework where the same base model can be "strong" for easy tasks and "weak" for hard tasks, predicting different optimal curation strategies. The extension to model collapse (showing that strategic pruning stabilizes iterative self-training) adds a second novel dimension, connecting one-shot data curation to long-term training stability.

## Suggestions

1. **Reframe Section 4.2 as interpretive analogy, not validation.** Change "Our theory resolves this cleanly" to language like "Our theory provides a lens to interpret these findings." Remove or substantially weaken the claim in the abstract that the framework "provides a principled explanation" for LLM results. This would strengthen the paper by making its honest contributions stand out rather than appearing to overreach.

2. **Add theoretical curve overlays to Figure 2.** Even approximate agreement would significantly strengthen the claim that the theory is predictive, not just post-hoc descriptive. If exact curves cannot be computed for the ImageNet setup, state this explicitly and explain why.

3. **Explicitly address the "keep hard valid" vs. "keep easy" tension in the model collapse experiment.** Explain why label-aware pruning (the "valid" component) changes the effective generator quality, making "keep hard" then optimal. This connects the experiment to Theorem 3 rather than leaving it as an apparent inconsistency with Theorem 2.

4. **Discuss the effect of finite ρ* on the main results.** At minimum, provide a qualitative sketch of how imperfect pruner quality shifts the optimal strategy boundary.

## Score and Decision

### Calibration Anchors

| Anchor ID | Topic | Avg Score | Round | Comparison |
|-----------|-------|-----------|-------|------------|
| EOPLy80bBm | Data pruning roles disentangling | 3.00 | 1 | Less theoretical depth, narrower scope |
| e2F0mJJeN0 | Robust data pruning (GM matching) | 3.00 | 1 | Less theoretical depth |
| gInIbukM0R | Emergence in NNs/pruning | 2.50 | 1 | Unrelated topic |
| lZRRfupxYn | Mesoscience for generalizability | 3.00 | 1 | Unrelated topic |
| CtOA9aN8fr | Effective pruning web-scale datasets | 5.25 | 1 | Empirical, less theoretical depth; paper under review is stronger |
| qUJsX3XMBH | Random selection for SFT data | 4.40 | 1 | Empirical; paper under review has much stronger theory |
| i9K2ZWkYIP | Scaling laws sparse foundation models | 7.00 | 1 | Comparable scaling law contribution; paper under review has cleaner core theorem but weaker practical connection |
| Bk13Qfu8Ru | Severing spurious correlations with pruning | 7.00 | 1 | Stronger practical results, weaker theory; different domain |
| HhfcNgQn6p | Statistical theory of data selection | 5.50 | 2 | Very similar topic; paper under review has cleaner Theorem 2 and broader scope |
| FT4gAPFsQd | How sparse can we prune (geometric) | 6.00 | 2 | Different domain but similar theoretical ambition |
| Piod76RSrx | Slicing MI generalization bounds | 5.50 | 2 | Different approach; paper under review is more focused |
| I9Dsq0cVo9 | Synthetic data RMT (Firdoussi et al.) | 5.50 | 2 | Same RMT framework, same group; paper under review generalizes it significantly |
| O6znYvxC1U | Bayesian treatment empirical kernel | 6.33 | 2 | Different application of RMT in ML |
| VoI4d6uhdr | Effective theory of bias amplification | 7.00 | 2 | Clean RMT theory with good practice connection; comparable quality |
| wFD16gwpze | Neural scaling laws two-layer networks | 7.33 | 2 | More focused and well-connected theory-to-practice; slightly higher quality |
| i9Vs5NGDpk | Sketched ridge ensembles RMT | 7.50 | 2 | Strong technical RMT contribution but different domain |
| Xr5iINA3zU | Collapse or thrive synthetic data | 5.75 | 2 | Paper under review addresses similar topic with stronger theory |
| P5UETqZXqT | Model collapse diffusion finetuning | 5.75 | 2 | Different domain; paper under review has stronger theory |
| mVCcWCjeEz | ToEdit text data model collapse | 6.25 | 2 | Paper under review has broader and cleaner theoretical framework |
| MQXrTMonT1 | Beyond model collapse verification | 6.50 | 2 | Predecessor paper by same group; paper under review extends it with generalization and Theorem 2 |

### Bracketing

**Round 1 bracket:** Between 5.5 and 7.0. The paper clearly exceeds the rejected papers (~3.0) and the 5.25 data pruning paper. It is comparable to but more theoretically ambitious than the HhfcNgQn6p (5.50) and I9Dsq0cVo9 (5.50) anchors. It is comparable to VoI4d6uhdr (7.00) and wFD16gwpze (7.33), but those have tighter theory-to-practice connections.

**Round 2 narrowing:** Between 6.0 and 7.0. The paper clearly exceeds the predecessor "Beyond Model Collapse" paper (MQXrTMonT1, 6.50) in theoretical generality (Theorem 2's dichotomy is novel and clean) and validation scope (ImageNet), but that predecessor has a tighter, more honest theory-to-practice connection with actual transformer and LLM experiments. The paper is comparable to VoI4d6uhdr (7.00) in RMT sophistication but has a weaker bridge between theory and the motivating application.

**Final score:** 6.5. The paper is a genuine, solid theoretical contribution with clean results (Theorem 2, Figure 1 validation), real-world ImageNet experiments, and a valuable model collapse connection. It clearly exceeds the 5.50 anchors (more general, cleaner core result, broader validation) and is comparable to the 6.50 predecessor paper which it extends. However, the significant overclaiming about LLM applications prevents it from reaching the 7.0+ range where the theory-to-practice connection is tight.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>