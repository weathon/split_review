# Sports-Traj: A Unified Trajectory Generation Model for Multi-Agent Movement in Sports

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Understanding multi-agent movement is critical across various fields. The conventional approaches typically focus on separate tasks such as trajectory prediction, imputation, or spatial-temporal recovery. Considering the unique formulation and constraint of each task, most existing methods are tailored for only one, limiting the ability to handle multiple tasks simultaneously, which is a common requirement in real-world scenarios. Another limitation is that widely used public datasets mainly focus on pedestrian movements with casual, loosely connected patterns, where interactions between individuals are not always present, especially at a long distance, making them less representative of more structured environments. To overcome these limitations, we propose a Unified Trajectory Generation model, UniTraj, that processes arbitrary trajectories as masked inputs, adaptable to diverse scenarios in the domain of sports games. Specifically, we introduce a Ghost Spatial Masking (GSM) module, embedded within a Transformer encoder, for spatial feature extraction. We further extend recent State Space Models (SSMs), known as the Mamba model, into a Bidirectional Temporal Mamba (BTM) to better capture temporal dependencies. Additionally, we incorporate a Bidirectional Temporal Scaled (BTS) module to thoroughly scan trajectories while preserving temporal missing relationships. Furthermore, we curate and benchmark three practical sports datasets, \textbf{\textit{Basketball-U}}, \textbf{\textit{Football-U}}, and \textbf{\textit{Soccer-U}}, for evaluation. Extensive experiments demonstrate the superior performance of our model. We hope that our work can advance the understanding of human movement in real-world applications, particularly in sports. Our datasets, code, and model weights are available at~\href{https://anonymous.4open.science/r/UniTraj-ICLR25/README.md}{link}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors focus on the trajectory prediction in sport scenes. They propose a trajectory generation model. They extend the Mamba model into a bidirectional temporal Mamba for the purpose to enhance the temporal dependencies with a transformer encoder for feature extractor. The proposed method aims to. solve the trajectory prediction, imputation and spatial-temporal recovery tasks in a unified paradigm. The applied methods are designed specified to the sports scenarios but some proposed modules can be appliable to more general tasks. The authors construct several sport scenario focused datasets with existing datasets. On the proposed benchmarking platform, the proposed method achieves good experimental results.

### Strengths
- the proposed method is well designed for the sport scenes, such as soccer or basketball. With also tracking and forecasting the ball motion, the proposed method can be useful for the related sport activities..
- The proposed ghost masking embedding used to replace the usual head token can provide the order-invariant properties to the agent features, which can be extended to many related applications without losing generalization.
- Built upon the usual Mamba blocks, the proposed Bidirectional Temporal Mamba provides an improved fashion of processing spatial-temporal features with good adaptation to handle features on missing time steps.
- On the sports datasets, Basketball, Soccer and Football videos, the proposed method shows good quantitative results when compared to other related works.
- Overall, the paper is well written and the technical section can be easily followed.

### Weaknesses
1. My main concern about the proposed method is its generalizability. To be precise, the proposed method is evaluated on the three datasets Basketball-U, Soccer-U and Football-U, which are built by the authors themselves thus lacking a well established benchmarking. Therefore, it is hard to estimate the significance of the experimental performance by the provided benchmarking results. I would suggest the authors to add the experiments on the existing benchmarks, such as SDD, ETH/UCY or HM3.6M and include the recently published trajectory prediction methods into the comparison for a more convincing and well-established benchmarking.
2. The proposed methods model the ball trajectory and offensive/defensive player position explicitly. It is not clear whether the other baselines also follow this convention. For many previous works on NBA benchmark, based on which Basketball-U dataset is constructed, only the players position is considered. Such details of implementation alignment between the proposed method and baseline methods included in the benchmark results is critical to conduct a fair experiment and provide reliable experimental evidence.
3. There are many more recent related works, though they are mostly published on the benchmarking of ETH/UCY and SDD, should have been included in the experimental comparison, to provide a up-to-date evaluation of the quantitative significance of the proposed method. To name some: Eqmotion[1], MemoiNet[2], Flowchain[3].

### Questions
My questions to be answered and my concerns to be addressed have been discussed in the `weakness` section.

### Soundness
2

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
This paper proposed a Unified Trajectory Generation model, UniTraj, that processes arbitrary trajectories as masked inputs, adaptable to diverse scenarios in the domain of sports games, integrating trajectory prediction, imputation, and spatial-temporal recovery into a single framework. Key contributions include the development of a Ghost Spatial Masking module for spatial feature extraction, a Bidirectional Temporal Mamba encoder for enhanced temporal modeling, and the curation of three new sports datasets for robust evaluation.

### Strengths
originality: This paper proposes a novel approach for handling multiple tasks, including trajectory prediction, imputation, and spatial-temporal recovery for multi-agent movement analysis. It introduces the innovative Ghost Spatial Masking module and extends the Mamba model with a new Bidirectional Temporal Scaled module to enhance the extraction of comprehensive spatial-temporal features from various incomplete trajectory inputs.

quality: The quality of this is generelly good. The method is well explained.

clarity: The paper is well-written and organized logically. The use of figures, especially the architectural diagrams and flowcharts, effectively aids in understanding the model's components and their interactions. Each section of the paper builds upon the previous one, leading to a cohesive narrative from problem formulation to experimental validation.

significance: The significance of this research lies in its potential impact on sports analytics and related fields requiring accurate multi-agent trajectory analysis.

### Weaknesses
The research problem is not well explained. The paper does not explain why all-in-one methods for the three tasks, trajectory prediction, imputation, and spatial-temporal recovery, have not been proposed. What are the challenges? The proposed methods should be compared separately with relevant methods for each task. Although the paper tests the model on three sports datasets, sports differ significantly in their dynamics and player interactions. More varied tests are needed.

### Questions
1.  Why have all-in-one methods for the three tasks, trajectory prediction, imputation, and spatial-temporal recovery, not been proposed.?
2. What are the challenges? 
3. Comparisons with other methods should be given.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
They focus on the domain of sports and address the problem of modeling multi-agent trajectories by considering various situations in real practice, emphasizing the need for a general approach. To accommodate diverse real-world scenarios, they introduce a unified trajectory generation task that simultaneously handles multiple input situations.

### Strengths
This paper introduces a new problem (a unified trajectory generation task) along with several new datasets, with relatively comprehensive experiments and a substantial amount of work. They propose a Unifed lrajectoryenyironments.Generation model, UniTraj, that processes arbitrary trajectories as masked inputs.adaptable to diverse scenarios in the domain of sports games. They further extend recent State Space models (SSMs), known as the Mamba model, into a Bidirectional Temporal Mamba (BTM) to better capture temporal dependencies.

### Weaknesses
1.Could you please try LSTM/CNN or any other backbones instead of MLP to achieve better performance?

2.Some equations are very similar, so you can combine them together (such as Eq.7). It's unnecessary to write them again.

3.You can also compare the FLOPs and total parameters with state-of-the-art methods to demonstrate your models’ efficiency.

### Questions
See weakness above.

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The contributions of the paper are as follows:
(1) The authors unified trajectory prediction, imputation, and spatial-temporal recovery into a single framework.
(2) They introduced the UniTraj model, capable of processing arbitrary trajectories as masked inputs, making it adaptable to diverse and incomplete datasets, particularly useful in sports scenarios.
(3) The paper shows how the Ghost Spatial Masking (GSM) module and the Bidirectional Temporal Scaled (BTS) module help achieve state-of-the-art performance by improving spatial feature extraction and preserving temporal relationships in trajectory data.
(4) The authors curated and benchmarked three practical sports datasets, namely Basketball-U, Football-U, and Soccer-U, which will serve as valuable resources for other researchers working in the field of sports analytics.

### Strengths
The paper presents an original idea by unifying three tasks—trajectory prediction, imputation, and spatial-temporal recovery—into a single framework. The selection of network components, such as the Ghost Spatial Masking (GSM) module and the Bidirectional Temporal Scaled (BTS) module, is well justified, and their effectiveness is thoroughly evaluated through extensive experiments. The model's performance is further validated using three distinct sports datasets, demonstrating its robustness and applicability across different scenarios.

### Weaknesses
In real-world scenarios, trajectory masking isn't limited to binary values (0 or 1); detection errors often lead to incorrect trajectories. For instance, a referee might be mistakenly tracked as a player, or an incorrect ball-like object could be detected as the ball instead of the actual one. These errors highlight the need for models to handle not only missing but also erroneous data in trajectory prediction and recovery tasks. The current approach of using binary masks does not account for the varying degrees of uncertainty or error that can occur in real-world tracking data. Furthermore, the model's reliance on clean, binary masked inputs may limit its robustness when faced with noisy or corrupted data, which is common in practical applications. The paper does not explore how the model would perform with different types of masking, such as Gaussian or other forms of probabilistic masking, which could better simulate real-world sensor noise and detection errors. The model's performance could be significantly impacted by the quality of the input masks, and this aspect needs further investigation.

### Questions
(1) At line 474, should it read "The 'w/o BTS' variant excludes the Bidirectional Temporal Scaled (BTS) module" instead of "w/o GSM"?

(2) At line 413, why is a total of K=20 trajectories generated? What is the variability among these 20 trajectories? I understand that generating multiple trajectories is necessary due to the model being generative, but I would like to know if selecting different values for K affects the experimental results (such as minADE). Additionally, were the baseline models evaluated under similar conditions, such as using K=20 trajectories?

(3) In Table 2, the minADE for UniTraj is reported as 94.59 pixels. What is the size of the soccer field in pixels? I want to understand how significant this error is in real-world measurements. Also, will you provide visual examples to demonstrate the quality of the generated trajectories, particularly for average cases?

### Soundness
2

### Presentation
3

### Contribution
3
