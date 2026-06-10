Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

FedCDA proposes a novel cross-round model selection strategy for federated learning aggregation. Instead of naively averaging only the current round's local models, the server maintains a cache of recent local models per client and selects, at each round, the model from each client's cache that jointly minimizes pairwise divergence before averaging. A batch-based greedy approximation reduces exponential selection complexity, and the paper provides theoretical analysis (approximation error bounds, convergence) with experiments on Fashion-MNIST, CIFAR-10, and CIFAR-100. The core idea—exploiting the fact that clients converge to different but individually valid optima across rounds—is genuinely novel and well-motivated.

---

## Strengths

1. **Novel and well-motivated aggregation direction.** The paper identifies a genuinely new dimension in FL aggregation—selecting from cached historical local models rather than only current-round models. The motivation (Figure 1) is clear: different rounds produce different local optima for each client, and a well-chosen historical model from client A may diverge less from client B's current model, enabling a closer global-model fit to all clients' data. This idea is orthogonal to prior weight-setting, model-fusion, and distillation approaches.

2. **No auxiliary dataset required.** Unlike distillation-based methods (FedDF, FedGEN) that require a proxy dataset or data generator, FedCDA operates purely on model parameters, making it applicable in settings where auxiliary data is unavailable or privacy-sensitive.

3. **Principled warmup analysis validates the method's regime of applicability.** The warmup ablation (Figure 4) systematically shows: without warmup (models unconverged → cross-round selection hurts), with moderate warmup (~100 rounds → benefits emerge), with excessive warmup (150 rounds → models too similar → benefits diminish). This experimentally confirms the paper's central thesis that cross-round selection helps precisely when local models are converged but diverse—and the paper is transparent about this boundary condition.

---

## Weaknesses

### Major

1. **Only 2 runs per setting with no statistical testing.** The paper states "each experiment setting is run twice" (line 165). The reported "standard variance" is computed from averaging the final 10 rounds within each run and comparing two resulting numbers—this is not a meaningful estimate of variability. With n=2, several reported improvements (e.g., 62.46% vs. 60.63% on CIFAR-10 Dirichlet 0.1; 47.38% vs. 41.04% on CIFAR-100 Dirichlet 0.1) could plausibly fall within noise. This materially undermines the headline claim that FedCDA "achieves the best performance on almost all settings." For a top-tier venue, at least 5 runs with confidence intervals or statistical tests are expected.

2. **The batch-based approximation mechanism is under-analyzed.** The paper's central computational contribution is the greedy batch approximation (Eq. 8, complexity O(B·K^{P/B})). However:
   - The paper claims P/B can be "maintained as a constant" but does not analyze how approximation quality degrades as B (and therefore per-batch independence) increases. In the extreme B=P, each batch is a single client and selection reduces to independently picking each client's model closest to the already-fixed average—losing the joint cross-client optimization.
   - The empirical validation (Figure 2a) uses only 10 clients with K=3, which may not generalize to larger or sparser settings. The "Effect of Batch Number" analysis (B = 1…7) is done only for one dataset (CIFAR-10, 50 clients) and reports no accuracy numbers—just a qualitative statement.
   - The key comparison between "optimal" and "approximate" selection is limited to a single (10-client, K=3) configuration. A systematic study across client counts, cache sizes, and data heterogeneity levels is needed.

3. **The convergence guarantee (Theorem 3) is inherited from FedAvg, not from the selection mechanism.** The proof sketch (line 153) explicitly confirms: first bound the gap between FedCDA and FedAvg models, then appeal to FedAvg's convergence. The paper is honest about this ("our algorithm does not achieve faster theoretical convergence," line 149), but this means the theoretical section provides no support for why selection helps—it only shows that selection does not _break_ convergence. Theorem 2 requires strong convexity and idealized conditions that the paper itself acknowledges "may be idealized in practical settings." Consequently, the theoretical contribution is weaker than the paper's framing suggests.

### Minor

4. **The gradient approximation (∇Fₙ≈0) limits the theory to a regime the paper cannot characterize quantitatively.** The central simplification from Eq. 4 to Eq. 5 relies on assuming local models are near critical points. Theorem 1 bounds the approximation error by 4Lε² + 2LDε, where ε is the distance from each model to its nearest critical point. However, ε is not algorithmically controlled—the bound can be arbitrarily large for unconverged models. The paper handles this practically via warmup (50 rounds of FedAvg), creating internal consistency, but the theory itself provides no guarantee for intermediate stages. This is a limitation common in non-convex optimization, but the paper should explicitly acknowledge that Theorem 1 provides insight rather than a hard guarantee.

5. **The method underperforms on small datasets/simple models with only a speculative explanation.** The paper notes that "the results of our method on relatively small datasets and simple CNN are not the best" and attributes this to "the features of models with different rounds are more similar on small datasets and simple models" (line 172). This explanation is untested. If the method's advantage depends on model capacity and dataset complexity, the paper should characterize this boundary more precisely rather than treating it as an aside.

6. **Limited evaluation scale.** The main results (Table 1) use 20 clients; the secondary results (Table 2) use 100 clients but only one dataset (CIFAR-100) with different hyperparameters than the main experiments. The method's reliance on per-client caches and per-round model selection raises scalability questions at larger client counts that are not addressed.

7. **Warmup design should be more carefully controlled.** FedCDA uses 50 rounds of FedAvg warmup before its selection mechanism kicks in, while baselines operate without a warmup phase. Although total rounds are equal across methods, this design means FedCDA has a 50-round "stabilization period" that baselines do not receive. The paper should either (a) give baselines an equivalent warmup period before their specific mechanisms activate, or (b) demonstrate that FedCDA's advantage persists when all methods start from the same initialization without asymmetric warmup.

### Trivial

8. **The Lipschitz constant L is set to 1 for all clients** (line 165) without estimation or sensitivity analysis. While this is a practical simplification, its effect on the Taylor expansion bound quality is unclear.

---

## Nice-to-Haves

- **Direct divergence measurement.** The paper hypothesizes that cross-round selection reduces divergence before aggregation, but never directly measures this. A plot showing pairwise divergence of selected models vs. current-round models across training rounds, with a correlation to global model accuracy, would validate the mechanism rather than just the outcome.
- **Cache staleness analysis.** Non-participating clients' models are frozen at their last selected value. With 20 clients sampled at 20%, a client participates every ~5 rounds, meaning K=3 caches span ~15 rounds. The paper should discuss how staleness affects performance in non-stationary settings or with sparser participation.
- **Interaction between cache size K and sampling rate.** The current experiments use K=3 with 20% sampling. How should K scale with sampling rate and total client count?

---

## Removed Points

These points from the inputs were filtered under the review guidelines. They are retained here for reference only and should not be weighted in the final assessment:

- **Harsh critic's "asymmetric warmup advantage" framed as major/fatal**: The critic argued that warmup gives FedCDA an unfair advantage. However, total communication rounds are equal (200) for all methods; warmup is an integral part of FedCDA's design, not a resource asymmetry. The concern is real but minor (weakness #7 above), not structural.
- **Harsh critic's "structural issue" about ∇F≈0**: Framed as a "fundamental mismatch between the regime where the theory works and the claim that the method generally improves aggregation." The paper uses warmup to operate in the valid regime, creating internal consistency. The limitation is real but common in non-convex optimization and handled practically; not a fatal flaw.
- **Harsh critic's "small-scale evaluation"**: The critic claimed 20 clients is insufficient. Many FL papers at top venues use 10–50 clients for main results. This is a minor limitation, not a major one.
- **Harsh critic's claim about missing discussion of "FedBuffer" and related methods**: The paper cites relevant related work across three aggregation families. The critic's assertion about missing baselines is unverifiable without external knowledge.
- **Strength Finder's strength about "convergence guarantee"**: The convergence rate is inherited from FedAvg (weakness #3), so it does not validate the selection mechanism. Downgraded accordingly.
- **Strength Finder's "strong and consistent empirical gains"**: Tempered by the 2-run issue (weakness #1). The direction of improvement is plausible but not reliably established.
- **Harsh critic's point about "the tables are rendered as images and are unreadable"**: This is a parser artifact, not an author error.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Increase experimental rigor**: Run at least 5 seeds per configuration, report confidence intervals or p-values. Without this, the empirical claims cannot be trusted at the level expected by ICLR.

2. **Systematically analyze the batch approximation gap**: Vary B, P, K, and N together in a controlled experiment to show how the gap between optimal (Eq. 3) and approximate (Eq. 8) selection grows with batch independence. Report accuracy and computation time jointly.

3. **Add a direct mechanism validation**: Plot the pairwise divergence of selected models vs. current-round models across training rounds. Show that (a) selected models have lower divergence and (b) lower divergence correlates with better global model accuracy. This would directly support the paper's central thesis.

4. **Clarify the warmup control**: Either give baselines an equivalent warmup phase before their mechanisms activate, or explicitly argue (and preferably test) that warmup is uniquely needed for FedCDA and does not benefit other methods.

5. **Expand evaluation scale**: Test on 200+ clients to demonstrate scalability of the cache-and-select mechanism. At minimum, provide a complexity analysis or simulation showing computation/memory cost as a function of N.

6. **Sensitivity on L**: Provide an ablation or discussion of how the L=1 assumption affects the bound quality and selection outcomes.

---

## Score and Decision

The paper introduces a genuinely novel aggregation idea with clear motivation and practical advantages over distillation-based methods. However, the experimental evidence is materially weakened by only 2 runs per setting with no statistical testing, the approximation mechanism is under-analyzed, and the theoretical convergence guarantee is inherited from FedAvg rather than validating the selection mechanism. The core idea has merit and is worth pursuing, but in its current form the empirical support is insufficient for acceptance at a top venue. The paper would benefit from major experimental strengthening and more rigorous analysis of its approximation quality.

**Score**: 5.0 / 10

**Decision**: Reject

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>