# Learning Task Belief Similarity with Latent Dynamics for Meta-Reinforcement Learning

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Meta-reinforcement learning requires utilizing prior task distribution information obtained during exploration to rapidly adapt to unknown tasks. The efficiency of an agent's exploration hinges on accurately identifying the current task. Recent Bayes-Adaptive Deep RL approaches often rely on reconstructing the environment's reward signal, which is challenging in sparse reward settings, leading to suboptimal exploitation. Inspired by bisimulation metrics, which robustly extracts behavioral similarity in continuous MDPs, we propose SimBelief—a novel meta-RL framework via measuring similarity of task belief in Bayes-Adaptive MDP (BAMDP). SimBelief effectively extracts common features of similar task distributions, enabling efficient task identification and exploration in sparse reward environments. We introduce latent task belief metric to learn the common structure of similar tasks and incorporate it into the real task belief. By learning the latent dynamics across task distributions, we connect shared latent task belief features with specific task features, facilitating rapid task identification and adaptation. Our method outperforms state-of-the-art baselines on sparse reward MuJoCo and panda-gym tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper uses the bisimulation metrics to measure task similarity and learn the common structure across tasks for rapid task identification and adaptation in meta-RL.

### Strengths
- The proposed method is well formulated and clearly presented.
- The effectiveness of the latent task belief metric is validated by theoretical guarantee. 
- Experiments demonstrate the superiority of the proposed method over strong baselines, especially the generalization capabilities to OOD testing tasks.

### Weaknesses
 - The topic of online meta-RL is kind of old. 
- The core of the proposed method is using the reward and state transition functions $p(s’,r|s,a)$, or called world model, to measure task similarity in a latent space and hence infer task belief for context-based meta-RL. This kind of task inference has been investigated by existing works like VariBAD. 
- The baselines are kind of old, mainly 2019-2021.
- The key difference and advantages over VariBAD could be further enhanced and elaborated, since both infer task beliefs using the world model.
- Some notations are not well explained and kind of confusing, e.g., $z_l$ and $z_r$ are confusing, and why use two distributions?
- The proposed method is motivated by the bisimulation metric, which is originally proposed for deterministic MDPs (Castro, 2020). Can the proposed method scale to stochastic MDPs?

### Questions
- No major flaws with the paper. The key difference and advantages over VariBAD could be further enhanced and elaborated, since both infer task beliefs using the world model.
- Some notations are not well explained and kind of confusing, e.g., $z_l$ and $z_r$ are confusing, and why use two distributions?
- The proposed method is motivated by the bisimulation metric, which is originally proposed for deterministic MDPs (Castro, 2020). Can the proposed method scale to stochastic MDPs?

### Soundness
4

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
3

### Summary
This paper presents a novel framework called SimBelief, which effectively extracts common features of similar tasks using the Bisimulation metric for meta-RL tasks.

### Strengths
This paper is generally well-constructed and well-motivated and provides some theoretical background on the proposed method.
In addition, the paper has the potential to help the community understand the use of latent embedding for task generalization.

### Weaknesses
The paper includes many symbolic notations, which can confuse readers without strict and coherent representation. For example, in Fig 2, it seems $q_{\phi}$ outputs h, but the notation of Eq. (6) or others in the manuscript, $q_{\phi}$ outputs $z_r$. This inconsistency between the figure and the equations makes it difficult to track the information flow within the model. Furthermore, the role of $h$ as an intermediate representation is not clearly explained, and its relationship to the task belief $z_r$ is ambiguous.

Similarly, some of the notations are used before proper definition, which hinders the readers from fully understanding the contents. For instance, the use of $N$ in Sec. 2.1 is not defined before its usage, and the concept of inverse dynamics in Definition 2 and Eq.(3) is introduced before a formal definition is provided. This lack of proper sequencing of definitions and their application makes the paper harder to follow, requiring the reader to infer the meaning of symbols from context, which is not ideal for a technical paper.

The paper's reproducibility is questionable as it consists of various complex components for the framework. The interaction between the context encoder, the latent dynamics model, and the bisimulation loss is not fully transparent. The lack of a detailed algorithm or pseudocode in the main body of the paper makes it difficult to understand the exact implementation details. The paper would benefit from a more thorough description of the training procedure and the specific hyperparameters used.

### Questions
(1) Regarding readability: In Sec. 2.1., N is not properly defined before use. Inverse dynamics in Definition 2 or Eq.(3) is used before it is properly defined.

(2) Some of the manuscript's functions are unclear. What is the output of inverse dynamics $I_{i}^{\pi}(s_i^{+},s_i^{',+})$ ? 
What is the input and output for $q_{\phi}$, $\psi_{l}$, $\psi_{r}$ ?

(3) Similarly, In Algorithm 1, it is unclear $b_{r}^i={q_{\phi}(z_r^i|\tau_{:t})}_{0:T-1}$ means. 

(4) What are the $L_{rec}$ and $L_{bisim}$ in Figure 2? If they are defined in the manuscript differently, please use the same notation.

(5) How to determine a proper $w_r$? and how sensitive is it to the overall framework?

(6) The proposed method is complex and contains various components, so presenting only a simple algorithm raises questions about reproducibility. Do the authors plan to release the code for the benefit of the RL community?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a novel meta-RL method tackling the problem of efficient task identification in sparse reward settings, where methods that do reward reconstruction are not sufficient.  In a context-based meta-RL framework, they propose inferring the latent task representation through a Gaussian mixture of a variational latent representation and a new task belief similarity latent representation the authors introduce.  This task belief similarity latent is trained to model a  bisimulation-inspired latent task belief metric between two tasks.  They demonstrate modest improvements compared to prior methods in sparse reward, simulated locomotion and manipulation tasks and robustness to OOD task variations.

### Strengths
* Introducing ideas of modeling task similarity to meta-RL is interesting and worth exploring
* Sound experimental setup and results

### Weaknesses
The biggest weakness is that the proposed method lacks motivation and reasoning about how they achieve the claims the authors make.
* Combining the variational task belief $z_r$ with their proposed task belief similarity $z_l$ through a Gaussian mixture.  This does not combine both types of task representations, but instead samples from one or the other.  Furthermore, $z_r$ already models dynamics information in order to reconstruct the trajectory, so it's unclear what information $z_l$ adds. This is also flawed because the task belief similarity is not modeled as a distribution (at least based on Section 3.2).
* There are a couple things in Section 3.3 that are mentioned briefly but not explained: using the Q-function to train offsets for the task similarity distributions and minimizing KL divergence to the variational task belief $z_r$ when predicting $z_l$.  These details seem important to the method and the fact that the KL divergence is required to “ensure the agent does not confuse similar tasks” indicate that $z_l$ may not be as effective as the authors claim.

Other major weaknesses include:
* Clarity of writing.  The method section, especially 3.2, was difficult to understand.  The experiments section does not describe what the different tasks are in each environment, and Figures 4 and 5 are hard to interpret.
* Insufficient discussion of relevant related work, especially MetaCURE, which seems to tackle the exact problem of task ID with sparse rewards.
* Insufficient discussion of results, especially providing insight into why comparison methods may under or over perform.
* No ablations provided.

### Questions
* Why is the inverse dynamics required in Definition 2?  Have you done any ablations for how it compares to the bisimulation metric?
* What are the offsets mentioned in section 3.3 and how are they trained?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work considers meta RL, especially these sparse reward settings. This work proposes to utilize bisimulation metrics to extract behavioral similarity in continuous MDPs and proposes SimBelief, which can extract common features of similar task distributions. This work further theoretically validates the effectiveness of the latent task belief metric in BAMDPs. Experiments show the effectiveness of SimBelief, especially in sparse reward settings and o.o.d settings.

### Strengths
- It is novel to include Bisimulation to measure the task similarity.

- Sparse reward is a hot topic in the meta RL community.

- Several experiments show that SimBelief performs better than several baselines, especially in sparse reward settings.

### Weaknesses
 - The writings of the proofs are poor with several typos.

(1) in lines 714-715, the value function update should be $V_{n+1} = ... V_n$

(2) in lines 719-710, $d^n$ here seems to be $d$

(3) in lines 733-739, why we can use the Lipschitz property of the value function to get the result? It seems the core to prove the result but the proof does not include a detailed discussion of this inequality.

(4) If you use the Lipschitz property of the value function, what is the Lipschitz constant?

(5) The proof of Theorem 2 is even more poor and needs to be thoroughly polished.

- The baselines compared in the paper are somehow old. The latest baseline in this paper is MetaCURE and  HyperX, which were published in 2021. There are several much more new baselines for meta RL, especially sparse reward settings or o.o.d. settings like [1-3], which should be discussed and compared. Also, it seems the evaluation environments are designed by this paper, are these previous works utilizing these environments?

- Sparse reward is indeed an important setting in RL, but why the proposed method can boost the agent's performance in sparse reward environments? As the reward structure may be independent of the dynamic structure, "extracting common features of similar task distributions" may not benefit the extremely sparse reward settings. Assume that there are n tasks that own the same dynamic, and we can only get the reward in the terminal step, there is no way to identify what is the current task as it is independent of the dynamic structure / previous rewards. Although it is not my major concern (experiments show that the proposed method can perform better than baselines in sparse settings), it will make the paper more solid if there are theoretical analyses about why the proposed method can handle sparse reward settings.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
