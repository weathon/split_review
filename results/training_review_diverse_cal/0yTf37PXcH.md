Now I have thoroughly read the paper and verified the reviewer's claims. Let me produce the consolidated review.

## Summary

This paper presents Arcana, a multimodal large language model with two architectural innovations: (1) **MM-LoRA**, which decouples visual and language token processing in the LLM decoder by assigning separate LoRA subspaces to each modality, and (2) **QLadder**, a lightweight query-based adapter that adds 64 learnable visual tokens to a frozen CLIP encoder to enrich visual representations without requiring a second frozen encoder. Experiments on VQA and LVLM benchmarks (using ~2M training data) show consistent improvements over LLaVA-v1.5 and competitive results against contemporaneous MLLMs.

## Strengths

- **QLadder outperforms adding a second visual encoder (MOF) while being more efficient.** Table 5 (additional visual encoder comparison) shows QLadder (+64 tokens) achieves **+3.6 on MMVP**, **+2.0 on MMBench**, and **+0.6 on TextVQA** over LLaVA-v1.5, whereas MOF (fusing DINOv2 with 256 tokens) degrades MMBench (−4.2) and TextVQA (−1.7). This is a clean, well-controlled comparison that directly supports QLadder's core benefit: richer visual features without the drawbacks of multi-encoder setups.

- **MM-LoRA with separate vision/language subspaces consistently outperforms standard LoRA.** The ablation in Table 4 shows the optimal MM-LoRA configuration (β=0.25, γ=0.75) improves over standard LoRA by +0.6 on TextVQA, +2.1 on ScienceQA, +1.0 on MMBench, and +40 on MME. The β=1 (γ=0) configuration causes sharp drops (−6.9 on TextVQA, −7.4 on MMBench), confirming that modality-specific subspaces are critical — directly supporting the decoupling claim.

- **Competitive results with limited training data.** Arcana achieves strong performance using only ~2M total training samples (1.2M pretrain + 934K instruction tuning), e.g., **71.2 on ScienceQA**, **67.4 on MMBench**, **87.1 on POPE** — outperforming LLaVA-v1.5 on most benchmarks despite using the same backbone and comparable data scale.

- **QLadder introduces minimal computational overhead.** Table 7 shows QLadder adds only **0.58 GB of memory** and slows inference by merely **0.11 tokens/s**, making the improvement practical for deployment.

- **Attention visualizations provide interpretable evidence.** Figure 4 shows MM-LoRA increases attention to visual tokens in middle/late LLM layers, and QLadder further boosts visual attention across all layers, directly illustrating the mechanism behind the performance gains.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No variance reporting across any experiment.** The paper's evidence rests on fine-grained performance differences (typically 1–3 points), yet all results are reported as single runs without standard deviations or confidence intervals. While single-run evaluation is common in this subfield for large-scale benchmarks, the absence is notable for ablation studies where improvements are small. The paper's central claims would be strengthened by at least 2–3 runs on key ablations (Tables 4 and the QLadder ablation). That said, this does not invalidate the core claims — the pattern of improvement is consistent across multiple benchmarks.

- **The "data engine" is mentioned as a contribution but never validated.** The conclusion states "we designed a data engine that uses diverse visual annotation models and large language models to generate captions rich in visual information," yet no experiment uses data from this engine. All training data comes from ShareGPT4V and standard instruction-tuning datasets. The data engine appears only in the conclusion and the "limitations and future work" section, creating an impression of an undeployed contribution. The paper should either remove this claim or validate it with experiments.

- **The language understanding comparison (Table 3) is a weak control.** The paper compares Arcana against pure language models (LLaMA-2, Vicuna-v1.5) to show it preserves language ability. The proper control would compare Arcana's language performance against a comparable MLLM baseline (e.g., LLaVA-v1.5 with LoRA) to isolate whether MM-LoRA specifically protects language ability better than standard MLLM fine-tuning. The current comparison only shows that the MLLM does not catastrophically degrade language performance, which is already well-understood.

- **MM-LoRA inference overhead is acknowledged but not quantified.** The limitations section notes that MM-LoRA's parameters cannot be merged into base weights, increasing inference costs. However, the paper does not report throughput or memory measurements for MM-LoRA (only QLadder's overhead is reported). Given that MM-LoRA uses two separate low-rank matrices of the same total rank as LoRA, the inference cost should be quantified.

### Trivial

- **The "QLadder" name is evocative but the mechanism is a standard Q-Former-style design** (cross-attention + FFN initialized from CLIP weights). The "ladder" metaphor implies hierarchical progressive refinement, but the architecture is multiple stacked layers of the same operation. This is a naming choice rather than a technical flaw.

- **The claim "demonstrates for the first time that with limited multimodal training data, retaining the capabilities of a pre-trained model and adding a small number of visual encoders can still enhance the performance"** is somewhat overstated. Prior works (BLIP-2, InstructBLIP, LLaVA-HR) also add adapters or tokens to frozen encoders with limited data. The novelty lies in the specific design, not in being the first demonstration of this category.

## Nice-to-Haves

- Comparisons against more recent MLLMs (e.g., LLaVA-NeXT, InternVL, Qwen2-VL) would strengthen the claim of advancing state-of-the-art, though the existing baseline set is reasonable for the paper's scale.
- An analysis probing where MM-LoRA specifically reduces modality interference (e.g., comparing attention distributions, analyzing token-level representations between modalities) would deepen the mechanistic understanding beyond what the current attention visualizations provide.
- A pure vision task evaluation (e.g., classification probes on the QLadder features) could further isolate the visual encoder improvement, though this is outside the paper's MLLM scope.

## Removed Points

- **Reviewer's claim that QLadder gains are "relative to a baseline that already includes MM-LoRA":** This is factually incorrect. The QLadder ablation baseline (ScienceQA 69.1, MMBench 63.8, MME 1460) matches the standard LoRA row from Table 4 — it does *not* include MM-LoRA. The reviewer misread the ablation structure.
- **Reviewer's criticism that the β=0/γ=1 configuration outperforms β=0.25/γ=0.75 on MMBench as evidence of inconsistency:** While MMBench favors β=0 (65.4 vs 64.8), β=0.25 wins on 3 of 4 benchmarks (TextVQA, ScienceQA, MME). The paper's claim of optimal overall performance at β=0.25 is reasonable and supported by the aggregate data.
- **Reviewer's claim that the community standard requires error bars / significance tests:** This is not standard practice in MLLM papers for large-benchmark evaluation (seen in LLaVA, InstructBLIP, mPLUG-Owl2, etc. — none report such statistics). The concern about variance is valid but the stated standard is incorrect.
- **Reviewer's demand for ablation on "pure visual recognition tasks" (ImageNet classification, detection, segmentation):** The paper's scope is improving MLLMs, not advancing pure vision encoders. This demand evaluates the paper against the wrong class of expectations.

## Novel Insights

The harsh reviewer correctly identifies that the paper's contributions are incremental and the evidence would benefit from statistical grounding, but overstates several issues to the point of factual error (e.g., misreading which baseline QLadder ablates against). The key insight from cross-referencing the reviews is that Arcana's most compelling result is the direct comparison against MOF (Table 5), where QLadder achieves *better or comparable* gains on visual grounding (MMVP) while *avoiding degradation* on general comprehension benchmarks — this is a genuinely useful finding that goes beyond the individual improvements of MM-LoRA and QLadder. The efficiency argument (64 tokens vs 256 tokens, no second encoder) is the paper's strongest contribution, yet it is somewhat buried in the ablation section rather than highlighted in the main results.

## Suggestions

1. **Add at least 2–3 runs for the core ablations** (Tables 4 and QLadder ablation) and report means. This single change would dramatically strengthen the paper's credibility.
2. **Remove the data engine claim entirely** from the conclusion, or add a brief experiment showing its impact. As written, it undermines the paper's credibility.
3. **Replace or supplement Table 3** with a comparison against LLaVA-v1.5 with LoRA on language benchmarks to demonstrate that MM-LoRA specifically protects language ability relative to standard LoRA fine-tuning.
4. **Report MM-LoRA inference overhead** (throughput and memory vs. standard LoRA) to complement the QLadder cost analysis already present.
5. **Highlight the QLadder vs. MOF comparison more prominently**, as it is the paper's strongest and most differentiating result.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>