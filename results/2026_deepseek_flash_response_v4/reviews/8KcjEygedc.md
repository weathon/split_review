Now I have all the calibration data I need. Let me finalize the review.

## Summary

This paper develops a theoretical framework for data curation in high-dimensional binary classification, deriving exact scaling laws for test error under difficulty-based pruning oracles (Theorem 1) and characterizing a sharp phase transition where "keep hard" outperforms "keep easy" when the generator is strong, and vice versa when the generator is weak (Theorem 2). The theory is validated on synthetic data and ImageNet, and used as an interpretive lens for recent LLM reasoning results (LIMO, s1) where the same model shows different optimal strategies on average vs. hard problems.

## Strengths

- **Theorem 1 provides an exact closed-form test error for difficulty-based pruning, generalizing prior work.** Prior RMT analyses (Feng et al. 2025; Firdoussi et al. 2024) only handled label-checking oracles ($q \equiv 1$). This paper extends the analysis to oracles that assess example difficulty, characterizing any pruning strategy via four scalar constants ($p, \gamma, \beta, \tilde{\beta}$). This is a genuine technical advance over the prior state of the art.

- **Theorem 2 proves a sharp, actionable phase transition.** The result that keep-hard is optimal when both generator and pruner are excellent ($\rho \to 1, \rho_* \to 1$) while keep-easy is optimal when the generator is poor but the pruner is excellent ($\rho < 1, \rho_* \to 1$) is a precise, testable prediction that prior work did not provide. It gives practitioners a concrete condition for when to curate aggressively.

- **ImageNet validation at scale (Figure 2) demonstrates the predicted crossover.** The experiment shows the theory's qualitative phase transition holds on a real large-scale vision benchmark: with 160K examples (weak generator) keep-easy wins; with 1.2M examples (strong generator) keep-hard wins. This is the paper's strongest empirical contribution.

- **Model collapse experiment (Figure 3) shows that strategic pruning stabilizes iterative self-training.** While training on all pseudo-labeled data causes error to climb from ~30% to ~52% over 6 rounds, the "keep hard" strategy holds error steady at ~30–32%. This provides practical evidence for the theory's implications beyond one-shot efficiency.

## Weaknesses

### Major

- **Theorem 2 requires $\rho_* \to 1$, a condition the experiments do not fully realize and the paper does not acknowledge as a limitation.** Both parts of Theorem 2 assume the pruning oracle is essentially perfect ($\rho_* \to 1$). In the synthetic experiments (footnote 1), $\rho_* = \rho$, so this holds when $\rho = 1$ (strong generator, left column of Figure 1) but fails when $\rho < 1$ (poor generator). In the ImageNet experiments, the same model serves as both generator and pruner, so $\rho_*$ degrades with $\rho$. The paper never discusses this gap, nor does it test whether the theory's predictions are robust when $\rho_* < 1$. This matters because Theorem 2 is the paper's most practically consequential result—the central prediction of when to keep easy vs. hard—yet its formal guarantees apply in a regime the experiments only partially realize.

- **The claim that the theory "resolves" the LLM paradox overstates the evidence.** Section 4.2 maps average-AIME performance to the strong-generator regime and hard-AIME performance to the weak-generator regime, invoking the theory as explanation. This is a post-hoc interpretation with no measurement or estimation of $\rho$ for the Qwen2.5-32B model, no control for confounds (different data sources, base models, and evaluation protocols across Tables 1-2), and no tested predictions. The framing of "resolves" (line 204) and "principled explanation" (abstract) implies stronger evidence than the paper provides. Downgrading to "is consistent with" or "provides an interpretive lens for" would match the evidence.

### Minor

- **Synthetic experiment parameters are underspecified.** Section 4.1 does not state the exact $\rho$ value for the "poor generator" regime, the dimension $d$, the regularization $\lambda$, or the number of random trials. The visual "match between our theoretical predictions and the empirical results" is reported without numerical goodness-of-fit metrics. These details are needed for reproducibility and assessment.

- **The optimal strategy in Theorem 2 requires a specific limit order ($\phi \to 0$, then $\lambda \to 0$).** The data-rich, unregularized regime is the only one analyzed for Theorem 2. The paper does not discuss whether the optimal strategy changes for finite $\phi$ or finite $\lambda$, which would be the regime practitioners operate in.

- **The $\rho_* \to 1$ assumption is not mentioned in the Limitations section (Section 6).** This is the most significant constraint on the theory's applicability, yet it is absent from the discussion.

### Trivial

- The pruning ratio $p$ is defined abstractly but never connected to the threshold $\alpha$ for keep-easy/keep-hard strategies, making it harder to interpret the x-axes of Figures 1-2.

## Nice-to-Haves

- Running synthetic experiments under the $\rho_* \to 1$ condition (Theorem 2's formal regime) and then systematically relaxing $\rho_*$ to test robustness would substantially strengthen the empirical validation.
- Measuring or estimating $\rho$ and $\rho_*$ in the ImageNet experiments (rather than inferring them indirectly from $n$) would enable quantitative verification of the theory's predictions, not just qualitative trend-matching.
- Error bars or variance statistics across the ImageNet results would improve reproducibility assessment.

## Removed Points

These points were raised in the inputs but do not survive verification against the paper:

- **"Theorem 1's key functions ($m, \tilde{m}, r$) are not specified in the main text"** — This is standard practice for theoretical papers with page limits and appendix structure. The paper states they are "explicitly determined by the constants in Eqn (8)" and identifies $m$ as the Stieltjes transform of a deformed Marchenko-Pastur law. The structure of the result is clear from the main text.
- **"Relation to prior work under-explained"** — Remark 1 explicitly states that Feng et al. (2025) and Firdoussi et al. (2024) are special cases where $q \equiv 1$. This is a clear and sufficient comparison.
- **"None of the experiments satisfy the $\rho_* \to 1$ condition"** — When $\rho = 1$ (strong generator, left column of Figure 1), the synthetic experiments set $\rho_* = \rho = 1$, which does satisfy the condition. The critic overstated this.
- **"No error bars"** — Figure 1's caption explicitly mentions "empirical results with error bars."

## Novel Insights

The harsh critic's structural observation—that Theorem 2's most practically relevant prediction (when to keep easy vs. hard) is proven only under $\rho_* \to 1$, yet the paper never discusses this limitation or tests robustness to violations—is the most important insight from the review process. Combined with the strength finder's correct identification of the ImageNet crossover as the single most compelling piece of evidence, the key takeaway is that the paper's core theoretical framework is sound and its large-scale validation is genuinely impressive, but the paper overreaches in its LLM claims and under-acknowledges the gap between Theorem 2's formal assumptions and the experimental (and practical) regimes.

## Suggestions

1. Explicitly discuss the $\rho_* \to 1$ assumption as a limitation in Section 6, and ideally add a synthetic experiment that tests Theorem 2 under this condition and then relaxes $\rho_*$ to probe robustness.
2. Downgrade LLM claims from "resolves" (line 204) and "principled explanation" (abstract) to "is consistent with" or "provides a possible interpretive lens for," and acknowledge confounds across Tables 1-2.
3. Report specific numerical values for all synthetic experiment parameters ($d$, $\lambda$, exact $\rho$ values, number of trials) in the main text.
4. Clarify the relationship between pruning threshold $\alpha$ and pruning ratio $p$ for the keep-easy/keep-hard strategies.

## Score and Decision

### Calibration Anchors

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Firdoussi et al. ("Maximizing the Potential of Synthetic Data") | I9Dsq0cVo9 | 5.50 | R1/R2 | Directly comparable prior work; this paper extends and improves upon it with difficulty-based pruning and stronger empirical validation → current paper is **stronger** |
| "Effective pruning of web-scale datasets" | CtOA9aN8fr | 5.25 | R2 | Empirical pruning paper; less theoretical depth → current paper is **stronger** |
| "Improving Data Efficiency via Curating LLM-Driven Rating Systems" | DKkQtRMowq | 5.75 | R2 | Method paper with broader LLM eval but less theory → current paper is **comparable** |
| "How Sparse Can We Prune A Deep Network" | FT4gAPFsQd | 6.00 | R1/R2 | Network pruning theory paper (Rejected despite score); different subarea but similar level of theory → current paper is **comparable** |
| GIO ("Gradient Information Optimization") | 3NnfJnbJT2 | 7.00 | R2 | Well-executed data selection paper with broad experiments; current paper's theory is deeper but validation narrower and overclaiming is worse → current paper is **weaker** |
| DRoP ("Distributionally Robust Pruning") | fxv0FfmDAg | 7.33 | R2 | Strong data pruning paper with theory and comprehensive experiments → current paper is **weaker** |
| "Scaling Laws for Associative Memories" | Tzh6xAJSll | 7.60 | R1 | Clean theoretical paper with extensive validation, no overclaiming issues → current paper is **weaker** |

**Round 1 bracket:** Between 5.0 and 7.0.

**Round 2 narrowing:** Compared against anchors in the 5.25–7.33 range. The paper is stronger than the Firdoussi et al. prior work (5.50) and comparable to method papers at 5.75–6.00, but clearly weaker than well-executed papers at 7.00+ due to overclaiming on the LLM interpretation and the unacknowledged $\rho_* \to 1$ gap.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>