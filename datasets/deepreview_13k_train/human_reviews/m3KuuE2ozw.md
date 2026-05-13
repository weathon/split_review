# CAT-3DGS: A Context-Adaptive Triplane Approach to Rate-Distortion-Optimized 3DGS Compression

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
3D Gaussian Splatting (3DGS) has recently emerged as a promising 3D representation. Much research has been focused on reducing its storage requirements and memory footprint. However, the needs to compress and transmit the 3DGS representation to the remote side are overlooked. This new application calls for rate-distortion-optimized 3DGS compression. How to quantize and entropy encode sparse Gaussian primitives in the 3D space remains largely unexplored. Few early attempts resort to the hyperprior framework from learned image compression. But, they fail to utilize fully the inter and intra correlation inherent in Gaussian primitives. Built on ScaffoldGS, this work, termed CAT-3DGS, introduces a context-adaptive triplane approach to their rate-distortion-optimized coding. It features multi-scale triplanes, oriented according to the principal axes of Gaussian primitives in the 3D space, to capture their inter correlation (i.e. spatial correlation) for spatial autoregressive coding in the projected 2D planes. With these triplanes serving as the hyperprior, we further perform channel-wise autoregressive coding to leverage the intra correlation within each individual Gaussian primitive. Our CAT-3DGS incorporates a view frequency-aware masking mechanism. It actively skips from coding those Gaussian primitives that potentially have little impact on the rendering quality. When trained end-to-end to strike a good rate-distortion trade-off, our CAT-3DGS achieves the state-of-the-art compression performance on the commonly used real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a new method called CAT-3DGS for compressing 3D Gaussian Splatting (3DGS) representations. This method aims to optimize the rate-distortion trade-off by using a context-adaptive triplane approach. It captures spatial correlations through multi-scale triplanes and leverages intra correlations within Gaussian primitives for efficient coding. Additionally, it incorporates a view frequency-aware masking mechanism to skip less impactful primitives, achieving state-of-the-art compression performance on real-world datasets.

### Strengths
+ The paper introduces a new compression method for 3DGS that utilizes a triplane-based hyperprior. This method leverages multi-scale triplanes oriented along the principal axes of Gaussian primitives.
+ The paper presents a novel pruning approach in 3DGS using a view frequency-aware masking mechanism. This mechanism assesses the significance of Gaussian primitives based on their impact on rendering quality, allowing less critical ones to be skipped during coding.
+ The paper presents comprehensive ablation studies of various modules in the proposed compression method.

### Weaknesses
 - Entropy coding is a variable-length coding technique, typically decoded sequentially. However, 3DGC, used in rendering, is a highly parallelized method. The paper does not clearly explain how the proposed compression method can manage this parallelization without impacting rendering speed.
- The paper does not address decoding complexity. While CHARM enhances compression performance, it could significantly impact decoding speed, which in turn may affect rendering speed.
- The paper does not clarify whether real entropy coding was used during rendering or if the bit-rate was calculated based on theoretical entropy coding.

### Questions
* Are there scenarios where CAT-3DGS underperforms? Which modules in CAT-3DGS contribute to the drop in performance?

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
4

### Summary
This paper proposed a context-adaptive triplane based hyperprior entropy model to capture the inter correlation among Gaussian primitives in the 3D space  (i.e. spatial correlation) for spatial autoregressive coding in the projected 2D planes. The channel-wise autoregressive coding is performed to leverage the intra correlation within each individual Gaussian primitive. Besides, the view frequency-aware masking mechanism is proposed to actively skip from coding those Gaussian primitives with little impact on the rendering quality. Experimental results show that the proposed CAT-3DGS achieves the state-of-the-art compression performance on the commonly used real-world datasets.

### Strengths
- ***Novelty of Framework:*** The key idea of decomposing the dense 3D hash-graid in HAC with triplane hyperprior entropy model is novel and reasonable.
- ***Technological Innovation:*** This paper proposed the SARM and FARM modules to exploit the inter-correlation and intra-correlation, respectively. Speciflly, the view frequency-aware masking mechanism is designed to to skip less critical Gaussian primitives from coding.
- This paper is well organized and easy to follow.

### Weaknesses
 - Ablation experiment for CARM is not sufficient, the proposed method is only evaluated on one scenario, *e.g.*, bicycle scene.
- The paper is based on the work of HAC. However, the rate parameter setting used by HAC in the comparison experiment is not the same as that used by the proposed method. I doubt the fairness of this setting.

### Questions
- The FARM proposed by the author is interesting. According to the manuscript, the anchor feature is a latent representation of the anchor point, which does not have a clear mathematical correlation like the spherical correlation coefficient of 3DGS. What is the motivation of the proposed channel-wise autoregressive processing of anchor features?
- It is noted that the rate parameters setting used by the authors on different datasets are not consistent. Why?

### Soundness
4

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
The paper presents CAT-3DGS, a context-adaptive triplane approach for compressing 3D Gaussian Splatting (3DGS) data with a focus on optimizing the rate-distortion trade-off. CAT-3DGS introduces multi-scale triplanes aligned with the principal axes of Gaussian primitives in 3D space, leveraging both spatial and channel-wise autoregressive models to capture inter and intra correlations for efficient compression. This approach also includes a view frequency-aware masking mechanism to skip encoding less impactful Gaussian primitives. Experiments demonstrate CAT-3DGS achieves superior rate-distortion performance compared to prior 3DGS compression models like HAC, particularly on commonly used real-world datasets.

### Strengths
1. Innovative Triplane-Based Hyperprior: 

By projecting 3D Gaussian primitives onto triplanes, the paper introduces an efficient hyperprior structure that captures spatial correlation, which improves entropy coding performance.

2. Enhanced Coding Efficiency: 

The combination of spatial and channel-wise autoregressive models effectively utilizes both inter and intra correlations, which is particularly valuable in reducing the bit rate while maintaining high rendering quality.

3. Practical Masking Mechanism: 

The view frequency-aware masking mechanism selectively encodes only those primitives crucial for rendering, further optimizing storage and bandwidth usage.

4. Comprehensive Experimental Evaluation: 

The method is tested across several datasets and compared against notable baselines, showcasing significant rate savings and quality retention.

### Weaknesses
1. (Minor) Autoregressive Model Use: 

While the channel-wise and pixel-wise autoregressive models are novel in this context, they are a commonly applied strategy in image compression tasks. However, this paper does make a unique contribution by applying it to 3DGS.

2. Lack of Comparative Analysis with ContextGS: 

Although ContextGS is cited as a related work, there is no direct performance comparison with it. Given that ContextGS provides detailed results and its code is available, a comparative evaluation would enhance clarity on CAT-3DGS's improvements over previous models, especially regarding contextual coding efficiency.​

### Questions
I do not have other questions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces CAT-3DGS, a context-adaptive compression method for 3D Gaussian splatting (3DGS) that optimizes rate-distortion performance. CAT-3DGS uses multi-scale triplanes to embed spatial correlations of Gaussian primitives and employs autoregressive models for encoding. Additionally, it uses a channel-wise autoregressive model to enhance compression efficiency within each primitive and introduces a view frequency-aware masking mechanism to skip encoding primitives that minimally impact image quality. Experimental results demonstrate the effectiveness of the proposed method.

### Strengths
1. PCA-guided triplanes as the hyperprior
2. Channel-wise Autoregressive Model: Enhances compression by leveraging internal correlations within each voxel.
3. View Frequency-aware Masking Mechanism: Skips encoding for primitives with minimal impact on rendering quality, reducing redundancy and enhancing overall performance.

### Weaknesses
1. The ablation study of PCA guidance need to be included since there are already serval works that utilizes triplanes to compress the 3DGS/Nerf.
2. The efficiency of the model. The model seems a bit complicated. The coding time greatly increased due to the proposed context model. Besides, how about the training time?
3. Missing quantitative comparison with ContextGS, which is an important baseline method which also uses context model. For many benchmarks, the improvements appear somewhat marginal.
4. Figure 2 may not be entirely accurate; to my knowledge, CompGS does not utilize a context model.

### Questions
Please see the weakness part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors present a context-adaptive and rate-distortion-optimized 3DGS coding approach named CAT-3DGS. The approach introduces several modules for efficient attribute 3DGS compression, including a triplane-based hyperprior, spatial autoregressive models (SARM), channel-wise autoregressive models (CARM) and view frequency-aware masking. These modules are jointly trained in a rate-distortion-optimized framework. Experimental results demonstrate that CAT-3DGS achieves rate reductions of 78× and 26× compared to 3DGS and Scaffold-GS, respectively, while surpassing existing 3DGS compression schemes in rate-distortion performance.

### Strengths
1.The coding architecture is well-structured and theoretically solid, with four distinct modules specifically designed to address various redundancies.

2.The proposed method achieves exceptional rate-distortion performance, surpassing other 3DGS compression techniques.

### Weaknesses
1.The effectiveness of view frequency-aware masking is somewhat ambiguous. In Sec. 5.3, the authors report a 16% BD-rate reduction due to view frequency-aware masking. However, it’s unclear whether the anchor configuration (labeled as “w/o VFM” in Fig. 10) excludes masking altogether, or retains the masking operation but removes the weights $p_{n,k}$ only.

2.Spatial redundancies within attributes are not fully exploited. The proposed SARM only addresses inter-redundancies within triplanes (hyperpriors) rather than anchors. Given the fact that spatial redundancies exist between anchors, this aspect is not leveraged in the current framework.

### Questions
Please see weakness

### Soundness
3

### Presentation
2

### Contribution
2
