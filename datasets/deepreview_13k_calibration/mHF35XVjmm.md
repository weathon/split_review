# MADiff: Offline Multi-agent Learning with Diffusion Models

- Decision: Reject
- Avg Score: 5.40
- Scores: 6, 5, 6, 5, 5

## Abstract
Diffusion model (DM) recently achieved huge success in various scenarios including offline reinforcement learning,
where the diffusion planner learn to generate desired trajectories during online evaluations.
However, despite the effectiveness in single-agent learning, it remains unclear how DMs can operate in multi-agent problems, where agents can hardly complete teamwork without good coordination by independently modeling each agent's trajectories.
In this paper, we propose \our, a novel generative multi-agent learning framework to tackle this problem.
\our is realized with an attention-based diffusion model to model the complex coordination among behaviors of multiple agents.
To the best of our knowledge, \our is the first diffusion-based multi-agent learning framework, which behaves as both a decentralized policy and a centralized controller. During decentralized executions, \our simultaneously performs teammate modeling, and the centralized controller can also be applied in multi-agent trajectory predictions. 
Our experiments show the superior performance of \our compared to baseline algorithms in a wide range of multi-agent learning tasks, which emphasizes the effectiveness of \our in modeling complex multi-agent interactions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper extends previous work in diffusion-based offline RL to offline cooperative MARL, and in particular to the CTDE and centralized control settings.

The main contribution is the inclusion of an attention module in the diffusion model to help integrate information from other agents during centralized training and help coordination. The method is called MADiff

During online centralized control, an action is selected at each time step by first generating a future joint-observation sequence conditioned on the current joint-observation. An inverse dynamics model then infers the joint-action required to produce that observation sequence, and that is the joint-action taken by the agents.

The paper then evaluates MADiff in two offline MARL settings: SMAC (2 maps) and MPE (3 envs), and on the NBA trajectory prediction dataset.

### Strengths
This paper extends the application of diffusion models to offline multi-agent RL, with a non-trivial modification to the the usual U-Net architecture to facilitate coordination. The problem setting is significant, with potential applications to sports, urban planning, traffic prediction, ecology and other fields.

The empirical evaluation is relatively diverse, and compares to multiple relevant baselines.

At a high level, the paper is also generally well structured, and it is easy to follow from one section to the next. The Preliminaries section is particularly well contained.

### Weaknesses
 **Clarity** 
- While the paper is well structured, the writing could benefit from spell-checking and rephrasing since it often hurts understanding. A few examples:
  - "more high-frequency and less smooth nature of actions" : What does it mean for actions to be "high-frequency"?
  - the diffusing process is said to condition on information $y(\tau)$, which based on Fig. 1 includes "Returns" and "Other information". In that case, why are there multiple returns? Is it expected future discounted returns, or final returns for that trajectory? How are the returns encoded? What is the extra information?
  - reading section 3.1, it is unclear how the attention mechanism incorporates the information of other agents, and how this is supposed to help coordination.
  - the term "opponent" or "opponent modelling" is used repeatedly, despite the work only dealing with cooperative settings
  - Section 5.4 as a whole is unclear to me, including exactly what the Valid Ratio is measuring.

**Results**
- In SMAC, it is common to report the win rate rather than the return, because the return is much less interpretable. I would like the authors to provide the win rates.
- Figure 3 has no errorbars.
- No mention of the number of seeds used for Table 1 or Figure 3.
- The results for SMAC seem underwhelming, especially since SMAC lacks relevant stochasticity and partial observability 

**Experiment Limitations**
- While the use of 2 different MARL settings and of the NBA dataset is welcome, the paper does not evaluate MADiff in settings where coordination is particularly challenging, either due to stochasticity, partial observability or both. It also does not acknowledge any potential limitations of the method in such settings. For instance, I encourage the authors to consider environments such as SMACv2 [1], Multi-Agent Mujoco [2] or Hanabi [3].




### Questions
1. Why downsample the NBA dataset from 25 Hz to 5 Hz? How does this affect MADiff and the baseline?

2. Have the authors tried training MADiff on combined datasets of mixed quality (e.g. Good+Medium+Poor)? I suspect the additional data would benefit MADiff the most by improving the inverse dynamics model without hurting the quality of the generated trajectories when conditioning on high return.

3. The environment with the most agents is *5m6m*, which has only 5 agents. How does MADiff scale to a large number of agents?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents MADIFF, a centralized training-decentralized execution diffusion framework for multi-agent RL problems. MADIFF performs return-conditioned trajectory modeling with an attention-based diffusion architecture for information interchange among agents. MADIFF can be applied to both centralized and decentralized execution settings. Especially in the decentralized execution, MADIFF performs the opponent modeling, predicting the other agents' joint observations based on its local observation. In the experiments, MADIFF generally outperforms the baselines in MPE and is competitive in SMAC. For the MATP problem, MADIFF-C significantly outperforms the baseline.

### Strengths
1. A Diffusion-based offline MARL algorithm (an extension of DecisionDiffuser to a multi-agent setting) is presented, with a suitable attention mechanism for information interchange among agents in MARL.
2. In the experiments, MADIFF generally outperforms the baselines. The ablation study confirms that the proposed attention modules were indeed helpful.

### Weaknesses
1. The novelty of the work seems a bit limited. MADIFF heavily relies on the existing work DecisionDiffuser (Ajay et al., 2023), and it can be seen as its simple extension to the MARL setting, with an additional attention layer that processes information exchange among agents. Adopting an attention mechanism for multi-agents itself does not seem to be a new idea. (e.g. [1,2])
2. More baseline (MADT-KD [3]) could have been compared in the experiments.
3. MADIFF relies on the inverse-dynamics model (IDM) for action selection, but it can be suboptimal when the transition dynamics are stochastic. In MARL, even though the underlying environment is deterministic, if we see the other agents as a part of the environment (thinking of decentralized execution), the transition dynamics (by other agents' actions) will be stochastic when other agents' policies are stochastic. Even in this situation, doesn't using IDM cause any problems?

### Questions
1. In the top-middle of Figure 2, why is the planned trajectory of the planning agent (purple) different from the real sampled trajectory?
2. MADIFF relies on the inverse-dynamics model (IDM) for action selection, but it can be suboptimal when the transition dynamics are stochastic. In MARL, even though the underlying environment is deterministic, if we see the other agents as a part of the environment (thinking of decentralized execution), the transition dynamics (by other agents' actions) will be stochastic when other agents' policies are stochastic. Even in this situation, doesn't using IDM cause any problems?
3. If we view the MARL problem as a single-agent problem (by viewing joint action space as a single-agent large action space & joint observation space as a single-agent observation space), how is MADIFF-C different from DecisionDiffuser? Is MADIFF-C still performing better than DecisionDiffuser which operates in the joint observation/action space?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel diffusion-based offline multi-agent learning framework, called MADIFF. Specifically, MADIFF proposes the attention-based architecture in Section 3.1 to interchange information and learn coordination between agents. MADIFF is also designed with centralized training and decentralized execution, inherently enabling the framework to perform the opponent modeling during execution. Evaluations in MPE, SMAC, and MATP show the effectiveness of MADIFF against competitive baselines.

### Strengths
1. Overall, the paper is very clearly written achieving the SOTA results compared to baselines.
2. MADIFF is a principled diffusion-based framework without needing complicated components to achieve effective performance. 
3. Code is available for reproducibility.

### Weaknesses
Overall, I enjoyed reading this paper and learning about MADIFF, but there are a few questions that I would like to follow up on:
1. Because MADIFF needs to predict the next observations (Equations 8 and 9), I would like to ask whether MADIFF can be applied to domains with high-dimensional inputs (e.g., image). I noticed that the experimental domains have relatively small dimension inputs. 
2. In Equation 9, inferring all other agents' observations could be very difficult when $N$ is large. Could MADIFF scalability benefit by inferring only the agent $i$'s neighbors instead of all $N$ agents?
3. Can MADIFF be applied to general-sum settings or would it be limited to cooperative settings only?

### Questions
I hope to ask the authors' responses to my questions outlined in the weaknesses section.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes MADiff which incorporates diffusion models for either a centralized planner or decentralized actors. The diffusion model builds on Decision Diffuser (Ajay et al., 2023) and additionally uses an attention layer for better coordination among the agents. The training procedure enables the decentralized policies to have opponent modeling capabilities where agents predict the observations of other agents. MADiff is evaluated on SMAC and MPE as well as the NBA Dataset for trajectory prediction.

### Strengths
The use of diffusion models for offline MARL is interesting and this combination is, as far as I know, novel. Diffusion models have shown promise in offline RL due to its potential for stitching and generalization capabilities. In this context, whether diffusion policies can improve offline MARL is an important problem, and it is interesting to view this from the lens of opponent modeling. Furthermore, viewing offline MARL as trajectory prediction makes it more scalable without requiring restrictive assumptions such as IGM. Finally, the attention mechanism which is the main difference between Decision Diffuser and MADiff seems important in the offline MARL setting, as shown in the ablation studies (Section 5.5).

### Weaknesses
1. The overall structure of the paper and algorithm is very similar to Decision Diffuser (Ajay et al. 2023), but with an additional attention layer.  
2. The benefits of using diffusion policies mentioned in Decision Diffuser, such as generating novel behaviors, stitching or different conditions for $y(\tau)$ such as constraints or skills are not addressed in MADiff in the context of MARL. 


3. The inverse dynamics loss in Eq. 7 looks a little strange since the observations $s^i, s^{i’}$ are used, which makes it unclear what this is predicting, since other agents’ actions as well as partial observations are involved. This is essentially assuming that the next state observation only conditions on the current local observations and local actions. This may be fine for simple tasks but may not translate to more complex tasks where the other agents’ actions impact the dynamics. Also, the notation $s^i$ is confusing here since Section 2 uses $o^i$. 
4. Only a small number of agents (3-5) are considered in the experiments . 
5. While opponent modeling is mentioned as one of the contributions, previous work in opponent modeling are missing from the Related Work section (e.g. [1] and references therein) and there is no explicit mention about what kinds of information are available at test time (e.g. only local observation-action history of ego-agent). 
6. OMAR is excluded from SMAC tasks as a baseline despite OMAR also reporting SMAC results. 
7. (Minor) The perturbed states $\tilde x$ in $\hat \tau_k := [s_t,\tilde x_{t},... ]$ above Eq. 4 are not properly defined.
8. (Minor) Grammatical error in 5.4: “We that..”

### Questions
1. How do diffusion models address the curse of dimensionality of the joint action space? How does MADiff scale as $N$ increases?
2. In the second paragraph of the Introduction, do you mean that “learning the $\textbf{incorrect}$ centralized value for each agent…”? Does this mean that extrapolation error can occur even when the correct value is learned, or is this a typo?
3. Please address the points raised in Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers cooperative multi-agent problems within the centralized training decentralized execution paradigm. The paper proposes the first multi-agent method to use a diffusion model in order to generate trajectories during online execution. The advantage of using a generative model to create policies is that the diffusion method is able to learn from behavioral data with severe extrapolation errors. Prior value-based methods are unable to do this due to the updates from out-of-distribution points. Additionally, prior methods have yet to apply this type of method to multi-agent cases. The paper introduces a novel attention-based diffusion model for multi-agent learning which combines CTDE, opponent modeling, and trajectory prediction. The paper evaluates on benchmark CTDE environments with offline data available and finds that their method tends to perform better.

### Strengths
+ Using diffusion to model the agents in multi-agent learning is a very interesting premise. There is great potential for this method to be quite impactful in a multi-agent learning context. The ability to generalize from the value-based methods may prove useful given a way to combine this with online finetuning. This may be interesting for future work on foundation models in this area.

### Weaknesses
 - This is a very interesting paper but there are unfortunate issues with the experimental design. SMAC (Version 1) has known issues. There is a recent version that was recently accepted at NeurIPS but has been released for a while that fixes the “open-loop” issues of SMACv1 called SMACv2[1]. Given that these tasks were essentially solved by the community with in the easy maps that are compared with in the results, the results may not be as convincing as currently indicated. Why is the score for SMAC so low. Typically the SMAC reported value is winrate, which should be near 100% for these easier SMAC tasks, especially with QMIX. There must be a bug in the evaluation or the data is far to limited to evaluate the method properly.
[1] Ellis, B., Moalla, S., Samvelyan, M., Sun, M., Mahajan, A., Foerster, J. N., & Whiteson, S. (2022). SMACv2: An improved benchmark for cooperative multi-agent reinforcement learning. arXiv preprint arXiv:2212.07489.

- Regarding the other experimental design items, it is unclear what hypothesis the MPE environments test that would not be tested by SMAC. For the MATP, this seems like a niche task. It is unclear if the test games have a distribution of trajectories that are out of distribution of the training/validation set. Otherwise, it is hard to understand the generalization capability of the method.

- How does the centralized control version scale with the number of agents? It is unclear if this is a useful avenue of exploration compared with the CTDE paradigm.

- Regarding Q6, I do not believe that this is a fair comparison with respect to empirical comparison. It is hard to say whether the diffusion aspect or the attention aspect is helping the method increase the performance. If a comparison of just your method with and without the attention mechanism existed, would there be an increase in performance? I think the use of diffusion is very novel and interesting, but I am having trouble being convinced that the results are strictly due to the diffusion aspect.

### Questions
I still do not understand the “Decentralized policy and centralized controller” terminology. I assumed that this means centralized training decentralized execution (CTDE). The new language is confusing.

Is an attention network used for all comparison baselines?

Please see Weaknesses for additional questions.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
