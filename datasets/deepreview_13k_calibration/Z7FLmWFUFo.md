# The Critic as an Explorer: Lightweight and Provably Efficient Exploration for Deep Reinforcement Learning

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 3, 6

## Abstract
Exploration remains a critical challenge in reinforcement learning (RL), with many existing methods either lacking theoretical guarantees or being computationally impractical for real-world applications. We introduce Litee, a lightweight algorithm that repurposes the value network in standard deep RL algorithms to effectively drive exploration without introducing additional parameters. Litee utilizes linear multi-armed bandit (MAB) techniques, enabling efficient exploration with provable sub-linear regret bounds while preserving the core structure of existing RL algorithms. Litee is simple to implement, requiring only around 10 lines of code. It also substantially reduces computational overhead compared to previous theoretically grounded methods, lowering the complexity from O(n^3) to O(d^3), where n is the number of network parameters and d is the size of the embedding in the value network. Furthermore, we propose Litee+, an extension that adds a small auxiliary network to better handle sparse reward environments, with only a minor increase in parameter count (less than 1%) and additional 10 lines of code. Experiments on the MiniHack suite and MuJoCo demonstrate that Litee and Litee+ empirically outperform state-of-the-art baselines, effectively bridging the gap between theoretical rigor and practical efficiency in RL exploration.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents Litee, a lightweight algorithm for efficient exploration in reinforcement learning. Litee computes an uncertainty term from state embeddings using either UCB or Thompson Sampling techniques. To address sparse reward environments, the authors introduce Litee+, an extension that adds a minimal number of additional parameters. Compared to prior methods, Litee+ significantly reduces the parameter overhead while preserving exploration effectiveness. The paper also establishes a theoretical upper bound on the regret for both algorithms and demonstrates their effectiveness through experiments in both sparse and dense reward settings.

### Strengths
1. The authors present an algorithm with theoretically provable exploration efficiency and strong empirical performance. The algorithm incorporates either UCB or Thompson Sampling to calculate the uncertainty term. The exploration is achieved with only a minimal increase in parameters.
2. The authors employ an Inverse Dynamics Network (IDN) to address the sparse reward problem, achieving strong practical performance.

### Weaknesses
1. This approach has been extensively studied. The Litee with UCB term is nearly identical to classic algorithms for linear MDPs (e.g., https://arxiv.org/pdf/1907.05388). The novelty of Litee remains unclear. Specifically, the use of state embeddings to compute an uncertainty bonus is a common technique, and the paper does not sufficiently articulate how their approach differs from existing methods. The connection to linear MDP algorithms is not just superficial; the core mechanism of using an uncertainty-based bonus derived from a linear model is directly analogous to algorithms like UCB for linear MDPs. The paper needs to clearly delineate the novel aspects of their method beyond simply applying this technique to state embeddings.
2. The experiments are not solid. There is no table of results, and the paper only presents some plots based on three or seven repetitions, with no explanation for the variation in repetition count. Additionally, this method fails to solve all tasks in MiniHack. The lack of a comprehensive table makes it difficult to assess the statistical significance of the results. Furthermore, the inconsistent number of repetitions across different experiments raises concerns about the reliability of the reported performance. The failure to solve all MiniHack tasks, especially when other methods have demonstrated success, indicates a limitation in the algorithm's general applicability.
3. Computational cost is not a significant constraint in RL. DRL often employs simple architectures (sometimes only a shallow MLP), and even a 100% increase in parameters to handle exploration would not be a problem for GPUs. While parameter efficiency is a desirable trait, the argument that computational cost is a major bottleneck in DRL is not well-supported. Many successful DRL models use relatively small networks, and the overhead of adding parameters for exploration is often negligible compared to the overall computational demands of training.
4. The theoretical contribution is limited. The proof has fewer than five pages and does not introduce new techniques or new messages. The theoretical analysis, while present, does not offer any significant advancements in the understanding of exploration in RL. The proof techniques are standard and do not introduce any novel insights or methodologies.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Litee, an RL exploration algorithm designed to be lightweight. Litee utilzes the value network’s state embeddings to compute theexploration bonus without adding new parameters,hence reduces the computational complexity. Litee+, an enhanced version of Litee, integrates an auxiliary network trained with inverse dynamics to improve the exploration bonus.

### Strengths
1. The authors not only provide experimental results, but also provide a theoretical guarantee of the proposed algorithm, which makes the paper very comprehensive.

2. Litee and Litee+ are more parameter efficient compared to E3B

### Weaknesses
1. $\textbf{Lack of novelty}$: the novelty of the work is quite low, as the algorithm is almost identical to LSVI-UCB (except for the feature $\phi$ is changing over time). The theoretical framework mostly comes from [1] and [2] with some tweaks and re-organization. And Litee+ is quite related to the prior exploration RL algorithm ICM [3], and the authors do not sufficiently discuss the relations between this work and [1] [2] [3]

2. $\textbf{The experimental results are not convincing}$. The authors use part of the MuJoCo benchmark, missing HalfCheetah, Ant and Humanoid, which are most commonly used by other reinforcement learning works. SAC-Litee outperforms PPO and SAC in the swimmer task with a large margin, however, the task is too easy, which makes it a less convincing evidence that Litee is strong. Similarly, only a very small subset of tasks in MiniHack domain is used. In general, the whole set of tasks in a domain would test some aspect of an RL algorithm (exploration, credit assignment, memory, etc) comprehensively, performing well on 3 tasks is not convincing.

3. The theoretical part of the work can be better organized. In Theorem 4.2, the neural tangent kernel H comes from nowhere, and the readers will have to refer to the paper [2] in order to understand the theorem and the proof. 

4. (minor)  I am not an expert of deep learning theory, but it is strange to me that the authors directly "assume" the neural tangent kernel to be $\textbf{postive-definite}$ instead of $\textbf{positive-semidefinite}$.

### Questions
I have mentioned most of my concerns above, in the weakness section, and I will potentially lift my rating if the authors can help me understand the following points:
1. Can authors clarify their contribution on the theoretical side of the work?
2. Can authors provide a more comprehensive benchmark results, on both MuJoCo, and MiniHack? 
3. How would Litee and Litee+ perform compared to other more popular / stronger exploration algorithms on MuJoCo and MiniHack, just as used in E3B paper: E3B x RND, E3B x ICM, etc. Can the authors compare to the setting like SAC + RND, SAC + ICM?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes exploration methods for RL inspired from UCB and Thompson sampling based methods from linear bandit literature. The paper provides theoretical regret bounds for the methods as well as empirical validation.

### Strengths
The paper addresses a common issue in existing RL literature. The disconnection between the RL theory and deep RL literature when it comes to exploration. The paper tries to bridge this gap by proposing algorithms that are theoretically principled while being empirically scalable.

### Weaknesses
1. In line 72-79 and line 134-136, the paper posits that there is no RL algorithm that is both theoretically grounded as well as empirically efficient. This is not true as there have been recent works that are both empirically well performing as well as have provable theoretical guarantees (Ishfaq et al 2024a, Ishfaq et al 2024b for example).

2. The Litee algorithm builds off from Eq 2 and then utilizes UCB based bonus function and Thompson sampling. It’s not clear what’s the novelty here compared to existing RL exploration algorithms that already utilizes UCB or Thompson Sampling approach.

3. In eq 3 it uses the typical UCB bonus which are already standard in RL theory literature. For example, LSVI-UCB paper by Jin et al 2020 uses exact same bonus function. Also, $\beta(s,a)$ depends on feature parameter $\phi$. It means each time representation is updated through value network update, the bonus function needs to be recomputed based on new updated feature. Similarly, the variance matrix $A$ needs to be updated using the newly updated feature (as highlighted in Eq 5).

4. In Eq 4, for Thompson sampling based approach, it requires to take inverse of the noise variance matrix $A$, which is high dimensional matrix. Taking inverse of it is computationally non-trivial. 

5. In Algorithm 2, line 10 and line 11, the Thompson sampling baed action value uncertainty estimation and reshaping reward function is essentially same as the LSVI-PHE approach described in Ishfaq et al 2021 (see Algorithm 2: LSVI-PHE for linear function approximation for example in that paper). However, the similarity with LSVI-PHE was not discussed nor the paper was cited.

6. The baselines used in the experiments are not state of the art. For example, for mujoco tasks, one of the strong baselines these days is DSAC-T from Duan et al 2023. Can you compare Litee and Litee++ with DSAC -T ?

7. Most lemmas and proof approaches are direct adaptation of existing papers for example Lemma 7. This limits the theoretical contribution of the work.

### Questions
1. Can you comment on your regret bound and how they will be if we consider linear MDP setting from Jin et al 2020?

2. How are Algorithm 1 and 2 are different from existing RL algorithms that uses UCB and Thompson sampling/randomized value function approach?

3. Can you anonymously share the full code base so that the reviewers can go through it in more detail. Just putting snippets of code in Listing 1 and Listing 2 seems insufficient to understand how Litee is implemented in the bigger picture.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a lightweight exploration method named Litee, which leverages linear multi-armed techniques (e.g., UCB and Thompson Sampling) as the uncertainty measurements. Theoretical analysis shows that the sample efficiency of Litee in the context of regret bound. Experimental results also show that Litee and Litee+ both achieve better sample efficiency in the dense and sparse reward settings, respectively.

### Strengths
1. The motivation behind the proposed method is clear and straightforward (lines 72-79).
2. This paper presents both theoretical analysis and empirical results on the sample complexity.

### Weaknesses
The reviewer has no concerns about the proposed method but has some suggestions on the experiments.

## Experiments
1. Although the theoretical analysis of DQN with Litee (Algorithm 1) provides the theoretical results in sample efficiency, its experimental results are needed somehow. For instance, DQN can explore nothing in Montezuma’s Revenge within limited steps. How much does Litee or Litee+ improve the DQN in this task or other tasks with sparse reward?
2. As illustrated by the authors (Section 3.3), how much does the inverse dynamics network(IDN) improve the Litee? It would be better to see the ablation studies on the sparse reward settings. For instance, the comparison of the Litee and Litee+ on MiniHack.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
