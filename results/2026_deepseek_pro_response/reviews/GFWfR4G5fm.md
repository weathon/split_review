Now let me finalize the review with the calibrated score. Let me synthesize all anchor comparisons.

**Round 1 anchors:**
- JzFLBOFMZ2 (3.20, Reject) — LLM-based CSL, weak baselines, limited theory. Our paper is clearly stronger.
- ZXs3pkmrRG / TICL (5.50, Reject) — Very similar TTT-for-SCL paper, but with poorer execution, unclear presentation, niche applicability. Our paper is clearly stronger.
- x3F8oPxKV2 / Zero-Shot Causal Models (6.25, Reject) — Different paradigm, limited evaluation, unrealistic assumptions. Our paper has better empirical validation.
- xByvdb3DCm (8.00, Accept) — Strong theoretical contribution, unanimous 8s. Our paper is weaker, lacking theoretical depth.

**Round 2 anchors:**
- eeJz7eDWKO / Meta-Learning Bayesian CD (6.00, Accept) — All 6s. Clear method, limited by no-confounder assumption. Comparable quality to our paper.
- 8muemqlnG3 / DrBO (6.50, Accept) — Novel BO for CD, clean method, strong experiments. Slightly stronger than our paper due to fewer specification gaps.
- wmV4cIbgl6 / CausalRivers (7.33, Accept) — Major benchmarking contribution, not directly comparable.
- pOoKI3ouv1 (5.75, Accept) — Theoretical result, high variance scores. Different category.

**Bracket:** 5.50 – 7.33. Narrowed to **6.00 – 6.50**.

**Final assessment:** The paper falls between Meta-Learning Bayesian CD (6.00) and DrBO (6.50). Like the 6.00 anchor, it has a clear contribution with some limitations. The acceptance criterion specification error and several underspecification gaps pull it below DrBO's 6.50, but the novel TTT-SCL framework, strong motivation with three-diagnosis experiments, and solid real-world empirical results push it above 5.50. Score: **6.0**.

---

## Summary
This paper identifies three failure modes of static supervised causal learning (SCL) — fragility to distribution shifts, failure in compositional generalization, and a synthetic-to-real performance gap — and proposes TTT-SCL, a test-time training framework that dynamically generates training data aligned to each test instance. The TACTIC instantiation uses a log-likelihood-based score (AD) with an L0 sparsity penalty to guide stochastic graph search, then trains an SCL model on forward-sampled data from the refined graphs. Experiments show TACTIC outperforming baselines on several OOD settings including real-world (Sachs) and pseudo-real (Syntren) data.

## Strengths
- **Diagnosis of SCL limitations with a well-designed compositional generalization test (Section 3, Figure 2).** The "component-mixed" condition — where all individual components are seen during training but specific combinations are withheld — cleanly isolates whether SCL models memorize configurations or learn modularly. The AUROC drops (e.g., RFF_G_97.8 from 100 i.i.d. to 91 component-mixed) are a genuinely sharper finding than generic OOD claims.
- **Strong empirical results on real-world and shifted data (Table 2).** TACTIC achieves 78.9 AUROC on Sachs vs. 62.3 for the pre-trained AVICI baseline and 67.1 for PC, and 80.1 on Syntren vs. 65.4 for AVICI. On synthetic domains where AVICI was not pre-trained (Linear_U, Chebyshev_G), TACTIC similarly leads (86.3, 83.0). These margins directly support the central claim that test-time aligned training bridges the synthetic-to-real gap.
- **Informative stage-wise analysis decomposing gains into search and learning improvement (Table 4).** The jump from the highest-scoring graph found during search to the final SCL output (e.g., 66.6 → 78.9 on Sachs) demonstrates that training an SCL model on the generated data extracts signal beyond what the search alone captures.
- **Clean sparsity ablation (Table 3).** Removing the sparsity term causes consistent degradation (e.g., 83.0 → 69.7 on Chebyshev_G, 78.9 → 63.5 on Sachs), confirming that AD alone is insufficient and that the causal minimality constraint is essential.
- **Architecturally agnostic framework.** The paper explicitly notes compatibility with any identifiability assumption (LiNGAM, ANM, PNL) and reports consistent failure patterns with a second SCL backbone (SiCL), suggesting the approach could generalize beyond the tested AVICI backbone.

## Weaknesses

### Fatal
None.

### Major
- **The acceptance criterion in stochastic graph refinement is mathematically ill-specified when scores are negative (Section 4.2, Figure 3).** The transition probability is given as α = min(1, score(G_{k+1}) / score(G_k)). Since AD is a log-likelihood (typically negative) and the sparsity penalty subtracts further, scores will be negative. With negative scores, the ratio exceeds 1 when the new score is worse (more negative), meaning worse proposals are always accepted — the opposite of correct Metropolis behavior. If scores have mixed signs, the ratio can become negative, producing a meaningless probability. The paper provides no discussion of normalization or correction. This could be a documentation error (the text says "accepted with probability proportional to its score," which differs from the ratio formula), but as presented it is a specification gap that affects reproducibility.

### Minor
- **The AD metric is framed with overstated novelty.** The paper presents AD as a proposed metric for "distributional alignment," but Eq. (3) is a standard per-variable conditional log-likelihood — essentially a goodness-of-fit score for DAG structures. The novelty lies in how AD is used (to guide test-time training data generation for a downstream SCL model), not in what AD is. The current framing in Section 4.1 risks misleading readers familiar with score-based causal discovery.
- **The connection between compositional generalization failure (Issue 2) and the TTT-SCL remedy is underexplained.** The paper demonstrates that SCL models fail on novel combinations of seen components, but never clarifies the mechanism by which test-time training specifically addresses compositionality. The implicit argument — that generating per-instance aligned data bypasses the need for compositional generalization — should be made explicit.
- **Several implementation details are unspecified.** The regression method used for SIM (linear regression? neural network?) is not stated. The value of λ is mentioned as a hyperparameter but never reported. The number of stochastic refinement iterations is not given. These gaps limit reproducibility.
- **The forward-sampling noise default of N(0,1) creates a mismatch with non-Gaussian test noise (Section 4.2).** For settings like Linear_U where the true noise is Uniform, the generated training data has a systematically different noise distribution from the test data. The paper does not discuss or evaluate the impact of this mismatch.
- **Only AUROC is reported in the main text; structural metrics like SHD are absent.** For causal discovery, especially on Sachs where a consensus graph exists, structural Hamming distance would be more informative than edge-wise AUROC, which treats edges as independent binary classifications and ignores DAG constraints.
- **No statistical significance tests are reported.** Several comparisons show overlapping standard deviations (e.g., TACTIC(random) 79.6±6.7 vs. TACTIC(Notears) 83.0±8.7 on Chebyshev_G), and without formal tests it is unclear which differences are reliable.
- **The unique value of the SCL training step over direct graph ensembling is not isolated (Table 4).** The stage-wise analysis compares the final SCL model (trained on K=200 graphs) against the single highest-scoring graph, but the SCL model inherently benefits from ensembling across those 200 graphs. An ablation that directly ensembles the top-K graphs (e.g., edge-wise majority vote) without the SCL training phase would strengthen the claim of "learning improvement." The gains are large enough (e.g., +12.3 on Sachs) that this is unlikely to overturn the conclusion, but the control is worth adding.

### Trivial
- The paper sets the noise distribution to N(0,1) by default for forward-sampling but does not justify this choice or discuss alternatives.

## Nice-to-Haves
- An ablation replacing the SCL model with direct ensembling (e.g., edge-wise majority vote or averaging over the top-K graphs) would strengthen the claim that the SCL training phase provides unique value beyond ensembling.
- A sensitivity analysis for λ (the sparsity coefficient) and K (number of training graphs) would help readers understand robustness to hyperparameter choices.
- Reporting SHD against the Sachs consensus graph would provide a more standard causal discovery evaluation.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"TACTIC(Notears) uses NOTEARS as its seed, making the comparison against NOTEARS partially circular"** — REMOVED. TACTIC(random) exists and performs competitively without NOTEARS initialization (e.g., 82.3 on Linear_U vs. NOTEARS 82.0), so the circularity concern is addressed by the paper's own experiments.
- **"TACTIC underperforms AVICI on the one in-distribution setting (RFF_G: 91.8 vs. 97.8)"** — REMOVED. The paper explicitly acknowledges that AVICI was trained on RFF_G and that TACTIC's performance is slightly lower but still strong. This is expected behavior for a method targeting OOD settings and is not a weakness.
- **"The forward-sampling step adds noise that regularizes predictions"** — REMOVED. This is speculative from the reviewer and not a claim made or implied by the paper.
- **"TACTIC is essentially score-based search with post-hoc ensembling"** — REMOVED as a fatal claim. The stage-wise analysis shows substantial gains from the SCL phase (e.g., 66.6 → 78.9 on Sachs), and while an ensembling ablation would be informative, the claim that TACTIC *reduces to* score-based search with ensembling is not supported by the evidence and ignores the two-stage architecture. Demoted to Minor.

## Novel Insights
None beyond the paper's own contributions. The reviews independently confirm the value of the component-mixed experimental design for diagnosing compositional generalization failure and the stage-wise decomposition of TACTIC's gains, but these are insights already presented in the paper.

## Suggestions
- Fix the acceptance criterion: either use α = min(1, exp(score(G_{k+1}) − score(G_k))) or shift scores to be strictly positive, and report the actual formula used in experiments.
- Add an ensembling baseline (K-graph majority vote or edge averaging) to Table 4 to isolate the SCL model's unique contribution.
- Include at least one structural metric (SHD) in the main results, especially for Sachs where a consensus graph is available.
- Report the λ value, regression method, and number of refinement iterations used.
- Clarify how TTT-SCL specifically addresses compositional generalization (Issue 2), or acknowledge that this issue motivates the paradigm shift rather than being directly solved by the current method.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>