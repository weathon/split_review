Here is my final consolidated review:

## Summary

This paper introduces DocMIA, the first document-level membership inference attacks specifically targeting Document Visual Question Answering (DocVQA) models. It proposes optimization-based features — the L2-norm of parameter change and number of optimization steps after fine-tuning on a single QA pair — as membership signals in a white-box setting, and a distillation strategy that transfers these signals to a proxy model for black-box attacks, all without auxiliary datasets. The method is evaluated on three model families (VT5, Donut, Pix2Struct) across two benchmarks (DocVQA, PFL-DocVQA).

## Strengths

- **Novel optimization-based discriminant features for DocMIA.** The core idea — fine-tuning a model on individual QA pairs and using the L2 parameter change distance (Δ) plus optimization steps as membership signals (Definition 4.1, Section 4.2.1) — is well-motivated and creative. The intuition that member documents converge faster with smaller parameter changes is conceptually sound and empirically supported: the proposed methods achieve up to a 10% F1 improvement over the single-step gradient baseline GRADIENT-UA on Donut (Section 6.1), demonstrating that iterative optimization extracts a more discriminative signal.

- **Practical black-box attack via distillation without auxiliary data.** The distillation-based black-box strategy (Section 4.3) transfers membership-indicative behavior from a black-box model to a proxy model using only output predictions — crucially, without needing an auxiliary dataset, a constraint that much prior multimodal MIA work (Ko et al., 2023; Hu et al., 2022) required. The attack remains effective even with mismatched architectures: using VT5 and Donut as proxies against Pix2Struct yields gains of +3.04% accuracy and +4.88% F1 over the best score-based baseline (Section 6.2).

- **Computationally efficient variants (FL, FLLoRA, IG).** The three practical variants (Section 4.2.2) reduce per-document optimization cost by optimizing a single layer, using LoRA with Kaiming initialization, or optimizing pixel inputs. These address a key practical barrier and the paper shows they maintain competitive attack effectiveness.

- **Effectiveness against models with minimal overfitting.** The black-box distillation attacks remain effective against Pix2Struct-Large (Section 6.2), which exhibits strong generalization and a small train-test gap (Figure 9). Score-based baselines rely on the generalization gap, yet the distillation approach transfers membership information even when the raw score signal is weak, which is a notable empirical finding.

## Weaknesses

### Fatal

None.

### Major

- **The abstract and conclusion overclaim performance relative to the reported numbers.** The abstract states: "Our unsupervised methods outperform existing state-of-the-art membership inference attacks across a variety of DocVQA models and datasets" and the conclusion reasserts "significantly outperform existing membership inference baselines." However, in the white-box setting, the strongest baseline SCORELOSS-UA_all achieves **84% F1 on Donut** and **75% on VT5**, while the proposed methods (FL, FLLoRA, IG) achieve **82.5% on Donut** and **72% on VT5** — the baseline is better on 2 of the 3 model families. Only on Pix2Struct does the proposed method lead (72% vs. 69%). The paper's more careful internal wording ("deliver either the best or near-best performance," "generally outperforming") is honest, but the abstract and conclusion misrepresent the results. The claims should be reframed as: the proposed methods are competitive with strong baselines, with advantages on certain model-dataset combinations. This mismatch is significant for a top-venue submission.

### Minor

- **The "exact training questions" assumption in the black-box threat model is insufficiently justified.** Section 4.1 assumes the adversary knows "the exact training questions" for each document, arguing that "an adversary can approximate them based on the knowledge of the training document type." Knowing the document type does not generally enable one to approximate the exact questions used during training. The paper does not evaluate how sensitive the attack is to this assumption (e.g., by using different but semantically related questions). This weakens the practical plausibility of the black-box threat model.

- **The FL variant does not specify which single layer is selected for optimization.** Section 4.2.2 states "we select one specific layer L to optimize" without reporting which layer is chosen for each model architecture (e.g., early vs. late, encoder vs. decoder). Different layers encode different information, and attack effectiveness could depend heavily on this choice. This omission affects reproducibility.

- **The black-box attack mechanism would benefit from stronger validation.** The proxy model is trained on D_test labels from the black-box model, creating a scenario where all test documents are "members" of the proxy's training set. The paper asserts that membership information from the black-box model "transfers" through distillation (Section 4.3). While the mechanism is plausible (the proxy inherits the black-box's differential output quality on members vs. non-members), a control experiment — e.g., training the proxy on labels from a randomly initialized model and showing the attack fails — would strengthen the causal claim. Without this, the extent to which success stems from transferred membership information versus the proxy training setup is unclear.

- **Clustering stability is not reported.** The attack uses KMEANS with the heuristic that the cluster with larger average Δ corresponds to non-members. The paper reports results over 5 random seeds but does not report the stability of the cluster-label mapping (e.g., how often the Δ-heuristic yields the correct mapping across seeds). If the heuristic inverts in some seeds, the reported metrics would be misleading. Reporting per-seed variance or using a more robust binary classification framework would address this.

### Trivial

- **Duplicated text in the evaluation section.** The same evaluation paragraphs appear twice in Section 6 (first in lines 166–170 discussing baseline performance, and again in the same block of text). This appears to be a copy-paste error in the manuscript rather than a parser issue, and should be cleaned up.

## Nice-to-Haves

- **Computational cost analysis.** The paper acknowledges that per-document optimization "is relatively slow" but provides no quantitative analysis of runtime or FLOPs. For a 1.3B parameter Pix2Struct model running optimization per document per QA pair across 600 documents, this cost could be substantial. Quantifying it would help readers assess practical feasibility.
- **Ablation on number of optimization steps.** Varying the maximum optimization steps S would directly test the claim that multi-step optimization is more informative than single-step gradients.
- **Ablation over different layers for FL.** Showing whether layer choice matters (early, middle, late, head) and, if so, justifying the chosen layer.

## Removed Points

These points were considered but removed with justification:

- **Criticism about low TPRs at low FPR (8-11% at 3% FPR) undermining practical utility.** Removed because: this is standard in the MIA literature (Carlini et al., 2022) and the paper reports these numbers transparently alongside Balanced Accuracy and F1. The numbers are not particularly low for the field. The critic's claim that metrics are "inflated" conflates different evaluation standards.

- **Criticism about IG requiring differentiable image pathways.** Removed because: the paper already explicitly states "this assumes the target model allows differentiation of the document image through its architecture" (Section 4.2.2), fully acknowledging this constraint.

- **Criticism about black-box hyperparameters being tuned on target model architecture.** Removed because: re-reading Section 5.2, the hyperparameters are tuned per model architecture, but in the black-box setting the adversary knows their own proxy model's architecture (which is what the hyperparameters are tuned for). The critic's assumption that hyperparameters are tuned for the unknown target architecture is not clearly supported by the paper's description.

- **Criticism about logit/probability availability from auto-regressive models.** Removed because: the paper's claim is that these features are "difficult to adapt" (not impossible), and the paper's use of Min-K% and Min-K%++ as baselines confirms they acknowledge token-level information exists. The framing is about difficulty of aggregation, not unavailability.

- **Criticism about proxy model pre-training data overlap.** Removed because: the paper states the pre-training data is "inaccessible and assumed to be disjoint from the private dataset D_t" (Section 4.3). Verifying this is impractical and the assumption is standard.

## Novel Insights

The reviews surface an interesting tension in the paper's evaluation design that goes beyond the listed weaknesses: the paper's clustering-based attack pipeline introduces a circular dependency between feature quality and metric interpretation. The KMEANS algorithm assigns labels based on the Δ heuristic, and then performance is evaluated against ground-truth labels using the same Δ-based cluster assignment. If the Δ heuristic were inverted for a given model (members having larger Δ than non-members), the attack would achieve near-zero accuracy — yet the evaluation protocol would not detect this as a failure of the signal; it would be absorbed as "low performance" indistinguishable from a genuinely weak signal. This means the reported 72–82% F1 numbers simultaneously measure (a) how well the Δ heuristic separates members from non-members and (b) whether the heuristic's sign is correctly oriented. The paper does not disentangle these. A direct plot of Δ distributions for members vs. non-members (without any clustering step) would be a more transparent diagnostic for the core claim.

## Suggestions

1. **Reframe all claims about performance honestly.** Replace "outperform SOTA" in the abstract and conclusion with language like "are competitive with or in some settings exceed strong baselines." This single change would significantly improve the paper's integrity.
2. **Specify which layer is selected for FL** and provide an ablation justifying this choice.
3. **Run the suggested control experiment for the black-box attack** (proxy trained on labels from a random model) to demonstrate that membership transfer through distillation is the active mechanism.
4. **Plot the distribution of Δ for members vs. non-members** for each model-dataset combination as a direct diagnostic for the core assumption.
5. **Report per-seed stability of KMEANS** cluster-label mapping across random seeds.
6. **Acknowledge the strength of the "exact training questions" assumption** and discuss its implications for real-world applicability.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>