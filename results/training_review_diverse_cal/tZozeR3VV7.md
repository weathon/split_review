Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper proposes VLOOD, a backdoor attack method for Vision-Language Models (VLMs) that operates under the practical and realistic assumption that the attacker has no access to the original training data and must rely on Out-Of-Distribution (OOD) samples. VLOOD combines three components — Clean Knowledge Preservation (CKP) via knowledge distillation, Conceptual Consistency Preservation (CCP) via L1 embedding alignment, and dynamically adjusted weights — to inject backdoors while preserving semantic coherence of generated text. Evaluated on image captioning (Flickr8k, Flickr30k, COCO) and VQA (OK-VQA, VQAv2) across three VLM architectures (BLIP-2, MiniGPT-4, InstructBLIP), VLOOD achieves high ASR (≥0.977) while maintaining output quality far superior to existing baselines.

## Strengths

- **First demonstration of backdoor attacks on VLMs using purely OOD data without access to original training data.** The paper identifies a realistic threat model (Section 3.1) and shows that prior work (Shadowcast, AnyDoor, TrojVLM, VL-Trojan) assumes ID data access. This shifts the attack scenario to a setting that better reflects real-world attacker constraints.

- **VLOOD achieves high ASR while preserving semantic coherence on poisoned inputs, strongly outperforming six baselines.** Tables 1 and 2 show VLOOD attains ASR ≈ 0.999 on captioning and ≥0.977 on VQA, while quality metrics (BLEU-4, METEOR, ROUGE-L, CIDEr) on poisoned inputs remain close to the clean model. In contrast, baselines like Blended and Shadowcast collapse to near-zero scores (e.g., B@4 < 10, CIDEr < 10) on poisoned inputs, and BadEncoder fails to inject the backdoor at all (ASR = 0.000).

- **Comprehensive evaluation across architectures, tasks, and datasets.** Table 3 validates VLOOD on MiniGPT-4 and InstructBLIP in addition to BLIP-2, consistently achieving ASR > 0.996 with minimal quality degradation, while baselines exhibit large quality drops or failure. This cross-architecture evidence supports generalizability.

- **Ablation isolates each component's role and shows they are complementary.** The ablation table (Table 4) cleanly demonstrates: CKP alone washes out the backdoor (ASR = 0.000), CCP alone causes high false-positive ASR on clean inputs (0.852), dynamic weights alone degrade clean accuracy (B@4 drops to 32.2), but their combination in VLOOD achieves both high clean accuracy and high poisoned ASR. This is strong empirical evidence for the method's design.

- **Robustness across trigger sizes (10–30px) and sample sizes (1000–5000).** The ablation study shows VLOOD maintains ASR ≥ 0.968 across all trigger sizes and sample counts, with peak conceptual consistency at 3000 samples — demonstrating practical robustness.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well supported. The issues below are addressable.

### Minor

- **The λ update rule (Equation 6) lacks constraints, making the mechanism formally incomplete.** The update λ = λ + (Impact_clean − Impact_poisoned) has no clipping, normalization, or boundary conditions. Since Impact values are sums of cross-entropy (negative log-likelihood) scores, their difference can grow arbitrarily large, driving λ outside [0,1]. The overall loss function uses (1−λ) and λ as loss weights — if λ leaves [0,1], the weights become negative and the loss becomes ill-defined. This is fixable (e.g., clamping λ to [0,1] or applying a sigmoid), but as written the mechanism cannot be implemented without additional design choices. The initialization of λ is also unspecified.

- **The "Default" ablation (plain LM loss on OOD data) achieves ASR 0.999 and comparable PI quality to VLOOD, but this baseline is absent from the main results tables (Tables 1, 2).** The ablation table (Table 4) shows that on Flickr8k, "Default" achieves B@4 36.8 / CIDEr 111.4 on poisoned inputs — very close to VLOOD's 36.1 / 110.7. VLOOD's primary advantage over Default is reducing false-positive ASR on clean inputs (0.627 → 0.000), which is a genuine improvement, but this is only visible by cross-referencing two different tables. Including "Default" as a row in the main tables would better contextualize VLOOD's contribution and prevent the impression that VLOOD's advantage over all baselines is uniform.

- **The defense evaluation section slightly overclaims robustness.** The paper tests Spectral Signatures and Beatrix — both designed for classification tasks — and correctly explains why they are ill-suited for image-to-text generation (lines 389–393). However, the caption of Table 5 claims "our attack is highly resistant to backdoor defenders" and "indicates the robustness of our method." Since no defense designed for this setting exists, the results only confirm a well-known mismatch rather than demonstrating intrinsic robustness. The paper would be better served by framing this section as "limitations of existing defenses for VLM generation tasks" rather than as evidence of VLOOD's robustness.

- **The "impact" definition in the dynamic weighting section (lines 208–210) conflates logits and cross-entropy scores.** The text first says g reads "the logits... where the ground truth token is located" but then says g "is computed using the cross-entropy score." A logit (pre-softmax) and a cross-entropy (negative log-probability after softmax) are different quantities. The mechanism's intent is clear, but the description should precisely define g as returning the per-token negative log-likelihood.

### Trivial

- The OOD data source (which specific public dataset the 3000 OOD pairs are drawn from) is not named in the main text. The paper says "Details can be found in Appx." (line 249). While the appendix (present in the original submission) presumably contains this information, naming the source in the main text would improve reproducibility.

- The trigger pattern used by VLOOD (beyond its size of 20×20 pixels) is not described. Figure 2 shows triggers for baselines but VLOOD's trigger design is only specified by pixel dimensions and placement (Section 3.1). A sentence describing the pattern would help reproducibility.

## Nice-to-Haves

- It would be informative to ablate the dynamic λ mechanism against a fixed λ (e.g., λ = 0.5) to verify that the adaptive weighting provides a measurable benefit over a static balance.
- The ChatGPT evaluation (Section 4.4) is mentioned but results are deferred to the appendix. A summary in the main text (e.g., correlation coefficient or alignment rate) would strengthen the claim that traditional metrics align with human judgment.
- Cross-dataset evaluation tables could explicitly state which dataset was used for OOD training and which for testing, rather than deferring to the appendix.

## Removed Points
These points from the reviewer are flagged for removal; treat them with caution:
- **"OOD data is never specified, making the core contribution unverifiable"** — The paper explicitly states "Details can be found in Appx." (line 249) and "To achieve OOD training, we train the backdoored model on one dataset and evaluate it on another." The OOD data source is specified in the appendix, which the parser strips from all submissions. The core claim (OOD attack) is empirically verified through results on five datasets across three architectures.
- **"OOD setting not evaluated against OOD-adapted baselines"** — The experimental setup states all methods are trained on one dataset and evaluated on another (line 249), meaning baselines are also trained on OOD data under the same protocol. The comparison is fair as-is.
- **"The paper does not thoroughly survey related work"** — Per policy, missing related works are not included as weaknesses since external sources cannot be verified.
- **"The ChatGPT evaluation results are not shown"** — Results and prompts are in the appendix (Appx.~\ref{app:chatGPT}), which exists in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the interesting nuance that VLOOD's main advantage over a simple LM loss baseline lies in suppressing false-positive ASR on clean inputs (a "cleanliness" gain) rather than improving poisoned-output quality — a distinction that is visible from the ablation table but could be highlighted more clearly in the paper's framing.

## Suggestions

1. Add a constraint (clamp to [0,1] or sigmoid normalization) to the λ update rule (Equation 6) and specify the initialization value.
2. Add a "Default (LM loss)" row to the main results tables (Tables 1 and 2) so readers can directly see VLOOD's improvement over the simplest OOD training baseline.
3. Rename Section 4.3 from "Defense Method Discussion" to a framing that better reflects the exploratory nature: e.g., "Why Existing Classification Defenses Fail for VLM Generation Tasks."
4. Precisely define the function g in the dynamic weighting section as returning the per-token negative log-likelihood (cross-entropy) of the ground-truth token, rather than conflating logits and cross-entropy.

## Score and Decision

The paper addresses an under-explored and practically relevant problem (backdoor attacks on VLMs without original training data), proposes a well-structured method with three complementary components, and provides strong empirical validation across multiple architectures, tasks, and datasets. The weaknesses are non-fatal and addressable. The core contributions are solid.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>