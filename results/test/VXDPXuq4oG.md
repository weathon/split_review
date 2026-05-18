Now I have all the information needed to produce the final consolidated review.

## Summary

This paper proposes Order-Preserving GFlowNets (OP-GFNs), which replace the explicit scalar reward in GFlowNets with a learned reward that respects a provided (partial) order over candidates. The key idea is to minimize a KL divergence between a labeling induced by Pareto dominance (or pairwise comparisons, in the single-objective case) and the distribution induced by the learned reward over a batch. The paper provides theoretical analysis showing that the learned reward forms a geometric progression under idealized conditions, and presents experiments on HyperGrid, molecular design, neural architecture search (NAS), and multi-objective tasks.

## Strengths

1. **Novel and well-motivated approach to removing the scalar reward requirement in GFlowNets.** OP-GFNs learn a reward function that is consistent with a provided (partial) order, eliminating the need for explicit scalarization in multi-objective settings and the need to tune a reward exponent β in single-objective settings. The unified formulation via Pareto labeling (Eq. 3) naturally handles both total-order and partial-order problems.

2. **Strong empirical results across diverse single-objective tasks.** In molecular design (Bag, QM9, sEH, TFBind8/10), OP-TB outperforms previous GFN methods (TB, DB, subTB, MaxEnt, GTB) and RL methods (A2C, SQL, PPO, MARS) in both top-100 average reward and number of distinct optimal candidates found (Fig. 2). In NAS on NATS-Bench, OP-TB variants achieve higher test accuracy at lower accumulated T&T time than TB, REA, BOHB, and REINFORCE (Fig. 3).

3. **Reward sparsification theory provides useful intuition.** Propositions 1 and 2 show that under an idealized static optimization setting (minimizing pairwise KL losses over a fixed set with bounded rewards), the learned reward converges to a geometric progression that assigns exponentially higher values to better candidates and nearly equal values to candidates with the same objective. This offers an intuitive explanation for the exploration-exploitation dynamics observed in practice.

4. **Effective on multi-objective Pareto front approximation without scalarization.** OP-GFNs demonstrate competitive or better Pareto front approximation compared to preference-conditioned (PC) and goal-conditioned (GC) GFlowNets across HyperGrid, n-gram, DNA, and fragment-based molecule tasks, while avoiding the need to specify preferences or goals (Tables 1-3, Fig. 4-6). The method handles non-convex Pareto fronts, which is a known limitation of linear scalarization.

5. **Generality across GFlowNet training objectives.** The order-preserving loss is compatible with TB, FM, DB, and subTB formulations, and the paper provides ablation studies showing similar performance gains across all variants.

## Weaknesses

### Fatal
None.

### Major

1. **Missing GFN-β baseline in molecular design experiments weakens the central empirical claim.** The paper's motivation centers on the difficulty of choosing the reward exponent β. Yet the molecular design experiments (Section 4.2, Fig. 2) compare OP-TB against standard TB (β=1), DB, subTB, MaxEnt, GTB, and RL methods — but not against GFN-β with a tuned β. The NAS experiments (Section 4.3) do include GFN-β (β=4,8,16,32,64,128), and OP-TB outperforms it there. However, without this comparison in the molecular domain — where the paper makes its strongest "outperforms all baselines" claim — the advantage of OP-GFNs could partly reflect suboptimal default β rather than a genuine benefit of order-preserving learning. This is the most directly relevant baseline for the paper's own stated motivation.

2. **Gap between theoretical analysis and actual training procedure.** The core theoretical results (Propositions 1 and 2) analyze a **static** minimization problem: minimizing a sum of pairwise KL losses over a fixed set with known total order and rewards constrained to [1/γ, 1]. This does not directly describe the actual algorithm, where (a) rewards are unconstrained and the GFlowNet loss is jointly optimized with the order-preserving loss on streaming batches, (b) the ordering is computed from batch samples rather than a predetermined ranking, and (c) γ is a bound in the analysis, not a trainable parameter. The paper asserts that the idealized behavior "carries over" to the dynamic setting (e.g., line 117: "γ is driven to infinity when minimizing L_OP-N with a variable γ"), but this connection is asserted, not argued. The exploration-exploitation balance claim (Contribution 4 in Section 1) is presented as a theoretical result but is not rigorously justified for the actual joint training dynamics. Addressing this gap would require either analyzing the actual training procedure or providing compelling empirical evidence (e.g., tracking reward ratios over training steps) that the predicted sparsification occurs. As it stands, the theory provides intuition but is disconnected from the algorithm it claims to describe.

### Minor

3. **The "state-of-the-art" claim in the abstract overstates the multi-objective results.** The abstract claims "state-of-the-art performance in ... multi-objective Pareto front approximation," but the paper's own text characterizes the multi-objective results more modestly: "OP-GFNs achieve comparable or better performance" (line 220), "similar or better" (line 214). The multi-objective comparison includes only preference-conditioned and goal-conditioned GFlowNets; while these are the most relevant baselines, the results show competitiveness rather than clear superiority. The paper should align its abstract language with the more measured tone of the body.

4. **Proposition 3 (flow assignment) is an existence result under strong assumptions that does not establish the claimed credit assignment during actual training.** The proposition shows that in a prepend/append MDP with uniform P_B and sufficiently sparsified reward (α_γ > 4), the expected flow concentrates on longest common substrings. This result depends on conditions (fixed ordering, bounded reward, uniform backward policy) that may not hold during joint training of the flow and the order-preserving loss. The connection to "efficiently assign high credit to the important substructures" (Contribution 3) is claimed rather than demonstrated.

5. **The use of a replay buffer in multi-objective experiments is a significant design choice mentioned only in passing.** The paper notes (Section 5.2) that a replay buffer is used to stabilize training in the n-gram and fragment-based molecule experiments, and says GC-GFNs also use it. However, this modification is not discussed in the method section (Section 3), and its effect on performance is not ablated. Since the replay buffer can fundamentally change training dynamics (especially for an online sequential sampler like GFlowNets), this deserves more attention.

6. **Evaluation is limited to top-k discovery and cannot assess distributional accuracy.** The paper acknowledges (Section 3.3) that because the true reward is unknown, standard distributional metrics (Spearman correlation between log p(x) and R(x)) cannot be used. However, the paper does not attempt to validate that the learned distribution is well-calibrated, even in a synthetic setting where the true reward could be made known. The evaluation focuses entirely on whether good candidates are found, which conflates sample efficiency with distributional fidelity.

7. **Ablation of batch size B for the order-preserving loss is absent.** The order-preserving loss is computed on batches of size B, which determines the effective number of pairwise/Pareto comparisons. No analysis or ablation is provided for how B affects performance, sparsification rate, or stability.

### Trivial

8. The bound R(x) ∈ [1/γ, 1] in the theoretical analysis is not justified; in practice, rewards can be arbitrary positive values. This is a known limitation of the idealized setting.

9. The first 64 candidates in NAS experiments are from a random policy (footnote, Fig. 4). The paper should clarify how this affects the early training dynamics and the exploration-exploitation claim.

## Nice-to-Haves

- An ablation study of batch size B for the order-preserving loss.
- Discussion of computational overhead from pairwise/Pareto comparisons within each batch.
- A discussion of the backward KL regularization and trajectory augmentation techniques used in NAS in the main text, not just the appendix.
- A synthetic experiment where the true reward is known (e.g., a simple function with known optima) to evaluate whether OP-GFNs produce a well-calibrated distribution, not just good top-k candidates.

## Removed Points

These points were identified in the reviews but are removed after cross-checking against the paper:

1. **"L_OP-N is not defined clearly in the main text"** — The paper defines L_OP-N in Eq. 5 (eq:lemma_objective) as ∑_{i=1}^n L_OP({x_{i-1}, x_i}; r). The definition is present and correct. Removed as a style nitpick.

2. **"The paper uses 'order-preserving' in two different senses that are not formally connected"** — The paper explicitly presents a unified framework in Section 3.1 (Pareto labeling) and shows in Section 3.2 how the single-objective case is a special case (reducing to pairwise comparisons). The connection is established; the critic missed Section 3.1. Removed as a misreading.

3. **"Evaluation protocol limitation is not acknowledged"** — The paper explicitly states (line 138): "Therefore, we only focus on evaluating the GFlowNet's ability to discover the maximal objective." The limitation is acknowledged. The suggestion to add synthetic evaluation is valid but the criticism that the paper hides this is not. Removed and moved to Nice-to-Haves.

4. **"Missing non-GFN baselines for molecular design"** — The critic acknowledges "this is acceptable given the paper's focus on GFlowNets, but the SOTA claim should be qualified." The paper's primary contribution is a methodological extension to GFlowNets; comparing against Bayesian optimization or genetic algorithms is outside its scope. Removed as scope creep.

5. **"NAS main text doesn't specify training budget in trajectories"** — The paper specifies the budget in accumulated T&T time (50K/100K/200K seconds), which is the relevant cost measure in NAS where different architectures have different training times. This is standard practice in the NAS literature. Removed as a preference issue.

6. **Notation criticism of Proposition 1** — The critic claims L_OP-N is only introduced in Eq. 5 and not given a full definition; but the equation is the definition. The paper's notation is standard and correct. Removed.

## Novel Insights

A genuinely novel insight that emerges from this review is that the paper's central technical contribution — replacing scalar rewards with order information — is actually *two distinct contributions* under a single framework. The single-objective case (pairwise comparisons, implicit geometric progression of rewards) and the multi-objective case (batch Pareto labeling, replay-buffer stabilization) are solving different fundamental problems. The single-objective version addresses the β-tuning problem by dynamically sparsifying the learned reward landscape, while the multi-objective version addresses the scalarization problem by learning from partial orders. These could have been separate papers; their unification is a strength (coherent framework) but the paper would benefit from being explicit about the distinct challenges each version addresses. The efficiency gain in NAS — using the ordering of a cheap proxy (u₁₂) to train a sampler that performs well on an expensive metric (u₂₀₀) — is an underappreciated contribution that deserves more prominence in the paper.

## Suggestions

1. **Add GFN-β with tuned β to the molecular design experiments.** This is the most important addition. Select β values on a held-out subset or a cheap proxy, and report the results. Without this, the paper's central empirical claim is incompletely supported.

2. **Reframe the theoretical analysis as providing intuition for a static minimizer, with stronger empirical validation of the predicted dynamics.** Track the learned reward ratios (R̂(xⱼ)/R̂(xᵢ)) over training steps to demonstrate that the geometric progression and sparsification actually occur during joint training. This would bridge the gap between theory and practice.

3. **Align the abstract's claims with the paper's actual multi-objective results.** Replace "state-of-the-art" with "competitive performance" in the multi-objective context, or provide clearer evidence of superiority.

4. **Discuss the replay buffer in the method section (Section 3)** and provide an ablation showing its effect in multi-objective settings.

5. **Consider adding a controlled experiment** (e.g., on HyperGrid with a known reward function) where distributional accuracy (Spearman correlation) can be evaluated to separate sample efficiency from distributional fidelity.

## Score and Decision

**Originality:** 7/10 — The core idea (learning rewards from order information instead of using explicit scalar rewards) is novel within the GFlowNet literature and clearly motivated.

**Importance of research question:** 8/10 — Eliminating the need for scalar reward specification and β-tuning is practically important for GFlowNet applications.

**Claims support:** 5/10 — The empirical claims are partially supported but the missing GFN-β baseline in molecular design and the gap between theory and algorithm weaken the evidence. The abstract's "state-of-the-art" claim for multi-objective tasks is not fully supported by the results.

**Soundness of experiments:** 6/10 — The experiments are extensive and cover diverse domains, but the omission of the most directly relevant baseline (GFN-β in molecular design), the unablated use of a replay buffer in multi-objective settings, and the absence of batch-size ablation reduce overall soundness.

**Clarity of writing:** 7/10 — The paper is generally well-written but the theory section could be clearer about what is idealized vs. what directly applies to the algorithm.

**Value to community:** 7/10 — The method is practically useful and the framework is general. Once the empirical weaknesses are addressed, it will likely be used by the GFlowNet community.

**Overall assessment:** The paper proposes a genuinely novel and well-motivated extension to GFlowNets with strong empirical results across several domains. However, the missing GFN-β baseline in the molecular design experiments and the disconnect between the idealized theory and the actual training procedure are significant concerns that prevent a stronger assessment. The contributions are real and the empirical work is extensive; the paper is publishable but should address these issues in a revision.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>