Now I have enough calibration data. Let me write the final review.

## Summary

This paper proposes RAC-LoRA, an iterative low-rank adaptation framework that alternates between randomly sampling one matrix (A or B) and training the other, creating a chain of low-rank updates. The key theoretical contribution is proving convergence guarantees for this random-projection-gradient-descent view of LoRA: O(1/T) sublinear rate to a stationary point under smooth non-convex assumptions and linear convergence under the PL condition. The paper also provides a counterexample where standard LoRA/COLA diverge, and presents experiments on linear regression, MLPs on MNIST, and RoBERTa on GLUE.

## Strengths

1. **First rigorous convergence analysis for a chained LoRA-style method.** The derivation in Section 5.1 showing that the RAC-LoRA update is equivalent to a random projected gradient step (Equation 3) is clean and correct. Theorems 5.3 and 5.5 provide genuine, first-of-their-kind convergence guarantees for a method that operates with genuine low-rank updates (unlike the COLA analysis which replaced low-rank with full-rank optimization). This is a non-trivial theoretical contribution.

2. **Concrete counterexample demonstrating convergence failures of existing methods.** Section 3's 3×3 quadratic example (Equation 2) with Figure 1 provides a clear, reproducible demonstration that LoRA, AsymmLoRA, and COLA can diverge or converge to suboptimal points, while RAC-LoRA converges to the optimum. This directly motivates the need for the proposed approach.

3. **Theoretical rate matches empirical behavior on linear regression.** Figure 2 shows that convergence speed scales with r/n as predicted by the theory, and full-rank (r=n) recovers FPFT's convergence. This direct theory-to-experiment validation is a strong point.

## Weaknesses

### Major

1. **The headline claim that RAC-LoRA "bridge[s] the gap between FPFT and low-rank adaptation" is not empirically supported.** On the GLUE benchmark (Table 2), RAC-LoRA performs *worse* than standard LoRA on all 4 tasks (e.g., MRPC: 87.0 vs 87.7, CoLA: 58.5 vs 60.8). The paper acknowledges this and attributes it to the tasks being "simple" such that a single LoRA adaptation already matches FPFT. But this admission directly undercuts the central motivation — if LoRA already matches FPFT on these tasks, the premise that LoRA underperforms FPFT is not demonstrated, and the claim that RAC-LoRA bridges a non-existent gap is unsubstantiated. The only evidence of chaining benefit is the MNIST experiment (Table 3), which is an artificial domain-transfer setup at rank 1. The paper needs at least one realistic task where FPFT clearly outperforms LoRA and RAC-LoRA recovers most of that gap.

2. **Convergence rates depend on λ_min^H which can be impractically small in low-rank regimes, but this is not discussed.** The linear rate in Theorem 5.5 is (1 − γ μ λ_min^H)^T. The remark gives λ_min^H = r/n under isotropic sampling. For typical settings (n ~ 10^4, r ~ 10), λ_min^H ≈ 0.001, multiplying the effective condition number by ~1000 relative to full GD. The sublinear rate in Theorem 5.3 scales as n/(r T). The paper presents these as favorable results without commenting on the practical implication: convergence may be extremely slow at low ranks. This creates a gap between the formal correctness of the rates and any claim of practical efficiency.

3. **Table 3 (MNIST) does not report any measure of variability (standard deviations or confidence intervals).** The key comparison — RAC-LoRA (Zero | Gaussian) at 96.1% vs AsymmLoRA at 81.6% with 912 params each — is presented without error bars. Given that these numbers likely depend on random initialization and sampling of the sketch matrices (which is the core of Algorithm 1), single-run results are insufficient to support the claimed improvement.

### Minor

4. **The GLUE comparison is partially confounded by different training setups.** Rows marked "*" (FPFT*, LoRA*) are taken from Hu et al. (2021) with different hyperparameters. The fair comparison is among the non-star rows (LoRA, AsymmLoRA, COLA, RAC-LoRA) run with the same codebase. In these fair rows, RAC-LoRA underperforms standard LoRA. The paper should have emphasized this rather than including the star rows which create an apples-to-oranges impression.

5. **No discussion of variance or potential failure modes of the random projections.** The theory provides an expectation bound, but a practitioner reading this would benefit from understanding what happens when a sampled matrix is badly conditioned or poorly aligned with the gradient. The paper does not discuss worst-case behavior or practical mitigation strategies.

6. **The connection between the theoretical stepsize γ (which absorbs α/r) and the AdamW learning rate used in experiments is not made explicit.** This weakens the link between theory and practice for the neural network experiments.

### Trivial

7. **Figure 1 shows single runs with no statistical variability.** While this is a simple illustrative counterexample (not a benchmark), showing multiple seeds would strengthen confidence that the claimed behavior is not a random artifact.

## Nice-to-Haves

- A comparison of total computational cost (gradient evaluations per block or wall time) between RAC-LoRA and baselines, to clarify whether the chaining comes at a computational premium.
- Clarification of what "10 chains, 10 epochs" means for the GLUE experiments — whether "epochs" refers to passes over the full training data per block or total.

## Removed Points

- **Federated learning extension not empirically tested:** The appendix (which contains the federated analysis) was stripped by the parser. Per the review guidelines, criticisms about missing appendix content that cannot be verified are removed. The federated analysis may be present in the full submission.
- **Missing engagement with randomized subspace methods literature:** Per the guidelines, missing related works should not be raised since we cannot verify their existence or absence.
- **Parameter count confusion for RAC-LoRA vs AsymmLoRA:** The critic claimed RAC-LoRA (Gaussian | Zero) uses 912 params vs AsymmLoRA's 133, but Table 3 shows both have 133 params for that configuration. The 912-row comparison is between RAC-LoRA (Zero | Gaussian) at 912 and AsymmLoRA (Zero | Gaussian) at 912 — same param count. This criticism is factually wrong.
- **Reproducibility concerns about hyperparameters, undisclosed implementation details:** These are nitpicks about trivial implementation details that are standard to omit.
- **Formatting/presentation nitpicks:** Parser artifacts, not author errors.
- **Pure speculation about confounders not supported by paper content:** Removed as speculative.

## Novel Insights

The most interesting observation from the reviews is that RAC-LoRA is structurally very similar to GoLore (from the "Subspace Optimization for Large Language Models with Convergence Guarantees" paper): both identify convergence issues in a popular low-rank method, both fix it by replacing a fixed or SVD-based projection with a random projection, both provide convergence theory for the resulting method, and both have experiments showing only marginal or mixed empirical gains relative to simpler baselines. The convergence analysis of RAC-LoRA is cleaner (standard random projection GD) while GoLore's analysis focused on the SGD noise interaction. But the shared pattern — "theory fixes a heuristic, experiments show the fix doesn't help much in practice" — suggests a structural challenge in this subfield: provably convergent methods in the LoRA family may converge to the right point but do so slowly, and the empirical benefit is only visible in carefully constructed low-capacity regimes.

## Suggestions

1. **Demonstrate the method on a task where there is an actual performance gap between LoRA and FPFT.** For example, use rank-1 LoRA on a more challenging NLU task, or a domain adaptation scenario, and show that RAC-LoRA's chaining recovers most of the gap. Without this, the headline claim is unsupported.
2. **Add standard deviations to Table 3** and ideally show that the benefit over AsymmLoRA is statistically significant.
3. **Add a discussion section on the practical implications of λ_min^H scaling**, perhaps with a figure showing how many more iterations are needed at r/n = 0.001 vs full-rank, and whether the MNIST experiment's observed convergence speed matches the predicted n/(r T) scaling.
4. **Clarify the relationship between the theoretical γ and the experimental AdamW learning rate** — even a brief paragraph would bridge the theory-practice gap.

## Score and Decision

**Round 1 bracketing:** I queried for papers on low-rank adaptation + convergence theory. Low band (<3.5) returned papers with avg 2.5–3.0 (withdrawn/rejected with clear flaws). Middle band (3.5–7.5) returned papers with avg 3.75–7.0. High band (>7.5) returned papers with avg 7.75–8.67 (all accepted). Based on the structure of the paper (solid theory + weak experiments), I placed the initial bracket at 4.5–5.5.

**Round 2 narrowing:** I queried inside the bracket and found GoLore (avg 5.25, reject) and SubTrack-Grad (avg 4.75, reject) as the most topically similar anchors.

- vs **GoLore (5.25, reject):** Both papers share the same structure — identify convergence issues in a popular method, propose a random projection fix, provide convergence theory, run experiments. RAC-LoRA's theory is cleaner (standard random-projection GD) while GoLore's experiments showed marginal improvement. RAC-LoRA's experiments are arguably weaker (method underperforms on GLUE). RAC-LoRA is slightly below GoLore in overall quality.

- vs **SubTrack-Grad (4.75, reject):** RAC-LoRA has cleaner, more rigorous theory. RAC-LoRA is clearly above this anchor.

- vs **GLoRA (4.75, reject):** RAC-LoRA's theory is far more solid. RAC-LoRA is above this anchor.

The paper sits between GLoRA/SubTrack-Grad (4.75) and GoLore (5.25), closer to GoLore. The theoretical contribution is genuine and well-executed, which prevents it from falling to the 4.0–4.5 level. But the experimental weakness — the method underperforming baselines on the main benchmark — is a significant gap that the GoLore paper did not have to the same degree. Score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>