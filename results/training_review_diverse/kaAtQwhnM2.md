Now I have all the information I need. Let me compile the final consolidated review.

## Summary

This paper extends Energy Discrepancy (ED) — previously defined for continuous spaces with Gaussian perturbations — to discrete binary spaces. It proposes three types of discrete perturbations (Bernoulli noise, deterministic transformations, neighbourhood-based), develops gradient-informed importance-sampling proposals, provides theoretical consistency guarantees, and demonstrates the approach on Ising models, density estimation, graph generation, and binary image modeling. The core claim is that ED enables training discrete EBMs without MCMC while offering theoretical guarantees.

## Strengths

- **Novel framework for discrete perturbations enabling ED in binary spaces.** The paper introduces three concrete perturbation types (Bernoulli, deterministic, neighbourhood-based) with explicit mathematical forms and practical sampling procedures, extending ED beyond the Gaussian-only setting. This is validated empirically: ED-Bern and ED-Grid achieve better NLL than MCMC-based baselines on discrete density estimation (Table 1, e.g., 35.96 NLL vs. 40.36 for PCD on 8-Gaussians) and outperform most baselines on graph generation (Table 2, ED-Grid achieving 0.023 avg. MMD vs. 0.057 for CD+GWG).

- **Gradient-informed proposals with closed-form tractability and consistent (though task-dependent) improvement.** The gradient-informed proposal derived via importance sampling and a linearized approximation yields a tractable closed-form Bernoulli proposal (Equation 13) that improves over the uninformed counterpart on most datasets. ED-∇Bern outperforms ED-Bern on three of four image benchmarks (Table 3), and the paper explicitly acknowledges that the improvement is absent for grid-neighbourhood perturbations, providing a plausible explanation (local trapping).

- **Strong results on density estimation and graph generation.** On three discrete density estimation tasks (Table 1), all ED variants significantly outperform PCD, ALOE+, and EB-GFN. On graph generation (Table 2), ED-Grid achieves the best average MMD across degree, clustering, and orbit metrics. These results convincingly demonstrate that ED can train effective discrete EBMs without MCMC on these problem classes.

- **Clear conceptual connection to and differentiation from CD-1.** The paper identifies that ED with M=1 and gradient-informed proposals resembles CD-1 but with initial perturbation from q(y|x) rather than x, and explains why multiple negative samples and importance weights provide theoretical grounding that CD-1 lacks. This is a well-articulated contribution that positions the method clearly in the literature.

## Weaknesses

### Fatal
None.

### Major

- **Large performance gap on MNIST undermines the "competitive" claim for image modeling.** On MNIST (Table 3), the best ED variant (ED-∇Bern) achieves NLL ≈ 118.46, while Gibbs/GWG/DULA achieve ≈ 81–83 — a gap of ~35–37 nats. The paper acknowledges this gap but dismisses it by citing efficiency (parallelizable M=32 evaluations). However, a 35+ nat gap on a standard benchmark is not "competitive" by any reasonable standard. The paper's conclusion states that ED "can achieve competitive results even for intricate data sets such as discrete images" — this is contradicted by the MNIST results. The Omniglot results are closer, but the claim is overstated for the overall image modeling category. The paper should either (a) show that increasing M closes this gap, (b) explain what structural property of high-dimensional binary images causes ED to struggle, or (c) qualify the claim as applying only to Omniglot-scale problems.

### Minor

- **Theoretical conditions for discrete perturbations are not fully specified.** Proposition 1 states that "under mild conditions on q" the ED minimizer recovers the data distribution, but the paper never states these conditions explicitly for the discrete case or verifies them for the proposed perturbations. The KLC equivalence (lines 55–67) provides a general theoretical justification that partially addresses this — KLC_Q(p1,p2) is zero iff p1=p2 for any proper convolution operator Q — which is a reasonable foundation. However, the paper asserts this property without establishing what properties Q must satisfy for it to hold. The deterministic transformation q(y|x) = δ_{g(x)}(y) is many-to-one, and it is not obvious that the resulting convolution operator yields a valid KLC divergence. A brief discussion of the required conditions would resolve this.

- **No runtime or efficiency comparison provided.** The paper repeatedly claims efficiency and parallelism advantages over MCMC-based training, but provides no wall-clock time or function evaluation comparisons. For the efficiency claim to be meaningful, the paper should compare e.g. training time per epoch for ED vs. CD methods, or at least quantify the cost of M forward passes vs. k MCMC steps. Without this, the efficiency advantage is asserted but not demonstrated.

- **No ablation or sensitivity study for the stabilisation parameter w.** The w-stabilisation (introduced in Algorithm 1 and the loss function) affects both bias and training stability, yet the paper provides no analysis of how w is chosen, how sensitive results are to its value, or what happens when it is too large or too small.

- **ED-∇Bern improvement over ED-Bern is marginal on MNIST.** The improvement is <1 nat on MNIST (119.21 → 118.46), and the claim that gradient guidance is "consistently" helpful is technically true but the practical benefit on this task is negligible.

### Trivial
None.

## Nice-to-Haves

- An empirical analysis of the ED estimator's bias/variance as a function of M (e.g., M=1,4,16,64,256) on a small problem like the Ising model would make the consistency claim (Theorem 1) concrete and help practitioners choose M.
- A brief discussion of how to choose the perturbation type for different problem sizes/dimensions would improve practical utility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Table 4 is referenced but not present"** — Removed per rule: appendices are stripped by the parser and exist in the original submission.
- **"Theoretical grounding is incomplete / 'mild conditions' unverified for discrete case"** — Partially removed as a fatal issue and downgraded to Minor. The KLC equivalence (lines 55–67) provides a general justification that does not require case-by-case verification. However, the paper should still be more explicit about conditions.
- **"Theorem 1 is oversold / trivial asymptotic guarantee"** — Removed. This is a standard consistency result; the paper does not oversell it beyond stating the theorem. The Taylor expansion limitation is already acknowledged by the authors (line 154).
- **"Missing related works (DiGress, score-based discrete diffusion)"** — Removed per rule: the reviewer should not assert missing related works without external verification.
- **"Framing 'without MCMC' is misleading"** — Removed. The paper's claim is about training without MCMC, which is accurate. Post-training evaluation/sampling using MCMC is standard and does not contradict this.
- **"The paper should also cover additional domains"** — Removed as scope creep.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Address the MNIST gap directly.** Either show results with larger M (e.g., M=128,256) to test whether the gap closes, or provide an analysis explaining why ED underperforms on high-dimensional binary images (e.g., Bernoulli flips may be too aggressive for spatially structured pixels, or the gradient signal may be too weak in high dimensions). Qualify the "competitive" claim to reflect this limitation.

2. **Add a brief theoretical section** stating the required conditions on q for the KLC divergence to be a proper divergence (support properties, injectivity of the convolution operator) and verifying each of the three perturbation types against these conditions. This would resolve the theoretical gap without changing experiments.

3. **Add a runtime comparison** (training time per epoch or per iteration) for ED vs. CD methods on at least one benchmark, to substantiate the efficiency claim.

4. **Add an ablation of the w-stabilisation parameter** showing how NLL varies with w (e.g., w ∈ {1, 10, 100, 1000}) on a simple task.

5. **Moderate the concluding claim** about "competitive results on discrete images" to acknowledge that performance varies substantially by dataset (strong on Omniglot, weak on MNIST).

## Score and Decision

The paper presents a worthwhile extension of Energy Discrepancy to discrete spaces and introduces multiple perturbation types with gradient-informed proposals. The density estimation and graph generation experiments are strong and support the method's value. The core weaknesses are (1) a large performance gap on MNIST that contradicts the paper's claim of being "competitive" on image modeling, and (2) the lack of explicit verification of theoretical conditions for discrete perturbations (partially mitigated by the KLC equivalence). These are addressable in revision rather than structural fatal flaws. The contributions are significant enough to merit acceptance.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>