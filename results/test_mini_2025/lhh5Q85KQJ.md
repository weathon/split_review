Now I have all the information I need. Let me write the comprehensive review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now produce the final consolidated review.

Here is my framework:
1. **Round 1 bracket**: 3.5–7.5 (weak anchors ~3–3.4, strong anchors ~7.6+)
2. **Round 2 narrowing**: Read FedMAP (avg 4.0, withdrawn/reject — similar submodel training in FL) and TSAM (avg 6.25, reject but mixed — stronger SAM variant paper). Compared to FedMAP: this paper has much stronger experiments (50-56% vs ~30% accuracy) and more extensive theory. Compared to TSAM: this paper has a less clean contribution (combining existing ideas) and framing issues, but addresses an important practical problem TSAM doesn't.
3. **Final score**: ~5.0 — between the FedMAP and TSAM anchors, closer to FedMAP because the framing mismatch and evaluation gaps are real concerns, but above FedMAP because the experimental results are credible and the theoretical analysis is non-trivial.

The round-1 bracket was 3.5–7.5 based on the weak/middle/strong anchors.

Let me write the review now.Now I have all the information needed. Let me produce the final consolidated review.

## Summary

The paper proposes SubDisMO, a federated learning algorithm that combines submodel training (for resource-constrained clients) with sharpness-aware perturbation (SAM-style inner maximization) to improve generalization. The authors provide convergence analysis achieving rate $O(1/\sqrt{QTC^*})$ where $C^*$ is the minimum covering number, and a PAC-Bayesian generalization bound that incorporates the per-layer parameter remaining rate $s_j$ and perturbation $\delta$. Experiments on CIFAR-10/100 with ViT models show that SubDisMO outperforms existing resource-limited FL methods (IST, OAP, PruneFL, FedRolex, RAM-Fed) across heterogeneous settings.

## Strengths

1. **First convergence and generalization theory for submodel training with perturbation in FL.** Theorem 1 and Corollary 1 provide a convergence rate dominated by $O(1/\sqrt{QTC^*})$, where the minimum covering number $C^*$ captures the effect of submodel overlap — a novel parameter not present in full-model or standard submodel analyses. Theorem 2 explicitly relates generalization error to per-layer perturbation $\delta$ and parameter remaining rate $s_j$, going beyond existing PAC-Bayesian bounds that assume full-model training.

2. **The method subsumes multiple prior algorithms as edge cases.** Remark 1 (line 197) and the associated discussion show that setting $\delta=0$ recovers RAM-Fed, $C^*=N$ recovers FedSAM, both recovers FedAvg, and $C^*=1,\delta=0$ recovers OAP. This unification cleanly demonstrates the framework's generality.

3. **Consistent empirical improvement over submodel baselines.** Table 1 shows SubDisMO achieves the highest accuracy among all resource-limited methods across 6 settings (CIFAR-10/100 × $\mu$=0.5,1.0,IID), with gains of 1.52%–2.97% on CIFAR-10 and 0.55%–1.26% on CIFAR-100 over the next-best submodel method, while also maintaining competitive deviation.

## Weaknesses

### Major

1. **Misalignment between minimax framing and experimental evidence.** The paper labels SubDisMO a "distributed minimax optimization algorithm" and claims to be "the first resource-aware distributed minimax optimization algorithm." However, the inner maximization is a single-step gradient ascent perturbation (Eq. 5: $\tilde\theta = \theta + \delta \cdot g/\|g\|$) — exactly the standard SAM procedure. While SAM can be viewed as minimax, the paper does not evaluate on any genuine minimax problem (e.g., AUC maximization, distributionally robust optimization, adversarial training). All experiments are standard classification. The contribution is better described as "federated SAM with resource-adaptive submodel training." The gap between the claimed scope (minimax optimization) and what is demonstrated (perturbation improves submodel classification) weakens the paper's central narrative.

2. **Missing natural baselines: SAM applied to existing submodel methods.** The baselines include submodel methods (IST, OAP, PruneFL, FedRolex, RAM-Fed) combined with FedAvg/FedProx/SCAFFOLD/FedAdam — all *minimization-only* aggregation algorithms. The paper does not compare against SAM+OAP, SAM+IST, etc. This makes it unclear whether the improvement comes from the perturbation specifically or from some interaction between perturbation and the paper's particular aggregation scheme. Since the perturbation is the main claimed innovation over prior submodel work, this control experiment is important.

3. **No specification of the general mask policy $P(\theta_q; R_n)$.** The paper introduces an "adaptive mask policy" (line 65, Algorithm 1) but never defines it as a general procedure. The experiments use a fixed, random, non-overlapping partition into 4 blocks with manual assignment of sizes — this is a specific instance, not a demonstration of general resource adaptivity. Without specifying how resources $R_n$ deterministically produce masks $m_{q,n}$, the method is under-specified as a general algorithm.

### Minor

1. **Convergence guarantee only covers trained parameters.** Theorem 1 bounds $\sum_{i \in \mathcal{K}_q} \mathbb{E}[\|\nabla f^i(\theta_q)\|^2]$ — only the gradients of parameters that were trained in round $q$. There is no bound on the gradients of untrained parameters $\mathcal{S} - \mathcal{K}_q$, so the overall convergence to a stationary point of the full model is not guaranteed. The paper acknowledges this (Remark 2) but does not discuss it as a limitation.

2. **Assumption 3 (normalized gradient variance) is non-standard and its validity for Lemma 2 is not fully established.** The paper bounds variance of *normalized* stochastic gradients (Eq. 10). Lemma 2 (drift bound due to perturbation) is cited from Qu et al. (2022) but applies the smoothness constant $L$ of $f$, not of $\nabla f/\|\nabla f\|$. The gap between smoothness of $f$ and smoothness of the normalized gradient direction is not addressed. Since Lemma 2 is borrowed from existing work this is not a fatal error, but it makes the theoretical foundation less self-contained than claimed.

3. **Standard deviations are large relative to gains in some settings.** For example, on CIFAR-10 $\mu=0.5$, SubDisMO achieves 48.50% ± 8.47%, while OAP.O achieves 45.53% ± 12.13%. While the mean improvement is ~3%, the error bars overlap. The paper does not report statistical significance tests, and the loss landscape visualization (Figure 3) only compares against RAM-Fed, not the strongest submodel baselines.

4. **Practicality of the convergence rate.** The recommended learning rates $\eta_l = 1/\sqrt{Q}$, $\eta_g = \sqrt{C^*}/\sqrt{T}$ depend on knowing $C^*$ a priori, which is the *minimum* covering number — a worst-case quantity that may be difficult to estimate in a dynamic resource setting. If $C^*$ is small, this forces a small $\eta_g$, potentially slowing convergence.

### Trivial

- The paper states "OAPA achieves the lowest deviation on Dir($\mu=1.0$) for CIFAR-10" but Table 1 shows OAPA has deviation 7.16, while OAP.P has 7.18, OAP.S has 7.17, etc. The difference is negligible and the claim is imprecise.
- Equation labeling is occasionally ambiguous (e.g., Eq. 4 is repeated, and the objective in Eq. 2 uses $\epsilon_i$ while Eq. 4 uses $\epsilon$ without $\epsilon_i$).

## Nice-to-Haves

- An experiment on an explicit minimax problem (AUC maximization on a federated dataset, or DRO) would directly validate the claimed optimization setting.
- An ablation combining SAM perturbation with existing submodel methods (SAM+OAP, SAM+IST) would isolate the effect of the perturbation from the effect of the aggregation scheme.
- A concrete example or algorithm for deriving masks $m_{q,n}$ from resource constraints $R_n$ would improve reproducibility and completeness.

## Removed Points

- **"Theoretical analysis has questionable technical steps — Assumption 3 is non-standard"** (from Harsh Critic): The critic's concern about Lemma 2 requiring smoothness of the normalized gradient direction is a concern about a lemma *cited directly from Qu et al. (2022)*, not a contribution of this paper. The paper inherits the lemma from existing FedSAM theory. This is not a weakness specific to this submission.
- **"Lemma 1 borrows directly from Qu et al. (2022) but is applied to submodels — dependence on submodel mask is not shown"** (from Harsh Critic): The paper explicitly cites Lemma 1 as (Qu et al., 2022). The application to submodels is via the mask in the gradient computation (Eq. 5-6). The paper acknowledges this inheritance.
- **"Generalization bound has many constants and is stated as O bound"** (from Harsh Critic): This is standard practice for PAC-Bayesian bounds. Most such bounds in the literature are stated this way.
- **"The loss landscape visualization compares only RAM-Fed and SubDisMO"** (from Harsh Critic): The purpose of the visualization is to illustrate the *arbitrary submodel sharpness* phenomenon that motivated the method, not to rank all methods. It is a qualitative illustration, not a quantitative comparison.
- **"Scalability analysis is in the appendix"** (from Harsh Critic): Standard practice for ICLR submissions given page limits.
- **Generic strengths from Strength Finder** (e.g., "the paper addresses an important problem"): Removed as too generic to be informative.
- **"Missing related works"** and **"Reproducibility details missing (hyperparameters)"**: Removed per hard rules — missing related works cannot be verified, and trivial implementation details/nitpicks about reproducibility are excluded.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the contribution as "federated SAM with resource-adaptive submodels"** or similar. This aligns with what the method actually does and avoids the overclaim. The existing framing inflates expectations that the experiments cannot meet.
2. **Add at least one genuine minimax experiment** — e.g., AUC maximization on a federated dataset, or a distributionally robust optimization problem — to support the claim that the algorithm solves minimax problems.
3. **Include a SAM+submodel baseline** (e.g., applying SAM's perturbation to OAP or IST submodels) to demonstrate that the improvement is not simply due to the perturbation itself but to the combination proposed.
4. **Provide a concrete, general mask policy** — even a simple heuristic (e.g., "keep the top-$k$ parameters by magnitude where $k$ scales with available compute, sample uniformly") — so the method is fully specified.
5. **Discuss the limitation that only trained-parameter gradients are bounded** and clarify what this means for overall convergence.

## Score and Decision

**Round 1 (Bracketing):** Three queries anchored this paper between weak (~3.0–3.4 avg, withdrawn/reject papers on submodel FL) and strong (~7.6+ avg, accept-level papers). Plausible bracket: 3.5–7.5.

**Round 2 (Narrowing):** Two queries searched inside the bracket. Read full reviews of:
- `/home/wg25r/review_agent/human_reviews/fxCSiPPulq.md` (FedMAP, avg 4.0, withdrawn) — submodel pruning in FL with theory. This paper has weaker experiments (~30% accuracy vs ~50%+ for SubDisMO) and no generalization bound. SubDisMO is clearly stronger.
- `/home/wg25r/review_agent/human_reviews/nXTpz8pTHK.md` (TSAM, avg 6.25, reject) — SAM variant with cleaner theory and broader experiments. SubDisMO is less novel (combining existing ideas) and has framing issues but addresses a practical problem TSAM doesn't.
- `/home/wg25r/review_agent/human_reviews/9Q9KXUTjmd.md` (FedTOGA, avg 4.0, withdrawn) — SAM in FL with convergence theory. SubDisMO provides both convergence AND generalization bounds, and tackles the underexplored submodel setting, making it somewhat stronger.
- `/home/wg25r/review_agent/human_reviews/s2SLzC0IPZ.md` (FFMDR, avg 4.0, withdrawn) — federated minimax with convergence. SubDisMO is in a different sub-area (resource-limited submodels vs full-model minimax).

SubDisMO is stronger than the submodel-focused anchor (FedMAP, 4.0) and the generic FL-SAM papers (FedTOGA, FFMDR, both ~4.0), but not as strong as the clean SAM-variant anchor (TSAM, 6.25) which has a more novel formulation and broader experiments. The framing mismatch and missing baselines are meaningful concerns that prevent a higher score.

**Final Score: 5.0/10**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>