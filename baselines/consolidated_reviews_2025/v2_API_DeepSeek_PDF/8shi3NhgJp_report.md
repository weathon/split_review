## Summary
# Final Review Report

## Summary

This paper introduces Imprecise Bayesian Continual Learning (IBCL), a method for Continual Learning under Specific Trade-offs (CLuST). The core idea is to replace per-preference retraining (required by rehearsal-based methods) with a constant-time convex combination of posterior distributions stored in a finitely generated credal set (FGCS). The paper makes three claims: (C1) formalizing the CLuST problem with efficiency requirements, (C2) proposing IBCL as a Bayesian CL algorithm that generates models via convex combination, and (C3) empirical validation on four benchmarks. The approach is conceptually interesting—leveraging imprecise probability theory to amortize preference-specific model generation—and the efficiency improvement over rehearsal-based methods is a valid research direction. However, the paper has several significant issues: the Pareto-optimality guarantee (Theorem 2) is a definitional tautology rather than a substantive result, the key Assumption 1 on task similarity is untestable and unverified, the evaluation lacks statistical rigor (single seed, 10 random preferences, no confidence intervals), and several writing/positioning claims (e.g., "first to rigorously formulate") are overstated. With substantial revisions, the paper could be a solid contribution.

## Strengths
1. **Problem framing is timely and practical.** The CLuST formulation—generating customized models for arbitrary stability-plasticity trade-offs without per-preference retraining—addresses a genuine need in deployed continual learning systems (e.g., recommendation systems, personalized assistants). The paper clearly identifies the efficiency gap in existing rehearsal-based approaches.

2. **Imprecise probability theory is a novel angle for CL.** The use of finitely generated credal sets (FGCS) from imprecise probability to represent the knowledge base is a creative connection that distinguishes IBCL from standard Bayesian CL methods. This framework naturally captures epistemic uncertainty through a convex set of distributions rather than a single posterior.

3. **Constant-time model generation is well-motivated.** The core algorithmic insight—replacing per-preference retraining with convex combination of FGCS extreme elements—is clean and principled. If the theoretical assumptions hold, this provides a substantial efficiency advantage over methods whose training overhead scales linearly with the number of preferences.

4. **Comprehensive ablation studies.** The appendix includes ablations on the distance threshold d, significance level α, number of priors, prior variance, and β weights, which helps characterize the algorithm's sensitivity to hyperparameters. The "equal β" simplification is empirically justified.

5. **Domain-incremental setting is cleanly scoped.** The paper restricts to domain-incremental CL (shared input/label space, no task IDs), which simplifies the problem and makes the convex combination approach tractable. This scope is clearly communicated.

## Weaknesses
1. **Theorem 2 is a definitional tautology, not a substantive guarantee (Major).** The claim that the HDR contains the true parameter with probability ≥ 1−α is a direct consequence of how HDRs are defined (Definition 2/5), not a novel algorithmic guarantee. The substantive gap—whether the estimated convex-combination distribution q̂_w approximates the true posterior of p_w—is unaddressed theoretically.

2. **Assumption 1 (task similarity) is strong and unverified (Major).** The assumption that all task distributions lie in a convex set F with bounded Wasserstein diameter r is central to the theoretical framework but is not tested empirically for any of the four benchmarks. If violated, the algorithm could suffer catastrophic forgetting even with exact Bayesian inference (as the paper itself notes via Kessler et al. 2023). No sensitivity analysis is provided for r.

3. **Single-seed evaluation without statistical rigor (Major).** All experiments are run once (single seed). Given the stochastic nature of variational inference and random preference sampling (n_prefs=10), the reported improvements of "up to 45%" could be within noise. No confidence intervals, significance tests, or variance estimates are reported in the main text.

4. **Prior variance inconsistency across benchmarks (Major).** CelebA uses 10× smaller prior standard deviations ({0.2,0.25,0.3}) than the other three benchmarks ({2,2.5,3}), and a different learning rate (1e-3 vs 5e-4). This discrepancy is not discussed, and its impact on the reported results is unclear.

5. **Pareto-optimality via convex combination is unverified for non-convex settings (Major).** The paper assumes that convex combination of task-specific posterior distributions yields Pareto-optimal distributions for the preference-weighted objective. This is justified only under strong convexity assumptions that do not hold for Bayesian neural networks. No empirical validation on a synthetic problem with known Pareto front is provided.

6. **Unconventional use of "zero-shot" (Minor).** The term "zero-shot" typically refers to generalization to unseen classes/tasks without training examples. Here it means "no retraining for new preferences," which is creative but may confuse reviewers expecting the standard definition.

7. **Overclaim on efficiency (Minor).** IBCL's training overhead (28,614 batch updates on CelebA) is higher than L2P (9,538). The "constant overhead" advantage is only realized when the number of preferences exceeds a crossover point that is not analyzed.

8. **Missing quantitative results table (Minor).** The Results section relies entirely on visual trends in Figures 3-6 without a summary table of concrete accuracy values, confidence intervals, or per-benchmark comparisons.

## Key Issues
### Issue 1: Theorem 2 is a Definitional Tautology (Severity: Major, Object: Issue)

**Evidence anchor:** Page 8 - Theorem 2 and surrounding text (lines 58-77). The theorem states that `Pr[θ*_w ∈ Θ^α_w] ≥ 1-α` under distribution q̂_w.

**Root cause:** The theorem's conclusion follows directly from the definition of Highest Density Regions (Definition 2/5): the HDR is defined as the smallest region containing (1-α) probability mass under the specified distribution. Theorem 2 merely restates this definition while applying it to q̂_w.

**Scientific risk:** The paper presents this as a key theoretical guarantee ("Probabilistic Pareto-optimality"), but it does not establish that q̂_w is the correct posterior for p_w. Without this link, the guarantee is vacuous: any distribution's HDR trivially contains (1-α) of its own mass.

**Required action:** Rewrite Theorem 2 to clarify it is an HDR coverage property, not a Pareto-optimality result. Add theoretical or empirical evidence that q̂_w → p_w posterior as data increases.

---

### Issue 2: Assumption 1 (Task Similarity) is Unverified (Severity: Major, Object: Issue)

**Evidence anchor:** Page 4 - Assumption 1 (lines 89-91).

**Root cause:** The assumption requires all task distributions to lie within a convex set F with bounded 2-Wasserstein diameter r. No empirical verification is performed for any of the four benchmarks (CelebA, CIFAR-100, TinyImageNet, 20NewsGroup). The paper acknowledges (via Kessler et al. 2023) that violating this assumption can cause catastrophic forgetting even with exact Bayesian inference.

**Scientific risk:** If the assumption is violated, all theoretical guarantees (Theorem 1, 2) may break, and the algorithm may perform no better than standard BCL.

**Required action:** Add empirical verification of Assumption 1 by estimating pairwise 2-Wasserstein distances between learned posteriors. Report a sensitivity analysis with intentionally dissimilar task sequences to test robustness to assumption violation.

---

### Issue 3: Insufficient Statistical Rigor in Evaluation (Severity: Major, Object: Issue)

**Evidence anchor:** Page 8 - Metrics paragraph (lines 107-114); Page 9-10 - Results (lines 64-89).

**Root cause:** (a) Single-seed evaluation for all experiments. (b) Only 10 random preferences sampled per task. (c) No confidence intervals or significance tests reported. (d) The key numerical claims ("up to 45% improvement") are reported without baseline-specific deltas.

**Scientific risk:** Without variance quantification, the reported improvements may be statistically insignificant. The "at most 45%" claim uses L2P as baseline on 20NewsGroup, where the paper notes L2P "generally works poorly" — this is a weak comparator.

**Required action:** Report mean±std over ≥3 seeds. Increase preference samples to ≥50 per task or use deterministic grid sampling. Add statistical significance tests.

---

### Issue 4: Prior Variance Inconsistency Across Benchmarks (Severity: Major, Object: Issue)

**Evidence anchor:** Page 19 - Appendix H (lines 66-76).

**Root cause:** CelebA uses prior standard deviations 10× smaller than other benchmarks (0.2/0.25/0.3 vs 2/2.5/3), with a different learning rate (1e-3 vs 5e-4). This difference is not justified, and no control experiment with uniform priors is reported.

**Scientific risk:** The CelebA results may be partially attributable to stronger regularization (narrower priors) rather than the IBCL algorithm. Cross-benchmark comparisons are confounded.

**Required action:** Add a CelebA control experiment with priors {2,2.5,3} and explain the rationale for different hyperparameters, or standardize all benchmarks to use the same prior family.

## Actionable Suggestions
### S1. Reframe Theorem 2 as an HDR coverage property, not Pareto-optimality guarantee (Must)

Replace "Probabilistic Pareto-optimality" with "HDR Coverage Property." Explicitly state that Theorem 2 follows from the definition of HDRs (Definition 2/5) and that the substantive challenge is whether the estimated distribution q̂_w approximates the true posterior of p_w. Add this clarification:

**Replace Theorem 2 text (Page 8, lines 58-77) with:**
"**Theorem 2 (HDR Coverage).** By construction of the α-level HDR (Definition 2), we have Pr_{θ∼q̂_w}[θ ∈ Θ^α_w] ≥ 1-α. This is a standard property of HDRs. The practical utility of this result depends on how well q̂_w approximates the true posterior of p_w; we provide empirical evidence for this approximation in Section 5.2 and Appendix I."

### S2. Add multi-seed evaluation with confidence intervals (Must)

Report all main results (average per-task accuracy, peak per-task accuracy, backward transfer) as mean ± std over 3 random seeds. Increase the number of sampled preferences from 10 to 50 per task (or use deterministic grid sampling for small task counts). Add a sentence:

**Add after Metrics paragraph (Page 8, line 114):**
"All metrics are reported as mean ± std over 3 independent runs with different random seeds and preference samples. We use 50 randomly sampled preferences per task. Statistical significance against the best baseline is assessed via a paired bootstrap test (p < 0.05)."

### S3. Add empirical verification of Assumption 1 (Must)

Include a new appendix section (Appendix J) that reports pairwise 2-Wasserstein distances between learned posterior distributions for each benchmark. Show that the maximum pairwise distance is bounded by some r, or discuss when it exceeds reasonable bounds.

### S4. Add a quantitative results table (Must)

Create Table 2 reporting: Benchmark | Method | Final Avg Accuracy | Peak Accuracy | Backward Transfer. Include 95% CI for all metrics.

### S5. Add a crossover analysis for training efficiency (Nice-to-have)

Compute the breakeven number of preferences at which IBCL becomes more efficient than rehearsal methods.

### S6. Add a control experiment for prior variances (Must)

Run CelebA with priors {2, 2.5, 3} to verify that the performance gain is not an artifact of narrower priors.

### S7. Replace "first to rigorously formulate" with a scoped claim (Must)

Change Contribution (1) from "We are the first to rigorously formulate the CLuST problem" to "We provide a novel formalization of the CLuST problem that targets efficiency under an unbounded number of preferences — a direction not addressed in prior preference-based CL formulations."

### S8. Expand limitations section (Must)

**Replace the current limitations paragraph (Page 10, lines 100-106) with:**
"Limitations: (i) The theoretical guarantees rely on Assumption 1 (task similarity), which is untested for the reported benchmarks. (ii) The Pareto-optimality guarantee holds under the assumption that convex combinations yield Pareto-optimal distributions — this is unverified for non-convex BNN settings. (iii) All experiments use a small BNN (64 hidden units); scaling to larger architectures is future work. (iv) Results are from single-seed runs without statistical significance testing. (v) The algorithm's performance depends on hyperparameters d and m, which require tuning."

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction follows this structure:
- P1: CL definition + stability-plasticity trade-off → CLuST problem
- P2: "Why CLuST is important" (motivation)
- P3: Movie recommendation example
- P4-P5: Bayesian formalization + critique of rehearsal methods
- P6-P7: IBCL solution description + contributions

**Problems:** The gap between problem statement and proposed solution is not sharp enough. The movie example (P3) conflates genre preference with stability-plasticity trade-off. The Bayesian formalization (P4) appears before readers fully understand why existing methods fail.

### Recommended Storyline: "Problem-Solution-Evidence" Arc

**Paragraph plan:**

- **P1:** CL and the stability-plasticity trade-off → The understudied problem of generating customized models for specific trade-off points (CLuST). State the core challenge: existing methods require per-preference retraining, which is prohibitive when preferences are many or unbounded.

- **P2:** Concrete application scenario (streamlined). "Consider a movie recommendation system that must serve millions of users, each with a unique stability-plasticity preference over genres. Training a separate model per user is infeasible." This directly illustrates the efficiency requirement without conflating genre preference with trade-off preference.

- **P3:** Formalize CLuST in one paragraph: domain-incremental setting, preference vectors, three requirements (zero-shot generation, probabilistic coverage, sublinear buffer growth). State what the paper achieves.

- **P4:** Key idea without technical overload: "Our key insight is that if we maintain the set of all task-specific posterior distributions as a convex set (a credal set), then any preference-weighted model can be obtained as a convex combination in constant time."

- **P5:** Contributions (revised, scoped wording).

### Abstract Outline (Revised)

**S1 (Problem):** Continual learning requires balancing stability (remembering old tasks) and plasticity (adapting to new tasks). When customized models for specific stability-plasticity trade-offs are needed, existing methods require retraining for each trade-off, which is inefficient.

**S2 (Gap):** This inefficiency becomes prohibitive when the number of trade-off preferences is large or unbounded, as in personalized recommendation or user-adaptive systems.

**S3 (Method):** We propose Imprecise Bayesian Continual Learning (IBCL), which maintains a convex set of posterior distributions (finitely generated credal set) and generates a model for any given trade-off via convex combination in constant time—no retraining needed.

**S4 (Evidence):** Experiments on four continual learning benchmarks show that IBCL improves average per-task accuracy by up to 45% and peak per-task accuracy by up to 43% over existing CLuST baselines, while maintaining near-zero backward transfer and constant training overhead independent of the number of preferences.

**S5 (Scope):** Limitations discussed: the approach assumes task similarity (bounded Wasserstein distance) and is demonstrated on small-scale Bayesian neural networks; scaling to larger architectures remains future work.

## Priority Revision Plan
### P0: Must-fix before resubmission (high impact, moderate effort)

| Priority | Issue | Required Action | Expected Impact |
|----------|-------|-----------------|-----------------|
| P0 | Theorem 2 tautology (Issue 1) | Rewrite Theorem 2 as HDR coverage property; clarify it is definitional, not substantive | Restores theoretical credibility |
| P0 | Multi-seed statistics (Issue 3) | Add 3-seed evaluation, 50 preferences/task, confidence intervals, significance tests | Enables statistical validation of claims |
| P0 | Prior variance inconsistency (Issue 4) | Add CelebA control with standard priors; explain or standardize hyperparameters | Ensures fair cross-benchmark comparison |
| P0 | "First to formulate" overclaim (S7) | Replace with scoped claim | Avoids rejection over unverifiable novelty |
| P0 | Expand limitations (S8) | Add 5 explicit limitations: assumption dependence, non-convex gap, small-scale only, single-seed, hyperparameter sensitivity | Shows reviewer awareness of scope |

### P1: Should fix (high impact, higher effort)

| Priority | Issue | Required Action | Expected Impact |
|----------|-------|-----------------|-----------------|
| P1 | Assumption 1 verification (S3) | Add pairwise W2 distance analysis; add sensitivity experiment with dissimilar tasks | Validates theoretical foundation |
| P1 | Quantitative results table (S4) | Add Table 2 with mean±std for all metrics | Enables verifiable evidence for claims |
| P1 | IBCL-L2P efficiency crossover (S5) | Compute breakeven n_prefs for each benchmark | Clarifies efficiency advantage scope |

### P2: Nice-to-have (medium impact, low effort)

| Priority | Issue | Required Action | Expected Impact |
|----------|-------|-----------------|-----------------|
| P2 | Rewrite movie example (S... metadata) | Align example with stability-plasticity axis | Improves reader comprehension |
| P2 | Add "zero-shot" clarification (Weakness 6) | Define unconventional usage in abstract | Prevents reviewer confusion |
| P2 | Add synthetic Pareto-front validation | 2-task synthetic problem with known Pareto front | Empirically validates convex-combination assumption |

### ASCII Diagram — Revision Strategy Roadmap

```text
[P0: Credibility fixes]
    ├── Rewrite Theorem 2 (tautology → coverage)
    ├── Add multi-seed stats + significance tests
    ├── Fix prior inconsistency (CelebA control)
    ├── Replace "first" claim with scoped wording
    └── Expand limitations section
    ↓
[P1: Evidence strengthening]
    ├── Verify Assumption 1 empirically
    ├── Add quantitative results table
    └── Compute efficiency crossover point
    ↓
[P2: Polish + extra validation]
    ├── Align movie example with stability-plasticity
    ├── Clarify "zero-shot" usage
    └── Add synthetic Pareto-front validation
    ↓
[Expected outcome: acceptance-quality manuscript]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|---------------------------------------|---------|--------------|-----------------|-------------------|
| E1 | Compare IBCL vs rehearsal (GEM, A-GEM, VCL) and prompt (L2P) baselines on CLuST | 4 benchmarks: CelebA (15 tasks), Split-CIFAR100 (10), TinyImageNet (10), 20NewsGroup (5). Domain-incremental, n_prefs=10. Pre-extracted ResNet-18 (images) or TF-IDF (text) features. Small BNN (64 hidden). | Avg per-task accuracy, Peak per-task accuracy, Backward transfer | IBCL has "top" accuracy across figs; "at most 45% improvement" over L2P on 20News | C3 (empirical support) | Single-seed; 10 prefs; no CIs; visual-only reporting |
| E2 | Training overhead comparison | Batch update counts per dataset (Table 1) | # batch updates at last task | IBCL constant w.r.t. n_prefs; absolute cost higher than L2P, lower than GEM | Efficiency claim | No crossover analysis; wall-clock time not reported |
| E3 | Ablation on distance threshold d | 20NewsGroup and Split-CIFAR100; d=0.002, 0.005, 0.008 | Buffer growth, performance | Larger d reduces memory but drops performance | Algorithm 1 design | Only 2 benchmarks; no theoretical bound linking d to approximation error |
| E4 | Ablation on significance level α | 20NewsGroup; α=0.01, 0.1, 0.25 | Pareto-front proximity, accuracy | Smaller α → wider HDR → higher chance to sample Pareto-optimal models | Theorem 2 usage | Only 2 tasks; sampling-based evaluation |
| E5 | Ablation on priors (variance and count) | 20NewsGroup and Split-CIFAR100; stds {0.2,0.25,0.3}, {2,2.5,3}, {20,25,30}; counts 3,5,8 | Avg/peak accuracy, backward transfer | Performance differences in early tasks converge later; 3 priors sufficient | Robustness of m=3 | CelebA uses different priors (0.2 scale) |
| E6 | Ablation on β weights | Equal vs randomized β's | Performance trends | Equal and randomized β's give similar trends | Equal-β simplification valid | Only 2 benchmarks |

### Research-Theme Gap Diagnosis

1. **New knowledge contribution is unclear (unresolved).** The paper's primary novelty claim (C1: "first to formulate CLuST") is unverifiable without external literature search (deferred due to Retrieval-Disabled Mode). Even if novel, the theoretical guarantee is weakened by the tautology in Theorem 2.

2. **Reproducibility is partially compromised (unresolved).** Single-seed runs, visual-only results for accuracy, and hidden hyperparameter tuning choices (different prior variances per benchmark) reduce reproducibility.

3. **Impact on practice is overstated (unresolved).** The paper claims applicability to "large-scale models" but only tests on a tiny BNN (64 hidden units). No evidence supports scalability.

### Proposed Research Experiments

**P0 Experiment: Multi-seed replication with confidence intervals**
- **Target Claim:** C3 (IBCL outperforms baselines)
- **Hypothesis:** IBCL's improvement is statistically significant
- **Minimal Design:** Run all 4 benchmarks with 3 random seeds, 50 preferences/task
- **Controls/Baselines:** Same as current (GEM, A-GEM, VCL, L2P)
- **Metrics:** Mean ± std of avg accuracy, peak accuracy, backward transfer; paired bootstrap p-value
- **Success Criterion:** ≥2 benchmarks show p < 0.05 improvement over best baseline
- **Estimated Cost/Time:** ~3× current compute (3 seeds × 1.7× more preferences)
- **Expected Paper-Quality Gain:** Transforms evidence from visual-trend to statistically rigorous

**P0 Experiment: Prior variance control on CelebA**
- **Target Claim:** C3 (consistent performance across benchmarks)
- **Hypothesis:** IBCL's CelebA results are not artifacts of narrower priors
- **Minimal Design:** Run CelebA with priors {2,2.5,3} (same as other benchmarks), keep other settings
- **Controls/Baselines:** Original CelebA configuration
- **Metrics:** Accuracy difference ≤ 2% or explain deviation
- **Success Criterion:** Performance difference < 2% or acceptable with explanation
- **Estimated Cost/Time:** ~1 CelebA run
- **Expected Paper-Quality Gain:** Removes confound in cross-benchmark comparison

**P1 Experiment: Synthetic Pareto-front validation**
- **Target Claim:** C2 (convex combination yields Pareto-optimal models)
- **Hypothesis:** Models obtained via convex combination lie on or near the true Pareto front
- **Minimal Design:** 2-task synthetic problem (e.g., sinusoid regression with known posteriors); enumerate true Pareto front via grid search
- **Controls/Baselines:** True Pareto front, single-task models, random convex combinations
- **Metrics:** Distance to true Pareto front (hypervolume indicator)
- **Success Criterion:** IBCL models within 5% of optimal hypervolume
- **Estimated Cost/Time:** 1-2 days
- **Expected Paper-Quality Gain:** Empirically validates core algorithmic assumption

**P2 Experiment: Dissimilar-task sensitivity test**
- **Target Claim:** Robustness to Assumption 1
- **Hypothesis:** IBCL degrades gracefully when tasks are dissimilar
- **Minimal Design:** Create a 5-task sequence with increasing dissimilarity (e.g., MNIST → FashionMNIST → CIFAR-10 → SVHN → random labels)
- **Controls/Baselines:** Standard BCL (VCL), rehearsal-based GEM
- **Metrics:** Accuracy retention, backward transfer
- **Success Criterion:** IBCL's forgetting is not worse than VCL's
- **Estimated Cost/Time:** 2-3 days
- **Expected Paper-Quality Gain:** Bounds the method's operating range realistically

### ASCII Diagram — Experiment Upgrade Plan

```text
[Current evidence: visual trends, single-seed, confounded priors]
    │
    ├── P0: Multi-seed (3×) + 50 prefs + CIs + significance test
    │         → statistically rigorous evidence
    │
    ├── P0: CelebA prior control
    │         → removes cross-benchmark confound
    │
    ├── P1: Synthetic Pareto-front validation
    │         → empirically verifies convex-combination assumption
    │
    └── P2: Dissimilar-task stress test
              → bounds method's robustness
    │
    [Target: acceptance-quality empirical section]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5/10**

**Rationale:** The paper introduces a creative connection between imprecise probability and continual learning, and the problem of zero-shot model generation for arbitrary trade-offs is well-motivated. However, the core theoretical guarantee (Theorem 2) is a definitional tautology rather than a substantive result, the evaluation lacks statistical rigor (single seed, no confidence intervals), key assumptions are unverified, and the main empirical claims are based on visual trends rather than quantitative tables. The approach has genuine potential, but the current evidence is insufficient to support the strength of the claims.

**Scoring dimensions:**
- **Research value & contribution (primary): 5/10** — Problem is worth studying, but the solution's theoretical foundation has a significant gap (tautological guarantee). Novelty cannot be fully assessed due to Retrieval-Disabled Mode.
- **Theoretical soundness: 4/10** — Theorem 2 is definitional; Assumption 1 is unverified; convex-combination Pareto-optimality is unproven for non-convex settings.
- **Empirical validity: 5/10** — Coverage of 4 benchmarks is good, but single-seed, no CIs, no significance tests, visual-only reporting.
- **Reproducibility: 6/10** — Algorithm description is clear; hyperparameters reported; missing multi-seed data and confidence intervals.
- **Writing & presentation: 6/10** — Generally clear structure; overclaiming in contributions and abstract; unconventional "zero-shot" usage may confuse.

**Post-Revision Target: [6.5, 7.5]/10**

**Rationale:** If the authors (a) reframe Theorem 2 honestly as a coverage property, (b) add multi-seed evaluation with confidence intervals, (c) fix the prior inconsistency, (d) add a quantitative results table, and (e) expand limitations, the paper would present a well-motivated algorithm with honest evidence. The upper bound of 7.5 reflects the inherent limitation that the theoretical guarantee is weaker than claimed, and novelty verification requires external literature review beyond the paper's scope.