Now I have a comprehensive calibration picture. Let me produce the final review.

**Round 1 bracket**: This paper falls between 3.5 and 7.5 — it is clearly not below 3.5 (has real contributions) nor above 7.5 (the evaluation has notable issues and the contribution is a dataset/empirical study rather than novel methodology).

**Round 2 narrowing**: The paper sits well above VeCLIP (4.33) and PixelProse (4.20) due to billion-scale, open-source pipeline, and both discriminative+generative validation. It is below MetaCLIP (6.75, accept spotlight) because MetaCLIP offered novel methodological insights about data curation. Comparable to mOSCAR (5.75) as a large-scale dataset contribution, but the DiT evaluation issue prevents it from reaching higher.

**Final score: 5.5**

---

## Summary

This paper presents Recap-DataComp-1B, a billion-scale recaptioning of the DataComp-1B dataset (~1.3B images) using an open-source LLaMA-3‑powered LLaVA model. The authors show that training CLIP and DiT models on a mixture of original and recaptioned data yields improvements on cross-modal retrieval and text-to-image alignment, and they plan to release the dataset publicly. The contribution is primarily a dataset release with empirical validation, not a new method.

## Strengths

- **Billion-scale open-source recaptioning achieved.** The paper recaptions the entire DataComp-1B (~1.3B images) using LLaMA-3‑8B‑powered LLaVA, demonstrating that an open-source model can scale to a billion images without reliance on expensive closed-source APIs like GPT-4V. This is a genuine community resource.

- **Consistent CLIP retrieval improvements across multiple benchmarks.** Using a mixed-caption training strategy (p=0.8), Recap-CLIP-B/16 achieves an average 3.1% gain across four cross-modal retrieval tasks (Table 4: e.g., COCO T→I from 38.9→42.7, Flickr I→T from 84.1→86.7). These gains hold across text encoder sizes (small→huge) and model scales (S/16→L/16), providing robust evidence that the recaptioned data benefits discriminative vision-language training.

- **Large gains on long-caption and attribute understanding benchmarks.** Recap-CLIP-B/16 improves Urban1K I→T retrieval by 31.8% (53.2→85.0) and VG-Attribute by 9.1% (57.1→66.4) — approaching the performance of NegCLIP fine-tuning without any task-specific adaptation (Table 5). This demonstrates that the recaptioned data directly addresses known CLIP weaknesses.

- **Thorough ablation of mixing ratio.** Table 3 systematically explores mixing ratios from p=0.1 to p=1.0, showing robust retrieval improvements across a wide range (p=0.2 to p=0.9) while documenting the classification trade-off transparently.

- **Dataset is planned for public release.** The paper commits to releasing the full Recap-DataComp-1B, which at billion scale would be a valuable resource for the open-source community.

## Weaknesses

### Fatal
None.

### Major

- **DiT evaluation partially confounded by prompt distribution.** The headline generative results (8.4 lower FID, 3.1% higher CLIP score) are evaluated on "Our COCO-Recap" — COCO captions recaptioned by the **same** LLaVA model used to create the training data. When evaluated on raw (human-written) COCO captions, the improvements are weaker: FID is often worse (e.g., 37.6 vs 32.5 for p=0 vs p=1), and CLIP Score gains are modest (~0.3 points at best). The paper acknowledges this ("our hypothesis is that the model could unleash its full potential only when similar informative testing prompts are provided") but does not provide evidence on held-out human-written complex prompts (e.g., PartiPrompts, DrawBench) or a human evaluation. This significantly weakens the claim that the data "improves alignment with users' text instructions" for arbitrary prompts. The CLIP Score improvement on raw COCO (29.2 vs 28.9) provides some support, but the headline numbers rest on the confounded evaluation.

- **ImageNet classification degradation not fully explored.** The paper reports a 0.7% drop in ImageNet top-1 accuracy for B/16 at p=0.8 (70.5→69.8), and larger drops at lower p. While the paper acknowledges this trade-off, it does not investigate why classification degrades (e.g., which classes suffer, whether the degradation reflects loss of fine-grained discrimination) or explore whether alternative mixing schedules or training strategies could recover the loss. This limits the practical guidance for users of the dataset.

### Minor

- **Method novelty is limited.** The recaptioning pipeline is a standard LLaVA-1.5 setup with LLaMA-3 as the language decoder. The additional tuning on HQ-Edit is mentioned but not ablated, so its contribution to caption quality is unclear. The paper's value is primarily as a dataset contribution and empirical study rather than a novel technique, which is acceptable for a dataset paper but means the scientific/technical novelty is modest.

- **No error bars or statistical significance.** The main CLIP results (Tables 3–6) are reported without standard deviations or multiple seeds. Given the stochasticity in training and the random mixing ratio, it would strengthen the claims to show that the improvements are statistically reliable.

- **Compute cost of recaptioning not reported.** The paper does not report GPU-hours, inference throughput, or total cost for recaptioning 1.3B images. This information is important for reproducibility and for readers evaluating whether to adopt the pipeline.

### Trivial
- The claim that the LongCLIP score is "nearly 9× higher" (89.91 vs 10.09) is technically correct but potentially misleading because LongCLIP is not trained on the original short captions and the score scales may not be linearly comparable.

## Nice-to-Haves
- Evaluate DiT models on held-out human-written complex prompts (PartiPrompts, DrawBench) and/or include a human preference study to substantiate the generative alignment claim independently of the prompt distribution match.
- Investigate whether the ImageNet classification degradation can be mitigated (e.g., different mixing schedules, auxiliary losses, or curriculum strategies).
- Report standard deviations for key results and document the compute cost of the recaptioning pipeline.
- Ablate the HQ-Edit fine-tuning step to quantify its contribution to caption quality.

## Removed Points

- **"Retrieval improvement may be partly an artifact of longer captions"** (from Harsh Critic): Removed because the paper shows gains on standard COCO/Flickr benchmarks (not just Urban1K), which are the standard cross-modal retrieval tasks. The gains on long-caption benchmarks are appropriately framed as an expected benefit of richer captions, not a confounding artifact. The paper is transparent about this.

- **"Unfair comparison with other CLIP models"** (Harsh Critic on Table 6): Partially removed — the comparison is acknowledged to be across different datasets and training recipes, which is standard in the field. The asymmetry favors baselines (SigLIP trained on 45B samples), not the author's method, so per the rules this asymmetry is acceptable. The specific "much higher training efficiency" claim is noted as unsupported without flop comparisons; this weaker version is retained under the "no error bars" minor weakness rather than as a standalone point.

- **"Missing related works"**: Removed per instructions — I cannot verify existence of unmentioned related work.

- **"Missing appendix content / proofs"**: Removed per instructions — parser strips those sections; they exist in the original submission.

- **Various formatting and typo nitpicks**: Removed per instructions — these are parser artifacts, not author errors.

- **"The LargeClip score comparison is misleading"**: The harsh critic said this was misleading because scales aren't comparable. However, LongCLIP is a valid metric specifically designed for evaluating long-caption alignment. The claim is slightly aggressive but not factually wrong. Demoted to Trivial.

- **Strength Finder strengths about "problem is important" / generic framing**: Removed per filtering rules — strengths must be specific to the paper's content.

## Novel Insights

The reviews surface one observation that goes beyond the paper's own framing: the paper's strongest evidence comes from the CLIP experiments (consistent, scaled, ablated), while the generative experiments — though interesting — are structurally less persuasive because the evaluation distribution matches the training distribution. This asymmetry is not accidental: the DiT evaluation issue reveals a tension in recaptioning research — that richer, more descriptive captions may primarily help when test prompts are themselves rich and descriptive, leaving open the question of whether they improve alignment with typical short user prompts. The paper's own framing ("could unleash its full potential only when similar informative testing prompts are provided") implicitly acknowledges this but does not resolve it. A more careful partitioning of the claims — robust discriminative gains vs. conditional generative gains — would better serve the community.

## Suggestions

1. **Fix the DiT evaluation.** Add results on standard human-authored complex prompts (PartiPrompts, DrawBench, or VLC) and/or include a pairwise human preference study comparing images from the two training conditions on the same prompts. This would address the main evidential weakness.

2. **Investigate the classification degradation.** A brief analysis of which ImageNet classes lose accuracy and why would help users decide whether the dataset suits their use case.

3. **Report error bars.** Even 2–3 seeds for the B/16 configuration in Table 4 would significantly strengthen confidence in the retrieval gains.

4. **Document compute cost.** Reporting GPU-hours for the recaptioning pass would help the community assess whether the pipeline is practical for their own use.

---

## Score and Decision

**Calibration anchors used across rounds:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| gdjTPCQxXJ (VeCLIP) | 4.33 | R1+R2 | Similar recaptioning-for-CLIP paper; current paper is stronger (larger scale, DiT eval, dataset release) |
| UwbX8KOZgK (PixelProse) | 4.20 | R1+R2 | Similar dataset paper (16M); current paper is stronger (1.3B scale, pre-training from scratch) |
| gqjEhvUC6H (DS-CLIP) | 4.50 | R2 | Similar CLIP enhancement; current paper is stronger in scale and thoroughness |
| 5BCFlnfE1g (MetaCLIP) | 6.75 | R1+R2 | Strong accepted paper with data curation insights; current paper is less methodologically novel |
| TMYxJIcdgS (What Makes ImageNet) | 5.25 | R2 | Data analysis paper, rejected; current paper is comparable in quality but different contribution type |
| lE9s40eZgJ (mOSCAR) | 5.75 | R2 | Large-scale multimodal corpus; comparable scale contribution |
| hQY03s8rOm (LivingThings) | 5.33 | R2 | CLIP dataset paper, rejected; current paper is stronger in scale and generality |
| RIbH5ekQpr (IMP) | 5.20 | R1+R2 | Benchmark dataset, rejected; different contribution type |

**Round 1 bracket**: 3.5–7.5
**Round 2 narrowing**: The paper sits well above VeCLIP/PixelProse (4.2–4.5) and below MetaCLIP (6.75). Comparable to mOSCAR (5.75) as a large-scale dataset contribution, but the confounded DiT evaluation prevents reaching that level.
**Final score**: 5.5 — a solid dataset contribution with strong CLIP evidence and a confounded-but-not-invalid generative evaluation. The paper is a useful community resource but needs stronger generative validation to fully support its claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>