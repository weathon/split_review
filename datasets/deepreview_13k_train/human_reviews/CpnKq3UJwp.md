# Efficient Multi-agent Reinforcement Learning by Planning

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Multi-agent reinforcement learning (MARL) algorithms have accomplished remarkable breakthroughs in solving large-scale decision-making tasks. Nonetheless, most existing MARL algorithms are model-free, limiting sample efficiency and hindering their applicability in more challenging scenarios. In contrast, model-based reinforcement learning (MBRL), particularly algorithms integrating planning, such as MuZero, has demonstrated superhuman performance with limited data in many tasks. Hence, we aim to boost the sample efficiency of MARL by adopting model-based approaches. However, incorporating planning and search methods into multi-agent systems poses significant challenges. The expansive action space of multi-agent systems often necessitates leveraging the nearly-independent property of agents to accelerate learning. To tackle this issue, we propose the MAZero algorithm, which combines a centralized model with Monte Carlo Tree Search (MCTS) for policy search. We design a novel network structure to facilitate distributed execution and parameter sharing. To enhance search efficiency in deterministic environments with sizable action spaces, we introduce two novel techniques: Optimistic Search Lambda (OS($\lambda$)) and Advantage-Weighted Policy Optimization (AWPO). Extensive experiments on the SMAC benchmark demonstrate that MAZero outperforms model-free approaches in terms of sample efficiency and provides comparable or better performance than existing model-based methods in terms of both sample and computational efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers MARL in a game environment, using a model-based approach. The heart of the paper is to extend MuZero, a model-based single agent RL algorithm that incorporates planning, to the multi-agent case in a Dec-POMDP setup.  The new algorithm is called mullti-agent Zero (MAZero). The extension of MuZero is achieved by adding and modifying the 3 functions of MuZero to create 6 functions that incorporate communications and expands how predictions are made.  The paper then focuses on efficient Monte Carlo tree search (MCTS) so that the planning complexity is reasonable. Numerical studies are carried out in Starcraft multi-agent challenge (SMAC) environments.  The experiments compare to model-free and model-based methods as baseline.  The results generally show improved learning efficiency for CDTE execution.

### Strengths
The paper is a logical extension of MuZero to the multi-agent case, and builds on those ideas to create six neural network functions that underly the model.  The writing is clear and the various cost functions and parameters are well laid out.  T

The experiments push the MARL problem in terms of action space complexity, and show that the MCTS method is effective in providing good performance with reduced search.  The primary contribution of the paper is to use prediction along with the reduced search in the multi-agent setting. 

It appears that the method is generally applicable to Dec-POMDP problems under the assumptions in the paper, in particular the CDTE assumption. 

The advantage-weighted policy optimization (AWPO) is an interesting way to balance cloning loss and the reduced tree search (the optimistic value).

### Weaknesses
Ultimately, the method gains in learning efficiency for the game studied, which is an important contribution, although it isn’t clear that there is any performance gain compared to other CDTE methods.

The method seems to require global reward information at each agent during execution.

It isn't clear how the MAZero method addresses the challenge of heterogeneous agent behavior, given that the parameter sharing encourages homogeneous solutions. While parameter sharing is a common technique, the paper does not adequately address the limitations this imposes on the diversity of learned strategies. The discussion in Section 3.1 touches on this, but it doesn't provide a clear connection to how MAZero handles this potential issue. The use of a shared individual dynamic network, while intended to capture both shared and individual aspects, seems conceptually difficult to interpret. The paper could benefit from a more detailed explanation of how this network is structured and how it manages to balance shared parameters with the need for individual agent dynamics. Furthermore, the positional encoding method for distinguishing agents, while mentioned, lacks sufficient detail to fully understand its effectiveness, particularly in complex, dynamic environments.

Appendix C's discussion on Adam's effectiveness over SGD is brief and doesn't provide sufficient justification beyond the general knowledge that Adam often performs better. The lack of specific details on the optimization landscape and how Adam navigates it compared to SGD makes this point less impactful. Some of the language used, such as "ingenious" and "audacious", may be overly enthusiastic and could be replaced with more objective descriptions. The paper also refers to "real world" cases, but the experiments are confined to a game environment, which is a significant difference.

### Questions
It seems that the method assumes that the agents have access to the global reward at each step during inference?  

In Figure 6, please clarify the difference between communication and sharing.  

Section 3.1, the discussion about the degree to which a homogeneous solution is a good one is interesting and certainly depends on the particular scenario, but it isn’t clear how the MAZero fits into this.

Could you say more about the Shared Individual Dynamic Network g ?  Perhaps it is just the terminology but the idea seems confusing.  

Section B.1, could you say more about how to “use positional encoding to distinguish agents in homogeneous settings”?

Appendix C, why do you think Adam is more effective than stochastic gradient descent?  Isn't this well known?

Some small items:  Perhaps “ingenious” and “audacious” are terms better left for the reader to decide for themselves?  The paper refers to “real world” cases but ultimately this is about a game environment.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents MAZero, a model-based multi-agent reinforcement learning (MARL) algorithm that combines a centralized model with Monte Carlo Tree Search (MCTS) for policy search. The authors propose an ingenious network structure to facilitate distributed execution and parameter sharing. They introduce two novel techniques, Optimistic Search Lambda (OS(λ)) and Advantage-Weighted Policy Optimization (AWPO), to enhance search efficiency in deterministic environments with sizable action spaces. Extensive experiments on the SMAC benchmark demonstrate that MAZero outperforms model-free approaches in terms of sample efficiency and provides comparable or better performance than existing model-based methods in terms of both sample and computational efficiency.

### Strengths
* MAZero is the first empirically effective approach that extends the MuZero paradigm into multi-agent cooperative environments.
* The proposed OS(λ) and AWPO techniques improve search efficiency in large action spaces.
* Extensive experiments on the SMAC benchmark demonstrate the effectiveness of MAZero in terms of sample efficiency and performance.

### Weaknesses
 * The paper focuses on deterministic environments, and it is unclear how well MAZero would perform in stochastic environments.
* The proposed techniques may not be applicable to all types of multi-agent environments, and further research is needed to generalize the approach.
* The reliance on centralized training could limit scalability to very large numbers of agents or highly heterogeneous environments. The computational expense of MAZero, while offering sample efficiency, may be a practical limitation in resource-constrained scenarios.

### Questions
* How does MAZero perform in stochastic environments compared to deterministic ones?
* Can the proposed OS(λ) and AWPO techniques be applied to other model-based MARL algorithms?
* Are there any potential drawbacks or limitations of the proposed network structure that the authors have not discussed?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce a novel algorithm, MAZero, based on the model-based ideas in MuZero, for the multi agent setting in order to improve problems with sample efficiency. Because the model based approach requires roll-outs to select policies, an efficient method of tree search is required, and so Optimistic Search Lambda (a method which weights optimistic values more highly) and Advantage-Weighted Policy Optimization (which uses a novel policy loss function based on the optimistic search lambda values).

The authors then compare this model based MARL algorithm to a number of others on the Starcraft Multi-Agent Challenge followed by a number of ablations of the different methods.

### Strengths
The paper is in general well-written, and clear, with thorough appendices for the details. 

The results given show that this model-based approach is not only more sample efficient than model-free approaches in the MARL setting but also, importantly, tractable when the Optimistic Search Lambda Algorithm and Weighted Policy Optimization are used within the tree-search. While these results are not surprising, such an approach has not been taken before and so there is definitely originality and significance to these results within the domain explored.

### Weaknesses
 The major issue comes down to the single, very specific domain that this has been tested on. While the results are, as stated above, impressive, they are only impressive in this single domain, and it would not seem difficult to show that they are just as significant in other domains with different types of action and state spaces (continuous, discrete, visual, tabular). 

In addition, I believe that it should become standard within the community to utilise the evaluation protocol of Gorsanne et al (https://arxiv.org/abs/2209.10485) in the Multi-agent setting. These standard practices have not been followed and I believe weaken what could be a strong case for the effectiveness of these algorithms.

No discussion is given to hyper parameter tuning, or the choice of hyperparameters for the baselines that MAZero is being compared against.

On a stylistic note, the paper has a lot of grammatical typos and needs to be gone over thoroughly. An LLM should be able to pick up all of these mistakes.

I would not use the word "ingenious" in the abstract to describe your own algorithm, or, as later used "audacious".
CTDE is not spelled out the first time it is mentioned.
The different loss terms in equation 2 are not spelled out.
Is Figure 1 a single seed? It looks remarkably smooth.

### Questions
The questions all relate to the weaknesses described in the previous section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes a model-based multi-agent RL approach similar to MuZero, performing MCTS over the joint action space of all agents as imagined by learned models of the dynamics and reward. The authors propose to use optimism (Optimistic Search Lambda in conjunction with Advantage-Weighted Policy Optimization) to improve the performance over the behavioral cloning loss used in Sampled MuZero. Experiments on the SMAC benchmark compare the performance of this method with some previously proposed model-based and model-free MARL methods.

### Strengths
The paper demonstrates better or similar performance compared with several baselines. The paper is easy to follow (at least for someone familiar with MuZero and related works). Regarding novelty, I have not found any previous application of MuZero to multi-agent setting.

### Weaknesses
There are several major weaknesses of the paper.

1. The empirical validation of the method is very weak.
    1. Despite the authors proposing the method to tackle large action spaces and mentioning the 27m_vs_30m settings as a motivating example in Section 3.2, there is no experiment in these large action space settings. The largest action space tested, 10m_vs_11m, while large, does not fully demonstrate the method's scalability to the extreme action space sizes mentioned in the motivation.
    2. There’s a lack of experimental validation beyond the SMAC benchmark, and the same benchmarks settings are used across all results and ablations. For example, Google Research Football and Multi-agent MuJoCo would be candidates for other tasks. The use of a single Google Research Football task is insufficient to demonstrate the method's general applicability in that domain. Furthermore, the lack of diversity in the SMAC tasks, with many being variations of similar scenarios, limits the conclusions that can be drawn about the method's robustness.
    3. The SMAC benchmark is outdated and should be replaced by the SMACv2 benchmark, as many tasks have been shown to be trivially solvable due to the lack of stochasticity in the SMAC benchmark. The deterministic nature of the SMAC benchmark may not accurately reflect the challenges of real-world multi-agent scenarios, where stochasticity is often a key factor.
    4. The baselines used are relatively few compared to other published MARL works. There should be comparison with other recent methods like MBVD, RODE, CDS, etc. The absence of comparisons with a wider range of state-of-the-art MARL algorithms makes it difficult to assess the true novelty and performance of the proposed method.
    5. It’s not clear how many seeds the work used for the main Table 3. The work mentions 3 seeds for followup ablations, but this is too few to ensure that the performance is not due to luck. The results should be reported across at least 10 seeds. The lack of statistical rigor in the main results raises concerns about the reliability of the reported performance gains.
2. To my knowledge, the search-based component of methods like MuZero are very reduced and not significantly useful for many non-board game tasks. For example, while MuZero utilizes a large search depth for Go, it uses a very small search depth for Atari, which raises the questions of how much performance gain the search component contributes. This work mentions that it uses 5 unroll steps, which is still very small. For MCTS-based works like this one, there should be empirical investigations with respect to the number of unroll steps at both training and test time to see whether search is offering any benefits. The paper does not adequately explore the impact of the search depth and number of simulations on the overall performance, which is crucial for understanding the contribution of the MCTS component.
4. As this work mostly treats multi-agent decision problem as a single-agent RL with a very large action space, the authors should demonstrate $OS(\lambda)$ and AWPO more extensively on (single-agent) decision problems with large action space; indeed, the author could even solely consider these single-agent settings rather than bringing in the multi-agent SMAC benchmark at all. The single-agent bandit experiment in Figure 1 is too simplistic and insufficient to demonstrate the authors’ point. Also, in very large action spaces, MCTS with a limited budget (e.g. $N = 100$ MCTS simulations as considered in this work) seems very sparse and unlikely to simulate the same action multiple times from a given state. This would significantly weaken the motivation for $OS(\lambda)$, which relies on simulating each action many times from a given state. In such large action spaces, a very relevant heuristics baseline is to sample $N$ simulations (each starting with a different action) with the learned policy and simply follow the action given by the best simulation. Overall, there's insufficient experiments demonstrating that $OS(\lambda)$ and AWPO solve the stated large action space problem without suffering from unintended side-effects of the additional optimism, and there should be more trivial heuristics baselines which may also work well for searching large action spaces with a fixed budget.

### Questions
Is MCTS being performed at evaluation time, or is only the learned policy used? If search is being performed at evaluation time, there should be a quantification of the search overhead compared with baselines.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
