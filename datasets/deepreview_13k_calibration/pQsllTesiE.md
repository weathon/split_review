# Scalable Decision-Making in Stochastic Environments through Learned Temporal Abstraction

- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8

## Abstract
Sequential decision-making in high-dimensional continuous action spaces, particularly in stochastic environments, faces significant computational challenges. We explore this challenge in the traditional offline RL setting, where an agent must learn how to make decisions based on data collected through a stochastic behavior policy. We present \textit{Latent Macro Action Planner} (L-MAP), which addresses this challenge by learning a set of temporally extended macro-actions through a state-conditional Vector Quantized Variational Autoencoder (VQ-VAE), effectively reducing action dimensionality. L-MAP employs a (separate) learned prior model that acts as a latent transition model and allows efficient sampling of plausible actions. During planning, our approach accounts for stochasticity in both the environment and the behavior policy by using Monte Carlo tree search (MCTS). In offline RL settings, including stochastic continuous control tasks, L-MAP efficiently searches over discrete latent actions to yield high expected returns.
Empirical results demonstrate that L-MAP maintains low decision latency despite increased action dimensionality. Notably, across tasks ranging from continuous control with inherently stochastic dynamics to high-dimensional robotic hand manipulation, L-MAP significantly outperforms existing model-based methods and performs on par with strong model-free actor-critic baselines, highlighting the effectiveness of the proposed approach in planning in complex and stochastic environments with high-dimensional action spaces.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a model-based method for planning in stochastic environments called Latent Macro Action Planner (L-MAP). Their method first learns an encoder-decoder architecture to encode return-to-go estimates, states, and a sequence of actions, which they call macro actions. The learned discrete codes are then used to learn a state-conditioned latent prior $p(z|s)$ which is used to seed a modified Monte Carlo Tree Search (MCTS). The MCTS uses progressive widening to expand the search based on the prior initialization using a heuristic based on the number of children in the tree and the number of times a state-action node is visited and uses the prior to sample children for leaf nodes. 

The authors evaluate their method in two stochastic offline reinforcement learning tasks, Hopper and Walker, and compare their method in the standard Hopper, Walker, HalfCheetah, AntMaze, and Adroit deterministic tasks. They also provide ablations over some of their hyperparameters used in their method.

### Strengths
The authors propose pre-constructing the latent search space using their learned prior and show benefits over searching without this pre-constructed prior, which is interesting.

### Weaknesses
The proposed algorithm has many layers of complexity and it is unclear which components contribute to the method's success. The two transformer-based baselines that they compare against do not utilize any temporal action compression, begging the question of if they would benefit similarly from predicting macro actions. While the authors ablate over macro action length and planning horizon, they do not provide any experiments supporting their decisions to utilize UCT for selection, progressive widening, or parallel expansion, and do not provide the values for hyperparameters $M,N,B,\alpha$ in their experiments. 

Their results also leave a lot to be desired. The only environment where the method separates itself from existing methods is in the stochastic environments, but they only test in two such environments.

### Questions
How does your method compare to versions of TT or TAP that learn macro actions?
In Table 4, you include a column named "DT". Is this decision transformer and if so, why do you include it in the results when it is not mentioned in the paper?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes Latent Macro Action Planner (L-MAP), an offline RL algorithm designed for high-dimensional continuous action spaces in stochastic environments. L-MAP learns a discrete latent space of temporally extended macro-actions to reduce the action dimensionality and simplify the planning process. A causal transformer is learnt in tandem as a latent transition model, predicting future latent codes. Planning is performed using MCTS with progressive widening. Experiments show that L-MAP outperforms model based and model free baselines in stochastic environments while being on par in deterministic environments, highlighting its versatility.

### Strengths
- Comprehensive experiments: The paper provides a suite of experiments covering multiple tasks with good model based and model free baselines. 
- The inclusion of the Adroit hand task showcases the scalability of the proposed method to high dimensional problems.
- The use of macro-actions and a pre-constructed search space allows for faster decision-making. 
- Additionally, L-MAP provides a way to trade off latency and longer planning depending on the user requirements.
- The ablation study provides insights into the importance of different hyperparameters and design choices, strengthening the paper's conclusions.

### Weaknesses
 - Could you explain the source of stochasticity in the Mujoco tasks used in the paper? Is it primarily from the dataset generating policy or are the environments themselves modified in some way?
- Why is L-MAP less performant in the deterministic environments? Is there an underlying theoretical reason for lower performance in deterministic settings given that it was more consistently the best performing algorithm in the stochastic setting?
- Could the authors study how L-MAP compares to the baselines with increasing levels of stochasticity(in either the dataset or transition dynamics) ? This can be for a single environment/task.

### Questions
- Could you explain the source of stochasticity in the Mujoco tasks used in the paper? Is it primarily from the dataset generating policy or are the environments themselves modified in some way?
- Why is L-MAP less performant in the deterministic environments? Is there an underlying theoretical reason for lower performance in deterministic settings given that it was more consistently the best performing algorithm in the stochastic setting?
- Could the authors study how L-MAP compares to the baselines with increasing levels of stochasticity(in either the dataset or transition dynamics) ? This can be for a single environment/task.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Paper focusses on stochastic planning in offline RL settings (where the data was collected by a stochastic behavioral policy). To avoid the stochasticitiy related with continuous action spaces, paper focuses on a temporally extended (latent) macro-action policy that is obtained via a vector-quantized variational autoencoder (VQ-VAE).

### Strengths
- I love the integration of primitive actions in the raw state space which is then abstracted temporally via encoders (VQ-VAE) to generate a discrete latent code. Sticking a transformer on the latent codes sounds good for creating a distribution over state and primitive action representations.

+ I think it's nice that the authors were thoughtful enough to add a conditionally widening MCTS tree to the search in the latent space to further aid the autoregressive and stochastic continuous L-MAP policy.

- Perhaps supply the examples of stochastic environments that motivated the question you asked in the Introduction.

### Weaknesses
 - Perhaps supply the examples of stochastic environments that motivated the question you asked in the Introduction.

+ I love the motivation in the introduction that many environments appear stochastic but a couple of examples where offline RL has been tried and where significant gaps in efficiency has been noticed would further strengthen the authors' argument.

+ While it's true that continuous action spaces and stochasticity in environments may make planning horizons longer, the authors would do well to mention the role of robust control or robust RL in mitigating some of these challenges whilst highlighting how their proposed method complements these existing methods;
 - In this sentiment, I am interested to see a motivation for why the authors decided to embark on the temporal abstractions proposal;

 + There is a significant body of work in continuous space RL in the realm of the viscosity solutions to Hamilton-Jacobi equations. The authors should discuss some of these in their intro/related work. Example texts:

  - A Study of Reinforcement Learning in the Continuous Case by the Means of viscosity Solutions: https://www.ri.cmu.edu/pub_files/pub1/munos_remi_1999_3/munos_remi_1999_3.pdf

  - Solving high-dimensional partial differential equations using deep learning: https://www.pnas.org/doi/pdf/10.1073/pnas.1718942115

+ Please define what sg signifies in equation (2)!

### Questions
+ How is the length of the macro action chosen? Predetermined or randomly assigned in an on-the-go fashion?

+ What are examples of real-world problems with high-dimensional continuous action spaces in the opinion of the author(s)?

+ I think you missed a couple of connecting words between lines 76 and 77. Do you want to fix those?

+ I am curious to see how this offline L-MAP policy behaves in off-policy RL settings. Can you provide an example or two?

+ L127-128: "particularly for online approaches"; why was this qualification needed seeing we are dealing only with offline RL in this paper?

+ How did you determine the instanteneous rewards, r_i, for the computation of R in equation (1)?

+ Lines 167-171, what loss function did the authors use in the reconstruction process? There have been instances in reconstruction like this when the choice of loss makes a huge difference in the reconstruction. See https://arxiv.org/pdf/2311.03534

+ What happens if instead of using the l2 norm on the embeddings regularizer, you try the l1 norm? Does it improve the repreesentation's fidelity?

+ Can you supply a proof, empirical results, ot citation for the claim on lines 213-217?

### Soundness
3

### Presentation
3

### Contribution
3
