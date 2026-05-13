# Latent Point Collapse Induces an Information Bottleneck in Deep Neural Network Classifiers

- Decision: Reject
- Scores: 3, 6, 3, 5

## Abstract
The information-bottleneck principle suggests that the foundation of learning lies in the ability to create compact representations. In machine learning, this goal can be formulated as a Lagrangian optimization problem, where the mutual information between the input and latent representations must be minimized without compromising the correctness of the model's predictions.
Unfortunately, mutual information is difficult to compute in deterministic deep neural network classifiers, which greatly limits the application of this approach to challenging scenarios. In this paper, we tackle this problem from a different perspective that does not involve direct computation of the mutual information. We develop a method that induces the collapse of latent representations belonging to the same class into a single point. 
This point collapse not only significantly reduces the entropy of the latent distribution, thereby creating an information bottleneck that correlates with improved generalization, but also makes the network Lipschitz, offering guarantees for enhanced robustness.
Our method is straightforward to implement. We demonstrate that it substantially improves the network's robustness, provides a small yet statistically significant increase in generalization, and enhances the network's ability to detect misclassifications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new approach to compress feature vectors by integrating a bottleneck layer and incorporating L2 norm regularization for the newly added layer. This method is grounded as an surrogate for the Lagrangian optimization framework, aiming to minimize mutual information loss.

### Strengths
- The proposed approach is straightforward and easy to implement, requiring the addition of only a single bottleneck layer and minimal modification of the loss function
- The empirical results effectively demonstrate the method’s ability to reduce entropy, aligning well with the theoretical intuition presented in the paper.

### Weaknesses
 - The empirical improvements are unconvincing, as the study lacks comparisons with other established regularization techniques.
- The experimental setup is also limited, with no evaluations conducted on large-scale datasets, such as ImageNet for image classification or Wikitext for language modeling.
- The paper does not provide a theoretical guarantee that the proposed method reduces mutual information loss.

### Questions
- Could you include additional baselines to compare your method with other regularization techniques for a more comprehensive evaluation?
- Since your approach appears to induce neural collapse, could you provide a comparison with methods that explicitly leverage neural collapse to enhance model performance?
- Could you offer a theoretical proof or rationale to substantiate that minimizing the proposed loss function effectively reduces mutual information loss?
- Could you consider adding experiments on large-scale datasets to enhance the empirical evaluation of the paper?

### Soundness
2

### Presentation
3

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
The paper investigates a phenomenon termed latent point collapse by introducing information bottleneck (IB) layers and modifying the loss function in neural networks. Through an information-theoretic lens, the paper derives the loss function and demonstrates its effects. Experimental results indicate that incorporating IB layers enhances the network's robustness to input perturbations and improves reliability in predictions.

### Strengths
* The paper is overall clearly written.
* The experiments on the improved robustness when adopting the IB layer are persuasive and interesting.

### Weaknesses
The paper would benefit from a more detailed comparison with the existing Neural Collapse (NC) literature. Based on the reviewer's understanding, the main distinctions between this work and NC research lie in two areas:
* Architectural Addition Between Penultimate Layer and Classifier: This paper introduces an extra architectural component between the penultimate layer and the classifier. However, if we interpret the output of this new component as the features used in NC, the framework here still aligns with the NC paradigm. Additionally, the loss function presented in Equation (3) closely resembles the unconstrained feature models commonly employed in NC studies.
* Class Number Exceeding Feature Dimension: This study explores scenarios where the number of classes can exceed the feature dimension, a setup less frequently examined in NC literature. However, recent works have addressed this case, as in [1] and [2]. The authors may want to discuss these works more closely. 

The binary encoding structure shown in Figure 1 appears to represent a single class. Could the authors clarify the relationship between the features of different classes within this structure?

The paper employs the Swish activation function for all experiments. How would the results differ with the standard ReLU activation? The binary encoding won't be possible in this scenario.

In Tables 1 and 2, the NOPEN architecture seems to represent the default ResNet model without architectural modifications. How would applying the loss function from Equation (3) directly to the true penultimate layer affect the results? Would it still exhibit the benefits of the Information Bottleneck (IB) method?

### Questions
* The binary encoding structure shown in Figure 1 appears to represent a single class. Could the authors clarify the relationship between the features of different classes within this structure?

* The paper employs the Swish activation function for all experiments. How would the results differ with the standard ReLU activation? The binary encoding won't be possible in this scenario. 

* In Tables 1 and 2, the NOPEN architecture seems to represent the default ResNet model without architectural modifications. How would applying the loss function from Equation (3) directly to the true penultimate layer affect the results? Would it still exhibit the benefits of the Information Bottleneck (IB) method?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a method that induces the collapse of latent representations belonging to the same class into a single point, creating an information bottleneck in machine learning models. By focusing on reducing the entropy associated with the latent distribution, the method enhances the network's robustness, generalizability, and reliability without the need for direct computation of mutual information.

### Strengths
>The paper introduces a novel method to avoid calculating mutual information in IB settings.

>Some improvements are achieved on 3 standard benchmarks.

### Weaknesses
The improvements seem to be marginal, for e.g. in Table 1.

Some more experiments are expected on larger datasets like ImageNet.

Some theoretical benefits of applying the proposed method in IB are needed.

There seem to be discussions of neural collapse and information theory in the literature [1] [2] that are closely related but are not discussed.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents an innovative approach to enhancing robustness and generalization in deep neural network classifiers. The authors introduce an additional linear layer as the latent feature layer, along with a regularization term for the learned latent features. They claim that this method creates compact representations of input data by inducing a latent point collapse, where same-class representations converge into single points in the latent space, effectively reducing entropy and creating a bottleneck effect without the need to directly compute mutual information.

### Strengths
The proposed method is easy to implement and slightly increases classification accuracy.

### Weaknesses
1. **Lacking of rigorous analysis**. Although the authors claim that their method leads to the collapse of all same-class representations into a single point, there is no theoretical proof to substantiate this claim. The analysis provided is heuristic and lacks mathematical rigor. For example, the paper claims that optimizing the cross-entropy loss is equivalent to maximizing $W_{\bar{y}}^T z$, but this equivalence is not rigorously derived. The bias term is not explicitly addressed, and the assumption that the weight vector of the true label $W_{\bar{y}}$ forms a hypercube is not justified. Projecting a hypercube from a high-dimensional space to a lower-dimensional space does not necessarily preserve the hypercube structure, and the claim that $W_{\bar{y}}$ must form a hypercube for its low-dimensional projection to exhibit such a structure is not substantiated.
2. **Lacking of experiment proof**. The experiments show that the entropy and covariance of latent features decrease, but these metrics could naturally decline due to the regularization term applied to $z$. Clear evidence of latent feature collapse is lacking, such as metrics comparing the distance between class centers or between the origin and class centers. The authors claim that class points are located at the vertices of a hypercube, but the evidence provided does not support this claim. A small within-class covariance, $\Sigma_w$, only implies that latent representations for the same class collapse into a single point, but it does not prove that these points are equidistant from the origin or that they lie at the vertices of a hypercube. The claim that each class point must occupy a distinct position equidistant from the origin is not empirically demonstrated.

### Questions
Currently, the paper is purely hypothetical, lacking both theoretical and empirical evidence of latent point collapse.

### Soundness
2

### Presentation
2

### Contribution
1
