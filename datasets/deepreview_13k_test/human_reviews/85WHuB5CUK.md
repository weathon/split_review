# STOP! A Out-of-Distribution Processor with Robust Spatiotemporal Interaction

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
Recently, spatiotemporal graph convolutional networks have attained significant success in spatiotemporal prediction tasks. However, they encounter out-of-distribution (OOD) challenges due to the sensitivity of node-to-node messaging mechanism to spatiotemporal shifts, leading to suboptimal generalization in unknown environments. To tackle these issues, we introduce the **S**patio-**T**emporal **O**OD **P**rocessor (STOP), which leverages spatiotemporal MLP channel mixing as its backbone, separately incorporating temporal and spatial elements for prediction.   To bolster resilience against spatiotemporal shifts, STOP integrates robust interaction including a centralized messaging mechanism and a graph perturbation mechanism. Specifically, centralized messaging mechanism configures Context Aware Units (ConAU) to capture generalizable context features, constraining nodes to interact solely with ConAU for spatiotemporal feature interaction. The graph perturbation mechanism uses Generalized Perturbation Units (GenPU) to disrupt this interaction process, generating diverse training environments that compel the model to extract invariant context features from these settings. Finally, we customized a spatiotemporal distributionally robust optimization (DRO) to enhance generalization by exposing the model to challenging environments. Through evaluations on six datasets, STOP showcases competitive generalization and inductive learning. The code is available at https://anonymous.4open.science/r/ICLR2025-STOP.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces STOP (Spatio-Temporal Out-of-Distribution Processor), a model designed to enhance the robustness of spatiotemporal predictions in out-of-distribution (OOD) environments. Traditional spatiotemporal graph convolutional networks (STGNNs) often struggle with OOD scenarios due to their reliance on node-to-node messaging, which is highly sensitive to shifts in temporal data distributions or structural changes in graph networks. STOP overcomes these limitations by integrating a novel client-server (C2S) messaging mechanism and a graph perturbation strategy that simulates various training conditions.

### Strengths
1. The client-server messaging approach with Context Perception Units is a clever departure from traditional node-to-node interactions, reducing sensitivity to structural shifts and enhancing adaptability in OOD settings.
2.  STOP’s design primarily relies on lightweight MLP layers, making it more computationally efficient than complex STGNNs or Transformer-based models, which often require high processing power.
3. The model was thoroughly tested across a variety of datasets, demonstrating not only generalization but also strong performance in both temporal and spatial OOD scenarios, enhancing the model’s credibility. 
4. The ablation studies are thorough and convincing.

### Weaknesses
See the questions listed below.

### Questions
1. Adding a paragraph discussing the research motivation and broader impacts of STOP could strengthen the work, particularly in terms of situating the work within the broader context of spatiotemporal OOD challenges. Additionally, the positioning of Figure 1 alongside the introductory text makes the flow slightly disjointed. A more developed introduction with a refined layout could improve the paper’s readability and help frame the significance of STOP’s contributions.

2. While the authors present the CPUs, GPUs, and DRO as core mechanisms in STOP, the paper could benefit from a more in-depth analysis of why each component specifically enhances spatiotemporal OOD detection. A theoretical analysis of how the graph perturbation strategy affects the model's ability to learn robust representations would provide a more solid grounding for their effectiveness and make the claims more convincing. 

3. What's the potential limitation of STOP? The authors may add a section to discuss potential trade-offs or scenarios where STOP might not perform as well compared to other approaches, which would provide a more comprehensive evaluation of the model's capabilities and limitations.

### Soundness
4

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
3

### Summary
This paper proposes the Spatio-Temporal OOD Processor (STOP) to enhance the generalization of spatiotemporal graph convolutional networks in out-of-distribution (OOD) environments. STOP uses spatiotemporal MLP channel mixing to separately incorporate temporal and spatial elements. It introduces Context Perception Units (CPUs) and Generalized Perturbation Units (GPUs) to capture generalizable context features and create diverse training environments, thereby improving robustness against spatiotemporal shifts. Additionally, a customized Distributionally Robust Optimization (DRO) is developed to further enhance generalization.

### Strengths
1. meticulous work and comprehensive experiments: The paper presents a thorough and detailed introduction and study, with extensive experiments conducted across multiple datasets. 

2. effective illustrations: The figures and diagrams included in the paper are well-designed and enhance the reader's understanding of the mechanisms introduced.

### Weaknesses
1. excessive use of abbreviations leading to confusion: The paper employs an abundance of abbreviations, some of which overlap with commonly understood terms like CPUs and GPUs. Abbreviations should be distinctive and aid in communication, rather than repurposing established terms in a way that might confuse the reader. 

2. lack of original innovation and theoretical justification: The proposed method appears to be a combination of existing modules and techniques borrowed from other works, giving an impression of an engineering patchwork rather than introducing novel contributions. The authors have not provided sufficient theoretical explanations to justify why their design choices effectively address the research problem.

3. lack of discussion regarding the potential limitations of the proposed method.

### Questions
See weaknesses.

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
3

### Summary
This paper presents the STOP model, designed to address OOD shifts in spatiotemporal prediction tasks. STOP employs an MLP channel-mixing backbone with robust interaction mechanisms, including C2S messaging and graph perturbation, to enhance resilience to spatiotemporal shifts. The C2S messaging mechanism utilizes CPUs for feature interactions, reducing dependence on global node-to-node messaging, while GPUs simulate spatiotemporal shifts to create diverse training environments. A customized DRO is also integrated to improve generalization.

### Strengths
This paper addresses the important and meaningful problem of spatiotemporal shifts. By introducing a lightweight MLP layer to model spatial and temporal dynamics, it effectively mitigates out-of-distribution (OOD) challenges while maintaining efficiency.

### Weaknesses
See questions part for more details.

### Questions
1. Section 5.4 only examines the hyperparameters \( K \) and \( M \), but since this paper focuses on model design, a more thorough exploration of hyperparameter choices (e.g., those discussed in Section 5.1) would be beneficial. Specifically, assessing the ease of finding optimal hyperparameters and their generalizability across downstream tasks is necessary. I feel the current discussion on these points is insufficient. Additionally, was the choice of \( M \) analyzed in Section 5.4 without being mentioned in Section 5.1?

2. The STOP model incorporates various component designs, including CPU and GPU interactions. While ablation studies that remove modules individually are common for validating component effectiveness, they often focus solely on the independent impact of specific components and may overlook interactions between modules. I suggest designing more comprehensive experiments, such as dual (or multiple) module ablations, to observe potential synergies or interdependencies among components.

3. This paper chooses an MLP as the backbone, differing fundamentally from the graph convolution architectures used in prior work. Aside from being more lightweight, what clear advantages does the MLP offer for addressing these types of problems?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors focus on the problem of spatial-temporal out-of-distribution learning. Specifically, they model temporal and spatial information separately and combine them with DRO loss for prediction. At the same time, corresponding modules are designed for the capture of temporal and spatial correlation. For the structural drift problem, this method attempts to model the global correlation between node features. Empirically, experiments have been conducted on a large number of datasets to verify their effectiveness.

### Strengths
1. The research question is critical
2. The technical description is clear
3. Comparative experiments with SOTA methods were conducted on multiple datasets

### Weaknesses
In general, from my point of view, this is good work in terms of technology. However, the connection between the problem scenario and the technology used is weak, and there is a lack of certain verification and explanation. Although this method avoids the problem of structural distribution drift by discarding the original structural information and modeling the global correlation between features, it wastes data information to a certain extent. At the same time, this paper lacks ablation experiments on DRO.  Specifically:

1) The author mentioned that the reason why STGNN performs poorly under distribution drift is: global node-to-node messaging for spatiotemporal interaction. Is this verified? Can the attention propagation method mentioned in this paper be avoided?

2) In the field of spatial-temporal graph learning, many operations model temporal information and spatial information separately. At the same time, why can this operation alleviate the error accumulation mentioned? Further explanation is needed here, or corresponding references are provided.

3) Some nouns are not named properly. For example, CPUs and GPUs are proper nouns. Also, Client-Server (C2S), is there any scenario involving federated learning here?

4) The description of related work is too simple and unsystematic.

5) In the methods section, where is the low-rank reflected? Is it the low-rank of the similarity matrix? What is its advantage in this scenario? This needs explanation, and the intuition of using this technique is not clear.

6) There are no ablation experiments for the DRO learning strategy.

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
