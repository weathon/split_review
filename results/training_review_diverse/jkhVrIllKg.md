Now I have a thorough understanding of the paper and all the reviewer claims. Let me synthesize the final review.

## Summary

This paper proposes SABER, a federated learning algorithm that combines bias correction (inspired by SCAFFOLD's control variate idea) with regularization (inspired by FedProx) into a local subproblem for each client. Under second-order data heterogeneity (Hessian similarity), the paper claims state-of-the-art communication complexity: \(O(\delta\varepsilon^{-2}\sqrt{M})\) for non-convex objectives and \(O((\frac{\delta}{\mu}\sqrt{M}+M)\log\frac{1}{\varepsilon})\) for PL objectives. The algorithm is stateless (no per-client control variates) and supports partial participation. Experiments on logistic regression, CIFAR-10, and FEMNIST compare SABER with FedAvg, FedProx, and SCAFFOLD.

## Strengths

- **Well-motivated use of second-order heterogeneity.** The paper clearly articulates why second-order (Hessian similarity) heterogeneity is more suitable than first-order heterogeneity for non-IID federated settings, providing the logistic regression example showing that \(\delta\) can be small even when gradients point in opposite directions (Section 1, Assumption 1 and surrounding discussion). This is a genuine conceptual contribution that distinguishes the work from the vast majority of FL theory.

- **Novel combination of bias correction and regularization in a single local subproblem.** SABER's local objective explicitly merges a bias-correction term \(\langle\mathbf{v}_k - \nabla f_m(\mathbf{w}_k), \mathbf{w} - \mathbf{w}_k\rangle\) with a proximal term \(\frac{1}{2\eta}\|\mathbf{w} - \mathbf{w}_k\|^2\) (Section 3, Equation (4)). This synthesis of SCAFFOLD-style control variates and FedProx-style regularization is methodologically novel and is presented with a clear derivation showing how it emerges from the Hessian similarity assumption.

- **Stateless design with a single shared control variate.** Unlike SCAFFOLD, which maintains per-client control variates that must be stored and updated, SABER maintains a single shared vector \(\mathbf{v}_k\) that approximates the global gradient. This is architecturally appealing for large-scale FL deployments where client memory is constrained and clients may not be revisited (Section 3, Algorithm 1).

- **The claimed communication complexity rates, if the full proof holds, represent a genuinely state-of-the-art theoretical contribution.** The rates \(O(\delta\varepsilon^{-2}\sqrt{M})\) for non-convex and \(O((\frac{\delta}{\mu}\sqrt{M}+M)\log\frac{1}{\varepsilon})\) for PL improve over prior second-order methods (SVRP, SVRS) while not requiring convexity. Lemma 1 in Section 3.2 provides a descent-like inequality that is a building block toward these rates.

## Weaknesses

### Fatal
None.

### Major

- **The deep learning experiments do not demonstrate that SABER outperforms properly tuned baselines, undermining the core empirical claims.** For CIFAR-10 and FEMNIST (Tables 2, 3), all methods use the *same fixed* hyperparameters (lr=0.01, batch size=32, 1 local epoch) — only the logistic regression experiments report tuning. SCAFFOLD is known to be sensitive to hyperparameters (local steps, server/client learning rate split), and FedProx is sensitive to the proximal coefficient. The paper uses \(\eta=0.5\) for both SABER and FedProx, but this is a SABER-specific hyperparameter that may not be suitable for FedProx. Meanwhile, SABER additionally benefits from sampling 50–100 clients for its control variate update — a mechanism with no analogue in the baselines. The reported gains (4.04× speedup over SCAFFOLD on CIFAR-10 α=0.1, 18.2 pp accuracy gain) are implausibly large without evidence that baselines were configured competitively. This does not refute the paper's theoretical contribution, but it makes the empirical claims not credible as evidence of practical superiority.

### Minor

- **The rounds-to-accuracy comparison does not account for SABER's substantially higher per-round communication cost.** SABER samples 50 (CIFAR-10) or 100 (FEMNIST) additional clients with probability \(p=0.5\) for control variate updates, averaging 25–50 extra client-server communications per round. This overhead is not reflected in the rounds-to-accuracy metric, so the claimed "speedup" in communication rounds may not translate to savings in total communication or wall-clock time. The paper should report total bits communicated or wall-clock time to substantiate practical efficiency claims.

- **Notational inconsistency between the conceptual derivation and the algorithm.** Equation (7) (line 125) writes the SABER subproblem as \(f_m(\mathbf{w}) + \langle\mathbf{v}_k - \mathbf{v}_{k,m}, \mathbf{w} - \mathbf{w}_k\rangle + \frac{1}{2\eta}\|\mathbf{w} - \mathbf{w}_k\|^2\), but Algorithm 1 (line 160) uses \(\nabla f_{m_k}(\mathbf{w}_k)\) in place of \(\mathbf{v}_{k,m}\). The paper states "The way we define \(\mathbf{v}_k\) and \(\mathbf{v}_{k,m}\) is, however, quite different from that of SCAFFOLD" (line 128) but never explicitly states that for SABER, \(\mathbf{v}_{k,m} = \nabla f_m(\mathbf{w}_k)\). This ambiguity is confusing, especially since \(\mathbf{v}_{k,m}\) is introduced as SCAFFOLD's per-client control variate in the preceding equations.

- **Gap between theory (Algorithm 1) and experiments (Algorithm 2).** The theory analyzes a single-client-per-round scheme with occasional exact full gradients for \(\mathbf{v}_k\). The experiments use 10 clients per round and approximate full gradients from subsets of 50–100 clients. The paper dismisses this gap with "the effect of minibatching has already been thoroughly studied" (line 130), but the specific recursive control variate estimator under partial client participation — where the control variate update depends on the subset composition — is nontrivial and the claimed theoretical guarantees do not directly apply to the experimental protocol. A heuristic argument or empirical analysis of this gap would strengthen the paper.

- **No error bars or repeated-run statistics for the main experimental results.** Tables 2 and 3 report single numbers without standard deviations or confidence intervals. Given the magnitude of the claimed improvements (up to 4.04× speedup, 18.2 pp accuracy gains), statistical variability is a material concern. This is not necessarily fatal — single-run benchmarks are common in some FL work — but it weakens the evidence.

### Trivial
None that survive filtering after accounting for parser artifacts.

## Nice-to-Haves

- A wall-clock time or total-communication comparison in the experiments, to complement the rounds-to-accuracy metric.
- A sensitivity analysis for the proximal coefficient \(\eta\) and the synchronization probability \(p\), showing how these affect convergence.
- A heuristic discussion of how the theory (single-client analysis) relates to the practical multi-client setting.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing convergence theorems in main text"** — The full theorem statements with rates and proof details are standardly deferred to the appendix, which was stripped by the parser. The main text states the rates clearly (abstract, contributions) and provides Lemma 1, a key building block. The missing Assumption 2 conditions (line 141) are almost certainly a parser artifact (a bullet list or equation that got garbled). Per the guidelines, criticisms about missing appendix content or parser artifacts are removed.

- **"Algorithm 1 description is incomplete (otherwise branch)"** — The complete details of the control variate update are in Algorithm 2, which is in the appendix (stripped by the parser). The surrounding text (line 94) describes the mechanism. Per guidelines, this is removed as parser-related.

- **"Empirical superiority in high-heterogeneity federated learning"** (from Strength Finder) — This claimed strength conflicts with the verified major weakness above (untuned baselines making the empirical results not credible as evidence of superiority). Per the instructions, the weakness prevails and the strength is moved here.

- **"State-of-the-art non-convex communication complexity"** (second part from Strength Finder) — The rates themselves are legitimate theoretical claims; the part about "Lemma 1 and associated theorem" being present in the main text is misleading — only Lemma 1 is present, the full theorem is in the appendix. However, the rates are stated explicitly enough that this is a genuine contribution. Kept as a strength with appropriate qualification.

## Novel Insights

Beyond the paper's own contributions (the Hessian-similarity motivation for combining bias correction and regularization, and the claimed theoretical rates), the most interesting observation emerging from the reviews is the tension between the stateless design and the practical communication overhead: SABER eliminates per-client state but introduces a different cost (occasional full/subset gradient computation across many clients) that may negate the communication savings from improved round complexity in deployment scenarios where per-round communication is the bottleneck. This trade-off is not discussed in the paper and points to a meaningful open question about when stateless methods are genuinely advantageous over stateful ones.

## Suggestions

1. **Run controlled experiments with tuned baselines.** For each baseline on the deep learning tasks, perform a hyperparameter search (at minimum over learning rate and local epochs) and report the best configuration. Show the range of achievable performance so readers can assess whether the chosen settings are reasonable.

2. **Report total communication or wall-clock time** in addition to rounds-to-accuracy, so that SABER's higher per-round cost is visible and the claimed speedup can be properly evaluated.

3. **Resolve the \(\mathbf{v}_{k,m}\) vs. \(\nabla f_m(\mathbf{w}_k)\) notation.** Explicitly state that for SABER, \(\mathbf{v}_{k,m}\) is specialized to \(\nabla f_m(\mathbf{w}_k)\) (the current client gradient), and use consistent notation throughout.

4. **Include error bars or multiple-run statistics** for the main experimental tables to establish the reliability of the large reported gains.

## Score and Decision

The paper has a well-motivated core idea and the theoretical rates, if fully substantiated in the appendix, are a genuine advance for the second-order heterogeneity line of work. The stateless design is conceptually appealing. However, the experimental evaluation has a significant methodological gap — the baselines are not tuned in the deep learning experiments, making the very large claimed improvements (4.04× speedup, 18.2 pp accuracy gains) unreliable as evidence of practical superiority. Additionally, the per-round communication cost of SABER is not accounted for, and there is a meaningful gap between the theoretical setup and the experimental protocol. These issues do not invalidate the theoretical contribution but substantially weaken the empirical case. The paper would benefit from a major revision focused on experimental rigor.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>