# Model-based Reinforcement Learning for Parameterized Action Spaces

- Decision: Reject
- Avg Score: 4.40
- Scores: 6, 1, 5, 5, 5

## Abstract
We propose a novel model-based reinforcement learning algorithm---Dynamics Learning and predictive control with Parameterized Actions (DLPA)---for Parameterized Action Markov Decision Processes (PAMDPs). The agent learns a parameterized-action-conditioned dynamics model and plans with a modified Model Predictive Path Integral control. We theoretically quantify the difference between the generated trajectory and the optimal trajectory during planning in terms of the value they achieved through the lens of Lipschitz Continuity. Our empirical results on several standard benchmarks show that our algorithm achieves superior sample efficiency and asymptotic performance than state-of-the-art PAMDP methods.}}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the problem of model-based reinforcement learning for parameterized action markov decision processes (PAMDPs), by proposing a framework referred to as Dynamics Learning and Predictive Control with Parameterized Actions (DLPA). The core idea of DLPA lies in the integration of neural-network based model learning (transition model, termination model, and reward function) and the model predictive control using model predictive path integral. Extensive experiments against multiple baseline algorithms for PAMDP are provided to demonstrate the efficiency of DLPA.

### Strengths
+ The proposed framework is technically sound and the key idea of DLPA is clear.

+ Extensive experiments are given against multiple baseline algorithms.

### Weaknesses
 - The novelty seems rather limited as the main framework of DLPA follows the standard data-driven MPPI, with the contextualization from MDP to PAMDPs. For example, an information theoretic MPC framework was proposed in [G. Williams et al, ICRA 20217] to incorporate the model learning in the MPPI-based planning procedure.

- Some key information is not provided, e.g. which neural network algorithms are used to optimize Eq. 1?

- No theoretical analysis is given to justify the performance applied to PAMDPs, which seems necessary to help readers understand the significance of the DLPA beyond simple contextualization of data-driven MPPI to PAMDPs. As PAMDPs concerned about finding the right action and the associated parameters to use, is there any guarantee of convergence to the selected parameterized actions during training from DLPA?

### Questions
1. What is the main contribution behind DLPA, or could authors comment on specific challenges solved when using MPPI for PAMDPs?

2. What algorithms are used to solve Eq. 1 in terms of model learning? Also, it is unclear why the authors imply that the ground truth state was not used as input to train their model in DLPA. For example, the ground-truth state s_{t+1} is needed to compute the loss L_joint defined in Eq. 1.

3. Does DLPA deliver any theoretical properties to justify its performance on PAMDPs? Authors are encouraged to discuss the convergence of parameterized actions from the DLPA framework, if any.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers reinforcement learning problems in settings where actions are of a mixed type and interactions are readily described by Parameterized Action MDPs (PAMDPs). In this setting, the paper asks whether there exist model-based methods that can efficiently find solutions.

The paper proposes a model-predictive control algorithm called DLPA, and it thoroughly evaluates it against current algorithms on PAMDP baselines.

The paper makes the following contributions.
 * A model-based RL method for PAMDPs called Dynamics Learning and predictive control with Parameterized Actions (DLPA).
 * DLPA is the first model-based algorithm for the PAMDP setting.
 * Empirical evidence that DLPA performs effectively in PAMDP benchmarks.

I really enjoyed reading this paper. Aside from some minor issues, I think the study was well executed and makes clear contribution. I elaborate on my position below.

### Strengths
* The paper is generally well written. I was able to easily identify the research questions and understand the main contributions.
* The empirical study is excellent. The experiments are constructed around the standard methodology which is aimed at supporting its main claim for SOTA performance in PAMDP benchmarks. The benchmarks and baselines seem reasonable and fairly chosen. The results provide positive evidence for its SOTA claim and demonstrate a significant performance margin between the proposed method and other baselines. The experiment in Section 5.3 addresses a nuanced claim made in Section 4.1---supporting that with clear positive evidence.
* The paper makes a significant contribution.

### Weaknesses
 * Many of my comments on this paper are minor.
* The proposed algorithm seems limited to small-horizon problems, as its backward-pass computation and the number of parameters both seem to scale linearly in the horizon length. This linear scaling with horizon length could be a significant bottleneck for applying the method to more complex, long-horizon tasks. The computational cost of the backward pass, particularly when calculating gradients through the predicted trajectories, may become prohibitive for longer planning horizons. Furthermore, the parameter space grows linearly with the horizon, potentially leading to overfitting and increased sample complexity.
* The proposed algorithm has a lot of hyperparameters, which could make the algorithm difficult to tune. The sensitivity of the algorithm to these hyperparameters is not thoroughly explored, and the paper does not provide clear guidelines for setting them. This lack of guidance could hinder the practical application of the algorithm, as users may struggle to find optimal hyperparameter configurations. The paper should include a more detailed analysis of the hyperparameter sensitivity and provide recommendations for their selection.


### Questions
General comments and questions
 * Section 2.2: "model to take in ~~this~~ actions"
 * Section 2.2: From what state are the action sequences sampled?
 * Section 2.2: It would be helpful to include a reference to introductory material on Model Predictive Control.
 * Section 3: This dichotomy of model-based methods confused me, because the two categories (random shooting and data augmentation) don't entire split the class of methods. Here, my issue is with random shooting. I suggest using a more descriptive and potentially conventional dichotomy which splits the class based on how the model is used in planning, such as Dyna-based methods and decision-time planning methods. One uses planning for credit assignment and the other for policy evaluation.
 * Section 4: Section 4.1 and Figure 1 point to notation that isn't defined until Section 4.2. Consider introducing notation earlier.
 * Figure 1: The illustrations are nicely done here. However, the caption could use more supporting text so readers understand the semantics of the green dots and the trajectories inside the states.
 * Section 4.1: Why do you call $s_t$ an observation when it was previously defined as a state in Section 2 (assuming it comes from $S$ )? If you want to distinguish it from outputs of the dynamics model, then you can always use "environment state" and "model state."
 * Section 4.1: Should $r_{t+1}$ have a hat, since it is an estimated quantity?
 * Section 4.1: "by learning to inferring" --> "by learning to infer".
 * Section 4.1: The proposed loss computes errors between the observed transition quantities and the respective predictions at each step---the latter of which are, importantly, functions of intermediate predictions. The authors claim this choice is preferable to using observed quantities in place of the intermediate predictions. Presumably, this choice allows gradients to flow back through time and assign credit more effectively than the alternative. The last few sentences of the final paragraph could make this point more clearly.
 * Section 4.2: Defining the parameters before they are used in $\mathcal{C}^0$ would add clarity to this section.
 * Section 4.2: Equation 4 should explicitly state that $\hat{s}_{t_0}=s_{t_0}$ .
 * Section 4.2: Are your action distributions are unconditional on any context?
 * Section 4.2: You are overloading notation for $d$ . Consider using $\text{d}$ or some other notation do avoid overloading.
 * Algorithm 1: "Execute the first action ..."---It would add clarity to write out the action using your notation.
 * Algorithm 1: The "training" variable is never defined, so it is unclear why the conditional statement is included. I understand what the paper hopes to communicate here: there is an initial period of data gathering with no updates. However, the pseudocode should either reflect this more accurately or it should exclude this logic---considering it as an implementation detail.
 * Figure 3: It would be more accurate to label the vertical axis "Average Episodic Return", as the reward is just a momentary quantity.
 * Table 1: I need help understanding these results, because they don't seem consistent with Figure 3. In Figure 3., DLPA achieves the highest performance in Platform and Goal. Why then is HyAR bolded?
 * Section 5.2: "action-spercialized"?
 * Section 5.3: "that just do random shooting"---fix grammar.
 * Section 5.3: The last paragraph needs a grammatical revision.
 * Section 5.3: The last paragraph could do a better job explaining why Random Shooting fails.
 * This algorithm seems to use a heavy amount of computation. Can you comment on the algorithm's complexity?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces DLPA - a model based RL approach that brings together parametrized action MDPs with model predictive control. The method was applied to 8 environments that previous works have used and demonstrate up to 30x sampling efficiency.

### Strengths
The key difference between previous work and DLPA is that model learning is performed by relying just on the initial state and the actions trajectory instead of all intermediate transitions. This provides better inductive bias for longer time horizon tasks and is show to be a critical component by the ablation study in section 5.3. 

The reported results show that DLPA learns much faster (in terms of number of samples) compared to previous benchmarks which again can be the result of learning longer horizon models.

### Weaknesses
The paper brings together PAMDPs and model predictive control in a very conventional way and so I do not find DLPA novel enough from a technical perspective. In terms of results, despite the reported sampling efficiency, even though the testing environments are used by other previous works, they still seem to be relatively simplistic even compared to other game based benchmarks such as ATARI.

Also, the reported results both in Figure 3 and Table 1 seem to much lower than the results reported in Li et al. 2022 and their HyAR approach. How much resources did you spend training the benchmarks versus your DLPA? My biggest concern is that the reported sample efficiency is caused by better hyper parameter tuning.

Learning models conditioned just on the initial state and not intermediate transitions must be much more difficult in stochastic environments (either stochastic transitions or actions), have you done any analysis in this direction?

### Questions
Also, the reported results both in Figure 3 and Table 1 seem to much lower than the results reported in Li et al. 2022 and their HyAR approach. How much resources did you spend training the benchmarks versus your DLPA? My biggest concern is that the reported sample efficiency is caused by better hyper parameter tuning.

Learning models conditioned just on the initial state and not intermediate transitions must be much more difficult in stochastic environments (either stochastic transitions or actions), have you done any analysis in this direction?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper applies a model-based RL method to the parameterized action MDP (PAMDP).

### Strengths
- The paper is easy to understand.

### Weaknesses
 - Novelty and contribution is limited.

### Questions
- What is the research question you study? In other words, what is the specific difficulty or particular problem when applying existing model-based RL methods on PAMDP tasks?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors present the first model-based solution, DLPA, for the RL problem in PAMDP settings where both discrete and continuous actions coexist. DLPA initially learns an environment model that accommodates both discrete and continuous actions. It optimizes this model using prediction errors over a continuous H-step horizon when the state input includes only the true state at the first step. Subsequently, DLPA employs the CEM method extended to the PAMDP setting, based on this model, to perform MPC.

### Strengths
1. This paper introduces a model-based approach for the first time in the context of PAMDP settings and addresses the learning challenges posed by the large action space through the application of CEM-based MPC methods.
2. The experimental results showcase the superior performance of the approach presented in this paper in terms of sample efficiency and final performance.

### Weaknesses
1. Quite a few grammar errors：
    - Sec 1, first paragraph: “… at each time step the agent must choose a discrete action type (move, ribble or shoot) and also continuous parameters (related to) that chosen discrete action, … each discrete action is parameterized by some continuous parameters, …”.
    - Sec 1, second paragraph: “By contrast, in continuous/discrete-only action spaces, …”.
    - Sec 1, third paragraph: ”It then performs Model Predictive Control …”.
    - Sec 4.2, third paragraph: “The discrete actions and continuous parameters …”.
    - Sec 4.2, fourth paragraph: “This is because each time, the agent needs to first sample from the discrete actions then sample from the corresponding continuous parameters. And each discrete action has a independent continuous parameter space. This becomes …”.
    - Sec 4.2, fifth paragraph: “… the agent executes E steps of forward planning while updating the distribution parameters over discrete actions and continuous parameters. Then it uses the first action …”.
    - Sec 5, first paragraph: “Goal: The agent needs …”.
    - Sec 5, first paragraph: “The number of parameterized actions is …”.
    - Sec 5, second paragraph: “HyAR learns an embedding of the parameterized action space …”.
    - Sec 5.1, first paragraph: “We find that DLPA achieves significantly higher sample efficiency …, … which is consistent with the results …, … DLPA on average achieves 30× higher sample efficiency compared to the best model-free method …”.
2. The author's description of the key innovations in this paper, such as the calculation of the H-step loss in model learning or the introduction of the CEM method, does not place enough emphasis on what makes these approaches unique when applied to the specific problem scenario PAMDP. For instance, what sets apart the H-step loss in DLPA compared to the traditional model-based approaches, or how does this paper's use of CEM bring innovation in the context of PAMDP, especially regarding handling the relationship between discrete and continuous actions? These are the questions that are more central to the paper and that I would like to have a better understanding of.
3. During the experimental process, the number of training steps for DLPA differs from the other baseline methods. This discrepancy makes it challenging to adequately assess the stability of DLPA's training, including whether it exhibits oscillations or other issues. Additionally, it appears that HyAR may not achieve full convergence in certain environments. Therefore, it would be advisable to provide additional experimental results with a consistent number of training steps for all algorithms to ensure a fair comparison.
4. For the experiments assessing the impact of CEM-based MPC on DLPA, it would be beneficial to include ablation studies with other traditional model-based non-MPC methods, such as MBPO, applied in the context of PAMDP.

### Questions
1. What specific form do the parameters of CEM take in this context? Are they similar to the parameters of a policy neural network, and how do they relate to the state input?
2. How does the computational complexity of CEM change as the action space expands?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
