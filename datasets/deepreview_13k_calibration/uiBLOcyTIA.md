# NEXTLOCLLM: NEXT LOCATION PREDICTION USING LLMS

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Next location prediction is a critical task in human mobility analysis and serves as a foundation for various downstream applications. 
Existing methods typically rely on  discrete IDs %embedding tables 
to represent locations, which inherently overlook spatial relationships and cannot generalize across cities.
In this paper, we propose NextLocLLM, which 
leverages the advantages of large language models (LLMs) in processing natural language descriptions and their strong generalization capabilities for next location prediction.
Specifically, instead of %adopting IDs%embedding tables
using IDs, NextLocLLM  encodes locations based on continuous spatial coordinates to better model spatial relationships.
These coordinates are further normalized to enable robust cross-city generalization.
Another highlight of NextlocLLM is its LLM-enhanced POI embeddings.
It utilizes LLMs' ability to encode each POI category's natural language description into embeddings.
These  embeddings are then integrated via nonlinear projections to form this LLM-enhanced POI embeddings, effectively capturing locations' functional attributes.
 Furthermore, task and data prompt prefix, together with trajectory embeddings, are incorporated as input for  partly-frozen LLM  backbone.
NextLocLLM further introduces prediction retrieval module to ensure structural consistency in  prediction.
 Experiments show that NextLocLLM outperforms existing  models in next location prediction, excelling in both supervised and zero-shot settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents NextLocLLM, a model designed to predict the next location by enhancing the extraction of spatial relationships and improving generalizability across different cities using a large language model (LLM) approach. First, NextLocLLM employs normalized spatial coordinates to represent discrete locations, accurately modeling spatial relationships and bypassing location ID inconsistencies across cities. Second, the model integrates LLM-enhanced POI category information, which captures functional attributes of locations more effectively. Finally, NextLocLLM leverages a KD-tree to convert output coordinates into the top-k most likely predicted locations, thereby incorporating neighborhood spatial relationships into the prediction process.

### Strengths
S1. Unlike other methods that rely solely on location IDs for prompt design, NextLocLLM focuses on spatial relationships and semantic embeddings derived from natural language descriptions of POI categories. By using spatial coordinates, the model gains a deeper understanding of spatial relationships between locations, enhancing transferability and generalization across diverse urban environments.
S2. The authors conduct extensive experiments with various models and baselines. These experiments are comprehensive, covering four datasets and demonstrating strong performance in both supervised and zero-shot settings.
S3. The paper is well-written and easy to follow.

### Weaknesses
W1.  Ablation studies to assess whether using spatial coordinates provides a clear advantage over location IDs is missing.
2. The paper does not include a detailed description of raw trajectory processing. For instance, there is no clarification on determining the length of historical and current trajectories or whether noisy points in the raw trajectory data are filtered out.
3. The paper could benefit from further analysis on which specific design modules contribute to the zero-shot capability of NextLocLLM and why it outperforms other LLM-based methods.

### Questions
Q1. How is the frequency of each POI category within a location calculated?
Q2. In fully-supervised scenarios, such as for training methods like DeepMove, is the same data used as with NextLocLLM? Additionally, are the POI category and stay duration included as training data for DeepMove?

### Soundness
2

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
5

### Summary
This article proposes a novel method for next location prediction based on fine-tuning large language models.

### Strengths
1. Well written, clear structure, easy to understand.

2. Proposed a series of key insights to enhance the adaptation of LLM in the next location prediction task.
   - Applying *Spatial Coordinate Normalization* to unleash LLM's cross-city generalization ability
   - Proposing *LLM-enhanced POI Embedding* to integrate diverse functional attributes of regions.
   - Predicting spatial coordinates as intermediate results, then using KD-tree retrieval for top-k locations, which is a **rather smart idea** that not only retain the generalization ability brought by coordinate prediction itself, but also is compatible with classic problem definition (Next **Location ID** prediction).

3. Conducted sufficient ablation study to demonstrate the importance of each module.

### Weaknesses
1. The **model parameters** and **configurations** are **completely lacking** in introduction.
     - **Basic training parameters**: learning rate, batch size, optimizer, etc.
     - **Key hyperparameters**: the dimension of $d_{llm}$, etc.
     - **Model Input**: Length of historical and current trajectories.
     - **LLM Tokenizer and LLM Token Embedding Layer**: Which models/methods are used for?
  
2. **Lack of sensitivity analysis on hyperparameters**.
   Although the authors conducted a complete ablation study demonstrating the key roles of each module, it is still necessary to conduct corresponding sensitivity analysis on key parameters, such as the embedding dimensions and the number of LLM layers, to demonstrate the robustness of the model. Specifically, it is important to understand how performance varies with different settings of these parameters, and whether the chosen values are optimal.

3. The overlooked issue of **computational efficiency**.
Inference efficiency of LLMs has always been a critical issue. The proposed model not only requires using *pre-trained LLM as the backbone network* but also needs to use *LLM encoding POI information and prompt prefix*. Therefore, I am very concerned about the computational efficiency issues of the proposed method, including training and inference time as well as resource utilization. I hope that the authors can report on this point and compare it with baselines. It is acceptable that the computational efficiency is not good for an ICLR paper, but it is better to discuss the drawback (if have)

### Questions
Q1. Why is the NextlocLLM model labeled as a **white box model** in Figure 1(c)? I did not find any evidence in this paper to support this claim.

Q2. In the conclusion section, the authors mentioned that the *geographical distance error remains a challenge*, and maybe further reducing the grid size can mitigate this? The current study used a grid size of 500m x 500m for location prediction. I would like to know how grid size affects accuracy.

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
4

### Summary
The paper proposes a novel LLM-based framework, NextLocLLM, for next-location prediction. By integrating trajectory and POI data with a fine-tuned LLM, the framework aims to enhance prediction accuracy. The primary components include spatial coordinate encoding for better spatial representation, LLM-enhanced POI embeddings capturing functional location attributes, and a prediction retrieval module to provide top-k predictions.

### Strengths
• Innovative Framework: The use of LLM for next-location prediction is a key improvement, as it integrates semantic POI information, which is not fully leveraged by traditional methods.
•  Extensive Experiments: The authors present comprehensive experiments validating the model's performance across various datasets, demonstrating its robustness.
•  Clarity: The paper’s structure is well-organized, making the methodology clear and accessible.

### Weaknesses
• Innovation Concerns: The core contribution, POI information embedding, appears somewhat incremental since it aligns with previous works' embedding logic but integrates this with LLM-based representation.
•  Contribution of KD-tree: The KD-tree application is commonplace in traffic scenarios, particularly with GNN-based models, and thus may not qualify as a novel contribution.
•  Model Architecture Innovation: There appears to be limited innovation in the model structure. I would appreciate a discussion with the authors to ensure I am not overlooking any novel aspects.
•  Case Studies in Experiments: The inclusion of case studies could bolster the practical applicability of the framework by demonstrating real-world scenarios.
•  Minor Errors: Minor errors, such as in Equation 9, should be corrected for accuracy.

### Questions
Please refer to weakness. In addition, I hope the author can give an intuitive analysis of why the LLM-based model performs better. And what aspects of the design the author thinks are most effective, for example, the prompt prefix.

### Soundness
3

### Presentation
3

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
This paper addresses a significant research question concerning model transferability across different cities and introduces NextLocLLM, which integrates large language models (LLMs) with next location prediction models. The method incorporates multi-dimensional trajectory content embeddings, LLM-enhanced POI embedding, an LLM backbone, and a prediction retrieval module, purportedly achieving state-of-the-art (SOTA) results in both fully supervised and zero-shot settings. Despite these claims, the experimental design, framework rationale, and methodological clarity are not convincing enough, leading me to lean towards rejection.

### Strengths
1. The paper tackles the crucial issue of model transferability across urban settings, a topic of growing importance in location-based services.
2. This paper demonstrates improvements in performance, achieving state-of-the-art results in both fully supervised and zero-shot next location predictions.
3. This paper innovatively integrate multiple data sources, including points of interest (POI), textual descriptions, and trajectory data, enriching the model’s contextual understanding.

### Weaknesses
1. The experiments are not solid. For example, 1) why using LLaMA2 and LLaMA3 does not outperform GPT2. The paper does not adequately address the counterintuitive result that larger, more capable LLMs like LLaMA2 and LLaMA3 underperform GPT2. This raises concerns about the suitability of the chosen LLM architecture and the overall framework design. 2) It seems that the proposed KD-Tree-based prediction contributes, but you did not involve it in the experiments. The paper fails to isolate the contribution of the KD-tree, making it unclear if the reported state-of-the-art (SOTA) performance is due to the proposed framework or the KD-tree. 3) In the ablation study, only using LLM-enhanced POI achieves the second-best result. It challenges the significance of the proposed methods. The ablation study results, where LLM-enhanced POI alone performs nearly as well as the full model, undermine the necessity of the other components. In addition, it is weird that using both POI and LORA will lead to worse performance than pure POI. The performance degradation when combining POI and LoRA raises questions about the interaction between these components and the overall model design.

2. This framework seems not reasonable. This work aims to achieve generalization ability by LLM. However, I am wondering whether this ability can be achieved without road graph. It seems that this paper aim to realize zero-shot generalization with purely POI even without trajectory. The paper's claim of achieving zero-shot generalization using only POI information, without explicit road network information, is questionable. The reliance on POI data alone for generalization is not well-justified, particularly given the importance of road networks in mobility modeling.

3. The formalization is a little bit confusing. TI=\{(d,t)\} and t is time-of-day (0 ≤ t ≤ 23 in hours). Since Taxi data seem to be less than an hour. This formalization seems not complete. The formalization of the time component 't' as the hour of the day is not sufficiently detailed, especially considering that taxi trip data often has a finer granularity than one hour. The lack of clarity in how sub-hourly data is handled raises concerns about the completeness of the formalization.

### Questions
Please explain the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
