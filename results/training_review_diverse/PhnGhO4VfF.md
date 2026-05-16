Now I have read and verified the full paper. Let me produce the consolidated review.

---

## Summary

This paper studies how pretraining label granularity affects transfer learning in image classification. It provides a theoretical analysis using a simplified two-layer ReLU network with orthonormal features, proving that coarse-grained pretraining cannot learn fine-grained (rare) features while fine-grained pretraining can. Empirically, it shows that leaf-level pretraining on ImageNet21k yields a ~10% improvement over coarse-level pretraining on ImageNet1k, and systematically investigates conditions (meaningful hierarchy, label alignment) for effective fine-grained pretraining using iNaturalist 2021, revealing a U-shaped error curve.

## Strengths

1. **Formal theoretical analysis of why fine-grained pretraining helps.** Theorems 1 and 2 prove, under a defined feature hierarchy, that coarse-labeled SGD cannot learn fine-grained features even with polynomially many steps, whereas fine-grained pretraining does learn them and achieves near-perfect accuracy on both easy and hard test samples. This formalizes the intuitive correspondence between label granularity and feature learnability using a multi-view data model and cross-entropy loss — advancing beyond prior NTK-based or hinge-loss analyses (Section 4).

2. **Clear empirical validation on ImageNet21k→ImageNet1k with ViT-B/16.** Table 1 shows a monotonic improvement in finetuning accuracy from 72.75% (granularity level 9, 38 classes) to 82.51% (leaf level, 21,843 classes). This directly supports the core claim and the common practice of using leaf-level labels, with a practically significant ~10% gain over the coarsest level.

3. **Systematic dissection of conditions for effective fine-grained pretraining using iNaturalist 2021.** Figure 2 reveals a U-shaped error curve for manual hierarchies and contrasts it with random labels, per-superclass clustering, and whole-dataset clustering. This goes beyond a simple "finer is better" story, showing that both label alignment and meaningful hierarchy matter — random labels perform worst, and extreme granularity (unique labels per sample) degrades performance.

4. **Identification of label function alignment as a key factor.** The comparison between kMeans per superclass (forced alignment, lower error) versus kMeans on the whole dataset (no alignment, higher error) isolates the importance of source and target label functions sharing discriminative features. This is a novel practical finding not present in prior work on label granularity.

5. **Novel theoretical framework connecting feature rarity with solution complexity.** The data model (Definitions 1–4), where features are orthonormal, easy samples contain both common and fine-grained features, and hard samples lack common features, formalizes the hierarchy present in natural images. The proof techniques tracking hidden neuron dynamics under cross-entropy loss extend beyond prior analyses.

## Weaknesses

### Fatal
None.

### Major

1. **Theory-experiment gap: the proposed mechanism is not empirically validated.** The theory (Theorems 1 and 2) predicts that fine-grained pretraining helps specifically because it learns rare features that improve accuracy on *hard* test samples (where common features are absent or weak). However, the experiments report only overall validation accuracy — they do not split test samples into easy/hard categories, nor do they analyze whether fine-grained pretraining indeed produces stronger feature representations for rare features. The paper does not claim the experiments *validate* the theory's mechanism (they are presented as separate contributions), but the claimed explanation remains untested by the data. This disconnect weakens the narrative arc: the reader is left wondering whether the theoretical mechanism actually operates in the experimental settings. The paper has the machinery to operationalize a hard-sample split (e.g., samples misclassified by a coarse-pretrained model) and test whether fine-grained pretraining differentially improves them, but does not do so.

### Minor

1. **Figure 2 caption is imprecise about the operating range.** The caption states "The manual hierarchy outperforms the baseline and every other hierarchy," while the body text (Section 5.2) explains this holds *"as long as the pretraining label granularity is beyond the order of 10^2"* and notes that the U-shaped curve rises at extreme granularities. The caption should qualify the range or explicitly note that the manual hierarchy's advantage holds within the plotted granularity regime but degrades at extremes. This is a presentation issue that could mislead a casual reader.

2. **Theoretical model is quite stylized, limiting direct applicability.** The analysis assumes: orthonormal features, frozen second-layer weights, training on *only* easy samples, a single hierarchy level, and no distribution shift between source and target. The paper acknowledges some of these limitations (Section 4, paragraph after Theorem 2) but in a single paragraph. The assumptions are reasonable for a theoretical proof-of-concept, but the gap between this setting and practical deep-network training deserves more prominent discussion — ideally a dedicated "Limitations of the Theoretical Analysis" paragraph — to manage reader expectations and prevent over-interpretation.

3. **iNaturalist experiments use only the mini training set.** While justified as a way to "generate a greater gap between the performance of different hierarchies and to shorten training time" (Section 5.2), this limits confidence that the observed trends (U-shape, relative ordering of methods) would hold at full dataset scale. A brief note on whether preliminary experiments with the full set show consistent trends would strengthen the claims.

### Trivial

1. The theorems are presented as "Summaries" rather than full formal statements. While this is common for space reasons, the exact dependence on parameters like \(d\) and \(f(\sigma_\zeta)\) is difficult to verify from the summary alone. Adding the full theorem statements to the appendix (which likely exists in the original submission but was stripped) would address this.

## Nice-to-Haves

- A hard-sample analysis (e.g., splitting test samples by whether a coarse-pretrained model classifies them correctly) would directly bridge the theory-experiment gap and substantially strengthen the paper's central claim. This is the single highest-value addition the authors could make.
- Reporting learning curves or convergence behavior during pretraining would add depth, given the theory's focus on training dynamics.
- A brief discussion of sensitivity to the choice of embedding model for the kMeans clustering (CLIP ViT-L/14) would improve the iNaturalist analysis.

## Removed Points

These points were raised by reviewers but are removed after verification against the paper; they are listed here for completeness but should be treated with caution.

- *"No discussion of the limitations of the theoretical model in the main text (only a footnote)"* — **Factually incorrect.** The paper devotes a full paragraph (lines 194–195, Section 4.4) to discussing the "easy samples only" limitation, explicitly calling it an "exaggerated" presentation of the feature-learning bias. The paper also footnotes the perturbed-results extension. The limitations are discussed substantively in the main text.
- *"The experiments do not support the core claim"* — The paper separates theoretical and empirical contributions. The empirical experiments validate the trend (finer granularity → better accuracy) and identify practical conditions. They do not claim to validate the theory's mechanistic prediction about hard samples, so this is not a contradiction — it is a gap (which is kept as a Major weakness above).
- *"The paper overstates the explanatory power of the theory"* — The abstract uses "explain" and the introduction uses "theoretical explanation." Given the simplified setting, these word choices are appropriate for a theoretical paper. The claims are not inflated relative to the analysis presented.
- *"Missing learning curves / convergence behavior"* — This is a wishlist item, not a weakness. The paper's claims do not depend on it. Moved to Nice-to-Haves.
- *"The kMeans using CLIP embeddings is an unfair advantage"* — CLIP is used only to generate alternative label hierarchies for controlled comparison, not as a pretrained backbone for the main experiment. This is a legitimate experimental design choice, not a weakness.

## Novel Insights

The reviews surface one genuinely novel observation that goes beyond the paper's own contributions: the U-shaped curve for manual hierarchies in iNaturalist is particularly striking because it simultaneously vindicates the "finer is better" intuition (over most of the range) and reveals a failure regime at extreme granularities. No prior work has systematically mapped this operating regime for fine-grained pretraining while controlling for the data and network architecture. The contrast between per-superclass and whole-dataset kMeans clustering isolates label alignment as an independent factor — this is a clean experimental design insight that future work can build on directly.

## Suggestions

1. **Bridge the theory-experiment gap.** Define "hard" test samples operationally (e.g., those misclassified by a coarse-pretrained model or those with low prediction confidence from a coarse model) and show that fine-grained pretraining differentially improves accuracy on these samples. This single addition would substantially strengthen the paper's central contribution.
2. **Correct the Figure 2 caption** to qualify the performance claim with the granularity range, or align it precisely with the text's description.
3. **Add a "Limitations" paragraph** that explicitly itemizes what the theoretical analysis does and does not account for, rather than burying the discussion after the theorems.

## Score and Decision

The paper makes meaningful progress on an important and under-explored question. The theoretical framework is novel, the empirical findings (U-shaped curve, label alignment) are practically useful, and the ImageNet21k→ImageNet1k results confirm a widely used but poorly understood practice. The primary weakness is the disconnect between the theory's mechanistic prediction (hard-sample improvement) and the experimental evaluation (overall accuracy only) — this is a real gap but not a fatal one, and it is addressable. The presentation issues are minor. I assess the paper as solid and deserving of acceptance, with the expectation that the authors address the theory-experiment gap in a revision.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>