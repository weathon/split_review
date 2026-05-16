Now I have thoroughly verified the paper content against all reviewer claims. Let me construct the final consolidated review.

---

## Summary

This paper proposes using the complexity of generated visual programs as a proxy for question difficulty in VideoQA. It introduces CodePlexity, a method that mines common subroutines from program ASTs and learns which ones correlate with model failures, yielding both a quantitative complexity metric and interpretable insights (e.g., temporal ordering and fine-grained object details are universally hard). The paper also uses CodePlexity to select hard questions from generated candidates, creating CodePlex-QA — a new benchmark that is 1.9× harder than NExT-QA for existing models.

## Strengths

1. **Clever and well-motivated core idea with strong initial evidence**: The insight that generated code (an intermediate artifact of code-based VQA methods) carries richer structural information about question difficulty than the natural language question itself is original and compelling. The human study (Figure 3, left) cleanly demonstrates that even expert subjects misjudge difficulty — questions rated "average" are actually the hardest — establishing a clear motivation for an automated approach. The finding that even simple code metrics (cyclomatic complexity) outperform human estimates is immediately convincing and well-presented.

2. **Interpretable mining of difficulty patterns that generalize across architectures**: CodePlexity's subtree analysis (Section 3.3) goes beyond a black-box difficulty score to identify specific programming patterns tied to model failures. The Venn diagram (Figure 4) shows 8 subroutines shared across three diverse architectures (SeViLA, ViperGPT, VIOLET), and the qualitative findings — that temporal ordering and fine-grained object extraction pose universal challenges — align with known weaknesses in VideoQA. This is a genuinely useful diagnostic tool that no prior text-based or perceptual-difficulty approach provides.

3. **Rigorous evaluation on held-out models**: The paper splits 8 models into training (4) and held-out validation (4) sets, using mPEG (averaged over difficulty quantiles) as the evaluation metric. CodePlexity consistently outperforms all baselines (LoC, cyclomatic complexity, BERT, dependency-tree depth, GPT-4) on all held-out models (Table 1), demonstrating that the learned complexity signal generalizes beyond the models used to train it. This design prevents overfitting to specific architectures.

## Weaknesses

### Fatal

None.

### Major

1. **Benchmark validation confounded by domain shift (Section 5)**. The paper's claim that "CodePlex-QA is 1.9 times harder than NExT-QA" compares model performance on CodePlex-QA (questions generated from MOMA, ActivityNet, ActionGenome videos) versus NExT-QA (questions from a different set of videos). Because the source videos differ in content, length, and distribution, the performance gap could partially reflect domain differences rather than the complexity-filtering mechanism. The paper lacks a within-dataset control: comparing model performance on high-Complexity vs. low-Complexity subsets from the *same* pool of generated questions (e.g., questions above vs. below threshold δ). Without this, the central applied contribution — that CodePlexity can *automatically construct* a harder benchmark — rests on incomplete evidence. This is fixable (a within-pool ablation would directly test the claim), but the paper as written does not support it.

### Minor

1. **Multiple comparison correction absent in subtree analysis (Section 3.3/4.3)**. The paper tests thousands of subtrees using a p<0.01 threshold without any correction (Bonferroni, FDR, permutation testing). This inflates the number of individually "significant" subtrees. However, the paper's most important finding — the *intersection* of 8 subroutines shared across three models — is substantially more robust than the individual sets, because the probability that a false positive appears independently in all three model analyses by chance is very low. The qualitative takeaways (temporal ordering, fine-grained details) are also consistent with prior literature. The lack of correction weakens the *individual* subtree lists but does not threaten the paper's core claims. The authors should report corrected p-values or acknowledge this limitation.

2. **Thin margins over simpler baselines for some held-out models (Table 1)**. For Tarsier, CodePlexity (0.164) narrowly beats cyclomatic complexity (0.163); for InternVideo, the gap is 0.234 vs 0.218. Without confidence intervals or bootstrapped errors, it is unclear whether CodePlexity's advantage is statistically meaningful for these individual models. While the *consistent advantage across all held-out models* is reassuring, reporting uncertainty would strengthen the comparison.

3. **No discussion of program generation failures.** The paper does not report how many NExT-QA questions ViperGPT failed to produce valid programs for, or whether those questions were excluded. If non-code-generatable questions are systematically different (e.g., ones requiring different reasoning), this could bias the analysis toward questions with code-amenable structure. The authors should report the coverage rate and discuss potential selection bias.

4. **Potential overlap confound in the training and generation pipelines.** CodePlexity is trained on programs from NExT-QA (using ViperGPT) and then applied to evaluate complexity of questions from different datasets. Since ViperGPT is also used to generate programs for the new benchmark questions, and the LLM prompter for question generation may produce questions with similar linguistic patterns to NExT-QA, CodePlexity could be biased toward assigning high complexity to questions that look "unusual" relative to NExT-QA rather than genuinely hard. This confound is not discussed.

### Trivial

- The threshold δ is described as "calibrated on NExT-QA" without specifying the calibration procedure (e.g., do the authors compute CodePlexity scores on NExT-QA and set δ to keep the top 10%, then apply the same threshold to new questions?). This should be clarified.
- Logistic regression is used without mention of regularization (L1/L2) for high-dimensional sparse one-hot features. This is a minor implementation detail that does not affect the validity of the metric evaluation.

## Nice-to-Haves

- A within-dataset validation (see Major weakness #1): compare model performance on the top-X% hardest generated questions (by CodePlexity) vs. a random subset of equal size from the same generation pool.
- Report bootstrapped confidence intervals for mPEG values in Table 1 to quantify uncertainty.
- Report the fraction of NExT-QA questions for which ViperGPT successfully generated a program, and the impact on the complexity analysis.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The manual filtering of 12% of questions introduces selection bias"**: The paper explicitly states that manual filtering only removes question/answer pairs that are unanswerable due to captioning errors or LLM hallucination — standard dataset quality assurance, not selection on difficulty. The 12% is modest and the pipeline is described as "fully automatic pipeline is capable of producing useful datasets by itself" (line 110), which is a reasonable characterization. **Reason for removal**: the criticism mischaracterizes a standard quality-control step as a methodological flaw.

- **"The claim that the pipeline is 'fully automatic' is overstated"**: The paper explicitly acknowledges the manual filtering step (line 110) and qualifies that the *automatic part* is "capable of producing useful datasets by itself." The word "fully automatic" is not used to describe the complete pipeline. **Reason for removal**: strawman — the paper does not claim what the reviewer says it claims.

- **"The model split is arbitrary"**: Any split of 8 models into train/validation is to some degree arbitrary. The split covers diverse architectures (contrastive pre-trained, code-based, frame-selection, GNN-based) and the held-out set contains 4 models including the strongest (Tarsier). **Reason for removal**: this is a judgment call where the paper's design is reasonable.

- **"No analysis of program generation failures"** and **"Overlap between training/evaluation datasets"**: Moved here from Minor because these are secondary concerns that don't affect the paper's main contributions. Kept as Nice-to-Haves instead.

- **Strength from Strength Finder about benchmark generation**: The Strength Finder claimed "Automated generation yields a benchmark 1.9× harder than manually designed ones" as a core strength. This conflicts with the verified Major weakness (the cross-dataset comparison is confounded). **Reason for removal**: the weakness wins; the claim is not well-supported as presented.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel observation: the paper's "bottom-up" approach (mining code structure for complexity) stands in contrast to the dominant "top-down" paradigm in benchmark design (experts hypothesize what is hard and construct examples targeting those skills). The reviews collectively recognize that this paradigm shift is the paper's most distinctive contribution, but they also correctly note a pattern: the paper's validation of its benchmark-generation application inadvertently reintroduces a top-down assumption — that a single complexity threshold learned on one dataset (NExT-QA) will transfer to entirely different video domains. This tension between the bottom-up philosophy of the method and the top-down flavor of the validation is an interesting meta-observation that the paper could productively address in future work.

## Suggestions

1. **Add a within-dataset ablation**: Take the full pool of generated question candidates (before CodePlexity filtering), compute CodePlexity scores for each, and compare model performance on the top-X% (high complexity) vs. bottom-X% (low complexity) subsets. If the performance gap is large, this directly validates that CodePlexity selects genuinely harder questions regardless of video domain.

2. **Report corrected p-values or permutation tests for the subtree analysis**, or at minimum acknowledge the lack of multiple-comparison correction and note that the intersection across models provides some protection.

3. **Add uncertainty quantification** (confidence intervals or bootstrapped errors) to Table 1's mPEG values to clarify whether CodePlexity's advantage over cyclomatic complexity is statistically meaningful, especially for the models with the narrowest gaps (Tarsier, InternVideo).

## Score and Decision

The paper introduces a genuinely novel approach — using generated code complexity as a proxy for VideoQA question difficulty — with compelling initial evidence (human study, Figure 3; held-out model evaluation, Table 1). The interpretable subtree analysis provides actionable insights that go beyond black-box metrics. However, the validation of the benchmark-generation claim (a stated core contribution) is confounded by domain shift and lacks within-dataset controls, and the subtree analysis has an unaddressed multiple-comparison issue. These are fixable but material weaknesses. Overall, the paper's primary contributions (the complexity estimation method and the interpretable analysis) are well-supported and valuable; the benchmark claim requires strengthening.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>