Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper proposes Universe Graph Matching (UGM), which decomposes the ambiguous pairwise partial matching problem into two well-defined subgraph matching problems via a learned latent universe graph (addressing occlusion), coupled with an energy-based out-of-distribution (OOD) detection module that filters annotation errors before matching. The method is evaluated on Pascal VOC and Willow Object Class datasets under occlusion, random outlier, and combined settings, consistently outperforming prior state-of-the-art methods across all six configurations.

## Strengths

- **Principled problem decomposition.** The reformulation \(\mathbf{X}_{ij} = \mathbf{X}_{iu}\mathbf{X}_{ju}^\top\) transforms the ill-posed partial matching problem into two unambiguous subgraph matching tasks (Section 3.3). This is a clear conceptual advance over dummy-node heuristics, and the text explains why the decomposition helps: the universe graph contains all points and edges, so each input graph becomes its subgraph. The 9.7% F1 lead over GCAN on Willow occlusion (where the outlier filter is inactive) provides empirical support that this structural reformulation is beneficial.

- **First application of energy-based OOD detection to annotation error filtering in graph matching.** The paper adapts the energy score from Liu et al. (2020) to the graph matching setting, uses a margin loss to widen the inlier/outlier energy gap, and applies it as a pre-matching filter (Section 3.2). The ablation study (Table 4) confirms that removing this component causes the largest performance degradation in the random outlier setting, validating its role.

- **Consistent improvements across diverse challenging settings.** UGM achieves the highest F1 in all six evaluated scenarios: +2.2% on Pascal VOC unfiltered, +4.8% on Pascal VOC with random outliers, +9.7% on Willow occlusion, +1.7% on Willow random outliers, and +5.9% on Willow occlusion+random outliers (Tables 1–3). The advantage spans both datasets (20 vs. 5 categories) and both challenge types (occlusion vs. outliers), suggesting genuine robustness rather than dataset-specific tuning.

- **Practical category-sharing design with ablation support.** Rather than learning a separate universe graph per category, the paper shares node/edge embeddings across all categories and re-injects category information via a learned class embedding derived from global image features (Section 3.1). The ablation study (Table 4) explicitly tests the "without class embedding" condition, confirming its positive contribution.

- **Honest and detailed limitation discussion.** Section 3.3 openly acknowledges three specific weaknesses: closed-set limitation, edge distribution imbalance harming some edge embeddings, and error propagation through the universe graph. This transparency is rare and valuable.

## Weaknesses

### Fatal

None.

### Major

None. The core contributions are supported by the experimental evidence, and no identified weakness invalidates the paper's central claims.

### Minor

- **Missing ablation on the occlusion-only setting.** The ablation study (Table 4) is conducted only on Pascal VOC with random outliers. While the Willow occlusion results (+9.7% over GCAN) provide indirect evidence that the universe graph helps with occlusion (since the outlier filter should be largely inactive without outliers), an explicit ablation on occlusion-only data (e.g., full UGM vs. UGM with universe graph replaced by universe points, on Willow occlusion) would cleanly isolate the universe graph's contribution. Without it, the paper's claim that "the latent universe graph structure offers a considerable benefit" for occlusion relies on inter-dataset inference rather than a controlled experiment.

- **Key baseline (URL) not compared on all settings.** URL (Nurlanov et al., 2023) learns a universe point representation for partial matching and is the most directly related prior work. The paper states it "failed to replicate [URL] because [it] did not release publicly available code" and therefore does not report URL in Tables 2 and 3 (random outlier and Willow settings). The authors are transparent about this, but its absence weakens the SOTA claim on the very settings where a universe-based approach would be most relevant. The qualitative lead over GCAN and AFAT is clear, but a comparison with the most similar competitor would strengthen the paper.

- **Underspecified OOD training data generation.** The method trains the energy-based detector using a margin loss with in-distribution \(\mathcal{D}_{in}\) and out-of-distribution \(\mathcal{D}_{out}\) data (Section 3.2). The experimental protocol (Section 4.1) describes adding random outliers at test time by "randomly sampl[ing] the coordinates on images." However, the paper does not clearly specify how \(\mathcal{D}_{out}\) is generated during training or whether it uses the identical procedure as test-time outlier generation. If so, the detector could be tuned to a specific synthetic noise model, and generalization to real annotation errors with different characteristics remains unexamined.

- **No statistical significance reporting.** All results are reported as single F1 scores without variance estimates or multiple runs. This is common in the graph matching benchmark literature, but given the gap sizes (e.g., 1.7% on Willow random outliers), confidence intervals would help assess whether differences are meaningful.

- **Brittleness on rare classes.** The pressure test (Figure 3) shows 32–61% performance drops for classes like "sofa," "train," and "table" as outlier count increases. The paper correctly attributes this to limited training data, but this is a practically significant limitation: the method's robustness depends on having sufficient per-class training examples, which may not hold in real-world long-tailed distributions.

### Trivial

- The compared methods section lists URL with an inconsistent citation: "(Lin et al., 2023)" vs. "(Nurlanov et al., 2023)" used elsewhere. This appears to be a citation error that should be corrected.
- The phrase "out method UGM" in Table captions (lines 204, 206, 208) should read "our method UGM."

## Nice-to-Haves

- An occlusion-only ablation on Willow data (full UGM vs. universe-point baseline vs. without edge learning) would directly confirm the universe graph's role in occlusion handling.
- An analysis of the outlier detector's standalone performance (e.g., AUC for inlier vs. outlier classification, or precision/recall at the chosen threshold) would help separate its contribution from the matching component.
- A comparison where URL is re-implemented or the authors obtain its code would make the SOTA claim conclusive.
- t-SNE visualizations of the learned universe node embeddings across categories would demonstrate whether shared nodes capture semantically meaningful correspondences (e.g., "left wheel" from cars and "left handlebar" from bikes mapping to the same node).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Internal inconsistency in the 4.8% claim"** — The reviewer claimed a contradiction between UGM exceeding the next best method by 4.8% while GCAN has a smaller performance drop (ranking first in robustness). There is no contradiction: UGM can have a higher absolute F1 score than GCAN while GCAN shows a smaller relative drop from its own (lower) unfiltered baseline. The 4.8% and the 8.8% drop refer to different quantities. The reviewer's speculation about table values (63.3 vs. 63.2) is unverifiable since the tables are image-based and stripped by the parser.

- **"The class embedding ablation is missing"** — The reviewer claimed the paper does not show whether the class embedding is necessary. The ablation study (Table 4) explicitly includes a "without class embedding" condition. The paper describes it: "Without class embedding, we directly used the local key point features extracted by the backbone to learn the node embeddings."

- **"Unusual to feed BBGM pre-trained affinities into learning-free solvers"** — This is standard practice in the deep graph matching literature, established by BBGM and followed by subsequent works. The comparison is informative about solver behavior with learned affinities, and the paper is transparent about this design.

- **"The paper does not mention a validation set"** — The standard protocol in this field uses the specified train/test splits without a separate validation set. This is not a methodological gap.

- **"Choosing hyperparameters based on test performance is data leakage"** — The paper runs a sensitivity analysis, notes the overfitting concern explicitly ("we are concerned that this might lead to some overfitting in the model"), and defaults to the principled choice \(\tau = (m_{in} + m_{out})/2\). This is standard practice for hyperparameter sensitivity studies and is not data leakage.

- **"Missing appendix/proofs"** — The parser strips appendix sections from all submissions; they exist in the original PDF.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation emerging from the review process is the sharp asymmetry in ablation severity: the outlier filter's removal causes a catastrophic collapse (39.8 vs. 63.3 full), while removing edge learning or class embedding produces much milder degradation. This suggests that the energy-based OOD detection is the dominant mechanism driving gains in the random outlier setting, while the structured universe graph (edges + class embedding) provides a smaller but consistent additive benefit. The paper's discussion of this asymmetry could be deepened — for instance, one could ask whether a simpler baseline (outlier filtering + standard pairwise matching) would recover most of the gain, and whether the universe graph's main value is specifically in occlusion settings where the outlier filter cannot help.

## Suggestions

1. **Add an occlusion-only ablation** on Willow data: compare full UGM vs. UGM without edge learning (universe points only) vs. UGM without the universe graph (standard matching with the same backbone). This would directly validate the claim that the structured universe graph helps with occlusion.
2. **Specify OOD training data generation** clearly: state whether \(\mathcal{D}_{out}\) is generated using the same procedure as test-time outliers, and discuss the generalization gap to real annotation errors.
3. **Run at least 3 replicates** with different random seeds and report mean ± std for the main results, especially where the margin over baselines is small (e.g., 1.7% on Willow random outliers).
4. **Report the outlier detector's standalone performance** (AUC or precision-recall for inlier vs. outlier classification) to separate its contribution from the matching stage.
5. **Correct the URL citation inconsistency** in the compared methods section.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>