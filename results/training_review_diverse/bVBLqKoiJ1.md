## Summary

This paper introduces "Paint by Inpaint," a framework that constructs a large-scale, high-quality dataset (PIPE) for text-guided object addition by inverting the object-removal process. The key insight is that removing objects (via inpainting) is easier than adding them, so the paper creates training pairs where real images serve as targets and their inpainted (object-removed) versions serve as sources, then trains a diffusion model to reverse the process. The resulting model achieves strong quantitative and qualitative results across multiple benchmarks and is preferred by human evaluators 72.5% over InstructPix2Pix.

## Strengths

- **Clever and well-motivated inversion insight.** The observation that object addition is the inverse of object removal, and that this inversion allows leveraging abundant segmentation data to create training pairs with *real* target images (rather than synthetic ones), is genuinely novel and clearly articulated (Abstract, lines 7–11, Section 3).

- **Large-scale, high-quality dataset with real targets.** PIPE contains ~1M image pairs, ~1.88M instructions, and >1,400 classes. As Table 1 shows, it is the only dataset offering both real target images and general classes, with consistency between source and target enforced by construction.

- **Consistently strong empirical performance.** The trained model outperforms IP2P, Hive, SDEdit, and VQGAN-CLIP across L1, L2, CLIP-I, and DINO on the PIPE test set, MagicBrush (both zero-shot and fine-tuned), and OPA (Tables 2–4). The human evaluation (72.5% overall preference over IP2P, Table 5) provides strong complementary evidence.

- **Careful data curation pipeline.** The multi-stage filtering (pre-removal CLIP filtering, CLIP consensus, multimodal CLIP filtering, consistency enforcement, importance filtering) is thorough and well-reasoned (Section 3.1, Figure 3).

- **Diverse instruction generation.** Using VLM-LLM (CogVLM + Mistral) and manual references (RefCOCO/RefCOCO+/RefCOCOg) produces varied, natural-language instructions beyond simple class names (Section 3.2).

- **General editing enhancement.** Combining PIPE with the IP2P dataset and fine-tuning on MagicBrush yields improved general editing performance (Table 6), demonstrating utility beyond object addition.

## Weaknesses

### Fatal

None.

### Major

None.  

The paper's core contributions (the inversion insight, the dataset, the trained model) are sound and well-supported. The concerns below are substantive but do not threaten acceptance.

### Minor

- **Training–inference mismatch in source-image structure.** During training, every source image has the object region pre-filled with plausible background (via inpainting). At inference, the user provides a natural image with arbitrary content where the object should go. The paper provides strong evidence that the model generalizes (OPA uses natural source images; MagicBrush is fully out-of-distribution), but it does not analyze *how* the model decides where to place objects or whether it relies on cues from the inpainted region (e.g., interpolation artifacts) that are absent at test time. This does not invalidate the contribution—the empirical results speak for themselves—but it leaves an important question unexamined. The authors should add localization analysis (e.g., attention maps, comparison to ground-truth positions on OPA) or at minimum acknowledge and discuss this discrepancy explicitly. The existing generalization evidence partially addresses the concern, but the lack of analysis is a genuine gap.

- **Narrow baseline comparison for the general editing claim (Section 6).** The paper states that combining PIPE with IP2P data yields "new state-of-the-art scores for the general editing task" (line 508). The comparison is limited to IP2P (original and fine-tuned on MagicBrush). The harsh critic's claim that "no comparison is made with MagicBrush's own trained model" is **incorrect**—IP2P FT *is* the MagicBrush-trained model, since the MagicBrush paper (Zhang et al.) fine-tuned IP2P on MagicBrush data and established it as the prior SOTA on that benchmark. However, the broader point stands: only IP2P variants are compared. Adding at least one more contemporary baseline (e.g., Hive, which is compared in the object-addition experiments but not in the general editing experiment) would substantially strengthen the SOTA claim. The claim is defensible as written (beating the previous best model on this benchmark), but the framing overreaches given the narrow comparison set.

- **No confidence intervals or error bars on quantitative metrics.** For the MagicBrush object-addition subset (144 edits) and OPA, variance could be non-negligible. While the improvements are large enough to likely be significant, reporting standard deviations or bootstrap confidence intervals would improve rigor, especially given that the paper notes reproducibility difficulties with the IP2P MagicBrush fine-tuning baseline (line 505).

- **Fine-tuning reproducibility gap.** The paper honestly reports being unable to reproduce IP2P's MagicBrush fine-tuning results (line 505). Reporting the exact configuration used for fine-tuning IP2P (learning rate, steps, scheduler, seed) would help future comparisons and mitigate this concern.

### Trivial

None that survive filtering.

## Nice-to-Haves

- **Statistics on filtering stages.** Reporting how many examples are removed at each pre-removal and post-removal stage would help readers understand the quality–diversity trade-off. This is particularly relevant for the pre-removal CLIP-object similarity filter, which the paper itself notes removes "abnormal object views" and "occluded objects" (line 216)—quantifying the fraction removed would contextualize potential class bias.

- **Ablation comparing PIPE to a synthetic object-addition dataset.** Training the same model on a synthetically generated object-addition dataset (matched in scale to PIPE) would cleanly demonstrate that real target images are the key advantage. This is a natural follow-up experiment, not a weakness of the current paper.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"No comparison is made with...MagicBrush's own trained model"* — Factually incorrect. IP2P FT (line 491, Table 6) **is** the MagicBrush-trained model, as the MagicBrush paper fine-tunes IP2P on the MagicBrush dataset. The comparison is therefore present.
- *Alpha-blending boundary artifacts (Consistency Enforcement)* — Purely speculative concern with no evidence that such artifacts exist or that the model exploits them. The paper states the blending ensures "a smooth, natural transition between the regions" (line 248), which is standard practice.
- *Pre-removal CLIP filtering biases toward easy objects* — This is inherent to any quality filtering and is acknowledged by the paper's design (filtering "abnormal object views...occluded objects," line 216). The concern is valid in principle but is a design choice, not a flaw. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the authors have missed or that recontextualizes their contribution in a surprising way.

## Suggestions

1. **Add a discussion and analysis of the training–inference mismatch.** Even a short paragraph acknowledging the discrepancy and providing evidence that the model does not rely on inpainted-region cues (e.g., showing attention maps, comparing output locations to ground-truth positions on OPA) would significantly strengthen the paper.

2. **Broaden the baseline set in Section 6 (general editing) or temper the SOTA claim.** Adding Hive and/or the original MagicBrush model to Table 6 would either confirm the SOTA claim or reveal its limits. If adding baselines is impractical, replace "sets new state-of-the-art" with "improves over the previous best method (fine-tuned IP2P) on this benchmark."

3. **Report standard deviations or confidence intervals** for the quantitative results, especially on the smaller test sets (MagicBrush: 144 edits; OPA).

4. **Include the exact fine-tuning configuration** used for the IP2P baseline that the authors could not reproduce, to aid reproducibility.

## Score and Decision

**Originality:** High — the inversion insight is genuinely clever.  
**Importance of question:** High — mask-free object addition is a practically relevant and challenging task.  
**Claims support:** Good, with minor overclaiming in Section 6.  
**Soundness:** Solid — experiments are well-designed, the dataset pipeline is thorough, and the human evaluation is rigorous.  
**Clarity:** Good — the paper is well-structured and the core idea is clearly communicated.  
**Value to community:** High — the dataset, model, and framework are likely to be widely used.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>