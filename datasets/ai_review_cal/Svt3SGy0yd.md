- Decision: Reject
- Avg Score: 5.80
- Scores: 8, 5, 6, 5, 5
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes GEARnn, a method for growing compact neural networks robust to common corruptions entirely on an edge device (NVIDIA Jetson Xavier NX). The key idea is a two-phase approach: first grow the network using clean data via One-Shot Growth (OSG), then robustly train it using Efficient Robust Augmentation (ERA). This is contrasted with a one-phase approach (GEARnn-1) that jointly grows and robustly trains. Experiments across CIFAR-10/100 and Tiny ImageNet using MobileNet-V1, VGG-19, and ResNet-18 show that GEARnn-2 achieves 2–4× reductions in training time and energy compared to a robustly-trained fixed-size baseline at comparable robust accuracy. The paper also shows that single-shot growth is superior to multi-shot growth in this setting.

## Strengths

- **First demonstration of growing networks robust to common corruptions.** The paper is explicit that prior growth methods (Firefly, GradMax) only use clean data, and prior robust training methods (AugMix, PRIME) use fixed-size networks. The paper's combination of growth + robust training is novel in this space (stated in Section 1, supported throughout).

- **2-Phase (clean growth then robust training) consistently outperforms 1-Phase (joint growth+robust training).** Tables 1 and 2 show GEARnn-2 achieves higher robust accuracy and lower training time/energy than GEARnn-1 across all architectures, datasets, and hardware platforms. For example, on Jetson VGG-19 CIFAR-10: GEARnn-2 achieves 83.45% robust accuracy in 596 min vs GEARnn-1's 82.25% in 652 min (Table 2). This directly answers **Q1**.

- **One-Shot Growth (OSG) is superior to multi-shot growth.** Table 4 shows that 1-step growth achieves the best or tied-best clean/robust accuracy with the lowest training energy (155 kJ) compared to 2–4 growth steps for GEARnn-2 on Jetson, answering **Q2**.

- **Real edge-device validation demonstrates significant training efficiency gains.** Table 2 shows GEARnn-2 reduces training time by ~2.3× and energy by ~2.8× on average compared to the robust baseline Small(𝒟ₐᵤ₉) while maintaining robust accuracy within ~2 pp on the NVIDIA Jetson Xavier NX. This is the paper's most practically significant result.

- **Ablation cleanly decomposes contributions of OSG and ERA.** Table 6 isolates each component: OSG+ERA yields the best robust accuracy (54.31%) with lower cost than the vanilla+AugMix combination (53.74%, higher cost), confirming the synergy.

- **Evaluation spans multiple architectures, datasets, and hardware.** Results on MobileNet-V1, VGG-19, and ResNet-18 for CIFAR-10, CIFAR-100, and Tiny ImageNet on both Quadro (server GPU) and Jetson (edge device) show consistent trends, strengthening generality.

## Weaknesses

### Major

- **No variance estimates in main result tables.** All accuracy, time, and energy values in Tables 1, 2, and 4 appear to be from single runs. The paper states at line 598 that "fixed seeds" are used for reproducibility, but does not report standard deviations or confidence intervals. Given that the robustness gap between GEARnn-2 and the Small(𝒟ₐᵤ₉) baseline is often 1–3 pp (e.g., VGG-19 CIFAR-10 on Quadro: 83.77% vs 85.73%), it is not possible to assess whether this gap is statistically meaningful or just noise. The paper's central claim of "comparable" robustness rests on these comparisons. Running multiple seeds (at least for a representative subset of experiments) and reporting variance is needed.

### Minor

- **Robustness gap is systematically present but under-discussed.** The paper describes GEARnn-2 as having "comparable" robust accuracy to Small(𝒟ₐᵤ₉) (line 384). However, the gap is present in nearly every comparison: e.g., −2.28 pp for VGG-19 CIFAR-10 on Jetson, −2.63 pp for VGG-19 CIFAR-100 on Quadro, −2.05 pp for ResNet-18 CIFAR-10 on Quadro. The paper would be strengthened by explicitly quantifying and discussing this trade-off — 2–4× efficiency gain for a 1–3 pp robustness cost is still a favorable trade-off, but it should be stated rather than glossed over.

- **Initial backbone sizes for main experiments not specified.** The hyperparameter table (Table 5) gives growth ratios (γ) but not the absolute or relative size of the initial backbone f₀ for the main Quadro and Jetson experiments (Tables 1 and 2). The initial backbone size is only stated for the single growth-power comparison (1.4% for VGG-19 CIFAR-10, line 389). This hinders reproducibility.

- **Fourier spectrum analysis is qualitative and based on limited examples.** Section 7.2 and Figure 5 provide an intuitive explanation for why clean-data initialization aids robustness (common corruptions occupy low-frequency space, similar to clean images). However, this analysis relies on visual inspection of individual corrupted/augmented image spectrums rather than a quantitative metric (e.g., mean frequency energy across the full dataset). The claim would be stronger with dataset-level statistics.

### Trivial

- **Energy measurement polling frequency not reported.** Line 205 states that energy is computed by "summing the mean power values polled" from Nvidia-SMI and Jetson Stats, but does not specify the polling interval. If the interval is coarse (e.g., 1 Hz), energy estimates on short training runs could be approximate.

## Nice-to-Haves

- Separating the effects of ERA and OSG in the main comparison tables (e.g., an additional row in Table 1 showing GEARnn-2 with full AugMix instead of ERA) would help isolate whether the small robustness gap is due to the growth process or the modified augmentation.
- A brief experiment demonstrating that the two-phase advantage holds under a different growth algorithm (e.g., GradMax) would increase confidence in the generality of the approach. The paper notes this flexibility (line 73) but does not test it.
- Showing absolute model sizes alongside the "Size (%)" column in Table 1 would improve readability.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"VGG-19 motivation stacks the deck"** (Harsh Critic, Section-by-Section Notes): The critic argues that using a 20M-param VGG-19 to motivate the problem is unfair since the paper's own baselines are much smaller. This misunderstands the motivation: the 2-day figure illustrates why training full-size models on edge is impractical, motivating the need for compact robust networks. The actual method targets small models, not full-size VGG-19s.
- **"ERA parameter choice missing justification"** (Harsh Critic): The critic notes that the (W,D,J) = (1,3,4) choice references Appendix A (stripped by parser). Per the review guidelines, missing appendix content is a parser artifact. The justification exists in the original submission.
- **"Baseline Small(𝒟ₐᵤ₉) epoch sensitivity"** (Harsh Critic): The critic asks whether 160 epochs is optimal and whether GEARnn could benefit from fewer. This is a generic criticism that could apply to any comparison. The baseline uses more epochs (160) than GEARnn-2 (121 for CIFAR-10), so any effect likely favors the baseline.
- **"Equation (1) constraint ambiguity"** (Harsh Critic): The critic wants 𝒞 defined more explicitly in the equation, but it is defined clearly in the text directly below (line 107): "𝒞(f) = Σ w_l represents the complexity estimate of network f." This is a presentational nitpick that does not impede understanding.
- **"Generalizability to other growth methods"** (Harsh Critic): Requesting a full experiment with an alternative growth method is a nice extension but not a requirement for the paper's current claims. The paper acknowledges this as future work.

## Novel Insights

None beyond the paper's own contributions. The two-phase insight (clean growth followed by robust training) and the finding that single-shot growth is sufficient in this setting are the paper's key novel observations. The Fourier spectrum intuition connects clean-data initialization to common-corruption robustness in a way that is plausible and interesting, though not rigorously proven.

## Suggestions

1. **Add variance estimates.** Run at least 3 seeds for a representative subset (e.g., VGG-19 CIFAR-10 and CIFAR-100 on both Quadro and Jetson) and report mean ± std in the main tables. This is the single highest-impact improvement.
2. **Explicitly discuss the robustness–efficiency trade-off.** In the abstract, conclusion, and results sections, quantify the typical gap (e.g., "GEARnn-2 achieves 2–4× training efficiency at a cost of 1–3 pp lower robust accuracy") rather than only using "comparable."
3. **Report initial backbone sizes** for all main experiments, not just the growth-power comparison.
4. **Clarify the energy polling frequency** in the experimental setup section.
5. **Consider adding a quantitative summary** of the Fourier analysis (e.g., the fraction of energy in low-frequency bands averaged over the full dataset) to strengthen the discussion in Section 7.2.
