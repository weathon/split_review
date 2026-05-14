Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper introduces a model merging benchmark for Multimodal LLMs that categorizes five capabilities (VQA, Geometry, Chart, OCR, Grounding) and explores merging across modalities (vision, audio, video). The authors also propose **OptMerge**, a method that applies SVD-based low-rank approximation to denoise task vectors and uses SGD with centroid initialization to stabilize merged-vector optimization. Experiments on InternVL2.5 and Qwen2-VL show OptMerge consistently outperforms 10 merging baselines, and the merged model can approach or exceed mixture training while requiring dramatically less GPU memory and time for the merge step. All checkpoints and code are publicly released.

## Strengths

- **Comprehensive MLLM merging benchmark with capability categorization.** The benchmark covers five distinct capabilities with at least 100k training samples each (Table 1), carefully selected evaluation suites (e.g., MathVista, ChartQA, TextVQA, RefCOCO), and is evaluated using unified toolkits (VLMEvalKit, LMMs-Eval). This fills a genuine gap: prior work either merges only two models (AdaMMS) or treats each dataset as an independent task without capability grouping (UQ-Merge).

- **Cross-architecture and cross-paradigm evaluation.** Testing on both InternVL2.5 (full fine-tuning) and Qwen2-VL (LoRA fine-tuning) reveals meaningful differences in task vector distributions (Figure 2) and merging behavior — for instance, Iso-C works on full FT models but collapses on LoRA models. This breadth makes the benchmark immediately useful.

- **Modality merging experiments (Table 5).** Merging vision-language, audio-language, and video-language models into a single model is a valuable direction beyond same-modality capability merging. OptMerge achieves 67.00 avg vs. 65.38 for Task Arithmetic, and as a static merge (one model) it is competitive with online composition methods that require 3× parameter storage.

- **Practical validation on community-released Hugging Face checkpoints (Table 6).** Testing on independently fine-tuned models (math reasoning, OCR, Vietnamese VQA, Pokemon domain) demonstrates that OptMerge works outside controlled benchmark settings, supporting decentralized development.

- **Consistent empirical gains across scales.** OptMerge achieves best or second-best average across nearly all settings: 57.44 on InternVL2.5-1B (Table 2), 63.30 on Qwen2-VL-7B (Table 3), 66.70 on Hugging Face models (Table 6), and 72.52 on Qwen2.5-VL-32B (Table 9, +1.56 over next-best individual model). The ablation study (Table 4) cleanly decomposes contributions: centroid initialization provides the largest boost (+4.43%), with low-rank approximation adding further gains.

- **Released artifacts.** The paper provides all fine-tuned checkpoints, merging code, and evaluation scripts, which will accelerate follow-up work.

## Weaknesses

### Fatal

None.

### Major

None. The core contributions — the benchmark and the OptMerge method — are well-supported.

### Minor

- **Theoretical framework loosely connected to method.** Theorem 3.1 derives an upper bound on merged model loss involving cross-task interference (δ) and curvature (η²T²), which motivates controlling parameter drift during fine-tuning. However, OptMerge does not operationalize δ, ηT, or any bound-derived quantity. The theorem serves as qualitative motivation (≈ "don't fine-tune too aggressively") rather than directly deriving or validating the SVD truncation, SGD, or centroid initialization choices. The paper would be stronger if it either measured these quantities empirically or derived a more specific connection between the bound and OptMerge's design.

- **Source of the "2.48% average performance gain" is unclear.** The abstract and contributions section cite this number prominently, but it is not traced to a specific table or calculation. Table 4 shows +4.65% for Qwen2-VL and +2.35% for Vicuna-7B over the WUDI baseline — neither matches 2.48%. Clarifying how this figure is computed (e.g., averaged across which settings) would improve transparency.

- **Mixture training comparison framing could be more precise.** Table 7 reports merging time (3.78h) vs. mixture training time (24.56h), but the merging time excludes the cost of the 5 separate fine-tuning runs needed to produce the expert models. In the community model reuse scenario (Hugging Face, Table 6) this cost is already sunk and the comparison is valid. In the "from scratch" scenario, total cost is 5 × fine-tuning + merging, which should be acknowledged. The paper already uses appropriately hedged language ("closely match or even surpass," "potentially surpasses") and the numbers do show near-parity, so this is a presentation issue rather than a claim validity problem.

- **No variance estimates across seeds.** The paper reports single-run results without standard deviations or confidence intervals. While single-run evaluation is standard practice in the model merging literature (none of the competing baselines originally reported variance either), reporting at least 2-3 seeds for the main result would strengthen confidence in the small-margin comparisons (e.g., OptMerge 57.44 vs. TSV 57.00 in Table 2).

- **General benchmark evaluation (Table 10) compares only against individual specialists, not against other merging methods.** Showing that OptMerge's merged model outperforms individual specialists on MMMU, DocVQA, ScienceQA, AI2D, and InfographicVQA is valuable, but evaluating at least the top 2-3 competing merging methods on these same benchmarks would clarify whether this integrated-capability benefit is unique to OptMerge or a general property of model merging.

### Trivial

- The paper claims "outperforms online composition methods" for modality merging (Table 5), but the margins against NaiveMC (66.88) and DAMC (66.79) are 0.12-0.21 points — essentially tied. The language should reflect this. Note that OptMerge has the structural advantage of being a static merge (single model) vs. online composition requiring separate storage per modality.

## Nice-to-Haves

- **Failure mode analysis.** The benchmark exposes interesting failure cases (e.g., Iso-C collapsing on LoRA, some task pairs degrading more than others). A deeper analysis of *which* capability pairs conflict most and why would provide valuable insight beyond method comparison.

- **Scaling to more tasks/modalities.** The benchmark has 5 capabilities and 3 modalities. How does performance degrade as more tasks are added? These scaling curves would strengthen the paper's claim about model merging as a scalable approach.

- **Task vector interference visualization.** Showing pairwise cosine similarity matrices between task vectors before and after OptMerge's denoising would make the method's mechanism more intuitive.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"Overclaiming surpasses mixture training with an invalid comparison."** REMOVED because the paper does *not* overclaim. The language is carefully hedged ("closely match or even surpass," "potentially surpasses"). In Table 2, OptMerge (57.44) is slightly *below* mixture (57.66) — the paper reports this honestly and uses "closely match." In Table 3, OptMerge (63.30) does surpass Qwen2-VL-Instruct (62.23) which is used as the upper bound. The claim as stated is accurate.

- **"DARE drop rate and TIES density not discussed."** REMOVED because these are standard defaults from the original papers. The paper states it follows standard practice with λ grid search over [0.1, 0.3, 0.5, 0.7, 1.0, 1.5] for all methods — this is the established protocol from Task Arithmetic and subsequent work. OptMerge's additional hyperparameters (rank k, learning rate, optimizer) are fully disclosed, and k is set by a simple formula (rank / number of tasks), not tuned per-setting.

- **"The paper never uses Theorem 3.1 to derive OptMerge."** Partially removed as a standalone fatal criticism. The theorem does inform the benchmark design (small learning rates, conservative fine-tuning) as stated in Section 3.2. The connection is loose but not absent. Retained as a minor weakness above.

- **"Weight Averaging being competitive (60.55) suggests limited task vector conflict, reducing practical significance."** REMOVED. Weight Averaging performs reasonably well on Qwen2-VL (LoRA) because LoRA task vectors are already low-rank and have smaller magnitude, but it is substantially worse on InternVL2.5 (49.12 vs. OptMerge 57.44). The benchmark's difficulty is heterogeneous — some settings are harder than others, which is a feature, not a bug.

- **"Qwen2-VL-Instruct as upper bound is unclear because models are fine-tuned by different groups."** REMOVED. The paper explicitly states Qwen2-VL-Instruct is used as an upper bound because it was trained on extensive diverse SFT data, making it a reasonable proxy for the best achievable multi-task performance on this architecture.

- **"Substituting ΣV^T for x is unclear / not justified."** REMOVED as a standalone criticism calling the method invalid. The paper provides explicit justification: the SVD-truncated version discards secondary row space information while preserving column feature space (principal components), yielding "more accurate estimates of x_i,l than using τ_i,l^T" (lines 551-556). Whether this argument is fully convincing is debatable, but the paper does provide reasoning, and the empirical results support it.

- **"SGD mechanism not fully explained."** REMOVED as a demand for theoretical proof of an empirical observation. The paper provides an empirical observation (Figure 3: Adam leads to magnitude shortcuts) and a grounded explanation (SGD provides implicit regularization, better escapes flat local optima in null-space directions). This is a reasonable level of explanation for an empirical systems paper.

## Novel Insights

The paper's most interesting insight is that **model merging can integrate capabilities in a way that produces emergent multi-task competence beyond any individual expert** (Table 10). The merged model outperforms every individual specialist on general QA benchmarks (MMMU, DocVQA, ScienceQA, AI2D, InfographicVQA) by an average of 10.85%, suggesting that the complementary knowledge from different capabilities synergizes rather than merely summing. This goes beyond the standard "merged model ≈ average of experts" finding and hints at genuine knowledge integration. A second useful insight is the demonstration that merging behavior differs fundamentally between full fine-tuning and LoRA — Iso-C works on full FT but collapses on LoRA — which has practical implications for anyone building on LoRA-tuned community models.

## Suggestions

- Clarify how the 2.48% average gain is computed (which settings, against which baselines) or replace it with per-setting gains that are directly traceable to tables.
- In Table 7, add a footnote clarifying that the merging time excludes the cost of individual fine-tuning, and note that in the Hugging Face reuse scenario this cost is already amortized.
- Tone down the "outperforms online composition" language for modality merging, since the margin is negligible; instead highlight OptMerge's structural advantage (single model vs. 3× storage).
- Consider reporting results for at least 2 random seeds on the main benchmark to address variance concerns, or cite precedent from the model merging literature establishing single-run evaluation as standard.

---

## Score Calibration

Anchor papers retrieved and compared:

| Path | Avg Score | Comparison |
|------|-----------|------------|
| Expert Merging (`Awf3ebMpKw`) | 5.00 (Accept Poster) | Similar MLLM merging scope; requires unlabeled calibration data vs this paper's data-free approach; weaker benchmark contribution |
| AdaRank (`fTygcJVOni`) | 4.50 (Accept Poster) | SVD-based merging method, vision/language only; no MLLM benchmark; narrower scope |
| Learn to Merge (`NYUxN6plEh`) | 4.50 (Reject) | Meta-learning for merging coefficients; method-focused, no MLLM benchmark |
| PAVE (`IBRldWTC3F`) | 4.00 (Reject) | SVD-based task vector purification; requires training data access |
| Subspace Boosting (`0Rn9oMU6g9`) | 3.50 (Reject) | SVD-based merging; training-free but vision/language only; no MLLM benchmark |
| Mixup Model Merge (`HZ0YvjVzpj`) | 3.50 (Withdrawn/Reject) | Simple interpolation; limited to 2 models |
| Model Merging Scaling Laws (`vpKXTmMtBQ`) | 5.50 (Reject) | Strong empirical contribution with scaling law; rejected for limited practical implications |
| Is Extending Modality (`nsMow1yhEE`) | 3.50 (Reject) | Related modality merging investigation; limited novelty |

The current paper is stronger than Expert Merging (5.00) because: (a) it provides a more comprehensive benchmark with released artifacts, (b) OptMerge is data-free (no calibration data needed), and (c) it covers modality merging in addition to capability merging. It is comparable to Model Merging Scaling Laws (5.50) in empirical contribution quality — the scaling laws paper was rejected for limited practical implications while this paper has clearer practical value through the benchmark and method. The paper's weaknesses (loose theory connection, no variance estimates, Table 10 missing method comparisons) are real but do not undermine the core benchmark + method contributions. The benchmark alone is a substantial community resource.

**Score: 6.0, Accept (Poster)**

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>