- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 5
Now I have all the information I need. Let me carefully construct the final review.

---

## Summary

This paper proposes Stochastic Positional embeddings (StoP) for Masked Image Modeling (MIM). The core idea is to add Gaussian noise to the positional embeddings of masked tokens, forcing the model to learn representations robust to location uncertainty. The paper builds on I-JEPA and shows consistent improvements across image classification, dense prediction, counting, and depth ordering tasks. The method introduces a shared projection matrix A that serves a dual role — projecting both the noise for masked tokens and the encoder features for context tokens — which naturally prevents the degenerate solution of scaling the noise to zero.

## Strengths

- **Consistent and substantial performance gains across architectures and tasks**: Tables 1–5 report improvements on linear probing (e.g., +2.5% for ViT-H with 1% data on IN-1k), full fine-tuning (+2.3% for ViT-L), dense prediction (+2.5% J&F on DAVIS 2017 with ViT-L), and transfer tasks (+3.3% on iNAT18). The gains are directionally consistent across all evaluated settings, which is strong empirical evidence for the method's effectiveness.

- **Theoretically motivated design with a clear interpretation**: Proposition 1 (Section 3.3) shows that under Gaussian positional noise, the optimal predictor performs a spatial smoothing (convolution of the clean expected values with a Gaussian). This provides a principled link between the proposed stochastic positions and the learned representations' robustness to location uncertainty.

- **Clever regularization mechanism to prevent degenerate solutions**: The dual role of matrix A (Section 3.2) — simultaneously projecting context features for context tokens and noise for masked tokens — is elegant. Section 4.3 verifies that increasing σ reduces the norm of A, confirming the mechanism works as designed. The L1 regularization ablation (+1.5%) vs. full StoP (+3.5%) further shows that the gains go beyond simple regularization.

- **Practical simplicity**: The implementation change is minimal (Algorithm 1), with no additional runtime or memory overhead, making it easily adoptable.

## Weaknesses

### Fatal
None.

### Major

- **The causal mechanism is not fully isolated**: The paper's central claim is that *stochasticity in positional embeddings* drives the improvement. However, the method introduces two simultaneous changes relative to I-JEPA: (1) stochastic noise on masked token positions, and (2) a data-dependent additive term A s_{x_i} on context token positional embeddings. The paper does not include an ablation that removes the noise on masked tokens while keeping the context projection term A s_{x_i} (i.e., deterministic positions for both context and masked tokens, with the same architecture but no noise). The existing L1 regularization ablation partially addresses this by showing that full StoP (+3.5%) outperforms deterministic positions + L1 regularization (+1.5%), suggesting a ~2% gain from the noise component. However, this does not fully resolve the concern because the L1 regularizer changes how A operates, and the cleanest control would be the same architecture with deterministic positions for both token types. Without this ablation, the paper's attribution of the gains specifically to *location uncertainty* (rather than to the broader design change) is supported but not airtight.

### Minor

- **No variance or multi-seed reporting**: All results appear to be from single runs. For linear probing where results typically vary by 0.2–0.5% across seeds, this is notable — especially for the +0.1% gain on depth ordering (Table 4) and smaller improvements. While the main gains (2–3%) are likely robust, the absence of variance estimates weakens the statistical evidence.

- **Cross-method comparisons are not controlled**: Table 2 compares StoP to published results from MAE, iBOT, etc. under different training recipes. The paper acknowledges this ("past published performance"), but still uses the table to demonstrate competitiveness. This is a mild over-claim, though the paper's primary comparison (StoP vs. I-JEPA under identical conditions) is properly controlled.

- **No discussion of potential downsides under exact spatial reasoning**: The paper evaluates tasks where StoP helps, but does not discuss tasks that require precise spatial localization (e.g., keypoint detection, small object detection). Adding noise to positions could plausibly harm performance on such tasks, and an honest discussion of this trade-off is missing. The Limitations section (Section 5) focuses on MAE incompatibility and invariance-based methods still outperforming MIM, but does not acknowledge this potential limitation.

### Trivial
None.

## Nice-to-Haves

- An ablation that **removes the A s_{x_i} term from context tokens entirely** (reverting to ψ_i) while keeping noise on masked tokens would help determine whether the context projection contributes to the gains independently. Conversely, an ablation that **removes noise on masked tokens but keeps A s_{x_i} on context tokens** (deterministic positions for both) would more cleanly isolate the stochasticity effect. Either would address the main mechanistic ambiguity.
- Reporting results with at least 3 random seeds for the key comparison (Table 1) would strengthen the statistical evidence.

## Removed Points

- *Criticism about notation clarity (d_p, d_e dimensions unclear)*: The paper defines ψ_i ∈ ℝ^{d_p} (positional embedding dimension) and s_{x_i} ∈ ℝ^{d_e} (encoder output dimension), with A ∈ ℝ^{d_p × d_e}. This is sufficiently clear for the intended audience. **Removed** — notation is standard and unambiguous in context.
- *Claim that Proposition 1 is "tangential" and "a general fact about Bayes estimators"*: The proposition provides theoretical motivation directly connecting the method to spatial smoothing, which is of value to readers. Whether it belongs in the main text or appendix is a formatting preference, not a methodological weakness. **Removed** — reasonable to include; not a weakness.
- *Claim that the paper's identification of location uncertainty as a problem is "intuitively compelling" but the paper "does not later compare seriously" to invariance-based methods*: The paper explicitly acknowledges that invariance-based methods still perform better (Limitations section), and its stated scope is improving MIM, not beating all self-supervised methods. **Removed** — scope creep; the paper delivers on its stated goal.
- *"The 3-line-code claim is somewhat oversimplified"*: The core change (adding noise to masked token positions) is indeed simple, and Algorithm 1 verifies this. The dual-role A is part of the design but doesn't add implementation complexity beyond what's shown. **Removed** — the claim is accurate for the actual code change.

## Novel Insights

None beyond the paper's own contributions. The harsh critic raises a valid confound concern (stochasticity vs. context projection) that is partially addressed by the paper's existing L1 ablation but would benefit from a cleaner separation. This observation — that the current experimental design conflates two mechanisms — is useful but does not produce a novel insight beyond what a careful reader would infer from reading the paper.

## Suggestions

1. **Run the missing ablation**: Train a variant where the architecture is identical (including A s_{x_i} on context tokens) but masked token positions are deterministic (set n_j = 0). Compare to full StoP. This would cleanly isolate the contribution of stochasticity.
2. **Report multi-seed results**: At least 3 seeds for the main linear probing comparison (Table 1) to establish statistical significance.
3. **Add a limitations discussion** about tasks requiring precise spatial localization, where adding positional noise could harm performance.
4. **Reframe the L1 ablation more precisely**: The current text says "simply regularizing the predictor projection layer leads to 1.5% improvement." Clarifying that this variant still uses A s_{x_i} for context tokens would help readers understand what exactly the ablation controls for.
