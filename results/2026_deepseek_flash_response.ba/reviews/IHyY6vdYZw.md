## Summary

This paper introduces VisualPRM400K, the first large-scale multimodal process supervision dataset (~400K samples with ~2M step-level annotations), and VisualProcessBench, a human-annotated benchmark (2,866 samples, 26,950 step labels) for evaluating step-level error detection in multimodal reasoning. Building on these resources, the authors train VisualPRM, an 8B multimodal Process Reward Model, and demonstrate consistent Best-of-N improvements (up to +8.9 points) across three MLLM families and four model scales. The dataset, benchmark, and model are promised for release.

## Strengths

1. **First multimodal process supervision dataset fills a clear gap.** Prior process supervision datasets (PRM800K, Math-Shepherd) were text-only; VisualPRM400K extends this to the multimodal setting with ~400K samples and ~2M step-level annotations generated via an automatic Monte Carlo pipeline adapted from Math-Shepherd (Section 3.1). This is the paper's core contribution and is genuinely novel.

2. **Well-constructed human-annotated benchmark.** VisualProcessBench improves over prior work (ProcessBench, PRM800K) by requiring detection of *all* erroneous steps rather than only the first (lines 162–163). The annotation process uses 13 human experts with ~39 person-days and a 10% per-split author review cycle (line 168), providing high-quality ground truth. This is the cleanest contribution in the paper.

3. **Consistent BoN gains across diverse models and scales.** Table 2 shows improvements for MiniCPM-V2.6 (+8.0), Qwen2.5-VL-7B (+3.7), InternVL2.5-8B (+8.4), InternVL2.5-26B (+8.9), InternVL2.5-38B (+6.3), and InternVL2.5-78B (+5.9) — six models from three families at four scales — demonstrating generality beyond a single architecture.

4. **Systematic ablation shows PRM superiority over ORM and SC grows with N.** Figure 4 shows PRM outperforming Self-Consistency and ORM at N=8, with the gap widening to 3.1 and 4.3 points at N=128 (line 267). This scaling evidence directly supports the claim that step-level process supervision provides better signal for test-time scaling.

5. **VisualPRM-8B is competitive with proprietary models on step-level detection.** On VisualProcessBench (Table 3), VisualPRM achieves 62.0 overall macro F1, outperforming GPT-4o (60.3) and GPT-4o-Mini (57.9), and matching Gemini-2.0-Flash (62.3), at 8B parameters.

6. **Inference efficiency advantage.** VisualPRM scores all steps in a single forward pass via token-probability readout, whereas prompted MLLMs generate autoregressive judgments per step (Section 4.3). This is a practical advantage for deployment.

## Weaknesses

### Major

- **Potential data leakage between training data and evaluation benchmarks (unaddressed).** The VisualPRM400K training questions are sourced from "MMLR v1.1" (Wang et al., 2024c). The BoN evaluation benchmarks — MMMU, MathVision, MathVerse, DynaMath, WeMath, MathVista, LogicVista — are standard multimodal reasoning benchmarks commonly used in constructing multimodal training data. If MMLR/MMRP drew questions from any of these benchmarks, the headline BoN improvements could be inflated by the PRM having been exposed to evaluation-benchmark questions during training. The paper neither analyzes this overlap nor provides a decontamination procedure. This is a genuine threat to the paper's validity, and the absence of any discussion is a significant oversight. (Note: this is a concern about *potential* overlap; the paper should report whether decontamination was performed regardless of the outcome.)

### Minor

- **Asymmetric evaluation protocol on VisualProcessBench.** PRMs are evaluated via token-probability readout (a direct signal from their trained classification head), while MLLMs are prompted for free-text judgments parsed into binary labels (lines 236–238). These are fundamentally different inference paradigms, and the PRM's approach is inherently more favorable. The headline that VisualPRM "outperforms GPT-4o" should be understood with this caveat. The paper describes the protocol but does not discuss the asymmetry as a limitation.

- **Data generation pipeline has a circular dependency, not discussed upfront.** Solutions are sampled using InternVL2.5 models (line 130), and the MC rollouts that produce step-level supervision labels also depend on model completions from the same family. If the generator makes systematic errors on certain problem types (e.g., geometry), the supervision labels propagate those same errors. The paper acknowledges this indirectly in the ablation (lines 269–270: "inherent noise in our training data, which is generated through an automatic data pipeline") but does not discuss it as a limitation in the main text or conclusion. The noise is likely structured (correlated with model blind spots), not random.

- **Text-only results lack explanation of mechanism.** Table 5 shows VisualPRM improves text-only reasoning (e.g., +9.4 on MATH-500 for InternVL2.5-8B, +6.6 on GPQA for Qwen2.5-72B). However, the paper does not explain how an 8B multimodal model processes purely text inputs — whether via blank/null images, a bypassed vision encoder, or other mechanism. Without this, the results are intriguing but uninterpretable.

- **Base model architecture not explicitly stated.** VisualPRM is described as "an advanced multimodal PRM with 8B parameters" (line 25), but the base model (almost certainly InternVL2.5-8B, given the ablation comparisons) is never explicitly identified in the main text.

### Trivial

- Naming inconsistency: the training data source is called "MMLR v1.1" in Section 3.1 (line 130) but the related work discusses "MMPR" (line 110); both cite Wang et al., 2024c. This should be harmonized.

## Nice-to-Haves

- Report statistical significance / variance estimates for BoN results.
- Include error analysis showing what types of problems benefit most/least from PRM-based BoN (e.g., why MathVerse-VO gains +16.9 while DynaMath gains +1.4 for MiniCPM-V2.6).
- Compare against using the policy model's own sequence-level log-probability as a BoN scoring baseline, which would further isolate the benefit of the learned PRM.
- Analyze PRM calibration (whether "+" token probability corresponds well to actual step correctness).
- Evaluate proprietary models on VisualProcessBench under the same token-probability paradigm for a fairer comparison.

## Removed Points

- "Baseline Pass@1 numbers for InternVL2.5-78B (46.0) seem low compared to public leaderboards" — speculative; different evaluation setups yield different numbers and no evidence is provided.
- "Uneven improvements across benchmarks" — improvements naturally vary across benchmarks with different difficulty distributions and content; not a meaningful weakness.
- "No error analysis" / "No calibration analysis" / "No statistical significance" — moved to Nice-to-Haves as these are beyond the paper's stated scope or non-standard in this setting.
- "The comparison set for BoN could be broader" — moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Conduct and report a decontamination analysis** between the VisualPRM400K training questions (from MMLR/MMPR v1.1) and all evaluation benchmarks. This single step would resolve the most serious concern about the paper's validity.
- **Explicitly state the base model** for VisualPRM and explain the inference mechanism for text-only inputs.
- **Add a limitations paragraph** that discusses the data leakage concern, the asymmetric evaluation protocol on VisualProcessBench, and the circular dependency in the automatic pipeline — rather than only stating that modeling strategies were underexplored.
- **Harmonize the naming** of the training data source (MMLR vs. MMPR) throughout the paper.

## Calibration

**Round 1 bracket:** I identified that the paper plausibly sits between the weak anchors (avg scores < 3.5; irrelevant multimodal dataset papers in other domains) and strong anchors (avg scores > 7.5; very well-received benchmark papers like RM-Bench). Middle-band anchors (3.5–7.5) were most relevant.

**Round 2 anchors and comparisons:**
- **OpenPRM** (avg 6.00, Accept) — About open-domain PRMs. The paper under review has a more novel domain (multimodal) and comparable evaluation breadth, but the data leakage concern is a liability OpenPRM doesn't have. VisualPRM400K is slightly weaker overall.
- **Let's Verify Step by Step** (avg 5.50, Accept) — Introduced PRM800K, the seminal text-only PRM dataset. The paper under review extends to multimodal, uses automatic (not human) process labels, and has more evaluation. Slightly stronger due to novelty, but data leakage concern tempers this.
- **Inference-Aware Fine-Tuning for BoN** (avg 5.67, Accept) — BoN training method tested on a single model/task. The paper under review has broader evaluation and a more concrete contribution (dataset + benchmark) but less novel methodology.
- **ToolComp** (avg 5.40, Reject) — Process supervision benchmark with small scale (485 prompts). The paper under review has much larger scale and was rejected; VisualPRM400K is stronger.

**Final calibration:** The paper sits between the Let's Verify (5.50) and OpenPRM (6.00) anchors — its multimodal novelty is genuine, its evaluation is extensive, but the unaddressed data leakage concern prevents it from reaching the OpenPRM level. Final score: **6.0**.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>