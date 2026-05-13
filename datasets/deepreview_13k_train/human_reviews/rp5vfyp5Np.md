# BATTLE: Towards Behavior-oriented Adversarial Attacks against Deep Reinforcement Learning

- Decision: Reject
- Scores: 5, 3, 3, 6

## Abstract
Evaluating the performance of deep reinforcement learning (DRL) agents under adversarial attacks that aim to induce specific behaviors, i.e., behavior-oriented adversarial attacks, is crucial for understanding the robustness of DRL agents. Prior research primarily focuses on directing agents towards pre-determined states or policies, lacking generality and flexibility. Therefore, it is important to devise universal attacks that target inducing specific behaviors in a victim. In this work, we propose BATTLE, a universal behavior-oriented adversarial attack method. In BATTLE, an intention policy is trained to align with human preferences for flexible behavior orientation, while the adversary is trained to guide the victim policy to imitate the intention policy. To improve the attack performance, we introduce a weighting function that assigns importance weights over each state. Our empirical results over several manipulation tasks of Meta-world show the superiority of BATTLE in behavior-oriented adversarial attack settings, outperforming current adversarial attack algorithms. Furthermore, we also demonstrate that BATTLE can improve the robustness of agents under strong attacks by training with adversary. Lastly, we showcase the strong behavior-inducing capability of BATTLE by guiding Decision Transformer agents to act in line with human preferences across various MuJoCo tasks. Our videos are available in https://sites.google.com/view/jj9uxjgmba5lr3g.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies behavior-oriented attacks agains deep RL agents, where the adversary forces the victim to have specific behaviors. The proposed attack first learns an intention policy based on human preference, and then trains an adversary to perturb the victim observation such that the behavior follows the intention policy. The adversary also adopts importance weights of states to optimize the attack objective. Experiments on multiple meta-world and mujoco show that the proposed method is able to manipulate the victim with high success rates, including offline policies based on decision transformer. The method can be also used to improve the robustness of agents.

### Strengths
This paper proposes an interesting type of attacks that are oriented by desired behaviors. Compared to prior works focusing on reward minimizing, the proposed attack can be more widely applicable. In real-world environments where rewards are not well-defined, such attack objective can be interesting to investigate. Learning the intention policy from human preference is also an interesting idea, although I have some concerns on it (see weakness).

### Weaknesses
1. The human preference-based intention policy learning brings extra requirement and uncertainty to the process - the collection of human preference data can be expensive. More importantly, to obtain human preference labels, one need to first collect diverse behavior data so that human can pick the intended policy. Would the collection of the behavior data already involve a pre-defined target policy? (If that's the case, why not directly use the target policy for attacks?)
2. In experiments, the authors mainly evaluate the attack success rate. However, it is not clear how the success rate is defined. Is it based on whether the victim acts as the intention policy suggests? But would it be biased since the intention policy is just an approximation of the real human intention? What if the intention learning does not learn a desired reward model or intention policy?
3. For baselines, the authors used the codebases of SA-RL and PA-AD and modified their attack's reward as the learned reward. However, this straightforward modification of the PA-AD baseline contradicts with the original method (PA-AD's formulation is for a reward-minimizing adversary, so directly replacing the attacker's reward may not work). Since the original PA-AD method is to use an RL director to find the target policy and to use an actor to conduct targeted attack, a more natural modification of PA-AD in the behavior attack scenario can be to directly use the learned intention policy as the target of actor ($\hat{a}$ in Equation (G) in the original paper).

### Questions
How are the behavior sequences generated for human preference labeling?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
They introduce a method to attack reinforcement learning policies. There are three key components. First, they use PbRL to train a policy to exhibit the desired behavior. This is a relatively novel step because most work in adversarial RL assumes that the desired target behavior is already known and incentivized by a reward function. Second, they train a weighting function to help prioritize relevant states and keep the next step from policy drift. Finally, they attack the target policy with an adversarial policy that makes it behave similarly to the target behavior using the weighting function.

### Strengths
- Working with both classic RL agents and decision transformers makes for much more thorough experiments.
- Adversarial policies that result in targetedly bad behavior is an area of research I believe is important and neglected.

### Weaknesses
1. Writing
    - I have found some of the writing to be confusing and verbose. For example, “intention policy” is not defined until multiple mentions in. The description of what it is in the abstract is very ambiguous. “Inner” and outer” level loss are not described. I don’t see a definition for “success rate” in the paper. I don’t think the paper does as good of a job as it could with laying out things in a way that is clear and quick to understand.
    - I do not understand the rationale in the first paragraph of section 4.1. I do not think this makes sense as an explanation of why an intention policy is needed instead of a direct attack.
    - I do not understand figure 1. Why is there an arrow between reward learning and the replay buffer?
    - Numerous grammar mistakes. I would recommend using a grammarly browser plugin.
2. This may speak to either issues with my reading of the paper, its writing, or the quality of the experiments. But I am unsure why BATTLE trains an intention policy with PbRL instead of just training the adversarial policy directly with PbRL. This would seem to be substantially simpler. 
3. I do not understand how SA-RL can perform so poorly relative to BATTLE unless it is just due to reward shaping. What is the reward function used for SA-RL? If an adversarial policy is directly trained to minimize the agent’s reward, how can this do worse than BATTLE at making the target agents’ reward be minimized? If the key difference truly is just reward shaping, then this paper would just seem to be one about how PbRL makes reward shaping automatic and implicit. And if so, then this paper would seem to have no novelty.
4. Relatedly, I do not understand why this paper is about adversarial attacks. BATTLE could be used to make RL policies do anything — not just to targetedly adversarially attack them. But in reality, to make RL policies do things, we just finetune them directly. This relates to why I do not understand why the intention policy was used. Why not just finetune the target angent or adversary directly wit pbrl?

### Questions
- Which experiments were performed with real humans and which were with synthetic feedback?
- See weaknesses

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces BATTLE, an adversarial attack framework targeting DRL agents. The main focus is on behavior-oriented adversarial attacks, which aim to induce specific behaviors in a DRL agent, as opposed to merely reducing the agent's rewards or driving it to a pre-determined state. BATTLE uses an intention policy aligned with human preferences and an adversary to guide the victim DRL agent to imitate the intention policy. A weighting function is also introduced to optimize the effectiveness of the attack. The authors claim that BATTLE outperforms existing methods in inducing specific behaviors and can also be used to improve the robustness of DRL agents when used in an adversarial training setup.

### Strengths
The availability of both code and demos enhances the paper's reproducibility. The paper enhanced the proposed methodology with convergence guarantees for BATTLE, adding rigor to the work.

### Weaknesses
1. The presentation quality could benefit from further refinement for better clarity and impact.
2. The method's reliance on extensive human labeling hampers its real-world applicability, raising concerns about scalability.
3. The paper could be strengthened by including more motivating examples from real-world scenarios. The assumption that an adversary can modify observations is strong and raises questions about practicality. For instance, if an adversary has the ability to control the sensor, they might as well directly control the effector, making an agent-based adversarial approach seem more practical. Additionally, the rationale for using preference-based RL remains unclear.
4. The paper lacks some critical methodological details. For example, it doesn't specify how the victim policy approximator is trained or the volume of data required, leaving gaps in the understanding of the implementation.
5. The experimental setup and evaluations could be more convincing. The choice of baselines (PA-AD and SA-RL), which are un-targeted attacks, makes the comparison seem potentially unfair. Moreover, while various defense methods like adversarial training, robust learning, policy ensemble, and policy distillation exist, the authors have limited their experimentation to ATLA.

### Questions
1. Could the authors elaborate on potential real-world applications for the proposed method and discuss the challenges that might arise in such contexts?
2. Expanding the experimental results to include additional comparison metrics would be valuable. Specifically, how does PALM fare against targeted attacks and various other defense methods?
3. What is the extent of annotation required, especially in relation to the complexity of the task at hand?
4. Could you provide details on the training process for the victim policy approximator, including the amount of data needed for effective training?
5. How generalizable is the weighting function across different types of tasks and domains?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces BATTLE, a novel universal behavior-oriented adversarial attack method designed to induce specific behaviors in deep reinforcement learning (DRL) agents. Unlike prior approaches that focus on directing agents towards predetermined states or policies, BATTLE employs an intention policy aligned with human preferences for flexible behavior orientation, guiding the victim agent to imitate it. The paper demonstrates the effectiveness of BATTLE through empirical results across various manipulation tasks in Meta-world, showing its superiority over existing adversarial attack algorithms. Additionally, BATTLE enhances the robustness of DRL agents by training with the attacker, achieving a convergence guarantee under mild conditions, and proving effective even against the latest Decision Transformer agents. In summary, the paper makes contributions in the realm of behavior-oriented adversarial attacks on DRL agents, both in theory and practical applications.

### Strengths
1. The paper introduces an interesting and novel concept, proposing a new type of attack based on preference-based RL.

2. The design of the inner-level optimization and outer-level optimization is well-founded, and the paper provides theoretical analysis of the algorithm.

3. The paper sets up different scenarios for evaluating various agents and conducts detailed ablation studies.

### Weaknesses
1. The writing needs improvement, particularly in clarifying several terms and diagrams. For example, some terms like "find a precise weighting function to balance the state distribution" need better explanation. Specifically, it's unclear how this weighting function is parameterized, what its inputs and outputs are, and how it is optimized. Clarification is also needed for the diagram in Figure 2. The diagram lacks sufficient detail to understand the flow of information and the interaction between the different components of the proposed BATTLE framework. The roles of the intention policy and the victim policy should be explicitly defined within the diagram.

2. The presentation of experimental results is somewhat confusing. The differences of scenarios in Figure 4 and 5 are not clear, and additional explanations are required for the target coordinates mentioned for Figure 4. The description of the manipulation scenario in Figure 4 needs more detail on how the target objects are positioned and how the adversary influences the grasping behavior. Captions of Figures 7 (a) and (b) might need to be swapped, and sections (c) and (d) require clearer explanations. Specifically, the performance metrics used in Figure 7 should be defined, and the rationale behind the specific comparisons should be better articulated. The reader needs more context to understand the significance of the results presented in these figures.

3. The paper lacks a discussion of limitations, which should be addressed. The limitations of the proposed approach in terms of scalability, computational cost, and sensitivity to hyperparameter settings are not discussed. The paper should also address the potential for the attack to be detected or mitigated by the victim agent.

### Questions
1. It's disappointing that the paper doesn't include RADIAL-RL[1] or WocaR-RL[2] as baselines when discussing robust training. Even if only ATLA is selected as a robust baseline, it would be valuable to mention other adversarial robust RL papers in the related work.
2. In the introduction, the paper illustrates the practical implications of targeted attacks on robotics, but the concern is raised that BATTLE is a white-box attack applying perturbations to states. In the context of robotics, its practical applicability is very limited. The paper could benefit from a more thorough clarification or discussion of this concern and its potential implications for practical applications. It fails to persuasively underscore the significance and relevance of this work within the field.

[1]Robust deep reinforcement learning through adversarial loss

[2]Efficient adversarial training without attacking: Worst-case-aware robust reinforcement learning

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
