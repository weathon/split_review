## Summary
TSPulse is a family of ultra-compact (1M parameters) pre-trained time-series models that introduces disentangled masked reconstruction across multiple representation spaces (temporal and spectral) and abstraction levels (fine-grained and semantic). By assigning distinct training objectives to different embedding segments—time patch tokens, FFT tokens, and vision-inspired register tokens—TSPulse produces three complementary embedding views that can be selectively combined via lightweight post-hoc fusers (Multi-Head Triangulation for anomaly detection, TSLens for classification). The paper reports strong gains across four diagnostic tasks: anomaly detection, classification, imputation, and similarity search, often surpassing models 10–100× larger.

---

## Strengths

- **Impressive efficiency-performance trade-off.** A 1M-parameter model achieves state-of-the-art on the TSB-AD leaderboard (VUS-PR 0.52 univariate, 0.39 multivariate), UEA classification (0.733 mean accuracy), and similarity search (0.68 PREC@3), outperforming 40M–340M-parameter baselines. The CPU-friendly inference enables deployment scenarios where GPU-based models are infeasible.

- **Concrete disentanglement evidence.** Table 2 quantitatively shows expected behavioral differences: temporal embeddings are highly sensitive to phase shifts (130% distortion), FFT embeddings show moderate phase sensitivity (21%), and semantic register embeddings are most robust to all perturbations (12% phase shift, 4.6% missingness distortion). This directly motivates the downstream task routing strategy.

- **Practical novelty in hybrid masking.** The choice to define mask tokens at the raw patch level rather than embedding space is technically clean and allows a single learnable token to support both full and partial patch masking. The ablation in Table 1(c) confirms a massive 79% degradation when using only block masking during pre-training, validating this design choice's importance for real-world imputation scenarios.

- **Thorough ablation coverage.** Table 1 provides ablations across all four tasks, individually isolating disentanglement (short/long embeddings), TSLens vs. pooling, dual-space learning, hybrid masking, and identity initialization of channel mixers—each showing meaningful contributions (7–16% drops when removed), giving confidence that all design elements earn their place.

- **Adaptation of register tokens to time-series.** Borrowing register tokens from vision transformers (DINOv2-style) and training them via a semantic frequency-signature objective is a creative cross-domain idea that appears to work well for robustness to distortions.

---

## Weaknesses

### Fatal
None.

### Major

1. **"Zero-shot" anomaly detection uses a labeled tuning set.** The paper explicitly states that a small official labeled tuning set is used to select the best-performing head (Head_triang.). This is effectively supervised model selection, yet the results are labeled TSPulse (ZS). While all TSB-AD leaderboard methods have access to this tuning set, the paper's framing conflates "zero-shot" (no target domain data) with "head selection using labeled supervision." The discrepancy is particularly notable given the +33% improvement claimed over SubPCA in zero-shot; it is unclear whether non-pre-trained baselines enjoy an equivalent model selection step or use it differently.

2. **Fine-tuned imputation ties with linear interpolation.** Table in Figure 6 shows TSPulse (FT) achieves MSE=0.039, identical to simple linear interpolation (0.039). The paper does not acknowledge this, yet it significantly undermines the practical significance of the fine-tuning contribution for imputation. The zero-shot result (0.074) is genuinely strong, but fine-tuned TSPulse offers no advantage over a parameter-free baseline.

3. **Similarity search evaluation is narrow and potentially self-confirming.** Only two baselines (MOMENT, Chronos) are compared on a custom evaluation protocol that uses augmentation distortions (time shifts, magnitude changes, noise) that are precisely the same perturbations TSPulse's semantic embedding was designed to be robust to. There is no independent held-out evaluation with naturally-occurring distortions, and no comparison to classical approaches (e.g., learned metric embeddings, shapelet-based methods) or stronger alternatives like TNC or TS2Vec embeddings for retrieval.

4. **Classification baseline set omits strong competitors.** The 5–16% gains over VQShape and MOMENT are notable, but the paper omits high-performing time-series classification methods like ROCKET, Hydra, or InceptionTime, which routinely achieve top-tier performance on the UEA archive. Without these comparisons, the state-of-the-art claim for classification is overstated.

### Minor

1. **Task-specific pre-training creates separate models per task.** TSPulse reweights loss objectives to specialize for each task, implying separate pre-trained checkpoints are maintained for each task. This overhead is not highlighted in the efficiency discussion and reduces the universality claim compared to a single general-purpose model.

2. **TSLens mechanism underspecified.** TSLens is described as a "gated attention module" that "selectively attends to features," but the mechanism—how gating weights are learned and what they gate over—is not detailed in the main paper. The improvement over average/max pooling (11–16%) is significant enough to warrant clearer exposition.

3. **Sensitivity analysis uses synthetic signals only.** The disentanglement analysis in Section 6 and Table 2 uses controlled synthetic experiments. While informative, it would be more convincing to also show distortion patterns on real downstream datasets.

### Trivial
None.

---

## Nice-to-Haves

- Add a comparison to ROCKET/Hydra on UEA classification to anchor the state-of-the-art claim.
- Acknowledge and discuss the linear interpolation parity on fine-tuned imputation.
- Include at least one additional retrieval baseline (e.g., TS2Vec or TNC embeddings) in similarity search.
- Clarify that TSPulse-ZS on anomaly detection uses labeled head selection, and distinguish this from truly unsupervised zero-shot settings.
- Report per-dataset classification results on the full 85-dataset UEA archive (not just 29 datasets) to enable reproducibility and fair comparison.

---

## Novel Insights

The most genuinely novel architectural insight is the use of vision-transformer register tokens as semantic embedding slots in a time-series pre-training context, trained exclusively via a semantic frequency-signature objective (softmax over log-magnitude spectrum). This creates a natural information bottleneck where global spectral semantics are compressed into a small fixed-dimensional representation, decoupled from the reconstruction objectives applied to patch tokens. The emergent invariance to time shifts, noise, and magnitude—properties that are not explicitly enforced but arise from the structural separation of objectives—provides a principled explanation for why these embeddings are superior for retrieval tasks. The complementary insight that different embedding segments can serve different downstream tasks through lightweight post-hoc fusers, without modifying the shared backbone, is a clean architectural pattern with potential applicability beyond time series.

---

## Suggestions

- **Clarify zero-shot definition:** Introduce terminology to distinguish "label-free inference" from "label-free inference + labeled head selection," and use it consistently.
- **Add interpolation comparison in the abstract:** The abstract's "+50% on imputation" refers only to the zero-shot regime; clarify scope.
- **Provide dataset selection justification for classification:** Explain why 29 of the 85 UEA datasets were selected to enable replication and address selection bias concerns.
- **Extend similarity search with natural distortion data:** Evaluate on a benchmark where distortions arise naturally (e.g., UCR anomaly or the TSER archive) rather than only synthetic augmentations.

---

## Score and Decision

TSPulse delivers genuine practical value: a deployment-ready, CPU-friendly 1M-parameter model that meaningfully outperforms much larger systems on multiple established benchmarks. The architectural ideas—register-token-based semantic disentanglement, hybrid patch-level masking, multi-head triangulation—are well-motivated and empirically validated. The ablations are comprehensive. The primary concerns (zero-shot definition for AD, imputation tie with interpolation, narrow similarity search evaluation, missing classification baselines) are real but do not invalidate the core contributions; they suggest the paper's framing of certain results is more optimistic than warranted. This is a solid applied ML contribution that the community will find useful, but not a breakthrough result.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>