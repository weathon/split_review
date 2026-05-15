Now I have thoroughly verified the paper content against all reviewer claims. Let me produce the final consolidated review.

## Summary

The paper proposes AntifakePrompt, which formulates deepfake detection as a visual question answering (VQA) task and uses soft prompt tuning on InstructBLIP (a VLM) to distinguish real from fake images. The method tunes only 4,864 parameters (two pseudo-word embeddings) while keeping the backbone frozen, and is evaluated across 23 datasets spanning 6 categories of generated/edited images. The paper reports strong average accuracy (91.81%) across held-out datasets, substantially outperforming non-VLM baselines.

## Strengths

- **Novel formulation of deepfake detection as VQA with prompt tuning yields strong generalization.** The paper demonstrates that prompt tuning raises average held-out accuracy from 36.53% (pretrained InstructBLIP without tuning) to 91.81% (AntifakePrompt) across 21 held-out fake datasets (Table 2). This directly supports the core claim that VLM + prompt tuning improves cross-domain generalization, and the within-backbone comparison cleanly isolates the effect of prompt tuning.

- **Extreme parameter efficiency.** The method tunes only 4,864 parameters (two pseudo-word embeddings of dimensions 768 and 4096) while keeping the backbone frozen. This is orders of magnitude fewer than baselines (e.g., 23M for ResNet-50-based Wang2020, ~4M for LoRA). Despite this, AntifakePrompt achieves the best average accuracy among all methods in the main comparison (Table 2).

- **Comprehensive, standardized evaluation across diverse fake image types.** The paper curates 23 testing datasets spanning text-to-image (SD2, SD3, SDXL, IF, DALLE-2, DALLE-3, etc.), inpainting, super-resolution, face swap, stylization, and image attacks. This provides a valuable benchmark for the community and demonstrates careful thinking about distribution coverage.

- **Systematic ablation studies.** The paper ablates pseudo-word position, which modules receive tuning (Q-Former only, LLM only, both), and training data size (180K down to 150 images). Results consistently support the chosen configuration and show graceful degradation with less data.

## Weaknesses

### Fatal
None. The core claim — that prompt-tuned VLMs outperform untuned VLMs and most existing baselines for deepfake detection — is supported by evidence. The pretraining contamination concern does not invalidate the primary comparison (AntifakePrompt vs. InstructBLIP P), since both share the same backbone and pretraining.

### Major

- **DIRE F baseline is unsubstantiated and potentially broken.** DIRE is a reconstruction-based method, not a classifier; its original formulation does not support direct finetuning with binary cross-entropy loss. The paper provides no explanation of how DIRE was adapted (loss function, hyperparameters, architecture changes), and the resulting average accuracy of 33.61% (close to random) suggests the adaptation may be flawed. This baseline inflates the apparent gap between AntifakePrompt and existing methods and should either be explained properly or removed.

- **Attack dataset task definition is ambiguous.** The three "attack datasets" (adversarial, backdoor, data poisoning) are perturbations applied to real photographs. Whether these should be labeled "real" (the underlying image is a genuine photograph) or "fake" (the image has been manipulated) depends on the task definition, which the paper never clarifies. If the ground truth is "real" (a valid alternative framing), then the reported accuracies of 87–96% on these datasets mean something different from the other fake-detection results. This ambiguity makes the attack-dataset results difficult to interpret.

- **Factual error in the Conclusion about training data composition.** The Conclusion states the method is "trained solely on generated images using SD3 and real images from COCO datasets," but the actual training set uses both SD3 **and SD2IP** (SD2-inpainting) — 30K images from each. This is not a trivial omission since SD2IP contributes roughly one-third of the fake training data. The error suggests inadequate proofreading and should be corrected.

### Minor

- **Abstract's claimed improvement (71.06% → 92.11%) is not verifiable from Table 2.** The abstract states that accuracy improves "from 71.06% to 92.11%" but no per-dataset average in Table 2 equals 71.06% for any baseline. The closest are LASTED F (72.11%) and DE-FAKE F (72.34%). The comparison is qualitatively correct but the specific number is unsubstantiated. (The "92.11%91.23%92.73%" is a parser artifact, not an author error.)

- **Justification for choosing InstructBLIP over CogVLM is weak.** The pilot study shows both models perform near chance on held-out data (InstructBLIP P: 36.53%, CogVLM P: 33.98%). Claiming that InstructBLIP has "greater potential" based on a 2.55% gap near random levels is not convincing. While the choice itself may be reasonable, the stated justification is insufficient.

- **The 0.15K training result (99%+ on COCO/Flickr real images with only 90 real training examples) is not critically discussed.** The ablation table shows that with 150 total training images (90 real + 60 fake), the model achieves 99.07% on COCO and 99.73% on Flickr real images, while fake detection collapses on most datasets. This pattern suggests the model may be leveraging VLM pretraining priors about "realness" rather than learning from the training data, but the paper does not flag or analyze this phenomenon.

- **Explanation of VLM generalization is hand-wavy.** The paper attributes the method's strong generalization to "the notable generalizability of LLM, brought by its large training corpus" without further analysis. This is speculative and does not explain why prompt tuning specifically (as opposed to the VLM backbone alone) enables generalization across diverse generator types.

- **"First to leverage VLMs" novelty claim is unsupported.** The paper states "We pioneer to leverage pretrained vision-language models to solve the deepfake detection problem." By 2026, this claim is unlikely to hold, and the paper provides no literature survey to support it. The contribution does not depend on being first, so this claim should be moderated.

### Trivial
None. (The garbled numbers in the abstract are parser artifacts, not author errors.)

## Nice-to-Haves
- Report per-dataset standard deviations or confidence intervals. Many baselines already exceed 95% on several datasets, so point estimates alone make it hard to assess whether improvements are statistically significant.
- Include a control experiment on real images from a source released after the VLM's training cutoff to fully address pretraining contamination concerns.
- Clarify how DIRE was adapted for direct finetuning, or replace it with a more straightforward baseline.
- Disentangle the contributions of VLM pretraining vs. prompt tuning vs. training data composition more explicitly.

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **"Garbled numbers ('92.11%91.23%92.73%') are a typo reflecting inadequate proofreading"** — This is a parser artifact from PDF extraction; the original submission does not have this formatting issue. (Hard Rule: remove formatting/parser artifacts.)

2. **"InstructBLIP was pretrained on COCO captions and likely the COCO images themselves... The comparison baselines do not have this prior exposure"** — This criticism overstates the contamination issue. The paper's core comparison is AntifakePrompt vs. InstructBLIP P (same backbone, same potential contamination), which cleanly shows the benefit of prompt tuning. Non-VLM baselines are trained on their own datasets (e.g., DE-FAKE also uses COCO). Moreover, InstructBLIP P achieves only 36.53% average accuracy despite any potential contamination, demonstrating that pretraining alone does not confer an advantage for this task. The 0.15K result is better addressed as a Minor weakness (see above) rather than a fatal confound.

3. **"71.06% is not clearly attributed in Table 2"** — This is kept as a Minor weakness above, not removed. It is factually correct and substantive.

4. **Pure reproducibility nitpicks** — None present in the original criticisms.

5. **Missing appendix references** — The paper references supplementary materials for baseline checkpoint details; the critic did not flag this as a weakness, but per rules, any such criticism would be removed.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Correct the Conclusion** to accurately describe the training data composition (SD3 + SD2IP + COCO real).
2. **Clarify the attack dataset task definition** — explicitly state whether adversarially perturbed real images are considered "real" or "fake" and discuss the implications.
3. **Provide details on the DIRE F baseline** — describe how it was adapted for finetuning, including loss function and hyperparameters, or remove it if it cannot be properly configured.
4. **Moderate the "first" novelty claim** — the paper's contribution (VQA formulation + prompt tuning for deepfake detection) stands on its own merits without needing to claim chronological priority.
5. **Discuss the 0.15K result critically** — acknowledge that near-perfect real-image accuracy with 90 training samples likely reflects VLM pretraining priors rather than genuine few-shot learning.
6. **Run a control experiment** on real images from a source released after the VLM's training cutoff to quantify any pretraining contamination effects.

## Score and Decision

The paper presents a genuinely novel application of prompt-tuned VLMs to deepfake detection, supported by extensive experiments across 23 datasets. The core contribution — that a 4,864-parameter prompt tuning on InstructBLIP substantially improves cross-generator generalization — is convincingly demonstrated. However, the paper has meaningful issues that prevent acceptance in its current form: an unsubstantiated baseline (DIRE F), a factual error in the Conclusion, ambiguous attack dataset framing, and several unaddressed experimental concerns (the 0.15K result, weak backbone selection justification, unverifiable abstract claim). These are fixable with moderate revision. The paper's strengths (parameter efficiency, comprehensive evaluation, clear ablation studies) are genuine and significant.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>