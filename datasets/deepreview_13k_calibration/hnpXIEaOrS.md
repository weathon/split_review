# Federated Maximum Likelihood Inverse Reinforcement Learning with Convergence Guarantee

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3

## Abstract
Inverse Reinforcement Learning (IRL) aims to recover the latent reward function and corresponding optimal policy from observed demonstrations. Existing IRL research predominantly focuses on a centralized learning approach, not suitable for real-world problems with distributed data and privacy restrictions. To this end, this paper proposes a novel algorithm for federated maximum-likelihood IRL (F-ML-IRL) and provides a rigorous analysis of its convergence and time-complexity. The proposed F-ML-IRL leverages a dual-aggregation to update the shared global model and performs bi-level local updates -- an upper-level learning task to optimize the parameterized reward function by maximizing the discounted likelihood of observing expert trajectories under the current policy and a low-level learning task to find the optimal policy concerning the entropy-regularized discounted cumulative reward under the current reward function. We analyze the convergence and time-complexity of the proposed F-ML-IRL algorithm and show that the global model in F-ML-IRL converges to a stationary point for both the reward and policy parameters within finite time, i.e., the log-distance between the recovered policy and the optimal policy, as well as the gradient of the likelihood objective, converge to zero. Finally, evaluating our F-ML-IRL algorithm on high-dimensional robotic control tasks in MuJoCo, we show that it ensures convergences of the recovered reward in decentralized learning and even outperforms centralized baselines due to its ability to utilize distributed data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a federated learning framework for Inverse Reinforcement Learning in the discounted case, which performs IRL on each individual client and then aggregate the action-value functions and reward parameters. 
There are numerous claims made in the paper appear to be invalid, which makes it questionable on the legitimacy of the proposed aggregation scheme and the theoretical claim, the majority of which itself is largely a repetition of existing analysis results.

### Strengths
The federal learning framework for Inverse Reinforcement Learning seems interesting. The proposed algorithm is intuitive and practical. The theoretical analysis is solid.

### Weaknesses
There are a few places the paper falls short.

> We note that when the $Q$-values are represented by another network with parameter $\psi$, the aggregation of the $Q$-values will simply become aggregation of model parameters.

1. The above claim made in line 282-283 implies that a neural network is linear. Correct me if I'm wrong but the common practice in federal learning is to aggregate the gradients of the functions, instead of the weights of the local updated model themselves. This claim is particularly concerning because it suggests a misunderstanding of how neural networks operate within federated learning contexts. The aggregation of model parameters directly, as suggested, would not account for the non-linear transformations learned by each client's model, potentially leading to a poorly performing global model. The paper should clarify why they chose to aggregate parameters instead of gradients, and provide justification for this choice.

2. The same claim is made for the reward function as well. Together with the first point, the proposed algorithm seems to have little to do with the theoretical results, except that if we consider a linear function approximation of both the $Q$-function and the reward estimation, which does not seems to be the focus of this work. The theoretical analysis appears to be disconnected from the practical implementation, which raises questions about the validity of the theoretical claims. If the theoretical analysis is based on a linear approximation, this should be explicitly stated and justified, and the limitations of this approximation should be discussed.

3. Since obtaining the average of the action-value function is trivialized in this paper, the proof of theorem 1 (lemma1 and 2 have already been shown in prior works, please cite properly) appear exactly the same for the most part (say, up until equation 51). Can authors elaborate the key difference and contribution of this work in analysis compared with the prior work of MLIRL? The analysis seems to be a straightforward extension of existing work, and the paper does not clearly articulate the novel contributions of the theoretical analysis. The authors should highlight the specific challenges addressed in the federated setting and how their analysis differs from existing work on single-agent MLIRL.
4. Some experiments do not seem to make sense: in more than one case, a centralized agent presented with demonstrations of medium level of performance can learn a policy that performs the best. This result is counterintuitive and suggests potential issues with the experimental setup or the algorithm itself. The paper should provide a more detailed analysis of this phenomenon and investigate why the centralized agent with medium-level demonstrations outperforms the other settings.

### Questions
1. In Alg1, line 16-20, what is the index that's being looped over and how it affects the aggregation?
2. Can the authors say more on why standard federated learning framework can't work? Judging from the implementation, it seems that the proposed framework is also just a simple aggregation of objectives, which this case, the primal and dual objectives from IRL, i.e., the action-value function and reward function.
3. It seems that in the experiments section, the proposed algorithm has a large deviation of performance, while the table does not show the standard deviation. Is this intentional?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper develops an algorithm for federated inverse reinforcement learning (IRL). The algorithm combines maximum likelihood IRL in the reference [Zeng 2022] and model averaging in federated learning. Convergence analysis of the algorithm is provided. Experiments are conducted in MuJoCo where four baselines are included.

### Strengths
1. Federated IRL is an interesting addition to the literature of IRL.
2. Convergence of the algorithm is mathematically guaranteed.
3. The paper is clearly written and easy to follow.

### Weaknesses
1. The novelty of the algorithm is quite limited. As shown in Figure 1, the algorithm consists of local training and global update. The algorithm of the local training is identical to the maximum likelihood IRL algorithm in the reference [Zeng 2022]. The global update adopts averaging, a classic approach in federated learning.
2. The introduction claims that IRL with distributed data is an open problem. The statement is incorrect. Below are some recent papers on the topic.
R1: Federated Inverse Reinforcement Learning for Smart ICUs with Differential Privacy
R2: Federated Imitation Learning: A Privacy Considered Imitation Learning Framework for Cloud Robotic Systems with Heterogeneous Sensor Data
R3: Federated Imitation Learning: A Cross-Domain Knowledge Sharing Framework for Traffic Scheduling in 6G Ubiquitous IoT
R4: Federated Imitation Learning for UAV Swarm Coordination in Urban Traffic Monitoring
R5: Distributed Inverse Constrained Reinforcement Learning for Multi-agent Systems
3. The local Q functions and the global policy are communicated. Thus, the algorithm cannot deal with continuous state and action spaces. For large-scale discrete state and action spaces, the communication overhead is high.
4. The experiments should compare the developed algorithm with some algorithms in the above references. In addition, the centralized algorithms should have the same set of trajectories as the federated IRL algorithm. Consider the case that the federated IRL algorithm has 3 clients and each client has 100 trajectories. ML-IRL should be trained over the same set of 300 trajectories.
5. There are quite a few typos in mathematical expressions. It makes difficult to verify the correctness of the theoretic results. Here are some examples.
5.1 In the soft value function of (5), \theta^i_{m,k+1} should be \theta^i_{m,k}. 
5.2 In (9), \alpha should be time-varying. 
5.3 In Theorem 1, \bar{\pi}^i_{(m,T)} and \bar{\theta}^i_{(m,T)} are never defined.
5.4 The notations in (18) and those of Step 1 on Page 8 do not match.
5.5 In Steps 1-3 on Page 8, the notations of the local soft value functions do not match.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes federated maximum likelihood IRL, an integration of federated learning and ML-IRL to handle the case where the demonstration data is distributed to a group of clients. The paper proposes an algorithm to solve this problem and provide finite-time convergence guarantee. MuJoCo simulations are used to validate the effectiveness of the proposed algorithm.

### Strengths
The topic on the integration of federated learning and IRL has some practical applications.

### Weaknesses
1. The main weakness is that the contribution is limited or is not clearly demonstrated. The paper seems to be a simple combination of federated learning and ML-IRL, and the current presentation largely follows ML-IRL. It is possible that there are some unique challenges caused by combining federated learning and ML-IRL, and these challenges do not appear in ML-IRL nor federated learning. However, the current presentation does not clearly demonstrate what the unique challenges are. I highly suggest the authors to outline the unique tenchincal challenges of this paper. From the current presentation, the problem formulation and the algorithm are simple combinations of federated learning and ML-IRL. For example, the problem formulation (4) is almost the same as the problem formulation in ML-IRL. The only difference is that the upper-level problem is now distributed. Also for the algorithm, lines 7-12 in Algorithm 1 are just the policy update and reward update of ML-IRL. Lines 17-19 are also standard practice in federated learning to aggregate parameters. Can the authors specify the unique challenges solved by this paper or some unique mechanisms proposed by this paper?

2. The discussion with the most relevant literature is lacking. In introduction (line 49), it is said that "We note that IRL using decentralized clients and distributed data is an open problem." However, there are already some distributed IRL works that can handle distributed data and distributed clients. The authors do not discuss the distinctions from these works, and even do not mention these works. By a simple search in Google with the keyword "distributed inverse reinforcement learning", I can find the following papers that solve for distributed demonstration data: 
 
[1] Distributed inverse constrained reinforcement learning for multi-agent systems  
[2] Distributed inverse optimal control  
[3] Distributed estimation and inverse reinforcement learning for multi-agent systems

[1] and [2] both provide theoretical guarantees. I highly suggest the authors to compare with the existing distributed IRL methods given that they are the most relevant works to this paper.

3. The motivation of solving for distributed data needs to be better justified. The introduction (line 41) says that "demonstration data in practice are often distributed across decentralized clients". Why? Can the authors provide some concrete applications or scnarios to justify this?

4. It is said in related works (lines 159-160) that "However, existing FL methods could not be directly applied to the ML-IRL problem with decentralized clients, since ML-IRL requires a bi-level optimization involving both policy improvement and reward estimate using maximum likelihood." This sentence is also questionable. Basically, this sentence means that FL methods cannot be directly used because this problem is bi-level. However, there are already some theoretical papers on federated bi-level optimization (see below):

[4] Communication-Efficient Federated Bilevel Optimization with Local and Global Lower Level Problems

[5] Achieving Linear Speedup in Non-IID Federated Bilevel Learning

[6] FedNest: Federated Bilevel, Minimax, and Compositional Optimization

Can the authors discuss why these works cannot solve the problem? I highly suggest the authors to discuss the distinctions from the most relevant literature in detail, otherwise, it is hard to see the contribution of this paper.

### Questions
What is the unique challenge solved by this paper other than simply combining federated learning and ML-IRL? By unique challenges, I mean the challenges that do not appear in ML-IRL, federated learning, and distributed bi-level optimization.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors extend the maximum-likelihood formulation for IRL to the federated setting, i.e., when data is shared across multiple devices and subject to privacy constraints. Then, the authors provide both a theoretical and empirical evaluation of the proposed algorithm.

### Strengths
- The authors provide both theoretical and empirical validation of the proposed algorithm.  
- The analysed problem is novel and of practical importance.

### Weaknesses
PRESENTATION:
The paper is written in a very imprecise and gross manner. Specifically: 
- Many symbols are introduced along the way since the background section in confusing and lacks some definitions.
- the related works are written very bad. It is not clear whether the authors have understood the content of some papers mentioned in the related works. For instance, in line 108 they say that "Apprenticeship learning via inverse reinforcement learning" use the recovered reward to derive an effective policy, while the authors do not recover any reward in that paper. 
- No citation for lines 144-145. Moreover, what is $f$ in Eq. (3)? 
- The preliminaries are also written very badly. 

There are many typos. Some of them are:
- 045: FL never defined  
- 107,109, ... : must use \citep instead of \citet  
- 117: "an MDP" 
- 285: "inequation" 
- ... many others 

CONTRIBUTION:
The contribution of the paper is fairly poor. While the idea is interesting, the problem is addressed in a non-adequate manner. Specifically:
- The paper is incremental: They simply take the algorithm developed by Zeng et al. (ML-IRL) and extend it in a very simple manner with some averages. While simplicity is in general an amazing tool, I believe that here it reflects a poor analysis of the problem. 
- There is no technical novelty.

### Questions
- In Eq. (4), why not weighting on the number of trajectories owned by each client? Why the average?

### Soundness
2

### Presentation
1

### Contribution
2
