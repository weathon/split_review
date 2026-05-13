# Flow-based Maximum Entropy Domain Randomization for Multi-step Assembly

- Decision: Reject
- Scores: 5, 3, 6

## Abstract
Domain randomization in reinforcement learning is an established technique for increasing the robustness of control policies learned in simulation. By randomizing properties of the environment during training, the learned policy can be conformant to uncertainty along the randomized dimensions. While the environment distribution is typically specified by hand, in this paper we investigate the problem of automatically discovering this sampling distribution via entropy-regularized reward maximization of a neural sampling distribution in the form of a normalizing flow. We show that this architecture is more flexible and results in better robustness than existing approaches to learning simple parameterized sampling distributions. We demonstrate that these policies can be used to learn robust policies for contact-rich assembly tasks. Additionally, we explore how these sampling distributions can be used for out-of-distribution detection in the context of an uncertainty-aware multi-step manipulation planner.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method to automatically discover a good sampling distribution for domain randomization in reinforcement learning to learn conformant policies. This is done by using normalizing flows to learn a neural sampling distribution that maximizes the return and entropy of the sampling distribution. The approach is validated in simulation and a gear-assembly task. Finally, the learned sampling distribution is used for out-of-distribution detection to enable uncertainty aware manipulation planning.

### Strengths
- This paper addresses an important problem of improving robustness of control policies learned in simulation and would be of interest to the robotics community.
    
- Experimental comparison with prior methods shows that GoFlow learns a better sampling distribution.
    
- Using the learned distribution to estimate the belief space precondition is a useful contribution.
    
- Experiments on real robots on a challenging gear assembly task indicate the efficacy of the approach.

### Weaknesses
- The main novelty of using normalizing flows to learn the parameter sampling distribution is somewhat limited. However, it has been shown to be quite effective.
- The related work section is brief. I would like to see a more thorough discussion of the baselines and of methods that learn the domain randomization distribution.
- Error in estimating the belief space precondition can lead to incompleteness in planning.

### Questions
- What is the true uncertainty distribution in the gear assembly task? Is it artificially induced or due to to uncertainty in perception and actuation? How is it simulated during training?
    
- How sensitive is the method to the regularization coefficient hyperparameter? The scale of the expected return J depends on the reward function. Does one need to tune the coefficient for every reward function?

### Soundness
3

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
5

### Summary
The authors propose a method (GoFlow) for the automatic design of domain randomization distributions to facilitate sim-to-real transfer in absence of real-world data. In particular, GoFlow finds the right balance between a maximum entropy distribution and good policy performance within this distribution, while employing normalizing flows for extreme flexibility in capturing feasible patterns. The results demonstrate superior generalization performance when policies are trained with GoFlow.

### Strengths
- The method extends current state-of-the-art algorithms for Domain Randomization by employing flexible distribution representations through normalizing flows.
- The method demonstrates that normalizing flows can be learned in this context to autonomously capture complex patterns among unobservable parameters, such as circular shapes in Fig. 2.
- The authors successfully deploy a probabilistic pose estimation model that allows guiding the agent to seek additional information in partially observable settings.

### Weaknesses
- Poor description of the method and contextualization relative to existing works:
  - The authors present the method as a novel approach for learning DR distributions. However, to my understanding, the presented opt. problem in Eq. 5 has been recently proposed by Tiboni et al. [1] (aka DORAEMON) under an equivalent formulation, which, in turn, took inspiration from the self-paced curriculum learning opt. problem [2] (See Eq. 3 and Sec. B in [1], and see Eq. 12 and Eq. 20 in [2]). All these methods involve a joint opt. problem between the policy performance and an entropy/KL objective from a target distribution. However, the authors fail to make connections to these existing works, while proposing an equivalent formulation. The authors shall explain which parts of the method are novel, and which come from existing works in literature.
  - The final objective for optimizing the sampling distribution in line 9 of Algorithm 1 includes a third term beyond the entropy and the KL term which is not discussed in the main text. It's also unclear why this term is added. Perhaps more importantly, this term was introduced by LSDR [3] but no connection/citation is reported in the manuscript by the authors. In fact, the final algorithmic implementation in Algorithm 1 appears to be equivalent to LSDR, but extended to normalizing flows.
  - DORAEMON [1] and LSDR [3] provide clear motivations behind their choices of the respective objective functions. However, the authors here do not discuss how the opt. problem described in Eq. 5 translates to Algorithm 1. As a result, the algorithmic implementation in Algorithm 1 appears disconnected from the motivation and the general problem described by Eq. 5.

- Validity of the experimental evaluation:
  - DORAEMON [1] recently showcased successful deployment of FullDR, ADR, and DORAEMON in the cartpole and other locomotion tasks. However, in this paper these methods seem to score critically low in the same environments. This raises questions on the validity of the experimental evaluation, if not properly analyzed and discussed. E.g. why are the success rates so low across all methods?
  - Are baseline methods such as LSDR, ADR and DORAEMON trained with privileged value functions as well? This is known to drastically affect the results, and should be implemented for all baselines for a fair comparison.
  - ADR and DORAEMON assume that the initial sampling distribution is a feasible one, i.e. a near-optimal policy may and should be learned before ever stepping the sampling distribution. Is this assumption satisfied across the experimental evaluation? If not, it should be made clear that this assumption is violated.
  - How does the entropy change for different methods across the training process? What is the starting distribution/entropy for each method? No insight on the varying training distributions is reported, making it harder to draw conclusions on why each method is performing the way it does.
  - Hyperparameter curves for ADR and Doraemon seem to only include one value in some plots of Fig. 9, 10, and 11.

- Lack of proper citing or outdated citations:
  - Sec. 1: "too broad a distribution leads to unstable [...] while too narrow a distribution leads to poor real-world generalization". Citation required, this claim is not demonstrated in this paper.
  - Sec. 1: "many esisting methods rely on real-world rollouts from hardware experiments to estimate dynamics parameters". DROPO [4] and NPDR [5] are recent state-of-the-art methods that compare and beat the cited and older papers BayesSim and SimOpt. They should likely be cited as well.
  - Sec 1: "As shown in this paper and elsewhere". "Elsewhere" should be accompanied by one or more references.


[1] Tiboni, G. et al. "Domain Randomization via Entropy Maximization." ICLR 2024.

[2] Klink, Pascal, et al. "A probabilistic interpretation of self-paced learning with applications to reinforcement learning." Journal of Machine Learning Research 22.182 (2021): 1-52.

[3] Mozian, Melissa, et al. "Learning domain randomization distributions for training robust locomotion policies." 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, 2020.

[4] Tiboni, G., Arndt K., and Kyrki V. "DROPO: Sim-to-real transfer with offline domain randomization." Robotics and Autonomous Systems 166 (2023): 104432.

[5] Muratore, Fabio, et al. "Neural posterior domain randomization." Conference on Robot Learning. PMLR, 2022.

### Questions
- What is the starting distribution and entropy of GoFlow? How does it vary during the algorithm? E.g., it starts wide and then it shrinks to focus on the feasible regions, or viceversa.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents GoFlow, a novel method to domain randomization for reinforcement learning. In robotics, domain randomization is a common technique used to enhance the robustness and performance of sim-to-real reinforcement learning. In recent years, sim2real RL methods have enabled quadrupeds and humanoids to achieve impressive locomotion and manipulation skills [1][2][3]. However, often domain randomization procedures require extensive human engineering. The proposed method seeks to automate the tuning of domain randomization parameters using a normalizing flow architecture and maximum entropy principle.

The method improves the robustness of control policies learned in simulation by adaptively randomizing simulation physical properties during training. It produces policies that can handle uncertainties more effectively. The authors demonstrate the capabilities of this approach with one multi-step real-world contact-rich assembly robotic task. Experiments in the paper suggest that it outperforms existing methods in terms of success rate in both simulated and real-world settings.

However, in its current form, I cannot recommend acceptance due to the following reasons:
- experimental evaluations are limited, and cannot support the claims of the core contributions
- real robot results are impressive in video, but not presented quantitatively or clearly in the paper 

[1]: UMI on Legs: Making Manipulation Policies Mobile with Manipulation-Centric Whole-body Controllers, Huy Ha et al, CoRL 2024.
[2]: Takahiro Miki et al. ,Learning robust perceptive locomotion for quadrupedal robots in the wild.Sci. Robot.7,eabk2822(2022).DOI:10.1126/scirobotics.abk2822
[3]: Expressive Whole-Body Control for Humanoid Robots, Cheng et al, RSS 2024

### Strengths
Originality:
- While prior works such as DORAEMON have explored automating domain randomization using maximum entropy principles to enhance the generalization capacity and performance of RL policies, this is the first work that combines normalizing flow and maximum entropy to perform domain randomization for RL, to the best of my knowledge. The authors also demonstrated the effectiveness of their method on a challenging robotics task: multi-step contact-rich assembly, which is new to this line of literature.

Quality:
- The proposed algorithm, GoFlow, is shown to outperform prior works on 4 simulation tasks and 1 real robot task. While the presented success rate is seemingly low (ranging from 0.1-0.2), the real robot video seems convincing.

Clarity:
- The paper is overall well written and easy to flow. The authors provided a comprehensive overview of related works, background, and method sections. Graphics are helpful for understanding the motivation and strength of the proposed method. Specifically, figure 2 provides a good visualization of the multimodal ability of the normalizing flow approach and figure 5 demonstrates how GoFlow can be used to perform belief space planning for multi-step gear insertion tasks on a real robot.

Significance:
- From the perspective of more effective domain randomization for sim2real RL, this work shows it outperforms prior methods. From the angle of multi-step manipulation, this work also shows it is able to plan over belief space and perform contact-rich assembly tasks.

### Weaknesses
1. Experimental evaluations are limited:
- For the comparisons against baseline methods, the range of tasks is too narrow (only 4 simulation tasks).

2. Sim results are hard to interpret
- Out of the 4 sim tasks, it is difficult to assess the effectiveness or significance of GoFlow's improvements or better performance, especially when all methods and tasks have relatively low success rates. For instance, in quadcopter, it is hard to draw a conclusion that 0.02 achieved by GoFlow is indeed better than baseline methods in a statistically significant manner.   
- For cartpole and gears, GoFlow performs similarly to some baseline methods.

3. Real robot results are also limited
- Although I truly appreciate the effort to design and perform such a challenging real robot experiment, it is hard to find the success rates or other evaluation metrics for the multi-step gear insertion task presented in the paper. Thus, it is difficult to assess the effectiveness of this method quantitatively, despite the cool results from the supplementary video.

### Questions
1. If the aim is to make domain randomization easier or better for RL, the experimental results need to demonstrate that on a wider range of tasks, such as tasks that are highly relevant to real robotic systems, such as quadrupeds / humanoid locomotion tasks, manipulation tasks, etc, or simulation benchmarks that contains more than 4 tasks.

2. Related to the current experimental results, why are the success rates lower than the numbers presented in prior works and baseline papers (for example Doraemon)? It would really help if the authors could explain the difference in evaluation protocols and metrics in more detail.

3. The proposed method seems to have a high variance in success rate and low success rate from Figure 3. Could authors elaborate on this?

4. Could the authors perform more experimental evaluations on the real robot task? For example, it is hard to tell the success rate for the overall multi-stage task, or the success rates for each stage of the multi-step task.

### Soundness
3

### Presentation
3

### Contribution
2
