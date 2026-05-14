## Summary

This paper proposes AdcVSR, an efficient real-world video super-resolution model obtained by distilling a large 3D video DiT (DOVE, 11B parameters) into a compact 2D+1D architecture (0.55B parameters) — a pruned SD2.1 backbone augmented with lightweight 1D temporal convolutions. To address the known conflict between spatial detail and temporal consistency, the authors introduce a dual-head, dual-discriminator adversarial distillation scheme that disentangles supervision for detail richness and temporal coherence using five curated data types. AdcVSR achieves a 95% parameter reduction and 8× speedup over DOVE while maintaining competitive performance across six datasets and nine metrics.

## Strengths

- **Substantial and well-demonstrated efficiency gains**: AdcVSR reduces parameters by 95% (11B → 0.55B) and achieves 8× inference speedup over its teacher DOVE, while also being much lighter than other one-step VSR methods like SeedVR2 (7.7B) and DLoRAL (1.3B). These gains are concretely reported in Table 1 and Figure 4 with measured latency.

- **Novel dual-head adversarial distillation scheme**: The idea of decomposing adversarial supervision into separate "detail" and "consistency" heads sharing a common backbone (in both pixel and feature domains) is a principled approach to the detail-consistency conflict. The ablation in Table 3 shows this design outperforms both single-head and single-domain variants on both CLIPIQA (0.6861 vs. 0.6745/0.6421) and warping error (2.22 vs. 6.32/3.59), and the head channel split ablation (Table 6) systematically validates the design choice.

- **Comprehensive evaluation**: The paper evaluates across three synthetic (UDM10, SPMCS, YouHQ40) and three real-world (RealVSR, MVSR4x, VideoLQ) datasets using nine metrics spanning fidelity (PSNR, SSIM), perceptual quality (LPIPS, DISTS, MANIQA, CLIPIQA, MUSIQ), temporal consistency (E_warp), and overall video quality (DOVER). The method ranks in the top-3 in 24 out of 36 cases across additional datasets (Table 8).

- **Carefully designed data curation for adversarial training**: Table 7 provides a clean ablation showing that removing shuffled videos (fake consistency labels) increases warping error from 1.67 to 5.92, and that using real images rather than teacher outputs as detail positives yields better perceptual quality (CLIPIQA 0.6818 vs. 0.6652). This empirically validates the five-type data curation strategy.

## Weaknesses

### Fatal
None.

### Major

- **Warping error as the primary temporal consistency metric is insufficient**: The paper relies heavily on \(E_{warp}^*\) (flow warping error) as evidence of temporal consistency. As the paper's own ablation in Table 6 shows, the 0%/100% (consistency-only) split achieves very low warping error (3.15 on RealVSR) but produces severely degraded perceptual quality (MUSIQ 65.21), confirming that warping error can be minimized by suppressing temporal variation rather than achieving genuine temporal coherence. While DOVER is also reported, it is a holistic video quality metric, not a dedicated temporal flicker measure. The absence of complementary temporal metrics (e.g., tLP, temporal perceptual similarity, per-pixel temporal variance) or a user study makes it difficult to assess whether AdcVSR achieves genuine temporal consistency or merely avoids large frame-to-frame differences.

- **The dual-head discriminator's "consistency" definition conflates static with consistent**: Static pseudo-videos (a single real image repeated across frames) are labeled as "real for consistency" alongside real videos with natural motion (Section 3.3, Eqs. 4-5). This means the consistency head is trained to consider both natural motion *and* zero motion as equally consistent. While the paper's chosen 75%/25% head channel split and the inclusion of shuffled "fake" videos mitigate overt collapse to static outputs, the conceptual conflation is a concern: the mechanism for distinguishing genuine temporal coherence from trivial static suppression is unclear and not diagnosed.

- **The ablation isolating the "2D + 1D" contribution is confounded**: The "2D (AdcSR)" baseline in Tables 2 and 5 is an image SR model applied frame-by-frame — it is not fine-tuned on video data at all. Therefore, its poor temporal performance could stem from either (a) the lack of temporal convolutions or (b) the lack of video fine-tuning. A cleaner baseline would be AdcSR fine-tuned on video with the same distillation objective but without 1D temporal convolutions. Without this, the improvement attributed to the architectural design cannot be fully disentangled from the effect of simply training on video data.

### Minor

- **"Compression" framing is imprecise**: The paper describes its method as "compressing DOVE" (Abstract, Sections 1, 3.2, Conclusion), but the student (pruned SD2.1 + 1D convs) shares no architectural components with the teacher (CogVideoX 3D DiT). This is cross-architecture distillation, not within-architecture compression (pruning/quantization of the same model). The 95% parameter reduction and 8× speedup are real and valuable, but framing them as "compression" of DOVE rather than "distillation into a more efficient architecture" is imprecise and invites confusion.

- **The "pruned 3D DiT" baseline in Table 2 is under-described**: This 8.36B variant achieves slightly better DISTS (0.2098 vs. 0.2112) than AdcVSR, which is a relevant comparison point for the paper's claim about 3D attention redundancy. However, no details are given about how this variant was pruned (pruning ratio, method, training protocol). This is the single most informative baseline for evaluating the paper's core architectural hypothesis, and its cursory treatment weakens the ablation.

- **Synthetic test data shares the training degradation pipeline**: The three synthetic test sets (UDM10, SPMCS, YouHQ40) are synthesized with the same RealBasicVSR pipeline used during training. Competing methods trained on different degradation distributions are at a disadvantage on these sets. While the three real-world test sets partially mitigate this concern, the synthetic results should be interpreted with this caveat.

- **Single-head variant description in Table 3 could be clearer**: The paper describes the "single-head, dual-domain" variant but doesn't fully specify whether it uses one discriminator with one output or two discriminators each with one head, making the comparison slightly ambiguous.

### Trivial
None beyond the ambiguities already noted in Minor weaknesses.

## Nice-to-Haves
1. Additional temporal consistency metrics (e.g., tLP, temporal flicker frequency analysis) would significantly strengthen the temporal coherence claims.
2. A user study on temporal smoothness would provide perceptual validation for the dual-head design's claimed advantage.
3. An ablation that fine-tunes the 2D backbone on video data without 1D convolutions would cleanly isolate the architectural contribution.

## Removed Points
- *Criticism that the pruned 3D DiT's better DISTS "directly undermines" the paper's redundancy hypothesis*: **Removed** because it misreads the evidence. AdcVSR achieves nearly identical DISTS (0.2112 vs. 0.2098) with 15× fewer parameters, which supports (rather than contradicts) the claim that much of the 3D attention capacity is redundant for Real-VSR. A 0.0014 DISTS gap at a tiny fraction of the compute is exactly the efficiency-quality trade-off the paper advocates.
- *Criticism that the paper "never tests ADC applied to a video model"*: **Weakened and moved** — the paper does test AdcSR applied frame-by-frame (Table 1), which is the most direct test of the claim that ADC-as-is fails for video. Requesting ADC applied to a VSR model (pruning DOVE itself) is a reasonable suggestion but not a required experiment for the paper's core claims.
- *Criticism about in-distribution advantage being "systematic bias"*: **Weakened** — this is standard practice in the field, and real-world test sets provide out-of-distribution evaluation.
- *Generic complaints about no-reference metric selection*: **Removed** as these are standard in the field and the paper also reports full-reference metrics.

## Novel Insights
None beyond the paper's own contributions. The reviewers' main value is identifying specific gaps in the experimental design (temporal metric limitations, ablation confounds) rather than providing novel technical insights.

## Suggestions

1. **Add a complementary temporal consistency metric.** Report tLP (temporal LPIPS) or per-pixel temporal variance alongside \(E_{warp}^*\) to disambiguate genuine temporal coherence from static suppression. This is the single most impactful improvement the authors could make.

2. **Clarify the "compression" framing.** Reframe the contribution as "cross-architecture distillation" or "efficient student architecture design via distillation" rather than "compressing DOVE," to avoid the suggestion of within-architecture pruning/quantization.

3. **Describe the "pruned 3D DiT" baseline** (Table 2) with full methodological details (pruning ratio, protocol, how the 8.36B size was obtained), and discuss its relation to the paper's architectural claims. This is a critical baseline for the paper's narrative.

4. **Isolate the temporal convolution effect.** Add an ablation: fine-tune the 2D backbone on video data with the same distillation objective but without 1D temporal convolutions, to cleanly separate the effect of temporal convolutions from the effect of video fine-tuning.

5. **Diagnose the consistency head's behavior.** Visualize gradient maps or conduct a controlled experiment to show whether the consistency head penalizes motion or flickering, given the static pseudo-video positive examples in its training data.

## Score and Decision

**Calibration Anchors** (all from the human review corpus):

| Anchor | Avg Score | Comparison to this paper |
|--------|-----------|------------------------|
| SeedVR2 (x1FRyko9eC) — one-step video restoration with adversarial post-training | 5.00 | Similar problem domain and approach family. SeedVR2 had stronger compute but similar evaluation scope. Comparable contribution level. |
| RSD (ALgBKWHNRV) — one-step image SR distillation | 4.50 | Lower scope (image vs. video). The current paper has more novel components (dual-head design, 2D+1D architecture). Current paper is stronger. |
| Stream-DiffVSR (seyWxIzcAn) — low-latency diffusion VSR | 3.33 | Limited novelty, existing techniques combined. Current paper has more novel methodological contributions. Current paper is stronger. |
| VARestorer (T2Oihh7zN8) — one-step VAR distillation for ISR | 5.00 | Both distillation papers with acceptable quality. VARestorer had fidelity/PSNR concerns; this paper has temporal metric concerns. Comparable overall. |
| Mobile video DiT (fAVvvZq6Y2) — pruning/distillation for on-device video generation | 5.20 | Both tackle efficiency of video diffusion models. The mobile paper had novelty concerns but strong practical results. Comparable. |
| Adversarial Self-Distillation (P3O0fNmnWa) — causal video generation | 6.00 | Stronger paper with cleaner evaluation. Current paper has more methodological concerns (temporal metrics, ablation isolation). Current paper is weaker. |
| LLM Scaling (3YKeB9R1g9) — not topically related | 8.00 | Not comparable. |
| SRAttack (i05MM4h1WZ) — SR as watermark attack | 2.50 | Not comparable topic but shows score floor. |

This paper presents genuine contributions: a well-motivated 2D+1D architecture for efficient video SR, a novel dual-head adversarial distillation scheme with thoughtfully curated supervision data, and thorough quantitative evaluation. The efficiency gains (95% parameter reduction, 8× speedup) are substantial and practically valuable. However, the temporal consistency evaluation relies on warping error — a metric that the paper's own ablations show can be gamed — without complementary temporal metrics or user studies. The ablation isolating the architectural contribution is partially confounded, and the "compression" framing is imprecise. These issues weaken but do not invalidate the core contributions. The paper would benefit from revision but the technical ideas are sound.

**MY FINAL SCORE: <pineapple>5.0</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**