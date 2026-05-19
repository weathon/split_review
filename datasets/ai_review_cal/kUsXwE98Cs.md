- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 1, 3, 5
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes AutoBench-V, an automated framework for benchmarking Large Vision-Language Models (LVLMs) on demand. The pipeline takes a user-specified evaluation capability (e.g., "spatial understanding"), uses GPT-4o to hierarchically generate evaluation aspects and image descriptions, employs Flux-pro for text-to-image generation with a self-validation step, and produces VQA test cases. The framework is evaluated on seven LVLMs across five user inputs, with additional experiments on examiner fairness, position bias, and human evaluation of generation quality.

## Strengths

1. **Principled pipeline design addressing real challenges in automated LVLM evaluation.** The paper identifies and explicitly tackles several genuine problems: reducing repetition in generated aspects (hierarchical generation with semantic graph diversity constraint), mitigating self-enhancement bias (generating questions from text descriptions rather than images), ensuring image-description alignment (self-validation via VQA), and handling position bias in multiple-choice answers. The modular pipeline (aspect generation → description → image generation with validation → Q&A with error control) is coherent and well-motivated.

2. **Examiner priority experiment tests an important form of bias (Section 4.2, Figure 3).** The paper validates that when all models are given only text descriptions (withholding images), their accuracy is nearly identical — variance of 0.4% on easy questions and 2.4% on hard questions. This provides direct evidence that the generated questions do not contain text-level bias favoring GPT-4o, supporting the claim that the description-based generation strategy mitigates answer leakage.

3. **Position bias analysis and mitigation (Section 4.6).** The paper identifies that LLM-generated reference answers tend to cluster around option A, and manually enforces an even distribution of correct answers across all options. The deviation analysis (e.g., GLM-4V showing \(R_A=-19\%\) when answers are concentrated at A vs evenly distributed) demonstrates that this is a real concern and that the mitigation is justified.

4. **Comprehensive model evaluation across difficulty levels.** The paper evaluates seven models and presents performance breakdowns by difficulty (easy/medium/hard) and by capability dimension (basic, spatial, semantic, reasoning, atmospheric understanding). Results show meaningful patterns — e.g., LVLMs excel at semantic and atmospheric understanding but struggle with spatial reasoning, and performance gaps widen as difficulty increases — that are consistent with expectations and lend face validity to the benchmark.

## Weaknesses

### Fatal
None.

### Major

1. **The fairness claim is only partially supported. The key experiment tests text-level bias but not description-level or benchmark-level validity.** The paper argues (Section 4.2) that generating questions from text descriptions eliminates self-enhancement bias, and validates this by showing models perform similarly on text-only inputs. However, this experiment only shows that the *text portion* of the benchmark is not discriminatory. It does not address whether GPT-4o (as the description writer) generates descriptions that favor its own visual processing style — e.g., foregrounding visual features it excels at recognizing while underemphasizing features other models handle better. A stronger test would use a different examiner model and check if rankings are consistent, or compare rankings against an independently constructed benchmark. As it stands, the paper's central claim about fairness is established for one specific bias pathway but the broader fairness claim remains unvalidated.

2. **No comparison to existing benchmarks or alternative evaluation methods.** The paper evaluates seven models but never asks whether the resulting rankings correlate with established benchmarks such as MMBench, MME, or SEED-Bench. Without this comparison, the results are uninterpretable in context: if the ranking matches existing benchmarks, the contribution is a more expensive replication; if it differs, the paper needs to explain why AutoBench-V should be trusted over established measures. This is the most consequential gap in the experimental validation — the paper demonstrates that the framework *can* produce numbers, but not that those numbers are meaningful.

### Minor

1. **Table 1's metric is undefined.** The caption of Table 1 (labeled `tab:effectiveness`) reads "Effectiveness of hierarchical aspect generation under various hyperparameter settings" and reports numbers labeled "Raw" and "+Hierarchy." The paper states that the best configuration (m=4, n=6) "yields the highest diversity," but the numbers are presented as accuracy-like values (0.767, 0.786, etc.) without any definition of what is being measured — accuracy of what on what task? The reader cannot interpret the table without this information.

2. **Self-validation process has a potential circularity concern and is underspecified (Section 3.3).** The self-validation uses GPT-4o to generate validation questions about the generated image, then calculates alignment as the ratio of "correctly answered questions." It is not specified which model answers these validation questions. If GPT-4o both writes the description and validates whether the image matches it, the validation may be biased toward confirming its own descriptions. The paper cites TIFA but does not clarify whether a separate evaluator (a different model or human) is used for the answer-checking step.

3. **"First automated framework" claim is overstated given cited related work.** The paper claims AutoBench-V is "the first automated framework for benchmarking LVLMs' capability" (line 35), yet the related work section (line 58) cites Task Me Anything (Zhang et al., 2024), described as a framework for "assessing LLM/LVLMs performance across diverse tasks." Without a clear and explicit differentiation, the "first" claim is too strong and should be qualified.

4. **Position bias analysis makes broad claims from limited evidence (Section 4.6).** The paper claims "position bias becomes more evident with increasing question difficulty" but discusses numerical results only for GLM-4V (deviation rates of \(R_A=-19\%\), \(R_D=-8\%\)). The figure presumably shows data for other models, but the text does not confirm whether the trend is monotonic or consistent across the model set. The generality of the claim is not supported by the presented analysis.

### Trivial

- **Algorithm 1's exclusion mechanism (removing top-\(e\) degree nodes at iteration \(e\)) is not well-justified.** The number of removed nodes equals the iteration number, which is presented without principled motivation. A brief justification or ablation would clarify the design choice.

## Nice-to-Haves

- **Comparison to at least one established LVLM benchmark** (e.g., reporting Spearman correlation of rankings) would substantially strengthen the paper's claims about benchmark validity.
- **Examiner replacement experiment:** Regenerating a subset of evaluation cases using a different examiner model (e.g., Gemini-1.5-Flash or Claude-3.5-Sonnet) and checking rank consistency would directly address the fairness concern.
- **Cost/API analysis:** Reporting the computational or monetary cost of a full evaluation run would help readers assess practicality and reproducibility.
- **Difficulty calibration via human pilot:** A small human study on a subset of questions would validate the difficulty grading mechanism beyond the circular model-performance-based validation.
- **Sensitivity analysis on the self-validation threshold \(\zeta\)** would clarify whether results are robust to this hyperparameter choice.

## Removed Points

These points were flagged for removal; treat them with caution.

1. **Complaint about human evaluation being underspecified (Section 4.5).** The paper explicitly references "\autoref{humaneval detail}" for details on human evaluation. This points to an appendix that was stripped by the PDF parser. Per policy, weaknesses about missing appendix content that exists in the original submission are removed. *(From Harsh Critic, Critical Issue #4)*

2. **Complaint about missing statistical rigor in human evaluation (confidence intervals, inter-annotator agreement, etc.).** These details are standard for appendix content. The paper's main-text presentation of alignment rates is appropriate for a conference paper format where detailed annotation protocols go in the appendix. *(From Harsh Critic, Critical Issue #4)*

3. **Complaint about the model exclusion being "survivorship bias" (Section 4.1).** The paper tests but excludes LLaVA-1.6 and MiniGPT-4 because they "performed poorly" and their "capabilities differ significantly." While the justification could be more detailed, the primary evaluation already covers 7 models including both proprietary and open-source. Excluding near-floor models from the main analysis does not introduce survivorship bias into any claim; the paper's conclusions are explicitly about the models tested. This is a presentation detail, not a methodological flaw. *(From Harsh Critic, Critical Issue #3, demoted from the main review)*

4. **Weakness about reproducibility/disclosed hyperparameters.** The reviewer complains about specific values not being justified (e.g., \(\zeta\) thresholds). These are standard hyperparameter choices with reasonable justification in the paper. *(From Harsh Critic, "Strengthening the Paper" section)*

5. **Complaint about "dynamic benchmarks" comparison (DyVal/DyVal2).** The paper already covers these in the related work section; requesting additional explicit comparison for the visual modality is scope creep beyond what the paper attempts. *(From Harsh Critic, "Missing Parts" section)*

6. **Strength about Table 1 providing "direct evidence" of diversity.** The metric in Table 1 is undefined, so the claim of direct evidence is unsupported. The hierarchical approach is a genuine design contribution, but the supporting table cannot be interpreted as presented. *(From Strength Finder, Core Strength 1 — kept partially but moved because the table's ambiguity undermines the strength claim)*

## Novel Insights

The harsh critic raises a genuinely insightful point that the paper's own analysis does not surface: the fairness validation experiment (Section 4.2) tests and rules out *text-level* answer leakage, but this is only one of at least two distinct pathways for self-enhancement bias. The second pathway — whether the descriptions GPT-4o generates emphasize visual features it handles well and underrepresent features other models handle better — is not addressed and would require a different experimental design (e.g., swapping the examiner model and checking rank consistency). This distinction between *generation-level bias* (what the harsh critic calls "description-level bias") and *text-level bias* is a conceptual contribution that goes beyond what the paper itself articulates and provides a concrete direction for future work on automated evaluation fairness.

## Suggestions

1. **Most impactful single addition:** Compare AutoBench-V's model rankings against at least one established benchmark (e.g., MMBench, MME, or SEED-Bench) and report Spearman correlation. This would transform the results from uncontextualized numbers into validated measurements.

2. **Run an examiner replacement experiment on a subset of cases.** Use Gemini-1.5-Flash or Claude-3.5-Sonnet as the examiner to regenerate evaluation cases for one user input dimension, and verify that model rankings are consistent. This directly addresses the fairness concern.

3. **Clarify the metric in Table 1.** Define what "Raw" and "+Hierarchy" accuracy values represent — are they measuring diversity, relevance, non-repetition, or something else? Without this definition, the table is uninformative.

4. **Qualify the "first" claim** to acknowledge Task Me Anything and other related automated approaches, making explicit the specific novelty (e.g., full end-to-end automation including image generation) that differentiates AutoBench-V.

5. **Specify which model answers the self-validation VQA questions** in Section 3.3, and if it is GPT-4o, discuss the circularity concern or provide evidence that the validation is still meaningful.
