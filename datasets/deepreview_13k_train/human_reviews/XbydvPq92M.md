# Information-Ordered Bottlenecks for Adaptive Dimensionality Reduction

- Decision: Reject
- Scores: 5, 3, 3, 5

## Abstract
We present the information-ordered bottleneck (IOB), a neural layer designed to adaptively compress data into latent variables ordered by likelihood maximization. Without retraining, IOB nodes can be truncated at any bottleneck width, capturing the most crucial information in the first latent variables. Unifying several previous approaches, we show that IOBs achieve near-optimal compression for a given encoding architecture and can assign ordering to latent signals in a manner that is semantically meaningful. IOBs demonstrate a remarkable ability to compress embeddings of image and text data, leveraging the performance of SOTA architectures such as CNNs, transformers, and diffusion models. Moreover, we introduce a novel theory for estimating global intrinsic dimensionality with IOBs and show that they recover SOTA dimensionality estimates for complex synthetic data. Furthermore, we showcase the utility of these models for exploratory analysis through applications on heterogeneous datasets, enabling computer-aided discovery of dataset complexity.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces the Information-Ordered Bottleneck (IOB), that proposes to adaptively compresses data into hierarchically ordered latent variables, streamlining multiple existing methods into a unified framework. The IOB's flexibility is demonstrated through various synthetic and real datasets, including image and text embeddings, where it achieves near-optimal compression and meaningful latent ordering. Comparative results showcase IOB's superior performance in data reconstruction and intrinsic dimensionality estimation, outpacing state-of-the-art methods and facilitating exploratory dataset analysis.

### Strengths
* IOB provides an adaptive data compression mechanism, allowing for the dynamic adjustment of bottleneck width while ensuring likelihood maximization. This adaptability ensures the most crucial information is captured first, enhancing the efficiency of data utilization.
* IOB provides a unified framework putting other works such as the Nested Dropout, Triangular Dropout and PCAAE. Its application across diverse datasets, both synthetic and real, underscores its broad adaptability and relevance.
* IOB model's ability to capture semantically meaningful latent ordering and intrinsic dimensionality adds depth and interpretability to the learned latent space.

### Weaknesses
 * The algorithmic novelty is not clear. The core of IOB formulation and training seems to be based on Nested Dropout and the unit-sweeping introduced in that work. The paper does not sufficiently articulate how the specific combination of these existing techniques results in a novel contribution beyond a straightforward application of these methods. The adaptive compression mechanism, while useful, appears to be a direct consequence of the unit-sweeping approach, lacking a unique theoretical or practical advancement.
* Few key approaches on ordered dimension reduction have not been discussed, for example [1] where a stochastic latent dimension and ordered sparsity has been applied through a Bayesian prior, where IOB seems to be a special case of it where the weighting is fixed to be linear or geometric. The paper should include a more thorough discussion of how IOB relates to methods that also use a stochastic latent dimension, particularly those that employ Bayesian priors to induce ordered sparsity. The current analysis lacks a detailed comparison to these methods, which limits the assessment of IOB's unique contributions.

### Questions
See the Weakness above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an information-ordered bottleneck~(IOB) layer to compress data into latent representations. The basis of IOB is dynamic adjustment bottleneck width at inference based on likelihood maximization. Given a neural architecture, IOB can compress the input data while maintaining the semantic properties of data. Experiments on synthetic and real datasets show the effectiveness of the designed IOB.

### Strengths
1. The research topic is interesting and important in DL community, that learning high-quality compressed representation.
2. The authors conduct many experiments on synthetic and real datasets to verify the effectiveness of the proposed IOB layer.

### Weaknesses
1. The motivation of this paper is not clear. The authors argue that the current compression methods, like PCA, and Auto-Encoder need dimension parameters artificially, however, the threshold k_max in IOB also depends on empirical.
2. Lacking of theoretical contribution. Directly masking top-k elements of latent variables seems too simple, and easy to discard semantic information. I hope the authors can provide analytic evidence of how to compress data without data distortion.
3. In experiments, why not compare current model compression methods, such as Distillation, Quantization, and Pruning?

### Questions
Refer weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to seek an ordered latent embedding that can reveal its impact in minimizing the likelihood. In particular, the authors gradually increase the dimension of the latent embedding to ensure that top-ranked latent channels convey more impactful information. The proposed method has been demonstrated on synthetic and real image datasets using different pre-trained models.

### Strengths
1. The paper is overall easy to read, although some part in technology and experiment is not clear. 
1. The study problem is interesting and the proposed method is very simple and intuitive.

### Weaknesses
1. Overall, the current version is insufficient and can not explain very well why the proposed method can deliver ordered latent variables.

2. It is claimed that the proposed method can be plugged into different pre-trained models, but there are only limited experiments from this perspective.

3. This paper lacks theoretical guidance and intuitive explanation behind the heuristic experiment settings.

4. It is claimed in the abstract that this paper introduces a "novel theory for estimating global intrinsic dimensionality," but I cannot find any theoretical analysis related to this claim.

5. Regarding Eq. 2, it is unclear (i) whether $b_i$ is shared by all $f_{\theta}^i$ where $i\ge k$, and (ii) whether all the $b_i$ are updated at the same time.

6. In Fig. 2, the left panel of Fig. 2(a) is the same as the right panel of Fig. 2(a). In Fig. 2(c) and (d), it seems that the performance of PCA is similar to the proposed IOB. The baseline PCA is too simple; why not compare with more complex baselines, such as Kernel PCA and PCAAE?

7. Fig. 3 shows that Separate AEs are comparable with the proposed method. Does this mean that Separate AEs can perform the same function, i.e., delivering ordered latent embedding, as the proposed IOB?

### Questions
1. It is claimed in the abstract that this paper introduces a "novel theory for estimating global intrinsic dimensionality," but I cannot find any theoretical analysis related to this claim.
1. Regarding Eq. 2, it is unclear (i) whether $b_i$ is shared by all $f_{\theta}^i$ where $i\ge k$, and (ii) whether all the $b_i$ are updated at the same time.
1. In Fig. 2, the left panel of Fig. 2(a) is the same as the right panel of Fig. 2(a). In Fig. 2(c) and (d), it seems that the performance of PCA is similar to the proposed IOB. The baseline PCA is too simple; why not compare with more complex baselines, such as Kernel PCA and PCAAE?
1. Fig. 3 shows that Separate AEs are comparable with the proposed method. Does this mean that Separate AEs can perform the same function, i.e., delivering ordered latent embedding, as the proposed IOB?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a method for ordering latent variables based on their impact in minimising likelihood. The proposed framework generalises previous approaches. The adaptive compression capabilities of the model are demonstrated through experiments. The formalism also allows the intrinsic dimensionality problem to be addressed.

### Strengths
- Clearly defined scope
- Numerous experiments
- The method seems well suited for dimensionality reduction and shows promising results for intrinsic dimensionality estimation.

### Weaknesses
For the theoretical part
- The method depends on static hyperparameters: weights and k-max, with only two models of weights distribution proposed (geometric and linear) . 

Regarding the experimental part :
- The organisation into several sections is confusing.
- Lack of numerical evaluation : it is difficult to compare or evaluate the performance of the method with the elements given in the experimental section (notably section 4.).
- Many toy data sets (S-curves, n-disk, dSprite)

### Questions
- Could the hyperparameters be learned or at least adjusted automatically ? 
- Since the goal of compression is to somehow measure the amount of information, could any modification of the IOB layer provide a precise information-theoretic measure?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
