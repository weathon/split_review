- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5
Now I have a thorough understanding of the paper and the reviews. Let me write the final consolidated review.

## Summary

This paper proposes Di-SkilL, a method for learning diverse skills in contextual episodic policy search (CEPS) using a mixture of deep experts with energy-based per-expert context distributions. The approach enables automatic curriculum learning where each expert focuses on context sub-regions it favors, while the EBM parameterization avoids needing hand-tuned penalty terms for context bounds. Experiments on simulated robotic tasks (reacher, table tennis, box pushing, minigolf) show Di-SkilL outperforms single-mode (BBRL) and linear-MoE (SVSL) baselines.

## Strengths

1. **EBM-based per-expert context distribution enables multi-modal, bounded curriculum without prior knowledge of context bounds** (Section 3.2, Eq. 8). By modeling π(c|o) as an EBM and approximating the normalizing constant over batches from p(c), the method naturally respects valid context regions while representing sharp discontinuities and multi-modality — eliminating the hand-tuned penalty term required by prior work (Celik et al., 2022).

2. **Trust-region updates stabilize the bi-level MoE optimization** (Section 3.3, Eq. 9). Both the expert networks and per-expert context distributions are constrained to change slowly across iterations, which is critical since the contexts sampled for one expert depend on its own changing π(c|o). This enables stable training of deep (non-linear) experts, whereas prior work was limited to linear experts.

3. **Ablation demonstrates automatic curriculum learning is empirically necessary** (Section 4.1, Fig. 3b). Disabling the curriculum by flattening π(c|o) to uniform (Di-SkilLwoCurV1/V2) causes success rate on table tennis to fall well below Di-SkilL, even with 5.2× more samples per expert. This cleanly isolates the contribution of the per-expert context distribution.

4. **Outperforms single-mode baselines on tasks requiring multi-modal behavior** (Section 4.2, Fig. 4). Di-SkilL achieves ~85% success on box pushing (vs. ~65% for BBRL) and ~70% on minigolf (vs. ~50%), on tasks where an obstacle introduces genuine multi-modality. Figure 5 provides qualitative visualization of diverse box trajectories.

5. **Scales to higher-dimensional context spaces** (Section 4.2, Fig. 4a). The extended table tennis task uses 5 context dimensions (vs. 2D in prior CEPS MoE work), and Di-SkilL achieves competitive or better final performance than BBRL.

## Weaknesses

### Fatal

None.

### Major

1. **No quantitative diversity metric is reported, despite diversity being the paper's central framing.** The title, abstract, introduction, and conclusion all emphasize learning "diverse skills" and "multi-modal behavior," yet the experiments evaluate only task performance (success rate, return). Figure 5 provides one qualitative example of varied box trajectories, but no direct measure of diversity is computed — not entropy of the expert assignment distribution π(o|c), not the number of distinct strategies per context, not pairwise trajectory dissimilarity, not effective skill-mode count. The outperformance of single-mode baselines on tasks with multi-modal solutions is *consistent with* diversity but does not constitute evidence for it: a well-tuned multi-modal policy could collapse to a single effective skill per context while still outperforming a unimodal policy through better function approximation. The paper either needs to quantitatively measure diversity (e.g., conditional entropy H(o|c) over contexts, clustering of rollout parameters) or revise its framing to match what is actually demonstrated (a high-performing deep MoE method with automatic curriculum).

### Minor

2. **Derivation of the per-expert context update objective (Eq. 10) is underspecified.** The paper states that Eq. 10 follows from Eq. 7 because "many terms can be calculated in closed form" and that the full derivation is in Celik et al. (2022). However, the term `log∑_o ṽ(o|c)` appearing in Eq. 10 does not obviously correspond to anything in Eq. 7, and the intermediate algebraic steps are not shown. Given that the EBM parameterization and its tractable optimization are core contributions, the paper would benefit from a self-contained derivation connecting Eq. 7 to Eq. 10, including the treatment of the log-partition function and the closed-form terms.

3. **EBM sampling procedure's reliance on a finite batch from p(c) is under-discussed.** The method does not generate novel context samples from the learned EBM — it reweights a finite batch drawn from p(c) each iteration (Section 3.2). The paper acknowledges this ("by resampling a large enough batch... the EBM will encounter important parts of the context space") but does not discuss the regime (batch size, context dimensionality) in which this approximation is reliable or provide a sensitivity analysis. In higher-dimensional contexts (e.g., 5D), the batch size needed for adequate coverage could be prohibitive.

4. **Ablation study is conducted on only one environment (table tennis).** The claim that "automatic curriculum learning is a necessary feature for Di-SkilL to solve the task" (Section 4.1) is supported for one environment. Demonstrating the same pattern on at least one additional environment (e.g., box pushing or minigolf) would strengthen the generality of this finding.

5. **Reacher task performance comparison is not statistically clear.** The paper states (Section 4.2) "Di-SkilL converges a bit slower than BBRL, but eventually achieves a higher return." The reported IQM with 95% confidence intervals (Fig. 3c) shows overlapping intervals for most of training; whether the final separation is significant is not testable from the figure as shown. The authors should report final performance with confidence intervals or a significance test.

6. **Hyperparameters α, β, and the trust-region KL bounds are not ablated or justified.** Given that α controls the diversity-entropy trade-off and β controls the curriculum-KL trade-off, their settings (α=0.5, β=0.5 for Di-SkilL, β=2000 for the ablation) are likely critical to performance but receive no sensitivity analysis.

### Trivial

None.

## Nice-to-Haves

- **Comparison to a non-EBM curriculum baseline**: The paper compares Di-SkilL to no-curriculum variants (Di-SkilLwoCur) and to LinDi-SkilL (linear experts + EBM). A baseline using a fixed (e.g., Gaussian) per-expert context distribution with a penalty term (similar to Celik et al., 2022 but with deep experts) would isolate the benefit of the EBM over Gaussian curriculum learning while controlling for expert architecture.
- **Computational cost discussion**: The method requires a forward pass through all experts for all context samples in the batch to compute EBM probabilities. A brief discussion of this cost and how it scales with batch size and number of experts would aid practitioners.
- **Batch size sensitivity analysis**: Since the EBM's ability to represent the per-expert context distribution depends on batch size, showing performance vs. batch size would validate the approach and provide practical guidance.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Trust-region updates to restrict the change of both distributions"**: The critic notes that the paper uses trust-region layers for the expert but only PPO for the context distribution, calling this a gap. However, the paper explicitly addresses this: Section 3.3 states "We can not apply the trust region layers... as π(c|o) is a discrete distribution... Yet, we can still use PPO." PPO with clipping is a trust-region method; the paper provides a justification for using a different mechanism. This is not a genuine weakness.

- **"Claimed advantage against unknown bounds is asserted but not validated"**: The paper motivates the EBM approach by noting that Gaussian curricula require known context bounds. While the paper does not run an experiment where bounds are unknown, the environments used have well-defined p(c), and the EBM naturally respects these bounds without needing a penalty term — this is a structural advantage of the method that holds regardless of whether an explicit "unknown bounds" scenario is tested.

- **"No comparison to discrete MoE with fixed curriculum"**: The paper includes an ablation (Di-SkilLwoCur) that disables curriculum learning entirely, as well as comparing to SVSL (linear MoE with Gaussian curriculum). The critic's suggestion of a fixed Gaussian context curriculum with deep experts is a reasonable extension but not a missing critical baseline — the ablation already shows that removing curriculum hurts, and the comparison to SVSL shows the EBM's advantage over Gaussian curricula in the linear case.

- **Several presentation nits about appendix, typos, etc.**: Removed per hard rules — the paper's PDF is complete; missing appendix content is a parser artifact.

## Novel Insights

None beyond the paper's own contributions. The reviewer analyses surface a genuine framing-evidence gap (diversity claimed but not measured) and several expositional shortcomings, but do not reveal novel connections or insights about the method that the paper itself does not articulate.

## Suggestions

1. **Add quantitative diversity metrics** to the experimental section. For each task, compute and report: (i) conditional entropy of expert assignment H(o|c) averaged over test contexts — high entropy confirms multiple experts are used for the same context; (ii) pairwise KL divergence between expert parameter distributions π(θ|c, o₁) and π(θ|c, o₂); (iii) number of distinct trajectory clusters per context (measured via clustering rollout parameters). This directly supports the paper's central claim.

2. **Provide a self-contained derivation** from Eq. 7 to Eq. 10 so the reader can verify the tractable PPO-style objective without reading Celik et al. (2022). Show the expansion of the expectation and entropy terms, and explain how the closed-form terms in Eq. 10 arise.

3. **Include a batch-size sensitivity analysis** for the EBM sampling procedure, showing performance vs. batch size (e.g., on the box-pushing task) to validate the finite-batch approximation and give practical guidance.

4. **Extend the ablation study** to at least one additional environment (e.g., box pushing) to confirm the necessity of automatic curriculum learning is not environment-specific.

5. **Report final numerical performance** with confidence intervals for all comparisons, and clearly state when differences are or are not statistically significant (e.g., for the reacher task where Fig. 3c shows overlapping intervals).
