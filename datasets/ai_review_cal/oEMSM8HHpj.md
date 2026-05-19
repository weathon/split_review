- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5
Now I have all the information needed to verify the reviewer claims against the paper. Let me compose the final review.

## Summary

This paper proposes a self-supervised urban visual representation framework that designs three contrastive learning strategies—temporal, spatial, and self (standard data augmentation)—to learn representations specifically tailored to different urban downstream tasks from street view imagery. The core idea is that different contrastive strategies encode different aspects of the urban environment (temporal-invariant built environment features, spatial-invariant neighborhood ambiance, or global scene information). The framework is evaluated on visual place recognition, socioeconomic indicator prediction, and safety perception, with attention-map analysis providing mechanistic evidence for why each strategy suits its target task.

## Strengths

1. **Clear and well-motivated conceptual framework.** The paper articulates three testable hypotheses (temporal invariance for VPR, spatial invariance for socioeconomic prediction, global information for safety perception) and the experimental design directly tests each one. The three hypotheses are grounded in the natural spatiotemporal structure of street view imagery, giving the framework conceptual coherence beyond ad-hoc engineering.

2. **Strong, consistent empirical support for the core thesis.** The experimental pattern is clear and consistent across all three tasks: temporal contrast achieves 100% Recall@K on CrossSeason VPR (Table 1), spatial contrast achieves the highest average R² of 0.5888 on socioeconomic prediction across 18 indicators (Table 2), and self-contrast achieves the highest accuracy of 88.68% on safety perception (Table 3). Each hypothesis is validated by the task where its corresponding strategy performs best.

3. **Mechanistic evidence from attention analysis.** The attention-map visualizations (Figure 2) and attention-distance measurements (Section 4.5) provide interpretable evidence that temporal contrast ignores dynamic objects (even when queried on them), spatial contrast shows broad consistent attention, and self-contrast focuses on individual objects. This goes beyond black-box performance comparison to explain *why* each strategy behaves differently.

4. **Controlled experimental design for internal comparison.** All models use the same ViT-Base backbone, are pre-trained on datasets standardized to 1 million image pairs, and are evaluated with frozen backbones and [CLS] token extraction. This isolates the effect of the contrastive strategy itself from confounding factors like model capacity or evaluation protocol.

## Weaknesses

### Fatal

None.

### Major

1. **Abstract overclaims relative to experimental scope.** The abstract states: *"Our approach significantly outperforms traditional supervised and unsupervised methods in tasks such as visual place recognition, socioeconomic estimation, and human-environment perception."* However, the experiments compare only four models: ImageNet-Self (an unsupervised MoCo v3 baseline), GSV-Self, GSV-Temporal, and GSV-Spatial. No **supervised** method is tested (e.g., Places365, which the paper itself cites as a common approach in the field). No dedicated task-specific methods are included: for VPR (e.g., NetVLAD), for socioeconomic prediction (e.g., Urban2Vec, KnowCL, or the results from Fan et al. 2023 whose dataset is used), or for safety perception (e.g., published results on PlacePlus 2.0). The internal comparison convincingly validates the paper's core thesis that different contrastive strategies suit different tasks, but the broad "outperforms" claim is unsupported and should be scoped to what is actually tested: comparison against a single ImageNet self-supervised baseline and across the paper's own variants. This matters because a reader cannot tell whether the proposed representations are practically competitive with existing approaches for these tasks.

### Minor

1. **No statistical uncertainty reported.** Results in Tables 1, 2, and 3 are reported as point estimates without standard deviations, confidence intervals, or variance across folds/seeds. For socioeconomic prediction, 5-fold cross-validation is mentioned (Section 4.3, line 104) but no fold variance is reported. For VPR, Recall@K is commonly reported without error bars in the literature, but given the paper's claims of significance, some measure of variability would strengthen the results.

2. **Missing random-initialization baseline.** The paper compares pre-trained models against each other but includes no "scratch" baseline (ViT with random weights, no pre-training). Without this, it is impossible to disentangle how much downstream task performance comes from the contrastive pre-training versus the ViT architecture and training setup itself. This would be a simple and informative control.

3. **Underspecified pre-training architecture.** The paper references MoCo v3 settings (Section 4.1, line 70) but does not specify key architectural details: whether a momentum encoder is used, the queue size, the momentum coefficient, the projection MLP architecture, or the exact augmentation pipeline. While the training hyperparameters (optimizer, batch size, learning rate, schedule) are provided, the architectural choices that define the contrastive framework are only referenced by name. For a method paper, this level of underspecification hinders reproducibility.

4. **Imprecise description of pre-training data scale.** Line 64 states *"over 42 million street view images used for pre-training,"* while line 68 clarifies that each contrastive dataset contains 1 million image pairs sampled from this pool. The 42M figure refers to the collection pool, not the training set. This imprecision could mislead a casual reader about the scale of actual training data.

### Trivial

1. The abstract's phrasing should be tempered to match the controlled comparison that is actually conducted.
2. The sample size for the attention distance analysis (Section 4.5) is not stated, making it unclear how broadly the reported patterns generalize across the dataset.

## Nice-to-Haves

- An ablation study varying the number of training pairs (e.g., 100K, 500K, 1M) to show whether performance saturates at the current 1M-pair scale, especially given the 42M-image collection pool.
- A discussion of limitations: e.g., scenarios where temporal contrast may fail (sparse historical images), or where spatial contrast may struggle (highly heterogeneous neighborhoods).
- Comparison of the attention distance metric on a larger, statistically powered sample.

## Removed Points

These points from the input reviews are excluded from the main assessment:

- **"Contrastive learning description confuses distance and similarity"** — REMOVED. The paper describes minimizing distance conceptually (line 38), then provides the exact InfoNCE loss with temperature τ (lines 40-44). This is standard pedagogical language; the mathematical formulation is correct and complete.
- **"Missing related works"** — REMOVED. The paper cites Urban2Vec and KnowCL in Section 2.3 and explicitly contrasts with them. The rule prohibits flagging missing citations without external verification.
- **Several method underspecification concerns (shooting angle determination, buffer zone counts, sampling procedures)** — REMOVED. The paper explicitly refers to Appendix Sections A.1 and A.2 for data collection details. The appendix is stripped by the parsing pipeline; these details exist in the original submission per the rules.
- **"42M figure is misleading" as an independent weakness** — MERGED into Minor weakness 4 above (treated as imprecision rather than a separate critique).
- **Generic "evaluation lacks rigor" / "comparison unfair" sweeps** — REMOVED where they lacked concrete anchors in the paper. The remaining Major weakness captures the specific overclaim issue with direct quotes from the abstract.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's internal and external validity. The internal comparison is well-designed and produces clean, interpretable results that convincingly validate the conceptual framework. However, the external framing (both in the abstract's language and in the absence of task-specific baselines) creates a gap between what the paper demonstrably proves and what it claims. This gap is common in representation learning papers that focus on comparing strategies within a family rather than benchmarking against the full literature, but it is particularly salient here because the abstract explicitly invokes "traditional supervised and unsupervised methods." A productive framing would be to present the work as a systematic **ablation study of contrastive strategies for street view representation** rather than as a claimed performance improvement over all prior work.

## Suggestions

1. **Scope the claims precisely.** Replace the abstract's "significantly outperforms traditional supervised and unsupervised methods" with language that describes the internal comparison: e.g., "We systematically compare three contrastive strategies and show that different strategies learn features suited to different urban tasks, outperforming an ImageNet-pretrained self-supervised baseline by a substantial margin on each task."
2. **Add statistical reporting.** Report standard deviations across cross-validation folds for socioeconomic R² values, and ideally report results across multiple random seeds for VPR and safety perception.
3. **Consider adding one key external baseline per task** to connect to the literature: NetVLAD for VPR, Places365 or the Fan et al. (2023) reported numbers for socioeconomic prediction, and a published result for PlacePlus 2.0 safety perception.
4. **Add a random-initialization baseline** to quantify the benefit of pre-training itself.
5. **Specify the MoCo v3 architecture details** (queue size, momentum, projector MLP) either in the main text or by providing a reference with the specific configuration used, to ensure reproducibility.
