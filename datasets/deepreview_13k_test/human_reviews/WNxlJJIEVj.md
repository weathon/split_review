# Contrastive Diffuser: Planning Towards High Return States via Contrastive Learning

- Decision: Reject
- Scores: 1, 3, 3, 5

## Abstract
The performance of offline reinforcement learning (RL) is sensitive to the proportion of high-return trajectories in the offline dataset. However, in many simulation environments and real-world scenarios, there are large ratios of low-return trajectories rather than high-return trajectories, which makes learning an efficient policy challenging. In this paper, we propose a method called Contrastive Diffuser (CDiffuser) to make full use of low-return trajectories and improve the performance of offline RL algorithms. Specifically, CDiffuser groups the states of trajectories in the offline dataset into high-return states and low-return states and treats them as positive and negative samples correspondingly. Then, it designs a contrastive mechanism to pull the trajectory of an agent toward high-return states and push them away from low-return states. Through the contrast mechanism, trajectories with low returns can serve as negative examples for policy learning, guiding the agent to avoid areas associated with low returns and achieve better performance. Experiments on 14 commonly used D4RL benchmarks demonstrate the effectiveness of our proposed method. Our code is publicly available at \url{https://anonymous.4open.science/r/CDiffuser}.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper combines a trajectory planning method based on a diffusion model and contrastive learning to select states with higher returns. States are grouped into fuzzy sets of low and high reward and then used to constrain the trajectory planning by pulling states towards regions of higher return. An extensive ablation study, comparison with state of the art and hyperparameter search shows good results and the importance of all components.

### Strengths
The method is suprisingly simple yet effective. It can be probably easily adopted for a wide range planning problems or even tasks without explicit trajectories beyond the typical RL tasks in table 1.

### Weaknesses
It is hard to find weaknesses in this paper. Sometimes the sentences are a bit long and convey a lot of concepts at the same time which is not necessarily bad but harder to understand. One example is the sentence around equation 13. The impact of predictions in the future of planning could be elaborated a bit more, but this is just an example to illustrate my point.

While being best and second best in the med-replay datasets, it could be argued if being so close to the other results can be called significant improvements and highlighting the second best is potentially done to have the results in the best possible light. However, the authors put their results in ample perspective and give reasonable hypothesis about the impact of expert examples.

### Questions
- More a suggestion, Figure captions like Figure 2 could provide more information. The general function of both modules as take away message for the reader could improve the figure understanding even though it appears in the text pointing to this figure

- In figure 5 I find it hard to see what is supposed to be in and out of distribution. Maybe some circles could help making the points from section 4.4. All three figures also look very alike. I get the idea of comparison here but not sure about the overall value of this. The nuanced color changes are also hard to see and some people are color blind.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a diffusion-based trajectory generation based on contrasting high-return and low-return training samples, called CDiffuser. The core approach in the method is performing a contrastive learning between generated trajectory and samples in the dataset. The contrastive learning serves as a guidence to the diffusion process, and pushes the generated trajectories towards high return states and away from low return states. Experimental results on Gym show the improvements of the proposed algorithm.

### Strengths
- The idea of combining contrastive learning with trajectory generation is somehow novel.

- The analysis on the similary of generated states are informative.

- The ablation study on different loss terms are appreciated. The study on using high-reward samples only is great.

### Weaknesses
1. The performance improvement may not be significant. According to Table, 1 the performance is highly comparable to DD. 

2. The benchmark only uses Gym.

3. The method is using one step generation from EDP. However, Table 1 and ablation study do not include the comparison against this method. 

4. The method highly relies on EDP to make the contrastive loss differentiable through the generated states, from my understanding. However, this could be hard to generalize to other diffusion-based methods. 

5. The guidence on return is confusing. The return is predicted from the very **first state** of the **noisy trajectory**, according to the third line after Equation (6). How can the prediction and the learned model be accurate, when solely from a noisy state?  And clarifications on its backpropogation is needed, since it only takes the noisy trajectory input, and the denoising process only takes one step.

6. The original diffuser seperately trains the auxiliary return prediciton model on all data. This modification is not discussed and experimentally validated.

7. Can the authors explain the reasons of intriguing properties presented in 4.4?

8. The contrastive loss Equation (9) seems to not be a common form. Usually the denominator considers all the samples, for example in [2,3]. This is a concern on the correctness of this implementation and a justification is needed.

Based on the points above, I am not convinced the proposed method is sound and could actually work in terms of training.

[1] Bingyi Kang, Xiao Ma, Chao Du, Tianyu Pang, and Shuicheng Yan. Efficient diffusion policies for offline reinforcement learning. arXiv preprint arXiv:2305.20081, 2023.

[2] Oord, Aaron van den, Yazhe Li, and Oriol Vinyals. "Representation learning with contrastive predictive coding." arXiv preprint arXiv:1807.03748 (2018).

[3] Khosla, Prannay, et al. "Supervised contrastive learning." Advances in neural information processing systems 33 (2020): 18661-18673.

### Questions
Please see weaknesses.

### Soundness
1 poor

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel contrastive diffusion probabilistic planning approach to tackle offline reinforcement learning (RL) tasks. It expands upon the foundational Diffuser model, leveraging contrastive learning to enhance the quality of samples by generating high-return trajectories. This focus on sequence modeling within offline RL is both interesting and important. The paper is well-written, though it lacks some specifics, and the visual representations, particularly Figure 1, are insightful.

### Strengths
- The focus on sequence modeling in offline-RL is both innovative and significant, addressing a crucial aspect of this field.
- This paper proposed a novel method of integrating contrastive learning that showed improvement over the baseline Diffusers.
- Figure 1 is quite illustrative and intuitive.

### Weaknesses
### Missing Details in Methodology:

- The training process of the model remains unclear. While Equation 14 suggests end-to-end training, it is unclear where the contrastive loss is integrated. If added to the diffusion probabilistic model, which aims to reconstruct the un-corrupted trajectories, will this added loss diverge the learning, making the training unstable?
- Is the contrastive loss involved during guidance sampling? 

### Insufficient Experiments:

- The claim of 'significant improvements in medium and medium-replay datasets' seems overstated. The improvements are noticeable in only one task from each dataset compared to DD.
- Extending experiments to more complex control tasks or scenarios with high-dimensional state/action spaces would substantiate the method's effectiveness.
- A comparative test incorporating DD + Contrastive Learning would add effectiveness to the proposed method.
- Figure 6 requires more explanation, particularly regarding the methodology for generating and comparing states in each showcased scenario.

### The method introduces several additional hyperparameters, as depicted in Figure 7, indicating a significant sensitivity to these parameters, which could complicate the tuning process.

### Questions
- The distinctions among the three models presented in Figure 5 are not very clear to me.
- For the experiments depicted in Figure 6, how are the generated states and actual states obtained in each case?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the problem of learning state-action trajectory generation with diffusion models. To better leverage the high-return states in the offline dataset, the authors proposed a contrastive learning mechanism to drive the generated trajectory toward the high-return states. Experiments are performed on D4RL benchmarks to validate the idea.

### Strengths
The motivation for leveraging contrastive learning to guide the generation process is interesting and reasonable; 

The paper is well-written and easily read.

### Weaknesses
The method seems on par or slightly worse than the baseline approaches; 

The experiments were only conducted on a few simple periodic tasks, which could not sufficiently demonstrate the effectiveness of the method; 

There is no analysis of failure modes and limitations.

### Questions
What is the task shown in Fig. 5? For visualizing the task, it would be better to align some of the high-return and low-return states to the visual observations of the environment, which may help readers better understand the task. 

For Fig. 6, could the authors provide the annotations for the x-axis and y-axis? 

It would greatly enhance the paper if the authors could offer a more in-depth analysis of failure cases. Additionally, aside from relatively straightforward periodic tasks, it would be beneficial if the authors explored more complex tasks. Demonstrating the applicability of their approach in scenarios like robot navigation or manipulation would significantly bolster the paper's overall impact and practical relevance.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
