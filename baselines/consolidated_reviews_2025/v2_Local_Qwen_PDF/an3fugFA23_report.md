## Summary
The paper proposes Glimpse, a probability distribution estimation approach that reconstructs full token distributions from partial top-K API observations. This enables classical white-box detection metrics (Entropy, Rank, Log-Rank, Fast-DetectGPT) to be applied using proprietary scoring models (e.g., GPT-3.5, GPT-4). Experiments across five source models and multiple datasets demonstrate that Glimpse significantly improves detection accuracy (average AUROC ~0.95) and efficiency compared to open-source baselines and existing black-box methods. The work addresses a practical bottleneck in LLM-generated text detection: the inability of white-box methods to access full distributions from proprietary APIs.

## Strengths
1. **Practical Problem Solving:** The paper addresses a highly relevant and practical bottleneck in AI safety: enabling efficient white-box detection metrics on proprietary LLMs that only expose partial API information.
2. **Methodological Simplicity and Effectiveness:** Glimpse introduces a clean, assumption-light framework (Geometric, Zipfian, MLP) to estimate tail distributions from top-K probabilities. The approach is computationally lightweight and seamlessly integrates with existing metrics.
3. **Comprehensive Empirical Validation:** Experiments cover five major proprietary source models, multiple datasets, and diverse languages. The ablation studies on estimation algorithms, top-K sizes, and prompts provide thorough insights into method behavior.
4. **Efficiency Gains:** The demonstration that Glimpse is 4.1x faster and ~10x cheaper than DNA-GPT while achieving higher accuracy offers a compelling practical advantage for real-world deployment.

## Weaknesses
1. **Novelty Claim Scoping:** The claim "first to investigate white-box detection methods using proprietary models" is broad and may overlap with recent logit-estimation or black-box adaptation works (e.g., DLAD). The claim should be scoped to "distribution-based white-box metrics" to maintain defensibility.
2. **Terminology Ambiguity:** Classifying methods using open-source surrogates to detect proprietary sources as "white-box" based solely on scoring model access may confuse readers. The distinction between source-model access and scoring-model access needs sharper definition.
3. **Statistical Reporting:** Main results report median AUROC over three runs but lack variance/std or significance tests. Given small margins between top methods (e.g., 0.9537 vs 0.9554), statistical reliability cannot be fully assessed.
4. **Hypothesis Validation:** The speculation that performance drops on GPT-4 stem from "distribution mismatch" between small surrogates and large sources is plausible but lacks direct empirical validation (e.g., logit divergence analysis).

## Key Issues
1. **Claim-Evidence Alignment for Novelty:** The "first to enable" claim requires precise scoping to avoid overlap with concurrent logit-estimation research. Without bounding, reviewers may perceive the contribution as incremental.
2. **White-Box/Black-Box Definition Clarity:** The paper's definition of white-box (based on scoring model access) diverges from common intuition (source model transparency). This risks confusing readers about the actual access assumptions.
3. **Statistical Significance of Marginal Gains:** Differences between Glimpse variants (Geometric vs Zipfian vs MLP) and top baselines are often <0.01 AUROC. Without variance reporting, the practical significance of these gains is unclear.
4. **API Dependency Limitation:** Glimpse relies on APIs returning top-K logprobs. Many newer proprietary models restrict this feature. The paper should explicitly discuss this deployment constraint and its impact on long-term viability.

## Actionable Suggestions
1. **Scope Novelty Claims:** Revise the introduction and conclusion to specify "first to enable *distribution-based white-box metrics* (e.g., curvature, rank) via partial observation estimation." Add a brief comparison with DLAD or similar logit-estimation works in Related Work.
2. **Clarify Access Definitions:** In Section 2.1, explicitly state that "white-box" refers to the *scoring model's* access level (full logits), distinguishing it from the *source model's* access level. Add a footnote or sentence to prevent reader confusion.
3. **Report Statistical Variance:** Add mean ± std or confidence intervals to Table 1 and main text claims. If margins are <0.01, acknowledge that differences may not be statistically significant without larger-scale testing.
4. **Validate Distribution Mismatch Hypothesis:** In Section 3.3, either add a small empirical analysis (e.g., KL divergence between Neo-2.7B and GPT-4 logits on a sample) or soften the language to "We hypothesize that..." to maintain scientific rigor.
5. **Bound Cost Claims:** In Section 3.3, explicitly state that cost comparisons are "under current API pricing models" and clarify that Glimpse avoids output token costs by only echoing input probabilities.

## Storyline Options + Writing Outlines
**Abstract Outline (S1-S5):**
- S1 (Problem): LLMs generate indistinguishable text, necessitating reliable detection tools.
- S2 (Gap): White-box methods require full model access unavailable for proprietary LLMs; black-box methods are inefficient.
- S3 (Solution): Glimpse estimates full token distributions from partial top-K API observations.
- S4 (Method): Adapts white-box metrics (Entropy, Rank, Fast-DetectGPT) to proprietary scoring models using Geometric/Zipfian/MLP estimators.
- S5 (Result): Achieves ~0.95 AUROC across five source models, outperforming open-source baselines by 51% relative to remaining space, demonstrating proprietary LLMs as effective universal detectors.

**Introduction Outline (P1-P5):**
- P1 (Motivation): LLM capabilities rise, detection difficulty increases, societal risks demand robust tools.
- P2 (Gap): Proprietary models limit API access; white-box needs full distributions, black-box is costly/inefficient.
- P3 (Hypothesis): Fast-DetectGPT drops on GPT-4 due to surrogate-source distribution mismatch; large proprietary models could bridge this if accessible.
- P4 (Solution): Glimpse reconstructs distributions from top-K logprobs, enabling white-box metrics on proprietary APIs.
- P5 (Contributions): (1) Distribution estimation framework, (2) Extension of 4 white-box methods, (3) Empirical validation showing accuracy/efficiency gains, (4) First adaptation of distribution-based white-box metrics to proprietary models.

## Priority Revision Plan
| Priority | Action | Expected Impact | Effort |
|---|---|---|---|
| P0 | Scope novelty claim to "distribution-based white-box metrics" and add DLAD comparison. | Prevents novelty rejection; strengthens defensibility. | Low |
| P0 | Clarify white-box/black-box definition in Section 2.1 (scoring vs source access). | Eliminates reader confusion; improves terminology precision. | Low |
| P1 | Add mean ± std to Table 1 and main text claims. | Validates statistical reliability of marginal gains. | Medium |
| P1 | Soften "distribution mismatch" speculation or add KL divergence evidence. | Improves scientific rigor of motivation. | Medium |
| P2 | Bound cost claims to "current API pricing" and clarify input-token-only cost. | Ensures long-term claim validity. | Low |
| P2 | Add brief limitation on API logprob availability in Conclusion. | Balances strong claims with practical constraints. | Low |

## Experiment Inventory & Research Experiment Plan
**Completed Experiment Inventory:**
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Limitation |
|---|---|---|---|---|---|---|
| E1 | Glimpse improves accuracy over open-source baselines. | 5 source models, 3 datasets, Mix3/Mix6. | AUROC, ACC | ~0.95 AUROC avg; +51% rel. gain. | Yes | No variance reported. |
| E2 | Glimpse is more efficient than DNA-GPT. | Same datasets, timing/cost tracking. | Time, Cost | 4.1x faster, ~10x cheaper. | Yes | Pricing-dependent. |
| E3 | Estimation algorithm ablation. | Geometric vs Zipfian vs MLP. | AUROC | Dataset-dependent preferences. | Yes | MLP training cost not analyzed. |
| E4 | Top-K and Rank-List size ablation. | K=1..10, M=100..1000. | AUROC | Higher K/M generally better. | Yes | Limited to GPT-4 source. |
| E5 | Robustness across domains/languages. | Cross-dataset thresholds, 6 languages. | ACC | High stability; Russian lower. | Yes | Russian under-training noted. |
| E6 | Paraphrasing attack robustness. | DIPPER (60L, 60O). | TPR@1%FPR | Outperforms open-source baselines. | Yes | XSum anomaly noted. |

**Research-Theme Gap Diagnosis:**
- Statistical reliability of marginal gains (<0.01 AUROC) is unverified.
- Distribution mismatch hypothesis lacks direct empirical validation.
- Long-term API dependency constraints are not fully explored.

**Proposed Research Experiments:**
| Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Cost | Gain |
|---|---|---|---|---|---|---|---|
| Statistical Significance | Glimpse gains are stable across seeds. | 5-seed runs on Mix3. | Baselines same seeds. | Mean±std AUROC | p<0.05 vs baseline | Low | Validates marginal gains. |
| Distribution Mismatch | KL divergence correlates with detection drop. | Compute KL(Neo-2.7B, GPT-4) on sample. | None. | KL vs AUROC delta | Negative correlation | Low | Supports motivation. |
| API Constraint Robustness | Glimpse degrades gracefully if top-K restricted. | Test K=1,2,3 on GPT-3.5. | Naive zero-tail. | AUROC drop | <5% drop from K=5 | Low | Assesses deployment risk. |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
Final Score: 7.5/10
Post-Revision Target: [8.0, 9.0]/10

**Rationale:** The paper addresses a highly practical and timely problem in AI safety with a clean, effective solution. The empirical validation is comprehensive, covering multiple models, datasets, and languages. The efficiency gains over existing black-box methods are compelling. However, the novelty claim requires scoping to avoid overlap with concurrent logit-estimation works, and the white-box/black-box terminology needs sharper definition to prevent reader confusion. Statistical variance reporting is missing for marginal gains. With these revisions, the paper will be significantly stronger and more defensible.