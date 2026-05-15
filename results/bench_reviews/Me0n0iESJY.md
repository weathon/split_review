Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper makes two contributions to model merging for Multimodal LLMs: (1) a new benchmark that categorizes MLLM capabilities into five fine-grained task types (VQA, Geometry, Chart, OCR, Grounding) and studies both capability merging and modality merging across full-finetuned and LoRA-tuned models, with all checkpoints and code publicly released; and (2) OptMerge, a data-free merging method that applies low-rank SVD denoising to task vectors and improves optimization stability via SGD and mean-vector initialization. The method achieves the best average performance across most settings evaluated and demonstrates substantial computational savings over mixture training.

## Strengths

- **Genuine benchmark contribution.** The paper constructs the first structured model-merging benchmark for MLLMs, with five well-defined capability categories, both full-finetuning and LoRA scenarios, and a modality-merging setting. Each task uses ≥100K public training samples. The release of fine-tuned checkpoints, task vectors, and merging code for two base model families provides an immediately useful resource for the community (Tables 1–3, Sec. 5.1).

- **Comprehensive baseline evaluation.** Ten data-free merging algorithms (linear interpolation, sparsification, SVD-based, optimization-based) are systematically evaluated across multiple settings, providing the field with a reliable comparison point that previously did not exist (Tables 2–3, 5–6).

- **Practical validation on real-world checkpoints.** Merging four independently developed Hugging Face models (math reasoning, domain-specific, PDF OCR, Vietnamese VQA) with OptMerge yields a combined model that outperforms each individual model across all evaluated capabilities (Table 6). The method also scales effectively to a 32B model (Table 9), demonstrating practical applicability beyond curated benchmarks.

- **Substantial computational efficiency.** OptMerge completes in 0.22–3.78 hours with 2.62–21.97 GB GPU memory, compared to 24+ hours and 240+ GB for mixture training (Table 7). This makes the approach immediately practical for rapid model development.

- **Reasonable theoretical motivation.** Theorem 3.1 provides a bound linking fine-tuning intensity (learning rate, iterations) to merging quality, which usefully motivates the benchmark design principle of controlled parameter drift and explains why aggressive fine-tuning can harm mergeability (Sec. 3.2).

## Weaknesses

### Major

- **The claim that merging surpasses mixture training is not convincingly supported.** On InternVL2.5 (Table 2), OptMerge scores 57.44 vs. mixture training's 57.66 — the merged model is slightly *worse*. On Qwen2-VL (Table 3), the comparison uses Qwen2-VL-Instruct as a proxy (63.30 vs. 62.23), but that checkpoint was trained with different data, a different compute budget, and possibly auxiliary objectives, making it an unfair baseline. The paper hedges with "potentially surpasses," but the headline messaging overstates the evidence. A controlled mixture-training baseline for Qwen2-VL using the same task-specific datasets would be needed to properly support this claim.

- **The low-rank SVD contribution is marginal in the ablation.** Table 4 shows that on Qwen2-VL, switching from WUDI Merging (58.65) to +SGD+Initialization (63.08) accounts for +4.43 p.p. of improvement, while adding the low-rank component yields only +0.22 p.p. more (63.30). On InternVL2.5 (Table 2), OptMerge's advantage over WUDI is just +0.44 p.p. This substantially weakens the paper's narrative that low-rank noise reduction via SVD is the critical innovation; the mean initialization and optimizer change appear to do most of the work.

### Minor

- **No error bars or multiple-run statistics.** The margins between top merging methods are often small (e.g., OptMerge 57.44 vs. WUDI 57.00 on InternVL2.5; TIES+DARE 61.88 vs. OptMerge 63.30 on Qwen2-VL). Without any measure of variance (standard deviation over ≥3 seeds), it is impossible to determine whether these differences are reliable or within noise. The "2.48% average gain" quoted in the abstract is never decomposed — the baseline, set of tasks, and confidence intervals are not specified.

- **AdaMMS and UQ-Merge are discussed but not included in the benchmark.** The paper explicitly scopes its evaluation to data-free methods, which excludes these two (they require test-set access). However, since AdaMMS and UQ-Merge are the only prior methods specifically designed for MLLM merging, a reader reasonably expects a direct comparison or at least a more prominent justification for their exclusion. The current treatment in Related Work (lines 64) is brief.

- **The theoretical result (Theorem 3.1) motivates benchmark design but does not inform the method.** The bound is used to justify limiting parameter drift during fine-tuning, but OptMerge's design (SVD truncation, SGD, mean initialization) is not derived from or guided by the theorem. The connection between theory and method is therefore loose.

### Trivial

- The "2.48% average gain" figure in the abstract and contributions list lacks a clearly stated baseline, making it difficult to interpret.

## Nice-to-Haves

- Expanding the modality-merging evaluation beyond MUSIC-AVQA and AVQA to a broader set of audio-visual-language benchmarks would strengthen the generality of the modality-merging findings.
- Providing a public leaderboard and standardized evaluation script would increase the benchmark's long-term community impact.
- A controlled mixture-training experiment for Qwen2-VL (using exactly the same task-specific data and compute as the individual fine-tuning runs) would properly anchor the merging-vs-mixture comparison.

## Removed Points

These points were flagged for removal from the main review. Treat them with caution:

- **"The benchmark omits comparison to prior MLLM merging methods (structural)"** — The paper explicitly scopes to data-free methods (Sec. 2, line 60–61), and AdaMMS/UQ-Merge require test-set access. This is a scope decision, not an error. Kept as a weakened minor point about clarity of justification rather than a missing experiment.

- **"The description of OptMerge is confusing: it mixes two distinct strategies (full-finetuned vs. LoRA) without a unified principle"** — The paper clearly separates these in Sec. 4.1 (full fine-tuning) and Sec. 4.2 (LoRA), explaining that different parameter properties require different strategies. This is a misreading by the reviewer.

- **"The 2.48% gain figure is presented without context"** — Partially valid but already captured in the minor weakness about unspecified baseline. The figure exists; the issue is insufficient documentation, not absent evidence.

- **Various formatting/typo concerns from the harsh critic** — These are parser artifacts; the original paper does not have these issues per the review instructions.

## Novel Insights

The paper's empirical finding that model merging can effectively combine different modalities (vision, audio, video) into a unified Omni model — with the merged model outperforming each individual modality model and rivaling online composition methods that store 3× the parameters — is genuinely novel. While the result is somewhat expected (multimodal tasks require multimodal inputs), the demonstration that data-free static merging can achieve this without modality-specific training data is a valuable proof of concept. The task-vector distribution analysis (Fig. 2), showing distinct patterns between full-finetuned (right-skewed) and LoRA-tuned (multimodal) parameter changes, provides useful diagnostic insight for future merging method design.

## Suggestions

- Temper the "surpasses mixture training" claim or support it with a controlled mixture-training baseline for Qwen2-VL. The current evidence shows merging is competitive with, not clearly superior to, mixture training.
- Report standard deviation over ≥3 random seeds for the main results tables to establish whether the reported ranking differences are statistically meaningful.
- Clarify what the "2.48% average gain" is measured against (which baseline, which models/tasks) and provide confidence intervals.
- Restructure the narrative around OptMerge to more accurately reflect the ablation results: the mean initialization and SGD change appear to be the primary drivers of improvement, with low-rank SVD providing a small additional benefit. The current framing overemphasizes the SVD component.

## Score and Decision

### Anchor comparison

| Path | Paper | Avg Score | Comparison |
|------|-------|-----------|------------|
| `awyJs71tE7` | FlexMerge | 5.00 (Accept Poster) | Similar data-free merging framework + empirical study. Our paper adds a structured MLLM benchmark and released resources, making a stronger practical contribution, but shares the issue of modest method novelty. |
| `NYUxN6plEh` | MetaMerging | 4.50 (Reject) | Meta-learning for merging; marginal gains, requires data. Our paper is data-free with broader evaluation and a benchmark — clearly stronger. |
| `y0gom847Oy` | GMF-Mean | 5.33 (Reject) | Novel theoretical reframing but assumptions questioned. Our paper has less theoretical depth but substantially more comprehensive experiments and real-world validation. |
| `HZ0YvjVzpj` | Mixup Model Merge | 3.50 (Withdrawn) | Simple two-model method. Our paper is substantially stronger in scope, scale, and contribution. |
| `1FDBJPYWCb` | Tiny-R1V | 3.00 (Withdrawn) | Lightweight reasoning + merging, marginal gains. Our paper has a more clearly defined benchmark contribution. |
| `vpKXTmMtBQ` | Model Merging Scaling Laws | 5.50 (Reject) | Empirical scaling laws with massive experiments; insightful but limited practical evaluation. Our paper is more applied and directly useful to practitioners. |
| `ocEoHCrezd` | Latent Merging | 2.50 (Withdrawn) | Much weaker contribution. |
| `IBRldWTC3F` | Purifying Task Vectors | 4.00 (Reject) | Related SVD-based task vector work but narrower scope. |
| `fObtmKj0Ok` | Model Merging Beyond Classification | 3.60 (Reject) | Related merging benchmark work but narrower domain. |

The paper under review contributes a genuinely useful benchmark for a growing subfield, releases valuable resources (checkpoints, code), evaluates 10 methods comprehensively, and proposes a method that achieves best results even if the improvements are modest and the low-rank contribution is smaller than presented. The weaknesses — overstated mixture-training claims, marginal low-rank contribution, and lack of error bars — are real but addressable. Compared to anchors, this paper sits between FlexMerge (5.00, Accept Poster) and GMF-Mean (5.33, Reject), with the benchmark contribution pushing it toward acceptance. I place it at 5.5, with a poster accept decision — the benchmark and resources provide clear community value, and the method is a reasonable contribution, but the headline claims need tempering and the ablation analysis needs more honest framing.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>