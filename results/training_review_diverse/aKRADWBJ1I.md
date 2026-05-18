Here is my final consolidated review:

---

## Summary

ActSafe proposes a model-based RL algorithm for safe exploration that combines a theoretical framework (safety guarantees and sample-complexity bounds under RKHS assumptions on dynamics) with a practical variant that scales to high-dimensional vision-based control via RSSM ensembles and Log-Barrier SGD. The theory guarantees safety throughout learning and finite-time convergence to near-optimal policies for an idealized algorithm, while the empirical results demonstrate reduced constraint violations on Safe Gym and RWRL benchmarks compared to SafeDreamer, LAMBDA, CPO, and BSRP-Lag.

## Strengths

- **First theoretical safety + sample-complexity guarantees for model-based safe RL in continuous state-action spaces.** Theorem 1 proves that the idealized ActSafe maintains safety with high probability and achieves an ε-optimal policy within a finite number of episodes, with an explicit bound involving the maximum information gain γ_n(k). This is a genuine theoretical advance over prior work: Berkenkamp et al. (2021) provides similar guarantees but in a model-free, low-dimensional setting; Koller et al. (2018) and Curi et al. (2020) provide safety but no optimality guarantees. The combination of model-based learning, continuous spaces, and both safety + sample complexity is new.

- **Clear conceptual framework for the exploration–expansion dilemma.** Section 4.2 explicitly identifies the need to expand the safe set beyond the initial seed, defines the safe set expansion operator (Definition 3.2) using a pessimistic cost estimate P_n and a distance D(π,π'), and designs an intrinsic exploration phase driven by epistemic uncertainty. The GP experiments (Figures 1–2) validate that this mechanism works: ActSafe covers the state space while respecting safety boundaries, unlike the ablations without pessimism.

- **Practical variant integrates with modern deep RL and achieves strong empirical safety.** The paper derives a tractable formulation (Equation 8) using Log-Barrier SGD and RSSM ensembles, and demonstrates on Safe Gym benchmarks (Figure 3) that ActSafe "significantly reduces constraint violation on all tasks" compared to SafeDreamer, LAMBDA, CPO, and BSRP-Lag. The sparse-reward experiments (Figure 4) further validate that intrinsic exploration is crucial for both safety and task performance.

- **Comprehensive empirical design including ablation studies.** The paper compares against variants without pessimism (GP experiments), against a Greedy baseline without intrinsic exploration (vision experiments), and includes an ablation of LBSGD (in appendix). This provides clear evidence for the necessity of each component.

## Weaknesses

### Major

1. **Unsubstantiated claim that the practical safe set inherits theoretical safety guarantees.** The paper states (line 247) that $\widehat{\mathcal{S}}_n \subseteq \mathcal{S}_n$ "making it a conservative estimate of $\mathcal{S}_n$, therefore selecting policies from $\widehat{\mathcal{S}}_n$ still preserves the safety guarantees." This claim is not justified. The theoretical $\mathcal{S}_n$ (Definition 3.2) is defined via a recursive expansion operator requiring proximity to an already-safe policy in $\mathcal{S}_{n-1}$ with the pessimistic estimate $P_n$ computed under $\mathcal{M}_n$ (the *intersection* of all confidence sets). The practical $\widehat{\mathcal{S}}_n$ uses only the current $\mathcal{Q}_n$ and has no expansion constraint. A policy satisfying $\max_{f'\in\mathcal{Q}_n} J_c(\pi,f')\leq d$ can be arbitrarily far (in terms of $D$) from any policy in $\mathcal{S}_{n-1}$, so the claimed subset relationship does not follow from the given definitions. Since Theorem 1's safety guarantee is predicated on $\pi_n \in \mathcal{S}_n$, the theoretical safety certification does not automatically transfer to the practical variant. The paper should either prove $\widehat{\mathcal{S}}_n \subseteq \mathcal{S}_n$ under stated conditions, or provide an alternative argument for the practical algorithm's safety (e.g., via direct constraint satisfaction by LBSGD combined with the well-calibrated model property, which would be a different argument). *Why it matters:* This cuts to the core claimed contribution — the paper presents ActSafe as a single algorithm with both theoretical guarantees and practical scalability, but the bridge between them is unverified.

2. **Sample complexity bound does not apply to the practical algorithm.** Theorem 1's bound (Equation 6) involves two components that do not carry over to the practical variant: (a) it concerns $\tilde{\pi}_n = \argmax_{\pi\in\mathcal{S}_n} \min_{f\in\mathcal{M}_n} J_r(\pi,f)$, i.e., a *pessimistic* objective over the *intersection* model set, whereas the practical algorithm solves $\argmax_\pi \max_{f\in\mathcal{Q}_n} J_r(\pi,f)$ (an *optimistic* objective over the *current* confidence set); (b) the bound depends on the maximum information gain $\gamma_n(k)$ of a GP, which has no defined analogue for the RSSM ensemble used in all high-dimensional experiments. The paper does not acknowledge these gaps or discuss whether any theoretical insights (e.g., the role of intrinsic exploration) carry over under the approximations made. *Why it matters:* Readers may incorrectly assume the practical algorithm inherits the finite-sample optimality guarantee, when in fact the bound is specific to a different algorithm with a different model class.

3. **Imprecise scope of the "first to show" claim.** The paper claims (lines 32, 87, 229) to be "the first to show safety and finite sample complexity for safe exploration in model-based RL with continuous state-action spaces." While this is likely accurate when parsed precisely, the surrounding context could mislead. Berkenkamp et al. (2021) provides both safety and sample complexity for safe exploration but in a *model-free* setting; Koller et al. (2018) and Curi et al. (2020) provide safety but no sample complexity in model-based settings. The paper should explicitly delineate what specific combination of properties is new (model-based + continuous state-action + safety guarantees + polynomial sample complexity) to avoid the appearance of overclaiming. *Why it matters:* A contested novelty claim can distract from the paper's real contributions.

### Minor

1. **Offline data initialization and the initial safe seed assumption.** The vision experiments initialize with 200K offline steps collected by a random policy. The paper states (line 111) that the initial safe set $\mathcal{S}_0$ "could be obtained from a simulator or offline demonstration data" — but 200K random-policy steps are qualitatively different from a seed set of safe policies. A random policy on these tasks will likely visit unsafe states. The paper should clarify how the offline data relates to Assumption 3 (initial safe seed) and whether any safety filter is applied during this data collection phase. The additional experiments "without offline data" (line 322) are in the appendix, which is stripped, so the extent to which the method works without this initialization cannot be assessed from the main paper.

2. **Per-episode vs. cumulative cost visualization.** Figure 3 reports cumulative cost with a horizontal dotted line for the constraint. Since the constraint $d$ is per-episode, a cumulative cost plot makes it impossible to determine whether individual episodes violate the constraint. LAMBDA may have higher cumulative cost while still satisfying the per-episode constraint, or may be repeatedly violating it; the figure as presented conflates these two scenarios. Per-episode cost plots (or reporting violation rates) would provide a cleaner comparison.

3. **No limitations section or explicit discussion of the theory-practice gap.** The paper would benefit from a brief discussion of which guarantees carry over to the practical variant and which do not, and under what conditions the practical algorithm could fail to be safe. The absence of this discussion is a presentation gap rather than a technical error, but it compounds the issues in Major weaknesses 1–2.

### Trivial

- The experimental section does not report $n^*$ (the switch point from intrinsic to extrinsic exploration) or explain how it was chosen.
- The paper says it ablates LBSGD in the appendix, but the main text does not summarize that result.

## Nice-to-Haves

- A per-episode cost plot or violation-rate table alongside the cumulative cost plots in Figure 3 would strengthen the safety analysis.
- Clarifying whether baselines receive the same 200K offline initialization (and if not, discussing the confound) would improve fairness of comparison.
- Reporting $n^*$ or the criterion for switching exploration phases would aid reproducibility.

## Removed Points

- *Criticism about missing appendix / proofs:* These exist in the original submission; the parser strips them. Removed per hard rules.
- *Criticism about fairness of baseline comparisons without evidence of unfairness:* The paper states it uses "the same experimental setup from Safe Gym and [As et al., 2022]" — this is a reasonable claim. The reviewer's concern is speculative.
- *Criticism about LBSGD feasibility guarantees with ensemble cost estimates:* The paper references an ablation in the appendix. Without seeing the appendix, this is an unverifiable concern. Moved to Nice-to-Haves.
- *Strength finder's generic strengths without specific citation (e.g., "this paper addressed an important problem"):* Removed as superficial.
- *Request to compare against closed-source/API-only models or models requiring weight access the authors don't have:* Removed as infeasible.
- *Request for human studies or pretraining from scratch:* Removed as infeasible.

## Novel Insights

The core tension this paper surfaces — that the theoretical machinery (safe set expansion via intersecting confidence sets and distance-based certification) is fundamentally at odds with the optimization-friendly formulation (constraint satisfaction under a single current model set) — is a genuinely important problem for the safe RL community to address. The paper implicitly demonstrates that the practical algorithm works despite this gap, raising the question: is the conservative expansion operator in $\mathcal{S}_n$ strictly necessary for safety, or does direct pessimistic constraint enforcement under a well-calibrated model suffice? The answer could substantially simplify future theoretical safe RL work.

## Suggestions

1. **Address the $\widehat{\mathcal{S}}_n \subseteq \mathcal{S}_n$ issue directly.** Either prove the inclusion under reasonable additional conditions (e.g., if every policy in $\widehat{\mathcal{S}}_n$ can be connected via $D$ to $\mathcal{S}_{n-1}$), or explicitly state that the practical algorithm's safety comes from LBSGD constraint satisfaction under a well-calibrated model rather than from the theoretical safe set construction. A one-sentence caveat acknowledging this distinction would go a long way.

2. **Separate the theory and practice more explicitly in the presentation.** The paper could frame the theoretical algorithm and the practical variant as two contributions with different statuses — one with formal guarantees (under RKHS assumptions, for low-dimensional GP models), one heuristic but empirically effective. Avoid claiming or implying that the practical variant inherits the sample-complexity bound.

3. **Add per-episode cost statistics** (violation rate, maximum episode cost) alongside cumulative plots to give readers a clearer picture of constraint satisfaction.

4. **Clarify how the offline data interacts with Assumption 3** (initial safe seed). If the random policy is not safe, discuss whether any data filtering or safety monitor is applied.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>