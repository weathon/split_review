Now I have all the information needed to produce the final review. Let me compile my analysis.

**Anchor list for calibration:**

| Anchor | Avg Score | Round / Query Bucket | Comparison |
|--------|-----------|---------------------|------------|
| RwiUmrEHgR | 3.00 | R1-topic-low | Cost-sensitive loss for long-tail — much weaker paper, limited experiments, no SSL. CoLA is clearly stronger. |
| 2aebB2mf0q | 3.00 | R1-topic-low | Semi-supervised IR detection — different topic. Low quality. |
| WM5G2NWSYC | 2.00 | R1-topic-low | Projected subnetworks — different topic. Very low quality. |
| E0UsEIRBQ8 | 3.00 | R1-topic-low | Semi-supervised underwater detection — different topic. |
| zLHP6QDWYp | 3.80 | R1-topic-mid | ROLSSL with logit adjustments. Criticized for limited novelty, outdated baselines, weak experiments. CoLA is substantially stronger (current baselines, novel method, broad experiments). |
| OeKp3AdiVO | 6.25 | R1-topic-mid, R2 | Classifier re-training in long-tailed recognition (fully supervised). Strong empirical results on ImageNet-LT and iNaturalist. CoLA is in more complex LTSSL setting but lacks large-scale benchmarks. |
| u1yvEwYfK9 | 5.67 | R1-topic-mid | Label shift correction for long-tail. Accepted-level work. CoLA is comparable in rigor. |
| II81zQUS1x | 5.67 | R1-topic-mid, R1-weakness, R2 | MLA theory paper. Comparable theoretical depth, broader in some dimensions. CoLA has stronger empirical support. |
| 25kAzqzTrz | 8.00 | R1-topic-high | Theoretical SSL analysis — different genre, top-tier. |
| zl0HLZOJC9 | 8.00 | R1-topic-high | Learning to defer — different topic. |
| RvUVMjfp8i | 8.00 | R1-topic-high | SSL evaluation in open environments — different topic. |
| Fk5IzauJ7F | 8.00 | R1-topic-high | Partial-label learning — different topic. |
| SRn2o3ij25 | 4.67 | R2 | IKL for long-tail recognition. Criticized for limited novelty (temporal ensembling). CoLA has cleaner novelty. |
| BUDxvMRkc4 | 4.67 | R2 | BLG with CLIP for long-tail. Lower quality. |
| b66P1u0k15 | 6.00 | R2 | PLOT (Pareto optimization for long-tail). Comparable quality — well-motivated with clear contributions, but some weaknesses. |
| WPsnH6875d | 6.00 | R2 | SSL with unseen classes. Different topic. |
| HvkXPQhQvv | 6.00 | R2 | Semi-supervised model evaluation. Different topic. |
| uBU33YNVL3 | 5.25 | R1-weakness, R2 | Bounded loss robustness. Mixed reviews. |
| E2RyjrBMVZ | 4.17 | R1-weakness | Variance in evaluation benchmarks. Different topic. |
| bsXxNkhvm6 | 2.60 | R1-weakness | Benchmarking stock prediction. Low quality. |
| bqf0aCF3Dd | 6.00 | R1-weakness | SOO-Bench. Different topic. |
| JNZdhbDBUH | 4.33 | R1-weakness | Federated long-tail learning aggregation. Different topic. |
| j5EbZEyK9I | 4.50 | R1-weakness | Data composition effects. Different topic. |
| pK4Z6NZ2DB | 5.20 | R1-weakness | Loss decomposition analysis. Different topic. |

**Round-1 bracket**: 4.5–6.5, based on the clear gap between low-band (<3.5) and high-band (>7.5) papers, with mid-band anchors ranging from 3.8 to 6.25.

**What did the low-band anchors fail at, and does the paper under review share any of those failures?** The low-band ROLSSL paper (3.80) failed due to limited novelty (logit adjustment technique was already known), missing key baselines, and small-scale experiments. The IKL paper (4.67) failed due to limited technical novelty (techniques from prior work on temporal ensembling). CoLA does NOT share these failures: its DDDE (effective rank) and LMC (meta-learning τ) are genuinely novel; it compares against many current baselines; and it covers 4 benchmarks across 6 distribution types. However, CoLA partially shares a failure mode with some weakness-anchored papers: incomplete evidential support (missing SIN-127 variance, aggregated CIFAR-10 reporting).

**Narrowing**: Round 2 confirmed the 5.0–6.0 range by pulling anchors at 4.67 (IKL — weaker), 5.67 (MLA theory — comparable), 6.00 (PLOT — comparable), and 6.25 (LORT — somewhat stronger on scale). CoLA sits in the 5.0–6.0 band, between the clearly weaker papers (4.67) and the somewhat stronger ones (6.25).

Final score: 5.5 — reflecting a solid methodological contribution with principled components and broad experiments, but held back by incomplete evidential support on a key benchmark (SIN-127 variance missing) and aggregated reporting that prevents full statistical assessment.

Now let me write the final review.

---

Let me verify: the SIN-127 table (Table 3) indeed shows no standard deviations. The CIFAR tables (Table 1-2) do show ± values. STL-10-LT (Table 2) shows ± values.

The paper's Table 3 caption: "Comparison on SIN-127." — no mention of standard deviations or number of runs. The text says "From the results in Table 3, we can observe that CoLA outperforms the other methods." This is problematic because ACR achieves 36.28 on 64×64, while CoLA gets 37.49 — a 1.21% gap, but without any variance measure, we can't assess if this is meaningful.

OK, let me now produce the review.## Summary

This paper identifies two blind spots in the dominant Logit Adjustment (LA) paradigm for Long-Tailed Semi-Supervised Learning (LTSSL): (1) naive frequency counting overestimates head-class prevalence due to sample redundancy, causing over-suppression; and (2) treating the overall adjustment strength τ as a fixed hyperparameter is brittle because the optimal τ is highly sensitive to the estimated distribution. The authors propose CoLA, which co-designs the two LA components by (a) replacing frequency counting with a De-Duplicated Distribution Estimate (DDDE) based on the effective rank of feature representations, and (b) learning τ via a Logit Meta-Calibration (LMC) procedure on a proxy set that mirrors the DDDE-refined distribution. A theoretical generalization bound links the two components. Empirically, CoLA achieves the highest mean accuracy across five distribution types on CIFAR-10/100-LT, STL-10-LT, and SIN-127.

## Strengths

1. **DDDE convincingly improves distribution estimation** (Section 4.1, Table 5). The effective-rank-based estimate consistently achieves the lowest L₂ distance to the true unlabeled distribution across all 10 tested scenarios on CIFAR-10/100-LT, outperforming MCA and NWGMA. This directly validates the core motivation that frequency counting overestimates head classes due to sample redundancy.

2. **Both components contribute and their interaction is empirically demonstrated** (Table 4, ablation study). The full CoLA (w/ D-L) outperforms variants with fixed τ (w/o D-τ) and LMC without DDDE (w/o D-L) across all 10 distribution-configurations on CIFAR-10/100-LT. The pattern that w/o D-L outperforms the best fixed-τ variant, and w/ D-L outperforms w/o D-L, cleanly shows that both accurate class-wise estimates and learned overall strength are necessary and synergistic.

3. **Broad experimental scope** — four benchmarks (CIFAR-10/100-LT, STL-10-LT, SIN-127) across six distribution types (consistent, uniform, reversed, middle, head-tail, unknown). This provides a reasonably comprehensive picture of the method's behavior across diverse long-tail scenarios.

## Weaknesses

### Fatal
None.

### Major

1. **SIN-127 results are reported without variance (Table 3).** No standard deviation, error bar, or seed count is given. Given that the CIFAR experiments show substantial variance (often 1–3% even at the per-distribution level), the absence of variance on SIN-127 makes the scalability claim ("CoLA can also be applied to large-scale datasets") uninterpretable. The margin over ACR on 64×64 (37.49 vs. 36.28) may or may not be meaningful without this information. This is a concrete omission that must be filled.

2. **Aggregated CIFAR-10-LT reporting obscures per-configuration performance (Section 6.2.1).** The paper averages over 2–4 distinct imbalance-ratio settings per distribution (×5 seeds), yielding standard deviations as large as 2–4% on CIFAR-10-LT. The high variance means that CoLA's mean advantage over baselines like ACR, Meta-Expert, and Sim-Pro may be driven by one setting rather than reflecting reliable superiority. The paper states that per-setting results are in Appendix J (stripped by the parser), but the main paper as presented does not allow a reader to verify how many configurations CoLA *strictly* dominates. A per-setting breakdown or a sign test across configurations would substantiate the SOTA claim.

### Minor

1. **Missing ablation of the linear vs. logarithmic form in LMC (Section 4.2).** CoLA replaces the standard `-τ·log p` with `-τ·p` (linear), citing Mor & Carmon (2025) for motivation. While the motivation is reasonable, this is a genuine design change relative to every LA-based baseline and the LA formulation in Eq. (1). The ablation in Table 4 compares full CoLA against variants that change multiple things at once (DDDE on/off, LMC on/off) but never directly tests `-τ·p` vs. `-τ·log p` within the LMC framework. This leaves ambiguous whether the gains attributed to meta-learning τ depend on the linear form or would also hold with the logarithmic form. A controlled comparison would resolve this.

2. **No statistical significance tests.** Given the large CIFAR-10-LT variance and the multiple comparisons, the paper would benefit from a paired test (e.g., Wilcoxon signed-rank) comparing CoLA against the best baseline per underlying configuration. This would directly quantify the reliability of the claimed improvements.

### Trivial

1. **Typo in Table 1:** The category header reads "Logo Adjustment-Based" instead of "Logit Adjustment-Based."

## Nice-to-Haves

- A breakdown of CIFAR-100-LT results by many/medium/few-shot groups would clarify whether CoLA's gains are concentrated on tail classes or spread uniformly.
- Adding a comparison with ADELLO (which the paper mentions deferring to Appendix I) to the main text rather than the appendix would strengthen the STL-10-LT evaluation.

## Removed Points

The following points raised by the harsh critic are removed or downgraded for the reasons stated:

- **"Missing ablation on the core design choice of LMC" as a Major issue**: Downgraded to Minor. The paper provides a clear motivation for the linear form (numerical stability, citation to Mor & Carmon 2025) and the ablation controls for the presence of LMC as a meta-learning procedure (w/o D-L uses LMC but without DDDE). The missing comparison is `-τ·p` vs. `-τ·log p` within LMC, which is informative but not a fundamental omission that invalidates the core claims.
- **"Aggregated reporting as a critical issue"**: Kept as Major but qualified. The per-setting data exists in Appendix J (which the parser stripped but exists in the original submission). The issue is that the main paper does not present this data in a way that allows statistical assessment. This is a presentation gap, not a data absence.
- **Section-by-section note about "convexity analysis... not present in the main text"**: Removed. The paper explicitly states "Due to page limitations, additional analysis... is presented in Appendix E and F." This is standard practice.
- **Strength Finder's claim #1 about DDDE mitigating over-suppression**: Kept and reformulated. The evidence (Table 5) supports it.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a key insight: the paper's central thesis — that the class-wise and overall LA components must be *co-designed* — is well-supported by the ablation results showing that LMC with DDDE outperforms LMC without DDDE, which in turn outperforms any fixed τ. This bidirectional dependency is cleanly demonstrated. A secondary observation is that the effective-rank-based DDDE could have applications beyond LTSSL, e.g., in any setting where frequency counting from high-confidence predictions is used to estimate class priors (e.g., self-training, partial-label learning). The reviews do not yield novel insights beyond what the paper itself articulates.

## Suggestions

1. **Add standard deviations (or at least the number of runs) to Table 3 (SIN-127)**. This is necessary to support the scalability claim.
2. **Include a per-setting breakdown or a sign test for the CIFAR experiments** — either in the main paper or by summarizing the number of configurations where CoLA strictly outperforms the best baseline.
3. **Run the controlled ablation comparing `-τ·p` vs. `-τ·log p` within LMC** (both with and without DDDE). Even a small-scale experiment (e.g., 2 distributions, 3 seeds) would clarify whether the linear form is critical.
4. **Fix the typo in Table 1** ("Logo" → "Logit").
5. **Include confidence intervals or statistical tests** for the main comparative results where standard deviations overlap with runner-up methods.

## Score and Decision

**Round 1 bracket**: 4.5–6.5 (derived from topic-band and weakness-anchored queries: low-band papers at ~3.0 are clearly weaker, mid-band at 3.8–6.25 are comparable, high-band >7.5 are different-genre top-tier papers). **Round 2 narrowing**: anchors at 4.67 (IKL — weaker, limited novelty), 5.67 (MLA theory — comparable), 6.00 (PLOT — comparable), 6.25 (LORT — stronger on scale) confirm the 5.0–6.0 band. **What the low-band anchors failed at**: limited novelty and insufficient experiments. CoLA does not share these failures — its DDDE and LMC components are genuinely novel and the experimental scope is broad. However, CoLA partially shares the failure mode of incomplete evidential support (missing SIN-127 variance, aggregated CIFAR-10 presentation). The score of 5.5 reflects a solid methodological contribution held back by these evidential gaps.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Weak Accept</decision>