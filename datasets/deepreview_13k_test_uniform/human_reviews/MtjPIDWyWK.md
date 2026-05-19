# Action Sequence Planner: An Alternative For Offline Reinforcement Learning

- Decision: Reject
- Scores: 3, 3, 3, 3, 3

## Abstract
Offline reinforcement learning methods, which typically train agents that make decisions step by step, are known to suffer from instability due to bootstrapping and function approximation, especially when applied to tasks requiring long-horizon planning. To alleviate these issues, in this paper, we propose a novel policy gradient approach by planning an action sequence in a high-dimensional space.This design implicitly models temporal dependencies, excelling in long-horizon and horizon-critical tasks. Furthermore, we discover that replacing maximum likelihood with cross-entropy loss in policy gradient methods significantly stabilizes training gradients, leading to substantial performance improvements in long-horizon tasks. The proposed neural network-based solution features a simple architecture that not only facilitates ease of training and convergence but also demonstrates high efficiency and effective performance. Extensive experimental results reveal that our method exhibits strong performance across a variety of tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes Action Sequence Planner (ASP), a novel framework for offline reinforcement learning. ASP replaces the commonly used likelihood maximization loss in policy gradient methods with cross-entropy loss, resulting in stable training and consistent gradients. Rather than predicting actions step-by-step at each state, ASP directly predicts an entire action sequence using fully connected neural networks, avoiding the need for more complex architectures.

### Strengths
- The main idea of the paper—using cross-entropy loss to replace the commonly used likelihood loss—is both interesting and novel, with significant potential to open a new direction for offline RL.
- The novelty of the proposed approach is evident.
- The experimental results demonstrate the advantages of the proposed method effectively.

### Weaknesses
## Technical Issues
- The proposed method claims to address or relax the issue of inaccurate value estimation caused by using value functions to bootstrap future returns. However, throughout the paper, the only approach taken to achieve this seems to be the replacement of the value/advantage function with the discounted return, which appears insufficient. As discussed in work like GAE [1], multiple design choices could serve as learning objectives or weigh the action reproducing likelihood. The use of a value function, rather than the true return, helps avoid high variance caused by different rollouts. Directly using the true return may increase variance, potentially harming training stability, which weakens the technical justification.

- From a deep learning perspective, using fully connected (FC) layers to directly generate trajectories or sequences is not technically sound, due to their poor scalability to sequence length, with complexity $O(N^2)$. Generally, sequence models like RNNs and Transformers are preferred for sequence modeling. The proposed method contradicts this intuition without providing strong arguments or experiments to justify why FC layers are chosen over alternative models that might better fit sequence modeling tasks.

- The mapping from the action trajectory to its distribution in line 189 may lead to constant shift risks. For instance, if a constant is added to all actions in a trajectory, the distribution remains unchanged. Using such a distribution in the learning objective could introduce a constant shift in the learned action trajectory. Please analyze this potential risk.

- The trajectory distribution calculation in line 189 does not account for the dimensionality of actions. For tasks with high-dimensional action spaces, how should this distribution be computed?

- The content between lines 227 and 230 is unclear. Please consider restructuring it for clarity.

- Line 231, if $y_t(a)$ is a scaling factor that adjusts each action’s contribution to the gradient update, does this mean that the action with the minimum value will always have zero contribution, as its corresponding $y(t)$ would be zero?

- In line 236, why does incorporating actions that are deemed more significant by the normalized distribution benefit the policy? The causality here is unclear, as the distribution is merely a numerical representation of the action value, not a meaningful distribution that captures the reproducing capability. Please provide further explanation.

- In line 251, why is an off-policy method mentioned here?

- The proposed method, particularly the trajectory distribution matching component, is technically quite similar to Behavior Cloning (although BC is imitation learning rather than offline RL). What causes the ablated method, ASP-MLE, to consistently perform worse than BC in Table 1? Is the setting for ASP-MLE fair, given that it uses hyperparameters from a model trained with a different loss function? Notably, the gradient magnitude differs by $10^4$?

## Writting
The storyline of the paper feels somewhat loose and could benefit from proofreading. Many arguments and conclusions are presented without sufficient supporting evidence or references to relevant literature.

## Missing discussions to literature works
Several RL papers [2, 3] relate to action sequence generation and might offer alternative design choices beyond using FC layers. Please consider discussing and comparing these methods.

## Minor
Please number key equations in the paper for readability.


## References
[1] Schulman, John, et al. "High-dimensional continuous control using generalized advantage estimation." ICLR 2016.

[2] Raffin, Antonin, Jens Kober, and Freek Stulp. "Smooth exploration for robotic reinforcement learning." Conference on robot learning. PMLR, 2022.

[3] Zhang, Haichao, Wei Xu, and Haonan Yu. "Generative planning for temporally coordinated exploration in reinforcement learning." ICLR 2022.

### Questions
Please address the issues listed in the weaknesses section.

### Soundness
1

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
4

### Summary
The paper presents an imitation learning / offline RL method that combines recent insights into the stable training of neural networks with cross-entropy losses and KL divergence minimization. The resulting agent predicts action sequences and achieves strong performance on the common D4RL benchmarking dataset.

### Strengths
The paper is mostly cleanly written and presents its insights well (with one notable exception below).

The experimental section is thorough, although I would encourage the authors to add some ablations.

### Weaknesses
Overall, the presentation of that paper leaves me unsure how the components of the loss are actually computed. The cross entropy formulation requires the actions to be binned, e.g. with the two-hot or HL-Gauss methods presented in Farebrother et al. However, in those formulations, the output of the action network would be a categorical. In this paper, the network outputs a Gaussian, which would not allow one to compute a cross entropy loss.

Another interpretation is that the authors don't use a categorical transformation, in which case their objective is not a cross entropy objective. It is unclear whether $y(a_t)$ is the probability of action $a_t$ (which would be necessary for the cross entropy objective) or simply the normalized action itself? In this case, how do the authors deal with the fact that $a_t$ is multidimensional? Their objective is then also mostly an MLE objective weighted by the size of the action, which has no clear probabilistic interpretation.The introduction of cross entropy which does not mention probabilities at all makes me think this might be the case? 

From a theoretical angle, combining both a cross entropy loss and a KL minimization is odd, as both losses are mathematically equivalent, except for an additive constant which solely depends on the target. This means that adding a KL loss is simply equivalent to multiplying the cross entropy loss by 2. Writing out the two loss components together, this becomes somewhat obvious. $log (y(a_t))$ does not depend on the learned function, and the second part is equivalent to the (unweighted) cross entropy loss. When rearranging both losses, the added KL is equivalent to adding an offset of $\lambda$ to the return weighing factor.

While the paper talks about MLE, KL minimization (and therefore also cross-entropy) is closely related to MLE [1]. This makes the juxtaposition of the two somewhat confusing here. I assume the authors want to talk about the well-documented phenomenon that squared errors, corresponding to MLE under the assumption of a constant variance Gaussian, is an unsuitable loss for many neural network training setups. This should be clarified.

Reward weighted imitation learning has been proposed in the literature before, this should be acknowledged and differences discussed [2].

Similarly, predicting action sequences is well established in imitation learning, compare for example [3,4,5]. Again, this should be discussed.

3 seeds are well known to not result in statistically reliable results. Please follow established common practice here and report on a sufficiently large number of seeds. In addition, please report uncertainty estimates such as confidence or tolerance intervals. (compare [6] for advice)

All results seem to be reported on expert datasets. Given that the method is presented as an offline RL and not an IL method, it would be important to highlight if the learned policies can outperform the expert. I am unsure that the method would be able to exhibit relevant phenomena for strong offline RL such as trajectory stitching, given it's close reliance on IL objectives.

References:
[1] https://jaketae.github.io/study/kl-mle/
[2] Using reward-weighted imitation for robot reinforcement learning, J Peters, J Kober, 2009 IEEE Symposium on Adaptive Dynamic Programming and Reinforcement Learning
[3] Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware, Tony Z. Zhao, Vikash Kumar, Sergey Levine, Chelsea Finn, CORL 2023
[4] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion, Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, IJRR 2023
[5]  RoboAgent - Towards Sample Efficient Robot Manipulation with Semantic Augmentations and Action Chunking,  Homanga Bharadhwaj, Jay Vakil, Mohit Sharma, Abhinav Gupta, Shubham Tulsiani, Vikash Kumar, ICRAA 2024
[6] https://arxiv.org/pdf/2304.01315

### Questions
n/a

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper argues that deciding on a single action step-by-step may be detrimental to long-horizon or horizon critical tasks. Thus, it proposes to plan a sequence of actions for multiple steps at a time. In addition, it suggests to replace the traditional maximum likelihood based loss function with the cross-entropy loss commonly used in supervised learning for better stability. They perform experiments on couple of environments and demonstrate improved performance.

### Strengths
1. This paper presents an interesting idea and considers that for long-horizon tasks the agent should plan a sequence of actions instead of traditional single action. Their motivation came from modeling the temporal dependency which is a crucial aspect in sequential decision making. The hyperparameter k, denoting the length of the predicted action sequence, provides an opportunity to control the granularity of making a decision. Careful tuning of this variable indeed can lead to improved performance. 

2. The cross-entropy (CE) loss, although is not a novel one in RL, the use of that with multi-step action prediction is somewhat new direction. I appreciate the author's effort to align CE loss with general policy gradient objective. The use of $G_t$ in the CE loss facilitates achieving core RL objective by preferring actions with higher returns.

3. Experiments with the custom Budget Allocation Environment add values to the validation. After the methodology secrtion, I was interested to see such experiments with varying trajectory length. The proposed approach performs better with increased trajectory length.

### Weaknesses
1. One of my main concern is related to the possibility of overfitting. The policy learns multiple actions for consecutive time-steps just based on a single observed state (the model sees every k'th state as depicted in figure 2). Further, the model incorporates KL divergence based regularization. Such a term that reduces the discrepancy between the policy and target distribution across the full trajectory may lead to memorization of the training trajectories. However, the paper doesn't investigate the generalization performance in-depth.

2. The comparison between CE loss and MLE loss is not fully comprehensive. In figure 3, the y-axis denoting gradients have different scale. Thus, the comparison is not fair. A more zoomed-in look at the CE gradients [1.0-1.5] may reveal otherwise. 

3. This paper doesn't include rigorous ablation studies to properly attribute performance gain to the introduced components. Experiments with removing KL divergence based regularization, action normalization, etc. one at a time would be helpful.

4. The paper should include more information regarding the hyperparameters, components, and  experimental settings for reproduction and clear understanding. For example, there is no discussion regarding the position embedding as illustrated in figure 2. Also, the related work section needs improvement.

### Questions
1. Is there any observed relation between the trajectory length and the value of $k$, especially in proportion to the trajectory length?

2. Does smaller value of $k$ have any advantage over larger value of $k$?

3. Can you please elaborate on how position embedding helps in this context?

### Soundness
2

### Presentation
3

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
This work deals with offline RL.  It presents a policy gradient method that performs planning the next sequence of actions in a higher dimensional representation space.  

The first few modifications are relatively basic, they first learn the policy using a cross entry loss, to optimize the action sequences.  They then introduce a cross entropy policy gradient loss.  A KL term is added to keep the target action distribution and policy action distribution close.

A neural network is introduced that outputs a sequence of actions per each time step and predicts the mean and standard of each action step in the sequence.  The target action distribution is then computed and the policy parameters are updated using the cross entropy loss with the targets

The method is evaluated on D4RL and they also show results that support the cross entropy loss having more stable gradients than the LLH loss.

### Strengths
* This paper takes a bold approach at offline RL, taking a drastically different approach to policy gradient methods.
* The multi step planning approach has good justification in many other works.

### Weaknesses
* This is a highly unusual format and I question the validity of this approach.  I would appreciate if the authors derive the policy gradient theorem under this objective.  I would also like to see more theoretical or empirical support for this since it greatly differs from standard policy gradients.  I see many problems where this loss would fail to be efficient or stable.  While the gradient may show stability in one experiment I would like to see stability of the method for offline RL learning.
* The method fails to outperform currently offline RL algorithms in a large portion of tasks and is only evaluated on one environment.  In some environments, the planning method is dramatically worse than CQL.  There are only modest improvements in a few tasks.
* The method is only evaluated on D4RL.
* The paper is relatively hard to read and the changes to the loss need further justification.  

I recommend rejection of this work given the limited empirical results and the bold changes to standard RL that are not completely justified in the text.

### Questions
Please see weaknesses and address questions about the cross-entropy loss.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new method for offline reinforcement learning. Instead of learning Q-values or update policy in a conservative mode, the approach 'imitate' the trajectories, in which actions are normalized and weighted. With this simple approach, the paper shows that the proposed method has reasonablly good performance on D4RL benchmark and especially better performance on budget allocation environment.

### Strengths
1. The proposed method is novel to me, as it abandon many techniques for conservative value or policy learning, and propose to update a loss function that with normalized actions and weights.
2. The empirical results show superior performance on budget allocation environment.

### Weaknesses
1. The presentation is bad. In general, the notation is confusing and it is hard for me understand the method from the beginning. y(a), \hat{a} are not clearly representative of their meanings and there is abuse of notations that are not reasonable.
2. The connection of the method with the classic policy update is not straightforward to me. That is to say, sec 3.2 is not informative. One should interprate the weights in a more intuitive way.
3. The empirical results is not compelling, especially there are new hyper-parameters being brought in the method. It is unclear if the approach is sensitive (or not) to hyper parameters. This is important to empirical offline RL algorithms in practice. Furthermore, the performance is not persuasive on D4RL benchmark.

### Questions
1. Could you show hyper-parameter sensitivity of the method?

### Soundness
2

### Presentation
2

### Contribution
3
