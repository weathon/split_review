# Gradient Inversion Transcript: A Generative Model to Reconstruct Training Data by Gradient Leakage

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 3, 6

## Abstract
We propose Gradient Inversion Transcript (GIT), a generic approach for reconstructing training data from gradient leakage in distributed learning using a generative model. Unlike traditional gradient matching techniques, GIT requires only the model architecture information, without access to the model's parameters, making it more applicable to real-world distributed learning settings. Additionally, GIT operates offline, eliminating the need for intensive gradient requests and online optimization.
Compared to existing generative methods, GIT adaptively constructs a generative network, with an architecture specifically tailored to the structure of the distributed learning model. Our extensive experiments demonstrate that GIT significantly improves reconstruction accuracy, especially in the case of deep models.
In summary, we offer a more effective and theoretically grounded strategy for exploiting vulnerabilities of gradient leakage in distributed learning, advancing the understanding of privacy risks in collaborative learning environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces GIT, a novel gradient reconstruction attack designed for scenarios where the parameters of the victim models are unknown and only partial training data is accessible. GIT first leverages the available training data to pre-train a proxy model that can generate gradients identical to those produced by the victim client models when given the same data. This is accomplished by computing the inverse of each layer and minimizing the distance between the final reconstructed input and the original data. Once trained, the proxy model enables the attacker to reconstruct the victims' private data upon receiving gradients from the clients. Experimental results demonstrate that GIT achieves lower mean squared error (MSE) compared to previous methods.

### Strengths
1. The task considered in this paper is meaningful.
2. The attempt to relax the assumption and find a proxy model is interesting.

### Weaknesses
1. My main concern is the assumption. While the authors claim that they relax assumptions, their assumptions are impractical or barely different from those of the existing works.
    - Access to training data. This violates the privacy protection attempt in FL in the first place. The authors currently use up to 10000 training images, i.e., 20% of the original dataset size. While people could argue that some publicly available data is shared online, the authors should design more coherent experiments to support their claim and conduct an ablation study on the effect of available data points. The core issue is that the attack model is trained on a substantial portion of the training data, which is not a realistic scenario in federated learning where data is distributed and private. The paper needs to clarify the practical implications of this assumption and how it compares to scenarios where no such data is available to the attacker. Furthermore, the paper should explore the sensitivity of the attack to the size and distribution of this leaked data.
    - The training data labels are unknown. The authors assume access to the training data but not labels, which is counterintuitive. It is unclear why an attacker would have access to the data but not the corresponding labels, especially given that labels are typically required for training any supervised model. This assumption needs further justification, as it is not a standard setting in the context of federated learning attacks. The authors should clarify the specific scenario where this assumption holds true.
    - No access to clients' model parameters but per-client gradients. While the authors claim the former, their approach highly relies on the latter, which seems equivalent and thus contradicts their claim. A more reasonable problem formulation would be to use the aggregated gradients solely. This is more practical as the FL server can only observe the aggregated gradients when using protocols like homomorphic encryption. The reliance on per-client gradients is a strong assumption, as in many practical FL settings, only aggregated gradients are available to the server. The authors should justify why they need per-client gradients and not aggregated gradients, and they should discuss the implications of this assumption on the applicability of their method.
2. Claims of offline training. Despite the claim, the authors require clients to produce gradients. How do they do it offline? The term 'offline training' is misleading since the proposed method requires access to client gradients, which are inherently generated during the online training process of federated learning. The authors need to clarify the exact meaning of 'offline' in their context and how it differs from the standard online training process in federated learning.
3. Limited experiments.
    - The authors conduct experiments only on two models and one dataset. The experimental evaluation is limited in scope, as it only considers two models and one dataset (CIFAR-10). This raises concerns about the generalizability of the proposed method to other architectures and datasets. The authors should extend their experiments to include a wider range of models and datasets to demonstrate the robustness of their approach.
    - The considered baselines might not be valid as they consider totally different assumptions. The comparison with baselines is problematic because the baselines operate under different assumptions. This makes it difficult to assess the true performance of the proposed method relative to existing techniques. The authors should carefully select baselines that align with their assumptions or provide a clear explanation of the differences in assumptions and their impact on the results.
    - (Minor) While I understand it is challenging and may take time to solve, the authors only consider small batch sizes and small images. The focus on small batch sizes and small images limits the practical relevance of the proposed method. The authors should investigate the performance of their method on larger batch sizes and higher-resolution images to demonstrate its scalability and applicability to real-world scenarios.
4. Experiment design.
    - More insightful analysis could be conducted, such as the distance between the learned weights and the victim model weights and performance when using OOD or hold-out datasets. The analysis lacks depth, as it does not explore the relationship between the learned weights and the victim model weights. Furthermore, the authors should evaluate the performance of their method on out-of-distribution (OOD) or hold-out datasets to assess its generalization capabilities. This would provide a more comprehensive understanding of the method's strengths and limitations.
    - Moreover, the authors currently only report MSE errors. It is known that MSE errors might not directly translate to visual quality. It would be interesting to additionally measure perception loss or inception score. Otherwise, as the results presented in Figures 2 and 3 show, it is difficult to judge what kind of information is leaked. The evaluation metric is limited to MSE, which is not a reliable indicator of visual quality. The authors should include additional metrics such as perceptual loss or inception score to provide a more comprehensive evaluation of the reconstructed images. The current results make it difficult to assess the practical impact of the attack.
    - Can the proposed method scale up to larger images beyond cifar10?

Overall, while the proposed technique is interesting, it might not fit in the application or is not ready for publication at this point.

Editorial comments:
1. (minor) I recommend the authors provide an overview and state the contributions at the beginning of Sec. 3. Given the current presentation, I feel the readers might get lost.
2. The term "threat model" often refers to the problem settings and the assumptions for both the attacker and the defender in most privacy, security-related work.

### Questions
1. What does $\sigma^\prime$ mean in L167?
2. In L194, there are two $\sigma$.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes the Gradient Inversion Transcript (GIT), focusing on its theoretical basis and empirical application in reconstructing training data with generative model. The setting is that the model could only get access to the leaked gradient. The central concept relies on a mathematical extension based on Equation 4 and gradient-based back-propagation. The paper conducts experiments on the CIFAR-10 dataset and reconstructs images with lower MSE error than the baselines.

### Strengths
GIT introduces a theoretically informed generative model tailored to the target model’s architecture, making it expirically better compared to traditional fixed architectures.

### Weaknesses
Several critical weaknesses are listed below:

[Theoretical Side]: 

The theoretical benefits from the paper is limited. GIT is essentially based on Equation 4, and Equation 4 is a straightforward extension and observation from the gradient back-propagation.

[Empirical side]: 

1.The empirical experiment is limited. Experiments are only conducted on cifar10 dataset.

2.Lack of important implementation details in the experiments.
What is the size of the fixed MLP layers? Does it have the same number of parameters of the NN discovered by GIT for fairness?
Also the implementation of the baselines are blank. There is no images generated by the baseline shown in the paper.

3.Lack of important experiment results in the experiments. What is the optimized neural network architecture? How similar is it towards the target leaked model? How to define a metric to illustrate the effectiveness of the optimized neural network structure?

### Questions
1.The paper does not consider the UNet structure as a baseline, Why UNet leverages priors from public data? It actually should be a wel-established widely used baseline.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes GIT (Gradient Inversion Transcript) to reconstruct training data from gradient information in distributed learning settings. Unlike previous methods that require model parameters or repeated gradient queries, GIT only needs model architecture information and works offline. It adaptively designs the generative network's architecture based on the target model's structure, theoretically derived from backpropagation equations. The authors demonstrate better reconstruction accuracy compared to baselines, especially for deeper models.

### Strengths
1. The adaptive architecture of the generative model, mirroring the target model's structure, allows for more effective exploitation of gradient information compared to fixed-architecture generative methods.
2. The paper considers a practical attack scenario where the adversary only has access to shared gradients without knowledge of model parameters, labels, or the ability to query the model. This aligns with real-world constraints faced by attackers.
3. The method has some theoretical analysis of backpropagation, providing a stronger justification for the design choices compared to purely heuristic approaches.

### Weaknesses
1. Overfitting issues: The authors acknowledge significant overfitting problems but don't provide solutions
2. Experimental scope: Experiments are primarily limited to CIFAR-10 and two specific network architectures (LeNet and ResNet).
3. Baseline comparison: The paper lacks a comprehensive comparison with state-of-the-art methods, making it difficult to conclude the superiority of GIT over existing approaches.

### Questions
1. Theoretical Foundation of the approximation: The paper uses the pseudo-inverse for approximation. While the pseudo-inverse offers a solution for non-invertible matrices, the paper lacks a theoretical justification for its application in this specific context. Furthermore, are there any analytical bounds on the error introduced by this approximation, and how does this error may propagate through the reconstruction process?
2. Practical Applicability and Advantages of MLPs: Given the acknowledged numerical instability of directly computing approximation, the paper often resorts to using MLPs for approximation. This raises questions about the practical advantages of GIT over simply training a larger, more complex MLP directly from gradients to input data. If MLPs are primarily used, what specific advantages does GIT retain over other generative methods? Any explanation on why GIT may still have an edge over MLP methods?

### Soundness
2

### Presentation
1

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
The authors a method called propose Gradient Inversion Transcript (GIT) relying on generative models to reconstruct the input. GIT does not rely on model weights but only needs the model architecture. The authors claim that this makes it more applicable to the real world setting. Further, their method adaptively chooses an architecture for the generative method. 

Their experiments where conducted over LeNet and ResNet for batch sizes of up to 4 over the CIFAR-10 dataset, demonstrating the effectiveness against baselines. Further, they conduct an ablation study over the number of training samples used to train their model.

### Strengths
- Gradient inversion attacks are a crucial way to investigate the privacy of federated learning methods. 
- The training approach as formalized in Algorithm 1 seems interesting and novel. 
- It is good to demonstrate the effectiveness of this method in the setting of noisy gradients. 
- The paper was overall easy to read.

### Weaknesses
 - The threat model appears to be not well motivated: It is unclear in which scenario an attacker has access to the gradient updates but not the  model weights. In other words - what is the incentive to not prevent sending gradients to 3rd parties that do not contribute to training? Following that - how is it more practical for the attacker to have access to input-gradient pairs? Where would they come from in practice. 
- It is unclear if the claim that some assumptions are stronger holds here in practice? Specifically, what is a stronger assumption - having sufficient training data or the network weights? There are some approaches that do not rely on priors on the dataset, don't need multiple gradient querying, no labels and are exact (see [1] and [2]). Also the math appears related. 

Further:
- L33 - the sentence after "federated learning (FL)" does not seem complete. 
- L48 - the use of the term "threat model" for the model doing the attack is unfortunate, unnecessarily overloading there this term. This is problematic because the authors claim relevance of a weaker threat model where the attacker does not have access to model weights. 
- Table 3 - maybe the best reported number could be bolted. 

Citations:
- 1) Dimitrov et al. "SPEAR: Exact Gradient Inversion of Batches in Federated Learning", https://arxiv.org/abs/2403.03945
- 2) Petrov et al. "DAGER: Exact Gradient Inversion for Large Language Models", https://arxiv.org/abs/2405.15586

### Questions
- How does it generalize to Federated learning settings like federated averaging? 
- What Architectures? Appears that only linear and skip connections can be dealt with (Section 3). What about say transformer architectures? 
- In which circumstances is the threat model realistic? Access to lost of training data but not the model weights?
- Given the number of training samples of inputs and gradients - could one adapt gradient matching techniques to weight matching techniques to reconstruct weights? 
- How does your approach scale to larger batch sizes and more complex datasets? How do you scale to deep networks? Does the reviewer suppose correctly that this is more difficult? 

Typos
- 194: "Since both $\sigma$ and $\sigma$" appears wrong
- 245 - there should be $\{\}$ around $g_i$.

### Soundness
3

### Presentation
3

### Contribution
3
