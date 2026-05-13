# Splitting & Integrating: Out-of-Distribution Detection via Adversarial Gradient Attribution

- Decision: Reject
- Scores: 3, 6, 5, 6

## Abstract
Out-of-distribution (OOD) detection is essential for enhancing the robustness and security of deep learning models in unknown and dynamic data environments. Gradient-based OOD detection methods, such as GAIA, analyse the explanation pattern representations of in-distribution (ID) and OOD samples by examining the sensitivity of model outputs w.r.t. model inputs, resulting in superior performance compared to traditional OOD detection methods. However, we argue that the non-zero gradient behaviors of OOD samples do not exhibit significant distinguishability, especially when ID samples are perturbed by random noise in high-dimensional spaces, which negatively impacts the accuracy of OOD detection. In this paper, we propose a novel OOD detection method called **S \& I** based on layer **S**plitting and gradient **I**ntegration via Adversarial Gradient Attribution. Specifically, our approach involves splitting the model's intermediate layers and iteratively updating adversarial examples layer-by-layer. We then integrate the attribution gradients from each intermediate layer along the attribution path from adversarial examples to the actual input, yielding true explanation pattern representations for both ID and OOD samples. Experiments demonstrate that our S \& I algorithm achieves state-of-the-art results, with the average FPR95 of 29.05\% (38.61\%) and 37.31\% on the CIFAR100 and ImageNet benchmarks, respectively. Our code is available at: https://anonymous.4open.science/r/S-I-F6F7/.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes the Splitting and Integration methods for out-of-distribution detection. It is based on the method GAIA  (Chen et al. 2023) and compares the proposed method with GAIA and other algorithms.  Splitting is a simple division of network layers into parts (as indicated in line 118), and integration is based on gradient splitting. The integrated gradient is based on the IG method. The experimental results are comparable to GAIA but do not significantly surpass GAIA's performance in order to be a new state of the art.

### Strengths
The paper proposes a modification to GAIA (Chen et al. 2023). GAIA uses image x =  0 as a baseline for Integrated Gradient attribution, whereas the proposed method uses adversarial image $x_{adv}$). The results of the experiments slightly improve to GAIA in few cases.

### Weaknesses
The paper experiment results are almost the same as GAIA except for a slight improvement on one dataset (SVHN).
The paper writing in most places is full of authors' assumptions, or at least the sentences give such an impression (see lines 115, 202, 311). These statements rather should be backed by evidence or citations. There are questions about the use of variables and their definition in many equations. (see Question section). Proof  2 appears to be based on the assumption that $x_{adv}$ of $x_{out}$ will exhibit overly confidence.

### Questions
Define the term "overly confident" or not overly confident. 

Clarify the score OOD score in Algo 1 as $\tau$. This appears for the first time in the paper and is not used anywhere else. 

In Eq. confidence score, $\Omega(x)$ is, and $\xi$ is the threshold. The confidence score is not mentioned in Eq. 1 anywhere else.  This disconnects the latter discussion. This should be referred to elsewhere in order to keep the concept flowing. 

Define the boundary of threshold $\xi$.

The author mentions this is the first time the authors use adversarial attribution.  However, Sec in line 172 suggested that they are using the Integrated Gradient (IG) method by Sundarajan et al. 2017.  Clerfy explicitly whether they are applying IG methods from literature when they take image $x=0$ to $x_{adv}$ as baseline. 

Define indices $x_{(r,s)}$. Are they pixel-wise features or indicate a feature of image x with the same dimension? This could also be related to Fig. 1 for more clarity.

Variable $T$ in line 188 indicates this is the number of intervals; in line 216, it is iteration. Rectify or clarify. 

Figure 2 text should be made legible. 
Figure 2 caption should explain what is in the image rather than stating the method in general. Not explaining the figure properly makes this irrelevant. 

Table 1 text is too small- should be made large, or the Table should be re-arranged.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses the problem of out-of-distribution (OOD) detection, crucial for enhancing the robustness of deep learning models. The authors propose a novel method called S & I (Splitting & Integrating) that improves on existing gradient-based OOD detection approaches like GAIA by introducing adversarial examples and integrating gradient attribution across split intermediate layers of the neural network. The S & I algorithm smooths gradient fluctuations and identifies true explanation patterns, outperforming state-of-the-art (SOTA) methods on CIFAR100 and ImageNet benchmarks, as shown through extensive experiments.

### Strengths
+ The introduction of layer splitting combined with adversarial gradient attribution integration is innovative.
+ The method demonstrates superior performance on CIFAR100 and ImageNet benchmarks, achieving lower FPR95 and higher AUROC compared to baselines.
+ The paper provides a mathematical basis and proofs for the concepts introduced.
+ The authors evaluate their approach against multiple baseline methods, showcasing clear advantages.

### Weaknesses
 - On CIFAR100, the performance gains over GAIA are not substantial, suggesting limited effectiveness in smaller label space datasets.
- The algorithm's complexity, involving iterative adversarial updates and integration across multiple layers, may hinder scalability or applicability to extremely large models.

### Questions
- Have you considered the potential security risks introduced by using adversarial examples as baselines, and how might this affect deployment?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes the S&I method to enhance the performance of OOD detection.

### Strengths
1 The structure is clear.

### Weaknesses
1 The experimental results are suboptimal, with an average improvement of no more than 0.5% (AUROC metric) across different datasets. If the improvement is not significant, it suggests that the problem addressed in this paper may not be highly important. Please provide an experiment that can significantly enhance performance.

2 In Figure 2, the meanings of the x and y axes are not explained; the two histograms on GAIA lack subtitles to distinguish them. Please clarify these details.

3 The first two contributions summarized in the last paragraph of Chapter 1 require an ablation study to demonstrate their effectiveness separately.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Due to the non-zero gradient behaviors of OOD samples, which do not exhibit significant distinguishability, this negatively impacts the accuracy of OOD detection. Considering this issue, the paper proposes a novel OOD detection method called S & I based on layer Splitting and gradient Integration via Adversarial Gradient Attribution. The proposed method incorporates adversarial attacks into attribution to explore the distributional characteristics of ID and OOD samples. Experiments demonstrate that S & I algorithm achieves state-of-the-art results.

### Strengths
The proposed method has been evaluated on multiple datasets.  
The paper provides theoretical proof to ensure the rationality of the method.

### Weaknesses
1. The experiments conducted in the paper do not effectively support the proposed arguments.  
a) The paper mentions that "we argue that the non-zero gradient behaviors of OOD samples do not exhibit significant distinguishability, especially when ID samples are perturbed by random noise in high-dimensional spaces, which negatively impacts the accuracy of OOD detection." However, the experiments in the paper are just some general evaluations and do not highlight the points argued above. There is no experiment to discuss detecting the non-zero gradient behaviors of OOD samples. Specifically, the paper lacks experiments that directly measure the distinguishability of gradients between ID and OOD samples, particularly when ID samples are perturbed with noise. This is a critical omission because the core motivation is based on this claim, and without direct evidence, the argument remains unsubstantiated. Furthermore, the paper does not provide any quantitative analysis of how the proposed method improves the distinguishability of these gradients.
b) There is a lack of ablation studies to verify the importance of each part. Specifically, there is no baseline comparison against a model without the layer-splitting component, nor a model trained without adversarial examples. This makes it difficult to assess the individual contribution of each component to the overall performance.

2. The distributional differences caused by adversarial attacks are completely different from the differences between various datasets. Why can introducing adversarial attacks enhance OOD detection across different datasets? The paper does not adequately explain why training with adversarial examples, which are designed to fool a model within the same data distribution, would generalize to detecting OOD samples, which come from entirely different distributions. The underlying mechanism of how adversarial perturbations translate to improved OOD detection is not clear. It is also unclear if the adversarial examples are simply acting as a form of data augmentation, and if so, why this particular form of augmentation is superior to other methods.

3. Can the proposed OOD detection be applied to distinguish between adversarial examples and clean examples? The paper does not address whether the proposed method, which is trained using adversarial examples, can be used to detect adversarial examples themselves. This is a relevant question, as adversarial examples can be seen as a specific type of out-of-distribution data. If the method cannot distinguish between adversarial and clean examples, it raises questions about its robustness and practical applicability.

4. Is OOD detection still important in current deep learning? For example, in classification tasks with adversarial examples, one approach to avoid outputting the incorrect labels is to use detectors to refuse adversarial examples and only allow clean examples to be classified. However, these methods are gradually being abandoned because a robust system should be able to output correct labels for any input, not just simply refuse to output labels for adversarial examples. Therefore, under the settings of this paper, I am curious about which specific scenarios the OOD method is applicable or necessary to at present.

5. Due to the presence of adversarial attacks and layer-splitting technology, will this lead to the consumption of a large amount of computational cost in the whole process?

Since I am not completely familiar with this task, I have set the confidence as 2.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
