# On Disentangled Training for Nonlinear Transform in Learned Image Compression

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Learned image compression (LIC) has demonstrated superior rate-distortion (R-D) performance compared to traditional codecs, but is challenged by training inefficiency that could incur more than two weeks to train a state-of-the-art model from scratch. Existing LIC methods overlook the slow convergence caused by compacting energy in learning nonlinear transforms. In this paper, we first reveal that such energy compaction consists of two components, \emph{i.e.}, feature decorrelation and uneven energy modulation. On such basis, we propose a linear auxiliary transform (AuxT) to disentangle energy compaction in training nonlinear transforms. The proposed AuxT obtains coarse approximation to achieve efficient energy compaction such that distribution fitting with the nonlinear transforms can be simplified to fine details. We then develop wavelet-based linear shortcuts (WLSs) for AuxT that leverages wavelet-based downsampling and orthogonal linear projection for feature decorrelation and subband-aware scaling for uneven energy modulation. AuxT is lightweight and plug-and-play to be integrated into diverse LIC models to address the slow convergence issue. Experimental results demonstrate that the proposed approach can accelerate training of LIC models by 2  times and simultaneously achieves an average 1\% BD-rate reduction. To our best knowledge, this is one of the first successful attempt that can significantly improve the convergence of LIC with comparable or superior rate-distortion performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a linear auxiliary transform (AuxT) to address the slow convergence issue in learned image compression (LIC). Specifically, this paper analyzes and designs the method based on feature decorrelation and uneven energy modulation. Experimental results demonstrate that, compared to traditional LIC methods, AuxT accelerates model training by 2 to 3 times and achieves an average 1% BD-rate reduction, improving convergence and rate-distortion performance.

### Strengths
1. The paper is well-written.
2. This paper introduces a valuable new research direction. Accelerating convergence in training learned image codecs is indeed an underexplored area and is both novel and important for this field. 
3. The idea of analyzing the training process from the perspective of energy compaction is interesting.
4. The experiment results are extensive and complete, showing the effectiveness of the proposed method.

### Weaknesses
1. This paper appears to focus solely on cases where learned image codecs do not incorporate a context model. However, including a context model could potentially enhance coding performance by leveraging correlations between latents. However, this paper primarily aims to decorrelate. It remains unclear whether the proposed method is applicable in scenarios with a context model, and if so, whether it would still provide the same benefits, or if the decorrelation would interfere with the context model's ability to exploit dependencies.
2. The motivation of adding additional branch is unclear. Is it possible to merge the operation of the proposed method (DWT / IDWT + Sub-band-aware scaling + OLP + orthogonality constraint) to $g_a$ and $g_s$? The paper does not provide sufficient justification for why a parallel branch is necessary, rather than integrating the proposed operations directly into the existing analysis and synthesis transforms. This raises questions about the architectural choices and whether a more streamlined approach could be equally effective.
3. In Section A.2, this paper compares the proposed method with two alternatives that substitutes the sub-sampling and up-sampling layers with DWT and IDWT to highlight the effectiveness of introducing a bypass auxiliary transform. However, the comparison is not entirely fair, as the proposed method also includes OLP layers and orthogonality constraints. It is not clear whether the performance gains are due to the bypass structure, or the additional components of the proposed method. A more controlled ablation study is needed to isolate the impact of each component.
4. The appendix of this paper compares the proposed method with an energy compaction penalty. However, the paper “Towards Efficient Image Compression Without Autoregressive Models (NeurIPS'23)” also addresses latent decorrelation for learned image compression, but this paper does not discuss or compare it. This omission is a significant oversight, as the paper directly addresses a similar problem and should be discussed in the context of the proposed method.

### Questions
1. The input to the WLAS in the proposed method is either the coded image x or the output from the previous layer of WLAS. I t would be interesting to compare this with using the intermediate features from the analysis transform at the corresponding resolution as input for the 2nd, 3rd, and 4th layers of WLAS. Similarly, for iWLAS, the input could be the intermediate features from the synthesis transform at the corresponding resolution.
2. Are $s_{ll}, s_{lh}, s_{hl}, s_{hh}$ trainable? Are they shared across all WLAS and iWLAS?
3. Is there an explanation for why employing more complex wavelets, such as the Daubechies wavelet db4 and biorthogonal wavelet bior2.2, performs worse than the simpler Haar wavelet?
4. In the ablation study “Effect of the linearity of AuxT,” it is mentioned that the 1x1 convolution layer W in OLP is placed before the added non-linear (ReLU or GDN) layer in comparison. However, it is unclear whether the orthogonality constraint is applied before or after the non-linear layer.
5. In Fig.1, it would be better to explain how energy is measured.
6. Cross-ref of figures mentioned in Section 5.4 should be wrong.
7. In Fig. 8, [A4] DWT -> Conv should be [A3] DWT -> Conv.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper identifies the slow convergence in training Learned Image Compression (LIC) models due to energy compaction issues and proposes a Linear Auxiliary Transform (AuxT) to address this. AuxT uses Wavelet-based Linear Shortcuts (WLSs) to improve feature decorrelation and energy modulation. Integrating AuxT into LIC models can accelerate training by 2-3 times and achieve a 1% reduction in BD-rate, improving both efficiency and performance.

### Strengths
(1) This paper explores the problem of slow convergence in LIC. Through a large number of experiments, the author designed a universal plug-in AuxT to solve this problem to a certain extent. I think the paper is interesting and novel.

(2) AuxT shows very strong generalization, achieving a significant reduction in training time and a small increase in performance in several classic LIC architectures (mbt2018,ELIC,TCM, etc.).

### Weaknesses
(1) In Subband-aware scaling of wavelet-based linear shortrcut (WLS), the authors appear to adopt simple linear scaling (reduction coefficients 1,0.5,0.5,0) for the four subbands LL,LH,HL,HH to modulate. Can you give further reasons for the use of these reduction coefficients, that is, it is proved through experiments that the reduction coefficients set in this way are optimal? It is unclear if these coefficients are fixed or learnable, and if fixed, what is the justification for this specific configuration, given that different subbands may require varying degrees of scaling depending on the input image characteristics and the specific LIC model architecture.

(2) The derivation of Loss Function seems to be a little short, I am not sure what $L_{orth}$ includes. Can you give the formula? Are they added on top of the original Rate-Distortion loss? It is not clear how the orthogonality constraint is implemented and what impact it has on the overall training dynamics. The relationship between the orthogonality loss and the rate-distortion loss should be further clarified.

(3) In Table 1, what does Trainning time (-64%), (-40%) mean and to whom is it compared? The lack of a clear baseline makes it difficult to assess the true impact of the proposed method on training time. It is important to specify the anchor model used for comparison.

(4) TCM is a relatively new model in the field, and it seems that AuxT has relatively little performance improvement when applied on TCM. Can you further analyze the reason? It is important to understand why the proposed method does not yield significant gains on this particular architecture, as it might reveal limitations of the approach or suggest areas for further refinement.

### Questions
Please see Weaknesses.

### Soundness
3

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
5

### Summary
The aim of this paper is to accelerate the convergence of learned image compression models. The authors observe the phenomena of energy compaction and decorrelation in learned image compression training. A portion of the channels in the model takes up most of the energy, and the energy compaction becomes more pronounced as the number of iteration steps increases. For a learned model, it usually requires many iterations to achieve energy compaction. This paper proposes the use of a wavelet transform based bypass transform module, to achieve coarse approximation of feature decorrelation and uneven energy modulation, which enhances the convergence speed of the model.

### Strengths
1) The experimental results demonstrate the effectiveness of the bypassed wavelet transform module, and the model with the wavelet transform module requires only 1M iterations to achieve comparable rate-distortion performance compared to the original model with 2M iterations.

2) The authors demonstrate the validity of their approach on most of the existing models (e.g. ELIC, Minnen’18, STF, TCM).

### Weaknesses
1) The introduction of AuxT will introduce additional hyperparameters ($\lambda_{orth}$), will the optimal $\lambda_{orth}$ be different for different models? According to Table 2 in the Supplementary Material, different $\lambda_{orth}$ will have a large impact on the performance, how to choose the optimal $\lambda_{orth}$? It is unclear how sensitive the performance is to this hyperparameter, and whether a single value can be used across different architectures and datasets. A more thorough analysis of the impact of $\lambda_{orth}$ on different models and datasets is needed to establish the robustness of the proposed method.

2) In the training of image compression models, is the difficulty in aggregating energy due to the presence of entropy constraints? In the presence of entropy constraints, in order to avoid large bit rates, the model would automatically reduce the rate of information aggregation to match the entropy model's ability to estimate redundancy? In fact, in the training of the DCVC series [1], only reconstruction loss training would be performed first, and then entropy constraints would be introduced later, and I intuitively think that this approach would accelerate the training of the model. Please compare with this approach (e.g. performing 200,000 reconstruction error training followed by 400000 joint training). It is important to understand if the observed energy compaction is a natural consequence of the rate-distortion trade-off or an artifact of the training procedure. The interaction between the entropy constraint and energy aggregation needs further investigation.

3) Also, there are currently methods that will train a small model (e.g. only hyperprior) [2] and then reload the trained transform module and then add a more complex entropy model, in terms of total time, how does this compare to the training time of the method that introduces AuxT (e.g. TCM & ELIC)? The paper needs to provide a more detailed comparison of the proposed method with other training strategies, including the two-stage training approach, in terms of total training time and resource consumption. It is important to demonstrate that the proposed method is not only effective but also efficient compared to existing alternatives.

### Questions
Please refer to weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Overall, this paper presents a linear auxiliary transform (AuxT) to disentangle energy compaction in training nonlinear transforms. By analyzing the characteristics of the LIC framework, the authors find the factors that caused the slow convergence of the LIC. Their methods accelerate the training of LIC models by around 2 times with compatible performance.

### Strengths
1. The authors analyze the training process of LIC from the perspective of energy compaction and highlight the inefficiency of existing nonlinear transforms in achieving effective feature decorrelation and uneven energy modulation necessary for optimal energy compaction.

2. The authors propose an auxiliary transform (AuxT) specifically designed to enhance energy compaction by enabling coarse feature decorrelation and uneven energy modulation.

3. Experimental results demonstrate that their method can reduce training time by approximately 45%.

Overall, this is an interesting and insightful paper. The authors propose a straightforward method that results in significant improvements.

### Weaknesses
1. Typos: For example, in the sentence: "and further observe two characteristics of nonlinear transforms to realize energy (i.e., feature decorrelation and uneven energy modulation)," there seems to be a missing word. It would be clearer to say "realize energy compaction" to fully capture the intended meaning.

2. Phrasing Recommendation: (1). Instead of using the phrase "this is the first successful attempt", which may not be entirely accurate, consider revising the sentence to: 

"To the best of our knowledge, this is one of the first successful attempts in LIC that significantly accelerates the convergence of training while achieving comparable or superior R-D performance."

Additionally, it would be beneficial to include the earlier contemporaneous work that also explored training acceleration for LIC in the RELATED WORK section. You could reference:
"Accelerating Learned Image Compression with Sensitivity-aware Embedding and Moving Average" (https://openreview.net/forum?id=V1sChEsXZg).

(2). "Experimental results demonstrate that the proposed approach can accelerate the training of LIC models by 2 to 3 times while simultaneously achieving an average 1% BD-rate reduction."

However, based on Table 1, when the training time is reduced to approximately one-third of the original, there is no observed BD-rate reduction. I suggest revising the statement to: "can accelerate the training of LIC models by 2 times while simultaneously achieving an average 1% BD-rate reduction."


3. It would be important to add a subsection in RELATED WORK discussing the acceleration of training in other tasks. This could provide a broader context and demonstrate awareness of related methodologies in the field. You could discuss approaches from other domains that have addressed similar challenges in accelerating the training process.

### Questions
Please refer to the weaknesses section. I am open to increasing my rating if the authors further enhance the quality of their manuscript.

### Soundness
3

### Presentation
3

### Contribution
4
