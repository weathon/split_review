# MambaQuant: Quantizing the Mamba Family with Variance Aligned Rotation Methods

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
Mamba is an efficient sequence model that rivals Transformers and demonstrates significant potential as a foundational architecture for various tasks. Quantization is commonly used in neural networks to reduce model size and computational latency. However, applying quantization to Mamba remains underexplored, and existing quantization methods, which have been effective for CNN and Transformer models, appear inadequate for Mamba models (e.g., Quarot suffers a 21% accuracy drop on Vim-T$\dagger$ even under W8A8). We have pioneered the exploration of this issue and identified several key challenges. First, significant outliers arepresent in gate projections, output projections, and matrix multiplications. Second, Mamba’s unique parallel scan further amplifies these outliers, leading to uneven and heavy-tailed data distributions. Third, even with the application of the Hadamard transform, the variance across channels in weights and activations still remains inconsistent. To these ends, we propose MambaQuant, a post-training quantization (PTQ) framework consisting of: 1) Karhunen-Lo`eve Transformation (KLT) enhanced rotation, rendering the rotation matrix adaptable to diverse channel distributions. 2) Smooth-Fused rotation, which equalizes channel variances and can merge additional parameters into model weights. Experiments show that MambaQuant can quantize both weights and activations into 8-bit with less than 1% accuracy loss for Mamba-based vision and language tasks. To our knowledge, MambaQuant is the first comprehensive PTQ design for the Mamba family, paving the way for further advancements in its application.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a quantization scheme for a family of under-explored models, mamba based models. The authors observe that the outliers exists in certain type of projections in mamba models, and the parallel scan further make the issue worse. And the Hadamard transform, commonly used in quantization literature for Transformer models, is insufficient to address the outlier issue. The authors design a Karhunen-Loeve Transformation enhanced rotation to control the variance for offline weight quantization and Smooth-Fused rotation to control the variance for online activation quantization.

### Strengths
1. The KLT enhanced rotation for controlling the variance is interesting. 
2. The experiments show significant improvement compared to quantization methods proposed for Transformer models.

### Weaknesses
1. I think it is possible (also easier) to control the variance of Hadamard transformed weight by simply applying a diagonal scaling matrix so that the variance of each row is the same. This is similar to per channel quantization, where different scalings are applying to different rows of weight matrix before doing rounding. I am wondering how does this scheme compare to the proposed method. 
2. The visualized value distribution in Figure 1 looks very similar to the visualization for Transformer models. More discussion on why quantization for Transformer models failed for mamba would be interesting. 
3. 8 bit quantization for Transformer models is quite easy without noticeable performance drop, but it looks like that quantization for mamba is hard based on the experiments. Can the authors comment on this?

### Questions
1. I think it is possible (also easier) to control the variance of Hadamard transformed weight by simply applying a diagonal scaling matrix so that the variance of each row is the same. This is similar to per channel quantization, where different scalings are applying to different rows of weight matrix before doing rounding. I am wondering how does this scheme compare to the proposed method. 
2. The visualized value distribution in Figure 1 looks very similar to the visualization for Transformer models. More discussion on why quantization for Transformer models failed for mamba would be interesting. 
3. 8 bit quantization for Transformer models is quite easy without noticeable performance drop, but it looks like that quantization for mamba is hard based on the experiments. Can the authors comment on this?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper find out current PTQ methods on Transformer-based LLMs failed to quantize Mamba. Then it proposes MambaQuant with offline KLT-enhanced rotation and online smooth-fused rotation to improve PTQ performance. Experiments show MambaQuant achieves 1\% accuracy loss on W8A8, better than QuaRot and SmoothQuant.

### Strengths
1. This paper studies the PTQ problems for Mamba,  finding out that current PTQ methods on Transformer-based LLMs failed to quantize Mamba.
2. MambaQuant applies SmoothQuant's smoothing vector to Mamba's non-linear SiLU and PScan.
3. Experiments show MambaQuant achieves 1\% accuracy loss on W8A8.

### Weaknesses
1. This paper does not detail how to get $K$ for different input $X$.
2.  KLT-enhanced ratation seems unable to solve all input's channel in-variance and outliers.

### Questions
KLT-enhanced rotation $KH$ seems to be also fixed, like Hadmard matrix $H$, for different input. To perform offline transformation, eigenvectors $K$ also need to be fixed for all input.  Thus it may not uniformly transform each X's channel variance?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores post-training quantization for Mamba family of state-space models and identifies several key challenges, namely the presence of outliers in gate projections, output projections and the fact that Mamba’s PScan operation further amplifies these outliers.

Authors proposed MambaQuant, a post-training quantization framework for Mamba model family, consisting of two extensions over Hadamard-based methods: 1) Karhunen-Loève Transformation (KLT) enhanced rotation; and 2) Smooth-fused rotation, which equalizes channel variances and can be merged into model weights.

Experiments show that MambaQuant can quantize both weights and activations into 8-bit with less than 1% accuracy loss for Mamba-based vision and language tasks.

### Strengths
* Authors demonstrate the effectiveness of MambaQuant on both vision and language tasks and different model sizes. Solid performance against the recent PTQ methods including GPTQ, SmoothQuant, QuaRot.
* Ablation studies and figures to demonstrate that how the proposed method improves the distribution of problematic activations and hence improves their quantizability.
* Authors intend to release the code.

### Weaknesses
 * Paper claims to be the first comprehensive analysis of quantizability of Mamba, however many of the insights including the existence of outliers in gate and output projections were already discussed in “Mamba-PTQ” [1]. Could you elaborate on any additional differences between these two approaches?

* It seems that KLT enhanced rotation is very straightforward and boils down to simply applying an SVD decomposition on weights/activations (or equivalently, eigenvalue decomposition on the covariance matrix), and fusing the emerging matrix K into H. Is there is any additional insight to it?



### Questions
* Would be great if authors could include detailed per-task results for LM-eval benchmark in the appendix, to improve reproducibility and make it easier to compare to.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a post-training quantization framework, called MambaQuant, which applies to Mamba models. MambaQuant relies on the observation that there are weights and outliers in Mamba models which are significantly larger than the rest, and that this disparity is increased by the parallel scan operation. The authors first study the effectiveness of the Hadamard transformation, which incorporates pre- and post- multiplies the features by Hadamard matrices so as to spread out the largest values, and show that it is ineffective at equalizing variance across channels, which makes quantization performance suffer. Then they discuss the MambaQuant framework which consists of two operations:
- An offline whitening step, which they call the Karhunen-Loeve transform: first diagonalize the feature covariance matrix at the given layer, then multiply the appropriate Hadamard matrix by the matrix of eigenvectors of the feature covariance. Multiplying the features by this product matrix instead of the Hadamard matrix will spread out the massive values and also ensure that the variance across each channel is balanced.
- An online smoothing step: do a transformation on the SILU, e.g., $x \sigma(W x) \mapsto x \sigma(s \odot [(W \oslash s)x])$ where $\odot, \oslash$ are elementwise multiplication/division respectively and $s$ is a smoothing vector, and there exists an algorithm to compute $(W \oslash s)x$ accurately and efficiently via fusing with multiple operations.

### Strengths
- The proposed toolkit MambaQuant is clearly motivated, and the motivation follows from both theoretical and empirical perspectives; the weaknesses of the prior methodology (that is, smoothing large values via Hadamard transformation) are clearly demonstrated in the context of Mamba.
- Accordingly, the solutions proposed by MambaQuant are shown to resolve these issues effectively using the same methodology.
- The shown empirical results demonstrate minimal performance degradation compared to Mamba on both language and vision tasks.
- The paper conducts several ablations to show that in their experimental setup, all changes significantly improve a property of the model to make quantization easier.

### Weaknesses
 - The whitening transformation (KLT) seems to be computationally prohibitive to run. It is true that the paper thus classifies it as an offline transformation. However, it is still not clear whether the eigenvectors of the feature matrix are similar across batches (so that the transform truly whitens the data and equalizes variance across all channels). That would be an interesting insight, if true, but it's not confirmed here, and so the KLT needs more empirical evidence on more diverse data to be validated in real applications. Specifically, the paper should investigate the stability of the computed eigenvectors across different batches and datasets. If the eigenvectors vary significantly, the offline KLT may not be as effective as claimed, and the computational cost of recomputing the transform for each new dataset would be a significant practical limitation. Furthermore, the paper should provide a more thorough analysis of the computational overhead of the KLT, including the time and memory requirements for both the offline computation and the online application of the transform. 
- The methods proposed are only studied in the context of, and only apply to, the Mamba family of architectures. This is an explicit limitation of the paper. It would be great if the methods here transferred to different architectures without significant performance downgrades (i.e., they still sort of work). While the paper acknowledges this limitation, it would be beneficial to explore the potential for adapting the proposed techniques to other architectures, even if it requires some modifications. The core idea of addressing variance imbalances could potentially be applicable to other models, and investigating this could broaden the impact of the work. For example, it would be interesting to see if the KLT-based approach could be applied to transformer models, even if the specific smoothing technique needs to be adapted.

### Questions
- See weaknesses section; more empirical validation would be great in order to demonstrate the generalizability of the MambaQuant operations.
- Is there any aspect of runtime which is significantly improved or made worse by these changes? E.g. prefill time or average runtime? Same with the memory constraints. It's acknowledged that the appendix contains some estimates for time and space complexity but it would be interesting to see how these bear out in practice.

### Soundness
3

### Presentation
3

### Contribution
3
