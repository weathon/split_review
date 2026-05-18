Now I have a thorough understanding of the paper and all reviewer claims. Let me compose the final consolidated review.

---

## Summary

This paper proposes the Prompt-guided Dynamic Network (PDN) for single image super-resolution, together with a plug-and-play Dynamic Correlation Module (DCM) that can be inserted into existing SR backbones. DCM consists of two components: a Spatially Multi-Modal Attention Module that computes pixel-wise similarity between LR features and a prompt embedding (text or image), producing an attention mask that highlights prompt-relevant regions; and a Prompt-Guided Dynamic Convolution Module that generates dynamic convolutional kernels conditioned on the prompt embedding rather than on image features. The method uses CLIP to extract prompt embeddings offline. The strongest evidence for the method's effectiveness is Table 3, where inserting DCM into EDSR, RDN, and RCAN (all trained identically on COCO) yields PSNR gains of 0.11–0.51 dB at ×4 scale.

## Strengths

- **Plug-and-play DCM consistently boosts multiple SR backbones under fair comparison.** When DCM is inserted into EDSR, RDN, and RCAN and all models are retrained on COCO ×4 with identical settings (Table 3), the upgraded networks achieve PSNR gains of 0.11–0.51 dB and SSIM gains of 0.009–0.02. This is the paper's cleanest and most convincing evidence, as it controls for training data and protocol.

- **First to condition convolutional kernel estimation on multi-modal prompts in SR, with clear differentiation from prior work.** The paper argues in the Remark (Section 3.3) that using prompt embeddings from CLIP (rather than image features as in CondConv) yields higher-variance, more discriminative dynamic kernels. This is distinguished from TGSR, which uses text attention but not kernel estimation. The novelty claim is specific and defensible.

- **The attention masks are interpretable and align with prompt content.** Figures 4 and 5 show that the learned attention masks highlight spatial regions corresponding to informative words in captions (e.g., "cats," "tennis player"). This provides qualitative validation that the model learns meaningful cross-modal correspondences.

- **PDN outperforms the only prior text-guided SR method (TGSR) on most metrics.** On what is contextually the COCO ×8 task (Table 2), PDN achieves higher PSNR, SSIM, lower NIQE, and lower FID. The paper offers reasoned analysis for why TGSR underperforms (e.g., LSTM trained from scratch, static inference).

- **Ablation confirms both sub-components contribute.** Table 4 shows that removing either the attention module or the dynamic convolution module from EDSR+ degrades performance, validating the two-part design.

## Weaknesses

### Fatal

None.

### Major

- **Table 1 comparison likely uses baselines trained on different data, undermining the claimed state-of-the-art results.** Section 4.2 compares PDN (trained on COCO/FFHQ) against RCAN, RDN, EDSR, SRGAN, ESRGAN, and SPSR, but never states that these baselines were retrained on the same data. The mention that "RDN does not provide ×8 and ×16 models in the official source code, so we add additional up-sampling blocks" implies use of pretrained (likely DIV2K-trained) models. This makes the observed PSNR/SSIM gap uninterpretable — it could stem from different training distributions rather than from the proposed method. The only fair comparison for PDN as a full network would require retraining all baselines on COCO/FFHQ.  
  **Mitigating factor:** The paper's core claim (DCM boosts existing methods) is independently validated by Table 3, which uses fair, same-data comparisons. The Table 1 issue primarily affects the claim that "PDN achieves state-of-the-art" as a standalone network, not the DCM contribution.

- **The ablation study never isolates the prompt itself.** Table 4 removes entire sub-modules (replacing dynamic convolution with standard convolution, removing the attention mask) but never replaces the prompt embedding with a baseline (e.g., a zero vector, a random vector, or a learned constant) while keeping the rest of DCM intact. Without this, the improvement cannot be attributed to the *semantic content* of the prompt versus the added network capacity of the dynamic convolution + attention machinery. This is a genuine gap: the flipped-image prompts used on FFHQ/Set5/Set14/Urban100 are transformations of the same image, so the "semantic information" from the prompt is largely redundant with the LR features, making the capacity-based explanation especially plausible.

- **The TGSR comparison (Table 2) does not explicitly state the evaluation dataset.** The caption reads "Quantitative results of TGSR and PDN" without specifying which dataset or scale factor was used. The surrounding text discusses COCO context, but the omission is a reproducibility concern.

### Minor

- **No parameter count, FLOPs, or inference time reported for DCM.** The paper describes DCM as "lightweight" and "plug-and-play" but provides no quantitative overhead numbers. This makes it difficult to assess the practical cost-benefit trade-off, especially since DCM is inserted at multiple positions (e.g., after every residual block in EDSR).

- **Several hand-tuned hyperparameters without sensitivity analysis.** The temperature coefficient (initialized at 34, decayed by 3 every 10 epochs), the scaling factor ζ (initialized at 50), and the number of basis kernels (n=4) are set without any ablation or robustness study. It is unclear how sensitive the results are to these choices.

- **No limitations or failure-case discussion.** The paper does not discuss scenarios where the method might falter (e.g., inaccurate or too-generic captions, mismatch between prompt and image content, or failure modes on out-of-distribution prompts).

### Trivial

None.

## Nice-to-Haves

- A qualitative / ablative comparison between text prompts, flipped-image prompts, and a no-prompt baseline (e.g., zero embedding) would substantially strengthen attribution.
- Retraining the full set of baselines on COCO/FFHQ for Table 1, or at minimum adding a clarifying statement about the training data used for each baseline.
- Reporting overhead (parameters/FLOPs for DCM vs. the base model).
- A hyperparameter sensitivity study for the temperature coefficient, ζ, and n.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Set5 and Set14 are no longer standard for modern SR."** (Harsh Critic, "Other Observations"). This is factually incorrect — Set5 and Set14 remain standard benchmarks in SR literature, and the paper additionally evaluates on Urban100 and Celeba-HQ. The paper itself describes them as "commonly used benchmarks."
- **"The novelty is incremental: the dynamic convolution module is a standard CondConv..."** (Harsh Critic, "Other Observations"). This is a subjective opinion, not a verifiable weakness. The paper explicitly distinguishes from CondConv in the Remark (Section 3.3), noting the use of prompt embeddings rather than image features, which the authors argue yields higher-variance kernels. Whether this constitutes sufficient novelty is a judgment call, not a factual error.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a prompt-level ablation.** Replace the prompt embedding with (a) a zero vector, (b) a random fixed vector, and (c) a learned constant vector, while keeping all other DCM components intact. This would directly test whether the *semantic content* of the prompt drives the improvement, or whether the gains come from added capacity alone.
2. **Clarify the training data for all baselines in Table 1.** If baselines are pretrained on different data, either retrain them on COCO/FFHQ or add a clear statement and discuss the potential confound.
3. **Explicitly state the evaluation dataset and scale factor for Table 2.**
4. **Report the parameter count and FLOPs** for DCM relative to each base model, and discuss the practical overhead.
5. **Add a limitations paragraph** discussing when prompts may be unavailable, inaccurate, or unhelpful.

## Score and Decision

**Overall assessment:** The paper has a genuine contribution — conditioning dynamic convolution on multi-modal prompt embeddings for SR is a novel direction with practical potential. The strongest evidence is Table 3, where DCM boosts three established backbones under fair, same-data conditions. However, the evaluation has two significant gaps: (1) the main Table 1 comparison appears to use baselines trained on different data, making the headline "state-of-the-art" claim unsubstantiated, and (2) the ablation never isolates the prompt itself, so the improvement cannot be attributed to semantic guidance rather than added capacity. These issues are addressable with revision but limit the paper's credibility in its current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>