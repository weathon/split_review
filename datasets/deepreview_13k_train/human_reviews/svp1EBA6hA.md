# Adding Conditional Control to Diffusion Models with Reinforcement Learning

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Diffusion models are powerful generative models that allow for precise control over the characteristics of the generated samples. While these diffusion models trained on large datasets have achieved success, there is often a need to introduce additional controls in downstream fine-tuning processes, treating these powerful models as pre-trained diffusion models. This work presents a novel method based on reinforcement learning (RL) to add additional controls, leveraging an offline dataset comprising inputs and corresponding labels. We formulate this task as an RL problem, with the classifier learned from the offline dataset and the KL divergence against pre-trained models serving as the reward functions. We introduce our method, \agl (\textbf{C}onditioning pre-\textbf{T}rained diffusion models with \textbf{R}einforcement \textbf{L}earning), which produces soft-optimal policies that maximize the abovementioned reward functions. We formally demonstrate that our method enables sampling from the conditional distribution conditioned on additional controls during inference.
Our RL-based approach offers several advantages over existing methods. Compared to commonly used classifier-free guidance,
our approach improves sample efficiency, and can greatly simplify offline dataset construction by exploiting conditional independence between the inputs and additional controls. Furthermore, unlike classifier guidance, we avoid the need to train classifiers from intermediate states to additional controls.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces an RL-based approach for integrating conditional control into pre-trained diffusion models. The primary contribution of the proposed algorithm is its RL objective, which is coupled with an analytical form of the KL divergence, allowing for seamless optimization using standard reinforcement learning algorithms. The authors benchmarked the proposed method against established controllable generation techniques, specifically classifier guidance and classifier-free guidance, and empirically demonstrated the effectiveness of the CTRL.

### Strengths
+ This paper is well-organized and the presentation is clear. 

+ Unlike classifier guidance and classifier-free guidance, CTRL approaches controllable generation from a distinct perspective by framing conditional generation as a reinforcement learning problem and fine-tuning the diffusion model over the reverse diffusion process. While a few prior works (e.g., [1]) have explored similar perspectives, this work is distinguished by its use of a KL-regularized RL framework, deriving the analytical form of KL regularization through Girsanov’s theorem. Additionally, I especially appreciate that the authors included a discussion in the main text on the relationship between CTRL, classifier guidance, and classifier-free guidance, providing valuable context for understanding the nuances of these methods.

[1] Kevin Black, Michael Janner, Yilun Du, Ilya Kostrikov, Sergey Levine. Training Diffusion Models with Reinforcement Learning.

### Weaknesses
 + Theoretically, an RL formulation allows us to view equation (5) as a sequential decision-making problem, enabling the learning of value functions for each diffusion time step $s$ and policy optimization based on these estimated values. However, in this paper (Algorithm 1), the authors instead use the diffusion model to roll out a diffusion path, preserving the gradient of each intermediate $x_t$ (assuming this interpretation is correct), computing the loss, and finally backpropagating the gradient across the entire diffusion path. This approach likely demands higher GPU memory, as it requires gradient preservation throughout the generation process, as well as increased computation, given the need to backpropagate gradients through the model multiple times. These requirements could limit the scalability and broader applicability of the proposed method.

+ Besides, in order to achieve controllable generation, classfier guidance and classifier-free guidance need to train either the classifier or a finetuned model, while CTRL needs to train both of them. This complicates the overall procedure.

+ While there are indeed numerous works that frame the reverse diffusion process as an MDP and use reinforcement learning to optimize the diffusion model, I am concerned that such optimization may lack sufficient constraints. To clarify, consider two consecutive time steps, $t$ and $t+1$ in the forward diffusion process, we have the following equation:
 $$p_{t+1}(x_{t+1})=\int p_t(x_t)\mathcal{N}(x_{t+1}; \sqrt{1-\beta_{t+1}}, \beta_{t+1}I)$$
Now, suppose we apply CTRL to fine-tune the reverse process. Since neural networks are used to approximate the score functions and are updated directly to maximize the objective without explicit constraints, it is likely that the above relationship will no longer hold after optimization. In other words, following reinforcement learning, the forward process might no longer correspond to the original stochastic differential equation (SDE). Could the authors provide insights into this concern? Specifically, will such a deviation impact the performance or generalization capability of the diffusion model?

### Questions
+ While there are indeed numerous works that frame the reverse diffusion process as an MDP and use reinforcement learning to optimize the diffusion model, I am concerned that such optimization may lack sufficient constraints. To clarify, consider two consecutive time steps, $t$ and $t+1$ in the forward diffusion process, we have the following equation:
 $$p_{t+1}(x_{t+1})=\int p_t(x_t)\mathcal{N}(x_{t+1}; \sqrt{1-\beta_{t+1}}, \beta_{t+1}I)$$
Now, suppose we apply CTRL to fine-tune the reverse process. Since neural networks are used to approximate the score functions and are updated directly to maximize the objective without explicit constraints, it is likely that the above relationship will no longer hold after optimization. In other words, following reinforcement learning, the forward process might no longer correspond to the original stochastic differential equation (SDE). Could the authors provide insights into this concern? Specifically, will such a deviation impact the performance or generalization capability of the diffusion model?

### Soundness
3

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
3

### Summary
This paper proposes a novel method, CTRL, to address adding conditional control to diffusion models. CTRL consists of three main stages: constructing the augmented model with a pre-trained model, training a classifier as a reward model, and solving a reinforcement learning problem to introduce conditional control in the diffusion model. Compared to classifier-free guidance, CTRL is adaptable to more flexible offline datasets, and compared to classifier-guidance methods, CTRL avoids accumulated inaccuracies caused by predicting $y$ from $x_t$ at each denoising step. This makes CTRL applicable in a broader range of scenarios with a more controllable generation process. Finally, experimental results validate the effectiveness of CTRL in terms of controllability and generation quality in tasks involving compressibility and multi-task generation.

### Strengths
1. The problem the authors attempt to address—adding conditional control to pre-trained diffusion models—is highly valuable. The author’s use of RL modeling for this problem is novel, and the derivation process is both reasonable and rigorous.
2. Compared to previous methods, CTRL has more flexible requirements for offline datasets and does not require training a predictor $x_t\rightarrow y$, resulting in a broader range of applications and a more controllable generation process.
3. In the experimental section, compared to classifier-free guidance and classifier guidance, CTRL demonstrates superior performance in controllability for image generation.

### Weaknesses
1. The evaluation metrics used in the paper are insufficient; for instance, the author only verifies the controllability of CTRL without providing results on the image quality generated by CTRL. Specifically, metrics such as FID or Inception Score, which are commonly used to assess the quality of generated images, are absent. This makes it difficult to ascertain whether the improved controllability comes at the cost of image fidelity. The lack of these standard metrics raises concerns about the practical applicability of the method, as a controllable but low-quality image generator is of limited use.
2. The experimental tasks are limited. The author only uses compressibility and aesthetic pleasingness as conditional controls. It is necessary to compare more complex conditions, such as sketch, normal map, as suggested in [1]. The current conditions are relatively simple and may not fully demonstrate the capabilities of the proposed method in more challenging scenarios. Furthermore, the paper lacks a clear explanation of how these conditions are encoded and incorporated into the model, which makes it difficult to assess the generalizability of the approach to other types of conditions.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces CTRL to enhance pre-trained diffusion models by integrating additional conditional controls through reinforcement learning. CTRL reformulates the conditional generation as an RL problem, where the reward function is derived from the conditional likelihood of labels given data, and the KL divergence from the pre-trained model acts as a regularizer. This method has key advantages over traditional guidance techniques, as it can use pairs of samples instead of triplets by leveraging conditional independence. CTRL is empirically validated on image generation tasks, demonstrating superior performance in single-task and multi-task settings, including cases requiring compositional controls, like generating images with specific compressibility and aesthetic properties.

### Strengths
1. The using of reinforcement learning to add conditional controls to diffusion models is novel. By reframing conditional generation as an RL problem, this approach leverages optimal policy learning to achieve conditional sampling without needing complex data dependencies. This use of RL significantly improves sample efficiency and offers a new, effective pathway for conditional generation, especially beneficial for complex, multi-condition tasks.
2. The comparison with prior work is comprehensive. The authors thoroughly contrast their RL-based CTRL method with traditional methods such as classifier guidance and classifier-free guidance, highlighting where CTRL overcomes limitations in sample efficiency, dataset requirements, and control precision. By detailing the theoretical and practical distinctions, such as the use of conditional independence to simplify dataset construction, the paper effectively demonstrates how CTRL builds upon and enhances past work, providing readers with a well-rounded understanding of its innovations.
3. Experimental results show that CTRL not only meets target conditions more accurately but also maintains high performance across diverse tasks with fewer data dependencies, underscoring its efficiency and robustness in practical applications.

### Weaknesses
1. While the core RL formulation and the connection to conditional diffusion are well-explained, the theoretical framework could be strengthened with a deeper exploration of the method's convergence properties and guarantees. Specifically, the paper lacks a rigorous analysis of how the learned policy converges to an optimal solution, given the non-convex nature of the reward function and the stochasticity inherent in the diffusion process. It would be beneficial to see a discussion on the conditions under which the RL training is guaranteed to converge, or at least a characterization of the convergence behavior in practice, such as the rate of convergence and the impact of different hyperparameters on convergence.
2. The experiments primarily compare CTRL with two standard methods: classifier guidance and classifier-free guidance. Including additional baseline methods, such as more recent variants of guided diffusion techniques or alternative conditional generation approaches, would provide a clearer picture of CTRL’s advantages and limitations. For example, comparing against methods that also leverage reinforcement learning or other optimization techniques for conditional generation would provide a more comprehensive evaluation of CTRL's performance. Furthermore, the paper could benefit from a more detailed analysis of the computational cost associated with CTRL compared to these baselines, especially given the iterative nature of RL training.

### Questions
In the error analysis section, the paper briefly discusses three sources of error. Could these three types of errors be more precisely quantified?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a conditional image generation method based on the diffusion model conditions with classifier guidance. Different from other methods of conditional generation of diffusion model in classifier guidance, this paper uses reinforcement learning to optimize conditional image generation of the diffusion model to maximize the log-likelihood probability of conditional generation as the reward function. It eliminates the need to train the classifier according to the intermediate diffusion frame and reduces the difficulty of training the classifier.

Note that as a researcher in reinforcement learning, I pay more attention to the problems related to RL in this paper. And I'm not familiar with image conditional generation.

### Strengths
1. This paper builds a good theoretical framework for RL-based conditional control to diffusion model.
2.  As far as I can see, the idea of using reinforcement learning to fine-tune the generation conditions of diffusion models is interesting.
3. The source code is attached in supplementary material, and I believe it is easy to reproduce.

### Weaknesses
1. The experimental part of the paper is very limited, only comparing the two methods in 2022. However, the field of conditional diffusion generation is changing rapidly, and this paper lacks a comparison with the latest methods. This paper does not perform an ablation analysis of the proposed method.
2. The author's specific methods of using RL are not very clear. Only the reward function is introduced, but how to formalize the problem into MDP, the state, the action, the transfer function, and so on are not introduced.

### Questions
1. Obviously, CTRL is a splitter-based method, but why is the experimental verification presented as the main comparison with the method without a classifier? Is this unfair? Please explain the considerations behind this.
2. Are there comparisons with more advanced conditional generation models?
3. The authors claim in Appendix G.2 that the proposed method can be adapted to any off-the-shelf RL algorithm, which I take with a grain of salt. There are many kinds of RL algorithms, and the two examples given by the author are both model-free on-policy methods. Did the author take into account offline RL algorithms, model-based RL algorithms, etc.? Is there a more detailed explanation, analysis, or experiment on this?
4. If possible, it is recommended to include a citation to the paper proposing the PPO method [1].

[1] Schulman J, Wolski F, Dhariwal P, et al. Proximal policy optimization algorithms[J]. arXiv preprint arXiv:1707.06347, 2017.

### Soundness
3

### Presentation
3

### Contribution
3
