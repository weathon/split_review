# Q-SFT: Q-Learning for Language Models via Supervised Fine-Tuning

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
Value-based reinforcement learning (RL) can in principle learn effective policies for a wide range of multi-turn problems, from games to dialogue to robotic control, including via offline RL from static previously collected datasets. However, despite the widespread use of policy gradient methods to train large language models for single turn tasks (e.g., question answering), value-based methods for multi-turn RL in an off-policy or offline setting have proven particularly challenging to scale to the setting of large language models. This setting requires effectively leveraging pretraining, scaling to large architectures with billions of parameters, and training on large datasets, all of which represent major challenges for current value-based RL methods.
In this work, we propose a novel offline RL algorithm that addresses these drawbacks, casting Q-learning as a modified supervised fine-tuning (SFT) problem where the probabilities of tokens directly translate to Q-values.
In this way we obtain an algorithm that smoothly transitions from maximizing the likelihood of the data during pretraining to learning a near-optimal Q-function during finetuning.
Our algorithm has strong theoretical foundations, enjoying performance bounds similar to state-of-the-art Q-learning methods, while in practice utilizing an objective that closely resembles SFT.
Because of this, our approach can enjoy the full benefits of the pretraining of language models, without the need to reinitialize any weights before RL finetuning, and without the need to initialize new heads for predicting values or advantages.
Empirically, we evaluate our method on both pretrained LLMs and VLMs, on a variety of tasks including both natural language dialogue and robotic manipulation and navigation from images.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposed Q-SFT, a method that integrates Q-learning with SFT for LLMs in the multi-turn RL setting. To exploit both the representation and the logits in LLMs learned in the pretraining stage and bypass the poor scaling effect of TD-style objectives, the authors proposed a novel weighted cross-entropy loss that embeds the learning of the Q-value into the weights. In this way, the logits prior in the pretrained LLMs can be leveraged, and no new head is needed to learn the Q-values. Theoretical analysis has shown the guarantee of the new learning objective leading to a conservative estimation of the value function. Experiments on several scenarios have demonstrated the effectiveness and efficiency of the proposed method.

### Strengths
- The work targets at the multi-turn RL scenario for LLMs, which is vital for the development of complex reasoning and agentic use in LLMs.
- The proposed algorithm is backuped with a solid theoretical motivation.
- The experimenting scenarios have a broad coverage, and the performance is well-demonstrated.

### Weaknesses
While the theoretical analysis shown in Section 4.3 demonstrates that the Q value learned with Equation (3) has the bounds independent from the hyperparameter \gamma, I wonder what the ablating effect \gamma brings in practice: Will certain configuration of \gamma contribute the learning of a better Q-value estimation? This question has another motivation: In Equation (3), some of the probability mass is allocated to the dummy actions a', and the weight ratio between the actions in the demonstration trajectory and the dummy ones has one degree of freedom determined by \gamma. It would therefore be great to sweep \gamma to study the ablation effect of the weight ratio.
   - And by the way, how is the \gamma set in the demonstrated experiments?

- According to Equation (3), learning the Q-value function requires a learned behavior policy \pi_\beta in prior. How will the quality of the behavior policy impact the learning of the Q-values, and the performance of the ultimate policy? While I appreciate the experiments in Figure 4 where only 10% of the training data are used to get the \pi_\beta, I wonder how the performance grows with the quality of the initial behavior policy. For example, if the initial behavior policy is near perfect, will it be that the ultimate policy, although weighted with the learned Q-values, performs similarly with the initial one?

### Questions
- While the theoretical analysis shown in Section 4.3 demonstrates that the Q value learned with Equation (3) has the bounds independent from the hyperparameter \gamma, I wonder what the ablating effect \gamma brings in practice: Will certain configuration of \gamma contribute the learning of a better Q-value estimation? This question has another motivation: In Equation (3), some of the probability mass is allocated to the dummy actions a', and the weight ratio between the actions in the demonstration trajectory and the dummy ones has one degree of freedom determined by \gamma. It would therefore be great to sweep \gamma to study the ablation effect of the weight ratio.
   - And by the way, how is the \gamma set in the demonstrated experiments?

- According to Equation (3), learning the Q-value function requires a learned behavior policy \pi_\beta in prior. How will the quality of the behavior policy impact the learning of the Q-values, and the performance of the ultimate policy? While I appreciate the experiments in Figure 4 where only 10% of the training data are used to get the \pi_\beta, I wonder how the performance grows with the quality of the initial behavior policy. For example, if the initial behavior policy is near perfect, will it be that the ultimate policy, although weighted with the learned Q-values, performs similarly with the initial one?

### Soundness
4

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
This paper proposes a method that leverages the LLM logits learned via supervised fine-tuning to approximate the Q-learning objective. Authors argue that traditional Q-learning setup suffers from discarding the logit head, and learning a new head for Q values, so the proposed method directly translates the learned logits to Q values, with theoretical analysis on its bound and approximation. Experiments include text-based games, image-based navigation and robotic manipulation, and show some benefits of the proposed method over the prior value-based RL method.

### Strengths
- Using probability prediction in the Q-learning objective is cool, and it sounds particularly beneficial for large vocabulary/action space. 
- The implementation of the method is straightforward: learning two models using different objectives, and use both at inference time

### Weaknesses
 - I found the pitch very confusing: it emphasizes multi-turn problems like dialogue, but the actual math formulation treats each turn as a single token in an utterance (i.e., the action space is the vocabulary space). The generation process is to generate an utterance token by token, which is conventional, and it’s confusing where the multi-turn setup plays a role other than using this generative model repeatedly to generate different utterances at different parts of the dialogue. In other words, the value function here is not the reward per utterance as stated in the intro (line 074), and question answering is also not a single-step problem as the answer is also generated token by token.
- Experimental setup seems simplified in terms of 1) for language-based tasks, the game nature makes the effective vocabulary very small and unambiguous, 2) the well-defined reward function setup in text games do not translate into practical problems, 3) why no supervised learning results from prior work as a direct comparison?; 4) most of the datasets already have RL method outperform supervised learning which is contradictory to the intro “offline RL fine-tuning of LLMs does not reliably outperform supervised fine-tuning”. Therefore, it’s unclear whether the improvement brought by the proposed method should be contrasted to what exactly.
- The writing can be further improved in terms of clarity, accuracy, and fixing typos. A few examples below: 
   - Table 1: number from the proposed method is bold in the Wordle column, but it’s not the best performance method
   - Define h used in line 162
   - Prime should be on a, instead of argmax in line 218
   - Consistently use “RL” instead of having “RI” occurred 
   - Citation should be within a pair of parentheses: line 037, 039

### Questions
Please see the previous section.

Response to the rebuttal: (posted here since the rebuttal ended)

Thanks for all the clarification and discussion -- I raised my scores accordingly. It would be very valuable to revise the paper to address the points we discussed, especially the clear definition on step vs turn, the potential to scale better than existing RL approaches, the setup and comparable work of SFT baselines, motivation to alleviate the downsides of using RL, etc.. The rebuttal was helpful to better understand this work, and it would definitely be better if readers only need to read the paper itself to sufficiently appreciate this work.

### Soundness
3

### Presentation
1

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
This paper proposes a new RL training method for LLMs that take advantage of the pretraining. It is based on Q-learning, but instead of attaching a new value head, the method uses the existing token probabilities as value function. There is some theoretical guarantees and diverse experimental results involving multi-steps interactions.

### Strengths
- Novelty: the method seems to be quite novel. The way it works is quite different from a typical Q-learning where L2 loss is used. Instead it relies on a cross-entropy loss that is modified. Given the importance of RLHF in LLMs and the need of multi-step interaction, a study like this can be impactful and important.
- The experiments are quite diverse, ranging from LLM-based text tasks to VLM-based robotic manipulation. It is also compared to a diverse set of baselines, which helps to solidify the claims.
- There is a proof about a theoretical guarantee, which is always nice to have. The method also leads to an improvement in performance in practice too, where the gap increasing as the model scales. Given the lack of value-based approaches in LLMs, it would be interesting to see if this method will adopted widely.
- Paper is well written and easy to follow.

### Weaknesses
 - I felt like the writing of the experimental results were a bit too short. It would have been good to have more ablation studies to understand why the method works, and in which situations it is more optimal. For example, since the main motivation is that the value head is not initialized from scratch, what will happen if we do that but keep the loss the same. Also there is not much on the training details, such as the number of training steps etc. I think the other parts can be condensed to make space. 
- Another important part that was too short was the method itself. The method is introduced between L230-261, which is about only half page. It doesn’t give enough explanation about why this method should work, so it was quite hard to understand it. For example, can you give more insight into why the proposed method should be more stable? 
- Reuse of the pretrained weights is emphasized as the main motivation, but some of the tasks actually train the model from scratch and others are not in natural language, which is a bit conflicting. There is still an improvement when trained from scratch, which is good, but there is a lack of explanation why it works better.

### Questions
- Some typos: L39 citation, L84 sentence, L194 “performing”, Fig2 top left, 
- Eq2 should have a negative sign? Also tab1 -2.08 should be bold, not -2.11. 
- The figure 1 was bit too small and hard to read.
- L153 defines RL as MDP, but what about POMDP?
- About the theoretical guarantee, how good is the lower bound? A probability from a policy can be quite low for large vocabulary, in which case then the bound is not that tight?
- How many models needed to be loaded during training? There is the main model, also a target model and the original model. So is that 3? How does that affect memory usage?
- Given that some baselines use different base models, it would be nice to put them in the table. This will help if they perform better because their base model is stronger or not.
- In fig3, the error bars correspond to different seeds?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes Q-SFT, a new approach that enables fine-tuning of LLMs and VLMs within an offline RL framework but using a supervised learning-style loss function. The method matches or outperforms previous approaches across a range of LM fine-tuning benchmarks.

### Strengths
- The motivation is clear: the instability of the Q-learning objective is a well-known challenge in the RL literature.
- The proposed method is straightforward and demonstrates strong empirical performance, with improvements in sample efficiency and scalability over previous methods.
- The evaluation covers a wide range of benchmarks.

### Weaknesses
It seems there are some limitations to the proposed approach that are not addressed in the paper.
- During inference, the approach requires double the number of forward passes—one for the original pretrained LM and one for the fine-tuned LM. This can be challenging in practical scenarios where real-time decision-making is essential, such as robotic manipulation. The computational overhead of this dual-pass approach is significant, particularly for large language models, and the paper does not provide sufficient analysis of the latency implications, which could limit its applicability in time-sensitive environments.
- In Theorem 4.1., the lower bound for the learned p_theta is Q* multiplied by pi_beta. If pi_beta is small, the resulting pi_theta can be overly conservative compared to the true Q*. This conservatism could lead to suboptimal policy learning, especially in scenarios where exploration is crucial. The paper lacks a discussion on how this lower bound affects the practical performance of the algorithm, particularly in environments requiring more aggressive exploration strategies.

### Questions
.

### Soundness
3

### Presentation
3

### Contribution
3
