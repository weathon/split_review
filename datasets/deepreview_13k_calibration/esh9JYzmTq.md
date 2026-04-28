# Assessing the Impact of Distribution Shift on Reinforcement Learning Performance

- Decision: Reject
- Avg Score: 4.67
- Scores: 5, 3, 6

## Abstract
Research in machine learning is making progress in fixing its own reproducibility crisis. Reinforcement learning (RL), in particular, faces its own set of unique challenges. Comparison of point estimates, and plots that show successful convergence to the optimal policy during training, may obfuscate overfitting or dependence on the experimental setup. Although researchers in RL have proposed reliability metrics that account for uncertainty to better understand each algorithm's strengths and weaknesses, the recommendations of past work do not assume the presence of out-of-distribution observations. We propose a set of evaluation methods that measure the robustness of RL algorithms under distribution shifts. The tools presented here argue for the need to account for performance over time while the agent is acting in its environment. In particular, we recommend time series analysis as a method of observational RL evaluation. We also show that the unique properties of RL and simulated dynamic environments allow us to make stronger assumptions to justify the measurement of causal impact in our evaluations. We then apply these tools to single-agent and multi-agent environments to show the impact of introducing distribution shifts during test time. We present this methodology as a first step toward rigorous RL evaluation in the presence of distribution shifts.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a set of evaluation methods that measure the robustness of Reinforcement Learning (RL) algorithms under distribution shifts. The paper argues to account for performance over time while the agent is acting in its environment. The authors recommend time series analysis as a method of observational RL evaluation and show that the unique properties of RL and simulated dynamic environments supports their additional assumptions needed to measure the causal impact in their experimental evaluation.

### Strengths
1. Detailed background of the various causal inference topics is provided. Even though most of the information can be moved to the appendix, this amount of information makes the paper easy to read for someone new to the field.

### Weaknesses
1. Lack of novelty: The paper does not have a novel contribution. The idea of using simulators to perform interventional analysis is not new [1-5].

Though they talk about the focus in the paper being on "adversarial attacks on images (Atari game observations) and agent switching in multi-agent environments", there is nothing that is specific to the adversarial nature of the distribution shifts. The paper as is will be applicable if distribution shifts happen due to any other factor.

2. Verbose description: The setup is unnecessary and made complex to justify the simple idea of using a simulator to perform interventions. Simple things like an average of sampled data is dedicated a definition and equation (eq. 1), which I think is not needed. Only Section 4.2 is something that talks about a new approach, everything before that is motivation or background.

3. Insufficient experimental analysis: Experimental evaluation is not sufficient. Figures 3 and 4 are not analyzed in detail, and the inferences from these experiments are not explained properly. Even in the appendix, only the plots are added without any analysis.

### Questions
1. How would you comment on the related literature showing that simulators can be used for interventions? How is your idea new compared to them? My failure to understand this is the biggest reason for my score. Maybe I am missing something, and I would appreciate it if you could comment on it. 

2. Is the choice of adversarial nature of distribution shift important to the ideas presented in the paper? If we perform an interventional analysis on this paper and make the distribution shifts non-adversarial (something simply changed in the environment), then would the analysis you present still hold? If not, why?

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the evaluation of RL algorithms against distribution shifts.
In particular, it proposes the usage of evaluation techniques from the time series literature to take into account changes in the environment.

### Strengths
- The paper is written in an intuitive way, which would help the adoption of the proposed methodology by the RL community.

- The evaluation of RL algorithms is certainly an important issue

### Weaknesses
 - It did not come across to me what is the precise problem the paper is trying to solve. The problem formulation is somewhat vague and relies on artificial examples that make it difficult to connect it with the application of RL algorithms.

- The methodology proposed is somewhat scattered. It is unclear how this evaluation methodology would be applied. Perhaps the paper could include a pseudo-code or a flowchart to ground all the steps of the proposed methodology.

- Although the paper provides several examples, it does not provide a proper interpretation of the results. For example, in Figure 5, which agent is more robust? In Figure 3, what is the conclusion regarding the performance of A2C and PPO? Should we favor one of them in practice?

- The related work section only lists the contribution of related papers but does not provide a description of how this paper distinguishes from those.

- Could you describe more formally the assumption that "the trained agents achieved a clear trend in performance"? In particular, how is this related to the convergence of an RL agent? Does it mean the agent has reached an optimal performance? Furthermore, as the assumption does not consider a distribution shift, does it mean the agent continues to update its behavior?

- Considering the change in the dynamics of the environment, I think we cannot always conclude that the change in performance is due to the agent's behavior. For instance, in some cases, although the dynamics change, the optimal policy may remain the same. Could this methodology help identify if the agent is underperforming?

### Questions
1. Could you describe more formally the assumption that "the trained agents achieved a clear trend in performance"? In particular, how is this related to the convergence of an RL agent? Does it mean the agent has reached an optimal performance? Furthermore, as the assumption does not consider a distribution shift, does it mean the agent continues to update its behavior?
2. Could you comment on the connections from this methodology with non-stationary MDPs?
3. Considering the change in the dynamics of the environment, I think we cannot always conclude that the change in performance is due to the agent's behavior. For instance, in some cases, although the dynamics change, the optimal policy may remain the same. Could this methodology help identify if the agent is underperforming?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Reinforcement learning (RL) contains unique challenges in fixing its reproducibility problem. Current displays of evaluation take attention away from other important factors such as model overfitting and experimental design. RL researchers have developed various reliability evaluation metrics to understand the strengths and weaknesses of each RL algorithm, but these metrics do not take out-of-distribution observations into account. The authors propose time series analysis tools to measure model robustness under the presence of distribution shift. They apply these analytical tools in both single-agent and multi-agent environments to show the effect of introducing distribution shifts during test time.

### Strengths
I appreciate the plot showing the flaw of solely relying on point estimates to perform model evaluation.

### Weaknesses
The authors don't list potential weaknesses of their current method in the main text.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
