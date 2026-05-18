Now I have a thorough understanding of the paper and have verified the reviewer claims against the actual text. Let me produce the final consolidated review.

## Summary

MotionClone proposes a training-free framework for cloning motion from a reference video into generated videos. The key insight is that the dominant components (top-1 per spatial location) of temporal attention maps from a single denoising step serve as a sufficient and efficient motion representation. By computing an attention-map alignment loss and injecting its gradient during early sampling steps, MotionClone achieves motion transfer across T2V, I2V, and sketch-to-video without any fine-tuning or DDIM inversion.

## Strengths

- **Novel and well-motivated training-free approach.** The observation that sparse temporal attention weights (top-1 per spatial location) capture motion cues while discarding scene-specific noise is a genuine insight. The paper shows that "plain control" (aligning all attention weights) produces weak motion transfer, while the proposed "primary control" focusing on top-1 weights substantially improves motion fidelity (Fig. 2, Fig. 6). This contrasts with prior methods that require training or fine-tuning (VMC, MotionDirector), and the training-free nature is a clear advantage for practical adoption.

- **Single-step extraction eliminates costly inversion.** The paper demonstrates that motion representation extracted from a single denoising step at t_α=400 is nearly as effective as full DDIM inversion (Fig. 7, "Inversion_2" vs. "MotionClone"), while being far more efficient. This is a practical engineering contribution that directly supports the flexibility claim.

- **Versatility demonstrated across multiple generation paradigms.** MotionClone is evaluated on text-to-video (AnimateDiff), image-to-video, and sketch-to-video (SparseCtrl), showing the method generalizes beyond a single base model and supports multiple task settings (Fig. 7). The user study scores MotionClone highest on all four criteria (motion preservation 3.69 vs. next best 3.50, appearance diversity 4.31 vs. 3.51, textual alignment 4.15 vs. 3.79, temporal consistency 4.28 vs. 3.34), indicating real practical advantage.

- **Systematic ablation study for key hyperparameters.** The paper ablates k ∈ {1,2,4}, t_α ∈ {200,400,600,800}, attention block choice, precise prompt vs. null text, and DDIM inversion versus single-step extraction (Figs. 6-7, Section 4.5). This provides empirical support for the default choices and helps readers understand the method's sensitivity.

## Weaknesses

### Major

- **The core design choice (k=1 mask) is validated only qualitatively across the test set.** The ablation for k ∈ {1,2,4} is shown on a single video example (Fig. 6), and no quantitative metric (e.g., motion similarity score, optical-flow alignment, or even a user-study ablation over k) is reported across the full 40-video test set to establish that k=1 is systematically superior. Given that the entire method hinges on the claim that top-1 weights are sufficient and that larger k dilutes motion guidance, this is a structural gap. The user study does compare MotionClone (which uses k=1) against baselines, but does not compare MotionClone against a "k=4" or "plain control" variant under the same evaluation protocol, making it impossible to attribute the user-study advantage specifically to the sparsity choice versus other aspects of the framework. This is fixable with additional experiments but weakens the current evidence.

### Minor

- **Automatic metrics show only marginal gains over VMC, undercutting the "notable superiority" claim on objective grounds.** In Table 1, MotionClone's Textual Alignment (0.3187) and Temporal Consistency (0.9621) are extremely close to VMC's (0.3134 and 0.9614). No confidence intervals, standard deviations, or significance tests are reported. While the user study shows clearer advantages, the paper's abstract and conclusion claim "notable superiority in terms of motion fidelity, text alignment, and temporal consistency" without qualifying that the automatic metrics tell a more modest story. This overclaim is small but worth correcting.

- **Number of motion guidance steps is set empirically without ablation.** The paper uses 50/100 steps for camera motion and 180/300 for object motion (Section 4.1), citing prior work on spatial attention. However, no ablation varies this hyperparameter to study the trade-off between motion fidelity and appearance diversity. Given that this is a user-facing design choice, understanding its sensitivity would be valuable.

- **No analysis of whether the optimal t_α varies with motion speed or amplitude.** The paper ablates t_α ∈ {200, 400, 600, 800} on one example and reports that 200-600 all work while 800 degrades. However, it does not test whether fast motions (e.g., a running person) benefit from a different t_α than slow motions (e.g., a turning head). Since a user with a new reference video has no guidance on whether to adjust this parameter, the claimed "flexibility" is partly undermined.

- **The gradient computation for motion guidance is underspecified.** Equation 2 (Eq. 3 in the paper) defines the guidance update with a gradient term ∇_{z_t} g, but the paper does not clarify whether a full backward pass through the U-Net's temporal attention layers is performed per guidance step, or whether an approximation is used. This matters for both reproducibility and the efficiency claims, since backprop through temporal attention at high resolution can be expensive.

### Trivial

- The paper uses `up_block.1` (lines 93, 145, 225) — which is what the paper states — but the reviewer wrote `up_blocks.1`; the paper's naming is correct and consistent.

## Nice-to-Haves

- A per-video breakdown (e.g., scatter plots of motion preservation vs. textual alignment, colored by motion type) would help reveal whether MotionClone's advantages are concentrated in specific categories or are broadly applicable.
- An ablation of the number of motion guidance steps on 3-5 diverse videos with both a motion fidelity metric and an appearance diversity metric would make the hyperparameter choice empirically grounded.
- The paper could strengthen the comparison by including a variant of VMC that is applied in a training-free manner (if feasible), or by reporting an automatic motion similarity metric (e.g., cosine similarity between temporal attention maps of reference and generated videos) that isolates motion transfer from appearance.

## Removed Points

These points were raised by reviewers but removed or downgraded after verification against the paper:

- **"The comparison includes methods not designed for motion cloning"** — The paper explicitly acknowledges this limitation in the introduction (Section 1, line 16-17). Including these methods as additional baselines is standard practice and does not inflate the paper's claims beyond what is disclosed. The user study results stand on their own regardless.
- **"Precise prompt ablation is surprising and needs analysis"** — The paper already provides a reasonable speculation for why precise prompts don't matter (motion information is preserved in diffusion features at t_α=400). This is a minor curiosity, not a weakness.
- **"No inter-rater reliability for user study"** — While true, this is not standard practice for video generation papers at major venues; 20 raters with average scores is an accepted methodology.
- **"Missing appendix or proofs"** — Parser artifact; the original submission has these sections.

## Novel Insights

The reviewer's analysis surfaced an interesting tension that is not fully explored in the paper: the method uses a sparsity mask derived from the reference video's attention maps, but the same mask is reused across all sampling steps of the generated video. Since the generated video's own attention maps evolve during denoising, there is a potential misalignment between where the reference had strong correlations and where the generated video "needs" guidance at a given step. The paper's observation that single-step extraction works implies this misalignment is tolerable, but understanding the boundary conditions — when does the fixed mask become misleading? — would be a natural extension. The mention of failure cases for overlapping motion (Section 4.6) hints at this but does not connect to the fixed-mask issue specifically.

## Suggestions

1. Add a quantitative ablation of k (1, 2, 4, full) across the full 40-video test set using an automatic motion fidelity metric. Even a simple cosine similarity between the generated and reference temporal attention maps would dramatically strengthen the validation of the core design claim.
2. Qualify the "notable superiority" language when referring to automatic metrics (Textual Alignment and Temporal Consistency in Table 1), since the numerical differences from VMC are very small.
3. Add a brief discussion or ablation of the number of motion guidance steps, even if just for 3 representative videos, to show the sensitivity of this hyperparameter choice.
4. Clarify in the implementation details whether full backpropagation through U-Net temporal attention is performed at each guidance step, or whether a cheaper approximation is used.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>