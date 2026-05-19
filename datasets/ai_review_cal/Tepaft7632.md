- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 3, 6, 5, 5
Now I have a clear picture of the paper. Let me write the consolidated review.

## Summary

This paper proposes MADCluster, a framework for unsupervised time-series anomaly detection that learns a normal-data cluster center dynamically via a self-supervised clustering module, avoiding both hypersphere collapse and the expressiveness limitation of fixed centers. The method combines a neural Base Embedder (D-RNN), a Cluster Distance Mapping loss, and a Sequence-wise Clustering module with a novel One-directed Adaptive loss. Experiments on four benchmark datasets report F1 improvements when MADCluster is applied to 11 diverse baseline models.

---

## Strengths

1. **Novel approach to learning cluster centers for one-class anomaly detection**: The paper identifies a genuine limitation of DeepSVDD — that fixing the center to avoid collapse limits representational power — and proposes a self-supervised clustering mechanism to learn the center dynamically. This is a well-motivated architectural contribution.

2. **Empirically consistent F1 improvements on neural baselines**: On 7 neural baselines (USAD, Anomaly Transformer, DCdetector, DeepSVDD, ITAD, THOC, D-RNN), applying MADCluster yields higher F1 on all four datasets (Table 1). For example, D-RNN on MSL improves from 81.24 to 94.84 F1. The pattern is consistent and non-trivial in magnitude.

3. **Qualitative evidence of single-clustering convergence**: Figure 4 shows that over 300 epochs, MADCluster's hidden embeddings converge toward a single center (82.4% of normal data within 3σ at epoch 300), while DeepSVDD forms multiple clusters away from its fixed center. Figure 5 empirically validates that the One-directed threshold ν increases and converges as intended across all datasets.

4. **Self-adjusting threshold mechanism**: The One-directed Adaptive loss (Eq. 6) is designed so that ν automatically increases during training, tightening the decision boundary. Figure 5 confirms this behavior empirically — a non-trivial design target that the paper achieves.

---

## Weaknesses

### Fatal
None.

### Major

1. **Integration protocol for non-neural baselines is unspecified, undermining claimed comparisons (Table 1).**  
   The paper states it "appl[ies] MADCluster to 11 baseline models" (line 161), including non-neural methods (LOF, OC-SVM, IsolationForest, VAR). However, MADCluster's architecture (Figure 1, Algorithm 1) requires a neural Base Embedder that outputs embeddings `h_t^f`. The paper never explains how the pipeline is instantiated for models that lack a trainable feature extractor. If the "after" version uses D-RNN features + MADCluster while the "before" version uses raw features, the comparison is not apples-to-apples. This does not invalidate the neural-only results (7 of 11 baselines), but the claimed "model-agnostic" improvements across all 11 models cannot be assessed without a transparent integration protocol.  
   *(Anchored to: Section 4.2 baselines list, Section 4.3 Table 1 description, Section 3.1 Figure 1, Algorithm 1.)*

2. **No ablation study isolating the contributions of the two loss terms and the dynamic center.**  
   The method jointly optimizes L_distance (Cluster Distance Mapping) and L_cluster (Sequence-wise Clustering). The paper provides no comparison against (a) MADCluster with a fixed center (to isolate the benefit of learning the center), (b) MADCluster without L_distance, or (c) MADCluster without L_cluster. Without ablations, it is unclear whether the dynamic center, the clustering loss, or their combination drives the improvements.  
   *(Anchored to: Section 4 — no ablation section exists; Section 3.1.2–3.1.3 defines the two losses but they are not independently evaluated.)*

3. **Model-agnosticism is claimed but only one Base Embedder architecture (D-RNN) is tested.**  
   The paper states "model-agnostic characteristics are achieved by applying various architectures to the Base Embedder" (abstract) and that MADCluster "can be applied to various deep learning architectures" (line 32). However, every experiment uses D-RNN as the Base Embedder. To substantiate model-agnosticism, results with at least one alternative Base Embedder (e.g., LSTM, Transformer) on a common dataset are needed.  
   *(Anchored to: Section 3.1.1 — "In the Base Embedder, we use the Dilated Recurrent Neural Network (D-RNN) as the base model"; Table 1.)*

### Minor

4. **The One-directed Adaptive loss function has unaddressed mathematical and differentiability issues.**  
   - The argument of the first log in Eq. 6 is `(1-ν^{1-ν})/(1-ν)·(q_t-1) + 1`. Since `q_t-1 ≤ 0`, the expression could become non-positive for some `(q_t, ν)` without explicit constraints, making the log undefined. The paper states no constraints guaranteeing positivity.  
   - The hard thresholding `p_t = 1 if q_t ≥ ν else 0` (Eq. 8) introduces a non-differentiable boundary. The paper mentions label smoothing in Section 4.2 (experiments) as a fix for over-confidence, but does not discuss how gradients flow through the hard decision in the method's forward pass (e.g., straight-through estimator, stop-gradient).  
   *(Anchored to: Eq. 6, Eq. 8, Section 4.2 label-smoothing description.)*

5. **The paper reuses the symbol ν for two different purposes without clarification.**  
   In Section 3.1.2 (line 64), `ν` is mentioned as the hyperparameter determining the radius `R` via a quantile of network outputs. In Section 3.1.3, `ν` is the One-directed threshold in the clustering loss. The paper does not state whether these are the same hyperparameter or distinct ones with the same name, making the method ambiguous.  
   *(Anchored to: Section 3.1.2 line 64, Section 3.1.3 Eq. 8.)*

6. **No hyperparameter sensitivity analysis.**  
   The method introduces several hyperparameters (ρ, λ, τ, initial ν, the quantile for R). None are analyzed for sensitivity. Given the complexity of the joint loss function, it is unclear how stable the reported results are to hyperparameter choices.  
   *(Anchored to: Section 3.1.2: ρ, λ; Section 4.2: τ; Section 4.2 mentions no sensitivity study.)*

### Trivial

7. **The description of the point-adjustment protocol (Section 4.2) states it is used for MADCluster but does not explicitly confirm it is applied identically to all "before" baselines.** While the paper says it "aligns with a widely-adopted adjustment strategy" and follows "established protocols," a direct statement would remove ambiguity.

---

## Nice-to-Haves
- Report standard deviations or run-to-run variance for the key results in Table 1, as is common in deep learning benchmark evaluations.
- Provide runtime or parameter-count comparison to support the claim that MADCluster is "lightweight."
- Clarify the train/validation/test split (Section 4.1 mentions "20% of the training data was used for evaluation" but does not specify whether this is a held-out validation set drawn from the training portion).

---

## Removed Points

- **"The mathematical proof is relegated to the (missing) appendix."** — Removed per rule: the parser strips appendix sections from all papers; the proof is assumed to exist in the original submission.
- **"Results are suspiciously uniform and likely artifacts of an unfair protocol."** — Removed as speculative. The uniform improvement pattern is not inherently suspicious; it could indicate a genuinely effective method. The underlying concern about protocol clarity is retained in Major #1.
- **"The paper conflates hypersphere collapse with limited representational power."** — Removed. The paper explicitly distinguishes these: it notes that fixing the center *avoids* collapse (line 28) but *limits* expressiveness (line 137). This is correctly framed.
- **"DeepSVDD comparison does not demonstrate collapse vs. no collapse."** — Removed. The paper compares MADCluster (dynamic center) against DeepSVDD (fixed center) and shows MADCluster converges to a tighter single cluster. This is a valid comparison that supports the paper's claim about expressiveness, even if the word "collapse" is used somewhat loosely.
- **Strength Finder's strengths #1 and #3 as stated in the original** — Partially moderated (the "model-agnostic" claim is retained as a net-weakness in Major #3; the consistent improvement is retained as Strength #2 but scoped to neural baselines).

---

## Novel Insights

The most interesting observation from the reviews — which does not appear in the paper itself — is that the paper's central empirical table (Table 1) implicitly contains a natural experiment: the "before" baselines span fundamentally different methodological families (reconstruction, density estimation, clustering, autoregressive), yet MADCluster improves all of them. If the integration protocol is clean (i.e., the same D-RNN features are used in both "before" and "after" for non-neural baselines, or non-neural baselines are excluded), this would suggest that the dynamic-center + clustering-loss recipe is complementary to a remarkably broad set of existing approaches — perhaps because the limitation MADCluster addresses (center expressiveness) is orthogonal to the inductive biases of those methods. This is worth drawing out explicitly if the authors clean up the experimental description. Conversely, if the protocol is not clean, the table loses its evidential value.

---

## Suggestions

1. **Specify the integration protocol for every baseline.** Provide a table or pseudocode showing exactly how MADCluster attaches to each model, especially non-neural ones. If non-neural baselines cannot be fairly integrated, remove them from the comparison or use a common D-RNN feature extractor for both "before" and "after" conditions.
2. **Add an ablation study:** (a) MADCluster with fixed center vs. learned center; (b) L_distance alone; (c) L_cluster alone. This would isolate the contribution of each component.
3. **Demonstrate model-agnosticism** by running MADCluster with at least one alternative Base Embedder (e.g., LSTM or Transformer) on one dataset.
4. **Address the log-argument positivity constraint** in Eq. 6 by stating the mathematical condition under which the argument is always positive, or modify the formulation to guarantee positivity.
5. **Clarify whether ν in Section 3.1.2 (radius computation) and ν in Section 3.1.3 (clustering threshold) are the same or different** — if different, rename one to avoid confusion.
6. **Provide a hyperparameter sensitivity study** for at least ρ and τ on one dataset.

---
