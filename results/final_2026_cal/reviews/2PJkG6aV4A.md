Now I have a good calibration. Let me write the final consolidated review.

## Summary

This paper proposes a guardrail-agnostic evaluation framework for societal bias in LVLMs. The core idea is elegant and practical: replace attribute-inferring prompts (which trigger safety refusals) with person-irrelevant prompts (e.g., "Write a fictional story"), attaching images only as provisional user context. This achieves zero refusals across all 20 tested models (both open-source and proprietary), enabling bias measurement where prior benchmarks fail. The evaluation covers three tasks (story generation, term explanation, exam-style QA) on gender and racial bias, revealing that all models exhibit bias—though proprietary models show lower scores—and that bias patterns are task-specific.

## Strengths

1. **Novel, practically-motivated methodology that solves a concrete, growing problem**: The guardrail-agnostic approach directly addresses the critical blind spot that attribute-inferring prompts trigger refusals in safety-aligned models (Table 1 shows prior benchmarks have 35–100% refusal rates for GPT-5 and Claude 3.7 Sonnet; the proposed method achieves 0% for all models). The idea of decoupling the task from the depicted person by using person-irrelevant prompts with images as user context is conceptually clean and clearly explained (Section 3.1, Figure 1).

2. **Comprehensive empirical evaluation across 20 models and three diverse tasks**: Table 2 provides gender and racial bias scores for 16 open-source (7B–38B) and 4 proprietary LVLMs across story generation, term explanation, and exam-style QA. This breadth enables systematic comparison and supports the claim that all models exhibit bias while proprietary models tend to show lower scores. The analysis of task-specific bias patterns (Observations 2.3–2.5) goes beyond a single score to reveal meaningful structure.

3. **Concrete demonstration of biased outputs with qualitative examples**: Figure 2 gives vivid illustrations (GPT-4o generating *mechanic* for male users vs. *nurse* for female users; Claude 3.7 Sonnet providing more technical NLP explanations for male/White users than female/Southeast Asian users) that ground the TVD scores in tangible behavior. The Appendix figures (10, 11) further support the quantitative findings.

4. **Analysis revealing that bias is not monolithic**: The correlation analysis (Figure 3) demonstrates weak cross-task correlations (−0.11 to 0.21) and strong gender-race interdependencies (0.49–0.93), making the point that evaluations must use diverse tasks and address multiple demographic axes simultaneously. This is a practically useful finding for practitioners.

## Weaknesses

### Fatal
None.

### Major

1. **No uncertainty quantification for bias scores**: The TVD scores in Table 2 are reported as point estimates with no confidence intervals, standard errors, or significance tests. For story generation, scores are derived from 500 generated stories per group via an LLM-based attribute extractor; for term explanation, from 12,000 pairwise comparisons. Key comparative claims (e.g., "proprietary models show lower bias") rest on differences of a few TVD points (e.g., 14.53 vs. 21.57 for story gen gender bias) that could fall within sampling variability. Without bootstrapped intervals or permutation tests, the strength of evidence for the paper's central comparisons is unclear. This is especially important because the paper's contribution is partly empirical—it wants to tell the community something about which models are more/less biased.

2. **Exam-style QA bias metric is underspecified**: The paper states that the per-domain bias score is "computed with the TVD metric as the deviation of accuracies {Acc_a} from their mean" (Section 3.2). TVD is defined for probability distributions, not as deviation from a mean of scalars. The exact formula needs to be stated explicitly (e.g., is it ½Σ_a|Acc_a − μ|? is it |Acc_female − Acc_male|? or something else?). Without this, the exam-style QA results are not replicable, and it is unclear whether the metric faithfully captures "unfair influence of demographics on reasoning ability." The paper's own exclusion of LLaVA-1.6 variants from this task due to "near-random accuracies leading to misleadingly low bias scores" (Table 2 caption) further indicates that the metric's behavior in low-performance regimes needs discussion.

### Minor

1. **Figure 3 caption is confusing and potentially mislabeled**: The caption lists "Story Gen. to Exam QA (r = −0.11), Exam QA to Story Gen. (r = 0.11)" for gender bias correlations. Pearson correlation is symmetric—two different values for the same task pair should not occur. While the main text correctly states that task-wise correlations are weak (−0.11 to 0.21 range) and the actual findings are coherent, the caption as presented is confusing. This appears to be a labeling/presentation error rather than a computational error, but it should be corrected with a proper correlation matrix and clear annotation of which values correspond to task-wise vs. gender-race correlations.

2. **Section 5 discussion of continuous monitoring as a bias-reduction factor is speculative**: The paper argues that "continuous monitoring and iterative refinement" explains lower bias in proprietary models, but acknowledges this is a hypothesis ("we argue," "a plausible explanation"). The comparison with Gemma3 (explicit safety training but still high bias) is a fair counterpoint, but the discussion would benefit from a clearer separation between what the data support and what is conjecture. This is a minor issue because the paper appropriately hedges its language.

3. **Lack of null-distribution baseline for interpreting TVD scores**: The TVD values in Table 2 range from 0.36 (GPT-5, exam race) to 48.03 (InternVL3.5-14B, story gender). Without a baseline established by shuffling demographic labels and recomputing scores, it is difficult for readers to calibrate what constitutes a "large" vs. "small" bias score. A simple permutation-based null distribution would clarify whether a score like 0.36 is trivially zero or still indicative of systematic bias.

### Trivial
None.

## Nice-to-Haves

- **Control for image-level confounds beyond demographics**: The paper already acknowledges contextual confounds (Section 2) and controls for non-target demographic distributions. However, a brief discussion or simple experiment (e.g., comparing bias scores with blank placeholder images) would further strengthen the claim that observed disparities come from demographic cues rather than correlated image features like background or clothing.
- **LLM assistant agreement statistics in the main paper**: The paper states in Section 4.1 that Qwen3-32B judgments align well with human judges (Appendix D). Including the actual agreement statistics (e.g., Cohen's kappa) in the main paper would transparently bound the measurement noise introduced by the attribute extractor.

## Novel Insights

The finding that bias is task-specific (weak cross-task correlations) while gender and racial biases are strongly interdependent (r = 0.49–0.93) is a non-obvious result with practical implications: it means a single bias score or task cannot proxy for overall model fairness, but addressing one demographic axis may partially address others. This insight emerges cleanly from the three-task design and is well-supported by the data.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Three queries retrieved anchors across score bands. Weak band (score < 3.5): four papers on bias in VLMs with avg scores 0.67–3.00. Middle band (3.5–7.5): four papers with avg scores 4.50–5.50. Strong band (>7.5): four papers with avg scores 8.00 (but on unrelated topics). Initial bracket: **4.0–7.0**.

**Round 2 (Narrowing):** Three queries within the bracket retrieved anchors including "Vision Language Models are Biased" (5.50, Accept Poster), "Revealing ICL Gender Bias in LVLMs" (5.33, Reject), "Benchmarking Bias Mitigation" (5.50, Accept Poster), "Fair in Mind, Fair in Action" (6.50, Accept Poster), and "IndicVisionBench" (6.00, Accept Poster). The paper under review compares favorably to the 5.5 anchors—it has a more novel methodology (solving the refusal problem rather than just measuring or mitigating known biases), broader model coverage (20 vs. 4–5 models), and clearer practical impact. It is slightly weaker than the 6.5 anchor ("Fair in Mind, Fair in Action") on theoretical framing but stronger on methodological clarity and direct practical applicability. **Final score: 6.5.**

**Anchor details:**
- DG4S2OlGQA (5.50): Narrow counting-focus bias benchmark; less novel methodology than this paper.
- 3rO59y6pgO (5.33): ICL gender bias; only 4 models, 2 tasks, no guardrail-agnostic innovation.
- GLPmZhhCAE (5.50): Bias mitigation benchmark; useful but confirms known findings, less novel than this paper.
- NYphgYTloq (6.50): Comprehensive fairness framework but over-engineered; this paper is cleaner and more directly applicable.
- bKkdttFgYQ (3.00): Object-state bias; weak methodology, poor "bias" framing—this paper is far stronger.
- LmJoLn04iL (6.00): Cultural benchmark; comparable in scope and rigor to this paper.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>