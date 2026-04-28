# VLP: Vision-Language Preference Learning for Embodied Manipulation

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Reward engineering is one of the key challenges in Reinforcement Learning (RL). Preference-based RL effectively addresses this issue by learning from human feedback. However, it is both time-consuming and expensive to collect human preference labels. In this paper, we propose a novel Vision-Language Preference learning framework, named VLP, which learns a vision-language preference model to provide preference feedback for embodied manipulation tasks. To achieve this, we define three types of language-conditioned preferences and construct a vision-language preference dataset, which contains versatile implicit preference orders without human annotations. The preference model learns to extract language-related features, and then serves as a preference annotator in various downstream tasks. The policy can be learned according to the annotated preferences via reward learning or direct policy optimization. Extensive empirical results on simulated embodied manipulation tasks demonstrate that our method provides accurate preferences and generalizes to unseen tasks and unseen language, outperforming the baselines by a large margin. The code and videos of our method are available on the website: https://VLPref.github.io.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work we propose a vision-language preference (VLP) learning that uses a vision-language model to provide preference feedback. It defines three types of language-conditioned preferences and contributes a vision-language preference dataset. The framework is evaluated on the Meta-World Benchmark.

### Strengths
1. This work proposes three forms of language-conditioned preferences: ITP, ILP and IVP. 

2. This work proposes a framework vision-language preference learning with theoretic analysis of its behavior.

3. Experiments are well organized to answer four key questions. 

4. Experiments show that the proposed VLP leads to better performance than other state-of-the-art baselines.

### Weaknesses
1. In the experiments, only a single benchmark, Meta-World, is used.
- This is limited to show the generality of the proposed preference learning framework.
- Related works in section 4 have tested on several different environments.

2. Only five tasks in the Meta-work are evaluated among 50 tasks.  
- This set of test tasks is not so challenging compared to 45 training tasks. 

3. Why are RL-VLM-F and CriticGPT not compared?  

4. The dataset construction itself may not be a notable contribution. 
- The trajectory sampling pipeline is rather simple, so its diversity may be unclear. 
- The dataset size is not big. 

5. Figures can be improved. 
- Fig. 2 is somewhat standard and conveys only limited value for the novelty. 
- In Fig.3, the attentions are not clearly seen.

### Questions
Please refer to Weaknesses.

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
4

### Summary
This paper proposes a novel video-based, vision-language-interleaved preference learning method for robotic control, named VLP. It defines three types of language-conditioned preferences: ITP, ILP, and IVP. The authors introduce a novel vision-language preference alignment framework that includes a learnable cross-modal transformer model to fuse video tokens and language tokens. They constructed a vision-language preference dataset with clear intra-task preference relations, MTVLP, containing 4.8K videos. Experimental results demonstrate the superiority of VLP compared to other RLHF methods with scripted labels or other vision-language rewards. Additionally, empirical evidence suggests that ILP and IVP, alongside the traditional ITP, contribute to improved performance, and that the 4.8K videos are both necessary and sufficient to achieve over 97% ITP accuracy.

### Strengths
* This paper presents strong empirical evidence and extensive experiments supporting the proposed approach. 
* The novel cross-modal architecture effectively fuses video and language through learnable parameters to compute preferences. 
* Furthermore, the introduction of language-conditioned preferences, namely Intra-Task Preference (ITP), Inter-Language Preference (ILP), and Inter-Video Preference (IVP), is a notable contribution that enhances the model's adaptability across different scenarios.

### Weaknesses
 * The theoretical claim seems to lack clear logical reasoning to justify the assertion that "the proposed preference model can be considered as parameterized negative regret that approximates the true negative regret of the whole segment". Although Eq. (10) and Eq. (11) have similar shapes, that does not mean that one approximates the other. The core issue is that the preference model, $f_\psi$, is trained on a dataset with pseudo-labels derived from optimality and video-language alignment, while the regret is defined with respect to the ground truth reward. The paper does not adequately address how optimizing $f_\psi$ with these pseudo-labels leads to a model that accurately approximates the true negative regret. The optimization objective for $f_\psi$ is based on a cross-entropy loss between the predicted preference and the pseudo-labels, which are not directly derived from the true reward function. Therefore, the claim that $f_\psi$ approximates the true negative regret requires more rigorous justification.
* I'm concerned that the simplicity of ILP and IVP definitions may limit VLP's generalizability. The preference labels defined in Table 1 overlook potential similarities between videos or language instructions across different tasks: They can assign a negative signal even if two videos from different tasks are similar (or in the case where the video and language from different tasks are semantically related) This approach may only work effectively within a carefully selected task distribution, potentially weakening the paper's claims of generalizability. The current definitions of ILP and IVP do not account for the possibility of shared subgoals or semantically related instructions across different tasks. For example, if two tasks involve manipulating a similar object, such as a drawer and a cabinet, the current preference labeling would not recognize the potential transfer of knowledge between these tasks. This could lead to the model learning overly specific task representations that do not generalize well to new scenarios with similar underlying structures.

### Questions
* Comparing this work with RoboCLIP (Sontakke et al., 2023) may provide valuable context. Baselines in this paper lack video input, so VLP’s advantage might come from its temporal reasoning. While VLP is compute-efficient, RoboCLIP is zero-shot. Demonstrating the cross-modal architecture’s distinct benefits would strengthen the claims.
* Regarding the second weakness: (1) How are video pairs in MTVLP constructed for ITP, ILP, and IVP regarding optimality levels? Are all combinations (e.g., expert, medium, random) considered? (2) Could you provide more examples of how medium-optimality is defined across the 50 tasks? Do any tasks share similar initial subtasks?
* Writing clarification suggestions: (1) It would be great if Table 1 is accompanied by v_i^j and l^k notations. (2) In several places, “language” is used to mean "language instructions," which might cause confusion. For instance, "unseen language" might imply a different spoken language rather than new instructions in English.

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
4

### Summary
This paper introduces VLP (Vision-Language Preference learning), a framework for learning general preference feedback for embodied manipulation tasks. The key contribution is a vision-language preference model that provides feedback by aligning video and language modalities. The paper presents extensive empirical evaluation, demonstrating strong performance and generalization capabilities to unseen tasks and language instructions.

### Strengths
1. The paper presents an effective framework that combines vision-language alignment with preference learning for robotic manipulation tasks. The experimental results show consistent improvements over VLM-based approaches across multiple tasks and demonstrate good generalization performance.
2. The paper is well-structured and easy to follow, presenting its ideas clearly.

### Weaknesses
1. The evaluation is limited to relatively simple Meta-World tasks, without testing on more complex task domains (e.g., MANISKILL2 [1] and MyoSuite [2]).
2. The paper lacks comparison with human preference labels, which would validate the quality of the generated preferences against human intent.
3. The theoretical analysis assumes access to all possible segments, weakening its practical implications.
4. (minor) The paper does not report the performance of scripted policies, which would help establish an upper bound for task performance and validate the quality of collected expert demonstrations.

### Questions
1. How does the computational cost of training VLP compare to other approaches like R3M or VIP?
2. How sensitive is the model to the quality and diversity of language instructions? Is there a significant performance drop when using instructions generated by a less capable model than GPT-4V?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces VLP, a vision-language preference learning framework, where the preference model is designed to generalize across unseen tasks. The preference model is based on an open-sourced CLIP model augmented with a trainable component. The model is trained using different types of preferences, categorized as ITP, ILP, and IVP. The experiments on the Meta-World benchmark support the paper's claims.

### Strengths
- The division of video-language preference types is novel and thoughtfully structured. ITP reflects traditional preferences, while IVP appears to enhance the model’s instruction-following capabilities. ILP seems to serve as a regularizer, adding robustness to the model. This categorization is well-conceived.
- The writing is clear, and the graphical illustrations effectively convey the content, enhancing overall readability.
- Both theoretical analysis and empirical findings support the framework.

### Weaknesses
 - A primary concern is the rationale behind the train-test task split in Meta-World. While the experimental results favor the proposed framework, it is unclear if the task split was specifically selected for favorable outcomes. Using Meta-World's ML45 benchmark, which provides a pre-defined split for comparability across works, could enhance the reproducibility and rigor of the results. Clarifying this point would strengthen the paper, and I would be inclined to raise my score if this concern is addressed, as the rest of the experimental design is robust.

 - The authors claim novelty in the architecture (line 071), yet it is not immediately clear what sets it apart, and this assertion seems somewhat overstated. Could the authors clarify the specific architectural innovations that distinguish this approach? Specifically, the use of cross-modal attention, while effective, is not a novel architectural contribution in itself. The claim of novelty needs to be more precisely defined, focusing on the specific way the architecture is adapted for this problem, rather than the use of a common attention mechanism.

### Questions
- The authors claim novelty in the architecture (line 071), yet it is not immediately clear what sets it apart, and this assertion seems somewhat overstated. Could the authors clarify the specific architectural innovations that distinguish this approach?

### Soundness
3

### Presentation
4

### Contribution
3
