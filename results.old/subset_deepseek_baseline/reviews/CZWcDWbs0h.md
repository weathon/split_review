## Summary

The paper proposes ALiRAS, a multi-view representation learning approach for audio deepfake detection that integrates automatically-labeled expert-informed phonetic and phonological features (breath, pitch anomaly, audio quality) with foundation models (XLSR-Wav2vec, HuBERT, WavLM). The method aims to simultaneously improve explainability (via SHAP on the linguistic features), scalability (31% time reduction through a cost-efficient ensemble that uses the lightweight ALiRAS model as a first-pass filter), and effectiveness (maintaining or improving EER on the XLSR baseline).

## Strengths

- **Interdisciplinary novelty**: The paper bridges sociolinguistic expertise with deep learning for ADD, exploring expert-informed features that are rarely studied in this domain.
- **Practical multi-objective framing**: Addresses explainability, scalability, and effectiveness together, which is more realistic than focusing on accuracy alone.
- **Transparent auto-labeling pipeline**: The use of a small expert-labeled dataset (840 samples) to fine-tune a lightweight VGGish model for auto-labeling linguistic features is a reasonable strategy to scale expert knowledge.
- **Informative cost-efficient ensemble**: The two-stage filtering approach (ALiRAS first, foundation model only on uncertain samples) provides a clear path to speed up inference for real-time or large-scale deployment.

## Weaknesses

### Fatal

None.

### Major

- **Misleading effectiveness claim**: The abstract states “decreased the Equal Error Rate of this baseline model in audio deepfake detection with at least 7%”, but this only holds for the XLSR-ResNet18 baseline. The HuBERT-ResNet18 baseline already achieves EER=0.171, and the ALiRAS ensemble does not improve it (EER=0.171). The 7% figure is relative and applies only to one of three baselines.
- **Suspiciously high XLSR-ResNet18 EER**: In Table 5, XLSR-ResNet18 has EER=0.400, which is much worse than HuBERT (0.171) and WavLM (0.277). This is unusual for a strong foundation model and suggests possible issues in the experimental setup (e.g., hyperparameters, data split, or feature extraction). The paper does not discuss this anomaly.
- **Modest auto-labeling accuracy**: The VGGish auto-labeler achieves only 0.71 ROC AUC on the expert-labeled dataset (Table 2). The paper does not evaluate the quality of auto-labeled features on the large-scale dataset (e.g., by sampling and human validation nor by comparing ADD performance using ground-truth expert labels vs. auto-labels). Noise in the auto-labeled features may be propagated and could partly explain the limited gains on HuBERT/WavLM.
- **Shallow explainability evaluation**: The SHAP analysis is limited to one example and global mean values. The paper does not show whether the SHAP explanations are consistent with expert knowledge, how they vary across attack types, or whether they provide actionable insights beyond the three predefined features. The claim of “first expert-in-the-loop explainability for ADD” is overstated since SHAP itself is standard and the novelty is in the features, not the explanation method.
- **Lack of statistical rigor**: Results are reported from a single run without confidence intervals, standard deviations, or error bars. The 31% time reduction and EER comparisons cannot be assessed for robustness.

### Minor

- The paper uses “expert-in-the-loop” but the loop is one-time (initial labeling + fine-tuning), not an interactive process—this could be clarified.
- The 0.55 threshold for the cost-efficient ensemble is chosen empirically without discussion of sensitivity or generalizability to other datasets.
- The fraction of data that actually reaches the second-stage foundation model in the cost-efficient ensemble is not reported, making it hard to evaluate the claim beyond total time reduction.

### Trivial

None.

## Nice-to-Haves

- Validate a random sample of auto-labeled features on the large-scale dataset by human experts.
- Provide per-sample or per-attack-type time savings in the cost-efficient ensemble.
- Report results with multiple runs (seeds) to establish variance.

## Novel Insights

None beyond the paper’s own contributions.

## Suggestions

1. **Clarify the effectiveness claim**: Specify that the 7% EER decrease is relative and applies only to the XLSR-ResNet18 baseline. Provide a clear comparison table showing absolute and relative improvements for each baseline.
2. **Investigate and explain the XLSR EER=0.400 result**: Check if the ResNet18 architecture or training procedure is suboptimal for XLSR embeddings; consider using the same downstream classifier for all foundation models or reporting best-known results from literature.
3. **Evaluate auto-labeling quality on the large dataset**: Sample 100–200 files from the large-scale dataset, have experts label them linguistically, and compare to ALiRAS outputs. Report agreement and its impact on ADD performance.
4. **Strengthen explainability evaluation**: Show SHAP values broken down by attack type, compare SHAP-based feature importance with expert intuition, and include more diverse examples (including misclassified samples).
5. **Add error bars and significance tests**: Run each experiment at least 3 times with different seeds and report mean ± std for EER and AUC.

## Score and Decision

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>