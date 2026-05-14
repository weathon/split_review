Now I have all the material needed. Let me compose the final review.

## Summary

This paper proposes Pi-CCA, a replay-free continual learning framework for vision-language models that preserves cross-modal alignment geometry through a compact "CCA certificate" capturing the top-k canonical correlations and sketched subspaces of the whitened image-text cross-covariance. During adaptation, the certificate constrains spectral and subspace drift via differentiable losses, while a prompt-invariance mechanism averages over text-prompt perturbations. Evaluated on MTIL, X-TAIL, VLCL, and ConStruct-VL, Pi-CCA achieves state-of-the-art results among replay-free methods, often matching or exceeding synthetic-replay baselines without storing past data.

## Strengths

- **Principled reframing of forgetting as alignment-geometry drift.** The paper identifies that prior VL-CL methods "regularize outcomes (similarities, logits, weights, routes) rather than directly controlling the alignment object that underlies cross-modal generalization" (Section 1). This conceptual shift to preserving CCA spectrum and subspaces is well-motivated and distinguishes Pi-CCA from proxy-distillation approaches. The ablation study (Table 3) confirms that both the spectral term ($\lambda_1$) and subspace term ($\lambda_2$) contribute meaningfully to retention.

- **Replay- and generator-free, constant-memory design.** The certificate stores only the top-$k$ canonical correlations and $h$-dimensional sketched bases (Eq. 4), requiring memory independent of the number of tasks. The Pareto analysis (Figure 2) shows that small certificates ($k=64, h=256$) lie on the efficient frontier, supporting the "small yet sufficient" claim. This is a practical advantage over generative replay methods (e.g., GIFT) that require diffusion models.

- **Consistent SOTA across four diverse benchmarks.** Pi-CCA achieves the highest results among replay-free methods on MTIL (Avg 76.8), X-TAIL (Avg 68.1), VLCL (I2T R@1 48.6), and ConStruct-VL (FA 75.2, AF 2.7). The margins over top baselines are modest (+1.6 on MTIL, +0.7 on X-TAIL) but consistent across settings, and on VLCL retrieval Pi-CCA even surpasses the synthetic-replay method GIFT. The task-order sensitivity analysis (Figure 5) shows robustness across 20 random orderings.

- **Thorough ablation and analysis.** Table 3 systematically ablates each loss term, EMA mechanism, sketch type, and pairing strategy, with clear decomposition of contributions. The prompt-invariance stress test (Figure 4) validates that $\mathcal{L}_{\text{pi}}$ effectively reduces sensitivity to prompt perturbations under both ID and OOD templates.

## Weaknesses

### Major

- **Suspiciously perfect Spearman correlations in Figure 3.** The paper reports Spearman $\rho = 1.00$ for all four scatter plots relating geometry drift to performance drop. A perfect rank correlation with two-digit precision across empirical hyperparameter sweeps is essentially impossible for real data with any noise or irreducible variation. The paper states these are "sweep realistic perturbations (certificate size, EMAs, invariance strength, whitening, pairing, LoRA capacity/LR, sketch type)" — if the drift metric and performance drop are deterministically linked, this should be explained. As presented, the perfect $\rho$ values undermine the credibility of this analysis and, by extension, the claim that "preserving CCA geometry predicts retention." The paper's conceptual contribution rests partly on this evidence, making this a non-trivial concern. The authors should (a) explain whether the scatter data is from deterministic evaluations or contains any stochastic variation, (b) report the raw $p$-values and number of data points, and (c) ideally add error bars per point if multiple seeds were used.

### Minor

- **"Invariant" framing overstates what the method achieves.** The paper repeatedly describes the certificate as preserving "invariants" and treating "alignment as a first-class invariant." However, Eq. (13) explicitly refreshes $\rho_{1:k}^*$, $S_v^*$, and $\bar{S}_t^*$ via EMA with rate $\alpha > 0$. The certificate is a moving target, not a fixed invariant. The paper acknowledges this as "controlled plasticity" but never reconciles it with the invariant language. This is not a fatal flaw — the method is transparent about the update — but the framing is misleading. The method is better described as enforcing *temporal smoothness* of alignment geometry against a slowly-updated reference than as preserving the original pre-trained alignment. The paper should either (i) adopt more precise language throughout, or (ii) study a variant with $\alpha=0$ (truly fixed certificate) and analyze whether the EMA update is necessary or harmful.

- **Missing confidence intervals for classification results (Table 1).** Confidence intervals are reported for VLCL and ConStruct-VL (Table 2) but not for MTIL and X-TAIL (Table 1). Given that margins over the best baselines are small (+1.6 on MTIL Avg, +0.7 on X-TAIL Avg), the reader cannot assess whether these differences are statistically significant. Since the paper has room to report intervals for retrieval tasks, the omission for classification tasks raises selective-reporting concerns.

- **Computational cost of differentiable SVD is not analyzed.** The paper mentions using block power iteration for differentiable SVD but provides no analysis of training stability, gradient variance, or per-step wall-clock overhead beyond the capacity-vs-performance Pareto sweep. Given that SVD is computed every mini-batch, this gap is notable for a method claiming efficiency.

### Trivial

- The Y-axis label in Figure 3 uses notation ($D_{\text{avg}}$, $D_\rho$) that is partially defined but inconsistently referenced in the caption text. The caption spells the angle drift as $\sum \sin^2 \theta_i$ but refers to it as "$D_{\text{avg}}$" while the text calls it "$D_{\text{ang}}$." A minor consistency fix.
- Table 3 reports "w/o certificate EMA ($\alpha=0$)" which is informative but a broader sweep over $\alpha$ values would be more informative.

## Nice-to-Haves

- **Certificate drift relative to the original pre-trained model.** Currently, the paper only reports geometry drift metrics relative to the current (EMA-updated) certificate. Plotting drift relative to the *original* pre-trained model's CCA structure would directly test whether the EMA preserves the original alignment or allows gradual divergence, and would clarify the practical effect of the "controlled plasticity."
- **Comparison with a fixed-certificate variant ($\alpha=0$).** The ablation already includes this as "w/o certificate EMA" (Table 3), showing only a small drop (MTIL Avg 75.6 vs. 76.8). The paper should discuss this result more: if a truly static certificate works almost as well, the "invariant" framing would be more justified, and the EMA complexity might be unnecessary.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism that "all four plots list Pearson r = 1.00."** Factually incorrect: the figure caption shows two plots with r=0.99 and two with r=1.00. The core concern about Spearman ρ=1.00 remaining is kept as a major weakness above.
- **"Methodological gap: training stability" framed as a critical issue.** The paper mentions differentiable SVD with power iteration and addresses stability mechanisms (spectral clipping, eigenvalue flooring, stop-gradient). This is a reasonable implementation description for an empirical paper.
- **Demand for "concrete example of prompt invariance" with retrieval examples.** A nice addition but not a core requirement for a paper already presenting quantitative stress tests.
- **Demand for "training loss curves."** Standard for some fields but not a customary requirement for a systems/empirical paper at ICLR.
- **Criticism that "the paper never analyzes or bounds this drift" (of the EMA certificate).** The paper provides the ablation (Table 3) and the geometry→performance analysis (Figure 3). A formal bound is not expected for an empirical paper at ICLR.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Figure 3: Address the ρ=1.00 issue directly** — explain whether data points are deterministic (single-run evaluations per hyperparameter configuration) or stochastic, report the number of configurations and whether any noise is present. If the data is truly deterministic (e.g., each configuration run once with fixed seed), state this explicitly and consider adding variance via multiple seeds.
2. **Add confidence intervals or standard deviations to Table 1** (MTIL, X-TAIL) to match Table 2, so readers can assess whether the claimed SOTA margins are statistically significant.
3. **Tone down "invariant" language** to something like "slowly-updated reference geometry" throughout the paper to more accurately reflect the EMA update in Eq. (13).
4. **Report per-step wall-clock time** for the full Pi-CCA pipeline (including differentiable SVD) vs. key baselines to substantiate the efficiency claim.
5. **Sweep over EMA rate α** beyond just α=0 (as in Table 3) to show sensitivity to certificate update speed.

## Score and Decision

**Calibration Anchors:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/IdW0d0mRnG.md` (Heads collapse, features stay) | 7.33 (Accept) | More theoretically rigorous; Pi-CCA has stronger empirical breadth but weaker theory |
| `/home/wg25r/review_agent/human_reviews_2026/rMHZfCznhZ.md` (RLAP-CLIP) | 6.00 (Accept) | Similar VL-CL scope; Pi-CCA's CCA certificate is more novel than RL-based prototypes, but RLAP-CLIP has cleaner statistics |
| `/home/wg25r/review_agent/human_reviews_2026/Vr5f3kRvLD.md` (IDER) | 6.00 (Accept) | Similar empirical quality; IDER has a cleaner story but Pi-CCA evaluates on more diverse benchmarks |
| `/home/wg25r/review_agent/human_reviews_2026/ptFP9yT9DK.md` (ConDU) | 5.50 (Accept) | Very similar quality level; both have novel approaches and solid results with some presentation gaps |
| `/home/wg25r/review_agent/human_reviews_2026/hWw269fPov.md` (PAC-Bayes for CL) | 5.33 (Accept) | More theoretical but narrower scope; Pi-CCA's empirical contribution is larger |
| `/home/wg25r/review_agent/human_reviews_2026/mDuton6Tg7.md` (Cross-modal alignment CL) | 3.00 (Reject) | Similar topic but Pi-CCA is significantly stronger — clearer framing, better experiments, more novel method |
| `/home/wg25r/review_agent/human_reviews_2026/0za6569Jqd.md` (CoRe) | 2.00 (Reject) | Incremental contribution; Pi-CCA has a genuinely novel approach with broad evaluation |
| `/home/wg25r/review_agent/human_reviews_2026/WLSt5tIOSA.md` (Fine-tuning VLMs) | 4.00 (Reject) | Pi-CCA is more novel and has broader experimental evaluation |
| `/home/wg25r/review_agent/human_reviews_2026/HN18kuyf4o.md` (Caption-guided replay) | 4.00 (Reject) | Pi-CCA is replay-free and has a more principled approach |

Pi-CCA presents a genuinely novel idea (CCA certificate for geometry preservation) with solid SOTA results across four benchmarks and thorough ablations. However, the suspiciously perfect Spearman correlations in Figure 3 and the overclaimed "invariant" framing are real concerns that prevent this from being a strong accept. Relative to the calibration anchors, the paper's contribution level and empirical quality are most comparable to the mid-range accepted papers (ConDU at 5.50, RLAP-CLIP at 6.00), but the Figure 3 issue and framing concerns pull it slightly below those.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>