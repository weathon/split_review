Now I have all the information needed to produce the final consolidated review.

## Summary

SPARC proposes a rehearsal-free and surrogate-light continual learning approach that combines task-specific depth-wise separable convolutions (working memories) with shared point-wise filters updated via EMA (semantic memory), plus a weight re-normalization technique to mitigate task recency bias. The central claim is that this design achieves competitive or superior Class-IL accuracy while using dramatically fewer parameters than both rehearsal-based methods (e.g., DER++, CLS-ER) and full-model-surrogate approaches — for example, using only 6% of CLS-ER's parameters on Seq-TinyImageNet while outperforming it.

## Strengths

1. **Extreme parameter efficiency without sacrificing performance**: SPARC uses 6% of the parameters required by full-model surrogates on Seq-TinyImageNet (Table 4, Figure 3), yet achieves superior Class-IL accuracy (47.65% vs. CLS-ER's 46.91% with buffer 200, Table 1). On Seq-CIFAR100 (5 tasks), SPARC reaches 63.20% without any replay buffer or EMA model surrogates, matching or exceeding rehearsal-based methods like DER++ (62.40%) and CLS-ER (64.80%).

2. **Scalable parameter growth across task sequences**: Table 4 shows that SPARC grows much more slowly than both rehearsal-based (CLS-ER) and growing-architecture methods (PNN). For 20 tasks on Seq-CIFAR100, SPARC uses 1.8M parameters vs. CLS-ER's 12.9M. This directly supports the claim of memory-constrained deployment.

3. **Effective semantic memory design validated by ablation**: Table 5 shows that sharing half the point-wise filters via EMA achieves near-hard-parameter-isolation performance (59.39% vs. 60.35%) while using 59% fewer parameters. This validates that a small shared component can consolidate cross-task knowledge without full model surrogates.

4. **Better stability-plasticity trade-off**: Using the metric from Section 4.1, Figure 4 shows SPARC achieves substantially higher stability than ER, DER++, CLS-ER, and TAMiL on Seq-CIFAR100 (buffer 500) while maintaining moderate plasticity, providing a direct evaluation of the method's retention vs. new-learning balance.

## Weaknesses

### Fatal
None.

### Major

1. **Inference cost in Class-IL is not adequately characterized.** SPARC processes each test image through *all* k task-specific sub-networks during Class-IL inference (Section 3.4). The paper reports forward/backward passes during training (Table 1, column ℱ) but provides no analysis of inference-time cost — no total MACs per test sample, no comparison of how k-forward-passes-through-small-sub-networks scales vs. single-forward-pass-through-large-network for replay methods. The sub-networks are parameter-efficient, but the reviewer's concern about linear growth in inference cost with k is valid and self-acknowledged in the limitations ("SPARC grows in size... In longer task sequences... SPARC grows way beyond other rehearsal-based and weight regularization counterparts"). For a method marketed as "scalable" and "practical," this blind spot weakens the claim relative to rehearsal-based methods whose inference cost is constant regardless of sequence length.

2. **Weight re-normalization (a stated contribution) is under-validated.** The technique uses a robust upper bound based on IQR and a scaling constant κ=5 (Eq. 5). No sensitivity analysis over κ is provided, no distribution of the normalization constant η across tasks is reported, and no before/after logit magnitudes are shown to verify that the technique actually reduces task-specific bias as claimed. Since this is Contribution 3 in the introduction, the lack of scrutiny leaves it as a plausible heuristic rather than a validated component. The paper conducts careful ablations on width, depth, and semantic memory ratio; the absence of similar attention to this component is a gap.

### Minor

1. **Title / framing tension around "model surrogates."** The title says "beyond... model surrogates" and the paper consistently says "without *full* model surrogates." The EMA-updated shared point-wise filters are technically a lightweight parametric surrogate — not a full model copy, but a surrogate nonetheless. The distinction from CLS-ER (two full EMA models) is one of degree, not kind. This does not undermine the experiments, but the framing would be more precise if it acknowledged this explicitly rather than setting up "surrogate-free" as a binary claim.

2. **EMA coefficient α not stated in the main text.** Figure 4 (right) discusses that "higher value of α leads to a better trade-off" but the actual value used in experiments is never given in the main text. Given its importance to the stability-plasticity trade-off, this should be reported explicitly.

3. **Shared-to-task-specific point-wise filter ratio (50/50) is not ablated.** The paper fixes half the point-wise filters as shared. An ablation varying this ratio (e.g., 25%, 50%, 75%) would clarify whether the chosen split is near-optimal.

4. **Figure 2 reports only Task-IL for the 20-task parameter-isolation comparison.** Since Class-IL is the more challenging and practically relevant setting, showing the Class-IL version would strengthen the comparison.

### Trivial
None.

## Nice-to-Haves

- Include growing-architecture methods (PNN, CPG) explicitly in Table 4's parameter-growth comparison.
- Ablate the shared-to-task-specific filter ratio (25%, 50%, 75%).
- Report the Class-IL version of the 20-task experiment in Figure 2.

## Removed Points

These points were identified in the reviewer inputs but removed per the filtering rules:

- **BN statistics interaction concern** (Harsh Critic's "Other Observations" point 4): The paper clearly states that each sub-network processes images independently with its own BN statistics (Section 3.4: "each image is independently processed through all sub-networks, including their respective batch normalization layers"). No interaction or mismatch occurs — the critic misread the paper.
- **Task-free setting limitation**: Already acknowledged by the authors in Section 5 (Limitations). Not a missing analysis — it is an explicit design choice scoped to the standard benchmark setting.
- **Generic strength from Strength Finder**: Several generic or superficial strengths (e.g., "this paper addressed an important problem") were filtered out.

## Novel Insights

Beyond the paper's own contributions, the review reveals that the paper's strongest evidence is not its absolute accuracy (which is competitive but not uniformly state-of-the-art) but rather its *accuracy-to-parameter ratio*. The ablation in Table 5 is genuinely informative: it shows that the shared EMA point-wise filters capture almost all the benefit of hard parameter isolation at a fraction of the cost, while the all-shared and no-sharing extremes both degrade. This gives concrete architectural guidance for designing parameter-isolation CL systems. The key tension that the paper does not fully resolve, however, is the inference cost vs. parameter-count trade-off: SPARC is excellent for storage-constrained deployment but potentially costly for latency-sensitive inference as k grows.

## Suggestions

1. **Add a table or figure reporting total MACs per test sample** for SPARC (at various k) vs. representative baselines (single forward pass), to directly address the inference-cost concern.
2. **Add a sensitivity sweep over κ** (e.g., 1–10) for at least one benchmark, and show logit magnitudes before/after normalization for a few tasks to validate the weight re-normalization claim.
3. **Explicitly state the EMA coefficient α value** in Section 3.2.
4. **Adjust the framing** to acknowledge that the shared point-wise filters constitute a lightweight parametric surrogate (distinguished from *full* model surrogates), to avoid the appearance of overclaiming.
5. **Ablate the shared-to-task-specific filter ratio** (25%, 50%, 75%) for at least one benchmark.

## Score and Decision

**Overall assessment**: The paper makes a genuine contribution — demonstrating that a carefully designed parameter-isolation approach with cheap DSC layers and a small shared EMA component can match or exceed replay-based methods on standard benchmarks while using a fraction of the parameters. The experiments are thorough across multiple datasets, and the ablations (Table 5, Figure 4) are informative. The two major weaknesses (inference cost uncharacterized, weight re-normalization under-validated) are real but addressable in a moderate revision — neither invalidates the core results. The paper's strengths in parameter efficiency and competitive accuracy are well-supported. Therefore, the paper merits acceptance contingent on addressing the above major concerns, ideally with additional analysis rather than architectural changes.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>