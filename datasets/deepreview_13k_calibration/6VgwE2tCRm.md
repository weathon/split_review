# POGEMA: A Benchmark Platform for Cooperative Multi-Agent Navigation

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Multi-agent reinforcement learning (MARL) has recently excelled in solving challenging cooperative and competitive multi-agent problems in various environments with, mostly, few agents and full observability. Moreover, a range of crucial robotics-related tasks, such as multi-robot navigation and obstacle avoidance, that have been conventionally approached with the classical non-learnable methods (e.g., heuristic search) is currently suggested to be solved by the learning-based or hybrid methods. Still, in this domain, it is hard, not to say impossible, to conduct a fair comparison between classical, learning-based, and hybrid approaches due to the lack of a unified framework that supports both learning and evaluation. To this end, we introduce POGEMA, a set of comprehensive tools that includes a fast environment for learning, a generator of problem instances, the collection of pre-defined ones, a visualization toolkit, and a benchmarking tool that allows automated evaluation. We introduce and specify an evaluation protocol defining a range of domain-related metrics computed on the basics of the primary evaluation indicators (such as success rate and path length), allowing a fair multi-fold comparison. The results of such a comparison, which involves a variety of state-of-the-art MARL, search-based, and hybrid methods, are presented.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces POGEMA, a benchmark for multi-agent pathfinding (MAPF) and its lifelong version (LMAPF) on grids. The contributions include a fast CPU-based environment, problem generators, visualization, and benchmarking tool for learnable, hybrid, and purely learned approaches.

### Strengths
The writing of this paper is crisp, and the visualizations are of excellent quality. The authors provide several examples and extensive code. While this is not the first paper to focus on MARL navigation, it is the first to fully focus on MAPF variants in a single repository. The proposed metrics are a much-needed tool to assess the performance of (L)MAPF approaches, not just based on the classical SoC/throughput but also on other metrics that can identify possible research directions.

### Weaknesses
1. The title and abstract are misleading about the scope of the paper: while POGEMA appeals to a broad audience of MARL-based navigation in the title and abstract, in fact, it is about two variants of MAPF on discrete grids with simplified settings. For instance, in terms of MAPF, continuous variants like [1] do not appear to be considered. Moreover, there does not seem to be any mention of any-angle versions that would make the problem more realistic and interesting like [2].

2. One main concern about this paper is that while authors introduce a new MARL environment, they mostly perform inference with it, and several results are not reproduced by retraining models. For instance, the DCC and SCRIMP codes do not contain any training script or guidance on how to reproduce results. Comparing training performance or speed with the proposed environment against the original implementation would strengthen the paper. Specifically, it would be beneficial to see how POGEMA facilitates or accelerates the training process compared to the original environments used for these methods.

3. Authors claim scalability of >1000 agents. I cannot find any result to substantiate this claim. The paper should include experiments demonstrating performance with over 1000 agents, ideally with comparisons to existing methods that struggle to scale to this level.

4. The LaCAM version the authors mention refers to the first publication. However, new variants were released open source, i.e. LaCAM3 [3]. Moreover, versions as [4] can solve scales up to 10k agents in seconds. The paper should be updated to reflect the latest developments in LaCAM, including a comparison with LaCAM3 and other highly scalable solvers.

5. Authors acknowledge the limitation of lack of JAX support and GPU-based parallelization tools. In this aspect, I believe the proposed (L)MAPF environments could be created by quite simple modifications of existing environments in Jumanji as the RobotWarehouse. The paper should either justify the decision not to use JAX or explore the possibility of adapting existing JAX-based environments for (L)MAPF.

6. While this is a relatively minor point, I believe there are quite a few problems in terms of writing for the related work. Firstly: I don’t see why the paper should mention all multi-agent benchmarks, when the considered problems are only two very specialized ones. In this sense, Table 1 should contain information about “topic” or “area,” which is missing. GPU parallelization is not considered in the table. The main issue here is that it appears that POGEMA solves all the issues of previous MARL benchmarks such as Nocturne, while they solve arguably much simpler problems in restricted settings. Finally: I don’t see why there is a need to explain every single component as a separate paragraph for a total of almost 3 pages, such as “Python-based” and “PyPI listed”.

7. Finally, as a benchmark, it would be nice to include insights, i.e., what are possible future directions of research. Looking at the graph, one might conclude that there is no point in conducting research in MARL+MAPF, given that heuristic approaches perform well in all metrics, except scalability, only for the LMAPF case.

### Questions
1. One problem I have about the paper is more on the conceptual level, i.e. why the “PO” in POGEMA. “PO” stands for partially observable, and this makes sense in unknown environments that need exploration, such as the mentioned Nocturne benchmark. However, in the case of the proposed benchmark, I do not see why one should limit the observability as partial. Indeed, in my experience, the (L)MAPF problem arises in industrial settings in which maps are known a priori, which motivates the use of global heuristic controllers such as Lacam and RHCR. Why is partial observability used in such discrete settings, while SOTA heuristic approaches don’t use such a notion? Could leveraging full maps improve the performance of underperforming neural approaches?
    
2. What is the impact of sparse vs dense rewards in MARL for MAPF? Is it better to give +1 only at the end of the episode or a dense reward at each step?
    
3. In terms of conclusions for such a benchmark, it would be more interesting to identify the shortcomings of current models and help identify future research directions. What do you think these could be?

### Soundness
3

### Presentation
4

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
This paper presents a benchmark for multi-agent navigation tasks. The overall work includes a fast and scalable environment for multi-agent navigation tasks, a series of built-in tasks, a set of visualization tools, and an evaluation framework.

### Strengths
1. The overall platform proposed in this paper is capable of integrating search-based, learning-based, and hybrid approaches together, using the same metric for comparison.
2. As an environment that supports large-scale multi-agent reinforcement learning algorithm training, performing more than 10K steps per second is quite remarkable.

### Weaknesses
(Major) The primary issue with this paper is that its contributions are not sufficiently prominent. As a benchmark in the multi-agent systems domain, POGEMA's positioning is unclear and lacks irreplaceable advantages. For instance, for a researcher in the MARL domain, it may mainly offer features related to partial observability, rapid training, and scalability to >1000 agents. However, benchmarks already exist in the MARL domain that possess these characteristics, such as [1][2], making this work not irreplaceable. Specifically, while the environment claims scalability, it is unclear how this is achieved beyond simply increasing the number of agents, and whether the complexity of the environment scales accordingly. For a researcher interested in the domain of multi-agent cooperative navigation, the overall scenario elements of this work are overly simplified and idealized, presenting a significant gap from real-world scenarios. The environment's grid-based nature and discrete action space limit its applicability to real-world robotic systems, which often operate in continuous spaces with complex dynamics. It might be better to focus more on issues in real-world applications, such as unexpected situations in open environments and the transferability of algorithms from simulation to reality.


(Minor) There are concerns and suggestions regarding the writing of the introduction part. For example, the content about decentralized cooperative learning discussed in lines 53-58, is it closely related to the necessity of this work? Similarly, the transition in lines 59-77 related to partial observability and large-scale agents is too lengthy and seems not to be the focus of the problems the paper intends to solve. A well-written introduction should quickly highlight contradictions and then state the necessity of the work. Writing too much content with no clear relevance can impact readability.

### Questions
In addition to my primary concerns, there are also the following questions: 
1. Please carefully check the writing of the paper. For example, on the first line of the third page, "both" needs to be removed.
2. Is it "NP-Hard" or "HP-Hard" in line 88 of the paper? 
3. The definitions of competitive and cooperative behaviors in lines 221-225 might not be rigorous enough. For instance, in competitive behaviors, the rewards of agents might not sum up to a fixed value but could have a relationship akin to being inversely proportional; in cooperative behaviors, agents do not necessarily share rewards, but they are working towards the same task. Do the authors have a more rigorous perspective on this?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a new benchmark for multi-agent path-planning and reinforcement learning. The main contribution of the new benchmark appears to be its ability to be computationally efficient, the ability to procedurally generate new problems, and to allow a diverse set of map styles. The tasks are generally navigation tasks, in which an agent has to avoid collisions and reach a goal. The paper presents sufficient details on the new benchmark and compares a large number of different MARL and other multi-agent path planning algorithms.

### Strengths
- I like the extensive comparison and differentiation to previous multi-agent environments
- I appreciate the large number of evaluated algorithms on the new benchmark
- The analysis and experimental studies in this paper are strong
- The new environment seems to be in particularly interesting when evaluating a large number of agents in large environments
- I like that the authors promise to release the code under an open-access license.

### Weaknesses
 - While I appreciate the computational efficiency and the ability to procedurally generate new environments, I am wondering after reading the paper if the benchmark can further the field by sparking new ideas or raising open problems. The benchmark seems more like an engineering achievement allowing the study of larger agent populations, but I am wondering if this is really _the_ open problem we need to consider in MARL.
- Similarly, the observation space seems relatively simple. I may have missed it, but there is also no uncertainty or noise in the sensor measurements. Again, this reinforces the impression that the introduced task-sets are relatively simple, I am failing a bit to see that this will truly push forward the field.
- This is due to the fact that the considered environments are, in principle, simple, as they are _just_ navigation tasks requiring a minimalistic representation. Again, I worry this is simply a too-simple set of tasks to further the research frontier...

### Questions
Feel free to respond to my concerns raised in the weaknesses. Overall, I think the implementation work seems good, the evaluation of algorithms extensive, but I fail to see the truly novel aspect where this will raise new open questions for multi-agent planning, new avenues for research or challenge the existing algorithms. 

Hence, a rating of 6 may be the highest I am willing to give the paper in its current state.

### Soundness
3

### Presentation
4

### Contribution
2
