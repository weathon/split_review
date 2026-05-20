Now I have sufficient anchor information. Let me write the final consolidated review.

## Summary

This paper proposes HVOP (Hebbian View Orthogonal Projection), a method for multi-view incremental learning on graphs. The key idea is to use orthogonal gradient projection (approximated via Hebbian learning and recursive lateral connections) to prevent "view forgetting" when views arrive sequentially. The method maintains a Knowledge Transfer Space (KTS) where gradient updates are projected orthogonal to the principal subspace of previous views' representations, implemented through an Oja-rule-based Hebbian update of lateral connection weights R. Experiments on node classification across six multi-view datasets show strong results.

## Strengths

- **Strong empirical performance on multiple benchmarks.** In Table 1, HVOP achieves the best ACC on 4 out of 6 datasets (Animals, Flower17, Iaprtc12, NGs, NoisyMNIST_15000), often by substantial margins (e.g., NGs: 95.19% vs. 90.65% for best static method LGCNFF). The results include standard deviations and multiple metrics (ACC, Precision, Recall, MAFI), providing a reasonably thorough evaluation.

- **Clear problem framing and formalization.** Section 3.1 provides formal definitions of "View Forgetting" (Definition 3.1) and "View Transfer Learning" (Definition 3.2), which clearly distinguish the setting from standard task- and class-incremental learning and provide measurable criteria.

- **Ablation confirms orthogonal projection is essential.** Figure 5 shows that removing the orthogonal projection module ("w/o OP") causes accuracy to fluctuate dramatically (e.g., on YaleB_Extended, dropping from ~85% to ~40% when a new view arrives, versus HVOP staying above ~75%). This provides direct causal evidence that the proposed projection mechanism is responsible for the stability benefit.

- **Biologically-motivated dynamic PCA is a principled idea.** Replacing static SVD with Oja's rule (Eq. 9) to dynamically update the lateral connection matrix R offers a theoretically grounded way to avoid storing all previous view data for SVD recomputation, which is conceptually appealing for incremental settings.

## Weaknesses

### Major

- **The shared weight matrix has an unresolved dimensional inconsistency.** In Equation (1), $\mathbf{X}_v \in \mathbb{R}^{n \times d_v}$ with "distinct dimensionality" $d_v$ per view, and the shared weight matrix $\mathbf{W} \in \mathbb{R}^{d_v \times d}$. If $d_v$ varies across views, a shared $\mathbf{W}$ cannot have a fixed dimension that matches all views simultaneously. The paper never addresses how views with different feature dimensions are reconciled with a single shared weight matrix — whether there is a projection to a common space, or the notation is misleading. This is a fundamental technical ambiguity that undermines the method description.

- **The method is underspecified to the point of being non-reproducible.** Critical algorithmic details are missing: (1) how the lateral connection matrix $\mathbf{R}$ is initialized and updated when a new view arrives (is it trained online during the view's training, or computed once?); (2) how the gradient projection $\mathbf{P}^* = \mathbf{I} - \mathbf{R}^T\mathbf{R}$ is applied to the GCN weights vs. the fully connected layer; (3) how the KTS representation $\mathbf{Q}_v$ is maintained and used across views; (4) what $k$ (number of principal components) is and how it is chosen. The derivation from Eq. 4 (exact SVD-based projection) to Eq. 8 ($\mathbf{I} - \mathbf{R}^T\mathbf{R}$) asserts "a striking similarity" but never shows analytically that $\mathbf{R}^T\mathbf{R}$ approximates $\mathbf{K}\mathbf{K}^T$ when $\mathbf{R}$ is learned via Oja's rule, nor specifies conditions (orthonormality of $\mathbf{R}$ columns) needed for this to hold. Without these details, the claimed contribution cannot be evaluated or built upon.

- **The paper claims "for the first time, as view transfer learning" (Section 5), which overstates novelty.** View incremental learning is a specific instance of online/sequential multi-view learning, and gradient projection for continual learning is well-established (GEM, A-GEM, GPM, OGD). The paper acknowledges Saha et al. (GPM) but does not adequately situate HVOP within this literature or explain what is fundamentally new beyond the Hebbian approximation of PCA.

### Minor

- **The view forgetting analysis in Figure 4 partly weakens the paper's own claims.** On the Animals dataset, HVOP's accuracy on View 1 drops notably after View 2 is learned (from ~4.5 to ~2.5, based on the figure description), recovering only after View 3. The paper states that "HVOP demonstrates a smoother decline, even stabilizing in some instances" — this is better supported on NGs than on Animals. No error bars or standard continual learning metrics (average forgetting, backward transfer) are provided for these bar charts, making the claims qualitative rather than quantitative.

- **The reconstruction loss $\mathcal{L}_{RE}$ stores past adjacency matrices $\mathbf{A}_t$.** The loss is defined as $\mathcal{L}_{RE} = \frac{1}{2} \sum_{t=1}^{|T|} \|\mathbf{A}_t - \sigma(\mathbf{Q}_{|T|} \mathbf{Q}_{|T|}^T)\|_F^2$, which requires storing all previous view adjacency matrices. This partially contradicts the premise of not retaining old data and is not discussed as a trade-off or memory cost.

- **t-SNE visualizations (Figure 3) are presented without quantitative clustering metrics** (e.g., NMI, ARI), reducing them to qualitative illustrations. The "w/o OP" ablation in Figure 5 is described as "removing the orthogonal projection module" without specifying which components are removed (lateral connections? Hebbian learning? both?), which diminishes the informativeness of the ablation.

### Trivial

- Standard deviations are reported in Table 1 but no information is given on the number of independent runs used to compute them.
- The sigmoid application to the Gram matrix $\sigma(\mathbf{Q}_{|T|} \mathbf{Q}_{|T|}^T)$ in the reconstruction loss is notationally unusual and its motivation is not explained.
- No analysis of computational cost (additional memory for KTS, Hebbian update overhead) is provided.

## Nice-to-Haves

- A controlled comparison against exact SVD-based orthogonal projection (e.g., GPM-style) would help demonstrate whether the Hebbian approximation offers any advantage beyond computational convenience.
- Adding standard continual learning metrics (average accuracy, average forgetting, forward/backward transfer) across multiple runs with error bars would substantially strengthen the evaluation.
- Pseudocode for the complete incremental algorithm would significantly improve clarity and reproducibility.
- A discussion of limitations (sensitivity to view order, scenarios where views are not complementary, memory/computation costs) would improve the paper's completeness.

## Removed Points

- **Criticism about unfair comparison with static multi-view methods** — REMOVED. The asymmetry favors the baselines (static methods see all views simultaneously, giving them an information advantage). If anything, this comparison is conservative for the proposed method.
- **Missing related works (GEM, A-GEM, OGD)** — REMOVED per hard rules (do not mention missing related works without external sources).
- **Biological plausibility overstated as a "weakness"** — REMOVED. This is a matter of framing and opinion; the paper clearly states it draws inspiration from neural mechanisms, and the core technique (Hebbian PCA for orthogonal projection) is a legitimate technical contribution regardless of whether one finds the biological framing compelling.
- **"Loss of GCN fluctuates sharply may be due to different learning rate"** — REMOVED as speculative; no evidence supports this claim.
- **"No comparison to gradient-projection continual learning methods"** — REMOVED per hard rules on missing related works.
- **Strength Finder's generic strengths** (e.g., "clear formal framing of the problem" is kept; "biologically motivated dynamic principal-component extraction" is kept as a genuine specific strength). Generic claims about "addressing an important problem" are removed.

## Novel Insights

The primary novel observation that emerges from synthesizing the reviews is that this paper's core technical contribution — using Hebbian learning (Oja's rule) as an online, dynamic alternative to SVD for orthogonal gradient projection in an incremental multi-view setting — is reasonable and potentially valuable, but the paper's presentation undersells it by being vague about implementation, overclaiming on biological framing, and including a dimensional inconsistency in the shared weight matrix that casts doubt on whether the method is even correctly specified. A very similar technical approach appeared concurrently in the SNN continual learning literature (HLOP, accepted at a top venue with avg score 6.5), suggesting the idea has merit but this paper's execution and evaluation do not yet match that bar.

## Suggestions

1. **Clarify the weight-sharing mechanism.** Explain how a single $\mathbf{W}$ handles views with varying feature dimensions $d_v$ — or correct the notation if all views have the same dimension.
2. **Provide pseudocode.** One page of pseudocode showing the view-incremental loop, how $\mathbf{R}$ is updated and applied per view, and where gradient projection occurs would resolve most reproducibility concerns.
3. **Add quantitative forgetting metrics.** Replace or supplement Figure 4 with standard metrics (average forgetting, backward transfer) with error bars across multiple runs.
4. **Tone down overclaims.** Remove "for the first time" framing and acknowledge the connection to GPM-style orthogonal projection more explicitly.
5. **Run a controlled comparison with SVD-based projection** (exact GPM on your architecture) to isolate whether the Hebbian approximation itself provides a benefit.
6. **Specify the ablation clearly.** When describing "w/o OP," state exactly which components are removed (the lateral connection update? the Hebbian learning? the gradient projection step?).

## Score and Decision

**Calibration anchors:**

| Anchor path | Avg Score | Round | Comparison |
|---|---|---|---|
| /home/wg25r/review_agent/human_reviews/WM5G2NWSYC.md | 2.00 | 1 (bracket, <3.5) | Much weaker; unserious submission |
| /home/wg25r/review_agent/human_reviews/HCCkCjClO0.md | 3.00 | 1 (bracket, <3.5) | Comparable in underspecification but weaker results |
| /home/wg25r/review_agent/human_reviews/Pbz4i7B0B4.md | 5.75 | 2 (narrow, 4.0-6.5) | Stronger clarity and evaluation; accepted poster |
| /home/wg25r/review_agent/human_reviews/b2fhCbhe62.md | 5.25 | 2 (narrow, 4.0-6.5) | Comparable contribution level but better specified |
| /home/wg25r/review_agent/human_reviews/hac6DzbMa7.md | 4.50 | 2 (narrow, 4.0-6.5) | Similar method clarity issues; rejected |
| /home/wg25r/review_agent/human_reviews/Xi7UoErFRt.md | 5.00 | 2 (narrow, 4.5-7.0) | Better specified method; rejected but close to threshold |
| /home/wg25r/review_agent/human_reviews/MeB86edZ1P.md | 6.50 | 2 (narrow, 4.5-7.0) | **Closest technical match** (same core idea); accepted poster with much better clarity and evaluation |
| /home/wg25r/review_agent/human_reviews/gc8QAQfXv6.md | 9.00 | 1 (bracket, >7.5) | Far stronger; oral-level work |

**Round 1 bracket:** 3.5–7.5 (the paper is clearly better than the weakest anchors and clearly worse than the strongest ones).

**Round 2 narrowing:** The closest technical anchor (MeB86edZ1P, same Hebbian+orthogonal projection idea, avg 6.5, accepted) is substantially clearer, better evaluated, and does not have the dimensional inconsistency present here. The hac6DzbMa7 anchor (avg 4.5, rejected for method clarity issues) is the closest comparator in terms of overall quality. This paper sits between the two — the empirical results are stronger than hac6DzbMa7, but the method specification is significantly weaker than MeB86edZ1P.

**Final score: 4.5** — below the acceptance threshold for a top venue. The paper tackles an interesting problem and shows promising empirical results, but the underspecified method, unresolved dimensional inconsistency in the shared weight matrix, and overclaims relative to existing work prevent acceptance in its current form.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>