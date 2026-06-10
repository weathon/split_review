Here is my final synthesized review.

---

## Summary

This paper presents the first systematic empirical study of normalization strategies (type, position relative to SSM, and combinations thereof) within the Mamba architecture, covering 5 normalization methods across two tasks: long-sequence modeling (Breakfast dataset) and image classification (ImageNet-100). It finds that applying normalization after the SSM module consistently outperforms pre-SSM normalization, and that certain cross-type combinations (e.g., IN→SSM→LN) can yield additional gains. The authors propose an L2-norm-based analysis to explain these effects and validate recommended configurations on LRA ListOps and ImageNet-1k.

## Strengths

- **Systematic ablation across a large design space**: The paper runs a controlled sweep over 5 normalization types × 2 positions × 25 combinations in two distinct task domains (Tables 1–4), going significantly beyond prior ad-hoc choices in the Mamba literature (documented in Section 2). This provides concrete, traceable evidence for its recommendations.

- **L2-norm-based insight into why post-SSM normalization helps**: Figure 4 shows that without normalization or with only pre-SSM BN, deeper Mamba layers develop much larger and more polarized L2 weight norms; applying post-SSM normalization (None→BN or BN→BN) makes the L2 norms nearly uniform across layers. This provides a mechanistic explanation, rooted in scale invariance, for the consistent advantage of after-SSM normalization reported in Tables 2–3.

- **Discovery of "harmonic" cross-type combinations**: The paper identifies a specific case (BN before SSM + IN after SSM on ListOps) where the combined configuration's L2 weight norm lies between those of the individual normalizations, yielding a ~10% performance improvement over either alone (Figure 5). This goes beyond "more normalization is better" and points to a non-trivial interaction.

- **Validation on standard benchmarks**: The recommended configurations are tested on LRA ListOps and ImageNet-1k (Table 5), showing improvement over original Mamba/VMamba defaults (e.g., 82.5% → 83.1% on ImageNet-1k). This demonstrates transfer beyond the main experimental datasets.

- **Actionable task-specific recommendations**: The paper distills concrete guidelines (e.g., "GN after SSM for sequence modeling," "LN as a versatile default") that are directly traceable to specific entries in Tables 1–4.

## Weaknesses

### Fatal

None.

### Major

1. **No statistical reporting in any experiment**. Every result in Tables 1–5 is a single accuracy number with no standard deviations, confidence intervals, or indication of multiple seeds. For an empirical study whose contribution is comparative — claiming "combination X outperforms Y" — this is a significant gap. While the largest differences (e.g., 20.5% vs 70.1% for GN before vs. after SSM) are clear, many comparisons in Table 4 involve gaps under 1% (e.g., 72.5% vs 72.2% on sequence, 87.3% vs 86.8% on vision). Without variance estimates, the reader cannot distinguish systematic improvements from noise. This directly limits the strength of the paper's more granular recommendations.

2. **Missing training and architectural details needed for reproducibility**. The paper does not specify: number of Mamba layers used in the main experiments (only "4-layer" for the L2 norm analysis on ListOps, line 216), hidden dimension size, state dimension (H), optimizer, learning rate schedule, batch size, training epochs, weight decay, gradient clipping, or hardware. A grep for "seed," "epoch," "learning rate," "batch size," "optimizer," and "hyperparameter" returns no matches. Since normalization behavior interacts with model depth, width, and training dynamics, these omissions prevent reproduction and limit confidence that the findings generalize beyond the undisclosed configuration.

### Minor

3. **Main experimental grid uses non-standard datasets**. The sequence modeling experiments use only the Breakfast dataset (an action segmentation dataset with ~1,700 videos, not a standard SSM/Mamba benchmark), and the vision experiments use ImageNet-100 (a 100-class subset). The standard in the SSM literature is the Long Range Arena (LRA) benchmark, which is only used in the validation section (Section 4.5) for the recommended configurations, not for the main comparative grid. This narrow base weakens the generality of the paper's recommendations. The paper acknowledges that "optimal combinations differ between tasks" but then offers general recommendations, creating a tension that is not fully resolved.

4. **"Harmonic structure" analysis is a single case study, not a general framework**. The harmonic balancing effect is illustrated with one example (BN→SSM→IN on ListOps, Figure 5). No formal definition of "harmonic" is given, no metric quantifies it, and the paper does not demonstrate that this phenomenon generalizes to other successful combinations (e.g., IN→SSM→LN, RMSN→SSM→BN). The paper itself states that this "is not intended as an essential explanation" (line 214), but this undercuts the claimed contribution of providing "intuition for harmonizing normalization strategies" (line 22).

5. **Section 4.2 ("Impact of Different Normalization Types") confounds type with position**. This section reports results for configurations like BN→SSM→BN, GN→SSM→GN, LN→SSM→LN — i.e., the same normalization at *both* positions. This is a study of a specific symmetric configuration, not of normalization type in isolation. A proper study of "type" would fix positions and vary types (as Section 4.3 does correctly). The headline numbers from Table 1 (e.g., GN→SSM→GN at 68.8%) are cited as evidence about GN being a good type, but the design conflates type with the decision to normalize at both positions.

6. **N1 affects both the SSM branch and the parallel gating branch — an unacknowledged confound**. As described in Section 3.1 (lines 51–61), N1 normalizes the input that feeds *both* the SSM pathway *and* the parallel gating pathway. When the paper compares "normalization before SSM" vs. "after SSM," the before-SSM condition also changes gating behavior. This confound is never discussed and could affect the interpretation of why pre-SSM normalization sometimes underperforms post-SSM normalization.

7. **Validation gains are modest and task-dependent**. The ImageNet-1k improvement is 0.6% (82.5%→83.1%), and the recommended configurations differ entirely between tasks (IN→SSM→IN for sequence vs. RMSN→SSM→BN for vision). This means the validation does not confirm a single consistent principle but rather that task-specific tuning helps modestly, which is a weaker finding.

### Trivial

- The L2 norm figures (Figures 4, 5) are described as having "purple points" but appear to be grayscale in the printed version; the paper could benefit from clearer visual differentiation of layers.

## Nice-to-Haves

- **L2 norm plots for more combinations**: Showing L2 norm behavior for at least 3–4 successful and unsuccessful combinations (not just BN/IN) would turn the "harmonic structure" observation into a more general analytical tool.
- **Ablation controlling for the parallel branch**: Applying normalization only to the SSM input (not the gating path) would isolate whether the observed pre-SSM effects are due to SSM conditioning or gating interference.
- **Extended task coverage**: Running the main grid on at least one standard long-sequence benchmark (e.g., LRA subset) would substantially strengthen the generality claims.

## Removed Points

*The following points from the inputs were removed for the reasons stated:*

- **Criticism about Section 2 "No Normalization" category (Harsh Critic):** Speculates that cited models "may use normalization internally in less obvious places." This is a hypothetical concern not verifiable from the paper, not a concrete weakness. *Removed per rule: remove strawman/factually unsupported criticisms.*
- **Criticism about Conclusions extending to Mamba2 (Harsh Critic):** The paper states this as future work ("future research will focus on extending"), not a claimed contribution. Criticizing absence of evidence for something explicitly scoped as future work is scope creep. *Removed per scope-creep rule.*
- **Several generic strength entries from Strength Finder** (e.g., "addressed an important problem," "useful contribution"): These lack specific content anchored to the paper's evidence. *Removed per rule: drop generic strengths.*
- **Strength about "Actionable recommendations" as a core strength:** Retained in filtered form above; the original framing was slightly overclaimed but the recommendations are traceable to table entries, so kept in modified form.

## Novel Insights

The most distinctive observation across the reviews is that the paper's two claimed contributions pull in opposite directions: the *large-gap findings* (post-SSM > pre-SSM) are robust and supported by the L2 norm analysis, but they are also relatively unsurprising (normalizing after computation helps). The *fine-grained findings* (which specific combination is best) are where the novelty lies, yet they are precisely the claims that the methodological weaknesses (no error bars, single dataset per task, thin harmonic analysis) fail to support. This asymmetry — strong high-level findings that are unsurprising, and specific novel claims that are under-evidenced — is the central tension in evaluating this paper. Addressing the methodological gaps would disproportionately strengthen the most interesting parts of the work.

## Suggestions

1. **Run all main experiments with at least 5 random seeds and report mean ± std in every table.** This is the single most important improvement. Without it, the comparative claims are not empirically grounded.
2. **Add a reproducibility appendix** with full training configurations: number of layers, hidden dimensions, state size H, optimizer, learning rate schedule, batch size, epochs, weight decay, gradient clipping, and compute hardware.
3. **Run the main normalization grid on at least one standard long-range benchmark** (e.g., LRA ListOps or Text) to establish that patterns are not specific to Breakfast's action-segmentation structure.
4. **Disentangle Section 4.2**: First study normalization type at a single position (either before or after SSM, with the other position fixed to None), then study combinations. This would resolve the type/combination conflation.
5. **Expand the harmonic structure analysis** to show L2 norm plots and quantitative balance measures for at least 3–4 successful and unsuccessful combinations, providing a more general account.

## Score and Decision

**Score**: 5.0  
**Decision**: Reject

The paper addresses a worthwhile question and produces a useful first mapping of normalization configurations in Mamba. The core finding (post-SSM normalization is generally beneficial) is supported by large performance gaps and an L2 norm analysis. However, the paper falls short of ICLR standards for an empirical study: the complete absence of statistical reporting (no variance estimates anywhere), the missing training details that prevent reproducibility, and the thinness of the "harmonic structure" analysis relative to the claims made about it, collectively prevent the paper from being a convincing, self-contained contribution in its current form. A substantially revised version addressing the methodological gaps could be a solid empirical paper.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>