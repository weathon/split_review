## Summary

This paper introduces Ano, an optimizer that decouples update direction (from momentum sign) from magnitude (from instantaneous gradient norm), with a Yogi-style second-moment update enhanced by a β₂-decay mechanism. A derived variant, Anolog, uses a logarithmic momentum schedule to reduce hyperparameter sensitivity. The method is evaluated on CIFAR-100, GLUE, MuJoCo (SAC), and Atari (PPO), and includes a non-convex convergence analysis. The core idea is clean and well-motivated, and the RL results are the strongest evidence for the paper's claims.

## Strengths

1. **Clear empirical advantage in reinforcement learning.** Table 4 shows Ano achieves the best mean rank (1.4) and highest normalized average (99.48%) across five MuJoCo tasks under default hyperparameters, and Figure 2 demonstrates that Ano reaches Adam's final performance in 50–70% fewer steps on most environments. The Atari results (Table 5) reinforce this pattern. This is the strongest evidence for the paper's central claim about non-stationary / high-variance settings.

2. **Noise robustness is demonstrated directly.** Table 1 injects Gaussian noise into CIFAR-10 gradients and shows Ano degrades less than Adam and Lion, with the gap widening at higher noise levels (59.54% vs. 52.46% for Adam at σ=0.20). This clean ablation supports the decoupling design.

3. **Systematic ablation study isolates each component.** Table 6 compares 11 variants, separating the contributions of gradient norm, momentum direction, second-moment rule, and momentum schedule. Key finding: AdamGrad (decoupling with Adam's second-moment rule) reaches 9855 vs. Ano's 10520 on the DRL task, suggesting the core gains come from the decoupling itself. This honest reporting lets readers assess each design choice.

4. **Hyperparameter robustness is demonstrated.** Figure 3 shows Ano maintains high reward across a wider range of learning rates and β values than Adam on a HalfCheetah proxy, supporting the claim that Ano is less sensitive to hyperparameter choice.

## Weaknesses

### Fatal
None.

### Major

1. **Discrepancy between the text and pseudocode for the core update rule (verifiable from the paper).** The text in Section 3 (lines 75–77) defines the update as  
   `x ← x − (η/√v+ε)·|g_k|·sign(m_k)`, using the *gradient norm* for magnitude.  
   Algorithm 1 (line 63) writes the update as  
   `x ← x − (η/√v̂+ε)·g_k·sign(m_k)`, using the *raw gradient* (without explicit |·|).  
   Since g_k = |g_k|·sign(g_k), the pseudocode computes |g_k|·sign(g_k)·sign(m_k). This equals the text's |g_k|·sign(m_k) only when sign(g_k)=sign(m_k); when they disagree, the effective direction differs. The paper does not clarify which version was implemented. Both formulations are individually well-defined, but the ambiguity between the text's stated design intention and the pseudocode's update means the method as described is not unambiguously reproducible from the paper alone. (Note: the authors state code is released, which resolves the practical reproducibility concern, but the paper itself should be self-consistent.) This is the most significant weakness and the authors must reconcile it.

### Minor

2. **Theory-practice gap.** The convergence proof (Section 5.1) assumes β_{1,k}=1−1/√k and η_k=η/k^{3/4}, while the practical Ano uses fixed β₁=0.92 and (from the appendix references) constant or cosine LR schedules. The analysis guarantees convergence for a scheduled variant, not the algorithm actually run. This is standard practice in optimization theory (the Lion and Signum papers do similarly), and the paper is transparent about the assumptions, but the claimed "theoretical backing" for Ano is weaker than stated. A clear delimitation of scope (e.g., "the theory applies to a scheduled variant; the practical benefits are validated empirically") would be appropriate.

3. **Anolog's reduced sensitivity is claimed but not directly tested.** Section 4 claims Anolog removes sensitivity to β₁ tuning, and Table 6 shows the log schedule outperforms sqrt and harmonic schedules. However, there is no direct sensitivity sweep for Anolog comparable to Figure 3 for Ano vs. Adam. A heatmap showing Anolog's reward across a β₁×LR grid would directly support the claim that it reduces tuning burden.

4. **GLUE table has a labeling inconsistency.** Table 3 lists two rows labeled "Adam" under both Default and Tuned sections with different numerical values. This is likely a copy-paste error (possibly one should be Adan, which is listed separately in Table 2 but absent from Table 3). While this does not affect the scientific conclusions, it must be corrected.

5. **AdamGrad's competitive performance deserves more discussion.** In Table 6, AdamGrad (decoupling with Adam's second-moment rule) achieves 9855±1173 on DRL vs. Ano's 10520±416, with overlapping confidence intervals. The paper notes this briefly but does not discuss whether the β₂-decay extension provides statistically significant gains over the simpler decoupling alone. Given that AdamGrad uses the same core decoupling idea, this comparison warrants deeper analysis.

### Trivial

6. **Figure 3 axis labels are confusing.** The x-axis is labeled "beta" but the tick values (1e-05, 1e-04, 1e-03) resemble learning rate values, not momentum coefficient values. The caption says "beta" but references "betas" in the plural in the main text. This should be clarified.

## Nice-to-Haves

- Direct sensitivity comparison (similar to Figure 3) for Anolog vs. Ano, to validate the claim of reduced hyperparameter sensitivity.
- Explicit discussion of whether the practical algorithm follows the text (`|g_k|·sign(m_k)`) or the pseudocode (`g_k·sign(m_k)`), and whether this distinction matters in practice.
- Including a simple SGD with momentum baseline would help calibrate whether Ano's gains stem from adaptivity or from the decoupling specifically.

## Removed Points

The following points from the reviewers were flagged for removal with justification:

- **"Missing SGD baseline"** (Harsh Critic): The paper compares against the most relevant adaptive optimizers (Adam, Adan, Lion, Grams, RMSprop). SGD is a reasonable baseline to add but its absence is not a weakness — the paper's scope is adaptive optimizers for noisy settings, and requesting SGD is scope creep. → Removed as soft-rule scope creep.
- **"Noise robustness experiment does not capture non-stationarity"** (Harsh Critic): The paper explicitly limits this experiment to additive i.i.d. Gaussian noise as a controlled ablation. The RL experiments (MuJoCo, Atari) directly test non-stationarity. → Removed as scope creep; the paper already provides multiple lines of evidence for the non-stationarity claim.
- **"GLUE formatting"** beyond the labeling issue: The harsh critic calls it "messy" — this is a presentation nitpick about table layout, which is a parser artifact issue. The substantive labeling error (two "Adam" rows) is retained as Minor. → Removed formatting nitpick.
- **"Confidence intervals overlap"** (Harsh Critic): The paper reports 95% CIs and IQM, following RL best practices. Overlapping intervals are standard in RL and the paper does not overclaim statistical significance. → Removed, as this is standard practice.
- **"Hyperparameter details in appendices are stripped"** (Harsh Critic): The PDF parser strips appendices; they exist in the original submission. → Removed per hard rules.
- **Strength Finder strengths about "addressing an important problem" and generic praise**: → Removed as generic / sycophantic.
- **Strength about "hyperparameter robustness demonstrably better than Adam's"** — this directly conflicts with the verified Figure 3 axis label confusion. → The strength that Figure 3 *exists* and *shows a pattern* is retained; the specific claim about axis labels being confusing is separately handled in Trivial.
- **"The convergence guarantee matches sign-based methods"** — This strength is retained in qualified form, but the theory-practice gap weakness (Minor) qualifies it.

## Novel Insights

The most interesting observation from the cross-review is the AdamGrad comparison in the ablation study: a simple decoupling of gradient norm and momentum direction (without the Yogi+β₂-decay extension) achieves 94% of Ano's DRL performance with overlapping CIs. This suggests the core contribution is the direction–magnitude decoupling itself, with the second-moment tweak providing a smaller incremental benefit. The paper could foreground this distillation more explicitly. A second observation is that Ano's hyperparameter robustness heatmap (Figure 3) and the theory's reliance on scheduled β₁ present an unresolved tension: the fixed-β₁ version is claimed to be robust, but the theory needs a decay schedule — understanding the domain where fixed β₁ works vs. where scheduling matters would sharpen the contribution.

## Suggestions

1. **Resolve the update-rule ambiguity immediately.** State explicitly whether the implementation uses `g_k·sign(m_k)` or `|g_k|·sign(m_k)`. If it's the former, explain why this choice was made (it is actually a different algorithm from the text description); if it's the latter, correct the pseudocode. This is the single most important fix.

2. **Add a sensitivity heatmap for Anolog** (comparable to Figure 3) to directly support the claim that the logarithmic schedule reduces β₁ sensitivity.

3. **Discuss the AdamGrad result more deeply** — acknowledge that the decoupling itself may be the primary driver and clarify what the Yogi+β₂-decay adds beyond it.

4. **Fix the GLUE table** — the duplicate "Adam" rows need to be corrected (likely one is Adan).

5. **Clarify Figure 3's axes** — ensure the x-axis label and tick values are consistent and correctly indicate whether the swept parameter is β₁ or learning rate.

## Score and Decision

### Calibration Anchors

| Anchor Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/XHXe1pGwzA.md` | 2.00 | R1 | Much weaker — trivial contribution about weight decay correction |
| `/home/wg25r/review_agent/human_reviews_2026/Op8RDj5qX1.md` | 3.00 | R1 | Much weaker — mostly theoretical optimizer design, minimal experiments |
| `/home/wg25r/review_agent/human_reviews_2026/E9qZRF5gCj.md` | 2.50 | R1 | Much weaker — narrow ablation of whitening optimizers |
| `/home/wg25r/review_agent/human_reviews_2026/gqkayvdfM7.md` | 3.00 | R1 | Much weaker — pure theory paper on sign-based bounds |
| `/home/wg25r/review_agent/human_reviews_2026/RPly1hhiUG.md` | 4.80 | R1 | Worse — Grams paper, same topic but weaker experiments (small models, no RL), rejected |
| `/home/wg25r/review_agent/human_reviews_2026/Lk0tQYo76o.md` | 5.00 | R1 | Worse — mostly theoretical sign-based analysis, minimal experiments |
| `/home/wg25r/review_agent/human_reviews_2026/KirKWFPYJA.md` | 5.00 | R1 | Comparable theory quality, narrower scope (SGDM bounds only, no new optimizer) |
| `/home/wg25r/review_agent/human_reviews_2026/gqKw2hblMa.md` | 4.00 | R1 | Worse — finite-time optimization, less comprehensive evaluation |
| `/home/wg25r/review_agent/human_reviews_2026/yDLD3D95w3.md` | 6.00 | R2 | Comparable — similar theory-practice gap but stronger LLM experiments; our paper has broader domain coverage |
| `/home/wg25r/review_agent/human_reviews_2026/tx1ZvypKqS.md` | 6.50 | R2 | Slightly stronger — XQC has thorough RL experiments but is an architecture solution, not an optimizer |
| `/home/wg25r/review_agent/human_reviews_2026/Gwe6gbGng5.md` | 7.00 | R2 | Stronger on theory but the CWD paper's theory had identified flaws; still accepted |
| `/home/wg25r/review_agent/human_reviews_2026/RUzxUqTpzW.md` | 6.00 | R2 | Different topic (differentiable simulators for RL) |

**Round 1 bracket:** 4.0–7.0 (clearly above the 2–3 range papers; below the 7.5+ papers which are on unrelated topics).

**Round 2 narrowing:** The paper is stronger than Grams (4.80, rejected) due to more comprehensive experiments and RL evaluation. It is comparable to the Parameter-free Sign-SGD paper (6.00, accepted) — both have theory-practice gaps but provide reasonable empirical validation. It is slightly below XQC (6.50, accepted) which had more thorough RL experiments but is a different type of contribution (architecture-based rather than optimizer-based). The algorithm ambiguity issue prevents a higher score but is fixable.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>