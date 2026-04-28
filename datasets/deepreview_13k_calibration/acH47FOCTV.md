# Direct Advantage Estimation in Partially Observable Environments

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Direct Advantage Estimation (DAE) was recently shown to improve sample-efficiency of deep reinforcement learning algorithms. However, DAE assumes full observability of the environment, which may be restrictive in realistic settings. In the present work, we first show that DAE can be extended to partially observable domains with minor modifications. Secondly, we address the increased computational cost due to the need to approximate the transition probabilities through the use of discrete latent dynamics models. Finally, we empirically evaluate the proposed method using the Arcade Learning Environments, and show that it is scalable and sample-efficient.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper extends and improves an existing off-policy reinforcement learning (RL) algorithm called direct advantage estimation (DAE) to the setting of partially observable environments. 

The paper motivates learning advantage functions, as opposed to value functions, given their more stable learning dynamics. Then, it explains how DAE can work in the off-policy case by separating the return in two advantage functions: one associated with the actions of the agent and the other with the transitions, interpreted as environment actions. Based on this separation, the paper re-introduces value and advantage functions as functions of observation (and action and reward) histories, rather than states, and provides an optimization problem whose minima contain the real value and advantage functions. 

Moreover, it is explained that, since some of the constraints in the optimization problem depend on having access to the real dynamics, there is a need for some type of approximate model. As a solution, the paper introduces a predictive recurrent architecture that models the dynamics of the environment in an embedding space, mimicking a discrete version of variational autoencoders (VQ-VAEs). 

Finally, the paper evaluates the performance of the algorithm based on return maximization in 5 different Atari environments, including some ablations. The results show that the algorithm can compete with state-of-the-art methods like Rainbow with a considerably smaller number of samples, that the off-policy correction introduced by the use of the environment's advantage function is critical to compete with existing techniques, that there are diminishing returns on the multi-step size considered to estimate advantages, that frame-stacking can be replaced by an LSTM given that the algorithm supports partial observability, and that naive truncation of the history can be detrimental.

### Strengths
Originality:
- The paper makes use of a simple modification to a previously introduced concept to be able to leverage previous theory. In particular, the paper redefines the environment's advantage function in terms of the reward and V- and Q- value functions, as opposed to just the V-value function. This allows transferring an existing algorithm to the more challenging partially observable setting.
- The paper provides a conceptually simple predictive model in encoding space to manage the approximation of the dynamics.

Quality:
The paper is thorough in its empirical evaluation. In particular, it includes a sufficient number of seeds, relevant baselines, and multiple ablations. Some of the ablations are particularly appropriate since they provide some evidence that the algorithm does maximize return under partial observability.

Clarity:
In general, the paper is easy to read due to its simplicity and clarity. It introduces very succinctly the problem and clearly states the contributions. It also introduces all the relevant notation and explains in detail the experiments carried out.

Significance:
The paper provides convincing evidence to conclude that the proposed algorithm is state-of-the-art. In particular, it is shown that the algorithm makes use of fewer samples to obtain similar or better performance than the baselines in medium size environments that require the use of function approximation and handling some degree of partial observability.

### Weaknesses
In my opinion, there is only one weakness worth focusing on. The main contribution is supposed to be the extension of DAE to the partially observable setting, but the Atari environments chosen are arguably not challenging from the partially observable perspective. In particular, the fact that DQN and Rainbow, algorithms that are typically paired with non-recurrent architectures, can maximize rewards in them suggests that partially observability is not a big issue on them. In this sense, I think that ablation studies in these environments, for example, one comparing frame-stacking vs. LSTMs, are not as effective as choosing tasks where partial observability is a crucial factor for good performance. 

Now, while I consider that the paper should be accepted in its current version, I think that a higher score requires considering more appropriate environments. For example, see Pašukonis et al., Evaluating Long-Term Memory in 3D Mazes, in ICLR, 2023.

### Questions
- What is the computational overhead of the predictive model?
- In line 246, why is $\hat{x}$ being called an information vector?

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper extends and improves upon Off-Policy Direct Advantage Estimation, both by extending it to the POMDP case by modifying the way the loss is computed, but also by modelling the transitions in the latent space of a VQ-VAE, which improves the computational cost of training models with DAE.

### Strengths
The theoretical analysis is quite complete and sound, and the authors bring techniques from other subfields of Reinforcement Learning (World Models) to improve DAE and make it more practical.

### Weaknesses
The experimental analysis is rather weak, they compare their model with Rainbow and DQN, while using a recurrent and residual architecture signifcantly more complex and costly. Comparing with Impala and R2D2 would have been more meaningful. Besides that they report only mean and 1 standard error of their agents, whereas reporting the median agent performance and either a 2 standard deviation interval or better yet a tolerance interval would have improved the visualization of their algorithm performance.

### Questions
1. Would it be possible to compare the performance with methods using similar networks to the ones you used, like Impala and R2D2? Why did you think this comparison was irrelevant?
2. Would it be possible to report ablations on using a Exponential Moving Average network vs a periodically updated network (DQN-style) as your target network? If not would it be possible to justify the choice a bit more?

### Soundness
4

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents an extension of the off-policy Direct Advantage Estimation (DAE) method to partially observable Markov Decision Processes (POMDPs). The proposed approach demonstrates improved performance on certain benchmark problems compared to DQN. However, the notation throughout the paper is unclear, making it difficult to follow the methodology. Additionally, the baseline algorithm used for comparison is outdated, limiting the persuasiveness of the results. The motivation for applying DAE in this context is also insufficiently explained, and I find the necessity of the proposed method unconvincing.

### Strengths
1. This paper extend off-policy DAE to POMDP with minor modifications.
2. Authors address the problem of increasing computational costs by modeling the latent space transition with RNN.
3. Partial experimental results demonstrate that the proposed method has good performances.

### Weaknesses
1. The paper is hard for me to follow, and the writing could benefit from further polishing. For instance, the parameter notation $\theta$ is used in various forms, such as $f_\theta(h, a)$, $g_\theta(s, a, z)$, and $p_\theta(z|h_t, a_t)$. This raises questions about whether these functions share the same parameters, which the paper does not clarify. Additionally, the notation for $z$ in Eq. (10) is undefined until $\mathcal{Z}$ is introduced before Eq. (11), making the notation confusing.

2. The authors appear to consider only the simplest case, with finite state and action spaces. Under these conditions, why is DAE necessary, and why wouldn’t a TD loss with a Bellman operator suffice? The motivation for introducing DAE in this context is unclear and could be better presented.

3. The benchmark algorithms used in this paper date back 6-9 years, which weakens the strength of the comparison. I recommend that the authors incorporate more recent, robust baselines to more convincingly showcase the advantages of their proposed method.

### Questions
Same as the weakness.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper extend the off-policy Direct Advantage Estimation (DAE) technique into the POMDP environments with model estimation trick to reduce the complexity.

### Strengths
The idea is sound and motivation is intuitive with straightforward explanation, building upon the previous works of DAE and off-policy DAE[4,5]. The method itself has been proved effective on the Arcade Learning benchmarks. Authors have also conducted extensive experiments to validate hyper-parameters selection and various corrections.

### Weaknesses
1, line 247, 255, and 266 would be better to refer to Eq 9 instead of Eq 14 back in the appendix.
2, Though technical sound, this paper seems a bit incremental comparing with previous works[4] with a different dynamic reparameterization for high-dim state space.
3, Section 3.2 states the reduction of computational complexity comparing to LSTM and RNN based methods, but it would be great to have some empirical or theoretical demonstrations.
4, The authors claim that off-policy correction is crucial for stochastic environment and performance improvement. It would be better to explain how the stochastic part is validated. 
5, Reviewer is also interested in seeing the comparison with other recent works with support for pomdp such as [1,2,3]. Current comparisons with Rainbow and DQN might not be sufficient.

### Questions
1, Is it necessary to incorporate reward signal $r_{0:t-1}$ to the information vector $h_t$? Since $r_t$ info seems not be incorporated in the $h_t$.\
2, The reviewer is a little bit confusing on the mixing use of state $s$, $h$, $z$, and $x$. It would be great to have a better clarification on these symbols and definitions of corresponding $\hat{A}, \hat{B},$ and $\hat{V}$.\

### Soundness
3

### Presentation
3

### Contribution
2
