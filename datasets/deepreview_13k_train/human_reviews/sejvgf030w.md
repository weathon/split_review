# Towards Flexible and Controllable Unknown Rejection

- Decision: Reject
- Scores: 5, 8, 5, 3

## Abstract
Reliable prediction is an essential requirement for deep neural models that are deployed in open environments, where both covariate and semantic out-of-distribution (OOD) data arise naturally. Recent studies have formulated and pursued two problems named OOD generalization and detection independently, where the former aims to correctly recognize covariate shifts while the latter focuses on rejecting semantic shifts. However, existing methods are misaligned with real-world applications in two aspects. First, in practice, to make safe decisions, a reliable model should accept correctly recognized inputs while rejecting both those misclassified covariate-shifted and semantic-shifted examples. Second, considering the potential existing trade-off between rejecting different failure cases, more convenient, controllable, and flexible unknown rejection approaches are needed. To meet the above requirements, we propose a novel and elegantly simple unknown rejection framework to unify and facilitate classification with rejection under both covariate and semantic shifts. Our key insight is that by separating and consolidating failure-specific reliability knowledge with low-rank adapters and then integrating them, we can enhance the unknown rejection ability effectively and flexibly. Extensive experiments demonstrate the superiority of our framework.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper addresses the challenge of unknown rejection under both covariate and semantic shifts in deep neural models. The authors argue that existing methods for out-of-distribution (OOD) generalization and detection are misaligned with real-world applications because they either lack a rejection option or struggle with covariate shifts. TrustLoRA unifies classification with rejection by separating and consolidating failure-specific reliability knowledge using low-rank adapters, allowing for flexible and controllable unknown rejection. The framework enhances the model's ability to accept correctly classified covariate-shifted examples while rejecting misclassified ones and unknown semantic-shifted samples. Extensive experiments demonstrate TrustLoRA's superiority in handling unknown rejection compared to existing methods, showcasing its potential for safe and reliable AI applications.

### Strengths
- The paper proposes TrustLoRA, a simple unknown rejection framework that unifies classification with rejection under both covariate and semantic shifts, addressing a gap in real-world application requirements for deep neural models.

- TrustLoRA offers a flexible and controllable approach to unknown rejection, allowing for the adjustment of the model's reliability strength based on user preferences without the need for full retraining, which is an advantage in dynamic environments.

- The use of low-rank adapters for separating and compressing reliability knowledge is innovative, leading to a parameter-efficient method that is computationally lightweight and efficient, which is beneficial for models that need to adapt quickly to new failure cases.

- The paper provides extensive experimental results demonstrating TrustLoRA's strong performance in various scenarios, including different severities of covariate shifts and semantic shifts, showcasing its robustness and effectiveness.

### Weaknesses
 - Although Proposition 3.1 is presented in the main paper, its proof is not provided.

- When the pre-trained model is fixed and only the LoRA module is fine-tuned, how can we ensure that the model avoids underfitting? Specifically, how can knowledge consolidation be effectively integrated into the model? It's unclear how the low-rank adaptation, which introduces a limited number of parameters, can effectively capture the complexity of reliability knowledge, especially when the pre-trained model's parameters are frozen. The risk of underfitting is a significant concern, as the LoRA module might not have sufficient capacity to learn the nuances of both covariate and semantic shifts.

- The authors referenced [R1] in the Introduction, which also addresses covariate and semantic shifts, yet a comparative analysis with these results is absent from the experiments. This is a critical omission, as it's necessary to benchmark the proposed method against existing approaches that tackle similar challenges. Without this comparison, it's difficult to assess the true novelty and effectiveness of TrustLoRA.

- Additional experiments on large-scale datasets, such as ImageNet, are necessary to further demonstrate the effectiveness of the proposed methods. The current experiments are limited to smaller datasets, which may not fully reflect the performance of the method in more complex, real-world scenarios. The scalability of TrustLoRA to larger datasets and more complex models remains a question.

### Questions
See **Weaknesses**

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the significant challenge of deploying deep neural networks in open environments where models may encounter both **covariate shifts**—changes in the input distribution while the label space remains the same—and **semantic shifts**, where inputs belong to new, unseen classes. Traditionally, methods have dealt with Out-of-Distribution (OOD) generalization (handling covariate shifts) and OOD detection (identifying semantic shifts) separately. However, in practical applications, a model needs to accept correctly classified inputs while rejecting both misclassified covariate-shifted examples and all semantic-shifted samples.

To solve this problem, the authors propose a framework that leverages **Low-Rank Adapters (LoRA)** to acquire and compress failure-specific reliability knowledge. By fine-tuning LoRA modules on specific tasks—such as handling covariate shifts using AugMix and semantic shifts using Outlier Exposure (OE)—the model can flexibly combine these modules during inference through simple arithmetic operations like addition and scaling. This approach allows for a controllable and efficient method to enhance unknown rejection capabilities under both types of distributional shifts.

**Problem Definition and Proposed Method:**

As summarized above, the paper addresses the challenge of unknown rejection in open environments, where a model must handle both covariate shifts, which are changes in the input distribution, and semantic shifts, involving new, unseen classes. During the training phase, the model learns from in-distribution data composed of pairs of inputs and their corresponding labels. This data is sampled from a specific distribution over a defined input and label space, including multiple classes. The classifier operates by selecting the class with the highest confidence score produced by the model for a given input, effectively determining the input's class based on the model's assessment of each possible class.

In deployment, the model encounters data from covariate shifts $ P_{\text{covariate}}^{\text{out}} $ (with shifted input distribution but same labels) and semantic shifts $ P_{\text{semantic}}^{\text{out}} $ (inputs from unknown classes $ y \notin Y $). The goal is to accept correctly classified samples from both $ P_{\text{in}} $ and $ P_{\text{covariate}}^{\text{out}}$, and to reject misclassified samples and all samples from $ P_{\text{semantic}}^{\text{out}} $. To achieve this, the authors propose using Low-Rank Adapters (LoRA) to capture failure-specific knowledge. LoRA adds low-rank matrices $ A $ and $ B $ to the model's layers, modifying the forward pass to $ z = W x + B A x $, where $ W $ are the original weights (kept frozen) and $ r = \text{rank}(A) \ll \min(u, v) $. Separate LoRA modules are fine-tuned for covariate shifts (using AugMix) and semantic shifts (using Outlier Exposure with auxiliary data $ D_{\text{aux}} $). These modules are then combined using $ \tau = (1 - \alpha) \tau_{\text{cov}} + \alpha \tau_{\text{sem}} $, where $ \alpha \in [0, 1] $ controls the emphasis between handling covariate and semantic shifts. The updated model parameters are $ \theta = \theta_{\text{pre}} + \tau $.

**Conclusion:**

By integrating LoRA modules through simple arithmetic operations, the proposed framework efficiently combines failure-specific knowledge, offering flexibility and control over the model's behavior in open environments. This method enhances the reliability of deep neural networks by simultaneously addressing covariate and semantic shifts. Addressing potential dependencies on auxiliary data and exploring scalability can further strengthen the framework, making it highly applicable in practical scenarios where robustness to various distributional shifts is essential. Moreover, the adaptable nature of this approach opens up exciting possibilities for future expansions.

### Strengths
- **Practical Relevance:** The method effectively addresses the challenge of unknown rejection in environments where covariate and semantic shifts occur, which is common in real-world applications.

- **Efficient Knowledge Integration:** Using LoRA modules and arithmetic operations allows for efficient integration of failure-specific knowledge without retraining the entire model, saving computational resources.

- **Flexibility and Control:** The scaling parameter$ \alpha$ enables dynamic adjustment of the model's behavior, allowing practitioners to tailor the model according to specific operational needs or preferences.

- **Comprehensive Experimental Validation:** The authors conduct extensive experiments on datasets like CIFAR-10, CIFAR-100, and ImageNet, using architectures such as ResNet and Vision Transformers. The results demonstrate that the proposed method outperforms several baselines in enhancing unknown rejection capabilities.

- **Theoretical Support:** The theoretical analysis provides insight into how the method can achieve desirable trade-offs in multi-objective optimization, reinforcing the practical findings.

### Weaknesses
 - **Dependence on Auxiliary Data:** Reliance on Outlier Exposure means that the method requires access to auxiliary outlier data, which may not always be readily available or vary in quality, potentially affecting performance. This dependency is a significant limitation, as the performance of the method is directly tied to the representativeness and quality of the auxiliary dataset. The method's effectiveness could be severely compromised if the auxiliary data does not adequately cover the range of potential semantic shifts encountered in real-world scenarios. Furthermore, the process of acquiring and curating such auxiliary data can be resource-intensive and time-consuming, adding to the practical challenges of deploying this method.

**Minor comments**
L239: For semantic *shifts*

### Questions
1. **Evaluation of Dependence on Auxiliary Data**

   - How dependent is the proposed method on the quality and availability of auxiliary outlier data used in Outlier Exposure (OE)? Can the model maintain high performance without this auxiliary data, and what alternative strategies could mitigate this dependency?

2. **Understanding Gradient Interference in Multi-Task Learning**

    - How does gradient interference in traditional multi-task learning impact the simultaneous optimization of covariate shift adaptation and semantic shift detection tasks? Could a theoretical and empirical analysis demonstrate how the proposed LoRA-based approach mitigates gradient conflicts compared to standard MTL methods?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This study proposes a learning approach that integrates OOD generalization and OOD detection to enable more reliable deployment of deep neural networks in real-world applications. To effectively distinguish correctly classified samples from incorrectly classified covariate-shifted and semantically shifted samples, the authors introduce a strategy that merges LoRA weights trained on each failure case. The proposed method demonstrates superior unknown rejection performance, validated on CIFAR-10/100 and ImageNet-200/500 benchmarks.

### Strengths
- This study addresses the unknown rejection task, a desirable property required in real-world applications where inputs come from various sources at test time, and proposes an effective solution. This approach offers a useful methodology for practitioners.
- The use of LoRA for unknown rejection is interesting. LoRA is parameter-efficient and portable, allowing flexible adaptation to deployment situations. Additionally, the merging of LoRA weights with different objectives demonstrates the effective handling of multi-objective scenarios.
- Through extensive experiments, the study provides insights into the unknown rejection task. For example, the impact of covariate shifts on MisD and OOD detection (Fig. 2) and the trade-off between rejecting misclassified covariate-shifted samples versus semantic-shifted samples (Fig. 4) highlight the challenges of the unknown rejection task and offer important motivation for future research.

### Weaknesses
 - The primary concern with this study is the insufficient review of prior research on unknown rejection. Even though previous works may not have integrated OOD generalization and OOD detection as stated in the motivation of this study, there are several existing studies focused on developing robust models from an unknown rejection perspective. To rigorously assess the advantages of the proposed method, discussions and comparative experiments with prior works on unknown rejection or failure detection are necessary:
  - Zhu et al. “RCL: Reliable continual learning for unified failure detection”, CVPR 2024
  - Cen et al. “The devil is in the wrongly-classified samples: Towards unified open-set recognition”, ICLR 2023
  - Zhu et al. “OpenMix: Exploring outlier samples for misclassification detection”, CVPR 2023
  - Li et al. “SURE: Survey recipes for building reliable and robust deep networks”, CVPR 2024
- The failure rejection setting in this study does not align with requirements for real-world environments. In this paper, the main experiments in Tables 1 and 2 aim to distinguish between “correctly classified covariate-shifted” and “misclassified covariate-shifted + semantic shift” cases. However, in a real inference environment, ID, covariate-shifted, and semantic-shifted samples may all be input to the model. For the model to be reliable in such settings, it should effectively distinguish between “correctly classified ID + correctly classified covariate-shifted” and “misclassified ID + misclassified covariate-shifted + semantic shift” samples. Although the performance on clean ID data is discussed on page 8, including ID test data in the main experimental setup would better align the study with realistic scenarios.


### Questions
- In Fig. 1, it is necessary to specify what each red cross and green check mark represents.
- On page 5, it is mentioned that only the B matrix of LoRA is trained, but since LoRA itself does not have many parameters, it is unclear why efficiency is so crucial. Are there other advantages besides efficiency? Does training both A and B affect performance?
- In the CIFAR-10/100 experiments, it is not specified which data was used as $D_{aux}$.
- Proposition 3.1 suggests that TrustLoRA can approximate a family of mappings $f_n$, but can this be guaranteed solely through the linear combination of LoRA weights?
- Typos
  - A closing bracket is missing in Proposition 3.1.
  - Line 318: “generally keep equal numbers of misclassified semantic-shifted data” → should be “generally keep equal numbers of misclassified covariate-shifted data.”
  - Line 485: The reference “Narasimhan et al.” is missing the publication year.
  - Line 491: “Fig. 8” should be “Fig. 7.”

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work introduces a novel reliability arithmetic framework using low-rank adaptation to separate and compress reliability knowledge, enabling unified and controllable rejection of unknowns under both covariate and semantic shifts, with experimental results showing its superiority over existing methods.

### Strengths
The presentation is fluent and the experimental results are sufficient.

### Weaknesses
1. From my perspective, the novelty of this paper seems somewhat limited, and the approach doesn't feel particularly compelling. For example, Equations (4) and (5) are essentially a combination of existing methods with LoRA, and this integration seems rather straightforward without much innovation. The core idea of applying LoRA to existing OOD generalization and detection techniques, while practically useful, does not present a significant methodological advancement. The method essentially fine-tunes LoRA weights using AugMix and Outlier Exposure (OE) objectives, which are well-established techniques, and then combines these weights. The process lacks a novel theoretical underpinning or a significant algorithmic contribution beyond this combination.

2. Additionally, some parts of the paper might be a bit overly complicated in their presentation, though this is not a major issue. However, it could make the paper more challenging to understand for readers like myself. For instance, in the paragraph around line 180, the authors introduce the concept of “knowledge,” where they first acquire and then compress knowledge. However, there’s no clear formal definition of what this “knowledge” actually represents. In reality, it refers to the LoRA weights, and the so-called “compressed knowledge” is simply a linear combination of different LoRA weight increments. I feel that using the term “knowledge” here might make the understanding of the paper more difficult for readers.

3. The paper aims to address Unrecoverable, Inflexible, and Inefficient problems, but in my view, these issues are quite easily resolved by introducing LoRA and are not directly tied to the proposed concepts of knowledge acquisition and compression. This, in turn, limits the paper’s contribution in terms of innovation. The use of LoRA, while providing parameter efficiency, does not inherently solve the core issues of unrecoverability or inflexibility in a way that is directly attributable to the method's novelty. The benefits seem to stem from LoRA's properties rather than the specific 'knowledge' framework.

4. I’m having some difficulty understanding how the proposed method demonstrates superiority over others. Equations (4) and (5) are fairly common techniques, and the subsequent knowledge compression doesn't appear to significantly boost model performance. It seems to me that the main improvements might actually stem from the use of AugMix and auxiliary datasets rather than the method itself. For example, in most experiments, AugMix performs as the second-best method (only slightly behind the proposed one), while many other methods perform worse than this baseline. Therefore, it’s possible that the performance gains claimed by the paper could be largely due to AugMix, which is a strong baseline. The marginal improvements over AugMix raise questions about the actual contribution of the proposed framework.

5. The paper devotes considerable space to discussing OOD generalization and detection, which, while important, doesn't seem to align closely with the core contribution of this work. I feel this aspect may not be directly related to the main method presented in the paper.

A few additional minor points:
1. There appears to be an issue with the citation or text on line 47: "Bai et al., (Bai et al., 2023)" may need to be corrected.
2. The numbering in the paper might be incorrect: (2) Recoverable should likely be (3) Recoverable.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
2
