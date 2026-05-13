# Graph Neural Networks Gone Hogwild

- Decision: Accept
- Scores: 6, 8, 5, 6

## Abstract
Message passing graph neural networks (GNNs) would appear to be powerful tools to learn distributed algorithms via gradient descent, but generate catastrophically incorrect predictions when nodes update asynchronously during inference.
  This failure under asynchrony effectively excludes these architectures from many potential applications, such as learning local communication policies between resource-constrained agents in, e.g., robotic swarms or sensor networks.
  In this work we explore why this failure occurs in common GNN architectures, and identify ``implicitly-defined'' GNNs as a class of architectures which is provably robust to partially asynchronous ``hogwild'' inference, adapting convergence guarantees from work in asynchronous and distributed optimization, e.g., \citet{bertsekas1982distributed, hogwild}. 
  We then propose a novel implicitly-defined GNN architecture, which we call an \emph{energy GNN}. We show that this architecture outperforms other GNNs from this class on a variety of synthetic tasks inspired by multi-agent systems, and achieves competitive performance on real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper investigates the performance of Graph Neural Networks (GNNs) in partially asynchronous inference settings, where nodes update in a staggered or asynchronous manner. The authors categorize GNNs into two types: "explicitly-defined" and "implicitly-defined." They demonstrate that explicitly-defined GNNs are highly vulnerable to asynchronous updates. In contrast, implicitly-defined GNNs are shown to be robust. Additionally, the authors propose a novel explicitly-defined model, termed Energy GNN, which achieves notable improvements over existing methods on synthetic datasets.

### Strengths
- Although I am not deeply familiar with the literature on asynchronous inference in GNNs, the proposed Energy GNN model introduces a novel and meaningful contribution to this field.
- The paper is of high quality. The authors provide comprehensive mathematical proofs for the convergence of Energy GNNs. They also provide a detailed description of the experimental setup and results, which are well-organized and easy to follow.
- The paper is generally well-structured, with a clear definition of the problem space and a concise summary of related GNN methods. The paper clearly defines the problem of asynchronous inference in explicitly-defined GNNs.
- The proposed Energy GNN model demonstrates significant improvements on synthetic datasets, and competitive performance on real-world datasets.

### Weaknesses
The paper lacks a clear and intuitive explanation of implicitly-defined GNNs, which is essential for understanding their robustness to asynchronous updates. While the authors offer detailed explanations for explicitly-defined GNNs, which are more straightforward, they do not provide the same depth of insight into implicitly-defined GNNs. This makes it difficult for readers unfamiliar with the topic to understand how implicitly-defined GNNs work and why they are resilient to asynchronous inference.

Additionally, although the proposed Energy GNN shows strong results on synthetic datasets, its performance on real-world datasets is rather competitive. On the PPI dataset, in particular, its performance is comparable to that of explicitly-defined GNNs, which were expected to fail under asynchrony. This discrepancy between synthetic and real dataset performance is not explained. A broader evaluation across various real-world datasets would increase the credibility of Energy GNNs as a robust solution.

Line 369. There appears to be a typo in the index notation within the description of targets for the Sums dataset.

### Questions
- Could you provide a more intuitive explanation of implicitly defined GNNs, specifically highlighting the mechanisms contributing to their robustness under asynchronous updates?
- Do you have any insight into why the performance on real-world datasets is not as great as on synthetic data?
- Can you offer an explanation or hypothesis as to why explicitly defined GNNs did not perform as poorly as expected on the PPI dataset under asynchronous conditions?

Line 369. There appears to be a typo in the index notation within the description of targets for the Sums dataset.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies GNNs in the asynchronous “hogwild” setup – when node states are not updated simultaneously at the same time. Such setup is common in distributed environments, agentic systems, and temporal learning where enforcing synchronous node updates might be impossible or too expensive to maintain. Standard, explicitly-defined GNNs trained in the synchronous mode fail in the async mode, so the authors turn their attention to implicitly-defined GNNs (further categorized into fixed-point and optimization-based GNNs). 

It is shown that implicit GNNs are robust to partial asynchronicity. Motivated by the theoretical findings, the authors propose EnergyGNN - an optimization-based implicit GNN where node states minimize a convex energy function. The space of possible energy functions is rather wide and allows for node-wise, edge-wise, and attention-based parameterizations. Experimenting on a range of synthetic tasks, the proposed EnergyGNN outperforms other implicit GNNs in the synchronous regime, is robust to the delayed node update setup, and is on par with synchronous baselines on MUTAG and Proteins datasets.

### Strengths
**S1**. A theoretical study on the async inference with GNNs is timely and important - many real-world tasks are of that nature, so having a principled, robust approach for such problems (instead of tinkering standard sync GNN architectures) might be of interest to the graph learning community.

**S2**. The paper is well-written - complex concepts are properly introduced and explained (which is often a challenge in the literature on implicit GNNs), the story and motivation are easy to follow.

### Weaknesses
The main problem of the work is in the experiments - it is hard to judge the claimed effectiveness of the proposed EnergyGNN using only synthetic experiments and basic GCN / GAT as baselines.

**W1**. In the proposed suite of tasks, all implicit GNNs are robust in the async setup (the main goal of the work), and the main difference lies in the performance in the sync setup. Is there a different way to evaluate the differences among implicit GNNs other than on sync tasks? EnergyGNN is better than other implicit models but comparing against vanilla GCN and GAT on benchmarks defined to be of a long-range nature (where vanilla GNNs are bound to fail) is questionable. There is a variety of explicitly-defined GNNs that might be stronger baselines in such setups like Half-Hop [1], DRew [2] and other graph rewiring methods, as well as various graph transformers from the dedicated Long-Range Graph Benchmark [3]. 

**W2**. The proposed synthetic benchmarks are rather small and might not correlate with the performance on real datasets where async inference is important (or MUTAG and Proteins with sync inference); it seems to be a stretch to attribute chains, node counting, and node sums to “agentic” tasks. Instead, experiments on more real benchmarks might be more informative and evidential: 
* Since some tasks focus on the long-range dependencies, LRGB [3] is a suitable choice;
* As async inference implies nodes appearing and disappearing at some moments of time, temporal graph benchmarks with many snapshots [4] might be a great choice.

Generally, I am willing to increase the score if the authors add more modern baselines and/or real-world datasets.

### Questions
Stemming from the weaknesses:

**Q1 (W1)**. Is there a different way to evaluate the differences among implicit GNNs other than on sync tasks?  
**Q2 (W1)**. How strong is EnergyGNN compared to more long-range optimized GNNs like Half-Hop, DRew, and graph transformers?  
**Q3 (W2)**. Does the synthetic EnergyGNN performance correlate with the tasks from more real-world benchmarks like LRGB and TGB?

### Soundness
3

### Presentation
4

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
This paper introduces Graph Neural Networks (GNNs) for distributes multi-agent systems with asynchronous communication. Traditional GNNs struggle with asynchronous execution and unreliable communication. This results in unreliable predictions. To address this, the authors focus on implicitly-defined GNNs, a class of models that can handle partial asynchrony. They introduce a model called energy GNNs, which outperform existing implicitly-defined GNNs on synthetic multi-agent tasks.

The experimental results highlight potential applications for GNNs in control tasks and real-time inference on dynamic graphs. This is an important property for multi-robot systems. The paper also notes the training limitations for implicitly-defined GNNs, particularly in achieving convergence, as it requires complex and often unpredictable computations. Strategies like warm-start initialization and implicit differentiation could help with these challenges, but challenges remain in achieving stability.

### Strengths
By focusing on implicitly-defined GNNs, the work addresses a major limitation of conventional GNNs in handling asynchronous and unreliable communication, making it highly relevant for real-world multi-agent systems.

Experimental results show that energy GNNs outperform other implicitly-defined GNNs on synthetic tasks, providing empirical validation for the architecture's effectiveness in multi-agent tasks (although most experiments are toy-ish.)

### Weaknesses
The experiments are conducted on toy examples.

For the experiments other than the "terrain" examples there are great solutions that do not require machine learning. The results on the benchmark datasets in the supplementary show small improvements as compared to the more toy examples in the main manuscript.

### Questions
Please consider changing the term energy GNN. My first reaction was that this solution was energy-efficient which is a very big concern in AI at the moment. However this work is not about energy efficient AI. 

The experiments are on toy examples that do not need machine learning. Please expand the experimental range to other problems and to larger problem scale. 

Can you be clearer about what you summarize from existing work and what are the new contributions in sections 2, 3, 4 

The description of energy GNN is very sparse, please explain the computation of the neuron and node, architecture, and the method for training in the main manuscript. Please address summarize the properties of this model in Section 5. 

Can you say anything about the performance and energy consumption of these models?

### Soundness
3

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
3

### Summary
In this paper, the authors tackle the issue of asynchrony in graph neural networks (GNNs). Traditional GNNs, particularly multi-layer variants, assume synchronized node updates, which is often unrealistic in real-world distributed systems like robotic swarms or sensor networks. 

The authors identify a class of GNNs called "implicitly-defined" GNNs that are robust to asynchronous or "hogwild" inference. They propose a novel implicitly-defined GNN architecture called "energy GNN", which leverages input-convex neural networks to parameterize a convex energy function. The results from experiments on synthetic multi-agent tasks and benchmark graph datasets demonstrate the superior performance of energy GNNs under asynchrony and their competitiveness even in synchronous settings.

### Strengths
1) Adoption of GNNs in real-world distributed systems.
2) Theoretical guarantees for the robustness of implicitly-defined GNNs to asynchrony, drawing on concepts from distributed optimization.
3) The proposed energy GNN offers a flexible and expressive way to define convex energy functions, potentially leading to more powerful GNN models.
4) Experiments on both synthetic (chains, counting, sums, coordinates) and benchmark datasets (MUTAG, PROTEINS, PPI) demonstrate the effectiveness of the proposed approach.

### Weaknesses
1) Even though the paper proposes mitigation strategies for trraining implicitly-defined GNNs. They are computationally expensive due to the iterative nature of the forward pass. This would be a challenge in practical scenarios.
2) The experiments primarily focus on single-layer energy GNNs. The performance of multi-layer variants and their scalability to larger graphs are unclear.
3) The convergence of implicitly-defined GNNs can be sensitive to the choice of hyperparameters like step size and convergence tolerance. Have the authors investigated the robustness perspective?
4) While the paper motivates the problem with real-world scenarios(in abstract) the experiments are primarily on synthetic datasets. Unsure how well these would be effective in real world scenarios due to few of the weaknesses pointed above

### Questions
1) How does the choice of the staleness bound B and stagger time S affect the performance and convergence of energy GNNs in practice? Is there a principled way to select these parameters?
2) The authors mention the potential for numerical instability due to ill-conditioned Hessians or Jacobians. Have they explored techniques like preconditioning to address this issue?
3) How does the performance of energy GNNs scale with the size of the graph and the number of nodes? Would these be applicable to very large graphs? (I see a comment on this in conclusion section but would be interesting to know the authors intuition about this)

### Soundness
4

### Presentation
3

### Contribution
3
