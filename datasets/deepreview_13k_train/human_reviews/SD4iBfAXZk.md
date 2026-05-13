# DynaBO: Dynamic Model Bayesian Optimization for Tokamak Control

- Decision: Reject
- Scores: 6, 5, 5, 8

## Abstract
Despite recent advances, state-of-the-art machine learning algorithms struggle considerably with control problems where data is scarce relative to model complexity. This problem is further exacerbated if the system changes over time, making past measurements less useful. While tools from reinforcement learning, supervised learning, and Bayesian optimization alleviate some of these issues, they do not address all of them at once. Considering these drawbacks, we present a multi-scale Bayesian optimization for fast and data-efficient decision-making. Our pipeline combines a high-frequency data-driven dynamics model with a low-frequency Gaussian process, resulting in a high-level model with a prior that is specifically tailored to the dynamics model setting. By updating the Gaussian process during Bayesian optimization, our method adapts rapidly to new data points, allowing us to process current high-quality data quickly, which is more representative of the system than past data. We apply our method to avoid tearing instabilities in a tokamak plasma, a control problem where modeling is difficult, and hardware changes potentially between experiments. Our approach is validated through offline testing on historical data and live experiments on the DIII-D tokamak. On the historical data, we show that our method outperforms a naive decision-making algorithm based exclusively on a recurrent neural network and past data. The live experiment corresponds to a high-performance plasma scenario with a high likelihood of instabilities. Despite this base configuration, we achieved a 50\% success rate in the live experiment, representing an improvement of over 117\% compared to historical data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper discusses  a  Bayesian optimization approach to improve data efficiency and adaptability in control problems with limited, evolving data in the domain of nuclear fusion.

### Strengths
- Very interesting domain
- The paper is written rather well and easy to understand
- Overall the approach to use a high-frequency model (here, an RNN) and a low frequency model (here a GP) makes sense
- Real empirical evaluations on a Tokamak

### Weaknesses
 - Under normal circumstances the proposed method would struggle, because it does not plan and only does 1-step planning so to say. The authors get around this problem by employing models of different frequency (RNN and GP) and by infusing domain knowledge into the architecture (page 5). While reasonable, this limits the generality of the approach.

- Experiments limited: 
1. In the introduction the authors say: "In the case of tokamak control, BO has been used, e.g., to control the rampdown of a real tokamak (Mehta et al., 2024), and to control neutral beams in a tokamak simulator (Char
et al., 2019). However, the work of Mehta et al. (2024) does not address critical plasma instabilities, whereas Char et al. (2019) relies on a simulator. Moreover, these methods use a poorly specified prior and require an extensive amount of experiments to perform well."

These shortcomings could have been evaluated empirically in this paper.  E.g. one could have shown empirically that "Moreover, these methods use a poorly specified prior and require an extensive amount of experiments to perform well." 

2.  While I acknowledge that for experiments in 4.2 comparisons and extensive studies will be difficult to do due to external constraints for 4.1 additional analyses would have been needed. Just a couple of proposals:
 How robust is the proposed method (compare different choices of kernel functions, RNN hyper-parameters,  available data, alternative modeling methods?)



Minor:
(Line 221, page 5): \cittep

### Questions
n/a

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a Bayesian optimization algorithm to find steady and open-loop control values for the gyrotron angles in a tokamak in order to prevent a certain type of plasma instability from happening. The method is applied to historical data from a tokamak as well as to live experiments in the same tokamak.

### Strengths
The paper provides a good introduction on the control of plasma instabilities in tokamaks. The proposed method is original in that it combines an RPNN with a GP for the objective function to optimize (here, the time to tearing instability). The RPNN, which provides a prior mean to the GP, is trained with historical data, while the GP is "trained" with live data acquired during the Bayesian optimization iterations.

### Weaknesses
1. It is not clear whether the authors claim to introduce a general framework for BO that uses a special prior mean, or whether they claim to introduce a specific method to control tearing instabilities in a tokamak. If it is the former (as the abstract suggests), the paper needs a much more comprehensive results section containing many more example systems and baseline methods. If it is the latter, the novelty from a purely ML standpoint seems limited and the work might be more appropriate in a field-specific venue.
2. The main novelty of the BO framework put forth in this paper seems to be the GP prior mean, computed using the RPNN trained on historical data. However, the authors clearly observe in Section 4.1 that "the RPNN is not accurate enough to faithfully predict tearing instabilities". Thus, I am not convinced that the GP prior mean in fact leads to faster or better convergence during the BO iterations. One critically missing baseline in Section 4 is to use the same BO algorithm but with zero mean.
3. In the introduction, the authors explain in detail the shortcoming of model-free and model-based RL methods when applied to controlling plasma dynamics, before presenting BO as a potentially superior method. This sounds extremely misleading to me as BO is only applicable to finding open-loop (and, in this case, steady) control actions, as opposed to the closed-loop and time-dependent control actions that RL policies typically output. In general, I feel that this paper is making large simplifying assumptions when it comes to the plasma control setting (open-loop and steady gyrotrons angles during an experiment, ability to control the ECH profile directly, etc), and it would be helpful to list all these simplifications at the outset in Section 2, rather than dispersed throughout Section 3.

### Questions
1. The authors mention in Section 2.1 that "Electron Cyclotron Heating (ECH) is one of the most effective methods to counteract tearing instability". This begs the question: does ECH already work, and if yes, what kind of control algorithm is currently used?
2. In Section 4, it is mentioned that the RPNN is "trained using 15,000 one-step state transition observations". Is the RPNN trained using only one-step trajectories?
3. Overall, I found Section 4.1 very difficult to understand. For example, what is meant in lines 321 to 323? In the right column of Figure 5, why are most of the curves only red?
4. In the live experiments, did each of the 8 experiments involve 8 BO iterations (and therefore 8 separate runs)?
5. Many typos throughout the paper: sometimes the bar is missing above $\beta_N$ for the target pressure, wrong index in line 228, the $\arg \min_t T_t$ formulation in equation (6) should simply be $\min t$, incomplete sentence in line 279, etc.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a method for controlling tokamak fusion reactors with the objective of maximizing the time to an instability failure. Within each shot (experiment trial) an RPNN models the system dynamics at a fine timescale. Across shots, a GP refines the RPNN predictions by predicting the time-to-failure residual as a function of shot-level control variables. Experiments on historical data and live experiments show a significant advantage over baselines.

### Strengths
This is a high-profile and high-stakes application. The live experiments on a working fusion reactor are impressive. The experiment results apparently show an advance over SOTA in this area.

### Weaknesses
The work is light on theoretical advances. The RPNN and its particular encoding of states and actions appear not to be new (please correct if I'm wrong). The main contribution is to use a GP to learn residuals of this model.

A primary motivation given for the proposed method is to model changes in the hardware (e.g., aging and reconfiguration). The model is said to operate on two timescales. Thus I expected time to be included in the GP input space as a proxy for hardware changes. However, the GP is not time-indexed. As formulated here, the GP is exchangeable, meaning its posterior would be invariant to permutation of the training data. Thus it doesn't learn rapidly from new data as claimed, in the sense that recent data have greater influence than older data.

It appears the GP is simply learning residuals of the RPNN, which while useful, is not a substantial theoretical advance. The claim of modeling time-dependent changes is not fully realized, as the GP treats all training data exchangeably, failing to capture temporal dynamics beyond a simple distribution shift between the initial RPNN training data and the current experimental configuration. The GP's conditioning on 125 historical shots, alongside the 8 live shots, further underscores this point, as all 133 shots are treated without any temporal weighting.

### Questions
For the live experiments sec 4.2 seems to suggest the GP was trained just for the 8 shots ("8 BO iterations") but sec A.1 seems to say it was first trained on 125 historical shots ("For online testing we use this as training set"). Please clarify.

Sec 2.2: It would help to state the shapes of variables, e.g. what is a scalar and what is a field (I know the details are in the appendix).

Sec 4.1: Why is there any variety in the action of the RPNN planner? Line 323 seems to indicate there is no exploration.

Line 201: mu should be eta

(7): sigma_n

There is inconsistency between a^g and a_g.

line 285: uncontrolled but not unknown because you measure the ECH profile

(10) Is tau the actual maximum in the dataset? Is t^(i)_TM the empirical time to failure for the planner's choice of a_g?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The manuscript describes an online optimization framework for avoiding so-called tearing-mode instabilities, when operating tokamak reactors. The manuscript is well-written, clear, and includes successful experimental evaluations (!) of the proposed optimization strategy.

The work has a great tutorial character and a real-world implementation/application flavor from which the machine learning and specifically the RL community would benefit. While the individual building blocks of the pipeline (recurrent neural networks for modelling dynamics; Gaussian processes; Bayesian optimization) are standard, the manuscript shines by presenting real-world experiments that are convincing and challenging to do. As a result, I suggest to accept the manuscript, as it would broaden the scope of work presented at ICLR and showcases an exciting and impactful example, where machine learning approaches solve challenging real-world problems related to dynamical systems.


Detailed comments/questions:
- the variable h seems to have been reused with different meanings. On p. 3 below (3), h maps to an electron cyclotron heating profile and on p. 4, h predicts the probability that a tearing mode occurs. -> Please update the manuscript accordingly.

- the gyrotron angles are kept fixed throughout each experiment. How limiting is this assumption? Have the authors considered relaxing this assumption, for example by introducing profiles that are computed a-priori? In reinforcement learning this is typically called the "options framework". 

- how significantly does the online optimization improve performance in the practical experiments? The practical experiments include eight iterations, and it is unclear to me whether similar results could also have been obtained without the online updates? Is there a way to conduct experiments for a longer period of time or is this simply not doable on the DIII-D reactor?

- related to the last question: is there a more fine-grained performance metric rather than "Tearing Instability Avoided Yes/No"? This might help to underscore the effectiveness of the online optimization.

### Strengths
see above

### Weaknesses
- the variable h seems to have been reused with different meanings. On p. 3 below (3), h maps to an electron cyclotron heating profile and on p. 4, h predicts the probability that a tearing mode occurs. -> Please update the manuscript accordingly.

- the gyrotron angles are kept fixed throughout each experiment. How limiting is this assumption? Have the authors considered relaxing this assumption, for example by introducing profiles that are computed a-priori? In reinforcement learning this is typically called the "options framework".

- how significantly does the online optimization improve performance in the practical experiments? The practical experiments include eight iterations, and it is unclear to me whether similar results could also have been obtained without the online updates? Is there a way to conduct experiments for a longer period of time or is this simply not doable on the DIII-D reactor?

- related to the last question: is there a more fine-grained performance metric rather than "Tearing Instability Avoided Yes/No"? This might help to underscore the effectiveness of the online optimization.

### Questions
see above

### Soundness
3

### Presentation
4

### Contribution
4
