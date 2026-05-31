Now I have a complete picture of the paper. Let me compose the final consolidated review by carefully cross-checking every claim from both reviewers against the paper text.

## Summary

This paper formally defines "knowledge conflict" in multi-task model merging (Definition 1) as the change in task-specific loss when another task's vector is included. Through Taylor expansion analysis at the pre-trained model, the authors show that task vector components orthogonal to the loss gradient cause minimal interference, while both positively and negatively aligned components can increase loss. Based on this insight, they propose TATR: a trust region defined over parameter dimensions where the cumulative absolute product of gradients and task vectors is small, restricting merging to these conflict-safe dimensions. TATR is training-free, data-efficient (working with as few as 1–16 exemplars), and serves as a plug-and-play module for existing TA-based methods (Task Arithmetic, Ties-Merging, AdaMerging, Surgery). Experiments on 8 datasets with CLIP ViT-B/32 and ViT-L/14 show consistent improvements across all baselines.

## Strengths

1. **Formal definition and clear framing of knowledge conflict (Definition 1, Section 4):** The paper introduces an operationally precise definition distinguishing knowledge conflict in static model merging from negative transfer in dynamic multi-task training. This provides a concrete target for mitigation and a vocabulary for future work in the area.

2. **Genuinely insightful analysis of task vector components (Section 4, Figure 2):** The decomposition of task vectors into positive, negative, and orthogonal components relative to the gradient at θ_pre, paired with loss-landscape visualization, is the paper's strongest contribution. The finding that even gradient-descent-aligned components cause harm (contrary to intuition) is non-trivial and well-explained via Taylor expansion breakdown at large task-vector magnitudes. This analysis cleanly motivates the trust-region design.

3. **Data efficiency and plug-and-play generality (Section 5, 6.2):** TATR works with remarkably few exemplar samples (1-shot achieves 72.3% vs 72.8% peak with 16 samples, per Figure 3a). The method consistently improves *all* tested TA-based methods (TA, Ties-Merging, AdaMerging, AdaMerging++, Surgery) on both ViT-B/32 and ViT-L/14, demonstrating broad compatibility.

4. **Layer-wise sensitivity diagnosis (Section 6.4, Figure 4):** The analysis showing shallow layers and bias parameters are most sensitive to knowledge conflict, while digit datasets (SVHN, MNIST) exhibit lower sensitivity, goes beyond average performance to explain *where* conflicts arise. This provides actionable guidance for future merging strategies.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core analytical contribution is sound and its method is well-motivated. The weaknesses below are real but manageable.

### Minor

- **Improvements on ViT-L/14 are modest, especially on strong baselines (Section 6.2):** The gains shrink from +3.7% on ViT-B/32 to +0.8% on ViT-L/14 for plain TA, and from +1.1% (AdaMerging++ on B/32, as reported) to +0.2% on L/14. On the strongest baseline (AdaMerging++, L/14: 91.3→91.5), the gain is marginal. This does not invalidate the method—consistent improvement across 8 methods is still meaningful—but it tempers the practical significance claim, especially since computing gradients on a ViT-L/14 for 8 tasks incurs non-trivial cost.

- **The paper defines a formal conflict metric C (Definition 1) but never directly measures it:** The central narrative is that TATR "navigates knowledge conflicts," and C provides a direct, quantitative measure of conflict. The experiments instead only report accuracy. Computing C for TA vs. TA+TATR (or a subset of task pairs) would directly substantiate the core claim. The accuracy gains are *evidence* of conflict reduction but the gap between the defined metric and the reported metric weakens the causal narrative.

- **Hyperparameter τ tuning protocol is not fully specified (Section 6.1):** The paper states τ is tuned over {0.1%, 0.2%, 0.5%, 1.0%, 2.0%, 5.0%} but does not state whether this tuning uses a held-out validation split or reports test-set results for the chosen τ. This is a transparency concern, though consistent with reporting conventions in this field. A sensitivity plot across τ values (average accuracy vs. τ) would clarify stability.

- **No discussion of limitations or failure modes:** The paper does not discuss when TATR might underperform—e.g., when the gradient at θ_pre poorly approximates the loss landscape because fine-tuned models are far from θ_pre, or when tasks share very similar domains (where the orthogonality assumption may be less useful). A limitations paragraph would strengthen the paper.

- **The "near-zero" threshold in the decomposition (Section 4) is not operationalized:** The analysis uses "≈ 0" to define the orthogonal component (line 114). This is fine for exposition, but a reader might wonder how this threshold relates to the actual trust-region selection in practice (which uses the ranking-based τ). Not a flaw in the method, but a small gap in the exposition.

### Trivial

- The zero-shot variant using |Δ_k| as a gradient proxy (Equation 7) lacks any analysis of when this approximation is reliable vs. unreliable. The paper acknowledges estimation errors but provides no diagnostic.

## Nice-to-Haves

- **Directly compute the knowledge conflict metric C** (Definition 1) for TA and TA+TATR on a subset of task pairs, showing measurable reduction. This would close the gap between the formal definition and the experimental evidence.
- **Add a baseline that prunes task vector dimensions by magnitude alone** (analogous to Ties-Merging's trim step but on all dimensions), to isolate the benefit of using gradient information over simple magnitude-based filtering.
- **A sensitivity plot for τ** showing average accuracy vs. the proportion of kept dimensions per dataset, so readers can assess stability.
- **Benchmark the computational overhead** of computing gradients for 8 tasks on ViT-L/14 and acknowledge the cost relative to the "training-free" label (which describes no iterative training, but still requires a one-time backward pass per task).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The connection to the orthogonal component is indirect"** — The trust region (Definition 2) uses the absolute product |∇L_j[n] · Δ_i[n]|, which directly measures deviation from orthogonality. When this product is small, the vectors are approximately orthogonal by construction. The connection is direct, not indirect. Removed as factually inaccurate.
- **Criticism about tables being "not visible"** — This is a parser artifact from the PDF extraction; the original submission contains the tables. Removed as a parsing issue.
- **"The method is sensitive to τ because values are very small"** — The chosen τ values span a 50× range (0.1%–5.0%), which is a reasonable search range. The critic infers sensitivity from the values being "small" without evidence; the paper simply lists the candidate values. Removed as speculative.
- **Strength Finder claim about "automatically avoids manual tuning"** — τ itself is a tuned hyperparameter. The method avoids manually setting ε, but τ still requires selection. This claim is slightly overblown; moved here rather than kept as a strength.

## Novel Insights

None beyond the paper's own contributions. The key insight (orthogonal components are safe; gradient-aligned components cause harm in both directions due to Taylor approximation breakdown) is the paper's own intellectual contribution. The reviews do not surface a genuinely novel observation beyond what the paper already provides.

## Suggestions

1. Directly compute the conflict metric C (Definition 1) for a subset of task pairs comparing TA vs. TA+TATR. This is the single highest-leverage addition to validate the core claim.
2. Add a sensitivity plot of average accuracy vs. τ, and clearly state whether τ was selected on a validation set.
3. Include a brief limitations paragraph discussing when gradient-based trust regions may fail (e.g., when fine-tuned models are far from θ_pre or when tasks share high domain similarity).

## Score and Decision

**Score:** 7.0  
**Decision:** Accept

**Rationale:** The paper makes a genuine analytical contribution (decomposition of task vectors into gradient-aligned vs. orthogonal components, with the counter-intuitive finding that negative-gradient-aligned components also harm performance) that advances understanding of why and when task arithmetic conflicts arise. The TATR method is clean, well-motivated by this analysis, data-efficient, and broadly compatible with existing approaches. The weaknesses—modest gains on the larger model, lack of direct C measurement, unspecified τ tuning protocol—are real but do not undermine the paper's core contributions. With the suggested additions (direct C measurement and τ sensitivity analysis), the paper would be materially stronger.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>