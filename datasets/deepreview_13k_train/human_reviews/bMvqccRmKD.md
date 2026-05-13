# Towards Generalizable Reinforcement Learning via Causality-Guided Self-Adaptive Representations

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
General intelligence requires quick adaption across tasks. While existing reinforcement learning (RL) methods have made progress in generalization, they typically assume only distribution changes between source and target domains. In this paper, we explore a wider range of scenarios where not only the distribution but also the environment spaces may change. For example, in the CoinRun environment, we train agents from easy levels and generalize them to difficulty levels where there could be new enemies that have never occurred before. To address this challenging setting, we introduce a \textit{causality-guided self-adaptive representation}-based approach, called CSR, that equips the agent to generalize effectively across tasks with evolving dynamics. Specifically, we employ causal representation learning to characterize the latent causal variables within the RL system. Such compact causal representations uncover the structural relationships among variables, enabling the agent to autonomously determine whether changes in the environment stem from distribution shifts or variations in space, and to precisely locate these changes. We then devise a three-step strategy to fine-tune the causal model under different scenarios accordingly. Empirical experiments show that CSR efficiently adapts to the target domains with only a few samples and outperforms state-of-the-art baselines on a wide range of scenarios, including our simulated environments, CartPole, CoinRun and Atari games.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work augments model-based methods such Dreamer with a mechanism for facilitating policy adaption. The method is evaluated on a synthetic task, a modified CartPole with changing dynamics, CoinRun (Procgen) and 5 Atari games with modes and difficulty levels enabled.

**Claims**

C1. The method distinguishes between and addresses two situations: i) distributions shifts ("changes in transition, observation or reward functions") and ii) state/action space expansions ("differences in latent or action spaces")

C2. Causal representation learning (as employed here) uncovers the structural relationships among variables, enabling the agent to autonomously determine in which of the two situations they are in.

**Assumptions**

Identifiability of the model parameters assumes conditional independence between estimated states at different time-steps (Markov condition) and the (stronger?) faithfulness assumption.

Identifiability of the "expanded state space" further assumes linearity, but provides empirical evidence of monotonic correlation between estimated parameters and the ground-truth for simple cases.

### Strengths
- the problem tackled here is difficult and highly relevant. Generalization under variations of the underlying dynamics is an area that has shown little progress
- paper is well structured, fairly easy to follow and the description of the method appears to be complete
- I take the results on the toy synthetic task in fig 3a and the modified CartPole experiment to be the most clear evidence in supporting C1 and C2.
- the ablation on the expansion mechanism suggests that indeed the performance gain is not merely correlated with the increased capacity of the estimators but with the quality of the approximation of the underlying causal graph.

### Weaknesses
 - The paper would benefit from more qualitative analysis in support of C1 and C2. For example graphs showing the evolution of $\mathcal{L}_{\text{pred}}$ and the ratio between the two modes of the algorithm (distribution shift detection and space expansion). What I am going for is whether it would be possible to visualize a correlation between a task and which mechanism is selected during adaption to that task.
- I take the empirical results on Atari to be somewhat weak, with the baseline (Dreamer) often performing statistically insignificantly from the proposed method. Furthermore I would encourage the authors to make a more principled selection of environment when training on a small subset of ALE, for example Atari-5 or Atari-10 games that support tasks [1].
- I have some reservations regarding the way the distinction between the two scenarios is presented. Given that for any number of tasks we could write down the full MDP using a single transition (and reward) matrix, I believe it could be better exemplified not through CoinRun (which is fairly opaque) but maybe through a simple Factored MDP or a structural causal model.

### Questions
- Given that we can describe any two tasks as a single MDP with an SCM that contains a task variable that takes values in ${0,1}$ and which can be used to activate/deactivate other state variables, couldn't the method drop the expansion mechanism? Shouldn't learning $D$ and $\theta$ be sufficient to identify the underlying changes in the MDP?
- Is the Dreamer baseline configured to account for the extra learned parameters of CSR (eg. does it have the same state size as CSR eventually reaches)?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a novel model, CSR to enhance RL generalization across diverse and dynamic environments. CSR tackles distributional changes and environmental space variations, such as introducing new elements or challenges. CSR uses causal representation learning to identify latent variables and structural relationships, enabling agents to recognize and respond to environment changes more efficiently. The approach is structured around a three-step process: detecting shifts, expanding the model when necessary, and pruning irrelevant variables for task-specific learning. Experimental results show that CSR achieves faster adaptation and better performance than existing methods on tasks like CartPole, CoinRun, and Atari games.

### Strengths
- This paper is well-written. The structure of CSR is clearly explained, and the authors provide some technical details. 

- The three-step CSR framework (detection, expansion, and pruning) is well-structured. It provides a systematic way to handle different environment changes, contributing to effective and efficient policy adaptation.

- Including ablation studies and comparative evaluations for various expansion strategies (random, deterministic, self-adaptive) provides valuable insights into the effectiveness of different design choices.

### Weaknesses
 - CSR's effectiveness depends on accurately identifying latent causal variables and relationships. In noisy or complex environments, causal discovery can be error-prone, impairing the model's adaptability and leading to suboptimal or even incorrect adaptations. Therefore, it is necessary to see whether CSR can work in a complex environment or task. Specifically, the reliance on observational data for causal inference, without explicit interventions, may limit the robustness of the learned causal model, particularly when dealing with unobserved confounders or feedback loops. The paper should include experiments in more complex environments with higher dimensional state and action spaces to demonstrate the scalability and robustness of the approach.

- Techniques like causal representation learning for domain adaptation, adaptive policy updates, and structure discovery in RL are not entirely new. Many recent papers explore causal inference within RL and adaptive mechanisms for generalization, such as AdaRL. I cannot tell if this paper's novelty differs from AdaRL. The paper needs to more clearly articulate the specific differences and advantages of CSR compared to existing methods, particularly in terms of the problem setting and the proposed solution. A more detailed comparison, highlighting the unique aspects of CSR, is needed to justify its contribution.

- Based on my understanding, $\theta$ is trained on the data collected from the target domain. Therefore, how does CSR adapt to an unseen task? The paper should clarify how the model handles the scenario where the target task is significantly different from the training tasks, and how the learned causal structure can be effectively transferred or adapted to such novel situations. The current description lacks clarity on the generalization capabilities of CSR beyond the observed task distributions.

- The self-adaptive strategy, which searches for the optimal structure of causal variables, can be computationally intensive. Can authors clarify the training cost for each step of CSR? The paper should provide a detailed analysis of the computational cost associated with each step of the CSR framework, including the time and resources required for shift detection, model expansion, and pruning. This analysis should also discuss the scalability of the approach to more complex environments and tasks.

- CSR concentrates on improving the performance of an RL agent with causal representation in dynamic change environments. I am inquisitive about how CSR compares to other curriculum RL methods regarding sample efficiency and final performance, such as ALPGMM. The paper should include a comparison with curriculum learning methods to evaluate the sample efficiency and final performance of CSR, as the problem setting of dynamic change environments can be seen as a curriculum of tasks.

### Questions
Refer to the questions above.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduce *causality-guided self-adaptive representation* (CSR), for RL agents. It introduces a causal world model into RL agents, that allow them to distinguish two types of environmental changes:
1. distribution shifts
2. State/Action space expansion. 
The causal world model generates the next observation and can be adjusted if the predicted observation differs too much from the observed one, allowing to detect that the environment has changed.

Thus, the authors evaluate their baselines on different sets of environments such as the famous Atari and Procgen.

### Strengths
**Interesting and novel motivation**. The idea to use causality to distinguish different types of changes is interesting, and might be one of the most promising directions to allow RL agents to generalize past their training environments.

**Soundness of the method**. The method is overall sound.

**Overall clarity**. The overall structure of the paper makes it quite easy to follow and understand the method. The clarity ~can be~ has been improved (as detail led below).

**Broad experimental evaluation**. The experimental evaluation is broad (Procgen+Atari), and demonstrate the superiority of CSR in terms of pure performances to the baselines. The Atari modifications of the environments have been introduced in [1], it would be nice to cite them.

[1] Farebrother, J., Machado, M. C., & Bowling, M. Generalization and regularization in DQN. arXiv (2018).

### Weaknesses
Several points are unclear: 
* **Implicit world models** CSR still encodes an implicit world model. The learned world models cannot be interpreted. The use of causality had me first think of the contrary. It could be nice to insist on this point. Explicit RL reasoning agents have also been developed ([1, 2, 5]). Specifically, the paper does not clarify how the causal relationships are extracted from the latent space, or how these relationships are used to guide the agent's policy. The method seems to learn a latent representation and then applies causal discovery techniques, but the connection between the discovered causal graph and the agent's decision-making process remains opaque. This lack of transparency makes it difficult to assess whether the causal model is truly guiding the agent or if it's just another layer of abstraction.
* **The difference between the two types of change is not clear**. Beside the apparent effort of the authors to explain this point, I'm still unsure of the difference, and it's a core contribution. I would advise using the MDP in the introduction, explaining how the MDP is modified for this type of change. For example, a distribution shift could be framed as a change in the transition probabilities or reward function, while a state/action space expansion would involve adding new states or actions to the MDP. This distinction needs to be made more explicit and connected to the formal definition of an MDP.
* **What are the answered scientific questions?** The experimental evaluations can be reorganized in terms of scientific questions (Q1 learning ability, Q2 adaptivity, Q3 core components for performances, i.e. ablation)... 

A potentially striking point for the paper would be:
Could a causal world model help mitigate misgeneralisation/misalignment problems ([2, 3]) ? The misalignment detected in [2] on the *LazyEnemy* variation of Pong [4] (where they show that RL agents tend to follow the vertical position of the enemy instead of the ball) is quite striking. A causal world model, that could then update itself to detect that the Enemy is following the ball instead of the contrary could there help, couldn't it ?
A discussion on this issue or its use in introduction/future work could demonstrate the potential benefit of causal WM in RL.

### Questions
* how does CSR compare with the other methods in terms of added parameters and training/inference time ?

### Soundness
4

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
The authors introduce a new algorithm, Causality-guided Self-adaptive Representation-based approach, or CSR. CSR aims to allow an RL agent to quickly adapt to novel tasks which are similar to previous tasks, but involve changes in various latent variables. These latent variables are divided into a state and a "task-specific change factor"; changes in these correspond to distributional shifts and shifts in the environmental structure, respectively. 

CSR uses a world model, which consists of probabilistic mappings that approximate observations, rewards, transitions, and next-state inference functions. Within these models are various causal masks, which screen-off some conditioning variables, inducing a sparse causal structure. 

Three theorems are given which show that the world models and their sub-components are identifiable under certain assumptions. 

Details are then given for how CSR operates:
* How the world model is trained
* How distributional shifts are detected
* How the state-action space is modified when distributional shifts are insufficient to capture changes in observations

Lastly, experiments are done showing that, compared to various existing methods, CSR performs favorably following changes in the environment

### Strengths
Overall, I liked this paper a lot, and thought it contained many good ideas. I was impressed by the experimental results. 

Originality: 
- The core of the method proposed by the paper (uncovering structural relationships between latent variable to allow for quick adaptation to novel environments) is, to my knowledge, a new and creative contribution. 
- Moreover, the algorithm is non-trivial, and involves multiple steps. The authors have solved numerous problems in order to create a pipeline which works.  

Quality: 
- The algorithm proposed by the paper, CSR, works well, and can outperform policy transfer with existing algorithms. 
- The authors perform numerous experiments across different domains to demonstrate the performance of CSR. 
- Solutions to various problems are not ad-hoc, and seem well-motivated. 
- Finally, the authors provide multiple theoretical results which justify their approach.  

Clarity: 
- The writing was in general good, and the paper had a nice overall flow.

Significance: 
- Transfer learning is an increasingly important topic in ML, and the authors do a good job of tackling the problem head-on.

### Weaknesses
The main weakness of the paper was that, at various points, the paper under-specified various implementation details for the algorithm. This significantly hurts the reproducibility of the work. Leaving various details under-specified in the main text would have been acceptable if the algorithm in the appendix (page 19, line 1013) filled in these details, and the main text included pointers to that appendix. Currently, the algorithm in the appendix is even less helpful for clarifying implementation details than the main text is! If the text and appendix are modified so that another research could *actually* reproduce the algorithm from the descriptions given, I think it likely I would increase my rating from borderline reject (5) to accept, good paper (8). A reader should not have to guess what you are doing - it ought to be clear from the text; otherwise it makes it very challenging for others to build upon your work. The method is very complicated - and while this is not a bad thing in and of itself, it does mean that care is needed to be clear about how the many aspects of the method work, and how they fit together. At present, that care has not been shown. If you are low on space in the main text then this is exactly the purpose of an appendix. My questions have illuminated at least some, but not all, of the points where implementation details are unclear for the paper. 

(315) - "Let $d'$ denote the number of causal variables to be added, we first determine the value of $d'$ and introduce new causal features." This is not good grammar. Replace the comma with a period. 

(319) - You say that the "existing parts of the world model are fine-tuned". Does your method suffer from catastrophic forgetting of previous tasks, or does it retain performance on task $M_1$ after going through tasks $M_2, \dots, M_9$ (for example)? Additionally, can you clarify why fine-tuning takes place, given that the previous model is intended to capture the existing relationships between variables? 

(361) - You say that $D$ can "[transition] from $1$ to $0$ during model estimation". But earlier, in line (168), you say $D$ is a binary mask, i.e., each element is in $\{ 0, 1 \}$. It's unclear to me whether $D$ is a continuous or discrete variable, or whether you threshold $D$ at some point, and if so, at which point and how. Please clarify this, and (if necessary), remove the claim that $D$ is binary. Also, is $D$ constrained in $J_{\rm reg}$? Can it be negative?

(371) - The policy is conditioned on the state - how is the state generated? Presumably Thompson sampling through your world model. Is that correct? This detail should be in the paper. 

(377) - "we train the newly added structure in the policy network while finetuning the original parameters". Train how? You haven't given sufficient details as to how you learn a policy. It looks deterministic, so is trained through DDPG? Or some other method? This is a very important detail! 

A final note - it is not exactly clear to me where to position your method within the literature, or what problem it seeks to pose. At first, it seems as though it is a continual learning algorithm. But you don't test on a continual learning problem - you test on sequential learning. So is the imagined use-case for the algorithm simply adaptation to tasks in sequence?  

Additionally, it appears that CSR requires notification whenever the task has changed. But this is surely a weakness compared to policy adaptation methods, which can just continue training on the incoming data without being informed of a distributional shift.

### Questions
(140) - "In each period, only a replay buffer containing sequences from the current task is available, representing an online setting." I'm not sure I understand the reasoning here. If one maintains a replay buffer for each task, and tasks are encountered sequentially, why can't you access a replay buffer for a previous task during the current task? 

(276) - In the expression for $J_{\rm rec}$, is there meant to be a log around the second probability term? 

(276-283) - Can you clarify what exactly you mean by the expectation under $q_\alpha$ in the definition of $J_{\rm KL}$ and $J_{\rm rec}$? Importantly, are the $s_{t-1}$ and $s_t$ sampled afresh according to $q_\alpha$, or recalled from the memory replay buffer? Are gradients passed through these samples, or are they held fixed? Do you pass gradients through the samples using analytic expressions for the KL-divergence, via the reparametrisation trick, or by a REINFORCE/score-function style estimator? 

(276-283) - I would also appreciate clarity on what the objectives are a function of. I'm assuming they're functions of $\phi, \beta, \alpha$, but they could also be functions of $\theta$. This just isn't clear from the main text. 

(293) - "Therefore, in this step, we exclusively updates [sic.] the domain-specific part $\theta_i$, while keeping all other parameters unchanged". Can you be more specific about how these updates are done? Are they done using the objective $J$? How many updates are performed? Do you train to convergence? With early stopping? Using a train/validation split? 

(303) - "Upon implementation, we use the final prediction loss of the model on the source task as the threshold value". This threshold seems to stringent in my mind. If there is some noise in $L_{\rm pred}$ (which would occur simply because the loss is sample based), then if $M_2 = M_1$, you would expect that on half of occasions the threshold would be violated, simply because of the noise. Am I missing something here? If not, can you confirm that this doesn't happen when $M_2 = M_1$.

### Soundness
3

### Presentation
3

### Contribution
3
