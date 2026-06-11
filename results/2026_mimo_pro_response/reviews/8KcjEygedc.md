Now I have enough calibration data. Let me write the final review.

**Reporting calibration anchors:**

| Anchor Paper | Avg Human Score | Decision | Round | Comparison |
|---|---|---|---|---|
| Strong Model Collapse (et5l9qPUhm) | 8.0 | Reject | R1,R2 | Same research group, RMT for model collapse; similar theoretical depth, our paper has broader validation |
| Scaling Laws for Precision (wg1PCg3CUP) | 8.0 | Accept | R1 | Scaling laws paper; more empirical, less theoretical |
| Scaling Laws for Associative Memories (Tzh6xAJSll) | 7.6 | Accept | R1 | RMT-based scaling laws; similar technical style |
| How Feature Learning Can Improve Neural Scaling Laws (dEypApI1MZ) | 7.2 | Accept | R2 | Theoretical scaling laws; comparable depth, our paper has broader validation |
| Analyzing Neural Scaling Laws in Two-Layer Networks (wFD16gwpze) | 7.33 | Accept | R2 | RMT scaling laws; similar scope |
| An Effective Theory of Bias Amplification (VoI4d6uhdr) | 7.0 | Accept | R1 | RMT exact formulas for ridge regression; very similar approach |
| Self-Consuming Generative Models Go MAD (ShjMHfmPs0) | 6.67 | Accept | R2 | Model collapse; empirical, less theoretical |
| Distilling the Knowledge in Data Pruning (9ccZzuix2D) | 5.33 | Reject | R1 | Data pruning; less theoretical, limited novelty |

**Round 1 bracket: 7.0 – 8.0.** The paper's theoretical contribution (RMT exact formulas + phase transition) is comparable to anchors at 7.0–7.6, with broader practical validation than most. The unquantified ρ in the LLM section and the label-aware theory gap prevent it from reaching the 8.0 tier.

**Round 2 narrowing: 7.0.** The paper sits at the level of "An Effective Theory of Bias Amplification" (7.0) — similar RMT approach, exact formulas, practical relevance — but with broader multi-domain validation. It does not reach the 7.5–8.0 tier because of the unquantified LLM interpretation and the label-aware theory gap.

---

## Summary
This paper develops a random matrix theory (RMT) framework for data curation in high-dimensional binary classification, deriving exact scaling laws for test error under label-agnostic and label-aware pruning strategies. The central result (Theorem 2) establishes a sharp phase transition: "keep hard" is optimal when the data generator is strong (ρ→1), while "keep easy" is optimal when it is weak (ρ<1). The framework is validated on synthetic data and ImageNet, and is used to explain contradictory findings in LLM math reasoning (LIMO/s1 vs. Sun et al.).

## Strengths
- **Sharp phase-transition characterization (Theorem 2, Section 3.1):** Derives a precise result showing the optimal pruning strategy flips based on generator quality, rigorously characterized over the set of all symmetric pruning strategies with fixed pruning ratio. This is a genuinely informative and elegant theoretical result.
- **Reconciliation of contradictory empirical findings in LLM reasoning (Section 4.2, Tables 1–2):** Provides a principled explanation for why LIMO/s1 succeed with aggressive pruning on average AIME (strong generator → "keep hard" optimal) while Sun et al. observe "more is more" on the hardest AIME questions (weak generator → scaling with data is better), connecting to real published results in a falsifiable way.
- **Empirical validation across synthetic, ImageNet, and LLM settings (Figures 1–3):** Controlled 2×2 grid (Figure 1) shows tight theory-empirics agreement. ImageNet experiments (Figures 2–3) confirm the predicted crossover between "keep easy" and "keep hard" as generator strength varies, and demonstrate that strategic pruning prevents model collapse across iterative self-training rounds.
- **Generality over prior RMT-based curation analyses (Remark 1):** Subsumes Feng et al. (2025) and Firdoussi et al. (2024) as special cases when q≡1, extending analysis to a strictly richer class of curation rules including difficulty-based pruning used by LIMO/s1.
- **Closed-form test error formula parameterized by interpretable constants (Theorems 1 and 3):** The exact test error depends on a small number of geometric quantities (ρ, ρ*, ρ_g, τ) with clean interpretations as cosines of angles between generator/oracle/ground-truth vectors (Eqn 7), making the theory practically legible.

## Weaknesses

### Fatal
None

### Major
- **LLM math reasoning interpretation relies on unquantified generator quality (Section 4.2):** The reconciliation of LIMO/s1 vs. Sun et al. hinges on asserting that the base LLM is a "strong generator" for average AIME problems and a "weak generator" for hard AIME problems, but the paper never measures or estimates ρ for the LLM on these problem slices. The text states "the base LLM is a **strong generator** (high ρ) for the majority of problems" (line 207) and "a **weak generator** (low ρ) relative to this difficult data slice" (line 230), but these remain unquantified assertions. In a framework where predictions depend on ρ relative to critical thresholds, this converts a principled explanation into a post-hoc narrative. Even a rough proxy measurement would substantially strengthen this section.

### Minor
- **Label-aware optimal-strategy result not stated in main text (Section 3.2):** The most practically relevant predictions (model collapse mitigation, LIMO/s1 justification) come from label-aware curation. The main text presents Theorem 3 (test error formula for label-aware curation) but defers the label-aware analogue of Theorem 2 (optimal strategy as a function of generator quality) entirely to the appendix ("Refer to the appendix for full proofs, various corollaries and their phenomenological implications," line 169). This creates a gap between the theory the reader sees in the main text and the experiments it is supposed to ground, particularly the model collapse experiment which uses label-aware curation ("hard, valid examples," Figure 3).
- **ImageNet experimental protocol details sparse in main text (Section 4.3):** Architecture, training procedure, and how pseudo-labeling and pruning are implemented are not sketched in the main text. Given that these experiments are the paper's primary bridge to practice, readers should be able to evaluate them without consulting the appendix.

## Nice-to-Haves
- A brief discussion of how practitioners might estimate ρ (generator quality) in real settings would increase the framework's practical utility, since this is the key quantity governing strategy choice.
- Statistical details for ImageNet experiments (number of seeds, variance) would strengthen confidence in the crossover finding.
- Extending the model collapse experiment to test the "keep easy" strategy for weak generators across rounds would more completely test the theory, since the current experiment only demonstrates "keep hard valid" works.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh critic's concern about appendix content**: Per rules, the appendix is stripped by the parser but exists in the original submission. The paper explicitly references "Appendix C" (line 157) and "various corollaries and their phenomenological implications" (line 169). The label-aware corollaries likely exist in the appendix. The main text presentation gap is kept as a minor weakness, but the absence of appendix content cannot itself be cited as a flaw.

## Novel Insights
The paper's most genuinely novel insight is the identification of generator quality ρ as the single parameter that determines whether data curation helps or hurts, with a sharp phase transition. This reframes the "less is more" vs. "more is more" debate from competing empirical camps into a unified theoretical picture where both sides are correct in different regimes. The connection to model collapse — where iterative pseudo-labeling degrades generator quality over rounds, making strategic pruning increasingly important — is a non-trivial extension that links one-shot curation theory to the dynamics of self-training loops.

## Suggestions
- State at least one key corollary from the label-aware analysis (analogous to Theorem 2) in the main text, especially the conditions under which "keep hard valid" is optimal for weak generators — this would directly ground the model collapse experiment.
- Add a rough proxy measurement of ρ for the base LLM on easy vs. hard AIME slices (e.g., base LLM pass rate) to make the Section 4.2 interpretation quantitatively grounded.
- Include a brief paragraph in Section 4.3 describing the ImageNet experimental protocol (architecture, training setup, pruning implementation).

## Score and Decision

### Calibration Report

**Round 1 bracket: 7.0 – 8.0.** The paper's RMT-based exact test error formulas and phase transition result place it alongside theoretical scaling laws papers in the 7.0–7.6 range. Multi-domain validation (synthetic + ImageNet + LLM) is stronger than most anchors. The 8.0 tier (Strong Model Collapse, Scaling Laws for Precision) is not reached due to the unquantified LLM interpretation.

**Round 2 narrowing: 7.0.** The paper sits at the level of "An Effective Theory of Bias Amplification" (7.0, ACCEPTED) — same RMT approach, exact formulas, practical relevance — but with broader validation. It does not reach 7.5+ because of the moderate gap between the label-aware theory and the model-collapse experiment it is supposed to ground.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>