Now I have all the anchors I need. Let me write the consolidated review.

---

## Summary

This paper develops a theoretical framework based on random matrix theory to analyze data curation strategies in high-dimensional binary classification. The authors derive exact asymptotic scaling laws for test error under both label-agnostic and label-aware pruning (Theorems 1, 3) and characterize which curation strategy — "keep hard" vs. "keep easy" — is optimal as a function of generator quality (Theorem 2). The framework is used to explain contradictory findings in LLM mathematical reasoning (LIMO/s1 vs. scaling-law results) and validated on ImageNet, where the predicted crossover between curation strategies is observed. The paper also shows how principled curation can mitigate model collapse in iterative training.

## Strengths

- **Rigorous asymptotic theory for data curation**: Theorems 1 and 3 provide exact closed-form characterizations of test error under label-agnostic and label-aware pruning in the high-dimensional proportionate limit. The derivations, using random matrix theory, are sound under the stated assumptions and represent a genuine theoretical advance over prior work (Feng et al., 2025; Firdoussi et al., 2024).

- **Clear characterization of optimal pruning strategy**: Theorem 2 analytically proves that when the data generator is strong (ρ → 1), "keep hard" uniquely minimizes test error at fixed pruning ratio p; when the generator is weak (ρ < 1), "keep easy" is optimal. This provides a principled answer to the question of *which type* of data to keep.

- **Empirical validation of strategy crossover on ImageNet**: Figure 2 convincingly demonstrates the predicted regime-dependent crossover — by varying the initial training set size (160K vs. 1.2M examples), the optimal strategy shifts from "keep easy" (weak generator) to "keep hard" (strong generator), matching the theoretical prediction.

- **Unifying interpretation of LLM reasoning results**: The framework provides a coherent explanation for why LIMO/s1 (aggressive curation of hard examples) improves average AIME performance while "more is more" holds for the hardest AIME problems — by mapping these to high-ρ and low-ρ regimes respectively.

- **Geometrically interpretable quality parameters**: The alignment constants ρ, ρ_*, ρ_g (Eqn. 7) map directly to test error via arccos, giving practitioners an intuitive, quantitative language for discussing generator and oracle quality.

- **Model collapse mitigation**: Figure 3 shows that "keep hard" pruning stabilizes iterative training, preventing the performance degradation seen when training on all pseudo-labeled data.

## Weaknesses

### Major

- **Gap between abstract claims and delivered theoretical results**: The abstract promises "analytical conditions" and "precise phase transition curves tied to data size and quality" for when p < 1 outperforms p = 1. However, Theorem 2 optimizes over pruning *strategies* (q) at a *fixed* pruning ratio p — it tells you whether to keep hard or easy examples at a given p, not what p is optimal. The finding that p < 1 can beat p = 1 is demonstrated only numerically in Figure 1 (bottom-left panel), using the theory's formulas, but no analytical phase boundary or closed-form condition is derived. This means a reader looking for the promised "analytical conditions for when less is more" will find a numerical demonstration, not a theorem. The contribution is genuine but overstated in its current framing.

### Minor

- **ImageNet experiments do not directly test p < 1 vs. p = 1**: The ImageNet experiments (Figures 2–3) validate which curation *type* is preferred under different generator strengths at fixed pruning ratios, but they do not show that pruning to p < 1 can outperform training on the full dataset (p = 1). The paper's framing in Section 4.3 and the abstract slightly overstates what the ImageNet results establish relative to the "less is more" headline. The model collapse experiment (Figure 3) is interesting but orthogonal to the p < 1 optimality question.

- **LLM reasoning section is interpretive, not empirical validation**: Section 4.2 applies the theoretical framework post hoc to explain existing results from LIMO, s1, and Sun et al. (2025). The mapping from "base LLM quality" to ρ is qualitative and not quantified. This section is insightful as an illustration but should not be presented as validation of the theory — it is an interpretation. The paper currently treats it somewhere in between.

- **The F(q) limit lacks robustness discussion**: Theorem 2's optimal strategy result uses the triple limit φ → 0, λ → 0, d,n → ∞ (Eqn. 12) to define the error functional F(q). The paper treats this as the "data-rich, unregularized regime" without discussing whether finite-n or finite-λ effects could reverse the conclusions (e.g., could "keep hard" be suboptimal at finite regularization even when ρ → 1?). A brief remark would strengthen the exposition.

### Trivial

- Figure 4 and Appendix B are referenced for "comprehensive validations" but the appendix is not included in the review copy (parser artifact). The main text would benefit from summarizing the key additional findings.

## Nice-to-Haves

- Deriving an analytical phase boundary (even in simplified form, e.g., in the φ → 0, λ → 0 limit) for when p < 1 is optimal vs. p = 1 would close the gap between the abstract's promises and the delivered theory. A phase diagram with derived boundaries would significantly strengthen the paper.
- Extending the ImageNet experiments to show a U-shaped error curve as a function of p (for a strong generator) would directly validate the central "less is more" claim in a realistic setting.
- Quantifying ρ for the LLM reasoning case (e.g., using the base model's per-problem accuracy to estimate ρ) would strengthen Section 4.2.

## Removed Points

*These points were flagged for removal; treat them with caution.*

- **Missing d, λ, φ values for Figure 1 simulations**: These may be specified in the stripped appendix. The main text does not report them explicitly, but per the review protocol, missing appendix content is not a valid criticism.
- **Missing ImageNet implementation details (architecture, hyperparameters)**: These are likely in the stripped appendix. The paper references using a pre-trained model as generator/pruner in a standard ImageNet setup; the stripped appendix presumably contains the details.
- **"Should discuss robustness of finite-n effects" framed as a fatal gap**: This was speculative (the harsh critic didn't demonstrate that finite-n effects would actually reverse conclusions) and has been demoted to Minor.
- **"Only one simulation regime shown"**: The paper shows four regimes in a 2×2 grid (Figure 1), which is sufficient for its purposes.

## Novel Insights

The paper's most novel theoretical insight is that the optimal curation strategy undergoes a sharp transition governed entirely by generator quality ρ: for ρ → 1, keep the hardest examples; for ρ < 1, keep the easiest. This clean dichotomy, proven analytically in the high-dimensional limit, provides a unifying principle that had not been formalized in prior work. The corollary that aggressive curation (keep hard) can prevent model collapse is also genuinely novel — it reframes curation not merely as an efficiency tool but as a stability mechanism for iterative training.

## Suggestions

- **Re-scope the claims in the abstract and introduction**: Replace "analytical conditions" and "phase transition curves" with language that accurately reflects what is delivered — e.g., "exact asymptotic formulas that reveal when keep-hard vs. keep-easy strategies are optimal, and numerical phase diagrams showing when pruning beats full-data training." This would eliminate the mismatch without changing any content.
- **Add a brief numerical phase diagram**: Using the exact formulas from Theorem 1, compute and plot the optimal p as a function of (ρ, φ, n) across a grid. Even as a purely numerical result derived from the exact theory, this would substantiate the "less is more" claim far better than the single data point in Figure 1.
- **Clarify the status of Section 4.2**: Explicitly label the LLM reasoning section as "interpretation" or "illustration" rather than validation, and acknowledge the qualitative nature of the ρ mapping.
- **Discuss the F(q) limit briefly**: Add one sentence on whether finite-λ or finite-φ effects could reverse the Theorem 2 conclusions in practically relevant regimes.

## Score and Decision

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| I9Dsq0cVo9 | Maximizing the Potential of Synthetic Data | 5.50 | R1 | Closest comparable — same RMT approach, similar setting. Our paper is stronger (broader theory, ImageNet experiments, LLM connection, model collapse). |
| FT4gAPFsQd | How Sparse Can We Prune A Deep Network | 6.00 | R1/R2 | Theoretical pruning phase transition paper, rejected. Similar score range, different topic. |
| O6znYvxC1U | Bayesian Treatment...Neural Networks | 6.33 | R2 | RMT-based theory, accepted. Good theory, limited experiments. Our paper has more empirical validation. |
| Bk13Qfu8Ru | Severing Spurious Correlations with Data Pruning | 7.00 | R1 | Accepted. Strong empirical contribution on data pruning. Different type of paper (empirical vs. theoretical). |
| wFD16gwpze | Analyzing Neural Scaling Laws | 7.33 | R2 | Accepted. Rigorous theory paper that delivers precisely what it promises. Our paper has a claim-evidence gap that this paper avoids. |
| et5l9qPUhm | Strong Model Collapse | 8.00 | R1 | Same research group, RMT-based, more polished. Our paper is clearly below this. |

**Round 1 bracket**: 5.5–7.5, with most mass in 6.0–7.0.

**Round 2 narrowing**: The paper sits above I9Dsq0cVo9 (5.50) — which is the most similar anchor — because it offers broader theory, real-data experiments, and a compelling narrative. It sits below wFD16gwpze (7.33) because of the gap between abstract/intro promises and delivered theory, and because the ImageNet experiments don't directly test the "less is more" claim. Within the 6.0–6.5 range, the paper is comparable to O6znYvxC1U (6.33) in terms of theoretical rigor and experimental scope.

**Final score**: 6.0. The paper makes a solid theoretical contribution (exact scaling laws, optimal strategy characterization) with genuine empirical validation and insightful connections to practice. However, the headline promise of "analytical phase transition curves" for when p < 1 beats p = 1 is not delivered in the main text — the finding is numerical, not analytical. This gap between claims and delivery, while not fatal, prevents the paper from reaching the 7+ range where papers that fully deliver on their promises reside. The score reflects a paper that should be accepted after modest revisions to align claims with delivered content, or after strengthening the analytical derivation of the optimal pruning fraction.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>