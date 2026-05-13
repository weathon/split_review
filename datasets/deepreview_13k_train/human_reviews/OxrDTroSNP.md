# GenNet: A Generative AI-Driven Mobile Network Simulator for Multi-Objective Network Optimization

- Decision: Reject
- Scores: 5, 3, 3, 6

## Abstract
Simulation-based optimization has emerged as a crucial methodology in the field of mobile network optimization, addressing the need for dynamic and predictive network management. To address the scarcity of open-source mobile network simulators for advanced research, we developed GenNet—a generative AI-driven mobile network simulator. GenNet can create virtual replicas of mobile users, base stations, and wireless environments, utilizing generative AI methods to simulate the behaviors of these entities under various network settings with high accuracy. GenNet features a tailor-made API explicitly designed for reinforcement learning environments, enabling researchers to finely adjust network parameters such as tilts, azimuth, and transmitting power. Extensive experiments have employed GenNet to benchmark multi-objective optimization algorithms, focusing on enhancing network coverage, throughput, and energy efficiency, validating its effectiveness as a robust platform for advancing network optimization techniques. Through this innovative tool, we aim to empower researchers and practitioners to identify and implement the most effective approaches for network optimization, paving the way for future advancements in mobile network management.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors developed GenNet—a generative AI-driven mobile network simulator to replicate mobile users, basestations, and wireless environments. GenNet features a tailor-made API explicitly designed for reinforcement learning environments, enabling researchers to finely adjust network parameters such as tilts, azimuth, and transmitting power. The simulator is then used to understand the performance gains of multi-objective optimization algorithms.

### Strengths
The authors proposed a generative AI based network planning and optimization tool. The tool appears to have various features as mentioned in Table-1 of the paper and a comparison is presented  with various state-of-the-art research works.

### Weaknesses
My main concerns are as follows:
1. Literature review is not comprehensive, especially related to multi-objective optimization in cellular networks, such as 
[a] Multi-objective energy efficient resource allocation and user association for in-band full duplex small-cells
[b] Multi-objective optimization for spectrum and energy efficiency tradeoff in IRS-assisted CRNs with NOMA
[c] Generalized Multi-Objective Reinforcement Learning with Envelope Updates in URLLC-enabled Vehicular Networks
Therefore, it is not clear why multi-objective reinforcement learning techniques are beneficial compared to multi-objective optimziation techniques and how envelope outperforms other RL solutions. The authors should include a brief comparison of multi-objective optimization techniques versus multi-objective reinforcement learning approaches in the context of cellular networks. Additionally, a discussion on how Envelope compares to other RL solutions should be included.
2. The presented results are not comprehensive and it is hard to gain any insights in terms of the computation or time complexity or dimension of the Generative AI based proposed simulator. The runtime comparisons between GenNet and traditional simulators can be included, and the authors should elaborate how the simulator's performance scales with network size.
3. The considered optimization problem is rather simple as it has no non-convex quality of service rate constraints
4. the reliability of the ray tracing results and how well they match with the platforms reported in Table-1. Quantitative comparisons between their ray tracing results and those from established platforms should be included
5. Constraint violation probability should be included in the results.
6. MORL algorithms can be easily implemented using OpenAIGym, is there an interface available for OpenAI Gym. Discuss the advantages of their custom API compared to using OpenAI Gym, and explain if there are plans to provide compatibility with OpenAI Gym in future versions of GenNet.

### Questions
My main concerns are as follows:
1. Literature review is not comprehensive, especially related to multi-objective optimization in cellular networks, such as 
[a] Multi-objective energy efficient resource allocation and user association for in-band full duplex small-cells
[b] Multi-objective optimization for spectrum and energy efficiency tradeoff in IRS-assisted CRNs with NOMA
[c] Generalized Multi-Objective Reinforcement Learning with Envelope Updates in URLLC-enabled Vehicular Networks
Therefore, it is not clear why multi-objective reinforcement learning techniques are beneficial compared to multi-objective optimziation techniques and how envelope outperforms other RL solutions. The authors should include a brief comparison of multi-objective optimization techniques versus multi-objective reinforcement learning approaches in the context of cellular networks. Additionally, a discussion on how Envelope compares to other RL solutions should be included.
2. The presented results are not comprehensive and it is hard to gain any insights in terms of the computation or time complexity or dimension of the Generative AI based proposed simulator. The runtime comparisons between GenNet and traditional simulators can be included, and the authors should elaborate how the simulator's performance scales with network size.
3. The considered optimization problem is rather simple as it has no non-convex quality of service rate constraints
4. the reliability of the ray tracing results and how well they match with the platforms reported in Table-1. Quantitative comparisons between their ray tracing results and those from established platforms should be included
5. Constraint violation probability should be included in the results.
6. MORL algorithms can be easily implemented using OpenAIGym, is there an interface available for OpenAI Gym. Discuss the advantages of their custom API compared to using OpenAI Gym, and explain if there are plans to provide compatibility with OpenAI Gym in future versions of GenNet.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The goal of this paper is to develop a network simulation for wireless mobile systems. The simulator is based on generative AI techniques (like GANs and auto-encoders), and it focuses on problems of reinforcement learning in wireless systems. The authors discuss the simulator and benchmark its performance (including simulation time) against state-of-the-art.

### Strengths
+ The wireless community has a need for realistic simulators.
+ The open source nature of this simulator can help in adoption across the community.
+ The simulator seems to perform well in terms of execution time.

### Weaknesses
- This work does not contribute much to the field of machine learning. It uses off-the-shelf techniques to simulate a wireless system and does not really advance any of the tools used (e.g., auto-encoders, reinforcement learning, etc.). It is perhaps more appropriate for wireless conferences like SIGCOMM or GLOBECOM where the core contribution can lie in wireless and not in AI/ML.
- The authors do not provide technical justification on the choice of the various collection of machine learning techniques that they used. It seems that those choices are arbitrary and not based on technical reasons or arguments stemming from the wireless physics or the simulator.
- Reinforcement learning has not yet made it into real-world wireless systems, hence, it is questionable on whether the focus on this approach will allow the simulator to be used in real-world systems. For instance, you focus only on reinforcement learning, but that has not yet been adopted in standards like 3GPP or others. Current wireless networks use heuristics for optimization and may use ML techniques like auto-encoders for transceiver design. RL, while meaningful, cannot be the only approach used for performing evaluation of wireless networks.
- The modeling of the base stations and wireless links is very simplified and may not follow the real-world physics of wireless propagation environments.
- The utility function in (1) is arbitrary and based on very heuristic weighting. Using scalarization in multi-objective optimization is not very effective, and the authors must justify this choice. Moreover, the various terms used in this utility are not realistic wireless metrics, and they seem oversimplified.

### Questions
- How can you justify that the optimization problem in (1) can indeed work for real-world systems like 5G or 6G? How can you handle the realistic propagation environment characteristics like interference?
- Can you explain what are the contributions of this work to the field of AI or machine learning?
- The results in the experiments do not show a smooth behavior, can you explain why?
- How many mobile users and base stations can your simulator support? 
- Can you comment on scalability?

### Soundness
3

### Presentation
2

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
This paper develops a network simulator for multi-objective optimization using generative AI and establishes a reinforcement learning interface. Based on a grey-box approach, the paper constructs modules for user mobility, wireless environment, and models base stations and network performance. The authors employ various generative algorithms to simulate user movement, service traffic, and wireless propagation models. Based on this simulator, the authors conducted reinforcement learning experiments to optimize base station coverage, throughput, and energy efficiency.

### Strengths
The authors propose the use of generative AI to construct modules in communication network simulators, which is a good design idea for simplifying network simulators.

### Weaknesses
The simulator developed by the author claims to be fast. In reality, since the simulator is only used for specific functions such as traffic, coverage, and energy optimization, it cannot control other functions of wireless networks and cannot observe other performance metrics of wireless networks, such as slice control, congestion control, quality of service assurance, deterministic guarantees, etc. When these functions are added, the software scale and simulation speed will also increase. Moreover, due to the black-box nature of generative AI, the coexistence of AI modules with different functions is questionable. That is to say, the scalability of the system is questionable.
By searching the paper title on GitHub, the paper’s code information has been retrieved. This seems to violate the double-blind peer review agreement. By analyzing the code, it can be concluded that the work is aimed at a specific reinforcement learning algorithm, and the simulation work uses generative AI to simulate some functions.

### Questions
1. Due to the use of generative AI technology, the fidelity of its capabilities compared to traditional system-level simulation tools is questionable. Please explain the accuracy of the generated information.
2. The simulation experiment uses GPU and generative AI to simulate system functions, compared to traditional simulation software that uses CPU. It's unfair. In fact, there is also a large amount of work using GPU to accelerate simulation experiments. If GPU acceleration is used in both cases, what conclusion would the author draw about the performance comparison?
3. Could the authors explain how many control parameters, performance metrics, and functions need to be retained in a comprehensive simulator, such as NS-3, OPNET, OMNET++, to be generally applicable to most simulation experiments? What is the framework for the full implementation of the simulator proposed by the author, and how is its scalability ensured?
4. Please clarify the statement about MATLAB in the INTRODUCTION Section. The author mentioned in the related work that MATLAB is a link-level simulator. As we know, MATLAB provides a scientific computing tool. Based on this tool, link-level simulators and system-level simulators can be developed. For example, the well-known Vienna Platform can implement the protocol stack for LTE and 5G systems and complete system-level simulations.
5. The author claims in the introduction that the simulation speed of NS-3/OPNET/MATLAB/OMNET++ is slower than real networks. Please provide evidence or citations supporting their claim about simulation speeds.In my opion, discrete event-driven simulators do not require waiting for physical time to elapse and are faster than validating real networks.
6. In section 2.1, the author claims that OPNET/NS-3 lacks user mobility modeling and is not suitable for mobile access networks. In fact, these simulators have interfaces or are open-source, allowing for the development of mobility models and are widely used in mobility experiments. Many research works on mobility based on these simulators can be found through Google Scholar. Please clarify your statement.
7. Please provide the system architecture about your proposed scable, full functional system-level simulator.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper develops GenNet, a generative AI-driven mobile network simulator designed for mulit-objective network optimization with reinforcement learning. GenNet can create virtual replicas of mobile users, base stations, and wireless environments, utilizing generative AI methods to simulate the behaviors of these entities under various network settings with high accuracy. It utilizes generative AI methods to accurately simulate the behaviors of these entities under various network settings based on extensive real-world data, thereby surpassing traditional discrete-event-driven simulations.

### Strengths
1. This paper proposes the first open-source generative AI-driven mobile network simulator, which breaks away from traditional event-driven simulators and shows originality by leveraging data-driven generative AI to enhance realism and simulation efficiency.
2. GenNet’s compatibility with RL-based optimizations and multi-objective network tuning positions it as a potentially impactful solution for researchers and practitioners in mobile networking.
3. The paper is well-structured, with a clear logical flow that guides readers through the motivations, design, implementation, and evaluation of GenNet. The clarity in writing enhances the paper's readability.

### Weaknesses
1. Ideally, Table 1 should be one of the most critical tables in the paper, as it is intended to reveal the advantages of GenNet over other simulators. However, the table does not make GenNet’s superiority immediately apparent, aside from its support for realistic traffic. Furthermore, the paper itself acknowledges GenNet’s lack of a comprehensive protocol stack, which raises further questions about its value compared to existing simulators. Specifically, the absence of detailed protocol implementations (e.g., MAC layer contention, RLC segmentation, and retransmission) limits the simulator's ability to accurately model network behavior under various traffic loads and channel conditions. This omission is significant, as these protocols directly impact network performance metrics such as throughput, latency, and packet loss, which are crucial for evaluating optimization algorithms.
2. Although the simulation results are promising, the paper lacks an evaluation of GenNet’s performance in actual network environments or a discussion on the challenges and potential adjustments needed for deployment in real-world network conditions. The validation is limited to comparisons with other simulators, which may not fully capture the complexities of real-world deployments. For example, the simulator's ability to handle unpredictable interference patterns, hardware limitations, and dynamic channel variations, which are common in real-world networks, remains unclear. This lack of real-world validation limits the practical applicability of the simulator.
3. The simulators selected for comparison with GenNet, such as CityFlow and MATSim, are relatively dated, which may not fully reflect the current advancements in network simulation technology. To strengthen the evaluation, the authors are encouraged to include comparisons with more recent simulators. Specifically, simulators that incorporate more advanced channel models, support for emerging wireless technologies (e.g., mmWave, massive MIMO), and offer more detailed protocol implementations should be considered. This would provide a more robust and relevant benchmark for evaluating GenNet's performance and capabilities.

### Questions
1. It seems that the AI-driven simulator proposed primarily involves the straightforward application of generative models like GANs, VAEs, and diffusion models. Please provide specific details on any modifications or innovations they made to the generative models to adapt them for mobile network simulation. 
2. The introduction does not clearly outline any specific challenges in implementing this AI-driven simulator. With available datasets and pre-existing AI models, it is unclear what technical or conceptual work was required to make this solution viable. Please add a specific section in the introduction or methodology detailing the key technical challenges in developing GenNet and how you overcame them.
3. In Table 2, the primary advantage of GenNet appears to be reduced computation time. However, given that this is a simulation platform for validating optimization algorithms, it is unclear whether computation time is a critical factor. Please provide specific examples or use cases where reduced computation time in network simulations leads to tangible benefits in research or industry applications. This would help justify the importance of GenNet's speed improvements.
4. For the experimental results in Figures 7, 8, and 9, how should these be interpreted? What are the evaluation criteria for each metric, and how do these criteria indicate that MAPPO PG is optimal?  Please add detailed explanations of each metric directly in the figure captions or in an accompanying text box. Additionally, please provide a clear interpretation guide for these figures in the main text, explaining how to read the graphs and what conclusions can be drawn from them.
5. Which specific datasets were used for training GenNet? Could this choice potentially limit the system’s generalizability or make it overly dependent on particular datasets? Please provide a detailed description of the datasets used, including their size, diversity, and any potential biases. Additionally, please discuss how you addressed or mitigated potential overfitting to these specific datasets, and what steps you took to ensure GenNet's applicability to a wide range of network scenarios.

### Soundness
2

### Presentation
3

### Contribution
3
