- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 5, 5, 8
## Summary

This paper investigates pre-trained attention patterns for infrared semantic segmentation. It first benchmarks six pre-training methods on three infrared datasets, revealing that ImageNet fine-tuning performance poorly correlates with infrared transfer. Through layerwise analysis of attention maps, it identifies three attention pattern types (local, hybrid, global) and argues that hybrid patterns — which attend to both nearby and foreground tokens — are critical for dense prediction. Building on these insights, the paper proposes UNIP, a framework combining (1) NMI-guided hybrid-attention distillation (NMI-HAD) from a larger teacher, (2) a mixed RGB+infrared dataset (InfMix), and (3) a last-layer feature pyramid network (LL-FPN). UNIP achieves large improvements over same-size baselines (up to +13.6 mIoU for ViT-T) and reaches performance comparable to MAE-L at 1/10 the computational cost.

## Strengths

- **Introduction of NMI as a quantitative metric for attention patterns.** The paper defines normalized mutual information of the attention matrix to distinguish local, hybrid, and global patterns numerically (Section 3.2, Fig. 4). This provides a measurable, principled way to identify where hybrid patterns reside, going beyond qualitative visualization.

- **Large and consistent performance gains across model sizes.** Table 4 reports that UNIP-T, UNIP-S, and UNIP-B improve average mIoU over MAE baselines by 13.57%, 8.98%, and 4.34% respectively, with UNIP-S matching MAE-L at 1/10 the FLOPs. These gains are consistent across three teacher models (MAE-L, iBOT-L, DINO-B).

- **NMI-HAD outperforms feature distillation (controlled comparison).** Table 6 directly compares attention distillation (NMI-HAD) against feature distillation using the same teacher and student, across multiple layers. Attention distillation consistently wins by several mIoU points, providing evidence that the choice of what to distill matters beyond the data or framework.

- **Benchmark reveals domain-specific findings.** Table 1 reports Pearson coefficients showing near-perfect correlation between infrared LP and FT (ρ ≈ 1.0) but no consistent correlation between ImageNet FT and infrared FT. This is a useful empirical finding that justifies domain-specific benchmarking rather than relying on RGB-centric metrics.

- **InfMix dataset ablations demonstrate necessity of all components.** Table 9 systematically ablates each component of InfMix (InfPre, ImageNet subset, COCO, grayscale), showing performance drops when any component is removed. This validates the dataset design as more than just "more data."

- **LLP evidence extends hybrid-pattern hypothesis to RGB and depth.** Table 10 shows that for DINO-S and DeiT-S on ADE20K, NYUv2, and SUN RGB-D, middle-layer (hybrid) features outperform deep-layer (global) features in linear probing, mirroring the infrared pattern and suggesting broader relevance.

## Weaknesses

### Fatal

None.

### Major

- **The effect of the distillation method and the effect of additional/different training data are not fully disentangled.** UNIP trains on InfMix — a dataset larger and more diverse (multi-modal, grayscale-converted) than the teacher's own pre-training data (ImageNet-1K). The only control experiment (Tab. 8) compares MAE-S continually pre-trained on InfMix vs. UNIP-S, showing UNIP wins by 5.84%. While this is informative, it covers only one student size (ViT-S) and one teacher (MAE-L). For other configurations (e.g., iBOT-L teacher, ViT-B student), no analogous control is run, so the relative contribution of the distillation method vs. the data itself remains incompletely characterized. The paper's central framing ("distilled models even outperform their teacher models") conflates these two effects.

- **No ablation comparing the NMI-guided layer selection against simpler baselines.** The NMI-HAD method selects the distillation target layer by minimizing |NMI(A_l) – s| with s=0.09. Fig. 7 shows stability across s values (0.06–0.12), and Fig. 6 shows correlation between ΔNMI and FT performance. However, no experiment compares the chosen layer against: (a) a fixed baseline layer (e.g., the last layer), (b) a random layer, (c) an adjacent layer with NMI farther from s. Without these, we cannot determine whether the NMI rule is meaningfully better than picking any middle-to-deep layer. The claimed advantage of NMI-HAD over "picking any reasonable layer" is asserted but not demonstrated.

- **No reported variance across runs.** All experiments appear to be single runs, with no standard deviations or confidence intervals reported for any result table. Given that the claimed gains are large (up to 13.5%), readers cannot assess whether these results are stable or potentially influenced by random seed. Multiple seeds are standard for establishing reproducibility even in large-scale vision experiments.

### Minor

- **The list of the 23 infrared datasets used to construct InfPre is not provided.** The paper states that the three evaluation datasets are excluded from InfPre, which is a necessary step. However, without listing the source datasets, and without any near-duplicate analysis (e.g., feature matching) between InfPre and the evaluation splits, the possibility of unseen image overlap across different infrared benchmarks cannot be assessed from the paper alone. This is a transparency issue that could affect the credibility of the reported gains.

- **Texture bias evidence is limited to one model comparison.** Table 2 supports the texture-bias claim with a single comparison (MAE-B vs. DeiT-B and DINO-B on three datasets). While the MFNet-RGB vs. MFNet-T paired comparison is the cleanest controlled setup, only two model families are compared. Including more models or using texture-shifted datasets would strengthen this claim.

- **LL-FPN architecture details are underspecified.** The paper describes LL-FPN as constructing multi-scale features "upon the last layer's features" (Section 4.1) and references ViTDet, but does not specify the number of deconvolution layers, how feature map scales are generated, or how the baseline multi-layer FPN (Fig. 8a) selects which layers to use. This hurts reproducibility and makes the ablation (Tab. 7) harder to interpret independently.

- **Tab. 5 comparisons use different training epochs.** The paper notes that Tab. 5 comparisons (Mask2Former, TINN) use 200/300 epochs for SODA and MFNet-T, while the paper's own default is 100 epochs throughout. The transparent disclosure is appreciated, but this mixing of regimens means the numerical values in Tab. 4 and Tab. 5 are not directly comparable, and the claimed margin over SOTA could partly reflect added training budget.

- **Grayscale conversion mechanism is empirically validated but not explained.** The ablation (Tab. 9) shows that removing grayscale hurts performance, confirming its role. However, the paper's rationale ("to resemble infrared images more closely") is imprecise: infrared images are physically distinct from grayscale RGB (thermal radiation vs. luminance). The paper speculates about "balance between modalities" without analysis of what the grayscale transformation actually accomplishes.

### Trivial

- The abstract mentions "limited training data" as motivation, but no experiments test low-data regimes — all evaluations use full benchmark datasets. This is a framing minor issue.

- Pearson coefficients in Tab. 1 are computed over only 6 data points (6 pre-training methods); with such a small sample, a single outlier can drive the coefficient. Reporting p-values or confidence intervals would help.

## Nice-to-Haves

- Running the NMI-HAD vs. continual-pre-training comparison (Tab. 8) for at least one additional configuration (e.g., iBOT-L teacher → ViT-B student) would substantially strengthen the claim that distillation adds value beyond the data.
- Reporting main results (Tab. 4) as mean ± std over 3 seeds would improve credibility.
- Providing the list of 23 InfPre source datasets in the supplement would address the transparency concern.

## Removed Points

- **Data leakage as a "structural/fatal" issue (Harsh Critic #1):** The paper explicitly states that the three evaluation segmentation datasets are excluded from InfPre. The critic's concern about near-duplicate images across different infrared benchmarks is speculative ("if even a small fraction… could be dramatically inflated") and is raised without evidence that such overlap actually exists. Kept as a minor transparency concern (list not provided), but the fatal framing is removed.
- **"Missing appendix" and "missing proofs in appendix":** Removed per instructions. The parser strips appendix content from all papers; these criticisms reflect parser limitations, not author omissions.
- **Tab. 5 "mixes regimens" criticism:** The paper transparently states the epochs used (200/300) for comparisons with published methods. This is standard practice; the table is clearly labeled. Not a weakness.
- **"No small-training-set regime tested" criticism of abstract framing:** This is a generic observation about scope; the paper never claims to test low-data regimes.
- **NMI not overlaid on LLP curves:** This is a suggestion, not a weakness.
- **Generic "could the metric be measuring a proxy?" speculation:** Removed as speculative, not anchored to a specific error in the paper.
- **Strength Finder items about "the problem is important" or generic value judgments:** Removed as superficial. Only concrete, evidenced strengths are retained.
- **Unfair comparison claims where asymmetry favors baselines:** None present in the reviews.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a limitation or observation about the paper that the authors themselves have not already noted or implicitly addressed.

## Suggestions

1. **Run the "distillation vs. same-data continued pre-training" control for at least one additional teacher/student pair** (e.g., iBOT-L → ViT-B, or DINO-B → ViT-S). This is the single most important experiment to clarify whether NMI-HAD adds value beyond the InfMix data.

2. **Validate the NMI selection rule by comparing** the chosen layer (closest to s=0.09) against a fixed baseline (e.g., the last layer), a layer with NMI far from s, and a randomly selected layer — for the same teacher and data. This would directly test whether the NMI heuristic outperforms simpler alternatives.

3. **Report main results as mean ± std over 3 random seeds** (at least for the headline numbers in Tab. 4). This is standard practice for establishing reproducibility.

4. **Provide the list of 23 datasets used to construct InfPre** (in the supplement or a footnote), and ideally perform a near-duplicate check between InfPre and the three evaluation sets to quantify any potential overlap.

5. **Expand the texture-bias analysis** (Tab. 2) to include at least one more model pair (e.g., MAE-S vs. DINO-S) or use a texture-shifted benchmark.

6. **Specify the LL-FPN architecture** (number of deconv layers, how scale levels are chosen, which layers are used in the multi-layer FPN baseline) to aid reproducibility.
