Here is the final consolidated meta-review.

---

## Summary

This paper proposes Proto Successor Measure (PSM), a zero-shot RL method built on the insight that successor measures satisfying Bellman flow constraints form an affine set. A basis Φ and bias b for this affine set can be learned reward-free from environmental interaction, enabling zero-shot optimal policy inference for downstream rewards by solving a low-dimensional linear program. The theoretical contribution includes Theorem T2, which proves successor-measure bases span a strictly larger class of value functions than direct value-function bases of the same dimension. Empirical evaluations on gridworlds, FetchReach, and continuous control benchmarks show PSM achieving competitive or superior zero-shot performance compared to Forward-Backward (FB), Laplacian, and HILP baselines.

## Strengths

1. **Theorem T2 provides a provable expressivity advantage over value-function bases (Section 4, line 222):** The paper proves span{Φ^vf} ⊆ {span{Φ}r}, showing that any value function representable by a direct linear basis (as in Proto Value Functions) can also be represented via the successor measure basis with the same dimensionality, while the converse does not hold. This is a concrete theoretical advantage over a whole family of spectral methods.

2. **The discrete-codebook trick reduces a two-player game to a single-player optimization (Section 4.2, lines 249–261):** By parameterizing policies via a random seed z through π(a|s,z) = UniformSample(seed=z+hash(s)), the joint optimization of Φ, b, and w(z) can be performed in a single objective (Eq. 9), avoiding the bilevel or adversarial optimization required by prior methods like Forward-Backward.

3. **PSM achieves the highest average scores on 3 of 4 continuous-control benchmarks (Table 1):** PSM outperforms FB, Laplacian, and HILP on Walker (689.07 vs 594.67 for FB), Cheetah (607.61 vs 586.31), and Quadruped (618.74 vs 568.64), with especially large margins on tasks like Walker-Flip (640.75 vs 277.95 for HILP). All methods use the same representation dimension (d=128), discount factor, and inference protocol.

4. **PSM exhibits stable learning while FB shows performance degradation (FetchReach experiment, lines 342–366):** PSM reaches optimal performance quickly and maintains it, whereas FB's performance drops during training. The paper identifies the cause: FB uses Bellman optimality backups leading to overestimation bias, while PSM avoids this by not tying reward representation to optimal-policy representation.

5. **Explicit formal connection to successor features with transparency about expressivity trade-offs (Section 6, lines 283–302):** The paper proves that when the PSM basis is decomposed as φ(s,a,s⁺) = φ_ψ(s,a)^T φ(s⁺), it recovers standard successor features, and explicitly notes that this decomposition reduces representation capacity and that PSM does not require it.

## Weaknesses

### Fatal
None.

### Major

1. **Unaddressed gap between theory and practice in policy coverage (Section 4.2, lines 249–261):** The paper's central theoretical claim (Corollary T1) is that *any* successor measure can be represented as an affine combination of policy-independent basis functions. The practical algorithm learns Φ and b by optimizing over a *finite* set of policies sampled from a discrete codebook of seeds. While the mathematical claim that uniformly random seeds induce a uniform distribution over deterministic policies is correct, the paper provides no analysis of how many seeds are needed, no bound on the approximation error from finite-policy sampling, and no evidence that the learned basis generalizes to policies not seen during training. The paper conflates "provably uniform sampling" (a property of the sampling mechanism) with "provably covering all policies" (a property that would require infinite samples or a generalization guarantee). **Why this matters:** This is the single most important weakness. The theory promises universal coverage; the algorithm delivers finite-policy approximation. Without any quantification of this gap, it is unclear whether the practical method delivers on the theoretical promise. The paper should acknowledge this limitation explicitly and provide either theoretical bounds or empirical analysis.

### Minor

1. **Continuous control experiments adopt a factorization that undermines the claimed expressivity advantage (Section 5.3, lines 371–373; Section 6, lines 298–302):** The main continuous control experiments decompose φ(s,a,s⁺) as φ_ψ(s,a)^T φ(s⁺). The paper acknowledges this "reduces the representation capacity of the basis" (line 302) but then claims this is "not a limiting assumption" because features can be "arbitrarily non-linear" (line 373). A rank-1 factorization of a 3-argument function into a product of two 2-argument functions imposes a structural bottleneck regardless of nonlinearity. This means the paper's strongest empirical results do not evaluate the unrestricted method advertised in the theory. The paper does not compare the factored vs unfactored PSM even on a small problem where the unfactored version would be feasible.

2. **Gridworld evaluation is qualitative with unsubstantiated quantitative claims (Section 5.1, lines 318–341):** The gridworld results are presented as visualizations only. The paper claims "100% success rate" without specifying over how many goals, seeds, episodes, or trials. No standard errors, no quantitative comparison to baselines, no ablations.

3. **Several individual task comparisons in Table 1 have statistically ambiguous margins (Table 1):** While PSM achieves the highest average on 3 of 4 environments, multiple individual tasks have overlapping confidence intervals between PSM and the best baseline (e.g., Walker Stand: PSM 872.61±38.81 vs FB 902.63±38.94; Cheetah Run Backward: PSM 286.13±25.38 vs FB 307.07±14.91). On Pointmass, the average difference between PSM and Laplacian is minimal (514.09 vs 501.23) with overlapping error bars.

4. **Missing ablations and analysis (throughout Section 5):** The paper does not ablate the number of codebook seeds, does not analyze the learned basis functions, does not analyze constraint satisfaction during inference (how often does the non-negativity constraint bind? how does the Lagrangian dual optimization behave?), and does not compare the full non-factored PSM against the factored version even on small problems.

### Trivial
None.

## Nice-to-Haves
- A comparison of non-factored PSM vs factored PSM on gridworlds would directly measure the expressivity loss.
- An ablation varying the number of codebook seeds would help quantify the theory-practice gap.
- Analysis of constraint satisfaction (Φw+b≥0 violations) during inference would strengthen confidence in the method.

## Removed Points
- **"Discrete codebook claim is false":** Removed. The critic asserted the uniform-sampling claim is "false as stated." It is not: a uniform random seed z with independent offsets per state (z+hash(s)) does induce a uniform distribution over deterministic policies. The mathematical claim is correct; the practical limitation of finite samples is a separate issue, now covered in Major weakness 1.
- **"Does not demonstrate zero-shot for arbitrary reward functions":** Removed. No empirical paper can demonstrate "any" reward. The paper tests goal-conditioned, reaching, and diverse locomotion rewards — a reasonable range. This is scope creep.
- **"Missing proofs (appendix stripped):"** Removed per hard rules — the parser strips appendices from all papers.
- **"Baselines are limited":** Removed. The paper compares to FB, Laplacian, and HILP — the main zero-shot RL baselines. No specific missing baseline that would change conclusions is identified.
- **Strength: "provably samples from among all possible deterministic policies uniformly":** Removed from strengths. While mathematically correct, presenting this as a strength overstates what is practically delivered (only a finite set of policies are sampled).

## Novel Insights
None beyond the paper's own contributions. The reviews surface the central tension (theory promises universal coverage, practice delivers finite-policy approximation) but do not identify fundamentally new implications beyond what the authors already articulate.

## Suggestions
1. Provide a theoretical or empirical analysis of how many codebook seeds are needed and how the learned basis generalizes to policies not seen during training.
2. Add a gridworld experiment comparing non-factored PSM against factored PSM to measure the expressivity loss from the factorization.
3. Substantiate the "100% success rate" claim with explicit numbers (how many goals, trials, seeds) and standard errors.
4. Add an ablation on codebook size to show how performance varies with the number of seeds.
5. Discuss the finite-policy coverage gap explicitly in the limitations section, rather than only mentioning representation dimension and dataset coverage.

## Score and Decision

The paper's core insight (successor measures form an affine set) is genuinely novel and well-motivated. Theorem T2 provides a clear theoretical advantage over spectral methods. The empirical results are competitive and the discrete-codebook trick is clever. However, the gap between the theoretical claim of universal policy coverage and the practical finite-codebook approximation is significant and unaddressed. The strongest empirical results use a factored representation that the paper acknowledges reduces expressivity, yet the paper does not compare the factored and unfactored versions even where feasible. The evaluation would benefit from more rigorous quantification, ablations, and substantiation of claimed results. The paper has clear merit but does not fully deliver on its ambitious claims in its current form.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>