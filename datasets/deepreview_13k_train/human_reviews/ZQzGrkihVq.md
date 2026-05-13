# HAL: Harmonic Learning in High-Dimensional MDPs

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
Since the initial successes of deep reinforcement learning on learning policies purely by interacting with complex high-dimensional state representations and a decade of extensive research, deep neural policies have been applied to a striking variety of fields ranging from pharmaceuticals to foundation models. Yet, one of the strongest assumptions of reinforcement learning is to expect to receive a reward signal from the MDP. While this assumption comes in handy in certain fields, i.e. automated financial markets, it does not naturally fit in many others where the computational complexity of providing such a signal for the task at hand is larger than in fact learning one. Thus, in this paper we focus on learning policies in MDPs without this assumption, and study sequential decision making without having access to information on rewards provided by the MDP. We introduce We introduce harmonic learning, a training method in high-dimensional MDPs, and provide a theoretically well-founded algorithm that significantly improves the sample complexity of deep neural policies. The theoretical and empirical analysis reported in our paper demonstrates that harmonic learning achieves substantial improvements in sample efficient training while constructing more stable and resilient policies that can generalize to uncertain environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes an algorithm for the forward and inverse problem, similar in spirit to RLSVI, that enjoys [deep] adversarial robustness.

### Strengths
This paper explores a novel and interesting idea (to the best of my knowledge) and develops it fairly well. The writing is clear and the proofs are there. There are a few weaknesses but they should be easy to address.

### Weaknesses
There are a few methodological weaknesses, 
- DQN was used instead of rainbow (or any of the more recent SOTA),
- The reward curve was not included for both methods. Given that this paper claims to be much more sample efficient in practice, more effort (put into tuning) is necessary. 
- The setting of the experiment is a weird mix between on-policy and off-policy, where they sample trajectories at every epoch but from the expert policy. Usually, a dataset of expert trajectories is given.
- IQL uses regularized values and has a policy that is proportional to the softmax of the estimated Q function. Since the trajectories were generated from a Q learning-based algorithm (a degenerate expert) and the temperature for IQL was relatively high ($	au=0.1$, Munchausen uses 0.03, SQL uses an even smaller amount if used with the auto temperature algo or its default value, IQL uses 0.01), It's not surprising that IQL's values are neither accurate nor that it struggles with learning a performant policy. A fairer benchmark would have also compared the result with the output of an algorithm like SQL or Munchausen or actual human data. This is also relevant for 4.2, the soft algorithm may have to overestimate Q to get the right policy. From personal experience, temperature is particularly important in games like pong.
- The results of section 4.1, robustness to the exact perturbation model, are somehow, not meaningful. It's not surprising that the model trained to be robust to noise is robust to the exact kind of noise it was trained on.
- This paper includes citations to Korkmaz 2022, 2023, 2024, and Korkmaz & Brown-Cohen 2023. Unfortunately, it misses critical citations to Korkmaz 2020, 2021a, 2021b.
The introduction presents more adversarial definitions of robustness, which are not tested here (think FSGM or Korkmaz 2020).
The paper would have benefited from more experiments in a variety of environments. ALE has 50-something games; five are used here, and in some of the experiments, only one is used. Mujoco would have also been a more computationally economical alternative.
- This method does not seem to be applicable in environments where the observation space is discrete.
- The networks used are not particularly big by 2024 standards. (I think).
- The authors forgot to include the code for training in Appendix 2 (it only samples actions).

### Questions
- Would it be possible to add a proof (or reference) for 231, For instance, it's unclear how the basis needs to be sampled to ensure that the distribution of possible values has full support like RLSVI. The code in Appendix 2, for instance, does not have this property.
- 253: is the assumption that the weighted gap between the value of the best and second best action is greater than epsilon reasonable? In many MDPs (especially discounted ones), many actions have the same value (think moving up or right on a grid to reach the top right corner).
- 265, I believe that 3 should be max, not argmax.
- 432, Can you please include the average discounted reward?
- 432, Given that the MDP is finite horizon, and that IQL has a high temperature, does $E[\text{max}_a Q(s, a)]$ mean anything?
- 447, what does DCT stand for?
- Should Osband, Ian, Benjamin Van Roy, and Zheng Wen. "Generalization and exploration via randomized value functions." be cited for RLSVI?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new inverse reinforcement learning algorithm, termed harmonic learning, which estimates approximate Q-values without the need for reward signals. The core idea of harmonic learning is to decompose the MDP into basises and inject uncertainty into value estimation by eliminating specific components along a random basis. The authors validate their approach through a series of numerical experiments, comparing the harmonic learning algorithm with inverse Q-learning in terms of performance, sample efficiency, and robustness.

### Strengths
The harmonic learning algorithm introduces a unique approach within the inverse reinforcement learning domain, particularly for MDPs with general function approximation. The experimental results support the robustness and sample efficiency of harmonic learning compared to inverse Q-learning.

### Weaknesses
The experimental evaluation only includes a comparison with inverse Q-learning, lacking other standard benchmarks. Including additional benchmarks, such as Generative Adversarial Imitation Learning (GAIL) or Adversarial Inverse Reinforcement Learning (AIRL), would help position the proposed algorithm within the broader IRL landscape and offer a more comprehensive evaluation.

The authors introduce a novel robustness measure, referred to as SBRA, to evaluate RL policy robustness. While the intuition and process behind SBRA are described, its effectiveness as a robustness metric appears inadequately supported. The current evidence, including Figure 2, does not provide sufficient support for SBRA as a reliable or comprehensive robustness measure. The justification for SBRA's validity seems circular; the authors use SBRA to demonstrate the robustness of harmonic learning and then use this result to argue for SBRA's validity, without independent validation of SBRA itself.

Following the previous question, the results from SBRA seem inconsistent with the other two robustness measures in Figure 5. For example, while the other two measures illustrate that harmonic learning is more robust in almost every case, in SBRA, there are certain scenarios in which inverse Q-learning is better.

The algorithm seems to fall under the category of inverse reinforcement learning, but the authors avoid this term in both the abstract and introduction. Is there a specific reason for this choice?

How does the algorithm handle computational complexity as the state dimension d increases?

### Questions
1) See above, given the empirical nature of the paper, algorithm evaluation is largely based on experimental comparisons. Why was inverse Q-learning selected as the only comparison benchmark? It is recommended that the authors give a stronger justification or provide additional experiments. 
2) The authors introduce a novel robustness measure, referred to as SBRA, to evaluate RL policy robustness. While the intuition and process behind SBRA are described, its effectiveness as a robustness metric appears inadequately supported. The current evidence, including Figure 2, does not provide sufficient support for SBRA as a reliable or comprehensive robustness measure. 
3) Following the previous question, the results from SBRA seem inconsistent with the other two robustness measures in Figure 5. For example, while the other two measures illustrate that harmonic learning is more robust in almost every case, in SBRA, there are certain scenarios in which inverse Q-learning is better. 
4) The algorithm seems to fall under the category of inverse reinforcement learning, but the authors avoid this term in both the abstract and introduction. Is there a specific reason for this choice? 
5) How does the algorithm handle computational complexity as the state dimension d increases?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Authors introduce a framework that can learn robust value functions from expert demonstrations. The central methodological contribution is that they sample from a perturbed distribution of features for a featurized Markov decision process (MDP). The prime use case here is perturbed features from a neural Q function where the perturbation vectors are sampled from a Gaussian which has covariance that is the inverse of the dominant feature vectors in the data. They lay foundational arguments using Lemmas that show approximation of a policy, in return, under perturbation. They also show empirical results for various Atari environments.

### Strengths
I observe the following strengths:
1. The authors explain the idea of noisy features very well.
2. The results seem promising in terms of the performance from the samples.
3. They take several different approaches to study robustness.

### Weaknesses
Overall the authors can do a better job at making a case for harmonic learning by explaining their experiments and algorithm better, and increasing the number of domains they test their method on. Further, the writing could also be better (see minor issues below). I see the following three major issues.

**How is the epsilon-stable basis different from radial basis functions [1]?** While I see the obvious distinction that you define and learn a $\kappa$-dimensional basis for the $Q$ function in the $\kappa$-dimensional features, I believe that your formulation of the $\epsilon$-stable basis has similairites to a the scalar basis, with variable dimensionality weighted by the boltzmann distribution, provided by Asadi et al. I would also look at work on using Fourier bases for value functions [2]. As you have noted (lines 289-293) it is a natural choice. I acknowledge that you are using this fact to remove components in the Fourier basis but a comparison to other methods that use bases is warranted in my opinion.

**Issue with connecting robustness to their work empirically:** while the authors allude to the robustness of their method I am unclear as to what is the robustness with respect to? I would expect them to explain how Korkzman, 2024 measure natural robustness (line 314-315). While the authors do describe a measure for "impact on the policy performance" (line 382) I am not sure if this is the same as natural robustness. They also plot the score $\mathcal I$ wrt $\delta$ but I do not see an explaination as to what $\delta$ is and how it is connected to the frequency of the Fourier basis. I have a guess based on algorithm 3 but I would expect it to be explained in detail as it is central to the authors' work.

In Section 4.2 they measure robustness wrt over-fitting on the data. I am unclear as to what the x-axis is in Figure 4. While there is a mismatch between the obtained return and predicted return I do to fully understand how this demonstrates that the policy (derived from $\max_a Q(s,a)$) is overfitting to the data? There is a difference between the error  between true value and estimated value, and the choice of best action based on the application of $\max_a Q(s,a)$. I believe overfitting in this setting should be viewed using the latter sense.

**Issues with time variance vs time invariance:** up until section 3 you use time variant notation for $Q$ function and parameters, then in section 3.1 and later you drop this notation. This gives me the impression that you are switching the setting. I hope they can clarify this. It surfaces again in line 284 of algorithm 2 but then it is nowhere in rest of the algorithm. This can be confusing for the reader.


-----------

### Questions
**Minor issues and questions:**

Line 54: "fewer interactions" -> what does it mean?

Line 48: "non-robust directions" seems a bit vague here. Please define it or explain it better.

Line 57: What do you mean by "non-robust environments"?

Line 89: Q function is associated with a policy but you seem to define it as "the expected cumulative discounted rewards obtained if the action a is taken in state s". What happens after action a is taken at state s? Ideally you follow the corresponding policy.

Line 91: in RL value function is also defined with respect to a policy not as a max over actions of a q-function.

Line 95: add a full stop, the equation is not very well explained. What is the gradient update used for? What is the $\nabla$ there?

Line 100: undefined $\mathcal S_{\rho}$ ?

Line 105: what is a "functioning policy"? Then you shift to "expert policy"? Line 113 as well.

Line 111: You are changing the definition of the reward function. This is confusing for me without clarification.

Line 151: why are you changing the definition of an MDP here?

Line 147-48: cite Osband et al for RLSVI

Line 170: "This has the effect of directly injecting uncertainty into value estimates proportional to a natural posterior distribution on the parameters" What does it mean? What is the posterior here? What is the prior?

Line 175: I would write it as the scalar has distribution equal to the normal distribution

Line 178: . "In the general function approximation setting, e.g. when using deep neural networks, it is no longer possible to directly compute the correct noise level to perturb the value estimates via an inversion of the feature covariance matrix" -> why is this so?

Line 196: Could you please add some background on "uncertainty principle in harmonic analysis" in the appendix.

Definition 3.1: You are using the index i from above (see Eq 1) but they seem to be indexing different objects.

Algorithm 2: what is $s^{spc}$ and how is it used in the training of the $Q$-functions? Is this the Fourier component you remove from the observations?

Algorithm 2: What is the notation $[x:y,z]$ here? Is this numpy array slicing? This is not very common in pseudo-code so the reader might benefit from an explanation.

Algoirthm 2: Do you expect access to the "Occupancy measure of the expert policy" or samples from it?

Line 372: volatilities in decision making -> volatility in decision making

Line 393: You claim "there is a high increase in the sensitivities towards lower frequencies" but I see a high increse in sensitivity for both low and high frequencies.

Line 463-463: Please provide citation(s) for "recent work connected the relationship between adversarial robustness and natural robustness"

Table 2: Is this reward or is it the return (which is cumulative reward over time steps)? I would be surprised if you were obtaining a single step reward was this large. Why are the scales of the estimated Q function and the return so different?

Line 431: What are $e(s), \epsilon(e)$ here?

Line 464: The phrases in "natural robustness in a given MDP in terms of the damage caused by these natural directions" seems vague to me.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies robust policy learning in high-dimensional MDPs without access to reward signals. To handle robustness, the authors introduce a new method called harmonic learning, which generalizes the idea of randomized least-squares value iteration and extends to general function approximation scenarios. The authors further explain the theoretical intuition for harmonic learning and provide some experimental results to show the efficiency of the proposed harmonic learning algorithm.

### Strengths
(1) The authors explain clearly the relationship between randomized least-squares value iteration (RLSVI) and their randomized elimination of basis functions, it is easy to follow this generalization with the concept of uncertainty.

(2) The random basis function elimination inspired by harmonic analysis is interesting. The newly defined uncertainty metric makes sense to me.

### Weaknesses
(1) From my point of view, the main contribution of this paper is to introduce a new uncertainty metric and use it in harmonic learning algorithms. However, in the abstract, the authors spend quite a lot of space discussing reward information, which may distract readers' attention (It seems that this paper doesn't adopt new methods to handle no reward signals? Please correct me if I am wrong). In addition, when the authors claim: "provide a theoretically well-founded algorithm that significantly improves the sample complexity of deep neural policies." Readers usually expect the paper to provide some sample complexity bounds, but this paper only provides experimental results to show sample efficiency. The authors may reorganize the abstract and presentation.

(2) For the key algorithm 2: HAL: Harmonic Learning, I think it is worthwhile to explain the main steps in detail. For example, like line 277, the authors mention it is the discrete Fourier transform of the state s in section 4.1, but what is $m,n$ and $s(m,n)$? (I guess it is something like grids to discretize $s$, maybe the author can explain this in detail.) The description of how the Fourier basis is actually implemented and used in the algorithm is lacking, making it difficult to reproduce the results or fully understand the method's practical aspects. Specifically, the paper needs to clarify how the discrete Fourier transform is applied to the state space, especially when the state space is continuous or high-dimensional. The paper should also discuss the choice of the grid size and its impact on the performance of the algorithm.

(3) This paper is based on the key notion of $\epsilon$-Stable Basis for both linear MDPs and general function approximation. A natural question directly comes to me is the existence of such $\epsilon$-Stable Basis. As it requires all $s,a$ to hold for the inequality, it is not trivial. I suggest the author may have more discussions about this such as providing some proofs. Maybe some smoothness assumptions over rewards are required. The paper adopts the Fourier basis in experiments, maybe the authors can show the Fourier basis satisfy the inequality. The paper should provide a more rigorous justification for the existence of such a basis, especially in the context of general function approximation. It is not clear under what conditions such a basis can be found, and the paper should discuss the limitations of this assumption. For example, are there specific classes of MDPs or function approximators for which an $\epsilon$-stable basis can be guaranteed?

### Questions
Please see above.

One more question: the theorems in section 3 hold for real $Q$ function, will similar results hold for estimated $Q$ function? I understand this is not easy to understand and make it clear during rebuttal. The authors can only provide some high-level explanation to me. 

Also, the idea in this paper to define uncertainty is interesting to me and I am open to raising my scores if my concerns are solved.

### Soundness
3

### Presentation
2

### Contribution
3
