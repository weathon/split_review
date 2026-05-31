## Summary
The paper introduces the Normalized Matching Transformer (NMT), a deep learning architecture for sparse keypoint matching. The method combines a Swin-Transformer backbone, a SplineCNN for geometric feature refinement, and a "Normalized Transformer" (nGPT) that enforces unit-norm embeddings at every layer. The model is trained using a combination of InfoNCE contrastive loss and a hyperspherical uniformity loss to ensure discriminative and well-distributed features.

## Strengths
- **Strong Empirical Results:** The paper demonstrates a significant performance boost over recent state-of-the-art methods like GMTR and COMMON, achieving a +5.1% improvement on PascalVOC and +2.2% on SPair-71k.
- **Training Efficiency:** The authors report a $1.7\times$ faster convergence in terms of epochs compared to existing baselines, which is a practical advantage for large-scale matching tasks.
- **Methodological Synergy:** The integration of hyperspherical normalization within the transformer layers (nGPT) is well-motivated for matching tasks, where cosine similarity is the standard metric for establishing correspondences.
- **Ablation Study:** The ablation study (Table 4) clearly identifies the contribution of each component, showing that the hyperspherical/InfoNCE loss combination is the primary driver of performance, followed by the backbone and the normalized transformer architecture.

## Weaknesses
### Fatal
None.

### Major
- **Backbone Fairness in Comparison:** A significant portion of the performance gain (+4.9% according to Table 4) comes from switching to a Swin-Large backbone, whereas many baselines (BBGM, ASAR, COMMON) use VGG16. While the authors do provide a VGG16 ablation, the main tables (Table 2 and 3) compare NMT (Swin) against VGG-based methods, which makes the "State-of-the-Art" claim slightly misleading regarding architectural innovation versus raw backbone power.
- **Inconsistency in Table 2:** Table 2 lists "COMMON Liu et al. (2020)" and "CGMPT Cao et al. (2020)" with identical scores (75.2) across all categories. This looks like a copy-paste error or a placeholder issue in the results table, as it is highly improbable for two different methods to have identical per-class accuracies across 20 categories.

### Minor
- **Hyperparameter Sensitivity:** The hyperspherical loss uses a layer-wise weighting parameter $p=0.3$. There is little discussion on how sensitive the model is to this specific value or the linear scheduling.
- **Sinkhorn during Inference only:** The paper states Sinkhorn is used only during inference, while training relies on InfoNCE. While this simplifies training, many recent works argue that training through the Sinkhorn layer (or a differentiable proxy) helps enforce the one-to-one matching constraint more effectively.

### Trivial
- **Table 3 Icons:** The icons in the header of Table 3 are not labeled with text, making it difficult to identify specific categories without cross-referencing the SPair-71k dataset documentation.

## Nice-to-Haves
- A comparison of inference time against BBGM or GMTR to see if the "Normalized Transformer" overhead is significant in practice.
- Visualization of the feature distribution on the hypersphere (e.g., t-SNE) to qualitatively validate the effect of the hyperspherical loss.

## Novel Insights
The primary insight is the application of the "Normalized Transformer" (nGPT) architecture—originally designed for LLM stability—to the geometric task of keypoint matching. By enforcing unit-norm constraints at every residual block and combining this with hyperspherical uniformity losses, the model maintains a high degree of feature discriminability throughout the depth of the network. This prevents the feature collapse or oversmoothing often seen in deep GNNs/Transformers applied to graphs, leading to faster convergence and higher accuracy.

## Suggestions
- Correct the duplicate entries/values in Table 2 to ensure the baseline comparison is accurate.
- Include the VGG16 version of NMT directly in the main comparison tables (Table 2 and 3) to provide a more direct "apples-to-apples" comparison with older baselines.
- Clarify if the Sinkhorn algorithm is used with a fixed number of iterations and what the temperature parameter for the Softmax/Sinkhorn is during inference.

## Score and Decision
The paper presents a solid improvement in a well-established computer vision task. The combination of modern backbones, geometric GNNs, and pervasive normalization is technically sound and empirically successful. Despite some concerns regarding the fairness of backbone comparisons and potential errors in the results table, the magnitude of the improvement and the efficiency gains make this a valuable contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>