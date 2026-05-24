Now I have enough calibration. Let me compile the final review.

---

## Summary

This paper develops a theoretical framework for data curation in high-dimensional binary classification with ridge regression, deriving exact asymptotic test-error formulas (Theorem 1) and characterizing the optimal pruning strategy (Theorem 2) under label-agnostic and label-aware curation rules with imperfect oracles. The central finding is a phase transition: when the generator and pruner are both strong, "keep hard" is optimal ("less is more"); when the generator is weak but the pruner is strong, "keep easy" is optimal. The theory is validated on synthetic data and ImageNet, and used to interpret recent contradictory results in LLM reasoning (LIMO, s1, Sun et al.).

## Strengths

1. **Exact analytical characterization (Theorem 1).** The paper derives a closed-form asymptotic expression for test error under any symmetric pruning function via random matrix theory, going well beyond heuristic or qualitative treatments common in prior work on data pruning.

2. **Crisp phase-transition prediction (Theorem 2).** The theorem provides precise, testable conditions for when "less is more" vs. "more is more" applies — specifically, that the optimal strategy flips based on generator quality ρ and pruner quality ρ_*. This is cleaner than prior work which offered empirical observations without principled conditions.

3. **Generalization beyond prior theoretical work (Remark 1).** The label-aware curation rule subsumes the special cases of Feng et al. (2025) and Firdoussi et al. (2024) (which only filter by label correctness) by additionally incorporating difficulty-based pruning, giving a demonstrably more general model.

4. **Real-world validation on ImageNet.** Figure 2 shows a crossover where "keep easy" outperforms under small data (160K, weak generator) and "keep hard" outperforms under large data (1.2M, strong generator), matching the theoretical prediction. This demonstrates the theory's relevance beyond toy settings.

5. **Principled explanation of LLM reasoning contradictions (Section 4.2).** The paper uses the theory to unify the seemingly contradictory findings of LIMO/s1 (less is more) vs. Sun et al. (more is more) by noting that the optimal strategy depends on whether the generator is strong or weak relative to the slice of the test distribution, providing a coherent explanation where none existed.

## Weaknesses

### Major

1. **Synthetic experiments do not directly test Theorem 2(B).** The synthetic experiments (Figure 1) compare "keep hard" vs. random pruning but never test "keep easy" in a regime where Theorem 2(B) applies (weak generator with an *excellent* pruner, ρ_* → 1). The footnote reveals that ρ_* = ρ in the synthetic setup, so when ρ < 1, the pruner is *not* excellent and Theorem 2(B)'s conditions are not met. The paper instead relies on ImageNet experiments to support this half of the theory, but those operate under very different assumptions (real images, nonlinear models, pseudo-labeling). This leaves a gap: the reader cannot verify from controlled synthetic data that the theory's specific mechanism actually produces the "keep easy" prediction.

2. **Model collapse experiment (Figure 3) lacks necessary controls.** The comparison is between "training on all data" and "training on hard valid examples," which differ in both *strategy* and *dataset size* — the pruned condition keeps fewer examples. Without a control that trains on the same number of randomly selected (but label-filtered) examples, it is impossible to attribute the stability to the "keep hard" strategy specifically rather than to simply discarding noisy labels. Additionally, only 6 rounds are shown, which is insufficient to establish long-term stability. This experiment is presented as evidence for a bullet-point contribution ("mitigate model collapse"), but the evidence is substantially weaker than claimed.

### Minor

1. **Ambiguous mapping between theory and empirical settings.** Theorem 2 is proved for *label-agnostic* curation, but the ImageNet and LLM discussions mix intuitions from both label-agnostic and label-aware settings without clearly stating which theorem applies. The ImageNet protocol involves checking pseudo-label correctness (making it closer to label-aware curation, Theorem 3), yet the paper invokes Theorem 2 when discussing the crossover. Similarly, the LLM reasoning discussion (verifying correctness of traces) is label-aware but does not reference Theorem 3.

2. **Reproducibility details missing for synthetic experiments.** The paper states that Figure 1 uses n=100/5000 and compares "keep hard" vs. random, but does not specify the exact values of ρ, ρ_g, ρ_*, the threshold α for "keep hard," or the number of trials used for error bars. These are needed to reproduce or evaluate the empirical match.

3. **LLM reasoning section is purely post-hoc interpretation.** Section 4.2 provides a compelling narrative but no new experiments or measurements (e.g., estimating ρ for the base LLM on the relevant task). It adds plausibility rather than independent confirmation.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- Add a synthetic experiment that directly tests Theorem 2(B): in the regime ρ < 1 with ρ_* ≈ 1, compare "keep easy," "keep hard," and random pruning, and show that "keep easy" achieves the lowest error at p < 1.
- Add a control to the model collapse experiment that uses the same number of randomly selected examples (with label filtering) to isolate the effect of the "keep hard" strategy.
- Provide a brief intuitive explanation of the constant τ (cotangent of the angle between pruner and generator) and its role in the constants β and β̃ in Eq. (8), to help readers build geometric intuition.

## Removed Points

These points were raised but are not included as weaknesses in the main review:

- **Claim about "exact scaling law curves" overclaiming (Harsh Critic Point 4):** The paper's abstract and introduction are ambitious but the Limitations section (Section 6) explicitly acknowledges the Gaussian, linear, binary setting. As a theory paper, framing the results in relation to classical scaling laws is acceptable. This is a matter of rhetorical preference, not a substantive weakness.
- **"The introduction of τ and the four constants would benefit from intuitive explanation":** Addressed under Nice-to-Haves. This is a presentation preference rather than a weakness.
- **Strength about "model collapse prevention (Figure 3)":** Removed because it conflicts with verified weakness #2 (lack of controls). The claim exceeds the evidence provided.
- **"Disconnect between theory and LLM/ImageNet discussion" framing as critical:** Downgraded to Minor. The paper does discuss both label-agnostic and label-aware settings, and the mapping is implicit. Making it explicit would improve clarity but the mismatch does not invalidate the qualitative insights.

## Novel Insights

The reviews surface a genuine tension that the paper does not fully resolve: the theory is exact and precise for the isotropic Gaussian model, but the real-world phenomena it aims to explain (LIMO, s1, ImageNet pruning, model collapse) all violate the theory's core assumptions in ways that are acknowledged but never bridged by intermediate experiments that gradually relax assumptions. This leaves the paper in an awkward position — too clean to directly apply, too applied to be pure theory. A path forward would be to design experiments that test the *specific functional form* of the predicted phase boundary (e.g., the exact threshold in ρ space) rather than only the qualitative direction of the effect. None of the current reviewers identified this gap, but it emerges from the contrast between the strength of the theoretical tool and the looseness of its validation.

## Suggestions

1. In the synthetic experiments, add a direct test of Theorem 2(B): fix ρ < 1, set ρ_* ≈ 1, and compare "keep easy" vs. "keep hard" vs. random pruning. Show that "keep easy" achieves the minimum at p < 1.
2. Add a control to the model collapse experiment that trains on the same number of randomly selected (label-filtered) examples to isolate the effect of the "keep hard" strategy from mere dataset shrinkage.
3. Clearly label each experiment with the specific theorem it tests (e.g., "Theorem 2 (label-agnostic)" or "Theorem 3 (label-aware)"), to help the reader assess how far the theory is being stretched.
4. Report the exact parameter values (ρ, ρ_*, ρ_g, n, d, α) for the synthetic experiments in the main text or a dedicated table.

---

## Score and Decision

**Calibration Report**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| TqjmCEjrEa | 2.50 | R1-bracket | Weak paper on data selection; substantially weaker theory and results. |
| kx3txPrC2B | 2.50 | R1-bracket | Model pruning paper; unrelated topic, much lower quality. |
| 7unPwFQEWB | 3.33 | R1-bracket | Linear prediction rules; weaker empirical validation. |
| LNkeiyIp4f | 3.00 | R1-bracket | Parameter pruning dynamics; unrelated topic. |
| ycxzArIvgF | 4.00 | R1-bracket | Data pruning via score extrapolation; empirical paper with limited theory. Our paper is substantially stronger on theoretical depth and insight. |
| vxkzW4ljeX | 5.50 | R1-bracket | Compression theory for lottery tickets; similar structure (theory+experiments) but weaker experiments and significant practical applicability gaps. Our paper has cleaner validation. |
| AGCOnxvJAh | 3.60 | R1-bracket | Data attribution for pruning; empirical, no theory. |
| pJcHaD3mvn | 4.00 | R1-bracket | Scaling laws extrapolation; weaker theoretical foundation. |
| nCsF3Bsn2n | 8.00 | R1-bracket | Kernel function for angle testing; unrelated topic, top-tier score. |
| Ahdsg2nkNH | 8.00 | R1-bracket | Multilevel control functional; unrelated topic. |
| yRtgZ1K8hO | 8.00 | R1-bracket | Matrix sign methods; unrelated topic. |
| 248ysaRatx | 8.00 | R1-bracket | Quantum neural networks; unrelated topic. |
| e0zcvj4nLy | 5.00 | R2-narrow | Kernel ridge regression rates; similar methodology but narrower scope. |
| 9RdhTvYbX0 | 5.50 | R2-narrow | Model collapse in linear regression; incremental contribution concerns. Our paper has greater novelty. |
| qPKTDOJ5Xs | 6.00 | R2-narrow | ℓ_r norm scaling; similarly clean theory but narrower practical impact. |
| nn5Vf6GEsV | 6.40 | R2-narrow | Kernel regression learning curves; approximate theory (ansatz) vs our exact theory. Comparable overall quality. |
| Q3yLIIkt7z | 7.00 | R2-narrow | Scaling laws for neural networks; stronger empirical scope. Our paper is slightly weaker on experiments. |
| xDLE5n3x9Y | 6.50 | R2-narrow | BBP transitions in neural networks; similar theory quality. |
| 2FZC0c06jP | 6.50 | R3-narrow | Data curation with proxy models; strong empirical paper. Our theory is more rigorous. |
| yKUbw7q1IA | 6.80 | R3-narrow | Data-efficient LLM training; empirical, different methodology. |
| vAU1fo1zRV | 7.00 | R3-narrow | Decision calibration; different topic, strong theory. |

**Round 1 bracket:** Initial bracket was [4, 7] — below the strong theory papers at 7+ but clearly above weak papers at 2–4.  
**Round 2 narrowing:** Compared against papers at 5.5–7.0. Our paper is stronger than 9RdhTvYbX0 (5.50, which had incremental contribution concerns) and similar in quality to nn5Vf6GEsV (6.40, approximate theory with strong experiments) and 2FZC0c06jP (6.50, empirical paper with solid theory). It is slightly weaker than Q3yLIIkt7z (7.00, more extensive experiments).  
**Final score:** 6.5 — the theoretical contribution is novel and exact, the writing is clear, but the empirical validation has notable gaps (missing synthetic test of Theorem 2(B), under-controlled model collapse experiment) that prevent it from reaching the 7+ tier.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>