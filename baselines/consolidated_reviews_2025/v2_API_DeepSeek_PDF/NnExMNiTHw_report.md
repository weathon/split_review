## Summary
# Final Review Report

## Summary

This paper proposes SpecDec++, an enhancement to speculative decoding that adaptively determines the candidate length (K) per speculation round rather than using a fixed K. The authors formulate dynamic K selection as a Markov Decision Process (MDP) and prove that the optimal stopping policy is a threshold on the cumulative rejection probability. They train a lightweight acceptance prediction head on top of the draft model to estimate this probability, and stop speculation when the predicted rejection probability exceeds a tunable threshold. On llama-2-chat 7B&70B, SpecDec++ achieves 2.04x speedup on Alpaca (7.2% relative improvement over fixed-length baseline), 2.26x on GSM8K (9.4% improvement), and 2.23x on HumanEval (11.1% improvement).

The paper has clear strengths: a well-motivated problem, a clean theoretical framing (MDP + threshold policy), and solid empirical gains across multiple datasets with reasonable ablations. However, several significant issues limit the current contribution: (1) the MDP cost formulation has a potential double-counting issue that could affect the theoretical optimality claim; (2) Theorem 3.1 depends on an uncomputable constant Δ, creating a gap between theory and the practical algorithm; (3) the training-inference distribution shift for the prediction head is acknowledged but not quantified; (4) the claim of "strictly better Pareto frontiers" lacks statistical significance evidence; and (5) the forward-time measurement has a counterintuitive result that undermines the claimed overhead negligibility. Novelty and literature positioning cannot be fully verified due to Retrieval-Disabled Mode in this run and should be manually reviewed.

## Strengths
1. **Well-motivated problem and clean theoretical framing.** The paper identifies a genuine limitation of fixed-length speculative decoding — that the optimal candidate length varies per round — and provides a principled MDP formulation. Theorem 3.1 establishing that the optimal policy is a threshold on cumulative rejection probability is a theoretically interesting result that goes beyond the heuristic approaches in prior work (e.g., confidence thresholds in Liu et al. 2024, Kim et al. 2024).

2. **Pragmatic and lightweight implementation.** The decision to add a small prediction head (ResNet with 0-4 layers) on top of the frozen draft model, rather than retraining the draft model, is practical. The prediction head overhead is empirically shown to be negligible (within measurement noise), making the method easy to integrate into existing speculative decoding pipelines.

3. **Metric disentanglement.** The paper separates the evaluation into discard rate and verification rate metrics that are independent of hardware-specific forward times (tdraft, ttarget). This allows the Pareto frontier analysis (Figure 4) to generalize across hardware configurations, which is a thoughtful methodological choice.

4. **Solid empirical gains across datasets.** The reported improvements (7-11% relative speedup over fixed-length baseline) are consistent across three datasets with different characteristics: Alpaca (instruction-following), HumanEval (code), and GSM8K (math). The OOD evaluation suggests the method has some robustness to distribution shift.

5. **Comprehensive ablation study.** Table 3 systematically sweeps the three key hyperparameters (rejection weight wrej, network depth D, stopping threshold h) and identifies robust configurations that achieve >99% of peak performance across all datasets. The synergy analysis between wrej and h (heavier rejection weight → higher optimal threshold) is insightful and well-explained.

6. **Strong baseline comparison.** The baseline speculative decoding with tuned K is a fair and well-executed comparison, with K swept across a reasonable range. The forward-time linear regression (R² >= 0.98) confirms the cost model matches empirical measurements.

## Weaknesses
1. **[Major - Theory-Practice Gap] Theorem 3.1 depends on an uncomputable constant Δ.** The theoretical optimal stopping threshold involves Δ, which the authors themselves acknowledge "is hard to analyze theoretically or estimate empirically" (Appendix A). The practical algorithm replaces this with a trained prediction head and tunable threshold h, but the paper does not explain how h relates to Δ. This creates a gap between Contribution C1 (theoretical optimality) and the actual method.

2. **[Major - MDP Cost Double-Counting Risk] The immediate cost function in the MDP formulation has a subtle double-counting issue.** The cost for `continue` action is defined as I(∃1 ≤ i ≤ k+1, Yi is rejected) · c1, which includes previously generated tokens Y1...Yk. Since these tokens' drafting cost c1 was already accounted for in prior MDP steps, the same rejection event may be charged multiple times across successive `continue` actions. If this is the case, the derived threshold in Theorem 3.1 may be biased.

3. **[Major - Missing Statistical Significance] The claim "strictly better Pareto frontiers" is not supported by statistical evidence.** The paper shows aggregate discard rates and verification rates without variance estimates or confidence intervals. With only 150 test examples for HumanEval and GSM8K (Appendix C.1), the observed advantage could overlap with noise. The baseline K sweep range (2-14) is also narrower than SpecDec++'s max candidate length (20), creating a design-space asymmetry.

4. **[Major - Prediction Head Calibration Unknown] The training-inference distribution shift for the prediction head is acknowledged but not quantified.** The training loss uses mixed sequences (target-model and draft-model tokens interleaved), while inference uses pure target-model prefixes followed by draft tokens. The paper reports KL divergence on eval data from the same distribution as training, but not on the true inference distribution. The actual calibration error during inference is unknown, which affects confidence in the stopping decisions.

5. **[Major - Forward Time Measurement Anomaly] The paper reports that SpecDec++ has lower tdraft than the baseline SpecDec, which contradicts the expectation that adding a prediction head would increase computation.** The difference is attributed to "random noise," but this suggests the measurement may not be precise enough to support the claim of negligible overhead. Since the throughput calculations depend on these values, small measurement biases could affect the reported speedup ratios.

6. **[Minor - Regime Mismatch in Oracle Analysis] The motivating oracle analysis (Section 2.1) assumes greedy deterministic decoding, while the main experiments use stochastic sampling (temperature T=1, top-k).** The gap between the oracle upper bound (2.92x) and the achieved result (2.04x) is partially due to this regime difference, but the paper does not disentangle this from prediction head imperfection.

7. **[Minor - Conclusion Overclaim] The conclusion states the method "can be seamlessly integrated with other improvements" without any experimental validation of such integration.** While plausible, this claim is unsupported.

8. **[Deferred - Novelty Position] Due to Retrieval-Disabled Mode in this run, the novelty of the MDP formulation relative to confidence-threshold heuristics (Liu et al., Kim et al., Xu et al.) could not be fully verified against the literature.** Manual verification is needed to confirm that the trained prediction head provides a meaningful advantage over raw confidence thresholds.

## Key Issues
### Ranked Core Defect Board

| Rank | Defect | Severity | Validity Risk | Fixability | Confidence | Evidence Anchor |
|------|--------|----------|---------------|------------|------------|-----------------|
| 1 | MDP cost double-counting risk | Major | High — could bias the optimality claim | Medium — needs formal re-derivation or clarification | High | Page 5 - Immediate Costs definition |
| 2 | Theorem 3.1 depends on uncomputable Δ | Major | Medium — theory is motivational but the practical gap is glossed over | Low — Δ is inherently uncomputable | High | Page 6 - Theorem 3.1 + Appendix A |
| 3 | Prediction head calibration unknown | Major | Medium — distribution shift could cause suboptimal stopping | Medium — measure calibration on inference distribution | Medium | Page 7 - Weighted BCE loss |
| 4 | "Strictly better" lacks statistical support | Major | Medium — claim strength exceeds evidence | High — add CIs and significance tests | High | Page 8 - Performance Results |
| 5 | Forward time measurement anomaly | Major | Low-Medium — small effect | Medium — report regression CIs | Medium | Page 8 - Forward Time Analysis |

### Top Fatal/Fixable Analysis

- **Fatal issues:** None identified. The core idea (adaptive candidate length via learned prediction head) is valid and empirically demonstrated. The theoretical concerns weaken but do not invalidate the contribution.
- **Fixable issues (high impact):** The double-counting risk (Issue 1) and calibration measurement (Issue 3) can be addressed with clarifications and additional analysis without changing the algorithm. The statistical significance gap (Issue 4) can be addressed with bootstrapping.
- **Fixable issues (moderate effort):** The theory-practice gap (Issue 2) requires a more transparent discussion. The forward-time anomaly (Issue 5) needs better measurement reporting.

## Actionable Suggestions
### S1: Clarify the MDP Cost Model (Must — Page 5)
**Problem:** The immediate cost for `continue` includes the indicator over all k+1 tokens, which may double-count the drafting cost of earlier tokens.
**Action:** Add a clarifying derivation showing that over the full MDP trajectory, the cumulative cost equals Equation (2.2) without double-counting. Alternatively, redefine the cost as `I(Y_{k+1} is rejected) · c1` and explain that earlier rejection costs are incurred upon verification.
**Expected benefit:** Resolves a validity risk that could affect the theoretical optimality claim.

### S2: Acknowledge the Δ Limitation in Main Text (Must — Page 6)
**Problem:** Theorem 3.1's Δ is uncomputable, but the main text presents the threshold result without discussing this limitation.
**Action:** Add a sentence after Theorem 3.1: "Because Δ depends on the policy and problem instance and is not available at runtime, we cannot directly compute the optimal stopping threshold. Instead, we use a learned prediction head and treat h as a tunable hyperparameter, which corresponds to implicitly estimating the threshold structure."
**Expected benefit:** Bridges the theory-practice gap transparently.

### S3: Measure Prediction Head Calibration on Inference Distribution (Must — Page 7)
**Problem:** The paper reports KL divergence on eval data from the training distribution, not the true inference distribution.
**Action:** Run the trained prediction head on actual speculative decoding traces to produce a reliability diagram (expected calibration error) comparing predicted vs. empirical acceptance probabilities under inference conditions.
**Expected benefit:** Quantifies the distribution shift impact and validates whether the stopping decisions are well-calibrated.

### S4: Add Statistical Significance to Performance Claims (Must — Page 8)
**Problem:** "Strictly better Pareto frontiers" is not statistically supported.
**Action:** Report bootstrapped 95% confidence intervals for discard rates and verification rates in Figure 4. Add a paired significance test (e.g., Wilcoxon signed-rank) comparing throughputs of SpecDec++ vs. best fixed-K SpecDec.
**Expected benefit:** Strengthens the empirical claims and provides readers with uncertainty estimates.

### S5: Report Forward Time with Confidence Intervals (Must — Page 8)
**Problem:** The counterintuitive result (SpecDec++ tdraft < SpecDec tdraft) undermines the overhead claim.
**Action:** Report 95% confidence intervals for the regression coefficients (tdraft, ttarget) separately for each setting. Perform a significance test comparing SpecDec and SpecDec++ forward times.
**Expected benefit:** Either confirms the overhead is truly negligible or provides an adjusted (slightly higher) tdraft for SpecDec++.

### S6: Reposition the Oracle Analysis (Nice-to-have — Page 4)
**Problem:** The greedy decoding oracle analysis is used to motivate the approach, but the method is evaluated under stochastic sampling.
**Action:** Add a sentence noting that the oracle upper bound (2.92x) applies to greedy decoding, while the practical gains under stochastic sampling will be lower due to the inherent uncertainty.
**Expected benefit:** Prevents readers from incorrectly interpreting the gap between oracle and achieved speedups.

### S7: Strengthen Related Work Comparison (Nice-to-have — Page 9)
**Problem:** The comparison with confidence-threshold heuristics (Liu et al., Kim et al., Xu et al.) is too brief.
**Action:** Explicitly state the key differences: (a) raw draft-model confidence vs. trained prediction head, (b) marginal vs. cumulative decision criterion, (c) heuristic vs. MDP-derived stopping rule.
**Expected benefit:** Clarifies the novelty contribution and helps readers understand what is genuinely new.

### S8: Revise Conclusion (Nice-to-have — Page 9)
**Problem:** Unsupported claim about "seamless integration" and lack of specific limitations.
**Action:** Replace the final sentence with a bounded statement such as: "The prediction head adds negligible overhead and can be combined with orthogonal improvements to speculative decoding, such as draft-model distillation and token-tree verification, though these combinations remain to be empirically validated."
**Expected benefit:** Improves scientific credibility by not claiming unvalidated integration benefits.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows this structure:
- Paragraph 1: General LLM background + speculative decoding mechanism description.
- Paragraph 2: The K hyperparameter trade-off + critique of prior constant-rate assumption.
- Paragraph 3: MDP formulation + threshold theory + SpecDec++ proposal.
- Paragraph 4: Training challenges (class imbalance, sparse signal) + solutions.
- Paragraph 5: Empirical results summary.
- Paragraph 6: Contribution bullet list.

**Evaluation:** The current storyline is functional but could be significantly improved. The main weakness is that Paragraph 1 starts with general LLM background and a lengthy technical description of speculative decoding before establishing the specific research gap. Paragraph 2 introduces the K trade-off but does not fully motivate why adaptivity is necessary before Paragraph 3 presents the solution.

### Recommended Storyline (Option A — Best)

**Structure:** Big Picture → Specific Gap → Theory → Solution → Evidence → Contributions

- **Paragraph 1 (Stakes + Gap):** "LLM inference latency remains a bottleneck for deployment. Speculative decoding reduces latency by drafting K candidate tokens and verifying in parallel. However, the optimal candidate length K varies dynamically — when the draft model is confident, longer drafts are beneficial; when uncertain, shorter drafts avoid wasted computation. Existing methods use fixed K or simple confidence heuristics, which cannot capture this variability."

- **Paragraph 2 (Theory):** "We formalize adaptive K selection as a Markov Decision Process. The optimal policy is a threshold on the cumulative rejection probability: stop drafting when the risk of wasting computation exceeds the cost of verification. This theoretical result motivates our practical algorithm."

- **Paragraph 3 (Method):** "We propose SpecDec++, which trains a lightweight prediction head on the draft model to estimate token-level acceptance probabilities. At inference, it stops speculation when the predicted probability that any token will be rejected exceeds a tunable threshold h."

- **Paragraph 4 (Empirical Preview + Contributions):** "On llama-2-chat 7B&70B, SpecDec++ achieves 2.04x speedup on Alpaca (7.2% improvement), 2.26x on GSM8K (9.4%), and 2.23x on HumanEval (11.1%) over fixed-length speculative decoding. Our contributions are: (1) MDP formulation and threshold optimality proof, (2) SpecDec++ algorithm with trained prediction head, and (3) empirical validation."

### Alternative Storyline (Option B — Theory-First)

- **Paragraph 1 (Broad context):** LLM inference bottleneck and speculative decoding.
- **Paragraph 2 (Problem formalization):** Present the MDP formulation directly, then state Theorem 3.1 (threshold policy). This makes the theory the centerpiece.
- **Paragraph 3 (From theory to practice):** Explain that the threshold condition involves an uncomputable constant, motivating a learned approximation.
- **Paragraph 4 (SpecDec++ algorithm):** Prediction head, training procedure, stopping rule.
- **Paragraph 5 (Results + Contributions):** As in Option A.

**Evaluation:** Option A is recommended because it front-loads the gap and motivation, making it easier for readers to understand why adaptivity matters before encountering the MDP formalism. Option B would work for a more theory-focused venue but risks losing readers who are not familiar with MDPs.

### Abstract Outline (Complete)

S1 (Problem): "Speculative decoding accelerates LLM inference using a smaller draft model, but its efficiency depends on the candidate length K — the number of tokens drafted per round — which is typically fixed or chosen via simple heuristics."
S2 (Gap): "Prior theoretical analysis of optimal K assumes constant acceptance rates, which does not hold in practice as the alignment between draft and target models varies across contexts."
S3 (Solution): "We formulate adaptive K selection as a Markov Decision Process, proving that the optimal policy is a threshold on the cumulative rejection probability, and propose SpecDec++, which trains a lightweight prediction head to estimate this probability at inference time."
S4 (Evidence): "On llama-2-chat 7B&70B, SpecDec++ achieves 2.04x, 2.26x, and 2.23x speedup on Alpaca, GSM8K, and HumanEval respectively — 7-11% relative improvement over fixed-length speculative decoding."
S5 (Bounded Implication): "SpecDec++ preserves the exact output distribution of the target model and adds negligible computational overhead, making it a practical drop-in improvement for existing speculative decoding systems."

### Introduction Outline (Complete, Following Option A)

**P1 — Stakes and Gap (1 paragraph):**
- Role: Establish the practical importance of LLM inference efficiency and the specific limitation of fixed K in speculative decoding.
- Key claim: Fixed K is suboptimal because the draft-target alignment varies.
- Evidence: Refer to prior work (Leviathan et al. 2023) for the constant-rate assumption and its limitation.
- Transition: "This motivates our study of adaptive candidate length selection."

**P2 — Theory (1 paragraph):**
- Role: Present the MDP formulation and the threshold policy result (Theorem 3.1).
- Key claim: The optimal stopping policy is a threshold on cumulative rejection probability.
- Evidence: Theoretical result (proof deferred to appendix).
- Transition: "Building on this theoretical insight, we propose a practical algorithm."

**P3 — Method (1 paragraph):**
- Role: Introduce SpecDec++ and its two key components (prediction head, stopping rule).
- Key claim: A trained prediction head can estimate acceptance probabilities with negligible overhead.
- Evidence: Training procedure (weighted BCE loss, token mixing), inference rule.
- Transition: "We evaluate SpecDec++ on three datasets."

**P4 — Results + Contributions (1 paragraph):**
- Role: Summarize key empirical results and list contributions.
- Key claim: SpecDec++ consistently improves over fixed-length baseline.
- Evidence: Reported speedups on Alpaca, HumanEval, GSM8K.
- No transition needed (end of introduction).

### Three Alignment Checks

1. **Problem alignment (PASS):** The stated problem (K is suboptimally chosen) directly matches the proposed solution (adaptive K via prediction head). The critique that prior work assumes constant acceptance rates is directly addressed by the learned prediction head.

2. **Variable alignment (PASS):** The core concepts in the introduction (candidate length K, acceptance probability, stopping threshold) appear as key variables in the method (Eq. 3.1, Algorithm 2) and experiments (discard rate, verification rate).

3. **Contribution-evidence alignment (PARTIAL):** Contribution C1 (MDP + threshold theory) is partially supported — the MDP formulation is sound, but the threshold depends on an uncomputable Δ. Contribution C2 (SpecDec++ algorithm) is well-supported. Contribution C3 (empirical gains) needs stronger statistical evidence.

## Priority Revision Plan
### P0 — Publication-Critical (Must fix before acceptance)

| Priority | Action | Effort | Impact | Annotation Ref |
|----------|--------|--------|--------|----------------|
| P0.1 | Clarify the MDP cost model to resolve double-counting risk (S1) | Low (text change) | High — resolves validity risk in core theory | Page 5 - Immediate Costs |
| P0.2 | Acknowledge Δ limitation in main text (S2) | Low (text change) | High — closes theory-practice gap | Page 6 - Theorem 3.1 |
| P0.3 | Add statistical significance to performance claims (S4) | Medium (re-run with bootstrap) | High — supports main empirical claim | Page 8 - Performance Results |

### P1 — High Priority (Should fix before final submission)

| Priority | Action | Effort | Impact | Annotation Ref |
|----------|--------|--------|--------|----------------|
| P1.1 | Measure prediction head calibration on inference distribution (S3) | Medium (run inference traces + compute ECE) | Medium — quantifies robustness | Page 7 - Weighted BCE Loss |
| P1.2 | Report forward time with confidence intervals (S5) | Low (extract regression CIs) | Medium — validates overhead claim | Page 8 - Forward Time Analysis |
| P1.3 | Strengthen related work comparison (S7) | Low (text change) | Medium — clarifies novelty | Page 9 - Related Work |
| P1.4 | Revise conclusion to remove unsupported claim (S8) | Low (text change) | Medium — improves scientific credibility | Page 9 - Conclusion |

### P2 — Quality Improvement (Nice-to-have before submission)

| Priority | Action | Effort | Impact | Annotation Ref |
|----------|--------|--------|--------|----------------|
| P2.1 | Reposition oracle analysis with regime caveat (S6) | Low (text change) | Low — prevents misinterpretation | Page 4 - Oracle Analysis |
| P2.2 | Adopt recommended storyline (Option A) for introduction | Medium (rewrite 4 paragraphs) | Medium — improves readability | Page 1-2 - Introduction |
| P2.3 | Add abstract improvements (lossless property, precise gap) | Low (text change) | Low — polish | Page 1 - Abstract |

### ASCII Diagram — Revision Strategy Roadmap

```text
[Problem: MDP cost double-counting]
    -> [P0.1: Clarify cost definition]
    -> [Expected: Theory validity restored]

[Problem: Δ uncomputable, theory-practice gap]
    -> [P0.2: Acknowledge limitation in main text]
    -> [Expected: Transparent contribution framing]

[Problem: "Strictly better" Pareto claim unsubstantiated]
    -> [P0.3: Add bootstrap CIs + significance tests]
    -> [Expected: Statistical rigor established]

[Problem: Prediction head calibration unknown]
    -> [P1.1: Measure ECE on inference distribution]
    -> [Expected: Quantified calibration error]

[Problem: Forward time measurement noise]
    -> [P1.2: Report regression CIs]
    -> [Expected: Verified overhead claim]
```

### ASCII Diagram — Paper Structure & Evidence Map

```text
[Problem: Fixed K is suboptimal for speculative decoding]
    |
    v
[MDP Formulation (Section 3.1)]
    |-- States: s = (xprefix, (Y1,...,Yk))
    |-- Actions: {continue, stop}
    |-- Costs: c1 = tdraft, c2 = ttarget - tdraft
    |
    v
[Theorem 3.1: Threshold Policy]
    |-- Stop when P(rejection) >= (c2+Δ)/(c1+c2+Δ)
    |-- Caveat: Δ is uncomputable
    |
    v
[SpecDec++ Algorithm (Section 3.2)]
    |-- Trained prediction head estimates acceptance prob
    |-- Stop when 1 - prod(acceptance_probs) > h
    |
    v
[Empirical Validation (Section 4)]
    |-- Discard rate & verification rate Pareto frontier
    |-- Throughput comparison (Table 1)
    |-- Hyperparameter ablation (Table 3)
    |
    v
[Evidence Gaps]
    |-- No CIs on Pareto frontier → overclaim risk
    |-- No calibration on inference distribution
    |-- Forward time measurement noise
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (Data/Split/Protocol/Baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|---------------------------------------|---------|--------------|-----------------|-------------------|
| E1 | Oracle analysis: upper bound of spec decoding under greedy decoding | Alpaca prompts, llama-2-chat 7B&70B, greedy decoding, compare to target-only | Ntarget/N, throughput (tokens/s) | Oracle: 2.92x speedup, Ntarget/N = 0.164 | C1 (motivation) | Greedy regime only, assumes hindsight knowledge |
| E2 | Forward time verification: Eq (2.1) holds empirically | All prompts, both SpecDec and SpecDec++, linear regression on (Ndraft, Ntarget, Ttotal) | tdraft, ttarget, R² | R² ≥ 0.98, confirms linear cost model | C1 (cost model valid) | Anomalous result: SpecDec++ tdraft < SpecDec tdraft |
| E3 | Throughput comparison: SpecDec++ vs fixed-K baseline | Alpaca (2k test), HumanEval (150), GSM8K (150), llama-2-chat 7B&70B, temperature=1, top-k=50 | Tokens per second, speedup ratio | 2.04x Alpaca, 2.23x HumanEval, 2.26x GSM8K | C3 | No CIs, no significance tests |
| E4 | Pareto frontier analysis: discard rate vs verification rate | Same as E3, sweep K ∈ {2,4,6,8,10,12,14} for baseline, sweep (wrej, D, h) for SpecDec++ | Ndiscarded/N, Ntarget/N | SpecDec++ dominates baseline Pareto frontier | C2, C3 | No variance estimates, asymmetric design space |
| E5 | Hyperparameter ablation | Alpaca train/dev/test split, sweep wrej ∈ {1,3,6,12}, D ∈ {0,1,2,3,4}, h ∈ {0.1,0.3,0.5,0.7,0.9} | Binary KL divergence, throughput | wrej=6, D=3, h=0.7 achieves >99.3% of peak across datasets | C2 | KL measured on training distribution, not inference distribution |

### Research-Theme Gap Diagnosis

- **New knowledge (partially established):** The MDP formulation and threshold policy structure are new, but the Δ limitation downgrades the theoretical contribution from "actionable optimality condition" to "structural insight."
- **Reproducibility (mostly adequate):** Algorithm 2 and training details are specified. The main missing piece is hardware partitioning (which GPU holds which model) and the exact forward-time measurement methodology.
- **Impact on practice (good):** The lightweight prediction head approach is practical and could be adopted in production systems. The reported gains are meaningful (7-11% relative improvement) but modest enough to be realistic.
- **Weakest link:** The lack of calibration measurement and statistical significance testing weakens confidence in both the theoretical and empirical contributions.

### Proposed Research Experiments (P0/P1/P2)

#### P0 Experiment: Prediction Head Calibration Under Inference Distribution
- **Target Claim:** C2 — The prediction head produces well-calibrated acceptance probability estimates.
- **Hypothesis:** The calibration error on the true inference distribution is within acceptable range (ECE < 0.1).
- **Minimal Design:** Run SpecDec++ on 500 prompts, record predicted acceptance probabilities and actual acceptance outcomes at each position. Compute reliability diagram and Expected Calibration Error (ECE).
- **Controls/Baselines:** Compare against using raw draft-model confidence as the acceptance probability estimate (the heuristic from prior work).
- **Metrics:** ECE, reliability diagram, maximum calibration error.
- **Success Criterion:** ECE < 0.1 on the inference distribution. If ECE > 0.1, report calibration drift and suggest temperature scaling.
- **Estimated Cost/Time:** 20 GPU-hours (run inferences + compute metrics).
- **Expected Paper-Quality Gain:** Quantifies the distribution shift impact and validates the prediction head.

#### P1 Experiment: Statistical Significance of Throughput Gains
- **Target Claim:** C3 — SpecDec++ outperforms fixed-length SpecDec statistically significantly.
- **Hypothesis:** The throughput advantage of SpecDec++ is statistically significant across seeds and datasets.
- **Minimal Design:** Run both SpecDec++ and best fixed-K baseline 5 times with different random seeds. Report mean ± std. Conduct paired Wilcoxon signed-rank test on throughput per prompt.
- **Controls/Baselines:** Same as current experiments (fixed-K SpecDec).
- **Metrics:** Mean throughput, p-value, effect size.
- **Success Criterion:** p < 0.05 for all three datasets. If not significant, acknowledge and bound the claim.
- **Estimated Cost/Time:** 100 GPU-hours (5 runs × current eval cost).
- **Expected Paper-Quality Gain:** Provides rigorous statistical support for the main empirical claim.

#### P2 Experiment: Combining SpecDec++ with Draft-Model Distillation
- **Target Claim:** SpecDec++ is complementary to other improvements (DistillSpec, etc.).
- **Hypothesis:** Applying DistillSpec to the draft model before adding the prediction head yields additional gains.
- **Minimal Design:** (1) Train draft model with DistillSpec on Alpaca. (2) Train acceptance prediction head on top of distilled draft model. (3) Compare throughput against: (a) vanilla speculative decoding, (b) DistillSpec only, (c) SpecDec++ only.
- **Controls/Baselines:** All four combinations tested under identical settings.
- **Metrics:** Throughput, discard rate, verification rate.
- **Success Criterion:** DistillSpec + SpecDec++ outperforms each method individually. If not additive, analyze interference.
- **Estimated Cost/Time:** 300 GPU-hours (distillation + training + evaluation).
- **Expected Paper-Quality Gain:** Validates or refutes the "seamless integration" claim made in the conclusion.

### ASCII Diagram — Experiment Upgrade Plan

```text
[Current Evidence]
    |
    +-- E1: Oracle (greedy, hindsight) — motivational
    +-- E2: Forward time validation — partially inconsistent
    +-- E3/E4: Performance comparison — no CIs
    +-- E5: Hyperparameter ablation — eval on training distribution
    |
    v
[P0 - Low Effort, High Impact]
    |
    +-- Calibration measurement on inference distribution (P0.1)
    +-- Acknowledge Δ limitation + cost model fix (text changes)
    |
    v
[P1 - Medium Effort, High Impact]
    |
    +-- Multi-seed runs with significance tests (P1.1)
    +-- Forward time CIs (P1.2)
    |
    v
[P2 - Higher Effort, Medium Impact]
    |
    +-- DistillSpec + SpecDec++ combination experiment (P2.1)
    +-- Extended baseline K sweep to 20 (P2.2)
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

This score reflects the following evidence-grounded assessment:

- **Research value (primary dimension): 7/10.** The problem is well-motivated and practically important. The MDP formulation provides a principled framework for adaptive candidate length selection. The empirical gains (7-11% relative improvement) are meaningful but modest. The main research value is the combination of theoretical framing and a practical lightweight implementation.
- **Novelty (primary dimension): 6/10 (deferred manual verification).** The MDP formulation appears novel relative to the heuristic-based prior work cited in the paper, but full literature verification was not possible due to Retrieval-Disabled Mode. The core idea (learned prediction head for adaptive stopping) is a pragmatic engineering contribution rather than a fundamentally new paradigm.
- **Validity/soundness: 6/10.** The theoretical result (Theorem 3.1) is sound in structure but depends on an uncomputable constant Δ, which limits its actionable contribution. The MDP cost formulation has a potential double-counting issue that needs clarification. The empirical results lack statistical significance testing.
- **Reproducibility: 7/10.** Algorithm 2 and training details are well-specified. The main gaps are: (a) hardware partitioning between draft and target models not described, (b) forward-time measurement methodology not fully detailed, (c) prediction head calibration not measurable from provided data.
- **Presentation: 7/10.** The paper is generally well-written with clear figures and tables. The introduction could be strengthened by establishing the gap before describing the mechanism.

**Post-Revision Target: [7.5, 8.0] / 10**

This target assumes the following critical and major issues are addressed:
- **P0 items completed:** MDP cost clarified, Δ limitation acknowledged, statistical significance added.
- **P1 items completed:** Calibration measured, forward time CIs reported, related work strengthened.
- If these revisions are executed competently, the paper would earn a stronger score by resolving the main validity and rigor concerns. The score cannot exceed 8.0 without stronger empirical evidence (larger gains, more model pairs, or more comprehensive baselines) and full novelty verification against the literature.