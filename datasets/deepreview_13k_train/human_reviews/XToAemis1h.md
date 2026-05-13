# Learning Unified Static-Dynamic Representation across Multiple Visuo-tactile Sensors

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
Visuo-tactile sensors aim to emulate human tactile perception, enabling robots to precisely understand and manipulate objects. Over time, numerous meticulously designed visuo-tactile sensors have been integrated into robotic systems, aiding in completing various tasks. However, the distinct data characteristics of these low-standardized visuo-tactile sensors hinder the establishment of a powerful tactile perception system. We consider that the key to addressing this issue lies in learning unified multi-sensor representations, thereby integrating the sensors and promoting  tactile knowledge transfer between them. To achieve unified representation of this nature, we introduce TacQuad, an aligned multi-modal multi-sensor tactile dataset from four different visuo-tactile sensors, which enables the explicit integration of various sensors. Recognizing that humans perceive the physical environment by acquiring diverse tactile information such as texture and pressure changes, we further propose to learn unified multi-sensor representations from both static and dynamic perspectives. By integrating tactile images and videos, we present UltraTouch, a unified static-dynamic multi-sensor representation learning framework with a multi-level structure, aimed at both enhancing comprehensive perceptual abilities and enabling effective cross-sensor transfer. This multi-level architecture captures pixel-level details from tactile data via masked modeling and enhances perception and transferability by learning semantic-level sensor-agnostic features through multi-modal alignment and cross-sensor matching. We provide a comprehensive analysis of multi-sensor transferability, and validate our method on various offline datasets and in the real-world pouring task. Experimental results show that our method outperforms existing methods, exhibits outstanding static and dynamic perception capabilities across various sensors.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The author introduces an aligned multi-sensor tactile dataset to unify tactile data. The data across four optical-based sensors. Also, the author proposes a unified static-dynamic multi-sensor representation learning. The author also implements real world experiments to test their framework.

### Strengths
(1) The idea of aligned multi-sensor dataset, improve generalization across different sensors.
(2) Capturing both static and dynamic tactile features. This is novel to make the system have comprehensive tactile information understanding.
(3) The dataset labeling process involves language model. This could improve the efficiency of the dataset collection.
(4) Using t-SNE visualization is clear to show the impact of components on representation space.
(5) I recognize the authors' effort to collect large volume dataset of tactile

### Weaknesses
Major Weaknesses:
1. Although the author's idea of the aligned multi-sensor dataset, the author focuses to optical-based tactile sensors only, which simplifies the problem with similar tactile modalities(tactile image). The exclusive focus on optical-based sensors neglects the diversity of tactile sensing modalities, such as capacitive, resistive, or piezoelectric sensors, which offer different data characteristics and could provide a more comprehensive understanding of tactile perception. This limits the generalizability of the proposed framework to a broader range of tactile sensing applications.
2. In sec 5.2, the conclusion of the material classification task seems contradict to the motivation to build the aligned multi-sensor dataset. The reported performance degradation when incorporating more sensor data into the material classification task raises concerns about the effectiveness of the proposed multi-sensor representation learning approach. The fact that using only GelSight data yields the best performance suggests that the method may not be effectively leveraging the information from other sensors, potentially due to domain shift or inadequate feature alignment.
3. The experiment results are not convincing in Section 5.5. The performance of the proposed method on the real-world pouring task is not clearly superior to existing methods, and the reported mean error metric lacks sufficient detail to fully understand the task's complexity and the model's performance. The absence of a clear baseline comparison makes it difficult to assess the true contribution of the proposed approach.
4. Some components of methods are not proved effective in the experiment. The lack of a thorough ablation study to demonstrate the contribution of each component of the proposed method makes it difficult to assess the necessity and effectiveness of each part. The absence of analysis on the impact of different components on the overall performance makes it difficult to understand the model's behavior.
4. No limitations and future work are described in the main paper.

Minor Weaknesses:

1. The presentation needs to be improved. Readers may get confused for some point before reading the supplementary material

2. The author use too many colors to represent different sensor types in the main text, which may not be good for reading.

3. Some conclusions according to experiment results are not reasonable.

### Questions
1. For those four types of sensors, how many sensors you chose for each type? This is important because the tactile image can be very different even the same types of sensor. The dataset could be more diverse if more sensors for each type are used.

2. [line 189]. The author mentions that collecting fine-grained aligned tactile data is very costly. Please specify the reasons.

3. [line 431]. Incorporating data from more sensors leads to a performance drop. This may potentially reflect the robustness of the mode is not good enough. Using a single sensor for each type may hard to extract effective features of this type of sensor and only focus on some specific details of a single sensor.

4.[line 488-498] The performance of UniTouch and UltraTouch is similar, it is hard to claim the advantages of the current method.

5. Please mention real-world tasks in more detailed in the main paper. The reader will be confused about the task and the meaning of "mean error" before reading the appendix.

6. It would be better if the author have experiments to prove the effectiveness of the text in this dataset. 

7. [line 450-453] Please explain more details for this.

### Soundness
3

### Presentation
3

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
This paper proposes UltraTouch, a model that learns unified static-dynamic representations for multiple tactile sensors with different architectures. To train UltraTouch, a dataset called TacQuad is introduced by collecting multimodal data from four different tactile sensors. UltraTouch captures both pixel-level and semantic-level features, which are shown to be transferable and effective through experiments on multiple downstream tasks.

### Strengths
1. The collected dataset TacQuad, especially the fine-grained spatio-temporal aligned data can be a significant contribution to the community of tactile sensing. None of the prior works has collected tactile videos with shared speed and depth using multiple sensors. Although not fully explored in this work, I think this dataset and its data collection program will potentially benefit future research if being available to public.

2. The proposed UltraTouch framework, to the best of my knowledge, is the first model that learns the dynamic tactile representations through pretraining. This is a considerable improvement upon the prior works that learn unified tactile representations, which are all limited to static images. Future works that leverage touch for fine-grained manipulation tasks can potentially benefit from this framework.

3. The performance of UltraTouch model on the existing material classification/ grasp stability prediction seems promising, which is outperforming the previous pretraining frameworks significantly in most experiments. 

4. The proposed real-world pouring task demonstrates the effectiveness of learning dynamic representations (Table 4).

### Weaknesses
1. As is shown in A.4, only 3 frames are used for each tactile video clip. This seems to be a surprisingly small number of frames, and my concern is that this might not be sufficient for extracting some of the fine-grained tactile information (e.g., hardness, texture variations during sliding). The temporal context captured with only 3 frames might be too limited to model complex dynamic interactions. One possible ablation experiment would be training the model with different video lengths (e.g., 5, 7, or 10 frames) and evaluating the performance on downstream tasks that require temporal understanding. This would help to quantify the impact of the input video length on the model's ability to capture dynamic tactile information.

2. The paper proposes a novel calibration platform for collecting fine-grained spatio-temporal aligned data, and they claim that this can be used for fine-grained tasks such as cross-sensor generation. However, it seems that they don't explore much on the potential of this data. Most of the downstream tasks are performed on static perception, and the only pouring task, while demonstrating dynamic representation, does not directly leverage the fine-grained alignment. It would be interesting to see if the fine-grained alignment can be used for tasks such as generating high-resolution tactile images from low-resolution sensors or predicting the force distribution on one sensor based on the readings of another, which could better showcase the value of the proposed calibration platform and the fine-grained data.

### Questions
1. Referring to my first concern in Weaknesses section, I'm curious about the computational cost of training with tactile videos. It's common that the frame rate of the video being limited due to data loading/ computation limits, but only using 3 frames still seems too few to me. My guess is that using more frames may lead to better dynamic perception ability, and I'm wondering if an ablation experiment on this parameter can be possible?

2. Besides TacQuad, some of the other datasets also contain tactile videos, such as TAG and OF Real. I wonder if they are already treated as videos during the training of UltraTouch, if not, maybe it can further improve the model performance if they are used as videos.

3. I'm curious about the scalability of the calibration platform used for data collection. Is it easy for other researchers to build a similar platform to scale up the current dataset?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel and comprehensive representation learning framework for tactile data that addresses (1) V-T-L modalities alignment, (2) capturing dynamic information in tactile modality, and (3) generalization across different sensors together. It constructs a multi-sensor dataset called TacQuad and a 2-stage multi-task representation learning framework, equipped with pixel-level MAE, semantic-level multi-modal alignment, and cross-sensor matching techniques. With extensive experiments, the authors show this representation helps in some downstream tasks under various settings (seen and unseen sensors, different training dataset combinations, and real robot experiments).

### Strengths
1. Well-motivated and well-written. Authors observed the difference between tactile sensing and vision, and creatively designed corresponding modules to enhance the representation. 

2. Clear visualization. Fig 2 works as a nice abstract of the entire framework.

### Weaknesses
1. In Tables 2 and 3, the average performance of the TAG+Feel+YCB-slide+OF 2.0 model is better than the full model with the TacQuad dataset. This observation
  - Questions the necessity of your TacQuad dataset, and
  - Poses a new question: how do you choose the size & scope of the dataset? Contrastive learning has requirements on the dataset size, while too much data will, in turn, make it "lose focus". 

Please add more discussion and experiments on this issue, and figure out either the detailed reason (i.e. which dataset is bad for some reason) or how to find a good combination of datasets. 

2. Given you claimed the model has the ability to extract sensor-agnostic features from unseen sensors, it would be more convincing to show some downstream task performance on the new sensor, aside from qualitatively showing t-SNE visualization.

3. Some other results are not convincing enough as well. In Fig 4 / Sec 5.3, DuraGel samples are better clustered than baselines, but some samples from GelSight and DIGIT, which are previously seen, are far from each other and mixed with other samples. Is it due to some difficulties in tuning the corresponding weight for loss?



### Questions
1. Regarding Fig 7 and 8, is there a significant gap between GPT-4o outputs for OF-Real and TVL/SSVTP, given you didn't use tactile data for the latter? If so, will this affect your training? If not, do you think GPT-4o is making use of tactile input, given it may not be capable of analyzing images from tactile sensors? Can you show some raw output examples?

2. I noticed your "full model" removed Feel and OF 2.0 from the dataset. Is it on purpose? If the full model sees the Feel dataset, will its performance in Table 2 be lower than 80.53, between 80.53 and 82.3, or higher than 82.3? Similarly for OF 2.0. The claim that more is not always better itself is interesting, but I just wonder can it be simply due to the lack of some specific dataset? Your current experiment setting cannot rule out this possibility. 

3. Sec 5.4 explained the performance drop on material classification, but what about grasp? 

4. The tables are a bit hard to read. Is the first row in Table 1 from CLIP as explicitly said in Tables 2 and 3? In Table 2, the colorful detailed dataset configuration makes it hard to find what to compare before carefully reading Sec 5.4. 

Minor:
1. Citation format. Parenthesis missing in lots of scenarios.
2. Line 797 missing space.

### Soundness
2

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
This paper present a novel framework called UltraTouch and a large dataset TacQuad collected using 4 different tactile sensors. The UltraTouch framework has a multi-stage training in pixel level and semantic level. In stage 1, the authors use MAE to train on static and dynamic tactile images/videos. In stage 2, the authors do contrastive learning on multi-modal aligning and cross-sensor matching to understand semantic-level sensor-agnostic tactile properties. The authors also answer research questions by testing on downstream tasks like material classification, grasp prediction, and pouring.

### Strengths
Strengths of this paper includes:

- They collect and open-source a large tactile dataset called TacQuad, which makes good contribution to the multi modal robot learning community since the tactile data are far from enough compared with vision data. 
\
\
- The framework is novel. The idea of learning a unified tactile representation is very interesting and the authors study how tactile aligns with other modalities like vision and text, and how different sensors match with each other. 
\
\
- The experiments are comprehensive. The authors conduct extensive experiments on multiple downstream tasks like material classification, grasp prediction, and pouring, which demonstrate Ultratouch, learning unified representations, has advantages over other models.

### Weaknesses
Weaknesses of this paper include:

- Though vision based tactile sensors are very popular in robot learning community, it might not be the ultimate solution that people agree on. Tactile perception are more than images. Humans feel temperature, texture, shape, vibrations, etc. when interacting with objects. This is still an open question and is out of scope of this paper. But it will be interesting to see if how other tactile sensors align or match with the vision-based tactile sensors.


- I think there can be some study on the effect from the stage 1, the pixel level learning, on the downstream tasks. How does learning the pixel-level details help the downstream tasks? I think material classification and grasp prediction might not need that level of detail to achieve good performance.

- Even though the authors use a calibration platform, the precise localization of contact position in world coordinates across different sensors remains a concern. The method relies on pre-measured relative positions of sensor centers, but this might not fully account for variations in sensor mounting or object geometry, potentially leading to misalignment during data collection.

- The paper does not address the potential for variations in individual sensors of the same type. The pixel-wise difference of DIGIT sensors shown in Fig 7 of [1] highlights this issue. If multiple sensors of the same type were used during data collection, it's unclear how this variability might affect the model's performance, especially given that the sensors may have slightly different responses due to manufacturing variations or other factors.

- Missing space in line 797 between TAG and includes

### Questions
- In data collection process, how do you localize the contact position in world coordinate? How to ensure the contact position is the same for different sensors?

- How many corrections do you have to make when use GPT to generate descriptions? How well does it understand the data?

- Are you using the same sensor throughout the entire data collection process? I feel like most tactile sensors now are not very robust, especially the gel pad, which will degrade over time when it touches objects for too many times. Have you replaced gels during the collection process? Will the data be different after replacement? 

- Even the tactile sensors are of the same type. The difference between each individual sensor is huge. See the pixel-wise difference of DIGIT in Fig 7. in this paper [1]. Combined with my previous question, if you have use multiple sensors of the same type during collection and training, I'm curious how this will affect the performance.

- Missing space in line 797 between TAG and includes

[1] Bhirangi, Raunaq, et al. "AnySkin: Plug-and-play Skin Sensing for Robotic Touch." arXiv preprint arXiv:2409.08276 (2024).

### Soundness
4

### Presentation
4

### Contribution
4
