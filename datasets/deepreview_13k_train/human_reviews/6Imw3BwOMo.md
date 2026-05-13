# CAMMARL: Conformal Action Modeling in Multi Agent Reinforcement Learning

- Decision: Reject
- Scores: 8, 5, 6, 3

## Abstract
Before taking actions in an environment with more than one intelligent agent, an autonomous agent may benefit from reasoning about the other agents and utilizing a notion of a guarantee or confidence about the behavior of the system. In this article, we propose a novel \acrlong{marl} (\acrshort{marl}) algorithm \algo, which involves modeling the actions of other agents in different situations in the form of confident sets, i.e., sets containing their true actions with a high probability. We then use these estimates to inform an agent's decision-making. For estimating such sets, we use the concept of conformal predictions, by means of which, we not only obtain an estimate of the most probable outcome but get to quantify the operable uncertainty as well. For instance, we can predict a set that provably covers the true predictions with high probabilities (e.g., 95\%). Through several experiments in two fully cooperative multi-agent tasks, we show that \algo\ elevates the capabilities of an autonomous agent in \acrshort{marl} by modeling conformal prediction sets over the behavior of other agents in the environment and utilizing such estimates to enhance its policy learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes to extend MARL by providing agents with conformal predictions of other agents’ actions. By numerical experiments, the authors demonstrate convincingly that the approach can lead to faster convergence and better policies. They also demonstrate that the conformal prediction outperforms a probabilistic prediction of the actions.

### Strengths
The main novel idea is original and seemingly effective. The approach is presented clearly, and the experiments are well-designed. This is a convincing paper.

### Weaknesses
I would wish for some more explanation/insights on why conformal predictions would outperform other uncertainty-aware predictions. See questions for more details.

I would like some more information on why the conformal predictions outperform other approaches based on predictions that include uncertainty. The authors test this in Section 5, but they do not really give enough information on the alternative approach (APU) for me to understand. I have trouble following the arguments in the paragraph starting on line 469, and I would appreciate additional information/clarifications to better follow these arguments.
Related to this: I have difficulties following the sentence in line 423ff: “(5) CAMMARL can be preferred over strong benchmarks such as EAP owing to its higher interpretability due to the theoretical guarantees of conformal predictions in terms of coverage (Angelopoulos et al., 2020) (discussed more in Section 6).” – I am not sure that there is enough evidence for claiming that the theoretical guarantees of conformal predictions are the reason for the better performance. Firstly, these theoretical guarantees are only valid under certain assumptions, and I am not sure they are fulfilled in this case. Secondly, my intuition would be that the reason is that (a) uncertainty information does help and (b) maybe the specific format provided by the conformal predictions is easier to handle than other uncertainty predictions. In any case, the sentence should be weakened and some additional discussion in Section 5 would be appreciated. 
In this context, the reference to Section 6 is also unclear, maybe you mean Section 5?

### Questions
I would like some more information on why the conformal predictions outperform other approaches based on predictions that include uncertainty. The authors test this in Section 5, but they do not really give enough information on the alternative approach (APU) for me to understand. I have trouble following the arguments in the paragraph starting on line 469, and I would appreciate additional information/clarifications to better follow these arguments.
Related to this: I have difficulties following the sentence in line 423ff: “(5) CAMMARL can be preferred over strong benchmarks such as EAP owing to its higher interpretability due to the theoretical guarantees of conformal predictions in terms of coverage (Angelopoulos et al., 2020) (discussed more in Section 6).” – I am not sure that there is enough evidence for claiming that the theoretical guarantees of conformal predictions are the reason for the better performance. Firstly, these theoretical guarantees are only valid under certain assumptions, and I am not sure they are fulfilled in this case. Secondly, my intuition would be that the reason is that (a) uncertainty information does help and (b) maybe the specific format provided by the conformal predictions is easier to handle than other uncertainty predictions. In any case, the sentence should be weakened and some additional discussion in Section 5 would be appreciated. 
In this context, the reference to Section 6 is also unclear, maybe you mean Section 5?

### Soundness
3

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
4

### Summary
The paper presents an algorithm CAMMARL, which introduces a conformal prediction model to inform each agent of the confidence sets of actions taken by other agents. 
The method allows agents to model other agent’s actions along with a confidence set, leading to more informed policy learning. The authors evaluate CAMMARL in fully cooperative tasks with 2, 3, and 4 agent scenarios. The authors perform a comparison of their method with other baselines with increasing levels of agent modeling or information sharing. The authors also perform experiments in a mixed setting without a cooperation requirement.

### Strengths
The paper introduces a novel integration of conformal prediction with multi-agent reinforcement learning (MARL. Providing confidence sets enables agents to make a more meaningful decision when the actions of other agents may not be directly observable.
The paper is well organized and clear in the presentation of the methods used. The prediction module provides an important framework that can be used to create more adaptive and robust multi-agent systems.

### Weaknesses
The experimental results could be presented in a more compelling manner. Specifically, the plots in Figures 3a, 4a, and 5 are hard to read due to overlapping lines. Improving the clarity and readability of these figures would make it easier for readers to interpret the findings.

Additionally, while the paper discusses trends in confidence coverage, this claim could be more robustly supported with quantitative evidence. For example, including success rates and reward values would provide a clearer picture of agent performance improvements during evaluation.

A comprehensive assessment of agent performance with the trained model is missing. Adding metrics such as success rates, average rewards, and perf across varying conditions during post-training evaluation would significantly strengthen the experimental results section.

The claim regarding trends in confidence coverage needs more support, as the current presentation in Figure 7 is inconclusive. Similarly, the accuracy and loss curves in Figure 7 lack clarity.

### Questions
Could you clarify how the adapted conformal calibration in CAMMARL differs from existing conformal methods in multi-agent reinforcement learning? Is this calibration uniquely addressing specific challenges or nuances in multi-agent environments?

Improving the visual clarity of the figures and plots would greatly help in interpreting the data. A tabular representation of evaluation metrics would be beneficial.

### Soundness
3

### Presentation
2

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
This paper introduces CAMMARL (Conformal Action Modeling in Multi-Agent Reinforcement Learning), a novel algorithm for MARL that uses conformal prediction to model the actions of other agents as probabilistic sets, i.e. conformal action sets, to improve cooperative decision-making under uncertainty. Conformal prediction sets that CAMMARL provide are distribution-free confidence intervals for actions and their integration improves adaptability in cooperative multi-agent environments. The proposed framework is evaluated in several multi-agent cooperative tasks where CAMMARL demonstrates improved convergence and performance over baseline approaches.

### Strengths
1. **Novel Application of Conformal Predictions for Action Modeling:** CAMMARL´s use of conformal prediction sets provides a novel approach to handle uncertainty in agent actions without distributional assumptions. These conformal prediction sets enable agents to act with quantified confidence which offers an advantage where precise action predictions are difficult. Moreover, conformal action predictions provides better interpretability by offering agents clear confidence intervals on co-agent actions. 
2. **Empirical Results:** Initial experiments have supporting results, demonstrating CAMMARL´s faster convergence and higher rewards in cooperative tasks compared to baselines.

### Weaknesses
1. **Assumption of Global State Access:** As noted by the authors, CAMMARL assumes full access to the state space, which may limit its applicability in real-world settings. This assumption is particularly restrictive in decentralized multi-agent systems where agents typically have only local observations. The reliance on a global state representation prevents the direct application of CAMMARL to many practical scenarios where agents must make decisions based on their limited sensory input. Furthermore, the method's performance in environments with partial observability is unclear, and the paper does not provide sufficient analysis of how the algorithm would handle situations where the full state is not available to all agents.
2. **Simplistic Experimental Scenarios:** The chosen experimental environments, while useful for initial validation, are relatively simple and may not fully capture the complexities of real-world multi-agent interactions. The cooperative tasks used in the evaluation do not adequately address challenges such as non-stationarity, communication constraints, and the presence of adversarial agents. The lack of experiments in more complex environments raises concerns about the generalizability of the proposed approach to more realistic scenarios.
3. **Lack of Theoretical Convergence Analysis:** Although the conformal prediction set approach used in CAMMARL provides interpretability and a bounded measure of control over agent uncertainty through confidence sets, a formal convergence analysis is lacking. This absence of a theoretical foundation makes it difficult to assess the long-term behavior of the algorithm and to provide guarantees about its performance in different settings. The paper would benefit from a rigorous analysis of the conditions under which CAMMARL is guaranteed to converge to a stable solution.

### Questions
1. Given the global state access assumption in the mathematical model, could the authors clarify how CAMMARL would perform in environments with strictly local observations? Are there adaptations or modifications that would allow it to operate effectively under full partial observability?
2. Given the potentially high memory requirements, especially in multi-agent settings with extended time horizons, have the authors analyzed the memory complexity of CAMMARL?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a CAMMARL method, which introduces conformal prediction into opponent modeling to quantify uncertainty in action predictions. The authors conduct experiments on four MARL environments to evaluate the method.

### Strengths
1. The paper is well-motivated. The issue of uncertainty prediction in opponent modeling is interesting and noteworthy.
2. This paper introduces conformal prediction to quantify uncertainty in action predictions, which appears technically feasible.

### Weaknesses
1. The organization of the paper is poor, especially in the experiments, making it hard to read. I suggest introducing all baselines before discussing the results.
2. The paper lacks comparisons with existing opponent modeling algorithms. Moreover, the algorithm's performance seems to have no obvious advantage in many experimental results.
3. The motivation of the method in Section 3 is not clearly explained. Improving the clarity of the writing would be very helpful.
4. I suggest the authors include some technical background of conformal prediction.

### Questions
1. The algorithm demonstrates superior performance on Google Football compared to other tasks. Could you provide some insights into what types of tasks the proposed algorithm may be most effective for?
2. How does the setting of prediction accuracy threshold for selecting the action set impact the algorithm's performance?

### Soundness
2

### Presentation
1

### Contribution
2
