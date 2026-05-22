Now I have all the information needed to write the consolidated review.

Let me document my calibration anchors and finalize:

**Round 1 Bracket:** 4.5 – 7.5 (clearly stronger than the weak 2.6–3.0 data pruning papers; clearly weaker than the 7.6–8.0 scaling law papers on different topics).

**Round 2 Narrowing:** Most comparable anchors are at 5.50 (RMT synthetic data paper), 5.50 (data selection theory paper), and 7.00 (data pruning for spurious correlations). The current paper is meaningfully stronger than the 5.50 papers (broader theory, ImageNet validation, LLM interpretation) but not as empirically complete as the 7.00 paper. Score: **6.0**.

---

## Summary

This paper develops a theoretical framework for data curation in high-dimensional binary classification. It derives exact asymptotic test error under label-agnostic and label-aware pruning rules (Theorem 1), then proves a phase transition in the optimal curation strategy: "keep hard" is optimal when the generator is strong, while "keep easy" is optimal when the generator is weak (Theorem 2). The authors validate qualitative predictions on synthetic data (matching theory to experiment), on ImageNet (showing the predicted crossover between keep-easy and keep-hard), and use the framework to reconcile contradictory LLM reasoning results (LIMO/s1 vs. Sun et al.). They also demonstrate that strategic curation can prevent model collapse in iterative self-training loops.

## Strengths

1. **Exact analytical test error (Theorem 1)** — The paper derives a closed-form limiting test error for ridge regression under pruning oracles, using tools from random matrix theory. This provides a rigorous foundation for analyzing data curation that goes beyond heuristic arguments.

2. **Clean phase transition result (Theorem 2)** — The theorem proving that the optimal strategy switches from "keep hard" (strong generator) to "keep easy" (weak generator) is crisp, actionable, and directly addresses the paper's central question of when "less is more." The result is stated clearly and the conditions are explicit.

3. **Theory–experiment match across four regimes (Figure 1)** — The synthetic experiments show solid quantitative agreement between theoretical curves and empirical results for both "keep hard" and random pruning. The bottom-left quadrant (large n, strong generator) cleanly displays the predicted "less is more" optimum at p<1.

4. **Principled resolution of contradictory LLM findings (Section 4.2)** — The framework explains why LIMO/s1 (less is more on average AIME) and Sun et al. (more is more on hard AIME) are not contradictory: the generator quality ρ differs relative to the difficulty slice. This is a compelling demonstration of the theory's explanatory power beyond the paper's own experiments.

5. **Stabilization of model collapse (Figure 3)** — The demonstration that training on all data causes error to degrade from ~30% to ~52% while "keep hard" maintains performance around 30–32% is a clean and practically relevant illustration of principled curation breaking the model collapse cycle.

## Weaknesses

### Major

1. **Tension between Theorem 2(B) and the model collapse experiment.** The paper states (line 172) that keep-easy is the optimal strategy for weak generators (Theorem 2(B)) and notes that "this latter case is particularly relevant for mitigating model collapse, where a model trained on its own imperfect outputs acts as a poor generator." Yet Figure 3 uses "keep hard" to prevent collapse, with no comparison to "keep easy" and no discussion of why keep-hard is chosen over the theoretically predicted keep-easy. The paper's claim that "strategic pruning prevents model collapse" is supported for only one specific strategy, and the theory's own prediction for weak generators goes unaddressed. The authors should either (a) add a keep-easy baseline to the model collapse experiment, (b) explain why the specific regime (e.g., strong initial generator, high-quality fixed pruner) makes keep-hard appropriate even as the generator weakens, or (c) explicitly discuss the scope conditions.

2. **Synthetic experiments compare only "keep hard" vs. "random," omitting "keep easy."** Figure 1 compares only two strategies, yet Theorem 2 predicts that "keep easy" is optimal for weak generators. The right-hand quadrants (poor generator) are interpreted as "more is more" regimes based on comparison against random selection only. Without seeing how "keep easy" performs in these regimes, the empirical validation of Theorem 2 is incomplete — it is possible that "keep easy" would outperform p=1 in some regimes, altering the claimed interpretation. This gap is partially mitigated by the ImageNet experiments (Figure 2), which do compare keep-easy vs. keep-hard, but the synthetic validation should be complete on its own terms.

### Minor

3. **ImageNet experimental setup is under-described in the main text.** The paper specifies that "a pre-trained model" is used as generator and pruner, and that generator quality is controlled by its initial training set size, but provides no architectural details (architecture used, how pseudo-labels are generated, what "keep easy"/"keep hard" mean operationally — e.g., confidence thresholds, how α is set, whether pruning is one-shot or per-round for the collapse experiment). While the appendix presumably contains these details, the main text should include enough information for a reviewer to assess whether the experimental design is a faithful instantiation of the theoretical assumptions. A single paragraph describing the architecture, pruning procedure, and training protocol would suffice.

4. **No error bars on ImageNet experiments.** The synthetic experiments include error bars, but Figures 2 and 3 do not report error bars or confidence intervals. Given that the ImageNet results are central to the claim of bridging theory and practice, variability should be reported.

### Trivial

5. **Theorem 1's statement is opaque without the appendix.** The formulas (9)–(11) involve m, \tilde{m}, and r functions that are not defined in the main text, making the theorem uninterpretable without reading the appendix. A high-level statement of the functional form's dependence on the constants in Eqn (8) would improve readability.

## Nice-to-Haves

- Include a "keep easy" baseline in the synthetic experiments (Figure 1) to complete the validation of Theorem 2.
- Add a brief discussion of how finite φ and λ (finite data, non-zero regularization) affect the sharpness of the phase transition in Theorem 2, beyond the limit in Eqn (12).
- Clarify whether the limit λ→0 in Theorem 2 is compatible with the regularization used in synthetic/ImageNet experiments.

## Removed Points

The following points from the reviewers were removed or demoted:

- **"The ImageNet experiments are not independently verifiable from the main paper"** — The paper explicitly references the appendix for full details (Appendix B), which is standard practice for main-text page limits. This is a Minor weakness about presentation, not a methodological gap.
- **"The paper's theoretical contribution relies on random matrix theory. The proofs are in appendix... the core theoretical results are not fully verifiable from the main text"** — Proofs in the appendix are standard for theory papers. This is not a weakness.
- **"The paper does not compare to other strategies like keep-easy or random in the collapse setting"** — This was merged into Major weakness #1 (the model collapse tension), not removed. The original framing as a full separate weakness is addressed there.
- **"The pruning ratio p is controlled by α, which is fine"** — This was the critic acknowledging the setup is fine, not a weakness.
- **"The LLM interpretation is post-hoc and qualitative"** — The paper presents this as an interpretation ("the framework can interpret and unify"), not as a rigorous empirical test. This is within scope.
- Various formatting nitpicks and reproducibility concerns about hyperparameters.
- **"Statistical significance / error bars missing"** — Kept as a Minor weakness but toned down.

## Novel Insights

None beyond the paper's own contributions. The key insight — that the optimal pruning strategy undergoes a phase transition based on generator quality — is cleanly presented in the paper itself. The synthesis across reviewers does not surface additional novel angles.

## Suggestions

1. **Address the keep-hard / keep-easy tension in the model collapse experiment.** Either add a keep-easy comparison, or explain (with reference to the experimental regime) why the theorem's prediction for weak generators does not apply.
2. **Add a "keep easy" curve to the synthetic experiments in Figure 1.** This would complete the empirical validation of Theorem 2 and strengthen the paper's core empirical claim.
3. **Include a brief description of the ImageNet architecture and pruning protocol** (one paragraph) in the main text so the reader can assess the setup without consulting the appendix.
4. **Add error bars to Figures 2 and 3** to quantify variability in the ImageNet experiments.

## Score and Decision

**Calibration Summary:**
- Round 1 bracket: 4.5 – 7.5 (paper sits between weak data pruning papers at ~3.0 and strong scaling law papers at ~8.0)
- Round 2 anchors for narrowing:
  - "Maximizing the Potential of Synthetic Data" (avg 5.50) — closely related RMT theory paper; current paper is broader (label-aware curation, phase transition, ImageNet) → stronger
  - "Towards a statistical theory of data selection" (avg 5.50) — similar theoretical level; current paper has cleaner results and more compelling experiments → slightly stronger
  - "How Sparse Can We Prune" (avg 6.00) — theoretical pruning analysis; comparable rigor, different domain → similar quality
  - "Severing Spurious Correlations with Data Pruning" (avg 7.00) — stronger empirical validation but less theoretical depth → current paper is weaker on empirics
- Final score: **6.0** — The paper makes a substantive theoretical contribution with clean results (Theorem 2 in particular is novel and well-stated), and provides genuine empirical support despite clear evidential gaps. The weaknesses (missing keep-easy in synthetic experiments, tension in the model collapse setup, under-described ImageNet setup) are real but addressable and do not threaten the core theoretical contribution.

<score>6.0</score>
<decision>Accept</decision>