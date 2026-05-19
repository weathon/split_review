- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 8, 5
Now I have a thorough understanding of the paper and all reviewer inputs. Let me compose the final consolidated review.

---

## Summary

This paper proposes SDAR (Spatially Decoupled Action Repetition), a closed-loop action repetition framework for continuous control that makes independent act-or-repeat decisions for each action dimension. Unlike prior methods such as TAAC that force all dimensions to repeat or change together, SDAR uses a two-stage policy (selection → action) where a selection policy β outputs per-dimension binary decisions and an action policy π generates new values only for the "act" dimensions. The method is evaluated across 11 continuous control tasks spanning classic control, locomotion, and manipulation, showing improvements in sample efficiency, final episode return, and action smoothness over baselines including SAC, N-repetition, TempoRL, UTE, and TAAC.

## Strengths

- **Novel per-dimension decomposition of the act-or-repeat decision.** SDAR is the first method to decouple repetition decisions across action dimensions (Section 4.1, Eqs. 1–5, Fig. 1). The idea is clearly motivated — different actuators in a robot may require different repetition frequencies — and the two-stage architecture is cleanly formalized.

- **Consistent empirical gains across multiple task categories.** Table 1 shows SDAR achieves the highest normalized AUC scores in Classic Control (0.85±0.08), Locomotion (0.72±0.06), and Manipulation (0.78±0.05), and the learning curves in Fig. 3 show systematic advantages over baselines, particularly in complex tasks like Humanoid where SDAR overtakes TAAC in later training and sustains higher final performance.

- **Good balance of persistence, smoothness, and final return.** Table 2 shows SDAR obtains the best or near-best episode return in 6 out of 9 tasks while maintaining high Action Persistence Rate (APR > 3.0 in half the tasks) and low Action Fluctuation Rate (AFR). For example, on Humanoid, SDAR achieves episode return 1.23±0.17 with APR 3.69±1.56 and AFR 0.517±0.015, whereas TAAC's lower return (0.86±0.19) is paired with a lower APR (1.66±1.15) — SDAR is not simply repeating more; it repeats more effectively.

- **Visual evidence of dimension-specific repetition behavior.** Figure 4 and Table 3 directly show that SDAR learns different repetition patterns for different action dimensions (e.g., leg joints at 73.4% vs. foot at 64.3% in Walker2d), while TAAC forces uniform 55.4% for all joints. This provides direct evidence that the per-dimension mechanism is actually being used.

- **Practical optimization for high-dimensional action spaces.** Section 4.3 introduces an importance-sampling variant (Eq. 9) that avoids the exponential cost of enumerating all 2^{|A|} combinations, making the decoupled framework computationally tractable for tasks like Humanoid (|A|=17). This design choice is critical for real-world applicability.

## Weaknesses

### Fatal
None.

### Major

- **The spatial decoupling mechanism is not isolated from other design differences with TAAC.** The central claim is that per-dimension act-or-repeat decisions drive the improvement. However, SDAR differs from TAAC (the closest closed-loop baseline) in multiple ways beyond decoupling: the Mix operation (Eqs. 1–2) for input preprocessing, separate entropy temperatures α_β and α_π for the two policies, and importance-sampling-based optimization for β (Eq. 9). Any of these could contribute to the observed performance gap. The paper does not include a controlled ablation where the per-dimension output of the selection policy is replaced with a single binary decision applied uniformly to all dimensions while keeping all other infrastructure (Mix operation, separate entropy targets, importance sampling) unchanged. Such an experiment would directly attribute the gains to spatial decoupling versus other algorithmic innovations. Without it, the core claim is incompletely validated — the evidence supports SDAR as a whole method being effective, but not specifically that the decoupling (rather than auxiliary design choices) is responsible.

### Minor

- **Table 2 lacks uncertainty measures and reporting methodology.** The paper reports episode return, APR, and AFR in Table 2 with no standard errors, standard deviations, or confidence intervals, despite using at least 10 seeds (as stated for Fig. 3). Table 1 (AUC scores) and Fig. 3 (learning curves) do include standard errors, making the omission from Table 2 conspicuous. Additionally, the paper does not state whether the values in Table 2 are final policy performance, best performance during training, or averages over the last N episodes. This makes it difficult to assess the statistical reliability of the reported advantages.

- **The number of importance-sampling samples for β is not specified.** Equation (9) uses importance sampling over "several b" sampled from β_old to avoid the 2^{|A|} enumeration cost, but the paper never states how many samples are drawn. This is a reproducibility gap — the sample count affects both computational cost and estimator variance, and the choice could be task-dependent (e.g., more samples for Humanoid with |A|=17 than for LunarLander with |A|=2).

### Trivial
None.

## Nice-to-Haves

- A brief justification for the choice of ξ = -2 as the constant mask (outside the action range [-1,1]) would help readers understand the design rationale.
- A wall-clock time comparison would help practitioners assess the computational overhead of the two-stage decision process relative to SAC or TAAC.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism about PIC not being included as a baseline** (Harsh Critic, Section-by-Section Notes): The paper does not owe an explanation for every cited method's omission from the experimental comparison. The baseline set already covers the relevant categories (naïve, open-loop, closed-loop) and is reasonable. Removed.

- **Request for architecture details (layer sizes, activations)** (Harsh Critic, "Missing Parts"): Architecture details for MLP policies are standard and the paper's description ("MLP") is consistent with common practice in the field. This is a trivial reproducibility nitpick. Removed per instruction to remove such nitpicks.

- **"The evidence falls short of what is needed to definitively support the contribution"** — this overall assessment is not itself a weakness but a global evaluation. It is superseded by the specific weaknesses listed above. The paper provides substantial evidence; the gaps are addressable.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same picture: a well-motivated method with strong empirical results but missing a targeted ablation to isolate the core mechanism. There is no deep disagreement that would yield a novel insight beyond what the paper states.

## Suggestions

1. **Add a controlled ablation** that keeps the full SDAR infrastructure (Mix operation, separate entropy targets, importance-sampling) but changes the selection policy to output a *single* binary decision applied uniformly to all dimensions. Compare this variant to both full SDAR and TAAC. This is the single highest-leverage improvement and would cleanly validate the core claim.
2. **Add standard errors or confidence intervals to Table 2**, computed from the same at-least-10 seeds used elsewhere. Report whether the final-return differences between SDAR and TAAC are statistically significant (e.g., via a paired bootstrap test).
3. **State the number of importance-sampling samples** used for Eq. (9) for each task (or the heuristic used), and note whether the variance of the estimator was monitored during training.
