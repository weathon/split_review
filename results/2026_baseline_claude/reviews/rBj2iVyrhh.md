## Summary

This paper proposes **Classifier-Constrained Alternating Training (CCAT)**, a two-stage framework for addressing modality imbalance in multimodal learning. The key insight is that existing alternating training methods reduce encoder-level gradient interference but leave the shared classifier biased toward dominant modalities that converge faster. Drawing an analogy to class imbalance remedies, CCAT (1) pre-trains a balanced shared classifier using bidirectional cross-attention with a mutual-information-based modality contribution regularizer, (2) freezes this classifier as a stable anchor during modality-alternating encoder training, with lightweight per-modality LoRA adapters bridging the distribution gap, and (3) performs secondary updates on samples with extreme contribution imbalance. Results on CREMA-D, Kinetics-Sound, and MVSA show consistent SOTA improvements.

---

## Strengths

- **Compelling empirical motivation.** Figure 1 concretely demonstrates that MLA-style alternating training barely reduces contribution imbalance (0.90/0.10 at epoch 100 vs. 1.00/0.00 at epoch 0), establishing the existence of a classifier-level bias problem that prior work overlooked.

- **Theoretically grounded analogy.** The gradient dynamics analysis in Section 3.1 unifies class imbalance and modality imbalance under a shared "early-dominance → gradient suppression → representation degradation" cycle. While simplified, the mathematical framing (Eqs. 1–3) is coherent and provides non-trivial insight motivating the design of a frozen classifier.

- **Strong and consistent empirical gains.** CCAT achieves +1.35% (CREMA-D), +6.76% (KS), and +1.92% (MVSA) over prior SOTA. The +6.76% improvement on KS is large and difficult to dismiss as noise, especially averaged over three random seeds. The method tops all baselines across unimodal and multimodal metrics in most configurations.

- **Comprehensive ablation.** Table 2 systematically removes each of the four components (Fix, Alt, Sec, LoRA) and shows meaningful degradation in every case, confirming that the full system is not dominated by a single trick. The classifier-freezing component produces the largest individual gain (~2.83% multimodal on CREMA-D).

- **Quantitative t-SNE analysis.** The paper reports Calinski-Harabasz, Silhouette, and Davies-Bouldin scores (Figure 5), grounding the qualitative visualization in concrete clustering metrics (CH: 198.98 → 242.55; DB: 1.42 → 1.28), which confirms that the fixed classifier yields more discriminative feature representations.

---

## Weaknesses

### Fatal
None.

### Major

1. **Theoretical analysis does not fully match the actual architecture.** Section 3.1 models fused features as a weighted sum $f = \gamma_1 f^{(1)} + \gamma_2 f^{(2)}$ and then approximates the gradient under imbalance (Eq. 3). However, the pre-training stage uses bidirectional cross-attention fusion, which is highly non-linear and non-separable. The "implicit utilization coefficients" γ₁, γ₂ are not directly observable in cross-attention, so the gradient approximation is at best heuristic. The theoretical connection motivates the intuition but does not constitute a proof of classifier bias in the actual architecture used.

2. **Hyperparameter sensitivity and selection protocol.** The optimal threshold β varies from 0.05 (MVSA) to 0.15 (CREMA-D) to 0.30 (KS), and performance is sensitive to the choice (e.g., CREMA-D drops from 85.89% at β=0.15 to 84.14% at β=0.20). No principled criterion exists for selecting β; it requires a validation-set grid search. Combined with the LoRA rank r, this introduces two dataset-specific hyperparameters with non-trivial tuning cost, which could limit practical adoption without a held-out set.

3. **Distribution mismatch between pre-training and alternating stages is incompletely analyzed.** The pre-trained classifier is optimized for cross-attention fused features, but during alternating training it receives unimodal features. The paper correctly identifies this mismatch (Section 3.3) and proposes LoRA to bridge it, but provides no ablation on whether the pre-training fusion architecture (bidirectional cross-attention vs. simpler fusion) affects downstream performance, nor whether LoRA rank sufficiently captures the gap.

### Minor

1. **LFM baseline missing on MVSA without explanation.** Table 1 shows "-" for LFM on MVSA. Since this is the next strongest baseline and the gain on MVSA is the smallest (1.92%), clarity on why LFM is absent would strengthen the comparison.

2. **Secondary update selection criterion lacks principled basis.** The criterion $c_i^m < \beta$ flags samples where modality m contributes below a threshold as "extremely imbalanced." However, this is a global threshold applied uniformly across all samples, not adapted to per-class or per-dataset distributional properties.

3. **Scalability to 3+ modalities is acknowledged but unaddressed.** The "Future Work" section admits the method has only been tested bimodally. The alternating schedule and the MI-based contribution computation scale quadratically or worse with more modalities, which the paper does not analyze.

### Trivial

- The paper counts four contributions (i–iv in the introduction) but the fourth ("faithfully") appears to be a parser artifact.
- Figure 1 caption mentions "Ours" showing stronger imbalance than MLA, but this refers to the more balanced end state (0.65/0.35 vs. 0.90/0.10) — the opposite of "more imbalanced." The caption framing is slightly confusing.

---

## Nice-to-Haves

- An ablation replacing bidirectional cross-attention in pre-training with simple sum fusion would clarify whether the balanced classifier requires a sophisticated fusion mechanism or whether the regularization term alone is the key driver.
- A wall-clock time comparison with baselines would clarify the overhead introduced by the two-stage procedure and secondary updates.
- Experiments with stronger encoders (e.g., ViT-based models) would test whether the gains persist at larger scales.

---

## Novel Insights

The most genuinely novel contribution is the **gradient-level isomorphism between class imbalance and modality imbalance**: both exhibit a recursive early-dominance cycle in which the classifier's weight updates become dominated by one component (majority class / dominant modality), suppressing gradient signals for the weaker component and entrenching the structural bias. Importing the fixed-classifier strategy from long-tail class imbalance literature into alternating multimodal training is a non-obvious cross-domain transfer. The use of per-modality LoRA adapters as distribution adapters on a frozen classifier—rather than fine-tuning the classifier itself—is also a practically elegant solution that preserves the unbiased decision boundary while allowing modality-specific adaptation.

---

## Suggestions

- Provide an ablation on the contribution of the bidirectional cross-attention versus simpler pre-training fusion (e.g., sum fusion with the same regularization term) to isolate the effect of the regularizer from the fusion architecture.
- Report variance across seeds alongside mean accuracy in Table 1 to contextualize the significance of the reported gains.
- Include a study of the MI computation cost during secondary update identification, since this is applied at every epoch and may be expensive at scale.
- Clarify Figure 1's caption — "Ours" lines show better balance (0.65/0.35), not more imbalance; the current caption could be misread.

---

## Score and Decision

The paper addresses a real and underexplored gap — classifier bias in alternating multimodal training — with a motivated method that combines pre-trained frozen classifiers, LoRA adapters, and sample-level reweighting. The theoretical analogy to class imbalance is insightful and lends principled motivation. The empirical results are substantial (especially the 6.76% gain on KS) and verified with ablations and clustering metrics. The main limitations are a theoretical analysis that does not precisely match the implemented architecture and two sensitive hyperparameters requiring dataset-specific tuning. These are meaningful but do not invalidate the core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>