# Student-Informed Teacher Training

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
Imitation learning with a privileged teacher has proven effective for learning complex control behaviors from high-dimensional inputs, such as images. In this framework, a teacher is trained with privileged task information, while a student tries to predict the actions of the teacher with more limited observations, e.g., in a robot navigation task, the teacher might have access to distances to nearby obstacles, while the student only receives visual observations of the scene. However, privileged imitation learning faces a key challenge: the student might be unable to imitate the teacher's behavior due to partial observability. This problem arises because the teacher is trained without considering if the student is capable of imitating the learned behavior. To address this teacher-student asymmetry, we propose a framework for joint training of the teacher and student policies, encouraging the teacher to learn behaviors that can be imitated by the student despite the latters' limited access to information and its partial observability. Based on the performance bound in imitation learning, we add (i) the approximated action difference between teacher and student as a penalty term to the reward function of the teacher, and (ii) a supervised teacher-student alignment step. We motivate our method with a maze navigation task and demonstrate its effectiveness on complex vision-based quadrotor flight and manipulation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose to improve imitation learning between a privileged expert policy that sees more information and a partially observed student policy. They propose to train the teacher policy so that it maximizes return while staying close to the student policy distribution, so that the teacher and student trajectory distributions are more aligned. The authors show this improves performance in several simulated robotic setups.

---
Post rebuttal - the authors have done a decent job addressing my concerns on experimentation and improved the presentation.

Updated my score to 6.

I do agree with reviewer mh2n that this submission still feels a bit rushed, with a lot of important results (comparison to competitive baselines and ablations) coming in through the rebuttal period. I tend to be a bit more wary of results that come in through rebuttal, given the limited time and resources.

### Strengths
- Simple approach to handling asymmetry in teacher student policy distillation, where teacher is trained to minimize divergence between teacher and student. this will constrain the teacher to states where the student can explore
- Interesting experimental findings.
	- The experiments show that teacher policies trained in this manner are better for teaching student policies.
	- A teacher with this constraint gets higher returns than a teacher without, because learning to act with less inputs leads to more robustness and generalization behavior. This would be really interesting to explore further, with more experiments or analysis.

### Weaknesses
## Experimental section has several problems
- Experimental section is lacking, sparse in task selection and choices of baseline, and seem a bit contrived. Several ways to fix this:
	- More standardized benchmarks, using envs from prior work like  [1, 2]
	- better baselines and analysis (see below)
	-  Sim2real of the drone / manipulator results would round it out

- choice of baselines is lacking, really should compare with prior work in handling asymmetric RL / IL problems ( see references below)
- Baseline details are completely missing, even if BC and Dagger are widely known, their training details need to be written down.
- little-to-no ablations, i.e. why the shared feature encoder? Wouldn't we expect that the teacher representation be very different than the student representation in very partially observed settings? 

- The authors need to put more work in the experimental section, which is verbose and unorganized. Having two giant paragraphs per experiment, one for setup, and one for results, is lazy and hard for readers to parse. Would like to see more figures, analysis of the teacher and student behavior, especially in the drone and manipulator case. IMO, the color maze experiment, which is a toy experiment, does not require that much text and space dedicated to explaining it. It could even be moved to appendix.
- Another way to improve the experimental section, is to provide some real world robot results. Because this is ICLR (more focused on learning methods), I would say this isn't a strict requirement, and I would appreciate more rigorous comparisons in the previous experiments. But real robot results would definitely round out the experimental section.

## Another weakness - having to train a teacher policy from scratch
- One drawback of this paper is the need to train a teacher policy with their specialized objective. This makes the method harder to use in practice since this method requires training a teacher policy from scratch using RL and many, many samples in a fast simulator  (10^8 for maze, 100M for manipulation). Getting a good simulator and doing sim2real is not always feasible.
	- In contrast, other methods like ADVISOR, COSIL, etc. (see references below) assume that the teacher policy is given, and do not require teacher training. In robotics,  where reasonable teacher policies can be obtained through scripting and pre-existing controllers,  it seems that approaches that do not modify the teacher are easier to use. 

Some discussion here would be appreciated.


## Minor: missing connections to prior work on regularizing privileged teachers and representations
- Regularizing the privileged policy / representation so that it doesn't stray too far away from the student  has been explored in the past, see [6,7,8]

### Questions
See weaknesses above. I am eager to see the paper be improved.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the important problem of information asymmetry between teacher and student policies in imitation learning. The authors propose a novel joint training framework that encourages the teacher to learn behaviors that can be more easily imitated by the student, thereby mitigating the negative impact of the information gap. The core idea is to incorporate the performance bound of imitation learning into the teacher's objective function, resulting in two key modifications: a KL-divergence-based penalty term in the teacher's reward function and a KL-divergence-based supervisory signal for updating the teacher's network parameters. The effectiveness of the proposed method is validated through experiments on three diverse tasks: maze navigation, vision-based quadrotor obstacle avoidance, and vision-based drawer opening with a robotic arm.

### Strengths
1. The paper presents a novel approach to tackling the teacher-student information asymmetry problem by incorporating the imitation learning performance bound into the teacher's objective function, leading to a creative combination of ideas from imitation learning theory and practical algorithm design.
2. The proposed method is well-motivated and grounded in the theoretical foundations of imitation learning, with clear explanations for the design of the KL-divergence-based penalty and supervisory terms.
3. The method is evaluated on three diverse tasks, demonstrating its applicability to both discrete and continuous control domains. The results show improvements over baseline imitation learning approaches.
4. The paper is generally well-written and easy to follow, with a clear problem statement, detailed method description, and effective use of figures and tables.

### Weaknesses
1. Limited theoretical analysis: The paper lacks a comprehensive theoretical analysis comparing the proposed method to existing approaches. A more rigorous theoretical justification for the superiority of the method would strengthen the contributions. Specifically, the paper does not provide any analysis of convergence rates or sample complexity bounds for the proposed joint training framework, making it difficult to assess its efficiency compared to standard imitation learning techniques. A theoretical comparison with methods that also address teacher-student mismatch, such as those using adversarial training or domain adaptation, would be beneficial.

2. Insufficient ablation studies: The individual contributions of the reward penalty and the KL-divergence supervision are not clearly distinguished through ablation experiments, making it difficult to assess the necessity of each component. The paper should include experiments that isolate the effect of each component, for example, by training with only the reward penalty, only the KL-divergence supervision, and without either. This would allow for a more granular understanding of how each term contributes to the overall performance gains. Furthermore, the interaction between these two components should be investigated, as they might have synergistic or antagonistic effects.

3. Limited experimental evaluation: While the method is evaluated on three tasks, a more extensive experimental evaluation on a wider range of environments and benchmarks would provide stronger evidence for the generalizability and effectiveness of the approach. The current tasks, while diverse, might not fully capture the complexities of real-world scenarios. For example, the manipulation task could be extended to include more complex object shapes or manipulation goals. Additionally, the paper should include comparisons with more recent and state-of-the-art imitation learning algorithms to better contextualize the performance of the proposed method.

4. Clarity of certain technical details: Some aspects of the paper, such as the definition of the proxy student network and the justification for the equality of covariance matrices in equations (9) and (10), require further clarification. The paper should provide a more detailed explanation of how the proxy student network is implemented and how its parameters are updated. The assumption of equal covariance matrices needs a more thorough justification, as it might not hold in all scenarios and could potentially impact the accuracy of the KL-divergence calculation.

### Questions
1. How does the proposed method theoretically compare to existing approaches in terms of convergence guarantees and sample complexity?
2. What is the sensitivity of the method to the choice of the KL-divergence penalty weight, and how can this hyperparameter be effectively tuned?
3. Can the authors provide more detailed ablation studies to demonstrate the individual contributions of the reward penalty and the KL-divergence supervision?
4. How well does the method scale to more complex environments and tasks, and what are the potential limitations in terms of computational overhead and sample efficiency?
5. Can the authors discuss the potential extensions of the proposed framework to other imitation learning algorithms and settings, such as inverse reinforcement learning or multi-agent imitation learning?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes to tackle the problem of information asymmetry in the privileged training and distillation paradigm by proposing to adapt the teacher policy’s behavior to account for the student’s partial observability by adding a reward term to encourage imitability of actions. They additionally introduce a proxy student network that approximates how the student behaves conditioned on the teacher’s privileged observations to alleviate the need of generating potentially high-dimensional student observations for optimizing the teacher policy.

### Strengths
The motivation of the problem and proposed approach is presented intuitively (but lacks some clarity see clarification questions Q1-2).

### Weaknesses
The paper’s positioning in the related work as the only one considering information asymmetry in student-teacher framework is incorrect. There are several recent works that have looked at this problem [1-5], in fact the imitability cost like the one proposed is explored in [3].

As a consequence of the above, I think the paper misses key baselines that actually tackle problems under similar assumptions of asymmetry (the considered BC and DAgger baselines are bound to fail here) and therefore does not establish novelty.

Additionally, the introduced approach involves several hyperparameters – the balancing term for “imitability” cost, the update style (frequency/batch sizes) of the alignment phase. The paper does not describe the implications of these choices of the algorithm and in-reality these can be considerably hard to tune for each task and can raise concerns of applicability and reproducibility of the approach.

### Questions
(Q1) The description of the alignment phase (Sec 4.2) can benefit from more clarity: What subset of experiences are good enough to train the proxy student – how much divergence between student/student-proxy is tolerable? If this has to be a large subset of the data then there is no benefit from using a proxy student, one might as well use all the observations to update both the teacher and student. I think clarity of the approach will improve with a pseudocode description of all the phases with input requirements in the appendix.

(Q2) In the experiments, the baselines aren’t described clearly – what does w/o alignment mean? Does it suggest removal of proxy student network in (a) no imitability loss for teacher (so standard distillation setup) (b) imitability loss with actual student network. If (a), then why is the method “w/o align (ours)” in the result tables? Also, can the authors explain why the teacher returns w/o alignment are lower than with alignment in Figure 4, intuition suggests that it should be higher?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To address the asymmetry in observation spaces during teacher-student training in reinforcement learning, this paper introduces a KL divergence penalty term between the teacher policy and a proxy for the student policy. This penalty is added to the teacher's RL loss, encouraging the teacher to adapt its behavior based on the student's observation space. To facilitate efficient penalty computation during teacher training, the authors employ a proxy student with the same privileged observation space as the teacher. The student learns by imitating the teacher from its limited observation space, while the proxy student imitates the student using privileged observations. They validate their approach in simulation across a toy grid navigation task, a vision-based quadrotor obstacle avoidance environment, and a vision-based manipulation environment, demonstrating the emergence of perception-aware behaviors.

### Strengths
- Impressive qualitative results: The emergence of perception-aware behaviors is impressive, and the authors effectively demonstrate that their approach produces this outcome across different environments, including a quadrotor flight task and a vision-based manipulation task.
- Interesting approach: The teacher-student observation asymmetry is a relevant problem to address in robotics. The idea of penalizing the teacher for behaviors that cannot be reproduced from the student’s observation space is both simple and sound.

### Weaknesses
 - Missing important comparison and discussion: Several prior works focus on training the student with RL to achieve behaviors distinct from the teacher [1, 2, 3, 4, 5, 6, 7] (and likely more). While some of these are referenced in the paper, there is no thorough discussion of this class of methods, and the authors only compare their approach to BC and DAgger, which were not specifically designed to handle observation asymmetry. Since many of these prior works are motivated by teacher-student observation asymmetry, it is crucial that the authors include a proper discussion of this line of work and compare their approach to some of them.
- Clarity and methodological details: Certain aspects of the approach, especially in Section 4, lack clarity. The method involves alternating between data collection, RL policy updates with the proposed penalty, and policy alignment, but critical details are reserved for the appendix, such as the ratio of privileged to high-dimensional observation samples or the number of updates performed in each phase for each component. A potential drawback of this approach is that alternating training for both teacher and student before teacher training is complete might demand more high-dimensional samples than BC or DAgger, which train the teacher once and then the student. It is unclear how comparisons to baselines were made, particularly regarding environment interactions. Does the proposed method require more interactions than the baselines? Were baselines evaluated with equivalent budgets of privileged and high-dimensional samples? Additionally, compared to the baselines, the approach introduces a proxy student, a more involved training protocol and a KL penalty with associated hyperparameters, making it challenging to assess the algorithm's overall complexity. The “w/o Align” baseline is also not clearly explained, nor is it clear why its behavior differs from BC and DAgger. Finally, the shared action decoder is introduced without sufficient motivation; the authors could clarify this design choice, for instance through ablation studies.

### Questions
- Why does the "w/o align" baseline perform so well compared to BC and DAgger, particularly in the quadrotor environment? It seems this baseline would produce behaviors similar to that of BC and DAgger.
- Does the proposed method require more interactions than the baselines? Were baselines evaluated with equivalent budgets of privileged and high-dimensional samples?
- What is the performance without using a shared action decoder?
- How sensitive is the method to the weight of the KL divergence penalty term?
- Is it possible to have videos of the experiments in simulation ?
- Out of curiosity, have you experimented with using forward vs reverse KL divergence as the penalty term?

### Soundness
2

### Presentation
2

### Contribution
3
