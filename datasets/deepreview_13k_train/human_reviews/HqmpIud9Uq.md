# Tackling Non-Stationarity in Reinforcement Learning via Causal-Origin Representation

- Decision: Reject
- Scores: 3, 8, 3, 3, 3

## Abstract
In real-world scenarios, the application of reinforcement learning is significantly challenged by complex non-stationarity. Most existing methods attempt to model changes in the environment explicitly, often requiring impractical prior knowledge of environments. In this paper, we propose a new perspective, positing that non-stationarity can propagate and accumulate through complex causal relationships during state transitions, thereby compounding its sophistication and affecting policy learning. We believe that this challenge can be more effectively addressed by implicitly tracing the causal origin of non-stationarity. To this end, we introduce the \textbf{C}ausal-\textbf{O}rigin \textbf{REP}resentation (\textbf{COREP}) algorithm. COREP primarily employs a guided updating mechanism to learn a stable graph representation for the state, termed as causal-origin representation. By leveraging this representation, the learned policy exhibits impressive resilience to non-stationarity. We supplement our approach with a theoretical analysis grounded in the causal interpretation for non-stationary reinforcement learning, advocating for the validity of the causal-origin representation. Experimental results further demonstrate the superior performance of COREP over existing methods in tackling non-stationarity problems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses non-stationarity in reinforcement learning, highlighting its amplification through causal relationships during state transitions. Instead of directly modeling environmental changes, the authors introduce the Causal-Origin REPresentation (COREP) algorithm. COREP uses a guided updating mechanism to create a stable state representation, making policies more resilient to non-stationarity. Experimental results support COREP's effectiveness over existing methods.

### Strengths
1. The paper considers an important problem: addressing non-stationarity in reinforcement learning.

2. The authors provide a good literature review on three different techniques this paper utilized.

### Weaknesses
1. This paper integrates three different techniques but the underlying motivation is unclear.

- The choice of GNNs (specifically GAT) for representing causal graphs necessitates a stronger justification, given that causality inherently relies on the structure of directed acyclic graphs. While GATs can process graph-structured data, the paper does not adequately explain why GAT's attention mechanism is crucial for capturing causal relationships, especially when compared to other GNN architectures that might be more suitable for DAGs. The paper should clarify the specific advantages of using GAT over alternatives, particularly in the context of causal discovery where edge directionality is critical.

- Similarly, the adoption of causal-origin representation within the reinforcement learning framework also needs more justifications. The paper introduces this representation but does not clearly articulate why this specific form is superior to other potential methods for handling non-stationarity. A more detailed explanation of the theoretical underpinnings and the specific benefits of this representation in the context of RL is needed.

2. One of my biggest concerns lies in the theoretical analysis. As the paper is concerned with the non-stationary RL, the performance guarantees, i.e., regret bound and convergence rate, are not studied at all. The absence of these guarantees makes it difficult to assess the theoretical robustness and reliability of the proposed method, especially in comparison to existing approaches that do provide such analysis.

3. Another biggest concern is that the novelty and contribution of this work are not significant. The GAT, causal discovery, and non-stationary RL are well studied in many existing literature. The paper does not provide significantly novel methodological or theoretical techniques in the current stage. The combination of these techniques, while potentially useful, does not present a substantial advancement over existing methods.

4. The mixing of varying components for policy optimization makes the algorithm difficult to train. I am concerned about the efficiency and complexity of the proposed method, especially compared to the existing baselines (in terms of model complexity, computation, and sample efficiency). The paper lacks a detailed analysis of the computational cost and sample complexity of the proposed method, making it difficult to assess its practical applicability.

5. The total loss contains multiple tuning parameters (>3), how to efficiently tune these parameters, and what's the sensitivity of the model performance concerning these parameters? The authors only present some preliminary sensitivity analyses on tasks such as cartpole swingup, it is insufficient to demonstrate the robustness of these parameters. The sensitivity analysis should be extended to a wider range of tasks and parameter values to provide a more comprehensive understanding of the algorithm's robustness.

6. The training procedure is not fully disclosed. The authors need to provide specific learning rates, initial values set up, parameter-tuning details, and values for each task. Without these details, it is difficult to reproduce the results and verify the claims made in the paper.

7. The experimental design to emulate non-stationarity is somewhat naive and may not encapsulate the variety and complexity of non-stationarities encountered in practical settings. The algorithm's efficacy under more typical real-world conditions remains unverified, thus limiting the potential impact of the work. The chosen non-stationarity is too simplistic and does not reflect the complexities of real-world scenarios.

8. The presentation of this paper needs significant improvement. And I highly recommend the authors do more proofreading. In particular:

- The format of notations is not standard in RL, causal inference, or GNN literature, which puts additional burdens on readers to understand. The notation choices are inconsistent with established conventions, making it harder for readers familiar with these fields to grasp the concepts.

- The logical flow of the paper is not clear, and the central claim is vague. The paper lacks a clear and concise narrative, making it difficult to follow the authors' line of reasoning and understand the core contribution.

- There exist many typos and errors, like the repeated authors' names (redundant citations) in the section of related works.

### Questions
Please consider addressing the weaknesses above.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript introduces an efficient solution to tackle the challenges posed by non-stationary RL, by causality-inspired aspects. This facilitates the necessary adjustments to the policy, enabling it to adapt seamlessly to environmental shifts. The authors employ a graph representation to articulate the data generation process inherent to non-stationary RL systems, introducing a dual graph attention network designed to model both the core-graph and general-graph, which collectively encapsulate the graphical structure of the system. The learning of these graph structures from observed data is central to the identification of causal origins. Empirical evaluations verify the method’s efficacy across a diverse array of non-stationary environments, showcasing its robustness. In essence, this work not only presents a potent solution to non-stationary RL challenges but also holds promising implications for potential applications in related domains, such as transfer RL.

I am also a reviewer of the previous version of this paper. Most of my concerns have been addressed by the authors. However, some of them are still a bit unclear to me. I think the manuscript could benefit from additional clarity, particularly regarding the theoretical underpinnings of causality, and a more comprehensive analysis. Given these considerations, my preliminary assessment aligns with an accept recommendation, contingent upon the aforementioned enhancements.

### Strengths
**[About Motivation]** The utilization of causal modeling to understand the environmental aspects of the RL system, and identify the non-stationary origins, is technically sound;

**[About the Algorithm]** The general algorithm design is simple and easy to follow (while certain aspects of the method’s design could be described as empirical, without the grounded theoretical insights);

**[About Writing]** The overall writing is clear and easy to follow.

**[About Experiments]** The experimental design is comprehensive, including a variety of common non-stationary RL environments, as well as diverse factors of change.

### Weaknesses
I listed both the weaknesses and questions here.

**[About the theoretical insights of the proposed method]**

From the standpoint of empirical design, I can grasp the concept of amalgamating two graphs to extract the authentic causal graph. However, there remains a lack of clarity regarding the assurance that this specific design is capable of successfully distilling the causal origin of the changes observed. Providing theoretical insights or references that elucidate this process would contribute greatly to the understanding of the methodology. Alternatively, empirical validations, such as demonstrating a correspondence between the graphs generated by the model and the actual causal origins as defined within a simulator, would also serve to reinforce the credibility and effectiveness of the proposed design.

**[About graphs]**

If it is possible to empirically display the learned representation in both graphs? I understand that the environments used in the paper are complicated, and may lack ground truth to find a link between the learned graph representation to the real system parameters. However, the authors could consider doing it on some simulated MDPs (adding non-stationary factors to them) to validate the learned representation.

### Questions
I listed both the weaknesses and questions in the above section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses nonstationarity in reinforcement learning by positing the presence of a latent variable and utilizing mixture models to model the states. More specifically, the paper introduces an algorithm named COREP, which aims to acquire a stable graph representation for states referred to as the causal origin representation. This formulation can integrate with existing RL algorithms. The experimental results reported in the paper appear to be quite promising.

### Strengths
1. This paper introduces a causal interpretation for non-stationary Reinforcement Learning, attributing the nonstationarity to unobserved discrete variables denoted as "e," and it models the states using mixture models. This approach is reasonable.

2. The reported performance surpasses that of other baseline models.

### Weaknesses
This paper presents some challenges in terms of clarity and coherence, particularly in explaining how latent state dimensions (denoted as "h") are identified. This identification is crucial for understanding how the MAG is learned over the joint variables {s, h}.

While the authors use bidirected edges in the MAG to capture changes in the marginal distributions of s and h across various environments, it's worth noting that relying solely on bidirected edges may not suffice. It's important to consider that edges with circles might also have latent variable "e," resulting in distribution shifts.

### Questions
1. How are the latent state dimensions h identified?

2. Why only consider bidirected edges to indicate the changes?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a solution to dealing with a non-stationary environment using causal notions and deep RL.

### Strengths
The paper brings together a range of different notions, including causality, deep RL, Causal Structure Discovery, etc.

### Weaknesses
The primary issue with the paper is that there are known solutions to this problem that use far simpler approaches than those proposed. The authors are clearly unaware that this is a solved problem. As a consequence, I cannot recommend acceptance without clear comparison with existing solutions, both theoretically and empirically. Theoretically the authors need to justify why such a more computationally complex solution is justified given the existing solutions. Empirically, it is important to know if performance improvements can be obtained wrt state-of-the-art methods.

The paper defines a non-stationary environment " as a nonstationary mixture of various stationary environments".

  --  this is a strong assumption

  --  in control theory there are well-known solutions to systems under such an assumption. For example, multiple model adaptive control is a known solution.

Murray-Smith, R., & Johansen, T. (Eds.). (2020). Multiple model approaches to nonlinear modelling and control. CRC press.

Basically, given a collection of pre-defined stationary environments, if we generate a controller for each of these environments, then we have a guaranteed controller for any mixture of these stationary environments.

Some references about this:

Zhang, W., & Li, Q. (2020). Stable Weighted Multiple Model Adaptive Control of Continuous-Time Plant. In Virtual Equivalent System Approach for Stability Analysis of Model-based Control Systems (pp. 111-127). Singapore: Springer Singapore.

Provan, G., Quinones-Grueiro, M., & Sohége, Y. (2022). Towards Real-Time Robust Adaptive Control for Non-Stationary Environments. IFAC-PapersOnLine, 55(6), 73-78.

Deng, X., Zhang, Y., & Qi, H. (2022). Towards optimal HVAC control in non-stationary building environments combining active change detection and deep reinforcement learning. Building and environment, 211, 108680.

In all of this prior work, no notion of causality is necessary. Hence it is unclear why the causality-based solution proposed is indeed necessary.

Other Issues

Eq. 3.1 is hard to understand
Why not use standard dynamical systems state-space representation? Or probabilistic representation?
if you invent notation, it should be better than what exists. This is not.

Experiments: "we compare COREP with the following baselines: FNVAE (Feng et al., 2022), VariBAD (Zintgraf et al., 2019), and PPO (Schulman et al., 2017)."

---unless you compare COREP with a mixture-based MMAC solution then I cannot see how to understand how well it does. These are only RL-internal methods.

5 RELATED WORK
The authors completely miss known solutions as referenced earlier.

### Questions
1. What justifications can be provided for such a complex approach when  mixture-based MMAC already solves the problem? We can use learned models for the model bank in MMAC.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces a novel algorithm (COREP) aimed at addressing non-stationarity in reinforcement learning by emphasising causal relationships within states and utilising a "causal-origin" representation. The algorithm can be integrated with existing RL methods, and its effectiveness is supported by theoretical analysis and demonstrated through experiments in diverse non-stationary environments.

### Strengths
The main review will take place in this section owing to the flow in which the review was conducted.

### Abstract

- Aren't the first few sentences a bit of a contradiction? You are assuming causal knowledge which is perhaps the strongest prior impractical knowledge there is? But before that you say that modelling the non-stationarity (NS) is impractical because of the strong prior knowledge required.
- Seems like a misnomer to say that we are seeking to 'tackle NS' - surely you are wanting to model it, not treat it like a phenomena that needs to be overcome.

### Introduction

- [second paragraph] It is more correct to say that learning a causal graph from observations in an NS environment is difficult (normal causal discovery is exceptionally difficult in and off itself) because of the inherent distribution shift. This does not necessarily mean that the DAG itself is changing it could be a mechanism drift that is causing the change in dynamics and hence NS. You should explain this.
- I am not entirely sure that you need the last two paragraphs of this section because the information is so dense and specialised, it is okay for the reader to just wait for the main exposition of the method, rather than have you summarise it here in the introduction. I.e. I do not think it adds a lot.

### Methodology

- I do not follow how your method accounts for NS in the mechanism rather than NS in the topology. You are learning a graph topology to model the NS. But the mechanism (the functions, edges, of that DAG) may be generating the concept drift (NS). Consider that in a causal setting, non-stationarity can arise from both changing DAG topology and changing mechanisms within a static DAG topology:
1. **Changing DAG Topology**:
   Non-stationarity can occur when the causal relationships represented by the DAG change over time. For example, in a dynamic causal system, the underlying structure of causal relationships may evolve. This means that the set of variables and their connections, as represented by the DAG, can change. This situation is common in dynamic systems where, for instance, new causal pathways emerge, or existing ones disappear over time. Detecting and modeling these changes in the DAG topology is essential for understanding causality in a dynamic environment.

2. **Changing Mechanisms within a Static DAG Topology**:
   Even within a static DAG topology, non-stationarity can manifest if the mechanisms governing the relationships between variables change over time. This means that the functional forms or conditional dependencies between variables may vary under different conditions or time periods. For example, a medical treatment may have different causal effects on patients of different ages or genders. In this case, the underlying DAG structure remains the same, but the mechanisms, such as the strength of causal connections, can change.

-  Please comment on how your interacts with this setting.
- You assume that there are $K$ distinct stationary environments but $K$ is not upper-bounded. So if $K\rightarrow +\infty$ what happens then?

### Experiments

- [first sentence] Again you are treating NS as adversary rather than something to be modelled. The phrasing seems a bit odd given that you seek a model which can model the NS not remove it.
- Relating back to your abstract, you make the claim that "most existing methods attempt to model changes in the environment explicitly, often requiring impractical prior knowledge" (second sentence). You have not conducted any experiments which actually address that claim but have instead provided (impressive) results which compare your method to other SoTA methods. My main concern with this paper is that I simply do not believe that what you have proposed is in fact _more practical_ than having prior knowledge (as is your claim). 

### Related work

- Excellent section. Very comprehensive.

### Weaknesses
I am not convinced that this approach is better than the assumption of strong prior knowledge required to model NS in the system. This appears to be far more computationally burdensome.

### Abstract

- Aren't the first few sentences a bit of a contradiction? You are assuming causal knowledge which is perhaps the strongest prior impractical knowledge there is? But before that you say that modelling the non-stationarity (NS) is impractical because of the strong prior knowledge required.
- Seems like a misnomer to say that we are seeking to 'tackle NS' - surely you are wanting to model it, not treat it like a phenomena that needs to be overcome.

### Introduction

- [second paragraph] It is more correct to say that learning a causal graph from observations in an NS environment is difficult (normal causal discovery is exceptionally difficult in and off itself) because of the inherent distribution shift. This does not necessarily mean that the DAG itself is changing it could be a mechanism drift that is causing the change in dynamics and hence NS. You should explain this.
- I am not entirely sure that you need the last two paragraphs of this section because the information is so dense and specialised, it is okay for the reader to just wait for the main exposition of the method, rather than have you summarise it here in the introduction. I.e. I do not think it adds a lot.

### Methodology

- I do not follow how your method accounts for NS in the mechanism rather than NS in the topology. You are learning a graph topology to model the NS. But the mechanism (the functions, edges, of that DAG) may be generating the concept drift (NS). Consider that in a causal setting, non-stationarity can arise from both changing DAG topology and changing mechanisms within a static DAG topology:
1. **Changing DAG Topology**:
   Non-stationarity can occur when the causal relationships represented by the DAG change over time. For example, in a dynamic causal system, the underlying structure of causal relationships may evolve. This means that the set of variables and their connections, as represented by the DAG, can change. This situation is common in dynamic systems where, for instance, new causal pathways emerge, or existing ones disappear over time. Detecting and modeling these changes in the DAG topology is essential for understanding causality in a dynamic environment.

2. **Changing Mechanisms within a Static DAG Topology**:
   Even within a static DAG topology, non-stationarity can manifest if the mechanisms governing the relationships between variables change over time. This means that the functional forms or conditional dependencies between variables may vary under different conditions or time periods. For example, a medical treatment may have different causal effects on patients of different ages or genders. In this case, the underlying DAG structure remains the same, but the mechanisms, such as the strength of causal connections, can change.

-  Please comment on how your interacts with this setting.
- You assume that there are $K$ distinct stationary environments but $K$ is not upper-bounded. So if $K\rightarrow +\infty$ what happens then?

### Experiments

- [first sentence] Again you are treating NS as adversary rather than something to be modelled. The phrasing seems a bit odd given that you seek a model which can model the NS not remove it.
- Relating back to your abstract, you make the claim that "most existing methods attempt to model changes in the environment explicitly, often requiring impractical prior knowledge" (second sentence). You have not conducted any experiments which actually address that claim but have instead provided (impressive) results which compare your method to other SoTA methods. My main concern with this paper is that I simply do not believe that what you have proposed is in fact _more practical_ than having prior knowledge (as is your claim).

### Related work

- Excellent section. Very comprehensive.

### Questions
See Strengths section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
