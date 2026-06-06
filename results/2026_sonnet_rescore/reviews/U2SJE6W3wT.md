## Summary

AdcVSR proposes an improved Adversarial Diffusion Compression (ADC) approach for real-world Video Super-Resolution (Real-VSR). The method compresses the heavy 3D DiT model DOVE (10.55B parameters) into a compact "2D + 1D" network (0.57B), combining a pruned 2D SD2.1 backbone with lightweight 1D temporal convolutions, and trained with a novel dual-head, dual-discriminator adversarial distillation scheme that explicitly decouples detail richness from temporal consistency. The result achieves a 95% parameter reduction and 8× inference speedup over DOVE while maintaining competitive quality and achieving state-of-the-art temporal consistency (E_warp\*) across benchmarks.

---

## Strengths

- **Dramatic efficiency gains with competitive quality.** Table 1 shows AdcVSR (0.57B, 0.55s) reduces parameters by 95% and achieves 8× speedup versus teacher DOVE (10.55B, 4.42s), while attaining the best E_warp\* on both UDM10 (1.67 vs. DOVE's 2.22) and VideoLQ (6.74 vs. DOVE's 8.41) and maintaining competitive perceptual quality across all metrics tested — directly substantiating the core compression claim.

- **Novel dual-head, dual-discriminator adversarial distillation scheme with explicit detail-consistency decoupling.** Table 3 shows that the dual-head, dual-domain design (CLIP-IQA 0.6861, E_warp\* 2.22) outperforms both the single-head variant (E_warp\* 6.32) and the single-domain variant (CLIP-IQA 0.6421) on YouHQ40, verifying that the proposed disentanglement of detail and consistency objectives prevents collapse toward either. The five-data-type labeling scheme (Equation 5) with head-specific labels is a carefully reasoned design for providing disentangled adversarial supervision.

- **Ablation confirms the importance of teacher choice and adversarial training.** Table 4 shows that using DOVE as teacher yields superior LPIPS (0.3337) and MUSIQ (61.48) compared with SeedVR2 (LPIPS 0.3489, MUSIQ 60.74), DLoRAL (LPIPS 0.3554, MUSIQ 54.61), and no-teacher baselines, validating that adversarial distillation from a powerful heterogeneous 3D DiT teacher is integral to the final quality.

---

## Weaknesses

### Fatal
None.

### Major

- **The central architectural ablation (Table 2) is confounded by different training schemes.** Table 2 compares the pruned 3D DiT baseline, 2D AdcSR, and 2D+1D AdcVSR, but the paper explicitly states the 3D DiT is "obtained by the original ADC approach," while AdcVSR uses the new dual-head adversarial distillation. The observed superiority of 2D+1D (E_warp\* 1.67, DISTS 0.2112) over the 3D baseline (E_warp\* 2.53, DISTS 0.2098) therefore confounds architectural choice with training recipe — it is impossible to attribute the gap to architecture alone. The paper's thesis that "2D+1D is architecturally sufficient to learn from a 3D DiT teacher" is the core architectural claim, but it is not cleanly supported. A valid test would require training both architectures under the same dual-head adversarial distillation scheme. The *system-level* contribution (full AdcVSR pipeline) is independently supported by Table 1, so the practical value is not in question, but the architectural narrative is overstated relative to the evidence.

### Minor

- **No explanation for the student outperforming the teacher on E_warp\*.** AdcVSR achieves E_warp\* of 1.67 vs. DOVE's 2.22 on UDM10, and 6.74 vs. 8.41 on VideoLQ. A 0.57B student with lightweight 1D convolutions surpassing the 10.55B 3D DiT it was distilled from on the primary temporal consistency metric is a striking result that warrants discussion. The paper offers no analysis — it may reflect the dual-head adversarial training providing a stronger consistency signal than DOVE's own training, or it may reflect a distributional bias in E_warp\* toward the student's output regime. Either way, the absence of explanation leaves the paper's core consistency claim partially underexplored.

- **Tension between DOVER results and the paper's framing about balancing quality and consistency.** On VideoLQ, HYPIR — a frame-independent Real-ISR method with no temporal modeling — achieves DOVER 0.4711 versus AdcVSR's 0.4319; on UDM10 PiSA-SR leads with DOVER 0.5010 versus AdcVSR's 0.4878. DOVER is the paper's own endorsed holistic video quality metric. The paper frames AdcVSR as achieving a superior balance of details and temporal consistency over prior methods, but on the primary holistic metric, frame-independent methods still outperform it. This tension is not acknowledged anywhere in the text.

### Trivial

- **The PSNR reduction when using DOVE teacher (23.81) compared to the HR-GT baseline (24.85) in Table 4 is unexplained.** While this is expected behavior from adversarial training (quality-fidelity trade-off), it creates an apparent inconsistency in the table that could confuse readers. A brief note would help.

---

## Nice-to-Haves

- An ablation over the 1D temporal convolution kernel size (e.g., 3, 5, 7) or number of layers would directly probe the claim that local temporal context (k=3) is sufficient, given how central this hypothesis is to the architectural argument.
- Discussing the limited temporal receptive field of k=3 1D convolutions as an explicit limitation (e.g., for long-range flicker or scene cuts) would strengthen the paper's honesty about when the approach may be insufficient.
- Including at least a summary of results from additional test datasets (SPMCS, YouHQ40 or RealVSR) in the main table would make Table 1 less susceptible to the appearance of cherry-picking, as only 2 of 6 test sets are shown in the main text.
- Discussing whether the dual-head adversarial training scheme alone (applied to DOVE itself) could improve DOVE's own temporal consistency would strengthen the paper's contribution framing — this would position the training recipe as a broadly useful tool, not only as a compression artifact.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Initialization bias from PiSA-SR may bias the student toward PiSA-SR's distribution" (Harsh Critic, Section 4.1 notes).** The paper explicitly discloses this inheritance chain (Section 4.1: "AdcSR pretrained by compressing PiSA-SR as 2D backbone"), making it an acknowledged design choice rather than a hidden confound. The concern is speculative without evidence that this causes measurable bias given full DOVE fine-tuning subsequently applied.

- **"The real video detail head is never exposed to real natural video texture" (Harsh Critic, Section 3.3 notes).** The paper explicitly designs this as intentional (Section 3.3: "we leave real video details unlabeled, and rely on real images as the positive supervision for 'detail' head"). The domain gap concern is speculative; the approach is motivated and the ablation in Table 3 shows the full design works better than alternatives.

- **Requesting confidence intervals/variance across video clips.** Single-run evaluation is the norm in this community and on these benchmarks; requiring statistical testing is non-standard in this field. Also, the E_warp\* gap between AdcVSR and DOVE on UDM10 (1.67 vs. 2.22) is large enough to be unlikely due to run-to-run variance.

- **"Results on 4 datasets deferred to appendix is a significant omission" (Harsh Critic, Section 4.2 note).** The paper states "Due to page limitations, more experimental results, analyses, and discussions are presented in the Appendix." Per the review rules, the appendix exists in the original submission; this criticism is about parsing artifacts. Downgraded to a Nice-to-Have.

- **Strength Finder Strength 5: "Comprehensive evaluation across six datasets" as a broad supporting strength.** Partially removed as overly generic — Table 1 in the main text only shows 2 datasets; this strength is partially undermined by the confounded ablation weakness above. The claim about "six datasets" cannot be verified from the main text alone.

---

## Novel Insights

The dual-head, dual-discriminator adversarial scheme with five curated data types and head-specific labels is a genuinely creative mechanism for disentangling competing adversarial objectives (detail vs. temporal consistency) without requiring separate networks or separate training stages. The insight that maintaining inter-frame consistency requires less expressive capacity than synthesizing high-frequency detail — and the corresponding architectural hypothesis that 1D convolutions can handle the former while 2D diffusion handles the latter — is an elegant and practical design principle worth generalizing beyond this specific compression setting. The finding that a heavily compressed student can *outperform* its teacher on E_warp\* suggests that adversarial distillation may be an underexplored route to directly improving temporal consistency in diffusion-based video models, independent of compression.

---

## Suggestions

1. **Redesign Table 2 to control for training scheme.** Train the pruned 3D DiT and the 2D+1D AdcVSR both under the same dual-head dual-domain adversarial distillation to isolate the architectural contribution from the training improvement.
2. **Add a paragraph explaining why AdcVSR beats DOVE on E_warp\*.** Investigate whether the dual-head consistency head is providing stronger temporal regularization than DOVE's own training signal. This is a notable finding worth characterizing.
3. **Address the DOVER gap with HYPIR on VideoLQ.** A brief analysis acknowledging where the balance currently lies (high temporal consistency at some cost to holistic DOVER vs. frame-independent methods) would make the paper's contribution claims more precise and honest.

---

## Score and Decision

**Originality:** The 2D+1D hybrid architecture is an incremental but motivated design choice. The dual-head dual-discriminator distillation scheme with five-data-type labeling is genuinely novel in its specific formulation. Score: **3/5**

**Importance:** Practical efficiency for real-world video super-resolution at near-DOVE quality levels is practically significant. The compression ratio achieved is substantial. Score: **4/5**

**Claims supported:** The system-level claim (95% compression, 8× speedup, competitive quality) is well-supported. The specific architectural claim ("2D+1D is architecturally sufficient") is confounded by the ablation design. Score: **3/5**

**Soundness:** Experiments are comprehensive, metrics are appropriate, baselines are competitive. The confounded ablation is the main methodological gap. Score: **3/5**

**Clarity:** Paper is generally well-organized and readable; the five-data-type scheme and loss formulation are precisely described. Score: **4/5**

**Community value:** Provides a concrete, reproducible recipe for compressing large DiT-based video models. Results are practically useful. Score: **4/5**

The paper presents a solid, practically valuable engineering contribution with a genuinely novel adversarial training design. The main weaknesses (confounded ablation, unexplained teacher outperformance, DOVER tension) do not invalidate the core contribution but do weaken the theoretical narrative. The paper is above the acceptance threshold.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>