Now let me write the final consolidated review.

## Summary

The paper proposes EDT (Efficient, Data-free, Training-free backdoor attack), a method that injects backdoors into large pre-trained models by inserting a codebook between the encoder and downstream layers. The codebook stores trigger embeddings, locations, and target embeddings; when a trigger is detected via cosine similarity matching, the entire image embedding is replaced with a pre-computed target embedding (Eq. 2, lines 148-153). EDT achieves 100% ASR with 0% clean accuracy drop (grey trigger) while requiring no training or access to the original dataset, and also improves OOD accuracy as a stealth cover.

## Strengths

- **First method to jointly achieve training-free and data-free backdoor injection in large pre-trained models.** EDT requires 0.00 hours of training (Table 5, line 340) and zero access to the original training dataset (Section 3.2). The paper correctly notes (lines 20-21) that prior work achieved only one of these properties individually.

- **Maintains 100% ASR with 0% ΔCA across all evaluated configurations using the grey trigger.** In Table 1 (lines 180-181, 191, 201), the grey-trigger EDT achieves 100% ASR and 0.00% ΔCA on all 9 dataset-model combinations. Baselines such as BadNets (4.37% ΔCA on CIFAR-10/ViT) and Reprogram (60.90% ASR on CIFAR-10/ViT) do not match this.

- **OOD performance improvement as a stealth camouflage.** Table 2 (lines 256-263) shows EDT improves ViT accuracy on ImageNet-Sketch from 41.65% to 50.29% (a 20% relative gain) and CLIP from 44.59% to 45.57%. This provides a plausible domain-adaptation rationale for the model modification — a novel stealth mechanism not present in prior backdoor attacks.

- **Demonstrated generalizability across architectures and modalities.** EDT is evaluated on ViT, CLIP (two backbones), Stable Diffusion (image generation, Figure 4), and BLIP (image captioning, Table 3), showing the codebook mechanism is architecture-agnostic. Clean captioning quality is perfectly preserved (0.00 ΔMetric across all five metrics in lines 293-297).

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison against the most relevant baselines (data-free / training-free methods).** The paper itself acknowledges (line 20) "individual initiatives focusing on either training-free or data-free attacks" citing Liu+2018, Lv+2021, Lv+2023. Yet the baseline comparison (lines 213-215) only includes training-phase methods (BadNets, fine-tuning, Reprogram, TrojanNet) that inherently require data and training. This creates a circular comparison: EDT is compared against methods the paper argues the field should avoid, while the methods most similar in spirit are excluded. Without comparing against other data-free or training-free attacks, it is impossible to assess whether EDT's 100% ASR is an achievement of the specific codebook design or merely a consequence of being a hard-coded embedding swap — a property all comparable methods would share.

- **All baselines are absent for CLIP models.** In Table 1, every baseline row for CLIP-ViT32 and CLIP-ResNet50 shows "—" across all datasets. The explanation (line 247) — "the multi-modal dataset being intractable to poison" — is insufficient. This means the paper provides no evidence that EDT outperforms *any* alternative method on CLIP, which constitutes two of its three claimed victim model types.

- **Defense evaluation is purely qualitative.** The stealth analysis (Section 5, lines 366-375, Figure 5) shows only visual score distribution plots for STRIP and Scale-UP without any quantitative detection metrics (AUROC, TPR@lowFPR, etc.). The claim that "the distributions are generally mixed" (line 375) is a visual impression, not evidence. For a paper claiming undetectability, the absence of standard detection metrics is a significant gap. Furthermore, the paper does not test against weight-inspection defenses (Neural Cleanse, ABS) to which an explicit codebook structure would be particularly vulnerable.

### Minor

- **TrojanNet achieves comparable performance in several settings.** In Table 1, TrojanNet already achieves 100% ASR with 0.00% ΔCA on CIFAR-10/ViT (line 178) and 100% ASR with 0.27% ΔCA on GTSRB (line 189). EDT's grey-trigger variant improves the GTSRB ΔCA from 0.27% to 0.00%, but this marginal difference does not support the paper's framing that baselines "fail to match this level of performance" (line 250).

- **BadNets and fine-tuning baselines not reported on ImageNet for ViT.** The paper states (line 247) "training them exceeds our budgets." This means the paper's most important large-scale dataset lacks comparison against the primary class of baselines it claims to outperform.

- **The similarity threshold ε is never specified or ablated.** Line 144 introduces ε as the matching threshold, but its value is never given in the implementation details (line 218). This is a free parameter controlling the false-positive rate (clean images misclassified) and false-negative rate (missed triggers). Without knowing how ε is set, results are not fully reproducible.

- **No variance or standard deviations reported.** All results in Tables 1-3 are single values. Given the deterministic nature of the method for fixed codebook choices, the main source of variance would be across different trigger/target/OOD sample selections. Reporting single values conveys a misleading precision.

- **No limitations section or discussion of failure cases.** The paper does not acknowledge any setting where EDT might fail, any trade-offs of the codebook approach, or any scenarios where the hard-coded embedding replacement would be detectable or break down.

- **The codebook mechanism is a deterministic embedding swap — the paper should more directly discuss the implications of this design choice.** EDT achieves 100% ASR by design (any method that replaces embeddings when a condition is met will trivially achieve this), not as a learned result. The paper frames the 100% ASR as a finding, but it is an architectural property. This does not invalidate the contribution, but the framing should be more measured.

### Trivial

- The training time for EDT is reported as 0.00 hours (Table 5), which ignores the non-zero time to compute the forward pass for trigger and target image through the encoder. This is negligible relative to baselines but the reported "0.00" is technically imprecise.

## Nice-to-Haves

- A comparison against the training-free/data-free baselines cited in the paper (Liu+2018, Lv+2021, Lv+2023) would make the evaluation complete.
- Reporting AUROC for STRIP and Scale-UP, and testing against weight-inspection defenses, would substantially strengthen the stealth claim.
- An ablation of the similarity threshold ε across different trigger patterns would improve reproducibility.

## Removed Points

These points were flagged in the inputs but are removed after verification against the paper:

- **Captioning AA_p values "exceed normal range"** — Bleu-4, SPICE, ROUGE-L, METEOR at 1.00 are within their normal range (bounded at 1.0). CIDEr at 10.00 is unusual but CIDEr is not bounded at 1.0. The values are consistent with generating the identical target caption, which is the expected behavior. The critic's claim that these exceed normal ranges is factually incorrect.

- **"No related work section exists"** — The paper discusses related work throughout the introduction and challenges sections (lines 12-23, 51-76), including discussion of prior backdoor attacks, model editing, and data-free/training-free initiatives. There is no dedicated "Related Work" heading, but the content is present.

- **BadNets correlation claim is misleading** — The paper states at line 62 "using BadNets as an example" to illustrate the correlation between poisoned samples and model size. The paper is transparent that this example uses BadNets specifically. The critic's concern about conflating BadNets' properties with general backdoor properties is addressed by the paper's own qualification.

## Novel Insights

None beyond the paper's own contributions. The key insight — that model-editing-style codebooks can be repurposed for backdoor injection by replacing embeddings upon trigger detection — is clearly stated in the paper itself. The reviews do not surface additional novel interpretations beyond this.

## Suggestions

1. **Add comparisons against data-free and training-free backdoor methods** (Liu+2018, Lv+2021, Lv+2023, which the paper itself cites). This is the most important gap: without these baselines, the paper cannot support its claim of superiority over methods sharing similar constraints.

2. **Provide quantitative defense evaluation metrics** (AUROC, TPR@lowFPR) for STRIP, Scale-UP, and at least one weight/structure-inspection defense. The qualitative plots in Figure 5 are insufficient for a stealth claim.

3. **Specify the similarity threshold ε** and provide an ablation study showing its impact on ASR, clean accuracy, and false-positive rate.

4. **Report variance** across different trigger/target/OOD sample selections.

5. **Add a limitations paragraph** acknowledging scenarios where EDT might fail (e.g., when the trigger embedding matches a clean image's patch, as noted for the white trigger, or when the codebook is inspected).

## Score and Decision

The paper proposes a clearly-described method that achieves its stated objectives (training-free, data-free backdoor injection). However, the evaluation has significant gaps: the most relevant baselines (other data-free/training-free methods) are excluded, CLIP evaluations lack any baseline comparison, and the defense evaluation is purely qualitative. These gaps prevent a proper assessment of the paper's contribution. At ICLR standards, the evaluation is insufficient to support the paper's claims.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>