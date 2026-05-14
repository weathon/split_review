Now I'll write the comprehensive consolidated review.

---

## Summary

This paper proposes Classifier-Constrained Alternating Training (CCAT), a two-stage framework for mitigating modality imbalance in multimodal learning. Stage 1 pretrains an unbiased shared classifier using bidirectional cross-attention fusion with a contribution-regularization term. Stage 2 freezes this classifier and performs modality-wise alternating training, where only one modality's encoder and a lightweight LoRA adapter are updated per iteration, with additional sample-level secondary updates for severely imbalanced samples. The method is evaluated on CREMA-D, Kinetic-Sound, and MVSA benchmarks, demonstrating consistent improvements over prior methods.

## Strengths

- **Clear empirical motivation**: Figure 1 tracks modality contribution values through MLA training, revealing that even with alternating encoder optimization, a persistent classifier bias remains (contribution disparity only reduces from 1.00 → 0.92). This directly motivates the classifier-level intervention that is the paper's core contribution.

- **Well-structured ablation study**: Table 2 systematically removes classifier freezing, alternating training, secondary updates, and LoRA modules. Each removal degrades multimodal performance (e.g., CREMA-D drops from 85.89% to 82.80% without freezing, 81.45% without alternating training, 83.06% without secondary updates, 84.68% without LoRA), providing direct evidence that all components contribute meaningfully.

- **Strong empirical results**: CCAT achieves state-of-the-art performance across three diverse benchmarks (audio-visual emotion recognition, audio-visual action recognition, image-text sentiment analysis), covering different modality combinations and imbalance patterns.

- **Clean two-stage design**: The idea of pretraining an unbiased classifier and then freezing it as a stable decision anchor during alternating training is conceptually clean and well-motivated by the class-imbalance analogy. The integration of LoRA adapters to handle the distribution shift between fused pretraining features and unimodal alternating-training features is a sensible design choice.

- **Quantitative and qualitative feature-space analysis**: t-SNE visualizations with Calinski-Harabasz, Silhouette, and Davies-Bouldin scores show that CCAT's frozen classifier produces more discriminative feature representations with better intra-class compactness and inter-class separation compared to MLA and a non-fixed variant.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Theoretical section overclaimed**: Section 3.1 claims a "profound theoretical isomorphism" and a "new theoretical framework," but the analysis amounts to rewriting gradient expressions under one-sided dominance for both class and modality imbalance and observing that both involve gradient suppression and a vicious cycle. This is a motivational analogy rather than a rigorous theoretical contribution, and the method design (freezing a classifier) is imported from class-imbalance literature rather than derived from the gradient analysis. The inflated framing weakens an otherwise solid empirical paper.

- **Inference fusion mechanism not specified**: The paper states that unimodal predictions "are fused at the decision level for final output" (Section 3.3) but never specifies whether this uses simple averaging, weighted averaging, learned weights, or another scheme. While the specific choice (likely simple averaging, given the method's design) is unlikely to change conclusions, this omission prevents full reproducibility and should be clarified.

### Trivial

- **No sensitivity analysis for λ**: The contribution-regularization coefficient λ is set to 0.001 without ablation or justification. Since this term penalizes contribution disparity during classifier pretraining, its value could meaningfully affect the "unbiasedness" of the frozen classifier.

- **Cross-attention pretraining not isolated**: The bidirectional cross-attention fusion module used in Stage 1 pretraining is more expressive than the simple fusion operations in some baselines. While this is part of the method (not a confound — the paper's contribution is the full pipeline), adding a baseline that uses the same cross-attention pretrained backbone with standard joint training would have strengthened the claim that the alternating+freezing strategy (rather than the pretraining architecture) drives the gains.

## Nice-to-Haves

- A baseline combining the cross-attention pretrained classifier with standard joint training (without alternating or freezing) would cleanly isolate the contribution of CCAT's Stage 2 training strategy from the Stage 1 pretraining architecture.
- Reporting the performance of the cross-attention fusion model *as-is* after pretraining (before any alternating training) would reveal the performance floor and help readers understand how much the alternating stage adds.
- Qualitative examples showing cases where a weak modality's contribution increased after CCAT training compared to a baseline would help illustrate the bias-mitigation effect.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

**Removed: "Unequal evaluation protocol — CCAT uses decision-level fusion while all baselines use feature-level fusion."** The paper explicitly states (line 503-504) that "For MLA, MMPareto, LFM, and our method CCAT, unimodal results are directly acquired from decision-level fusion outputs." MLA, MMPareto, and LFM are listed as baselines (line 443-444) and all use decision-level fusion, making the comparison protocol fair. The critic appears to have missed these baseline rows from Table 1 (likely a parser artifact in the extracted PDF).

**Removed: "The gap between CCAT and OGM-GE (85.89 vs 68.14 on CREMA-D) is implausibly large."** OGM-GE is a feature-level fusion method, not the best prior. The abstract reports +1.35% improvement on CREMA-D, indicating the best decision-level fusion baseline (MLA or similar) achieves ~84.54%. The 68.14 from OGM-GE is not the relevant comparison point.

**Removed: "Multimodal accuracy (85.89%) far exceeding the best single modality (73.79%) cannot be achieved by trivial averaging."** This is incorrect as a general claim — multimodal fusion routinely exceeds the best unimodal accuracy when modalities provide complementary information with uncorrelated errors. Simple averaging can and does achieve this.

**Removed: Strength about "theoretical grounding via gradient dynamics analysis."** This is the same point flagged as overclaimed in the Weaknesses section. The gradient analysis is a motivational analogy, not rigorous theory.

**Removed: Strength that "this paper addressed an important problem" or "this paper targeted an interesting question."** Generic, superficial praise without concrete evidence.

## Novel Insights

The key insight emerging from the reviews is that the paper's Figure 1 — showing persistent classifier bias even under alternating encoder training — is genuinely valuable beyond the paper's own method. It provides empirical evidence that prior alternating training approaches (MLA) only partially address modality imbalance because they leave the classifier free to develop structural preferences. This observation, combined with the ablation showing that classifier freezing alone contributes ~3% accuracy on CREMA-D, suggests that classifier-level intervention may be a broadly applicable principle for multimodal imbalance beyond CCAT's specific instantiation.

## Suggestions

- Tone down the theoretical claims in Section 3.1. Present the gradient analysis as motivation/analogy rather than a "profound theoretical isomorphism" or "new theoretical framework." The method stands on its own empirical merits.
- Specify the exact decision-level fusion mechanism used during inference (e.g., "predictions from each modality are averaged").
- Add a brief note (even one sentence) on why λ = 0.001 was chosen, or note that moderate variation does not affect results.
- Consider adding the cross-attention-only baseline (pretrained classifier used directly for multimodal prediction) as a reference point in Table 1 or the ablation to help readers calibrate where gains come from.

---

## Score and Decision

### Anchor Comparison

- **ProMoBal** (`/home/wg25r/review_agent/human_reviews_2026/EIdbBjL6mJ.md`, avg 3.00, Reject): A modality balancing method with confusing presentation, unclear method design, and multiple serious weaknesses. CCAT is substantially stronger in method clarity, ablation rigor, and empirical validation.

- **GOAL** (`/home/wg25r/review_agent/human_reviews_2026/I3uFqoUZ2Y.md`, avg 4.50, Reject): A gradient-based modality balancing method with solid theoretical motivation and good experiments. CCAT is comparable in empirical quality but has a less rigorous theoretical foundation.

- **Intermediate Fusion IID** (`/home/wg25r/review_agent/human_reviews_2026/5bxmmuRhO6.md`, avg 4.50, Accept Poster): A theory-driven IF method with limited experimental comparisons. CCAT has broader experimental coverage and more thorough ablations but weaker theoretical analysis. Comparable overall.

- **Loss Landscape DML** (`/home/wg25r/review_agent/human_reviews_2026/cYZkZp3m8F.md`, avg 5.00, Reject): Good theoretical framework with a simple method but small-scale experiments. CCAT has more comprehensive empirical validation but less theoretical depth.

- **Compose and Fuse** (`/home/wg25r/review_agent/human_reviews_2026/oIvIsK5AwB.md`, avg 5.50, Accept Poster): A novel evaluation framework for multimodal reasoning with strong analysis and interventions. More novel and better executed than CCAT. CCAT does not reach this level.

CCAT sits between the 4.50 and 5.00 anchors: it has stronger experiments than the Intermediate Fusion paper (4.50, Accept) and the Loss Landscape paper (5.00, Reject), but weaker theoretical contributions. The method is clean, well-ablated, and the empirical results are convincing. The main weaknesses (overclaimed theory, underspecified fusion) are addressable and do not threaten the core contribution.

**Decision: Borderline Accept (Poster).**

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>