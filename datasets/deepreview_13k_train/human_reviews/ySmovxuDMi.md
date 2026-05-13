# HIVEX: A High-Impact Environment Suite for Multi-Agent Research

- Decision: Reject
- Scores: 3, 5, 6, 3

## Abstract
Games have been vital test beds for the rapid development of Agent-based research. Remarkable progress has been achieved in the past, but it is unclear if the findings equip for real-world problems. While pressure grows, some of the most critical ecological challenges can find mitigation and prevention solutions through technology and its applications. Most real-world domains include multi-agent scenarios and require machine-machine and human-machine collaboration. Open-source environments have not advanced and are often toy scenarios, too abstract or not suitable for multi-agent research. By mimicking real-world problems and increasing the complexity of environments, we hope to advance state-of-the-art multi-agent research and inspire researchers to work on immediate real-world problems. Here, we present HIVEX, an environment suite to benchmark multi-agent research focusing on ecological challenges. HIVEX includes the following environments: Wind Farm Control, Wildfire Resource Management, Drone-Based Reforestation, Ocean Plastic Collection, and Aerial Wildfire Suppression. We provide environments, training examples, and baselines for the main and sub-tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces HIVEX, a benchmark for multi-agent reinforcement learning that addresses critical ecological challenges. It includes five environments with varying levels of difficulty and supports over ten agents, accepting both vector and image inputs. Episodes can last up to 5000 steps. The benchmark provides PPO as a baseline, running through different environments and presenting the results.

### Strengths
1. It provides comprehensive code for both evaluation and training.
2. The task design is well-structured, and the benchmark’s support for image input is both rare and crucial for advancing multi-agent reinforcement learning (MARL) development.

### Weaknesses
1. The methods tested are quite limited, with only PPO evaluated. Have you considered testing additional methods like MAPPO or MAA2C?
2. The reward structure doesn’t clearly reflect the difficulty levels of the tasks. What is the best performance achievable with an optimal policy?
3. The role of image input is unclear. How does your method utilize visual inputs? If tasks are still achievable without image input, what is the intended value of including them?
4. The advantages of HIVEX compared to benchmarks like Melting Pot and Neural MMO remain unclear.
5. How can this benchmark be expanded? Is it easy for users to create custom tasks or modify existing ones within your benchmark?
6. Lack of innovation in new methods. How could the training pipeline or algorithm be modified to achieve better results?

### Questions
Please see the Weakness.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a benchmark for multiagent research. The benchmark provides environments about ecological challenges including wind farm control, wildfire resource management, drone-based reforestation, ocean plastic collection, and aerial wildfire suppression. This paper claims that the proposed benchmark presents more realistic environments than existing benchmarks, so the findings in the proposed benchmark have more potential to be equipped for real-world problems.

### Strengths
1. This work uses the Unity engine to create multiple environments representing ecological challenges and allows each environment to have different difficulties. Moreover, each environment provides both vector observations and visual observations, which is more realistic than many existing environments

2. Some environments allow their features to be procedurally generated and the test-time evaluation can use environments that have never been seen.

3. This work provides evaluation results for each environment which can serve as the baselines for future works.

### Weaknesses
1. This paper claims that the proposed environments are more realistic than existing environments. However, according to the description of the paper, this is done only by adding visual representations and low-level action/state space. It is unclear how accurately the environments can simulate the real-world environment, for example, the uncertainty of state transition. Therefore, the sim-to-real gap can still be considerably large. I know that the authors have discussed this in the limitation section, but it is indeed a problem that weakens the contribution of this work.

2. This paper proposes environments for multiagent research. However, when generating baselines for evaluation, this work only tests the performance of the PPO algorithm. Why not try some multiagent RL algorithms as the environments are for multiagent research?

3. The authors claim that Wildfire Resource Management and Ocean Plastic Collection are excluded from scalability tests because of fixed layout, agent count, and amount of plastic. Why these are fixed? The environments should allow for configuration like other environments.

### Questions
Please see the Weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel benchmark designed for multi-agent control systems, specifically tailored to address the challenges posed by climate change. This paper opens by emphasizing the critical nature of climate change and underscores the significance of climate research, thereby establishing the relevance and importance of the proposed benchmark. It proceeds to offer succinct introductions to each environment within the benchmark, detailing their contents and associated tasks via visually engaging interfaces and foundational setup descriptions. Subsequently, the paper employs classical PPO algorithms to execute comprehensive experiments across all environments and varying levels of complexity within the benchmark, effectively illustrating its exploratory potential and validity. Furthermore, it furnishes baseline performance metrics, facilitating future research endeavors on the benchmark. Overall, this work presents an innovative multi-agent cooperation benchmark within the climate domain, addressing the deficiency of suitable experimental platforms in this area and offering robust support for subsequent investigations.

### Strengths
1. Each environment is accompanied by lucid diagrams, aiding the reader in comprehending the numerous influencing factors and configurations present. The visually appealing interface also intuitively conveys the rendering capabilities of the environment.
2. The RELATED WORK section is thorough and informative, contrasting a multitude of existing multi-agent benchmarks, thereby enabling readers to grasp the current landscape of benchmark development in the multi-agent field and the underlying rationale for this study.
3. The experimental section includes assessments conducted at different difficulty levels for each environment, indicating substantial untapped potential for foundational reinforcement learning algorithms. This offers researchers objective comparative data to understand the essential characteristics of each environment and its respective challenges.

### Weaknesses
1. The paper does not clearly distinguish between the challenges inherent in the environments themselves versus the challenges posed by the tasks within those environments. A more explicit discussion of the specific difficulties in simulating climate-related phenomena, such as the complex interactions of environmental factors or the non-linear progression of climate change effects, would better justify the need for this benchmark. Highlighting the immediate needs for simulation environments within this domain could aid readers new to the field in appreciating the necessity of developing such a simulation environment.
2. The descriptions of the environment setups appear fragmented, detracting from the overall coherence of the manuscript. The current presentation makes it difficult to quickly grasp the key parameters and configurations for each environment. Consolidating these details into a unified format, perhaps through a tabulated summary of ENVIRONMENT SPECIFICATIONS alongside brief overviews of key points, would enhance clarity and conciseness. For example, a table could include parameters such as the number of agents, action space dimensionality, observation space characteristics, and key environmental variables for each scenario.
3. Despite being a pioneering effort in proposing a climate-focused benchmark, the paper would benefit from a tabular comparison highlighting the attributes of the proposed benchmark relative to other multi-agent environments. This comparison should not only focus on the application domain (climate) but also on technical aspects such as the complexity of the environment dynamics, the types of multi-agent interactions supported, and the computational resources required for simulation. Such a table would allow researchers to quickly assess the unique contributions and limitations of this benchmark in comparison to existing platforms.

### Questions
1. Does the framework offer a user-friendly interface that allows developers to modify parameters such as the reward function and the number of agents?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes HIVEX which is an environment suite to benchmark multi-agent research focusing on ecological challenges. The environments include Wind Farm Control, Wildfire Resource Management, Drone-Based Reforestation, Ocean Plastic Collection, and Aerial Wildfire Suppression. Although Drone-Based Reforestation is an interesting cooperative MARL task, the other environments do not seem to be related to MARL.

### Strengths
- The paper is generally easy to follow and interesting to read.
- Prior work hasn't extensively studies multi agent research on ecological challenges.
- Drone-Based Reforestation is an interesting cooperative MARL task. The agents need to pick up seeds and recharge at the drone station, explore fertile ground near existing trees, and drop seeds while ensuring sufficient battery charge to return to the station.

### Weaknesses
 - Wind Farm Control: In the Wind Farm Control environment, the agents' primary task is to adjust wind turbines to positions aligned against the wind direction to maximize energy generation, receiving rewards based on each turbine's performance. However, there is no mention of direct interactions or mutual influence among the multiple agents, nor is it clearly stated whether cooperation or competition exists between them. The absence of agent interaction beyond parameter sharing significantly limits the environment's relevance to multi-agent research. The description lacks details on how the agents' actions might affect each other's rewards or the overall system performance, which is crucial for a multi-agent setting.
- Wildfire Resource Management: Is "neighbouring watchtowers" referring to other agents? If so, why is there only 3 neighbors per agent? If not, then this environment is unrelated to MARL, as there is no competition or cooperation involved. The limited number of neighbors (3) seems arbitrary and lacks justification in the context of a multi-agent system. Furthermore, the lack of clarity on whether these neighbors are indeed agents or static entities undermines the environment's claim as a MARL benchmark. The interaction mechanism between these watchtowers, if they are agents, is not clearly defined, making it difficult to assess the environment's suitability for multi-agent learning.
- Ocean Plastic Collection: What is the advantage of implementing this environment in Unity. Is it merely to make the demonstration of the environment look more visually impressive. The use of Unity for this environment seems primarily focused on visual appeal, without a clear explanation of how this choice enhances the multi-agent learning aspect. The physics engine, while useful, does not inherently justify the choice of Unity over other simulation platforms if the core focus is on multi-agent interactions. The paper does not articulate how the specific features of Unity contribute to the complexity or relevance of the multi-agent problem.

### Questions
- From Figure 26 onwards, the epsilon parameter was set to 0.2 in all experimental tests. However, according to the standard procedure in the PPO algorithm, epsilon should generally be set to 0 during testing, as this phase is intended solely to evaluate the performance of the trained policy without any further updates. Setting epsilon to a non-zero value may introduce unnecessary policy perturbations, potentially biasing the test results. I recommend that the authors revisit this configuration and set epsilon to 0 in testing to ensure the accuracy and consistency of the experimental results.
- In Figure 144, the caption is too close to the figure, and other figures have similar problems.
- "Crossing the environment's boundary (a 1500x1500 square surrounding a 1200x1200 island) results in a negative reward of −100." However, in Table 6, from task 1 to task 9, the reward for crossing the border is 1, which does not match the description in this paper. For example, in task 8, if the agents' goal is to find fire, then the reward 'Crossed Border' should be set to 0.

### Soundness
2

### Presentation
3

### Contribution
2
