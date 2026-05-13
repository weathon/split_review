# Recurrent Action Transformer with Memory

- Decision: Reject
- Scores: 3, 6, 5, 5

## Abstract
Recently, the use of transformers in offline reinforcement learning has become a rapidly developing area. This is due to their ability to treat the agent's trajectory in the environment as a sequence, thereby reducing the policy learning problem to sequence modeling. In environments where the agent's decisions depend on past events (POMDPs), it is essential to capture both the event itself and the decision point in the context of the model. However, the quadratic complexity of the attention mechanism limits the potential for context expansion. One solution to this problem is to extend transformers with memory mechanisms. This paper proposes a Recurrent Action Transformer with Memory (RATE), a novel model architecture that incorporates a recurrent memory mechanism designed to regulate information retention. To evaluate our model, we conducted extensive experiments on memory-intensive environments (ViZDoom-Two-Colors, T-Maze, Memory Maze, Minigrid-Memory), classic Atari games, and MuJoCo control environments. The results show that using memory can significantly improve performance in memory-intensive environments, while maintaining or improving results in classic environments. We believe that our results will stimulate research on memory mechanisms for transformers applicable to offline reinforcement learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose a memory-augmented transformer to use for long episodes in reinforcement learning. At a high level, their approach augments a decision transformer with a recurrent update to alleviate the memory pressure caused by $O(n^2)$ space complexity. The authors propose different gating mechanisms applied to the recurrent state that they call "valves". They compare their model to other types of decision transformers, and perform an ablation of valves.

### Strengths
- The authors introduce a modification to decision transformers that improves performance
- The paper is fairly easy to follow

### Weaknesses
I find some of the experimental results dubious, specifically the T-Maze experiments. In particular, the fact that only the author's proposed method and the decision transformer can solve a simple T-maze task. To succeed at the T-maze task, all a sequence model must do is memorize one bit of information (left or right) for 90 timesteps. Given that Mamba and its predecessors S4/S5 have been shown to memorize much more information over 16,000 timesteps gives me pause. 90 timesteps should be well-within the memory capabilities of even the LSTM or GRU. Furthermore, a score of 0.5 is what I would expect a memory-free agent to achieve, and this is precisely the score that the Mamba/LSTM/GRU models achieve.

I suspected the authors may have made a mistake during implementation, so I examined the "T-Maze_new" directory provided in the anonymous code link. However, there is no code or references to Mamba, GRU, or LSTM, and so I am not sure how the authors arrived at their conclusion. I do not want to sound overly harsh, but reproducibility is the biggest issue facing RL today.

Furthermore, most of the experiment tasks are what I would consider poor tests of memory. As far as I understand, both T-Maze and VizDoom require storing 1 bit of information presented at the initial timestep, for a duration of less than 100 timesteps. So I would not consider this a sufficient comparison between RATE and other related work.

Finally, I do not think this paper is very novel. Using a decision transformer to solve a reinforcement learning task is certainly not novel, and there have been numerous papers that extend the context length of transformers through the use of a recurrent state. I would consider this an incremental work, which would be fine if the experiments were convincing. But they are not.

### Questions
- Why are LSTM, GRU, Mamba unable to make *any* progress beyond on a random agent on such a simple task?
    - Where is the code for these baselines?
- Why did you create your own valve/gating mechanism instead of using one of the existing methods proposed by prior recurrent transformers?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies how to design a new transformer architecture for RL tasks where history memory is needed. Due to the quadratic memory complexity of the vanilla transformer, naively expanding the context length would not result in an efficient solution to memory-intensive RL tasks. Therefore, authors propose to store memory information into a chunk that is updated after sequential processing of each segment. Through extensive experiments and detailed ablation study, the chosen memory chunk updating mechanism ---MRV--- is proven effective and superior towards other design choices.

### Strengths
## originality:
The usage of memory chunk bears some similarity to existing works but the proposed MRV is  original and interesting, to my knowledge.

## quality:
The method is well supported by its experiments and ablation studies.

## clarity:
The paper is well written. I find most of it easy-to-read.

## significance:
Efficient Transformer for memory-intensive (RL) tasks is of great need and research interest. And this paper successfully designs a novel MRV method for it. Through the experiments conducted, the efficacy and advantage is demonstrated against some baseline methods.

### Weaknesses
I have several  concerns regarding this work:
1. lack of theoretical guidance. Since there is no theoretical guidance towards the design of RATE/MRV, I  think they are  likely empirically determined. This somehow shadows the contribution of this work. But I understand demanding this is beyond the scope.
2. ablation study. As Transformer itself is prone to many hyperparameters, I hope to see more ablation studies regarding various components of RATE (details in questions)

### Questions
1. what is "cached hidden states"? It is mentioned multiple times throughout the paper but lacks a clear definition.  
2. which Positional Encoding (PE) is used? Do you use any PE in MRV module?  
3. could you provide some experiments comparing RATE to ERNIE-Docs? The code change should be just minimal from TrXL  
4. in your Table 1, the performance of DMamba in T-Maze is quite lower to DT under the same context window (K = 90). Why is this?  What is the corridor length?   
5. I hope to see more of ablation studies. Especially about the capacity of memory chunk, the length of segment $S_n$ and the number of layers of transformer.  In appendix F, some of them seem to have been performed but  are correlated  with the "cached hidden states" and I don't quite understand what you're ablating on
6. could you show the  attention map  of causal and cross attention  during evaluation of the method ?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents the Recurrent Action Transformer with Memory (RATE), which extends a transformer model with a recurrent memory mechanism for offline reinforcement learning. RATE utilizes memory embeddings, caching of previous hidden states, and the Memory Retention Valve to help effective decision making which depends on the history information. Experimental results on memory-intensive environments, Atari games, and MuJoco control environments show that RATE is especially effective when the environment requires memory.

### Strengths
1.	This paper is well-organized and a lot of details are included.
2.	RATE is validated on various memory-intensive environments. The results demonstrate RATE achieves good performance on different tasks and environments.
3.	The related works are well-studied and discussed.

### Weaknesses
1.	The idea of using the transformer for offline reinforcement learning tasks is not novel. At the same time, the motivation for Memory Retention Valve is not well explained.
2.	It seems that the hyperparameters of RATE are specifically tuned for each environment. At the same time, there are a lot of hyperparameters of RATE, which makes the tuning a really heavy workload.
3.	It is unclear that the hyperparameters of the compared baselines are tuned carefully.

### Questions
1.	Why could the Memory Retention Valve significantly improve the performance of RATE in memory-intensive environments? Could the authors give some examples or further explanations?
2.	As there are a lot of hyperparameters, is there some guidance to tune each of them?

### Soundness
2

### Presentation
3

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
This work investigates the use of memory mechanisms for the Decision Transformer (DT) architecture, a formulation of the offline RL problem as sequence modeling that leverages a transformer network. The motivation is that the vanilla DT does not present an explicit memory mechanism, and the context length is limited due to the quadratic complexity of the attention operation. To address this limitation, the paper proposes RATE, an architecture that conditions the DT architecture with a learned memory embedding. This memory is updated via a Multi-Head Attention module (namely Memory Retention Valve). This module ensures that past sub trajectories can affect future ones, extending the effective context window of the model. The work provides empirical evaluation in several classic and memory-intensive environments, presenting results that are comparable or superior to DT and other memory-augmented architectures.

### Strengths
- The work is well-written and easy to follow.

- The methodology looks simple yet effective; while the use of multi-head attention modules for memory is already present in the literature [1], the use for decision transformers looks novel (to the best of my knowledge).

- While there are some concerns in the evaluation setup (see below), the number of experiments is extensive and covers diverse environments. The MRV ablation (RQ3) is particularly interesting.

### Weaknesses
 - The major concern regarding the work is that the presented empirical evidence does not justify the motivation of straightforwardly assuming the sequence modeling framework for decision-making. It is unclear how this performs in comparison with the standard offline RL or behavior cloning (with simple memory architectures) for memory-intensive environments. For instance, all presented baselines (DT, TrXL, RMT, DLSTM, DGRU, SSM) assume the sequence modeling framework, which is naturally memory demanding. It would be important to contextualize with other simpler architectures, to understand what the gains are of assuming such a modeling framework. It is unclear if sequence modeling is actually needed/helpful for the considered benchmarks. For instance, presenting results of simple LSTM with CQL and (filtered) behavior cloning (as in the DT paper [2], but for memory-intensive environments) would help clarify this.

- The evaluation setup from VizDoom-Two-Colors is questionable. The work leverages a pre-collected dataset that apparently is biased towards one of the colors. The bias does not look slight as it greatly affects the performance of DT, for instance. The choice of considering this dataset ended up considerably affecting the evaluation, as all experiments were required to control for the color. A much simpler solution would be to train a new policy in the environment and ensure this effect does not happen. Why not take this alternative path? The biased data puts in question if the proposed method is indeed performing better than the baselines or if this result is particular to this configuration.

- Appendix D describes that RATE is trained without the feed-forward network because this leads to better results, but it is unclear why that is the case. Also, it is unclear if this same design choice would lead the other baselines to better results. There is no ablation on that, and this choice makes comparisons against the other methods not completely fair.

- The data collection procedure for the Memory Maze (Appendix D) looks arbitrary. Why does the work change the initial sampling timestep following the described rule? 
    - Also, the sampling horizons for Atari and MuJoCo are much shorter than the standard for the benchmarks (which is often set to at least 200). This choice of short horizons raises the question if RATE can perform well in the classic setup of these benchmarks, which are commonly handled by non-transformer architectures.


Typo:

L148: embeddingsx -> embeddings

### Questions
- From Appendix B.1, it looks like the data collection policies are optimal or near-optimal. Is that the case? It is unclear from the description if that is indeed the case. If that is the case, it would be interesting to know how the proposed method performs with suboptimal data.

- The memory update creates a recursive relationship throughout different trajectory segments. During learning, this should lead to some form of backpropagation through time. How does RATE deal with this? Does it truncate the gradient to flow through past forward passes?

- In Figure 4, why is the performance of TrXL-3 so different from other memory-augmented architectures? Most experiments present similar results among them.


**Summary of the Review**:

The work is clear, easy to follow, and provides a diverse set of environments to show the gains of the proposed method. Nonetheless, there are some design choices in the evaluation setup that are unclear and raise questions about its soundness. Most importantly, the work should bring some simple but crucial baselines to justify and contextualize its motivation of investigating memory in RL as sequence modeling. I believe these are the points that need to be addressed in order to recommend acceptance.

**References**:

[1] Ritter et. al. Rapid Task-Solving in Novel Environments, 2020.

[2] Chen et. al. Decision Transformer: Reinforcement Learning via Sequence Modeling, 2021.

### Soundness
2

### Presentation
4

### Contribution
2
