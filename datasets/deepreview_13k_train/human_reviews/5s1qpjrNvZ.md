# Guided Reinforcement Learning with Roll-Back

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Reinforcement learning-based solutions are increasingly being considered as strong alternatives to classical  system controllers, despite their significant sample inefficiency when learning controller tasks from scratch. Many methods that address this issue use prior task knowledge to guide the agent's learning, with several recent algorithms providing a guide policy that is sometimes chosen to execute actions instead of the learner policy. While this approach lends excellent flexibility as it allows the guide knowledge to be provided in any format, it can be challenging to decide when and for how long to use the guide agent. Current guide policy-based approaches typically choose a static guide sampling rate empirically, and do not vary it. Approaches that  transfer control use simple methods like linear decay, or require hyperparameter choices that strongly impact the performance. We show that under certain assumptions, the sampling rate of the guide policy can be calculated to guarantee that the mean return of the learning policy will surpass a user-defined performance degradation threshold. To the best of our knowledge, this is the first time a performance guarantee has been established for a
guided RL method. We then implement a guided RL (GRL) algorithm that can make use of this sample rate, and additionally introduce a roll-back feature in guided RL with roll-back (GRL-RB) to adaptively balance the trade-off between performance degradation and rapid transfer of control to the learner. Our approach is simple to implement on top of existing algorithms, robust to hyperparameter choices, and effective in warm-starting online learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a guided reinforcement learning method, GRL-RB, which adaptively balances the use of the guided policy and RL agent, providing the first performance guarantee in guided RL.

### Strengths
1. The main strength is that the paper provides a theoretical view on the selection rate of the expert policy in guided RL setup, which is important and novel.

### Weaknesses
1. The major weakness is the lack of existing baselines for this problem. For example, [1, 2] both focus on adaptively learning when to query the experts.
2. The presentation can be improved.
   * Line 79, the space also relates to the time step T;
   * Line 189, the definition of 'Combination Lock MDP' can be further explained with formulas;
   * For Figure 1,2, the same legend should use the same colours. In Figure 3, there is no legend for the expert performance.
   * The derivations on $\alpha$ should be explained more, regarding where it comes from and what it means.
3. The problem seems like an on-policy/off-policy problem, and it is not clear why an offline RL baseline is considered.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a sampling method that alternates actions between a guide policy (which can originate from various sources, such as model-based or imitation learning methods) and an online learning policy. The main contribution appears to be a mechanism that balances data sampling between the guide and online learning policies by adjusting a user-defined sampling rate, denoted as $\alpha$, which is based on policy performance.

### Strengths
The method effectively alternates actions from expert and learning policies, enabling the learning policy to leverage its own actions, a crucial factor for self-correcting estimations. Additionally, it is notable that GRB-RL appears resilient to distribution shift following pre-training, though more extensive testing is needed to confirm this observation.

### Weaknesses
 * *Lack of novelty*: The primary drawback is limited novelty, as similar approaches that interleave actions from expert and learning policies have been previously explored. The paper acknowledges this by referencing related works and including them as baseline comparisons (e.g., [1]).

* *Limited testing and baseline comparisons*: The approach was evaluated only within variants of the AntMaze environment considering high-dimensional state space environments, which limits insights into its broader applicability. Testing in more diverse environments, such as those found in Gymnasium, like Atari games or other complex benchmarks, could reveal the method's adaptability to different reward structures and exploration needs. Additionally, while the paper reviews a broad range of related works, the baseline algorithms included tend to underperform compared to simpler approaches, such as linear decay (LD) sampling. Also, it would also be interesting to assess how GRL-RB performs with varying data budgets during pre-training.

* *User-defined sampling rate*: The proposed method requires a user-defined sampling rate $\alpha$, which determines the proportion of actions sourced from the expert or the learning policy. While this flexibility can accelerate learning, it places a significant burden on the user to fine-tune $\alpha$, which may hinder practical applicability. Prior work, such as [2], explores this trade-off and provides insights into the optimal balance of data from both sources (expert and learner) to mitigate overestimation issues. Drawing from these insights might further constrain and optimize $\alpha$'s range.

**Overall Assessment**

Overall, the paper lacks novelty, a thorough baseline comparison, and diverse environment testing. The structure is sometimes difficult to follow, and I often found it necessary to consult the Appendix to clarify the role of certain variables. For future improvements, I recommend decoupling the method from its reliance on specific test environments and applying it to more complex, generalizable tasks.

**General remarks**

-Section 2. “Guide, Learning …”: Can be confusing how a policy $\pi$ is derived from an offline and online policy, since either actions are sampled from one of the previous ones. I suggest considering only policies $g$ and $l$ in the notation.

-Line 201 “the new guide sampling rate…” the authors should distinguish between the current $\alpha$ and the initial one used to update the former.

-The authors claim throughout the text that some features, such as the “roll back,” can, for instance, “speed up the transfer learning” before showing the results or evidence to support this (see section 4). Some (important) results are mentioned in the paper but are available in the Appendix.

-I think the paper would benefit from having a dedicated section to describe the baselines IQL and JSLR, and eventually any other method that could be included for comparison.

### Questions
[Q1] The authors show in section 3.2.3 a distinction between negative and positive dense rewards. What about a reward normalization such as [-1, 1]?

[Q2] I wonder if tested in more environments, eventually $\alpha$ would get stuck and not converge towards 0, even employing the roll back mechanism. Would that possibly happen?

[Q3] Have you tried to contact the authors of JSLR to obtain its implementation? It seems that their main result is a combination of IQL + JSLR. Is this the way it was tested in this work? 

[Q4] Why not consider different amounts of data during the pre-training phase?

[Q5] In G.1.2, could you clarify why you haven't employed the same parameters of the offline agent?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors identify issues in prior works dealing with guided reinforcement learning and aim to address them by deriving an adaptive guide policy sampling rate, which should enable fast & stable transfer of the guide knowledge to the learner policy, while at the same time maintaining performance above a defined maximum tolerable degradation threshold. The method is implemented on top of the commonly known IQL algorithm.

### Strengths
I like the general idea of the paper & the derivation of guarantees under some (strong) assumptions are interesting on their own. To the best of my knowledge those are novel & could be helpful in some (limited) scenarios.

### Weaknesses
Main weaknesses from my point of view:

1) The empirical evaluation is not very comprehensive:
There are 2 experiments in the CombinationLock environment, which are nice to get an intuitive understanding of the method, however are not very realistic RL tasks. Then there are 3 experiments on Antmaze, in which the LD baseline performs similarly well as the new algorithm. As the authors motivate the method from a quite applied perspective, I am wondering whether that means that there is not much expected gain from the method in practical scenarios. Also, I believe the positive dense reward setting is derived, but not experimented with. The lack of experiments in more complex, high-dimensional environments makes it difficult to assess the practical applicability of the proposed method. Furthermore, the similarity in performance with the LD baseline on Antmaze raises concerns about the added value of the proposed approach, especially given its increased complexity.

2) The assumptions leading to the derived sampling rates appear to be violated:
The authors realise that in practice the assumptions they make for the derivations are violated & thus add the Roll-Back method in order to improve performance. While the derived results are of course interesting on their own, one has to ask from a practical standpoint whether deriving & using something based on wrong assumptions makes a lot of sense - especially when taking into account the not so convincing empirical evaluation. The reliance on strong assumptions that are acknowledged to be violated in practice undermines the theoretical justification for the method. The roll-back mechanism, while attempting to address this, introduces an ad-hoc element that further weakens the theoretical grounding.

3) Slightly overstated claims:
E.g. in lines 67-69, you talk about "a guided RL approach, [...] with a guaranteed online performance above a user-defined threshold". This sounds like a broad claim which I think needs to be qualified further (only mean performance is above threshold, individual episodes can be below; limited to certain reward scenarios, i.e. not for general MDP / RL; only under questionable assumptions, i.e. convergence). The authors also still talk about guarantees when the Roll-Back approach is added in ("A GRL with a roll-back algorithm (GRL-RB) that helps to retain the performance guarantee of GRL while relaxing its assumptions"), even though at that point it becomes clear that there is no guarantee (Roll-Back happens exactly when guarantee is violated; plots show performance can be much below threshold for a long time). Generally I think one has to be more cautious with the term guarantee, e.g. in the abstract it is formulated better. The use of the term 'guarantee' is misleading, as the roll-back mechanism is triggered precisely when the performance falls below the threshold, indicating a violation of the supposed guarantee. The claims of guaranteed performance need to be significantly tempered to reflect the actual behavior of the algorithm.

4) Limited applicability when compared to all possible reward landscapes:
This is not such a big issue in general since guarantees even in just a few environments would be helpful. It's also briefly mentioned by the authors in the discussion.

5) I think Fig 4a might be misleading - it's not clear when something is rolled back, it just looks like violations occur in almost every step.

### Questions
- The evaluation sample rates in the bottom plots 1-3 don't align with what I expected, i.e. why are the percentages of the static baselines not exactly .25 & .75 (e.g. fig 2b has them below .2 & at .6)? I presume the variations (shaded region) of the baselines are the difference between true parameter and sampling? The LD baseline does not appear to really reduce alpha by the same amount every time step, why is that?

- One thing I also don't understand: Why is the alpha not degraded much faster? What I mean is why is it always degraded by $(1-\alpha_0)$ and not by $(1-\alpha_c)$ (algo 1, line 18) - if the assumptions on convergence you make were to hold, the updated alpha should be used for the next degradation or am I missing something?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper addresses guided reinforcement learning, utilizing prior task knowledge to enhance the agent’s learning process. Specifically, it proposes a dynamic sampling rate adjustment for the guide policy, referred to as GRL, along with a variant featuring a roll-back capability, called GRL-RB. The experimental results demonstrate that the proposed methods ensure user-defined performance and outperform other baseline approaches.

### Strengths
-  The paper addresses the critical issue of utilizing prior task knowledge to guide the agent's learning, a significant aspect of reinforcement learning.
- The paper provides a comprehensive introduction and overview of related work, laying a solid foundation for the proposed methods.

### Weaknesses
Overall, the paper writing and structure needs significant improvement, making it difficult to follow the overall flow.
- The motivation behind the proposed method and its specific details remain largely unclear. For example, in section 3, the authors mention employing a similar sampling approach to Chang et al. (2015) and Chang et al. (2023), as well as a method akin to JSRL (Uchendu et al., 2023). However, it is not clear what these methods entail or how they relate to the current work; readers should not have to refer to external papers for this information. A more detailed formal description of the proposed method should be included in the main body of the text.
- Additionally, several components of the method lack clarity and theoretical justification. For example, the rationale behind using $n_{\pi_l}/t$ as an additional threshold is not explained. Similarly, the reasoning for the new guide sampling rate being $\alpha-(1-\alpha)$ and the theoretical benefits of the roll-back mechanism are unclear. These choices appear to be made heuristically.
- The function of Section 3.2 is also confusing. The derivation of the sampling rate relies on perfect knowledge of the ‘Combination Lock’ task and the guiding policy, which is impractical for practical tasks like the AntMaze task used in this paper. While didactic examples can illustrate theoretical guarantees, the paper lacks more general theoretical results. As it stands, Section 3.2 only suggests that the method works under special conditions that require perfect information.

In summary, while the paper claims to provide a user-defined performance guarantee, it suffers from a lack of clarity and theoretical justification. The assertion that “the assumption of convergence between steps of $\alpha$ is key to the success of GRL” raises concerns. If the "key" to a method relies on an assumption, the authors should reconsider the method and adopt more conservative claims.

### Questions
See the weaknesses noted above.

### Soundness
2

### Presentation
2

### Contribution
2
