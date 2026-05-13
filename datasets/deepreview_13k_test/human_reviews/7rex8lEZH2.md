# Prompt Tuning with Diffusion for Few-Shot Pre-trained Policy Generalization

- Decision: Reject
- Scores: 6, 5, 8, 5

## Abstract
Offline reinforcement learning (RL) methods harness previous experiences to derive an optimal policy, forming the foundation for pre-trained large-scale models (PLMs).
    When encountering tasks not seen before, PLMs often utilize several expert trajectories as prompts to expedite their adaptation to new requirements.
    Though a range of prompt-tuning methods have been proposed to enhance the quality of prompts, these methods often face optimization restrictions due to prompt initialization, which can significantly constrain the exploration domain and potentially lead to suboptimal solutions.
    To eliminate the reliance on the initial prompt, we shift our perspective towards the generative model, framing the prompt-tuning process as a form of conditional generative modeling, where prompts are generated from random noise.
    Our innovation, the Prompt Diffuser, leverages a conditional diffusion model to produce prompts of exceptional quality. 
    Central to our framework is the approach to trajectory reconstruction and the meticulous integration of downstream task guidance during the training phase.
    Further experimental results underscore the potency of the Prompt Diffuser as a robust and effective tool for the prompt-tuning process, demonstrating strong performance in the meta-RL tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper identifies the generalization challenges in offline reinforcement learning due to the lack of data quantity and quality. The author(s) build a connection with pre-trained large-scale models that share a similar difficulty. Based on that, a new prompt-tuning method using generative modeling is proposed to improve the performance of offline RL.

### Strengths
The idea to identify similar difficulties with PLM and align with state-of-the-art technical is innovative.

The paper provides a detailed review and a smooth transition from the existing work of both PLMs and offline RL to the proposed work.

The methodology demonstration is clear and easy to follow.

### Weaknesses
The presentation of figures can be improved, e.g., the text in Figure 2 is too small compared to the bar size, so as in Figure 3.

The proposed method needs theoretical support other than empirical analysis to avoid being a mix of heuristic designs.

For experiments, the testing scenarios are limited to answering the three important questions at the beginning of Sec. 5. For example, the results of the ablation study in Figure 3 don’t have a common conclusion and need more analysis. Without comprehensive experiments and insights, It’s hard to generalize the approach to other problems.

### Questions
How big is the difference between seen and unseen environments and tasks in the testing cases? As this part of the motivation, the results may be sensitive to the scenario changes. Have you quantified the difference that makes the prompt-tuning useful for offline RL?

The reviewer doubts the effectiveness of using guidance from downstream tasks. Interestingly, Figure 3, which does not have the label for performance metric, doesn’t present the same conclusion for different tasks. Guidance loss may not be useful sometimes. Can you explain why? 

When considering the two losses, the gradient projection seems beneficial, but is there a comparison to validate the superiority over a linear combination?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The work introduces using generative modeling using a diffusion process to do prompt tuning where the prompts are generated using random noise. The method uses signals from downstream tasks to generate better prompts, thus gaining advantage over methods which do not use this form of signal propagation.

### Strengths
1. The method provides an interesting way to use diffusion methods for few-shot policy learning.
2. By using downstream task information and gradient guidance, the task can achieve good performance as compared to baseline methods.
3. The work is an interesting direction for prompt-tuning methods.

### Weaknesses
1. The work doesn't discuss the diversity of the prompts generated. An analysis, quantitative or qualitative, can help understand if there is enough variation in the generated prompts and their comparison with baseline methods.
2. The length of the prompts is considered small. An ablation over the effect of prompt sizes can be important.
3. The effect of downstream tasks seems to be an important factor in contributing towards the success of the method. An ablation on the effect of this vs the rest of the method will be useful - one example is - if the downstream task is restricted in some manner.
4. Although the method considers few-shot settings, an additional examination of the zero-shot setting can be useful to evaluate the transfer capabilities and analyze how tried the generated prompts are to the downstream method.

### Questions
1. How is the quality of the prompts generated? Is there enough diversity?
2. Have different prompt lengths been tried and what is their impact?
3. What is the impact of quality and size of downstream tasks, and zero-shot performance?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
the author propose Prompt Diffuser (PD), a generative module to augment the prompt tuning decision transformer for reinforcement learning. The authors train a reward-to-go conditioned generative model in order to obtain a better initialization of the prompt. The author provide empirical evidence showing its effectiveness on multiple benchmarks and perform proper ablations.

### Strengths
This is a good paper because it reveals the important insight about prompt turning in RL, which is the importance of visualization. The movitating example in Fig2 is very helpful to establish the hypothesis. The choice of using a conditional diffusion model is well motivated. The empircal results are solid, and the ablation in Table 2 show the effect of the better initialization from the diffusion model.

### Weaknesses
I might miss this, but I would encourage the author to also show the OOD generalization to novel environments as is done in the PDT paper section 6.4 to make the results stronger? 

More results on how the diffusion model generalize to unseen reward-to-go?

Any visualization on the diversity of generated prompts/trajectories?

### Questions
See above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel approach called Prompt Diffuser to prompt-tuning for few-shot pre-trained policy generalization in meta-RL tasks. The approach eliminates the reliance on initial prompts and instead generates high-quality prompts from random noise using a conditional diffusion model. The authors conduct experiments to demonstrate the effectiveness of this approach and compare it to other prompt-tuning techniques. The results show that the Prompt Diffuser outperforms other methods regarding sample efficiency and generalization performance.

### Strengths
> To my knowledge, this paper presents a new approach to overcome the limitations of prompt-tuning for PromptDT.

> Based on the experimental results, it is evident that the Prompt Diffuser outperforms the previous method in terms of performance.

### Weaknesses
> While the experimental performance of the algorithm is commendable, this paper primarily represents a combination of existing methods and needs more substantial innovation.

> The motivation of the paper needs some clarification. In the abstract, the authors emphasize the limitations of previous prompt-tuning methods when applied to previously **unseen** tasks, highlighting the need for enhanced generalization and diversity in generative models. There appears to be a discrepancy in this viewpoint, as the subsequent sections of the paper emphasize the **accuracy** of generating prompts within the existing prompt distribution. However, the diversity and the accuracy seem to be a trade-off for the generation.

### Questions
> Could the authors clarify whether Prompt Diffuser should output prompts that are more generalized for previously unseen tasks or more precise within the existing prompt distribution?

> Could the authors visualize or show the similarity between the generated prompts from Prompt Diffuser and the ground truth prompts under unseen target tasks? 

> Is there any reason for using DM rather than DT for prompt generation? Can the prompt generation be integrated into DT directly?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
