- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5
Now I have a thorough understanding of the paper and the reviews. Let me produce the final consolidated review.

---

## Summary

InstantIR proposes a diffusion-based blind image restoration (BIR) method that generates on-the-fly "previews" (instant generative references) during the reverse diffusion process. The core idea is to encode the LQ image into a compact representation (via DINO), decode it through a consistency-distilled one-step Previewer at each diffusion step, and fuse the preview with the original LQ input via an Aggregator to guide SDXL generation. An adaptive sampling algorithm (AdaRes) uses the relative distance between the preview and the denoising prediction as a quality indicator to modulate conditional signals.

## Strengths

1. **Novel previewing mechanism for dynamic condition alignment.** The paper introduces a genuinely novel architecture where a distilled Previewer generates a restoration preview at each diffusion step by decoding the DCP embedding, enabling the model to actively re-align the generation condition with the generative prior during inference. This differs from prior methods that use a fixed codebook (CoSeR) or static LQ encoding (StableSR, SUPIR). The use of consistency distillation to make the previewer a one-step generator (Eq. 4) is a practical innovation for efficiency.

2. **State-of-the-art perceptual quality on non-reference metrics.** In Table 1, InstantIR achieves the highest MANIQA and MUSIQ scores across all four test settings (e.g., MANIQA 0.4379 vs. 0.4152 for second-best CoSeR on synthetic 512²; MUSIQ 68.59 vs. 67.51), with margins up to 22% on MANIQA and 8% on MUSIQ. These results demonstrate that the dynamic previewing mechanism produces outputs that are visually preferred by these learned perceptual metrics.

3. **Interesting observation that preview variance correlates with input quality.** The paper discovers and visualizes (Figure 3) that the relative L2 distance between the preview and the ordinary denoising prediction reliably indicates input degradation level. This is an empirically grounded insight that could be useful beyond this specific method.

## Weaknesses

### Fatal
None.

### Major

1. **Severe PSNR/SSIM deficits that are acknowledged but not adequately addressed.** InstantIR achieves the lowest PSNR and SSIM among all compared methods across all test settings. On real-world data at 512² resolution, PSNR is 21.75 vs. 25.59 (next-worst CoSeR) and 26.38 (BSRGAN). The paper dismisses this as "misalignment with visual quality" (line 225) and notes future work should address "excessive generative prior diminishes fidelity" (line 323), but does not provide any human evaluation or calibrated perceptual study to support the claim that the visual quality compensates for the fidelity loss. For a *restoration* method — where faithfulness to the original content is the primary goal — this gap is significant. The paper relies exclusively on non-reference metrics (MANIQA, MUSIQ) that favor sharp, generative outputs regardless of faithfulness, while the one full-reference perceptual metric reported (LPIPS) does not favor InstantIR.

2. **Ablation tables are confusingly labeled and the relationship between them is unexplained.** The paper's two ablation tables (Tables 4a and 4b) have ambiguous naming conventions. Table 4a reports a "Baseline" row (LPIPS 0.3173, MANIQA 0.4024) and a "+Distillation" row (LPIPS 0.4306, MANIQA 0.2145), while Table 4b shows adding references *improves* LPIPS from 0.3672 to 0.3173 and MANIQA from 0.2128 to 0.3747. The paper never explains what "Baseline" in Table 4a refers to, nor does it reconcile why Tables 4a and 4b appear to tell conflicting stories about the value of the previewer. The text cross-references "ablation2" when discussing consistency distillation (line 313), which is likely a labeling error, further contributing to confusion.

3. **The adaptive algorithm (AdaRes) is underspecified.** Algorithm 1 passes the quality indicator `δ` to the noise-prediction network `ε_θ`, but the paper never specifies **how** `δ` modulates the network. The mechanism is described only conceptually ("conditional signals from the Aggregator should be amplified," line 110). There is no equation showing how `δ` scales the SFT parameters (α^l, β^l), the cross-attention weights `w^l`, or the residual connection strengths. Without this, the algorithm is not reproducible.

4. **AdaRes provides negligible empirical benefit.** From Table 4b, adding AdaRes to the version with references changes MANIQA from 0.3747 to 0.3766 (+0.0019) and MUSIQ from 64.86 to 64.94 (+0.08). These differences are within noise level for these metrics. The paper's claim that AdaRes makes the model "adaptive to input quality" is not supported by any evidence that `δ` correlates with degradation level across a large test set (only four trajectories are shown qualitatively in Figure 3), and the threshold `η` in Algorithm 1 appears arbitrary.

### Minor

1. **Creative restoration capability is presented without evaluation.** The paper lists "controllable restoration to text prompts" as a contribution (item 3), and describes a mechanism involving a text-guided Previewer and disabling the Aggregator at later stages. However, this capability receives no quantitative evaluation — no CLIP score, no user study, not even a systematic set of examples beyond two figures. Implementation details (how the previewer is conditioned on text, what "disabling" the Aggregator means technically) are omitted, making this a non-contribution in its current form.

2. **No failure analysis or limitations discussion.** The paper presents only cherry-picked qualitative successes (Figure 4). Given the method's large PSNR/SSIM deficit, a discussion of failure cases — where visual quality comes at the cost of factual inaccuracy — is essential but absent. The conclusion briefly mentions the fidelity issue as future work, but does not provide a limitations section.

### Trivial

- Table 4a's "Baseline" and "+Distillation" row labels should be clarified or renamed to indicate what is being ablated.
- The text at line 313 references "Tab.~ablation2" but appears to describe an ablation shown in Table 4a (ablation1).

## Nice-to-Haves

- A perceptual user study (e.g., human preference judgments against ground truth) would substantially strengthen the claim that the low PSNR/SSIM reflects a genuine improvement in perceptual quality rather than uncontrolled hallucination.
- Reporting confidence intervals or variance across multiple runs would help assess the method's stability and the significance of small metric differences.
- A correlation analysis between `δ` and actual degradation parameters across a large set of test images would validate the adaptive algorithm's claimed behavior.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The previewer could equally introduce new errors from the generative prior"** — This is speculative and does not identify a specific flaw in the paper. Removed.
- **"No statistical significance (confidence intervals)"** — Single-run evaluation is standard practice in large-scale BIR benchmarks. Removed per community standards.
- **"The analysis in Figure 3 is based on only four degradation levels"** — Four levels are sufficient to demonstrate a monotonic trend; this is not a weakness. Removed.
- **"The paper does not discuss how resolution adjustments affect metrics"** — The paper does describe the adjustments (lines 221-222) and the tradeoffs are well-understood in the field. Removed.
- **Strength: "Controllable restoration with text prompts"** — Unevaluated and underspecified; conflicts with verified weakness #1 in Minor. Removed.
- **Strength: "Ablation studies cleanly isolate each component's contribution"** — Conflicts with verified Major weakness #2 about confusing ablation presentation. Removed.
- **"Previewer is trained on synthetic data; generalization unknown"** — Training on synthetic degradations with real-data fine-tuning is standard BIR practice; not a specific weakness. Removed.

## Novel Insights

Beyond the paper's own contributions, the key structural finding from the review process is that the paper exhibits an **evidence gap between its novelty claim and its empirical support**. The core idea (on-the-fly generative previews) is genuinely novel, but the evidence for it is undermined by (a) ablations whose naming conventions obscure rather than clarify the contribution of each component, and (b) an adaptive mechanism whose quantitative benefit is too small to distinguish from noise. The paper would benefit from either demonstrating a larger effect from AdaRes or de-emphasizing the adaptivity claim and focusing on the previewing mechanism itself. The tension between the paper's "restoration" framing and the severe PSNR/SSIM deficits also highlights an unresolved question for the field: how should the community weigh perceptual quality against fidelity in methods that claim to do restoration rather than enhancement?

## Suggestions

1. **Clarify the ablations.** Rename rows in Table 4a to explicitly state what each configuration is (e.g., "DDIM predictions as references," "Distilled previewer as references"). Reconcile the apparent discrepancy between Tables 4a and 4b, or remove the confusing row labels.
2. **Specify the adaptive mechanism.** Provide the mathematical form of how `δ` modulates the Aggregator's SFT parameters, cross-attention weights, or residual connections. Without this, the method is not reproducible.
3. **Quantify the adaptivity.** Show that `δ` correlates with degradation level across a large set of held-out images, and demonstrate that the adaptive weighting produces measurably different behavior on easy vs. hard inputs.
4. **Either evaluate creative restoration or remove the claim.** If text-guided variation is a contribution, provide CLIP scores, semantic accuracy, or at least a systematic comparison across multiple prompts and images.
