Now I have a complete picture. Let me produce the final consolidated review.

## Summary

This paper proposes ProdInfluencerNet (PIN), a product-centric influencer recommendation framework that constructs a heterogeneous information network (HIN) with brand, product category, and influencer nodes. The core idea is to use product categories as a mediating bridge so that brands sharing the same product category can share information about previously collaborating influencers, enabling cold-start recommendation even when a product is new to a brand. Experiments on two Instagram datasets compare PIN against the GNN-IR baseline and include ablations over text vs. image vs. multimodal features.

## Strengths

- **Novel product-centric HIN structure for cold-start influencer recommendation.** The paper correctly identifies that existing profile-matching approaches struggle when a brand enters a new market or promotes a product in an unfamiliar category. Re-framing the problem around product categories — classifying sponsored post images into the Google Taxonomy and using those categories as explicit nodes in a heterogeneous network — is a genuinely creative solution that enables cross-brand knowledge sharing. The inductive learning setup tests generalization to unseen product category nodes, directly targeting the cold-start scenario.

- **Consistent results across two large-scale real-world datasets.** The paper uses two substantial Instagram datasets (I&B: 3,281 influencers, 14,801 brands, 70,417 posts; iKala: 15,214 brands, 3,422 influencers) and the results are qualitatively consistent across both. The data filtering steps (removing influencers with <10 collaborative posts) and feature dimensionality are clearly documented, supporting reproducibility of the datasets.

- **Interesting and practically useful finding about text vs. image features.** The paper shows that text-only features consistently outperform both multimodal and image-only variants for link prediction and recommendation. While the multimodal fusion analysis has gaps (see Weaknesses), the finding itself is counterintuitive relative to prior work that emphasized visual style (Gan et al., 2019; Elwood et al., 2021) and has practical implications: text-only pipelines reduce resource costs in deployment.

## Weaknesses

### Fatal
None.

### Major

- **The GNN-IR baseline comparison is not sufficiently documented to support the claimed factor-of-3 improvement.** The paper reports PIN achieving F1~0.7 while GNN-IR's best is ~0.2, but provides almost no detail about how GNN-IR was adapted to the proposed graph schema. The paper states "To facilitate a direct comparison with GNN-IR ... we aligned our metrics with theirs" (Section 4.2) and that PIN uses GraphSAGE as backbone — the same backbone GNN-IR uses — but does not specify whether the authors re-implemented GNN-IR or used original code, whether its hyperparameters (hidden dimensions, layers, learning rate) were tuned on the same validation set, or whether the same node features and data splits were used. Without this documentation, the comparison is uninformative. A factor-of-3 gap between methods sharing the same backbone on the same task demands careful analysis (e.g., ablation isolating the contribution of the HIN schema versus tuning differences), which the paper does not provide. This weakness concerns *documentation of the comparison*, not the results themselves, but it is severe because the paper's central claim of superiority rests on this comparison.

- **The multimodal fusion mechanism is not described, undermining the text > images claim.** The paper reports PIN_text > PIN_multimodal > PIN_image, but never explains *how* text and image features are fused (concatenation? attention-based? late fusion with separate GNNs?). Without this detail, it is impossible to determine whether the multimodal variant underperforms text-only because images are genuinely non-predictive for this task, or because the fusion strategy is suboptimal (e.g., naive concatenation causing feature imbalance, or using incompatible embedding spaces). The paper's claimed finding that "text features are more crucial than images" is potentially valuable, but the current experimental setup does not convincingly isolate whether this is a property of the data or a symptom of the architecture. A controlled ablation comparing different fusion strategies is needed.

### Minor

- **Cold-start evaluation is underspecified.** The inductive split is described in one sentence: "the product category nodes in the testing phase include nodes that were not seen during training" (Section 4.3). The paper does not report: (a) the number or percentage of unseen product category nodes, (b) the number of test edges involving these unseen nodes, or (c) the distribution of test edges per unseen category. This makes it hard to assess the difficulty of the inductive task. Additionally, the paper does not compare against a simpler non-graph baseline (e.g., cosine similarity between product category text embeddings and influencer text embeddings), so it is unclear whether the HIN structure itself adds value beyond the feature embeddings.

- **Pre-trained models used for feature extraction are not named.** The paper specifies embedding dimensionalities (text: 512-D, image: 640-D) but never identifies which pre-trained models produced them. This is a basic reproducibility gap — without knowing whether text embeddings came from sentence-BERT, CLIP, or another model, or whether image embeddings came from VGG-16, ResNet, or CLIP, the experiments cannot be reproduced or compared with prior work.

- **No evaluation of the product category classifier accuracy.** The entire data pipeline depends on classifying sponsored post images into Google Taxonomy categories via "image classification techniques" (abstract), yet the paper provides no accuracy, precision/recall, or human evaluation of this classifier. If the category assignment is noisy, the graph edges are noisy too, which propagates to all downstream results.

- **No statistical significance or variance reporting.** All results appear to be point estimates from a single run. Given the large number of experimental configurations (6 per dataset × 2 datasets), standard deviations over multiple runs or significance tests should be reported to assess whether observed differences (e.g., PIN_text vs PIN_multimodal) are reliable.

- **No graph density or node degree statistics reported.** The paper provides edge counts but not graph density, average node degrees, or the distribution of brands/categories per influencer. These statistics are standard in graph-based papers and help assess task difficulty and whether high AUC values may partly reflect an easy prediction task.

### Trivial
- Some awkward phrasing (e.g., "some influencer has post a number of articles") and instances of unclear prose.

## Nice-to-Haves

- A comparison against a simple content-based retrieval baseline (e.g., TF-IDF or sentence embedding cosine similarity between product category descriptions and influencer bios) would help isolate the contribution of the HIN structure from the contribution of the feature embeddings.
- Reporting ROC AUC for GNN-IR as well, to calibrate whether PIN's AUC >0.95 is remarkable or largely driven by graph structure properties common to both methods.
- A fixed random seed disclosure and multi-run statistics would improve reliability.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Typographical nitpicks ("lunching", "a number of post"):** Removed per instruction — these are potential typos but do not affect scientific content.
- **"Tables not visible in the extracted text":** Removed — table content is embedded as images in the PDF; the parser strips them but they exist in the original submission.
- **Criticism that the cold-start challenge is not the "most challenging" scenario:** Removed as scope creep — the inductive split over product categories is a reasonable and well-motivated cold-start evaluation. Demanding a more specific scenario (brand launching in a brand-new category) would be a different paper.
- **Criticism that "the paper does not test inductive learning in a rigorous cold-start evaluation":** This contradicts the paper's clear statement that test product category nodes are unseen during training (Section 4.3). The inductive setup *is* tested; the underspecification of details is a separate Minor weakness (retained above). The categorical claim that inductive learning is "untested" is factually incorrect given Section 4.3.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Document the GNN-IR adaptation in full.** Specify whether original code or a re-implementation was used; report the hyperparameter search space and the best configuration found; clearly state whether the same node features (including text/image embeddings from the same pre-trained models) were used for both methods. If the gap remains large after careful tuning, provide an analysis of *why* — e.g., does the product-category HIN provide more relevant neighborhood information per node?

2. **Describe the multimodal fusion mechanism and add a controlled ablation.** Report exactly how text and image features are combined. Then compare: (a) text-only, (b) image-only, (c) concatenation fusion, (d) attention-based fusion, and (e) late fusion (separate GNNs for each modality followed by pooling). If text-only still dominates across all fusion strategies, the claim about text dominance is strengthened; otherwise, the finding needs to be qualified as architecture-dependent.

3. **Provide cold-start evaluation statistics:** number of unseen product category nodes, test edges involving unseen nodes, and a non-graph baseline (e.g., embedding cosine similarity) to isolate the HIN's contribution.

4. **Name the pre-trained models** used for text and image embeddings.

5. **Report the accuracy of the product category classifier** on a held-out validation set, or at minimum describe its architecture and training data.

## Score and Decision

The paper has a genuinely interesting core idea — using product categories as mediating nodes in an HIN for cold-start influencer recommendation — and produces a practically useful finding (text features dominate images for this task). However, the experimental validation has two structural gaps that prevent proper assessment: (1) the GNN-IR baseline comparison is critically underdocumented, making the claimed factor-of-3 improvement unverifiable, and (2) the multimodal fusion analysis lacks the architectural detail needed to support the text-dominance claim. These are addressable in a revision, but in the current form the paper does not convincingly demonstrate that its central claims hold. I recommend rejection with a clear path to resubmission if the authors strengthen the evaluation as outlined in the Suggestions.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>