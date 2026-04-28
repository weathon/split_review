# Consistency Models as a Rich and Efficient Policy Class for Reinforcement Learning

- Decision: Accept
- Avg Score: 5.00
- Scores: 6, 6, 3

## Abstract
Score-based generative models like the diffusion model have been testified to be effective in modeling multi-modal data from image generation to reinforcement learning (RL). However, the inference process of diffusion model can be slow, which hinders its usage in RL with iterative sampling. We propose to apply the consistency model as an efficient yet expressive policy representation, namely \textit{consistency policy}, with an actor-critic style algorithm for three typical RL settings: offline, offline-to-online and online. For offline RL, we demonstrate the expressiveness of generative models as policies from multi-modal data. For offline-to-online RL, the consistency policy is shown to be more computational efficient than diffusion policy, with a comparable performance. For online RL, the consistency policy demonstrates significant speedup and even higher average performances than the diffusion policy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to use the recent "consistency models" as a way of parameterizing the policy for deep RL.  This is explored in offline RL, offline-to-online RL, and online RL with an actor-critic setup.  The performance is competitive with diffusion-BC despite requiring far fewer sampling steps.  This seems like a strong empirical advance to me, because the speed of sampling is essential for online reinforcement learning.  While the approach here is unsurprising, combining consistency models with RL, this still seems like an important contribution.  

notes: 
  -Diffusion inference is slow, so there could be value in using consistency models to define the policy, particularly for an actor-critic style algorithm.  
  -This paper considers both online, offline-to-online, and offline setups.  
  -The policy class is important for RL, especially that it be multi-modal.  
  -The paper lays out policy regularization to prevent out-of-distribution actions.

### Strengths
-I think that this project is very critical for the success of RL, as insufficiently rich policy classes are a major limitation.  Additionally, in RL it is important to draw as many samples as possible (either in a model or in the environment) so evaluating the policy quickly is critical.  So I think this work will have a lot of impact.   
  -I think it's also particularly impressive that the paper shows success in online RL, because in online RL it is important that the policy perform well even when it's imperfect (i.e. early in the training process).  Whereas in offline-RL, we could imagine that the policy only needs to perform well near the end of the training process.  We indeed see that the consistency model outperforms the diffusion model in the purely online setting (Figure 4).

### Weaknesses
 -The idea of using consistency models as RL policies is fairly intuitive and not terribly surprising.  
  -On the harder tasks like Kitchen and Adroit, there is a significant gap with Diffusion-BC baseline.

### Questions
-Have you thought about also using the consistency model as the "model" in the RL sense, i.e. to learn p(s' | s,a)?  If so, do you see any interesting challenges or opportunities there?

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes utilizing the consistency model to learn policies in modeling multi-modal data from image generation, which perform more efficiently than diffusion models. The authors evaluate their models on three typical RL settings: offline, offline-to-online, and online, and experiments show that the consistency policy can reach comparable performances than the diffusion policies while reducing half computation costs.

### Strengths
- The paper is well-written, and the experiments are sufficient, which include three different RL settings and four task suites with BC and RL baselines.
- The motivation behind this paper is natural and valuable.

### Weaknesses
The author claims the consistency policy is much more efficient than diffusion policies while keeping comparable results. However,
- the results in Tab. 1 and 2 can not support the conclusion in a way, which shows there are some significant drops in some tasks (such as halfcheetah-me, kitchen-xxx) between the Diffusion-BC and Consistency-BC or Diffusion-QL and Consistency-AC. Specifically, the performance drop in halfcheetah-me is quite substantial, and the kitchen-xxx tasks show inconsistent performance across different variations, making it hard to claim overall superiority. It is also unclear if these drops are statistically significant, and the lack of error bars makes it difficult to assess the robustness of the results.
- Moreover, in Tab. 3, when N = 5, the performance between Diffusion-QL and Consistency-AC is comparable while the time cost is also similar. This indicates that when the denoising step is small, the absolute scores of both methods are good enough. In this case, the consistency model has few advantages, which makes the improvement much more limited. The claim of efficiency is weakened by the fact that the consistency model's advantage is only clear when using a small number of steps (N=2), but its performance is not always competitive when using a larger N, which is needed for better performance.

### Questions
(1) The authors claim that "By behavior cloning alone (without any RL component), using an expressive policy representation with multi-modality like the consistency or diffusion model achieves performances comparable to many existing popular offline RL methods.", I'm wondering where is the multi-modality. Is the consistency policy trained for all tasks across all suites? Or does the offline dataset have different successful behavior policies? The author should make it more clear. 

(2) In the specific tasks in RL, the scenarios are not abundant and the trajectories are quite similar. If more expressive policy representation can result in better performances, what if using some large pre-trained representation models, can this problem be solved? (E.g. R3M)

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
It is known that the inference process of the diffusion model can be slow. In the context of RL, the diffusion model has been introduced and widely adopted recently. The authors focus on addressing the slow inference speed issue of diffusion in this paper. Their solution is to replace the diffusion model with the recently proposed consistency model. The authors make some minor adaptations of consistency models to make it fit the RL setting. The authors also test their method across offline RL setting, online RL setting, and offline2online finetuning setting, by building a consistency model on top of behavior cloning and actor-critic structure.

### Strengths
# Strengths

This paper pinpoints an interesting question that the current diffusion-based offline RL algorithms (e.g., Diffusion-QL) suffer from slow inference speed. The authors then propose to address this issue by using an existing method, the consistency model, and adapting it to the offline RL setting. This, as far as the reviewer can tell, is the first work that introduces the consistency model into the offline RL setting, online RL setting and offline2online setting. This paper is generally quite well-written, and I enjoy reading this work. The structure of this paper is clear and easy to follow. It is easy for the readers to capture the core points/conclusions in the experiment section. The authors conduct several experiments in D4RL domains like MuJoCo, AntMaze, etc., to show that their method can reduce the training time and inference time while maintaining comparable performance. The authors also do a good job in the related work part.

### Weaknesses
# Weaknesses

Despite the aforementioned strengths of this paper, I think this paper is below the acceptance bar of this venue. Please refer to the following comments

- (major) The novelty of this paper is limited. The authors simply borrow an existing method from the vision community and apply it to the RL tasks, with some minor modifications. I do not see much novelty in doing so. This paper seems more like a technical report or experimental report, in that the authors conduct several experiments and summarize the conclusions. One serious flaw of this paper is that the author merely reports some experimental phenomenons while the corresponding explanations and discussion are unfortunately missing. From an ICLR paper of this kind, I would expect to understand why such a phenomenon occurs. This paper leaves me with more questions than answers. For example, why on many offline and offline2online tasks, the consistency model underperform the diffusion model, while on some online hard tasks, the consistency model seems to be better? The authors do not provide any mechanistic explanation for these performance differences, which is a significant weakness.

- (major) This paper does not consider statistical significance. Written statements and the presentation of the results as tables (often without standard deviations) obscure this flaw. In fact, ALL tables in this paper do not include any signal of statistical significance for baseline methods, e.g., std, IQM [1]. We have reached a point of maturity in the field where claims need to be made in reference to actual statistical evidence, which seems to be lacking in the current presentation. The lack of statistical significance makes it difficult to assess the robustness of the proposed method and the validity of the conclusions drawn from the experiments. The absence of confidence intervals or standard deviations for the baselines makes it impossible to compare the proposed method with existing approaches in a statistically rigorous manner.

[1] Deep reinforcement learning at the edge of the statistical precipice. NeurIPS

- (major) The proposed consistency-BC or consistency-AC do not show much improvement over the diffusion-based counterparts. If one looks at the experiments in this paper, it is clear that the consistency-BC and consistency-AC cannot beat diffusion-BC or diffusion-QL on most of the tasks. The authors say that consistency-AC or consistency-BC can achieve less training time. Well, I do not see this as an appealing advantage over the diffusion-based methods, since training cost is somewhat unimportant, while the most critical part, from my perspective, is the inference speed. Let us then take a look at the inference cost. Based on Table 3 in the main text, it is clear that the inference speed of diffusion-QL is quite similar to that of the consistency-AC. For instance, when setting $N=5$, the inference speed of diffusion-QL gives 3.76ms and consistency-AC gives 3.39ms, while their performance differs (diffusion-QL has an average score of 108.2, while consistency-AC only has 101.4). I actually do not see many advantages of utilizing consistency-AC or consistency-BC in practice. The authors claim faster convergence, but the performance gap remains a significant concern.

- (major) Even worse, it seems that the performance of consistency-AC and consistency-BC are acquired by carefully tuning the hyperparameters. As a piece of evidence, one can see the hyperparameter setup in Appendix C (Table 5). This indicates that the generality and effectiveness of the proposed method are limited. The paper lacks a thorough analysis of the sensitivity of the proposed method to hyperparameter settings. The authors do not provide any guidance on how to select appropriate hyperparameters for new tasks, which raises concerns about the practical applicability of the method.

- (minor) On page 3, Eq 3 is the objective using clipped double Q-learning instead of vanilla double Q-learning. The authors ought to cite the TD3 paper here instead of the double Q-learning paper.

- (minor) No codes are provided in this paper, and the authors do not include a reproducibility statement section in the main text

### Questions
- why do you use different baselines on different domains? It is somewhat confusing that you use some quite weak baselines on domains like antmaze, adroit, and kitchen. As an example, why do you use AWR, BRAC, and REM on adroit tasks and kitchen tasks in Table 1? It seems to me that the advantages of consistency-BC and consistency-AC are illustrated by carefully picking the baselines.

- how important is the gradient norm to the consistency-BC and consistency-AC algorithms?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
