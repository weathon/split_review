## Summary

This paper develops a theoretical framework for data curation in high-dimensional Gaussian binary classification with ridge regression. It derives exact scaling laws for test error under label-agnostic and label-aware pruning rules, proving a phase transition (Theorem 2) where "keep hard" is optimal when the generator is strong (ρ→1) and "keep easy" when it is weak (ρ<1). The paper connects these results to ImageNet experiments and recent LLM reasoning findings (LIMO/s1).

## Strengths

- **Exact analytical phase transition for optimal pruning (Theorem 2, Section 3.1):** Theorem 2 provides precise, provable conditions determining when "keep hard" vs. "keep easy" minimizes test error, expressed cleanly via geometric alignment constants (ρ, ρ_*, ρ_g). This goes beyond prior empirical work (Sorscher et al., 2022) which showed pruning can bend scaling curves but did not derive exact phase boundaries.

- **Label-aware curation model subsuming prior work (Remark 1, Theorem 3, Section 3.2):** The label-aware curation rule (Eqn 6) jointly considers label correctness and example difficulty, generalizing the setups of Feng et al. (2025) and Firdoussi et al. (2024) as a special case (q≡1). Theorem 3 delivers exact test error for this more general setting, which directly models practical pipelines like LIMO and s1 that filter for both correctness and difficulty.

- **Theory-grounded demonstration that curation can mitigate model collapse (Figure 3, Appendix C):** The paper shows that "keep hard" pruning stabilizes iterative pseudo-labeling while training on all data degrades, giving a principled explanation grounded in Theorem 2(B). This provides a theoretically-motivated alternative to existing heuristic approaches for preventing collapse.

## Weaknesses

### Fatal
None.

### Major
- **Overclaimed "rigorous justification" for LLM methods (Section 4.2, lines 26–27, 198–232):** The paper claims to provide "a rigorous justification for why methods like LIMO and s1 succeed" (line 27). However, the LLM analysis in Section 4.2 is post-hoc reinterpretation without independent measurement of any theoretical parameter (ρ, ρ_*, ρ_g). When "less is more" works on average AIME, the generator is posited to be "strong"; when "more is more" works on hard AIME, the same generator is posited to be "weak." The theory is compatible with either outcome because ρ is never estimated from data—it is assigned post-hoc to fit each observation. A genuine test would require estimating ρ from the base LLM's performance on the relevant test slice and predicting whether keep-hard or keep-easy should be optimal. The paper does not do this, making the claimed "resolution" a conceptual analogy rather than a validated prediction. This gap between what is claimed ("rigorous justification") and what is actually established (qualitative consistency with existing observations under unmeasured parameters) is significant.

### Minor
- **Headline result (Theorem 2) derived in a specific limiting regime (lines 141–143):** Theorem 2's optimality characterization relies on the data-rich, unregularized limit (ϕ→0, λ→0). The paper is transparent about this, but it means the central practical insight is rigorously established only outside settings where regularization or data-limitation matters—regimes common in practice. The extent to which the phase transition survives finite-ϕ, finite-λ settings is unclear from the main text.

- **Isotropic Gaussian assumption limits quantitative reach (line 58):** The main results assume identity covariance for features (C_g = Σ = I_d). While the paper acknowledges this and defers general results to the appendix, the gap between isotropic Gaussian binary classification and structured high-dimensional data (images, text) is substantial. This limits how directly the theory's quantitative predictions transfer to the real-world settings the paper discusses.

- **Synthetic experiment reporting is sparse (Section 4.1, Figure 1):** Figure 1 shows qualitative agreement between theory and simulation, but the paper does not report numerical fit metrics (e.g., RMSE between theoretical and empirical error curves), systematic variation of key parameters (ρ, ρ_g, ρ_*, n, d, ϕ, λ), or statistical significance across multiple random seeds. This makes it hard to assess how precisely the theory matches simulations beyond visual inspection.

### Trivial
None.

## Nice-to-Haves
- Discuss how practitioners could estimate ρ in practice to determine which regime they are in.
- For the synthetic experiments, provide quantitative fit metrics and show systematic parameter variation.
- The paper mentions "more general results in the appendix"—if these include non-isotropic covariances, summarizing the key takeaway in the main text would strengthen the narrative.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Missing experimental details for ImageNet/model collapse experiments:** The harsh critic argues that ImageNet and model collapse experiments lack architecture, hyperparameters, training details. However, the paper states "For a comprehensive set of validations, please see Figure 4 and Appendix B" (line 173), and the model collapse analysis is deferred to Appendix C. Since the appendix was stripped by the parser, these details likely exist in the original submission. Per hard rules, weaknesses about missing appendix content are removed.

- **Theorem 1 and Theorem 3 are opaque without appendix:** The detailed formulas for m, \tilde{m}, r are in the appendix and proof sketches are brief. The parser strips appendix content from all papers; conveying full derivations in the main text is standard for theory papers at this venue. Removed per hard rules.

- **Model collapse analytical underdevelopment in main text:** The analytic content is in Appendix C (stripped). Removed.

- **Framing of scaling laws as "reductive" / straw-man tension:** Editorial opinion about how the paper frames prior work, not a substantive weakness.

- **Strength about "unified resolution of LLM reasoning findings":** This conflicts with the verified Major weakness that the LLM analysis is post-hoc reinterpretation without independent parameter measurement. Per the rule "when a strength and weakness disagree, the weakness wins," this strength is removed from the main list.

## Novel Insights
The most interesting observation from the review synthesis is the asymmetry between the strength of the theoretical contribution and the thinness of the empirical bridge to LLMs. The paper has a genuinely crisp theoretical result (Theorem 2) that cleanly separates regimes, but the LLM discussion operates at a level of abstraction (qualitative consistency) that does not match the precision of the theory. The paper would be more coherent if it either measured ρ in an LLM setting or explicitly positioned the LLM discussion as an intuitive analogy rather than a validation.

## Suggestions
1. Reframe the LLM discussion (Section 4.2) from "rigorous justification" to "qualitative consistency / conceptual analogy." Either independently estimate ρ, ρ_*, ρ_g from LLM data and show the theory predicts the observed outcomes, or be explicit that this is an interpretative lens, not a validation.
2. Provide numerical fit metrics (e.g., RMSE) for the synthetic experiments in Figure 1 and show systematic variation of the key parameters.
3. Clarify in the abstract and contributions that the ImageNet experiments are qualitative illustrations consistent with the theory, not rigorous empirical validation.

## Score and Decision

**Round 1 bracket:** 4.0 – 6.5 (informed by comparing against low-scoring heuristic pruning papers ~3.0, mid-range theory papers ~5.5, and strong theory papers ~8.0)

**Round 2 narrowing anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `I9Dsq0cVo9.md` (Maximizing Potential of Synthetic Data) | 5.50 | 1,2 | Similar RMT+Gaussian approach to synthetic data pruning. Current paper has cleaner core insight (Theorem 2 phase transition) but also clearer overclaiming issue. Current paper is slightly weaker. |
| `MQXrTMonT1.md` (Beyond Model Collapse, Feng et al. 2025) | 6.50 | 2 | Direct prior work. More thorough experiments (transformers, LLMs), less overclaiming. Current paper has broader theoretical scope but weaker empirical validation. Current paper is noticeably weaker. |
| `Xr5iINA3zU.md` (Collapse or Thrive?) | 5.75 | 2 | Studies model collapse with thorough multi-setting experiments. Current paper has more novel theoretical contribution but less experimental breadth. Roughly comparable with slight edge to current paper in theory novelty. |
| `93XT0lKOct.md` (Data Pruning by Information Maximization) | 6.00 | 2 | Empirical method paper with strong experiments. Different type of contribution (practical method vs. theory). |
| `et5l9qPUhm.md` (Strong Model Collapse) | 8.00 | 1 | Significantly stronger theoretical and empirical execution. Current paper is well below this level. |

**Final score determination:** The paper's theoretical contribution (Theorem 2) is genuinely novel and well-motivated, placing it above 4.0. However, the overclaiming on LLM "rigorous justification" (a verifiable weakness from the paper as written) and thin empirical validation keep it below the 5.5–6.0 range inhabited by comparable papers with stronger execution. The most comparable anchor is "Maximizing Potential of Synthetic Data" (5.50), which has similar methodology and weaknesses but lacks the overclaiming issue. The current paper's cleaner core insight (Theorem 2) is offset by its clearer overclaiming. I place it at **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>