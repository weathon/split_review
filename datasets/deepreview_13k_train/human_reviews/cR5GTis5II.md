# eQMARL: Entangled Quantum Multi-Agent Reinforcement Learning for Distributed Cooperation over Quantum Channels

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Collaboration is a key challenge in distributed multi-agent reinforcement learning (MARL) environments. Learning frameworks for these decentralized systems must weigh the benefits of explicit player coordination against the communication overhead and computational cost of sharing local observations and environmental data. Quantum computing has sparked a potential synergy between quantum entanglement and cooperation in multi-agent environments, which could enable more efficient distributed collaboration with minimal information sharing. This relationship is largely unexplored, however, as current state-of-the-art quantum MARL (QMARL) implementations rely on classical information sharing rather than entanglement over a quantum channel as a coordination medium. In contrast, in this paper, a novel framework dubbed entangled QMARL (eQMARL) is proposed. The proposed eQMARL is a distributed actor-critic framework that facilitates cooperation over a quantum channel and eliminates local observation sharing via a quantum entangled split critic. Introducing a quantum critic uniquely spread across the agents allows coupling of local observation encoders through entangled input qubits over a quantum channel, which requires no explicit sharing of local observations and reduces classical communication overhead. Further, agent policies are tuned through joint observation-value function estimation via joint quantum measurements, thereby reducing the centralized computational burden. Experimental results show that eQMARL with $\Psi^{+}$ entanglement converges to a cooperative strategy up to $17.8\%$ faster and with a higher overall score compared to split classical and fully centralized classical and quantum baselines. The results also show that eQMARL achieves this performance with a constant factor of $25$-times fewer centralized parameters compared to the split classical baseline.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposed a novel framework for multiagent RL, based on quantum entanglement. As compared to classical CTDE approaches wherein the communication between the centralized critic and agents happens in the form of sharing observations / states, the proposed framework uses quantum entanglement for information transfer. The framework uses a split critic such that the global value is calculated by transfer of information to a central server via quantum entanglement. The authors present results on two tasks - CoinGame and multi agent cartpole, demonstrating the effectiveness of the proposed framework in sample efficient learning.

### Strengths
* The framework proposed is novel and the paper explores the rather unstudied area of using quantum entanglement for information sharing in Multi-Agent RL
* The framework distributes computations across agents, which decreases the centralized computational burden thereby making the framework more scalable
* The proposed framework minimizes the communication overhead between the agents and the centralized critic as well as among the agents via quantum entanglement, as compared to classical information sharing in normal CTDE approaches. 
* The empirical evaluation includes a nice study justifying the choice of entanglement type.

### Weaknesses
 * The paper is not easily understandable to a reader not completely familiar with the area of quantum entanglement. The appendix provides the necessary background on this. However, a brief introduction of the same (a compressed version) in the main paper might provide some context to the reader in order to better understand the paper.
* Some parts of the experimental results section (specifically, lines 363 - 374 and 412 - 425 Section 3.4 and lines 457-464 in Section 3.5) are rather poorly written. Focusing more on the general conclusions as compared to specific numbers and focusing on one metric at a time (either sample efficiency OR absolute performance)  could help improve the readability of the section.
* Although the proposed framework results in lower variance across seeds, the results on multi-agent cartpole task don't seem very encouraging. The proposed framework fails to beat the baselines in the case of both MDP and POMDP
*  The plots in Figure 3 do not immediately make the conclusions clear. Replacing Figure 3 with Tables H.1 and H.2 could be more compelling.

### Questions
* From the description provided in Appendix E.2, the multi-agent cartpole does not seem to benefit much from coordination among different agents, since all the agents operate independently. Given that, is it really a good task for evaluating the framework?
* Is it feasible to run experiments with environments consisting of higher dimensional observation spaces. For eg. running experiments on some moderately challenging MiniGrid environments would be interesting.
* Can the authors provide details on the compute required for performing the experiments?

### Soundness
3

### Presentation
2

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
This paper proposes eQMARL, a novel quantum multi-agent reinforcement learning framework that uses quantum entanglement to enable distributed cooperation between agents, demonstrating faster convergence (up to 17.8%) and better performance compared to classical and quantum baselines while requiring 25 times fewer centralized parameters.

### Strengths
1. This paper seems to be the first to use quantum channels and entanglement for agent coordination, rather than just replacing classical neural nets with quantum circuits. The split quantum critic design that maintains cooperation without observation sharing seems novel to me.

### Weaknesses
1. The approach requires sophisticated quantum hardware for generating, maintaining, and transmitting entangled states across agents - capabilities that current NISQ devices don't reliably support. Specifically, the paper does not address the challenges of maintaining high-fidelity entanglement over distances, which is crucial for distributed multi-agent systems. The reliance on perfect quantum channels and error-free quantum operations is a significant limitation given the current state of quantum technology.

2. The method's scalability remains unclear, as it's only demonstrated with simple environments and few agents, and could face significant challenges with quantum decoherence and reduced entanglement fidelity as the system grows. The paper lacks a theoretical analysis or empirical evidence to support the claim that the approach can scale to more complex environments and a larger number of agents. The potential for exponential growth in the complexity of managing entangled states with increasing agents is not addressed.

3. The experiments have too small scale for a purely empirical paper. The chosen environments, while useful for initial testing, do not adequately demonstrate the practical applicability of the proposed method in real-world scenarios. The lack of experiments with more complex environments and a larger number of agents limits the generalizability of the results.

4. (Minor) you should specify in the main paper that $\otimes$ is the Kronecker (tensor) product.

### Questions
1. How does the approach handle agent failures or dropped quantum connections? The current design seems to assume perfect quantum channels and continuous agent availability.

2. How does the choice of entanglement scheme $(\Psi^+, \Psi^-, \Phi^+, \Phi^-)$ affect the information sharing capacity between agents? Why $\Psi^+$ performs best?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Distributed multi-agent reinforcement learning (MARL) faces challenges in balancing the benefits of player coordination with the communication and computational costs of sharing data between players. Quantum mechanics offers potential for more efficient collaboration through quantum entanglement mediated information sharing, but most current MARL approaches still rely on classical information sharing. This paper introduces a novel framework called entangled QMARL (eQMARL), which eliminates local observation sharing by leveraging quantum entanglement, an input entangled state is prepared and joint measurements are performed. A quantum split critic across agents enables joint observation-value estimation without any additional classical communication overhead to share local environment observations. Experimental results show eQMARL converges faster in some cases and with fewer parameters on a central server compared to classical and quantum baselines. 

The authors perform experiments on CoinGame and CartPole environments and run these as MDP and POMDP processes using different scoring metrics. Several classical and quantum variants of MARL are benchmarked and compared for converge behaviour, stability, robustness, solution quality and space complexity. Finally, an ablation study on network size supplements the main results and provides insight into the scaling of solution quality with the number of network layers.

### Strengths
The paper describes both a novel framework and a novel algorithm which clearly outline how you can train decentralised policies over quantum channels with entangled input qubits. All that is required are joint measurements without sharing local observations amongst agents or a central server. The framework and the technical details are well outlined in Sec 2. with a detailed exposition of the entanglement preparation and the different architectural components which are outlined in Fig. 2. This makes it clear to understand its contribution which lies in the incorporation of quantum channels. As outlined, these do not require explicit agent-server observation reporting and this is a novel Ansatz which has not been explored in the literature.

The benchmarks provided are comprehensive and well presented. Especially in Fig.4 for the CoinGame comparison the eQMARL shows superior convergence dynamics and also improved scores and higher own coin rates. The observation that entanglement stabilises the network is also well put and particularly interesting. Another strong point that is clearly outlined is the idea that additional information in the case of POMPDP would supposedly result in superior performance, but actually it suffices to use entangled input states to generate good learning dynamics. This is interesting for a broader audience. 

The work's significance is also clearly outlined. For the benchmarked examples the eQMARL algorithm requires fewer centralised parameters and exhibits more stable and robust learning dynamics than the alternatives. In some cases it also achieves a better solution.

### Weaknesses
The results in Fig. 3 are confusing and deserve a clearer exposition. Given the "None" benchmark performs similarly well to all the other Bell states (presumably no entanglement? but this is not clear from the text), how one can understand the role played by the entanglement if it does not significantly outperform "no entanglement"? It would also be interesting to understand why Bell states \Sigma^- and \Sigma^+ perform differently and what role is played by the relative phase?

The cart pole benchmark does not seem to conclusively show an advantage associated with using the eQMARL framework since in both MDP and POMDP cases the authors algorithm does not achieve the maximum reward and also does not seem to clearly outperform qfCDTE (MDP) or qfCDTE and sCDTE (POMDP)even though in the text an advantage - especially in terms of a high mean average reward at early epochs - is claimed to exist. The authors should consider revising the last paragraph and making it less strongly in favour of the performance of the eQMARL algorithm.

There is no mention of the time complexity of the novel framework and particularly the challenge associated with running quantum circuits and preparing entangled input states (notwithstanding the challenge of running this in a non-simulated real quantum device). This makes the benchmarks which all run for the same number or epochs less clear. Particularly in Fig.5b the authors claim the advantage of eQMARL lies in the fact that it achieves a higher reward at a much lower epoch number, but without any information on the per epoch runtime of the different algorithms this case becomes less strong. For example if sCDTE runs 10 times faster than this would not make a strong case for preferring eQMARL over sCTDE. The authors should also consider adressing this in Section 3 when discussing the scaling and performance for different network sizes.

### Questions
In the last paragraph the authors claim that "the overall system size is larger, however, the number of central parameters is significantly reduced in the quantum cases – requiring only 1 parameter instead of 25." - can the authors dive into a space time tradeoff here, because no information about algorithm runtimes is given? Even if the eQMARL has fewer centralised parameters, what is its runtime compared to the alternatives? A discussion of this would also be important when comparing the different algorithms in Figs 3-5. 

Does the preparation of the input entangled states introduce some computational overhead, can this be quantified? How does this compare to the benchmarked alternative algorithms?

Why does \Sigma^+ perform better than \Sigma^- in the discussion of Fig.3 ? It is only the relative phase which changes not the general entanglement structure.

Why does the None benchmark in Fig.3 perform almost as well as the \Sigma^+ benchmark, is entanglement even required to achieve any advantage and why can you achieve a high score without entanglement?

### Soundness
3

### Presentation
3

### Contribution
2
