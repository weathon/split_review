Here is my consolidated meta-review.

## Summary
FreDA proposes a test-time adaptation framework that handles heterogeneous (mixed-distribution) data streams by clustering incoming samples via their high-frequency Fourier amplitude components, then training separate fine-tuned models on each cluster with periodic parameter aggregation. A Fourier-domain amplitude perturbation augmentation module is also included. The paper provides extensive experiments across corrupted, natural-domain-shift, and medical benchmarks showing consistent improvements over existing TTA methods.

## Strengths

- **Novel, data-centric approach to heterogeneous TTA is well-motivated**: The paper identifies a genuine limitation in existing TTA methods — they assume homogeneity at each time step — and provides direct visual evidence (Figure 1 c–d) that high-frequency Fourier components separate samples from different Camelyon17 domains while model-extracted features do not. This grounding of the method in an observed property of the frequency domain is a concrete, evidence-backed insight.

- **Consistent and substantial empirical improvement across all benchmarks**: FreDA achieves the lowest error rate on every evaluated dataset. On CIFAR-10-C (Table 1) it reaches 22.9% vs. 26.2% for AdaContrast; on Camelyon17 (Table 2) 27.9% vs. 33.8% for the next-best method — a 5.9-point gain on a medical benchmark where most baselines fail to beat the no-training baseline. These are systematic, not isolated, wins.

- **Robustness to small batch sizes where prior methods collapse**: Figure 2 shows FreDA maintaining stable performance down to batch size 1 on CIFAR-10-C/100-C and ImageNet-C, while DeYO degrades from 27.7% to 89.8% error. This is a practical advantage distinguishing FreDA from existing methods.

- **Strong performance under the combined challenge of mixed distributions + dependent sampling**: Table 2 (right panel) shows FreDA at 23.0% on CIFAR-10-C under both challenges simultaneously, far ahead of the next-best UnMix-TNS at 41.9%, demonstrating applicability beyond the core scenario.

## Weaknesses

### Major

1. **Missing ablation: random clustering vs. Fourier clustering.** The ablation study (Table 4) shows that the Decentralized Training (DT) component — which includes Fourier-based clustering + K-model fine-tuning — accounts for most of the improvement (baseline 44.1% → DT 24.8% on CIFAR-10-C). Adding the other components only yields 1.9 more points. This makes it impossible to tell whether the gain comes from Fourier clustering producing semantically meaningful partitions, or simply from splitting data into K arbitrary groups and training separate models. A control where samples are assigned to K clusters randomly (matched to the same cluster sizes) would isolate the value of the Fourier insight. Without it, the core claim that "Fourier-space separation" is responsible for the improvement remains unvalidated.

2. **Cluster count K is not reported, and its sensitivity is not analyzed.** The number of clusters K is a critical structural parameter listed in Algorithm 1 but never given a numerical value for any experiment. The method's behavior depends entirely on whether K matches (or approximates) the true number of distribution types (15 on CIFAR-10-C, 5 on Camelyon17, 4 on DomainNet126). If K is set to these exact numbers, the method benefits from information no baseline has. If K is set arbitrarily, the sensitivity to misspecification is unknown. A sensitivity sweep over K (e.g., K=2,5,10,15,20 on CIFAR-10-C) is necessary to establish that the method works without oracle knowledge.

### Minor

3. **No quantitative evaluation of clustering quality.** The paper's central empirical claim is that high-frequency Fourier features separate distribution shifts. Yet the only evidence is a single t-SNE visualization on Camelyon17 (Figure 1d). No quantitative metrics (e.g., adjusted Rand index, normalized mutual information, purity) are reported for any dataset. Since the entire method depends on the clustering being reliable across 15 different corruption types on CIFAR-10-C, Gaussian noise on ImageNet-C, and natural domain shifts on DomainNet126, and since t-SNE can make even random structure look separated, quantitative clustering metrics across all datasets are needed.

4. **Fourier-based augmentation provides only small, though consistent, gains.** When added to the full pipeline (DT+SS), Sample Augmentation (SA) improves error rates by 0.8–2.2 percentage points across the four datasets. These gains are consistent but modest relative to the system's complexity. The paper frames augmentation as a core contribution, but the evidence suggests it is a minor supplementary component.

5. **No discussion of high-frequency mask limitations.** The method discards all low-frequency information (Eq. 4), which is motivated by the observation that high frequencies capture texture/style differences. However, some corruption types (e.g., brightness, contrast) manifest primarily in low frequencies. The paper does not discuss whether or how the clustering handles such shifts, nor does it analyze failure cases where this masking could be detrimental.

### Trivial

None.

## Nice-to-Haves
- Report computational cost (wall-clock time, total parameters trained per step) to help practitioners assess the resource trade-off of maintaining K models.
- Specify whether corruptions are interleaved at the sample level or in blocks in the mixed-distribution setting.
- A discussion of the method's limitations and settings where it might underperform.

## Removed Points
The following points from the original reviews were removed with justification:

- **"Conflates method benefit with computational resource advantage"** — Demanding that FreDA match single-model parameter count or compute is unreasonable; the method's design uses K models, and it is evaluated as such. The valid sub-concern (random-clustering ablation) is retained as Weakness #1 above. The broader compute-asymmetry argument is removed.
- **"Missing implementation details make results non-reproducible"** — Under review policy, undisclosed hyperparameter values (learning rate, H₀, ε, α, σ, λ, N, f) are classified as nitpicks about reproducibility and removed. The separate concern about K (which is structural, not a mere hyperparameter) is retained as Weakness #2.
- **"Camelyon17 table missing row labels"** — This is almost certainly a PDF extraction / formatting artifact rather than an author error; removed per policy on formatting artifacts.
- **"The primary source of improvement is having multiple specialized models rather than any insight about Fourier separation"** — This frames the decentralized training component as separate from the Fourier insight, when in fact DT includes Fourier clustering. The valid sub-request (random-clustering control) is retained; the framing as a resource advantage is removed as inaccurate.
- **Strength: "Ablation study validates synergy of all three components"** — The synergy claim is weak; DT alone provides the vast majority of the gain, and SA+SS add only 1.9 points. The evidence for synergy is limited, so this strength is dropped.
- **Strength: generic formulations about addressing important problems** — Removed as superficial.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a useful framing of the core weakness (random-clustering baseline would disambiguate the Fourier contribution) and the K sensitivity gap, but these are observations about missing analyses, not synthesized insights.

## Suggestions
1. **Add a random-clustering ablation** where samples are partitioned into K groups by random assignment (matched in size to the Fourier clusters) before decentralized training. If Fourier clustering outperforms random assignment, the core claim is supported.
2. **Report K for every dataset and run a sensitivity analysis** (K=2,5,10,15,20 on CIFAR-10-C; K=2,4,6 on DomainNet126). Show that performance does not collapse when K deviates from the true number of domains.
3. **Report clustering accuracy metrics** (adjusted Rand index or purity) for Fourier-based K-means against ground-truth distribution types on all datasets.
4. **Acknowledge the limitation** that the method discards low-frequency information, and discuss which types of shifts this might miss.

## Score and Decision
This paper tackles a real and under-explored problem, proposes a creative, well-motivated approach, and delivers strong empirical results across diverse benchmarks. The two major weaknesses — the missing random-clustering ablation and the unreported K value with no sensitivity analysis — are addressable and do not invalidate the core idea, but they prevent full validation of the central claim that Fourier clustering is the source of the improvement. The paper is solid and the contributions are real, but these gaps should be resolved before it is accepted.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>