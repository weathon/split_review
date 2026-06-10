## Summary

DiffILO proposes an unsupervised, differentiable framework for learning to solve binary integer linear programs. The key technical idea is to reformulate the discrete, constrained ILP into a continuous, unconstrained, and differentiable-almost-everywhere merit function via probabilistic modeling (Bernoulli relaxation of binary variables) and a reparameterized penalty method, enabling end-to-end training by gradient descent without solver-generated labels. On structured benchmarks (set covering, maximum independent set, combinatorial auctions), the method achieves competitive solution quality with a 13.2× average training speedup over the supervised Predict-and-Search baseline.

---

## Strengths

- **Theoretical equivalence proofs (Theorems 1–5)** provide rigorous grounding that the probabilistic reformulation (P2) is equivalent to the original ILP (P1) in feasibility and optimality, and that the surrogate merit function in (P4) is differentiable almost everywhere. This is a non-trivial guarantee that prior differentiable approaches for specific CO problems did not provide for general ILPs.

- **The expectation-form constraint transformation (Remark 4)** is the paper's key technical innovation: by reformulating constraints as expected violations in (P2), DiffILO eliminates the need for predefined closed-form constraint penalties, which prior differentiable approaches (Karalias & Loukas, 2020; Wang et al., 2022) required and which are hard to derive for general ILPs. This is what enables the method to handle general binary ILPs rather than being limited to specific problem classes.

- **13.2× average training speedup** (Figure 3) is concretely demonstrated and directly attributed to the elimination of solver-based label generation, not to architectural shortcuts.

- **High feasibility ratios on structured benchmarks** (Figure 4): 97.1% on IS and 99.4% on CA vs. 50.8% and lower for PS's raw predictions. This directly supports the claim that end-to-end training (minimizing constraint violation) aligns training and inference better than supervised imitation.

- **Case study (Section 4, lines 230–248)** provides mechanistic insight: closed-form smoothed optimization converges to sub-optimal solutions in 11/20 runs, while DiffILO's stochastic sampling approach converges to optimal in all 20 runs, illustrating why the sampling-based approach outperforms naive continuous relaxation.

---

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient implementation detail for reproducibility.** The three stabilization techniques (normalization, adaptive μ, cosine annealing) are described at a hand-wavy level: "we apply a normalization to modify the loss function" and "we introduce a dynamic and adaptive method for adjusting μ" (line 185) — with no specifics on what normalization is applied or how μ is adapted. The number of samples *K* is introduced as a hyperparameter (line 171) but never given a value. GNN architecture details (number of layers, hidden dimensions), learning rate, and batch size are absent from the main text. These omissions prevent the reader from assessing the method's complexity or reproducing the results. If these details exist in a stripped appendix, they must be summarized in the main text for review.

2. **Unclear fairness of PS baseline comparison.** The PS trust region search is controlled by three hyperparameters (*k₀, k₁, Δ*) that the paper calls "challenging and labor-intensive" to tune (line 216), but the paper does not state how these were set in the experiments. Without knowing whether PS's hyperparameters were reasonably tuned, the comparison — which is the paper's primary empirical case against supervised methods — is suspect. If PS was run with default or poorly chosen values, the reported advantages for DiffILO could be significantly inflated.

### Minor

1. **Overclaim about being "first."** The abstract states DiffILO is "the first method to employ pure ML techniques for training, without relying on traditional solvers" (line 28), but the Related Work (Section 2.2) cites Karalias & Loukas (2020) and follow-ups that also use pure ML (albeit for specific problems rather than general ILPs). The conclusion (line 255) correctly adds the qualifier "to solve general ILPs." The abstract and introduction should be corrected to match this narrower claim.

2. **Unexplained discrepancy in training epochs.** DiffILO trains for 1,200 epochs on SC and IS but 2,400 on CA, while PS trains for 2,400 on all datasets (line 216). No justification or learning curves are provided to explain this asymmetry.

3. **No analysis of gradient approximation bias.** The surrogate in Equation 2 uses ψ (binary-rounded) for violation detection but ξ (relaxed) for gradient flow — effectively a straight-through estimator. The bias introduced by this approximation is not discussed or analyzed.

4. **No statistical significance or variance reporting.** Results in Table 1 and Figure 4 are presented as point estimates without confidence intervals or standard deviations, despite the method's reliance on stochastic sampling during training.

5. **Limited real-world validation constrains the claimed generality.** The paper honestly reports that results on the heterogeneous neos dataset "were not significant enough to draw firm conclusions" (line 225). This is a genuine limitation: the method's success is demonstrated primarily on structured, homogeneous benchmarks, and its performance on heterogeneous real-world ILPs remains unestablished.

### Trivial
- Reference to "2 for more details" and similar appendix pointers scattered through the text suggest the camera-ready version should integrate these details more cleanly.

---

## Nice-to-Haves

- Add a baseline that solves each test instance from scratch by directly optimizing (P4) via gradient descent without a learned predictor — this would directly quantify the value of cross-instance learning, which is the core of the paper's contribution.
- Report the gap to optimality (not just BKS) for synthetic benchmarks where optimal solutions are known.
- An ablation study isolating the contributions of the GNN architecture, adaptive μ, number of samples *K*, and normalization.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic's "staged comparison" claim (Point 1):** The standalone prediction comparison (Figure 4) is not staged — both methods generate predictions, and comparing their feasibility/quality is informative. The paper also provides the solver-assisted comparison (Table 1). The distinction between the two forms of evaluation is already clearly delineated in the paper.
- **Harsh Critic's "practical subtlety about smoothness" (Point 4):** The paper already acknowledges the non-convexity and limited differentiability through Theorem 5 ("differentiable almost everywhere") and Remark 7. It does not claim the landscape is smooth.
- **Strength Finder's "MIPLIB validation" strength:** The paper itself states that neos results were not significant; promoting this as a strength overstates the evidence.
- Generic formatting/style nitpicks.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface no contradictions or alternative interpretations that the paper itself does not already acknowledge.

---

## Suggestions

- Provide the missing implementation details (architecture, hyperparameters, K, normalization procedure, adaptive μ algorithm) in the main text or a clearly referenced appendix.
- Specify how PS's hyperparameters were chosen (grid search, default values, or reference to original PS paper) to establish the fairness of the comparison.
- Add confidence intervals or standard deviations to the main results.
- Tone down the "first" claim in the abstract to match the paper's own qualification ("first method for *general* ILPs").

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>