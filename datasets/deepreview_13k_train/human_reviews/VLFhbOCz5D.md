# Tangent Transformers for Composition,Privacy and Removal

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
We introduce Tangent Attention Fine-Tuning (\method{}), a method for fine-tuning linearized transformers obtained by computing a First-order Taylor Expansion around a pre-trained initialization. We show that the Jacobian-Vector Product resulting from linearization can be computed efficiently in a single forward pass, reducing training and inference cost to the same order of magnitude as its original non-linear counterpart, while using the same number of parameters. Furthermore, we show that, when applied to various downstream visual classification tasks, the resulting Tangent Transformer fine-tuned with \method{} can perform comparably with fine-tuning the original non-linear network. Since Tangent Transformers are linear with respect to the new set of weights, and the resulting fine-tuning loss is convex, we show that \method{} enjoys several advantages compared to non-linear fine-tuning when it comes to model composition, parallel training, machine unlearning, and differential privacy

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces Tangent Attention Fine-Tuning (TAFT), a method for fine-tuning linearized transformers that are derived by computing a First-order Taylor Expansion around a pre-trained initialization. The key contributions of the paper are as follows:

Efficient Jacobian-Vector Product Calculation: The authors demonstrate that the Jacobian-Vector Product resulting from linearization can be efficiently computed in a single forward pass. This reduces the training and inference costs of linearized transformers to a similar order of magnitude as the original non-linear models, all while maintaining the same number of parameters.

TAFT presents an efficient and effective method for fine-tuning linearized transformers obtained through Taylor Expansion. It maintains performance parity with non-linear models while providing advantages related to model composition, training efficiency, unlearning, and privacy. This has significant implications for the practical use of transformers in various downstream tasks.

### Strengths
1. Efficient Jacobian-Vector Product Calculation: The authors demonstrate that the Jacobian-Vector Product resulting from linearization can be efficiently computed in a single forward pass. This reduces the training and inference costs of linearized transformers to a similar order of magnitude as the original non-linear models, all while maintaining the same number of parameters.

2. Comparable Performance: When applied to various downstream visual classification tasks, the Tangent Transformer fine-tuned with TAFT performs on par with fine-tuning the original non-linear network. This suggests that the linearized version is a viable alternative without compromising performance.

3. Convex Fine-Tuning Loss: The paper highlights that Tangent Transformers are linear concerning a new set of weights, resulting in a convex fine-tuning loss. This convexity offers several advantages over non-linear fine-tuning, particularly in terms of model composition, parallel training, machine unlearning, and differential privacy.

### Weaknesses
1. In Section 3.4, the author mentions basically the same things as in Section 2 Related work-Pravicy with no new theoretical analysis about differential privacy.

2. The interpretability of the proposed method is not thoroughly explored. While the authors mention the interpretability advantages of linear models, they do not provide a concrete analysis of how individual training samples influence the learned model and the predicted results, especially in the context of the proposed Tangent Attention Fine-Tuning (TAFT). The connection to methods like LQF, which provide detailed sample influence analysis, is not adequately addressed.

3. The paper highlights the advantages of linear models but does not sufficiently explore the specific implications of linearizing a transformer model versus a ResNet. While the authors mention that the inductive prior learned by transformers is better, they do not provide a detailed analysis of the specific advantages and disadvantages of linearizing a transformer model compared to linearizing a ResNet, particularly regarding the impact on feature biases and transferability across different layers.

### Questions
1. How about interpretability? A detailed analysis of how a given training sample affects the learned model and the predicted results is given in LQF. Is it possible for the authors to provide an analysis of the interpretability?
2. The authors detail the advantages of linear models in the introduction, but these advantages don't seem to be relevant to transformer, what are the advantages and disadvantages of linearizing the transformer model compared to linearizing ResNet?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce Tangent Attention Fine-Tuning (TAFT) for fine-tuning linearized transformers. It can perform comparably with fine-tuning the original non-linear network in various downstream visual classification tasks. It enjoys several advantages compared to non-linear fine-tuning when it comes to model composition, parallel training, machine unlearning, and differential privacy.

### Strengths
The paper is the first work to propose an efficient method to linearize models in the Transformer family of architectures, which is meaningful. The paper is clearly written with many experiments.

### Weaknesses
1.since this is a fine-tuning method, please provide more fine-tuning methods for comparison (lora,adapter...) in table 3. 
2.I wonder how TAFT works when applied to LLM? maybe some experiments can be added.
3.please derive in detail how to get the closed form expression in equation 5 and 6.

### Questions
see weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed a method for fine-tuning linearized transformers, called Tangent Attention Fine-Tuning (TAFT). 

The paper claims that TAFT can achieve comparable performance to non-linear fine-tuning on various downstream tasks while enjoying the benefits of linearity such as compositionality, parallel training, machine unlearning, and differential privacy. 

The paper also introduces Tangent Transformers, which are linearized versions of pre-trained transformer models, and shows how to compute their Jacobian-Vector products efficiently in a single forward pass. 

The paper demonstrates the advantages of TAFT and Tangent Transformers in several experiments using vision transformer models. 

To summarize, the paper's main contributions are:

- A novel method for fine-tuning linearized transformers that is computationally efficient and competitive with non-linear fine-tuning.

- A theoretical analysis of the benefits of linearity for model composition, parallel training, machine unlearning, and differential privacy.

- An empirical evaluation of TAFT and Tangent Transformers on various downstream visual classification tasks using vision transformer models.

### Strengths
The paper proposes a novel method for fine-tuning linearized transformers, called Tangent Attention Fine-Tuning (TAFT), which is computationally efficient and competitive with non-linear fine-tuning. The paper also introduces Tangent Transformers, which are linearized versions of pre-trained transformer models, and shows how to compute their Jacobian-Vector products efficiently in a single forward pass. The paper demonstrates the advantages of TAFT and Tangent Transformers on several experiments using vision transformer models.

In terms of originality, the paper introduces a new method for fine-tuning linearized transformers that is computationally efficient and competitive with non-linear fine-tuning. The paper also introduces Tangent Transformers, which are linearized versions of pre-trained transformer models, and shows how to compute their Jacobian-Vector products efficiently in a single forward pass. These contributions are novel and have not been explored before.

In terms of quality, the paper provides a theoretical analysis of the benefits of linearity for model composition, parallel training, machine unlearning, and differential privacy. The paper also provides an empirical evaluation of TAFT and Tangent Transformers on various downstream visual classification tasks using vision transformer models. The experiments are well-designed and the results are presented clearly.

In terms of clarity, the paper is well-written and easy to follow. The authors provide clear explanations of their methods and results. The paper also includes visualizations that help to illustrate the concepts presented.

In terms of significance, the paper’s contributions have important implications for the field of machine learning. The proposed method for fine-tuning linearized transformers is computationally efficient and competitive with non-linear fine-tuning. This has important implications for large-scale applications where computational efficiency is critical. Additionally, the theoretical analysis of the benefits of linearity has important implications for model composition, parallel training, machine unlearning, and differential privacy.

Overall, this is a well-written paper that makes significant contributions to the field of machine learning.

### Weaknesses
 (1) While the paper is well-written and easy to follow, it would be helpful to provide more detailed explanations of some of the concepts presented. For example, the paper could provide more details on how Tangent Transformers are computed and how they are used in practice (especially from Eq 5 to Eq 6). Specifically, the jump from the general Jacobian-vector product to the specific linearized attention calculation in Eq 6 is not sufficiently clear. The paper should elaborate on the specific matrix operations and approximations used to arrive at this efficient computation, including the handling of the softmax function's derivative within the attention mechanism.

(2) While the paper provides an empirical evaluation of TAFT and Tangent Transformers on various downstream visual classification tasks using vision transformer models, it would be helpful to see more experiments that compare TAFT with other fine-tuning methods on these tasks. The current comparison only against non-linear fine-tuning is insufficient to establish the practical competitiveness of TAFT. A more comprehensive comparison should include parameter-efficient fine-tuning techniques such as adapters and low-rank methods, which are commonly used and provide a more relevant baseline for comparison. This would help to establish the relative trade-offs between performance and computational efficiency.

(3) While the paper provides a theoretical analysis of the benefits of linearity for model composition, parallel training, machine unlearning, and differential privacy, it would be beneficial to provide more empirical evidence to support these claims. Specifically, it would be helpful to see more experiments that demonstrate the advantages of TAFT and Tangent Transformers on a wider range of tasks and datasets. The current experiments are limited to object-centric image classification tasks. Evaluating on datasets with different characteristics, such as texture-based classification (e.g., DTD) and action recognition (e.g., UCF101), would provide a more robust assessment of the generalizability of the proposed method.

### Questions
(1) Please give a detailed derivation process from Eq 5 to Eq 6 in the appendix.

(2) The selected datasets (Caltech-256 (Griffin et al., 2007), MIT-67 (Quattoni & Torralba, 2009), Oxford Pets (Parkhi et al.,
2012), Stanford Dogs (Khosla et al., 2011), CUB-200 (Wah et al., 2011), FGVC-Aircrafts (Maji
et al., 2013), and Stanford Cars (Krause et al., 2013)) are object-oriented. What about the performance of the proposed method on Describable Textures (DTD) (Cimpoi et al., 2014)？ 

(3) (Optional to reply) Could the proposed method be applied to temporal classification tasks, such as activity classification on UCF101?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
