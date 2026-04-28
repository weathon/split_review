# Leveraging Additional Information in POMDPs with Guided Policy Optimization

- Decision: Reject
- Avg Score: 3.25
- Scores: 3, 1, 6, 3

## Abstract
Reinforcement Learning (RL) in partially observable environments poses significant challenges due to the complexity of learning under uncertainty. 
While additional information, such as that available in simulations, can enhance training, effectively leveraging it remains an open problem. 
To address this, we introduce Guided Policy Optimization (GPO), a framework that co-trains a guider and a learner. 
The guider takes advantage of supplementary information while ensuring alignment with the learner's policy, which is primarily trained via Imitation Learning (IL). 
We theoretically demonstrate that this learning scheme achieves optimality comparable to direct RL, thereby overcoming key limitations inherent in IL approaches. 
Our approach includes two practical variants, GPO-penalty and GPO-clip, and empirical evaluations show strong performance across various tasks, including continuous control with partial observability and noise, and memory-based challenges, significantly outperforming existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The author propose a teacher-student RL framework that solves POMDP where the teacher takes privileged information and the student performs imitation learning.

### Strengths
The problem class is important and hard to solve for traditional methods. POMDPs are known to be hard to learn. The proposed idea is interesting and the results are satisfactory. 
In particular, the backtracking step seems the most interesting part, as other section has already been discussed in the relevant works (see below).

### Weaknesses
I found the proposed work largely overlap with the existing work [1], which is public since Feb 2024. [1] proposed a method for solving POMDP, where the teacher takes in state of the underlaying MDP and perform policy mirror descent, and the student performs imitation learning. In [1], the teacher collects the data through environmental interaction, and the student perform offline imitation, which is exactly the same procedure described in this work. The additional loss term L4 seems to be exactly the asymmetric loss in [1] if written out explicitly in the form of advantage function times a ratio. A later work [2] also proposed the same framework while utilizing PPO as backbone.

[1]. Wu, Feiyang, et al. "Learn to Teach: Improve Sample Efficiency in Teacher-student Learning for Sim-to-Real Transfer." arXiv preprint arXiv:2402.06783 (2024).

[2] Wang, Hongxi, et al. "CTS: Concurrent Teacher-Student Reinforcement Learning for Legged Locomotion." IEEE Robotics and Automation Letters (2024).

In view of this, the real contribution of this work seems minimal. A specific implementation using PPO seems more of a computational trick for stable training. This leave the real novelty with the back tracking step, i.e., setting $\mu^k = \pi^k$ at each iteration. But I am not sure how much novelty this holds.

Despite this, I have a few additional concern:
1. Due to the backtracking step, prop 1 and 2 seems to hold little value, assuming one can minimize $KL(\mu||\pi)$ accurately enough.
2. The overall usage of notation are abusive. The paper writing itself reflects its confusion. For example, in eq 9 and 10, $o_g$ (supposed to given to guider $\mu$) and $o_l$ seem to be out of place.
3. In the experiments section, it's rather strange to see PPO+BC can perform worse than PPO itself. Additionally PPO-V (asymmetric ppo) also performs reasonably well and in most cases achieves on par performance as the best in class. Then it makes one wonder what's really contributing to the performance of the proposed method. I think the only interesting case is rather GPO without the backtracking. However, I do not see the experiments on such case.
4. One can simply train a standard teacher student learning paradigm where we obtain a teacher first and then train a student. This is the standard idea dealing with POMDPs in robot learning field. This is crucial for comparison since if the proposed method cannot achieve the same level of performance, then it holds little practical value for the trained learner's policy. However, I do not see this set of experiments.

### Questions
The reward function and the ratio are both denoted as $r$. It is very hard to discern through the texts.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper introduces Guided Policy Optimization (GPO), a framework that co-trains a guider and a learner in partially observable reinforcement learning (RL) environments. The guider utilizes supplementary information to enhance training while maintaining alignment with the learner's policy. The guider is trained with RL, and the learner primarily learns through Imitation Learning (IL). This approach achieves optimality comparable to direct RL. Empirical evaluations demonstrate strong performance across various tasks, including continuous control with partial observability, noise, and memory challenges, significantly outperforming baseline methods.

### Strengths
- The paper addresses a pertinent challenge by leveraging additional information to improve training in RL environments.- 
- It is well-structured, clearly written, and easy to follow.
- Empirical studies show consistent improvements over baseline approaches across multiple benchmark domains.

### Weaknesses
 - The application of IL here is unclear, as there are no demonstrations, making it resemble a model distillation approach for partially observable settings. Restructuring the paper to emphasize knowledge distillation over imitation learning might better reflect the method's contributions.
- Several modifications and "tricks" are presented, but the paper lacks adequate empirical or theoretical justification for each. Specifically, the GPO-style update, the RL auxiliary loss for GPO-penalty, and the additional clip and mask for GPO-penalty are presented without sufficient ablation studies or theoretical backing to understand their individual contributions and necessity. The paper does not provide a clear explanation of why these specific modifications were chosen over other possible alternatives.
- There are no comparisons with state-of-the-art baselines, which limits the ability to gauge the method’s relative effectiveness. The absence of comparisons with established methods in the field makes it difficult to assess the true advancement offered by this approach.
- There is no discussion of related work.

### Questions
Have you tested the approach on real-world robots trained with data from simulations?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a method to co-train a guider and a learner. The former has access to the full state of the environment, while the learner only has access to a partial observation of the environment state. The guider commences learning in the environment from scratch, and is updated to maximise the objective while ensuring closeness with the learner policy. The learner policy is trained using a combined behaviour cloning and RL loss, based on the data collected by the guide.

### Strengths
1. Effectively simplifies learning in a noisy or partially observable environment, compared to learning from scratch
2. Thorough evaluation of the algorithm on many different kinds of environments, and good comparisons to other algorithms

### Weaknesses
1. I am not convinced as to the usefulness of this algorithm, if you truly have a task where a simulation represents a perfect noiseless and fully-observed version of the task, then why not just train a policy exclusively on the simulation, then for real-life application, just learn a map (i.e. your $f(s)$ from the partial to the full observations using supervised learning? This algorithm requires simultaneous access to the full and partial observation during training, so creating that map should be reasonably straightforward. You could then pass the full observation onto the policy trained on the simulation. Would this not be fully optimal? I’m not sure if I’m missing something here.
2. In Section 2.2, line 130 states “without requiring RL training for the learner”, by introducing the RL objective, it seems to be essentially RL, so it would have been good to see a comparison with a straight learner on the unaugmented noisy observations, just to verify the zero-padding was not slowing learning.
3. Would be good to reference the proof of Proposition 1 contained in the Appendix in the main text.

Minor
Line 201: missing “.”
Line 374: “betweetn”

### Questions
1. How would you foresee that this approach is different to, or superior to, my suggestion in Weakness 1.?
2. Shouldn't the the argmin in 2 and 3 should be an argmax, and only around the first term? In (Xiao, 2022), I believe they use an argmin in Equation 5 because they have swapped reward for regret in the value function, but it is not clear to me if you have done that also - it seems in item 2 in the list under Section 3.1, you state that you wish to maximise the objective.
3. Is the proof for Proposition 1 still relevant, given the final algorithm also includes the RL loss?

### Soundness
3

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
In RL for POMDP, a common approach is to train a teacher with access to full observations using standard RL, and a student with access to partial observations to imitate the teacher. This paper proposes to apply guided policy search to teacher student learning, which limits the teacher training to be “similar” to the student during an incremental procedure that trains teacher and student together. This way, the co-training is “smoothed out”, and it is claimed to perform better on several POMDP benchmarks. Several algorithm variants based on PPO are proposed.

### Strengths
Strengths:
1. The guided policy search approach for POMDPs makes a lot of sense.
2. The paper was (mostly) clearly written.
3. Proposition 1 is a nice insight, and helps to understand the fundamental soundness of the approach.
4. The empirical comparisons between the different proposed GPO variants and their analysis is extensive.

### Weaknesses
Weaknesses:
1. The general idea of GPS for POMDP is not new, and has been proposed in [1], a reference and discussion that is missing.
2. The authors dismiss methods that first train a teacher policy and then a student policy using RL as “inefficient”, but I do not find this convincing enough without proper evaluation. 
3. Following (2), the empirical comparison misses SOTA baselines that first train a teacher, like TGRL, and the authors modified the ADVISOR method to co-train the teacher and student together, which is not the intended use of ADVISOR and gives poor results. 
4. The authors performed evaluations on several domains that are different from domains in prior work (e.g., ADVISOR, TGRL). As the method seems to be hyper parameter sensitive, a comparison with *previously published* results is necessary to understand its performance.
5. Some of the claims need to be made more formal.

Details on weaknesses:
1. The work in [1] already proposed the idea of GPS, where teacher policy has access to full state, and student is partially observable. Although the implementation there is very different (is was before PPO), the writing of this paper should be significantly modified to reflect the novelty based on that work. E.g., Line 50-53: This key insight has already been proposed in [1]. Also, I’m not familiar with more recent extensions of [1], but it has 100 citations, so an in-depth literature survey of this line of work is required.
2. In Line 44-45: The authors dismiss several recent works by claiming “typically assume access to a pre-trained teacher, which may not always be feasible. While one could train a teacher using additional information before training the agent, this two-step process is often inefficient and computationally expensive”. Following this, in their experiments, the authors do not include comparisons with methods that first train a teacher (TGRL, the original ADVISOR implementation) even though these are SOTA. I don’t understand why training a teacher first is claimed to be so inefficient. It indeed requires training a teacher policy, but that may be *easy* as the teacher is fully observable. There are additional factors that affect the learning time - if the method is more sensitive to hyper parameters, a denser sweep is required. If a method is more sample efficient, maybe running the teacher learning is not that costly. Moreover, even if training a teacher separately is costly, if it leads to better performance of the student then it still may be preferred. Fortunately, this can easily be evaluated by comparing with methods that separate teacher and student learning, and reporting the total number of learning iterations (or wall clock time, etc.). Ideally, this would be reported also on domains where previous methods were tested and optimized for, or on new domains, but including the cost of the hyper parameter sweep too.
3. The authors should add comparisons to the original ADVISOR, and also with PPO+BC where the teacher policy is first trained to convergence. In [2], a paper that is cited by the authors, the TGRL method significantly outperforms the ADVISOR baseline. Therefore, a comparison to TGRL should be added. 
4. Importantly, as the algorithm seems to be sensitive to hyper parameters, an evaluation on domains where previous baselines were tested on, and their published results, is necessary to understand how much of the performance boost is due to hyper parameter tuning, and how much is due to the method (the authors evaluate on POPGym and noisy Mujoco, which is great, but different from previous work so impossible to directly answer this question). To emphasize this point: in several recent teacher-student algorithms for POMDPs (TGRL, ADVISOR, etc.) the key difficulty is balancing between several cost terms (teacher following, RL). From sections 3.2,3.3 it appears that a similar case holds here (though with different costs), and selecting tricks and hyper parameters that balance the costs well is critical. Since previous methods, such as TGRL, devised methods for automatically tuning the costs balance, an in-depth comparison with their results is relevant. 
5. In Line 167-174: it would be better if this “hand wavy” paragraph is translated into a formal result. E.g., can you write “In other words, the update of the learner’s policy can inherit the properties such as monotonic policy improvement (Schulman et al., 2015a) from trust-region algorithms.” formally? Or formalize the claim “This suggests that GPO can effectively address challenges in IL, such as dealing with a suboptimal teacher or the imitation gap, while still framing the learner’s policy as being supervised by the guider”? In particular, previous works like TRPO considered fully observable policies, but here \pi is partially observable - what results exactly carry over to this case? Line 176-185: the explanation here is also vague. Why do “policy gradients for the learner suffer from high variance”? It would be better to limit the explanation to concrete statements. Also, if I understand correctly, the intuition explained here is also the intuition behind many previous works on teacher-student learning, and not specific to the current method.

Summary (and explanation for my score): There is clearly an interesting idea here, and optimizing the teacher policy to “align” with the student seems like it could help learning. That said, as the novelty here is only in the implementation (and not the general idea), this paper should be evaluated based on empirical comparisons to SOTA teacher-student methods for POMDPs, which in their present form, are not extensive enough. Taking in the required changes in the writing and the experiments, my impression is that a major	revision is needed for this paper to be publishable.

Other comments (do not affect score):

Line 145: in Guider Training step 2: based on the definition of V in line 76, the solution to max_mu V_mu is the optimal MDP policy, regardless of steps 1,3,4. So I don’t understand why it makes sense to iteratively compute this step. If the point is to make an incremental update, that starts from the policy in step 4, this should be clearly stated.

Line 208: L_1 is defined for mu, not pi. Is this a typo? Also, should it be L_3(mu) and not L_2(pi)?

### Questions
see above.

### Soundness
1

### Presentation
3

### Contribution
2
