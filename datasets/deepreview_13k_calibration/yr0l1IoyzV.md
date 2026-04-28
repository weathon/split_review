# A GPU-accelerated Large-scale Simulator for Transportation System Optimization Benchmarking

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
With the development of artificial intelligence techniques, transportation system optimization is evolving from traditional methods relying on expert experience to simulation and learning-based decision and optimization methods.
Learning-based optimization methods require extensive interactions with highly realistic microscopic traffic simulators.
However, existing microscopic traffic simulators are inefficient in large-scale scenarios and thus fail to support the adoption of these methods in large-scale transportation system optimization scenarios.
In addition, the optimization scenarios supported by existing simulators are limited, mainly focusing on the traffic signal control.
To address these challenges, we propose the first open-source GPU-accelerated large-scale microscopic simulator for transportation system simulation and optimization.
The simulator can iterate at 84.09Hz, which achieves 88.92 times computational acceleration in the large-scale scenario with 2,464,950 vehicles compared to the best baseline CityFlow.
Besides, it achieves a more realistic average road speeds simulated on real datasets by adopting the IDM model as the car-following model and the randomized MOBIL model as the lane-changing model.
Based on it, we implement a set of microscopic and macroscopic controllable objects and metrics provided by Python API to support typical transportation system optimization scenarios including traffic signal control, dynamic lane assignment within junctions, tidal lane control, congestion pricing, road planning, e.t.c.
We choose five representative transportation system optimization scenarios and benchmark classical rule-based algorithms, reinforcement learning algorithms, and black-box optimization algorithms in four cities.
These experiments effectively demonstrate the usability of the simulator for large-scale traffic system optimization.
In addition, we build an open-registration web platform available at \url{https://moss.fiblab.net} to support no-code trials.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a fast simulator for transportation system optimization.
The main contributions of this paper is a high-performance traffic flow simulation environment and the implementation of 5 transportation optimization problems. The new proposed simulation environment is GPU-accelerated and based on SIMD and programmed in CUDA. The performance of the proposed simulator is compared against some of the existing ones and has demonstrated superior performance on runtime. Different benchmark algorithms are demonstrated on the new simulator.

### Strengths
This work is a wonderful contribution for transportation system optimization, and I strongly believe many researchers can take advantage of this platform. The manuscript is very well structured and written well. The authors covers a comprehensive review of the existing simulations.

### Weaknesses
The scope of this work is too narrow, since there will only be a small subset of researchers that will use this in the learning community. 

It will be nice to include an analysis of memory usage if possible.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors present a high-performance simulator for traffic system simulation and optimization, as well as the benchmark resulting for five scenarios with the simulator. The author clearly stresses the weakness of trending traffic system simulators and show through comparison that their proposed simulator can overcome the issues and outperform the SOTA one by running frequency and simulation realism. Overall, the presentation of the work is also clear and comprehensive, and tis work is good in its realm that from the comparison it does show the superiority in many aspects compared with existing simulators in the literature.

### Strengths
1.The proposed simulator is more efficient, realistic and capable compared to other candidates (sumo, cityflow, etc.). The proposed simulator is shown to be much faster than

2. The work has practical and application value, it can facilitate research and application in the relevant areas of traffic & transportation system. It is more versatile such that more component (traffic objects) are enabled in the simulator to be controllable. The authors also provide a few predefined evaluation metric APIs in the simulator to facilitate usage.

### Weaknesses
In Section 3, the authors described the design of each component of the simulator, however, it is not clear, which component is the main contribution of the design that improves the efficiency and performance of the traffic simulator. I would suggest the authors add a brief summary paragraph at the end of Section 3 that clearly states which specific components or techniques are the main technical contributions. It would be beneficial to explicitly identify the novel aspects of the simulator's architecture, such as whether the efficiency gains stem primarily from the two-phase parallel process, the linked-list based vehicle sensing indexes, or a combination of both. A more detailed explanation of how these components interact to achieve the reported performance would also strengthen the paper. For example, quantifying the performance impact of each component individually, if possible, would help the reader understand the core contributions.

### Questions
Please see the limitation and clarify the technical contribution of the paper better. Some additional questions include:
1.Does the simulator allow the researcher to add uncertainty to the vehicle model or the control of traffic objects in order to validate the robustness of a method, and allow researchers to compare algorithms that reflect the simulation to reality gap? The authors please answer the following questions to clarify this point: 1) Describe any existing functionality for adding uncertainty/stochasticity, or 2) Discuss whether and how you plan to add such capabilities in future versions if not currently supported.


2. Will it be easy (or possible) to make the car-following model selectable (instead of sticking to IDM)? We suggest the authors to briefly discuss the modularity of the vehicle behavior models and what would be involved in adding support for multiple selectable car-following models. The answer should help clarify how flexible the simulator architecture is for future extensions.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper presents a GPU-accelerated large-scale microscopic traffic simulator aimed at supporting optimization tasks within transportation systems. By leveraging GPU-based parallel computation, the simulator achieves high performance, simulating up to millions of vehicles at a significantly accelerated rate compared to traditional CPU-based simulators like CityFlow and CBLab. The simulator supports various transportation optimization scenarios, including traffic signal control, lane assignment, tidal lane control, congestion pricing, and road planning. The authors provide benchmark results across multiple cities to demonstrate the applicability and robustness of the simulator for different optimization algorithms.

### Strengths
## Originality
- The simulator is GPU-accelerated, which is helpful for traffic system simulation (while some GPU simulators are available for autonomous driving).

## Quality
- The paper provides benchmarks on various transportation optimization tasks, demonstrating practical applicability.

## Clarity
- The paper is well-organized and presents a clear problem statement, followed by the design choices and technical solutions implemented. 

## Significance
- By supporting large-scale simulations at high speed, this simulator could enable faster and more frequent experimentation with AI-based optimization methods, including reinforcement learning.

### Weaknesses
 - The paper lacks a comprehensive discussion of some relevant prior works. For example, recent works such as GPUDrive by Kazemkhani et al. (2024) and CityFlowER by Da et al. (2024) could provide essential insights and serve as useful points of comparison for evaluating the novelty and realism of the proposed simulator. For example, [1,3,4] are also a GPU simulators, are the techniques used for GPU acceleration in their papers the same as this paper? Is CityFlowER also as realistic as the proposed simulator?

[1] Kazemkhani, Saman, et al. "GPUDrive: Data-driven, multi-agent driving simulation at 1 million FPS." arXiv preprint arXiv:2408.01584 (2024). 

[2] Da, Longchao, et al. "CityFlowER: An Efficient and Realistic Traffic Simulator with Embedded Machine Learning Models." Joint European Conference on Machine Learning and Knowledge Discovery in Databases. Cham: Springer Nature Switzerland, 2024.

[3] Saprykin, Aleksandr, Ndaona Chokani, and Reza S. Abhari. "GEMSim: A GPU-accelerated multi-modal mobility simulator for large-scale scenarios." Simulation Modelling Practice and Theory 94 (2019): 199-214.

[4] Jiang, Xuan, et al. "Large scale multi-GPU based parallel traffic simulation for accelerated traffic assignment and propagation." Transportation Research Part C: Emerging Technologies 169 (2024): 104873.

- The authors claim that individual vehicle simulation is compatible with the SIMD model, arguing that the vehicles are homogeneous and can be simulated in parallel. However, this assertion could be problematic as vehicle interactions, particularly in congestion, often exhibit dependencies on nearby vehicles. The paper would benefit from a clearer explanation of how dependencies are managed in parallel to ensure realism without sacrificing computational performance. The paper does not provide citations or a detailed discussion distinguishing the proposed SIMD implementation from existing techniques. This omission raises questions about whether this technique is novel or merely an application of existing methods.

- In the Simulator Realism experiment, the paper mentions that the simulator achieves more realistic speeds compared to CityFlow. Given that CityFlowER now incorporates more realistic driving models, it would be valuable to benchmark the proposed simulator against it to provide a more comprehensive evaluation.

- When demonstrating scalability at large vehicle counts, the reported performance of CBLab appears to contradict with its original paper when simulating scenarios with over 1,000 vehicles, with CityFlow performing comparably or even outperforming in such instances. This discrepancy between claims and results needs further explanation on why CBLab is generally worse than CityFlow - is this because of your data is different from the CBLab? Can you provide more details about their experimental setup, including the specific datasets used and any differences from the original CBLab experiments? If so, can you use the similar dataset used in CBLab?  It would also be helpful to request a detailed comparison of their experimental setup with that of the original CBLab paper, including specifics on hardware configurations and simulation parameters.

-  The absence of scenario data within the provided code limits the reproducibility of results, particularly for scenarios such as traffic signal optimization and congestion pricing. Including this data would enhance transparency and reproducibility.

### Questions
1. Could the authors provide more justification for the assertion that vehicle simulations are “highly homogeneous” and compatible with the SIMD computational model? Specifically, how are dependencies between vehicles managed in congested scenarios?

2. Why does the simulator's performance appear to decline with scenarios of over 1,000 vehicles, as seen in the comparison with CityFlow? How does this relate to the scalability claims made in the paper?

3. Are there plans to include more detailed explanations of the simulation scenarios and the metrics used to evaluate them? This information would aid in validating the results for scenarios like congestion pricing and dynamic lane assignment.

4. Could the authors comment on the possibility of incorporating advanced driving models such as those used in CityFlowER, which have been shown to improve the realism of driving behavior?

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
4

### Summary
This paper proposes a microscopic simulator for large-scale urban traffic systems utilizing GPU acceleration. To overcome the computational limitations of existing simulators, the authors introduce GPU-based parallel processing, a two-phase parallel process, and a linked-list-based vehicle detection index. Through experiments simulating over 2.4 million vehicles, the proposed system achieved an approximately 88.92x performance improvement compared to existing systems. Furthermore, the authors present a framework that aims to integratively support five major traffic optimization scenarios: Traffic Signal Control, Dynamic Lane Assignment, Tidal Lane Control, Congestion Pricing, and Road Planning.

- Soundness (Score: 2 - Fair): The design and performance improvement of the GPU-accelerated simulator proposed in this research are technically convincing, and the experimental methodology is systematic. However, the simplifications, such as excluding intersection interactions and various traffic participants (e.g., pedestrians, bicycles, public transport), may significantly affect the realism of the simulation, and these aspects were not clearly validated. It is unclear whether prior research justified these exclusions. Although extensive benchmarking experiments were conducted, the lack of detailed analysis and interpretation of the results leaves the motivations behind the scenarios insufficiently explained.


- Presentation (Score: 3 - Good): The overall structure and explanations in the paper are clearly presented, particularly regarding system design and the use of GPU acceleration. However, the validation of each scenario within the same system is not clearly articulated. Additionally, it would be beneficial to provide a clear comparison of the proposed system architecture with existing studies, explaining the structural advancements and reasons for adopting this specific architecture.


- Contribution (Score: 2 - Fair): The proposed performance improvements through GPU acceleration and the integrated traffic simulator framework are meaningful contributions to the field. However, the lack of individual effectiveness analysis for the five scenarios and insufficient validation of the simulator's realism are notable shortcomings. The experiments with real-world data are limited, which poses a constraint on the practical contribution aspect.

### Strengths
Originality: The parallel design utilizing GPU features and the introduction of a linked-list-based vehicle detection index are promising approaches to overcoming the computational limitations of existing CPU-based traffic simulators.

Quality: The paper demonstrates a significant technical achievement by simulating over 2.4 million vehicles with GPU acceleration, achieving substantial performance improvement compared to CPU implementations. The system design and GPU usage are well-documented.

Clarity: The explanation of the system architecture is systematic.

Significance: To address urban traffic optimization, the authors propose an integrated simulation for five scenarios that were previously dealt with individually.

### Weaknesses
Scenario Validation and Motivation: It would be helpful to explain how the results from the five proposed scenarios provide insights for actual urban traffic planning or policy decisions. If empirical validation showing that similar results can be derived from simulating real-world policy changes were included, it would strengthen the motivation for policymakers to use the simulator. As a policymaker, I would want to validate planned changes beforehand with such a simulator, but the current motivation seems insufficient compared to the well-executed system implementation.

Lack of Realism: The simplifications, such as excluding intersection overlap, pedestrians, bicycles, and public transport, lack a clear basis for their effect on simulation outcomes. An analysis of the impact of these exclusions is necessary, including evidence from prior research or justifications for why their impact is minimal.

Insufficient Long-Term Scenario Evaluation: There is a lack of experiments evaluating how the proposed simulator functions under long-term urban traffic pattern changes. For example, reproducing outcomes of real-world urban policy changes using the simulator would help demonstrate its reliability.

Code Reproducibility Issues: Although the code was provided, the step-by-step explanations in the README.md were insufficient for successful reproduction. Specifically, two of the three provided source codes only included installation instructions without guidance on how to build or run scenarios. For the benchmark source code, even after locating it through references due to a missing GitHub link, the target version was not specified, preventing access to the necessary dataset for simulation. More detailed code instructions and thorough guidance on code operation are required, highlighting the lack of user-friendly considerations.

### Questions
Q1. Given the numerous experimental results presented, I felt that there was a lack of motivation for their inclusion. Could you provide additional explanations regarding the analysis and significance of these results?

Q2. There seem to be similar commercial services available (e.g., Aimsun). How does this work differentiate itself? There are also simulation games related to urban simulation, such as Cities: Skylines, which are known for their well-designed public transport systems, and the recent sequel has drawn significant attention. What are the commonalities and differences compared to such games? They support user-customized plugins for logging and debugging.

Q3. Could you explain the technical background that led to the design of the simulator's GPU-accelerated architecture, and how this design evolved from previous research efforts in the field?

Q4. Since the target is a simulator that is intended to be used alongside AI/ML-based technologies, which also use GPUs, resource constraints are expected if both the simulator and AI/ML technologies are to be used on servers that are not high-performance. Did you encounter this issue, and do you think it would be a significant problem?

** Additional Comments

There are inaccuracies in references.

- Unable to verify the original document. Only the citation is found. Please verify or update: HS Mahmassani. Dynamic traffic assignment and simulation for advanced network informatics (dynasmart). In the 2nd International Seminar on Urban Traffic Networks, 1992.

- The cited arXiv document version has been updated. Please verify or update: Alexander I Cowen-Rivers, Wenlong Lyu, Zhi Wang, Rasul Tutunov, Hao Jianye, Jun Wang, and Haitham Bou Ammar. Hebo: Heteroscedastic evolutionary bayesian optimisation. arXiv preprint arXiv:2012.03826, pp. 7, 2020.

- Duplicate reference entry. Please correct:
Qiang Wu, Ming Li, Jun Shen, Linyuan Lü, Bo Du, and Kecheng Zhang. Transformerlight: A novel sequence modeling based traffic signaling mechanism via gated transformer. Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, 2023a. URL: https://api.semanticscholar.org/CorpusID:260499801.
Qiang Wu, Mingyuan Li, Jun Shen, Linyuan Lü, Bo Du, and Ke Zhang. Transformerlight: A novel sequence modeling based traffic signaling mechanism via gated transformer. In Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, pp. 2639–2647, 2023b.

### Soundness
2

### Presentation
3

### Contribution
2
