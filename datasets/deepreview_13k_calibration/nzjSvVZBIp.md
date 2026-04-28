# An Effective Manifold-based Optimization Method for Distributionally Robust Classification

- Decision: Accept
- Avg Score: 5.60
- Scores: 6, 5, 6, 6, 5

## Abstract
How to promote the robustness of existing deep learning models is a  challenging problem for many practical classification tasks. Recently, Distributionally Robust Optimization (DRO) methods have shown promising potential to tackle this problem. These methods aim to construct reliable models by minimizing the worst-case risk within a local region (called ''uncertainty set'') around the empirical data distribution. However, conventional DRO methods tend to be overly pessimistic, leading to certain discrepancy between the real data distribution and the uncertainty set, which can degrade the classification performance. To address this issue, we propose a manifold-based DRO method that takes the geometric structure of training data  into account for constructing the uncertainty set. Specifically, our method employs a carefully designed ''game'' that integrates contrastive learning with Jacobian regularization to capture the manifold structure, enabling us to solve DRO problems constrained by the data manifold. By utilizing a novel idea for approximating geodesic distance on manifolds, we also provide the theoretical guarantees for its robustness. Moreover, our proposed method is easy to implement in practice. We conduct a set of experiments on several popular benchmark datasets, where the results demonstrate our advantages in terms of accuracy and robustness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a manifold-based DRO method that incorporates the geometric structure of training data to construct the uncertainty set. By integrating contrastive learning with Jacobian regularization, the method effectively captures the data manifold, providing theoretical guarantees for robustness. Experimental results on benchmark datasets demonstrate improved accuracy and robustness compared to conventional DRO methods.

### Strengths
1. The proposed manifold-based DRO method effectively captures the geometric structure of training data, leading to better robustness and accuracy compared to traditional DRO methods. This is achieved by integrating contrastive learning with Jacobian regularization, which helps in maintaining the data manifold structure.
2. The method provides theoretical guarantees for robustness by utilizing a novel approach to approximate geodesic distances on manifolds. This ensures that the model remains reliable even when faced with distributional shifts in the data.
3. Despite the complexity of incorporating manifold constraints, the proposed method is easy to implement and computationally feasible. The authors demonstrate this through experiments on popular benchmark datasets, showing that the method achieves superior performance without significant increases in computational cost.

### Weaknesses
I believe the motivation of this paper is reasonable and the method is effective. However, I would like to ask the authors whether the effectiveness of the algorithm depends on specific data? What kind of data characteristics would give MWDRO a greater advantage?

### Questions
See Weaknesses above.

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
5

### Summary
This paper proposes performing distributional robustness (DR) over data manifolds. It develops the dual form of DR over data manifolds and    uses the top singular principal vectors of the Jacobian matrix to characterize the tangent space of the data manifolds.

### Strengths
- The idea of developing distributional robust on data manifolds is intuitive and interesting.
- The paper is well-written.

### Weaknesses
 - It is unclear why we can use the linear span of top singular vectors of the Jacobian matrix of g can characterize the tangent space of data manifolds. The current explanations do not really convince me. Moreover, the experiments in Figure 2 only demonstrate that there are some dominant singular vectors and I cannot see how it explains why $T_{appr}(x, \tau_0)$ is a subspace of the tangent space. Specifically, the connection between the partial derivatives in the Jacobian and the local defining function of the manifold is not clearly established. It's not sufficient to say that the Jacobian captures how the representation changes; the link to the tangent space via a local defining function needs to be more explicit. Furthermore, it's unclear why the top singular vectors are used instead of the partial derivatives themselves, given that the columns of the Jacobian already represent partial derivatives along each input dimension.
- It is also unclear to me why the game in Section 4.2 helps extract tangent information. Evidently, the CL loss encourages the features of data examples in $M_{SI}(x)$ to be close, whereas the Jacobian regularization suppresses the feature variations for perturbations of x across all directions. They seem to share the same purpose and nature. The contrastive loss encourages similar representations for semantically similar samples, while the Jacobian regularization penalizes changes in the representation due to input perturbations. These two regularizations appear to be redundant, and it's not clear how they cooperate to extract the tangent space information.
- It is unclear to me why we can use the $pt^t$ in Alg 2 to approximate the geodesic distance from $q^t$ to $q^0$. The justification for using the accumulated discrete step sizes as an approximation of the geodesic distance is weak. While the strong concavity property is mentioned, the link between this property and the accuracy of the approximation is not clearly explained. A more rigorous analysis is needed to show that this approximation is valid.
- It is unclear how to do Exp operator to retract to the data manifolds. This seems impossible because we only assume that data lie in manifolds but we do not have anymore information of these manifolds. The Exp operator appears closed-form just for some simple and specific manifolds. The use of the exponential map is not well-defined, as it requires knowledge of the manifold structure, which is not available. Approximating it with a linear retraction $x+v$ is not a true retraction onto the manifold and does not guarantee that the resulting point remains on the manifold.
-  The proposed method is very computationally expensive, even more expensive than adversarial training. This is because we need to compute a trajectory for each data example which requires computing Jacobian matrix and also the gradients to data examples. The analysis on the computational complexity is necessary. The computational cost is a major concern, as the method requires computing the Jacobian and gradients for each data point, making it significantly more expensive than standard adversarial training. A detailed analysis of the computational complexity, including the cost of SVD and trajectory computation, is needed.
- The experiments do not demonstrate the benefit of performing DR on data manifolds. It would be better if the authors keep the same CL loss and Jacobian regularization, while replacing their manifold DR by standard DR on data space for a comparison. Moreover, the authors should provide the visualization of $q^1$,...,$q^t$ on the trajectory to see if we can make them on the data manifolds.

### Questions
Please address my questions in Weaknesses.

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
This paper introduces a manifold-based Wasserstein Distributionally Robust Optimization (WDRO) method aimed at improving the robustness of deep learning models. Furthermore, to tackle the challenges posed by the data manifold structure, the authors propose a game that integrates contrastive learning with Jacobian regularization.

### Strengths
S1. The paper is well-organized and presents its ideas clearly.
S2. The proposed methods demonstrate superior performance compared to state-of-the-art algorithms.
S3. The design of the manifold-guided game is a novel concept, leveraging neural networks to encode manifold information, particularly given the absence of a closed-form representation for the data manifold.

### Weaknesses
W1. The motivation for this work could be strengthened. In the Introduction, the authors mention that selecting an appropriate threshold for uncertainty is challenging and introduce a new uncertainty set by assuming that data is supported on a manifold. However, constraining the uncertainty set to manifolds also raises the same issue of threshold selection. The paper does not adequately address how the manifold constraint alleviates the fundamental challenge of choosing an appropriate uncertainty threshold, as the selection of a manifold radius or similar parameter introduces a similar problem. The authors need to clarify how their approach avoids the same issues of sensitivity to threshold selection that plague standard WDRO methods.

W2. The explanation of how the game aids in extracting tangent information is not intuitive enough. Including a figure to illustrate this concept would be beneficial. The current description lacks a clear explanation of how the contrastive learning objective, combined with Jacobian regularization, leads to the extraction of meaningful tangent information. A more detailed explanation, possibly with a visual aid, is needed to clarify the mechanism by which the proposed game learns the local geometry of the data manifold.

W3. As the experimental results show, MWDRO takes more time compared to other algorithms, and it would be desirable to have a further discussion on this part of the reason. The paper should include a more detailed analysis of the computational overhead introduced by the manifold-guided game. It is not sufficient to simply state that it takes more time; the authors should provide a breakdown of the computational costs associated with each component of the proposed method, particularly the Jacobian computation and SVD, and discuss potential strategies for optimization beyond randomized SVD.

### Questions
Q1. In Figure 3, the accuracy of each model is already distinguishable even when the noise size is 0. Could you provide further discussion on this observation?
Q2. Is the use of contrastive learning essential in the design of the manifold-guided game? Are there alternative optimization objectives that could be utilized instead?
Q3. As noted in W3, could you further analyze which phase of training contributes to the increased time required for MWDRO?
Q4. Is it possible to further optimize the design of the algorithm to reduce the time to loss? For example, by utilizing simplified geometric computations or low-rank approximations.

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
3

### Summary
This paper proposed a manifold-based distributionally robust optimization method to promote the robustness of existing deep learning models. Specifically, it designed a game that trades off between CL and Jacobian regularization to solve the DRO problem constrained by the data manifold. Both theoretical and empirical results show the robustness of the proposed method.

### Strengths
1. The proposed method is simple and effective. 
2. This paper provides a comprehensive analysis of their proposed method.

### Weaknesses
1. This paper should be further polished and re-organized. The introduction and methodology section should be more concise, and some contents should be moved to a more relevant part. I provide the details as follows: 1) the introduction of WDRO from line 49 to 71 can be more brief. 2) I can understand that the authors discussed the most relevant literature in Section 1.1, but the structure is a little strange. I suggest considering this part as a discussion part such as "Relation to xxx".  3) In the methodology, I also suggest the authors provide the literature or experiment support for the sentence that "we should emphasize that the learned representation for manifold from neural networks is not sufficient for extracting tangent space". 4) Eq (2) as a significant part of the methodology is mentioned in Section 1, which makes the methodology separate. I suggest the comparison between WDRO and MWDRO in the introduction being high-level, while its details can be put into Section 3 as the motivation. 
2. Some significant ablation studies are missing. For example, the effect of $\lambda$ and model architectures has not been discussed. I suggest the authors test a range of values of $\lambda$ to test its effect. As for the model architectures, the authors only provided ResNet18, which is insufficient. I suggest the authors try some state-of-the-art models such as ConvNext and Swin.
3.  The authors should clarify the advantages of the proposed method compared with [1] in Related Works and Experiments.

### Questions
1. Could you please discuss the effect of $\lambda$ and how to select the optimal value?
2. Could you verify the effectiveness of your proposed method on different model architectures such as ConvNext or Swin?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a novel manifold-based Distributionally Robust Optimization (DRO) method aimed at enhancing the robustness of deep learning models against distributional shifts. By integrating contrastive learning with Jacobian regularization, the proposed approach captures the manifold structure of the training data to construct a more accurate uncertainty set, thereby improving classification performance under various distributional changes.

### Strengths
1.	Writing: This work is presented with good writing style, where the summarized problems with detailed explanations make it easy for readers to understand the problem addressed in this article. However, there exist minor spelling and grammatical errors. The example in Fig.1 helps to understand the connections between geometric representation and semantic tasks.

2.	Novelty: It incorporates geometric structure into the construction of the uncertainty set, potentially leading to more realistic distributional assumptions. Contrastive learning with Jacobian regularization to encode manifold information is novel and seems to consume more geometric information. 

3.	Theory: Theorems 1&2 based on geometric scheme provides guarantees on approximation and gradient estimation, offering strong dual reformulations and approximation techniques for geodesic distances, which are crucial for establishing the method's reliability. 

The proof seems solid but I have not carefully checked the whole Appendix. 

4.	Experiments: Several scenarios and recent baselines are considered, implying improvements in accuracy and robustness under various distributional shifts.

### Weaknesses
1.	Approximation. There exists a gap between optimal solutions from original and dual problems. I’m not sure if Theorem 1 states the distances between the original and dual objects? 

2.	Selection on v. The bound derived in Theorem 1 heavily relies on v. I would appreciate it if the authors could give more detailed illustrations on the “dynamic mechanism” on setting v empirically?

3.	Broader baselines and empirical settings. 
For example, the settings for “Noisy Data” are kind of simple. What’s the variance of the added Gaussian white noise? It is suggested to follow the empirical settings in [1] to widen the difference between the training and testing sets, see Table 1 in [1]. 

More DRO approaches [1-3] for learning from noisy data are suggested to be included.
Moreover, it is kindly suggested to add introductions to these baselines in the supplementary file for better readability.

4.	Illustrations on manifolds. The paper could benefit from a more in-depth analysis of the algorithm's scalability, especially regarding its performance with large datasets or specific manifold structures. 
Synthetic experiments on toy examples with already known geometric structure, e.g., the Swiss or Torus, could help to visualize and estimate the investigated manifolds.


5.	Computational Cost. While the theoretical underpinnings are well-developed, the paper may not provide a comprehensive assessment of the computational efficiency and practicality of the proposed method in real-world applications. Like the computational complexity analysis or empirical time/memory cost.

### Questions
Please see the comments in Weakness.

I would be happy to raise my score if these issues are well addressed.

### Soundness
3

### Presentation
3

### Contribution
2
