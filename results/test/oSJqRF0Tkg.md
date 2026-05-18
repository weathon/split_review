Now I have all the information I need. Let me compose the final review.

## Summary

This paper introduces Leopard, a multimodal large language model designed for text-rich multi-image understanding tasks. It makes two primary contributions: (1) Leopard-Instruct, a large-scale instruction-tuning dataset (~925K instances, of which 739K target text-rich multi-image scenarios) spanning documents/slides, tables/charts, and webpage snapshots; and (2) an adaptive high-resolution multi-image encoding module that dynamically allocates sub-image budgets proportionally across input images and applies pixel-shuffling compression. Experiments on 13 benchmarks show that Leopard variants (on both LLaVA and Idefics2 backbones) substantially outperform prior baselines (e.g., Mantis, VILA, Idefics2, LLaVA-NeXT-Interleave) on text-rich multi-image tasks, with ablation studies confirming the contributions of both the dataset and the encoding module.

## Strengths

- **Large-scale, task-targeted instruction tuning dataset for a genuine gap.** The paper identifies and fills a real scarcity bottleneck: high-quality instruction data for text-rich multi-image scenarios. The 925K-instance Leopard-Instruct dataset is constructed through multiple systematic pipelines (native multi-image datasets, merged single-image instances, GPT-4o-generated annotations, tabular-to-image rendering, CoT rationale augmentation) and covers three practically important domains. The downstream impact is demonstrated: Leopard-Idefics2 outperforms the strong Idefics2 baseline by 6.4 points on single-image text-rich benchmarks, showing the dataset imparts capabilities not covered by existing large-scale training (Section 3.1, Q2 in Section 4.4).

- **Cross-architecture validation.** Leopard is instantiated on both LLaVA and Idefics2 backbones, and both variants show substantial gains over their respective baselines on text-rich multi-image benchmarks. This rules out the concern that improvements are tied to a single architecture (Section 4.4, Q1).

- **Comprehensive ablations isolate contributions.** The paper systematically ablates: (a) removing the adaptive encoding module (Table 4, showing drops of 23.4 points on DocVQA, 13.5 on Multi-page DocVQA, 9.8 on DUDE); (b) removing each data domain (document data causes the largest drop); (c) varying the sub-image budget M (Figure 5, with M=50 identified as optimal). These analyses provide clear evidence that specific design choices drive the gains.

- **Controlled backbone comparison.** When Leopard uses LLaMA-3 instead of LLaMA-3.1 to match competitor backbones, it still surpasses Mantis and VILA by large margins (e.g., +16.8 on Multi-page DocVQA, +14.9 on DUDE), confirming that results are not simply due to LM scaling (Section 4.4, Q6).

- **Broad benchmark coverage.** Evaluation spans 5 text-rich multi-image datasets, 3 single-image text-rich datasets, and 5 general-domain benchmarks. This breadth supports claims of both specialized strength and retained general capability.

## Weaknesses

### Fatal

None.

### Major

- **Missing comparisons with concurrent state-of-the-art MLLMs weakens the SOTA claim.** The paper lists LLaVA-OneVision (08/2024), Idefics3 (08/2024), NVLM (09/2024), mPlug-DocOwl-2 (09/2024), Molmo (09/2024), and Qwen2-VL (09/2024) as concurrent efforts in the Related Work (line 63) and then concludes Leopard achieves "superior performance compared to existing open-source MLLMs" (line 294) and "becomes the strongest open-source MLLM in this area" (line 228). Yet none of these models appear in the experimental comparison. While some may not have released checkpoints or evaluation code at the time of paper writing, several (e.g., Qwen2-VL, mPlug-DocOwl-2) are specifically designed for text-rich scenarios and have published results on overlapping benchmarks. Without comparison or a clear argument for exclusion, the paper's central competitive claim is not fully supported. This is the most significant weakness because it threatens the paper's headline result rather than a peripheral one.

- **GPT-4o data quality verification is thin relative to its importance.** The paper relies on GPT-4o to generate ~270K Q-A pairs and 250K CoT rationales. Quality is manually verified on only 100 slide instances (line 88). No human evaluation is reported for the web action prediction data, multi-chart data, or the 250K CoT rationales. While 90% accuracy on 100 slides is encouraging, this is too narrow a basis to certify quality across all domains, especially since GPT-4o-generated data is central to the training data contribution.

### Minor

- **Adaptive encoding module is an incremental combination of existing techniques.** The three components — proportional sub-image allocation, grid-search for optimal cropping (LLaVA-OneVision), and pixel-shuffling compression (Chen et al. 2024, Idefics2) — are all drawn from prior work and explicitly cited as such. The ablation (w/o Adaptive) shows the module as a whole is effective, but the paper does not compare against simpler alternatives (e.g., uniform sub-image allocation, no compression with a higher compression factor) that would isolate which design choice drives the gain. This makes it difficult to assess the novelty of the module beyond being a reasonable engineering integration.

- **Merging single-image instances is a limited proxy for cross-image reasoning.** The strategy of randomly concatenating 2–4 single-page document/QA pairs with prompts like "in the second image" (line 87) teaches the model to follow explicit linguistic references rather than to infer inter-image relationships (e.g., cross-referencing tables and charts that share columns). While this is only one of several data construction methods, the paper does not analyze how much of the multi-image benchmark gains come from this simpler strategy versus from native multi-image data, making it unclear whether the model genuinely learns cross-image reasoning or just reference-following.

- **Human evaluation of GPT-4o data is limited to one domain (slides).** As noted above, only 100 slide instances are manually checked. Web data and CoT rationales are not spot-checked. Given that the paper's central dataset contribution is built on GPT-4o, broader quality verification would significantly strengthen confidence.

- **No standard deviations or multiple training runs reported.** The main results (Table 3) are reported as single-point estimates. While single-run evaluation is common at this scale, the paper's reliance on GPT-generated training data makes variation across runs a meaningful concern.

### Trivial

- **Minor imprecision in dataset size reporting.** The abstract says "about one million," while Leopard-Instruct is 925K and ShareGPT4V adds 313K (~1.24M total). The "about one million" likely refers to Leopard-Instruct alone rounded up, but the discrepancy between 925K and "about one million" could be clarified.
- **The "Other Domains" multi-image data (64K samples)** is mentioned but not described in terms of how it was formatted for multi-image input, creating a minor clarity gap.

## Nice-to-Haves

- A contamination/overlap analysis between the GPT-4o-generated training data and the evaluation benchmarks would directly address the most concerning alternative explanation for the results.
- An ablation comparing proportional allocation against uniform allocation (or other simple baselines) would clarify whether the adaptive allocation itself provides benefits beyond "some high-resolution strategy."
- Including even a subset of benchmarks with one concurrent model (e.g., Qwen2-VL or mPlug-DocOwl-2) would substantially strengthen the SOTA claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"If GPT-4o was used anywhere in the benchmark creation pipeline"** (from Harsh Critic's Point 1) — This is speculation without evidence. The benchmarks cited are standard public datasets; the reviewer provides no indication that GPT-4o was involved in their creation. The general contamination concern is valid and retained above; the specific accusation about benchmark provenance is removed.

2. **"Figure 4 does not report whether M interacts with the baseline (w/o adaptive)"** (from Harsh Critic's Other Observations) — The "w/o adaptive" condition removes sub-image partitioning entirely, so varying M is not applicable to that baseline. This criticism reflects a misunderstanding of the experimental setup.

3. **Criticism that existing datasets "cannot be independently verified" or questioning the existence/release of cited references** — All cited models, benchmarks, and datasets are assumed to exist per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful tension between the paper's two contributions: the dataset contribution is empirically strong but potentially vulnerable to contamination concerns, while the encoding module is empirically effective but technically incremental. Neither reviewer observation elevates to a novel insight about the field beyond what the paper itself articulates.

## Suggestions

- **Conduct a contamination analysis** between the GPT-4o-generated portions of Leopard-Instruct and the evaluation benchmarks (e.g., n-gram overlap on image metadata or textual content). Report results and, if overlap exists, re-evaluate after removing affected samples.
- **Add comparisons with at least one concurrent model** (e.g., Qwen2-VL or mPlug-DocOwl-2) on the text-rich multi-image benchmarks, or provide a clear, principled justification for exclusion.
- **Add a simpler ablation** for the encoding module: replace proportional allocation with uniform allocation while keeping compression fixed, to isolate the effect of the adaptive allocation mechanism.
- **Expand human evaluation** of GPT-4o-generated data to include web action prediction data and CoT rationales (even 50–100 instances each).
- **Acknowledge the limited proxy of merged single-image data** as a design choice and discuss whether native multi-image data drives most of the multi-image gains.

## Score and Decision

**Overall assessment**: The paper addresses a genuinely important gap with a substantial dataset contribution and an encoding module clearly shown to work via ablation. The evaluation is broad and well-structured. However, the missing comparisons with concurrent strong MLLMs weaken the headline SOTA claim, and the heavy reliance on GPT-4o without broader quality verification introduces some uncertainty. These issues are addressable and do not invalidate the core contributions. The dataset alone is a valuable resource for the community.

**Score based on axes**: Originality (6/10), Importance (8/10), Claim support (6/10), Soundness (7/10), Clarity (7/10), Community value (7/10).

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>