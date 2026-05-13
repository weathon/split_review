# POIL: Preference Optimization for Imitation Learning

- Decision: Reject
- Scores: 6, 6, 3, 8, 8

## Abstract
Imitation learning (IL) enables agents to learn policies by mimicking expert demonstrations. 
While online IL methods require interaction with the environment, which is costly, risky, or impractical, offline IL allows agents to learn solely from expert datasets without any interaction with the environment.
In this paper, we propose Preference Optimization for Imitation Learning (POIL), a novel approach inspired by preference optimization techniques in large language model alignment. 
POIL eliminates the need for adversarial training and reference models by directly comparing the agent's actions to expert actions using a preference-based loss function. 
We evaluate POIL on MuJoCo control tasks under two challenging settings: learning from a single expert demonstration and training with different dataset sizes (100\%, 10\%, 5\%, and 2\%) from the D4RL benchmark.
Our experiments show that POIL consistently delivers superior or competitive performance against state-of-the-art methods in the past, including Behavioral Cloning (BC), IQ-Learn, DMIL, and O-DICE, especially in data-scarce scenarios, such as using one expert trajectory or as little as 2\% of the full expert dataset. 
These results demonstrate that POIL enhances data efficiency and stability in offline imitation learning, making it a promising solution for applications where environment interaction is infeasible and expert data is limited.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers a practical offline imitation learning setting, aiming at learning the agent’s policy from limited demonstration without environmental interactions. The proposed method is called Preference Optimization for Imitation Learning (POIL), which compares the agent’s actions with the expert’s actions and computes the preference loss for updating the policy parameters. The empirical results on MuJoCo show consistently superior performances compared to several offline imitation learning baselines.

### Strengths
1.	POIL adapts the preference optimization techniques from large language models, eliminating the need for preference datasets, a discriminator, or a preference model. The learning process is simplified, avoiding adversarial training instability. This work exemplifies the successful adaptation of DPO-like alignment methods in LLMs to control problems in reinforcement learning and imitation learning. 
2.	POIL is simple and effective and shows superior performance in MuJoCo tasks compared to several offline imitation learning methods. POIL also performs better than other preference optimization methods in MuJoCo tasks.

### Weaknesses
1.	From Section 2, we know that SPIN is the most closely related to the proposed POIL, however, the POIL objective is directly adapted from CPO instead of SPIN, which is strange and may cause confusion. I believe CPO is chosen because it avoids using a preference model. In this sense, maybe CPO is the most related work to POIL? 
2.	SPIN can generate its training data and refine itself by distinguishing between current and previous outputs, continuously updating its reference model. In Section 3.2, Equation (3) is explained to maximize the divergence between the agent’s current behavior and its previous, which tries to link POIL to SPIN. However, it is not clear how this goal has been achieved.

### Questions
1.	How does equation (3) maximize the divergence between the agent’s current and previous behaviors?
2.	It seems POIL works quite well when \lambda=0 in Table 1, and POIL is sensitive to different \lambda in Figure 3. Does it mean that there is no need to introduce the BC regularization to the POIL loss?

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
3

### Summary
This paper introduce an imitation learning method called POIL, a DPO-like method, that compares agent actions (negative example) with expert actions (positive example). It evaluates POIL on 3 Mujoco tasks: halfcheetah, hopper, and walker2D.

### Strengths
- POIL is an interesting application of DPO like methods to robotics.
- the results demonstrate sample-efficiency gains compared to a few IRL and one BC baseline on Mujoco environments
- the ablations comparing various DPO like methods in robotics is interesting

### Weaknesses
- This work is missing comparisons to (or atleast discussions in related work comparing to) sample-efficient BC approaches that can work with one or very few demonstrations like ROT [1] and MCNN [2].
- A comparison (or discussion about) CPL [3] and other baselines in the CPL paper, another RLHF method for robotics, is also missing. 
- The evaluation environments are very simple vector-observation mujoco environments. It would be helpful to extend to either more environments from D4RL that testing stitching like the ant maze environment, or more complicated image-based environments like Atari, or more dexterous robotics environments like Robosuite and Adroit.
- the return tabulated for different methods is not normalized --- this makes it hard to determine its performance between random and expert and hard to compare with other papers.


[1] S Haldar, et al, Watch and match: Supercharging imitation with regularized optimal transport, CoRL 22

[2] K Sridhar, et al, Memory-Consistent Neural Networks for Imitation Learning, ICLR 24

[3] J Hejna, et al, Contrastive Preference Learning: Learning from Human Feedback without RL, ICLR 24

### Questions
Please see weaknesses.
Also, have the authors investigated a provable upper bound on the sub-optimality gap for POIL, maybe building on guarantees for DPO-like methods?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors consider framing offline IL as a preference learning problem. Specifically, they generate actions from the learner on states from the expert demonstrations and try to raise the relative probability of the expert actions to the learner actions.

### Strengths
-  A generally clear exposition of the proposed method.

### Weaknesses
Apologies for LaTex failing to render properly below -- I spent some time playing around with things to no avail.

I am fairly confident the proposed method is provably equivalent to a noisy version of behavioral cloning. To see this, first note that for policies in the exponential family (e.g. Gaussians), we can always write $\pi(a|s) = \exp(f(s, a)) / \sum_{a'} \exp(f(s, a'))$. Then, the likelihood gradient can be expanded to $\nabla_{\theta} \log \pi_{\theta}(a_E|s) = \nabla_{\theta} f_{\theta}(s, a_E) - \nabla_{\theta} \log \sum_{a'} \exp(f_{\theta}(s, a')) = \nabla_{\theta} f_{\theta}(s, a_E)  - \mathbb{E}_{a \sim \pi_{\theta}(\cdot|s)}[\nabla_{\theta} f_{\theta}(s, a)]$. Observe that if we ignore the $\log \sigma$ in the POIL loss for a moment, the BC gradient is simply the "infinite sample" estimate of POIL loss. Put differently: MLE in exponential families already includes a "negative gradient," there is no need to add one in explicitly.

For the specific case of Gaussians, for which the sufficient statistics / moments ($f_{\theta}$ in the above notation) are the mean and variance, the negative gradient term is basically computing the mean by sampling from the policy. I don't see how this can provide any value compared to straight MLE / BC where we just use the fact we know the mean because we know the policy.

Of course, one might then ask about the effect of the $\log \sigma$. If one recalls the original MaxEnt IRL / DPO derivations, this term in the loss is meant to ensure closeness to the prior / reference policy. However, the POIL loss does not include any regularization to the prior (i.e. there is no $\pi_{ref}$ in the denominator), so this is at best providing entropy regularization (i.e. bumping up the variance for a Gaussian policy). This could be done without any samples from the policy, which again begs the question of what we're getting out of this more complex procedure compared to BC.

### Questions
1. Could you please add standard error bars to all the plots / tables in the paper?

2. Could you test out your method on something other than the three easiest Mujoco environments?

3. Could you try the "linear" version of the loss I discuss in the weaknesses section? Maybe try tacking on a variance bonus?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes the use of techniques from the preference learning literature for offline imitation learning. The paper utilizes recent techniques from the offline preference-learning literature such as DPO/SPIN/CPO (where the policy's log probability of an action is treated as the reward of the action) and proposes to utilize the combination of a DPO-style loss and a BC loss to prevent overfitting. The authors show surprisingly good results, especially in the low-data regime, where POIL outperforms state-of-the-art model-free offline imitation learning algorithms including IQ-Learn, DMIL, and DICE variants.

### Strengths
The experimental section is very well ablated, with strong performance of the proposed method. I am quite surprised that POIL does well in the low-data regime, especially considering most offline preference learning algorithms are very data hungry in the LLM finetuning context (albeit with larger models come larger dataset necessities). The ablation studies of the proposed method were also pretty exhaustive, where the authors ablated over the impact of the preference temperature parameter and the BC loss they use in practice.

### Weaknesses
There is no explicit theoretical justification in this work, but this is minor to me. I think DPO and its variants have strong theory as is when it comes to solving the KL-regularized RL problem. I feel like with less than 1 expert trajectory (which some offline imitation learning methods look into, albeit with additional suboptimal data) the method fails, but maybe this is not necessary in real-world settings.

I am curious as to whether an RLHF-centric approach to this problem can be good to compare to (e.g. in LLMs there is the PPO w/ RM vs. DPO debate), where one trains a reward model on policy data (low reward) vs expert data (high reward) as the agent trains. In some sense, I feel like this method is similar to DAC, which is outperformed by IQ-Learn anyway, so maybe this is unnecessary.

### Questions
No questions from my perspective for now.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduce a novel algorithm for offline IL, inspired by research from the RLHF literature. The algorithm is quite simple, but demonstrates strong performance against a range of strong baselines.

### Strengths
I see this paper as strong on several fronts. It is clearly written and motivated. There are many references to related work. The method is well-explained. There is a solid set of experiments with good baselines and ablations; as far as I can tell, the experimental setup is sound as well.

The final algorithm presented is relatively simple, and I appreciate that the authors do not try to obfuscate this fact. And yet, its performance is apparently quite strong, which should be of significance to the IL community.

### Weaknesses
The only criticism that I can produce is that it would be nice to know that this method scales to tasks that are more realistic than the MuJoCo benchmark environments, but the authors have already performed a set of experiments that should be considered sound in this particular research topic (fundamental IL algorithms).

Having tried similar approaches in the past, I was surprised that this method worked as well as it did. But, as shown in the authors' ablations, the scaling factor β is crucial, and in general should be significantly < 1. The authors mention "A smaller β value tends to smooth the preference function, which leads to more stable gradients and improved training dynamics", but do not say/show more about this (most results only show the final return); it would be nice to have more exploration of this.

### Questions
- Considering parallels to the LLM literature, I believe that BC is equivalent to supervised fine-tuning (SFT)? An example is in RPO [1]. But it appears that Xu et al. (2024), already cited in the paper, also does this.
- For readers outside of the offline IL literature, how can one determine how long to train for? Are trained policies simply evaluated on the environment, or is it possible to perform some sort of validation?
- As mentioned in the weaknesses, an analysis of how the learned and expert policies change over time could be a good empirical investigation of β's influence on the optimisation process.

[1] Liu, Z., Lu, M., Zhang, S., Liu, B., Guo, H., Yang, Y., ... & Wang, Z. (2024). Provably mitigating overoptimization in rlhf: Your sft loss is implicitly an adversarial regularizer. arXiv preprint arXiv:2405.16436.

### Soundness
3

### Presentation
4

### Contribution
4
