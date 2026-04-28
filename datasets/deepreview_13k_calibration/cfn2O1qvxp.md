# On-the-fly Preference Alignment via Principle-Guided Decoding

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
With the rapidly expanding landscape of large language models, aligning model generations with human values and preferences is becoming increasingly important. Popular alignment methods, such as Reinforcement Learning from Human Feedback, have shown significant success in guiding models with greater control. However, these methods require considerable computational resources, which is inefficient, and substantial collection of training data to accommodate the diverse and pluralistic nature of human preferences, which is impractical. These limitations significantly constrain the scope and efficacy of both task-specific and general preference alignment methods. In this work, we introduce On-the-fly Preference Alignment via Principle-Guided Decoding (OPAD) to directly align
model outputs with human preferences during inference, eliminating the need for fine-tuning. Our approach involves first curating a surrogate solution to an otherwise infeasible optimization problem and then designing a principle-guided reward function based on this surrogate. The final decoding policy is derived by maximizing this customized reward, which exploits the discrepancy between the
constrained policy and its unconstrained counterpart. OPAD directly modifies the model’s predictions during inference, ensuring principle adherence without incurring the computational overhead of retraining or fine-tuning. Experiments show that OPAD achieves competitive or superior performance in both general and personalized alignment tasks, demonstrating its efficiency and effectiveness compared to state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces On-the-fly Preference Alignment via Principle-Guided Decoding (OPAD), a novel approach for aligning large language model outputs with human preferences without requiring resource-intensive fine-tuning or retraining. Unlike RLHF, which rely on substantial data and computational resources, OPAD achieves preference alignment directly during inference. The method leverages a principle-guided reward function derived from a surrogate solution to an otherwise intractable optimization problem, allowing it to steer model predictions towards desired behaviors dynamically. OPAD demonstrates efficiency and effectiveness across general and personalized alignment tasks, often outperforming established baselines.

### Strengths
- OPAD offers a tuning-free alignment method inspired by the objectives of reinforcement learning, allowing it to align model outputs with human preferences without the need for additional tuning.
- The framework  can be applied to various tasks with minimal adjustments, making it a flexible solution for different alignment needs.
- Despite not requiring any model training, OPAD demonstrates competitive performance, often rivaling or surpassing traditional, training-intensive alignment methods.

### Weaknesses
 - In some cases, there is a high percentage of ties instead of clear wins or losses. How should we interpret this outcome?
- Since your method does not involve any model training, it would be valuable to demonstrate its performance on larger, more capable models to assess the trend and generalizability of your approach across different model scales.
- How does your method perform when LLMs do not achieve sufficient performance, such as smaller LLMs?

### Questions
- Would it be more appropriate to rename Section 5 from 'Discussion' to 'Conclusion' for clarity?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces On-the-fly Preference Alignment via Principle-Guided Decoding (OPAD), addressing the challenge of aligning language models with human preferences without requiring expensive fine-tuning or extensive data collection. The method works by designing a principle-guided reward function based on a surrogate optimization solution and directly modifying model predictions during inference to ensure adherence to target principles. Experimental results demonstrate that OPAD achieves competitive or superior performance compared to existing baselines across both general and personalized alignment tasks.

### Strengths
- The paper introduces a novel tuning-free alignment approach that uniquely leverages KL divergence between constrained and unconstrained policies during inference.
- The method demonstrates robust empirical validation through comprehensive experiments across multiple datasets and strong performance against RLHF, DPO, and other baseline methods.

### Weaknesses
 - The derivation of the surrogate optimization solution relies on an overly strong condition, namely 'The constraint c aligns well with the data distribution $P_{\text{data}}$'. In lines 214-215, there is a statement saying 'Direct optimization is infeasible since we have no access to $P_{\text{data}}$'. However, the authors did not explain how to design principles without access to $P_{\text{data}}$, and how to verify and guarantee this condition holds.
In fact, even if the constraint $c$ partially aligns with $P_{\text{data}}$, it could still lead to bad alignment. For example, let $P_{\text{data}}$ be 'professional medical advice', $P$ generate health-related statements with broad coverage but low accuracy, and $c$ be 'use formal medical terminology'. Maximizing $\text{KL}(P_c||P)$ might lead to technically-worded but meaningless or incorrect medical statements.
Therefore, the alignment quality of the principle is crucial. However, designing well-aligned principles without access to $P_{\text{data}}$ seems almost impossible; at least a surrogate $P_{\text{data}}$ is needed for guidance and principle evaluation. I believe the authors' experiments actually had access to $P_{\text{data}}$ (i.e., we clearly know we're dealing with the harmless and helpful aspects of hh-rlhf), so the designed principles could be well-aligned. But this contradicts the assumption of having no access to $P_{\text{data}}$.

- The proposed method lacks computational efficiency, running twice as slow as standard model decoding. While the tuning-free approach eliminates training costs, these costs are typically one-time investments, whereas inference requires continuous computational overhead. This computational burden limits the method's practical applications. Additionally, I recommend including computational efficiency comparisons with other in-context alignment methods to demonstrate whether OPAD offers advantages over similar approaches

-  For a paper focusing on decoding-time alignment, the Methodology section lacks both a complete description of the decoding steps and clear connections to the method overview presented in Figure 2, which reduces the paper's clarity. I recommend relocating the 'Relation with the residual EBMs' section to the later analysis and discussion portion, as it isn't a direct methodology description, and enhancing the method section with either a complete description of the decoding process or pseudocode to improve clarity.

### Questions
- Why do more steps hurt performance? Theoretically, global rewards are necessary because the text that aligns locally can violate principles globally. For example, for a medical advice principle, 'Take aspirin for headaches. Then take ibuprofen for fever.' While each 2-token window appears medically sound, this advice globally violates medical safety.

### Soundness
3

### Presentation
2

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
This work introduces a decoding method called OPAD that aligns model outputs with human preferences during inference. OPAD modifies model predictions to ensure compliance with human preferences. Compared to algorithms like DPO/PPO, OPAD achieves better performance without requiring additional training computational costs, which is very exciting.

### Strengths
The authors introduce an alternative objective that maximizes the KL divergence between constrained and unconstrained policies during decoding. This approach quantifies the model's adherence to target preferences, thereby determining the reward in the alignment process. This method adjusts token prediction probabilities to promote preference compliance.

The major advantage of this paper is that OPAD outperforms DPO/PPO algorithms and Best-of-N methods with significantly fewer computational resources and requires no additional training.

### Weaknesses
Recent research has focused on alignment during the decoding phase, such as [1][2][3][4], and the authors should discuss these works.

Some content lacks clarity, such as what constitutes a Principle in Alignment?  Additionally, to my knowledge, for models like Llama-3.1, if Principles are set in the system prompt, they can follow the described text. Therefore, experimenting with newer SOTA open-source models would help strengthen the paper's robustness.

The paper lacks theoretical explanation for why the proposed method is superior to placing Principles in ICL (In-Context Learning).

### Questions
How are Principles set in Summarization and HH-RLHF?

### Soundness
2

### Presentation
2

### Contribution
3
