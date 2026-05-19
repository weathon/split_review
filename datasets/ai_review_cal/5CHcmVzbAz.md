- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Now I have a thorough understanding of the paper. Let me compose the consolidated review.

## Summary

The paper proposes SePPO (Semi-Policy Preference Optimization), a method for aligning diffusion models with human preferences that avoids both explicit reward models and paired human-annotated data. SePPO uses previous model checkpoints as reference models to generate "reference samples" that replace losing images in preference pairs, and introduces an Anchor-based Adaptive Flipper (AAF) that decides on-the-fly whether to treat a reference sample as winning or losing. The method is evaluated on text-to-image (Pick-a-Pic, HPSv2, Parti-prompt) and text-to-video (ChronoMagic-Bench) benchmarks.

## Strengths

1. **Anchor-based Adaptive Flipper (AAF) is empirically shown to prevent performance degradation from uncertain reference-sample quality.** The ablation study (Table 5) confirms this clearly: removing AAF drops PickScore from 21.57 to 20.88 on the Pick-a-Pic validation set, and HPSv2 drops from 27.20 to 26.78. This demonstrates that simply treating all reference samples as negatives (as done in SPIN-Diffusion and DITTO) is suboptimal, and the adaptive sign mechanism is a genuine improvement.

2. **Random reference-model sampling strategy demonstrably improves training stability over fixed strategies.** Section 4.1 systematically compares three strategies (ref=0, ref=k-1, ref=[0,k-1]) and shows via ablation (Figure 2) that random sampling from all previous checkpoints avoids the overfitting observed with a fixed initial reference and the instability of only using the latest checkpoint. Table 5 confirms this: ref=[0,k-1] outperforms both ref=0 (21.41) and ref=k-1 (21.34).

3. **Competitive text-to-image results on multiple benchmarks without reward models or paired human-annotated data.** On the Pick-a-Pic validation set (Table 1), SePPO^w achieves the best PickScore (21.57), HPSv2 (27.20), and ImageReward (0.615) among all compared methods. Critically, SePPO also outperforms prior methods on out-of-distribution datasets (HPSv2 and Parti-prompt, Table 2), indicating that gains are not simply due to overfitting the training distribution.

4. **Ablation study convincingly disentangles the contributions of each component.** Table 5 isolates the effect of AAF and each reference-sampling strategy separately, providing clear evidence that both the AAF and the random reference selection contribute meaningfully to the final performance.

## Weaknesses

### Fatal

None.

### Major

1. **The AAF mechanism when sign=-1 lacks principled theoretical grounding, and the paper does not characterize what the modified loss actually optimizes.** When `sign=-1`, the loss in Equation (14) becomes a sum of two positive terms—both the winning image and the reference sample are pushed toward lower prediction error relative to the reference model. This is neither a pairwise preference loss nor derived from a consistent grounding (e.g., the Bradley-Terry model). The justification hinges on Theorem 1, which is essentially a restatement of "if model A has lower expected loss than model B, then model A is better" — it does not formally connect the sign of a single-sample comparison on *one* image (the winning anchor) to the quality of a different generated sample (x^ref). The paper's gradient analysis (Equation 13) is performed only for the non-AAF loss, not for the AAF-modified version. While the ablation study provides strong *empirical* evidence that AAF works, the paper's claim to have "designed a criterion" in a principled sense is overstated. The AAF is best understood as a well-motivated heuristic that happens to work well in practice.

2. **The claim that SePPO "surpasses all previous approaches" is not adequately supported by the evidence, due to missing statistical significance and very small margins on primary metrics.** On the Pick-a-Pic validation set (Table 1), SePPO^w achieves PickScore 21.57 vs. SPIN-Diffusion^* 21.55 — a marginal difference of 0.02. HPSv2 is 27.20 vs. 27.10. No confidence intervals, error bars, or statistical significance tests are reported for any metric. Without uncertainty quantification, a reader cannot assess whether these differences are likely to replicate. The paper's abstract and conclusion ("surpasses all previous approaches," "exceeds all previous optimization methods") overstate the strength of the evidence. The method's advantage on ImageReward (0.615 vs. 0.484) is more substantial, but the overall presentation should be honest about the uncertainty on the primary alignment metrics.

3. **The text-to-video evaluation is too limited to support claims of generalizability.** SePPO is compared only against vanilla AnimateDiff and SFT (Table 4). No other preference optimization methods (DDPO, SPIN-Diffusion, or any video-specific RLHF approach) are included as baselines. The dataset is restricted to time-lapse videos, and the metrics are standard image/video quality measures rather than human-alignment scores. The abstract claims SePPO "demonstrates outstanding performance on text-to-video benchmarks," but the evidence presented does not support competitive performance relative to existing preference optimization approaches — it only shows improvement over the base model and SFT. This section should either be expanded with meaningful baselines or presented as a preliminary demonstration.

### Minor

1. **The connection between the sign criterion (evaluated on a single noise-perturbed winning sample) and the quality of a separately generated reference sample is asserted without analysis.** The sign is computed using ε_ref(x_t^w) vs. ε_θ(x_t^w) — i.e., the relative loss on the winning image under a specific noise draw. The paper assumes this reliably indicates whether a *different* generated image (x^ref) from the reference distribution is winning or losing. No analysis of the correlation between these two quantities is provided. The ablation validates this empirically, but the assumption should be acknowledged and discussed.

2. **The exploration argument for random reference selection (Figure 1) is intuitive but not formally justified.** The paper argues that random sampling from all checkpoints "expands the space of policy exploration" (Section 4.1). While the ablation results support the empirical benefit, this claim remains heuristic without a formal analysis of how the exploration area changes with different reference-selection strategies.

3. **The limitations section is too brief.** It mentions only two very general limitations (open problem of theoretical analysis in diffusion models, pixel-space considerations) and does not discuss the theoretical gap in the AAF loss, the lack of statistical significance, or the limitations of the video evaluation.

### Trivial

None.

## Nice-to-Haves

- Reporting confidence intervals or bootstrapped significance tests for the main text-to-image comparisons (Table 1) would substantially strengthen the paper's empirical claims.
- A brief hyperparameter sensitivity analysis (β, learning rate) would help establish the method's robustness.
- A discussion of the computational overhead of storing multiple checkpoints and generating reference samples from them would be helpful for practitioners.

## Removed Points

- **Criticism about "reproduced checkpoints may not be optimally configured for fair comparison":** This is speculative — the paper uses publicly available checkpoints from HuggingFace, and no evidence is presented that they are misconfigured.
- **Criticism about missing reproducibility details (e.g., exact reference model selection procedure):** The paper specifies `ref ∼ U(0, k-1)` in Algorithm 1 — uniform random sampling from previous checkpoints. This is adequately documented.
- **Criticism about "SPIN-Diffusion's iter3 checkpoint is the result of multiple iterations":** This point is about differences between SePPO and SPIN-Diffusion that the paper already acknowledges — SPIN-Diffusion uses the latest checkpoint, SePPO uses random selection from all checkpoints. The paper clearly distinguishes itself.
- **Some generic strengths from the Strength Finder that are about "addressing an important problem" — these are generic and not specific to this paper's contribution.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Provide gradient analysis or fixed-point characterization of the AAF-modified loss when sign=-1.** Even a heuristic characterization would help the reader understand what the alternative mode of the loss does. Alternatively, explicitly acknowledge the AAF as an empirically-motivated heuristic.
2. **Temper the comparative claims** — replace "surpasses all previous approaches" with more measured language that acknowledges the small margins on some metrics and the lack of statistical significance testing.
3. **Expand the video evaluation** by including at least one other preference optimization baseline (e.g., SPIN-Diffusion adapted to video, or a reward-based method), or clearly label the video results as a preliminary demonstration of applicability rather than competitive performance.
