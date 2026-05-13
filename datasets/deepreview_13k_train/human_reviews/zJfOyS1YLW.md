# On-Policy Policy Gradient Reinforcement Learning Without On-Policy Sampling

- Decision: Reject
- Scores: 3, 6, 8, 5

## Abstract
On-policy reinforcement learning (\RL{}) algorithms perform policy updates using i.i.d.\@ trajectories collected by the current policy. 
However, after observing only a finite number of trajectories, on-policy sampling may produce data that fails to match the expected on-policy data distribution. 
This \textit{sampling error} leads to noisy updates and data inefficient on-policy learning.
Recent work in the policy evaluation setting has shown that non-i.i.d.\@, off-policy sampling can produce data with lower sampling error than on-policy sampling can produce~\citep{zhong2022robust}.
Motivated by this observation, we introduce an adaptive, off-policy sampling method to improve the data efficiency of on-policy policy gradient algorithms.
Our method, \textbf{P}roximal \textbf{R}obust \textbf{O}n-\textbf{P}olicy \textbf{S}ampling (\PROPS{}), reduces sampling error by collecting data with a \textit{behavior policy} that increases the probability of sampling actions that are under-sampled with respect to the current policy. 
We empirically evaluate \PROPS{} on both continuous-action MuJoCo benchmark tasks as well discrete-action tasks
and demonstrate that (1) \PROPS{} decreases sampling error throughout training and (2) improves the data efficiency of on-policy policy gradient algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper studies the problem that on-policy sampling may have sample error throughout the sampling process. Such sampling errors could be remedied by sampling using a different policy. This paper applied this idea to PPO by remediating the sampling error inside each minibatch. Specifically, this paper divides the minibatch of the PPO into more fine-grained nano batches and adjusts the sampling policy based on sampled nano batches to encourage under-sampled samples. This paper claims their results are better than PPO.

### Strengths
Strengths:
1. Estimating the on-policy gradient requires on-policy samples. Because we do not have access to the true gradient, using the target policy to draw on-policy samples to estimate the true gradient has an estimation error. This error is caused by under-sampled or over-sampled data. Encouraging under-sampled on-policy samples reduces the sampling error and improves gradient estimation. This paper is the first to apply this idea to the PPO algorithm.
2. This paper proposes an algorithm to learn the behavior policy to encourage data in PPO algorithms.

### Weaknesses
Weaknesses:
1. This paper adjusts the batch size of PPO to "1024,2048,4096,8192" which is much larger than the original batch size (64 samples) of PPO. This paper makes this change because they need to learn a behavior policy to encourage under-sampled data at each update step. In other words, they run a mini-PPO to encourage under-sampled data by finding a behavior policy. This drastic increase in batch size is not well-justified. In fact, it is confusing that their PPO algorithm still achieves the comparable performance of the original PPO with at least 16 times less update due to the batch size increase. I am not sure if the original PPO paper has such large room to change the batch size to 16 times larger while achieving the same performance under the same hyperparameters.
2. This paper is not well-written. The length of this paper can be greatly reduced. Currently, this paper has too many unnecessary examples and sentences. The theoretical inside of this paper is also weak. I think a good improvement direction is to discuss the relationship between the sampling error and the number of samples and how this paper can remediate the sampling error from the theoretical perspective. Some new interesting findings might also be discovered during this process.
3. This paper also introduces many fragile hyperparameters. For example, the learning rate for its proposed behavior policy ranges from 10^{-3} to 10^{-5} for an ADAM optimizer. Such a large difference in learning rate is not common for the ADAM optimizer. Moreover, they also require KL cutoff and regularizer coefficient inside the mini-PPO to encourage under-sampled data, which are two more dimensions of hyperparameters. The specific choice of batch sizes for each environment (Swimmer-v4: 4096, HalfCheetah-v4: 1024, Hopper-v4: 2048, Walker2d-v4: 4096, Ant-v4: 1024, Humanoid: 8192) also lacks justification. For instance, the Ant environment, with its 105-dimensional observation space, is arguably more complex than Hopper and Walker, which have observation spaces of 11 and 17 dimensions, respectively. Yet, Ant uses a smaller batch size (1024) than Hopper (2048) and Walker (4096), which is counterintuitive. The lack of a consistent batch size across environments also makes it difficult to assess the generalizability of the proposed method.

### Questions
What is the final choice of the batch size for PPO? Only candidates 1024, 2048, 4096, and 8192 are reported.

### Soundness
2

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
4

### Summary
The authors tackle the problem of sampling errors from insufficient data such that the empirical data has some discrepancy with desired policy. The authors propose a method to adaptively adjust the policy to resolve this discrepancy. They show their method works in several test cases including control and continuous action space.

** Post rebuttal change **
Now that I understood the paper better and following the discussions I have decided to increase my score.

### Strengths
1. The sampling errors problem the authors tackle is interesting, there has not been sufficient discussion on this topic in the RL community. 

2. The presentation and writing is generally clear. 

3. The sampling errors problem can arise in many real-world setups. 

4. The proposes solution is simple in a good way.

### Weaknesses
1. The experiments and motivation the authors provided are not accommodating for the problem. When is this really a problem in the real-world? In most standard examples there is ample time to correct the sampling errors with more data and simulation (this happens with a not a lot of samples in practice). Perhaps in cases of non-stationarity of the system itself this "quicker" adaptation become crucial? or maybe for very large state\action-spaces this is more of a problem. 

I propose the authors will try to distill where they're problem is really important and design experiments correspondingly, or at least motivate more strongly towards these cases.

2. Even in a quick look, Equation (5) can be rewritten much simpler to be -max(g, 1-eps). I'm not sure forcing it to look like PPO helps with insight, but it is confusing and unnecessary. That is, unless you formulate it similarly to the advantage.

3. Some questions were raised for me regarding the soundness of the proposed solution, see in the questions section.

### Questions
1. As a follow-up insight, there may be cases where we can improve the sampling error in one state, but this will cause worse sampling errors down the road because we will be forced to go into specific states. Wouldn't it make more sense to push this sampling error into the reward instead, and form a suitable policy? if you think this is not an issue, it would be helpful if you can explain why.

2. Something doesn't sit right with me regarding equation 6 and its motivation. If we are only aiming to improve the sampling, in the discrete case we wouldn't care about the distance from the target policy. If we are aiming to also improve control, then most algorithms prevent policy changing too much to improve stability in which case we don't need this additional term (for example in PPO). So is this specifically for the continuous case? It does not make a lot of sense to me, at least according to the examples for the discrete case. I would be happy if you could elaborate on this point. 

3. Why did you chose the form given in Equation 5? why not its log or difference? Some explanation, ideally guided by theory would be helpful (it is the importance sampling term, widely used in off-policy learning, so it should make some sense using it in some variation).

### Soundness
2

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
This paper tackles the usual problem of the high-sample complexity of on-policy policy gradient algorithms by refining a very interesting idea proposed by Zhong et al. in 2022. In that paper, the authors observe that when the number of samples is scarce, the samples might resemble the on-policy distribution poorly, which would be equivalent, in a sense, to dealing with an off-policy distribution. In more simple terms, a low number of samples usually cause a high variance policy gradient estimation. 

Zhong et al. observe that on-policy samples do not necessarily need to come from the on-policy distribution; for example, the samples

x_i = 0, 1, 1, 0 

can come from p(x=1) = 0.5 and p(x=0)=0.5, but also from q(x=1) = 0.4 and q(x=0) = 0.6. 
Similarly, a batch of samples that look very off-policy might actually have been generated from the on-policy distribution, for example

x_i = 1, 1, 1, 1, 

might have been generated from the policy $p(x=0) = 0.5$, $p(x=1) = 0.5$. 
Monte-Carlo estimation (i.e., $E[X] \approx 1/n \sum_i X_i$) has higher variance exactly due to the issue described above, when the number of samples $n$ is low, while the variance disappears for $n\to\infty$, making it a consistent estimator.

The variance is the main problem affecting MC estimators and, thus, policy gradient algorithms as well (which are all MC estimators, as they attempt to estimate a respected value using $1/n \sum_i X_i$).

The variance of MC estimators can be ideally reduced if small batches of samples seem to better adhere to the target distribution. This can be achieved by breaking the i.i.d sampling assumption. For example, when the target distribution is $p(x=0) = 0.5$, $p(x=1) = 0.5$, One can choose a deterministic policy that alternates 0s and 1s. Such policy makes the MC estimator strictly more efficient. In this sense, **an off-policy distribution (that violates the i.i.d assumption) can generate better samples "on-policy" samples than the target distribution.**

Zhong et al. in 2022 propose to learn a policy that aims to lower the variance of the policy gradient estimators by generating samples that adhere better to the target policy distribution.

The contribution of this ICLR 2025 paper is to use the idea of Zhong et al. for on-policy policy gradient estimation (and policy improvement), while in the original publication, the idea was only proposed for policy evaluation.

### Strengths
Originality
-------------

The idea proposed is novel. Although the method proposed until page 5 is from Zong's paper, and the application to policy gradient estimation seems somewhat trivial, I think it is still valuable and necessary.

Quality
----------

The quality of the paper is really good. The authors explain the problem and the main idea very well. The method is sounds and directly addresses the problem presented. The experiments are well-designed, explained, and commented on. The results are equipped with good statistical significance, and the appendix reports the hyperparameters necessary for reproducibility. 

Clarity
--------

The paper is well-written, and the overall idea is exposed very clearly.

Significance
-----------------

It is hard to assess the significance of this paper: 1) it heavily relies on a previous publication, and 2) it does not seem that the method improves so much over the baselines. However, I think the core idea is significant as it can serve as a source of inspiration for other RL problems, as MC is a core technique in RL to estimate many different quantities.

### Weaknesses
Contribution
-----------------

The paper's contribution starts on page 5: the author focuses on presenting Zhong et al.'s paper there. The core contribution is the application of Zhon's idea for PG estimation and the use of PPO clipping and KL divergence to prevent too aggressive updates.

While I think it is necessary that the authors devote that space to expose Zhong et al.'s idea, I think that it might not be clear to the reader that **that is not** the main core idea of the paper.

Clarity
--------

While the paper is well written overall, I do not always like the choice of words and how the problem is described. 
I find talking about on-policy "data" vs. "sampling" confusing. A sample is not per se on or off-policy. When we speak about "on-policy" and "off-policy" in estimation, we refer to the generating process (i.e., the distribution) that generates the samples. A sample X_i can be generated by an off-policy distribution $\beta$ and simultaneously very unlikely w.r.t. $\beta$ and very likely w.r.t. the target distribution $\pi$, but that does not make the sample on-policy (or off-policy). Policy gradient estimation is simply off-policy when the distribution that is used to generate the samples is off-policy. 

Pairwise, I find speaking of "empirical policy" as in Proposition 1 confusing. One thing is samples, and one thing is the distribution. What can be told, in general, is that if $n > m$, then $Var[1/n \sum_i^n X_i] < Var[1/m \sum_i^m X_i]$, where X_i are samples coming from the same distribution. Now, it would be possible to introduce a new distribution (as done in Proposition 1), and show that the variance of the batch of samples decreases even faster in $n$, when compared to the original distribution. 

Overall, I am conscious that much of the "nomenclature" is borrowed from Zhong et al., thus the authors might have preferred to keep consistency with that. 

Minor Comments
-----------------------

Equation 1 is unclear as it is written: s_0 comes from a different distribution than s_1, which comes from a different distribution than s_2, and so on. Writing $s \sim d_\pi$ gives the impression that all states are drawn from the same distribution. Usually, there are two ways to express the policy's return,

1. 

$$
J(\theta) = \mathbb{E}_{s \sim d^\gamma_\pi, a \sim \pi}\left[r(s, a)\right]
$$

 where $d^\gamma_\pi$ is the discounted state-action visitation (see Nota and Thomas "Is policy gradient a gradient?" and Sutton et al. "Policy gradient with function approximation")

2. 

$$
J(\theta) = \mathbb{E}\left[\sum_{t=0}^\infty \gamma^t r(s_t, a_t)\right]
$$

where $s_0 \sim d_0, a_t \sim \pi(\cdot | s_t), s_{t+1} \sim p(\cdot | s_t, a_t)$.

Equation 2 and 4, should be with the discounted state visitation (see Nota and Thomas "Is policy gradient a gradient?" and Sutton et al. "Policy gradient with function approximation" :D )


### Questions
I have only one question:

In Zhong et al., the policy is updated at every step in an online fashion: to me, this makes a lot of sense, since we want constantly to "correct" the sampling distribution. Ideally, one wants to employ the method you describe in Proposition 1. 

However, if I understand well, you propose first to use the target policy to collect the samples and, afterward, to generate a policy that "corrects" the previous behavior. However, such a policy is not well defined: it depends on how many samples will be drawn from such a policy. For example, suppose that the target policy is the distribution $\pi(a=0|s) = 0.5$ and $p(a=1|s)=0.5$. Suppose then that the samples drawn from this distribution are:

0, 0, 0, 0, 0.

The policy that you want to learn should then put much more probability density on 1 to compensate, but if we sample hundreds of samples with this new policy, then the dataset will be again "unbalanced". In my understanding, the idea of Zhong et al. to continuously update the policy is to avoid this issue.

Why did you propose this "batch update" rather than an "online update"?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes Proximal Robust On-Policy Sampling (PROPS), an adaptive off-policy sampling method designed to reduce sampling error and improve data efficiency in on-policy policy gradient algorithms. The paper generalizes the adaptive off-policy sampling method ROS introduced in Zhong et al. (2022) by proposing regularization techniques to handle continuous action spaces, and incorporates PROPS into RL training with PPO. Experiments on GridWorld, other discrete-action tasks, and MuJoCo benchmarks compare PPO with PROPS sampling to standard on-policy PPO and a version of PPO that naively reuses recent data without off-policy corrections.

### Strengths
- **[S1] Clear and well-written:** The paper is easy to read. The authors clearly present the interesting idea of on-policy data vs. on-policy sampling, as well as the proposed PROPS algorithm. 
- **[S2] Detailed, transparent presentation of experimental implementation:** The authors do a nice job of clearly describing the implementation details used in the experiments. This includes supporting analysis in the Appendix showing results across hyperparameter values.

### Weaknesses
 **[W1] Lack of novel theoretical analysis**
- While Proposition 1 is valuable because it is not obvious that this sampling procedure converges to the correct state visitation distribution, it is a slight generalization of a result that already appears in Zhong et al. (2022). It is also restricted to finite states and actions, and is based on a different sampling procedure than what is proposed in Section 5. 
- Proposition 1 only analyzes what happens in the limit of infinite data, but the transient behavior is important in the context of policy gradient algorithms where a finite (and often limited) amount of data is collected between each policy update. The analysis does not provide any guarantees on the convergence rate or the sample complexity of the proposed method, which are crucial for assessing its practical utility.
- It seems that there would likely be an important interplay between the size of policy updates, the amount of data to reuse, and the size of behavior policy updates determined by the PROPS objective. Unfortunately, the paper does not perform any analysis to connect these components, and instead sets all hyperparameters using a hyperparameter sweep. This lack of theoretical guidance makes it difficult to understand how these parameters should be tuned in new environments, and how they impact the overall performance of the algorithm. Specifically, there is no theoretical justification for how the PROPS update frequency, the size of the behavior policy update, and the amount of data reuse should be balanced to achieve optimal performance.

**[W2] Experiments do not demonstrate convincing performance benefits**
- The experimental results suggest that PROPS can achieve slightly better sampling error during RL training, but these improvements only lead to marginal performance benefits in continuous control MuJoCo tasks. The reported improvements are not substantial enough to justify the added complexity of the PROPS algorithm, especially considering the computational overhead of maintaining and updating the behavior policy.
- Experiments only compare against PPO and a version of PPO that naively reuses recent data (PPO-Buffer). There have been several works that improve data efficiency in a more principled way than PPO-Buffer that are similar to the goals of this work (see references in lines 122-124), but none of these are considered as baselines. Off-policy RL algorithms are also not included for comparison, which can significantly outperform on-policy or near on-policy methods in some of the tasks considered in this work. The lack of comparison with relevant baselines makes it difficult to assess the true value of PROPS.
- Due to the regularization needed for stable performance, PROPS requires the behavior policy to remain close to the current policy (small $\delta_{\textnormal{PROPS}}$). The experimental results suggest that this prevents PROPS from reusing a significant amount of past data (as mentioned in lines 470-471 and 1181-1183), limiting the data efficiency that can be achieved. This limitation undermines the core motivation of the paper, which is to improve data efficiency by reusing past data.

**[W3] Contribution is not clear relative to existing methods:** The paper does not clearly position its contribution relative to existing RL methods that also address data or computational efficiency. See [Q1] below.

### Questions
**[Q1]** What do the authors believe are the main benefits of PROPS relative to existing methods that address data or computational efficiency, including: 
- Methods that reuse data by making off-policy corrections (references in lines 122-124): These algorithms appear to be the most similar to PROPS, and some of them introduce similar levels of added complexity / runtime when compared to on-policy algorithms. However, they are not compared against in the experiments.
- Off-policy RL algorithms: These methods have been shown to be extremely data efficient and can even be used to train complex tasks directly from real-world data (e.g., [1]). They have also been shown to significantly outperform on-policy methods on some of the MuJoCo tasks used in this paper.
- Massively parallel on-policy implementations: When a simulator is available, it has been shown that massively parallel implementations of on-policy algorithms such as PPO can result in very efficient RL training in terms of wall-clock time (e.g., [2]). 

**[Q2] Experiments**
- The use of different hyperparameter values across each algorithm makes the comparison of PROPS and PPO difficult to interpret. I appreciate the value in the best vs. best comparisons presented in the paper, but how does PROPS perform when using the same hyperparameter values as PPO (and only tunes the PROPS-specific hyperparameters)?
- It is not obvious to me that reducing sampling error will necessarily lead to improved performance. Given the non-convex objective of policy gradient methods, noisy updates could even be helpful to avoid / escape local optima. Did you perform any experimental analysis on this connection (e.g., comparing PPO for the same number of total updates but varying batch sizes)? A comparison of PPO and PROPS for $b=1$ (with the same PPO hyperparameters) would also provide some insight into this question.
- It seems that “on-policy sampling” refers to PPO-Buffer in the sampling error figures, which does not seem like a fair comparison because PPO-Buffer does not attempt to correct for the use of off-policy data at all. What is the sampling error of standard on-policy PPO (and how does it compare to PROPS for $b=1$ with the same PPO hyperparameters)? Are similar trends observed?

**Minor:**
- In (1), the combination of an expectation over the visitation distribution and a summation over time inside the expectation is a bit strange. When summing over time inside the expectation, the expectation is typically written w.r.t. trajectories rather than the visitation distribution.
- Equation (5) can be written more directly as $\min(-\pi_{\phi} / \pi_{\theta}, -(1-\epsilon_{\textnormal{PROPS}}))$. The more complicated structure currently being used is needed in PPO’s objective because advantages can be positive or negative, but this is not relevant in (5).
- Why is IQM used as the performance metric? Typically the mean return is reported.
- Typos: line 341: Samping -> Sampling, line 485: Figure 5b -> Figure 3b
- Some of the legends appear inconsistent with other figures (Figure 12) / with the figure caption (Figure 15)

---

**References:**

[1] Smith et al. Demonstrating a Walk in the Park: Learning to Walk in 20 Minutes With Model-Free Reinforcement Learning. In RSS 2023.

[2] Rudin et al. Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning. In CoRL 2022.

### Soundness
3

### Presentation
3

### Contribution
2
