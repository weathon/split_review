I now have all the information needed to produce the final consolidated review.

---

## Summary

This paper proposes Newton Losses, a method that improves optimization of hard-to-optimize algorithmic supervision losses by exploiting their second-order information (Hessian or empirical Fisher matrix). The key idea is to construct a convex quadratic surrogate loss (the Newton Loss) whose gradient corresponds to one Newton step on the original loss, while training the neural network parameters with standard first-order gradient descent. The method is evaluated on eight differentiable algorithms across two established benchmarks (4-digit MNIST sorting and Warcraft shortest-paths), consistently improving performance — with more than 2× accuracy gains on the hardest cases — while introducing negligible computational overhead for the Fisher variant.

## Strengths

1. **Principled and novel approach to combining second-order loss optimization with first-order network training.** The paper formalizes a two-step optimization split (Eqs. 1–2) and derives a convex quadratic surrogate loss whose gradient recovers a Newton step on the original loss (Eq. after 3). This is a well-motivated departure from full-network second-order optimization, which is computationally expensive and can hurt generalization.

2. **Large performance gains on poorly-behaved algorithmic losses.** On the sorting benchmark, NeuralSort (n=10) improves from 24.26% to 48.76% with the Hessian variant, SoftSort from 27.46% to 55.07%, and Logistic DSN from 12.31% to 42.14% (Table 1). These are more than 2× improvements on settings known to suffer from vanishing/exploding gradients. The method improves or matches baselines in every one of the 8 algorithms × 2 benchmarks settings tested.

3. **Empirical Fisher variant incurs negligible computational overhead.** Runtime data (Appendix Tables 3–4) show that Fisher Newton Loss runtimes are indistinguishable from baselines (e.g., DSN n=5: baseline 1:10, Fisher 1:11; AlgoVision For+L₁: baseline 0:10, Fisher 0:10). This makes the method practical as a drop-in improvement.

4. **Thorough and honest evaluation.** The paper evaluates on 8 differentiable algorithms (4 sorting, 4 shortest-path), uses 10 seeds throughout, tunes baselines, reports statistical significance, and includes an ablation on the sole hyperparameter λ showing robustness over ~6 orders of magnitude (Figure 6). Runtime overheads are reported transparently (up to ~3.7× for naive Hessian AD on DSN; this is clearly caveated).

5. **Mathematical grounding and practical implementation.** The equivalence lemmas (Appendix), Woodbury identity derivation (Appendix), and the clever InjectFisher trick (Algorithm 2) bridge theory and practice cleanly. The paper also acknowledges known limitations of the empirical Fisher (citing Kunstner et al. 2019).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The formal Newton equivalence of the two-step split is proven only for scalar outputs (m=1).** The paper clearly states this ("for a special case of Newton's method... in the case of m=1," Lemma 2 in Appendix), and the actual method does not rely on this equivalence — it is motivated by it. However, the two-step split (Eqs. 1–2) is presented as the central motivating framework before narrowing to the scalar-output proof. Some readers may over-interpret the theoretical grounding, particularly missing that the formal equivalence does not extend to the general multi-output setting that is the paper's main use case. This is a clarity concern about framing, not a flaw in the method itself.

### Trivial

- **The third criterion for "meaningful settings" ("cannot be solved by a single GD step") is informally stated.** The paper clarifies with examples (MSE and cross-entropy), but a more precise definition (e.g., "the loss is not a convex quadratic or its gradient does not directly point to the global optimum") would strengthen the appendix's characterization.

- **Removed:** Several concerns raised by the harsh critic were found to be already addressed in the paper or reflect misunderstandings (see Removed Points).

## Nice-to-Haves

- The paper briefly notes that for Fenchel-Young losses, the Fisher variant is "not particularly meaningful" (line 533). A short discussion of *why* — the Fenchel-Young loss is defined only via its derivative, so the gradient outer product does not capture informative curvature — would deepen the analysis. This is already hinted at but could be made explicit.

- A small controlled synthetic experiment (e.g., a 2D loss landscape with known curvature) showing explicitly that the Newton Loss gradient follows the Newton direction and recovers a convex surrogate landscape would strengthen the paper's central claim. The existing gradient visualizations (Appendix Figure 8) are helpful but focus on mitigating exploding gradients rather than demonstrating recovery of the Newton direction.

- A comparison with a simple gradient preconditioning baseline (e.g., scaling loss gradients by inverse standard deviation) could help isolate whether the benefit comes specifically from the Newton curvature or more generally from any form of gradient re-scaling. This is not required, and adding it would strengthen the analysis of *why* the method works.

## Removed Points

The following concerns raised by the harsh critic were removed as they are already addressed in the paper or are not valid weaknesses:

- **"The paper could explicitly state a limitation: when m and N are both very large, matrix inversion may dominate cost."** — The paper already addresses this (Section "Woodbury Matrix Identity for High Dimensional Outputs"), providing the Woodbury identity to handle the case and noting that the inversion cost is typically small compared to the neural network computation. This is already present.

- **"The InjectFisher implementation implicitly assumes the Fisher matrix is constant across the batch."** — The empirical Fisher is defined as the batch-average outer product of gradients (Definition 2), and the implementation (Algorithm 2) faithfully implements this. The "constant across the batch" property is by design and already explained.

- **Pure formatting/style nitpicks and sentence-level pedantry.** These are parser artifacts or do not affect the paper's contribution.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a brief paragraph explaining *why* the empirical Fisher variant is ineffective for Fenchel-Young losses (the loss is defined only via its gradient, so the outer product of gradients provides Hessian-like information that is degenerate or uninformative).
2. Add a small 2D synthetic experiment demonstrating that the Newton loss gradient recovers the Newton direction and produces a convex surrogate landscape.
3. Tighten the "cannot be solved by a single GD step" criterion with a more precise definition in the appendix.

## Score and Decision

This is a well-executed paper with a novel, principled, and practically useful idea. The method is mathematically sound, the experiments are thorough (eight algorithms, two benchmarks, multiple seeds, tuned baselines, significance testing), and the computational overhead for the practical Fisher variant is negligible. The weaknesses are minor and relate to presentation clarity, not the validity of the contribution.

**Originality:** High — combining second-order loss-level optimization with first-order network-level training is novel.  
**Importance:** High — algorithmic supervision losses are increasingly popular and notoriously hard to optimize.  
**Claims:** Well-supported by experiments.  
**Soundness:** Sound — mathematics are correct, methodology is appropriate.  
**Clarity:** Clear — well-structured exposition with helpful algorithms and figures.  
**Value:** Significant — the method is ready to use as a drop-in improvement for algorithmic losses.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>