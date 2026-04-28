# Rotation Invariant Quantization for Model Compression

- Decision: Reject
- Avg Score: 5.25
- Scores: 8, 5, 5, 3

## Abstract
Post-training Neural Network (NN) model compression is an attractive approach for deploying large, memory-consuming models on devices with limited memory resources. 
In this study, we investigate the rate-distortion tradeoff for NN model compression. First, we suggest a Rotation-Invariant Quantization (RIQ) technique that utilizes a single parameter to quantize the entire NN model, yielding a different rate at each layer, i.e., mixed-precision quantization. Then, we prove that our rotation-invariant approach is optimal in terms of compression. We rigorously evaluate RIQ and demonstrate its capabilities on various models and tasks. For example, RIQ facilitates $\times 19.4$ and $\times 52.9$ compression ratios on pre-trained VGG dense and pruned models, respectively,  with $<0.4\%$ accuracy degradation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a new post-training quantization algorithm that given a neural network and some calibration images, produces mixed-precision quantized network. The key contribution of the paper is a new analysis technique motivated by the cosine-similarity based distortion measure between outputs quantized and unquantized network. The authors provide rate distortion analysis under the proposed measure and find the relation between the quantization bin width ($delta$) and layer's distortion (lemma 1) and the whole model's distortion (corollary 1). The authors then re-parametrize the search over $delta$ as search over parameter $k$ defined wrt distortion, and provide an efficient search algorithm (alg.1). Authors bound the possible values for optimal $k$ and make a heuristic search. The effectiveness of search algorithm, and of the proposed analysis is demonstrated on multiple networks and datasets.

### Strengths
- The technique is well motivated and executed; even without the application to compression, the results and its analysis have their merits on its own.
- The heuristic search over $k$ (alg 1), has good initial parameters and does not seem to require heavy tuning.
- Very good presentation and flow.

### Weaknesses
 - I found it a bit hard to understand how $k$ come into picture during the first readthrough of the paper. I feel like a little more work needed to introduce it. 
- There are a few arguable points that I count as a weakness, but they are easily addressable:
  - I would like to understand how good is the search parameters wrt a synthetically created problem where (say weights sampled from Gaussian/Laplacian), single, layer and etc. How much the heuristics during the search may (or may not) miss the optimal bin width?
  - Also, while I agree that in general setting search of $k$ is unbounded (as you write in the paper), practically speaking it is not the case: the weights are finite, and thus there are only certain number of  $delta$-s to check. This, has in fact been done in the work called "Optimal quantization using scaled codebook" (btw, you cite this paper but attribute it as QAT, which is not correct)
- Results:
  - I believe all compression results are given after ANS encoding; providing the compression ratio before ANS would be of great value (most papers report results before any additional encodings)

### Questions
Please see weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed a post-training mixed-precision weight quantization technique for neural networks by optimization based on an information-theoretic paradigm.  They choose to minimize layer-wise bitwidth constrained by cosine distance.  They experimented with example models in comparison with other methods.

### Strengths
- The paradigm of optimization for mixed-precision quantization is novel.  
- Theoretical results on optimization bounds are useful.

### Weaknesses
 - How do layer-wise quantization errors accumilate?  The proposed algorithm does not seem to address this.   
- In order for post-training quantization to be practical, activations are quantized too.  How activation quantization can be jointly done is not addressed.  
- Experimental results did not show a definitive advantage over competing methods.

### Questions
See above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a post-training quantization algorithm named Rotation-Invariant Quantization (RIQ) to quantify the NN to mixed-precision, and the main approach is picking the quantization bin width to be proportional to the layers’ norm. Based on the rate-distortion theory, the proposed method searching for the optimal solution over the family of spherical distributions. Empirical results show the competitive performance of RIQ on several benchmarks.

### Strengths
1.The authors provide a detailed analysis of the rate-distortion theory, which clarifies their research motivation well.

2.This paper is well-written and organized, and the supplementary material is sufficiently detailed.

### Weaknesses
1. Mixed precision is difficult to apply in the industrial scenarios. It usually requires the design of specialized chips to achieve a slight increase in inference speed, so I have doubts about the impact of the proposed method.

2. The experimental result lacks a comparison of inference speed of compressed model, between the proposed method and existing works.

3. The experimental result lacks a comparison of lightweight structure including separable convolution (like mobilenetv2) with existing methods like AdaRound or BRECQ.

### Questions
1. I suggest the author provide more descriptions about the scenarios where the mixed-precision model can be applied. The advantages of mixed-precision models can be manifested in NLP-type structures.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper examines post-training quantization of neural networks featuring linear layers, taking into account cosine distortion. The authors first demonstrate the rate-distortion trade-off between the original and quantized weights to establish the step size, $\Delta_{\ell}$, for each layer. Notably, all $\Delta_{\ell}$ values are governed by a singular parameter, $k$. Additionally, the paper investigates the rate-deviation analysis, wherein the deviation assesses the disparity in output. The authors introduce surrogate models in which the quantized weight is uniformly distributed across a space subject to random rotation, characterized by the angle $\theta_{\ell}$. Subsequently, it is proven that the mutual information is minimized when using the product distribution.

### Strengths
1. The paper is well-written and straightforward to understand.
2. The concept of rotational invariance in neural network quantization is intriguing.

### Weaknesses
1. The central assumption, $\|w\| = \|\hat{w}\| + o(\|w\|)$, appears to be contentious. For instance, with fixed-bit quantization, the discrepancy between $\|w\|$ and $\|\hat{w}\| $ is proportional to $\|w\|$, or in other words, $O(\|w\|)$. The use of little-o notation here is not well-justified, as the error is clearly of the same order as the norm of the weight vector, especially when considering practical fixed-bit quantization scenarios. This assumption needs much more rigorous justification, especially if the goal is to apply this to practical scenarios.

2. Lemma 1 could benefit from a more rigorous presentation, especially concerning the $o(\cdot)$. Additionally, both Lemma 1 and Corollary 1 do not appear to offer significant novel contributions. Specifically, the connection between bin width and cosine distance, while potentially useful, is not particularly surprising given the existing literature on quantization. The asymptotic connection needs to be more clearly established and its novelty better emphasized.

3. The surrogate model feels somewhat contrived. Moreover, the method for deriving $\tilde{w}_{\ell}$ is not clear. For instance, are the angles $\theta_{\ell}$ specified? The notion of being "uniformly distributed on a cone" is ambiguous due to its unbounded norm. This lack of clarity makes it difficult to understand the practical implications of the model. It is not clear how this cone is defined without a bounded norm, and the random rotation matrix $U(\theta_{\ell})$ needs to be more clearly defined. As a result, Theorem 1 requires a more comprehensive problem definition.

4. There seem to be some technical inaccuracies in the proof of Theorem 1. It is also essential to ensure that each mutual information, $I(w_{\ell}, \tilde{w}_{\ell})$, adheres to the distortion criteria. The proof needs to explicitly show how the minimization of mutual information is directly connected to the desired distortion criteria, and that the distortion criteria are met for each layer and not just for the overall output.

5. The link between distortion (related to weights) and deviation (pertaining to output) is unclear. The paper needs to explicitly show how the distortion in the weights translates to the deviation in the output, and what are the specific assumptions under which this relationship holds. This link is crucial for the practical application of the proposed method.

### Questions
Please check Weakness.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair
