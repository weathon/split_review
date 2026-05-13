# Learning Successor Features with Distributed Hebbian Temporal Memory

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
This paper presents a novel approach to address the challenge of online temporal memory learning for decision-making under uncertainty in non-stationary, partially observable environments. The proposed algorithm, Distributed Hebbian Temporal Memory (DHTM), is based on factor graph formalism and a multicomponent neuron model. DHTM aims to capture sequential data relationships and make cumulative predictions about future observations, forming Successor Features (SF). Inspired by neurophysiological models of the neocortex, the algorithm utilizes distributed representations, sparse transition matrices, and local Hebbian-like learning rules to overcome the instability and slow learning process of traditional temporal memory algorithms like RNN and HMM. Experimental results demonstrate that DHTM outperforms LSTM and a biologically inspired HMM-like algorithm, CSCG, in the case of non-stationary datasets. Our findings suggest that DHTM is a promising approach for addressing the challenges of online sequence learning and planning in dynamic environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel algorithm for learning successor features for reinforcement learning agents in non-stationary partially observable environments. The main feature of the algorithm is a new episodic memory architecture that combines ideas from Factor graphs, Hidden Markov Models and episodic control, along with a neuron concept similar to the Hierarchical Temporal Memory, which is in itself inspired by biological neurons as complex units with spatio-temporal computation. Features of this new type of memory include, efficiency of computation, distributed representations and a local (Hebbian) learning rule. The algorithm is embedded in a simple RL agent and tested, both, in a simple gridworld environment and in a more structure AnimalRL environment.

### Strengths
This paper is an very interesting contribution. The connection of successor features, factor graphs, episodic control and complex neuron morphologies is very attractive. In particular, it offers a practical computational interpretation of the role of complex morphologies in biological neural network: computing factors/features based on previous experiences. The paper covers a lot of theoretical ground in connecting the different ideas used to build the model. In general each aspect of the model is theoretically sound and the experiments are tested with a good set of baselines. I will try to be comprehensive in the weaknesses and questions with the intentions of making the contribution stronger.

### Weaknesses
1. The basis of comparison with the other baselines in experiment number 1, is the capacity of the model to forget, however, in algorithm 1, the DHTM agent includes a memory_reset() step. This seems to invalidate the whole argument of this experiment.
2. The connection with biology is only superficial, but I think it can be made stronger. It is not clear if some of the things I am going to mention are already in the authors minds, but they are definitely not clear in the text:
- The activity of each of the neurons in the model is associated with a spike only makes sense if there are two different timescales at play, so that you can collect many spikes before making a decision (this is what firing rate means). Do the neurons only spike once per episode/state visited?
- The appendix does not explain very clearly the connection of your model with HTM is not very well explained (and the citation of Hawkins paper is not the appropriate paper, choose one in which they explain the model). For example, it is never clear what you mean by the receptive field of a cell.
- Explain better how the computation of Fe relates to the columnar structure of the cortex? The authors seem to be confusing the morphology of one neuron with the structure of the cortex (this is related to the connection with HTM above). One is related with the sort of computations performed, the other with the origin and information carried by the afferents.

3. The presentation style is probably the weakest point of this paper. It is very difficult to follow. At the start, the definition of a POMDP is very difficult to read, adding a bit more words can make this and other definitions easier to read (if they are in the paper, they will be read by someone, otherwise they can go in the appendix).
- Many things are explained in the wrong place, before or after they appear in any equation. For example rec(l) for the receptive field, or the definition of log Li.
- The calculation of the emission factors E is never shown explicitly! but it appears in equation 7
- Equation 7 is not well justify at all, it is very difficult to see how you go from (4) to (7)
- Many times it is not clear what is part of your algorithm and what is you explaining the old way of doing things, for example: line 191- "the feature variables are considered independent (in this work?), however, the are interdependent (so which?).
- Similar to the previous one, in the exposition of algorithm 2, it seems that you are sometimes talking about DHTM and sometimes about the naive EC agent.

4. The scope of the paper seems a bit misleading. If the focus is the learning of successor representations for non-stationary environments, why not testing it in more standard and more complicated environments than the ones shown in this paper? The experiments are barely non-stationary and not the usual testing ground for comparison with the baselines chosen. As I said, I think this is a very interesting idea but I think the scope needs to be made more realistic or add the necessary tests. This makes me think that there is some problem with scaling the presented ideas; if that is the case what is it?
- Do the number of segments grow fast or exponentially with the complexity of the environment (please show evidence otherwise). The factors are defined in terms of combinations of ALL the RVs involved!
- Is the computation as efficient as suggested? Is having segments more efficient as claimed? How fast? (the results are shown in action steps but no mention about memory/time efficiency)
- What is the capacity of the memory?

5. Definitely needs more figures! figure 1 is infinitely complex, it has a lot of information (more than 3 sections worth of information). This figure can be split to illustrate different aspects of the exposition. For example, the details of the computation of LogLi can be added in a later figure. In relation to the figures, figure 6 also needs more information. Mark what the goal and the start position is (the colors have barely any contrast and someone with visual impairments could not get any information from this figure)

6. Others
- It is not clear to me how are new segments created
- the change from Fe to fl for the emission factors was confusing, please add some warning
- The calculation of the conditional probability on the features in 294 is only tangentially mentioned, but it is very important, here is the only time the features are introduced, and it deserves some discussion
- How is the planning horizon "T" determined. How are you measuring the shape of the distributions to determine this parameter?
- The explanation of the Episodic control agent needs to be rewritten for clarity.
- In equation 10, make clear that Rt is the reward coming from the environment (there are other definitions for Rt before)
- It took me some time to understand that each neuron is a state, and each neuron is also a factor. It is not clear how the population of neurons is set up. It seems that we would need to keep adding neurons with longer experiences? Again, it will be very helpful if the architecture and computations are separated from figure 1.
- 291,292, please explain this step.

### Questions
Any of the weakness are also questions.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel algorithm for online temporal memory learning in decision-making tasks with non-stationary / partially-observable environments. Distributed Hebbian Temporal Memory is a biologically-inspired algorithm that uses Hebbian learning rules in order to learn Successor Features, a powerful framework in reinforcement learning to decouple the environment's dynamics from the reward function.

### Strengths
- DHTM operates fully online using local learning rules due to its local Hebbian learning rules, making it well-suited for non-stationary environments without needing explicit resets or retraining. Its ability to dynamically form and update memory representations allows it to cope with sudden changes in the environment effectively. Furthermore, you can train it fully online since it doesn't require backpropagation through time. 
- The algorithm is computationally efficient due to sparse transition matrices and distributed representations, and could be potentially implemented efficiently in neuromorphic hardware.
- The experiments indicate that DHTM could achieve higher sample efficiency compared to some state-of-the-art models. For example, in the AnimalAI environment, DHTM requires significantly fewer interactions with the environment to learn effective policies than models like Dreamer V3.

### Weaknesses
 - The unique encoding of each observation sequence limits the model's ability to generalize across different sequences which represent the same underlying state.
- The performance of the algorithm is very close to that of Episodic Control on some tasks, which leads to a question of its advantage over a similar method. 
- The baseline models like LSTM may not be fully optimized for online learning, potentially skewing the comparison results.
- The paper lacks a thorough theoretical analysis of the algorithm's properties such as convergence guarantees and computational complexity.
- I think you should have more exposition explaining what CSCG, Episodic Control, and Dreamer V3 are.
- I am willing to improve my score if you address some of the questions posed in the following section.

### Questions
- Can you talk about how to incorporate mechanisms that enable the model to generalize across different sequences leading to the same state. Would hierarchical or abstract representations be useful here?
- It would be nice to see a experiment that shows a substantial improvement of the DHTM model over Episodic Control, or an explanation of why it's better to implement the full algorithm. 
- In the AnimalAI task, you only test DHTM with VAE whereas all of the other algorithms are only tests with k-means. Is there a reason why you can only test DHTM with VAE and not the others? If it's possible to test the others with VAE, I would be interested to see that in a comparison.
- It would be worthwhile to see the performance of Modern RNN architectures (such as LRU or RKWV mentioned in the beginning of the paper) instead of LSTM, unless there is a reason those architectures don't apply to these tasks. These algorithms also avoid using BPTT and are quite performant.
- Can you comment on how the architecture compares to other Temporal Memory architectures that are based on Hebbian Learning Rules such as Sequential Hopfield Networks? For example, how does it relate to Chaudhry et al. 2024 (Long Sequence Hopfield Memory) or Tang et al. 2024 (Sequential memory with temporal predictive coding). I think you should add a more thorough literature review of temporal memory.
- I would like to see the effect of an oracle on Episodic Control and DHTM in Figure 4.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces Distributed Hebbian Temporal Memory (DHTM), a model inspired by the HTM neuron (modeled after cortical columns) for spatial-temporal learning. The model takes in a sequence of observations generated from a trajectory through an environment and generates a hidden state representation. These are then used to predict the cumulative distribution of future states under a uniform policy to form a Successor Feature (SF) representation. This is then subsequently used by an RL agent to estimate the Q value (assuming the reward can be decomposed linearly) for action selection.

The authors perform experiments on GridWorld and AnimalAI environments and compare DHTM to LSTM and CSCG baselines, showing that it outperforms both, reaching the goal state in a few number of states in fewer episodes.

### Strengths
- The model proposed by the authors is novel and formulated using the factor graph framework, making it theoretically-grounded, allowing for techniques in that area to be easily applied.
- The model is online and uses local learning rules, which makes it more applicable.
- The model is biologically inspired and the authors make specific connections to its neural implementation/plausibility.
- The authors provide an interpretation of the model in terms of episodic control.

### Weaknesses
 - The description of DHTM is difficult to follow. I suggest adding paragraph-level divisions to clarify the logical structure of the sections, or at least outline the general structure of the section at the beginning.
- Since the model uses a factor graph formalism, I think having a section for that in the background would improve clarity.
- How does the DHTM scale? The experiments applied the model to 5x5 and 10x10 environments. What if the environment had a larger number of states and a larger number of actions? How does this affect the computational complexity and loss curve?
- How well does DHTM handle partial observability? Can it distinguish aliased observations well?
- CSCG has been shown to learn the spatial structure of the environment which allows for generalization during navigation. Can DHTM do the same?

### Questions
- How does the DHTM scale? The experiments applied the model to 5x5 and 10x10 environments. What if the environment had a larger number of states and a larger number of actions? How does this affect the computational complexity and loss curve?
- How well does DHTM handle partial observability? Can it distinguish aliased observations well?
- CSCG has been shown to learn the spatial structure of the environment which allows for generalization during navigation. Can DHTM do the same?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a new bio-inspired algorithm, Distributed Hebbian Temporal Memory (DHTM), for online learning to make decisions under uncertainty. This algorithm resembles a model of episodic memory, or a dynamic trajectory buffer, which remembers and replays sequences of actions which were rewarding in the past. It is implemented by compartmentalized neurons, with dendrites that recognize particular previous states and encourage recall of associated actions, and learning is realized by a Hebbian-like rule on these dendrites. The method is evaluated on two navigation tasks (GridWorld and AnimalAI) and compared against a few baselines -- LSTM, CSCG, and a simplified episodic controller which it resembles in performance.

### Strengths
* Exploring how bio-inspired neural networks can implement and perform inference on statistical models is an interesting opportunity for interplay between AI and neuroscience.
* The experimental evaluation of the method is reasonable and with some more detail would support its effectiveness.
* The discussion of limitations of the method in the conclusion is thoughtful and thorough.

### Weaknesses
 * The method is somewhat misrepresented in the introduction. What exactly it's meant to accomplish is not clear, and it's compared alongside very general learning methods which are meant to generalize effectively. After reading the entire paper, its focus seems to be on learning simple, non-generalizable strategies quickly.
* The description of the model is difficult to follow. A huge amount of notation is introduced, and much of it is not defined precisely and has to be inferred from context. This is most problematic in section 3.2, where the bio-inspired implementation is described. Ideally the neuron model would be laid out, and then the variables of the neuron model would be associated with variables from DHTM. The use of terms like 'compartmentalized neurons' is vague without a clear definition of how these compartments function and interact within the model. The connection between the mathematical formulation and the biological inspiration is not clearly established.
* Key details of the experiments, particularly how the baseline models were tuned, are missing and make it difficult to evaluate them. For example, the specific hyperparameter settings for the LSTM, CSCG, and the simplified episodic controller are not provided, making it impossible to assess whether these baselines were given a fair comparison. Furthermore, the training procedures, such as the number of training epochs or the optimization algorithms used, are not specified, which is crucial for reproducibility.
* The paper presents a simple episodic control-based model which is highly competitive with the much more complicated DHTM which it focuses on. It is unclear what the advantages of DHTM are compared to this simple model. The core distinction between the two models, particularly in terms of their representational capacity and learning mechanisms, is not sufficiently highlighted. The paper does not provide a clear justification for the added complexity of DHTM given the comparable performance of the simpler episodic controller.
* There is no substantial discussion of related work.

### Questions
* To my knowledge the term "temporal memory" is not in common use and should be briefly defined when it is used in the abstract.
* The distinction between requiring "complete data sequences to be available during training" (lines 53-54) and "access to only one sequence data point at a time" (lines 61-62) is not clear to me.
* "Factor graph formalism" should be defined in the introduction.
* "local Hebbian-like learning rules ... make the learning process much faster than gradient methods" (lines 70-71) should be revised to clarify in which sense "faster" is meant.
* Eq. (3) is unclear because of the summation over $\Omega_k$. I believe this is meant to express summation over all possible values of the "previous time step RV indexes [sic] included in the $F_c^k$ factor" which should be clarified.
* What is meant by "$f_l$ is proportional to several coincidences $s_l = c_t^j = 1$ in the recent past" (line )? 
* Isn't the VAE encoder in section 4.2 significantly more expressive than the k-means encoder? Doesn't this give DHTM-vae an advantage as the only model with this representation?
* It is claimed that the paper shows that "unlike CSCG and table EC, DHTM is able to handle distributed representations and account for statistical dependencies between variables of these representations". I'm not sure where this was shown or how.
* It may be beneficial to revise the storytelling in the introduction to emphasize the points raised in the conclusion that this is a weak but very fast form of learning which may complement a slower, more accurate method over the course of learning.

### Soundness
3

### Presentation
3

### Contribution
2
