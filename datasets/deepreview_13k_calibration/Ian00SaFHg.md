# Efficient Model-Based Reinforcement Learning Through Optimistic Thompson Sampling

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 3, 8, 5

## Abstract
Learning complex robot behavior through interactions with the environment necessitates principled exploration. Effective strategies should prioritize exploring regions of the state-action space that maximize rewards, with optimistic exploration emerging as a promising direction aligned with this idea and enabling sample-efficient reinforcement learning. However, existing methods overlook a crucial aspect: the need for optimism to be informed by a belief connecting the reward and state. To address this, we propose a practical, theoretically grounded approach to optimistic exploration based on Thompson sampling. Our model structure is the first that allows for reasoning about \textit{joint} uncertainty over transitions and rewards. We apply our method on a set of MuJoCo and VMAS continuous control tasks. Our experiments demonstrate that optimistic exploration significantly accelerates learning in environments with sparse rewards, action penalties, and difficult-to-explore regions. Furthermore, we provide insights into when optimism is beneficial and emphasize the critical role of model uncertainty in guiding exploration.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposed Hallucination-based Optimistic Thompson Sampling with Gaussian Processes (HOT-GP),  a method for principled optimistic exploration. It uses a GP with Thompson Sampling as the acquisition function to maintain a joint belief over state and reward distributions, enabling simulating optimistic transitions wrt the estimated reward. Experiments on MuJoCo and VMAS continuous control tasks demonstrate that the proposed approach matches or outperforms baselines, showing substantial improvements in challenging exploration settings. The paper also investigates factors influencing optimism through ablation studies, highlighting the importance of joint uncertainty modelling in guiding effective exploration.

### Strengths
- principled approach for exploration in continuous state-action space
- the first method to predict joint uncertainty over next state and reward

### Weaknesses
 - The description for Fig.2 in Section 6.2, references several methods that are not shown in the plots. For instance,
    - SAC and PPO as described in Line 430, “we use … SAC, and the on-policy PPO”
    - HOT-GP with k-branching (k=5) as described in Line 470.
- Learning curves seem to be from the training episodes. It would be better to report the performance in evaluation episodes instead, as done in SAC.
- The method introduces a crucial hyperparameter reward threshold r_{min}, which controls optimism during exploration. While the results do not seem to be overly sensitive to it, its effect in other tasks remains unclear. Although future work is mentioned to address this, its current implementation could limit its applicability.

### Questions
Could you provide any results on computational cost or computation speed for the proposed method?

### Soundness
2

### Presentation
3

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
This paper introduces a novel model-based reinforcement learning algorithm to explore effectively and improve sample efficiency. The introduced method uses a Gaussian processes to represent a posterior over transition functions and reward functions and models the (linearized) covariance of reward and successor states (the mean functions are later modeled by MLPs instead). The authors introduce an exploration method by modifying Thomposon sampling to be more optimistic: rewards are sampled with the condition of a minimum reward and successive states are taken to be the expected successor state, conditional on the same minimum reward. The authors conducted experiments that analyze the introduced algorithms empirically and show that their agents learns faster in early stages of training.

### Strengths
The paper is written clearly and it is easy to follow. The method adresses an important issue and from what I can see is applicable to a variety of algorithms. The experiments suggest that the proposed algorithm may aid sample efficiency, especially in early stages of training.

### Weaknesses
The main weakness of this paper to me is of conceptual nature. I have no good intuition for why the proposed algorithm performs efficient exploration. This is mainly due to two reasons:

1. I am not convinced the reward-uncertainty is significantly more useful than the dynamics uncertainty. As the authors describe, the de-facto standard way of formulating GPs is that output dimensions are considered independent predictions. The uncertainty of each dimension (the variance of the GP) of a GP conditioned on $X$ in a query-point $x$ is then given by $K(x,x) - K(x,X)K^-1(X,X)K(X,x)$ and depends only on the kernel choice and the data distribution. Unless one has specific knowledge about an appropriate reward-kernel, I have no intution  why the reward offers a better (or different) information gain signal than the dynamics. Specifically, if the reward is a deterministic function of the state, then the reward uncertainty will be entirely determined by the state uncertainty, and thus offer no additional information. The authors should clarify under which conditions the reward uncertainty provides a unique exploration signal.

2. It is unclear to me why the proposed sampling distribution is meaningful. The sampling distribution described in Eq. 8 seems to imply a risk-sensitive sampling strategy without motivating this. For example, one may easily construct MDPs, where optimal trajectories are guaranteed to contain a very small reward. Such trajectories could not be sampled under this strategy, despite being optimal. Mathematically speaking, it is unclear to me what the implications of conditioning on an impossible event is here (i.e., what if $r_t$ can't be greater than $r_{min}$). I can unfortunately not see why one would expect this algorithm to explore reliably. For instance, if the minimum reward is set too high, the algorithm may never explore regions of the state space where rewards are initially low, even if those regions lead to higher cumulative rewards in the long run. The paper lacks a discussion on the sensitivity of the algorithm to the choice of $r_{min}$.


Minor points: 

- The dimensions of the GP definition in line 269 don't seem to add up to me. The covariance matrix, as written here, has dimensions $2 \times 2$, while the mean functions are of dimension $|\mathcal{S}| + 1$. I moreover think the input dimensions of covariance functions $K$ defined in line 271 should operate on pairs of $S\times A$, not simply $S \times A$.

- Expected successor states (as described in 5.2, line 323) don't seem sensible to me. The expectation of a high-dimensional state is not necessarily a meaningful or even existant state. It was moreover not clear to me, how to the model predictions are conditioned on a certain reward level in practice.

- Given that the authors use a GP, I suspect many readers would appreciate a table (or similar) comparing the computational burden of this approach with alternative methods. Furthermore I would be interested to know the effect of subsampling smaller batches (as described in line 850) on the quality of uncertainty estimates with a GP.

### Questions
1. Why do the authors aim to relieve the stationarity assumption in line 285. Since this GP models the transition dynamics of an MDP, the transition kernel should indeed be stationary. Aiming to address non-stationary MDPs, I believe, would entail significant complications for the entire learning algorithm.

2. In most experiments, the asymptotic performance of the shown algorithm seems to be lower than the base-SAC implementation in all of the environments. Is this due to the cutoff in plotting or is the asymptotic performance indeed lower in most environments? Inserting a dashed line as with SAC into the figure might clear this up. 

3. Given that the authors perform k-branching rollouts, the value estimates bootstrapped at the end of model-generated rollouts should play an important role in quantifying uncertainty. Would omitting this uncertainty skew the ability of the algorithm to explore efficiently? It seems unlikely to me, that Thompson sampling maintains it's theoretical guarantees if one only samples single-step transitions around known trajectories. 

My suggestion would be to analyze the implications of the proposed algorithmic components carefully. 
1. What is the implication of performing Thompson sampling with a sampling probability dependent on the expected return of some policy?
2. What is the implication of performing Thompson sampling with a sampling probability dependent on the return and reward distribution of some policy (as suggested here).
3. What is the implication of performing Thompson sampling with limited branched rollouts?

Addressing these questions in my opinion would provide a compelling motivation for the proposed algorithm.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This manuscript introduces HOT-GP, a novel and efficient approach to model-based reinforcement learning that enhances performance through a unique combination of techniques. The core innovation of HOT-GP lies in its ability to learn the joint distribution of dynamics and rewards, paired with an optimistic sampling strategy for "in-model" policy optimization. By leveraging the latest model-based reinforcement learning techniques, HOT-GP selects models for policy optimization based on optimistic sampling, which promotes exploration in high-potential regions of the policy space. Evaluated across several continuous-action benchmarks, HOT-GP demonstrates superior performance compared to both baseline methods and other state-of-the-art algorithms.

### Strengths
1) The use of the joint distribution of dynamics and rewards in the learning process is a clever and impactful approach, offering new perspectives in model-based reinforcement learning.
2) The implementation is robust and well-executed, showcasing attention to both theoretical and practical details.
3) The manuscript is excellently presented—clear, concise, and engaging. It's a pleasure to read and straightforward to follow.
4) The experiments are adequately designed, with thoughtful discussions that provide meaningful insights into the method's strengths and limitations.
5) Providing the code for replicating experiments is greatly appreciated, allowing for easy validation and further exploration by the community.
6) The appendix is comprehensive and well-detailed, giving me confidence that I could implement the method from scratch!

### Weaknesses
1) The evaluation would benefit from more complex scenarios, such as object manipulation or long-horizon tasks, which could further demonstrate the method’s robustness and adaptability.

2) While the integration of a neural network to learn the GP mean is discussed in the main text, I feel like a small paragraph or additional description in the appendix is required. I understand the general approach and can infer the authors' method, but a concise explanation would be a helpful addition for readers.

### Questions
None

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a model-based reinforcement learning algorithm called HOT-GP (Hallucination-based Optimistic Thompson sampling with Gaussian Processes). This approach leverages Gaussian Processes to jointly model the reward and transition dynamics, addressing both state and reward uncertainties. The main goal is to optimize exploration by focusing on high-reward regions in the state-action space. HOT-GP introduces a new optimism-driven Thompson sampling strategy to balance exploration and exploitation, which is particularly useful in environments with sparse rewards or penalties for actions.

### Strengths
The HOT-GP proposed in the paper performs joint uncertainty modeling between rewards and state dynamics. This method innovatively combines the uncertainties in rewards and state transitions, achieving more efficient exploration in environments with sparse rewards and high penalties.

### Weaknesses
1. The experiments are insufficient. For environments with sparse rewards and difficult exploration, tasks like Maze and Navigation, such as Sparse-Point-Robot, might better illustrate the effectiveness of the approach.
2. In some environments, the training curves presented in the paper do not appear to have converged, leaving the convergence of the algorithm unclear and making it difficult to judge whether an optimal policy has been achieved.
3. The paper seems to lack ablation studies on different modules and tasks, which fails to adequately demonstrate the independent contributions of various components to overall performance. Without detailed ablation studies, it becomes challenging to evaluate the individual effects of joint uncertainty modeling and the optimistic strategy across different tasks.

### Questions
According to the paper, the HOT-GP algorithm is inspired by H-UCRL. Why, then, was H-UCRL not used as a comparative algorithm in the MuJoCo tasks?

### Soundness
2

### Presentation
2

### Contribution
2
