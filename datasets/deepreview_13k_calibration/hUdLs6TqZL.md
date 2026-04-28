# Mining your own secrets: Diffusion Classifier Scores for Continual Personalization of Text-to-Image Diffusion Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Personalized text-to-image diffusion models have grown popular for their ability to efficiently acquire a new concept from user-defined text descriptions and a few images. However, in the real world, a user may wish to personalize a model on multiple concepts but one at a time, with no access to the data from previous concepts due to storage/privacy concerns. When faced with this continual learning (CL) setup, most personalization methods fail to find a balance between acquiring new concepts and retaining previous ones -- a challenge that \textit{continual personalization} (CP) aims to solve. 
Inspired by the successful CL methods that rely on class-specific information for regularization, we resort to the  inherent class-conditioned density estimates, also known as diffusion classifier (DC) scores, for CP of text-to-image diffusion models. 
Namely, we propose using DC scores for regularizing the parameter-space and function-space of text-to-image diffusion models, to achieve continual personalization.
Using several diverse evaluation setups, datasets, and  metrics, we show that our proposed regularization-based CP methods outperform the state-of-the-art C-LoRA, and other baselines. Finally, by operating in the replay-free CL setup and on low-rank adapters, our method incurs zero storage and parameter overhead, respectively, over the state-of-the-art.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel framework for continual personalization (CP) in text-to-image diffusion models using Elastic Weight Consolidation (EWC) and Diffusion Scores Consolidation (DSC). A key part of their approach is using DC scores for regularization, which leverages class-specific information from the diffusion model.

### Strengths
- The use of diffusion classifier for continual learning is novel and interesting.
- The limitation of the previous work is well addressed.
- Related work is well summarized.

### Weaknesses
 - Variance in approximation of expectation: During consolidation and updating FIM, the expectation over DC scores is approximated with a single trial per minibatch. While the authors aim to mitigate this by averaging across epochs, this can induce a biased Monte Carlo estimate. More rigorous analysis or empirical evidence is needed to demonstrate that this approximation does not compromise stability or lead to noisy FIM updates. Specifically, the paper does not address the potential for high variance in the diffusion classifier scores across different timesteps within a single batch, which could lead to unstable FIM updates. The authors should provide a more detailed analysis of the variance of the DC scores and how this variance affects the quality of the FIM approximation.
- Loss Component Interactions: The paper introduces multiple loss components, which can make hyperparameter tuning challenging. While the authors conducted an ablation study to evaluate the impact of individual losses, they did not address how these losses interact with each other. A more in-depth analysis of the interactions between different loss terms would strengthen the paper and provide clearer insights into optimizing the overall training process. For example, how does the weighting of the EWC loss term affect the convergence of the DSC loss, and vice versa? The paper needs to provide a more systematic way to understand the interplay between these loss terms.
- The link between classification and generative quality: For **Sanity Check II**, the paper lacks sufficient detail regarding the experimental setup. It does not clearly define what classifier is being used or how the classification is being performed (Is that diffusion classifier accuracy with a single trial?).
    - Additionally, I don’t think that improved classification alone does not necessarily imply that the quality of generated images will also improve. There needs to be a clear demonstration of the connection between accurate classification and enhanced image generation to support this claim. The paper should provide a more detailed analysis of how the diffusion classifier scores are related to the generation quality, rather than simply assuming that improved classification implies better generation. For instance, are the regions of the image that are well-classified also the regions that are generated with higher fidelity?
- Selection of $k$ (number of sampled tasks) for figure 16**:** I think choosing the number of sampled tasks  $k$  is crucial for achieving good results. However, the paper does not provide a clear strategy for determining the optimal  $k$ . While it shows that selecting five tasks works best in an experimental setting with six total tasks, it does not offer guidance on how to select $k$ when the total number of tasks $n$ changes. The paper needs to provide a more principled approach for selecting $k$, perhaps based on the similarity of the tasks or the diversity of the concepts being learned. A more detailed analysis of how the choice of $k$ impacts the final performance is needed.
Editorials: The notation for class labels is somewhat unclear throughout the manuscript. c is introduced as a text prompt in line 103, used as a class label in line 146, and used as a one-hot label in line 245. Since this notation is widely used throughout the manuscript, it is important to clarify its definition in the first place. Using superscript as an index is confusing, especially with exponentiation.
- Minor comments
    - Equation 5 needs to be fixed. Since L_denoise is an expectation over data, noise, concept, and time steps, the second term in r.h.s. of Eq (5) needs to be an expectation over data.
    - The title of the manuscript is somewhat misleading. What does secret mean in this context?

### Questions
- In explaining the limitation of C-LoRA, it is said that “L_forget decreases throughout training, thus losing most of the information learned for task1”. If I’m not mistaken, no forgetting happens when L_forget is close to zero since the modified parts of the parameters do not overlap with the previous LoRA parameters. Is there something I’m missing?
- Is there a difference between the results in Section 3.1 and the proposed method? Specifically, could you provide the results in Figure 1 for the proposed method? I’m curious if the changes in weight and loss differ from those observed in C-LoRA.
- In line 172, the authors mention learning a new word vector  $V_n$ , but neither the algorithm nor the figure includes this  $V_n$ , which is important for personalization. It only appears to be used during evaluation. This creates confusion about how  $V_n$  is obtained and when it is used in the training process.
- Including specific examples of pre-trained concept $c_0$$c$  and  $V_n$  would make it easier to understand.

### Soundness
3

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
This paper introduces a novel approach for continual personalization of text-to-image diffusion models using Diffusion Classifier (DC) scores. The method focuses on integrating DC scores as regularizers to mitigate the problem of forgetting in continual learning setups. By employing parameter-space and function-space regularization techniques, the authors aim to maintain previously acquired knowledge while integrating new concepts. The approach is evaluated against several baselines across multiple datasets and scenarios, demonstrating improved performance in retaining learned concepts with minimal parameter overhead.

### Strengths
1. The motivation of the paper is straightforward and clear.
2. The paper is technically sound, presenting a well-structured approach for continual personalization of text-to-image diffusion models using Diffusion Classifier (DC) scores.
3. The method seems computationally efficient, supported by sufficient experimental results and details.

### Weaknesses
 **Strengths:**

1. The motivation of the paper is straightforward and clear.
2. The paper is technically sound, presenting a well-structured approach for continual personalization of text-to-image diffusion models using Diffusion Classifier (DC) scores.
3. The method seems computationally efficient, supported by sufficient experimental results and details.

**Weaknesses:**

1. While the paper is technically proficient, the novelty of this paper seems limited. The primary innovation appears to be the use of diffusion scores as a regularization term for continual personalization, which, while interesting, is not a significant departure from existing methods. The core of the approach builds upon well-established techniques such as Elastic Weight Consolidation, adapting them for diffusion models rather than introducing fundamentally new methodologies.
2. Since Stable Diffusion versions 1.5, 2.0, 2.1, and XL have already been released, why not use the newer versions? At the very least, incorporating some of them would demonstrate that your method can be easily generalized across different architectures.
3. The paper would be more interesting if it could test on more recently proposed personalization methods like LyCORIS [1] and DoRA [2]. 
4. Since multiple-concept generation is common when verifying the effectiveness of proposed personalization methods according to your cited papers [3,4], could the authors further provide experimental results on multi-concept generation results?

### Questions
see above

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on the continual personalization of pretrained text-to-image diffusion models. It aims to address the challenge of balancing new concept learning and previous concept forgetting 
using a two level optimization strategy, i.e Deep Model Consolidation (DMC) and Elastic Weight Consoliation (EWC) . Buliding on DMC and EWC, the author introduce Diffusion Classifier (DC) as an additional constrait during consolidation.

### Strengths
1. The key innovation of this paper is the combination of DC scores with the EWC algorithm. This provides an interesting approach to applying EWC in T2I diffusion models.
2. The paper is well-written, with a clear and detailed explanation of the preliminary concepts in the related work section. The discussion on the limitations of C-LoRA naturally leads to introducing the EWC algorithm and the use of DC for likelihood estimation.

### Weaknesses
1. The optimization for the $n_{th}$ task combines a function-space objective with DSC (Eq. 6) and a parameter-space objective using EWC, but the paper lacks a detailed objective function that includes the FIM. This makes it difficult to understand how DSC and EWC work together during optimization. The paper presents Algorithms 1, 2, and 3, but it would greatly benefit from a summary algorithm that corresponds to Fig. 2, explicitly showing how these algorithms are integrated into the overall optimization process. This would clarify the interplay between the different components, especially how the gradients from the DC loss and the EWC penalty are combined to update the model parameters.
2. In Fig. 4 and Table 2, results show that EWC + DC and DSC + EWC + DC achieve comparable performance. Given that the DSC algorithm introduces complexity similar to that of EWC + DC, this raises questions about the necessity of DSC’s design. The marginal performance gains do not seem to justify the added complexity of the DSC component, especially considering the computational overhead it introduces. A more thorough analysis is needed to demonstrate the unique benefits of DSC beyond what EWC + DC can achieve, perhaps by showing scenarios where DSC provides a clear advantage, or by analyzing the specific types of forgetting that DSC mitigates more effectively.
3. A key limitation of this method is computational complexity. Each iteration of DSC and EWC + DC requires multiple complete diffusion forward and backward passes (Eq. 4 and Eq. 6). In contrast, C-LoRA’s explicit regularization is more efficient. It is recommended to further discuss the complexity of a single iteration and to provide a quantitative description of the complexity reductions achieved through pruning optimizations, such as selecting a subset of seen concepts (Fig. 16). The paper should also provide a more detailed comparison of the computational cost per iteration with C-LoRA, including wall-clock time, to better contextualize the trade-offs between performance and efficiency.

### Questions
In Algorithm 1, lines 5-6, the update of the DC scores dictionary is unclear. Line 6 shows that $P_\theta[c^i]$ is normalized for a subset with a coordinate of $k$, while line 5 indicates it is a probability distribution over $n + 1$ concepts.

### Soundness
3

### Presentation
3

### Contribution
3
