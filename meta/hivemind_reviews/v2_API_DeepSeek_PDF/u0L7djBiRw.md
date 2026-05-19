## Summary
This paper proposes a Rademacher-like random embedding (RLE) that achieves O(n + k²) time and space complexity for embedding an n-dimensional vector into k dimensions—reducing to linear O(n) when k = O(√n). The key idea is to avoid explicitly constructing the k×n embedding matrix by using a smaller ζ×n Rademacher base matrix (ζ ≤ 3) and a set of auxiliary random arrays to implicitly generate the embedding via partial sums and random accumulation. Theoretical analysis proves that RLE preserves key Rademacher properties: entries are ±1/√k with probability 0.5, they are pairwise independent, the expected squared norm is preserved, and the same (ϵ,δ,d)-oblivious subspace embedding guarantees hold as for standard Rademacher embeddings. Numerical experiments on single-pass RSVD (7 test cases) show 1.5–1.7× average speed-up over Gaussian and sparse sign embeddings with comparable accuracy, and on randomized Arnoldi/GMRES (5 test cases ranging from 1.2E6 to 2.0E7 dimensions) RLE achieves 1.3× average speed-up over P-SRHT and sparse sign variants.

The paper addresses a genuine need in randomized numerical linear algebra: fast, robust, dense embeddings with linear-time cost and small practical time constants. The proposed construction is novel and the complexity improvement over standard dense embeddings (O(nk) → O(n + k²)) is significant when k is not too large relative to n. However, the paper would benefit from stronger empirical validation (multi-trial statistics, direct embedding quality tests), clearer discussion of the effective randomness reduction, and more precise claim bounding.

## Strengths
**S1. Novel complexity improvement.** The key strength of this paper is the proposed RLE construction, which reduces the complexity of dense Rademacher-style embedding from O(nk) to O(n + k²). This is a meaningful improvement for the regime k = O(√n), which covers many practical settings in randomized linear algebra. The implicit matrix construction using a small ζ×n base matrix and auxiliary random arrays is conceptually clever.

**S2. Solid theoretical foundation.** The paper proves several desirable properties: entries are ±1/√k, pairwise independence (though with reduced randomness relative to full Rademacher), norm preservation in expectation, and the same (ϵ,δ,d)-oblivious subspace embedding guarantees as standard Rademacher embeddings. The subspace embedding proof (Theorem 6) is correctly adapted from Achlioptas (2003) and Balabanov & Nouy (2019), using the established framework.

**S3. Practical speed-ups demonstrated.** The numerical experiments show consistent speed-ups across diverse test cases: 1.5–1.7× average speed-up on single-pass RSVD (against Gaussian and sparse sign embeddings) and 1.3× on randomized GMRES (against P-SRHT and sparse sign). The speed-ups are demonstrated on both synthetic and real-world matrices, including very large cases (FERET with 1E5×3.9E5 and thupg5 with 2.0E7 dimensions).

**S4. Two distinct application domains.** The paper validates RLE on two important RandNLA tasks—streaming low-rank approximation (single-pass RSVD) and Krylov subspace methods (randomized Arnoldi/GMRES)—which shows the method's versatility beyond a single application.

**S5. Ablation study on parameters.** The appendix includes an ablation study on the RLE parameters ξ, ζ, ω, showing that accuracy is robust to parameter choice while runtime varies predictably. This helps practitioners select appropriate parameters.

## Weaknesses
**W1. No statistical variance reported (major).** All experimental results are single-trial with no standard deviations, confidence intervals, or significance tests. Given the stochastic nature of random embeddings, this omission makes it impossible to assess whether observed accuracy differences are statistically meaningful. For example, on the "noise" case, Gaussian embedding gives errs=31.3 while RLE gives 6.92—a large difference that may suggest implementation issues rather than inherent method behavior. (See annotation on Table 1.)

**W2. Effective randomness concern not addressed (major).** With the default setting ζ=1, all k rows of the implicit Θ are derived from a single base Rademacher row. The paper acknowledges that "mutual independence of whole matrix entries does not hold" but does not analyze the practical impact of this reduced randomness. The effective number of independent random bits is much smaller than in a standard Rademacher matrix, which could affect embedding quality in edge cases. (See annotation on §3.1-3.2.)

**W3. Missing direct embedding quality tests.** The paper validates RLE only through downstream task accuracy (RSVD error, GMRES convergence). There are no direct measurements of embedding quality—such as norm preservation error (|||Θx||² - ||x||²| / ||x||²), subspace embedding distortion, or spectral norm of ||Θ^T Θ - I||. Direct tests would provide stronger evidence that RLE truly behaves like a Rademacher embedding.

**W4. Ablation study limited to one test case.** The parameter ablation (Appendix A.4) uses only "rajat31" (n=4.7E6, k=200). Different n/k ratios would produce different runtime trade-offs between the O(ξζn) and O(ωk²) terms, so the conclusions may not generalize.

**W5. Speed-up claims conflate randomization benefit with RLE benefit.** The "1.4x speed-up over standard Arnoldi process" primarily reflects the benefit of randomization (any fast embedding would show similar speed-up), not a unique advantage of RLE. The more informative comparisons are against P-SRHT and sparse sign, where RLE shows 1.3x and 1.3x respectively. The paper should separate these comparisons more clearly.

**W6. Argument strength for OSE guarantee (minor).** Theorem 6 proves RLE achieves the same subspace embedding dimension requirement as Rademacher embedding, but the proof relies entirely on adapting existing proofs from Achlioptas (2003) and Balabanov & Nouy (2019). While correct, the paper does not provide a self-contained derivation that accounts for RLE's specific dependence structure (pairwise independence without full mutual independence). A brief explicit verification that RLE's particular dependence structure satisfies the key lemmas would strengthen the theoretical contribution.

**W7. Writing quality (minor).** Several typos and grammatical issues: "Arnodli" for "Arnoldi" (Abstract), "entrices" for "entries" (§2.1), "dense embedding" should be "dense embeddings" (§1), and missing comma before "Musco" citation. The notation "k2" in the extracted text should be "k²" with proper superscript.

## Key Issues
### Issue 1 (Major): Missing statistical validation of experimental results
**Location:** Page 9 - Table 1 and Section 4.1  
**Evidence:** All results (errs, errf, Ttot) are single-trial with no standard deviation. The "noise" case shows Gaussian embedding with errs=31.3 vs RLE with 6.92—an unexplained 4.5× difference.  
**Risk:** Without multi-seed trials, readers cannot assess whether the observed accuracy differences are statistically significant or due to random fluctuation. This is particularly problematic for the RSVD results where error values vary by orders of magnitude across methods.  
**Repair:** Report mean ± std over at least 3 independent trials for a representative subset of test cases. Add a brief discussion of the anomalously large Gaussian embedding error on "noise."

### Issue 2 (Major): Effective randomness not quantified
**Location:** Page 5-6 - Sections 3.1-3.2 (RLE construction)  
**Evidence:** Default parameters (ξ=2, ζ=1, ω=2) mean all k rows of Θ are derived from ζ=1 base Rademacher row. The paper acknowledges lack of full mutual matrix entry independence but does not quantify how this reduced randomness affects embedding quality.  
**Risk:** For ζ=1, the implicit Θ matrix's rows are all generated from the same base row of P, only permuted and re-signed. This could produce subtle correlations that the pairwise independence guarantee (Theorem 3) does not capture, potentially affecting applications requiring higher independence.  
**Repair:** Add a synthetic experiment measuring ||Θ^T Θ - I|| (deviation from ideal) for various ζ values, comparing against standard Rademacher. Discuss scenarios where ζ needs to be larger.

### Issue 3 (Major): No direct embedding quality validation
**Location:** Page 8-10 - Section 4 (Numerical Experiments)  
**Evidence:** RLE is only validated via downstream task accuracy (RSVD error, GMRES convergence). No direct measurement of norm preservation or subspace embedding distortion is reported.  
**Risk:** Downstream accuracy can be affected by many factors beyond embedding quality (solver convergence properties, preconditioning, rank oversampling). Direct embedding quality tests are the standard way to validate a new embedding method.  
**Repair:** Add a direct embedding quality experiment: for random vectors x ∼ N(0, I), measure relative norm preservation error |||Θx||² - ||x||²| / ||x||², and compare against Gaussian, Rademacher, and sparse sign baselines.

## Actionable Suggestions
### Suggestion 1 (Must): Add multi-trial statistical reporting
**What:** Report mean ± standard deviation over at least 3 independent trials for all experimental results (Table 1 and Table 2).  
**Where:** Replace single-value entries in Table 1 (Ttot, errs, errf) and Table 2 (t_RLE, etc.) with mean ± std format.  
**Why:** Essential for scientific validity of stochastic algorithm comparisons.  
**Mentor guidance example for Table 1 revision:**
> "noise: Ttot = 0.0863±0.0021, errs = 31.3±5.2, errf = 6.53±0.89" instead of single values.

### Suggestion 2 (Must): Add direct embedding quality experiment
**What:** Create a synthetic experiment measuring relative norm preservation error and subspace embedding distortion.  
**Where:** New subsection in Section 4 (before 4.1), or a new Appendix section.  
**Design:** Generate random vectors x_i ∼ N(0, I) for n ∈ {10³, 10⁴, 10⁵} and various k values. For each embedding method (RLE, Gaussian, Rademacher, sparse sign), compute:  
  - Relative norm error: |||Θx||² - ||x||²| / ||x||²  
  - Spectral norm: ||Θ^T Θ - I||  
Report mean ± std over 100 random trials.  
**Why:** Directly validates the core claim that RLE behaves like Rademacher embedding.

### Suggestion 3 (Must): Quantify effective randomness
**What:** Add analysis showing how the reduced randomness (ζ small) affects embedding quality.  
**Where:** New paragraph at end of §3.3 or new appendix section.  
**Content:** Compare RLE with ζ = 1, 2, 3 against full Rademacher on norm preservation and subspace embedding distortion. Show that as ζ increases, RLE approaches Rademacher behavior. Provide guidance on selecting ζ for different applications.  
**Mentor Revised Version (new paragraph for §3.3):**
> "A practical consideration is the choice of ζ (rows of the base matrix P). With ζ = 1, all k rows of Θ are generated from a single random sequence, reducing the effective randomness compared to a full Rademacher matrix. While Theorem 3 guarantees pairwise independence, higher-order dependence may affect performance in some settings. Our experiments (Appendix A.5) show that ζ = 1–3 achieves similar accuracy to full Rademacher on the tested benchmarks, but ζ should be increased for applications requiring higher-quality randomness."

### Suggestion 4 (Must): Separate randomization benefit from RLE benefit
**What:** Revise the GMRES speed-up discussion to clearly separate the benefit of using any randomized embedding from the incremental benefit of RLE.  
**Where:** Section 4.2, paragraph starting "From the experimental results..."  
**Mentor Revised Version (revised paragraph):**
> "Compared with standard (deterministic) GMRES, all randomized variants show speed-ups due to replacing expensive Gram-Schmidt orthogonalization with sketched OLS. Among the randomized variants, RLE achieves 1.3× average speed-up over both P-SRHT and sparse sign embeddings, demonstrating its practical efficiency advantage."

### Suggestion 5 (Nice-to-have): Fix typos and improve notation
- Fix "Arnodli" → "Arnoldi" in Abstract  
- Fix "entrices" → "entries" in §2.1  
- Fix "dense embedding" → "dense embeddings" in §1  
- Fix missing comma before "Musco" citation  
- Ensure "k²" appears with proper superscript throughout  
- Improve the SRHT notation √(n/k) D H S with clear explanation of each matrix

### Suggestion 6 (Nice-to-have): Broaden ablation study
**What:** Extend the ablation study (Appendix A.4) to include test cases with different n/k ratios.  
**Suggested cases:**  
  - n = 10⁴, k = 50 (n/k = 200)  
  - n = 10⁶, k = 100 (n/k = 10000)  
  - n = 10⁸, k = 1000 (n/k = 100000)  
**Why:** The runtime complexity has two regimes (O(ξζn) vs O(ωk²)), so the optimal parameter setting may depend on the n/k ratio.

## Storyline Options + Writing Outlines
### Abstract Outline (5-sentence plan)
- **S1 (Problem):** Random embeddings (sketches) are essential for large-scale numerical linear algebra, but dense embeddings (Gaussian, Rademacher) cost O(nk) and alternatives like sparse sign embeddings suffer from irregular memory access.
- **S2 (Gap):** No existing embedding achieves both linear O(n) time and dense-matrix robustness with a small practical time constant.
- **S3 (Solution):** We propose Rademacher-like embedding (RLE), which uses a small ζ×n base Rademacher matrix and random accumulation tensors to implicitly generate a k×n embedding in O(n + k²) time.
- **S4 (Theory):** Theoretical analysis proves pairwise independence, norm preservation in expectation, and (ϵ,δ,d)-oblivious subspace embedding guarantees matching standard Rademacher embeddings.
- **S5 (Results):** On single-pass RSVD, RLE achieves 1.5–1.7× average speed-up over Gaussian and sparse sign embeddings with comparable accuracy; on randomized GMRES, it achieves 1.3× average speed-up over P-SRHT.

### Introduction Outline (6 paragraphs)

**P1 — Big Picture (revised):** Define random embedding (sketching) and its role as a core primitive in randomized numerical linear algebra (RandNLA). State that efficient embeddings are critical for RSVD, randomized least-squares, and Krylov methods. Cite Woodruff (2014), Martinsson & Tropp (2020).

**P2 — The Efficiency Challenge:** Explain that dense embeddings (Gaussian, Rademacher) are robust but cost O(nk). The sketching step in single-pass RSVD dominates runtime. Slow embeddings in randomized Arnoldi can negate the benefits of randomization. Cite Tropp et al. (2019), Balabanov & Grigori (2022).

**P3 — Existing Fast Embeddings and Their Limitations:** Survey P-SRHT (O(n log n)), sparse sign embedding (O(n) but requires sparse data structures and has non-negligible time constant), and Count Sketch (can fail catastrophically). State the open challenge: achieving O(n) time with dense-matrix robustness and small constant. Cite Martinsson & Tropp (2020), Tropp et al. (2019), Li et al. (2006).

**P4 — Proposed Solution (RLE):** Introduce RLE: a Rademacher-like embedding using a smaller base matrix and random accumulation to achieve O(n + k²) complexity while preserving Rademacher properties. Highlight that RLE is dense (no sparse data structures needed) and runs in linear time when k = O(√n).

**P5 — Theoretical Contributions:** RLE entries are ±1/√k with probability 0.5, pairwise independent, preserve norms in expectation, and achieve the same OSE dimension requirements as Rademacher embeddings.

**P6 — Empirical Validation and Outline:** Preview applications (single-pass RSVD, randomized Arnoldi/GMRES) and key results (1.5–1.7× and 1.3× speed-ups). End with paper roadmap.

### Alternative Storyline Candidate
**Title: "RLE: A Dense Rademacher-like Embedding with Linear Time and Robust Accuracy"**
- This shifts the emphasis from "with Linear Complexity" (current) to "RLE" as a named method with clear identity.
- Problem → Existing embeddings → Cost bottleneck → Our solution (RLE) → Theory → Experiments → Conclusion
- The advantage of this structure is that RLE is introduced as an explicit named entity earlier, helping readers anchor to the method.

### Alignment Checks
- **(a) Problem alignment:** Current intro states the problem (O(nk) cost, P-SRHT/sparse sign limitations) and RLE solves it (O(n + k²)). ✓  
- **(b) Variable alignment:** The core concepts (n, k, P base matrix, ζ, ξ, ω) in the intro appear as key method variables. ✓  
- **(c) Contribution-evidence alignment:** Intro claims (speed, accuracy) are directly tested in experiments. However, the intro's "robust" claim (used in title and abstract) is not explicitly tested via robustness/stress experiments—only downstream accuracy is reported. Suggest revising to "fast and accurate."

## Priority Revision Plan
### P0 (Must, before resubmission)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P0.1 | No statistical variance (W1) | Add 3-run mean±std for all Table 1 & 2 results | High: establishes scientific validity | Medium (re-run experiments) |
| P0.2 | No direct embedding quality test (W3, Issue 3) | Add synthetic norm-preservation and subspace distortion test | High: directly validates core claim | Low (random vectors + simple computations) |
| P0.3 | Missing effective randomness analysis (W2, Issue 2) | Add comparison of ζ=1,2,3 against full Rademacher; provide parameter guidance | High: addresses core methodological concern | Low (extend existing ablation) |
| P0.4 | Speed-up claim clarification (W5) | Revise §4.2 to separate randomization vs RLE benefit | Medium: improves scientific accuracy | Minimal (text revision only) |

### P1 (Important, should do)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P1.1 | Limited ablation scope (W4) | Extend ablation to 2-3 additional test cases with different n/k ratios | Medium: strengthens generality | Low-Medium (re-run with different matrices) |
| P1.2 | Missing limitation discussion | Add explicit limitations paragraph near the end of Conclusion | Medium: improves completeness | Minimal (text revision only) |
| P1.3 | Theorem 3 proof verification | Add formal covariance calculation showing E[Θ_{i,j}Θ_{l,r}] = 0 for (i,j)≠(l,r) | Medium: strengthens theoretical rigor | Low (short appendix derivation) |

### P2 (Nice-to-have, polish)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P2.1 | Typos (W7) | Fix "Arnodli", "entrices", "dense embedding", citation format | Low: improves professionalism | Minimal |
| P2.2 | Abstract precision | Clarify speed-up averaging method (weighted vs unweighted) | Low: improves precision | Minimal |
| P2.3 | Notation and equation formatting | Ensure "k²" has proper superscript everywhere | Low: cosmetic | Minimal |

### Revision Order
1. Fix typos and claim wording (P2.1, P2.2) — immediate, no experiments needed.
2. Add direct embedding quality test (P0.2) — one day of computation.
3. Add effective randomness analysis (P0.3) — extends existing code, one day.
4. Re-run experiments with 3 seeds for statistical reporting (P0.1) — most time-consuming but essential.
5. Revise GMRES discussion (P0.4) and add limitations (P1.2) — half day.
6. Add covariance verification derivation (P1.3) — half day.
7. Extend ablation study (P1.1) — one additional day if needed.
8. Remaining notation/formatting polish (P2.3) — final pass.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Limitation |
|--------|-----------|-------|---------|-------------|----------------|-----------|
| RSVD (Table 1) | Evaluate RLE vs Gaussian vs sparse sign on single-pass RSVD | 8 test matrices (synthetic, MNIST, FERET, Weather); k=10, r=11, s=23 | Ttot (s), errs, errf | RLE 1.5× (vs Gaussian) and 1.7× (vs sparse sign) avg speed-up | C3: practical efficiency | Single trial, no variance; FERET missing accuracy; unusual large Gaussian error on "noise" unexplained |
| GMRES (Table 2, Fig 2-4) | Evaluate RLE vs standard, P-SRHT, sparse sign in randomized Arnoldi/GMRES | 5 sparse matrices (rajat31, memchip, circuit5M, ibmpg4t, thupg5); k=200, ILU(3) | Runtime (s), residual convergence | RLE 1.3× avg vs P-SRHT and sparse sign, 1.6× vs standard GMRES | C3: practical efficiency | Single trial; speed-up vs standard GMRES primarily from randomization, not RLE-specific |
| Ablation (Fig 5, Appendix A.4) | Test sensitivity to ξ, ζ, ω | rajat31 only, randomized GMRES | Runtime and residual convergence | Accuracy robust to parameters; runtime varies with ξ,ζ | C2: parameter robustness | Only one test case; indirect accuracy metric (downstream GMRES) |

### Research-Theme Gap Diagnosis

1. **New knowledge (partially supported):** The RLE construction is genuinely new and the O(n + k²) complexity is a clear improvement over O(nk). However, the paper does not provide direct evidence that RLE's embedding quality is equivalent to standard Rademacher—it only tests downstream applications.

2. **Reproducibility (partially supported):** Algorithm 3 is clearly specified, and the parameter choices are documented. However, single-trial results without variance make it impossible to reproduce exact numbers.

3. **Impact on practice (moderately supported):** The speed-ups of 1.3–1.7× are practically meaningful, but the paper does not discuss deployment scenarios, memory requirements in detail, or when RLE might fail compared to alternatives.

### Proposed Research Experiments (P0/P1/P2)

| Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Est. Cost | Quality Gain |
|-------------|-----------|---------------|---------|---------|------------------|-----------|-------------|
| P0: RLE preserves norm like Rademacher | |||Θx||² - ||x||²| / ||x||² should match Rademacher within statistical tolerance | Generate 10⁴ random vectors x ∈ R^n for n ∈ {10³,10⁴,10⁵}, k ∈ {10,50,200}. Apply RLE, Rademacher, Gaussian, sparse sign. | Full Rademacher matrix | Relative norm error mean±std over 100 trials | RLE error within 1.1× of Rademacher error | ~2 hours | High — directly validates core claim |
| P0: Multi-seed stability of RSVD results | RLE accuracy variance is comparable to Rademacher | Repeat RSVD Table 1 experiments with 5 independent seeds for 3 representative cases (noise, inv, Weather) | Gaussian and sparse sign with same seeds | errs, errf mean±std | RLE variance not significantly larger than competitors (F-test) | ~1 day | High — essential for validity |
| P1: Subspace embedding distortion | ||Θ^T Θ - I|| spectral norm matches Rademacher bound | For d=20 subspace, measure ||U^T Θ^T Θ U - I|| where U is orthonormal basis | Full Rademacher with same dimensions | Spectral norm difference | RLE distortion ≤ 1.2× Rademacher distortion | ~1 day | Medium — strengthens theoretical claim |
| P1: Parameter sensitivity across n/k ratios | Optimal ξ,ζ,ω depend on n/k | Repeat Fig 5 ablation on 3 additional cases (MNIST-like, circuit5M-like, synthetic) | Fixed downstream solver | Runtime and residual convergence | Same qualitative pattern observed | ~2 days | Medium — generalizes ablation |
| P2: Memory footprint comparison | RLE O(k²) memory is practical | Measure peak memory for RLE, Gaussian, sparse sign, P-SRHT | Same problem sizes as Table 1 | Peak memory (MB) | RLE memory ≤ 2× Gaussian memory | ~1 hour | Low — useful documentation |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.0 / 10**

*Rationale:* The paper proposes a genuinely novel construction (RLE) that addresses a real computational bottleneck in randomized numerical linear algebra. The O(n + k²) complexity improvement over standard dense embeddings (O(nk)) is theoretically sound and the empirical speed-ups (1.3–1.7×) are practically meaningful. The theoretical analysis is largely correct and covers the essential guarantees (norm preservation, subspace embedding). However, the experimental validation is significantly weakened by the absence of statistical variance reporting, single-trial results, and the lack of direct embedding quality measurements. The effective randomness concern (ζ=1 case) is acknowledged but not analyzed. These gaps reduce confidence in the claims until addressed. The novelty is promising but some key evidence is missing.

*Score breakdown:*
- Research value: 7/10 (genuine need, practical speed-ups, but limited to specific regime k = O(√n))
- Novelty: 7/10 (construction appears new within RandNLA, but novelty verification deferred due to Retrieval-Disabled Mode)
- Theoretical soundness: 7/10 (proofs are correct but rely heavily on prior work; small proof notation issue)
- Empirical rigor: 4/10 (no variance, no direct embedding quality test, limited ablation scope)
- Reproducibility: 6/10 (algorithm clear, but single-trial results with no variance hinder exact reproduction)
- Presentation: 6/10 (generally clear, several typos, GMRES discussion conflates randomization vs RLE benefit)

**Post-Revision Target: [7.0, 7.5] / 10**

*Expected if P0 items are fully addressed:* Adding multi-seed statistical reporting (P0.1), direct embedding quality validation (P0.2), effective randomness quantification (P0.3), and claim precision improvements (P0.4) would substantially strengthen the evidence base and raise the score to 7.0–7.5. Beyond this range, extending the ablation study (P1.1) and adding the covariance derivation (P1.3) could further solidify the paper, but the core novelty and contribution are already well established. The upper bound 7.5 reflects the inherent limitation that the O(n + k²) → O(n) claim is conditional on k = O(√n), which restricts the method's applicable regime.