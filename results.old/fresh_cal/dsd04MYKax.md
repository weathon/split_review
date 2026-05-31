Now I have all the information needed to verify the claims. Let me synthesize the final review.

---

## Summary

This paper proposes Sum-of-Parts (SOP) models, a class of built-in explainable models that produce grouped feature attributions that are faithful by construction. The paper proves that standard feature attributions incur at least exponential error on simple polynomial functions (Theorems 1-2), motivating the need for grouped attributions. The SOP architecture decomposes a prediction into a weighted sum of group-specific predictions, where each group's score is directly attributable to a sparse subset of features. SOP is evaluated on ImageNet (best insertion AUC and grouped deletion among 8 methods) and demonstrated in a cosmology case study where it produced scientifically meaningful attributions validated by domain experts.

## Strengths

1. **Provable exponential lower bounds for feature-attribution faithfulness (Theorems 1-2, Section 2.1, Figures 2a-2b).** The paper formally proves that any feature attribution on monomials and binomials incurs at least exponential total deletion/insertion error, establishing a fundamental theoretical limitation that prior work did not formally characterize. This is a clean negative result that clearly motivates the need for alternative attribution paradigms.

2. **SOP architecture guarantees faithful grouped attributions by construction (Section 3, Figure 3).** The model decomposes the prediction into a linear sum $\sum_i c_i y_i$ where each group's logit $y_i$ depends only on its masked features $S_i \odot X$ and the group selector uses sparsemax for sparse scoring. Faithfulness is mechanically guaranteed by this design, unlike post-hoc methods or single-rationale approaches.

3. **Strong empirical results on ImageNet (Table 1).** SOP achieves the best insertion AUC (measuring how sufficient top attributions are) and the best grouped deletion among all methods, including GradCAM, SHAP, RISE, IntGrad, LIME, and FRESH. On grouped insertion it is statistically tied with Archipelago. These results directly validate the practical effectiveness of the approach.

4. **Compatibility with any backbone architecture.** The SOP framework wraps a pretrained backbone (ViT for ImageNet, CNN for cosmology) without modifying its weights, demonstrating practical versatility.

5. **Real scientific discovery validated by domain experts (Section 5, Figures 4-5).** The cosmology case study produced novel findings — such as voids carrying more predictive weight than clusters for both $\Omega_m$ and $\sigma_8$, and high-significance clusters contributing more to $\sigma_8$ than $\Omega_m$ — that were confirmed as meaningful by collaborating cosmologists. This goes beyond standard benchmark evaluation to demonstrate real-world utility.

6. **Rigorous formalization of faithfulness tests (Definitions 1-3, Section 2).** The paper provides precise mathematical definitions of deletion error, insertion error, and grouped attributions, enabling both the theoretical analysis and the design of grouped insertion/deletion metrics.

## Weaknesses

### Fatal
None.

### Major

1. **The central theoretical claim about grouped attributions overcoming limitations is asserted without formal support (Section 2.2, Contribution 1).** The paper proves that feature attributions incur exponential error (Theorems 1-2) and then states (line 94) that "Grouped attributions are able to overcome exponentially growing insertion and deletion errors when the features interact with each other." However, no theorem, proof, or synthetic example demonstrates that a grouped attribution achieves low error on *the same monomials and binomials* used in the lower bounds. A concrete demonstration — e.g., a single group $S = \{1,\dots,d\}$ with $c=1$ achieving zero error on the monomial $p(x)=\prod_i x_i$ — would take a few lines and directly bridge the narrative. The empirical results (SOP's strong grouped metrics) *indirectly* support the claim, but the explicit theoretical link between the negative and positive results is missing, making the framing incomplete.

2. **Method description is insufficiently precise for reproduction (Section 3, lines 126-132).** The GroupSelect equation (line 129) uses ambiguous notation:
   $$
   \mathsf{GroupSelect}(z_1,\ldots,z_G) = \mathsf{sparsemax}\left( \frac{W_{q'} C (W_{k'} z)^\top}{\sqrt{h}} \right), C z^\top
   $$
   The comma-separated output is not explicitly defined as a tuple; it is stated that $W_{q'},W_{k'},C \in \mathbb{R}^h$, but the dimensional compatibility of $C z^\top$ with this assumption is unclear, especially since $C$ is described as being "initialized to the weight matrix in the linear classifier" (which would have different dimensions). Training details — loss function, whether the backbone is frozen or fine-tuned, how $G$ is chosen, how sparsity is encouraged beyond sparsemax, end-to-end vs. stagewise training — are absent from the main text. While Algorithm 1 likely exists in the appendix, the main text should provide a self-contained training recipe for a methods paper.

3. **Grouped-attribution evaluation is limited to a single baseline (Section 4, Table 1).** Despite the paper's focus on grouped attributions, only Archipelago is compared on the grouped metrics (grouped insertion/deletion). Other grouped methods mentioned in Related Work — Parallel Local Search (Hase et al., 2021), Integrated Directional Groups (Sikdar et al., 2021) — are not evaluated on grouped tests. FRESH (a single-group built-in method) is only compared on standard metrics and is not adapted for the grouped tests, even though it is a natural grouped-attribution baseline. This narrow comparison weakens the empirical case for the method's core contribution. Additionally, Archipelago appears in Table 1 and results (line 180) without being introduced in Section 4.1's baseline enumeration, and no confidence intervals or variance are reported for any ImageNet results.

### Minor

4. **SOP's standard deletion AUC is low (Section 4.2, Table 1).** SOP achieves one of the lowest deletion AUCs among methods. The paper transparently acknowledges (line 176) that "SOP does not promise that the attributions it selects are comprehensive," but this caveat raises the question of whether important features are missed. The grouped deletion metric (where SOP excels) partially addresses this concern, but additional analysis — e.g., correlating total group score with prediction change when entire groups are removed — would strengthen the faithfulness claim.

5. **Cosmology case study could be more quantitatively validated (Section 5).** The identification of learned groups as "voids" and "clusters" relies on post-hoc thresholding (mean density $\leq 0$ for voids, $\geq +3\sigma$ for clusters) applied after group generation. The paper does not quantify what fraction of learned groups satisfy these thresholds or how well the natural group structure aligns with these physical categories. Comparison against other attribution methods (e.g., LIME, GradCAM) on the same cosmology data would strengthen the claim that SOP yields genuinely novel insights beyond what existing methods could uncover.

6. **No ablation studies on architectural choices.** The paper does not isolate the contribution of the group generator (sparsemax vs. softmax, number of groups $G$) or the group selector. Without this, it is difficult to attribute performance to specific design decisions.

7. **Theoretical lower bounds are computed only for $d \leq 20$ and extrapolated via fitted exponentials (Section 2.1, Figures 2a-2b).** The theorems produce fitted exponential curves for dimensions up to 20, with the claim that they grow exponentially "with respect to the dimension" (line 71). An analytic lower bound for arbitrary $d$ would strengthen the theoretical claim. Additionally, the "total error" measure sums over all $2^d$ subsets in the powerset, which is an extremely strong requirement whose relationship to the standard single-curve AUC metrics used in evaluation is not discussed.

### Trivial

8. **Archipelago omission from Section 4.1.** Archipelago is listed in Table 1 for grouped metrics and discussed in results (line 180) but is not introduced among the baselines in Section 4.1 (lines 155-161).

## Nice-to-Haves

- Provide a concrete synthetic example: a grouped attribution with $G=1$ group $S=\{1,\dots,d\}$, $c=1$ achieves zero deletion error on the monomial $p(x)=\prod_i x_i$. This would directly bridge the theoretical narrative at negligible cost.
- Report confidence intervals or standard deviations for ImageNet metrics across multiple seeds.
- Add an ablation comparing sparsemax to softmax in GroupGen, and varying the number of groups $G$.
- For the cosmology study, report the fraction of learned groups that meet the void/cluster thresholds without post-hoc filtering.

## Removed Points

These points are flagged to be removed; treat them with caution:
- **Criticism about missing Algorithm 1 details in main text (parser-stripped appendix).** The hard rule states that missing appendix content should not be treated as a weakness; Algorithm 1 exists in the original submission.
- **Criticism that the total deletion error summed over the powerset is an "extremely strong requirement."** While technically true, this is a theoretical construct used for provable lower bounds; the empirical evaluation uses standard single-curve AUC metrics, and the relationship is adequately motivated by the need for worst-case analysis.
- **Speculation about FRESH adaptation being "suboptimal" (58.7% accuracy).** The paper states "we adapt for vision" — details are likely in the appendix. The accuracy figure is reported transparently.
- **Request for confidence intervals as a major weakness.** Single-run evaluation on large-scale ImageNet benchmarks is standard practice in this literature; this is a minor point at most.
- **Generic "missing related works" complaint.** Removed per instructions: I cannot verify existence of unmentioned works.
- **Pure formatting/style nitpicks** about figure placement, equation spacing, etc. — these are parser artifacts.
- **Strength Finder's generic strengths** ("the paper addressed an important problem") — removed as superficial.

## Novel Insights

The two input reviews largely converge on the key issues (unclear method description, limited grouped-baseline comparison, and the gap between the theoretical lower bounds and the claim about grouped attributions), but they frame these at different severities. The Harsh Critic correctly identifies that the theoretical narrative is incomplete — the paper motivates grouped attributions via a negative result but provides no formal bridge to the positive claim. However, the Harsh Critic overstates this as undermining the entire contribution; in reality, the SOP architecture and its empirical validation stand on their own merit, and the theoretical gap is fixable with a simple example. An interesting observation not surfaced by either review is that the paper's strongest empirical result (best grouped deletion on ImageNet) is actually the most direct validation of the grouped-attribution claim, yet this connection is not explicitly made in the theoretical sections. The paper would benefit from stating explicitly: "a grouped attribution with one group per monomial term achieves zero error on the monomial example of Theorem 1, and SOP approximates such a decomposition."

## Suggestions

1. **Bridge the theoretical gap.** In Section 2.2, provide a concrete example: for the monomial $p(x)=\prod_i x_i$, a grouped attribution $\beta = \{(\{1,\dots,d\}, 1)\}$ achieves zero total deletion error (since $p(x) = 1 \cdot p(S\odot x)$). For the binomial case, $G=2$ overlapping groups achieve zero insertion error. This takes 3-5 lines and directly justifies the claim.

2. **Clarify the GroupSelect mechanism.** Rewrite Equation (7) to clearly separate the two outputs, e.g.:
   - $c = \mathsf{sparsemax}((W_{q'} C (W_{k'} z)^\top)/\sqrt{h}) \in \mathbb{R}^G$ (scores)
   - $y = C z^\top \in \mathbb{R}^{G \times \text{classes}}$ (partial logits)
   Specify all tensor dimensions explicitly.

3. **Add training details to main text.** State at minimum: (a) the loss function (presumably cross-entropy on the aggregated prediction), (b) whether the backbone is frozen or fine-tuned, (c) how $G$ is chosen, and (d) whether a sparsity regularizer is applied alongside sparsemax.

4. **Expand grouped-attribution evaluation.** Compare SOP against at least one more grouped method (PLS or Integrated Directional Groups) on grouped insertion/deletion. Adapt FRESH for grouped metrics as a single-group special case. Report standard deviations.

5. **Address the deletion AUC concern directly.** Add a simple experiment: compare the total weight of top-k groups with the actual prediction change when those groups are ablated. This would show whether the low standard deletion AUC reflects genuine non-comprehensiveness or a harmless artifact of the aggregation process.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>