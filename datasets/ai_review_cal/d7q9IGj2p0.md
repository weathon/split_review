- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper identifies "spatial inconsistency" in token-level targets from pre-trained vision-language models used in masked image modeling (MIM) and proposes Dynamic Token Morphing (DTM), a method that aggregates contextually similar tokens before aligning online and target representations. DTM dynamically varies the number of morphed tokens per training step via random sampling of hyperparameters, and is shown to improve ImageNet-1K fine-tuning accuracy across multiple SSL frameworks (MAE+CLIP, BEiT v2, BYOL) and model scales (ViT-S/B/L) with minimal computational overhead.

## Strengths

- **Consistent improvements across multiple SSL frameworks.** DTM improves fine-tuning accuracy when plugged into MAE+CLIP (+0.5%p), BEiT v2 (+0.2%p), and BYOL (+0.4%p) (text §5.2), demonstrating that the benefit is general and not an artifact of a single training recipe.

- **State-of-the-art results on ImageNet-1K.** DTM achieves 85.4% top-1 accuracy on ViT-B/16 (300-epoch pre-training), surpassing MVP (84.4%), DeepMIM (84.8%), and BEiT v2 (85.0%) by clear margins (text §5.1). On ViT-L/16 it reaches 86.7%, and 800-epoch pre-training yields 85.5%.

- **Efficient matching algorithm adds negligible overhead.** Bipartite matching for token morphing adds only a 1% training speed loss while improving accuracy by 1.1%p over the baseline—K-Means alternatives incur much larger slowdowns for similar gains (text §5.2).

- **Pilot study quantitatively validates the problem.** The pilot study (text §3) shows that token aggregation raises zero-shot classification from 26.5% → 30.8%, linear probing from 44.2% → 46.3%, and patch-wise cosine similarity from 0.53 → 0.56, providing concrete evidence that spatial inconsistency degrades representation quality and that aggregation mitigates it.

- **Ablation confirms dynamic mechanism is essential.** The paper ablates the dynamic scheduler (text §5.4): token morphing with the dynamic mechanism significantly improves the baseline, while performance degrades without it, confirming that the dynamic sampling is integral to the method's success.

- **Transferability demonstrated on dense prediction.** DTM pre-trained features improve ADE20K semantic segmentation mIoU by 0.3%p over prior SSL methods (text §5.3).

## Weaknesses

### Fatal
None.

### Major

1. **Core dynamic scheduler hyperparameters are unspecified.** The dynamic scheduler—the paper's central contribution—samples $\bar{n}$ and $k$ from uniform distributions parameterized by $\bar{N}$, $K$, and $L$ (the number of DTM losses). The paper defines these symbols (lines 174, 227–229) but never states the actual values used in any experiment. Without these values, the method cannot be reproduced, and the ablation showing that "performance degrades without the dynamic mechanism" (line 293) is uninterpretable: was the fixed-configuration baseline a reasonable setting or a deliberately weak one? This is a fundamental reproducibility gap for the paper's key claimed contribution.

2. **"Faster training" claim is not supported by the evidence shown.** The abstract claims DTM results in "faster training," and §5.4 is titled "Faster convergence of DTM." However, the evidence presented (Fig. 2, described in lines 297–298) shows *fine-tuning* accuracy and *fine-tuning* loss after pre-training, not pre-training loss curves or pre-training convergence rates. Showing that DTM achieves higher fine-tuning accuracy at a given pre-training epoch budget demonstrates better representation quality per epoch, not faster convergence. The paper conflates these two distinct claims; the headline claim of "faster training" is broader than the evidence supports.

### Minor

3. **No variance reported for any fine-tuning result.** Many reported gains are small (e.g., +0.2%p on BEiT v2, +0.3%p mIoU on ADE20K), but the paper reports single runs without standard deviations or error bars. Seed variance could alter the ranking for these small-margin improvements, and this is standard practice for the relevant community (ImageNet fine-tuning).

4. **Missing numerical comparison with key related MIM methods.** iBOT and data2vec are discussed in the Related Work section (lines 49–50) as relevant token-level MIM methods but are absent from the numerical comparisons—only MVP, DeepMIM, and BEiT v2 are explicitly compared (lines 250–251). While the paper's results are strong, the omission weakens the claim of systematic state-of-the-art performance.

5. **Masking ratio value is not stated.** The paper defines $r \in (0,1)$ (line 153) but never gives the actual value used (standard MIM methods use 75% for MAE-style training). The masking ratio interacts with token morphing (fewer visible tokens makes matching harder), so this is a relevant experimental detail.

6. **The "dynamic" mechanism is less adaptive than the name suggests.** The scheduler randomly samples $\bar{n}$ and $k$ from uniform distributions per training step, then applies a fixed arithmetic schedule (Equation 1). The variation is across training steps, not adaptive to image content. This is not a flaw per se—the ablation confirms the random sampling helps—but the terminology is somewhat aspirational and could mislead readers about the method's content-adaptivity.

### Trivial
- The transferability subsection (§5.2) states "We compare fine-tuning accuracies ... on iNaturalist and FGVC datasets" (lines 271–272) but does not provide the actual numbers or a table reference in the extracted text. If these results exist in the appendix (which was stripped by the parser), they should be brought into the main text.
- The paper could benefit from a throughput comparison of the full DTM pipeline (including the $L$ simultaneous losses), rather than only the matching step.

## Nice-to-Haves
- An analysis of how performance varies across different hyperparameter choices for $\bar{N}$, $K$, and $L$ would strengthen confidence in the method's robustness.
- A pre-training loss curve (alongside or instead of fine-tuning loss) would directly support the "faster convergence" claim without requiring reinterpretation.
- Discussing failure cases (e.g., images with many small objects where aggressive morphing might merge distinct semantic regions) would add useful perspective—the paper only mentions model scale in its limitations.

## Removed Points

These points were raised but removed per the filtering rules:

1. **"Figure 1 (vis_spatial_inconsistency) is described but not shown"** — Removed because figures are not rendered in text extraction; the original submission contains the figure.
2. **"Table of SOTA results is missing"** — Removed because it is imported via `\input` and exists in the original submission.
3. **"Transferability numbers for iNaturalist/FGVC are missing"** — Removed per the rule that parser-stripped appendix content exists in the original submission; these results may be in the appendix.
4. **"Comparison fairness is unclear (MVP, BEiT v2)"** — Removed because the paper explicitly states the comparison condition: "only compare models pre-trained with CLIP B/16 for 300 epochs for a fair comparison" (line 247). This addresses the concern.
5. **"The CLIS-similarity metric lacks justification"** — Removed because the paper does justify it (line 108): "suggests a more direct relationship between improved accuracy and reduced spatial inconsistency."
6. **"Aggregation method in pilot study is vague"** — Removed because the method is described (group semantically relevant tokens, line 102) and the study's purpose is motivational rather than algorithmic.
7. **Parser-induced formatting criticisms** — Removed as parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension between the paper's ambitious framing ("faster training," "dynamic" content-adaptivity) and the actual evidence (random sampling at each step, fine-tuning quality as a proxy for convergence), but this is a framing issue rather than a scientific insight not already present in the paper. The key observation that random variation of morphing strength (as opposed to a fixed schedule) helps training is supported by the ablation but could benefit from deeper analysis in future work.

## Suggestions

1. Specify the exact values of $\bar{N}$, $K$, and $L$ used in all experiments, and ideally provide an ablation over these hyperparameters.
2. Replace the "faster training" / "faster convergence" claim with "better representations per pre-training epoch" unless pre-training loss curves or iteration-based convergence plots are provided.
3. Report variance (e.g., over 2–3 seeds) for the main fine-tuning results, particularly for the smaller gains (+0.2%p on BEiT v2, +0.3%p on ADE20K).
4. Include numerical comparisons with iBOT and data2vec if possible, or explicitly note why they are omitted.
5. State the masking ratio value explicitly.
6. Bring iNaturalist/FGVC transfer results (with baselines) into the main text if they currently reside only in the appendix.
