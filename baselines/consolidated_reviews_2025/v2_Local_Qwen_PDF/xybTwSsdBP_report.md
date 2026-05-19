## Summary
The paper proposes OptBatch, an online data selection method for instruction tuning that aims to reduce computational costs while maintaining model performance. OptBatch combines loss-probability based stratified sampling to ensure distributional coverage with a farthest-point sampling strategy in an adaptive gradient space to maximize batch diversity. The method utilizes a second-moment gradient scaling (termed "Hessian gradient" in the manuscript) to stabilize selection across batches and provides a theoretical bound on training loss based on gradient Lipschitz continuity. Experiments on three datasets (NetLit, LLaMaQA, WikiMatrix) and two models (LLaMa3, ChatGLM3) demonstrate that OptBatch achieves comparable or superior performance to full-dataset training and outperforms baselines (Random, Online Hard, CCS, InfoBatch) across various pruning rates, reducing computational FLOPs by approximately 30-40%.

## Strengths
1. **Practical Motivation and Clear Problem Framing:** The paper addresses a highly relevant problem in LLM instruction tuning: the trade-off between data diversity, sample difficulty, and computational efficiency. The focus on whole-batch learnability rather than individual sample importance is a sensible and practical perspective for online training.
2. **Comprehensive Empirical Validation:** The experiments cover diverse tasks (dialogue, QA, translation), multiple models (LLaMa3, ChatGLM3), and various pruning rates. The inclusion of both reference-based metrics (BLEU, ROUGE) and LLM-as-a-judge/human evaluations (GPT-4 scores) provides a robust assessment of downstream performance.
3. **Theoretical Grounding:** The attempt to bound the training loss of the selected coreset by proving gradient Lipschitz continuity adds theoretical depth to the method, distinguishing it from purely heuristic selection strategies.
4. **Computational Efficiency Analysis:** The FLOPs analysis clearly quantifies the backward-pass savings, providing a concrete justification for the method's efficiency claims.

## Weaknesses
1. **Terminology Inaccuracy ("Hessian Gradient"):** The manuscript repeatedly refers to the adaptive moment-scaled gradient feature as "Hessian gradient optimization." This is mathematically incorrect; the method uses a first-order gradient norm scaled by Adam's second-moment estimate, not a second-order Hessian approximation or curvature estimation. This mislabeling inflates the method's theoretical complexity and misleads readers.
2. **Algorithm Pseudocode Inconsistency:** Algorithm 1 contains logical contradictions. It initializes a coreset via importance sampling (Line 2) but then describes a stratified farthest-point sampling loop (Lines 3-13) without clearly explaining how the initial sample interacts with the strata or how the per-stratum allocation `|Si|` is derived. This ambiguity threatens reproducibility.
3. **Formula-Text Contradiction in Gradient Computation:** Section 2.1 claims to use a "sequence-level gradient approach" to represent the entire sequence, but Equation (2) computes the L2 norm along `axis=1` of the `D×H` lm-head gradient matrix, which yields token-level vocabulary gradients, not a sequence-level scalar or vector.
4. **Overclaimed Performance vs. Full-Dataset Training:** The abstract and conclusion state that OptBatch "outperforms full dataset training." This is a strong claim that requires precise bounding. It likely means achieving comparable performance at a fraction of the cost, or outperforming full-data training under a fixed computational budget. The current wording is misleading.
5. **Baseline Fairness and Threshold Tuning:** The description of the InfoBatch baseline mentions manually increasing its threshold for higher pruning rates without explicitly defining the protocol. This raises concerns about cherry-picking or unfair baseline tuning.

## Key Issues
1. **Correct "Hessian Gradient" Terminology (Critical):** Replace all instances of "Hessian gradient" with "adaptive moment-scaled gradient" or "second-moment normalized gradient." The current terminology falsely implies second-order optimization, which undermines scientific credibility.
2. **Fix Algorithm 1 Pseudocode (Major):** Rewrite the pseudocode to clearly separate the stratum allocation step from the selection step. Explicitly show how `|Si|` is calculated based on the loss probability mass of each stratum, and remove the confusing initial importance sampling step that conflicts with the stratified loop.
3. **Clarify Sequence-Level Gradient Aggregation (Major):** Resolve the contradiction between the text claiming "sequence-level gradients" and Equation (2) computing token-level norms. Provide the exact aggregation formula (e.g., mean/max over tokens) used to derive the final sample representation.
4. **Bound Performance Claims (Major):** Revise the abstract and conclusion to accurately state that OptBatch achieves "comparable or superior performance to full-dataset training at a fraction of the computational cost," rather than implying absolute outperformance without qualification.
5. **Standardize Baseline Protocols (Minor):** Explicitly define how the InfoBatch threshold is determined for each pruning rate (e.g., matching the target pruning percentile) to ensure fair and reproducible comparisons.

## Actionable Suggestions
1. **Terminology Overhaul:** Conduct a global search-and-replace for "Hessian gradient" and substitute it with "adaptive moment-scaled gradient." Update Section 3.2 to accurately describe the mechanism as leveraging historical variance to stabilize gradient magnitudes, rather than approximating curvature.
2. **Algorithm Rewrite:** Restructure Algorithm 1 into three clear phases: (1) Compute losses and partition batch into `k` strata; (2) Allocate sample counts `|Si|` per stratum proportional to `exp(loss)` mass; (3) Iteratively select samples within/across strata by maximizing minimum L2 distance in the adaptive gradient space.
3. **Formula Clarification:** In Section 2.1, explicitly define the sequence-level aggregation. For example: `gradient_seq = mean(||gradient_lmhead||_2, axis=0)` or similar, and ensure the dimensions match the narrative claim.
4. **Claim Bounding:** In the Abstract and Conclusion, replace "outperforms full dataset training" with "achieves comparable or superior performance to full-dataset training while reducing computational costs by 20-40%."
5. **Baseline Protocol Specification:** In Section 4.1, add a sentence clarifying the InfoBatch threshold: "For fair comparison, the InfoBatch threshold is set to the loss percentile corresponding to the target pruning rate, ensuring consistent retention ratios across methods."
6. **FLOPs Nuance:** In Section 4.4, clarify that the ~30-40% FLOPs reduction primarily stems from the backward pass, as the full-batch forward pass is required for online selection. Provide a concrete numerical example (e.g., "At 70% pruning, total FLOPs drop by ~35% assuming Fb ≈ 2Ff").

## Storyline Options + Writing Outlines
### Abstract Outline (S1-S5)
- **S1 (Problem & Domain):** Instruction tuning enhances LLM capabilities but demands extensive data and prolonged training, creating a bottleneck for efficient model deployment.
- **S2 (Significance/Challenge):** The core challenge lies in identifying high-quality, diverse data subsets that maintain performance while significantly reducing computational costs.
- **S3 (Prior Gap):** Existing online selection methods often prioritize high-loss samples, which introduces noise and fails to balance distributional coverage with sample learnability.
- **S4 (Proposed Method):** We propose OptBatch, an online data selection method that optimizes whole-batch learnability through loss-probability stratified sampling and maximizes inter-sample adaptive gradient distances for diversity.
- **S5 (Key Result & Bounded Implication):** Extensive experiments show that OptBatch achieves comparable or superior performance to full-dataset training across diverse tasks, reducing computational costs by 20-40% while maintaining robust generalization.

### Introduction Outline (P1-P4)
- **P1 (Big Picture & Motivation):** Establish the importance of instruction tuning and the computational burden of large-scale datasets. Introduce data pruning as a solution but highlight the unique challenges in NLP (semantic redundancy, variable sequence quality) compared to CV.
- **P2 (Gap in Prior Work):** Categorize existing methods into offline (static, high overhead) and online (dynamic, but often biased toward high-loss outliers or lacking diversity). Explicitly state the unresolved trade-off between sample difficulty (learnability) and distributional coverage (diversity).
- **P3 (Proposed Solution & Intuition):** Introduce OptBatch's core intuition: treating the batch as a cohesive entity. Explain how stratified sampling ensures coverage across difficulty levels, while maximizing adaptive gradient distances prevents redundancy. Briefly mention the theoretical grounding (Lipschitz continuity bounding loss).
- **P4 (Contributions & Evidence):** List the three main contributions clearly: (1) The stratified + distance-maximization algorithm, (2) The adaptive moment-scaled gradient feature with theoretical loss bounds, (3) Comprehensive empirical validation showing state-of-the-art efficiency and performance across multiple datasets and models.

## Priority Revision Plan
### P0: Critical Fixes (Must complete before resubmission)
1. **Terminology Correction:** Globally replace "Hessian gradient" with "adaptive moment-scaled gradient" and update Section 3.2 to accurately describe the first-order adaptive scaling mechanism.
2. **Algorithm Reproducibility:** Rewrite Algorithm 1 to clearly separate stratum allocation from the farthest-point selection loop, removing the conflicting initial importance sampling step.
3. **Claim Bounding:** Revise Abstract and Conclusion to state that OptBatch achieves "comparable or superior performance at reduced cost" rather than implying absolute outperformance over full-data training.

### P1: Major Improvements (Highly recommended)
1. **Formula-Text Alignment:** Clarify the sequence-level gradient aggregation in Section 2.1 by providing the exact formula used to reduce token-level lm-head gradients to a single sample representation.
2. **Baseline Fairness:** Explicitly define the InfoBatch threshold protocol in Section 4.1 (e.g., matching the target pruning percentile) to ensure reproducible and fair comparisons.
3. **Theoretical Connection:** Add a sentence in Section 3.1 explicitly linking gradient Lipschitz continuity to the set-cover strategy, explaining why maximizing gradient distance bounds the loss approximation error.

### P2: Minor Polish (Quality of life)
1. **FLOPs Nuance:** Clarify in Section 4.4 that the ~30-40% FLOPs reduction primarily applies to the backward pass, as the full-batch forward pass is required for online selection.
2. **Limitations Tone:** Improve the grammatical structure and professional tone of the Limitations section, particularly regarding lm-head gradient sufficiency and loss-centric evaluation.

## Experiment Inventory & Research Experiment Plan
| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | OptBatch outperforms baselines across datasets | NetLit, LLaMaQA, WikiMatrix; ChatGLM3; 70% pruning | Loss | OptBatch achieves lowest loss across all datasets | Diversity + difficulty balance works | No variance/seeds reported |
| E2 | OptBatch is robust to pruning rates | NetLit; ChatGLM3; α=20% to 90% | Loss | Loss decreases to α=50%, then plateaus; 10% data ~ 90% data | High redundancy in web text | Limited to one dataset/model |
| E3 | Model-agnostic effectiveness | LLaMaQA; ChatGLM3 vs LLaMa3; 70% pruning | Loss | OptBatch stable across models; baselines fluctuate | Generalizability across architectures | No statistical significance test |
| E4 | Feature ablation (Embedding vs Grad vs Hessian) | NetLit; ChatGLM3; 70% pruning | Loss | Adaptive gradient (Hessian) > Grad norm > Embedding | Adaptive scaling improves selection | "Hessian" terminology is misleading |
| E5 | Downstream task validation | LLaMaQA, WikiMatrix; LLaMa3/ChatGLM3 | BLEU, ROUGE | OptBatch matches/exceeds baselines on reference metrics | Loss reduction translates to task performance | Only 70% pruning tested here |
| E6 | Role-playing quality evaluation | NetLit; ChatGLM3 | GPT-4 score, Human eval | OptBatch achieves highest high-score percentage (60.5%/61.8%) | Method preserves character alignment | Small sample size for human eval |
| E7 | Computational efficiency analysis | Theoretical FLOPs calculation | FLOPs | ~30-40% reduction at 70-80% pruning | Backward pass pruning saves compute | Forward pass overhead not fully quantified |

### Research-Theme Gap Diagnosis
The core research value (efficient instruction tuning via batch-level diversity) is well-supported, but robustness evidence is thin. Missing multi-seed variance reporting makes small margin gains (<0.3 loss) statistically unverifiable. Additionally, the claim of "outperforming full dataset training" lacks a direct head-to-head comparison under identical computational budgets (e.g., fixed FLOPs or time).

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Estimated Cost/Time | Expected Paper-Quality Gain |
|---|---|---|---|---|---|---|---|
| Statistical Reliability | OptBatch gains are consistent across random seeds | Run E1-E3 with 3 different random seeds | Same baselines | Mean ± Std Loss | Std < margin of improvement | 1-2 days (16 GPUs) | Validates robustness, removes reviewer doubt |
| Budget-Matched Fairness | OptBatch outperforms full-data training under fixed compute | Train full-data for 0.5 epochs vs OptBatch (70% pruning) for 1 epoch | Full-data (0.5 ep) | Loss, BLEU | OptBatch >= Full-data (0.5 ep) | 1 day | Justifies "outperforms full dataset" claim |
| Sequence-Length Sensitivity | lm-head gradients degrade on very long sequences | Test on dataset with seq_len > 4096 | Same baselines | Loss, Perplexity | Quantify performance drop | 1 day | Bounds limitation (1) with empirical evidence |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 5/10

**Justification:** The paper addresses a highly relevant problem in efficient instruction tuning and provides comprehensive empirical validation across diverse datasets and models. However, the current manuscript suffers from significant scientific credibility issues. The repeated mislabeling of a first-order adaptive moment scaling as "Hessian gradient optimization" falsely inflates the method's theoretical complexity. Additionally, critical inconsistencies between the narrative and mathematical formulations (e.g., sequence-level vs. token-level gradients) and logical contradictions in Algorithm 1 threaten reproducibility. The strong claim of "outperforming full dataset training" also requires precise bounding. These issues currently prevent the paper from meeting the rigor standards for publication.

**Post-Revision Target:** [7, 8]/10

**Path to Target:** If the authors execute the P0 and P1 revision plan—specifically correcting the terminology, rewriting Algorithm 1 for clarity, aligning formulas with text, and adding multi-seed variance reporting—the paper will become a robust and valuable contribution. The core intuition of balancing batch diversity and learnability is sound, and the empirical results are promising. Addressing the identified defects will transform this from a flawed submission into a strong, publication-ready manuscript.