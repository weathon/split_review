Now I have a thorough understanding of the paper and the reviews. Let me synthesize the final review.

---

## Summary

This paper proposes SABER, a federated learning algorithm that addresses data heterogeneity by combining bias correction (a shared control variate) with regularization in each client's local subproblem. Under a second-order (Hessian similarity) heterogeneity assumption, SABER achieves communication complexity \(O(\delta\varepsilon^{-2}\sqrt{M})\) for non-convex objectives and \(O((\delta/\mu\sqrt{M}+M)\log(1/\varepsilon))\) under the PL condition — improving on prior work when heterogeneity is high — while being stateless on the client side and supporting partial participation. Experiments on CIFAR-10 and FEMNIST show speedups over FedAvg, FedProx, and SCAFFOLD.

## Strengths

- **Provably better communication complexity under second-order heterogeneity.** SABER's non-convex rate \(O(\delta\varepsilon^{-2}\sqrt{M})\) and PL rate \(O((\delta/\mu\sqrt{M}+M)\log(1/\varepsilon))\) improve on the \(O((\delta^2/\mu^2+M)\log(1/\varepsilon))\) of SVRP when \(\delta/\mu \ge \sqrt{M}\), and unlike SVRP/SVRS, SABER does not require convexity. These rates are stated in the abstract and contributions (lines 63–65) and supported by Lemma 1 (lines 147–151).

- **Stateless client design.** Unlike SCAFFOLD, SABER maintains a single shared control variate \(\mathbf{v}_k\) on the server rather than per-client state, which is a practical advantage for deployment with many clients. This is clearly articulated (lines 86–94).

- **Empirical speedups on heterogeneous benchmarks.** On CIFAR-10 with LDA \(\alpha=0.1\), SABER achieves a \(1.89\times\) speedup in rounds-to-accuracy over FedAvg (Table 2) and a 14.14 pp higher top-1 accuracy after 1,000 rounds (Table 3). These gains are practically significant.

- **Clear motivation for second-order heterogeneity.** The paper provides a concrete example (logistic regression with opposite gradients) to argue why first-order heterogeneity is insufficient and why Hessian similarity is better suited for non-iid FL settings (lines 24–50).

## Weaknesses

### Fatal
None.

### Major

- **Unfair experimental comparison on client gradient budget.** The evaluation gives SABER substantially more gradient information per round than baselines without accounting for it. All methods use 10 clients per round for model updates, but SABER additionally samples 50 (CIFAR-10) or 100 (FEMNIST) clients with probability \(p=0.5\) for the control variate update (line 180). This means SABER averages 3.5–6× more gradient evaluations per round than FedAvg, FedProx, or SCAFFOLD. The speedups in Table 2 and accuracy gains in Table 3 may therefore be driven by this extra gradient information rather than the algorithm design itself. The paper does not report or control for total client gradient evaluations. A fair comparison would need either (a) reporting all methods under equal total gradient budgets or (b) transparently stating the total per-round gradient cost so readers can assess the trade-off. This issue does not invalidate the theoretical contribution, but it undermines the empirical claim that SABER "outperforms" baselines as a fair algorithmic comparison.

### Minor

- **Main theorem statements are not presented in the paper body.** The paper claims specific rates in the abstract and contributions (lines 63–65), but no formal Theorem 1 or Theorem 2 appears in the main text — only Lemma 1 (a descent lemma) is given. A reader cannot verify what the bounds depend on (the constants, \(p\), \(\eta\), inexactness parameters, worst-case assumptions) without seeing the full theorem statements. Even if these theorems reside in the appendix (which the parser strips), a theory paper should make its central results visible in the body. This is a presentation weakness that makes the theoretical contribution harder to evaluate.

- **Algorithm 1 pseudocode is incompletely specified.** The control variate update on lines 157–159 shows:
  ```
  v_k = {∇f(w_k), with probability p
         otherwise
  ```
  with the "otherwise" branch blank. The surrounding text (line 94) refers to "a refinement of the current estimate using the already sampled subset of clients," but the pseudocode does not encode this case. Additionally, the paper references "Algorithm 2" (line 94) for full details, but only Algorithm 1 appears in the extracted body. This ambiguity makes the algorithm difficult to reproduce from the main text alone.

- **Logistic regression results conflict with the "showcasing performance" framing.** Figure 1 shows SABER underperforming SCAFFOLD on both 'w8a' and 'a9a'. The paper acknowledges this (line 187) and offers plausible explanations (hyperparameter tuning favors SCAFFOLD, SCAFFOLD's accelerated rate). However, the abstract and contributions present the experiments as demonstrating SABER's performance, while the actual results are mixed. The paper would benefit from a more balanced framing that treats the logistic regression results as a validation of viability (rather than superiority) and is explicit about when SABER is expected to lag behind SCAFFOLD.

### Trivial

- **"Stateless" terminology could be clarified.** The paper describes SABER as "stateless by design" because it avoids per-client control variates, but the method still maintains a server-side control variate \(\mathbf{v}_k\) that aggregates gradient information. The term is accurate for *client-side* statelessness but could mislead readers who expect no state at all. A brief clarification would help.

- **Theory–experiment gap.** Algorithm 1 analyzes convergence for single-client-per-round sampling, while the experiments (reasonably) use minibatches of 10 clients. The paper acknowledges this gap (line 130) but does not discuss whether or how the theoretical rates extend to the minibatch setting or what additional assumptions are needed.

## Nice-to-Haves

- A discussion of the total communication and gradient-evaluation cost per round for each method, making the comparison transparent even if the budgets are not equal.
- A version of the experiments where SABER's control variate update uses the same 10 clients as the model update (rather than 50–100 extra clients) to isolate the effect of the algorithmic design from the effect of additional data access.
- Clarification of how the minibatch setting (used in experiments) relates to the single-client theory (Algorithm 1).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's point about whether the Table 1 claim on SCAFFOLD is properly verified:** The critic questions whether SCAFFOLD's restriction to "full participation and quadratic problems" is inherent or an artifact of the analysis. This is a question about the accuracy of a citation, which I cannot verify without external sources. Removed.

- **Harsh critic's claim that missing theorems is a "structural deficiency" that makes the paper unverifiable:** Per the rules, appendix sections containing theorems/proofs are stripped by the parser. The concern that the body should state formal theorems is retained as a Minor weakness (presentation), but the framing as a "structural deficiency" that invalidates the paper is too harsh and is downgraded.

- **Various minor formatting/typo observations from the harsh critic:** Removed per the rule about parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between SABER's stronger theory and SCAFFOLD's better practical performance on logistic regression, which deserves more nuanced treatment. The fairness of the experimental comparison is the most actionable concern.

## Suggestions

1. **Either restore Theorem 1 and Theorem 2 to the main text** or, at minimum, state the full rates with all constants and assumptions so the reader can evaluate the theoretical claims without consulting the appendix.

2. **Fix the experimental fairness issue** by either (a) reporting the total gradient-evaluation cost per round for each method and noting the gap, or (b) running an ablation where SABER's control variate update uses only the 10 clients already sampled for model updates, to isolate the effect of the algorithm design from the effect of additional data.

3. **Complete the Algorithm 1 pseudocode** so the "otherwise" branch of the control variate update is explicitly written, or replace it with a reference to the fully specified Algorithm 2 in the appendix.

4. **Reframe the empirical section** to more honestly acknowledge that SABER underperforms SCAFFOLD on logistic regression, and clarify that the experiments primarily validate the method's viability and stateless design rather than claiming universal superiority.

## Score and Decision

The paper identifies a meaningful problem and proposes a clean algorithmic idea with theoretically grounded rates. However, the experimental comparison is unfair to baselines in a way that undermines the empirical claims, the main theorem statements are absent from the body, and the algorithm pseudocode is incomplete. These are significant but addressable issues. The theoretical contribution is genuine and could be a solid conference paper after revisions.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>