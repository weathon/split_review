# Soft-TransFormers for Continual Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Inspired by \emph{Well-initialized Lottery Ticket Hypothesis (WLTH)}, which provides suboptimal fine-tuning solutions, we propose a novel fully fine-tuned continual learning (CL) method referred to as Soft-TransFormers (Soft-TF). Soft-TF sequentially learns and selects an optimal soft-network or subnetwork for each task. During sequential training in CL, Soft-TF jointly optimizes the weights of sparse layers to obtain task-adaptive soft (real-valued) networks or subnetworks (binary masks), while keeping the well-pre-trained layer parameters frozen. In inference, the identified task-adaptive network of Soft-TF masks the parameters of the pre-trained network, mapping to an optimal solution for each task and minimizing Catastrophic Forgetting (CF) - the soft-masking preserves the knowledge of the pre-trained network. Extensive experiments on Vision Transformer (ViT) and CLIP demonstrate the effectiveness of Soft-TF, achieving state-of-the-art performance across various CL scenarios, including Class-Incremental Learning (CIL) and Task-Incremental Learning (TIL), supported by convergence theory.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors attempt to solve the continual learning problem via a soft transformer idea, which adaptively selects subnetworks (specified by learnable masking for pre-trained parameters) and soft network tasked for detailed tasks in CL. During the sequential learning, the model will be trained to achieve a task-specific soft network based on the task-agnostic pre-trained model and sparsely activate some weights in the layers or deactivate someone. Besides, the authors support some theory proofs based on Well-initialized Lottery Ticket Hypothesis to analyze the rationale behind the improvements. Implemented on baselines, like DualPrompt, L2P, and L2p-PGP, they obtain competitive even SoTA performances.

### Strengths
1. The presentation sounds well.

2. The final experimental results present competitive even SoTA on some evaluated tasks.

3. Implementing the method on the Prompt Pool, which can divide the prompt pool into several groups and enable different group prompts to acquire different knowledge sounds reasonable while applying soft-network or binary masks on pre-trained weights can further boost the training.

### Weaknesses
1. Somehow, I believe such soft-network or subnetwork ideas have been widely studied among the communities, like model compression, model purification, or PEFT. One can think of employing the extra prompt vectors or using a learnable masking strategy, forcing the model to fit the downstream task while the pre-trained weights are fixed to hold the generalizability. Moreover, the prompt pool construction mechanism has been widely studied by DualPrompt, L2P.

2. I am curious about the training efficiency and inference latency since they utilize a large subnetwork or softnework compared with the baseline. 

3. Missing the tunable parameter comparisons with baselines and existing methods.

### Questions
Please refer to my above weaknesses.

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
3

### Summary
This work proposed sub-network over the prompt tuning technique for continuous learning. 
The overall presentation is clear but the motivation and the novelty is unclear.
Experimental results demonstrate superior performance to other methods.

### Strengths
The overall presentation is clear.
The experimental results demonstrate the effectiveness of the proposed method.

### Weaknesses
Firstly, the motivation is unclear.  In lines 84-85, the paper stated that " It cannot capture all the nuances of uncorrelated sequential tasks wildly if the task significantly differs from what the CL model was pre-trained initially on". It seems this work aims to address the reliance on a well pretraining, but the proposed method also require a well-initialized network as stated in lines 96-99. 
Besides, in lines 224-225, the task-specific prompts can be regarded as the explicit task-specific fine-tuning.

Secondly, the proposed method seems to be a combination of parameter-efficient fine-tuning method, e.g., prompt + LoRA, prompt + Adapter. How much performance improvement would be caused by adding LoRA or adapters for specific tasks in the baseline method。The superior performance seems contributed by more learnable parameters.

The experimental results requires more analysis. 
(i) Explain the ``Upper bound''. In fact, since the proposed method modifies the model architecture, the ``Upper bound''  cannot be the same as the other paper.
(ii) Why the proposed method achieves higher performance than the ``Upper bound''? 
(iii) Why the proposed method achieves higher performance when using DualPrompt as baseline while the improvement over the L2P seems smaller. 
(iv). In table 1, why the performance under the  20-Split-CIFAR100 is higher than  10-Split-CIFAR100? In general, the more incremental learning step, the weaker the performance due to forgetting. I suspect that the improved performance is due to learning more parameters. The number of parameters should be reported.

### Questions
Please refer to the weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents an approach that combines Prompt techniques with learnable soft masks to address catastrophic forgetting in continual learning.  Inspired by Well-initialized Lottery Ticket Hypothesis (WLTH), which provides suboptimal fine-tuning solutions, this paper proposes a fully fine-tuned continual learning (CL) method referred to as Soft-TransFormers (Soft-TF).

### Strengths
1. The paper includes extensive experiments across various datasets and tasks, providing comprehensive evidence for the method’s effectiveness.
2. The paper is well-written, with clear organization and logical flow that effectively communicates complex ideas.

### Weaknesses
### 1. Insufficient Technical Explanation

**1.1 Lack of Detailed Specification on Soft Mask \( m \) Initialization, Selection, and Optimization**
The paper suggests that the soft mask \( m \) is task-specific, adapting the subnetwork structure based on each task's needs. However, it lacks essential details on how these masks are initialized, selected, and optimized for each task. For instance, are there specific initialization strategies, criteria for mask selection, or task-transition strategies? The paper does not specify whether the masks are initialized randomly or based on some prior knowledge, nor does it explain the optimization process beyond a general reference to backpropagation. Furthermore, the method for selecting which mask to apply for a given task during inference is unclear. This lack of detail makes it challenging to understand the core contribution of the paper, especially as the optimization of these masks is crucial for retaining knowledge in continual learning.

**1.2 Potential Growth in Parameters Due to Task-Specific Masks**
As each task requires an independent soft mask \( m \), the storage cost may grow linearly with the number of tasks, not exponentially as originally stated. This is still concerning in scenarios with a large number of continual learning tasks, where storage costs could become prohibitive. The paper should discuss how to mitigate this issue, such as by employing techniques to compress or share mask parameters across tasks. The current approach appears to scale poorly with the number of tasks, which is a significant limitation for practical applications.

**1.3 Lack of Clarity on the Setting of \( \alpha_t \)**
The parameter \( \alpha_t \) is referenced but not clearly explained in terms of how it is set or updated for each task. The paper does not clarify if \( \alpha_t \) is a fixed hyperparameter or a learnable parameter. How does the method ensure that the sum of \( \alpha_t \) across tasks equals 1, and what role does this parameter play in mask composition? Detailed explanations and possible constraints for \( \alpha_t \) are necessary for comprehending how the method balances task adaptation and parameter sharing. The lack of clarity on this parameter makes it difficult to understand the overall mechanism of the proposed method.

**1.4 Redundant Calculation of \( t_x \) in Algorithm 2**
Algorithm 2 calculates \( t_x \) twice, raising the question of whether the indices for the E-Prompt and the learned subnetwork are identical. This redundancy lacks justification, and without clear reasoning, readers may question the necessity of these duplicate operations. A clarification is needed regarding the purpose of this repeated calculation and the roles of E-Prompt and learned subnetworks in relation to \( t_x \). It is unclear why the same task index needs to be computed twice, especially if the same index is used for both components.

**1.5 Increased Inference Cost Due to Subnetwork Selection**
According to Algorithm 2, selecting the learned subnetwork for a specific task requires backpropagation for subnetwork selection, which can significantly increase inference costs. This may limit the method's applicability in real-time or resource-constrained environments. The paper does not provide any analysis of the computational overhead associated with this subnetwork selection process, which is a critical aspect for practical deployment.

### 2. Unclear Core Mechanism

**2.1 Ambiguity in the Combination Mechanism of Soft Mask \( m \)**
The paper does not clarify why and how soft masks \( m \) can be combined based on different tasks. Ensuring each task's mask is unique and effectively isolated from other tasks is vital to avoid task interference and catastrophic forgetting. The paper lacks an explanation of how such task differentiation is achieved in practice. It is unclear how the masks are combined or whether they are simply selected based on the task ID. This is a crucial detail for understanding the validity of the proposed method's mechanism.

**2.2 Ensuring Task-Specific Mask Differentiation**
The authors do not provide details on how task-specific masks are designed to ensure they differ across tasks. If there is overlap or similarity between masks for different tasks, there is a high risk of interference, which could exacerbate forgetting. Further clarification on how each task’s mask maintains uniqueness would strengthen the proposed method. The paper needs to specify the mechanisms that prevent the masks from converging to similar configurations, which would undermine the task-specific learning.

### Questions
I recommend the authors address these concerns by providing detailed descriptions of the soft mask initialization, selection, and optimization processes, as well as methods for managing storage and computational costs with an increasing number of tasks. Clarifying the underlying mechanisms of mask composition and task differentiation would greatly enhance the transparency and reproducibility of the method.

### Soundness
3

### Presentation
3

### Contribution
2
