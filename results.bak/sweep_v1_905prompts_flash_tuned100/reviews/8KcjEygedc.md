Now I have sufficient information to calibrate. Let me write the final consolidated review.

**Round 1 Bracket:** The paper sits above the weak anchors (2.33–3.25, all clear rejects with fundamental issues) and below the strong anchors (7.6–8.0, papers with fully validated theoretical predictions against extensive experiments). The most comparable anchors sit at 5.5–6.0. Initial bracket: 4.5–6.5.

**Round 2 Narrowing:** Compared against the closest-matching anchor — "Maximizing the Potential of Synthetic Data" (5.50, Accept; RMT theory + experiments for pruning/synthetic data) — the current paper has a stronger theoretical result (Theorem 2 characterizing optimal strategy type, not just error curves) but weaker empirical validation (missing KH vs KE comparison in synthetic data, underspecified ImageNet setup). The current paper is slightly below that anchor on execution but slightly above on theoretical novelty. Another anchor, "Toward a Statistical Theory of Data Selection" (5.50, Accept), is very similar in format (theory + mixture of synthetic and real-world experiments) and shows similar reviewer disagreement (scores 1,8,5,8). The D² Pruning anchor (5.60, Accept) and Network Pruning anchor (6.00, Reject despite higher score due to a methodology-disconnect issue) confirm the 5.0–5.5 range.

**Final score:** 5.0. The paper's theoretical contribution is genuine, but the experimental validation has a central gap (no direct KH vs KE test in the controlled setting where it would be most informative) that prevents the paper from achieving the strong "empirically confirmed" claim made in the abstract. This is a borderline paper: real contribution, but the evidence as presented doesn't fully support the scope of the claims.

---

## Summary

This paper develops a high-dimensional theoretical framework for data curation in binary classification, deriving exact asymptotic test-error formulas (Theorem 1) under label-agnostic and label-aware pruning rules, and characterizing when "keep hard" vs. "keep easy" is optimal (Theorem 2): keep-hard wins when the generator is strong (ρ→1) and the pruner is excellent, while keep-easy wins when the generator is weak (ρ<1). The theory is validated on synthetic data (Figure 1 — theory-experiment curve matching), ImageNet (Figure 2 — KH vs KE crossover), and qualitatively connected to recent LLM reasoning results (LIMO, s1). A model-collapse mitigation experiment (Figure 3) shows that principled pruning stabilizes iterative self-training.

## Strengths

1. **Exact asymptotic test-error formula under pruning (Theorem 1).** The paper derives a closed-form expression for test error under label-agnostic pruning, characterized by four constants (p, γ, β, β̃) that capture the pruning rule's effect. This provides an analytical scaling law that goes beyond prior empirical demonstrations (Sorscher et al. 2022) and extends the theoretical literature (Feng et al. 2025, Firdoussi et al. 2024) by incorporating difficulty-based filtering. The formula is validated against synthetic experiments in Figure 1 with strong theory-experiment agreement.

2. **Provably optimal pruning strategy depends on generator quality (Theorem 2).** The paper proves that keep-hard is optimal when the generator is strong (ρ→1) and the pruner is excellent, while keep-easy is optimal when the generator is weak (ρ<1) — both under a fixed pruning ratio. This gives a rigorous, non-obvious condition for the "less is more" phenomenon and directly explains why the optimal strategy flips with generator strength. This is the paper's most distinctive theoretical contribution.

3. **Reconciliation of contradictory LLM reasoning findings (Section 4.2).** The theory provides a clean lens for understanding why LIMO/s1 (aggressive curation) improves average AIME performance while "more is more" holds for hard questions: the base LLM acts as a strong generator for average problems (high ρ) but a weak generator for hard problems (low ρ). This unification of previously separate empirical findings is elegant and genuinely useful for practitioners.

4. **Demonstration that curation prevents model collapse (Figure 3).** The iterative self-training experiment on ImageNet shows that "keep hard" pruning stabilizes error across rounds (~30% flat), while training on all data degrades from ~30% to ~52%. This provides concrete evidence that principled curation can avert the model collapse phenomenon, going beyond prior theoretical warnings.

## Weaknesses

### Major

1. **Synthetic experiment (Figure 1) does not test the theory's core prediction.** Theorem 2's headline claim is about when keep-hard (KH) beats keep-easy (KE) and vice versa. Yet the synthetic experiment compares KH against *random* pruning, not KE. Section 4.1 confirms this: "we compare a strategic 'keep hard' pruning strategy against a baseline 'random' selection." The bottom-left quadrant shows that KH beats random when the theory predicts KH should be optimal — but this is a much weaker test than comparing KH vs. KE directly. The crossover that distinguishes Theorem 2 from a trivial "informative pruner beats uninformative one" claim remains untested in the controlled setting where the theory could be cleanly validated. The ImageNet experiments *do* compare KH vs. KE and show the predicted pattern (Section 4.3, Figure 2), but these lack the controlled parameter variation (ρ, ρ_*) that synthetic data would allow. This gap substantially weakens the paper's claim to "empirically confirm our theoretical predictions" (abstract) for the paper's most novel result.

2. **ImageNet experiments are substantially underspecified (Section 4.3).** The description provides no details on: model architecture (ViT? ResNet?), training hyperparameters (optimizer, learning rate, epochs, regularization), how pseudo-labels are generated from the pre-trained model, how the oracle is constructed, the concrete thresholds defining "keep easy" and "keep hard" (which margin? which quantile?), the number of classes (binary or multi-class despite the binary theory), or the evaluation protocol. The rightmost subplot of Figure 2 shows "Error Rate vs Dataset Size" but the caption says it shows "Error Rate (%) from 0 to 50." Without these details, the experiments cannot be evaluated for soundness or reproduced. For a paper that claims to "bridge theory and practice," this is a significant methodological gap.

### Minor

3. **LLM connection is purely qualitative and post-hoc (Section 4.2).** Tables 1 and 2 are reproduced from existing work. The paper does not estimate any of its key parameters (ρ, ρ_*, ρ_g) from LLM data, does not run a single LLM experiment, and does not test whether the theory's quantitative predictions hold in that domain. The section provides a plausible narrative but no novel evidence. The paper should frame this section as "connections" or "implications" rather than as validation — the Limitations section partially acknowledges this, but the abstract's claim about providing "a principled explanation" for LLM results overstates what is done.

4. **Optimality claim is proven only in extreme limits.** Theorem 2 assumes ρ→1 (or ρ<1) and ρ_*→1, with the additional limit φ→0 and λ→0. Real oracles are never perfect (ρ_*<1), and finite samples (φ>0) with regularization (λ>0) are the norm. The paper does not discuss how the optimal strategy transitions as ρ_* degrades from 1 or as φ and λ become non-negligible. A brief discussion of finite-sample/finite-regularization behavior would help practitioners understand the robustness of the recommendation.

### Trivial

None.

## Nice-to-Haves

- Add a synthetic experiment directly comparing KH vs. KE as a function of ρ and ρ_*. This is the single highest-leverage improvement and would directly validate Theorem 2's central prediction.
- Provide full experimental details for the ImageNet experiments (architecture, training hyperparameters, pruning criterion thresholds, number of classes, evaluation protocol).
- Include an explicit worked example for Theorem 1 (e.g., the "keep all" case q≡1) so readers can see the formula in action and verify it recovers known results.
- Add error bars / confidence intervals for the ImageNet results, given the small number of data points in some plots.

## Removed Points

- **Criticism that the theory's assumptions are too strong and robustness is untested (Harsh Critic point 3).** The paper acknowledges these limitations explicitly (Section 6) and *does* test robustness via the ImageNet experiments, which violate the Gaussian-linear assumptions yet still show the predicted crossover. The LLM connection is framed as qualitative, which is appropriate for a theory paper. Weakness removed.
- **Criticism that the label-aware curation results (Theorem 3) are too thin in the main text (Harsh Critic point 4).** The paper states "Explicit formulae for the above constants are provided in the appendix" — this is standard practice for theory papers. The appendix is present in the original submission per our instructions; the parser strips it from all papers. Weakness removed.
- **Critique about missing proofs/details in the appendix (Harsh Critic's notes on Theorem 1).** Same reasoning: the appendix exists in the original submission.
- **Strength Finder's generic strength about "important problem."** Moved here as it is a generic sentiment applicable to many papers, not a strength specific to this paper's execution.
- **Strength about the paper being "well-written."** This is subjective and not an evidence-based strength of the contribution.

## Novel Insights

The most interesting observation from the reviews that goes beyond the paper's own contributions is the structural tension between the theory's strongest result (Theorem 2's precise characterization of when KH vs KE is optimal) and the experiments chosen to validate it. The synthetic experiments validate a *different* prediction (theory-experiment curve matching for KH vs random) than the one the paper most wants to claim (KH vs KE optimality). This suggests the authors may have prioritized demonstrating the tractability/accuracy of their asymptotic formulas over testing the paper's most distinctive and practically relevant claim. The ImageNet experiments fill this gap partially, but their underspecification prevents a clean evaluation. A more systematic experimental strategy — testing the KH/KE prediction directly in the synthetic setting where the theory's parameters (ρ, ρ_*, ρ_g) are fully controlled — would substantially strengthen the paper's evidential core.

## Suggestions

1. **Add a synthetic experiment comparing KH vs. KE directly** as a function of ρ (generator quality) and ρ_* (pruner quality). A phase diagram showing the optimal strategy frontier would directly validate Theorem 2 and be the paper's most compelling figure.
2. **Provide full ImageNet experimental details** in the main text or a clearly referenced appendix section: model architecture, training setup, pruning criterion, number of classes, evaluation protocol.
3. **Reframe the LLM connection** as "illustrative implications" rather than "validation" or "explanation." The theory genuinely sheds light on why LIMO/s1 work, but the paper should be transparent that this is a post-hoc interpretation, not an empirical test.
4. **Discuss the finite-φ, finite-λ behavior** of the optimal strategy. Even a brief remark about how the optimal strategy transitions away from the limiting regime would help practitioners.

## Score and Decision

**Calibration Anchors Used (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 2NwHLAffZZ (Weak Correlations) | 2.33 | R1 | Much weaker — unclear contribution, no clear empirical support |
| EOPLy80bBm (Data Pruning for Fine-Tuning) | 3.00 | R1 | Weaker — more applied, less theoretical depth |
| e2F0mJJeN0 (GM Matching) | 3.00 | R1 | Weaker — lacks clear theoretical contribution |
| vQIVbfTMzf (Finite-sample adaptation) | 3.25 | R1 | Unrelated topic, lower quality |
| HhfcNgQn6p (Statistical Theory of Data Selection) | 5.50 | R1 | Comparable — similar structure (theory + mix of synthetic/real experiments), accepted despite reviewer disagreement |
| I9Dsq0cVo9 (Maximizing Synthetic Data - RMT) | 5.50 | R1/R2 | Most similar anchor — RMT theory + pruning experiments, accepted; current paper has stronger theory (Theorem 2) but weaker empirics |
| Bk13Qfu8Ru (Severing Spurious Correlations) | 7.00 | R1 | Stronger — extensive experiments, clear practical relevance |
| FT4gAPFsQd (How Sparse Can We Prune) | 6.00 | R1 | Slightly stronger in experimental validation but rejected due to methodology-disconnect |
| Tzh6xAJSll (Scaling Laws for Associative Memories) | 7.60 | R1 | Stronger — comprehensive theory + experiments |
| 5t57omGVMw (Learning to Relax) | 8.00 | R1 | Stronger — rigorous theory with practical algorithms |
| et5l9qPUhm (Strong Model Collapse) | 8.00 | R1 | Stronger — more thorough theoretical development, though rejected |
| zxqdVo9FjY (Generalization for LR with Spiked Covariances) | 4.80 | R2 | Slightly weaker — more narrow contribution |
| 9ccZzuix2D (Distilling Knowledge in Data Pruning) | 5.33 | R2 | Comparable — empirical pruning paper with some theory |
| Piod76RSrx (Slicing MI bounds) | 5.50 | R2 | Less relevant topic, comparable quality |
| thbtoAkCe9 (D² Pruning) | 5.60 | R2 | Similar in scope but more empirical; accepted |
| Rz4UkJziFe (Medium-Difficulty Samples) | 5.75 | R2 | Similar applied pruning topic |
| icTZCUbtD6 (Dissecting Sample Hardness) | 6.20 | R2 | More comprehensive empirical study |

The paper's most relevant comparator is I9Dsq0cVo9 (5.50, Accept — RMT theory of synthetic data + pruning). The current paper has a stronger theoretical result but weaker empirical validation, placing it slightly below that anchor. Round-2 narrowing confirms the paper fits in the 4.5–5.5 range.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>