- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now let me construct the final consolidated review.

## Final Review

## Summary
Ctrl-U proposes uncertainty-aware reward modeling for conditional image generation. The method runs two forward passes with different noise timesteps, measures the prediction variance of a pre-trained reward model as an uncertainty indicator, and uses it to adaptively reweight the consistency loss during fine-tuning. Experiments on segmentation masks, edge, and depth conditions across ADE20K, COCO-Stuff, and MultiGen-20M show consistent improvements over ControlNet++ and other baselines in both controllability (mIoU, SSIM, RMSE) and generation quality (FID), supported by a human evaluation study.

## Strengths
1. **No-parameter uncertainty estimation.** The method estimates uncertainty via two forward passes with different timesteps (KL-divergence or ℓ₁ distance between reward model outputs, Eq. 1 and Sec. 3.1 Discussion 1). This avoids auxiliary regression networks that tend to overfit, and introduces no additional training parameters — a concrete design advantage over prior uncertainty approaches.

2. **Adaptive uncertainty regularization with principled design.** The loss in Eq. 4 (`ℒ^u = ℒ^c / exp(U) + λ·U`) dynamically down-weights unreliable reward feedback and penalizes unbounded uncertainty. Ablations (Tables a–d, Sec. 4.3) systematically validate each component and identify optimal settings, supporting the core claim that rectifying inaccurate rewards improves training.

3. **Consistent gains across diverse conditions and datasets.** Table 1 shows Ctrl‑U outperforms ControlNet++ on all five benchmarks: ADE20K (+6.53% mIoU), COCO-Stuff (+44.42% mIoU), Hed (+3.76% SSIM), Lineart (+1.06% SSIM), and depth (−8.7% RMSE, lower is better). All comparisons use the same base model (SD1.5) and same hyperparameter settings, isolating the effect of the uncertainty module.

4. **Simultaneous improvement in generation quality.** Table 2 reports uniformly better FID scores across all benchmarks (e.g., 15.79 vs. 19.29 on COCO-Stuff, 11.59 vs. 15.01 on Hed). This demonstrates that the method does not sacrifice image quality for controllability.

5. **Human evaluation confirms practical preference.** In a pairwise ranking study with 20 participants (Table 5), Ctrl‑U is preferred over ControlNet++ and other methods on all three criteria: image-condition alignment (72.5%), image quality (56.2%), and text alignment (50%).

6. **Thorough ablation studies.** Sec. 4.3 systematically investigates timestep difference |t₁−t₂|, timestep threshold t_thre, regularization weight λ, and consistency weight μ₀, providing clear rationale for each design choice.

## Weaknesses

### Fatal
None.

### Major
- **The 44.42% relative mIoU gain on COCO-Stuff (49.91 vs. 34.56) is an extreme outlier compared to the other benchmarks (+1.1% to +6.5%) and is not adequately explained.** The paper attributes it to "reducing the adverse effects of imprecise feedback" but offers no per-dataset analysis of why COCO-Stuff benefits so dramatically more than ADE20K (both are segmentation tasks with similar formulations). Possible explanations (e.g., COCO-Stuff has more categories with higher uncertainty, the baseline ControlNet++ reward model happens to be particularly weak on this dataset, or evaluation pipelines differ) are not explored. Without error bars, confidence intervals, or an analysis of per-image mIoU gains, it is hard to rule out that this result is driven by a small subset of images or an evaluation discrepancy. **This does not invalidate the paper's contribution** — the other four benchmarks show solid improvements — but the paper should provide (i) error bars or confidence intervals for all metrics, especially COCO-Stuff, (ii) a discussion of why the gain is so large on this specific dataset, and (iii) confirmation that the ControlNet++ baseline was re-run in exactly the same pipeline for COCO-Stuff (the CLIP-score table shows the authors re-implemented ControlNet++ CLIP scores, so the same re-implementation should be confirmed for the controllability metric).

### Minor
- **Training cost is not reported despite the method using two forward passes per training step.** The paper mentions "one-step efficient reward strategy" (which reduces cost per forward pass) and "8 A100 (80G) GPUs," but does not report GPU-hours, training time, or a direct efficiency comparison to ControlNet++. Since the method doubles the number of reward-model forward passes relative to the baseline, this overhead should be transparently acknowledged and quantified.

- **No standard deviations or confidence intervals reported.** The paper averages results over four groups of PNG generations but provides no variance estimates. For the COCO-Stuff result in particular, this is a significant omission. Given that all tables report only point estimates, the reliability of individual numbers (especially outliers) is hard to assess.

- **The exact sampling strategy for t₁ and t₂ is not specified in the main method.** The ablation (Sec. 4.3) tests various |t₁−t₂| values and finds |t₁−t₂|=1 optimal on ADE20K, but the main method description (Sec. 3.1) only says "different t₁ and t₂" without stating the interval used for the main results. The paper also does not clarify whether t₁ and t₂ are sampled randomly within a fixed interval or set deterministically.

- **The uncertainty estimation partially conflates image quality differences with reward model uncertainty.** Using different timesteps produces reconstructions of different quality (noisier t → blurrier image), so the reward model's prediction variance reflects both genuine cognitive uncertainty and lower-frequency signals from blurrier inputs. The paper acknowledges this (Discussion 2) and the |t₁−t₂|=0 ablation partially addresses it, but the framing as "uncertainty of the reward model" overstates what is being measured. A more precise description (e.g., "disagreement-weighted reward" or "variance-adaptive loss") would be more accurate.

- **Ablation hyperparameters (λ, μ₀, |t₁−t₂|, t_thre) are only tuned on ADE20K segmentation.** It is unclear whether the same settings are optimal for edge, depth, or COCO-Stuff conditions, which have different reward model characteristics.

### Trivial
- **Figure 1 motivation uses only a single image.** A quantitative summary across the full validation set would strengthen the motivation.
- **The CLIP-score table keeps the original ControlNet++ value of 13.13 (erroneous) alongside the corrected 30.93 in gray.** While the caption explains this, the formatting is confusing and could be simplified (e.g., replace the original value with a footnote).

## Nice-to-Haves
- The paper dismisses auxiliary uncertainty regression networks in a discussion paragraph but does not provide even a small-scale empirical comparison. A brief experiment on ADE20K comparing variance-based uncertainty vs. a learned head would directly justify this design choice.
- A per-image breakdown of mIoU gains on COCO-Stuff (e.g., a histogram) would help validate whether the large average gain is distributed across the dataset or driven by a few categories.
- An additional experiment varying the reward model architecture (e.g., different segmentation networks) would strengthen the claim that the method reduces inaccurate feedback rather than just fitting the specific reward model used.

## Removed Points
- *Speculation about whether the ControlNet++ baseline was properly tuned for COCO-Stuff or used a different validation set.* The paper explicitly states it "adheres to ControlNet++'s dataset construction principles" and uses the same hyperparameter settings. No evidence suggests a mismatch.
- *Claim that the CLIP-score table's dual values (13.13 / 30.93) "undermine trust."* The caption transparently explains both values: 13.13 is the originally reported number, and 30.93 (in gray) is the authors' re-implementation. This is a standard practice when correcting a baseline's reported metric and does not indicate an evaluation problem.
- *Criticism about missing supplementary material / appendix.* The parser strips these sections from all papers; they exist in the original submission.
- *Request for the paper to name reward models in the main text (rather than supplementary).* The paper says "see supplementary material," which is standard for implementation details.
- *Criticism about scalability to conditions without an off-the-shelf reward model.* This is outside the paper's stated scope; the method is designed for settings where a reward model exists, which is clearly scoped.

## Novel Insights
None beyond the paper's own contributions. The reviews did not surface any insight about the method that is not already articulated in the paper.

## Suggestions
1. **Provide error bars** (standard deviation or confidence intervals) for all main results, derived from the four independent generation runs already performed.
2. **Analyze the COCO-Stuff result** more deeply: show per-category mIoU, compare to ADE20K to explain the 44% vs. 6.5% gap, and confirm the ControlNet++ controllability numbers on COCO-Stuff were obtained with the same re-implemented pipeline used for the CLIP-score correction.
3. **Report training cost:** GPU-hours or wall-clock time for the 10k reward fine-tuning iterations, and compare to the same for ControlNet++.
4. **State the |t₁−t₂| value used for main experiments** explicitly in Sec. 3.1 (not just in the ablation).
5. **Discuss the conflation** between image quality and uncertainty more precisely, and consider reframing the method as "disagreement-weighted reward fine-tuning" rather than "uncertainty-aware reward modeling."

---
