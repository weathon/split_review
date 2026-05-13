# Aux-NAS: Exploiting Auxiliary Labels with Negligibly Extra Inference Cost

- Decision: Accept
- Scores: 6, 8, 6, 8, 8

## Abstract
We aim at exploiting additional auxiliary labels from an independent (auxiliary) task to \emph{boost the primary task performance} which we focus on, while preserving \emph{a single task inference cost} of the primary task. While most existing auxiliary learning methods are optimization-based relying on loss weights/gradients manipulation, our method is architecture-based with a flexible \emph{asymmetric structure} for the primary and auxiliary tasks, which produces different networks for training and inference. Specifically, starting from two single task networks/branches (each representing a task), we propose a novel method with evolving networks where only primary-to-auxiliary links exist as the cross-task connections after convergence. These connections can be removed during the primary task inference, resulting in a single-task inference cost. We achieve this by formulating a Neural Architecture Search (NAS) problem, where we initialize bi-directional connections in the search space and guide the NAS optimization converging to an architecture with only the single-side primary-to-auxiliary connections. % Such NAS design results in a discovered architecture with only  connections at the best locations while cutting off all the auxiliary-to-primary connections. Thus, all the auxiliary related computations/parameters can also be removed accordingly during the inference. \\
Moreover, our method can be incorporated with optimization-based auxiliary learning approaches. Extensive experiments with \emph{six} tasks on NYU v2, CityScapes, and Taskonomy datasets using VGG, ResNet, and ViT backbones validate the promising performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies how to harness additional auxiliary labels from an auxiliary task to elevate the performance of the main task without escalating the inference cost. To do so, the authors propose to employ individual networks for different tasks and only regularize the main task with the auxiliary task’s gradient. It’s understandable that this act allows the network trained on the auxiliary task to be completely pruned during inference. Furthermore, the authors propose to search for the most appropriate structure that satisfies the previously mentioned constraint with NAS. The paper accentuates its methodology's compatibility with prevailing optimization-based auxiliary learning techniques. The empirical validation, evident from experiments on NYU v2, CityScapes, and Taskonomy datasets using well-known backbones like VGG-16, ResNet-50, and ViT-B, demonstrates the efficacy of the proposed method.

### Strengths
++ The paper is well-written with clearly motivated arguments and insights. The auxiliary learning task is also meaningful when we only seek to boost one task with another and aim at quick inference. 

++ Table 1 provides a comprehensive understanding and meticulous survey of the field. The authors offer an exhaustive overview of both Multi-Task Learning (MTL) and Auxiliary Learning (AL) methods. Authors have incorporated a wide range of references from multiple years, indicating a holistic survey of both seminal works and recent advancements. The inclusion of their method alongside existing techniques also provides clarity on its positioning within the broader research landscape. 

++ The proposed method is backbone- and task-agnostic that is applicable to multiple backbones and tasks.

### Weaknesses
-- While the idea of using an auxiliary task's gradient to regularize the main task is interesting, I believe a more direct comparison with a specific baseline could strengthen the paper's claims. A potential baseline could involve sharing a single backbone between the main and auxiliary tasks. However, instead of directly combining the losses, the gradient of the auxiliary task could be projected onto the orthogonal direction of the main task's gradient. This projection could be applied to all or a selected subset of layers. This approach would maintain the advantage of no inference overhead while still leveraging the auxiliary objective signals. It would be valuable to see how the proposed method performs against such a baseline, especially in terms of performance gain versus computational cost during training.

-- The authors propose using NAS to find suitable architectures. However, the rationale behind "stitching" two distinct backbones, each trained with different weights and objectives, is not entirely clear. The paper would benefit from a more in-depth theoretical justification or empirical evidence supporting this design choice. It's not immediately obvious why this approach would be logically sound or advantageous. Are there any existing theories or studies that support the effectiveness of combining networks trained on different objectives in this manner? Without further clarification, this aspect of the methodology raises concerns about the coherence of the overall architecture.

-- The authors highlight the "promising performance" of their method. However, a closer examination of Tables 3 and 4 suggests that the performance gains might be marginal. Given the additional computational costs associated with the NAS search and optimization process, it's unclear whether the slight improvements justify the increased training complexity. The paper should provide a more thorough analysis of the trade-off between performance gains and training efficiency. Is the marginal improvement in accuracy worth the potential increase in training time and resource consumption?

### Questions
See weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an architecture based take on auxiliary learning. They recognize that the asymmetry between the auxiliary and primary tasks can be exploited by learning architectures with constraints that favor transfer of information from the auxiliary to the primary, but in an indirect way so as to minimize the possibility / effect of negative transfer.

### Strengths
1. The idea is novel and interesting.  I think the use of joint training, followed by the slow trimming of the aux-to-prim connections via L1 regularization is a clever way of more intimately introducing the auxiliary task  but remove it later to avoid needing it during inference.
2. The paper is clearly written and easy to follow
3. This has interesting implications for Auxiliary learning based architecture search -- since what was searched for in this paper were connections, there are expansions on this that can focus on other parts of the architecture space.

### Weaknesses
1. Method might be a bit too complex / cumbersome to be practically implemented widely -- especially given the size of the gains.
2. Method also significantly increases memory / compute overhead at training time
3. The experimental results have no error-bars. It's thus hard to judge the significance of the results



### Questions
1. Did you try further finetuning the final model on the primary task only after being done with the auxiliary-task based NAS ? This could result in extra performance boost

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new framework for auxiliary learning, in which the goal is to improve the performance on a task of interest (i.e., primary task) by utilizing auxiliary information. In particular, the proposed method aims to tackle auxiliary learning problems without introducing computational or parameter overhead during inference. To this end, the paper borrows inspiration from multi-task learning and neural architecture search to design an asymmetric network architectures, where the connections from primary-task network layers and auxiliary-task network-layers are directed (from primary to auxiliary), such that computations or parts of networks for auxiliary information can be removed during inference.

### Strengths
- The proposed method successfully tackles auxiliary learning without inducing extra computational overhead during inference, by utilizing NAS to design a network that has asymmetric connections directed from primary-task network parts to auxiliary-task network parts.

- The proposed method is flexible in that it can be combined with different auxiliary learning methods

- The paper is clearly written; easy to read and follow.

### Weaknesses
 - Is there a need to initialize search space to include all bi-directional connections? why not start from networks with only primary-to-auxiliary connections right away? It's unclear why the search space needs to include auxiliary-to-primary connections initially, given that these connections are ultimately pruned. This seems like an unnecessary expansion of the search space, potentially increasing computational cost during the search phase without a clear benefit.

- Lack of ablation studies related with the question above: the performance change as the search space only contains primary-to-auxiliary connections. The paper lacks a crucial ablation study to justify the choice of initializing with bi-directional connections. Specifically, it should compare the performance of the proposed method when the search space is restricted to only primary-to-auxiliary connections from the start. This would demonstrate whether the bi-directional search space is indeed necessary or if a simpler, unidirectional search space would suffice.

- Missing details: Are all auxiliary-to-primary connections are pruned at the end of training? It's not explicitly stated whether all auxiliary-to-primary connections are guaranteed to be pruned by the end of the training process. The paper should provide a more rigorous analysis of the final architecture and confirm that no auxiliary-to-primary connections remain.

- Missing details: What is the final architecture produced by NAS? How consistent is the final performance across different random seeds and trials? The paper lacks a detailed description of the final architecture produced by the neural architecture search (NAS). It should include statistics on the distribution of architecture weights, particularly for the primary-to-auxiliary connections, and demonstrate the consistency of the final performance across multiple trials with different random seeds. Without this, it's difficult to assess the robustness of the method.

### Questions
Written in the weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a learnable and flexible asymmetric network architecture designed for general-purpose auxiliary learning, where the auxiliary task plays a pivotal role in supporting the primary task's training process, and can be freely removed during the inference. As a result, the proposed method achieves a multi-task level performance while keeping a single-tasks level inference cost. The authors implement their design as adaptive layerwise feature fusion of multiple single-task branches, where the full network converges to an asymmetric architecture with only primary-to-auxiliary connections existed, enabling the removal of the auxiliary task during the inference. Two algorithms are developed to achieve this, where the more advanced one exploits a specifically designed NAS pruning to achieve an asymmetric architecture after convergence. The experiments are extensive across 6 tasks with 3 network backbone architectures, which sufficiently demonstrate the promising performance.

### Strengths
1.	This paper tackles the general-purpose auxiliary learning towards a multi-task level performance and a single-tasks level inference cost. The proposed method can be applied to various tasks and network backbones mathematically and also validated experimentally.
2.	The proposed method can also be freely combined with various multi-task or auxiliary task optimization methods listed in Table 1, which was also validated by the experiments.
3.	The single-task level inference cost is assured through the resultant converged asymmetric network architecture. Furthermore, the training cost exhibits a linear increase when incorporating additional auxiliary tasks, which is enabled by the supernet architecture for NAS that only encompasses the connections between the primary task and each of auxiliary tasks. 
4.	Table 1 present a very clear and comprehensive taxonomy about the position of the proposed method among the area of multi-task learning and the auxiliary task learning.
5.	The experiments are extensive, validating the generalization on 6 diverse tasks within 3 datasets, and 3 network backbones including both CNNs and Transformers.

### Weaknesses
This paper is well written, and I do not see major weakness, but the clarification of the following minor issues would further improve the paper: 
1.	I appreciate that the authors provide the full NAS objective in Eq. 10, but the details about how it is optimized need to be further elaborated. If I understand correctly, the model weight w and the architecture weight alpha should be updated iteratively? The precise optimization algorithm, including the learning rate schedules, batch size, and the number of iterations for each update, are not clearly specified. Additionally, the convergence criteria for the architecture search are missing, making it difficult to reproduce the results. It would be beneficial to know if there is a specific strategy to prevent the architecture weights from collapsing to a trivial solution.
2.	I suggest indicating the network backbone in the legends of Tables 3 and 4, as there are several tables in a similar shape that only differ from backbones. This lack of clarity makes it cumbersome to quickly compare results across different architectures.
3.	It is suggested to replace the figures with vector images for a better resolution. The paper, in its current version, used a lot of v-spacing; it is also advised to remove them for better readability.

### Questions
The author claimed that they implement the tailored version of PCGrad and AdaShare specifically for the auxiliary task learning, i.e., PCGrad-Aux and AdaShare-Aux. What are the details of those auxiliary task learning variants?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to harness the auxiliary tasks to enhance the performance of the primary task, while maintaining a single task inference cost for the primary task. The authors achieve this by designing an asymmetric network and further develops two algorithms: the first algorithm directly uses the asymmetric primary-to-auxiliary architecture, where the auxiliary tasks can be directly removed during the inference; the second algorithm initiates with an architecture with bi-directional connections, and subsequently exploits a tailored L1 constrained NAS optimization to prune all the auxiliary-to-primary connections, thereby enabling to remove the auxiliary task during inference. The proposed soft-parameter sharing architecture-based method can be integrate with existing optimization-based methods. The author validates their method with extensive experiments on 6 tasks with 3 CNN and transformer architectures.

### Strengths
1. This paper formulates the auxiliary learning problem through a task-oriented adaptive feature fusion approach without the need of explicitly identifying the task similarity. Mathematically, such architecture-based method can be seamlessly integrated with a variety of multi-task/auxiliary optimization methods such as loss re-weighting and gradient manipulation. The paper is well written and easy to understand, with an extensive literature review in Table 1 clearly demonstrating the contribution of the proposed method.
2. The evolving and asymmetric network design, coupled with a tailored NAS algorithm, ensures the converged network comprises only the primary-to-auxiliary connections, thereby guaranteeing a single-task inference cost for the learned architecture.
3. Beyond the benefits in the single-task inference cost, the authors also show (in Sect. 4.2.4 and the supplementary) that the training complexity exhibits a linear scalability to multiple auxiliary tasks.
4. The experiments are extensively performed on 6 highly diverse tasks with 3 base net architectures including CNN and transformers. The authors also checked the performance when the primary and the auxiliary tasks possess different architectures in the supplementary. The results of all those experiments are promising.

### Weaknesses
1. Is it possible to use Normalization and Activation operations other than BatchNorm and ReLU in Eqs. 13 and 14? While the paper focuses on the flexibility of the fusion operation, it would be beneficial to explore the impact of different normalization and activation choices, as these can significantly affect the training dynamics and final performance. For example, Layer Normalization could be more suitable for certain architectures or tasks, and activation functions like GELU or Swish might offer advantages over ReLU. The current discussion lacks this exploration, making it difficult to assess the robustness of the method across different configurations.
2. In Fig. 3, should the cut-off dash line be between the 1x1 conv and the add operations? The current illustration of the cut-off dash line between the auxiliary input and the concatenation operation is somewhat misleading. While the effect is the same, the visualization could be more precise by showing the cut-off after the 1x1 convolution, as this is where the actual pruning occurs. This would improve clarity and prevent potential misinterpretations of the network structure during the NAS process.
3. I suggest the authors to move the supplementary material into the Appendix of the main text for better readability.

### Questions
Please respond to those in the Weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
