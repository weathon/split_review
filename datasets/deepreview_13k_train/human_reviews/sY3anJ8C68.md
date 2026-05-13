# Efficient Masked AutoEncoder for Video Object Counting and A Large-Scale Benchmark

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
The dynamic imbalance of the fore-background is a major challenge in video object counting, which is usually caused by the sparsity of foreground objects. This often leads to severe under- and over-prediction problems and has been less studied in existing works.
To tackle this issue in video object counting, we propose a density-embedded Efficient Masked Autoencoder Counting (E-MAC) framework in this paper. 
To effectively capture the dynamic variations across frames, we utilize an optical flow-based temporal collaborative fusion that aligns features to derive multi-frame density residuals. 
The counting accuracy of the current frame is boosted by harnessing the information from adjacent frames.
More importantly, to empower the representation ability of dynamic foreground objects for intra-frame, we first take the density map as an auxiliary modality to perform $\mathtt{D}$ensity-$\mathtt{E}$mbedded $\mathtt{M}$asked m$\mathtt{O}$deling ($\mathtt{DEMO}$) for multimodal self-representation learning to regress density map.
However, as $\mathtt{DEMO}$ contributes effective cross-modal regression guidance, it also brings in redundant background information and hard to focus on foreground regions. To handle this dilemma, we further propose an efficient spatial adaptive masking derived from density maps to boost efficiency.
In addition, considering most existing datasets are limited to human-centric scenarios, we first propose a large video bird counting dataset \textit{DroneBird}, in natural scenarios for migratory bird protection.
Extensive experiments on three crowd datasets and our \textit{DroneBird} validate our superiority against the counterparts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a large video bird counting dataset DroneBird, in natural scenarios for migratory bird protection. In addition, an efficient masked autoencoder for video crowd counting framework is proposed. Specifically, to integrate the foundational model and take the density map as an auxiliary modality to perform self-representation learning, a density-embedded efficient masked autoencoder counting framework is proposed. Moreover, the authors propose an efficient spatial adaptive masking method to overcome the dynamic density distribution and make the model focus on the foreground regions. Extensive experiments on three crowd datasets and our DroneBird validate the effectiveness.

### Strengths
Strengths:
- A large bird video counting dataset is proposed, which is helpful for bird activities analysis;
- Applying masked authencoding learning for video crowd counting, which is interesting;
- The proposed approach achieves SOTA video counting performance on several benchmarks, especially for the proposed bird dataset;

### Weaknesses
Weaknesses: 
- Ambiguous performance gains: The proposed approach integrates a masked autoencoder for representation learning and formulates the previous density regression task as "density reconstruction" within an MAE-like framework for crowd counting. Additionally, the authors use the pre-trained ViT-B from MultiMAE as the encoder for discriminative feature extraction. However, given that pre-trained MAE models typically lead to significant performance improvements during downstream task fine-tuning, it remains unclear whether the observed performance gains stem from the designed new masked autoencoder-based framework or the usage of pre-trained MultiMAE. One suggestion: compared w/ a variant w/o using the pre-trained ViT;
- For the proposed Temporal Collaborative Fusion, it is unclear why we need to calculate $\hat{D}_{t}^{res}$ again after obtaining $\hat{D}_{t}$ and $\hat{D}_{t-1}$ from the decoder. If $\hat{D}_{t}$ and $\hat{D}_{t-1}$ are not accurate enough, then $\hat{D}_{t}^{res}$ calculated using them will also be inaccurate. Conversely, if $\hat{D}_{t}$ and $\hat{D}_{t-1}$ are accurate, there seems to be no need for the Temporal Collaborative Fusion module.
- A comparison of model complexity with the other approaches in Table 1 should be provided to ensure a fair evaluation, as the current work may use a relatively larger model.

### Questions
- One open question: As we all know that MAE pre-training can improve many downstream task fine-tuning. For video crowd counting, does the current approaches also benefit from the MAE pre-trained models (e.g., MAE ViT-base)? i.e., using them as the initialization weights for video counting fine-tuning.

As mentioned in the Weaknesses, my main concerns lie in the ambiguous performance gains and methodology design. Since the proposed approach uses the pre-trained MultiMAE model and jointly follows a masked autoencoder framework for fine-tuning, it is not clear whether the performance improvements stem from the pre-trained model or downstream masked fine-tuning with the designed framework from the authors.  I would like to see the author rebuttal in terms of this part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents a method and a new dataset for video object counting. The model performs well in multiple object-counting benchmarks using video as input.

### Strengths
- A video object counting benchmark, Dronebird, is established.
- A corresponding object counting method to deal with video data is proposed.

### Weaknesses
Many descriptions are not inconsistent, making it difficult to understand the paper. See Questions.

- In video counting, how is the count of a video defined? Is it the average count of objects, or the number of different instances that appear in the video?
- The TCF module presented in Fig. 2 is inconsistent with the corresponding description. In Eq. (1), the product of the "warp" operator is added to $\hat{D}_t$ to generate $\hat{D}_{\text{fuse}}$, and the "warp" operation involves $\hat{D}_t$. In the description, a cross-attention is applied to generate $\hat{D}_t^{\text{res}}$, which is then combined with $\hat{D}_t$ to produce $\hat{D}_{\text{fuse}}$. In Fig. 2, the generation of $\hat{D}_t^{\text{res}}$ does not involve $\hat{D}_t$ according to the arrows that demonstrate the data flow.
- In Eq. (2), $\mathbf{T}_D \in \mathbb{B}^{B \times \mathcal{N}_D \times C}$ is a token set including vectors. How are these vectors sorted?
- The description of SAM is also different from that in Fig. 2. The description takes the ground truth $D_t$ to mask tokens, while SAM in Fig. 2 involves $I_{t-1}$, $D_{t-1}$, and a random mask, which does not appear in Sec. 4.3.
- During training, $\mathbf{S}_t = \{I_t, D_t\}$ contains the input image and GT labels. How does the model work in inference, without GT as input?

### Questions
- In video counting, how is the count of a video defined? Is it the average count of objects, or the number of different instances that appear in the video?
- The TCF module presented in Fig. 2 is inconsistent with the corresponding description. In Eq. (1), the product of the "warp" operator is added to $\hat{D}_t$ to generate $\hat{D}_{\text{fuse}}$, and the "warp" operation involves $\hat{D}_t$. In the description, a cross-attention is applied to generate $\hat{D}_t^{\text{res}}$, which is then combined with $\hat{D}_t$ to produce $\hat{D}_{\text{fuse}}$. In Fig. 2, the generation of $\hat{D}_t^{\text{res}}$ does not involve $\hat{D}_t$ according to the arrows that demonstrate the data flow.
- In Eq. (2), $\mathbf{T}_D \in \mathbb{B}^{B \times \mathcal{N}_D \times C}$ is a token set including vectors. How are these vectors sorted?
- The description of SAM is also different from that in Fig. 2. The description takes the ground truth $D_t$ to mask tokens, while SAM in Fig. 2 involves $I_{t-1}$, $D_{t-1}$, and a random mask, which does not appear in Sec. 4.3.
- During training, $\mathbf{S}_t = \{I_t, D_t\}$ contains the input image and GT labels. How does the model work in inference, without GT as input?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents the E-MAC framework, which addresses the dynamic imbalance of fore-background in video object counting through density-embedded Efficient Masked Autoencoder Counting. By leveraging optical flow-based temporal collaborative fusion, E-MAC aligns features across frames to improve counting accuracy. The approach introduces Density-Embedded Masked Modeling (DEMO) to enhance intraframe representation of dynamic foreground objects. To mitigate redundant background information, an efficient spatial adaptive masking derived from density maps is employed. Additionally, the paper introduces DroneBird, a large-scale bird counting dataset for migratory bird protection, showcasing the framework’s effectiveness in natural scenarios and validating its superiority through extensive experiments on three crowd datasets.

### Strengths
1.The efficient spatial adaptive masking method adeptly handles dynamic density distribution, ensuring focus on foreground regions and tackling the imbalance of fore-background effectively.

2.Introduction of the DroneBird dataset, the first video bird counting dataset, significantly broadens the application domain, demonstrating the framework’s versatility and impact through extensive validation against competing methods.

### Weaknesses
1.The manuscript lacks visual analyses of the three key components, which would illustrate the targeted effectiveness of each module.

2.It is recommended to provide code or critical sections of the code for review to enable thorough evaluation of the methodology and results.

### Questions
1.In Table 1, do the compared methods use the same backbone network (ViT-B) as this paper's method? If not, please specify the reasons.

2.Why does the proposed method show higher RMSE on the VSCrowd dataset compared to GNANet in Table 1?

### Soundness
3

### Presentation
2

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
1. This paper addresses video object counting by introducing the DroneBird dataset for bird-counting scenarios and proposes a masked autoencoder-based counting framework.

2. The framework uses optical flow for temporal alignment and density maps for spatial focus to improve counting performance.

3. While each component is technically feasible, they lack integration to showcase a comprehensive advantage for crowd counting as a whole.

4. The dataset offers potential application value, though its academic innovation and contribution remain to be further substantiated.

### Strengths
1. Introduces a novel bird-counting dataset, DroneBird, captured from a drone’s perspective. 

2. Proposes optical flow-guided Temporal Collaborative Fusion (TCF) to extract temporal information from adjacent frames, enhancing object counting accuracy.

3. Integrates Density-Embedded Masked Modeling (DEMO), using density maps as an auxiliary modality with image data, helping balance foreground and background in the model.

4. Employs Spatial Adaptive Masking (SAM) to focus on foreground areas, potentially improving model efficiency and counting accuracy.

### Weaknesses
1. The methodology's components (such as DEMO, SAM, and TCF) lack cohesive integration, appearing independently implemented without clearly demonstrated necessity for crowd counting.

2. Although DroneBird introduces a new category, the dataset’s difficulty and uniqueness are not strongly evident, and it lacks clear differentiation in research value compared to existing datasets beyond adding a bird-counting scenario.

### Questions
**Questions:**

1. In Table 1, video-based methods underperform image-based methods on the DroneBird dataset. What might be the reasons for this discrepancy, and could this be further elaborated?
  
2. Optical flow is typically more effective for capturing dynamic objects in scenes with a static camera. In the drone viewpoint of DroneBird, how does the model address the challenge where all objects in the field of view are in motion? Particularly, TCF’s improvements are minor according to the ablation study—how might this be explained?

3. How is Exp. III in Table 2 implemented? Given my understanding, SAM’s application without DEMO may lack practical relevance—how does it contribute in the absence of DEMO?

4. Could you further articulate the scientific value of DroneBird, especially in terms of the new challenges it introduces for video-based research? Specifically, what novel research questions or difficulties does it bring?

### Soundness
4

### Presentation
4

### Contribution
4
