# Learning system dynamics without forgetting

- Decision: Accept
- Scores: 5, 6, 6, 8

## Abstract
Predicting the trajectories of systems with unknown dynamics (\textit{i.e.} the governing rules) is crucial in various research fields, including physics and biology. This challenge has gathered significant attention from diverse communities. Most existing works focus on learning fixed system dynamics within one single system. However, real-world applications often involve multiple systems with different types of dynamics or evolving systems with non-stationary dynamics (dynamics shifts). When data from those systems are continuously collected and sequentially fed to machine learning models for training, these models tend to be biased toward the most recently learned dynamics, leading to catastrophic forgetting of previously observed/learned system dynamics. To this end, we aim to learn system dynamics via continual learning. Specifically, we present a novel framework of Mode-switching Graph ODE (MS-GODE), which can continually learn varying dynamics and encode the system-specific dynamics into binary masks over the model parameters. During the inference stage, the model can select the most confident mask based on the observational data to identify the system and predict future trajectories accordingly. Empirically, we systematically investigate the task configurations and compare the proposed MS-GODE with state-of-the-art techniques. More importantly, we construct a novel benchmark of biological dynamic systems, featuring diverse systems with disparate dynamics and significantly enriching the research field of machine learning for dynamic systems. %Our code and benchmark datasets are available via \url{https://anonymous.4open.science/r/MS-GODE-BEB7/} and are introduced in Appendix \ref{sec:vcell systems}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposed a continual learning framework based on GraphODE over dynamical systems. The key motivation is to address the catastrophic forgetting problem if multiple systems of different configurations are within a sequence. The proposed Mode-switching Graph ODE (MS-GODE) is able to select the best sub-network mask for a given observation sequence, following the parameter-isolation category in continual learning. A new dataset on biological cellular systems is created in the experiment.

### Strengths
1. The paper studies an interesting problem in dynamical system modeling under distribution shifts. Though I feel the motivation example can be changed to more realistic one (see below). 

2. The paper proposes a useful benchmark for evaluating the distribution shifts in dynamical system modeling, on biological cellular systems.

3. The proposed method is able to achieve good performance over selected baselines.

### Weaknesses
1. While I in general get the motivation of this paper, I feel the examples used in the introduction section need to be further improved. First for Figure 1, there are so many contents/fonts in the figure that are not well-explained in the caption or the main text. It is suggested to use for example legend to denote different kinetic factors, using some boxes to denote the overall system consists of multiple objects. Here for me, it is hard to read from this figure along with its current explanations. For the second example, I feel it is not very natural to combine spring systems and charged particle systems, as there is no reasonable transition among them. A more proper example may be that some water particles will froze into solid when the temperature decreases, and the interaction among liquid and solid particles can be very different. I encourage the authors to further improve the motivation example so the audience from various backgrounds can understand them easily.

2. For the baselines, the authors chose different continual learning framework as comparison. However for learning over multiple systems, there are some work [1,2] that directly learn a generalized neural simulators. It is suggested to also discuss their performance and show if continual learning is the better way to learning over different systems.

3. For majority of the citation, it should be \citep (reference with a brackets) instead of \cite. For example, line 40-50.

4. For the experiment table 1, what does the results fine-tune and joint mean respectively? In line 400-402 the authors mention that for each baseline there are two options, so I overall do not get the meaning of the two rows in Table 1,which model are they based on ?

### Questions
1. For the experiment table 1, what does the results fine-tune and joint mean respectively? In line 400-402 the authors mention that for each baseline there are two options, so I overall do not get the meaning of the two rows in Table 1,which model are they based on ?

### Soundness
3

### Presentation
3

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
The main motivation of this paper is that, system dynamics are not static, rather subject to change over time in practice. Accordingly, the authors developed a mode-switching graph ODE (MS-GODE) to continually learn evolving system dynamics. Unlike most of the existing works on dynamics modeling, which have been focused on a single dynamics, MS-GODE can process multiple system dynamics by automatically switching binary masks on shared model weights (i.e., different weights for different system dynamics). Also, the authors introduces bio-CDL, a novel dynamic system benchmark to evaluate the proposed methods in addition to physics-based particle systems.

### Strengths
- Continual learning setup on interacting system dynamics is a novel problem. Since very recent works have explored evolving system dynamics, continual learning can provide a new insight on the related research community.

- As the authors mentioned in L131, neural ODE has been focused on a single dynamical systems. Combination of neural ODE with masked networks is a new approach. 

- The paper introduces a novel benchmark using biological cellular systems. Considering many benchmarks on interacting dynamical systems are based on physical systems (e.g., springs, charges), the new benchmark could provide another insight whether models still perform well when predicting dynamic states, not locations of particles.

- The details about the experimental settings and background are well presented.

### Weaknesses
 - While I still consider the combination of neural ODE with continual learning interesting, technical novelties seem somewhat limited. For example, both the network design (e.g., LG-ODE, NRI) and learning method (e.g., masked-based CL, edge-popup algorithm) are already well known. I think, unique technical contributions this paper had made should have been clearly presented.

- Also, the motivation of CDL needs to be better clarified. I don’t think continual learning is always required for all evolving dynamical systems. For example, what if a system never repeats the past dynamics once it evolves? what if the prediction model can quickly enough adapt to new dynamics? We don’t need to make the models avoid catastrophic forgetting in these cases. In other words, unless the system dynamics repeat again and again, which might narrow the scope of target applications, mitigating catastrophic forgetting won't be useful.

- The results from Table 1 (performance of all methods is better in high-level dynamics shift) are interesting. The authors provide a brief discussion in L471-L475, but is there any experimental or theoretical evidence to believe this? For example, how do the authors believe that “e.g. Fine-tune, the results indicate that diverse systems may guide the model to exploit different parameters for different systems”? In other words, the discussion and detailed analysis on the performance is not enough while comparison with other methods in terms of AP and AF are well studied.

- There have been many recent works to address evolving system dynamics [1,2,3] though they are not continual learning-based works. Since this paper specifically address such systems, I think related works should have included them to further clarify the novelty in the problem setup.

- In equation (3), do the authors assume the spatial-temporal edges (or graph structures) are known?

- Can the authors specify if task boundaries should be known for training? As there are many different continual learning setups, it would be nice to specify it.

- There are some typos (e.g., L208: “to x) as a state” -> “to x as a state”, L965: “backpropagatioon” -> “backpropagation”)

- It would be better if a code implementation was provided in the review stage.

### Questions
provided with weakness

### Soundness
2

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
4

### Summary
This paper tackles a significant gap in dynamics learning by introducing Continual Dynamics Learning (CDL), addressing systems whose dynamics evolve over time. The core contribution, Mode-switching Graph ODE (MS-GODE), combines sub-network learning with mode-switching to handle varying dynamics while preventing catastrophic forgetting. Their approach marks the first systematic treatment of this problem, supported by extensive empirical validation.

### Strengths
The paper's primary innovation lies in recognizing and formalizing the CDL problem, which has been overlooked despite its practical importance. The MS-GODE architecture effectively combines proven techniques (Graph ODEs, sub-network learning) with a novel mode-switching mechanism, demonstrating strong performance across different system configurations. The introduction of Bio-CDL, a benchmark featuring biological cellular systems, significantly enriches the field beyond traditional physics simulations.

### Weaknesses
 - Several important baselines are notably absent from the comparison, including CG-ODE, GG-ODE, PG-ODE, and HOPE.

- The experimental validation would be more convincing if it included tests on human motion and molecular dynamics (MD17) datasets, which could reveal how the approach handles different types of dynamic patterns. The model shows sensitivity to hyperparameters, particularly dropout rates and mask selection strategies, but lacks clear guidelines for parameter selection in practical applications.

- The paper also needs stronger theoretical foundations - while the empirical results are promising, there's no formal analysis of why mode-switching works better than traditional continual learning approaches.

### Questions
Contrary to the author's claim, there have been pretrained models for dynamical systems lately. Can they be leveraged to improve MS-GODE's performance, especially in sub-network learning?

Seifner, Patrick, et al. "Foundational inference models for dynamical systems." arXiv preprint arXiv:2402.07594 (2024).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces Mode-switching Graph Ordinary Differential Equations (MS-GODE), a model designed to address Continual Dynamics Learning (CDL) for predicting time-dependent systems with evolving dynamics. Traditional approaches struggle with continual learning when dynamics vary, leading to issues like catastrophic forgetting, where previous dynamics are “forgotten” once new patterns are introduced. In this work, MS-GODE incorporates sub-network learning with mode-switching capabilities to prevent forgetting, allowing the model to dynamically adapt to different systems without overwriting learned dynamics. Additionally, the paper presents Bio-CDL, a benchmark dataset focusing on biological systems with varied dynamics, to further assess CDL models.

### Strengths
- The methodological foundation of MS-GODE is robust, integrating sub-network learning and mode-switching mechanisms to handle evolving system dynamics. The model architecture is well-constructed, and the choice to use fixed backbone weights with adaptive binary masks for each dynamic mode is theoretically sound and practically effective.
- Besides, The paper is generally well-organized, with clear problem framing and concise descriptions of the core components of MS-GODE.

### Weaknesses
 - The model’s reliance on multiple components—such as sub-networks, binary masks, and a mode-switching module—adds to its complexity. While effective, this multi-faceted design may limit accessibility, especially for researchers less familiar with CDL or advanced dynamic modeling techniques. The interaction between these components, particularly how the mode-switching module dynamically selects the appropriate mask, could be more clearly explained with illustrative examples. Specifically, the criteria for switching and the impact of incorrect mask selection on prediction accuracy should be further elaborated.
- Although the Bio-CDL benchmark dataset represents a practical biological context, additional real-world datasets across broader domains (e.g., climate science, economics) could have bolstered the model’s credibility and practical relevance. The biological focus, while useful, limits insights into how the model would handle other types of complex, evolving systems. The current experiments do not fully explore the model's capacity to generalize across diverse dynamical systems beyond the specific biological and physics systems presented. The lack of datasets with varying levels of noise and complexity also limits the assessment of the model's robustness.
- The MS-GODE model’s performance is sensitive to the initialization of binary masks and dropout rates, as shown in the experiments. The sensitivity to these hyperparameters, particularly the mask initialization strategy, raises concerns about the model's reliability and ease of use. The paper should include a more in-depth analysis of how different initialization techniques affect the learning process and the final performance. Furthermore, the optimal dropout rate of zero, while empirically effective, lacks theoretical justification and should be further explored.
- The content in the main body about the benchmark introduced in this work is too short. As it is claimed to be a main contribution of this work, it would be better to describe more on the benchmark. The description should include details about the data generation process, the types of biological systems included, and the specific challenges it poses for CDL models. A more detailed analysis of the benchmark's properties, such as the distribution of dynamics and the complexity of the interactions, would also be beneficial.

### Questions
1. How robust is the model to variations in initial mask configurations? Would pre-training the masks on related dynamics (e.g., similar system behaviors) improve or stabilize performance?
2. With multiple modes and sub-networks, how does the model handle scaling to larger or more complex networks (e.g., with thousands of nodes)? Would the approach require significant modification for larger systems, or is it inherently scalable?
3. The paper notes that abrupt dynamics shifts yield better performance than gradual shifts. Could the authors clarify whether any architectural modifications could improve MS-GODE’s performance under gradual shifts, which are common in many real-world applications?
4. What if some interactions require longer time to have an effect? Will the method still work?
5. What if the switching of the dynamics is not observed in the trajectories? Will the performance of the proposed method drop?
6. Minor: Please check the citation form in the paper, especially in introduction. They are not properly cited and break the sentences.

### Soundness
3

### Presentation
3

### Contribution
3
