# Generalization and Distributed Learning of GFlowNets

- Decision: Accept
- Scores: 6, 5, 8, 6

## Abstract
Conventional wisdom attributes the success of Generative Flow Networks (GFlowNets) to their ability to exploit the compositional structure of the sample space for learning generalizable flow functions (Bengio et al., 2021). Despite the abundance of empirical evidence, formalizing this belief with verifiable non-vacuous statistical guarantees has remained elusive. We address this issue with the first data-dependent generalization bounds for GFlowNets. We also elucidate the negative impact of the state space size on the generalization performance of these models via Azuma-Hoeffding-type oracle PAC-Bayesian inequalities. We leverage our theoretical insights to design a novel distributed learning algorithm for GFlowNets, which we call *Subgraph Asynchronous Learning* (SAL). In a nutshell, SAL utilizes a divide-and-conquer strategy: multiple GFlowNets are trained in parallel on smaller subnetworks of the flow network, and then aggregated with an additional GFlowNet that allocates appropriate flow to each subnetwork.  Our experiments with synthetic and real-world problems demonstrate the benefits of SAL over centralized training in terms of mode coverage and distribution matching.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors develop the generalization bounds for GFlowNets, providing empirical guarantees that the models can generalize beyond the training data, using the PAC-Bayes technique. The authors explore the way how the structure of GFlow's network and trajectory lengths affect its generalization performance. Then the authors suggest a novel distributed algorithm called Subgraph Asynchronous Learning (SAL), which is shown to improve over its centralized counterparts in some experimental settings, such as subset generation, sequence design, and Hypergrid environments (Section 6).

### Strengths
To the best of my knowledge, neither the PAC-Bayes generalization bounds, nor the distributed training of Gflownets were previously considered in the literature, so both main contributions of the paper appears to be new. The literature review performed by the authors, is exhaustive and well-written, as well as the main text of the paper.

### Weaknesses
From the theoretical point of view, theoretical contribution of the paper is rather incremental, as the main theoretical findings of the paper are mostly corollaries from known results in PAC-Bayes literature. Moreover, the supervised setting for training GFlowNets is questionable and is of limited interest, since its implementation requires a sampler from the target distribution.

From the experimental point of view, I would also say that the proposed experimental investigation of the Subgraph Asynchronous Learning algorithm is insufficient. All considered environments can be considered as rather toyish, with actual number of terminal states less than $10^{10}$. This is quite far from the most challenging environments, for example, see for example the molecular generation problems from the recent papers [Jang et al, 2024], [Mohammadpour et al, 2024].

Although minor, I would also highlight some stylistic nuances in the exposition. For instance, the authors describe their own results in Theorem 5.2 as 'insightful' (lines 204 and 2130). It is uncommon in the literature to use such language when referring to one's own findings. Similarly, the statistical guarantees presented in the current submission, are often referred to as "non-vacuous" bounds. At the same time, it is not clear to me what exactly "non-vacuous" means in the context of statistical guarantees, which seems to be an overstatement.

***Minor typos*** 
1. I guess, that in line 148 $p_E$ should be defined as $p_E = (1-\epsilon)p_F + \epsilon p_{U}$;
2. page 3, line 149 - polciy -> policy;
3. Proposition 5.1 - $\tau_{\alpha}$ is undefined, only $\tau_{1 - \alpha}$ previously appeared;
4. page 9, line 223: assigment function -> assignment function;
5. line 979-980 - [ref] undefined;
6. General remark - the authors should be more accurate when using the $\lesssim$ symbol. At least it should be indicated, which problem-specific constants are omitted when it is used. 

***References*** 
[Jang et al, 2024] Hyosoon Jang, Yunhui Jang, Minsu Kim, Jinkyoo Park, and Sungsoo Ahn. Pessimistic backward
policy for Gflownets, 2024. 

[Mohammadpour et al, 2024] Sobhan Mohammadpour, Emmanuel Bengio, Emma Frejinger, and Pierre-Luc Bacon. Maximum
entropy gflownets with soft Q-learning. In International Conference on Artificial Intelligence and Statistics, pp. 2593–2601. PMLR, 2024.

### Questions
1. Is it possible to provide larger-scale experiments? For example, consider the applications of Subgraph Asynchronous Learning to molecular generation problems, such as QM9 or sEH, see [Mohammadpour et al,2024].

2. Can the authors provide more details on the way the Fixed-horizon DAG partition (definition 6.1) should be constructed? May be there are some heuristics or theoretically justified approached to it? It seems that the choice of partition should be of crucial importance for algorithm's performance, otherwise this partition itself can yield mode collapse and other issues with diversity of the samples.

***References***

[Mohammadpour et al, 2024] Sobhan Mohammadpour, Emmanuel Bengio, Emma Frejinger, and Pierre-Luc Bacon. Maximum
entropy gflownets with soft Q-learning. In International Conference on Artificial Intelligence and Statistics, pp. 2593–2601. PMLR, 2024.

### Soundness
2

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
The paper contributes to the theory of Generative Flow Networks (GFN) on finite directed acyclic graphs.  
The key contribution of the work consists in the formulation and the proof of several new so-called generalization bounds controlling the accuracy of the sampling distribution compared to its target.  The author uses these bounds as a motivation to introduce a divide-n-conquer distributed GFN training algorithms: SAL and recursive SAL. These algorithms pack several GFNs together by assuming that the initial flow of the one is the reward of another.

### Strengths
The paper provides new generalization bounds for Generative Flow networks together with rigorous proofs leveraging sophisticated pre-existing bounds. 
The paper also introduces an interesting recursive GFN training: recursive SAL algorithm
The appendix is rich with further theoretical analysis.

### Weaknesses
We feel the authors do not properly exploit the bounds they produce:
- A full section is devoted to describing when GFN do not generalize. Still, the conclusion that the number of states or the length of trajectories is detrimental to training is disappointing.
- motivating corner cases are not  discussed
- The SAL algorithm does not need the bounds to be motivated, as divide and conquer is a very common strategy in CS in general.

To elaborate on this, let's consider equation 5. The hypotheses seem to allow any $p_{E,T}$, but the context provided above Lemma 4.1 suggests it is intended as the forward policy of the GFN at hand. Now, in practical cases, the forward policy will be very different from the uniform policy to the point that $\chi^2(q_{E,T}||p_{E,T})$ may diverge. I tend to agree that target distribution is key, but it is not discussed how one may leverage this. For instance, the bound suggests one may use the product $\mathcal L_{TB} \times \chi^2(q_{E,T}||p_{E,T})$ as a regularization during training, or even that modifying the reward as $R_{\delta}(x):= R(x)+\delta \varphi(x) $ for some summable function $\varphi$ and let $\delta$ go to zero controlled by $ \chi^2(q_{E,T}||p_{E,T})$ would allow controlling the generalization better. Coming back to the declared intent (describing when GFN does not generalize well), I am still looking for specific examples (even in the appendix) of GFN together with couples (graph, reward) that would typically make the bound high yet have a low loss. This would be very useful to showcase when one should be careful when using GFNs. 

We feel the first four pages are too wordy. They announce the results several times, leaving too little space for the interesting matter: an insight discussion of the generalization bounds. 

Section 4 is unclear; the set generation problem is barely understandable.

Some mathematical results are strangely placed. For instance, the purpose of Lemma 4.1 is unclear in the section context, while Lemma D.1 is both trivial and stated after it is used.
 
The recursive SAL algorithm (which we find of interest) is only introduced in the appendix.

### Questions
1) Could you provide insight and/or examples illustrating the meaning of the bounds you introduce?
2) I am confused about the link between the FCS and TB losses. Could the author clarify this link and how they differ? Is FCS loss used for training? Is it computable as a metric during training? 
3) Are you able to provide deeper insight into the structural properties of the graphs or into the reward leading to lower generalization, deeper than the dimensionality curse?
4) How could one make your bounds actionable or act as a guardrail ?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors of this paper investigate the generalization properties of Generative Flow Networks (GFlowNets), focusing on providing theoretical guarantees for their performance. They introduce the first data-dependent generalization bounds for GFlowNets, leveraging PAC-Bayesian inequalities to analyze how the state space size affects generalization. Building on these theoretical insights, they propose a distributed learning algorithm, which employs a divide-and-conquer strategy to train multiple GFlowNets on subgraphs and then aggregate them to improve mode coverage and distribution matching.

### Strengths
1. The authors address the gap in the theoretical understanding of GFlowNets, namely, their generalization properties, by deriving the first data-dependent generalization bounds, which is a novel and impactful contribution. Traditional analyses of generalization have primarily focused on models like neural networks or reinforcement learning agents, so extending this to GFlowNets represents a fresh and innovative application of statistical learning theory.

2. By proposing a divide-and-conquer approach, where multiple GFlowNets are trained on different subgraphs of the flow network and then aggregated through a coordinating GFlowNet, the authors introduce a novel parallel training strategy that could address scalability challenges.

3. The quality of the research presented is high, with clear efforts to rigorously derive and justify the theoretical claims. By framing the generalization bounds in terms of the state space size, the authors have identified a key factor that impacts GFlowNets' generalization capabilities and provided a principled way to analyze it.

4. The structure of the paper is logical, and the methodology and experiments are presented in a well-organized manner.

5. The significance of this work is substantial. GFlowNets have shown empirical promise for a variety of applications, including distribution matching and probabilistic modeling, yet a rigorous understanding of their generalization capabilities has been lacking. By providing data-dependent generalization bounds, this paper addresses a core theoretical question that could impact how GFlowNets are used and optimized in the future.

6. The divide-and-conquer approach of SAL not only enhances scalability but also has potential benefits for robustness and mode coverage in the generated distributions. These improvements could make GFlowNets more viable for applications in domains like natural language processing, biology, and engineering, where large datasets and complex distributions are the norm.

### Weaknesses
1. While the paper presents experimental results for both synthetic and real-world tasks, the scope of these experiments might be limited in terms of diversity of datasets, complexity of environments, and breadth of tasks. Here are some suggestions: 

(i) Combinatorial Optimization over Graphs
Dataset: TSP, MAX-CUT, or Graph Coloring datasets commonly used in combinatorial optimization.
Task: Solve classic graph-based optimization problems, where the state space represents possible solutions (e.g., routes, cuts, or colorings) and the reward function evaluates the quality of each solution. For instance, in a MAX-CUT problem, the reward would be based on the cut size.
Importance for Distribution Learning: For combinatorial optimization tasks, covering a variety of valid solutions (e.g., different feasible paths with minimal distance in a graph problem) is crucial. Testing SAL here would show whether it can capture a distribution over multiple near-optimal solutions.

(ii) Financial Portfolio Optimization
Dataset: Historical stock or cryptocurrency price data.
Task: Generate diverse portfolio allocations that balance risk and reward, aiming to maximize expected returns with minimal risk. Rewards could be based on risk-adjusted performance metrics, like the Sharpe ratio.
Importance for Distribution Learning: Portfolio generation requires balancing exploration of different investment strategies with optimization for high returns. Distribution learning helps to capture diverse investment strategies and avoid over-optimizing for a narrow range of allocations, making it a good test for SAL.

(iii) Neural Architecture Search (NAS)
Dataset: CIFAR-10 or ImageNet for evaluating architectures.
Task: Generate neural network architectures that maximize performance on a validation set. Rewards could be based on model accuracy, computational efficiency, or other architecture characteristics.
Importance for Distribution Learning: NAS requires exploration across a diverse set of neural architectures rather than converging on a single high-performing design. This task would test whether SAL can generalize across different architectural choices and find multiple good architectures, covering a broad distribution in the search space.

2. The SAL approach, while promising for distributed training, may have significant computational and memory overhead due to the need to train multiple GFlowNets in parallel and then aggregate their results. This could be a limiting factor in resource-constrained environments or for applications where computational efficiency is critical.

3.  The generalization bounds do not take into account potential dependencies in the data that could arise in scenarios where GFlowNets are used for tasks like sequential decision-making. These dependencies could weaken the validity of the i.i.d. assumption and potentially affect the reliability of the bounds. It will be useful to discuss how the authors might extend their analysis to account for dependencies in sequential decision-making scenarios.

4. Although SAL is designed to improve mode coverage, aggregating multiple GFlowNets could still risk mode collapse if subgraph-trained models fail to adequately capture all modes of the target distribution. If some subgraphs do not represent certain regions of the distribution well, the aggregation process could overlook these regions, resulting in poor overall coverage.

### Questions
1. While the paper addresses generalization and distributed learning, it would be useful if it discussed the potential limitations of SAL more explicitly. For instance, are there scenarios where SAL might fail to converge, or does it require a careful balance of parameters to function well? 

2. Additionally, are there inherent limitations to the generalization bounds derived, particularly when applied to different classes of GFlowNets or domains with very large or complex state spaces?

3. The paper notes that traditional training of GFlowNets resembles active learning. Could you expand on how you envision incorporating active learning strategies into your framework? How might this impact the performance of GFlowNets compared to the current approach?

4. In the experiments, were there any signs of mode collapse when aggregating the outputs of subgraph-trained GFlowNets? What strategies would you recommend or envision to mitigate this issue during the aggregation phase?

5. Are there empirical limits which have been identified in the experiments regarding the effectiveness of SAL as the complexity of the underlying GFlowNet increases?

6. SAL relies on fixed partitions to divide the state space into subgraphs, which may limit the flexibility and adaptability of the approach. In real-world applications, the optimal partitioning of the state space may not be obvious and may vary over time as the policy evolves. A rigid partitioning could result in subgraphs that are either too sparse (leading to inefficient training) or too dense (leading to high computational cost). How do the authors envision adapting the partitioning scheme to be more flexible or dynamic as the policy evolves during training?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper investigates the Generative Flow Networks (GFlowNets), and presents several novel contributions to the understanding and development of GFlowNets: (i) Data-Dependent Generalization Bounds, which is the first data-dependent generalization bounds for GFlowNets, providing statistical guarantees for their learning capabilities; (ii) Impact of State Space Size,  which explores the influence of state space size on generalization performance, utilizing PAC-Bayesian inequalities to formalize these effects. (iii) Subgraph Asynchronous Learning (SAL) Algorithm, which is proposed to improve training efficiency and generalization in GFlowNets by partitioning the network into smaller subnetworks.

### Strengths
- This paper offers a unique perspective on GFlowNet generalization through PAC-Bayesian bounds.
- This paper is theoretically solid and well-orginazied.
- The authors validate their findings with experiments on both synthetic and real-world tasks, strengthening the reliability of the conclusions.

### Weaknesses
- The main idea of SAL (i.e., divide and conquer) is novel for GFlowNet. However, I wonder whether the aggregation accuracy will be compromised for large networks. In other words, is there a trade-off in the theoretical results about $m$?
- The time cost of the Fixed-horizon partition does not appear to be addressed. Does this operation impact model efficiency? More precisely, how can a Fixed-horizon partition be found efficiently?

### Questions
See it in the Weakness above.

### Soundness
3

### Presentation
3

### Contribution
3
