# Multi-Robot Motion Planning with Diffusion Models

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
Diffusion models have recently been successfully applied to a wide range of robotics applications for learning complex multi-modal behaviors from data. However, prior works have mostly been confined to single-robot and small-scale environments due to the high sample complexity of learning multi-robot diffusion models. In this paper, we propose a method for generating collision-free multi-robot trajectories that conform to underlying data distributions while using only single-robot data.
Our algorithm, Multi-robot Multi-model planning Diffusion (MMD), does so by combining learned diffusion models with classical search-based techniques---generating data-driven motions under collision constraints. 
Scaling further, we show how to compose multiple diffusion models to plan in large environments where a single diffusion model fails to generalize well. We demonstrate the effectiveness of our approach in planning for dozens of robots in a variety of simulated scenarios motivated by logistics environments.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a multi-robot motion planning algorithm leveraging diffusion models and MAPF algorithms. In the proposed MMD algorithm, a conditional diffusion model is used to generate collision-free trajectories for the robot, and MAPF provides the logic to impose constraints on robots such that it scales in a multi-agent setting. The paper benchmarks with A* search and tests it on multiple multiagent tasks with varying complexity. The results show good success rate and data adherence for the proposed methods.

### Strengths
1. This paper provides a very thorough discussion of how to combine MAPF algorithms with diffusion models and demonstrate its ability to scale to multi-agent settings.
2. The experiment setting is diverse with varying levels of difficulties.
3. The writing is clear and structured and the paper is easy to read.

### Weaknesses
1. It would be good to discuss other search algorithms in multi-agent motion planning or at least discuss why only A* is chosen
2. In Sec. 4.2, it would be good to discuss the computational complexity between A* and MMD.
3. The explanation of the motion pattern is insufficient. Then it becomes a bit confusing in Sec 3.3 how this task-relevant local diffusion model works and also in Sec. 4 what the data adherence means.

### Questions
1. Can you explain more about what the motion pattern is? Also how this task-relevent local diffusion works and how data adherence works based on this.
2. In Figure 3, do you have an intuition as that why A* methods maintain a good success rate for (b) and (c) even though the agent number keeps increasing? Is there any tradeoff with the computational efficiency compared to MMD?
3. Is there any other search algorithm other than A* that should we consider? Can have a closer connection between the related work and the baseline methods.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on the collision-free multi-robot planning problem. They combine single-robot diffusion planning models with multi-agent path finding (MAPF) algorithms. They leverage different MAPF algorithms to generate spatio-temporal constraint functions and use these functions to guide diffusion planning models to generate soft-constraint multi-robot trajectories.

### Strengths
* The questions of multi-robot motion planning that the paper aims to solve is meaningful and it has many real-world applications like automated warehouses.
* The method proposed by the paper is diretly and simple. They leverage state-of-art single-robot diffusion planning methods with classifical MAPF algorithms to solve multi-robot motion planning problems.
* They also evaluate their approaches in a variety of simulated scenarios and show better performance. They also conduct rich ablation studies including planning time, different strategies.

### Weaknesses
 * The novelty of the method seems limited. The paper seems simply combine diffusion planning methods and classifical MAPF algorithms. In the method section (3.2), It's hard to judge which parts are from classifical MAPF algorithms, which parts are contributed by the paper to adapt MAPF algorithms into diffusion planning methods.
* Lack of some experimental details and results. See questions.
* The methods are not very efficient when the number of agents increases.

### Questions
* How is the single-robot diffusion models training? Which dataset? Is it a single-robot dataset or a multi-robot dataset?
* Search-based algorithms (A*) achieve a higher success rate compared to MMD. Is it fair to compare search-based algorithms at data adherence scores since search-based algorithms are not learned from dataset?
* The performances of MPD are very low even if the number of agents is less than 5. Is it normal?

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
This paper presents a novel approach for multi-robot motion planning (MRMP) that combines diffusion models with multi-agent pathfinding (MAPF) constraint strategies. This approach leverages single-robot diffusion models to plan multi-robot trajectories while avoiding collisions and scaling well to larger, complex environments. Extensive simulations demonstrate this approach’s success in generating smooth, collision-free paths with high adherence to data distribution.

### Strengths
This paper introduces a novel approach for multi-robot motion planning, particularly in combination MAPF with diffusion models. This approach sidesteps the challenge of multi-agent data collection by training on single-robot data, allowing the method to efficiently address the curse of dimensionality typically seen in large-scale multi-agent systems. Also, it incorporates MAPF-based constraint methods, such as Conflict-Based Search, to dynamically enforce collision-free paths.

By using an ensemble of diffusion models for each robot, the capability of scaling the approach to large environments with numerous robots, without retraining, is a notable advantage. This makes the method adaptable to a range of real-world applications.

This paper provides a solid comparison of multiple MMD variants, which helps to assess the strengths and weaknesses of different constraint strategies. This thorough analysis adds value to the paper’s contributions.

The simulations conducted in various scenarios help validate the approach. Also, the success rates and data adherence scores are well presented.

### Weaknesses
A major limitation is the reliance on single-robot data for policy learning. This assumption may not be sufficient for complex, dynamic environments where multi-robot interactions are essential. While multiple experiments demonstrate the effectiveness of this approach, exploring the differences between multi-agent and single-agent data, and how single-agent data can benefit cooperative multi-robot motion planning, would add valuable insight.



### Questions
1. This paper could benefit from a more detailed discussion of the computational overhead, especially regarding the MAPF constraint strategies and the diffusion model’s denoising process.

2. Could you further clarify the computational trade-offs between the five MMD variants? It would help to know if certain strategies are more suitable for specific environments or robot counts.

3. How effectively does the approach generalize beyond warehouse-like environments? Could it perform well in less structured or highly dynamic settings?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses the challenge of collision-free multi-robot motion planning (MRMP) using diffusion models, aiming to enable the coordination of multiple robots with limited training data by leveraging single-robot trajectories. The proposed Multi-robot Multi-model planning Diffusion (MMD) method integrates single-robot diffusion models with constraint-based MAPF (multi-agent pathfinding) techniques, enabling multi-robot trajectory diffusion. MMD adapts classical MAPF strategies, including Prioritized Planning (PP) and Conflict-Based Search (CBS), to impose spatial and temporal constraints within the diffusion process, ensuring collision avoidance. An ensemble of local diffusion models is employed for long-horizon planning by sequencing trajectories across different environment contexts.

Evaluation is conducted through simulated tests across multiple scenarios and environments, including logistics-inspired settings with varying numbers of robots. Metrics used include success rates, data adherence (alignment of trajectories with data-derived patterns), and computation time. Comparisons are made with MAPF baselines and composite diffusion models trained with multi-robot data.

### Strengths
MAPF can be considered a hierarchical planning method for multi-robots, consisting of a high-level "negotiation" mechanism and a low-level "motion" planner.

1. It is interesting to see how the MPD [1] advantages are utilized in MAPF algorithms. Classical MAPF algorithms usually utilize RRT or PRM planners as underlying collision-avoidance planning. Indeed, utilizing a single-robot MPD model, which typically captures the local multimodality of planning behaviors as a learned smooth collision-avoidance mechanism, is a very interesting idea.

2.  The significance of MMD lies in amortization [2] low-level planning with MPD, which can infer a batch of solution efficiently (i.e., with a forward pass) without RRT or PRM subroutines. This is crucial since high-level multi-agent negotiation may induce many constraints for low-level and thus significantly speed up the overall algorithm.

3. The motivation is well-discussed, and the overall method is presented clearly.

[1] Carvalho, Joao, et al. "Motion planning diffusion: Learning and planning of robot motions with diffusion models." 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, 2023.

[2] Amos, Brandon. "Tutorial on amortized optimization." Foundations and Trends® in Machine Learning 16.5 (2023): 592-732.

### Weaknesses
1. It is unfortunate that this work does not consider Multi-Robot Planning with Gaussian Belief Propagation (GBP) [3], which I believe could seamlessly integrate with the MPD framework. [3] utilizes factor-graph formulation to communicate between agents, and it is straightforward to incorporate these signals into the guidance cost term Eq. 4. In contrast, MMD-CBS formulation has combinatoric negotiation between agents inherited from classical MAPF algorithms. There should be some discussions (as future works) on integrating GBP to MMD with potential advantages (e.g., distributed planning over an arbitrary time window, removing combinatoric negotiation via message-passing over factor graph) and disadvantages (e.g., high memory cost with many factors due to increasing trajectory length and number of agents, etc.).

2. The experiment outline is thoughtful and supports the main claims with good metrics and benchmarks. However, I believe the paper would be much stronger if MMD (and its variants) were additionally compared to bare GBP [3] in these benchmarks of Sec 4.2 and the long-horizon setting of Sec 4.3.

### Questions
1. I am curious to see how well the learning method MMD performs against bare GBP [3] as an additional baseline in highly-congested maps such as Circle and Weave setups and large maps such as 2 x 2 and 3 x 3 maps with increasing agents to 50 to further assess the scalability, with the same proposed metrics of SR and adherence. This will also shed light implicitly on how well GBP compares to classical MAPF algorithms, which benefits the MAPF community further. The code of GBP is publicly available [here](https://github.com/aalpatya/gbpplanner).

2. Please discuss the potential advantages and disadvantages of integrating GBP to MMD, as stated above.

### Soundness
3

### Presentation
4

### Contribution
4
