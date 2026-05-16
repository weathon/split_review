Now I'll synthesize the final consolidated review.

## Summary

Arcana proposes two architectural modifications for MLLMs to improve visual perception: (1) **MM-LoRA**, which assigns separate LoRA parameters to visual and language tokens within the LLM decoder to avoid modality interference, and (2) **QLadder**, a lightweight query-based adapter that extracts enhanced visual features from a frozen CLIP encoder using a small number of learnable query tokens. Experiments on six VQA and five LVLM benchmarks show competitive performance, and controlled ablation studies (using LLaVA-v1.5 data) demonstrate consistent but modest improvements.

## Strengths

- **MM-LoRA consistently outperforms standard LoRA in controlled ablations.** When trained on the same LLaVA-v1.5 data (Section 5.3, Table 5), MM-LoRA with β=0.25, γ=0.75 improves over LoRA on all four benchmarks: TextVQA (+0.6), ScienceQA (+2.1), MMBench (+1.0), MME (+40). The β=1 extreme (visual-only LoRA) shows severe degradation (−6.9 on TextVQA), confirming that joint modality-specific learning is necessary.

- **QLadder is demonstrably efficient and effective.** Adding just 64 query tokens (Table 6) yields +2.1 on ScienceQA, +1.0 on MMBench, +40 on MME over baseline. Compared to MOF (which adds a full second encoder with 256–576 tokens), QLadder achieves better or comparable results on MMBench (+6.2 vs MOF's −4.2 decline) and TextVQA (+0.6 vs MOF's −1.7 decline) while using only 64 tokens (Table 9). The inference overhead is minimal (memory +0.58 GB, speed −0.11 tokens/s, Table 11).

- **State-of-the-art results with a small ViT-L (0.3B) encoder.** Arcana* achieves the highest MME score (1520.93) among all methods in Table 2, including those with larger encoders (e.g., Qwen-VL-Chat with 1.9B encoder). This demonstrates efficient use of vision resources.

- **Language capabilities are preserved despite multimodal training.** Arcana matches or exceeds the base Vicuna-v1.5 on all four language benchmarks (Table 5: BBH +0.9, AGIEval +8.1, ARC-c +4.8, ARC-e +5.5), indicating no catastrophic forgetting of language ability.

- **Ablation study is properly controlled.** The paper explicitly states (Section 5.3) that ablation experiments use only LLaVA-v1.5 data, providing a fair foundation for isolating the method's contribution.

## Weaknesses

### Major

- **Main results are confounded by different training data.** The primary comparisons (Tables 1 and 2) train Arcana on ~2.1M total samples (1.2M ShareGPT4V pre-training + 934K instruction data), while LLaVA-v1.5 uses ~1.26M samples (~595K CC + ~665K instruction). The paper does not clearly flag this discrepancy when presenting main results. The observed gains (e.g., +3.1 on MMBench, +9.3 on LLaVA^W) could be partially or largely driven by data quantity/quality rather than the architectural contributions. The ablation study (Section 5.3) does control for data and shows more modest gains (e.g., +1.0 on MMBench, +2.1 on ScienceQA), but the paper's narrative in Sections 4.2 and the introduction presents the larger-margin results as primary evidence. This is a **structural framing issue**: the paper's strongest claims rely on a confounded comparison, while the clean evidence shows smaller effects. The contributions are real but modest, and the paper should reframe around the ablation evidence.

### Minor

- **The "modality interference" mechanism is asserted but not directly evidenced.** The paper claims MM-LoRA prevents "information confusion" between modalities, but no direct analysis is provided — no gradient conflict measurements, no KL divergence between visual/language representations, no comparison of language-only performance degradation after multimodal training with vs. without MM-LoRA. The ablation (Table 5) shows MM-LoRA works, but the improvement is equally consistent with a capacity-allocation story (different modalities benefit from different effective ranks) rather than "decoupling." The term "modality interference" is used as an explanation for what the method improves, but the paper does not independently measure interference to verify the causal mechanism. This does not invalidate the method's effectiveness but means the claimed mechanism is speculative.

- **The NLU evaluation (Table 5) does not isolate the method's effect on language preservation.** Arcana's language scores are compared to the base Vicuna-v1.5 (which received no multimodal training). This does not answer the important question of whether multimodal training degrades language ability and whether MM-LoRA helps preserve it. A cleaner comparison would include: (a) Vicuna-v1.5 after standard multimodal LoRA tuning (without MM-LoRA) on the same language benchmarks, or (b) a direct ablation of Arcana with vs. without MM-LoRA on language-only tasks. Without this, the claim that "MM-LoRA preserves language capabilities" is unsubstantiated; Arcana may simply benefit from additional training data (ShareGPT text-only data is included in its 934K instruction mixture).

- **No error bars or statistical significance for small-margin improvements.** Several reported gains in the ablation are 0.6–2.1 percentage points (e.g., QLadder +1.0 on MMBench, MM-LoRA +0.6 on TextVQA). Given that MLLM benchmarks can exhibit 0.5–1.5 point variance across seeds, these improvements may not be statistically significant. No multiple seeds or significance tests are reported. This weakens confidence in the quantitative claims, though consistency across multiple benchmarks partly mitigates the concern.

- **QLadder's performance drop at 128 queries (Table 6) is not explained.** The model peaks at 64 queries and degrades at 128. This pattern needs discussion — it may indicate that query tokens compete with patch tokens for representational capacity, or that the training data is insufficient to support more query tokens. The absence of analysis weakens the QLadder design justification.

### Trivial

None.

## Nice-to-Haves

- **Compare MM-LoRA against simply using separate LoRA ranks per layer** (rather than per modality) to better isolate whether the benefit is from modality-specific routing or from flexible rank allocation.
- **Include failure-case analysis** for QLadder and MM-LoRA to clarify the boundaries of the improvements (e.g., on which image types or tasks do they fail to help).
- **Provide a more detailed computational cost comparison** between QLadder and MOF (training time, GPU memory during training, not just inference).
- **Compare QLadder against simpler alternatives** such as fine-tuning the last CLIP layer or adding a single cross-attention layer without the multi-layer ladder structure.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Code/data not released"** — Hard rule: if the paper cites a URL, it exists. Cannot question availability/release status.
2. **"Claim about increasing learning space has no reference"** — The paper's own ablation (β=1 case in Table 5, where performance drops severely) provides the evidence. The reviewer missed this. This claim is supported.
3. **"The 'for the first time' claim is a generic property of finetuning"** — This is a minor overclaim in the conclusion but does not affect the actual contribution (QLadder itself is the contribution, not the discovery that finetuning preserves pre-trained knowledge). Not a weakness of the method.
4. **"MOF results may not be under same setup"** — The paper explicitly states they "conducted detailed experiments to directly compare Q-Ladder with the MoF method under the LLaVA-v1.5 setting." The ambiguity is resolved.
5. **Various generic strengths from the Strength Finder** — Strengths like "addressed an important problem" without specific support are dropped as generic.
6. **Formatting/style nitpicks and missing appendix concerns** — Parser artifacts, not author errors.

## Novel Insights

The most interesting finding is the comparison between QLadder and MOF (Table 9): adding a second full encoder (DINOv2 via MOF) improves visual grounding (MMVP) but *hurts* comprehensive benchmarks (MMBench −4.2, TextVQA −1.7), while QLadder improves both. This suggests that the "more encoders is better" assumption in the MLLM literature has a real downside — auxiliary SSL-based features may interfere with the language-aligned CLIP representations on non-grounding tasks. QLadder's ladder structure, which uses cross-attention to refine features within the CLIP space rather than merging a separate feature space, appears to avoid this interference. This is a genuinely non-obvious architectural insight that goes beyond simply reporting higher numbers.

## Suggestions

1. **Reframe the paper's narrative** around the controlled ablation results (using LLaVA-v1.5 data) as the primary evidence for the method's effectiveness, and present the larger-data results (Tables 1, 2) as an additional demonstration of scaling combined with the method. Explicitly state the data difference in the main results section.
2. **Either provide direct evidence for modality interference** (gradient conflicts, representation similarity analysis) or **moderate the causal language** to describe MM-LoRA as "allocating separate capacity" rather than "decoupling modalities."
3. **Add a controlled comparison for the NLU table:** include scores of Vicuna-v1.5 after standard LoRA multimodal tuning (without MM-LoRA) on the same language benchmarks to isolate the language-preservation effect.
4. **Run at least 3 seeds for the ablation experiments** (Tables 5, 6, 8) and report mean ± std. If resources are constrained, acknowledge the lack of error bars as a limitation.
5. **Discuss why 128 queries underperform 64 queries** in QLadder — this could reveal a meaningful design constraint.

## Score and Decision

This paper makes two real but modest architectural contributions. The ablation studies provide clean evidence that MM-LoRA and QLadder each yield small but consistent improvements (1–2 points) when training data is controlled. The QLadder vs. MOF comparison is the strongest contribution, revealing an interesting asymmetry. However, the paper's primary narrative overclaims by presenting confounded main results as the headline evidence, and the mechanistic claims about modality interference are not directly supported. With moderate revisions to reframe the evidence and add a few controlled comparisons, the paper would be acceptable. As it stands, the framing inflates the contribution beyond what the clean evidence justifies.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>