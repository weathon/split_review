# The Distributional Reward Critic Architecture for Reinforcement Learning Under Confusion Matrix Reward Perturbations

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 6, 3

## Abstract
We study reinforcement learning in the presence of an unknown reward perturbation. Existing methodologies for this problem make strong assumptions including reward smoothness, known perturbations, and/or perturbations that do not modify the optimal policy. We study the case of unknown arbitrary perturbations that discretize and shuffle reward space, but have the property that the true reward belongs to the most frequently observed class after perturbation. This class of perturbations generalizes existing classes (and, in the limit, all continuous bounded perturbations) and defeats existing methods. We introduce an adaptive distributional reward critic and show theoretically that it can recover the true rewards under technical conditions. Under the targeted perturbation in discrete and continuous control tasks, we win/tie the highest return in 40/57 settings (compared to 16/57 for the best baseline). Even under the untargeted perturbation, we still win an edge over the baseline designed especially for that setting.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the problem of performing reinforcement learning (RL) when the true rewards have been perturbed. Like previous works, the paper considers problems where the reward function is perturbed in a specific way: the range of the reward function is discretized into equal-width subintervals, which are then perturbed according to a row-stochastic "confusion matrix". In particular, this work assumes that the confusion matrix is mode-preserving in that "true reward is the most frequently observed class after perturbation" (see abstract). Under this condition, a method is proposed that learns a classifier mapping state-action pairs to bins corresponding to observed modes and uses it to recover the true reward. These recovered rewards are then used when training the user's RL algorithm of choice. Versions of the proposed method are provided for (a) when the number of subintervals and reward range is known, (b) when the reward range but not the number of subintervals is known, and (c) when neither is known. The proposed method improves on existing works that either apply only to reward perturbations that preserve the order of the true rewards or require that the true rewards take only finitely many values. Experimental results are provided indicating superior performance over existing methods on a variety of tasks.

### Strengths
The paper addresses an interesting and important problem that is likely of interest to the community. The proposed method generalizes previous work in the area (see summary above) and provides a practical scheme for performing RL with a certain class of perturbed rewards. Though the class of perturbations assumed is potentially restrictive (see weaknesses section below), the method proposed for training a classifier and recovering the true reward is clever and appears to be novel. The experimental evaluation is quite extensive and indicates superior performance to existing methods on the perturbed-reward environments tested.

### Weaknesses
Two important weaknesses of this paper include the following. If these issues can be clarified, it will be easier to more accurately judge the significance of this work.
1. Though the proposed method avoids some of the drawbacks of previous works, such as directly estimating the confusion matrix or the true reward function, or assuming order-preservation of the perturbation, the mode-preserving condition seems quite restrictive. Mode-preserving perturbations are not a generalization of order-preserving perturbations, since the latter may not be order-preserving. Also, methods that learn the confusion matrix may be more widely applicable (though more computationally expensive), since the perturbations can be quite general. Without further motivation of the mode-preserving condition and its advantages over other conditions imposed in the literature, the broader impact of this work is difficult to judge. It is unclear what types of real-world reward perturbation scenarios would satisfy this mode-preserving assumption, and the paper does not provide any concrete examples. For instance, in a scenario where a reward signal is corrupted by sensor noise, it's not immediately obvious that the true reward would be the most frequently observed value after discretization and perturbation. The lack of justification for this assumption makes it difficult to assess the practical relevance of the proposed method.
2. The experimental comparisons are extensive, but there are some issues regarding the fairness of comparisons with previous methods as well as their interpretability. Due to the lack of order-preservation mentioned at the end of the first paragraph of Sec. 5.3, the results in Fig. 5 and 6 may be unfair to the RE method. Comparisons on problems that enjoy conditions to which all methods are applicable would provide a fairer comparison. In addition, though the proposed DRC and GDRC methods show better performance than previous methods on a number of problem instances, they decidedly underperform on many others. Further discussion of this discrepancy is warranted to clarify when the proposed methods should be preferred. For example, it would be helpful to analyze the characteristics of the environments where DRC and GDRC fail, and to provide insights into why these methods are not robust across all tested environments. Finally, the impact of $n_o$ studied in Sec 5.2 is an important issue, but the meaning of Fig. 3 is difficult to interpret. This leaves the question of how to choose $n_r$ open, which is a key component to the applicability of GDRC, in particular.

### Questions
* the proposed method replaces the computational effort of estimating the confusion matrix with the computational cost of training a classifier estimating the bin to which the reward at a given state-action pair belongs; can you comment on how these two costs compare?
* does the classifier trained in line 7 of Alg. 1 -- which is called the "distributional reward critic" -- correspond to any specific action value function, like the standard critics used in actor-critic algorithms? if not, it is a little misleading to call it a critic.
* what is the main difficulty in proving Theorem 1? it seems like it should follow from a straightforward application of the law of large numbers.
* what should the reader take away from Fig. 3? it is currently tough to interpret.
* at the end of the **Algorithms** subsection of Sec. 5.2, it says the rewards are averaged over "10 seeds and 20 random trials"; independent trials are usually each associated with one seed -- can you clarify what you mean?
* in Fig. 6, why do you think DRC's performance improves as noise improves?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors consider the problem of training a reinforcement learning agent under a perturbed reward signal. Similar to Romoff et al. (2018), they propose to learn a reward estimator and then train the agent from the predicted rewards rather than the environment rewards. However, unlike Romoff et al., who strive to learn the expected reward, the authors propose to learn the reward distribution (assuming a categorical distribution), and then train the RL agent from the mode of the predicted distribution. This purportedly allows the approach to handle a broader range of reward perturbations, including those that are not order-preserving.

### Strengths
The idea of predicting the reward via a categorical distribution is novel, and it's an interesting adaptation of ideas from distributional RL. One thing I like about the approach is that, unlike the C51 agent (Bellemare et al., 2017), the number of intervals under GDRC is adaptive. The analysis in Section 5.2 supporting this adaptive approach is very nice. In fact, on the whole, all of the extra analysis that is done beyond the headline results is quite helpful. The authors are upfront about some of the shortcomings of the approach, e.g., the mode collapse problem described at the end of page 8 (where they again include extra, helpful analysis in the Appendix). While the content of the paper is fairly technical, it's mostly well-presented and I think I understood most of the main details. Lastly, I agree that this is an important research area, especially given that finetuning LLMs via RL with human feedback has become such a hot topic recently.

### Weaknesses
One desirable property of any approach to this problem is that it should never decrease performance on tasks where the rewards are *unperturbed*. However, this doesn't hold for the proposed approach. For example, consider a simple betting game where the reward of some bet is -1 with probability 0.9 and +10 with probability 0.1. Romoff et al.'s approach will (in theory) learn that the expected reward is 0.1, and thus the agent will learn that the bet is worth taking. On the other hand, the proposed approach will learn that the mode reward is -1, and hence the agent will learn to avoid the bet. Generalising from this, if we want the approach to be "safe" then it ought to preserve the expected reward.

If we somehow knew that the clean rewards were deterministic and the perturbation was mode-preserving then this would no longer be an issue, but this is a big assumption and it's hard to see how we'd ever know this in a realistic application. For example, human feedback for LLMs arguably is stochastic, not just "perturbed", since different humans have different preferences.  

Less pressing issues:

- The difference between the proposed approach and Romoff et al.'s can be broken into two parts: (1) Learning a categorical estimate, rather than a scalar one; (2) The agent is trained from the mode reward, rather than the mean. I'd like to see a comparison versus an approach that uses (1) but not (2), i.e., the reward distribution is learned, but the agent is trained from the mean of the distribution. This would disengangle how much of the performance impact comes from assuming a categorical distribution and how much comes from assuming that the perturbation is mode-preserving.
- Page 8 states: "The agents in Hopper and Walker2d are encouraged to live longer because of the positive expectation of perturbed rewards". However, this contradicts the statement on page 2 that affine transformations preserve optimal policies. The statement on page 2 should be refined to say that this only holds for non-episodic tasks.
- In my opinion, the proof of Theorem 1 is unnecessary and just overcomplicates the paper. All it really says is "under perfect conditions, the cross entropy loss will go to zero, and hence the approach learns what it's supposed to". We'd have AGI already if he had "sufficiently expressive" neutral networks + unlimited training samples + the necessary compute :p

### Questions
I was slightly confused by the statement on page 3: "we assume that the distribution of the perturbed reward depends only on the true reward, i.e., $\tilde{r}_t \sim \tilde{R}(R(s_t, a_t))$". Couldn't the proposed approach handle state- and action-dependent perturbations too?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies reinforcement learning with perturbed reward, where the reward perceived by the agent is injected with noise. Inspired by previous work, this paper proposes a new form of reward perturbation based on a confusion matrix, which shuffles the rewards of discretized intervals and can preserve local continuity within each interval. Under the mode-preserving assumption, which guarantees the true reward will be observed the most frequently, the paper proposes to learn a classifier to identify the interval index of the true reward when the discretization is known. When the number of intervals or even the reward range is unknown, the paper proposes to use an ensemble or a streaming technique to address the respective unknown parameter. Experimental results on four continuous control tasks show the effectiveness of the proposed techniques.

### Strengths
The strength of the paper is that it provides a comprehensive study of the proposed problem. As stated in the above summary, to address the new form of confusion matrix perturbation, the paper proposes a new algorithm as well as extends the new algorithm to handle scenarios in which some/all parts of the discretization are unknown. In addition, it also provides the guarantee that the correct reward can be predicted asymptotically and the theoretical justification for the voting mechanism of the ensemble approach when the number of intervals is unknown. 

In terms of presentation, the paper is well-written and organized.

### Weaknesses
In my opinion, the major potential weakness of the paper is that it has a restrictive type of perturbation. The paper assumes the rewards in different intervals are shuffled and the true reward is still the most frequently observed (mode-preserving property). However, I find this assumption too artificial and not natural. On the other hand, while the paper claims the assumption of RE (Romoff et al. 2018) to be stringent, I found it to be more natural. I understand the argument that RE can’t properly handle non-order-preserving perturbation. Can you provide more justification for this assumption? Also, how robust would the method be if GCM is not mode-preserving?



### Questions
See Weaknesses for major questions.

Clarification questions or typos that do not impact assessment:
What is SR_W? How is it different from SR?
The reference style is a bit messy and inconsistent throughout the paper.
On page 3, by convention, $\beta : \Delta(S)$ should be $\beta \in \Delta(S)$.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors study RL algorithms under corrupted rewards. By considering the reward distribution and using the discretizing techniques, the confusion matrix can be better estimated by incorporating a reward critic. They also extend their methods to recover the noisy rewards from the known interval and partitions to the unknown one to cater to practical scenarios. Experiments are conducted on a few classical control and Mujoco environments.

### Strengths
* Considering the reward distribution in the corrupted reward setting is natural and well-motivated.

* The paper also studies the unknown interval and partition settings, which is more practical.

### Weaknesses
 * **Potential concept misuse**. The reward is a naturally random variable and considering its distribution in the corrected reward setting is reasonable. However, it does not mean it is strongly correlated with distributional RL, which focuses on the return distribution instead of its expectation: value function.  I agree some density estimation techniques, such as categorical parameterization from C51 paper, can also be used here from distributional RL, but most of the technical issues, including the theoretical parts, between these two scenarios are very different. Emphasizing too much about the so-called distributional reward seems not natural. The core issue is that while the method uses a categorical distribution over rewards, it's not clear that this directly leverages the core concepts of distributional RL, which are about modeling the distribution of returns, not rewards. The connection feels superficial, borrowing techniques without fully engaging with the underlying theory.

* **Inaccurate theoretical statements**. Proposition 1 seems incorrect. Assume r equals $r_{min}$ and it is corrupted to be close to $r_{max}$, which exceeds the upper bound. Also, the proof in Appendix B.1 seems not complete, which I cannot directly follow. Specifically, the proof lacks clear steps and justifications for its claims. Also, Theorem 1 is a descriptive statement without rigorous mathematical statements. The theorem lacks precise mathematical formulations and proofs, making it difficult to assess its validity. Thus, the results are not convincing in a rigorous way. 

* **Limited contribution.** The confusion matrix is also well-studied in robust generative models, based on my knowledge, which can be naturally updated by a (critic) network. Thus, this contribution seems not sufficient. For avenues to cope with the continuous rewards, the discretization method this paper used is a direct application of C51 algorithm via the categorical parameterization. However, it seems the authors did not acknowledge that clearly. In distributional RL, C51 is typically inferior to quantile-based algorithms mainly due to its inability to handle unknown reward range and partitions. As far as I can tell, the paper mainly focuses on the known cases, with only heuristics strategies in the unknown settings. Hence, I can not recognize the sufficient contribution behind it and doubt its practical power. The novelty of using a critic network to estimate a confusion matrix is not clearly established, and the connection to existing methods in robust generative models is not adequately addressed. The reliance on a fixed discretization scheme, similar to C51, without a clear justification for its superiority over quantile-based methods, further weakens the contribution.

* **Technical questions.** I am very confused by selecting the most probable reward label in step 7 of algorithm 1 instead of doing a reweighted sampling from the distribution. Note that if we only choose a single one, the optimal label tends to be deterministic rather than truly learning reward distributions. In the current version, along with the computation of the predicted reward value step, I think it is very similar to just doing the regression instead of a real multi-class classification since the $\arg\max$ does not consider the other probabilities when the reward belongs to other bins. The use of argmax to select a single reward label seems to discard valuable information from the learned distribution, potentially leading to suboptimal performance. This approach effectively reduces the problem to a regression task, undermining the benefits of learning a full reward distribution.
* **Empirical significance** Although the authors claim the empirical performance is desirable, I am afraid I cannot truly agree with that as I find most learning curves are not significantly better than other baselines instead of only making conclusions based on the final return. I may also have a question: although the authors claim that the proposed method can recover the reward better, is this benefit directly related to better performance? More importantly, Atari games are suggested to test the value-based RL algorithms. The empirical results lack a clear demonstration of significant improvement over baselines. The focus on final return values, without a thorough analysis of learning curves, makes it difficult to assess the true effectiveness of the method. Furthermore, the lack of experiments on Atari games, a standard benchmark for value-based RL, raises concerns about the generalizability of the findings.

* **Computation issues.** Learning a confusion matrix mapping is OK in generative models, but learning a reward critic (similarly viewed as a confusion matrix mapping) can be costly in RL as RL algorithms typically lack sample efficiency. Based on this knowledge, determining $n_o$ via the training loss is normally intractable, especially in a large environment with huge state and action spaces. Last but not least, using the training loss is a typical cross-validation strategy, which is straightforward and even trivial for me.

### Questions
Please refer to the weakness part.

### Minors.
* For continuous perturbations, the discretization technique should always induce a reconstruction error, which seems to have conflicts with some statements in the paper.
* The writing can also be improved as there are many grammar errors and typos.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
