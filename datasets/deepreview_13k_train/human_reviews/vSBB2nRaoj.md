# Bi-Directional Goal-Conditioning on Single Policy Function for State Space Search

- Decision: Reject
- Scores: 3, 5, 3

## Abstract
State space search problems have a binary (found/not found) reward system. However,
in the real world, these problems often have a vast number of states compared
to only a limited number of goal states. This makes the rewards very sparse for
the search task. On the other hand, Goal-Conditioned Reinforcement Learning
(GCRL) can be used to train an agent to solve multiple related tasks. In our work,
we assume the ability to sample goal states and use the same to define a forward
task (τ ∗) and a reverse task (τ inv) derived from the original state space search
task to ensure more useful and learnable samples. We adopt the Universal Value
Function Approximator (UVFA) setting with a GCRL agent to learn from these
samples. We incorporate hindsight relabelling with goal-conditioning in the forward
task to reach goals sampled from τ ∗, and similarly define ‘Foresight’ for
the backward task. We also use the agent’s ability (from the policy function) to
reach intermediate states and use these states as goals for new sub-tasks. Further,
to tackle the problem of reverse transitions from the backward trajectories,
we spawn new instances of the agent from states in these trajectories to collect
forward transitions which are then used to train for the main task τ ∗. We consolidate
these tasks and sample generation strategies into a three-part system called
Scrambler-Resolver-Explorer (SRE). We also propose the ‘SRE-DQN’ agent that
combines our exploration module with the popular DQN algorithm. Finally, we
demonstrate the advantages of bi-directional goal-conditioning and knowledge of
the goal state by evaluating our framework on classical goal-reaching tasks, and
comparing with existing concepts extended to our bi-directional setting.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a way to sample and relabel goals to increase the sample efficiency of an off policy goal reaching agent. To do this, the authors propose three different state-goal samplers. The explorer, the scrambler and the resolver. 

The explorer tries to solve the original task of reaching desired goals from the starting states.  The scrambler inverts this problem. The scrambler is started from the desired goal states of the original task and tries to reach the starting states of the original task. The resolver samples subgoals or waypoints which balance two objectives:
1) are reachable from the original start states and,
2) the original goals are reachable from them.

The authors instantiate this method using a DQN agent and perform experiments on many grid world MDPs.

### Strengths
The idea of sampling waypoints can be very beneficial for sample efficient goal reaching. The paper recognizes this correctly.

### Weaknesses
Weakness:
1) It seems as if there is an implicit assumption (which should be explicitly stated) that the environment is reversible. That is, the start states can always be reachable from the goals states. This is not always true, for example you can't "uncook" food. More precisely, the method assumes that for any goal state *g* and start state *s*, there exists a sequence of actions that can take the agent from *g* to *s*. This assumption is critical for the scrambler component and should be clearly stated and justified, along with a discussion of its limitations.
3) Theoretically, there is no proof provided that the sampling method proposed can learn a meaningful goal conditioned policy. I understand it is difficult to provide any theoretical guarantees for relabeling methods, and perhaps this is out of scope of the paper. But, see the next point.
4) All experiments are performed on extremely simple toy MDPs where judging the benefits of a complex goal sampling technique can be difficult. Moreover, the proposed method SRE-DQN doesn't perform the best in any of the tasks. The grid world environments are too simplistic to demonstrate the potential of the proposed method. The state spaces are small and the optimal policies are relatively easy to learn, even without complex goal sampling strategies. The lack of complex dynamics or high-dimensional state spaces makes it difficult to assess the true value of the proposed approach.
5) It is surprising that the success rate on such simple MDPs is lower than 20%. For example in a 3x3 MDP, both the SRE-DQN and HER get around 0 success rate. I suspect that an error in the implementation is causing this. The reported success rates are unexpectedly low, suggesting potential issues with the implementation or hyperparameter tuning. The fact that established methods like HER also perform poorly raises concerns about the experimental setup.
5) Implementation details as well as the code have not been provided.

### Questions
Suggestions for improvement and minor questions:
1) After reading just Section 1, it is unclear how the agent can collect trajectories starting from the goal state. If this is a assumption that the authors are making, then they should state it clearly in the introduction. They should also state why this assumption makes sense, and what are its limitations.
2) In Section 4, 2nd para the authors state : "Scrambler generated backward trajectories from goal state adversarial to the explorer". Why are the goal state adversarial to the explorer?
3) What are "state space search" problems? Is this the same as goal conditioned RL problems where the goal space is equal to the state space?


Typos:
1) Section 2, 2nd para: simiilar -> similar
2) Section 3, 4th para: In the reward definition, $+1$ should be in the subscript. 
3) Section 4, 3rd para : generated -> generates
3) Section 5.1, 4th para:  multi-directional) -> there is no corresponding opening bracket.
4) In Section 3, para Surrogate Objective for Goal-conditioned RL:  $\tau$ -> $\tau^*$

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposes Scrambler-Resolver-Explorer (SRE), which extends hindsight experience replay (HER) with bi-directional goal conditioning. SRE consists of three modules, Explorer, Scrambler, and Resolver for both the usual exploration and backward trajectory sampling from (original) goal states. It aims at gathering more samples close to the goal state region for more efficient training. They evaluate the proposed approach and compare it with baseline methods in NChain and GridWorld.

### Strengths
- The GCRL problem is an important problem, especially in terms of having controllability connecting the agent and its state in the environment.
- Given the employed assumptions, the proposed method that uses both directions for more effective GCRL is somewhat novel and might be useful.
- The manuscript is easy to read and follow.
- The baselines for the experiments are formed to examine the importance of some of the proposed modules.

### Weaknesses
 - I believe the biggest weakness is that the empirical evaluation is done in simple environments, NChain and GridWorld. I believe that GCRL, which is about overcoming difficulties in reaching different goal states, needs environments with complexities in their dynamics to some degree (e.g., locomotion environments from MuJoCo) as testbeds.
- I have some concerns about the main assumption of the ability to spawn agents at arbitrary states, especially in the GCRL setting, where *reaching* specific goal states is the objective. Taking advantage of the simulated environments, if spawning at arbitrary states can be done without any costs, some combination of local exploration and spawning might be effective for both exploration and gathering various samples for re-labeling and goal-conditioned training.

### Questions
Please take a look at the weakness section.

### Soundness
2 fair

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This method proposes a framework called `SRE-DQN` which is a Goal-Conditioned Reinforcement Learning (GCRL) based framework where 
goal states are sampled to create both a forward and a reverse task from the primary state space search. They introduce hindsight re-labeling for the forward tasks and a concept called `Foresight` for reverse tasks. To learn reverse moves from the reverse paths, agents are initiated from these paths to gather forward moves. All these components are glued together in a framework named `Scrambler-Resolver-Explorer (SRE)`. 
Experiments are ran on toy problems with discrete state and action : `NChain` and a `Simple Gridworld`.

### Strengths
- This paper introduces an interesting exploration technique termed as `Scrambler-ResolverExplorer (SRE)`. I think the idea of learning forward and backward representations (i.e. learning how to reverse an action) is interesting in general. And this idea has similarity to [1] where a forward and backward representation of the reward is being learned.
- It is also a nice concept to try to have a distinction between an explorer, scrambler and resolver module where the primary focus of exploration of each module is distinct.





[1] Learning One Representation to Optimize All Rewards - https://arxiv.org/pdf/2103.07945.pdf

### Weaknesses
 - The experimental results presented in Figure 3 and 4 are not convincing at all. The tasks `NChain` and `Simple GridWorld` are too simple and despite that the results seem very unstable.
- All the results are single-seeded and there is no measure of variance among multiple runs. I recommend the authors to present multi-seeded results over at least `10` random seeds per run to ensure reproducibility.
- `Figure 3` : All methods including the `HER` and `RE` baselines seem to work on-par and `SRE_NITR` diverges on the 10Chain. And on 15Chain all methods perform the same.
- `Figure 4` : Mixed and unstable results. The proposed method `SRE_NC` seems to have divergence issues.
- There has been more work for exploration in RL, looking at expanding trees and search - for example [1] which can potentially be a baseline.
- The framework still operates under a simple discrete states and action setting building on `DQN`. The authors claim that nothing is preventing 
the framework to being extended to a continuous setting. However given the performance on the simpler setting, I'm not convinced it can readily be extended.
- HER has been tried on many grid world navigation tasks. I recommend to the authors to redo a literature survey on this to pull more related work.
- The writing and flow of the related work can be improved significantly. For instance, there is a related work section on `Surrogate Objective for Goal-conditioned RL` going through equations for the Lipschitz continuity assumption and Wassersetein distance and its not even relevant to their framework. Overall this makes reading the paper more difficult because I don't need to see the equations for related work.

### Questions
- Why is the HER baseline failing in Figure 4 ? If the reward is sparse and binary, HER should be resampling goals, why does it fail completely?
- Did the authros try other exploration mechanisms apart from `ϵ-greedy` ? For instance `Curiosity-driven Exploration` , or `Max-Entropy-RL` methods?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
