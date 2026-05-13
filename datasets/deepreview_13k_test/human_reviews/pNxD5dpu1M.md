# Learning Cooperative Mean Field Games on Sparse Chung-Lu Graphs

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Large agent networks are abundant in applications and nature and pose difficult challenges in the field of multi-agent reinforcement learning (MARL) due to their computational and theoretical complexity. While graphon mean field games and their extensions provide efficient learning algorithms for dense and moderately sparse agent networks, the case of realistic sparser graphs remains largely unsolved. Thus, we propose a novel cooperative mean field game (MFG) model based on the large class of Chung-Lu graphs including power law networks with coefficients above two. Besides a theoretical analysis, we design scalable learning algorithms which especially apply to the challenging class of graph sequences with finite first moment and infinite second moment. We compare our model and algorithms for various examples on synthetic and real world networks with MFG algorithms based on Lp graphons and graphexes. As it turns out, our approach outperforms existing methods in many examples and on various networks due to the special design aiming at an important, but so far hard to solve class of MARL problems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims at learning optimal policies in games with many players in which the players interact through a specific type of sparse graph. After discussing the connection between finite-player situations and the limiting setting when the number of players goes to infinity, two algorithm are described and tested on several examples. Comparison with two previous algorithms is included.

### Strengths
The paper is well written. The theory clarifies the link between finite-player games and the limiting game. The experiments cover several examples of large-scale graphs.

### Weaknesses
The paper focuses on a special family of graphs. There is no analysis for the learning algorithms. The contributions seem somewhat incremental compared with (Fabian et al., 2023; 2024).

### Questions
1. Page 1: “cooperative MFGs” It seems that these are usually called mean field control (MFC) problems. Can you please clarify? (By the way, it seems you use “MFC” on page 6 without explaining its meaning.)

2. Limiting system: Can't this system be reduced to a standard “cooperative MFG” by extending the state? For example, what about considering the “cooperative MFG” in which the state of a representative agent is $(X_t, \mathbb{G}_t)$?

3. Could you explain whether there is any theoretical convergence guarantees for these algorithms?

### Soundness
3

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
3

### Summary
This paper introduces a novel Chung-Lu Cooperative Mean Field Games (CLCMFG) framework designed for sparse graphs. The model effectively alleviates the computational challenges in applying multi-agent reinforcement learning to large, sparse networks. The authors provide a theoretical foundation for CLCMFGs and introduce a two-systems approximation that simplifies the learning process, reducing computational complexity. The two-systems approximation separates agents into high- and low-degree categories, reducing the computational burden and maintaining accuracy by addressing the heavy-tailed degree distributions typical in sparse graphs. Experiments demonstrate that this approach improves accuracy for sparse network scenarios, overcoming the limitations of prior MFG models, which primarily focus on dense or moderately sparse graphs.

### Strengths
1. In contrast to existing MFG models suited to dense graphs, CLCMFGs effectively handle networks with finite average degrees and heavy-tailed distributions, making them particularly relevant for real-world networks like social and communication systems. This advancement broadens the applicability of MFG models to a wider range of network types.
2. Leveraging the two-systems approximation, CLCMFGs avoid the exponential complexity common in MARL for sparse graphs. CLCMFGs address large-degree variance, capturing the impact of high-degree hubs and providing a more accurate representation of network dynamics.
3. The paper conducts a comprehensive empirical evaluation, testing CLCMFGs across multiple problems on both synthetic and real-world network datasets. Results show that CLCMFGs consistently outperform existing LPGMFG and GXMFG methods in accuracy across various settings, including epidemic modeling (SIS/SIR), graph coloring, and rumor spreading.

### Weaknesses
1.	While the two-systems approximation is conceptually interesting, there lacks a rigorous error analysis about this approximation, particularly with respect to the choice of $k^*$. Moreover, while the mean field highly depends on the hyperparameter $k^*$, which can significantly affect both the approximation accuracy and computational complexity, the paper has not discussed the choice of $k^*$ in theory or in experiments.  
2.	The model is specifically designed around the Chung-Lu graph, which raises questions about whether it can generalize well to other types of sparse networks (if any) and real-world networks. For the latter, it can be observed from Figure1 that there is  still a significant  gap between the proposed model and real-world networks.
3.	The experimental section miss some details, such as a comparison of computational costs for each method in Table 1 and the number of trials for the IPPO method in Figure 3, where results show notable fluctuations. Adding these would clarify computational demands and result reproducibility.

### Questions
1.	What key characteristics (e.g., degree distribution, sparsity, high-degree nodes) indicate that a real-world network is suitable for modeling with sparse Chung-Lu graphs?
2.	CLMFC emphasizes computational efficiency through approximation, while CLMFMARL maintains fidelity by interacting with the real graph. Figure 3 shows that CLMFC and CLMFMARL each have advantages in different scenarios. Could you advise on choosing the algorithm for various scenarios?
3.	Can the proposed approach be adapted to other types of random graph generation methods, such as the Barabási-Albert model or the Erdős–Rényi model?
4.	In Figure 1, visualization is used to show that the CL graph closely resembles the real YT network. Would it be possible to incorporate quantitative metrics to compare the performance of different network generation methods?

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
3

### Summary
This paper aims to model large agents on networks and proposes a cooperative mean field game over sparse graphs like Chung-Lu (CL). Two systems approximation is developed to describe how agents with different degrees of connections are connected. Two learning algorithms are proposed, namely, MFC MDP and single-agent RL.

### Strengths
The paper makes a unique contribution to large agents interacting over sparse graphs, given that the majority of existing literature on asymmetric interactions of mean field games (MFG) is focused on dense graphs.

### Weaknesses
Motivation: In practice, how could one tell if graphon MFGs should be used or the proposed game over CL graphs should be used? 

Model contribution: It remains unclear whether this paper makes more contributions to MFGs or graph theory, as the paper spends more space on introducing CL graphs and very little space on cooperative MFG. 

Model formulation: It seems this paper proposed a mean field control (MFC) problem over sparse graphs. But the formulation of the proposed model seems different from classical MFC. The finite model is introduced, but the formulation of the limiting system is unclear, partly because the formulation of the limiting system is not presented in detail. What is the exact formulation of the proposed limiting model? How is it related to MFC? It seems the proposed limiting model is simply an MDP with population as the agent. Could the authors clarify the difference between the proposed cooperative MFG here and a generic MFC over sparse graphs?

Learning algorithms: How are these algorithms different from existing scalable learning algorithms for MFGs?
How is the threshold $k^\ast$ determined in practice?
What is the convergence of the learning algorithm?

Examples: The numerical examples can also be applied to graphon MFGs. Could the authors compare the difference of the outputs using graphon MFGs v.s. using the proposed method? What’s the advantage of using CL graphs here?

### Questions
How is the CL graph embedded into the cooperative MFGs? 

This paper could better motivate why cooperative MFGs on sparse graphs are important in real-world and computation. For example, why is the embedding of a sparse graph challenging? How is it reflected in the formulation, algorithm design, and convergence?

P4 L170: The statement “All agents with degree k share a common policy at all time points.” Is this an assumption or a fact? If latter, could the authors clarify why that's the case?

P4 L189: “Our model also covers reward functions with actions as inputs by using an extended state space and splitting each step into two.” Could the authors detail how this is done for a regular state-action dependent reward?

P4 L203 “Large CL graphs under Assumption 1 have a locally tree-like structure.” Could the authors clarify how the tree-like structure would help with theoretical results?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a learning framework for cooperative behaviors among large agent populations on sparse graphs. Authors propose learning algorithms and conduct numerical experiments to demonstrate the performance.

### Strengths
Overall, this paper is well written and structured. The numerical results are thorough.

### Weaknesses
1. The research gap is not quite clear. The problem formulation of  cooperative mean field games is similar to mean field control (MFC). Authors should clearly present the relationship between the proposed work, MFC and multi-agent cooperative learning or compare the difference corresponding to the problem formulation or set-up and summarize them in a table. I feel like the proposed model in this paper is essentially an MFC over sparse graphs. 

2. Is the solution concept an extension of equilibria in multi-agent cooperative games when N goes to infinity?

3. Sparse graphs have been studied in many existing works (Leaning Mean Field Games on Sparse Graphs: A Hybrid Graphex Approach, 2024). Authors should highlight the contribution and novelty of the proposed sparse graphs in this work and demonstrate their superiority over other frameworks in numerical results, e.g., the comparison between Chung-Lu graphs proposed in this work and those in Leaning Mean Field Games on Sparse Graphs: A Hybrid Graphex Approach, 2024.

4. The solution properties of the cooperative mean field game (existence and uniqueness) are not discussed in this work.

5. The proposed two algorithms are very similar to some classic multi-agent reinforcement learning algorithms (e.g., MF-MARL, 2018). Authors should compare the difference between these algorithms in a table (e.g., complexity, setup, etc) to highlight their contribution. I feel like MF-MARL, 2018 also solves a multi-agent cooperative game. 

6. The theoretical analysis regarding algorithm performance (convergence, time complexity) is not discussed.

### Questions
Please see the list of questions in weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
