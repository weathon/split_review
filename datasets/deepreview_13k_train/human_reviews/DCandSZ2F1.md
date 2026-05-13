# Fast Feedforward 3D Gaussian Splatting Compression

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
\vspace{-5pt}
With 3D Gaussian Splatting (3DGS) advancing real-time and high-fidelity rendering for novel view synthesis, storage requirements pose challenges for their widespread adoption. Although various compression techniques have been proposed, previous art suffers from a common limitation: \textit{for any existing 3DGS, per-scene optimization is needed to achieve compression, making the compression sluggish and slow.} To address this issue, we introduce \textbf{F}ast \textbf{C}ompression of 3D \textbf{G}aussian \textbf{S}platting (FCGS), an optimization-free model that can compress 3DGS representations rapidly in a single feed-forward pass, which significantly reduces compression time from minutes to seconds.
To enhance compression efficiency, we propose a multi-path entropy module that assigns Gaussian attributes to different entropy constraint paths for balance between size and fidelity. We also carefully design both inter- and intra-Gaussian context models to remove redundancies among the unstructured Gaussian blobs.
Overall, FCGS achieves a compression ratio of over $20\times$ while maintaining fidelity, surpassing most per-scene SOTA optimization-based methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a new compression model for 3D Gaussian Splatting (3DGS) representations. It aims to reduce compression time in an optimization-free pipeline, which is different from existing work. It introduces a Multi-path Entropy Module (MEM) to adaptive control the compression size and quality. It also designs inter- and intra-Gaussian context models to enhance compression efficiency. Experiments on multiple datasets show a large compression rate and high image quality.

### Strengths
1. It proposes a novel optimization-free pipeline for 3DGS-based compression.
2. MEM module to adaptively control size and fidelity.
3. It also designs inter- and intra-Gaussian context models to enhance compression efficiency. 
4. The proposed method achieves a high compression rate and surpasses the existing optimized-based methods in various experiments.

### Weaknesses
1. The training data is very large, and it takes 60 GPU days to get. Per-scene optimization does not need such an amount of training data. Will smaller data hurt the effectiveness of the feedforward model? It's unclear how the model would perform with significantly less training data, and if the learned prior would be robust enough for unseen scenarios. The reliance on such a large dataset raises concerns about the practical applicability of the method, especially if the training data is not easily accessible or reproducible.
2. More discussion of failure cases. it could be useful to discuss / show scenarios where the method performs poorly. Specifically, it would be beneficial to understand the types of 3DGS representations that are challenging for the proposed compression model. For example, are there specific geometric or textural complexities that lead to significant compression artifacts or fidelity loss? A more detailed analysis of these failure cases would provide a better understanding of the limitations of the method.

### Questions
1. Can authors provide visualization of inter- and intra-Gaussian context models on real input data. It would help reader better understand how this method work. 

2. Will the code or data open-source for reproduction ? the training set is interesting and would benefit many other tasks.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel, optimization-free compression pipeline for 3D Gaussian Splatting (3DGS) representations, called FCGS (Fast Compression of 3D Gaussian Splatting). FCGS uses a single feed-forward model to compress 3DGS representations, drastically reducing compression time compared to pruning and optimization-based approaches. The paper further details the Multi-path Entropy Module (MEM) and context models that FCGS employs to balance size and fidelity during compression. Finally, the authors demonstrate the efficacy of FCGS through extensive experiments, achieving a compression ratio exceeding 20x while preserving high fidelity.

### Strengths
- The paper provides a complete overview of related works on 3DGS with compression and structure it according to the methodology, see Section 1 and 2.
- The overall goal of the paper is clear and the authors motivate compression potential for 3DGS scenes well.
- The quantitative evaluation is very good, as the authors provide a comparison to several relevant methods, like light gaussians and Niedermayr etal.,  on three different datasets (MipNeRF360, T&T and DL3DV-GS) and present results in expressive graphs that highlight the trade-off of size and quality, see Figure 4.
- In addition to comparisons to compression works, the author further extent t0 feed forward reconstruction models and find a more efficient representation of their approach.
- Overall the experiments indicate that the proposed methods is an effective approach for compression performs favourable to most other approaches in terms of (PSNR/SIZE), however less effective than, Niedermayr et al.. See Figure 4.

### Weaknesses
 - The methodology is very complex and the respective section in the paper is hard to understand even for someone familiar with 3DGS. The reason is that there is information missing at the appropriate position in the text. For example, figure 2 in line 262 is is unclear how the Gaussians are divided into batches (randomly, per grid cell stays unclear). Hence it appears to hard to reproduce. Please see the Questions sections for more open points.
- The method's focus lies very much on increasing the compression speed and it does not improve over existing methods in terms of PSNR/Size, see Figure 4 (Simon*). One could argue that there is limited interests in compression speed, since a 3D GS reconstruction takes several minutes to hours and a follow up compression of a few minutes (e.g. Niedermayr et al.) does not impact the overall reconstruction time significantly.
- For qualitative evaluation, I'd have expected more visual comparisons to baseline methods. There is only comparisons to 3DGS in paper and supplementary material. Please provide more qualitative evidence.

### Questions
- What are the analysis transform and synthesis transform exactly? Architecture? Space? 
- Why can "the potential nonlinearity of the MLPs still cause considerable deviations in decoded gaussians", line 222?
- How are the the set of Gaussian split and what is the criterion to split them?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a generalizable 3D Gaussian compression framework incorporated with an effective entropy minimization module inspired by 2D image compression. The main contribution of this work is compressing 3D Gaussians within a minute, using a feed-forward pipeline. To achieve this, the authors first divide Gaussian attributes into a) geometry attributes, and b) color attributes. Then, these attributes are encoded and decoded using hyper-priors from inter-/intra-Gaussian context models, along with context design from the image compression approach. Consequently, this paper achieves a compact size and comparable rendering quality compared to the existing compression method, while requiring only several seconds.

### Strengths
- This paper suggests a novel framework that efficiently compresses the 3D Gaussian in a feed-forward manner, whereas existing optimization-based compression methods require additional adaptation steps.

- Experimental results demonstrate that the framework achieves high compression performance with comparable rendering quality with existing compression methods.

- The authors validate that the proposed hyper-prior design, including inter-/intra-Gaussian context models, further improves the compression performance.

### Weaknesses
 - Despite the effectiveness, the design of context models comes from heuristic priors that the Gaussians share inter-/intra-information. It could be helpful to show those relations of Gaussians to understand the justification of the proposed hyper-prior designs.
- There is no ablation on the strategy for dividing chunks in the inter-/intra-Gaussian context model. It could be helpful to show the results for several splitting designs.
- Due to arithmetic coding-based compression, it might yield notable computational costs to encode and decode the parameters.

### Questions
- How much time is needed for encoding and decoding parameters?
- It could be helpful to add compression performance for each attribute by demonstrating the storage size of each attribute before and after compression. (or storage size of color attributes and geometry attributes)
- How many scenes are required to acquire a feasible compression performance?
- An optimization-based compression work, ContextGS [1], has already applied an image compression-based pipeline for 3DGS using hyper-prior similar to the design of inter-Gaussian context models. However, the authors do not need to consider it, since ContextGS has not been published yet, accepted to NeurIPS 2024. Therefore, it would be helpful to mention this paper as a concurrent work.


(+minor question)
- Do you have any plans to release DL3DV-GS, which is a training dataset for this work? This could be helpful for various generalizable 3DGS approaches, including compression.


---
### Reference
[1] Wang et al., ContextGS: Compact 3D Gaussian Splatting with Anchor Level Context Model, NeurIPS 2024

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces an optimization-free model, called FCGS, for 3D Gaussian Splatting (3DGS) compression, which allows compressing an optimized 3DGS representation in a feed-forward process. The model incorporates both intra- and inter-Gaussian context information. The authors project most Gaussian attributes into a latent space and utilize arithmetic encoding and decoding for data compression. Additionally, they employ an end-to-end progressive training scheme for the proposed pipeline.

### Strengths
As far as I know, this is the first generalizable optimization-free 3DGS compression pipeline. Without the need of  original  training images, this generalizable compression method enables the compression of 3DGS, expanding the application scope of 3DGS compression algorithms.  

This article provides a novel approach to context modeling for exploring the correlations between Gaussians.

### Weaknesses
I find the experimental content of this paper somewhat disorganized and difficult to follow. The authors present the main comparative experimental results using figures, but there are no numerical comparisons in the main paper. Although detailed data is provided in the Appendix, the absence of tables in the main paper causes some inconvenience for readers. 

Additionally, in Tables C-D, the authors report the running time, but I believe this comparison may not be entirely reasonable. The running time for methods that involve training from scratch includes the time for reconstruction. FCGS also requires a pre-trained 3DGS, and the time spent pre-training the 3DGS should be reflected in the table. 

In the comparative experiments, the authors only compare methods with worse rendering quality than FCGS. However, there are existing 3DGS compression methods that offer better rendering quality and higher compression rates than FCGS. While these methods are not generalizable, readers should still be informed of the current gap between FCGS and the state-of-the-art.

### Questions
It seems that the process of generating m by MLP_m is not illustrated in Figure 2. By reading the method section, it is somewhat difficult for readers to understand the role and position of m in the pipeline (although there is a formula provided). It is suggested to draw a more detailed pathway in Figure 2.

### Soundness
3

### Presentation
2

### Contribution
3
