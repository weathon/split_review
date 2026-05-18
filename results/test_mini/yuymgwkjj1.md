Now I have sufficient calibration material. Let me produce the final review.

## Summary

This paper addresses the well-known complexity bias in normalizing flows—the tendency to assign higher likelihoods to simpler inputs even when they are OOD. The authors propose training with synthetic low-complexity outliers (generated via CutPaste/CutMix/MixUp + Gaussian blur for images, length filtering + WordNet synonym replacement for text) combined with a softplus-based bounded loss that penalizes high likelihood on OOD inputs without numerical instability. Experiments on benchmark image datasets, high-dimensional datasets, and a limited text setup show improvements over MLE and a real-outlier baseline.

## Strengths

- **Modality-spanning synthetic outlier generation.** The paper proposes concrete recipes for both images (stochastic augmentation + Gaussian blur, Sec. 2.2.1) and text (length filtering + synonym substitution, Sec. 2.2.2). The image pipeline is ablated into three variants (blur-only, CCM-only, and combined) across Tables 2–3, allowing readers to see the contribution of each component.

- **Softplus-based adverse likelihood loss avoids manual thresholding.** The loss in Sec. 2.3 uses Softplus(log p(x′)) which remains bounded as p(x′)→0. The gradient factor p/(1+p) automatically down-weights very-low-probability outliers, removing the need for a hand-chosen clamping threshold used in prior work (Schmier et al. 2022). Figure 1 visually confirms the bounded loss surface.

- **Consistent gains on high-dimensional real-world datasets.** Table 5 shows that plugging the proposed training into existing flow-based methods (CS-Flow, FastFlow) improves AUROC on Chest X-ray (e.g., FastFlow: 90.3% → 93.4%), RealBlur, and KonIQ-10k, demonstrating applicability beyond low-resolution benchmarks.

- **Synthetic outliers can approach or surpass a real-outlier baseline.** In several configurations (e.g., CIFAR-10→LSUN in Table 2: 97.5 AUROC vs. RO 96.9), the fully synthetic approach matches or exceeds training with 10% labeled real outliers, suggesting the method is a viable substitute when real OOD labels are unavailable.

## Weaknesses

### Major

- **Missing comparisons to the most directly relevant prior methods.** The paper cites SANFlow (Kim et al., 2023), Outlier Exposure (Hendrycks et al., 2018), and Virtual Outlier Synthesis (Du et al., 2022) in the introduction but does not include any of them as baselines. SANFlow is particularly relevant because it also trains normalizing flows with synthetic outliers. Without these comparisons, the reader cannot assess whether the proposed synthetic generation and softplus loss offer meaningful advantages over existing approaches, or whether the reported gains could be matched or exceeded by simpler alternatives. This is the single most significant weakness and limits the paper's ability to substantiate its claimed contribution.

- **Text experiments are too limited to support cross-modality claims.** The text evaluation (Sec. 3.3) uses only one ID dataset (IMDb), a single baseline (MLE), and small test sets (2,000 samples). The large gains on SST-2 (+35.1% AUROC) are reported without any non-MLE text OOD detection baselines (e.g., likelihood ratios, energy-based methods, or other flow-based text OOD detectors). While the paper is primarily about images, the text experiments as presented are a toy demonstration and do not convincingly show that the method generalizes to discrete data.

### Minor

- **Lipschitz constant analysis is heuristic and loosely connected to the core claims.** The Lipschitz estimate (max gradient norm over 1,000 samples, Sec. 3.1) is a rough approximation of the true local Lipschitz constant, and the paper does not establish a causal or even correlational link between this increase and OOD detection improvement. The analysis is presented as supporting evidence for Hypothesis 1, but the connection is asserted rather than tested (e.g., via controlled manipulation of the Lipschitz constant). This section adds little to the paper's evidential weight and could be de-emphasized or removed without harming the core contribution.

- **MVTecAD dataset is mentioned but results are absent.** The paper states "We also conducted experiments on the MVTecAD dataset" (Sec. 3.2) but no MVTecAD results appear in Table 5 or elsewhere.

- **No verification that synthetic text outliers are actually low-complexity OOD.** The text generation procedure (length filtering + WordNet synonyms) is described, but the paper does not verify that the resulting synthetic texts have lower complexity than the ID data (e.g., by reporting compressed bit-lengths) or that they are actually OOD in any meaningful sense.

### Trivial

- Complexity-adjusted scoring is shown to be misleading when OOD data is more complex than ID data (Tables 2–3). The paper acknowledges this, but the presence of both scoring methods without a principled selection rule adds unnecessary clutter.

## Nice-to-Haves

- A sensitivity analysis for the outlier synthesis probability (currently fixed at 0.5) and the Gaussian blur radius (fixed at 1) would strengthen the empirical characterization.
- An ablation on the text side comparing the full pipeline to simpler alternatives (e.g., length filtering only) would clarify which component drives the improvement.
- Reporting confidence intervals or multiple runs would improve reliability of the reported numbers.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **"No ablation isolating each component"** — The paper does have ablation: Tables 2 and 3 separately report "Gaussian blur," "CCM," and "CCM + Gaussian blur" variants.
- **"Abstract oversells by claiming 'comparable'"** — The results show synthetic outliers matching/exceeding RO in some cases and falling short in others. "Comparable" is a reasonable characterization.
- **"Softplus loss is marginal contribution"** — The paper explicitly distinguishes its approach from Schmier et al. (2022)'s threshold-based method. While incremental, the difference is meaningful and claimed accurately.
- **"Lack of comparison to methods not requiring OOD data"** — The paper claims to improve over standard MLE (no OOD data) which is included. Comparing to typical-set scoring or likelihood-ratio methods would be a nice addition but is outside the paper's stated scope.
- Various formatting/style nitpicks and reproducibility concerns about trivial implementation details.

## Novel Insights

None beyond the paper's own contributions. The insight that synthetic low-complexity outliers combined with a softplus-bounded loss can mitigate the complexity bias in normalizing flows is the paper's core observation, and it is novel at the level of technique combination. However, the broader observation that outlier exposure helps flow-based OOD detection is already present in SANFlow (Kim et al., 2023), and the softplus trick is a small variation on prior bounded-loss formulations.

## Suggestions

1. **Add SANFlow as a baseline** on the same CIFAR-10/100 and iSUN benchmarks. This is the most directly comparable method and its absence prevents proper evaluation of the paper's contribution.
2. **Expand text experiments** to include at least one more ID dataset and one non-MLE OOD detection baseline (e.g., a likelihood-ratio approach or an energy-based detector).
3. **Either strengthen or remove the Lipschitz analysis.** Either connect it rigorously to OOD performance (e.g., by demonstrating that models with higher Lipschitz constants consistently detect OOD better), or drop it as a claimed contribution.
4. **Include MVTecAD results** or remove the mention.
5. **Verify synthetic text outliers** by reporting their compressed bit-lengths relative to ID data.

## Score and Decision

**Calibration Anchors (all from the human-review corpus):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| N6ba2xsmds (HamOS) | 6.75 | Superior paper: comprehensive baselines including OE/VOS/NPOS, stronger theoretical motivation (HMC sampling), SOTA results. Under-review paper is weaker in both evaluation breadth and theoretical depth. |
| jQ596tXT3k (Likelihood Peaks) | 5.67 | Comparable overall quality but different contribution (theoretical explanation vs. empirical method). Under-review paper has clearer methodology but a critical gap in missing baselines that the Likelihood Peaks paper does not share. |
| 0rACj8JLAL (BOOD) | 5.50 | Similar domain (outlier synthesis for OOD). BOOD has more thorough evaluation with proper SOTA baselines. Under-review paper has a simpler, more general method but weaker evaluation. |
| gRXLa6LS3J (FoMo-0D) | 5.75 | Different approach (zero-shot pretrained transformers). Stronger empirical validation with multiple datasets and baselines. |
| Go8hf9wKJx (DOG) | 4.25 | Similar weaknesses: limited experiments and missing some baselines. Under-review paper has better ablation and cross-modality demonstration but shares the baseline gap. |
| X7nz6ljg9Y (NFL + Kolmogorov) | 5.00 | Different topic entirely. Comparable score band—both papers have a recognizable contribution held back by evaluation gaps. |
| 6Z8rZlKpNT (NF Latent Density) | 3.40 | Weaker paper: lacked novelty, had contradictory claims. Under-review paper has a clearer contribution and more solid experiments. |

Relative to these anchors, the paper sits below the HamOS (6.75) and Likelihood Peaks (5.67) papers due to the missing baseline comparisons, but above the 3.40 paper due to a clearer contribution. It is most comparable to the 4.25–5.50 band: a recognizable contribution with a non-trivial evaluation gap.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>