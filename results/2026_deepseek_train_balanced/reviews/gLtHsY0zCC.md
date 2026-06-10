## Summary

This paper introduces T-Measure, a data-centric transferability measure for ranking fine-tuned models in zero-shot transfer learning without requiring labeled target data. The method learns a dataset-aligned representation space via triplet loss fine-tuning of SentenceBERT on each source dataset, identifies the subset of source data most similar to the target, and computes the average Pointwise V-Information (PVI) of that subset to estimate model transferability. The paper evaluates T-Measure across 4 NLP tasks and 11 datasets, comparing against Naive, V-Usability, and an adapted PARC baseline.

## Strengths

1. **Addresses a practical problem under realistic constraints.** The paper targets model selection when no labeled target data is available, which is a common real-world scenario. The combination of representation learning (triplet-based alignment) with PVI computation on selected subsets is a reasonable approach to this problem.

2. **Broader task-level evaluation than typical prior work on transferability measures.** While prior transfer measure work focused on CV benchmarks (CIFAR, ImageNet), this paper evaluates across 4 NLP tasks (Emotion Recognition, Relation Classification, Question Answering, Response Selection) spanning 11 datasets, providing a wider view of task-level generalizability.

3. **Consistent gains over V-Usability and Naive baselines.** T-Measure achieves higher Kendall-τ than V-Usability on Emotion Recognition (+0.44) and Response Selection (+0.28), and on 3 of 4 tasks (all except Relation Classification) it achieves the best ranking performance among compared methods.

4. **Methodological fairness in baseline adaptation.** The paper adapts PARC-based measures to the zero-shot setting (Section 4.3), enabling a controlled comparison where all methods operate under the same constraints.

## Weaknesses

### Fatal

None.

### Major

1. **PVI computation from a single trained model is underspecified, affecting reproducibility.** The paper defines T-Measure as the average PVI of the selected subset on model φ (Eq. 192), and defines PVI in terms of a predictive family V with minimization over functions g, g' (Eqs. 180–185). However, it never explains how a *single fixed model* φ maps onto this framework — how the predictive family V is defined for φ, how the null input θ is operationalized for a BERT classifier, or how the minimization over V is performed (or bypassed) when computing PVI from one set of model parameters. A reader familiar with Ethayarajh et al. (2021) might fill in gaps, but the method as written cannot be reproduced without these details. Given that PVI is the core computation, this is a significant gap.

2. **No variance or statistical significance reported for the main ranking results.** Table 3 reports Kendall-τ as single point estimates without standard deviations, confidence intervals, or any measure of variability. With a probe set of only 100 labeled instances per target, the ground-truth ranking itself may be noisy, and the τ estimates could have wide error bars. The boxplots (Figure 6) help partially, but the central quantitative table lacks the rigor expected for a top-tier venue.

3. **Limited investigation of failure modes.** T-Measure underperforms PARC on Relation Classification (Table 3). The paper's explanation — "zero-shot characteristics of our problem" (line 272) — is too vague to be informative. The Emotion Recognition failure analysis (label distribution skew between DailyDialog and Empathetic) is post-hoc and covers only one case. Without a systematic characterization of when T-Measure succeeds or fails (e.g., source-target label divergence, model accuracy spread, alignment quality), the paper leaves readers unable to judge the method's reliability.

### Minor

4. **Evaluation is limited to NLP tasks, despite criticizing prior work for narrow CV-only evaluation.** The paper faults prior transferability measures for focusing on "CIFAR and ImageNet datasets" (lines 24–25), yet evaluates only on NLP. This is a symmetric limitation that weakens the generalizability claim.

5. **Some implementation details are missing.** The triplet fine-tuning (Section 4.1) specifies only "5 epochs" and the number of triplets per pair (20). Learning rate, batch size, optimizer, margin ε, and distance metric for the triplet loss are not reported, affecting reproducibility at the implementation level.

6. **Probe set of 100 instances is small for reliable ground-truth estimation.** For multi-class tasks like Emotion Recognition (7 classes), 100 instances may produce unreliable performance estimates, which in turn makes the ground-truth ranking used for evaluation itself noisy. The paper does not discuss or justify this choice.

### Trivial

7. **"Relative F1" is used without formal definition.** The term appears at line 274 and in Figure 6 but is never defined (e.g., is it F1(selected) / F1(best)?).

## Nice-to-Haves

- An ablation comparing the triplet-fine-tuned SentenceBERT space against off-the-shelf SentenceBERT embeddings would clarify whether the fine-tuning step meaningfully changes nearest-neighbor selection.
- A sensitivity analysis of the margin ε in the triplet loss and the probe set size would strengthen confidence in the method's robustness.

## Removed Points

These points were flagged by the reviewers but removed after cross-checking against the paper. They are listed here for reference only and should be treated with caution.

1. **"Zero-shot framing is misleading / scope mismatch."** Removed because Section 2.4 (line 110) *explicitly* states the constraints: same task, same architecture, same evaluation metric. The motivating example (780 models on HuggingFace) is a general motivation, not a misrepresentation. The paper self-constrains its scope honestly.
2. **"Circular dependency on SentenceBERT undermines data-centric claim."** Removed because fine-tuning a pre-trained representation with data-driven triplets is standard practice. The paper does not claim the representation is built from scratch.
3. **"Novel problem claim is overstated."** Removed because the claim is qualified ("to the best of our knowledge") and targets a specific combination (data-centric + zero-shot). This is a subjective judgment, not a verifiable flaw.
4. **"T-Measure does not win on all tasks."** Removed — no method must win on all tasks. PARC winning on RC is acknowledged by the paper.
5. **"Kendall-τ values are very low (e.g., 0.14 for RS)."** Demoted to minor concern at most; the paper explains the low τ arises from small performance differences among models on RS, which makes ranking inherently noisy. This is a limitation of the task, not the method.
6. **"Every target point maps to the same few source points."** Removed as pure speculation; no evidence in the paper supports this.
7. **"Notation is heavy/redundant."** Removed as a style nitpick.

## Novel Insights

None beyond the paper's own contributions. The synthesis of reviewer perspectives does not uncover an observation about the paper that its authors did not already state.

## Suggestions

- **Clarify the PVI computation.** Explicitly state: (a) how φ is used as the conditional predictor g'[x]; (b) how the unconditional predictor g[θ] is obtained (e.g., empirical label marginal, or a constant-output model); and (c) how the minimization over V is handled or avoided when using a single trained model. This is the single most important revision for reproducibility.
- **Add variance information.** Report per-target Kendall-τ values (not just averages) or include standard deviations across multiple probe set samples.
- **Systematically analyze failure.** Categorize target datasets by label distribution divergence from sources and report how T-Measure's τ varies with this divergence. This would replace the current one-off Emotion Recognition discussion with a quantitative characterization.
- **Report missing training hyperparameters** (learning rate, batch size, margin ε, optimizer) for the triplet fine-tuning step.
- **Formally define "Relative F1"** in Section 4.2.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>