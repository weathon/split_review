Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes a Prompt-guided Dynamic Network (PDN) for single image super-resolution, whose core contribution is the Dynamic Correlation Module (DCM). DCM uses CLIP-extracted multi-modal prompts (text captions or images) to (1) generate a spatial attention mask that highlights prompt-relevant regions via a Spatially Multi-Modal Attention Module, and (2) dynamically combine basis convolutional kernels based on the prompt embedding via a Prompt-Guided Dynamic Convolution Module. The module is designed as a plug-and-play component that can be inserted into existing SR networks (EDSR, RDN, RCAN), and experiments show consistent improvements across multiple benchmarks.

## Strengths

- **First use of multi-modal prompts for convolutional kernel estimation in SR.** The paper introduces a novel mechanism where prompt embeddings (from CLIP) directly determine convolutional kernel weights, going beyond prior work like TGSR that uses text for feature modulation rather than kernel estimation. The Remark in Section 3.3 clearly distinguishes this from conventional dynamic convolution (CondConv), which derives weights from image features alone.

- **Plug-and-play DCM consistently improves multiple strong SR baselines.** When integrated into EDSR, RDN, and RCAN, the proposed DCM yields PSNR gains of up to 0.51 dB and SSIM gains of up to 0.02 on Urban100 ×4 (Table 3, Section 4.4), with minimum improvements of 0.11 dB and 0.009 SSIM across all three backbones. This demonstrates the module's robustness and general applicability.

- **Attention masks visually align with prompt semantics.** Figures 4 and 5 show that the Spatially Multi-Modal Attention Module produces masks that highlight image regions corresponding to specific textual prompts (e.g., "a big cat and a small cat" highlights the cats, "Two cats sit side by side while looking at a television" also highlights the television). This provides direct evidence that the cross-modal attention is semantically meaningful.

- **Outperforms the only prior text-guided SR method on most metrics.** PDN surpasses TGSR in PSNR (by 1.14 dB on COCO ×4), SSIM, NIQE, and FID (Table 2, Section 4.3), while using a simpler non-adversarial training setting. The paper acknowledges the adversarial training difference and explains why its L1-based comparison is still meaningful.

## Weaknesses

### Fatal
None.

### Major

- **The effectiveness of flipped-image prompts (used for benchmark evaluations) is not analyzed.** For datasets without captions (Set5, Set14, Urban100, Celeba-HQ), the paper uses a horizontally flipped LR image passed through the CLIP *image* encoder as the "prompt" (Section 4.1). While this is within the paper's stated scope of supporting both text and image prompts, the paper provides no analysis of whether these flipped-image prompts actually provide useful semantic guidance vs. being mere extra computation. The attention mask visualizations (Figures 4, 5) are shown only for text prompts, never for the flipped-image prompts that produce the benchmark numbers in Table 1. This means the core claim — that multi-modal semantic information drives the improvement — is only directly validated on COCO (text prompts), leaving a gap in explaining benchmark performance.

- **PDN's backbone architecture is not precisely specified.** The paper states PDN uses "residual in residual (RIR) blocks" (Section 3.2) borrowed from RCAN, but does not clearly state whether PDN is simply RCAN with DCM built in from scratch or a different configuration. Table 1 reports PDN achieving 30.21 PSNR on Urban100 ×4 while Table 3 shows "RCAN+" (RCAN + DCM) achieving 29.92 — a 0.29 dB gap that is not explained. Without clarifying what distinguishes PDN (Table 1) from RCAN+ (Table 3), readers cannot fully interpret the headline results.

### Minor

- **Abstract understates reported improvements.** The abstract claims "PDN improves PSNR up to 0.11" at ×4, but Section 4.4 reports improvements "up to 0.51 dB" from the same DCM module. The phrase "up to 0.11" is factually inconsistent with the paper's own larger reported gains (0.51 dB). This appears to be an editing error (the paper likely means "at least 0.11 dB") but should be corrected.

- **Ablation study could more tightly control for parameter count.** The ablation (Table 4, Section 4.6) removes the Prompt-Guided Dynamic Convolution Module (replaced with standard convolution) or the Spatially Multi-Modal Attention Module, but does not add an equal-parameter-cost baseline (e.g., extra standard convolutions matching the parameter count of the removed modules). While the "w/o dy" variant replaces dynamic conv with standard conv (which partially controls for parameters), the "w/o att" variant's replacement is not described, making it unclear whether the gains are purely from added capacity.

- **No sensitivity analysis for prompt quality.** The paper never examines what happens with random prompts, mismatched prompts, or ablated prompt encoders (e.g., replacing CLIP with a randomly initialized encoder). This makes it difficult to attribute improvements specifically to semantic cross-modal knowledge vs. the mere presence of an additional input stream.

### Trivial

- None beyond the issues already listed above.

## Nice-to-Haves

- **Parameter-controlled ablation:** Adding a variant where DCM modules are replaced by standard convolutions with the same parameter count would strengthen the attribution of gains to the attention/dynamic mechanisms.
- **Prompt quality ablation:** Comparing CLIP embeddings against randomly initialized or fixed random embeddings would demonstrate that large-scale pre-training matters.
- **Flipped-image attention visualizations:** Showing attention masks from flipped-image prompts would clarify whether the model learns semantically meaningful correspondences in that setting.
- **Evaluation on a dataset with paired text captions (e.g., COCO test set)** using text prompts, with a breakdown of text vs. image vs. no-prompt results, would directly validate the multi-modal motivation for benchmark performance.

## Removed Points

- **"PDN's backbone is undisclosed making Table 1 uninterpretable"** — The paper describes PDN's use of RIR blocks (from RCAN) in Section 3.2, providing sufficient architectural information. The ambiguity is about the precise difference between PDN and RCAN+ (a valid clarity concern kept as a Major weakness), not a complete absence of specification.
- **"Flipped-image prompts contradict the multi-modal motivation"** — The paper explicitly defines prompts as "texts or images" (abstract, Section 3.1) and states "another augmented view" is a valid prompt. Using a flipped image as an image prompt is within the stated scope. The kept weakness concerns the lack of analysis, not a contradiction.
- **"Novelty claim ignores TGSR"** — The paper discusses TGSR in Related Work (Section 2.1) and the Remark in Section 3.3 clearly distinguishes prompt-guided *kernel estimation* from TGSR's text *feature modulation*. The distinction is adequately drawn.
- **"TGSR comparison is unfair due to adversarial training"** — The paper explicitly acknowledges this difference (Section 4.3: "Since TGSR is trained in an adversarial setting, it is expected that TGSR poses better PI values") and justifies why the other four metrics are still meaningful. The comparison is presented transparently.
- **"Attention masks shown only for text prompts, never for flipped-image prompts"** — Kept as part of the Major weakness about lacking analysis of flipped-image prompts, not as a separate weakness.

## Novel Insights

A genuinely interesting pattern across the reviews is that the paper's strongest evidence (consistent DCM improvements across three backbones in Table 3) and its weakest link (unexplained gap between PDN and RCAN+ in Tables 1 vs. 3) point to the same underlying ambiguity: the paper never crisply defines the architectural recipe that distinguishes a "PDN" trained from scratch from a "backbone+DCM" retrofit. The Table 3 results are clean and compelling — they directly show that adding DCM to existing networks yields consistent gains. The Table 1 results, however, mix this clean signal with the unknown confound of a different training pipeline. The paper would be stronger if it either (a) replaced the opaque "PDN" row in Table 1 with the specific backbone+DCM variants from Table 3, or (b) explicitly stated the architectural recipe for PDN and explained any gap with RCAN+.

## Suggestions

1. **Clarify the PDN ↔ RCAN+ relationship.** State explicitly whether PDN (Table 1) is RCAN trained from scratch with DCM, and if so, explain the 0.29 dB Urban100 gap with RCAN+ (Table 3). If the difference is due to DCM placement, training hyperparameters, or a different number of modules, describe this clearly.

2. **Add a prompt-source ablation.** Compare CLIP embeddings vs. a fixed random vector vs. a randomly initialized encoder as prompts. This would directly test whether large-scale pre-training is responsible for the gains.

3. **Analyze flipped-image prompts.** Show attention masks from flipped-image prompts on benchmark datasets, and consider including an experiment that compares text vs. image vs. no-prompt on a dataset where all three are available (e.g., a subset of COCO).

4. **Fix the abstract's "up to 0.11 dB" claim.** Change to "at least 0.11 dB" or "up to 0.51 dB" to match the actual results.

5. **Strengthen the ablation** by adding a parameter-matched baseline where removed DCM modules are replaced by standard convolutions with identical parameter counts.

## Score and Decision

The paper presents a novel and well-motivated approach for integrating multi-modal prompts (via CLIP) into SR through dynamic convolution. The plug-and-play DCM module shows consistent and sometimes substantial improvements across multiple backbones (up to 0.51 dB on Urban100), and the attention visualizations provide qualitative evidence of semantic alignment. The approach is clearly distinguished from prior work.

However, the paper has two significant weaknesses: (1) it does not analyze whether flipped-image prompts (used for benchmark evaluation) actually provide meaningful semantic guidance, creating a gap between the claimed contribution and the benchmark evidence; and (2) the relationship between "PDN" (Table 1) and the backbone+DCM variants (Table 3) is insufficiently explained, making the headline comparison partially ambiguous. These issues are addressable in revision but prevent full confidence in the current submission.

The paper represents a solid, incremental advance with a clean modular design and convincing plug-and-play results, but the evaluation has structural gaps that need filling.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>