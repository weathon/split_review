# Vlearn: Off-Policy Learning with Efficient State-Value Function Estimation

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 6

## Abstract
Existing off-policy reinforcement learning algorithms often rely on an explicit state-action-value function representation, which can be problematic in high-dimensional action spaces due to the curse of dimensionality.
This reliance results in data inefficiency as maintaining a state-action-value function in such spaces is challenging. 
We present an efficient approach that utilizes only a state-value function as the critic for off-policy deep reinforcement learning.
This approach, which we refer to as Vlearn, effectively circumvents the limitations of existing methods by eliminating the necessity for an explicit state-action-value function. 
To this end, we introduce a novel importance sampling loss for learning deep value functions from off-policy data. 
While this is common for linear methods, it has not been combined with deep value function networks. 
This transfer to deep methods is not straightforward and requires novel design choices such as robust policy updates, twin value function networks to avoid an optimization bias, and importance weight clipping.
We also present a novel analysis of the variance of our estimate compared to commonly used importance sampling estimators such as V-trace. 
Our approach improves sample complexity as well as final performance and ensures consistent and robust performance across various benchmark tasks.
Eliminating the state-action-value function in Vlearn facilitates a streamlined learning process, enabling more effective exploration and exploitation in complex environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel off-policy actor-critic reinforcement learning method called Vlearn that only learns a state-value function for advantage estimation to mitigate the curse of dimensionality in tasks with large action spaces. The algorithm is based on a state-value function loss upper bound of one that multiplies the importance sampling ratio with the Bellman target. Vlearn leverages an experience replay memory for data efficiency and employs delayed update, double-Q-learning-like training, importance sampling ratio truncation, and trust region optimization for stability.

The experiments done on the Gymnasium and DMC environments demonstrate a competitive performance of Vlearn on most of the continuous control tasks. Vlearn exhibits an impressive performance on the DMC dog tasks that previous methods struggled to learn. The empirical study concludes with an ablation study on the effect of the size of the replay buffer on the algorithm.

### Strengths
- The motivation for this work is easy to understand. The authors straightforwardly introduce the problem they are trying to solve and explain why it is important.
- The background material is abundant and comprehensive, crediting the proper related works.
- The experiments demonstrate the strength of VLearn in high-dimensional action space tasks compared to a fair selection of competitors.

### Weaknesses
 - The derivation skips directly to the final equation, not providing enough detail. It's also possibly erroneous. Please see the question section.
- Some equations and parts of the pseudocode are difficult to understand due to poor explanation of the notations. I will point out some examples in the question section.
- The ablation study only investigates the effect of the size of the replay buffer. However, Vlearn uses multiple techniques from previous works, e.g., importance sampling ratio truncation. Each of them may contribute to the reported final performance. A more comprehensive ablation study can definitely enhance the value of this work.

### Questions
- I tried to justify how the authors arrived at equation 4 from equation 2 using Jensen's inequality but failed. I hope the authors can explain how Jensen's inequality is applied here. The importance sampling ratios do not necessarily sum to one. Thus, the inequality may not hold.
- Some notations are used before definition. For example, I was unsure what $K$ represents until I got to the pseudocode to find out it was the mini-batch size.
- The pseudocode is somewhat vague. For instance, does the for $ i \in \\{1,2\\}$ indicate a for-loop or a random sample from the set in lines 9 and 13? What does $\theta$ in line 11 represent? It's not in the input to the algorithm.
- What is the motivation behind using two sets of parameters for the state-value function? The overestimation bias exists in Q-learning. I don't think it exists in the authors' formulation.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides an off-policy trust region method that using only V to learn the optimal policy. In details, this paper proposes some modification (an uppper bound learning objective) to V-trace, and learns the policy by TRPL. Vlearn is claimed to bring more efficient exploration and exploitation in complex tasks with high-dimensional action spaces. This paper tests Vlearn on both Gymnasium and DMC dog tasks, Vlearn achieves strong results across all tasks, especially on 38-dimensional dog tasks.

### Strengths
- Empirical results are strong, Vlearn achieves strong results on high-dimensional gym tasks and DMC dog tasks.
- Vlearn extends ppo (or TRPL) to off-policy methods, which is of good significance.

### Weaknesses
 - Why does the learning objective in Vlearn work better than 1-step V-trace is still not clear to me. Despite the empirical results, it will be more sound if the author could give some (theoritical) analysis to it. Specifically, the paper lacks a clear explanation of how the modified objective function, which appears to decouple the importance sampling ratio from the squared error term, inherently leads to better learning. The intuition behind why this decoupling is beneficial, compared to the standard V-trace formulation, is not sufficiently explored. The paper should provide a more rigorous justification, possibly through a variance analysis or by relating it to known properties of policy optimization.
- Although Vlearn only needs to learn V so as to bypass the problem in explicitly learning Q function representation, it seems will bring the  problem to the estimate of $\frac{\pi(a|s)}{\pi_b(a|s)}$ if the action space is high-dimensional. The paper does not adequately address the potential instability or high variance that could arise from estimating the importance sampling ratio in high-dimensional action spaces. While the policy is learned using TRPL, which imposes a constraint on policy updates, it's not clear how this mitigates the issue of potentially vanishing or exploding importance ratios. A more thorough discussion of the practical challenges and solutions for estimating these ratios in high-dimensional spaces is needed.
- Empirical results on easy, low-dimension task such as hopper, walker, cheetah are low. The paper's performance on standard low-dimensional benchmark tasks is not competitive, and this raises questions about the method's general applicability. While the authors emphasize the method's strength in high-dimensional tasks, the lack of strong performance on simpler tasks suggests that it may not be universally superior and might have limitations in certain scenarios. It would be beneficial to understand what causes this performance gap, and if there are specific conditions where Vlearn is expected to underperform.

### Questions
see weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new objective to estimate the state value function in off-policy setting. The new objective modifies the importance-weighted value iteration objective by a) moving the importance weights to the outside of the squared loss and b) subsuming the per-action weights to the summation over the time horizon. This state value estimation method is then combined with many other RL practice, including using the target network, applying trust region constraint, truncating the importance ratios etc, to form a new algorithm. The paper empirically evaluates this new algorithm in control tasks.

### Strengths
The paper is well written, with a clear statement of the research question. The related work also summarizes well the on-policy and off-policy methods. The use of a trust-region method to stabilize the training and the policy update is also convincing and turns out be to working well in empirical experiments.

### Weaknesses
### Clarity & quality
**Important details on the value loss function are missing and unclear**: 

The main contribution of this is the use of a surrogate objective for the value function learning. However, the deduction of this new surrogate objective lacks important explanations. 
1. “accomplish this by relaxing the squared loss function from Equation 2 using Jensen’s inequality”. It is not straightforward to me how to use Jensen’s inequality to obtain $L(	heta)$. Why we can move the ratios just outside of the square? Specifically, the Jensen's inequality is typically applied to a convex function of a random variable, not to an expectation of a squared term involving random variables. The paper needs to specify how the expectation is constructed to allow for this manipulation. It is unclear what random variable is being considered, and how the expectation is taken such that Jensen's inequality can be applied to move the importance weights outside of the square. The lack of clarity here makes it difficult to assess the validity of the derivation.
2.  In Equation (4), the paper just subsumes the summation over $j$ into the sum over $t$. I’m not sure quite how this can be done, given that the summation over $j$ “implicitly assumes multiple action executions per state”. But the $L(	heta)$ in Equation (4) clearly does not have such implicit assumption. Further, in the subsequent sections, there is no discussion on this, and Algorithm 1 just presents a single-action estimate for the loss. This step needs more justification, as it appears to be a significant simplification that may not be valid in all cases. The paper needs to clarify how this subsumption is valid and what assumptions are needed to make it hold. It is not clear if this subsumption is only an approximation or if it is a precise mathematical step.

### Significance
**Some conclusions and statements may need to be further justified**
1. **the conclusion from the cited work may not carry over straightaway to the value estimation in this paper**. Specifically, “the new loss function is an upper bound of the original loss function and shares the same optima”. However, in the cited work (Neumann & Peters, 2008), the proof is for the value estimation of $\pi$ with a given Q and samples generated by the same policy (if I understand correctly). This is different from objective function in Equation (4), which is estimated using target networks and the off-policy samples.  Can the authors provide a theoretical proof for this convergence to the same optima? Also, regarding “solving the relaxed loss should yield results consistent with the original loss”, does it mean that the final loss will be consistent? Or the final policy will be the same? The paper needs to clarify what is meant by “consistent” in this context, and provide a theoretical justification for the claim that the relaxed loss leads to the same optima, especially given the off-policy nature of the estimation and the use of target networks.

2. **It is unclear how the proposed state-value-estimation can be useful for the algorithm**: Particularly, the proposed algorithm is a combination of the multiple independent ideas: state value estimation, target networks, trust region projection, Gaussian policy approximation, replay buffer and importance weight truncation. Any of these ideas can be crucial and contributive for the strong empirical performance. It would be hard to detach the state value estimation from the other components and claim that the proposed state value estimation is the key. The paper needs to provide more evidence that the proposed state-value estimation is the key contributor to the empirical performance, possibly through ablation studies that isolate the effect of this component.
  
3. **Further empirical studies are needed to verify the proposed idea**: the main empirical results only show the evaluation reward/returns for the trained policies. They are insufficient to show if the proposed value estimation objective can be better in learning an accurate value estimate. Particular, those strong performance of Vlean can be (very likely) a result from other implementation tricks. The paper should consider using Monte Carlo estimate to compare the estimated values with Vlean and the groundtruth values. Moreover, the ablation studies on the replay buffer size are irrelevant to the main idea of the proposed value estimate and should be substituted with a more informative study, e.g., with/without the ratios when optimization $L(	heta)$. The current ablation studies give no clue on the state-value-function estimation.

### Questions
1. The paper states that “we aim to reduce the variance by replacing the standard importance sampling ratio with truncated importance sampling”. But Algorithm 1 has no such ratio clipping 

Some language issues (those do not affect my assessment): 
1. “This loss from Equation 5 can be optimized” Equation 5 is not a loss, but an objective to maximize.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Valued-based RL typically aims to learn the Q-function ("action value function"), which maps state-action pair to a Q-value. The complexity of this approach doesn't scale well with high-dimensional action space. Instead, this work proposes to learn the V-function ("state value function"). There's a some description of the mathematical foundation for the proposed loss function and algorithm. 

Experiments were conducted on continuous control tasks including gym (mujoco) and DeepMind control suite.

### Strengths
- Strong empirical performance in the experiments, especially compared to V-trace, which shares a similar mathematical formulation as the proposed approach Vlearn.

### Weaknesses
 - Lack of mathematical rigor in the algorithm description (see questions below)
- An important connection to a particular piece of prior work seems to be obscured in the paper as written

- Issues with mathematical notation
  - In eqn (2) and the eqn right above eqn (4): what is $j$, what is the sum over $j$, and what is $K$? Below eqn (2), the text says "$a_{t,j}$ defines the $j$th action in state $s_t$". Does this mean $j$ is enumerating the collected transitions (presumably in a buffer)? Or is this following some other distribution - what distribution would that be? The notation is particularly confusing because $K$ is used later as a batch size, which is not necessarily related to the number of actions being considered in this context.
  - In eqn (4), since you are no longer summing over $j$, do you still need $\frac{1}{K}$? It's unclear why the batch size $K$ is still in the equation, given that the summation over actions has been removed. This makes the connection between the two equations less clear.
  - Right above eqn (3), could you clarify what "upper bound" and "lower bound" this sentence is referring to, and why "truncated importance weights can provide an upper bound"? The text mentions that the truncated importance weights provide an upper bound, but it does not specify what quantity is being bounded. This makes the claim difficult to verify.
- The introduction mentions "upper bounds of actual Bellman error" - I assume this is referring to eqn (4) - however it was not explicitly stated around eqn (4). It's unclear how the bound in equation (4) relates to the Bellman error, and this connection should be made explicit.
  - How was Jensen's inequality used to derive eqn (4) from eqn (2)? Could walk through this explicitly. The paper needs to provide a step-by-step derivation, showing how Jensen's inequality is applied to move from the expectation over actions inside the square to outside the square.
- Connection to Mahmood et al. 2014
  - In that referenced paper, the authors considered linear function approx setting and presented two importance sampling approaches for off-policy learning.
  - What they call OIS-LS and WIS-LS seems to correspond to the difference between eqn (2) vs eqn (4). Specifically, their WIS-LS objective is $J(\theta) = \frac{1}{n} \sum_k \rho_k (Y - \theta^{\intercal} \phi_k)$, which basically corresponds to eqn (4) of this paper $L(\theta) = \frac{1}{K} \sum_{t} \rho_t (V_\theta(s_t) - (r_t + \gamma V_{\bar{\theta}}(s_{t+1}))^2$ except now $V_\theta$ is used in place of a linear function.
  - The core idea of the current proposed approach seems to be simply extending the linear case to general function approximation. Is there any other difference? Either way, this connection should be explicitly stated, perhaps citing the mathematical formulation as well. Of course, I understand the prior work did not consider any continuous control benchmarks, and the contribution of this work is still valuable. But I believe the connection should be made clear. The paper should highlight the specific differences between their approach and the prior work, beyond the use of general function approximation, and it should be clear if there are any other novel technical contributions.
- The conclusion states "proposed a novel approach applying trust region methods in the off-policy setting" -- is that the main contribution? Or is learning V-function instead of Q-function the contribution. The paper needs to clarify whether the main contribution is the off-policy trust region method or the use of the V-function, or perhaps a combination of both. This is currently ambiguous.

Minor issues:
- typo on page 4 paragraph 2 "Bellmann" -> "Bellman"
- typo on page 6 "populate]"
- typo on page 8 conclusion "an novel approach" -> "a novel approach"

### Questions
- Issues with mathematical notation
  - In eqn (2) and the eqn right above eqn (4): what is $j$, what is the sum over $j$, and what is $K$? Below eqn (2), the text says "$a_{t,j}$ defines the $j$th action in state $s_t$". Does this mean $j$ is enumerating the collected transitions (presumably in a buffer)? Or is this following some other distribution - what distribution would that be? 
  - In eqn (4), since you are no longer summing over $j$, do you still need $\frac{1}{K}$? 
  - Right above eqn (3), could you clarify what "upper bound" and "lower bound" this sentence is referring to, and why "truncated importance weights can provide an upper bound"? 
- The introduction mentions "upper bounds of actual Bellman error" - I assume this is referring to eqn (4) - however it was not explicitly stated around eqn (4). 
  - How was Jensen's inequality used to derive eqn (4) from eqn (2)? Could walk through this explicitly. 
- Connection to Mahmood et al. 2014
  - In that referenced paper, the authors considered linear function approx setting and presented two importance sampling approaches for off-policy learning. 
  - What they call OIS-LS and WIS-LS seems to correspond to the difference between eqn (2) vs eqn (4). Specifically, their WIS-LS objective is $J(\theta) = \frac{1}{n} \sum_k \rho_k (Y - \theta^{\intercal} \phi_k)$, which basically corresponds to eqn (4) of this paper $L(\theta) = \frac{1}{K} \sum_{t} \rho_t (V_\theta(s_t) - (r_t + \gamma V_{\bar{\theta}}(s_{t+1}))^2$ except now $V_\theta$ is used in place of a linear function. 
  - The core idea of the current proposed approach seems to be simply extending the linear case to general function approximation. Is there any other difference? Either way, this connection should be explicitly stated, perhaps citing the mathematical formulation as well. Of course, I understand the prior work did not consider any continuous control benchmarks, and the contribution of this work is still valuable. But I believe the connection should be made clear. 
- The conclusion states "proposed a novel approach applying trust region methods in the off-policy setting" -- is that the main contribution? Or is learning V-function instead of Q-function the contribution. 

Minor issues: 
- typo on page 4 paragraph 2 "Bellmann" -> "Bellman"
- typo on page 6 "populate]"
- typo on page 8 conclusion "an novel approach" -> "a novel approach"

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
