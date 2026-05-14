I've now thoroughly read the paper and cross-checked all reviewer claims. Let me now write the consolidated review.

---

## Summary

This paper presents MobileLLM-R1, a series of sub-billion-parameter reasoning models trained with heavily curated open-source data. The core methodological contributions are (1) a benchmark-free, influence-score-based data mixing strategy for pre-training that allocates token budgets across heterogeneous datasets according to their cross-domain contributions to code, math, and knowledge capabilities; and (2) a data-model co-evolution strategy for mid-training that iteratively prunes negative-influence samples and reweights datasets. The resulting MobileLLM-R1-950M model achieves strong results (AIME'24: 15.5, LiveCodeBench-v6: 19.9) using only 4.2T pre-training tokens—substantially outperforming prior fully open-source models and matching Qwen3-0.6B, which used 36T tokens. All models, code, data sources, and mixing ratios are released.

## Strengths

- **Compelling empirical results on uncontaminated benchmarks**: MobileLLM-R1-950M achieves an AIME'24 score of 15.5, dramatically exceeding OLMo-2-1.48B (0.6) and SmolLM2-1.7B (0.3), and surpassing Qwen3-0.6B (11.3). On LiveCodeBench-v6 it reaches 19.9 vs. Qwen3-0.6B's 14.9. These benchmarks have no training data exposure, making them clean measures of reasoning ability (Table 9, Figure 9).

- **Principled data mixing via cross-domain influence scores**: The use of influence scores computed across Code, Math, and Knowledge capability-probing datasets (Eqs. 2–5) provides a benchmark-free mechanism for dataset-level reweighting. Figure 4 demonstrates that the resulting mixture consistently yields lower perplexity on held-out benchmarks compared to uniform sampling—notably, without accessing any benchmark test data during mixture optimization. The framework extends AutoMixer (Chang et al., 2025) to the cross-domain setting in a novel way.

- **Effective data-model co-evolution for mid-training**: The iterative rejection sampling and dataset reweighting (Eqs. 6–7) produce a pronounced compression of influence score distributions toward zero (Figure 5), supporting the claim of near-complete information extraction. Figure 6 shows this subsampled data avoids the performance dip observed with the original mid-training set, providing actionable evidence of benefit.

- **Comprehensive and transparent empirical validation**: The paper compares against 15+ models across 6 benchmarks at multiple parameter scales (140M, 360M, 950M), including both base-model (Table 8) and post-trained (Table 9) comparisons. Table 2 provides the critical ablation of identical reasoning SFT across models, isolating the contribution of pre-training/mid-training data quality. The full recipe—architectures (Table 3), hyperparameters (Table 4), pre-training data (Table 5), mid-training data (Table 6), and post-training data (Table 7)—is openly documented for reproducibility.

- **Actionable diagnostic insights**: The RankMe analysis (Table 11) showing that higher learning rates during pre-training lead to higher representational rank and better downstream mid-training MMLU provides practical guidance. The RL vs. SFT ablation (Figure 10) showing SFT consistently outperforms RL for small models is practically valuable.

## Weaknesses

### Fatal

None.

### Major

- **Benchmark training data in the mid-training mixture**: Table 6 explicitly includes GSM8K (train), ARC-Easy (train), ARC-Challenge (train), OBQA (train), PIQA (train), BoolQ (train), TriviaQA (train), and NaturalQuestions (train) as a "Benchmark Set" comprising ~0.01–0.97% of the mid-training mixture. The paper acknowledges this on lines 1500–1501: "We also introduce a small but targeted set of benchmark-style datasets (e.g., GSM8K, ARC, OBQA) to align training with downstream evaluation." This means GSM8K and Commonsense Reasoning Avg (which includes ARC-Easy/ARC-Challenge) results in Tables 8–9 and Figure 8 are not clean measures of generalization—they reflect in-domain training exposure. While the fraction of contaminated tokens is very small relative to the total training budget (mid-training is 200B out of 4.4T total tokens, and the benchmark set is at most ~0.97% of that), and the headline AIME and LiveCodeBench results are entirely uncontaminated, the paper's conclusion (line 1164) that results are achieved "without exposing any benchmark data during training" is factually incorrect. The authors should either filter out all benchmark training splits and re-evaluate, or retract claims about those specific benchmarks and transparently acknowledge the contamination.

- **No downstream benchmark validation of the influence-based data mixing**: Figure 4 demonstrates that the influence-weighted mixture reduces perplexity on capability-probing datasets compared to uniform sampling. However, no downstream reasoning benchmark accuracy (e.g., MATH, HumanEval, AIME, GSM8K) is reported for a model trained with the influence-weighted mixture versus a model trained with uniform sampling under otherwise identical conditions. The final results in Tables 8–9 fold the influence-based mixture together with many other design choices (two-stage curriculum, mid-training, post-training), making it impossible to attribute any fraction of the strong results to the influence-based mixing specifically. Given that this is presented as a core methodological contribution, the absence of this ablation is a significant gap.

### Minor

- **The "11.7% tokens" comparison with Qwen3-0.6B partially confounds pre-training and post-training**: The post-trained comparison (Table 9) compares models with different post-training pipelines (Tülu-3 + OpenMath/Science/Code-Reasoning vs. Qwen3's proprietary recipe). The base-model comparison in Table 8 is cleaner, but the headline "matches Qwen3-0.6B with only 11.7% of tokens" claim in the abstract and conclusion blends the pre-training efficiency argument with post-training results where the confound exists. The paper would be strengthened by explicitly separating these claims or by noting the confound.

- **The Ask-LLM model used for capability-probing dataset construction is unspecified**: Section 2.1.1 describes using Ask-LLM (Sachdeva et al., 2024) to score samples for reasoning relevance, but does not name which language model was used for this scoring. Since the quality of the capability-probing datasets directly affects the influence score computations that drive the entire data mixing methodology, this is a transparency gap.

- **The blending factors αc,t in Eq. 4 are set heuristically**: The paper assigns linearly increasing weights across checkpoints and uniform weights across capabilities with no justification or sensitivity analysis. Given that these weights aggregate influence signals into the joint influence score that determines the final data mixture, the robustness of this choice matters.

- **Mid-training ablation (Figure 6) is only shown for MMLU**: The data-model co-evolution strategy is evaluated via MMLU, but the paper's stated goal is reasoning (math/code). Showing the effect of subsampling on math or code benchmarks would more directly support the claim that the method benefits the paper's primary objectives.

### Trivial

- The conclusion (line 1164) states results were achieved "without exposing any benchmark data during training or mixture construction," which contradicts the mid-training Benchmark Set in Table 6. This should be corrected to accurately scope the claim to the pre-training data curation method.

- No variance estimates are reported for benchmark numbers. While AIME uses 64 runs (reasonable) and single-run evaluation is standard practice for LLM benchmarks, reporting variance for key results would strengthen confidence, especially for small models where noise can be higher.

## Nice-to-Haves

- A controlled fine-tuning comparison with Qwen3-0.6B-base on the identical post-training data as MobileLLM-R1 would more cleanly isolate the pre-training efficiency claim from post-training confounds. The impracticality of this (Qwen3's pre-training data is proprietary and its post-training recipe is not fully disclosed) is understandable, but acknowledging this limitation would improve clarity.

- A sensitivity analysis of the αc,t blending factors (e.g., uniform vs. linear vs. exponential weighting, and non-uniform capability weights) would strengthen confidence in the influence-based mixing framework.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"Data contamination inflates benchmark results — requires retraining with proper data hygiene and re-evaluation" (from Harsh Critic, Issue 1, framed as fatal)**: The contamination concern is real, but the harsh critic overstates its scope and severity. The mid-training benchmark set is ~0.01–0.97% of a 200B-token phase within a 4.4T-token pipeline, and the headline AIME, LiveCodeBench, and HumanEval results are entirely unaffected. The GSM8K and ARC results are partially confounded, which is a real issue, but it does not "compromise every main result." Kept as a Major weakness with appropriate scope.

2. **"No controlled comparison with Qwen3-0.6B on identical post-training — headline efficiency claim unsubstantiated" (from Harsh Critic, Issue 2, framed as evidential/fatal)**: The paper provides clean base-model comparisons (Table 8) and identical-SFT comparisons with open models (Table 2). The post-training confound is acknowledged implicitly by presenting both base and post-trained results separately. The efficiency claim about pre-training tokens is primarily supported by base-model comparisons. Kept as a Minor weakness noting the confound in the headline claim.

3. **"Ask-LLM scoring with a large (unspecified) model introduces a hidden dependency on a much larger model" (from Harsh Critic, Section 2 note)**: The model used is unspecified, which is a transparency issue. However, this is a standard filtering paradigm and the dependency claim is not unique to this paper—all LLM-based data filtering methods share this property. Kept as a Minor weakness about transparency, not as a hidden dependency critique.

4. **"Influence scores computed from the same model that was trained on that data—a circular process" (from Harsh Critic, Section 3 note)**: This fundamentally misunderstands the method. The iterative process—model trained on data → compute influence → filter data → retrain—is the entire point of data-model co-evolution. The convergence to zero influence is presented as evidence of information exhaustion, not as a bug. REMOVED entirely.

5. **"Leave-one-out analysis uses a single run per ablation with no variance estimates" (from Harsh Critic, Section 2 note)**: Training 8+ models from scratch to 500k steps each is already extremely expensive; running multiple seeds per condition would be prohibitive. This is standard practice for such analyses. REMOVED.

6. **"Table 2 comparison not entirely clean — baseline models use instruct checkpoints vs. intermediate Tulu3-SFT" (from Harsh Critic, Section 4 note)**: The paper explicitly documents this difference in the Table 2 caption (lines 893–898). Using instruct checkpoints for baselines is reasonable since those are the closest available checkpoints to compare against an intermediate Tulu3-SFT stage. REMOVED as a nitpick.

7. **"No statistical error bars in Tables 8 and 9" (from Harsh Critic, Section 4 note)**: Single-run evaluation is standard for LLM benchmarks at this scale. AIME already uses 64-run averaging. REMOVED as a nitpick. Kept only as a Trivial note.

8. **Strength Finder claim: "The proposed mixture...yields consistently lower perplexity...despite these benchmarks not being used during training or data selection"**: This claim is partially contradicted by the mid-training Benchmark Set (Table 6) which does include training data from some of these benchmarks. The pre-training data mixing IS benchmark-free, but the overall pipeline is not. The strength is real for the pre-training phase but needs scoping.

9. **Strength Finder generic claims**: "This paper addressed an important problem" and "targeted an interesting question" — these are generic and not backed by specific evidence. REMOVED.

## Novel Insights

The paper's most genuinely novel insight is the use of **cross-domain influence scores** to simultaneously optimize dataset mixing ratios for multiple heterogeneous capabilities (code, math, knowledge) without accessing benchmark data. Prior work on influence-based data selection typically focuses on a single target task; extending this to a multi-capability setting where Code datasets can be weighted based on their transfer to Math (and vice versa) is a nontrivial conceptual advance. The observation that StarCoder benefits math more than OpenWebMath benefits code (Figure 3) is an intriguing empirical finding that challenges conventional wisdom about the directionality of cross-domain transfer.

## Suggestions

- Acknowledge the benchmark data in mid-training explicitly in the main text (not just the appendix) and either filter it out and re-evaluate, or clearly scope which results may be affected. The uncontaminated AIME and LiveCodeBench results remain strong enough to carry the paper's core claims.

- Add the missing ablation: train a model with uniform sampling (instead of the influence-weighted mixture) through the full pre-training → mid-training → post-training pipeline, and compare on the same final benchmarks. This would directly validate (or qualify) the influence-based mixing as a methodological contribution.

- Specify the Ask-LLM model used and provide brief justification for the linear α blending weights, or include a small sensitivity analysis.

---

## Score and Decision

**Anchor comparison:**

- `yKUbw7q1IA` (6.80, Accept Poster): "How to train data-efficient LLMs" — studied 22 data curation techniques with hundreds of pre-training runs. More rigorous on methodology ablation but narrower in scope (T5-style models, no reasoning focus). MobileLLM-R1 has broader empirical scope and tackles a harder problem (reasoning emergence in sub-billion models) but has the contamination issue and missing ablation that this paper avoids.

- `7xjoTuaNmN` (6.50, Accept Oral): "OpenThoughts" — open data recipes for reasoning models, matched DeepSeek-R1-Distill. Similar spirit of open-source contribution. MobileLLM-R1 has more methodological novelty but weaker evaluation rigor (missing ablation, contamination).

- `2FZC0c06jP` (6.50, Accept Poster): "Can Small Training Runs Reliably Guide Data Curation?" — methodological contribution about proxy model reliability. Comparable in methodological ambition. MobileLLM-R1 has much more comprehensive empirical results but less rigorous validation of its core method.

- `VmEkhV2yCX` (5.00, Accept Poster): "Front-Loading Reasoning" — similar topic space, systematic study of when to introduce reasoning data. MobileLLM-R1 is significantly stronger in empirical scope, model scale diversity, and documentation.

- `GFDSGlEks2` (4.67, Reject): "Impact of Post-training on Data Contamination" — contamination study with controlled experiments. MobileLLM-R1 has far broader empirical contributions and tackles a more ambitious question.

- `5LCCLqJX67` (3.50, Reject): "Thinking Augmented Pre-training" — limited novelty, weak evaluation. MobileLLM-R1 is clearly much stronger across all dimensions.

- `lUkqy21EBB` (3.33, Reject/Withdrawn): "Pushing LLMs to Their Logical Reasoning Bound" — limited empirical scope. MobileLLM-R1 substantially exceeds this.

**Assessment**: This paper makes a genuine contribution with strong empirical results on clean benchmarks (AIME, LiveCodeBench), full reproducibility, and a novel influence-based data mixing framework. The two main weaknesses—benchmark training data in mid-training and the missing downstream ablation for influence-based mixing—are real but do not invalidate the core contribution. The paper sits above the 4.67–5.00 range papers (which had narrower scope or weaker results) and below the 6.50–6.80 papers (which had cleaner evaluations or stronger methodological validation). The contamination issue is the primary factor pulling the score down from the 6.0+ range.

On originality, the cross-domain influence-based mixing and data-model co-evolution are creative contributions. The research question—whether strong reasoning can emerge in small models without massive data—is important and timely. The claims are mostly well-supported, though the influence mixing claim needs the missing ablation. The experiments are sound in scope and coverage. The writing is generally clear, though the contamination acknowledgment needs to move from the appendix to the main text. The value to the research community is high given the full open-sourcing.

**Score**: 5.5

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>