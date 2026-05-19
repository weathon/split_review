- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 5, 8, 5, 6
Now I have a thorough understanding of the paper and all reviewer claims. Let me write the consolidated review.

## Summary

This paper tackles partial graph matching by distinguishing between two causes of missing correspondences: point occlusion (handled via a learned structured universe graph with both node and edge embeddings) and annotation errors (handled via energy-based OOD detection that filters outliers before matching). The method is evaluated on Pascal VOC and Willow Object datasets across occlusion and random-outlier settings, consistently outperforming prior approaches.

## Strengths

- **Structured universe graph (nodes + edges) provides clear benefits over universe-point-only representations.** The ablation (Table 4) shows that removing edge learning drops F1 substantially (reported as 65.1 → 58.1), confirming that adding structural (edge) information to the universe representation meaningfully improves matching beyond URL's point-only approach.

- **Energy-based OOD filter is the most impactful single component.** The ablation study (Table 4) also shows that removing the outlier filter causes the largest performance drop (from 65.1 → reported low 50s), directly demonstrating that pre-matching OOD detection is essential for handling annotation errors.

- **Consistent SOTA margins across diverse settings.** On Pascal VOC unfiltered (Table 1) UGM achieves 69.8 F1 vs. best baseline 67.6 (GCAN, +2.2%); on Pascal VOC with outliers (Table 2) UGM achieves 65.1 vs. 60.3 (GCAN, +4.8%); on Willow occlusion (Table 3) UGM achieves 91.9 vs. 82.2 (GCAN, +9.7%). These margins hold across two datasets and multiple challenge conditions.

- **Clear conceptual separation of occlusion vs. annotation errors.** Section 1 explicitly distinguishes occlusion-caused outliers (which may still have cross-graph correspondences) from annotation errors (which are inherently meaningless), unlike prior work that conflates the two, and designs separate mechanisms for each.

- **Practical shared-universe design with class embeddings to control complexity.** Section 3.1 maps keypoints from different categories to shared universe nodes and re-injects category information via a learned class embedding, avoiding quadratic growth in universe size while maintaining category-specific matching quality.

- **Hyperparameter sensitivity analysis confirms practical stability.** Figure 4 shows that performance varies minimally across a reasonable range of temperature (0.8–10), threshold (-1.5 to -6), and margin values, with the principled default parameters yielding near-optimal results.

## Weaknesses

### Fatal
None.

### Major

- **Training procedure for the universe graph affinity in the presence of outliers is underspecified.** The cross-entropy loss \(\mathcal{L}_{\text{graph}}\) (Eq. 5) computes targets as \(y_n = \arg\max(\mathbf{X}_{iu}^{gt})\), which requires a valid ground-truth universe correspondence for every node. The \(\mathcal{L}_{\text{energy}}\) loss (Eq. 6) explicitly uses \(\mathcal{D}_{out}\) (out-of-distribution training data), indicating outliers are present during training. But the paper never states whether outliers are included in the \(\mathcal{L}_{\text{graph}}\) loss computation. If they are, the cross-entropy target is undefined for outlier points (they have no corresponding universe node), which would force the model to learn incorrect affinity values. If they are excluded, this design choice must be explicitly described, along with how training batches are constructed (e.g., two-stage training, separate data streams). As written, a reader cannot determine whether the two loss components are compatible. This is not a fatal flaw — there are plausible resolutions (e.g., train \(\mathcal{L}_{\text{graph}}\) only on inlier-annotated data and \(\mathcal{L}_{\text{energy}}\) on all data) — but the omission is a genuine evidential gap that must be clarified.

### Minor

- **Gap between surrogate training loss and test-time solver.** The paper trains with a cross-entropy classification loss on node/edge affinities (Eq. 5) but uses the LPMP solver at test time to produce a matching-consistent solution. The paper does not discuss whether these learned affinities actually lead to the correct matching via LPMP, or provide evidence (e.g., correlation between training loss and test matching accuracy) that the surrogate is sufficient. This gap is common in the literature but warrants explicit discussion.

- **Missing comparison with URL on Willow dataset.** URL (Nurlanov et al., 2023) is the most directly related prior work (universe point representation). The paper acknowledges that URL could not be replicated due to unavailable code, but this means Table 3 (Willow) lacks the closest competitor — particularly for the occlusion setting where URL's universe representation is most relevant. This weakens, though does not invalidate, the evaluation.

- **Evaluation of annotation errors is limited to uniformly random outliers.** The paper uses random coordinate-sampled outliers to simulate annotation errors. Real annotation errors may be more systematic (e.g., off-by-one pixel shifts, misplaced symmetric keypoints). The paper does not discuss whether the OOD filter would generalize to more structured annotation noise. This is an acknowledged evaluation limitation worth noting.

- **The "unfiltered" setting on Pascal VOC could be explained more clearly.** The paper states this setting "preserves all key points for graph pairs, to evaluate our method's performance under point occlusion." The relationship between preserving all annotations and measuring occlusion robustness (e.g., that occluded keypoints are present in the annotation but harder to match) is implied through the citation of BBGM's standard protocol but would benefit from a one-sentence clarification within the paper itself.

### Trivial

- The paper uses "URL (Nurlanov et al., 2023)" in Section 2.2 but "URL (Lin et al., 2023)" in Section 4.1. This is likely a citation inconsistency.
- Figure 4 and its description refer to "σ_in" where the text elsewhere uses "m_in."

## Nice-to-Haves

- Reporting precision and recall alongside F1 would give a more complete picture of the OOD filter's behavior (e.g., does it trade recall for precision?).
- Adding variance estimates (standard deviations) across multiple runs would help assess whether the reported improvements are statistically reliable, especially for margins in the 2–5 point range.
- A brief experiment correlating the surrogate training loss (cross-entropy on affinities) with the final LPMP matching accuracy would strengthen confidence in the training/solving pipeline.

## Removed Points

The following points were identified by reviewers but are removed or demoted for specific reasons:

1. **"Universe embedding collapse concern"** — The critic asks what prevents universe embeddings from collapsing under dot-product affinity. The cross-entropy loss with distinct keypoint-type labels naturally pushes embeddings to be discriminative; this is a standard property of classification-based training and not a genuine problem.

2. **"Pascal VOC occlusion protocol not defined"** — The unfiltered setting is a standard protocol from BBGM (Rolínek et al., 2020b), which is cited. The setting preserves all annotated keypoints (including occluded/truncated ones), creating natural partialness. The citation adequately defines the protocol; the paper does not need to re-derive it.

3. **"Missing architectural details (CNN backbone, GNN architecture)"** — The paper states these follow previous works (BBGM/NGM), which is standard practice in the graph matching literature. Architectural details that are inherited from prior work and unmodified do not need to be re-described in full.

4. **"Statistical significance not reported"** — While variance reporting would strengthen the paper, single-run evaluation is the norm in this benchmark setting (large-scale comparison tables over many categories). This is a community-standard practice, not a flaw specific to this paper.

5. **"Hyperparameter threshold chosen suboptimally"** — The paper transparently reports that τ=-2.5 gives the best F1 (66.37 vs. 65.1) but chooses to report the principled default τ=(m_in+m_out)/2 to avoid overfitting. This is defensible and standard practice, not a weakness.

6. **Strengths removed:** Some claimed strengths from the Strength Finder were too generic ("this paper addressed an important problem"). Only strengths with specific, verifiable evidence are retained.

## Novel Insights

The most interesting observation arising from the reviews is the asymmetry in how UGM's two components contribute across settings. The OOD filter delivers the largest single-component gain (ablation shows it's the most critical), yet the margin over baselines is largest in the *occlusion* setting (up to +9.7 F1 on Willow), where the universe graph — not the OOD filter — is the relevant mechanism. This suggests the structured universe graph provides a fundamentally better matching foundation that compounds with the OOD filter, rather than the two components operating additively. The paper itself notes this synergy (Section 4.3), but the numerical pattern across tables is more striking than the paper's discussion captures.

## Suggestions

1. **Explicitly describe the training data composition and loss handling for outliers.** State whether outliers are included in \(\mathcal{L}_{\text{graph}}\) batches, and if so, how the cross-entropy target is defined (or if not, how the two losses are combined/alternated). This is the single highest-priority revision.

2. **Discuss the surrogate training / test-time solver gap.** Add a paragraph explaining why cross-entropy on affinities is a reasonable proxy, and ideally include a small experiment correlating training loss with test matching accuracy.

3. **Add a comparison with URL on Willow** if code becomes available or if the authors can obtain results under the same protocol. If not possible, note this more prominently as a limitation.

4. **Clarify the Pascal VOC "unfiltered" setting** with a brief explanation of how occluded keypoints in the Berkeley annotations create natural partial matching.

5. **Standardize the URL citation** (Nurlanov et al., 2023 appears in one place; Lin et al., 2023 in another).
