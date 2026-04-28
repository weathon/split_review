# Embodied Referring Expression Comprehension Through Multimodal Residual Learning

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 3, 5, 6, 5, 6

## Abstract
Comprehending embodied interactions within real-world settings poses a considerable challenge, attributed to the multifaceted nature of human interactions and the variability of environments, necessitating the development of comprehensive benchmark datasets and multimodal learning models. Existing datasets do not adequately represent the full spectrum of human interactions, are limited by perspective bias, rely on single viewpoints, have insufficient nonverbal gesture capture, and have a predominant focus on indoor settings. To address these gaps, we present an Embodied Referring Expressions dataset (called Refer360), which contains an extensive collection of embodied verbal and nonverbal interaction data captured from various viewpoints across various indoor and outdoor settings. In conjunction with this benchmark dataset, we propose a novel multimodal guided residual module (MuRes) that helps the existing multimodal models to improve their representations. This guided residual module acts as an information bottleneck to extract salient modality-specific representations, and reinforcing these to the pre-trained representations produces robust complementary representations for downstream tasks. Our extensive experimental analysis of our benchmark Refer360 dataset reveals that existing multimodal models alone fail to capture human interactions in real-world scenarios comprehensively for embodied referring expression comprehension tasks. Building on these findings, a thorough analysis of four benchmark datasets demonstrates superior performance by augmenting MuRes into current multimodal models, highlighting its capability to improve the understanding and interaction with human-centric environments. This paper offers a benchmark for the research community and marks a stride towards developing robust systems adept at navigating the complexities of real-world human interactions.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces Refer360, a novel dataset designed for embodied referring expression understanding, capturing interactions from multiple perspectives. In addition, it proposes an innovative Multimodal Guided Residual Module (MuRes), which enhances cross-attention mechanisms by effectively fusing visual and language features. The MuRes module establishes an information bottleneck by leveraging the differences between query, key, and value in cross-attention, ensuring seamless integration with residual connections.

### Strengths
The dataset features multimodal data captured from a wide variety of environments, including both indoor and outdoor settings. This addresses a significant limitation of existing datasets, which predominantly focus on indoor scenarios.

The proposed MuRes module provides an effective method for fusing multimodal representations, with the potential to enhance performance in downstream tasks such as visual question answering (VQA).

### Weaknesses
Lines 051–053: Verbal Utterances and Natural Expressions
The authors argue that utterances like "left ball" and "right ball" introduce bias and limit the model's ability to understand interactions. However, such expressions are natural in human communication and essential for interpreting real-world interactions. Excluding them could reduce the dataset’s ability to model realistic communication, thereby limiting the model's generalization to human behavior. While minimizing biases is a valid goal, removing these phrases may unintentionally hinder the model’s ability to understand natural referring expressions.

Lines 070–073: Ego View and Occlusions
The paper claims that incorporating multiple perspectives (e.g., egocentric and exocentric) helps mitigate occlusions. However, in real-world human interactions, an individual's egocentric view is not accessible to others. Communication typically relies on third-person perspectives, and handling occlusions is a natural part of this process. Incorporating egocentric views may introduce an artificial setup that does not align with real-world scenarios. Furthermore, this approach increases complexity and hardware requirements (e.g., wearable cameras), which may not be practical or scalable.

Lines 213–215: Participant Demographics
The dataset participants are primarily students with a mean age of 26, introducing potential demographic bias. This narrow age range may not adequately represent the wider population, particularly younger or older individuals. Consequently, the dataset’s ability to generalize across diverse age groups and social contexts could be limited.

Lines 337–338: Discrepancies in Model Training
The paper notes that the BLIP-2 model was trained with a smaller batch size (2) compared to other models (32), while all models were trained for the same number of epochs. This leads to BLIP-2 undergoing significantly more gradient updates, potentially skewing the performance comparison. However, the paper does not sufficiently address this discrepancy or its implications for the results.

Table 3: Performance of MuRes across Models
The performance improvements achieved by MuRes are inconsistent across different models, raising concerns about its general effectiveness:

VILT: MuRes shows only marginal gains (0.5 for IoU-25 and 0.6 for IoU-50 under the best setting).
BLIP-2: Performance declines significantly for IoU-25 (-4 for V, -3 for L, and -13 for V+L) and shows only minor improvement for IoU-50 under the L setting.
Dual-Encoder: Improvements are minimal, with slight increases of 0.3 for IoU-25 and 0.8 for IoU-50.
Scholarship
The paper could improve its scholarship by referencing relevant recent work, such as Understanding Embodied Reference with Touch-Line Transformer [ICLR 2023].

### Questions
see weakness box

### Soundness
2

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
4

### Summary
This manuscript presents a method to interpret embodied referring expressions, featuring the development of the Refer360 dataset and a MuRes module. 

The Refer360 dataset, designed for diverse human interactions in various indoor and outdoor settings, overcomes typical limitations of existing datasets by capturing multiple perspectives and blending verbal and nonverbal cues. 
The MuRes module reinforces salient aspects of modality-specific representations through cross-attention.

Experiments demonstrate that integrating MuRes into existing multimodal frameworks improves performance on several metrics related to embodied referring expression comprehension and VQA.

### Strengths
- Refer360 dataset enhances multimodal model training by encompassing a diverse array of human interactions across various environments. It includes both verbal and nonverbal communication, offering a detailed representation of real-world scenarios and setting new standards for dataset quality and utility in model development.

- The MuRes module isolates and enhances key features from various modalities, increasing the clarity and detail in the analysis of complex interactions.

### Weaknesses
 - The technical contribution of the MuRes module is modest, as it relies on cross-attention for feature enhancement, a method already common in the multimodal field. 
Integrating the MuRes module into existing multimodal frameworks can increase computational demands considerably due to its complex cross-attention mechanisms, leading to higher processing times and resource usage.

- In Table 3, applying MuRes sometimes results in lower performance compared to models without residual modules. For larger models like BLIP-2, the performance significantly drops, suggesting that MuRes may not be well-suited for all model architectures.

- Table 4 does not include the results for BLIP-2, raising doubts about the effectiveness of the proposed method on larger models.

- It is recommended to add experiments for the VQA task on embodied-related datasets to further validate the method's effectiveness in this specific application area.

- (minor) It is advised to use \citep for in-text citations to ensure consistent formatting and improve readability.

### Questions
Please refer to the weaknesses section. 

After considering the advantages and disadvantages outlined above, my overall assessment leans negative. I will adjust the score accordingly based on any responses or clarifications provided.

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
This paper presents a dataset called Refer360 which has verbal and non-verbal data from different viewpoints for referential expressions in indoor and outdoor settings. Furthermore, a multimodal guided residual module (MuRes) which can be used for improving representations of existing multi-modal models. The MuRes is evaluated on two downstream tasks: referential expressions and visual question answering. The baselines are CLIP, ViLT and BLIP-2 with and without MuRes(V), MuRes(L) and MuRes(V+L). For the referential expression, MuRes does not show a consistent performance increase while on the vqa task, MuRes(V+L) shows better performance except on Clip.

### Strengths
- A large dataset contains multi-modal data for referential expression. The dataset is recorded with egocentric and exocentric camera views, which is beneficial for training models with better generalisability. 

- Part of the dataset is collected in outdoor scenarios while most previous datasets are collected in indoor settings.

### Weaknesses
 - The authors describe the dataset as "to facilitate the understanding of human interactions in real-world settings", however, there is no interaction in the experiment protocal. There is only referential expressions by a human participant. 

- The benchmarking on referential expression only uses image and text as input modality, discard other modalities in refer360, especially gaze, which is an import indication of human's intention in referential expressions. Additionally, using gaze to identify objects in human-robot interaction has been shown adequate for understanding humans' intended object in various works.

Shi, Lei, Cosmin Copot, and Steve Vanlanduit. "Gazeemd: Detecting visual intention in gaze-based human-robot interaction." Robotics 10.2 (2021): 68.
Yang, Bo, et al. "Natural grasp intention recognition based on gaze in human-robot interaction." IEEE Journal of Biomedical and Health Informatics 27.4 (2023): 2059-2070.
Belardinelli, Anna. "Gaze-based intention estimation: principles, methodologies, and applications in HRI." ACM Transactions on Human-Robot Interaction 13.3 (2024): 1-30.

With the multi-modality data, the authors could benchmark for instance scanpath prediction using other modalities, and model performance using videos captured from different viewpoints.

- There are details of how the dataset is collected missing, for details see comments below.

### Questions
- The authors mentioned that the dataset was collected under different conditions such as variable lighting conditions, object arrangements, and environment appearances. These need to be elaborated.

- In one session, does the robot move when the participant refers to one object? In different sessions, when a viewpoint changes, does the participant always refer to the same object?

- The description of task needs more details, does the participant freely decide which object to point at?

- Annotation details are needed. What is annotated? The frames where humans are pointing at something or the intended object bounding box? Are all objects annotated? 

- I'd use video language models with MuRes as the dataset is in the video form.

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
In this paper, the authors introduce an embodied referring expressions dataset called Refer360, including various settings and providing insights for the community. Accordingly, a base model called MuRes is designed for evaluation.

### Strengths
- Contributing a benchmark called Refer360, facilitating the study of real-world human-robot interaction.

- The proposed dataset covers various real-world scenarios such as indoor and outdoor, supporting real-world applications without the need for sim2real adaptations.

- The paper is well-organized and easy to follow.

### Weaknesses
 - It seems that the authors have overlooked some related literature, such as [1-3], which introduced datasets and methods related to embodied referring expression, aimed at enabling agents to navigate to target points based on natural language instructions (i.e., Instruction Following). Although I understand that the authors intend to build an interaction-oriented embodied referring expression database, these related works are still worth discussing.

 - The proposed baseline method is quite simple, raising doubts about whether it can handle such complex interactive embodied tasks. Why not use open-source MLLM for fine-tuning, such as by adding extra adapters or training with LoRA?

 - The performance of the proposed method on Refer360 is not promising compared to other methods.

 - More samples (current 14k) including interaction would be beneficial for embodied tasks.

### Questions
- Is it possible to test the model trained on the Refer360 database on other related databases to validate the benefits brought by the rich information of Refer360?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents an Embodied Referring Expressions dataset to compensate for the missing perspectives in existing datasets, such as the full spectrum, perspective bias, and single viewpoint. In addition, the authors propose the residual module to improve the performance of existing pre-trained VLMs.

### Strengths
* The proposed dataset includes both indoor and outdoor scene understanding, and the data scale is quite considerable. It may be helpful for subsequent research work.
* The information source of the proposed dataset is very rich, and the author declares that it includes exo visual views, such as ego visual view, depth, infrared, 3D skeletal data, audio, and robot camera motion.

### Weaknesses
 * In my opinion, the focus of this work is on the proposed new dataset (core contribution), however, the author's discussion on the proposed dataset is rare. For example, the proportion of samples in different scenes in the visual part, how to describe the text part, the length range of each scene's text token description, and how the proposed dataset can be helpful in downstream tasks, etc.
* The multimodal fusion method proposed in this article seems to be a simplified version combining BLIP and LLaVa (cross-attention and mlp across modalities), with the only difference being the shift in focus from modal mapping to modal information fusion. In addition, How is the information of exo visual view, ego visual view, depth, infrared, 3D skeletal data, audio, and robot camera motion processed and integrated? The description of the method in Figure 3 is not clear.
* From the results in Table 3, it can be seen that the proposed residual module has limited help for pre-training models, compared to Without Residual and Vanilla Residual.

### Questions
How are multiple visual features extracted and fused, such as depth information? How is the text description obtained and what are the bases? How many frames of information does each sample contain?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new dataset, Refer360, for embodied referring expression comprehension along with a novel multimodal fusion technique using a bottleneck architecture - MuRes. The authors argue that the existing datasets lack the necessary diversity and complexity to truly capture human interactions - hence, they introduced Refer360. The authors also argue that MuRes helps bridge modality gap by learning aligned complimentary representations.

### Strengths
1. Originality: 

The authors convincingly provide arguments to demonstrate the gap in current datasets - they are limited in the variety/complexity of human interactions and variety of environments. The paper addresses these two important problems in their dataset by incorporating multiple viewpoints, multiple perception modalities, and multiple environments in their data. They also collect the data in scripted and unscripted manners. This dataset, with inclusion of verbal and non-verbal cues, is a valuable resource for future research.

The fusion architecture (MuRes) introduced in this paper is an interesting addition to the work. Using cross-attention to reinforce salient features from each modality is creative.

2. Quality: 

The research is conducted to a high standard, with a clear and well-motivated methodology. The data collection process is rigorous, involving the use of Kinect sensors mounted on robots and smart glasses worn by participants. This approach allows for the capture of rich multimodal data, including both visual and linguistic information. 

The proposed MuRes method is well-grounded in existing literature and addresses a key challenge in multimodal learning, namely, the effective fusion of information from different modalities.

3. Clarity:

The paper is well-written and easy to follow. The authors provide a clear and concise description of their method, and the experimental setup is well-explained. The results are presented in a clear and informative manner, with helpful visualizations and tables. The paper also includes a concise (but sufficient) discussion of related work, placing the research in its proper context.

4. Significance:

This work has the potential to make a significant impact on the field of embodied AI. The Refer360 dataset is a valuable contribution that will enable researchers to develop and evaluate more sophisticated models for embodied referring expression comprehension or any other embodied AI task. 

The MuRes method also shows promise for improving the performance of multimodal learning models in a variety of applications. The experiments in the paper show a substantial increase in performance for certain tasks. These performance gains may also translate to other downstream tasks in multimodal settings.

Overall, this research represents an important step towards the development of AI systems that can interact with humans in a more natural and effective way. Having more datasets like these is the key to fast-track research in embodied AI.

### Weaknesses
1. Lack of Clear Definition and Contextualization: The paper delays defining "embodied referring expression comprehension" until the related work section. This key concept should be introduced and clearly defined upfront - in abstract. Doing so would significantly improve the readability and understanding for readers unfamiliar with this specific area of research. Additionally, while the authors mention the importance of verbal and non-verbal cues, they neglect to provide specific definitions and examples within the context of their research. Providing these would enhance the paper's clarity and comprehensiveness.

2. Inadequate Analysis of Performance Inconsistencies: The analysis of the results does not delve into the inconsistencies in performance gains observed across different MuRes variants (MuRes(V), MuRes(L), and MuRes(V+L)), particularly in the embodied referring expression comprehension task - refer to its results table. A more in-depth discussion of these inconsistencies is necessary. The authors should provide explanations that justify the choice of a specific bottleneck architecture based on the domain, offering insights into the interplay between the architecture and the specific characteristics of each task. There should be some experiments and analysis to understand which modality should be favored for a particular type of task.

3. Limited Comparison with other methods for learning complementary representations: While the paper does a good job of showing that MuRes improves multiple encoder-fusion architectures, its does not perform any comparison with existing techniques for learning complementary representations in multimodal settings. The paper does compare their bottleneck framework with simple residual-based fusion and fusion without residuals, but these do not sufficiently show how it compares against other existing methods. For example, explore methods like those presented in "Learning Cross-Modality Encoder Representations from Transformers" (Tan et al., 2019) and "Attention Bottlenecks for Multimodal Fusion" (Nagrani et al., 2021).

4. Potential Bias in Data Collection: The data collection protocol includes both constrained and unconstrained settings. As participants may have participated in both, there is a concern that their experiences in the constrained setting might have biased their behavior in the unconstrained setting. The authors should address this potential issue and discuss any measures taken to mitigate this bias.

5. Limited Theoretical Foundation: While the MuRes architecture demonstrates empirical success, the paper lacks a strong theoretical foundation to support its design choices. The justification for the cross-attention mechanism and the specific configuration of queries, keys, and values appears to be based primarily on intuition and experimental validation. A more rigorous mathematical grounding, potentially drawing inspiration from information theory or optimization theory, would significantly strengthen the paper's technical contribution and provide deeper insights into the underlying principles of the MuRes architecture.

### Questions
1. Please talk about how you may mitigate the potential biases introduced in the dataset by interleaving scripted and unscripted interactions. Scripted interactions can bias a subject to act in a certain way while performing an unscripted interaction. Did you perform any experimentation/analysis with randomizing/separating the scripted-unscripted session sequence to understand/mitigate this bias?

2. The diagram depicting MuRes architecture could do a better job at showing how this architecture is a “bottleneck residual connection” architecture. Having the projection and cross-attention blocks vertically stacked may better represent this. Or labelling the key, value, queries in the diagram may make it easier to follow.

3. The experiments are solid but not varied in tasks covered. Showing performance improvements on more tasks can bolster the claims made in the paper. It would best if these new tasks are generation-based.

4. Can you provide any theoretical foundation for the design choice (cross-attention based bottleneck) that leads to the MuRes architecture? If this is something that is described by a related work, please talk about this in the related work section. If not, add a section justifying this choice theoretically.

5. Please define the "embodied referring expression comprehension" earlier in the paper so that the paper becomes easier to follow.

### Soundness
2

### Presentation
2

### Contribution
2
