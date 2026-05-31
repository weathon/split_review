## Summary
The paper introduces the "Inverse Protocol Prediction" (IPP) task, which aims to reconstruct experimental conditions (e.g., cell line, medium, seeding density, timepoint) from a single bright-field microscopy image of a 3D spheroid. Utilizing the SLiMIA dataset, the authors benchmark various deep learning architectures for segmentation, multi-label protocol classification, and spatiotemporal growth prediction. They propose specialized architectures, including a Hierarchical Multi-Task Transformer (HMTT) to capture label dependencies and an Image-Shape Fusion Transformer to integrate classical morphometrics with deep features.

## Strengths
- **Novel Research Question:** The concept of "Inverse Protocol Prediction" is a compelling shift from traditional outcome-based analysis (measuring size/viability) to meta-analysis (validating the protocol itself), which has significant implications for experimental reproducibility.
- **Comprehensive Benchmarking:** The authors evaluate a wide range of modern architectures, including CNNs (ConvNeXt), Transformers (ViT), and hybrid models (CoAtNet), providing a clear picture of which inductive biases suit spheroid morphology.
- **Methodological Diversity:** The paper doesn't just treat the problem as a flat classification task; it explores hierarchical modeling to respect biological dependencies and incorporates physics-inspired models (PhyDNet) for temporal prediction.
- **Interpretability:** The use of Grad-CAM to verify if models are looking at biological features (like necrotic cores) versus dataset artifacts (like background illumination) adds a necessary layer of scientific validation.

## Weaknesses
### Fatal
None.

### Major
- **Dataset Artifacts and Leakage:** The authors admit that "Microscope and magnification achieve near-perfect scores, though these largely reflect dataset-specific artifacts." In a multi-label setting, if a model can perfectly identify the microscope/magnification based on image texture or metadata-correlated noise, it may use that information as a shortcut to "predict" the cell line or medium (which are often nested within specific microscope runs). This potential for "shortcut learning" weakens the claim that the model is primarily learning biological morphological signatures.
- **Temporal Prediction Performance:** The SSIM scores for time-series prediction are quite low (< 0.40). While the authors acknowledge this is due to the complexity of biological growth and data sparsity, the current results suggest the models are struggling to produce meaningful future frames beyond blurry approximations.

### Minor
- **Cross-Dataset Validation Scope:** While the authors test on RxRx1 and CTC, these are 2D monolayer datasets. While this tests "robustness," the core task is defined for 3D spheroids. The drop in performance is expected, but it makes it difficult to judge how well the IPP framework would generalize to a *different* 3D spheroid dataset.
- **HMTT Performance:** The Hierarchical Multi-Task Transformer, which is theoretically more sound for biological dependencies, actually performs worse than the flat CoAtNet model. The paper suggests this is a trade-off for "consistency," but more analysis on why the hierarchy hurts accuracy would be beneficial.

## Nice-to-Haves
- A more detailed ablation study on the "Image-Shape Fusion" to see which specific morphometric features (e.g., circularity vs. area) contribute most to specific protocol labels.
- Discussion on how this model would handle "out-of-distribution" protocols (e.g., a cell line it hasn't seen before).

## Novel Insights
The most significant insight is the demonstration that experimental metadata is "baked into" the visual morphology of 3D cultures to a degree that allows high-accuracy reconstruction. Specifically, the finding that hybrid architectures (CoAtNet) outperform pure transformers or CNNs suggests that spheroid analysis requires a balance of local texture (for cell-level features) and global geometry (for overall spheroid structure). Additionally, the observation that hierarchical modeling improves biological plausibility at the expense of raw accuracy highlights a common tension in AI for science: the trade-off between statistical performance and alignment with causal domain knowledge.

## Suggestions
- To address the "shortcut learning" concern, I suggest a "leave-one-microscope-out" cross-validation. If the model can still predict the cell line and medium on images from a microscope it hasn't seen, it would prove the features are truly morphological and not just acquisition artifacts.
- For the temporal models, consider using a latent space prediction (predicting the next embedding) rather than pixel-level reconstruction, which might yield more biologically meaningful results given the low SSIM scores.

## Score and Decision
The paper presents a well-executed study on a novel and important task. While there are concerns regarding dataset shortcuts, the authors are transparent about these limitations and provide interpretability analysis to mitigate them. The breadth of models tested and the introduction of the IPP task provide clear value to the ICLR community.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>