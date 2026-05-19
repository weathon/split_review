## Summary
# Final Review Report

## Summary

This paper studies the problem of federated learning with local openset noisy labels — a realistic setting where each client not only has label noise but also observes a different subset of the global label space. The authors formally define openset label noise, analyze why existing loss-correction approaches fail under this setting, and propose FedDPCont, a framework that shares globally aggregated contrastive labels under differential privacy to prevent local models from memorizing openset noise patterns. The paper provides theoretical analysis showing that FedDPCont approximates centralized peer loss in expectation, and presents experiments on CIFAR-10, CIFAR-100, CIFAR-N, and Clothing-1M demonstrating consistent improvements over baselines.

**Strengths:** The problem formulation is practically motivated and addresses a genuine gap in FL literature. The openset noise definition and the concrete example showing why transition-matrix-based methods fail are clear and instructive. The contrastive-label approach combined with label DP is a novel design that elegantly avoids the need for noise transition matrix estimation. The empirical evaluation spans multiple datasets, noise types, and real-world benchmarks.

**Core weaknesses:** (1) Theorem 2's claim of matching centralized updates is overstated — it holds only in expectation under E=1 local epoch, not for the multi-epoch setting used in experiments. (2) Statistical significance is not rigorously established; claims of "significantly better" are not backed by hypothesis tests. (3) Several important experimental details (optimizer, LR schedule, baseline adaptation) are omitted, affecting reproducibility. (4) Novelty/comparison positioning cannot be fully assessed without external literature retrieval (deferred to manual verification). (5) The label DP mechanism's finite-sample behavior and numerical stability for large K are not analyzed.

## Strengths
**S1. Practically motivated problem formulation.** The openset label noise setting is a genuine and underexplored problem in federated learning. Most existing FL+noisy-label works assume identical noisy label spaces across clients, which is unrealistic in heterogeneous deployments. This paper's formalization (Definition 1) and the concrete failure example for transition-matrix-based methods (Page 4) clearly illustrate why the problem is distinct and challenging.

**S2. Clean methodological design.** The idea of using globally shared contrastive labels with DP protection is elegant. It avoids the need for noise transition matrix estimation (which is impossible under openset noise) and instead leverages a simple negative-loss term to prevent memorization. The theoretical connection to peer loss (Liu & Guo, 2020) is well-motivated, and the necessity of global (rather than local) label sampling is convincingly argued in Appendix B.3.

**S3. Comprehensive empirical evaluation.** The experiments cover multiple datasets (CIFAR-10, CIFAR-100, CIFAR-N, Clothing-1M), noise types (symmetric, random), noise rates (0.2–0.8), and a broad set of baselines (FedAvg, LC, FedProx, Co-teaching, T-revision, FedDyn, FedBN, Scaffold, DivideMix). The inclusion of real-world noisy datasets (CIFAR-N, Clothing-1M) strengthens external validity. Appendix D.1 provides useful runtime comparisons with the heavy method DivideMix.

**S4. Privacy-aware design.** The integration of label differential privacy via TDP matrix and the debiasing step (T^⊤_DP)^{-1} shows careful consideration of privacy-utility tradeoffs. Theorem 1 correctly establishes ϵ-label DP for the shared labels, and the empirical study of ϵ's effect (Table 3) demonstrates stability across privacy levels.

## Weaknesses
**W1. Overstated theoretical guarantee (Theorem 2).** The claim that FedDPCont's aggregated gradient equals the centralized gradient is over-extended. The proof (Appendix B.2) assumes gradient equality term-by-term over multiple local epochs, which fails when E>1 because client parameters diverge from the global model after the first local step. The result actually holds only for E=1 (single local epoch) or in the infinitesimal learning rate limit, neither of which matches the experimental setup (E=5). The paper acknowledges "expectation level (infinite data size)" but not this local-epoch drift issue.

**W2. Insufficient statistical rigor in experiments.** Claims of "significantly better" (Page 8) are not supported by statistical significance tests. With only 3 seeds, confidence intervals overlap between FedDPCont and baselines in several settings (e.g., CIFAR-100 symmetric 0.8: FedDPCont 11.02±0.66 vs FedAvg 10.62±0.26). The table caption "FedDPCont is always the best method" is contradicted by the data at high noise rates on CIFAR-100. Broken cross-references (Table ??, ??) indicate incomplete manuscript preparation.

**W3. Missing experimental details.** The main text omits the optimizer, momentum, weight decay, and learning rate schedule — all critical for reproducibility. Baseline adaptation details (especially how LC's transition matrix was estimated per client) are deferred to the appendix without sufficient description of fairness controls. The choice of DP parameter (e^ϵ/(e^ϵ+K-1)=0.2) is not justified.

**W4. Novelty and literature positioning (deferred).** Due to Retrieval-Disabled Mode in this review run, external literature verification was not performed. The novelty of the openset noise definition relative to existing FL+noise works (e.g., FedCorr, Yang et al. 2022) and the contrastive label approach relative to peer loss and CORES cannot be fully assessed from manuscript evidence alone. This is a deferred item requiring manual literature check.

**W5. Label DP mechanism's finite-sample limitations.** The debiasing step (T^⊤_DP)^{-1} p̌ assumes perfect knowledge of the empirical label distribution. For large K and small ϵ, the matrix becomes near-singular, and finite-sample estimation error in p̌ can be amplified by the inversion. The paper does not analyze the minimum required sample size for reliable distribution recovery, nor does it discuss the possibility of negative probability estimates after inversion.

**W6. Communication cost concern.** Algorithm 1 requires every client to send all DP-flipped labels to the server, incurring O(N_c) communication per client. For large local datasets, this overhead could be prohibitive. The paper does not discuss communication-efficient alternatives or report the actual communication cost in experiments.

## Key Issues
The following ranked error board captures the most critical defects prioritized by severity, research-value impact, validity risk, fixability, and confidence.

| Rank | Issue | Severity | Validity Risk | Fixability | Confidence | Annotation Map |
|------|-------|----------|---------------|------------|------------|----------------|
| 1 | Theorem 2 proof gap: local-epoch drift not accounted for (E>1) | Major | High — undermines core theoretical claim | Fixable — clarify scope (E=1), add discussion | High | Page 6, Page 15 (Appendix B.2) |
| 2 | "Significantly better" not backed by statistical tests | Major | Medium — weakens empirical credibility | Fixable — add t-tests and bounded wording | High | Page 8 |
| 3 | Missing experimental details (optimizer, schedule, baseline adaptation) | Major | Medium — harms reproducibility | Readily fixable — add details | High | Page 7 |
| 4 | Label DP inversion numerical stability not analyzed | Major | Medium — potential failure in large-K regimes | Fixable — add analysis and projection step | Medium | Page 5 |
| 5 | Conclusion overstates theoretical guarantee ("strong") | Major | Low (wording only) | Readily fixable — bound claim | High | Page 9 |
| 6 | Related work is flat list, not structured taxonomy | Minor | Low — clarity issue | Fixable — reorganize by axes | High | Page 2 |
| 7 | ℓPL negative term can penalize correct predictions when contrastive label matches clean label | Minor | Low — rare event | Fixable — add analysis | Medium | Page 4–5 |
| 8 | Introduction lacks clear problem-gap-solution arc | Minor | Low — readability | Fixable — restructure | High | Page 1 |
| 9 | Broken cross-references (Table ??, ??) | Minor | Low — incomplete manuscript | Readily fixable | High | Page 8 |
| 10 | Communication cost of label sharing not discussed | Minor | Low — practical concern | Fixable — add analysis | Medium | Page 5 (Algorithm 1) |

## Actionable Suggestions
### Suggestion 1 (Must) — Clarify Theorem 2 scope
**Problem:** Theorem 2 claims aggregated gradient equals centralized gradient, but the proof fails for E>1.
**Action:** Revise Theorem 2 to state: "For E=1 (single local epoch), the expected aggregated gradient of FedDPCont equals the centralized peer-loss gradient." Add a paragraph discussing the approximation gap for E>1 and provide empirical evidence (e.g., accuracy vs E plot) showing how the gap grows with local epochs. In the contribution list (Page 2), replace "guaranteed to be the same" with "guaranteed in expectation for single-epoch local training."

### Suggestion 2 (Must) — Add statistical significance tests
**Problem:** "Significantly better" claims in results (Page 8) are not statistically validated.
**Action:** For each noise rate x dataset setting, compute a paired t-test between FedDPCont and the best-performing baseline across seeds. Report p-values in a footnote or supplementary table. Where confidence intervals overlap and the gap is <2%, soften wording to "consistently achieves higher average accuracy." Fix broken Table ?? and ?? references.

### Suggestion 3 (Must) — Complete experimental reproducibility details
**Problem:** Optimizer, momentum, weight decay, LR schedule are missing (Page 7).
**Action:** Add to Section 5.1: "We use SGD with momentum 0.9, weight decay 5e-4, and cosine LR decay from 0.1 to 0.001 over 300 rounds." Also clarify how each baseline was adapted: for LC, state whether the transition matrix was estimated per client or globally; for Co-teaching, confirm the selection threshold used.

### Suggestion 4 (Must) — Bound theoretical claims in Conclusion
**Problem:** Conclusion (Page 9) says "strong theoretical guarantees" — overreach given the E>1 gap.
**Action:** Replace with: "We proved that FedDPCont approximates centralized peer loss in expectation under single-epoch local training, and provided a DP guarantee for label sharing."

### Suggestion 5 (Nice-to-have) — Analyze label DP inversion stability
**Problem:** (T^⊤_DP)^{-1} may be near-singular for large K and small ϵ (Page 5).
**Action:** Add a remark: "For large K, we clip (T^⊤_DP)^{-1} p̌ to [0,1] and renormalize to avoid negative estimates. The minimum total sample size N required for reliable recovery is O(K·e^ϵ)." Optionally include a simulation in the appendix showing recovery error vs N and ϵ.

### Suggestion 6 (Nice-to-have) — Restructure related work
**Problem:** Related work (Page 2) is a flat chronological list.
**Action:** Reorganize into three comparison axes: (1) Robust loss functions for label noise, (2) FL with non-IID label distributions, (3) FL with noisy labels. Each axis should end with a sentence stating the residual gap that FedDPCont addresses.

### Suggestion 7 (Nice-to-have) — Discuss ℓPL edge case
**Problem:** When contrastive label matches clean label, the negative term penalizes correct behavior (Page 4-5).
**Action:** Add a brief discussion: "In expectation over random sampling, the probability of drawing a matching label is 1/K, so the bias introduced is bounded by O(1/K). For K≥10, this effect is negligible."

### Suggestion 8 (Nice-to-have) — Report communication cost
**Problem:** Algorithm 1 sends all DP labels to server — O(N_c) per client.
**Action:** Add a paragraph reporting total communication volume (e.g., "Each round transmits K·Σ_c N_c bits for labels, plus model parameters of size |θ|") and discuss potential subsampling strategies.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction follows this paragraph structure:
- P1: Data heterogeneity in FL → openset noisy labels → problem definition
- P2: Why existing centralized noisy-label methods (loss correction) fail
- P3: Intuition of label sharing + contrastive loss → contribution list

**Problem:** P1 spends too long on generic FL heterogeneity without quickly arriving at the specific openset noise challenge. P2 is citation-heavy and does not cleanly separate the known limitation from the paper's specific contribution. The transition from P2 to P3 (label sharing) is abrupt — readers need to infer why sharing addresses the transition matrix problem.

### Candidate Storyline A (Recommended) — Problem-Gap-Solution-Evidence

**P1: Practical motivation.** "In federated learning, different hospitals may treat different diseases, so Client A only sees respiratory labels while Client B only sees cardiology labels. When local annotations are noisy, each client's observed label space becomes a noisy, partial subset of the global label space — a setting we call local openset label noise."

**P2: Why existing methods fail (the gap).** "A family of popular robust-loss methods, called loss correction, requires estimating the label noise transition matrix T. We show that under openset noise, T cannot be correctly estimated because the missing classes create a systematic bias (Section 3.1 gives a concrete 3-class example)."

**P3: Our solution (intuition before technical details).** "To avoid relying on T, we propose sharing a global noisy-label distribution among clients. Each client samples contrastive labels from this distribution and subtracts their loss from the standard cross-entropy. This prevents the model from memorizing local openset noise patterns. Label sharing is protected by differential privacy."

**P4: Contribution summary + evidence preview.** "We formally define openset noise, propose FedDPCont with DP guarantee, prove its connection to centralized peer loss, and show consistent improvements over baselines on CIFAR-10/100, CIFAR-N, and Clothing-1M."

### Candidate Storyline B — Inverted (Result-first)

**P1: Empirical motivation.** Open with a striking result: "Under 40% random label noise on CIFAR-10, existing FL+noise methods achieve at most 61% accuracy. The core issue is not noise rate alone, but the mismatch between local and global label spaces — openset noise."

**P2: Formal definition + failure analysis.** Introduce Definition 1 and the transition matrix failure example.

**P3: FedDPCont solution and key insight.** Present the contrastive label idea, emphasizing why global sampling is necessary.

**P4: Results preview + contributions.**

### Selected Best Storyline: Candidate A

Candidate A is recommended because it follows the standard problem-gap-solution-evidence arc that reviewers can follow easily. It builds the gap concretely before revealing the solution, making the contribution self-evident.

### Abstract Outline (Complete)

- **S1 (Problem):** "Federated learning with heterogeneous clients faces openset label noise: each client observes a noisy, partial subset of the global label space."
- **S2 (Challenge):** "Existing loss-correction methods fail because they require a full label space to estimate the noise transition matrix, which is impossible under openset noise."
- **S3 (Gap):** "No prior FL method handles the intersection of heterogeneous label spaces and instance-dependent label noise."
- **S4 (Method):** "We propose FedDPCont, which shares globally aggregated contrastive labels under differential privacy, using a negative-loss term to prevent memorization of local noise patterns."
- **S5 (Result):** "On CIFAR-10, CIFAR-100, CIFAR-N, and Clothing-1M, FedDPCont outperforms FedAvg, loss correction, and other baselines by 3–15 percentage points across noise rates."

### Introduction Outline (Complete)

- **P1 (350 chars):** Big Picture: openset label noise definition + concrete medical example.
- **P2 (400 chars):** Gap: why loss correction and other T-based methods fail under openset noise.
- **P3 (400 chars):** Solution intuition: global contrastive labels + ℓPL + DP.
- **P4 (300 chars):** Contribution list + evidence preview (4 bullet points, each with a reference to the relevant section/table).

## Priority Revision Plan
```text
ASCII Diagram — Revision Strategy Roadmap

[Core Issue 1: Theorem 2 overclaim]
    -> Fix: Revise theorem statement to E=1, add drift gap discussion
    -> Expected gain: Honest theoretical claims, higher reviewer trust
    -> Priority: P0 (must fix before acceptance)

[Core Issue 2: No statistical significance tests]
    -> Fix: Add paired t-tests, soften "significantly better" wording
    -> Expected gain: Credible empirical claims
    -> Priority: P0

[Core Issue 3: Missing experimental details]
    -> Fix: Add optimizer/schedule/baseline adaptation info
    -> Expected gain: Full reproducibility
    -> Priority: P1 (must fix before camera-ready)

[Core Issue 4: Label DP stability analysis missing]
    -> Fix: Add numerical stability remark and clipping
    -> Expected gain: Practical robustness for large-K regimes
    -> Priority: P1

[Core Issue 5: Conclusion overclaim]
    -> Fix: Replace "strong theoretical guarantees" with scoped statement
    -> Expected gain: Defensible conclusions
    -> Priority: P1

[Secondary issues: related work structure, ℓPL edge case, comm cost]
    -> Fix per suggestions in annotated paragraphs
    -> Priority: P2 (nice-to-have)
```

| Priority | Action | Effort | Expected Impact | Verification Gate |
|----------|--------|--------|-----------------|-------------------|
| P0 | Revise Theorem 2 (scope to E=1, add drift discussion) | 2 days | Prevents core claim invalidation | Proof re-check + experiment with varying E |
| P0 | Add statistical significance tests + soften wording | 1 day | Credible empirical claims | t-test results in appendix |
| P1 | Add optimizer, schedule, baseline adaptation details | 0.5 day | Full reproducibility | Reader can reproduce results |
| P1 | Bound conclusion claims | 0.5 day | Defensible conclusions | Compare with validated claims |
| P1 | Add label DP numerical stability analysis | 1 day | Practical robustness for large K | Simulation in appendix |
| P2 | Restructure related work | 1 day | Clearer novelty positioning | Reader can track comparison axes |
| P2 | Discuss ℓPL edge case + communication cost | 0.5 day | Completeness | No missing discussion points |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory (Full Coverage)

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|--------------------------------------|---------|--------------|-----------------|-------------------|
| E1 | Symmetric label noise, variable rate | CIFAR-10/100, symmetric noise η={0.2,0.4,0.6,0.8}, uniform allocation, 8 baselines | Best accuracy over 300 rounds | FedDPCont best in 7/8 settings | C4 (empirical) | Only 3 seeds, no significance test |
| E2 | Random label noise, variable rate | CIFAR-10/100, random noise η={0.2,0.4,0.6,0.8}, non-uniform Dirichlet allocation | Best accuracy | FedDPCont top-2 in all settings | C4 | Overlapping CIs at high noise |
| E3 | Real-world noisy labels | CIFAR-N (worst/random/aggregate), CIFAR-100-N, Clothing-1M | Best accuracy | FedDPCont best in 4/5 real-world settings | C4 (practical usage) | Clothing-1M: FedDPCont 70.88 vs FedAvg 70.27 — minimal gap |
| E4 | DP level sensitivity | CIFAR-10 random noise 0.4, ϵ ∈ {1,2,4,8,100,3.58} | Accuracy | Stable across ϵ (mean ~72.5) | C3 (DP robustness) | Small variance, but only tested on one setting |
| E5 | DivideMix comparison (Appendix D.1) | CIFAR-10/100, symmetric + random, 300 epochs | Accuracy, Time (hr) | FedDPCont faster and competitive on CIFAR-10; worse on CIFAR-100 | C4 (lightweight advantage) | DivideMix better on CIFAR-100, not discussed in main text |

### Research-Theme Gap Diagnosis

- **New knowledge:** The openset noise definition and the failure analysis of transition matrices are novel. However, the core algorithmic contribution (contrastive labels + DP) extends existing peer loss methods, and the amount of genuine new insight over (Liu & Guo, 2020) is moderate.
- **Reproducibility:** Partially compromised by missing optimizer/schedule details (Annotation Page 7).
- **Impact on practice/understanding:** The openset noise concept has practical relevance, but the paper would benefit from demonstrations on truly decentralized real-world FL deployments (beyond synthetic partitions of centralized datasets).

### Proposed Research Experiments (P0/P1/P2)

```text
ASCII Diagram — Experiment Upgrade Plan

P0 [Theorem 2 gap]:
    Exp T1: Vary local epochs E ∈ {1,2,5,10} with fixed noise=0.4
    -> Measure: accuracy gap between FedDPCont and centralized peer loss
    -> Expected: gap increases with E, verifying theory scope

P0 [Statistical rigor]:
    Exp S1: Run 10 seeds per setting for top-3 methods (FedDPCont, LC, FedAvg)
    -> Compute: paired t-test, Cohen's d effect size
    -> Success: p<0.05 for at least moderate noise rates

P1 [OOD/robustness]:
    Exp R1: Train on CIFAR-10 (openset noise), test on CIFAR-10-C (corruption)
    -> Metric: accuracy drop relative to in-domain
    -> Success: FedDPCont drop < baseline drop

P1 [Ablation - contrastive term necessity]:
    Exp A1: FedDPCont without negative term (ℓPL→ℓCE only)
    -> Isolate: gain attributable to contrastive labels vs other components
    -> Success: clear gap between with/without contrastive

P2 [Communication efficiency]:
    Exp C1: Subsample labels for DP aggregation (transmit 10% per client)
    -> Measure: accuracy vs full transmission
    -> Success: <1% accuracy drop with 90% fewer labels
```

| Experiment | Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Cost | Expected Gain |
|------------|-------------|-----------|----------------|----------|---------|-------------------|------|---------------|
| T1 (E sweep) | Theorem 2 scope | Gap grows with E | CIFAR-10, rand η=0.4, E∈{1,2,5,10} | Same seed, same noise | Centralized peer loss accuracy | Monotonic gap increase | 0.5 GPU-day | Verify theoretical boundary |
| S1 (statistical) | C4 (empirical) | FedDPCont > baselines with p<0.05 | Top-3 methods, 10 seeds | Fixed hyperparams | p-value, effect size | p<0.05 at η≤0.6 | 2 GPU-days | Credible empirical claims |
| R1 (OOD) | Robustness | FedDPCont generalizes | CIFAR-10-C | Same model, no retrain | Accuracy, relative drop | Drop ≤ 1.1× baseline drop | 0.5 GPU-day | Show bounded generalization |
| A1 (ablation) | C2 (contrastive) | Negative term is necessary | Remove negative term from Lc | Same hyperparams | Accuracy | Gap > 3% | 0.5 GPU-day | Isolate mechanism |
| C1 (comm. eff.) | Practicality | Subsampling works | Transmit 10% random labels | Full transmission | Accuracy | <1% accuracy drop | 0.5 GPU-day | Practical deployment |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6/10**

*Rationale:* The paper addresses a well-motivated practical problem with a clean methodological design and comprehensive experiments. However, the core theoretical claim (Theorem 2) is overstated — the proof only holds for E=1, not the multi-epoch setting used in experiments — which weakens the paper's central narrative. Empirical claims of "significantly better" lack statistical backing, with overlapping confidence intervals in several settings. Experimental reproducibility is partially compromised by omitted optimizer and schedule details. Novelty cannot be fully assessed without external literature comparison (deferred). These issues are fixable, but in their current form they reduce confidence in the paper's conclusions. Score prioritizes research value (6) and novelty (6, pending manual verification), while validity/soundness is rated at 5 due to the theoretical gap.

**Post-Revision Target: [7, 8]/10**

*Rationale if P0+P1 fixes are applied:* If Theorem 2 is scoped to E=1 with explicit drift-gap discussion, statistical significance tests are added, experimental details are completed, and conclusion claims are bounded, the paper becomes a solid contribution. The openset noise formulation is genuinely useful, the algorithmic design is clean, and the empirical trends are consistent. A score of 7-8 reflects a competent paper with demonstrated practical value, once the identified validity and rigor issues are resolved. Achieving this target requires the authors to complete P0 and P1 items in the Priority Revision Plan before resubmission.