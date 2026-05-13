# $q$-exponential family for policy optimization

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Policy optimization methods benefit from a simple and tractable policy parametrization, usually the Gaussian for continuous action spaces. In this paper, we consider a broader policy family  that remains tractable: the $q$-exponential family. 
This family of policies is flexible, allowing the specification of both heavy-tailed policies ($q>1$) and light-tailed policies ($q<1$). This paper examines the interplay between $q$-exponential policies for several actor-critic algorithms conducted on both online and offline problems. We find that heavy-tailed policies are more effective in general and can consistently improve on Gaussian. 
In particular, we find the Student's t-distribution to be more stable than the Gaussian across settings and that a heavy-tailed $q$-Gaussian for Tsallis Advantage Weighted Actor-Critic consistently performs well in offline benchmark problems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on solving reinforcement learning problems with continuous action spaces using policy optimization methods. In such cases, a typical solution for handling continuous action spaces is to impose a probability distribution (specified by finitely many parameters) on the continuous space. A common choice is the Gaussian distribution. The authors propose using a different family of probability distributions: the q-exponential family. Extensive numerical simulations are provided.

### Strengths
The motivation for using the q-exponential family of distributions to encourage exploration seems intuitive. The numerical simulations are quite extensive and successfully demonstrate that it is not always optimal to use a Gaussian distribution to parameterize the policy in reinforcement learning.

### Weaknesses
I suspect that there is an exploration vs. exploitation trade-off in using heavy-tailed probability distributions. Is it possible to design a synthetic example to verify this? Additionally, once this is verified, there might be a way to switch probability distributions during training to balance the exploration-exploitation trade-off, which seems like an interesting direction to investigate.

### Questions
The results are clear and I do not have questions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper conducts an empirical investigation of the use of the q-exponential family of policy parameterizations as an alternative to the commonly used Gaussian for continuous state action spaces in RL for policy optimization. In particular, these policies have been incorporated into existing Actor-Critic algorithms and experiments have been performed to compare the different policies to showcase the improved performance of some of them compared to the Gaussian policy in online and offline settings across several environments.

### Strengths
- To the best of my knowledge, there is no such study in the literature and I believe it is useful for RL in practice. Proposing more alternatives to the Gaussian policy for continuous state action space settings is interesting.  
It would be nice to have the proposed parameterizations and their implementations integrated to existing RL packages to make them readily usable by practitioners. 

- The execution of the study is solid: experiments are methodologically and rigorously conducted, figures are professional and the presentation is pleasant, this effort is much appreciated for a practical paper.

### Weaknesses
 **Main Comments:**

- While the paper provides some insights, in terms of conclusions, it is hard to make a claim to extrapolate the findings beyond the interesting but expected fact that Gaussian policy might not always be the best choice and some other parameterizations might perform better. The paper does perform several experiments but  it is hard to derive actionable practical advice from 4 algorithms x 3 environments regarding which parameterization to be used in general. 
I think the paper could do better to showcase the advantages and shortcomings of each one of the policies, especially to demonstrate the intuitive points mentioned in the introduction regarding each one of them. While the environments tested are standard benchmarks in RL, I think it would be interesting to design and/or consider simple environments with different levels of exploration needed for instance to show the differences between the policies. From the viewpoint of the practitioner, can we come up with a procedure to decide which one to use rather than myopically testing each one of them an decide accordingly? Can we design an index performance of exploration hardness to be exploited? Little can be said regarding this from the paper. Of course, we cannot reasonably be confident to choose the right parameterization since this would highly depend on the setting at hand as the paper shows but even heuristics would be useful. In other (older) ML areas, such procedures seem to be widely used in practice (e.g. for model selection in classification …) 

- Other policy parameterizations than the Gaussian have been investigated in the literature as the paper acknowledges. Some additional relevant related work discussing the use of heavy tailed policies in RL and their benefits: 

Amrit Singh Bedi and Anjaly Parayil and Junyu Zhang and Mengdi Wang and Alec Koppel. ‘On the Sample Complexity and Metastability of Heavy-tailed Policy Search in Continuous Control’, JMLR 2024. 

S. Chakraborty et al., ‘Dealing with Sparse Rewards in Continuous Control Robotics via Heavy-Tailed Policy Optimization’, 2023 IEEE International Conference on Robotics and Automation. 

- The paper could comment about the overhead computational effort (if any) required when going for more ‘sophisticated’ policy parameterizations than the simple Gaussian, notably in terms of sampling mechanism complexity and number of samples requirements, for instance depending on the dimensionality of the problem. Any differences regarding efficiency depending on the dimensionality of the problem? 

- See questions below for clarifications. 

**Minor comments:** 
- l. 122-123: ‘In continuous action spaces, evaluating the log-partition function is generally intractable. Therefore, many researchers consider the Gaussian policy instead.’ I find this sentence a bit confusing. Is Gaussian policy only considered because BG policy cannot be used? In principle, one could consider any policy parameterization. For the continuous setting, it turns out that the Gaussian policy is the one of the simplest one can consider perhaps due to its omnipresence in statistics and parametric estimation as well as its widely available sampling procedure implementations.

### Questions
**Main questions (from the most to the least important):**

- Do all the policy neural networks have a similar number of parameters/weights across experiments for fairness of comparison? 
- Are the implementations mostly readily available in existing RL packages or other libraries that could be directly be used? I see that you provide some of the sampling mechanisms but these seem to be already well known in the statistics literature given their popularity. 
- Is GBMM only valid for 1 < q < 3? 
- l. 41: ‘Heavy-tailed distributions could be more preferable as they are more robust’, what do you mean by robustness here? Can you elaborate more? 
- Can you clarify the difference between the different Data settings in Fig. 8 (Medium-Expert, Medium, Medium-Replay)? 

**Additional questions:**
 
- Any comments about the so-called Lévy alpha-stable distribution? It seems it has been explored in the literature to model the SGD noise. 
See e.g. Simsekli et al. 2019. A Tail-Index Analysis of Stochastic Gradient Noise in Deep Neural Networks. ICML 2019. 
- SAC encourages exploration. Would it be interesting to see if just changing the policy parameterization with a heavy tailed policy would already perform better than SAC? SAC seems to combine two effects: the parameterization of the policy itself and and the regularization to force the policy to be closer to a BG policy (why?)? 
- More of a possible future work direction comment: This work explores in isolation each one of the parameterized policies to showcase the advantages and shortcomings of each one of them and compare them. Can we combine them to get the best of each one of them and have more flexibility like in ensemble methods or bagging approaches in Machine Learning? For instance we might need a very exploratory policy in some settings/regions of the action space or much less once we progress in policy optimization beyond the ability of single distributions to concentrate throughout learning.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In continuous action RL many researches parameterize the policy as a mapping from states to std and mean of a Gaussian from which the actions are sampled.
When also the standard deviation of the Gaussian is learned, the authors argue that phenomenon like instabilities and lack of exploration can occurs. To this end, this paper explores empirically other continuous distribution to use to parameterize policies. In particular, it seems that heavier tails distributions are beneficial in Continuous Online Control experiments such as Acrobot and Cartpole and in Offline MuJoCo experiments.

### Strengths
I think that it is useful to have a paper that clearly states that the Gaussian parameterization might not be the best performing in practice.

### Weaknesses
The paper does not have a clear explanation or conclusive experiment about which parameterization should be used in which cases.
The main take away is that Gaussian parameterization should be avoided but it is not clear with which other distribution it should be replaced.

### Questions
Is it possible to understand which characteristics of the environment makes ine distribution better than the other ?


It would be very useful for the user to get some prior information about which distributions could work well to avoid to search over all the distributions proposed in your work and finding the best performing one.

### Soundness
3

### Presentation
3

### Contribution
2
