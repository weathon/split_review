Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper introduces a **double-pessimism principle** for offline robust reinforcement learning, which conservatively handles both dataset scarcity (via a visitation-based penalty) and model mismatch (via a penalty that lower-bounds the robust value function without needing the transition kernel). The authors provide the **first model-free algorithm for offline robust RL** with sample complexity analysis under \(l_\alpha\)-norm uncertainty sets, for both finite-horizon and infinite-horizon settings. The theoretical memory advantage (\(O(SA)\) vs. \(O(S^2A)\) for model-based methods) is clearly articulated.

## Strengths

- **Novel double-pessimism principle.** The idea of jointly pessimistically addressing dataset uncertainty and model mismatch in a model-free way is conceptually elegant and fills a clear gap in the literature. Definition 1 and Lemma 1 provide a concrete construction of the model-mismatch penalty \(\kappa\) for \(l_\alpha\)-norm uncertainty sets that guarantees conservative estimation without requiring the transition kernel (lines 166–172, 202–206).

- **First sample complexity analysis for model-free offline robust RL.** Theorems 2 and 3 give sub-optimality bounds for both finite-horizon and infinite-horizon settings. This is a genuine theoretical contribution — prior offline robust RL work (Shi & Chi, 2022; Blanchet et al., 2023) is exclusively model-based. The finite-horizon result matches non-robust offline Q-learning sample complexity (Remark 3, lines 224–230), and the infinite-horizon result matches model-based robust RL in key parameters (Remark 4, lines 249–253).

- **Theoretical scalability advantage is clearly articulated.** Section 7.1 (lines 267–271) provides a concrete comparison: model-based approaches require \(O(S^2A)\) memory to store the transition model, while the proposed algorithm requires only \(O(SA)\). The per-step update also avoids the inner product \(\hat{P}_{s,a}V\) needed by model-based methods. This theoretical efficiency argument is well-grounded.

## Weaknesses

### Fatal
None. The core theoretical contribution (first model-free algorithm with sample complexity for offline robust RL) is novel and technically sound.

### Major

1. **Experiments compare only to a non-robust baseline, so they do not support the claimed improvement over existing robust methods.**  
   The abstract, contributions, and conclusion claim that the method "significantly improves robustness in a more scalable manner than existing methods" (lines 4, 22, 306). Yet the experiments (Sections 8.1–8.2) compare *only* to single-pessimism Q‑learning (Yan et al., 2022), which has no robustness mechanism whatsoever. No comparison is made to existing robust offline RL methods (Shi & Chi, 2022; Blanchet et al., 2023) that the paper positions as the key competitors. On the Garnet problems, where model-based robust methods could be run, this comparison is straightforward and its absence is a significant omission. Without it, the experiments demonstrate only that double-pessimism beats a non-robust baseline, not that it improves upon the robust state of the art.  
   *The paper's central empirical claim remains unsubstantiated.*

2. **Scalability claims lack empirical verification.**  
   The paper repeatedly emphasizes improved scalability (e.g., "more scalable manner," "model-free algorithm... suitable for large-scale problems," "effectiveness in solving more complex Classic Control problems with robustness guarantees, which have proven difficult or unsolvable for previous model-based robust methods" — lines 4, 22, 297–299). However, the experiments are limited to tiny tabular Garnet problems (e.g., G(50,100,50)) and discretized classic control tasks. **No runtime or memory measurements are reported anywhere.** The claim that "model-based approaches become ineffective" for Classic Control (line 297) is asserted without evidence — no model-based method was tested. The theoretical memory advantage is real, but the paper provides no empirical evidence that it translates to practical scalability advantages.

3. **"Near-optimal" sample complexity claim is unjustified without a lower bound.**  
   The paper calls its sample complexity "near-optimal" in the contributions list (line 22), Remark 4 (line 253), Section 7.1 (line 269), and the conclusion (line 306). The justification is that the rates match *non-robust* offline Q‑learning and model-based robust RL. However, **no lower bound for offline robust RL is provided or cited**. Matching a non-robust rate does not imply optimality in the robust setting, where the problem is fundamentally harder. The term "near-optimal" should either be supported by a formal lower bound or replaced with "competitive with" or "matching the best-known rates."

### Minor

4. **Robust single-policy concentrability is substantially stronger than standard "partial coverage."**  
   Assumptions 1 and 2 (lines 107–113, 136–139) take a maximum over *all* worst-case kernels \(P' \in \mathcal{P}\), not just the nominal kernel. The paper describes this as "only requir[ing] that the dataset covers the state-action pairs that are visited by the optimal policy, known as the partial coverage condition" (line 115). This is misleading: the condition requires coverage of state-action pairs reachable under *every* adversarial kernel in the uncertainty set, which is far more demanding. When the uncertainty set is large, \(C^*\) can be arbitrarily large or infinite. The paper does not discuss when this condition can reasonably hold or how it compares to assumptions in prior model-based offline robust RL.

5. **Apples-to-oranges comparison in Table 1 weakens the claims.**  
   Table 1 compares sample complexity across methods that study *different* uncertainty set structures (Shi & Chi, 2022 study KL-divergence; Blanchet et al., 2023 study non-rectangular RMDPs). The claim of "improved S‑dependence compared to (Blanchet et al., 2023) under the \(l_\infty\)-norm" (line 269) compares across different uncertainty set formulations, which is not an apples-to-apples comparison.

6. **Missing experimental details hamper reproducibility.**  
   - For Classic Control tasks, no discretization method or resolution is described, nor how the uncertainty set radii \(R_{s,a}\) were set.  
   - The "optimal robust value" in Garnet experiments (Figure 1) is not explained — it is presumably computed via robust value iteration with the true kernel, but this is never stated.  
   - The radius range \(R_{s,a} \in [0.1, 0.5]\) is given for Garnet (line 280), but no details are provided for how these values were chosen or how they affect results.

### Trivial
None that survive the instructions' filtering.

## Nice-to-Haves
- **Ablation study** separating the contributions of the two pessimism terms (\(\kappa\) vs. \(b\)) would strengthen the paper by validating the design principle.
- **Example trajectories or qualitative analysis** in Classic Control showing how the double-pessimism policy behaves differently under perturbations would provide useful intuition.
- **A discussion of how the robust concentrability coefficient \(C^*\) can be bounded** for common uncertainty set choices would help assess the practical relevance of the theoretical bounds.

## Removed Points
*These points were removed per the filtering rules; they are listed for completeness but should not be treated as valid weaknesses.*

1. **Criticism about missing algorithm pseudocode/textual description** — The core update rule is given in equation (15) and the penalty function \(\kappa\) is specified in Lemma 1. The algorithm images are parser artifacts. The textual description is sufficient for a theory paper.
2. **Criticism about extending to function approximation** — This is outside the paper's stated scope (tabular setting). Demanding it is scope creep.
3. **Strength from Strength Finder about "Experimental validation in realistic control tasks where model-based methods are infeasible"** — This conflicts with the verified weakness that the paper does not actually demonstrate model-based infeasibility. The claim is asserted without evidence.
4. **Strength from Strength Finder that lacks specific evidence** — Some phrasing was generic; the retained strengths above capture the concrete contributions.

## Novel Insights

An interesting observation that emerges from the reviews is the **tension between the model-free design's theoretical elegance and the practical demands of specifying the uncertainty set**. The double-pessimism principle is clever precisely because it avoids learning the transition kernel — yet the uncertainty set (including the crucial radii \(R_{s,a}\)) is defined relative to the nominal kernel. A practitioner must choose these radii without a model, which somewhat undercuts the "model-free" appeal. This tension is acknowledged in passing (the paper notes the radii must be "small enough" to keep perturbed probabilities non-negative) but deserves explicit discussion: the model-free benefit is in the algorithm's *computational* structure (avoiding \(O(S^2A)\) storage and inner products), not in eliminating the need to reason about the transition dynamics entirely.

## Suggestions

1. **Add baselines.** Run model-based offline robust RL methods (Shi & Chi, 2022; Blanchet et al., 2023) on the Garnet problems. Even a simplified version would substantiate the claim that double-pessimism offers comparable or better robustness with better scalability. Without this, the core empirical claim is unsupported.

2. **Provide runtime/memory measurements.** On Garnet problems of increasing size (e.g., \(S=50, 100, 200\)), report wall-clock time and memory usage for the proposed method vs. a model-based baseline. This would turn the theoretical \(O(SA)\) vs. \(O(S^2A)\) argument into concrete evidence.

3. **Tone down the "near-optimal" claim** unless a lower bound for offline robust RL is provided or cited. Replace with "competitive with the best-known rates for non-robust offline Q-learning and model-based offline robust RL."

4. **Acknowledge the strength of the robust concentrability assumption** explicitly. Clarify that it requires coverage under all adversarial kernels, not just the nominal one, and discuss settings where it might be reasonable (small uncertainty sets, smooth transitions).

5. **Add missing experimental details** (discretization, radius selection for Classic Control, how the optimal robust value was computed for Garnet) to ensure reproducibility.

6. **Clarify the Table 1 comparison.** Acknowledge that the comparison to Blanchet et al. (2023) involves different uncertainty set structures, or restrict the comparison to methods studying the same uncertainty set family.

## Score and Decision

This paper makes a genuine theoretical contribution — the first model-free algorithm for offline robust RL with sample complexity guarantees — and the double-pessimism principle is conceptually novel. However, the experimental evaluation has a **major gap** (no comparison to existing robust methods, no empirical scalability data), and several claims are overstated ("near-optimal" without a lower bound, "more scalable" without runtime measurements). The theoretical work is solid enough that the paper is not fatally flawed, but it cannot be accepted in its current form.

The paper needs a major revision focused on: (1) adding proper baselines to support the robustness claims, (2) providing empirical scalability evidence, and (3) calibrating the claims to what is actually demonstrated. With these changes, the paper could become a strong contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>