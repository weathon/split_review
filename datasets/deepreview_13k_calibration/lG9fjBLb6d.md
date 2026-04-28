# RFMamba: Frequency-Aware State Space Model for RF-Based Human-Centric Perception

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Human-centric perception with radio frequency (RF) signals has recently entered a new era of end-to-end processing with Transformers. Considering the long-sequence nature of RF signals, the State Space Model (SSM) has emerged as a superior alternative due to its effective long-sequence modeling and linear complexity. However, integrating SSM into RF-based sensing presents unique challenges including the fundamentally different signal representation, distinct frequency responses in different scenarios, and incomplete capture caused by specular reflection. To address this, we carefully devise a dual-branch SSM block that is characterized by adaptively grasping the most informative frequency cues and the assistant spatial information to fully explore the human representations from radar echoes. Based on these two branchs, we further introduce an SSM-based network for handling various downstream human perception tasks, named RFMamba. Extensive experimental results demonstrate the superior performance of our proposed RFMamba across all three downstream tasks. To the best of our knowledge, RFMamba is the first attempt to introduce SSM into RF-based human-centric perception.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes RFMamba, a frequency-aware state space model (SSM) for human-centric perception using RF signals. RFMamba addresses the challenges of processing long-sequence RF data, with an innovative dual-branch SSM block that handles frequency and spatio-temporal cues for better accuracy in human tracking tasks. The model is evaluated on downstream tasks and shows significant performance improvements over existing methods. The proposed method is inspiring and paper is well-structured, but could improve in clarity and visual representation.

### Strengths
The model offers a practical solution to handle long-sequence RF signals with linear complexity. The dual-branch design of the block integrates both frequency and spatio-temporal information, addressing the core challenge for RF signal representation learning. The proposed RFMamba shows clear improvements in localization, recognition, and action detection tasks.

### Weaknesses
1) Some equations and model parameters are not sufficiently explained. This makes it a bit hard to grasp the model's operation and how it ties into the broader methodology.
For example, some suggestions for modification:
- For Figure 1, it would be better to enlarge the font sizes of labels and titles.
- In Section 3.1.1, after the introduction of frequency and spatial analysis in RF sensing, would be better to connect more to the proposed method and methodology.
- In Section 3.1.2, eq (4), explain better, not clear what are h and h' meaning, and model parameters A, B, C, D's usage, also can connect more to the overall methodology.

2) While the paper claims linear complexity, it's a bit unclear the resulting computational costs compared with similar models. Some theoretical or empirical comparison would help better clarify its practical deployability.

3) The model's applicability to other domains and signal types can make a straightforward discussion to complete the methodology and usage range.

### Questions
1) Can the model specifically deal with extreme RF environments in practical use? such as high interference or low signal-to-noise ratios? and what about the demanded resources (data and computation) if adapted to practical scenarios?

2) How does RFMamba's computational efficiency compare to similar SSM or Transformer-based models in terms of real-time performance?

3) How generalizable is RFMamba to other RF-based applications beyond human perception?

### Soundness
3

### Presentation
2

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
This paper presents a state space model designed for RF-based human perception. The authors introduce various modules, incorporating both frequency domain and spatio-temporal domain components. Additionally, they develop a six-way scanning method within the frequency modeling branch. Experimental results demonstrate the effectiveness of the proposed approach.

### Strengths
(1) This paper is the first to apply the Mamba method for RF-based sensing, marking a novel contribution to the field.

(2) The authors provide comprehensive discussions for each module in the proposed framework.

(3) A six-way scanning strategy in the frequency modeling branch is proposed, enabling adaptive selection of the most informative frequency cues.

(4) Real-world experimental results demonstrate the effectiveness of the proposed method in terms of both accuracy and parameter efficiency.

### Weaknesses
(1) The introduction sections on RF sensing and SFCW are underdeveloped. A more detailed discussion on the model and data specifics for SFCW radar is needed, including the signal processing steps from raw ADC data to the input tensor used by the model. The specific parameters of the SFCW radar, such as bandwidth, center frequency, and antenna array configuration, should be explicitly stated and their impact on the data characteristics discussed.

(2) The related work section is limited. The authors should include a review of state-of-the-art wireless signal sensing work relevant to RF pose estimation and clarify distinctions between the proposed model and other Mamba-based approaches. Specifically, a comparison with methods using different RF modalities (e.g., WiFi, mmWave radar) and their respective advantages and disadvantages should be included. The discussion should also clarify how the proposed method addresses limitations of existing Mamba-based models in handling RF data.

(3) The framework of the model requires a more detailed discussion, and the training algorithm should be included in the paper. The functionality of each block in Fig. 2 needs further clarification, particularly the SiLU block and its role in feature modulation. The loss function requires more elaboration, including the specific mathematical forms of the pose estimation, action recognition, and ReID losses, and the rationale for their weighting in the joint loss function. A detailed description of the training algorithm, including optimization parameters, learning rate schedule, and batch size, is needed.

(4) The experimental results could benefit from further enhancement. The evaluation should include a more comprehensive analysis of the model's performance under various conditions, such as different levels of noise, occlusion, and varying subject distances. The results should also be compared against a wider range of baseline methods, including both traditional signal processing techniques and state-of-the-art deep learning models.

### Questions
(1)The authors primarily use a custom MIMO (SFCW) radar to validate their proposed method. Consequently, the paper’s title, which references RF-based human-centric perception, may overstate the scope, as other radar types and RF-based sensing modalities (e.g., Wi-Fi, RFID, LoRa) are not examined. The authors should clarify their motivation for selecting SFCW radar, including its advantages over existing options like TI mmWave radar.

(2) The introduction of SFCW radar in Section 3.1.1 lacks clarity. For example, it is unclear how Eq. 3 represents the signal across three key dimensions: fast time (distance), antenna (azimuth and elevation), and slow time (velocity across echoes). A more detailed explanation in this section would improve understanding.

(3) In the related work section, more state-of-the-art studies on wireless signal sensing relevant to RF pose estimation should be reviewed. The authors should also discuss distinctions between the proposed Mamba method and other Mamba-based methods.

(4) For the framework depicted in Fig. 2, while each block is briefly explained, more specific functionality should be provided, including details on the SiLU block. Additionally, the loss function and training approach require elaboration. For instance, the rationale for using different task losses to define the joint training loss in Eq. 11 should be clarified. Since the code is not provided, a detailed description of the training algorithm is needed.

(5) Though the proposed method is tested with a real-world setup, it would benefit from validation using a public dataset, such as an mmWave radar dataset. The authors should also consider benchmarking against advanced transformer models and other Mamba methods. Furthermore, the evaluation on generalization and multi-person scenarios is limited; additional tests across different time (different days) and involving more than three individuals would strengthen the findings.

### Soundness
3

### Presentation
2

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
This paper proposes a State Space Model (SSM) based method for human-centric perception with radio frequency (RF) signals. Specifically, the authors devise a two-branch model to learn frequency and spatial-temporal features, respectively. The authors have also conducted comprehensive experiments to demonstrate the superiority of their method.

### Strengths
1. The use of Mamba models in RF-based sensing is novel.
2. The authors have collected a new dataset and evaluated their method with three downstream tasks.

### Weaknesses
1. The motivation of using Mamba models is not clear enough. The authors mention that Mamba models are more capable of tackling long sequences, while the authors have not discussed the performance of models in terms of different lengths of sequences. Specifically, the paper lacks a discussion on how the sequence length impacts the model's ability to capture temporal dependencies and spatial information. It is unclear if the choice of sequence length is optimal for the given task, and how this choice affects computational cost and performance.
2. A common challenge in RF-based sensing is cross-domain sensing, since RF signals may differ between different environments. I understand that this paper pioneers the use of Mamba models for RF-based sensing, rather than focusing on cross-domain sensing, but the authors should provide more discussions on this. The paper does not address the potential variations in RF signals due to environmental factors such as multipath fading, interference, and changes in the physical layout of the sensing area. These factors can significantly impact the model's generalization capability and robustness in real-world scenarios.
3. The authors have compared their method with baselines in terms of the number of parameters, while the authors can also compare their detailed efficiency, such as training time, testing time, and throughput. A detailed comparison of computational efficiency is missing, making it difficult to assess the practical applicability of the proposed method. The paper should provide a more comprehensive analysis of the computational overhead, including training time, inference time, and throughput, to demonstrate the method's efficiency.
4. Many related works about Wireless Signal Sensing have not been discussed. For example, recent works have involved the use of WiFi signals, ultra-wideband radars, millimeter wave radars. The authors only discussed three related papers about wireless sensing. The related work section is limited, and lacks a thorough discussion of other relevant RF-based sensing techniques. The paper should include a more comprehensive review of existing methods, including those using WiFi, UWB, and mmWave radar, to provide a better context for the proposed approach.

### Questions
1. Can the authors provide more discussions about cross-domain sensing?
2. Can the authors compare their methods in terms of detailed efficiency?
3. Can the authors discuss more related works about wireless sensing?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents RFMamba, a novel frequency-aware state space model for RF-based human-centric perception (HCP), designed to process radio frequency (RF) signals for tasks like human pose estimation, activity recognition, and person re-identification (ReID). Leveraging the capabilities of state space models (SSMs), RFMamba uses a dual-branch architecture that combines frequency and spatiotemporal modeling to effectively capture the characteristics of RF signals. The model introduces an omni-dimensional scanning mechanism, selectively focusing on informative frequency cues. Experiments on the newly introduced THP dataset (covering both free-space and wall-occlusion scenarios) demonstrate RFMamba’s superior performance over existing methods in accuracy.

### Strengths
1. Motivation and practical use cases: The authors address real-world challenges in RF-based human perception, aiming to support applications like security, health monitoring, and emergency response by enabling through-wall sensing and multi-person tracking where visual methods may be ineffective.

2. Technical novelty with Mamba modules: RFMamba leverages Mamba-based state space modeling specifically adapted for RF signals, incorporating frequency and spatiotemporal Mamba modules to capture long-term dependencies within complex RF data.

3. Generally clear presentation: The paper is well-structured and understandable, though some details are missing, particularly regarding some design choices, data collection and experimental setup (see weaknesses below).

### Weaknesses
1. Lack of sequence length analysis: While the authors emphasize the model's capability to handle variable and long input sequences, they do not provide an analysis of how sequence length affects performance, efficiency, or stability. It would be useful to see experiments with varying sequence lengths, insights into computational complexity and memory impact, and clarification on the sequence length used in their experiments.
2. Potential for improved transformer-based model: The lower performance of RadarFormer likely reflects specific design choices rather than a fundamental transformer limitation for RF perception (e.g., using only amplitudes, using two successive frames instead of 12). The authors did not explore enhancements to RadarFormer, such as incorporating phase information, extending the temporal context, or adding RF-specific adaptations, which may have yielded results comparable to or better than RFMamba, questioning the necessity of Mamba-based SSMs.
3. Unclear design choices: Some design decisions are not fully explained. For instance, in Figure 3(a), the scanning path appears to follow a bidirectional approach converging at the center. It is unclear why the authors did not consider capturing both sequences (from T−6 to T+6 and T+6 to T−6) and concatenating them, which could potentially enrich the temporal representation and improve performance.
4. Lack of details on activity types, distribution, and environment diversity: The paper lacks specifics on the 19 activities in the THP dataset, their frequency distribution, and whether participants performed these activities statically or while moving freely. This is important for understanding the model’s generalization across activity types and movement patterns in RF-based perception. Additionally, the dataset was collected primarily in a single environment (with and without a wall), limiting environmental diversity. It remains unclear if the model would perform similarly in different settings, whether it would need extensive data collection, or if fine-tuning would be required in new environments.
5. Limited dataset accessibility: Although the THP dataset provides valuable scenarios for evaluating RF-based human perception, it is not confirmed for public release, restricting reproducibility and broader research applications in this area.
6. Unclear real-time performance: The paper lacks analysis on the compute and memory requirements needed for real-time performance, leaving practical deployment feasibility uncertain.
7. Lack of generalization comparison with baseline models: While the authors claim that RFMamba generalizes well across various scenarios, there is no direct comparison with existing methods on generalization performance. Without showing how baseline models perform in similar conditions, it is difficult to assess whether RFMamba’s improvements are specific to the training environment or if they extend to varied, unseen scenarios.

### Questions
1. What are the specific activities in the THP dataset, and what is their distribution?
2. Were participants stationary or moving freely during activities?
3. Would the model generalize to other environments without additional data collection or fine-tuning?
4. The authors used SFCW radars for evaluation. Would the proposed method generalize to FMCW radar systems as well, and if so, what adjustments might be necessary?
5. Will the THP dataset be made publicly available to support reproducibility and further research in RF-based human perception?
6. What are the compute and memory requirements for achieving real-time performance with RFMamba?
7. The dataset was split into a 4:1 training-testing ratio. How much data was allocated for validation, and what criteria were used for this split?
8. For pose estimation, the authors used the metric Mean Per Joint Position Error (MPJPE). Is this measured in 3D or 2D space?
9. Was IRB approval obtained for the human subject data collection, and were participants informed and provided consent for the use of their radar and camera data in this study?

### Soundness
2

### Presentation
3

### Contribution
3
