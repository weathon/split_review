Now I have enough calibration data. Let me write the consolidated review.

## Summary

This paper introduces OptMerge, a model merging method for Multimodal LLMs, along with a benchmark that divides MLLM capabilities into five categories (VQA, Geometry, Chart, OCR, Grounding) across two architectures (InternVL2.5 full fine-tuning and Qwen2-VL LoRA). The method combines SVD-based task vector denoising with robust optimization (SGD + mean initialization) to improve upon prior merging techniques. The paper further explores modality merging (vision+audio+video) and evaluates on real Hugging Face checkpoints. The core claim is that model merging can closely match or outperform mixture training at dramatically lower computational cost.

## Strengths

- **Comprehensive, purpose-built benchmark for MLLM merging.** The paper collects and releases fine-tuned checkpoints across five distinct capability categories with standardized evaluation protocols, covering both full fine-tuning (InternVL2.5) and LoRA (Qwen2-VL) scenarios. This fills a genuine gap — prior work (AdaMMS, UQ-Merge) either only merges two models or lacks capability categorization. The scale (100k+ samples per task, two architectures) makes this a useful community resource.

- **Extensive baseline coverage and thorough evaluation.** Ten merging methods are compared under consistent settings across multiple dimensions: capability merging (Tables 2-3), modality merging (Table 5), real Hugging Face checkpoints (Table 6), larger model scales (Table 9), and general QA benchmarks (Table 10). The consistency of OptMerge's results across such diverse settings — achieving best or near-best average performance in nearly every table — demonstrates genuine robustness.

- **Dramatic computational savings are clearly quantified.** Table 7 shows OptMerge requires 3.78 GPU-hours and 21.97 GB memory vs. 24.56 hours and 256 GB for data mixing. Even if the accuracy is comparable rather than superior, this efficiency gain alone is a meaningful practical contribution.

- **Practical validation on community models.** The Hugging Face checkpoint experiment (Table 6) merges independently-developed models (GRPO math, Pokemon, PDF OCR, Vietnamese OCR) and shows OptMerge achieving the highest average score (66.70%). This validates real-world applicability beyond controlled laboratory settings.

## Weaknesses

### Major

- **The claim that model merging "can outperform mixture training" is misleading.** The one controlled experiment (InternVL2.5, Table 2) shows OptMerge at 57.44 vs. genuine mixture training at 57.66 — slightly *worse*. For Qwen2-VL (Table 3), the "mixture training" baseline is Qwen2-VL-Instruct, a separate model checkpoint with extensive prior SFT on undisclosed data — this is not a controlled comparison. The paper honestly discloses this asymmetry (lines 693-695), but the abstract (line 33) and conclusion (line 126-128) nevertheless assert superiority without acknowledging these caveats. The data does support "closely matches mixture training at a fraction of the cost," which is a strong enough claim on its own.

- **The "2.48% average performance gain" is poorly specified.** The paper cites this number in the abstract and methodology contribution, but never clearly states what it is relative to (absolute percentage points? relative gain?), over what baseline (WUDI? over all baselines?), or across which experiments. The ablation table (Table 4) shows gains of 4.65% (Qwen2-VL, absolute points) and 2.35% (Vicuna-7B, absolute points), whose average is 3.50, not 2.48. This imprecision in reporting a headline number undermines trust in the paper's quantitative claims.

- **Table 10 (general QA tasks) lacks merging baselines.** The paper compares OptMerge only against individual expert models on these benchmarks, not against other merging methods (Task Arithmetic, TIES, WUDI, etc.). The resulting 10.85% improvement over individual models is expected — any reasonable merging method should improve over a single-expert baseline. Without merging-method baselines, the claim of "emergent integrated capabilities" (line 878) is not properly supported.

- **OptMerge's improvements over the strongest baselines are small.** On InternVL2.5 (Table 2), OptMerge averages 57.44 vs. WUDI's 57.00 — a 0.44 point gap. On the Hugging Face checkpoints (Table 6), OptMerge is 66.70 vs. TIES w/ DARE's 66.58 — essentially identical. On Qwen2-VL, OptMerge's 63.30 vs. TIES w/ DARE's 61.88 is the largest gap, but still modest. These incremental gains raise the question of whether the additional complexity of SVD + optimizer selection (applied only to linear layers with the rest averaged) is justified over simpler baselines.

### Minor

- **Theorem 3.1 is disconnected from the OptMerge method.** The theorem provides a bound on merged loss in terms of convergence error, cross-task interference, and curvature, motivating why small η and T matter. However, OptMerge's specific components (SVD denoising, SGD vs. Adam, mean initialization) are not derived from or guided by this bound. The theorem could apply to *any* merging method and is used primarily to justify benchmark construction. The paper would benefit from either operationalizing the bound (e.g., predicting which layers benefit from denoising) or separating the theoretical motivation from the method contribution.

- **The rank size k selection is ad hoc.** The paper sets k = rank_of_task_vector / 5 (line 650-651). While the ablation (Table 8) shows stability for 10-30% ratios, there is no principled criterion (e.g., cumulative explained variance threshold) for choosing k. This is a minor practical concern given the demonstrated robustness.

- **No analysis of failure cases or when OptMerge underperforms.** The limitations section (D.2) acknowledges resource constraints and data quality, but does not analyze when merging fails — e.g., when task vectors have large norms or strong directional conflicts. Providing even one concrete failure case would strengthen the paper's scientific rigor.

### Trivial

- The 2.48% number should be clearly defined with the reference baseline and whether it is absolute or relative improvement.
- No statistical significance or variance is reported, though this is standard practice for large-scale model merging evaluations in this field.

## Nice-to-Haves

- A controlled mixture training experiment on Qwen2-VL-Base (training on the same task-specific data) would cleanly resolve the "outperforms mixture training" claim.
- Including merging baselines in Table 10 would substantially strengthen the "emergent integrated capabilities" claim.
- Visualizing the task vector cosine similarity matrix (as suggested by Theorem 3.1's assumptions) would help explain why certain methods work better on these specific benchmarks.

## Removed Points

- **"OptMerge and TIES w/ DARE are tied at 63.30 on Qwen2-VL"** — Factually incorrect. From Table 3, OptMerge achieves 63.30, TIES w/ DARE achieves 61.88. The critic misread the table.
- **"AdaMMS and UQ-Merge already propose benchmarks for MLLM merging"** — The paper explicitly addresses this and distinguishes its contribution (fine-grained capability categorization, multi-model merging). The "first" claim is qualified appropriately.
- **"Modality merging experiment lacks a joint-training baseline"** — This demands the paper solve a different problem (joint training) that contradicts its "data-free" framing. The comparisons against individual modalities and online composing methods (NaiveMC, DAMC) are appropriate for the scope.
- **Various formatting/style nitpicks from the reviewer** — These are parser artifacts or trivial presentation issues.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel perspective or synthesis that the paper's authors have missed.

## Suggestions

1. **Reframe the core claim.** Replace "model merging can outperform mixture training" with "model merging closely matches mixture training at a fraction of the computational cost" — this is equally impactful and factually supported by the evidence (Tables 2, 3, and 7).

2. **Run the controlled Qwen2-VL-Base mixture training experiment.** This single experiment would either validate or retire the paper's strongest claim and could be done relatively cheaply given the infrastructure already in place.

3. **Add merging baselines to Table 10.** Include at least Task Arithmetic, TIES, and WUDI so the "emergent integrated capabilities" claim can be properly benchmarked.

## Score and Decision

**Calibration anchor comparison:**

| Anchor Paper | Avg Score | Comparison to This Paper |
|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/nsmow1yhEE.md` — "Is Extending Modality The Right Path..." | 3.50 | Weaker: that paper was a descriptive study without a novel method or benchmark. This paper has a concrete method and benchmark, making it stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/fObtmKj0Ok.md` — "Model Merging Beyond Image Classification" | 3.60 | Similar tier: both have genuine contributions but limited scope and oversold claims. This paper's benchmark is more comprehensive. |
| `/home/wg25r/review_agent/human_reviews_2026/IBRldWTC3F.md` — "Purifying Task Vectors (PAVE)" | 4.00 | Closely comparable: both propose task-vector denoising for merging with modest improvements. This paper has a broader evaluation and benchmark. |
| `/home/wg25r/review_agent/human_reviews_2026/y0gom847Oy.md` — "Gram-weighted Mahalanobis Fréchet Mean" | 5.33 | Stronger: cleaner theoretical framing, hyperparameter-free advantage. This paper's theory is less connected to the method. |
| `/home/wg25r/review_agent/human_reviews_2026/awyJs71tE7.md` — "FlexMerge" | 5.00 | Stronger: more novel framework (accuracy-size tradeoff), clearer contribution, accepted. |
| `/home/wg25r/review_agent/human_reviews_2026/NYUxN6plEh.md` — "Learn to Merge" | 4.50 | Similar tier: both propose merging methods with thorough experiments but marginal gains and oversold claims. |
| `/home/wg25r/review_agent/human_reviews_2026/HZ0YvjVzpj.md` — "Mixup Model Merge" | 3.50 | Weaker: simpler method, less evidence. This paper is more comprehensive. |
| `/home/wg25r/review_agent/human_reviews_2026/SKtC3JTCyr.md` — "Variational Model Merging" | 5.00 | Stronger: cleaner theoretical framing, accepted-level work. |
| `/home/wg25r/review_agent/human_reviews_2026/Awf3ebMpKw.md` — "Expert Merging" | 5.00 | Stronger: training-light with calibration data, accepted poster. |

This paper's profile most closely matches PAVE (4.00) and Learn to Merge (4.50). It has a genuine benchmark contribution that distinguishes it from purely method-focused papers, but its central claims are overstated relative to the evidence, and the method's improvements are small. The benchmark contribution is real but does not rescue the paper from its overclaiming.

**Final score: 4.5**

The paper has a solid benchmark contribution and the computational efficiency angle is genuinely useful. However, the headline claims about outperforming mixture training are not supported by the controlled experiment, the 2.48% gain is poorly defined, key baselines are missing from Table 10, and the method's improvements over strong baselines are marginal. These issues could be addressed with major revisions (reframing claims, adding controlled experiments), but the paper as submitted does not adequately support its central arguments.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>