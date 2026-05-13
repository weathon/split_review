# Offline Equilibrium Finding in Extensive-form Games: Datasets, Methods, and Analysis

- Decision: Reject
- Scores: 6, 3, 5, 3

## Abstract
Offline reinforcement learning (Offline RL) brings new methods to tackle real-world decision-making problems by leveraging pre-collected datasets. 
Despite substantial progress in single-agent scenarios, the application of offline learning to multiplayer games remains largely unexplored. 
Therefore, we introduce a novel paradigm ***offline equilibrium finding*** (Offline EF) in extensive-form games (EFGs), which aims at computing equilibrium strategies from offline datasets. 
The primary challenges of offline EF include i) the absence of a comprehensive dataset of EFGs for evaluation; ii) the inherent difficulties in computing an equilibrium strategy solely from an offline dataset, as equilibrium finding requires referencing all potential action profiles; and iii) the impact of dataset quality and completeness on the effectiveness of the derived strategies.
To overcome these challenges, we make four main contributions in this work. First, we construct diverse datasets, encompassing a wide range of games, which form the foundation for the offline EF paradigm and serve as a basis for evaluating the performance of offline EF algorithms. Second, we design a novel framework, BOMB, which integrates the behavior cloning technique within a model-based method. BOMB can seamlessly integrate online equilibrium finding algorithms to the offline setting with minimal modifications. Third, we provide a comprehensive theoretical and empirical analysis of our BOMB framework, offering performance guarantees across various offline datasets. Finaly, extensive experiments have been carried out across different games under different offline datasets, and the results not only demonstrate the superiority of our approach compared to traditional offline RL algorithms but also highlight the remarkable efficiency in computing equilibrium strategies offline.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigated how to find equilibriums in extensive form games with offline datasets. There are several main contributions made by this paper. First, motivated by the fact that offline game settings are under-explored in literatures, the paper constructed diverse datasets for benchmarking the performance of offline learning. Second, the paper designed a novel framework BOMB for modeling equilibriums with offline dataset. The BOMB integrated behavioral cloning techniques into model-based method to learn the equilibriums. Third, the paper provided solid theoretical analysis of the proposed BOMB framework. Finally, extensive experiments are carried out to demonstrate the effectiveness and efficiency of BOMB.

### Strengths
The paper provided a very comprehensive investigation into how to learn equilibriums in multi-player games with only offline datasets. There are several strengths of the paper.

Of most interest to me is the new datasets constructed in this paper. They serve as a very good benchmark for evaluating performances of future offline RL method for learning equilibriums. This has been a critical contribution to the community.

Second, the paper provided a framework BOMB for learning equilibriums with offline datasets. The authors also derived solid theoretical analysis on their method to guarantee that approximate equilibriums can be learned with BOMB. This is a great outcome.

Finally, I appreciate that the paper conducted extensive experiments on BOMB to showcase the success of their method. These empirical results complemented their theoretical analysis and really helped readers understand the algorithm.

### Weaknesses
The theoretical results are not exact and explicit enough in terms of quantifying the sample complexity. For example, assumption 4.3 requires that there is sufficient amount of data, but this kind of statement is very hand wavy. I would expect a more accurate quantification of the sample complexity. I was wondering if the authors could further improve their theoretical analysis.

### Questions
Please provide a more accurate quantification of the sample complexity.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposed the problem of offline equilibrium finding, which is to find equilibrium of a multiagent game using only offline dataset. The authors proposed BOMB, which is a method that output a policy as an interpolation of a behaivor cloning policy and a model-based MARL policy. The authors also gave experimental results.

### Strengths
The problem of offline equilibrium finding is novel.

### Weaknesses
The problem of offline equilibrium finding is novel.

The formulation of the problem is questionable. The technical contributions are limited.

The authors set an ambition goal of transferring offline RL to MARL regimes. However, my biggest concern is that there were already plenty of issues of offline RL, and adding multi-agent applications may complicate the problem more, not to mention the goal of offline MARL is questionable. Here are some detailed comments:

1. We know that offline RL have several issues. E.g., extrapolation error, distribution shift, overestimation of values. In MARL I can image these problems will even be more exaggerated. Have you observe similar issues in your studies? What is your approaches to these issues in offline MARL

2. The goal of offline equilibrium finding is even more questionable. Although the authors focus on NE or CCE which is well-defined, generally they are not unique. So how could you make sure that the state-action pairs in your dataset is essential for computing which equilibrium among all possibilities. Furthermore the offline equilibrium finding seems to highly relies on the underlying equilibrium finding algorithm you use -- whether it is CFR or PSRO. However, these algorithms themselves may introduce biases. Moreover, this paper seems to just use the vanilla version of these algorithms -- should there be any changes to address the offline setting? E.g., conservative value estimation.

3. The theoretical result looks too week. How can you be sure every state is visited. E.g., it is impossible in the game of chess or Go.

4. About BOMB How do you interpolate the two policies. Is it interpolating on the parameter space?

5. How do you apply those RL baseline in multiagent environment? Do you just let every player run this algorithm concurrently?

### Questions
The authors set an ambition goal of transferring offline RL to MARL regimes. However, my biggest concern is that there were already plenty of issues of offline RL, and adding multi-agent applications may complicate the problem more, not to mention the goal of offline MARL is questionable. Here are some detailed comments:

1. We know that offline RL have several issues. E.g., extrapolation error, distribution shift, overestimation of values. In MARL I can image these problems will even be more exaggerated. Have you observe similar issues in your studies? What is your approaches to these issues in offline MARL

2. The goal of offline equilibrium finding is even more questionable. Although the authors focus on NE or CCE which is well-defined, generally they are not unique. So how could you make sure that the state-action pairs in your dataset is essential for computing which equilibrium among all possibilities. Furthermore the offline equilibrium finding seems to highly relies on the underlying equilibrium finding algorithm you use -- whether it is CFR or PSRO. However, these algorithms themselves may introduce biases. Moreover, this paper seems to just use the vanilla version of these algorithms -- should there be any changes to address the offline setting? E.g., conservative value estimation.

3. The theoretical result looks too week. How can you be sure every state is visited. E.g., it is impossible in the game of chess or Go.

4. About BOMB How do you interpolate the two policies. Is it interpolating on the parameter space?

5. How do you apply those RL baseline in multiagent environment? Do you just let every player run this algorithm concurrently?


Some relevant papers in this direction. Could the authors compare your work with theirs:

[1] Offline PSRO with Max-Min Entropy for Multi-Player Imperfect Information Games. Luo et. al.

[2] COPSRO: An Offline Empirical Game Theoretic Method With Conservative Critic. Shao et. al.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors study offline equilibrium finding in imperfect information extensive form games. They formalize the problem and draw parallels to both the online equilibrium finding, and offline reinforcement learning (RL). They propose the BOMB algorithm, which combines two techniques from offline RL: behavior cloning and model based methods. They show that in the limit of perfect data and learning, their approach recovers the online properties. They demonstrate the applicability of their algorithm on a large number of small games.

### Strengths
I think offline equilibrium finding, the main focus of the paper, is interesting. The paper addresses both theoretical and empirical aspects of the problem. The paper is written well and easy to follow.

### Weaknesses
I believe the theoretical parts of the paper are quite weak. The theorems make strong assumptions about the size of the offline dataset, its coverage of the game, and the learning algorithm being able to perfectly learn the model of the environment. Once these are met, one can reduce the problem to the online setting, leveraging prior results. I would like to see some bound on the effectiveness of offline methods with randomly sampled datasets, assuming perfect learning. Or show how the error of the learning algorithm can affect the distance to the equilibrium similar to DeepStack (Moravcik 2017).

The BOMB algorithm seems to be a simple combination of BC and MB, with the predictor on top. I found the option of training on a smaller abstraction of a given game and scaling to a larger one quite interesting. It can maybe fit well into the offline framework, if the abstraction is created from the offline dataset. 

In your experimental analysis, I would expect some results with in the “truly offline” setting, i.e. a dataset of say human play of Kuhn poker. I would expect the offline algorithms to struggle without the guaranteed coverage of the game introduced by the random policy. This would nicely illustrate the hardness of the offline setting.

Continuing in the experimental section, I find it strange that you focus on the general sum games and NE. None of the algorithms considered in the paper has guarantees to converge to a NE in a general sum game, nor do I see a good reason the BOMB should converge closer to NE. Some of the statements in the paper related to general sum games are very strong. For example, line 506-507 if true not only contradicts your earlier statements about expert strategy datasets, but also impossibility of approximating NE well in polynomial time.

There seems to be a typo on line 223.

### Questions
1) The predictor of BOMB takes as input the similarity between BC and MB policy. That seems strange as swapping them would not affect the distance, but it would change the optimal \alpha. Did you consider other predictors, perhaps with more context?

2) On line 409, you mention that you use the grid search method in your experiments. Doesn’t that introduce bias to your results as you pick the best \alpha in each instance?

3) Fig 1, is the strategy really a NE? It seems to me p2 would choose b2 (getting reward of 2), thus p1 would prefer a1 initially.

4) In the RQ3 section (Fig 8 and 10), you show that the BOMB can outperform MB and BC. How can that not be the case when the grid search of the BOMB predictor includes both of them and more?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a method, called BOMB, for approximating equilibrium strategies in extensive-form games (EFGs) using offline datasets. It presents several datasets and proposes them as a benchmark for this task, while also demonstrating BOMB's ability to approximate Nash using them. The paper also presents some theoretical guarantees related to BOMB's solution quality given sufficient data and learned model expressiveness.

### Strengths
I think this is an important area of work that demands more attention.
* The problem setting is well-motivated; I agree with the authors that algorithms that require access to an accurate simulator or game model are difficult to apply to the real world. 
* BOMB is flexible: in case the training data is from expert play, it can weigh the behavior cloning policy more, and when the data is full of many different policies, it can use the learned environment model to compute a policy.

### Weaknesses
Though the domain is important, I found the contributions in this paper to be insufficient to claim progress in it.

* The curated datasets do not reflect datasets that are available for the settings that Offline EF is initially motivated for. They require an accurate simulator to construct, and in the expert and learning cases, require expensive computations using the simulator. I don't think progress on these benchmarks necessarily implies progress on the problem of learning equilibria from offline data because of the data collection methods. Are there available datasets collected from human gameplay in these, or other, games that the authors could use instead?
* The assumptions significantly weaken the theoretical results in Section 4. For instance, Theorem 4.5 is essentially saying that if we have sufficiently many trajectories sampled from an approximate equilibrium profile, and a function approximator with sufficiently low error, then the strategy learned by the function approximator is also an approximate equilibrium. I don't believe this strengthens the contribution. Theorem 4.4 and 4.6 are similar.
* The approximation results for Leduc Poker are poor. A NashConv around 2 is extremely high considering the OpenSpiel implementation of CFR+ achieves an exploitability of around 0.001 in minutes on a laptop.
* The tested domains are quite small and not reflective of the realistic offline scenario that the approach is intended for. Some toy domains help, but including experiments on larger games would increase the significance of the work. Have the authors considered evaluating BOMB on larger games such as Limit Hold'em?

### Questions
1) Is the optimization problem in definition 2.1 that we seek to minimize over all joint strategies $\Sigma$ in the original game, or some subset of these related to $\mathcal{D}$? 
2) What are the x-axes in figures 5, 6 and 7?
3) Why do the authors choose to primarily report NashConv in multi-player variants of Leduc and Kuhn when the equilibrium finding algorithm only guarantees convergence to a CCE? 

**Additional Comments**

* I recommend citing Deepstack.

### Soundness
2

### Presentation
3

### Contribution
1
