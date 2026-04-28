# HASARD: A Benchmark for Harnessing Safe Reinforcement Learning with Doom

- Decision: Accept
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
The advancement of safe reinforcement learning (RL) faces numerous obstacles, including the lack of simulation environments, demanding computational requirements, and a lack of widely accepted benchmarks. To address these challenges, we introduce **HASARD** (A Benchmark for **HA**rnessing **SA**fe **R**einforcement Learning with **D**oom), tailored for egocentric pixel-based safe RL. HASARD features a suite of diverse and stochastic 3D environments. Unlike prior vision-based 3D task suites with simple navigation objectives, the environments require spatial comprehension, short-term planning, and active prediction to obtain high rewards while ensuring safety. The benchmark offers three difficulty levels to challenge advanced future methods while providing an easier training loop for more streamlined analysis. Accounting for the variety of potential safety protocols, HASARD supports both soft and hard safety constraints. An empirical evaluation of baseline methods highlights their limitations and demonstrates the benchmark's utility, emphasizing unique algorithmic challenges. The difficulty levels offer a built-in curriculum, enabling more efficient learning of safe policies at higher levels. HASARD utilizes heatmaps to visually trace and analyze agent navigation within the environment, offering an interpretive view of strategy development. Our work is the first benchmark to exclusively target vision-based embodied safe RL, offering a cost-effective and insightful way to explore the potential and boundaries of current and future safe RL methods. The environments, code, and baseline implementations will be open-sourced.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents HASARD, a benchmark tailored to vision-based safe reinforcement learning (RL) using egocentric, pixel-based inputs. Built on the ViZDoom platform, HASARD comprises six unique 3D environments across three difficulty levels, each designed to test safe RL in increasingly complex and dynamic scenarios. The benchmark allows for a range of agent objectives, from navigation to item collection and hazard avoidance, focusing explicitly on embodied safe RL with vision-based inputs.

### Strengths
Diverse Scenarios: HASARD provides varied 3D environments with different objectives and challenges, such as item collection, navigating hazardous terrain, and avoiding neutral units. This variety enriches the learning and testing possibilities, ensuring that the benchmark assesses both task performance and safety considerations.

Structured Curriculum: By offering three difficulty levels, HASARD presents a built-in curriculum for training RL agents, allowing gradual learning in increasingly challenging conditions. This approach is effective for developing robust agents that can generalize to new, more complex scenarios.

### Weaknesses
Outdated Baselines: All the baseline algorithms were published over two years ago, and the original implementations of these baselines do not support visual inputs. The lack of SOTA vision-input baselines, such as Lambda [1], Safe SLAC [2], and SafeDreamer [3], limits the benchmark’s relevance in evaluating current state-of-the-art safe RL methods. Specifically, the absence of evaluations using methods that combine world models with safety constraints is a significant oversight, as these approaches have shown promise in complex environments.

Solvability by Existing Algorithms: Have the tasks introduced in this framework already been solved by existing algorithms? For instance, can PPO-PID successfully address these tasks? Are there settings within HASARD that current algorithms struggle to handle? By not including experiments with the latest baselines, it is unclear whether the HASARD benchmark will drive the development of new algorithms or simply reaffirm existing solutions. The paper lacks a clear performance upper bound, making it difficult to assess whether the proposed tasks are genuinely challenging or if current methods already achieve near-optimal performance. A human baseline, or an evaluation with an extremely strong RL agent, would be necessary to establish this upper bound.

Task Complexity:
What is the primary contribution of HASARD compared to existing safety benchmarks, such as Safety Gymnasium? Compared to Safety Gymnasium, HASARD primarily adds hard constraints and fast simulation. However, implementing hard constraints is relatively straightforward, merely requiring a single line of code to terminate the episode upon any unsafe action. As for fast simulation, HASARD achieves this by sacrificing simulation fidelity and simplifying the action space, which limits its meaningfulness as a contribution compared to Safety Gymnasium. The action space simplification, while improving simulation speed, may also reduce the complexity of the control problem, making it less representative of real-world scenarios. Moreover, most tasks in HASARD revolve around avoiding hazardous obstacles, which has already been extensively addressed and solved in Safety Gymnasium by existing algorithms (e.g., [1-3]). Given HASARD's simplified dynamics and action space, it would need to introduce more complex tasks than those in Safety Gymnasium to stimulate the development of new algorithms. However, I did not observe any such complexity in the task design that would distinguish it from prior benchmarks.

### Questions
1. Which tasks in HASARD require memory capabilities, and which involve long-horizon decision-making? It would be helpful if the authors could clarify how the benchmark challenges an agent’s memory and planning capabilities over extended time sequences.

2.  Why did you choose ViZDoom to build this benchmark? Does this platform offer specific advantages? From my perspective, it seems that ViZDoom allows only minor modifications to its existing game structure and may lack the flexibility to define more complex, varied tasks. Why not consider using a truly open-world environment, such as MineDojo [4], which enables safer RL environments with more sophisticated task definitions? A platform like MineDojo could potentially support a broader range of scenarios and facilitate more diverse task creation.

3. Additionally, I noticed that you used Omnisafe for algorithm benchmarking, but this wasn’t mentioned in the paper. I have some questions regarding one of the baselines you implemented. In the P3O algorithm code (see here:https://github.com/PKU-Alignment/omnisafe/blob/main/omnisafe/algorithms/on_policy/penalty_function/p3o.py#L82), there is a term  J_c  in the loss function that appears to be independent of the network parameters. What effect does including J_c in the loss function have? I observed in your experimental results that P3O also fails to satisfy the constraints, which may be related to the J_c term. This raises some doubts about the effectiveness of this baseline.

[4] MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge

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
4

### Summary
HASARD is a benchmark testing platform specifically designed for safe reinforcement learning, based on ViZDoom, providing a diverse range of 3D environments.

1. The tasks on this platform require agents to pursue high rewards while considering safety strategies, moving beyond simple 2D navigation to incorporate complex elements such as spatial understanding.
2. HASARD offers three difficulty levels and supports both soft and hard safety constraints, flexibly adapting to varying safety requirements.
3. The platform integrates Sample-Factory, enabling high-speed simulation that allows agents to address real-world safety challenges while reducing computational costs.
4. HASARD includes six environments based on ViZDoom and benchmarks various methods to demonstrate the limitations of existing technologies.

### Strengths
1. The authors tested six baseline algorithms on HASARD and provided an analysis of the results.
2. The tasks move beyond simple 2D navigation to incorporate complex elements such as spatial understanding

### Weaknesses
1. The reviewer believes that if the distinction between soft and hard constraints is merely based on whether the threshold is $0$, then other benchmarks share this characteristic, making this claim somewhat unsubstantiated.
2. Although multiple methods were tested in the current experiments, there is a lack of analysis on performance under different safety budgets. It is recommended to include experiments with varying safety thresholds to better understand the trade-off between safety and reward for each algorithm.
3. HASARD is based on the ViZDoom game engine, which, while computationally inexpensive, lacks detailed simulation of real-world physics.
4. The anonymous video link provided by the authors is inaccessible.

### Questions
1. The article does not provide an in-depth analysis of performance under different safety budgets. Is there a plan to supplement the experiments with varying safety thresholds to comprehensively demonstrate the trade-offs between reward and safety for each algorithm? This would be very helpful in understanding the adaptability of different methods under various safety requirements.
2. Considering the limitations of ViZDoom in simulating real-world physics, have the authors explored other engines with superior physical simulation capabilities (e.g., Isaac Gym)?

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
The paper proposes a new egocentric vision-based 3D simulated environment for benchmarking safe reinforcement learning. The benchmark is more realistic and challenging compared to common prior safe RL benchmark environments. In addition, the paper has evaluations for some safe RL algorithms on the proposed benchmark demonstrating its feasibility of use and the potential for building better approaches to perform more favorably on it.

### Strengths
- The paper is well motivated and targets an important problem - that of building realistic and reliable RL benchmarks, and more specifically benchmarks for safe RL. This involves addressing challenges with the simple natural of prior benchmarks - both visually and in terms of higher dimensional action space and increased temporal horizons. 

- The proposed benchmark HASARD is built on top of an existing game engine VizDoom and is able to inherit all of its properties for re-use. The multiple levels in HASARD can be potentially helpful in evaluating different notions of safety in proposed safe RL algorithms. 

- The paper has detailed evaluations of several safe RL algorithms on HASARD indicating that the framework is feasible for training constrained RL policies. The evaluations reveal that simple algorithms based on PPO and constrained PPO can achieve non-trivial performance in the benchmark and also reasonable constraint satisfaction. It is good to see that these simple algorithms do not saturate the benchmark and there is still a lot of room for improvement.

### Weaknesses
 - Unfortunately, while the paper is a decent attempt at building a safe RL benchmark, I am not convinced the safe RL community will be incentivized to use it. The main reason is that the notions of constraints in this benchmark are not directly tied to the very pragmatic safety considerations that need to be tackled in the real world - ranging from control systems to robotic deployments. The constraints, such as avoiding certain areas or limiting resource consumption within the game, lack the direct physical grounding that is crucial for real-world safety applications. This makes it difficult to translate the findings from this benchmark to practical scenarios where safety is paramount, such as in robotics or autonomous systems.

- The benchmark feels a bit incremental compared to the already existing VizDoom framework that has been around for years. The modifications for the different levels and environments in this framework do not capture the notions of open-world generalization and realism the field is headed towards in terms of evaluating RL systems. The visual fidelity and physics simulation of VizDoom are quite basic, lacking the complexities of real-world environments. This limits the ability of the benchmark to test the robustness and generalization capabilities of safe RL algorithms. In addition, a lot of prior safe RL works have bechmakred their systems on real-world systems like robotic navigation and manipulation, and I am not convinced that a modified VizDoom framework is likely to create a reasonable impact in the community.

- The evaluations are all with variants of PPO and no other safe RL algorithms are tested. It is unclear why this is the case, since in my understanding the benchmark should not be tied to a particular type of algorithm. The lack of diversity in the tested algorithms raises concerns about the benchmark's generality and its ability to evaluate a wide range of safe RL techniques. The exclusive use of PPO variants may bias the results and not fully explore the potential of the benchmark for other safe RL methods.

### Questions
Please refer to the weaknesses above:

- Unfortunately, while the paper is a decent attempt at building a safe RL benchmark, I am not convinced the safe RL community will be incentivized to use it. The main reason is that the notions of constraints in this benchmark are not directly tied to the very pragmatic safety considerations that need to be tackled in the real world - ranging from control systems to robotic deployments. Could the authors clarify how exactly they envision this benchmark to drive innovation in the safe RL community? And what sub-field of researchers would be likely to use it?

- The benchmark feels a bit incremental compared to the already existing VizDoom framework that has been around for years. Can the authors clarify if the proposed modifications are non-trivial and if they can be broadly applied to potentially other frameworks like Minecraft and other games?

- The evaluations are all with variants of PPO and no other safe RL algorithms are tested. It is unclear why this is the case, since in my understanding the benchmark should not be tied to a particular type of algorithm. Please clarify the evaluations and if there is any specific assumption on the type of safe RL algorithms that could be tested on the benchmark? 

- Can the authors make 1-1 comparisons with the proposed benchmark and the features of prior simulated and real world benchmarks that have been used by safe RL papers in  the past?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces the HASARD, a benchmark designed for egocentric pixel-based safe RL in diverse and stochastic 3D environments. Unlike existing benchmarks, HASARD emphasizes spatial comprehension, short-term planning, and active prediction for high rewards while ensuring safety. It offers three difficulty levels, supporting both soft and hard safety constraints. The benchmark includes heatmaps for visual analysis, aiding in strategy development. By targeting vision-based embodied safe RL, HASARD addresses the need for benchmarks mirroring real-world complexities. The paper's contributions include the design of six novel ViZDoom environments with safety constraints, integration with Sample-Factory for rapid simulation and training. Evaluation of baseline methods within HASARD highlights challenges in balancing performance and safety under constraints.

### Strengths
The paper demonstrates several notable strengths across the dimensions of originality, quality, clarity, and significance: 

  

1. **Originality**: It introduces HASARD, a benchmark specifically designed for vision-based embodied safe reinforcement learning (RL) in complex 3D environments. 

  

2. **Quality**: Comprehensive design of 6 diverse environments with 3 difficulty levels each, offering a range of challenges. 

  

3. **Clarity**: The paper is structured in a logical and coherent manner, facilitating the understanding of complex concepts. 

  

4. **Significance**: The paper Addresses an important need in safe RL research for more realistic and challenging benchmarks. It enables systematic evaluation and comparison of safe RL algorithms in vision-based 3D settings.

### Weaknesses
While the paper makes valuable contributions, several areas could be improved: 


1. The paper refers to ViZDoom as a 3D environment, but its pixelated, less detailed graphics compared to modern 3D games challenge this characterization. The use of sprites and precomputed lighting, rather than true 3D rendering with dynamic lighting and shadows, raises questions about the realism of the visual input. This difference in rendering techniques could limit the transferability of learned policies to more complex, visually rich environments.


2.  **Narrow Range of Baselines**: Evaluations focus primarily on PPO-based algorithms. Incorporating a more diverse set of methods, such as model-based safe RL or constrained policy optimization, would provide a more comprehensive assessment of the benchmark's challenges. Specifically, methods that explicitly model safety constraints or utilize predictive models could offer valuable insights into the benchmark's difficulty. The absence of these methods limits the scope of the evaluation.


3.  **Limited Visual Input Analysis**: Though vision-based learning is emphasized, the paper lacks a thorough analysis of how visual complexity impacts performance. The paper should explore how different visual conditions, such as varying lighting, the presence of distractors, or changes in texture, affect the performance of safe RL agents. Furthermore, comparing raw pixel inputs with simplified representations, such as segmented or depth-enhanced observations, would highlight the unique challenges of vision-based safe RL in this environment, especially given the less realistic visual inputs.


4.  **Action Space Limitation**: Only discrete action spaces are supported. The lack of support for continuous action spaces limits the benchmark's applicability to a subset of safe RL algorithms. Many real-world robotic control tasks require continuous action spaces, and the absence of this feature makes it unclear how such algorithms would be benchmarked.


5.  **Real-World Relevance**: The connection between the benchmark tasks and real-world safe RL challenges needs clearer articulation. While the paper mentions the importance of spatial reasoning and planning, it lacks concrete examples of how these skills translate to practical applications. Providing specific use cases would strengthen the motivation for the benchmark and its relevance to real-world problems.

### Questions
1. Is ViZDoom truly a 3D environment, considering its graphics appear pixelated and less detailed compared to modern 3D games? 

  

2. Why are the baseline algorithms limited to PPO-based approaches? Could the paper include more diverse methods, such as model-based safe RL or constrained policy optimization (e.g., https://arxiv.org/abs/2210.07573)? 

  

3. How can continuous safe RL algorithms be benchmarked when the paper only supports discrete action spaces?

### Soundness
3

### Presentation
3

### Contribution
3
