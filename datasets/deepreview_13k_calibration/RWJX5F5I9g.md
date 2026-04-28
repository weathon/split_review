# Brain Bandit: A Biologically Grounded Neural Network for Efficient Control of Exploration

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8

## Abstract
How to balance between exploration and exploitation in an uncertain environment is a central challenge in reinforcement learning. In contrast, humans and animals have demonstrated superior exploration efficiency in novel conditions. To understand how the brain’s neural network controls exploration under uncertainty, we analyzed the dynamical systems model of a biological neural network that controls explore-exploit decisions during foraging. Mathematically, this type of network (which is named the Brain Bandit Net, or BBN) is a special type of stochastic continuous Hopfield networks. We show through theory and simulation that BBN can perform posterior sampling of action values with a tunable bias towards or against uncertain options. We then demonstrate that, in multi-armed bandit (MAB) tasks, BBN can generate probabilistic choice behavior with an uncertainty bias in a way that resembles human and animal choice patterns. In addition to its high efficiency in MAB tasks, BBN can also be embedded with reinforcement learning algorithms to accelerate learning in MDP tasks. Altogether, our findings reveal the theoretical basis for efficient exploration in biological neural networks and proposes a general, brain-inspired algorithmic architecture for efficient exploration in RL.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a simple recurrent neural network model of exploratory action selection.

### Strengths
This paper extends the concept of Boltzmann machine to continuous valued recurrent neural networks. I could not follow all the details of the mathematics, but the analysis seems to be new and helpful.
The simulation results are compared with human behavioral data.

### Weaknesses
The implementation of bandit assumes the availability of the memory of the all past experience in the memory buffer, which may be impractical as a cognitive model.

### Questions
The pseudo code for the MDP tasks includes P_{sas'}. Does this mean that it is assumed that the agent has access to the true dynamics of the environment?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
# Summary
The authors present a biologically-inspired neural network model called Brain Bandit Network (BBN) that addresses the explore-exploit problem in sequential decision making tasks. 
The model itself is a stochastic continuous Hopfield network, which they show can implement a form of Bayesian posterior sampling and a tunable input uncertainty bias. 
They demonstrate the BBN's effectiveness in MAB tasks, showing that it approximates human and animal choice patterns, and on some MDP exploration benchmarks.

### Strengths
# Strengths
* Novelty: As far as I can tell, this is a novel combination of Stochastic Hopfield Networks applied to decision making / explore-exploit tasks. The connections with neuroscience are interesting.
* Well written/Thorough: Paper is quite clear and well written, and as such has high pedagogical value. The authors present extensive experiments comparing BBN against baseline methods on multiple tasks, providing empirical support for their claims. (Minor concerns addressed below)

### Weaknesses
# Weaknesses
* Niche/limited applicability: The method itself is quite niche, needs an SDE solver, and has several hyperparameters that require niche/expert knowledge to tune. While the authors suggest a simple Euler discretization might suffice, the need for any SDE solver at all introduces a barrier to entry. Furthermore, the practical implications of using a fixed step size, and the sensitivity of the model to this choice, are not fully explored. The claim that the model can transition between attractor states multiple times within a few hundred steps needs more rigorous justification, especially considering the potential for numerical instability with SDE solvers.
* Tuning the numerous hyperparameters requires specialized knowledge, making it difficult for non-experts to utilize effectively. The paper lacks a principled approach for determining optimal BBN parameters for new environments. While the authors provide suggested ranges, these are not derived from a theoretical understanding of the model's dynamics, and it is unclear how these ranges would generalize to different problem structures. The sensitivity analysis provided is insufficient to address this concern, as it only explores a limited subset of the parameter space. A more systematic approach, such as a gradient-based optimization of the hyperparameters or a Bayesian optimization framework, would be beneficial.
* The performance of this model in high-dimensions needs more exposition. Section 3.4 provides a start, but more extensive experiments and theoretical analysis are needed to understand the behavior and performance of BBN in high-dimensional settings. (ideally supported by some theoretical footing). The analysis of the increasing bias toward high-uncertainty states with increasing dimensionality is interesting, but the mechanism behind this phenomenon requires more rigorous investigation. The claim that noise anisotropy is the cause is not sufficiently substantiated. A more detailed analysis of the saddle point dynamics, including the effect of different noise structures, is needed. Furthermore, the empirical evaluations in high dimensions are limited to a few grid world variants, and it is unclear how the model would perform in more complex, high-dimensional environments.

### Questions
# Suggestions for improvement:
* L169 -- L174: What is MFPT? The lead up to these equations needs better development, esp. for someone not already familiar with this literature
* L202/208: Define escape efficiency
* L322/323: Define relative and total uncertainty
* L438 and elsewhere: Explain the rationale behind the choice of T steps for BBN simulation.
* Citation format seems wrong

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this work, the Authors propose a framework addressing the exploration-exploitation tradeoff using a stochastic continuous Hopfield network. They provide a derivation to show that the proposed framework implements a form of Bayesian inference while also displaying an uncertainty-related bias. The comparison of the proposed model with human and mouse data on multi-armed bandit task shows the similarity between the two; additional considerations and experiments are provided for two MDP tasks.

### Strengths
The work deals with an interesting and important problem of the exploration-exploitation tradeoff, particularly focusing on the aspect of human decision-making. As human decision-making, shaped by evolution, is expected to be optimal, at least in certain ways, understanding its mechanics may be useful for the design of future ML algorithms. This work combines the study of exploration-exploitation tradeoff with recurrent neural networks and bandit tasks, which are all relevant and interesting to the ICLR community.

The quality of the research in this work is high: it starts with the thorough derivations of the analytic predictions for the system’s behavior and then continues with numerical experiments where the model’s predictions are first validated and then comparisons are performed with human and animal data. The text is mostly well-written, following the standard structure of machine-learning papers and introducing concepts in a logical sequence, making it easy to follow.

The result regarding the similarity between the model’s predictions and human/mouse data on exploration/exploitation in multi-armed bandit tasks is novel and interesting. It is particularly strong as it spans multiple datasets from multiple works.

### Weaknesses
While the derivations for the analytic results are thorough and lengthy, most of them appear to be either existing or intuitive. The attractor structure of the Hopfield network with two neurons and inhibitory connections is known. Hopfield networks have been shown to be able to implement Bayesian inference, although the derivations have been provided for the discrete case. The fact that the probability of the network’s activity to stay in an attractor depends on the relative orientation of its Hessian matrix and the noise direction is clear and intuitive. Of course, none of that diminishes the novelty of the result regarding the similarity between the model’s behavior and human decision-making.

The MDP part may need a fuller description (ideally a Methods section; e.g. in the Appendix) to clarify what gives rise to the observed phenomena. The uncertainty Bellman equation is also worth mentioning in the text for the clarity. Please see the specific questions regarding the Gridworld task below.

One thing that I couldn’t understand is: What makes the model explore more than the baselines? In particular, how would the exploration in this task compare to the random walk? How would that result change based on the parameterization of the stare and the Q-function (e.g., tabular vs. deep learning)?

Finally, I didn’t quite understand why is the higher state coverage considered a positive thing in this task. Specifically, as the task is not rewarded (Figure 8 b-c), the exploration seems unnecessary. When rewards are present, their utility may be different depending on the reward and the task.

### Questions
How were the states and Q-values parameterized in the task? Please provide a Methods-style description of the model. This may be particularly important in the light of the next question.

One thing that I couldn’t understand is: What makes the model explore more than the baselines? In particular, how would the exploration in this task compare to the random walk? How would that result change based on the parameterization of the stare and the Q-function (e.g., tabular vs. deep learning)?

Finally, I didn’t quite understand why is the higher state coverage considered a positive thing in this task. Specifically, as the task is not rewarded (Figure 8 b-c), the exploration seems unnecessary. When rewards are present, their utility may be different depending on the reward and the task.

Overall, I think this is an interesting paper relevant to the ICLR community. I believe that it offers sufficient novelty and significance through the remarkable match between the model’s predictions and human behavior. Text-related issues can be addressed during the remaining time.

________________
Post-rebuttal: questions addressed by the Authors; raising the score to 8.

### Soundness
3

### Presentation
3

### Contribution
3
