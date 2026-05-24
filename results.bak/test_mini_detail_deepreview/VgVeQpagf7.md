## Summary

This paper proposes SPS (Summarize-Privatize-Synthesize) and its enhanced variant SPS+, differentially-private dataset-distillation algorithms that generate a synthetic version of a sensitive dataset using a public pretrained model. The method privatizes intermediate activation statistics (means and covariances) via the Gaussian mechanism and then synthesizes images that match these statistics. On CIFAR-10 and CIFAR-100, SPS+ achieves **96.2%** and **76.6%** at ε=1, surpassing the best DP-SGD results from De et al. (2022), making it the first generation-based method to outperform gradient-based private training on these benchmarks. The paper also demonstrates flexibility advantages including ensembling, federated learning, and continual learning without additional privacy cost.

## Strengths

1. **First generation-based method to exceed DP-SGD accuracy on standard image classification benchmarks.** Table 1 shows SPS+ (WRN34-10 Ensemble) achieves 96.2% on CIFAR-10 and 76.6% on CIFAR-100 at ε=1, compared to 94.8% and 70.3% from De et al. (2022). This is a genuine milestone for the DP synthetic data generation paradigm. Single-model results (SPS+ WRN28-10: 95.1% vs. 94.8% at ε=1) also show consistent improvement.

2. **Lower-dimensional privatized statistics improve SNR relative to DP-SGD.** As argued in Section 3.2.2, by tuning the projection dimensions D_G and D_C, the dimensionality of released statistics can be kept around 10^5, while DP-SGD gradients are typically 10^7 or more. This is a concrete architectural advantage tied directly to the paper's accuracy gains.

3. **Flexibility beyond DP-SGD demonstrated across multiple settings.** Section 5.5 shows SPS+ enables asynchronous federated learning with strong results (outperforming FedLAP-DP and FedDM). Section 5.6 demonstrates class-incremental continual learning on CIFAR-100 reaching 68.1% at ε=4, with no extra privacy cost for reusing the synthetic data. The post-processing property of DP (Section 3.2.5) allows using advanced optimizers like GSAM without additional privacy cost — a practical advantage the paper correctly highlights.

4. **Out-of-domain generalization on histopathology.** Table 2 shows SPS achieves 92.6% on CAMELYON17 at ε=8, outperforming DP-Diffusion (91.1%), Private Evolution (79.6%), and DP-SGD (90.5%), despite significant domain shift between ImageNet pretraining and medical images.

5. **Quantitative link between synthetic data quality and downstream accuracy.** Figure 3 shows a clear negative correlation between FID and accuracy, providing empirical evidence that better-quality synthetic images lead to better classification performance.

## Weaknesses

### Fatal
None.

### Major

- **The GPC (Grouped Pseudo-Classes) mechanism lacks theoretical analysis.** Section 4.2 describes the technique only heuristically: "only works due to dynamics of optimizing the loss function, specifically the Σ inversion in the KL-divergence, and the eigenvalue clipping of Σ." The paper explicitly states the method "does not offer benefits for direct mean estimation" but provides no analysis of why it works for the KL-based objective, how many pseudo-classes to use, or how grouping is performed. This is a genuine gap that limits understanding of the method's mechanics.

- **The DP-SGD baseline comparison, while not unfair, has a subtle confound that the paper does not fully discuss.** The paper compares against De et al. (2022), which uses the same public pretrained model (WRN22-8 trained on 32×32 ImageNet) — the paper says "in line with prior work (De et al., 2022)". However, SPS uses the pretrained model not just as initialization for fine-tuning (as DP-SGD does), but also as a feature extractor during the distillation process itself (to compute activation statistics). This means SPS extracts more "utility" from the same public model. This is a legitimate design advantage of the method, but the paper's framing that SPS+ "outperforms DP-SGD" would benefit from acknowledging this additional source of advantage. A controlled ablation where SPS is compared to DP-SGD fine-tuned from the *same* pretrained feature extractor (not just the same pretrained weights) would clarify the source of gains.

### Minor

- **Theorem 4.1 contains a typographical error.** The formula states ε = Mα/(2δ²), but the denominator should involve the noise scale σ², not the DP failure parameter δ. This is clearly a typo (the proof is in Section C.1 which was stripped), but it makes the formal statement misleading as written.

- **Private Evolution comparison at mismatched ε values.** Table 1 lists Private Evolution at ε=10 while SPS+ results are at ε=1–8. The best generation-based baseline is thus not compared on the same privacy budgets. The paper references Section F for additional comparisons, but that section is in the appendix.

- **CAMELYON17 DP-SGD baseline uses a different setup.** The DP-SGD number (90.5% at ε=10) is cited from Ghalebikesabi et al. (2023), not from a controlled experiment with the same architecture and pretraining. The improvement from 90.5% to 92.6% is modest and may not hold under fully matched conditions.

- **Continual learning performance drop is not benchmarked against a DP-continual baseline.** The performance drop from 76.9% (joint) to 68.1% (continual) at ε=4 is a ~9% degradation, but the paper does not compare to a DP-SGD continual learning baseline (e.g., DP-EWC), so it is unclear whether this degradation is better or worse than alternatives.

### Trivial
- The paper could standardize the notation for the clipping bound more clearly — the formula in Section 3.2.2 uses K_clip while the noise redistribution section (3.2.4) uses a slightly different form.

## Nice-to-Haves
- A controlled ablation isolating the contributions of multistage clipping vs. grouped pseudo-classes (SPS+ without MC, SPS+ without GPC) would clarify the importance of each component.
- Quantifying the computational cost (GPU-hours, wall-clock time) for generating 50k synthetic images at ε=1 vs. training a DP-SGD model to convergence would help practitioners evaluate the trade-off.
- Clarifying how the eigenvalue clipping of Σ (Section 3.2.3) handles negative eigenvalues that arise from noisy covariance estimates would improve reproducibility.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Unfair baseline comparison — DP-SGD baseline does not use a pretrained model"** (Harsh Critic point #1). **REMOVED.** This is factually incorrect. De et al. (2022) explicitly uses public pretrained models (WRN22-8 trained on 32×32 ImageNet). The paper states "in line with prior work (De et al., 2022)" and cites De et al. as an example of "common practice in the DP literature" of using public pretrained models (Section 3.2.1). The critic's claim that De et al. "trains from scratch on CIFAR" is wrong.

- **"Sensitivity analysis for per-class statistics is incorrectly specified"** (Harsh Critic point #2). **REMOVED.** The paper's clipping bound ‖v‖_max = K_clip √(L D_G^layer + |L_C| D_C^layer) correctly accounts for sparsity: due to the indicator function in Eq. 3, each data point has non-zero entries only in one class block. The bound does not include the C factor, correctly reflecting that only one class contributes per example. The critic's concern about the L2 norm being "not C√(...)" is exactly what the paper's formula already does. The noise is added to the full d_tot-dimensional vector, but the sensitivity (which determines the noise scale) is based on the correct per-exponent sparsity-aware bound.

- **"Missing Section F"** and **"Missing appendix content"** — **REMOVED.** These sections are in the appendix, which was stripped by the PDF parser. The original submission contains them.

- **"Missing related works"** — **REMOVED** per hard rule (cannot verify existence of external works).

- **"Missing computational cost"** — **REMOVED** as a major weakness. The paper explicitly mentions in Section 6 that "The cost of generating these images is relatively heavy (see section F.1 for discussion)," placing the discussion in the appendix. Moved to Nice-to-Haves.

- **"Formatting/style nitpicks and typo criticisms"** — **REMOVED** per hard rule.

## Novel Insights

The reviews surface a genuine tension in DP synthetic data evaluation: the paper's headline claim rests on comparing against De et al. (2022), which does use the same public pretrained model paradigm, but SPS exploits the pretrained model more extensively (as a feature extractor during distillation, not just initialization). This is a deeper version of the common "fair comparison" concern — not about cheating, but about understanding exactly where the gains come from. The paper's flexibility results (federated learning, continual learning, ensembling) are arguably more novel contributions than the marginal accuracy improvement over DP-SGD, because they demonstrate advantages that DP-SGD structurally cannot provide (unlimited reuse, no composition cost). The GPC mechanism, while heuristically described, is a genuinely interesting idea that connects DP noise mitigation to the geometry of the KL-divergence and eigenvalue clipping — a direction that deserves deeper analysis in future work.

## Suggestions

1. Add a controlled ablation experiment comparing SPS+ to DP-SGD fine-tuned from the **same pretrained features** (not just the same pretrained model), to isolate the advantage of the distillation+generation pipeline from the advantage of using the pretrained model as a feature extractor.
2. Fix the typo in Theorem 4.1 (δ² → σ²).
3. Provide a theoretical or intuitive explanation for why Grouped Pseudo-Classes work specifically with the KL-divergence + eigenvalue clipping objective, beyond the current heuristic description.
4. Report computational cost (GPU-hours, wall-clock time) for the main CIFAR-10/100 experiments at ε=1 and ε=8, to help practitioners evaluate the trade-off against DP-SGD.

## Score and Decision

**Round 1 (Bracketing):** The paper sits clearly above the weak anchors (2.5–3.0 range, which are papers with fundamental method flaws) and below the strong anchors (7.5+ range, exceptionally clean papers). The plausible bracket is **5.0–7.5**.

**Round 2 (Narrowing):** I retrieved anchors at 6.0, 6.25, 6.33, 6.5, and 7.0. The closest topical match is the 6.25 anchor ("Differentially Private Synthetic Data via Foundation Model APIs 1: Images"), which was accepted. The current paper has comparable or greater technical depth (actual algorithm design vs. API-based black-box usage) and stronger downstream classification results. However, it has more minor presentational issues (theorem typo, GPC heuristic analysis). The 7.0 anchor ("Towards Lossless Dataset Distillation") is cleaner but lacks the DP dimension. Comparing directly: the current paper is stronger than the 6.0 anchors (synthetic data audit, privacy analysis), comparable to the 6.25–6.33 anchors, and slightly below the 7.0 anchor. This places the paper firmly at **6.5**.

**Calibration anchors used across all rounds:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `TbOcySs6g8.md` | 2.50 | 1 | Fundamentally flawed paper; this paper is much stronger |
| `sruGNQHd7t.md` | 3.00 | 1 | Weak privacy method; this paper is much stronger |
| `KYipmCMmSO.md` | 6.33 | 1 | Similar DP fine-tuning topic; this paper has stronger empirical results but less theory |
| `nAR9xu8WM6.md` | 4.50 | 1 | DP-CLIP paper with serious experimental flaws; this paper is considerably stronger |
| `F52tAK5Gbg.md` | 4.00 | 1 | DP-SGD variant; this paper is stronger |
| `HOpQt44EzC.md` | 5.25 | 1 | DP vision-language; this paper has clearer contributions |
| `oZtt0pRnOl.md` | 8.00 | 1 | Very clean DP paper; this paper is weaker |
| `C8niXBHjfO.md` | 6.00 | 2 | Synthetic data privacy audit; this paper is slightly stronger |
| `YEhQs8POIo.md` | 6.25 | 2 | DP synthetic data via APIs; closely comparable — similar topic, similar quality, this paper has more technical depth |
| `rTBL8OhdhH.md` | 7.00 | 2 | Lossless dataset distillation without DP; cleaner evaluation but different topic |
| `1NHgmKqOzZ.md` | 6.33 | 2 | Progressive dataset distillation; comparable quality |
| `svIdLLZpsA.md` | 6.00 | 2 | Distribution matching for synthetic data; this paper is slightly stronger |
| `8rbkePAapb.md` | 6.20 | 2 | Privacy+fairness; different topic, comparable quality |
| `sVNfWhtaJC.md` | 6.50 | 2 | DP prompt synthesis; comparable quality, different domain |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>