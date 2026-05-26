## Summary

This paper introduces SPS and SPS+, algorithms for generating differentially private (DP) synthetic datasets by adapting dataset-distillation techniques (specifically D3S-style activation-statistic matching) to the DP setting. The core idea is to privatize intermediate activation statistics from a public pretrained model using the Gaussian mechanism, then synthesize images that match those statistics via KL-divergence minimization. On CIFAR-10/100, SPS+ achieves 96.2%/76.6% at ε=1, which is the first time a generation-based method has matched or exceeded state-of-the-art DP-SGD accuracy on these benchmarks. The paper also demonstrates benefits for ensembling, federated learning, and continual learning without additional privacy cost.

## Strengths

1. **First generation-based method to match DP-SGD accuracy on standard image benchmarks**: Table 1 shows SPS+ (WRN34-10 ensemble) achieving 96.2% on CIFAR-10 and **76.6% on CIFAR-100** at ε=1, compared to the best DP-SGD numbers of 94.8% and 70.3% from De et al. (2022). On CIFAR-100 the margin is substantial (~6 pp), and even at the same architecture (WRN28-10, no ensemble) SPS+ achieves 71.0% vs 70.3%.

2. **Principled dimensionality control gives SNR advantage over DP-SGD**: By projecting high-dimensional activations into smaller embedding spaces (D_G, D_C) and releasing only first/second moments (~10⁵ dimensions vs DP-SGD's ~10⁷), SPS achieves inherently better signal-to-noise ratio. The paper provides a clear analytical argument (Sec. 3.2.2, footnote 1).

3. **Enables downstream tasks infeasible under DP-SGD**: Because SPS produces a dataset rather than a model, it supports ensembling, federated learning, and continual learning without additional privacy cost. The federated learning experiment (Fig. 5d-e) shows accuracy improving from 86% to 89.5% at ε=1 with more data sources — a scenario where DP-SGD would require costly per-party composition.

4. **Strong cross-domain generalization**: On CAMELYON17 (histopathology) with ImageNet-pretrained models — a significant domain shift — SPS achieves 92.6% at ε=8, outperforming DP-Diffusion (91.1%), DP-SGD (90.5%), and Private Evolution (79.6%).

5. **Flexible dataset sizes**: SPS+ can generate datasets both smaller (10% of original with ~1% accuracy drop on CIFAR-10) and larger (up to 4×, with further gains on CIFAR-100), capabilities DP-SGD cannot offer.

## Weaknesses

### Major

1. **Grouped Pseudo-Classes (GPC) description is too vague to be reproducible or properly evaluated.** Section 4.2 introduces GPC as a core component of SPS+ but the description is critically incomplete. The variable N_{c/p} is never clearly defined — the paper states "each class belongs to PN_{c/p}/C pseudo-classes" without specifying how N_{c/p} is set. The claim that GPC "only works due to dynamics of optimizing the loss function, specifically the Σ inversion in the KL-divergence, and the eigenvalue clipping" is asserted without any analysis, derivation, or even a small-scale validation. Since GPC is one of two principal enhancements that distinguish SPS+ from SPS, and the reported gains (especially on CIFAR-100) are significant, the lack of a clear description and supporting analysis is a substantial gap. The paper also provides **no ablation study isolating the individual contributions** of multistage clipping (MC) and GPC — Table 1 only compares SPS vs SPS+ (MC+GPC combined), so the reader cannot assess how much each component contributes.

2. **Theorem 4.1 contains an error in the stated RDP guarantee.** The theorem claims ε = Mα/(2δ²) for the composition of M Gaussian mechanisms under RDP. This is incorrect: the RDP guarantee of the Gaussian mechanism is a function of the noise multiplier b₀, not the approximate-DP parameter δ. The correct expression is ε(α) = Mα/(2b₀²). The paper uses δ = 10⁻⁵ as the DP delta parameter; plugging it into the stated formula would give absurdly large ε values (~10¹⁰). While the paper references an external RDP accountant (Ahmed et al., 2025) for the actual experiments, and the appendix presumably contains the correct analysis, the presence of a mathematically wrong formula in a theorem statement in the main text is a significant error that must be corrected.

### Minor

3. **The central claim of outperforming DP-SGD relies on a literature baseline that is not controlled.** The paper compares to DP-SGD numbers from De et al. (2022) without reproducing that baseline. At the same architecture (WRN28-10), the margins on CIFAR-10 are small (0.3% at ε=1) with overlapping error bars (SPS+: 95.1±0.3, DP-SGD: 94.8±0.1). The strongest claimed advantages use larger architectures (WRN34-10) and ensembles (5 models) against a single-model DP-SGD baseline. While comparing to published SOTA is standard practice, for a headline claim this strong the paper would benefit from at least one controlled comparison under the same pretrained model and evaluation pipeline.

4. **No ablation separating MC and GPC contributions.** The paper only shows SPS vs SPS+ (both MC and GPC together). Without isolating each component, it is impossible to tell whether the gains come primarily from multistage clipping, grouped pseudo-classes, or their interaction. Figure 2 shows the effect of varying M (number of MC stages) within SPS+, but the individual contribution of GPC is never reported.

5. **Missing hyperparameter values that are crucial for the SNR argument.** The paper argues that SPS has lower dimensionality than DP-SGD (~10⁵ vs ~10⁷) but never reports the actual values of D_G, D_C, and |L_C| used in the experiments. Without these, the reader cannot verify the dimensionality or the claimed SNR advantage in practice.

6. **The noise redistribution technique (Sec. 3.2.4) lacks an explicit sensitivity recomputation.** The paper rescales per-class statistics by √S and states that "b₀ remains the same." A brief derivation confirming the ℓ₂ sensitivity of the rescaled vector would add rigor.

7. **Computational cost is acknowledged but not quantified.** The paper notes generation is "relatively heavy" but provides no wall-time or FLOP numbers for either generation or fine-tuning, making it difficult to assess practical trade-offs against DP-SGD.

### Trivial

8. Theorem 4.1 uses δ in a formula where b₀ (the noise multiplier) is intended. Notation should be fixed for consistency with the surrounding text, which correctly uses b₀ for the noise multiplier and δ for the approximate-DP parameter.

## Nice-to-Haves

- An ablation study isolating the individual contributions of MC and GPC.
- Reporting typical values of D_G, D_C, |L_C| used in experiments.
- A controlled DP-SGD comparison at a few ε values using the same pretrained model and fine-tuning recipe.
- Quantified computational cost (wall time for generation vs. DP-SGD training).
- Explicit confirmation that the parallel-composition argument holds for the federated learning setting (disjoint data partitions do not compose).

## Removed Points

- **"Uncontrolled DP-SGD baseline undermines the central claim" (framed as fatal)**: REMOVED as fatal — kept as Minor (#3). The paper compares to published SOTA from De et al. (2022), which is standard practice. The lack of a controlled replication is a legitimate concern but does not invalidate the contribution.
- **"Federated learning baselines not described" and "continual learning comparison to non-private is insufficient"**: REMOVED as scope creep. These experiments are demonstrations of flexibility, not the paper's central contribution. The baselines are cited and the qualitative claims are appropriate.
- **"Missing related works"**: REMOVED per protocol — cannot penalize for references I cannot verify externally.
- **"Abstract should qualify comparison conditions"**: REMOVED — presentation nitpick. Conditions are specified in the main text and Table 1.
- **"Appendix-dependent proof" complaint**: REMOVED per protocol — the parser strips appendices from all papers. The proof exists in the original submission.
- **Strength Finder's generic strengths about problem importance, topic relevance, and writing quality**: REMOVED per filtering rules. Only strengths backed by specific experimental evidence are retained.

## Novel Insights

The reviews collectively highlight an interesting tension: the paper's strongest empirical showing (CIFAR-100 at ε=1: 76.6% vs DP-SGD's 70.3%) is on the challenging many-class dataset, which is exactly where the GPC mechanism is designed to help by reducing the O(C/N) noise rate in per-class statistics. Yet this component — arguably the most novel methodological contribution — is the least clearly described. The paper's core innovation (privatizing activation statistics from dataset distillation) is well-motivated and the empirical results are strong, but the scientific narrative would benefit substantially from a more rigorous treatment of GPC, including both a clear formal description and an ablation isolating its effect.

## Suggestions

1. **Fix Theorem 4.1**: Replace δ² with b₀² (the noise multiplier) in the RDP formula, and provide a brief derivation or explicit citation to the standard RDP of the Gaussian mechanism.

2. **Clarify GPC**: Define N_{c/p} explicitly, provide the assignment procedure for creating pseudo-classes, show a formal argument for the noise reduction, and add an ablation table separating MC and GPC contributions.

3. **Add a controlled DP-SGD comparison**: For at least one or two ε values, run DP-SGD under the same conditions (same pretrained model, same evaluation protocol) to directly isolate the effect of synthetic data vs. private gradients. De et al. (2022) open-sourced their code, making this feasible.

4. **Report dimensionality hyperparameters**: Include a table showing D_G, D_C, |L_C|, and d_tot for each experiment so readers can verify the SNR claim.

5. **Provide compute estimates**: A supplementary table showing wall-clock time or GPU-hours for generation vs. DP-SGD training would help practitioners assess the method's practicality.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing**

| Anchor | Avg Score | Bucket | Comparison |
|--------|-----------|--------|------------|
| kzePnQWUvC (Tabular DD) | 3.33 | R1-topic-low | Much weaker: tabular domain, very weak results. Our paper is substantially stronger. |
| TbOcySs6g8 (DP Synthetic Alignment) | 2.50 | R1-topic-low | Much weaker: fatal DP flaws in clustering. Our paper has a sounder DP foundation. |
| ckabXglfiT (Privacy as Free Lunch) | 4.75 | R1-topic-mid | Weaker: fatal DP concerns about sampling without noise; rejected. Our paper has proper DP guarantees. |
| C8niXBHjfO (Synthetic Data Privacy Analysis) | 6.00 | R1-topic-mid | Different type (analysis paper), well-executed. Comparable overall quality. |
| YEhQs8POIo (Private Evolution) | 6.25 | R1-topic-high | Most comparable: DP synthetic image generation. Our paper has stronger classification accuracy but weaker presentation clarity. |
| nATTIkte9f (LMO-DP) | 4.75 | R1-weakness (DP-SGD baseline) | Weaker: imprecise presentation, privacy concerns; rejected. |
| fj5SqqXfn1 (Pitfalls for Privacy Accounting) | 5.00 | R1-weakness (privacy error) | Different type (privacy accounting), but shares dimension of addressing accounting concerns. |

**Round 1 bracket**: 4.5–6.5.

**Round 2 — Narrowing within bracket**

| Anchor | Avg Score | Bucket | Comparison |
|--------|-----------|--------|------------|
| 1NHgmKqOzZ (Progressive DD) | 6.33 | R2 | Dataset distillation without DP. Similar quality. |
| 0no1Wp2R2j (Class-aware CMI DD) | 5.25 | R2 | Dataset distillation without DP. Accepted but with concerns. |
| svIdLLZpsA (Real-Fake Distribution Matching) | 6.00 | R2 | Synthetic data for training. Accepted. |
| txZVQRc2ab (RAPID DP Diffusion) | 6.00 | R2 | DP diffusion models. Accepted. |
| HOpQt44EzC (DP Vision-Language) | 5.25 | R2 | DP training. Rejected. |

**Low-band failures**: The low-band anchors (≤3.33) all had fatal flaws in their privacy analysis or extremely weak results. Our paper shares neither of these failures — the DP mechanism is sound (standard Gaussian mechanism on privatized statistics), and the results are strong. The Theorem 4.1 typo is a presentation error, not a fatal privacy flaw.

**Final score rationale**: The paper presents a genuine methodological contribution with impressive results, placing it well above the low-band anchors (≤3.33). However, the unclear GPC description (Major #1), the Theorem 4.1 error (Major #2), and the reliance on an uncontrolled DP-SGD baseline for the central claim (Minor #3) prevent it from reaching the 6+ range occupied by the strongest accepted papers in this space. Compared to Private Evolution (6.25), the closest comparable, this paper has stronger accuracy but weaker methodological clarity and a concrete error in a theorem statement. Score of 5.5, Recommend Accept pending satisfactory rebuttal addressing Major weaknesses.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>