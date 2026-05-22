Now I have enough calibration data. Let me compile my final review.

**Round 1 bracket**: [(3.5, 7.5), (>7.5)]. The paper clearly sits above the weak band (papers scoring 2-3) and above most of the middle band (4-6). It's in or near the strong band (7.5+).

**Round 2 anchor comparison**: Compared to anchors in the 7.5-8.0 range (OCM at 8.0, Synthetic continued pretraining at 8.0, Prioritized Generative Replay at 7.5, Not All LLM-Generated Data Are Equal at 7.5), Neon offers a broader contribution (works across 4 model families instead of one), has stronger theoretical foundations, achieves clearer SOTA results, and is simpler. It's at least comparable to the 8.0 papers.

## Summary

This paper introduces Neon (Negative Extrapolation from Self-Training), a method that reverses the degradation caused by fine-tuning a generative model on its own synthetic data. By briefly fine-tuning on self-generated data and then extrapolating the parameters in the opposite direction ($\theta_{\text{Neon}} = \theta_r - w(\theta_s - \theta_r)$), Neon improves generation quality across diffusion, flow matching, autoregressive, and few-step models. The method is grounded in theoretical analysis showing that mode-seeking inference samplers (temperature < 1, top-k, CFG) create anti-alignment between synthetic and real-data gradients. On ImageNet-256, Neon elevates the xAR-L model to FID 1.02 (SOTA) with only 0.36% additional compute.

## Strengths

- **Simple, architecture-universal method with strong theoretical backing**: Neon's parameter merge (Eq. 2) is remarkably simple, yet Theorems 1 and 2 provide a rigorous theoretical explanation for why reversing self-training degradation works, tracing the mechanism to anti-alignment induced by mode-seeking samplers. This theory is validated across four distinct model families — diffusion, flow matching, autoregressive, and few-step — using the same formula, which no prior method achieves.

- **State-of-the-art results with negligible compute**: xAR-L + Neon achieves FID 1.02 on ImageNet-256, surpassing UCGM (1.06), using only 0.36% additional training compute and 750k synthetic samples (Section 4.2, Figure 5). Even with just 1k synthetic samples, xAR-L reaches FID 1.05 — nearly optimal. This is a concrete, verifiable SOTA result with unprecedented efficiency.

- **Extensive and well-designed empirical validation**: The paper tests Neon across CIFAR-10, FFHQ, and ImageNet, on 7+ model variants (EDM-VP, flow matching, xAR-B/L, VAR-d16/30, IMM), with thorough ablations including robustness to synthetic data quality (Figure 10), data efficiency (Figure 9, 1k samples), and cross-architecture transfer (Figure 8). The precision-recall analysis (Figure 4) directly confirms the predicted mechanism.

- **Cross-architecture transfer is a practical bonus**: Figure 8 shows that synthetic data from a Flow or IMM model can improve an EDM-VP model, with theoretical support in Appendix B.8. This capability is not reported in prior self-training methods and has practical value when generating from the target model is costly.

## Weaknesses

### Major
None.

### Minor

- **No statistical confidence for FID numbers**: The headline SOTA claim (FID 1.02 vs. UCGM 1.06) relies on a single FID evaluation without error bars, confidence intervals, or multiple random seeds. While single-run FID reporting is standard in the generative modeling literature (EDM, DDPM, etc. all do the same), the paper makes a precise SOTA claim where the margin (0.04) is within the known variance of FID estimates. Even a brief statement like "repeated with 3 seeds, observed FID 1.02 ± 0.03" would substantially strengthen the reliability of this result.

- **Theoretical guarantee for diffusion/flow models depends on an unverified assumption (A-MONO)**: Theorem 2's coverage of diffusion and flow models with CFG (footnote 2, Appendix B.7) requires the A-MONO condition — that certain curvature-density coupling increases with data log-density. This assumption is neither verified empirically nor discussed in the main text. The theory for autoregressive models is clean and doesn't need this, but the paper's framing ("we prove rigorously that mode-seeking inference samplers create a predictable anti-alignment") overreaches slightly for the diffusion/flow case.

- **No dedicated limitations section**: The paper lacks a discussion of limitations, including: (a) the need for real validation data to select $w$ (standard but worth stating), (b) the A-MONO assumption gap, (c) that Neon's improvement is bounded and may not help near-perfect models, and (d) the lack of variance estimates.

### Trivial
- The paper could benefit from explicit practical guidance on choosing $w$ without grid search.

## Nice-to-Haves
- Reporting the cost (number of FID evaluations) of the $(w, \gamma)$ grid search for autoregressive models would help practitioners.
- Testing the reverse transfer direction (e.g., EDM → Flow) would strengthen the cross-architecture transfer claim.
- A direct quantitative comparison with DDO on a likelihood-based model (where DDO applies) would contextualize the improvement.

## Removed Points
- **"No new real data claim is misleading because w requires validation data"**: The paper states "requires no additional real training data" (emphasis on training), which is accurate — hyperparameter selection on a validation set is standard practice and doesn't require new training data. This is standard for any method with one tunable hyperparameter.
- **"Figure 9 y-axis range is deceptive"**: The figure uses a log scale from 1 to 10 (wide range), so this criticism is factually wrong.
- **"Comparison to DDO is missing from main text"**: DDO is discussed in related work (Section 2) and the paper correctly notes DDO cannot apply to likelihood-free architectures. The SOTA comparison is with UCGM, which is the relevant ImageNet-256 benchmark.
- **"Transferability experiment thin (one target model)"**: The paper provides theoretical backing (Appendix B.8) and doesn't overclaim; the experiment is presented as a demonstration, not exhaustive validation.
- **"Missing related works"**: Removed per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions
1. Add error bars or a multi-seed experiment for the headline FID result (xAR-L, ImageNet-256) to substantiate the SOTA claim.
2. Either empirically verify the A-MONO assumption for the diffusion/flow models used, or weaken the theoretical framing to acknowledge the gap while letting the empirical results carry the weight.
3. Add a brief limitations section covering the points noted above.

## Score and Decision

**Calibration anchors used**:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Self-Consuming Models Go MAD (ShjMHfmPs0) | 6.67 | 1 | Studies MAD problem but doesn't offer improvement method; Neon is clearly stronger |
| On Stability of Iterative Retraining (JORAfH2xFd) | 6.75 | 1 | Theoretical stability analysis of retraining; Neon has practical method + SOTA results |
| Collapse or Thrive? (Xr5iINA3zU) | 5.75 | 1 | Synthetic data analysis paper; narrower scope than Neon |
| Not All LLM-Generated Data Equal (oI5tZaWkF9) | 7.50 | 2 | Weighting scheme for synthetic data in text; Neon has broader scope, stronger theory |
| Improving ProbDiff Models OCM (fV0t65OBUu) | 8.00 | 2 | Single-architecture improvement; Neon spans 4 model families with cleaner theory |
| Strong Model Collapse (et5l9qPUhm) | 8.00 | 1,2 | Theory paper rejected for weak empirical validation; Neon has stronger experiments |
| Synthetic Continued Pretraining (07yvxWDSla) | 8.00 | 2 | LLM synthetic data; comparable quality but different domain |
| Prioritized Generative Replay (5IkDAfabuo) | 7.50 | 2 | RL replay; narrower application than Neon |

**Round 1 bracket**: The paper sits between the middle band (3.5-7.5) and the strong band (>7.5). Compared to middle-band anchors (avg 4-6), Neon has much stronger theory, broader experiments, and a practical SOTA result. It belongs in or near the strong band.

**Round 2 narrowing**: Compared to Round 2 anchors (avg 7.5-8.0), Neon is comparable or stronger — it has a simpler method, broader architecture coverage, and clearer SOTA impact than the 7.5-8.0 papers I examined. The weaknesses (no error bars, A-MONO assumption) are real but do not undermine the core contribution.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>