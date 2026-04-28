# Point Cloud Self-supervised Learning via 3D to Multi-view Masked Leaner

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 3, 6, 8, 8

## Abstract
In recent years, the field of 3D self-supervised learning has witnessed significant progress, resulting in the emergence of Multi-Modality Masked AutoEncoders (MAE) methods that leverage both 2D images and 3D point clouds for pre-training. However, a notable limitation of these approaches is that they do not fully utilize the multi-view attributes inherent in 3D point clouds, which is crucial for a deeper understanding of 3D structures. Building upon this insight, we introduce a novel approach employing a 3D to multi-view masked autoencoder to fully harness the multi-modal attributes of 3D point clouds. To be specific, our method uses the encoded tokens from 3D masked point clouds to generate original point clouds and multi-view depth images across various poses. This approach not only enriches the model's comprehension of geometric structures but also leverages the inherent multi-modal properties of point clouds. Our experiments illustrate the effectiveness of the proposed method for different tasks and under different settings. Remarkably, our method outperforms state-of-the-art counterparts by a large margin in a variety of downstream tasks, including 3D object classification, few-shot learning, part segmentation, and 3D object detection

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes Multiview-ML, a novel 3D representation learning model that solely uses 3D point cloud data as input to reconstruct both the original point cloud and multiple depth images from different viewpoints. 

It leverages a two-stage training strategy with a teacher and student model, and outperforms existing approaches across various downstream tasks.

### Strengths
1. The paper is well-written and easy to follow, presenting good-quality figures.


2. The experimental results look promising.

### Weaknesses
1. The authors mention a limitation in prior work, stating that these methods *"inefficiently require both 2D and 3D modalities as inputs, even though 3D point clouds inherently contain 2D modality through their multi-view properties."* However, the authors provide insufficient evidence or ablation studies to substantiate this claim. Notably, previous works have often utilized only 3D inputs, projecting them into 2D during encoding without requiring both 2D and 3D modalities as explicit inputs. The core issue is not whether 2D is explicitly provided, but whether the method leverages multi-view information effectively, which needs more rigorous justification.


2. The authors mention that the epoch number is 300, while do not specify how these are distributed across each stage. If both stages indeed run for 300 epochs, it raises the question of whether the observed improvement primarily results from an extended training period, which is computationally intensive. The lack of a direct comparison with a single-stage training of the same total epochs makes it difficult to isolate the benefit of the two-stage approach.

3. It is better to demonstrate the individual effectiveness of each component in Table 5. Specifically, the contribution of each loss term (point cloud reconstruction and multi-view depth reconstruction) and the impact of the teacher-student setup should be clearly delineated through ablation studies. This would help in understanding the necessity of each component.

4. The ScanObjectNN and ModelNet40 datasets have reached saturation in point cloud understanding. Additional results on more complex and larger datasets, such as Objaverse, would be valuable. This is crucial for demonstrating the scalability and generalizability of the proposed method to more realistic and diverse 3D data.

5. In Supplementary Table 1, should "Ours (Point-M2AE)" actually be labeled as "Ours (Recon)"?

5. Typos: 'pertaining' on line 396.

### Questions
Please kindly see the weaknesses above.

### Soundness
2

### Presentation
3

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
They first project 3D point clouds to multi-view 2D images at the feature level based on 3D-based pose. Then, they introduce two components: (1) a 3D to multi-view autoencoder that reconstructs point clouds and multi-view images from 3D and projected 2D features; (2) a multi-scale multi-head (MSMH) attention mechanism that facilitates local-global information interactions in each decoder transformer block through attention heads at various scales. Additionally, a two-stage self-training strategy is proposed to align 2D and 3D representations.
The contributions are summarized as follows:
(1) They propose a 3D to multi-view autoencoder that reconstructs point clouds and multi-view images solely from 3D point clouds
(2) They propose a Multi-Scale Multi-Head (MSMH) attention mechanism that integrates local and global contextual information by organizing distinct, non-overlapping local groups at multiple scales within the reconstructed features.
(3) They develop a two-stage training strategy for multi-modality masked feature prediction

### Strengths
They propose a Multi-Scale Multi-Head (MSMH) attention mechanism that integrates local and global contextual information.
They employ a two-stage training strategy for multi-modality masked feature prediction.

### Weaknesses
We think that the paper does not present its designs and motivations clearly

My major concerns are:
(1)The inputs of this model consists of both point clouds and 2D depth images. WWhat is the role of depth images within the model? How do they differ from the rendered images provided by the dataset?
(2)“incorporating both 2D and 3D modalities as input for training is redundant and inefficient.”However, the projection for 2D depth images is time-consuming. Additionally, two-stage training always need much time.
(3)As stated in the abstract, "the input 2D modality causes the reconstruction learning to unnecessarily rely on visible 2D information, hindering 3D geometric representation learning." However, the proposed model also depends on 2D depth images: "These depth images then guide the reconstruction from 3D to 2D." The proposed method does not address or optimize the identified drawbacks.
(4) In the part segmentation experiment, there are no IoU (%) results of each category and visualization results, such as Point-MAE and Point-M2AE. 
(5) In the ablation experiments, there is no experiment conducted with other types of images (e.g., silhouettes, contours) as inputs.
(6)How about the training efficiency and parameters number? Introducing 3D to 2D projection, MSMH, and two-stage training strategy leads to additional training costs. This should also be discussed.

### Questions
My major concerns are:
(1)The inputs of this model consists of both point clouds and 2D depth images. WWhat is the role of depth images within the model? How do they differ from the rendered images provided by the dataset?
(2)“incorporating both 2D and 3D modalities as input for training is redundant and inefficient.”However, the projection for 2D depth images is time-consuming. Additionally, two-stage training always need much time. 
(3)As stated in the abstract, "the input 2D modality causes the reconstruction learning to unnecessarily rely on visible 2D information, hindering 3D geometric representation learning." However, the proposed model also depends on 2D depth images: "These depth images then guide the reconstruction from 3D to 2D." The proposed method does not address or optimize the identified drawbacks.
(4) In the part segmentation experiment, there are no IoU (%) results of each category and visualization results, such as Point-MAE and Point-M2AE. 
(5) In the ablation experiments, there is no experiment conducted with other types of images (e.g., silhouettes, contours) as inputs.
(6)How about the training efficiency and parameters number? Introducing 3D to 2D projection, MSMH, and two-stage training strategy leads to additional training costs. This should also be discussed.

### Soundness
2

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
4

### Summary
The paper focuses on the problem of self-supervised point cloud representation learning and presents a method named Multiview Masked Learner. The method learns 3D representation by first training a 3D to multi-view autoencoder to create informative latent features. Then a student network is trained to predict the latent features from masked point cloud input. The autoencoder is carefully designed so that  it encodes 3D point cloud and decodes both 3D point clouds and the corresponding multi-view projections. Multi-Scale Multi-Head attention mechanism is integrated to increase the expressivity of the features. The resulting 3D representation shows promising results in various point cloud analysis benchmarks including object classification, part segmentation, and object detection.

### Strengths
I would like to summarize the strengths of the submission from the following aspects.
1. The writing is clear and easy to follow. Though some claims are not quite intuitive to me which I will detail later but the overall flow is good.
2. The idea of unsymmetric encoder-decoder design is interesting. Enforcing the autoencoder to decode multiview representations from 3D point cloud only inputs sounds a reasonable way to encourage the multi-view geometric understanding in the learned representations.
3. The figures are quite helpful for presenting the architecture and training flow. 
4. The experiments cover a good range of tasks and the ablation studies also shows the effectiveness of the proposed MSMH attention, the choice of recovering token representations rather than the raw data, and the design of instance-level intra and inter-modality prediction.

### Weaknesses
There are several weaknesses with the submission.
1. I am concerned with the technical novelty. Combining MAE with cross-modal distillation has been explored previously, e.g., as in [1]. Though in [1], images are used rather than projection of point clouds but I think the general framework is quite similar. It seems not quite challenging to replace the images used there with the projection of point clouds. The MSMH attention scheme also looks very similar to the Grouped Vector Attention operation in Point Transformer V2 [2]. The current pipeline seems more like an ensemble of existing techniques.
2. The motivation of the method is not strong enough. I do not see a particularly strong reason to avoid using images during the 3D representation learning stage if the multimodal-based pretraining gives better performance in downstream applications. Notice this line of work does not require images while using the pre-trained 3D backbone. The authors claim that incorporating both 2D and 3D during training is redundant and inefficient but do not provide concrete evidence to back up this claim. The claim from Line 49 to Line 53 also confuses me. I do not understand in what context this discussion happens and what is the key idea the authors want to deliver. In line 90, the authors say that their key insight is “the limited effectiveness of using 2D images as input for 3D geometric learning through MAE”. But doesn’t this suggest that we should develop better ways of using both 2D and 3D modalities instead of aborting the 2D modalities? In my humble opinion, previous works already discovered this and that’s why many works use MAE for the 3D modality and link 2D and 3D modalities through contrastive learning as done in [1].
3. The experiments conducted in the main paper are not comprehensive enough. The compared baselines are not very up-to-date and some more recent baselines are missing. For example, there is no comparison with [3]. Also, it feels very strange to leave important comparisons with ReCon [1] and I2P-MAE to the supplementary. The comparisons with [1] are incomplete in the supplementary with the few-shot classification experiments missing. In [1], experiments are also conducted in the 3D-only pretraining setup, and the results there seem comparable or even better than what is presented in the submission. When it comes to few-shot classification, the submission is not always winning either. In [3], a large collection of images helps further boost the representation quality to another level. This is to say, the presented results in the submission do not seem to be the state of the art as claimed.
4. Some ablation studies can be further improved. For example, what the performance would be if the input modality is 3D and the output modality is 2D? Also, a more detailed analysis of the MSMH design would be helpful for understanding its effectiveness and difference from previous works.

### Questions
1. Can authors better justify the motivation of the work? Especially given the fact that leveraging multimodal data for 3D representation learning is indeed achieving impressive results in many applications.
2. Can authors carefully compare their design differences with [1] and the MSMH design with the Grouped Vector Attention operation in [2]?
3. Experiments-wise, the authors need to provide a more comprehensive comparison with [1] and add comparisons with more recent methods such as [3]. Additional ablation studies would also be helpful.

[1] Contrast with reconstruct: Contrastive 3d representation learning guided by generative pretraining.
[2] Point Transformer V2: Grouped Vector Attention and Partition-based Pooling.
[3] ShapeLLM: Universal 3D Object Understanding for Embodied Interaction.

### Soundness
3

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
This work proposed a 3D to multi-view autoencoder that reconstructs both point clouds and multi-view images. The proposed mutli-scale multi-head attention module provides broader local and global information. Besides, the two-stage training strategy ensures the student model learns well-aligned representations. The extensive experiments show the effectiveness of the proposed method.

### Strengths
1. The manuscript is well-organized and easy to follow. 
2. The experiments are extensive. The proposed method is tested on four tasks and compared with multiple baselines.

### Weaknesses
1. For the task part segmentation and few-shot learning, the proposed method achieved little increase. It would be better if more explanation and analysis can be given.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents a 3D-to-multi-view learner (Multi-View ML) that uses only 3D modalities as input and efficiently captures the rich spatial information in 3D point clouds. Specifically, we first project the 3D point cloud to a feature-level multi-view 2D image based on 3D pose. Then, we introduce two components: (1) a 3D-to-multiview autoencoder that reconstructs point cloud and multiview images from 3D and projected 2D features; and (2) a multi-scale multi-head (MSMH) attention mechanism that facilitates local-global information interaction in each decoder-converter block through different scales of attention heads. Furthermore, a novel two-stage self-training strategy is proposed to align 2D and 3D representations. The proposed method significantly outperforms state-of-the-art methods in a variety of downstream tasks, including 3D classification, part segmentation, and object detection.

### Strengths
1. The methodology section of the paper is quite well written, easy to understand and clearly guided. The four consecutive subsections show the implementation of the proposed method in a somewhat innovative way. It is recommended to add more details, e.g. the questions that follow.
2. In particular, the two-stage training strategy mentioned in the paper, i.e., aligning 2D and 3D representations using a network of teachers and students, is feasible and, moreover, the technique is challenging. The ability to appropriately apply it to multimodal self-supervised learning is a significant contribution, and I do hope that the authors will soon open-source this project for community advancement.
3. The proposed method is experimentally quite adequate and clearly outperforms state-of-the-art methods in a variety of downstream tasks including 3D classification, partial segmentation and object detection.

### Weaknesses
1. An obvious grammatical error, "leaner" in the title should be "learner". In addition, it is recommended to enlarge the fonts of the images in the paper to enhance the presentation quality, as they are even smaller than the font size of the main text.
2. The novelty of this work needs to be additionally and strongly illustrated. On the one hand, this paper only uses point clouds and as input, however, I2P-MAE (CVPR’2023) and TAP (ICCV’2023) also follow this paradigm. On the other hand, the multi-scale multi-head (MSMH) attention mechanism mentioned in this paper aims to mine more features of the network, however, this is also explored in Point-M2AE (NeurIPS’2023) and more unsupervised methods.
3. The implementation part of the paper has some advantages over contemporaneous methods. However, as point cloud self-supervised learning evolves, more excellent work such as PointGPT (NeurIPS’2023), ReCon (ICML’2023), and ACT (ICLR’2023) should be considered for inclusion in the comparative experiments.

### Questions
1. How are the feature-level images in the abstract represented in the main text, please?
2. How does the number or size of multi-view images affect the proposed method, please? This may require further experimentation and analysis by the authors, and reference to CrossNet (TMM’2023) and Inter-MAE (TMM’2023), which use multi-view images for comparative learning between multiple modalities, is highly recommended.
3. Could the authors please provide appropriate qualitative visualisations such as complementary maps in their experiments? It is suggested to refer to Point-MAE (ECCV’2022), Point-M2AE (NeurIPS’2023) and TPM (arxiv’2024), which compare missing inputs and complementary outputs before and after self-supervision.

Overall, this is a relatively good work. If the author can take my comments into consideration and make explanations and revisions, I may further improve my score. AND vice versa.

### Soundness
4

### Presentation
3

### Contribution
4
