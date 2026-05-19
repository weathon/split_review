## Summary
# Final Review Report

## Summary

This paper proposes Delta, an inference-time method that mitigates text hallucinations in LLMs using contrastive decoding with random input masking. The core idea is to compare the model's output distribution on the original input versus a randomly masked version, then subtract the masked logits to reduce hallucination-prone tokens. The method requires no retraining or additional data. Experiments on SQuAD v1.1/v2, TriviaQA, and Natural Questions show absolute exact match improvements of 2–14.5 percentage points under sampling decoding, with larger gains on SQuAD v2's "no answer" subtask. However, the method shows marginal or negative results without sampling and on context-free benchmarks (CommonsenseQA, MMLU).

The paper addresses a timely problem and proposes a straightforward, intuitive approach. However, several significant issues limit its current contribution: (1) the central claim of "hallucination mitigation" is inferred from QA accuracy metrics rather than directly measured; (2) the core assumption that masking amplifies hallucinations is unvalidated; (3) the claimed "computational efficiency" is contradicted by the requirement of an extra forward pass per generation step, with no overhead analysis; (4) experiments lack variance reporting and comparison with the most closely related method (CAD); and (5) a type inconsistency in the APC constraint description could affect reproducibility. These issues are fixable with additional experiments and more cautious claims, but in their current form, the paper needs substantial revision before acceptance.

## Strengths
1. **Timely and practical problem.** Hallucination in LLMs is a critical challenge, and the paper addresses it with an inference-only solution that requires no retraining or additional data, which is attractive for deployment.

2. **Simple and intuitive mechanism.** The core idea of contrasting original and masked input logits is conceptually clean, easy to understand, and could offer a practical alternative to more complex training-based approaches.

3. **Honest limitation disclosure.** The paper explicitly acknowledges that Delta does not improve context-free tasks (CommonsenseQA, MMLU) and shows marginal gains without sampling. This transparency is commendable and strengthens the paper's trustworthiness.

4. **Reasonable empirical gains under sampling.** On SQuAD v2 (no-answer EM), Delta achieves 14.53 and 11.81 percentage point improvements under sampling and non-sampling, respectively. These are practically meaningful for a method that requires no retraining.

5. **Ablation study on key hyperparameters.** The ablation over masking ratio and logit ratio α shows consistent gains across tested configurations, suggesting the method is not overly sensitive to hyperparameter choice.

## Weaknesses
1. **Unvalidated core assumption.** The paper asserts that masked-input logits represent "hallucinated" content without empirical evidence. The claim that masking amplifies hallucinations is supported only by a single anecdotal example (banana color), not systematic analysis. The method could be improving accuracy through other mechanisms (e.g., entropy reduction, denoising, regularizing the output distribution) that are unrelated to hallucination-specific suppression. (Issue annotation: Page 4 - Section 3.4)

2. **No direct hallucination measurement.** The paper evaluates on QA accuracy (Exact Match, F1) but claims to "mitigate hallucinations." These are not equivalent — a model can improve QA accuracy by being more conservative without reducing hallucination rates in open-ended text. Dedicated hallucination benchmarks (TruthfulQA, HaluEval, FActScore) are absent. (Issue annotation: Page 1 - Abstract; Page 7 - Section 5.1)

3. **Oversold computational efficiency.** The abstract and introduction describe Delta as "computationally efficient" and "easily deployable in real-time systems," but Delta requires an additional forward pass through the LLM for the masked input at each generation step, effectively doubling the inference compute. No latency, FLOPs, or throughput analysis is provided. (Issue annotation: Page 1 - Abstract; Page 1 - Section 1)

4. **Missing comparison with closest baseline (CAD).** Context-Aware Decoding (Shi et al., 2024) is the most closely related work — both are inference-only contrastive decoding methods. The paper dismisses CAD as "mainly based on context-driven datasets" without justification, and no direct experimental comparison is conducted. This omission makes it impossible to assess Delta's incremental value. (Issue annotation: Page 2 - Related Work)

5. **APC type inconsistency.** Equation (4) defines V_head as a set of tokens (vocabulary items), but the text in Section 3.6 describes checking "the sequence z" against a "set of plausible sequences." This is a type mismatch that could lead to implementation errors. (Issue annotation: Page 5 - Section 3.6)

6. **No statistical significance.** All results are single-point estimates without variance, confidence intervals, or multi-seed experiments. Given that the claimed gains range from 2 to 14.5 percentage points and baseline variances are unknown, statistical reliability cannot be assessed. (Issue annotation: Page 6 - Section 4.2)

7. **TriviaQA/NQ results are conditional on sampling.** Delta underperforms the baseline without sampling on TriviaQA (48.27 vs 48.13) and shows marginal changes on NQ. The paper's narrative emphasizes the sampling-condition improvements while glossing over the negative results. (Issue annotation: Page 7 - Section 5.2)

8. **Promotional language.** Terms like "powerful solution," "remarkable improvements," and "easily deployable" inflate the contribution beyond what the evidence supports. (Issue annotation: Page 8 - Section 7)

## Key Issues
### Issue 1: Core mechanism unvalidated (Severity: Major, Fixability: High)
The paper's central hypothesis — that masked-input logits specifically capture hallucination-related tokens — is not validated empirically or theoretically. The "banana" example is anecdotal. Without evidence that masking systematically amplifies hallucination probability (rather than just adding noise), the claimed mechanism remains speculative. **Fix:** Add per-token analysis showing that masking increases probability of factually incorrect tokens more than contextually correct ones; add a control experiment using random logit perturbation instead of masking.

### Issue 2: Hallucination-evaluation gap (Severity: Major, Fixability: Medium)
Delta is evaluated on QA accuracy metrics (EM, F1) but claims to "mitigate hallucinations." These metrics are only weak proxies for hallucination. A model could improve EM by becoming more conservative or by guessing more accurately, without reducing the rate of fabricated content. **Fix:** Evaluate on dedicated hallucination benchmarks (TruthfulQA, HaluEval, FActScore) that directly measure factual consistency.

### Issue 3: Oversold efficiency without overhead analysis (Severity: Major, Fixability: High)
The paper repeatedly claims computational efficiency while Delta requires 2× forward passes. No latency, throughput, or memory analysis is provided. **Fix:** Report inference time (ms/token), FLOPs, and peak GPU memory for baseline vs. Delta; honestly describe the compute trade-off.

### Issue 4: Missing comparison with CAD (Severity: Major, Fixability: Medium)
Context-Aware Decoding (Shi et al., 2024) is the closest prior art — also inference-only contrastive decoding. The paper's claim that CAD is "less generalizable" is unsubstantiated. A direct empirical comparison is essential to demonstrate Delta's incremental value. **Fix:** Add CAD as a baseline across all datasets under identical settings.

### Issue 5: APC type inconsistency (Severity: Major, Fixability: High)
Equation (4) defines V_head as a set of tokens, but Section 3.6 text describes checking sequences against V_head. This type confusion can lead to implementation errors. **Fix:** Rewrite Section 3.6 to consistently treat V_head as a set of next-token candidates, not sequences.

### Issue 6: No statistical significance (Severity: Major, Fixability: High)
All results are single runs without variance. Confidence intervals or multi-seed experiments are essential for reliable comparison. **Fix:** Report mean ± std over at least 3 seeds; add paired significance tests where appropriate.

## Actionable Suggestions
### S1. Revise Title and Abstract (Must)
**Current:** "DELTA - Contrastive Decoding Mitigates Text Hallucinations in Large Language Models"
**Problem:** The title claims hallucination mitigation but the paper only evaluates QA accuracy.
**Revised Title:** "DELTA: Contrastive Decoding with Input Masking for Improved Context-Grounded QA in LLMs"
**Abstract revision:** Replace "computationally efficient and scalable" with "inference-only (requiring one additional forward pass per token)" and replace "mitigates hallucinations" with "improves QA accuracy on context-rich benchmarks."

### S2. Add Direct Hallucination Benchmarks (Must)
Evaluate Delta on at least two of the following:
- **TruthfulQA** (measures truthfulness, directly relevant)
- **HaluEval** (hallucination detection benchmark)
- **FActScore** (factual consistency of generated text)
Report both accuracy/consistency metrics and hallucination rate (percentage of factually incorrect claims).

### S3. Add CAD as Direct Baseline (Must)
Run CAD (Shi et al., 2024) on the same six datasets under identical settings (Llama 3.1 8B, same quantization, same decoding parameters). Report results in Table 1. Discuss the differences: CAD removes entire context, Delta masks random tokens. Analyze which strategy works better for which type of question.

### S4. Report Computational Overhead (Must)
Add a table reporting:
- Inference time (ms/token) for baseline vs. Delta
- Peak GPU memory (GB)
- FLOPs per generation step
- Throughput (tokens/second)
Under both sampling and non-sampling settings.

### S5. Add Multi-Seed Variance (Must)
Repeat all experiments with at least 3 random seeds. Report mean ± std. Add paired bootstrap significance tests comparing Delta vs. baseline.

### S6. Validate the Masking → Hallucination Assumption (Must)
Conduct an analysis experiment: for a subset of SQuAD v2 examples, annotate whether masking increases the probability of factually incorrect tokens vs. correct tokens. Report the distribution of probability changes. If the assumption holds, this data should demonstrate that masking preferentially boosts hallucination-probable tokens. Add a control: replace the mask with random token substitution rather than [MASK] to isolate the effect of missing information.

### S7. Fix APC Description (Must)
Rewrite Section 3.5-3.6 to resolve the token-vs-sequence type inconsistency (see annotation Page 5 - Section 3.6).

### S8. Rephrase Promotional Claims (Nice-to-have)
Replace "powerful solution" with "inference-time method"; replace "remarkable improvements" with "consistent improvements under sampling"; replace "easily deployable" with "deployable without retraining, at the cost of 2× inference compute."

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)

**S1 — Problem and Domain:** "Large language models generate plausible but factually incorrect content (hallucinations), which undermines their reliability in high-stakes applications."

**S2 — Prior Gap:** "Existing hallucination mitigation methods require model retraining or external knowledge, limiting their deployability."

**S3 — Proposed Solution:** "We propose Delta, an inference-time method that reduces context-ungrounded outputs by contrasting the model's predictions on original and randomly masked inputs, without retraining or additional data."

**S4 — Key Result (bounded):** "On SQuAD v1.1/v2, TriviaQA, and Natural Questions under sampling decoding, Delta improves exact match by 2–14.5 absolute percentage points. On context-free benchmarks (CommonsenseQA, MMLU), gains are negligible."

**S5 — Scope/Limitation:** "Delta's benefit is most pronounced when inputs provide rich contextual cues and sampling decoding is used. The method introduces one additional forward pass per generation step. Direct hallucination-rate evaluation is needed for stronger claims."

### Introduction Outline (Complete)

**P1 — Establish Territory & Problem.**
Role: State the importance of LLMs, identify the hallucination problem, and explain why it matters for high-stakes domains.
Current weakness: Too generic ("rapid development," "remarkable capabilities"); lacks a precise gap statement.
Mentor Revised Version:
"Large language models (LLMs) are widely deployed in question answering, summarization, and dialogue, but they frequently generate content that is not grounded in the provided input — a phenomenon known as hallucination. This unreliability is particularly consequential in high-stakes domains such as healthcare and legal advice. Most existing mitigation approaches require retraining, auxiliary models, or external knowledge bases, making them difficult to deploy in resource-constrained or real-time settings."

**P2 — Identify Gap & Introduce Solution.**
Role: State what is missing in prior work and how Delta addresses it.
Current weakness: Overclaims efficiency without evidence; misrepresents related methods.
Mentor Revised Version:
"In this paper, we introduce Delta, an inference-only method that reduces hallucination-related errors by contrasting the model's output distribution on the original input against a randomly masked version. Subtracting the masked-input logits from the original logits suppresses tokens that are statistically plausible under missing context but incorrect given the full context. Unlike retraining-based approaches, Delta requires no parameter updates. Its closest relative is Context-Aware Decoding (CAD; Shi et al., 2024), which contrasts p(y|x) with p(y). Delta differs by masking individual tokens rather than removing the full context, which may better capture fine-grained contextual dependencies."

**P3 — Results Preview & Limitation Disclosure.**
Role: Summarize key findings and honestly state limitations.
Mentor Revised Version:
"On context-rich QA benchmarks, Delta improves exact match scores by 3–14.5 absolute points under sampling decoding, with the largest gains on SQuAD v2's unanswerable questions. However, improvements are marginal under greedy decoding and absent on context-free benchmarks (CommonsenseQA, MMLU), confirming that Delta's mechanism is tied to contextual grounding. We release code and analysis to facilitate reproducibility."

**P4 — Contribution Summary.**
Role: List 2–3 explicit, verifiable contributions.
Mentor Revised Version:
"Our contributions are: (1) a simple inference-time method for context-grounded decoding using input masking, (2) empirical evaluation across six datasets showing consistent gains on context-rich QA under sampling, and (3) analysis of when masking-based contrastive decoding succeeds and fails."

### Storyline Candidates

**Candidate A (Current — Problem/Solution/Evidence/Limitation):** The current storyline works but is weakened by (i) overclaiming in the efficiency/hallucination claims, (ii) insufficient differentiation from CAD, and (iii) promotional language. Recommendation: Keep the structure but adopt the Mentor Revised Versions above, making claims more bounded and precise.

**Candidate B (Gap-First — "Existing methods are not deployable; here's a light alternative"):** Emphasizes deployability and compute efficiency. Risk: needs actual efficiency measurements to support the claim.

**Candidate C (Mechanism-First — "We show that masking amplifies hallucinations and subtracting them improves grounding"):** Puts the masking-mechanism hypothesis front and center. Risk: requires direct empirical validation of the assumption.

**Recommendation:** Adopt Candidate A with the specific revisions above, as it most closely matches the paper's existing structure and experimental scope.

## Priority Revision Plan
```text
Priority Matrix:
| Priority | Low Effort (< 1 day)       | Medium Effort (1-3 days)        | Higher Effort (>3 days)          |
|----------|----------------------------|----------------------------------|----------------------------------|
| High Impact (core validity) | Fix APC type inconsistency; rephrase promotional claims | Add direct hallucination benchmarks (TruthfulQA); Add CAD baseline | Validate masking→hallucination assumption with per-token analysis |
| Medium Impact (completeness) | Add compute overhead (latency, FLOPs) | Add multi-seed variance + significance tests | Expand ablation to more datasets + β sensitivity |
| Lower Impact (polish) | Add revised abstract | Rewrite introduction per outline | Targeted masking comparison |
```

### P0 — Must-Fix before next submission (core validity)

1. **Validate masking→hallucination assumption** (Add per-token analysis and random-perturbation control; see S6)
2. **Fix APC type inconsistency** in Section 3.5–3.6 (see S7)
3. **Add CAD as direct baseline** across all datasets under identical settings (see S3)
4. **Report multi-seed variance** (≥3 seeds, mean±std) for all experiments (see S5)
5. **Rephrase all promotional claims** to bounded, evidence-grounded language (see S8)

### P1 — Should-Fix (completeness and rigor)

6. **Add direct hallucination evaluation** on TruthfulQA or HaluEval (see S2)
7. **Report computational overhead** (latency, memory, FLOPs) (see S4)
8. **Expand ablation** to include β sensitivity, MASK token comparison, and at least one more dataset (SQuAD v2)

### P2 — Nice-to-Have (quality improvement)

9. **Rewrite abstract and introduction** using the Mentor Revised Versions provided in this review
10. **Add targeted masking comparison** to the future work discussion with quantitative caveats
11. **Add code release** for reproducibility

### Expected Impact After Fixes

- Validity risk: HIGH→LOW (core mechanism validated through per-token analysis + CAD comparison)
- Novelty clarity: MEDIUM→HIGH (clear differentiation from CAD through experiments)
- Reproducibility: LOW→MEDIUM (variance reported, APC fixed, compute overhead disclosed)
- Overall score improvement: 4→6-7/10 after P0 fixes; 6-7→7-8/10 after P0+P1 fixes

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (Data/Protocol/Baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|----------------------------------|---------|--------------|-----------------|-------------------|
| E1 | SQuAD v1.1 performance | SQuAD v1.1, Llama 3.1 8B, Delta vs baseline, w/ and w/o sampling | EM, F1 | Delta improves EM by 3-4.4 pts | Delta improves QA accuracy on extractive QA | No variance reported; single model; no CAD comparison |
| E2 | SQuAD v2 performance | SQuAD v2, same setup | EM, F1, HasAns EM, NoAns EM | Delta improves EM by ~6 pts; NoAns EM by 11.8-14.5 pts | Delta effective for unanswerable questions | No direct hallucination metric for "no answer" decisions |
| E3 | TriviaQA performance | TriviaQA, same setup | EM | Delta improves by 7.84 pts w/ sampling; -0.14 pts w/o sampling | Delta effective under sampling | Negative result without sampling is under-discussed |
| E4 | Natural Questions performance | NQ, same setup | EM | Delta improves by 2.55 pts w/ sampling; -0.30 pts w/o sampling | Consistent with E3 pattern | Small absolute gains; high baseline variance likely |
| E5 | Context-free evaluation | CommonsenseQA, MMLU, same setup | Accuracy | Delta declines by 0.25-0.29 pts | Delta not beneficial for context-free tasks | Only 2 datasets; no analysis of why |
| E6 | Ablation: r_mask & α | SQuAD v1.1 w/ sampling, r_mask ∈ {0.3,0.5,0.7}, α ∈ {0.1,...,0.5} | EM, F1 heatmaps | All configs > baseline; σ_EM=0.66, σ_F1=0.21 | Method is robust to hyperparameter choice | Only 1 dataset + 1 decoding regime; no β or MASK-type ablation |

### Research-Theme Gap Diagnosis

1. **New knowledge gap.** The paper's core hypothesis (masking amplifies hallucination) is not validated. Without this validation, the paper's new knowledge is limited to "input-masking contrastive decoding improves QA accuracy" — which is useful but incremental.

2. **Reproducibility gap.** Single-seed results without variance, no code release, and ambiguous APC description limit reproducibility.

3. **Impact gap.** Without direct hallucination metrics and CAD comparison, the paper's practical significance in reducing LLM hallucinations cannot be assessed against existing methods.

### Proposed Research Experiments

```text
ASCII Diagram — Experiment Upgrade Plan

[P0 Experiments: Core Validity]
    ├── Exp-P0.1: Per-token hallucination analysis
    │   ├── Target: Validate masking→hallucination assumption
    │   ├── Design: On SQuAD v2 subset, compare token probabilities 
    │   │   under original vs masked input; annotate tokens as 
    │   │   factually correct/incorrect
    │   ├── Metric: Probability shift for correct vs incorrect tokens
    │   ├── Success: Masking increases incorrect-token probability 
    │   │   more than correct-token probability
    │   └── Effort: 2-3 days
    │
    ├── Exp-P0.2: CAD baseline comparison
    │   ├── Target: Determine Delta's incremental value over CAD
    │   ├── Design: Run CAD on all 6 datasets under identical settings
    │   ├── Metric: EM, F1, latency
    │   ├── Success: Delta outperforms CAD on ≥3 of 4 context datasets
    │   └── Effort: 2-3 days
    │
    └── Exp-P0.3: Multi-seed replication
        ├── Target: Statistical reliability
        ├── Design: Repeat main experiments with 3 seeds
        ├── Metric: Mean ± std for all Table 1 entries
        ├── Success: Reported std < 50% of claimed improvement
        └── Effort: 2-5 days (compute-dependent)

[P1 Experiments: Completeness & Generalization]
    ├── Exp-P1.1: Direct hallucination benchmark
    │   ├── Target: Measure factual consistency directly
    │   ├── Design: Evaluate on TruthfulQA + HaluEval
    │   ├── Metric: Truthfulness score, hallucination rate
    │   ├── Success: Delta improves truthfulness by >3 pts
    │   └── Effort: 1-2 days
    │
    ├── Exp-P1.2: Compute overhead analysis
    │   ├── Target: Quantify efficiency trade-off
    │   ├── Design: Measure latency, memory, throughput
    │   ├── Metric: ms/token, GB, tokens/sec
    │   ├── Success: Transparent reporting
    │   └── Effort: 0.5 day
    │
    └── Exp-P1.3: Ablation expansion
        ├── Target: Test β sensitivity + MASK token choice
        ├── Design: Vary β ∈ {0.05, 0.1, 0.2}; compare EOS vs [MASK] vs [UNK] tokens
        ├── Metric: EM on SQuAD v1.1
        ├── Success: Sensitivity <0.5 pts EM across settings
        └── Effort: 1 day

[P2 Experiments: Quality Improvement]
    └── Exp-P2.1: Targeted masking (future work preview)
        ├── Target: Improve upon random masking
        ├── Design: Mask only nouns/verbs vs random; compare
        ├── Metric: EM, F1
        ├── Success: Targeted masking > random masking
        └── Effort: 2-3 days
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 4/10

**Rationale:** The paper addresses a relevant problem (LLM hallucination) with a simple, intuitive approach (masking-based contrastive decoding). However, the core assumption that masking amplifies hallucinations remains unvalidated, the claimed "hallucination mitigation" is not directly measured, computational efficiency is oversold without analysis, the closest baseline (CAD) is not experimentally compared, and experiments lack statistical rigor (single-seed, no variance). These issues collectively limit the paper's contribution validity and reproducibility. The score prioritizes research value and novelty, which are both currently weakened by the absence of direct mechanism validation and missing baseline comparisons.

**Post-Revision Target:** [6, 7]/10

**Rationale for Target:** If the authors address all P0 fixes (validation of masking→hallucination assumption, CAD comparison, APC correction, multi-seed variance, and claim bounding), the paper would present a well-grounded empirical study of a novel inference-time method. The score could reach 6-7/10, reflecting a solid contribution with verified mechanisms. Full P0+P1 fixes (adding hallucination benchmarks, compute overhead analysis) could raise the target to 7-8/10, but the method's inherent limitation (requiring 2× forward passes, context-dependent) caps the ceiling.