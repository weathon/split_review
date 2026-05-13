The paper claims "mathematically proven" optimization but there is no theorem, proposition, lemma, or any proof in the main text. The parser rules say the appendix may have been stripped, so the proof may exist there. However, a claim this central ("mathematically proven" in the abstract) should at least have a theorem statement in the main text. This is a valid concern, though the proof may exist in an appendix that was stripped.

Let me now construct the final review.</think>Now I have all the information needed. Let me synthesize the final review.

## Summary
MADCluster proposes a model-agnostic framework for unsupervised time-series anomaly detection that addresses the "hypersphere collapse" problem by learning dynamic cluster centers instead of fixed ones. The framework consists of three modules: a Base Embedder, a Cluster Distance Mapping module, and a Sequence-wise Clustering module with a novel "One-directed Adaptive loss." Experiments on four benchmark datasets show F1 improvements when MADCluster is applied to 11 baseline models.

## Strengths
- **Core idea is sound and well-motivated**: Learning the cluster center dynamically rather than fixing it (as in DeepSVDD) is a natural and potentially effective solution to hypersphere collapse. Figure 4 provides visual evidence that MADCluster achieves tighter cluster distributions (82.4% of data within 3σ) compared to DeepSVDD (which forms multi-clusters), supporting the claim that dynamic centers prevent collapse.
- **Demonstrated improvements across multiple deep learning models**: Table 1 shows consistent F1 improvements when MADCluster is applied to deep learning baselines (D-RNN, USAD, Anomaly Transformer, DCdetector, DeepSVDD, ITAD, THOC) across four datasets, with particularly notable gains from recall improvements (e.g., D-RNN on MSL: +23.26% recall, +13.6% F1).
- **Transparent loss dynamics**: Figure 5 directly validates the claimed behavior of the One-directed Adaptive loss — the threshold ν increases and converges during training, and radius/loss decrease — which is consistent with the method's theoretical motivation.

## Weaknesses

### Fatal
None.

### Major
- **The "model-agnostic" framing is undermined by non-differentiable baselines in Table 1**: The paper's title and abstract claim MADCluster is "model-agnostic" and "applicable to various deep learning architectures." Table 1 shows results for LOF, OC-SVM, VAR, and IsolationForest "before and after applying MADCluster." However, these are not neural networks and cannot serve as differentiable Base Embedders producing feature vectors $h_t^f$ that feed into the Cluster Distance Mapping and Sequence-wise Clustering modules. The paper provides no explanation for how MADCluster is combined with these non-DL models. Either the comparison setup is misleading or the architecture description is incomplete. The conclusion partially acknowledges this ("future research should focus on developing methodologies that increase applicability not only to traditional machine learning techniques"), but the main experimental table nonetheless presents these rows as "before and after applying MADCluster," which inflates the model-agnostic claim. — This matters because the paper's central framing is "model-agnostic," and the table is the primary evidence for this claim.

- **The claimed "mathematically proven" optimization is absent from the main text**: The abstract states the loss optimization is "mathematically proven," and the contributions list "We provide a mathematical proof for optimizing the One-directed Adaptive loss." However, no theorem, proposition, or proof sketch appears in the main text. The One-directed Adaptive loss (Eq. 6) includes an unusual factor $\frac{1-\nu^{1-\nu}}{1-\nu}$ that is never derived or motivated — the paper merely states two properties of the loss without proving them. While a proof may exist in an appendix, a claim this central demands at minimum a stated theorem and proof sketch in the body. Without it, the "theoretical soundness" contribution is asserted rather than demonstrated. — This matters because the proof is listed as one of four main contributions.

### Minor
- **Label smoothing is critical for training but hidden in implementation details (Section 4.2)**: The label smoothing modification $\hat{p}_t = p_t \times (1-\tau) + (1-p_t) \times \tau$ changes the binary auxiliary target from hard to soft labels, which affects training dynamics significantly. This modification is absent from the method formulation (Eqs. 4–6) and Algorithm 1. A reader implementing the method from Section 3 alone would produce a different algorithm. — This matters for reproducibility and clarity but does not invalidate the results.
- **The radius $R$ computation is underspecified**: The paper states "$R$ is computed using a specific quantile of the neural network outputs and the data loss values" (Section 3.1.2). "Specific quantile" leaves the exact procedure ambiguous — this is an operational detail that determines what radius of hypersphere is used. — This matters for reproducibility but is a minor gap.

### Trivial
- None.

## Nice-to-Haves
- Ablation study of the One-directed Adaptive loss against simpler alternatives (e.g., standard cross-entropy on $q_t$, or MSE between $q_t$ and a target) to demonstrate whether the specific functional form with $\frac{1-\nu^{1-\nu}}{1-\nu}$ is necessary.
- Statistical significance (mean ± std over multiple seeds) for the F1 scores in Table 1.
- Comparison against DeepSVDD with its published collapse mitigations (fixed center, ℓ₂-regularization, bias removal) to show MADCluster's advantage is over and above addressing collapse by any means.

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- **Harsh Critic's "experiments don't validate model-agnosticism because they only test D-RNN+MADCluster vs baselines"**: This is partially incorrect. Table 1 shows results for *each* of the 11 baseline models before and after applying MADCluster, not just D-RNN. The valid concern is about non-differentiable baselines, not about only testing one architecture. However, the partially valid sub-concern (that only D-RNN is explicitly described as the Base Embedder in the method section) is real — other DL architectures serving as Base Embedders are not explicitly described in the method section.

- **Harsh Critic's "ν > 0.5 interaction with normalization"**: This is speculative and not shown to cause problems in practice. The paper demonstrates through Figure 5 that the method works. The concern about what happens when ν > 0.5 is theoretical and not backed by evidence of failure.

- **Strength Finder's "Empirical Verification of Model-Agnostic Design" (claims 40/44 improvements)**: Partially removed. The claim that "11 distinct baseline models... providing strong empirical evidence for model-agnosticism" is partially inflated because at least 4 of the 11 baselines (LOF, OC-SVM, VAR, IsolationForest) are non-differentiable and their combination with MADCluster is unexplained. The valid part (improvements on DL baselines) is retained.

- **Harsh Critic's "no standard deviations" concern**: Moved to Nice-to-Haves as single-run evaluation without variance is common in this field.

- **Harsh Critic's "point-adjust evaluation inflates F1" concern**: This is the standard evaluation protocol in time-series anomaly detection (as the paper cites). Flagging it is scope creep.

- **Harsh Critic's "failure cases not shown" concern**: While nice to have, this is not a standard expectation for papers proposing new methods.

- **Harsh Critic's "missing comparison against DeepSVDD with known fixes"**: This would strengthen the paper but is not a critical omission.

## Novel Insights
The key insight from the review synthesis is the gap between MADCluster's framing and its experimental validation: the paper's architecture clearly requires a differentiable Base Embedder that produces feature vectors $h_t^f$, yet Table 1 includes non-differentiable traditional ML methods (LOF, OC-SVM, VAR, IsolationForest) under "before and after applying MADCluster" without explaining how they can serve as Base Embedders. This inconsistency inflates the model-agnostic evidence. Meanwhile, the genuinely valid evidence for model-agnosticism — consistent improvements across *deep learning* baselines like USAD, Anomaly Transformer, DCdetector, DeepSVDD, ITAD, and THOC — is strong enough to partially support the claim but would be substantially strengthened by explicitly showing different base embedder architectures within the MADCluster framework.

## Suggestions
- Remove non-differentiable baselines (LOF, OC-SVM, VAR, IsolationForest) from the "before/after applying MADCluster" comparison in Table 1, or explicitly explain how MADCluster is applied to them (e.g., by using their anomaly scores as input features to D-RNN+MADCluster, which would be a fundamentally different setup).
- Include at least a theorem statement and proof sketch for the One-directed Adaptive loss optimization in the main text, with full proof in the appendix.
- Add the label smoothing formulation to Algorithm 1 and Section 3, since it materially affects the training procedure.

**Originality**: The idea of learning cluster centers dynamically alongside representations in anomaly detection is a natural extension of DeepSVDD, but the specific One-directed Adaptive loss formulation and the combined architecture are novel.

**Importance of research question**: Hypersphere collapse is a well-known practical problem in one-class deep anomaly detection, and addressing it is important to the community.

**Claims support**: Partially supported. The empirical improvements on DL models are credible, but the model-agnostic claim is weakened by the non-DL baseline inclusion and the method section only describing D-RNN as the Base Embedder.

**Experimental soundness**: Reasonable but with gaps (non-DL baselines unexplained, no variance reported, proof claimed but absent from main text).

**Clarity**: The paper is generally well-written, but the label smoothing being hidden in implementation details and the $R$ computation being underspecified reduce clarity.

**Value to research community**: Moderate. The framework provides a practical approach to preventing hypersphere collapse that can improve existing DL anomaly detectors.

## Score and Decision

The paper makes a reasonable contribution — a practical framework for time-series anomaly detection that addresses hypersphere collapse and shows consistent improvements across multiple deep learning architectures. The two major weaknesses (non-DL baselines inflating the model-agnostic claim, and absent proof for claimed mathematical contribution) are significant but not fatal: removing the non-DL rows from Table 1 still leaves 7 DL models with consistent improvements, and the proof may exist in an appendix. The contribution is incremental but valid.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>