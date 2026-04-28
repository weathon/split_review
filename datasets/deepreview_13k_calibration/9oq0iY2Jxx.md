# Symmetric Reinforcement Learning Loss for Robust Learning on Diverse Tasks and Model Scales

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
Reinforcement learning (RL) training is inherently unstable due to factors such as moving targets and high gradient variance. Reinforcement Learning from Human Feedback (RLHF) and Reinforcement Learning from AI Feedback (RLAIF) can introduce additional difficulty. Differing preferences can complicate the alignment process, and prediction errors in a trained reward model can become more severe as the LLM generates unseen outputs. To enhance training robustness, RL has adopted techniques from supervised learning, such as ensembles and layer normalization. In this work, we improve the stability of RL training by adapting the reverse cross entropy (RCE) from supervised learning for noisy data to define a symmetric RL loss. We demonstrate performance improvements across various tasks and scales. We conduct experiments in discrete action tasks (Atari games) and continuous action space tasks (MuJoCo benchmark and Box2D) using Symmetric A2C (SA2C) and Symmetric PPO (SPPO), with and without added noise with especially notable performance in SPPO across different hyperparameters. Furthermore, we validate the benefits of the symmetric RL loss when using SPPO for large language models through improved performance in RLHF tasks, such as IMDB positive sentiment sentiment and TL;DR summarization tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper considers the problem of a noisy signal affecting the policy updates when using actor critic algorithms for policy improvement. It takes inspiration from the idea of symmetric cross-entropy loss, which has been shown to mitigate a similar problem caused by noisy labels in supervised classification tasks. The paper proposes to modify the policy gradient updates for A2C and PPO by creating corresponding reverse losses for each of these algorithms, which when incorporated into the regular loss, gives us the "symmetric" A2C and PPO losses. Gradient analysis is done on these new losses to show  that their introduction does not interfere with the gradients of the original losses. Finally, experiments are done in tasks with discrete action spaces, continuous action spaces, and with LLM training, to show that these symmetric losses improve performance compared to the baselines. Specifically, this paper shows that the symmetric PPO loss improves performance over the regular PPO loss, probably because it mitigates the effects of the small batch, advantage normalization, and the progressively off-policy updates that take place in PPO.

### Strengths
* The paper takes an approach useful for classification with noisy labels and successfully modifies it for policy gradient approaches. The idea itself is intriguing and needs to be delved into deeper to better characterize how estimation errors due to function approximation or noisy rewards can be mitigated via this scheme.
* The gradient analysis in Section 4.3 gives some confidence that the proposed approach is not harming learning.
* Experiments successfully degrade performance of A2C and PPO, and show that the symmetric versions better deal with the noisy rewards.
* The hypothesized reasons for why SPPO improves over PPO make intuitive sense.
* Figure 2 is a great addition to the paper. It clearly shows that even though advantage normalization is necessary in PPO, that normalization can potentially change whether an action is encouraged or discouraged based on data in the mini-batch.

### Weaknesses
* This paper seems to have the seeds of a great idea. Some deeper investigation and perhaps an attempt at generalizing the proposed approach beyond two specific loss functions might be useful.
* I could see the parallels between the RCE loss and the proposed reverse A2C and reverse PPO losses. But a first principles derivation of the loss could perhaps be more convincing and lead to a more general loss. As it stands, the loss seems slightly shoe-horned, and I'm not convinced it is the correct drop in for a reverse cross-entropy loss. I see the advantage value $A(x, k)$ as the equivalent of $q(k|x)$. That cal also be connected to the noisy labels and the error in advantage estimation. But the proposed loss seems to consider the action taken by the agent to be $q(k|x)$. Could the authors explain the justification for this choice? One suggestion to instead use the advantages is to map the advantages to a simplex and turn them into probabilities. The RCE loss can then be directly adapted. Could that perhaps be a better approach?
* Perhaps this is a repeat of the previous point, but in equation 8 the clipping used in PPO is not present. Also since the PPO loss does not follow the CE loss structure of having a log p, the presence of Z in the reverse seems incongruous.
* Instead of more specific weaknesses for the work presented in the paper, I have questions for why certain approaches are not considered, or suggestions to strengthen the paper. I include these in the next section. The rest of this section I will point out minor typos and edits.
* On line 53, perhaps cite [1] as an example of ensembles being useful for better value prediction
* On like 54, perhaps cite [2] or some other paper for an example of normalization helping.
* Lines 68-70 seem like a generalization. A2C does not do advantage normalization
* The paper calls its solution the "symmetric RL loss" but the loss pertains to policy gradient, or even more specifically to actor-critic, methods. Perhaps call it the symmetric policy gradient loss?
* Line 177-178. The advantage function is slightly misconstrued here. The advantage function estimates how much better it would be to deterministically take action $a$ instead of following the current policy $\pi$.
* Line 178: " In the approach section" is an awkward phrasing. Consider "in the next section"
* Line 189: " ... also consider incorporates ..." is wrong grammatically. Perhaps drop "consider"
* Line 213 claims: `A highly engineered reward function is required to eliminate errors, ...`. A reference to back this claim up would be helpful.
* Line 215: "Has model errors", can be better expressed as "has estimation errors" or "approximation errors".
* Line 248: Perhaps the reference is meant for Equations 7 and 9, instead of 4 and 9?
* Line 399: Better to cite Bellemare et al. [3], for the arcade learning environment.
* Line 403 posits that the Atari environments only give rewards of 0 or 1. That does not seem to be correct. Is the paper focusing on a particular setup where the rewards are clipped?
* Line 457: Extra "is": `Note that the open-source GPT-J model "is" often outputs empty summarizations for most evaluation data`
* The table in Appendix 14 does not clarify whether the "performance increase" is perplexity or reward.
* Line 721, citation for Wang et al. can instead be for the published paper [4]
* Last few lines of page 15: it is helpful to review if you specify what operations you did at each step here.

References:
[1] Fujimoto, S., Hoof, H. and Meger, D., 2018, July. Addressing function approximation error in actor-critic methods. In International conference on machine learning (pp. 1587-1596). PMLR.

[2] Yue, Y., Lu, R., Kang, B., Song, S. and Huang, G., 2024. Understanding, predicting and better resolving Q-value divergence in offline-RL. Advances in Neural Information Processing Systems, 36.

[3] Bellemare, M.G., Naddaf, Y., Veness, J. and Bowling, M., 2013. The arcade learning environment: An evaluation platform for general agents. Journal of Artificial Intelligence Research, 47, pp.253-279.

[4] Wang, Y., Ma, X., Chen, Z., Luo, Y., Yi, J. and Bailey, J., 2019. Symmetric cross entropy for robust learning with noisy labels. In Proceedings of the IEEE/CVF international conference on computer vision (pp. 322-330).

### Questions
* Can a distributional critic, like in QR-SAC [1], be an alternative to this symmetric loss? The distributional critic can better model noisy rewards, and as long as the noise does not obscure the signal, it should be able to estimate the right thing to do.
* Equation 7 looks a little bit like the policy gradient loss for the actions not taken as seen in expected policy gradients [2, 3]. There are obvious differences, but could you elaborate on why the reverse RL loss is different? Would expected policy gradients be something worth comparing to?
* For the RLHF tasks, is the reward model used for training the same one used for evaluation? That seems like it could be prone to overfitting.
* Appendix A.1. Is this analysis dependent on a softmax parameterization of the policy? It would be helpful for readers if that was made clear here.
* In table 11, Performance of SPPO with noise seems better than noiseless atari with or without SPPO on the following games: Centipede, Gopher, StarGunner, VideoPinball, WizardofWor. This result seems very surprising to me. Could you speculate on what the reason for this improved performance when the signal is obscured might be?

References:
[1] Wurman, P.R., Barrett, S., Kawamoto, K., MacGlashan, J., Subramanian, K., Walsh, T.J., Capobianco, R., Devlic, A., Eckert, F., Fuchs, F. and Gilpin, L., 2022. Outracing champion Gran Turismo drivers with deep reinforcement learning. Nature, 602(7896), pp.223-228.

[2] Ciosek, K. and Whiteson, S., 2018, April. Expected policy gradients. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 32, No. 1).

[3] Allen, C., Asadi, K., Roderick, M., Mohamed, A.R., Konidaris, G. and Littman, M., 2017. Mean actor critic. arXiv preprint arXiv:1709.00503.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes the use of symmetric loss in reinforcement learning (RL) by drawing inspiration from supervised learning. By applying symmetric loss, algorithms such as Proximal Policy Optimization (PPO) and Advantage Actor-Critic (A2C) can achieve improved performance in scenarios with noisy reward functions. The authors provide gradient analysis to justify their method and conduct comprehensive experiments to demonstrate its effectiveness.

### Strengths
The idea of using symmetric loss from supervised learning to improve RL is promising. The authors substantiate their claims through thorough experimental evaluations and gradient analysis, demonstrating the efficacy of the symmetric loss.

### Weaknesses
1. The paper needs to be better polished and organized, especially in the Experiment section. For instance:
   - Figure 1 is placed on page 5 but is first cited on page 2.
   - Figure 2 is in the Approach section on page 6, but its first citation is in the Experiment section on page 10.
   - The caption of Table 2 is inconsistent with its content.
   - "Figure 4.1" is mentioned in line 466, but its reference is unclear.
   - The phrase "the sum of rewards as defined in 1" in line 167 is ambiguous; the specific reference needs clarification.
   - Notations in Section 5.2 are confusing. The first and second paragraphs introduce DA2C and DSPPO, but the third uses SA2C and SPPO.

2. Section 5.4 appears to contribute minimally to the paper. The observed benefits of SPPO over SA2C are likely due to the advantages of PPO over A2C, rather than the symmetric loss proposed in this paper.

### Questions
1. What are the performances of PPO and A2C on clean MuJoCo and Box2d environments? Given the 0.05 standard deviation of reward noise is relatively small, it seems unlikely that this level of noise would cause a significant performance drop since some existing work utilizes perturbed reward noise to boost performance.
2. Can you explain why SPPO and SA2C still perform better on clean Atari games?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper tackles the challenge of noise introduced by factors such as the reward function, which can degrade the accuracy of advantage-guided policy updates during RL algorithm training. To mitigate these effects, the authors propose integrating symmetric RL loss into RL to enhance the algorithm's robustness against noisy data. The paper begins by discussing how traditional RL algorithms and RLHF methods can be affected by noise due to human or environmental factors, leading to unstable learning. Drawing inspiration from Symmetric Cross Entropy, the authors adapt this concept to RL to reduce the impact of noisy data on performance. Theoretical analysis at the gradient level demonstrates the benefits of symmetric RL loss in noisy environments. The effectiveness of the proposed method is validated through experiments in various settings, and its potential in large-scale model training within RLHF tasks is highlighted. Overall, this paper introduces new ideas to enhance robustness in reinforcement learning and provides an innovative solution for improving robustness in RLHF.

### Strengths
1. The experimental section thoroughly examines the probability of advantage sign reversal under different conditions, using empirical data to illustrate the influence of noisy data on algorithm stability. This supports the argument for incorporating symmetric RL loss to enhance stability.
2. The paper validates the effectiveness of symmetric RL loss across multiple noisy reward function scenarios, demonstrating its ability to improve robustness under environmental noise. Experiments on the IMDB and TL;DR datasets show that the proposed algorithm can effectively boost performance in RLHF tasks, mitigating the impact of noise from subjective evaluations.

### Weaknesses
1. The introduction should provide more context on the current research directions and challenges in enhancing robustness within the field. Without this background, readers may struggle to understand the specific difficulties and the broader context of the problem.
2. The method section lacks clarity, making it difficult for readers to follow the transition from the standard RL loss described in the PRELIMINARIES section to the modifications introduced in the APPROACH section. Additionally, the definition of \( Z \) is vague, only stating that Equation 5 defines \( Z \), which complicates understanding.
3. The experimental section could benefit from comparisons with other methods aimed at enhancing robustness in RL. Such comparisons would provide a more comprehensive evaluation of the proposed method's performance and highlight its advantages and disadvantages relative to other robustness-enhancing techniques.

### Questions
1. Could symmetric RL loss be applicable to algorithms that do not rely on advantage to improve their robustness?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper claims RL training is unstable and enhances the stability of RL training by adapting reverse cross-entropy. The proposed method is called Symmetric PPO (SPPO) and Symmetric A2C (SA2C). The authors experimented with their techniques and found SPPO to obtain strong performance in standard deep RL tasks like Atari, MuJoCo, as well as RLHF tasks like IMDB positive sentiment and TL;DR summarization.

### Strengths
There seems to be some interesting analysis of how advantages work empirically, and the authors conducted experiments in various domains and validated their approach.

### Weaknesses
However, the experiment results are not convincing. 

First, the PPO baseline results in Atari seem to underperform the known results at [openrlbenchmark](https://github.com/openrlbenchmark/openrlbenchmark?tab=readme-ov-file#compare-cleanrls-ppo-with-openaibaseliness-ppo2-on-atari-games). See the table below, which shows the author's PPO performance significantly underperform the reported performance. I am using the results at 5M episodes for a fair compairson because it seems the authors used 5M episodes in Figure 3, which is missing a legend. 

| Game | PPO | SPPO | openai/baselines @ 5M steps |
|------|-----|------|---------------------------|
| Alien | 1128 ± 105 | 1081 ± 79 | **~1500** |
| Centipede | 2961 ± 379 | 3694 ± 224 | ~3100 |
| CrazyClimber | 86764 ± 3568 | 103588 ± 2871 | ~100000 |
| Gravitar | 371 ± 47 | 442 ± 67 | **~600** |
| Qbert | 4352 ± 128 | 4412 ± 282 | **~12500** |
| MsPacman | 837 ± 62 | 1204 ± 86 | **~1750** |
| NameThisGame | 5665 ± 280 | 5423 ± 63 | ~5400 |
| UpNDown | 58289 ± 21226 | 126830 ± 27534 | ~100000 |

The RLHF experiment design also seems problematic. The GPT4 win rate of a 6B model with SPPO in TL;DR summarization is only 52.50%, whereas comparable work using RLOO gets 77.9% win rate (https://arxiv.org/pdf/2402.14740) or PPO 67%. Some of these discrepancies might come from the training codebase / dataset. For example, the `CarperAI/openai_summarize_comparisons` has double spacing in its preference dataset between `TL;DR:` and the actual response. Some of the weird quirks the authors suggested with the policy model / RM might come from small but relevant details like this.

```
>>> from datasets import load_dataset
>>> ds = load_dataset("CarperAI/openai_summarize_comparisons", split="train")
>>> print(ds[0]["chosen"])
TL;DR:  Snooped, found something, should I admit what I found so we can have a more honest conversation about it with less denial on her part?
>>> ds
Dataset({
    features: ['prompt', 'chosen', 'rejected'],
    num_rows: 92534
})
>>> print(ds[0]["chosen"][5])
:
>>> print(ds[0]["chosen"][6])
 
>>> print(ds[0]["chosen"][7])
 
>>> print(ds[0]["chosen"][8])
S
>>> 
```

Overall, despite having interesting theory and analysis, I am concerned by the quality of the experiment design and results.

### Questions
What codebase did the authors use for the Atari / MuJoCo experiments?

### Soundness
1

### Presentation
2

### Contribution
1
