Now I have a comprehensive understanding of the paper. Let me write the final consolidated review.

## Summary

This paper benchmarks how language models internally represent beliefs of self and others, extending prior probing work (Zhu et al., 2024) by evaluating two model families (Pythia, Llama-2) across sizes (70M–70B), base vs. fine-tuned variants, multiple prompt designs, and contrastive activation addition (CAA) for steering. The main findings are: (1) protagonist-belief probing accuracy scales logarithmically with model size for base models (R² > 0.96); (2) fine-tuning yields substantial gains (up to +29%); (3) belief representations are sensitive to prompt variations; (4) PCA-based checks find no strong evidence of probe memorization; and (5) CAA improves ToM reasoning without training probes, outperforming Inference-Time Intervention (ITI).

## Strengths

1. **Systematic scaling analysis of belief representation quality across model sizes**: The paper shows that for protagonist beliefs, best probe accuracy scales logarithmically with model size for base Llama-2 (R² = 0.98) and Pythia (R² = 0.96), and linearly for fine-tuned Llama-2 (R = 1.0). This goes far beyond prior work (Zhu et al., 2024), which tested only two models of the same size. (Section 4.1, Fig. 2, Fig. 5)

2. **First investigation of prompt-variation effects on mental state probing**: The paper defines four prompt variations (Random, Misleading, Time Specification, Initial Belief) and shows that even a variation intended to help (Time Specification) does not improve accuracy, while misleading prompts consistently hurt performance. Prior work used a single fixed prompt, leaving this question open. (Section 3.2.3, Fig. 3)

3. **CAA improves ToM reasoning without training probes and outperforms ITI**: The paper shows that Contrastive Activation Addition (CAA) yields larger and more consistent accuracy gains than Inference-Time Intervention (ITI) across models and tasks (up to +56 points), and that steering vectors transfer to unseen BigToM tasks (Forward Action, Backward Belief). This is a clear advance over ITI, which requires probe training and attention-head selection. (Section 4.4, Table 1)

4. **Memorization in probes is examined via PCA dimensionality reduction**: The paper shows that training probes on only the top 10 principal components (a reduction of up to three orders of magnitude in parameters) recovers most of the original accuracy. This provides concrete evidence that probes are not simply memorizing high-dimensional training data. (Section 4.3, Fig. 4)

5. **Diverse model families with controlled data leakage**: The paper includes Pythia models (trained on the public Pile corpus, released before BigToM) alongside Llama-2, and also tests a fine-tuned Pythia variant. This broadens the evaluation beyond the two closed-source chat models used in prior work and controls for potential test-data leakage. (Section 3.3, model summary table)

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **CAA results lack variance information and hyperparameter sensitivity analysis**: The CAA accuracy improvements in Table 1 (up to +56 points) are reported as single-point numbers without standard deviations, confidence intervals, or any indication of multiple runs. Given that CAA involves a steering coefficient α, the results may be sensitive to this choice. The paper states that hyperparameter details are in the appendix (stripped), but even so, reporting single-point accuracy values without variance makes it difficult to assess whether improvements are robust or fragile. For a benchmarking paper, reproducibility would be strengthened by either multiple runs with different seeds or a sensitivity curve for α. (Section 4.4, lines 293–308)

2. **Probe train/test split sizes and details are not reported**: The paper does not state how many examples are used for training vs. testing the probes, whether the split is stratified, or the total dataset size. Given that probes with up to 16,385 parameters on a dataset of (presumably) a few thousand examples could overfit, reporting the split methodology and train vs. test accuracy would strengthen the analysis. Currently, only test accuracy is shown. (Section 3.2, lines 141–144)

3. **The base-vs.-fine-tuned comparison does not fully isolate the fine-tuning mechanism from data exposure**: The paper compares base models (pre-trained on next-token prediction only) with chat/instruct versions that received additional training on instruction datasets and/or RLHF. The paper's framing (RQ2: "Does fine-tuning with instruction-tuning and/or RLHF have an effect?") implies a causal question, but the experimental design cannot separate the effect of the training procedure from the effect of seeing additional data. This is an inherent limitation of any base-vs.-fine-tuned comparison, and the paper would benefit from explicitly acknowledging it rather than leaving it implicit. (Section 3.3, lines 145–149; Section 4.1, lines 260–263)

### Trivial

1. **The paper does not specify whether the 10 random tokens in the *Random* prompt condition are prepended, appended, or inserted into the belief statement.** The description states "add 10 random tokens to the belief statement" (Section 3.2.3, line 204), which is standard following Gurnee et al. but could be clarified for reproducibility.

## Nice-to-Haves

- **Statistical significance tests for size scaling comparisons**: The paper fits log-linear and linear models and reports R² values, which is good. Adding a simple McNemar's test on paired examples when comparing adjacent model sizes (e.g., Llama-2-7B vs. 13B) would strengthen the claim that larger models genuinely represent beliefs better. This is not a weakness but a nice addition.
- **Transfer of CAA to a different ToM benchmark beyond BigToM sub-tasks**: The paper tests CAA steering vectors on two other BigToM tasks (Forward Action, Backward Belief), which is a reasonable scope. Demonstrating transfer to a benchmark with a different structure (e.g., the one used in Zhu et al.) would further strengthen the generalization claim, but the current evidence is already positive.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Misleading condition changes the classification task"** — REMOVED. The paper clearly describes each prompt variation as modifying the *input* while keeping the same target labels. That is the entire point of a prompt robustness experiment. The probe is trained on the same labels but with modified input; the task design is standard and correctly scoped.

2. **"Memorization check could be more thorough (comparing train/test accuracy curves)"** — REMOVED as a weakness and kept as a nice-to-have. The PCA-based check is a valid and principled approach to detecting memorization. The critic's suggestion about comparing train and test accuracy curves is an alternative method, not a flaw in the existing analysis.

3. **"Statistical tests for size scaling"** — REMOVED as a weakness. The paper already reports R² values with high scores (0.96–1.0). Requesting McNemar's test on paired examples is a reasonable suggestion but not a flaw; it is moved to Nice-to-Haves.

4. **"Random tokens corrupting the belief statement"** — REMOVED. This concern is addressed by the paper: the tokens are added to the belief statement following a standard method from Gurnee et al. (2023). The probing target remains the same, and the variation tests robustness to extraneous input — a standard experimental design.

5. **"Missing appendix content"** — REMOVED per policy. The appendix is stripped by the parser; the original submission contains it. Any criticism about missing details that are explicitly deferred to the appendix cannot be evaluated from the extracted text.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's stated findings and do not surface new interpretations that the authors themselves missed.

## Suggestions

1. Report standard deviations (or confidence intervals) for the CAA and ITI results in Table 1, ideally from 3–5 runs with different random seeds. If computational cost makes this prohibitive, state this explicitly and report at minimum a sensitivity analysis over the steering coefficient α (e.g., α ∈ {0.5, 1.0, 1.5, 2.0}).
2. Add a brief sentence to Section 3.2 specifying the number of examples used for training vs. testing the probes and whether the split is stratified by belief type.
3. Add an explicit acknowledgment in the Limitations section that the base-vs.-fine-tuned comparison confounds training procedure with additional data exposure, and that the finding should be interpreted as "models that have undergone additional training with instruction-following and human feedback show better representations" rather than a causal claim about fine-tuning as a technique.
4. Clarify in the *Random* prompt description whether the 10 random tokens are prepended, appended, or inserted.

## Score and Decision

**Originality**: Moderate — the paper extends a known probing methodology to new dimensions (scale, prompt variation, CAA) rather than introducing a fundamentally new technique. The prompt-variation study for ToM probing is novel.

**Importance of research question**: High — understanding how LMs internally represent mental states is important for safety, alignment, and capability assessment.

**Claims supported**: Yes — the five RQs are each addressed by appropriate experiments, and the conclusions track the results. The main weakness is the absence of variance information for the CAA results.

**Soundness of experiments**: Good — the experimental design is sensible and follows established probing methodology. The PCA memorization check is a nice addition. Variance and split details are the main gaps.

**Clarity of writing**: Strong — the paper is well-structured, the RQs are clearly stated, figures are informative, and the text accurately describes the results.

**Value to the research community**: High — the paper provides a useful empirical reference point for the community studying ToM in LMs, including scaling trends, prompt sensitivity, and a practical demonstration of CAA for steering.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>