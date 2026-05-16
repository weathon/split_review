Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper presents MM-SAM, an adaptation framework that extends SAM to handle non-RGB sensor modalities (depth, thermal, LiDAR, SAR, etc.) and fuse multiple modalities. It introduces two lightweight modules: Unsupervised Cross-Modal Transfer (UCMT), which aligns non-RGB embeddings with SAM's RGB embedding space via an L2 loss and LoRA tuning, and Weakly-supervised Multi-Modal Fusion (WMMF), which uses a Selective Fusion Gate (SFG) to adaptively combine multi-modal embeddings, trained via pseudo-labeling. The method is evaluated on seven datasets covering eight sensor modalities, consistently outperforming SAM on false-color inputs.

## Strengths

- **First unified framework extending SAM to multi-modal sensor suites.** While prior work adapts SAM to individual non-RGB domains (depth, medical, etc.) via fine-tuning or false-color conversion, MM-SAM provides a single architecture that handles both cross-modal adaptation and multi-modal fusion across diverse sensor types (thermal, depth, LiDAR, HSI, SAR, MS-LiDAR, DSM). This is a genuine contribution to the foundation-model adaptation literature. (Section 3, Figures 1-2; stated "to the best of our knowledge" on line 38.)

- **Parameter- and label-efficient by design.** MM-SAM adds only 492.9K–1.5M trainable parameters (vs. SAM's 91M) depending on the modality's input channels (Table 1), and requires no mask annotations for training — UCMT uses unsupervised embedding alignment while WMMF uses pseudo-labeling with geometric prompts. This combination of parameter efficiency and label efficiency is the paper's central practical advantage.

- **Consistent and substantial improvements across all evaluated modalities and datasets.** MM-SAM outperforms SAM on false-color data on every dataset. Representative results: RGB+Thermal fusion on MFNet achieves 75.9 mIoU vs. SAM's 68.2 on RGB alone (Table 2a); MS-LiDAR adaptation on DFC2018 reaches 85.1 IoU vs. SAM's 75.1 on false-color MS-LiDAR (Table 3b); three-modality fusion (RGB+HSI+MS-LiDAR) reaches 89.3 IoU (Table 3b). The improvement is not limited to one or two favorable settings.

- **Adaptive fusion visualization provides intuitive support for the fusion mechanism.** Figure 3 shows SFG assigning higher weight to thermal in regions where RGB is degraded (e.g., car headlight glare), leading to more accurate segmentation. This provides qualitative evidence that the adaptive weighting is working as intended.

- **Robustness to backbone and PEFT choices.** Ablations show MM-SAM works with three PEFT methods (LoRA, AdapterFormer, VPT) and three ViT backbones (ViT-B/L/H) with consistent gains (Figure 2), demonstrating the framework is not brittle.

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation of the core technical claims.** Two central design choices are not isolated:
  1. **UCMT's embedding unification loss (L_U).** There is no comparison between "SAM with only new patch embedding + LoRA (no alignment loss)" vs. UCMT full (with alignment loss). Without this, the reader cannot tell whether the alignment loss itself is beneficial, or whether simply having a modality-specific patch embedding and LoRA (aligned through joint training with SAM's frozen decoder) would suffice.
  2. **WMMF's Selective Fusion Gate (SFG).** The fusion gate is not compared against simple alternatives such as averaging the two embeddings, concatenating them, or late-fusion of mask predictions. The paper shows MM-SAM RGB+X beats single-modality MM-SAM, but this could reflect the benefit of having two modalities rather than the *adaptive weighting* mechanism. An ablation comparing SFG to "average embeddings" or "learned constant weights" is needed to validate the claimed contribution of the gate.

  These are not fatal — the method works, and the overall improvements are clear — but they leave the *explanatory* claims under-supported. A paper that introduces two novel modules should demonstrate that each module specifically contributes beyond simpler alternatives.

- **Uninterpretable metric reporting for MFNet and FreiburgThermal.** Table 2a and Table 4a report mIoU as three slash-separated numbers (e.g., 68.2/72.6/65.1 for SAM on RGB). These are never defined. Other datasets (SUN RGB-D, SemanticKITTI) report a single number. The caption of Figure 2 mentions "MFNet ('Total' split)," suggesting the three numbers may correspond to day/night/total splits (a known convention for MFNet), but the paper does not state this explicitly anywhere. The reader cannot interpret the results without this information.

### Minor

- **No analysis of pseudo-label quality.** WMMF relies on pseudo-labels generated from single-modal predictions of the UCMT-adapted encoders. If UCMT produces poor embeddings for a modality far from RGB (e.g., SAR), the pseudo-labels may be noisy, and this noise propagates to the fusion training. The paper does not analyze pseudo-label quality (e.g., agreement with ground truth, confidence distributions) or study how it correlates with final fusion performance.

- **No variance or statistical significance reporting.** None of the results include error bars or multiple-run statistics. This is especially concerning for DFC2018, which has only 12 training pairs and 2 test pairs (Table 2), where a single run's result may not be stable. While single-run evaluation is common in this space, the very small test sets make reporting variance important.

- **The "mask-free" claim could be clarified regarding prompt sources.** The paper states training is "mask-free" and uses "geometric prompts" / "bounding box prompts." It is not explicitly stated whether these prompts come from ground-truth annotations (box labels) or are automatically generated (e.g., from a detector or SAM's automatic mask generator). If prompts are derived from ground-truth boxes, the method still requires some annotation (box-level), which is a meaningful reduction from mask-level but is not fully unsupervised. The paper's framing as "weakly-supervised" is accurate, but the exact source of prompts should be specified per dataset.

- **Zero-shot generalization claims are modest for same-sensor-type transfer.** The MFNet→FreiburgThermal zero-shot experiment transfers between two thermal datasets with similar road-scene content. This demonstrates robustness but is less impressive than the SUN RGB-D→NYU/B3DO cross-dataset transfer. The claims should be calibrated accordingly.

### Trivial
- The paper would benefit from reporting inference speed (even relative to SAM) to contextualize the overhead from the added modules.

## Nice-to-Haves
- Comparing UCMT against a simple domain-adaptation baseline (e.g., unsupervised domain adaptation with adversarial alignment) would further strengthen the label-efficiency claim.
- An analysis of when fusion helps vs. hurts (e.g., per-sample comparison of fusion vs. best single modality) would deepen understanding of the SFG's behavior.
- A discussion of whether UCMT could work with synthetic cross-modal pairs or unpaired data (e.g., cycle-consistency) would broaden the applicability scope.

## Removed Points

- **Criticism about missing supervised fine-tuning baselines (LoRA-finetuning with mask supervision).** The paper's core claim is label-efficient adaptation *without mask annotations*. Comparing against a method that requires mask supervision would test a different paradigm and would be asymmetric in favor of the baseline. The controlled comparison against SAM on false-color data is the appropriate baseline for the cross-modal claim. The reviewer's point about domain-adaptation baselines is moved to Nice-to-Haves.

- **Criticism about the "first work" claim being insufficiently scoped.** The paper already qualifies this as "To the best of our knowledge" (line 38, 151). This is appropriate for a first-claim.

- **Criticism about not discussing why L2 loss is preferred over contrastive/adversarial losses for UCMT.** This is a design choice discussion, not a weakness. The L2 loss is simple and demonstrably effective; the choice is adequately justified by the results.

- **Criticism about missing limitation of paired RGB training data.** The paper explicitly acknowledges this limitation (line 379: "Training MM-SAM requires paired modalities with RGB images, meaning an RGB camera must be included in sensor suites to collect training data. However, this constraint does not apply during inference.").

## Novel Insights

The most interesting observation emerging from the reviews is the distinction between the paper's two claims: (1) that the method *works* (producing good segmentations on non-RGB data without mask labels) and (2) that the specific *mechanisms* (L2 alignment loss and adaptive weighting gate) are responsible for the gains. The evidence strongly supports (1) across diverse modalities, but (2) remains under-ablated. This gap between "the method works" and "the method works for the stated reasons" is the review's central tension. The paper's strongest contribution is the overall pipeline and its demonstrated generality; the weakest link is the attribution of performance to specific component designs.

## Suggestions

1. **Add the two key ablations**: (a) UCMT with vs. without the L_U alignment loss (patch embedding + LoRA only), and (b) SFG vs. simple alternatives (average embeddings, learned constant weights, late fusion). These are the most impactful additions and directly test the paper's claimed contributions.

2. **Define the MFNet metric triples** explicitly (e.g., "day/night/overall" or whatever the splits are). This is a basic readability fix.

3. **Report variance** (mean ± std over 3 runs) for the small-test-set datasets (DFC2018 with 2 test samples, ISPRS Potsdam).

4. **Clarify the prompt source** for each dataset: are training prompts from ground-truth boxes, SAM's automatic mask generator, or a detector? This directly addresses the "mask-free" claim's precision.

## Score and Decision

The paper addresses a genuine gap — extending SAM to multi-modal sensor suites with label efficiency — and provides a clean, well-motivated architecture validated across an impressively broad range of modalities and datasets. The improvements over SAM on false-color data are consistent and substantial. However, the missing ablations of the two core modules (UCMT's alignment loss and SFG's adaptive weighting) leave the paper's *explanatory* claims under-supported, and the uninterpretable MFNet metrics are a basic reporting deficiency. These issues are fixable with additional experiments and clarifications and do not threaten the paper's core empirical finding (MM-SAM works well across modalities). The paper is a solid contribution that would be strengthened by the suggested additions.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>