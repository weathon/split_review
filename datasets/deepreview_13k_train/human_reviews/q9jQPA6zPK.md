# Leveraging Hyperbolic Embeddings for Coarse-to-Fine Robot Design

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Multi-cellular robot design aims to create robots comprised of numerous cells that can be efficiently controlled to perform diverse tasks. Previous research has demonstrated the ability to generate robots for various tasks, but these approaches often optimize robots directly in the vast design space, resulting in robots with complicated morphologies that are hard to control. In response, this paper presents a novel coarse-to-fine method for designing multi-cellular robots. Initially, this strategy seeks optimal coarse-grained robots and progressively refines them. To mitigate the challenge of determining the precise refinement juncture during the coarse-to-fine transition, we introduce the Hyperbolic Embeddings for Robot Design (HERD) framework. HERD unifies robots of various granularity within a shared hyperbolic space and leverages a refined Cross-Entropy Method for optimization. This framework enables our method to autonomously identify areas of exploration in hyperbolic space and concentrate on regions demonstrating promise.  Finally, the extensive empirical studies on various challenging tasks sourced from EvoGym show our approach's superior efficiency and generalization capability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the task of multi-cellular soft robot design given a specific robotic task in simulation. 

It proposes a novel robot design optimization method to enable efficient optimal design search in a vast robot design space. The proposed method searches the design space in a coarse-to-fine manner. The design space is first transformed into a hyperbolic space, where each robot design is embedded into the hyperbolic space via a train-free strategy. The finer design has a larger embedding norm, forming a coarse-to-fine robot hierarchy in the hyperbolic space. Then, the Cross-Entropy Method is adopted to search in the hyperbolic space.

This paper uses 15 tasks from EvoGym for experiments. It compares with manual design and several robot design methods. It also conducts ablations on the coarse-to-fine and hyperbolic embeddings.

### Strengths
1. This paper is well-written.
2. The experiment section provides enough evaluations, i.e., 15 diverse tasks in the simulation.
2. Searching robot design space in a coarse-to-fine manner via hyperbolic space is novel.

### Weaknesses
1. The issue of local optimal (not very good performance compared to other baselines) and large variance: Does the parent node of an optimal robot design node consistently outperform the parent node of a non-optimal robot design node? If not, coarse-to-fine seems greedy and vulnerable to local optimal. The proposal method, HERD, appears to have no mechanism for exploration in the global design space, potentially leading to the high variance in Figure 3. And HERD is not significantly better than baselines.

2. The high variance observed in Figure 3 raises concerns about the robustness of the method. While the authors mention that this is a common challenge in robot design, the lack of a clear mechanism to mitigate this variance is a significant weakness. The performance fluctuations across different runs suggest that the method may be sensitive to initial conditions or random seeds, making it less reliable in practice. The stochastic nature of CEM, while providing some exploration, does not seem sufficient to overcome this issue, especially given the complex and high-dimensional design space.


### Questions
1. What are the policy architecture and learning methods adopted for the baselines? Are they the same as those of HERD?
2. HEARD w/o HE:  how to integrate NGE with CEM? Could you provide more details on this ablation?
3. How is the performance of a HandCrafted robot determined？ Does it use a transformer-PPO policy? If yes, it should also be reported with variance, e.g., in Figure 3. 
4. How can we guarantee that sequential refinements on a coarse design are better than sequential refinements on another coarse design, given that the former coarse design outperforms the latter coarse design?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a coarse-to-fine method for designing multi-cellular robots with hyperbolic geometry.

### Strengths
1. The paper is well written, easy to follow, the visualizations are nicely designed and the accompanying website shows impressive results.
2. Incorporating hyperbolic geometry into robot planning is innovative and interesting.
2. The experiment shows promising results over a variety of tasks.

### Weaknesses
1. As one of the concerns of multi-cellar system, the design space is very large, so how hyperbolic solution solved this problem is not well examined.
2. The quantitative analysis of the proposed model is somewhat absent, some tables will help the understanding of the evaluation of different methods.

### Questions
please see the weaknesses

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel co-design algorithm for multi-cellular robots. The authors noticed two critical insights 1. "coarse-grained robots are less complicated to design and control due to their low degree of freedom" and 2. "coarse-grained robots can usually solve part of the task". Built on these two insights, the authors proposed a coarse-to-fine design algorithm where a CEM optimizer optimize robot design in Poincare ball hyperbolic embedding space. The hyperbolic embedding embeds a coarse-to-fine tree structure so the optimization effectively. The authors benchmark the proposed algorithm on a variety of environments in evo-gym and shows the effectiveness of the algorithm.

### Strengths
- The writing quality of this paper is very good. All design choices are introduced with clear motivation. Ideas are explained clearly with text and high-quality figures.  
- It's quite novel for the authors to map the robot design to a space that has a favorable optimization landscape for methods as simple as CEM. 
- The two insights the authors point out, 1. "coarse-grained robots are less complicated to design and control due to their low degree of freedom" and 2. "coarse-grained robots can usually solve part of the task", has a potential to motivate new research
- The proposed method is a sound algorithm  to the cellular robot design problem and the experiments thoroughly justified the point.

Overall this is a technically solid paper with novel contributions that's clearly above acceptance threshold.

### Weaknesses
 - It's unclear how general is the hyperbolic space is for robotics design. See my questions in the next section
- It's unclear to me to me how exactly any point on the manifold correspond to a robot configuration. Some concrete example may help understanding. If I randomly sample a point using a coordinate, what's the robot configuration it correspond to? It seems that human has to handcraft such rules.


### Questions
- The authors chose Poincare ball as the hyperbolic embedding space for the design tree. I am wondering how general is this? In particular, hyperbolic manifold seems very limiting. For example, let's say the robot can be comprised of material A and material B. From the center, I extend two different trees branching towards material A and material B separately. However, in each branch, fine-grained branches start to contain configurations that blends A & B which means the two branches should merge. In this case, you will have to have a finite cylinder manifold, correct?

- How exactly does the manifold correspond to designs or robot parameters? How many branches are there? I understand how do you map between the euclidean space and the hyperbolic space but this seems unclear. Giving more visualizations across the disk manifold will be helpful.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the soft cellular robot design problem. Instead of traditional approaches that apply genetic algorithms directly in the design space, this paper proposes to optimize the robot design in the robot embedding space, specifically a 2D hyperbolic space defined by Poincare ball. It constructs the embedding space by first sampling a set of robots in a coarse-to-fine procedure and applying Sarkar’s method to construct the Poincare ball. It then finds the optimal design from the sampled set by applying CEM in the hyperbolic space. During design optimization, it follows previous work [1] to gradually adapt and optimize a transformer-based policy via PPO to control the robot designs in the current CEM population.

### Strengths
1. Parameterizing the discrete robot design space into continuous embedding space and optimizing the robot in this continuous space is novel and interesting.

2. The experiments clearly show the advantages of the proposed NERD over baselines.

### Weaknesses
1. The generalizability of the proposed approach to other robot design representations is uncertain. Testing the approach on one common robot design representation would make it more convincing. The current coarse-to-fine approach appears highly specialized for the cellular robot representation in EvoGym, relying on K-means clustering of cells. It is unclear how this would translate to articulated rigid robots, where the design space involves joints, links, and their associated parameters, which do not lend themselves to the same clustering approach. A demonstration on a more standard robot design representation, such as those used in Wang et al. 2019 [1] or Gupta 2021 [2], would significantly strengthen the paper's claims.

2. The choice of Sarkar’s construction for hyperbolic embedding needs more justification. While the paper mentions its ability to embed tree structures, it lacks a discussion of why this specific method is superior to other hyperbolic embedding techniques, particularly given the specific structure of the robot design hierarchy. A comparison with alternative methods and a discussion of their suitability for the robot design problem would be beneficial.

3. The experiments need improvements. While the paper shows results on 15 tasks from EvoGym, it does not include results for the remaining 17 tasks. This raises concerns about the overall robustness and generalizability of the proposed method. Furthermore, the ablation study lacks sufficient detail. For example, it is not clear how HERD w/o C2F samples the robot design set, and the absence of pseudo-code makes it difficult to understand the exact differences between the ablation variations.

### Questions
1. The coarse-to-fine process seems specialized for the cellular robot representation in EvoGym. Is it generalizable to other robot design representations, such as articulate rigid robots (e.g. Wang et al. 2019 [1], Gupta 2021 [2])?

2. Since coarse-to-fine clustering is based on running K-Means with different random seeds, it seems to be possible that there are two robot designs located in different subtrees. Will such two designs be embedded in similar locations in the hyperbolic space?

3. Being relevant to the last question, it seems that the cell type is not used during the embedding. If I understand correctly, the embedding only captures the structural/subdivision similarity but not the cell functionalities. How can we interpret the distance in the embedding space into the similarity between designs? 

4. Some notations are unnecessarily complicated. For example, it would be easier to understand if just saying the algorithm clusters the robot cells into 2, 4, 8, …, Nc/2, Nc components instead of using logarithm and exponential expressions.

5. Page 6 “In practice, similarity here means that fine-grained robots only need to change one component to be the same as their parent robots”. What does it mean? The fine-grained robots have more clusters than the parent robot, does it mean the fine-grained robots only change the cell type of one “new” cell cluster?

6. During the algorithm, is the robot design set fixed after the initial sampling? In other words, when you do $argmin$ in line 9 (Algorithm 1), do you always search for a design in the pre-sampled robot design pool?

7. After reading the paper, the phrase “coarse-to-fine” is indeed the way of building the candidate robot design pool instead of a coarse-to-fine optimization process. If this understanding is correct, the paper (especially the abstract and introduction) needs to be more clear about this point to prevent confusion.

8. EvoGym has 32 tasks however the algorithm is only tested on 15 of them. It would be great if the authors could evaluate the proposed algorithm on other tasks as well.

9. It would be great to provide the pseudo-code for the ablation variations to help understand the design of those ablation methods. For example, does HERD w/o C2F differ from full NERD mainly on the pre-sampled robot design set? So how does HERD w/o C2F sample the robot design set?
10. From the visual results, most of the optimized designs only have one single cell type. Does this result from the limitation of the embedding approach since the embedding only captures structural information but is not informative about the cell types?

11. How does the proposed embedding approach compare to other embedding approaches such as neural network embedding (e.g. GLSO [3])

[1] Tingwu Wang, Yuhao Zhou, Sanja Fidler, and Jimmy Ba. Neural graph evolution: Towards efficient automatic robot design

[2] Agrim Gupta, Linxi Fan, Surya Ganguli, and Li Fei-Fei. Metamorph: Learning universal controllers with transformers

[3] Jiaheng Hu, Julian Whitman, and Howie Choset. GLSO: Grammar-guided Latent Space Optimization for Sample-efficient Robot Design Automation

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
