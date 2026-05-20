Now let me write the final consolidated review.

## Summary

This paper introduces a model merging benchmark for Multimodal LLMs (MLLMs) covering five vision-language capability categories (VQA, Geometry, Chart, OCR, Grounding) and a modality-merging setup (vision+audio+video). It evaluates 10 merging methods on this benchmark across two model families (InternVL2.5-1B and Qwen2-VL-7B), and proposes OptMerge, an extension of WUDI Merging that applies SVD-based denoising to task vectors and adjusts the optimizer (Adam for full fine-tuning, SGD with mean initialization for LoRA). Additional experiments on real Hugging Face checkpoints, modality merging, and larger model scales (Qwen2.5-VL-32B) are provided.

## Strengths

1. **First structured benchmark for MLLM model merging with task categorization.** The paper identifies a genuine gap — prior merging benchmarks focus on vision classification or LLMs, while MLLM merging lacks a standardized evaluation setup. The five-capability categorization (VQA, Geometry, Chart, OCR, Grounding) with ≥100k training samples per category provides a useful organizational template. The release of checkpoints and code is a genuine service to the community.

2. **Comprehensive comparison of 10 merging methods across multiple settings.** Tables 2, 3, 5, and 6 provide extensive experimental coverage: capability merging on two model families (full and LoRA fine-tuning), modality merging (Vicuna-7B with three encoders), and real-world Hugging Face checkpoints. The breadth of baselines (linear, sparsification, SVD, optimization-based) gives a thorough picture of relative performance.

3. **Modality merging experiments are genuinely novel and well-motivated.** The paper explores an underexplored use case: merging vision-language, audio-language, and video-language models into a single omni-model without retraining. The finding that merging methods can outperform individual modality models (Table 5) is practically interesting, even though the best results come from TSV Merging rather than OptMerge.

4. **Computational efficiency analysis is clear and impactful.** Table 7 shows OptMerge uses 0.22h/2.62GB vs. 25.38h/240GB for mixture training on InternVL2.5-1B, making a strong case for the practical value of model merging independent of whether it matches mixture training's accuracy.

5. **Validation on real community checkpoints (Table 6).** The experiment merging four independently developed Qwen2-VL-7B models from Hugging Face (math, Pokemon, OCR, Vietnamese VQA) demonstrates practical utility beyond hand-tuned expert models and is the setting where OptMerge shows its clearest advantage (66.70 vs. WUDI 64.80).

## Weaknesses

### Fatal
None.

### Major

1. **OptMerge's improvements over its primary baseline (WUDI Merging) are inconsistent, and the paper's main claim about beating mixture training is not supported by the evidence.** 
   - On InternVL2.5 (full fine-tuning, Table 2): OptMerge (57.44) vs. WUDI (57.00) — a 0.44 improvement, but *mixture training* (57.66) beats both. The paper's own data show that mixture training outperforms OptMerge on this setting.
   - On Qwen2-VL (LoRA, Table 3): due to table formatting artifacts in the extracted text, the exact numbers are difficult to verify. However, the paper's ablation study (Table 4) reports WUDI Merging at 58.65 on Qwen2-VL (without optimal coefficient search) and OptMerge at 63.30, showing a useful +4.65 gain *in that restricted comparison*. But Table 3 (with optimal λ search) suggests WUDI may be competitive or better. This inconsistency undermines confidence in the claimed advantage.
   - The paper claims "model merging can outperform mixture training" (Abstract, Contributions, Conclusion), yet its own InternVL2.5 results contradict this. The Qwen2-VL comparison to Qwen2-VL-Instruct is also confounded: the Instruct model was trained with extensive prior SFT using different data mixtures, not a controlled multi-task training from the same base.
   - The honest claim — "model merging achieves comparable performance at dramatically lower computational cost" — would be both accurate and impactful.

2. **The benchmark coverage is too narrow to serve as a "community benchmark" as claimed.** 
   The benchmark includes only two base models (InternVL2.5-1B-Instruct, full fine-tuning; Qwen2-VL-7B-Base, LoRA). For a claimed "first model merging benchmark" intended for community use, this is insufficient. A community benchmark would need: (a) models at multiple scales (e.g., 3B, 7B full fine-tuning), (b) different base architectures (e.g., LLaVA-based, different LLM backbones), (c) more task categories (temporal reasoning, document understanding, multimodal chain-of-thought), and (d) controlled analysis of how base model properties (instruct-tuned vs. pretrained) affect merging behavior. As-is, the benchmark functions primarily as a curated testbed for the authors' own method evaluation.

3. **The methodological novelty of OptMerge is incremental.** 
   OptMerge is directly built on WUDI Merging (Cheng et al., 2025): Eq. (3) is Eq. (1) with task vectors replaced by their low-rank SVD approximations. The additional components (SGD for LoRA, mean initialization) are practical heuristics rather than a new algorithmic principle. The method has two branches (Adam for full fine-tuning with centering; SGD for LoRA without centering) with different SVD treatments, described as necessary because of "different parameter properties" but without principled justification. Furthermore, Theorem 3.1 — presented as a theoretical contribution — does not lead to any specific design choice in OptMerge; it is used to motivate the already-known observation that small task vectors help merging.

4. **The modality merging experiment (Table 5) does not show OptMerge as the best method.**
   TSV Merging achieves 67.34 average vs. OptMerge's 67.00, and on MUSIC-AVQA, TSV (53.78) outperforms OptMerge (53.17). The paper bolded both TSV and OptMerge values in the Avg row, which is misleading — the text claims "the best merging method even outperforms online composition methods" without clarifying that the best method is TSV, not OptMerge.

### Minor

- **Insufficient detail for modality model training.** The vision/audio/video models used in Section 5.1 are described only by encoder names and connector types. Training data, hyperparameters, and checkpoints for these modality-specific models are not specified, making the experiment unreproducible as written. The paper refers to "App. C" for details, but the appendix is not available in the submission.

- **No statistical significance information.** Given that many method differences are <1%, the absence of confidence intervals or variance estimates makes it impossible to assess whether OptMerge's improvements over the nearest competitor are meaningful. This is especially relevant for the InternVL2.5 results where OptMerge leads by 0.44 over WUDI.

- **The ablation study (Table 4) shows the method is fragile in one setting.** On Qwen2-VL, replacing WUDI's Adam with SGD alone causes a catastrophic 9.77% drop (58.65 → 48.88). The final improvement (63.30) requires the specific combination of SGD + mean initialization + low-rank SVD, making it unclear which component is driving the gain across different settings.

### Trivial

- The paper states that the rank k is "set to rank of each task vector divided by the number of tasks (i.e., 5)" without motivation. This specific choice appears arbitrary.

## Nice-to-Haves

- **Failure analysis:** The paper notes that merging Qwen2.5-Math and Qwen2.5-Coder fails due to excessive parameter drift. A more systematic analysis of when and why merging fails on the benchmark would be valuable.
- **Rank sensitivity for the LoRA branch:** The rank k ablation (Table 8) is done only for InternVL2.5 (full fine-tuning). An equivalent analysis for the LoRA branch would strengthen the method's robustness claims.
- **Comparison of the benchmark's base model sensitivity:** InternVL2.5-1B-Instruct (instruction-tuned) and Qwen2-VL-7B-Base (pretrained) may behave very differently during merging. The paper does not discuss how this choice affects benchmark validity.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"The benchmark construction may have deliberately tuned expert models to have small task vectors making merging easier"** (Harsh Critic). This is speculation without evidence. The paper states it adjusted learning rates to minimize parameter changes while maintaining task performance — a standard and reasonable design choice informed by Theorem 3.1. The critic presents this as a methodological flaw rather than a deliberate design feature.

- **"Missing related works"** and **"missing appendix details"** — These are excluded per the hard rules, as the appendix is parser-stripped and external citation verification is not possible.

- **Several generic strengths from the Strength Finder** (e.g., "the paper addresses an important problem," "the method achieves the best average") that are either contradicted by verified weaknesses or are superficial claims without specific evidence.

## Novel Insights

The most interesting observation from combining the reviews is that the paper's strongest practical result (Hugging Face checkpoints, Table 6) and most novel experimental setting (modality merging, Table 5) are somewhat orthogonal to its main claimed contribution (the benchmark + OptMerge method). On the Hugging Face checkpoints — the setting closest to real-world model reuse — OptMerge shows its clearest advantage (66.70 vs. WUDI 64.80). This suggests the method's value may lie more in robustly merging independently developed, heterogeneous community models than in the controlled expert-model setting of the benchmark. Meanwhile, the modality merging results (where TSV Merging leads) suggest that different merging paradigms dominate in different regimes: SVD-based interference reduction works best for cross-modal models, while optimization-based methods like OptMerge may be better for same-modality capability integration. The paper would benefit from a clearer separation of these regimes rather than claiming a single method that works best everywhere.

## Suggestions

- **Reframe the core claim.** Drop or soften the claim about "surpassing mixture training." The evidence supports "model merging achieves comparable performance to mixture training at dramatically lower computational cost" — this is both accurate and impactful. 

- **Rebalance the benchmark and method contributions.** Either expand the benchmark substantially (more models, scales, architectures) before claiming it as a community resource, or reframe it as a focused evaluation testbed for the paper's experimental study.

- **Provide variance information.** At minimum report results across multiple λ selections or multiple random seeds. For the small-gap results, this would clarify whether the claimed improvements are stable.

- **Release the modality model training details.** The modality merging experiment is interesting but unreproducible without full specification of how the vision/audio/video models were trained.

## Score and Decision

**Round 1 — Bracketing:** I retrieved anchors in three bands on the topic of model merging for multimodal LLMs. Weak anchors (score <3.5, avg ~2.5–3.0) are papers with very limited contributions or purely empirical surveys. Middle anchors (3.5–7.5) include four model merging papers: PAVE (4.00, Reject), Learn to Merge (4.50, Reject), Expert Merging (5.00, Accept Poster), GMF-Mean (5.33, Reject), MergOPT (4.80, Accept Poster). Strong anchors (>7.5, avg ~8.0) are top papers with clear, well-supported novel contributions. Initial bracket: **4.0–5.5**.

**Round 2 — Narrowing:** I compared this paper against the most relevant anchors:

- **Expert Merging (5.00, Accept Poster)**: Same experimental setup (InternVL2.5, Qwen2-VL), similar claims about matching/surpassing mixture training. Expert Merging has a more principled method (hidden state/logit alignment), better result consistency, and a clearer contribution. The current paper's benchmark creation is a distinguishing feature, but the benchmark is narrower than needed for the claimed scope. **This paper is moderately weaker than Expert Merging.**

- **PAVE (4.00, Reject)**: Also uses SVD for task vector denoising. PAVE requires data access (limiting), while OptMerge is data-free. Both show incremental improvements over baselines. The current paper has broader scope (benchmark + modality merging) but also more overclaimed results. **Comparable or slightly stronger than PAVE.**

- **MergOPT (4.80, Accept Poster)**: A merge-aware optimizer with a novel perspective (shifting focus to fine-tuning stage). Clearer methodological contribution. The current paper has more extensive evaluation scope but a weaker core method. **Comparable, slightly weaker than MergOPT.**

**Final score:** 4.0. The paper makes useful contributions — the first structured benchmark for MLLM merging, comprehensive experimental comparisons, and interesting modality merging experiments. However, the method is incremental over WUDI Merging with inconsistent gains, the benchmark is too narrow to serve as a community resource, and several key claims are not supported by the paper's own data. The paper would benefit from a significant expansion of the benchmark and a more honest framing of the results.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>