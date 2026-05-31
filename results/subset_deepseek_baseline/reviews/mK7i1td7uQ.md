## Summary

This paper introduces ConforFormer, a molecular representation learning method that extends the Uni-Mol backbone with a contrastive learning objective (NT-Xent) over conformer pairs. The goal is to produce a task-agnostic, conformation-agnostic frozen embedding usable for property prediction and similarity search without fine-tuning the entire model. The authors also introduce PharmIsomer, a new benchmark for evaluating conformer/isomer discrimination, and demonstrate that the learned embeddings separate conformers from isomers in the embedding space, exhibiting an emergent ability to infer molecular graph structure from 3D geometry alone.

## Strengths

- **Well-motivated problem.** Capturing conformational diversity is genuinely important for molecular property prediction, and most existing foundation models ignore it. The paper correctly identifies this gap and proposes a principled approach.
- **Introduction of a useful benchmark.** PharmIsomer is a valuable new resource for evaluating whether models truly understand the difference between conformers and isomers at scale (3.3 billion pairs). This fills a gap in current evaluation.
- **Clean contrastive formulation.** The NT-Xent loss on conformer pairs is mathematically clear, and the overall pre-training loss (including the relative weights of token, coordinate, distance, and contrastive terms) is explicitly stated.
- **Demonstration of emergent graph-like understanding.** The analysis on PharmIsomer convincingly shows that ConforFormer embeddings separate conformers from isomers with high precision (83% at 50% recall for the frozen model), whereas the baseline Uni-Mol embeddings do not. The qualitative examples (Figure 5 vs Figure 6) are illustrative.
- **Reproducibility commitment.** The authors provide code, model weights, and a sample of the new dataset, with plans for full release.

## Weaknesses

### Fatal
None.

### Major

1. **Limited practical value of frozen embeddings on property prediction.** The primary claim is that ConforFormer produces "compact, informative representations suitable for downstream tasks" that can be used without fine-tuning. Yet on MoleculeNet benchmarks, the frozen ConforFormer-OMol embeddings underperform the fully fine-tuned Uni-Mol by a large margin (e.g., ROC-AUC on BBBP 0.673 vs 0.729; RMSD on ESOL 1.12 vs 0.79). For a practitioner, this gap is likely prohibitive. The argument that these results are "on par or exceeding most of 2020s level methods" is misleading because those older methods were also evaluated under different protocols; the comparison is not apples-to-apples for frozen embeddings.

2. **Insufficient baselines for frozen embeddings.** The paper compares only to fully fine-tuned models and a few frozen variants of Uni-Mol. It lacks comparisons against other frozen embedding approaches (e.g., Morgan fingerprints + simple MLP, pretrained GNNs frozen, or other conformation-aware frozen representations). Without such comparisons, it is unclear whether ConforFormer offers any advantage over simpler, cheaper alternatives for the frozen-embedding use case.

3. **Inconsistent improvement from contrastive learning.** On classification, ConforFormer-OMol improves over Uni-Mol (frozen) on only 5 of 8 tasks, and on regression it improves on 4 of 6. The magnitude of improvement is modest (e.g., +0.033 on BBBP, –0.052 on BACE). The paper does not analyze why contrastive learning helps on some tasks and hurts on others, leaving the robustness of the approach in question.

4. **Reproducibility and training details are incomplete in the main text.** The contrastive training procedure (number of steps, learning rate schedule, batch composition, temperature selection) is relegated to the Supporting Information, which is not provided in the review. This makes it impossible to fully assess the soundness of the training pipeline. The description of Uni-Mol replication (deprecated RDKit feature) introduces additional uncertainty about the baseline.

### Minor

- The "CLS token" used throughout is standard but its properties are not deeply analyzed beyond cosine similarity distributions. For example, does the CLS token suffer from anisotropy (all embeddings collapsing to a narrow cone)? The paper could benefit from measuring embedding space isotropy.
- The PharmIsomer analysis treats enantiomers as the same molecule by design, but this is a limitation for drug discovery applications where chiral specificity is critical. This is acknowledged but not explored.
- Some standard deviations in Table 1 are large (e.g., Conformer-OMol BACE std=13, ClinTox std=39), suggesting instability in some fine-tuning runs even with frozen embeddings. No discussion of what might cause this.

### Trivial

- The title inconsistently uses "CONFORFORMER" (all caps) while the model name is ConforFormer. The abstract also writes "Conformer" as the method name once.
- Figure descriptions in the main text are somewhat repetitive of the captions.

## Nice-to-Haves

- Compare ConforFormer frozen embeddings against a simple baseline using Morgan fingerprints (ECFP4) with the same MLP head. This would directly show whether the learned embedding adds value over a classic, fast alternative.
- Provide an analysis of how much the contrastive loss weight (2 in the total loss) affects downstream performance, as this is a sensitive hyperparameter.
- Report the classification performance on PharmIsomer as a formal discriminative task (AUROC) in addition to precision-recall curves.
- Include a plot of embedding dimensionality vs performance to understand whether all 512 dimensions are needed.

## Novel Insights

The most interesting finding is that the model learns to distinguish conformers from isomers without ever being trained on isomer labels, by virtue of the contrastive loss that aligns conformers and pushes apart different molecules. This emergent ability to infer molecular topology from 3D coordinates alone is a genuinely novel observation, supported by the precision-recall analysis on PharmIsomer. The paper shows that this property does not arise in the standard Uni-Mol pretraining, suggesting that the contrastive objective is responsible for inducing a more graph-aware representation.

## Suggestions

- Strengthen the property prediction experiments by including a direct comparison to other frozen embedding methods (e.g., ECFP + linear model, pretrained GNN frozen). This would clarify whether ConforFormer is actually useful as a drop-in feature extractor.
- Provide a thorough analysis of the tasks where contrastive learning hurts performance; this could reveal systematic limitations (e.g., tasks that require precise geometric information may suffer from the conformation-agnostic regularization).
- Consider releasing the full PharmIsomer benchmark with the submission so that reviewers and future researchers can reproduce the similarity analysis exactly.
- If the claim is that the model can be used without fine-tuning, demonstrate a concrete use case (e.g., similarity search against a large database showing that ConforFormer embeddings retrieve chemically similar molecules more accurately than baseline methods).

## Score and Decision

**Score:** 4.5  
**Decision:** Reject

MY FINAL SCORE: 4.5</score>
MY FINAL DECISION: Reject</decision>