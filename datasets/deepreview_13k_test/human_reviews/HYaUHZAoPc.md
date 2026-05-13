# Offline Inverse Constrained Reinforcement Learning for Safe-Critical Decision Making in Healthcare

- Decision: Reject
- Scores: 6, 3, 3, 6, 5

## Abstract
Reinforcement Learning (RL) applied in healthcare can lead to unsafe medical decisions and treatment, such as excessive dosages or abrupt changes, often due to agents overlooking common-sense constraints. Consequently, Constrained Reinforcement Learning (CRL) is a natural choice for safe decisions. However, specifying the exact cost function is inherently difficult in healthcare. Recent Inverse Constrained Reinforcement Learning (ICRL) is a promising approach that infers constraints from expert demonstrations. ICRL algorithms model Markovian decisions in an interactive environment. These settings do not align with the practical requirement of a decision-making system in healthcare, where decisions rely on historical treatment recorded in an offline dataset. To tackle these issues, we propose the Constraint Transformer (CT). Specifically, 1) we utilize a causal attention mechanism to incorporate historical decisions and observations into the constraint modeling, while employing a Non-Markovian layer for weighted constraints to capture critical states. 2) A generative world model is used to perform exploratory data augmentation, enabling offline RL methods to simulate unsafe decision sequences. In multiple medical scenarios, empirical results demonstrate that CT can capture unsafe states and achieve strategies that approximate lower mortality rates, reducing the occurrence probability of unsafe behaviors.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposed a constraint transformer method to tackle the problem that only historical data is provided in offline inverse reinforcement learning. The proposed method exhibits effectiveness in a sepsis task.

### Strengths
- The work is well motivated and investigates an important problem, where online test or interaction is unavailable and risky for ICRL.
- The paper is well written
- The proposed method achieved good performance on MIMIC-III derived dataset which is more realistic
- Limitation, especially that expert demonstrations are assumed as optimal, is well discussed.

### Weaknesses
- I’m curious any justification for only investigating one dataset for a specific task, sepsis treatment, though I agree sepsis is an important task and MIMIC-III has been broadly investigated. But given the proposed method is proposed targeting a general problem in healthcare, either more strictly scope the claims and investigated settings, or providing broader investigation could be helpful for further demonstrating the effectiveness of the proposed method.

### Questions
Please see weaknesses.

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
3

### Summary
This paper studies inverse RL with learnable constraints in the offline setting, focusing on practical applications in healthcare tasks. The main approach appears to be combining the decision transformer architecture in the offline RL literature with inverse constrained RL with max entropy framework. Experiments were conducted on two healthcare tasks: sepsis and mechanical ventilation.

### Strengths
This paper studies an interesting and potentially important problem.

### Weaknesses
There are some inconsistencies throughout the text in terms of mathematical descriptions, and the experimental evaluation also suffers from some issues.

### Questions
- Table 1: the definition of "too high" is somewhat problematic. Claiming "too high" is associated with increased mortality making it an "unsafe behavior" without conditioning on the patient state seems inappropriate. Even though the footnote says this should be patient-dependent, the table still shows a single threshold. 
- Sec 3 problem formulation defines a non-Markov decision process (non-MDP) but the remaining text all references an MDP (L173-L175).  
- L173: What does "the MDP derived by augmenting the original MDP with the network" mean exactly? Why do we augment the MDP with a network? Or do you mean augmented with the constraint? 
- L176-L206 evaluation metric defined using "DIFF": this graphical analysis known as the "U-curve" is deprecated and widely criticized because it cannot distinguish a good policy from a bad policy (even a random one). See Figure 4 in Gottesman et al. "Evaluating Reinforcement Learning Algorithms in Observational Health Settings" (https://arxiv.org/abs/1805.12298) 
  - also "We randomly select 2N patients from the dataset where N patients survived under the doctor’s treatment, and N patients died" do not seem justified. Depending on N this may not be representative of the dataset. Why not use some form of weighted average in the ranking? 
- L244: what does "creating an offline RL for violating data" mean? 
- L190: "probability of approaching the optimal policy" L438 "use ω to indicate the probability that the policy is optimal" - in offline setting, we can never obtain the optimal policy, so I don't believe this terminology is appropriate.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents an offline approach for inverse RL in constrained settings for safety critical decision making. The overall premise of the paper is the traditional RL methods might overlook common-sense constraints which might lead to potentially harmful decisions in a high-risk setting. Moreover, such healthcare decisions must usually be inferred from offline batch data, where there is no online/limited interaction with the environment and the exact constraints might be unknown as is typically the case in healthcare. The authors introduce a two step approach to overcome these issues: i) first they employ an attention-based architecture to identify long-range dependencies and critical aspects of a patient's history; ii) based on the learnt representation from i), the authors use a generative model of the environment for data augmentation that enables unrolling/simulating potentially unsafe decision sequences. The authors try demonstrate on MIMIC III that their approach recovers the relevant constraints accurately, is performant in offline settings and enables safe policy learning.

### Strengths
Overall I think the paper tries to address a very relevant and significant problem that is not only limited to healthcare. The paper is written well in general and I like the way the experiments are laid out in the sense that the authors clearly divide their analysis into questions that tackle various aspects of the evaluation. The authors also do a good job in motivating the problem overall.

### Weaknesses
1) The authors dont make explicit what their assumptions are and I had to do a lot of sifting through details multiple times, to get a clearer picture of the exact problem setting: it is assumed that there is a reward and a set of constraints (costs) within the MDP; the reward is observable but the constraints are unknown which is why an IRL approach is warranted. 

2) The authors also assume that the expert is optimal which may not be the case in practice so the authors should make this explicit in an assumptions section. The authors should in particular make very explicit what the distribution of clinician actions is for their applications and allow us to visualise this. For instance, if the most common clinician action choice is to provide very small doses of vasopressors and fluids, how does this impact the quality of the constraints learnt? I would think that if the distribution of clinician actions is strongly biased towards certain decisions, this might have significant impact on the constraints learnt/might end up overconstraining the problem or end up not learning anything meaningful.

3) My main criticism for this paper is I feel the method contains a LOT of components and it is not always clear what the purpose of each component is. While the purpose of the transformer is to retain relevant aspects of the patient history and capture critical states, I would have liked to have seen some analysis into what is learnt/whether these points are in fact critical, why they are important etc. There is a huge body of work on learning relevant representations e.g. through decision/task-focused learning (Sharma et al 2024 https://arxiv.org/pdf/2110.13221) or otherwise through information-based methods (Liu et al 2024, https://arxiv.org/pdf/2405.09308) or similar, but the authors dont compare the representations they learn to any other method which makes it hard to understand whether what is captured is indeed relevant. There is also a large amount of work related to capturing decision-regions or important points in a patient trajectory that might impact doctor decision making in terms of how much they agree on what to do (Zhang et al 2022 https://www.nature.com/articles/s41746-022-00708-4) which should be discussed here. If nothing else, the authors should compare what is learnt to a standard LSTM representation. Subsequently, a generative model is used to unroll or simulate downstream decision sequences and perform safe decision-making under constraints. There is little discussion on how the simulator behaves as a causal model and serves as an adequate means of simulating possible trajectories. I will elaborate on this next.

4) The authors also mention that the generative model used to simulate trajectories is causal in the abstract and elsewhere. How can this be verified? What makes the representation causal? Is it robust against confounding biases? Are there experiments that validate this where you demonstrate explicitly that the effects of such biases are minimised and do not have downstream consequences on the constraints learnt and the simulations produced? Did you validate the simulations with domain expertise to check whether these were indeed valid potential trajectories/simulations of how a patient might evolve?

5) Throughout the paper, there is extensive mention of the terms Safe RL yet the entire literature on safe RL is ignored/not discussed meaningfully in terms of related work or in terms of establishing baselines for the approach to compare to (see Garcia et al 2015 https://www.jmlr.org/papers/volume16/garcia15a/garcia15a.pdf as a starting point). I understand the difference is now you are learning C but one could think of C as being part of a multiobjective reward R in which case all the works on multi-objective RL need to be discussed in a lot more detail in the related work. Given that there are various notions of what it means to be safe e.g. risk sensitive, risk-directed/aware etc. Where does this approach sit? 

6) The authors dont provide any other experiments apart from MIMIC III. It would be good to have either some toy demonstrations to validate the utility of each component of the method and why it serves a purpose or to have another clinical data set with another clinical task where you demonstrate the performance of the approach (hopefully where the action distribution differs significantly)

### Questions
1) What are your assumptions in this work and why are they plausible?
2) How does the distribution of clinician actions impact/bias the work? If the clinician decisions are all centred around administering very few drugs does that not overconstrain the system or end up with you not learning any meaningful constraints at all? How do you deal with uneven clinician action distributions?
3) What is the purpose of each component in the story and what role does it play? Why dont you compare the representations you learn with other representation learning approaches.
4) What makes the learnt representation causal? Is it robust against various biases? Do you have clinical validation to support what you have learnt?
5) What role does the Safe RL literature play here. How do you compare to these? 
6) Do you have another domain in which you can validate and support your findings?

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
5

### Summary
This paper introduces the Constraint Transformer (CT) framework to enhance safe decision-making in healthcare. The proposed CT model uses transformers to incorporate historical patient data into constraint modelling and employs a generative world model to create exploratory data for offline RL training. The authors supported their points by presenting experimental results in scenarios like sepsis treatment, showing that CT effectively reduces unsafe behaviours and approximates lower mortality rates, outperforming existing methods in both safety and interoperability.

### Strengths
This paper shows its strengths in the following aspects:

The paper addresses the novel angle of ensuring safety in offline reinforcement learning (RL) for healthcare, a critical and previously underexplored issue.

It incorporates Inverse Constrained Reinforcement Learning (ICRL) into offline reinforcement learning (RL) for healthcare, introducing a novel approach to inferring constraints from expert demonstrations in a non-interactive environment.

The implementation of a causal transformer to learn the constraint function is interesting, allowing the integration of historical patient data and capturing critical states more effectively.

Extensive results on 2 well-known dynamic treatment regime datasets are presented. The proposed Constraint Transformer (CT) framework is shown to reduce unsafe behaviours and approximates lower mortality rates.

### Weaknesses
I think the paper is generally solid and I vote for its acceptance. However, there are quite a lot of presentation issues and technical details to be addressed.

1. result

The RMSE_VASO of the proposed method is greatly larger than that of other policies. Also, it seems that CDT+CT outperforms other baselines on the importance sampling-based method but not on DR. Could you explain why? The authors said, "Since CDT+CT produces safer and more conservative policies, there is a certain distance from the clinician’s policy, so it does not perform as well in terms of RMSEvaso and F1 score." From my understanding, more safe and conservative policies should result in a smaller distance from the clinician's policy. Is this statement inconsistent with the result?

2. presentation issue

This paper has multiple presentation issues. Due to the space limit, I will only point out a few of them. *a)* Figure 1 is quite confusing. If an agent learns stochastic policy, its action choice can still be distributional. The authors misunderstood some fundamental concepts of MDPs in RL. *b)* "The Markov decision is not compatible with medical decisions." is technically wrong. The Markov decision **IS** compatible with medical decisions if you define the MDP correctly. To do RL, we must use the MDP assumption in a certain way. If I understand the authors correctly, you meant to say 'strictly first-order Markov' is not a fit for medical decisions. But why bother mention it in the introduction? Wouldn't a RNN solve this problem? *c)* Line 63-77: these 2 challenges are not in ICRL, but in applying ICRL in healthcare.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an Offline Inverse Constrained RL method (ICRL) for medical applications, which aims to (1) learn decision-making constraints from observational data using a history-dependent model architecture (‘Constraint Transformer’, CT) as well as simulated unsafe decision-making trajectories, and (2) using these within a constrained offline RL optimization procedure.
The goal is to avoid unsafe behavior in the output policy.

### Strengths
- The paper addresses the interesting problem of learning safe decision-making policies from observational data, which is an important challenge for applying reinforcement learning to healthcare applications.
- Considering the inherent challenge of evaluating such methods, authors consider multiple metrics to assess the performance of policies trained with their method / different baselines.

### Weaknesses
1. The method proposed (and in particular its complexity, as it involves a range of different modeling steps) needs to be better motivated. Below are some example modeling choices that would require a more in-depth explanation + detailed experimental analysis:
- Is the generative model in L302 not biased by partial observability? As the policy changes from expert to violating policy, does this not induce confounding in the generative model? 
- The fact that medical decision-making problems are history-dependent or POMDPs is not new (Yu et al., 2020, Reinforcement Learning in Healthcare: A Survey), yet it is presented as a major contribution. 
- Authors find that the cost function correlates with the mortality rate. Isn’t this expected from the fact that doctors’ policy aims to avoid mortality? Is the cost function truly learning something distinct from the reward function, or is it just providing additional reward shaping based on imitation learning? Table 4 would benefit from additional results comparing to TD3+BC (RL and imitation learning regularization) and to CDT without cost or with custom cost.

2. Experiment results do not demonstrate a clear added value for the proposed method, considering its added complexity.
- Evaluation: constraints are inferred and optimized, but we have no ground-truth knowledge of what they should look like. I believe this could be evaluated in a toy experiment.
- Overlapping results: (1) Table 2: CDT with and without CT cost overlap. What is the added value of CT, considering the significant additional modeling complexity required? (2) Fig 7: Authors claim a difference at DIFF=0 between their methods and the baseline, but both curves overlap in confidence interval.
- How does CDT without cost work -- is it simply a decision transformer? If so, why does it perform so much better than DDPG?
- L504 Why is CDT+CT producing a policy that is more “distant from the clinician’s policy” than other offline RL baselines? Are we not specifically learning constraints based on what actions are *different* from the behavioral policy -- ie doing a form of regularization to imitation learning?


3. Clarity is poor overall, and this observation relates to my multiple questions above. Some additional comments:
- Is $\zeta_{\theta}$ dependent on $\tau$ or (s,a)?
- Vertical white space is reduced excessively throughout the paper, which makes for an unpleasant reading experience.
- L321 where does a_t come from, is it sampled from the dataset D_e? So is the objective simply imitation learning? Or is there a missing reward signal to make it an RL objective?
- what is the strategy for bolding results in Table 2, when they clearly overlap with others? Same comment for red numbers in Table 4.
- Table 2: How does the ‘generative model’ output a policy?
- Table 3: how can proportions for CDT + CT be 0% if at least one value exceeds the thresholds considered? Is 0% an approximation?
- Fig 7: How is mortality estimated here?

4. Additional details
- L262: Transformers are not ‘interpretable’ per se beyond the first layer.

### Questions
See above.
- How does the evaluation procedure described in L190 relate to off-policy evaluation methods / propensity-weighting schemes?
- Fig 1: what is a state?

### Soundness
3

### Presentation
2

### Contribution
2
