# Generalizable and Efficient Video-Language Reasoning via Multimodal Modular Fusion

- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 8, 6, 8, 6

## Abstract
Despite impressive advancements in recent multimodal reasoning approaches, they are still limited in flexibility and efficiency, as these models typically process only a few fixed modality inputs and require updates to numerous parameters. This paper tackles these critical challenges and proposes CREMA, a generalizable, highly efficient, and modular modality-fusion framework that can incorporate many new modalities to enhance video reasoning. We first augment multiple informative modalities (such as optical flow, 3D point cloud, audio, thermal heatmap, and touch map) from given videos without extra human annotation by leveraging sensors or existing pre-trained models. Next, we introduce a query transformer with multiple parameter-efficient modules associated with each accessible modality. It projects diverse modality features to the LLM token embedding space, allowing the model to integrate different data types for response generation. Furthermore, we propose a novel progressive multimodal fusion design supported by a lightweight fusion module and modality-sequential training strategy. It helps compress information across various assisting modalities, maintaining computational efficiency in the LLM while improving performance. We validate our method on 7 video-language reasoning tasks assisted by diverse modalities, including conventional VideoQA and Video-Audio/3D/Touch/Thermal QA, and achieve better/equivalent performance against strong multimodal LLMs, including OneLLM, BLIP-2, and SeViLA while reducing over 90% trainable parameters. We provide extensive analyses of CREMA, including the impact of each modality on reasoning domains, the design of the fusion module, and example visualizations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces CREMA, an efficient and generalizable framework for video-language reasoning that enhances understanding through multiple modalities, including video, depth, audio, and 3D point cloud data, among others. CREMA employs a modular fusion approach, with lightweight, modality-adaptive modules that allow for easy integration of new modalities with minimal added parameters. The framework also incorporates a novel self-gated attention fusion technique to reduce computational demands. Additionally, it proposes a modality-sequential modular training and adaptive early exit strategy to boost training efficiency and enable faster adaptation to new modalities. CREMA demonstrates superior performance across multiple benchmarks, such as SQA3D, MusicQA, NExT-QA, TouchQA, and ThermalQA, highlighting the benefits of integrating diverse input modalities for improved video reasoning.

### Strengths
- This paper proposes a framework capable of handling multiple modalities and addresses the issue of token quantity increasing with the number of modalities.

- A single Q-former is used to process multiple modalities, avoiding the large increase in parameters typically associated with multi-modal input. Each modality requires only a small amount of modality-specific parameters, and since the parameters for each modality within the Q-former are independent, processing different modalities does not cause interference.

- The modality-sequential and modular training approach accommodates the differences across various modalities, preventing overfitting or underfitting to any specific modality.

- The paper demonstrates through multiple benchmarks that the proposed framework effectively integrates information from diverse modalities, thereby enhancing video reasoning capabilities.

### Weaknesses
 - I believe the main focus of this paper is on ensuring that the number of tokens input into the LLM does not increase linearly with the number of modalities, while maximizing parameter sharing across modalities to avoid excessive parameter growth. However, I feel that the teaser image does not effectively highlight these key points.

- My biggest concern lies with the Self-gated Multimodal Query Fusion. This module concatenates tokens from different modalities along the channel dimension, meaning that the input modalities during inference must match those used in training exactly—neither more nor less—otherwise, there will be a parameter mismatch within the Self-gated Multimodal Query Fusion. Many videos, for example, may not contain point cloud information; however, if point cloud data was included as input during training, it must also be part of the input during inference. This limitation significantly restricts the flexibility of input modality types.

- Additionally, the description of the zero-shot setup is not clear enough. Before performing zero-shot evaluation on SQA3D and MUSIC-AVQA, which datasets were used to train and optimize the model's new parameters? Furthermore, as mentioned above, I believe that the Self-gated Multimodal Query Fusion limits the model's zero-shot reasoning capabilities, as different combinations of input modalities would require different models. This implies that different models were likely used for zero-shot evaluation on SQA3D and MUSIC-AVQA. Therefore, the authors should clarify which specific model was used for evaluation in each experiment.

- Some related works on integrating multiple modalities are missing, such as MultiPLY[1] and X-VILA[2], both of which are multimodal LLMs capable of handling various input modalities. The authors should discuss the relationship with these works.

### Questions
Please refer to the weakness section.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes CREMA, a generalizable and modular modality-fusion framework that augments multiple modalities without extra human annotation and incorporates them into a query transformer, enhancing video reasoning. It introduces a progressive multimodal fusion design, maintaining computational efficiency and improving performance. Validated on 7 video-language reasoning tasks, CREMA outperforms or matches strong multimodal LLMs while significantly reducing trainable parameters, demonstrating its effectiveness and innovation.

### Strengths
1. The paper is clear writing and easy to follow.
2. Few current works focus on integrating multiple modalities, so the authors' motivation is commendable.
3. I appreciate the paper's innovation. Although it may not introduce many new structures, the modality-adaptive early exit strategy appears to have broad application potential. It's the first time I've seen the use of gradients to determine whether to exit early, and it is also the first method to apply early stopping by modality. Therefore, I acknowledge the paper's innovative approach.

### Weaknesses
1. Overall, I believe this paper is worthy of acceptance and presents no significant issues. My only curiosity, as mentioned by the authors in the limitations section, is whether the method can be applied to more advanced baselines such as LLava, rather than just BLIP. If feasible, I would appreciate the authors addressing this point, which could lead me to adjust my score upwards.

### Questions
Please refer to the weakness

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
4

### Summary
This paper proposes a method, "CREMA," that addresses the problem of video understanding with diverse modalities, including optical flow, point clouds, audio, etc. CREMA first uses modality-specific encoders to encode each modality. Then CREMA introduces a Q-former to extract features from each modality. Before feeding the features into LLMs, CREMA further leverages a self-gating modality fusion guided by the video features. Such an approach has the advantage of significantly less trainable parameters and competitive performance across multiple datasets, including MUSIC-AVQA, SQA3D, etc.

### Strengths
* S1: The presentation of this paper is straightforward and clear.

* S2: The proposed fusion approach with Q-former (architecture) and modality-sequential training (training recipe) are both reasonable and looks simple for other researchers to follow.

* S3: The evaluation covers various domains, including audio, point clouds, optical flows, etc. The approach CREMA has demonstrated competitive performance across these scenarios, especially when the number of modalities is large.

### Weaknesses
 * W1: This paper lacks sufficient quantitative or qualitative analysis on why multi-modality assists the model. For example, the MUSIC-AVQA performance in Table 1 can benefit from depth and surface normal information, which is not very intuitive. Therefore, some visualizations or other formats of analysis the authors see fit will greatly enhance the motivation here. I saw Figure 3 and the analysis provided by the authors. However, it is unclear whether the learned Q-former indeed considers these modalities, as indicated by Sec. B.7. Since the author uses self-gate to fuse the modalities, is it possible to analyze the model's reliance on certain modalities with attention scores?

* W2: Following the previous point, the increased number of trainable parameters with more modalities makes it complicated to confirm whether the additional modalities are indeed helpful. For example, adding depth and normal information increases the trainable parameters from 9M to 38M. This raises concerns that the performance gains might be attributed to the increased model capacity rather than the effective use of the new modalities themselves. A more controlled experiment, perhaps by varying the parameter count of the unimodal model, would be needed to isolate the impact of the modalities.

### Questions
* Q1: Why CREMA is called a video-language model? For example, SQA3D mainly uses RGBD as input, and the authors call CREMA a video-language model because the visual information is formatted as a video sequence.

* Q2: Although the authors have compared the trainable parameter number, it is arguable what is the number of total parameters, as LORA is used. The questions is: what is the total number of parameters, and what is the speed of inference?

* Q3: It is interesting to see that modalities of depth or surface normal are used, or even helpful, for MUSIC-AVQA and NExT-QA. I suggest the authors provide analysis or visualizations of how such modalities benefit the models.

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
5

### Summary
The paper proposes CREMA, a flexible and efficient framework for video-language reasoning that incorporates multiple modalities, including optical flow, audio, thermal maps, and 3D point clouds. CREMA addresses the limitations of current multimodal models that require extensive parameters and fixed modality inputs by introducing a modular, parameter-efficient design. This framework allows seamless integration of new modalities while reducing computational costs, validated by superior performance on seven diverse reasoning tasks compared to baseline models.

### Strengths
This paper introduces CREMA, a novel, parameter-efficient framework that enables the seamless addition of new modalities without altering the core architecture—a significant advantage over existing models like BLIP-2 and SeViLA, which rely on fixed modality inputs and require extensive parameters. CREMA effectively integrates diverse modalities, such as 3D, thermal, and audio data, by projecting them into a unified representation space interpretable by the model for reasoning.

Key architectural innovations, including self-gated multimodal query fusion and sequential modality training, bring practical improvements to multimodal reasoning tasks, particularly in video-language applications. CREMA demonstrates broad applicability and efficiency across seven video-language reasoning tasks, achieving notable accuracy gains in VideoQA and 3D reasoning. Through reductions of over 90% in parameter requirements and optimizations like modality-sequential training and adaptive early exit, CREMA marks a significant advancement in multimodal reasoning, validated through extensive fine-tuning and zero-shot evaluations.

### Weaknesses
●  Prioritizing certain modalities as primary lacks quantitative backing, which could benefit from sensitivity analysis to validate this design choice across diverse tasks.

●  The Q-Former generates fixed-length tokens for each modality to extract the most informative features and remove any irrelevant information. However, this fixed-length constraint could risk omitting valuable details, particularly in modalities with high information density. The claim that the Q-Former removes irrelevant information remains qualitative, lacking concrete evidence of how this process is achieved and what specific types of information are discarded.

●  The decomposition of back-propagation by modality, while efficient, may limit the model’s ability to fully capture interactions between modalities, impacting the quality of multimodal reasoning.

### Questions
●Q1: In Line 177, the paper states that the Q-Former "extracts the most informative features from the input modality and removes any irrelevant information" by generating fixed-length tokens. However, the fixed-length constraint may risk omitting crucial details, particularly for modalities rich in information. To substantiate the claim of extracting only the most informative features, it would be beneficial to include empirical evidence or an ablation study comparing different token lengths and their impact on performance across modalities. 

●Q2: In Lines 194-195, the authors mention adding a fully connected layer (shown as a dashed box in Figure 1) for each data type when dimension misalignment occurs. Could you clarify why a fully connected layer was chosen over a potentially lighter-weight approach like interpolation? A fully connected layer seems more computationally intensive, so I am curious about the specific advantages it offers in this context. To clarify the advantages of this design choice, it would be helpful for the authors to provide a brief comparison, perhaps in terms of computational cost and performance, with lighter-weight options such as interpolation. 

●Q3: In Line 233, the authors select video queries as the "major" modality, with other modalities as "supportive," explaining this choice as mirroring human perception in video reasoning tasks. Could you clarify the rationale behind prioritizing video in this way? Additionally, was a sensitivity analysis conducted to verify the impact of this design choice? I am curious whether this prioritization consistently benefits performance across tasks or if certain scenarios might require a different modality emphasis. To support this prioritization, the authors could consider presenting results from ablation studies or sensitivity analyses across various tasks and modality combinations, demonstrating whether prioritizing video consistently enhances performance or if other scenarios might benefit from different modality emphasis. 

● Q4: In Line 259, the authors describe decomposing the back-propagation process for different modalities in each iteration. Could this approach limit the model’s ability to capture interactions between modalities, which is critical for vision-language tasks? It seems more like a trade-off for efficiency rather than a true remedy, as mentioned. This decomposition may prevent the model from fully learning cross-modal interactions and effectively fusing information across modalities. Could you clarify this design choice and its potential impact on performance?

● Q5: In Line 456, the paper mentions achieving a 'regularization effect on the model through parameter-efficient updates.' Could you elaborate on the specific mechanisms or components within CREMA that contribute to this regularization effect? Additionally, how does this approach enhance model generalization across various modalities?

● Q6: Could CREMA also accommodate remote sensing imagery as an input modality? Remote sensing images, captured from satellites or drones, provide detailed information on Earth’s surface across multiple spectral bands. If CREMA can process this type of data, would specific adaptations be needed to handle its unique spatial and spectral characteristics?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presents a multi-modal LLM pipeline CREMA to joint learning from different modalities: visual, depth map, optical flow, audio etc that are synchronized with a video input. Built on top of existing multimodal encoders and LLM, it proposes modal-specific queries and a modality fusion module to incorporate inputs from different modalities while keeping a low trainable parameter scale. The model is evaluated on tasks require multimodal inputs: audio-video QA, 3D situated QA, touchQA/thermal QA etc. It outperforms existing methods that are using the multimodal inputs such as OneLLM and 3D-LLM.

### Strengths
-	The proposed model is a general framework for language QA based on multimodal video inputs. It achieves impressive performance on a wide range of tasks: audio-video QA, 3D situated QA, touchQA/thermal QA etc. 
-	Some ablation studies are conducted for the choice and early exit strategy and modality fusion method (Table 7&8).

### Weaknesses
 - The performance of the proposed model seems to be dependent on the used multimodal encoders (ZoeDepth, Unimatch, NLL-AngMF to estimate depth, flow, normal, BEATs to encode audio, and ViT-G to encode visual). The comparison to existing methods might be unfair due to different encoders are used. More explanations are needed to verify this.
- The overall novelty is limited. The proposed model-specific queries and modality fusion module are subtle technical changes that does not bear a strong novelty.

### Questions
-  Motivation behind adaptive early exit is not clear. The equation used on line 284 says if the gradient for a modality is larger than a threshold, then it will exit training. Shouldn’t it be smaller than a threshold since the gradient scale will be small after convergence?
- Why using a sigmoid function in the fusion module in equation (3)? Seems it only does a scaling to the original q^{\bar}_\V which may not be necessary

### Soundness
2

### Presentation
3

### Contribution
2
