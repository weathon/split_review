# SYRAC: Synthesize, Rank, and Count

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5

## Abstract
Crowd counting is a critical task in computer vision, with several important applications. However, existing counting methods rely on labor-intensive density map annotations, necessitating the manual localization of each individual pedestrian. While recent efforts have attempted to alleviate the annotation burden through weakly or semi-supervised learning, these approaches fall short of significantly reducing the workload. We propose a novel approach to eliminate the annotation burden by leveraging latent diffusion models to generate synthetic data. However, these models struggle to reliably understand object quantities, leading to noisy annotations when prompted to produce images with a specific quantity of objects. To address this, we use latent diffusion models to create two types of synthetic data: one by removing pedestrians from real images, which generates ranked image pairs with a weak but reliable object quantity signal, and the other by generating synthetic images with a predetermined number of objects, offering a strong but noisy counting signal. Our method utilizes the ranking image pairs for pre-training and then fits a linear layer to the noisy synthetic images using these crowd quantity features. We report state-of-the-art results for unsupervised crowd counting. As part of our commitment to fostering reproducibility within the field, we plan to release all synthetic datasets, code, and model checkpoints.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents an unsupervised crowd counting approach based on synthetic data. Specifically, it generates synthetic data through stable diffusion with a selected prompt and then employs the rank loss and a count loss for prediction. The excellent experimental results demonstrate the advantages of the proposed unsupervised method.

### Strengths
The idea is novel and the experimental results demonstrate the advantages of the proposed unsupervised method.

### Weaknesses
A deep analysis of the experimental results is not provided.

1. Could the author provide a more comprehensive explanation for Figure 6? Both small and large counts are distributed throughout the entire space in the QNRF dataset. It is difficult to interpret the UMAP results without any explanation.
2. What is the advantage of generating synthetic data via stable diffusion, especially when compared with the large synthetic dataset GCC[1]? Both approaches are label-free, but GCC contains more detailed count and localization information. Additionally, [1] achieves better counting performance than the proposed method when there are no human-labeled annotations. It would be helpful to clarify the specific advantages of this paper.
3. Although this is an unsupervised method, it would be valuable to understand whether the pre-training phase performs as expected. The authors could randomly select pairs of images from SHA/SHB/QNRF to determine accuracy or probability and analyze cases in which it failed. Furthermore, the accuracy should be compared with a similar method presented in Liu et al[2].
4. The impact of patch size is only presented in the table. Could the authors provide a deeper analysis and discussion on the reasons for the observation that different patch sizes lead to different performance?

### Questions
1. Could the author provide a more comprehensive explanation for Figure 6? Both small and large counts are distributed throughout the entire space in the QNRF dataset. It is difficult to interpret the UMAP results without any explanation.
2. What is the advantage of generating synthetic data via stable diffusion, especially when compared with the large synthetic dataset GCC[1]? Both approaches are label-free, but GCC contains more detailed count and localization information. Additionally, [1] achieves better counting performance than the proposed method when there are no human-labeled annotations. It would be helpful to clarify the specific advantages of this paper.
3. Although this is an unsupervised method, it would be valuable to understand whether the pre-training phase performs as expected. The authors could randomly select pairs of images from SHA/SHB/QNRF to determine accuracy or probability and analyze cases in which it failed. Furthermore, the accuracy should be compared with a similar method presented in Liu et al[2].
4. The impact of patch size is only presented in the table. Could the authors provide a deeper analysis and discussion on the reasons for the observation that different patch sizes lead to different performance?"

[1] Wang, Qi, et al. "Learning from synthetic data for crowd counting in the wild," CVPR, 2019.
[2] Liu, Xialei, et al. "Leveraging unlabeled data for crowd counting by learning to rank," CVPR, 2018

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces an unsupervised counting method that utilizes latent diffusion models to create synthetic data. The approach involves two unsupervised techniques: first, removing pedestrians from actual images, resulting in ranked image pairs that provide a ranking loss of object quantity. Second, generating synthetic images with a predetermined number of objects, which gives a noisy but related counting label.

### Strengths
- The idea of utilizing a stable model to generate synthetic images seems feasible.
- The paper introduces two strategies: a weak but reliable object quantity signal and a strong but noisy counting signal. This approach seems quite reasonable, as it can potentially complement and enhance the model's performance.

### Weaknesses
 - What is the rationale behind the setting of N, which is the crowd count to generate synthetic images? What is the quality of the generated images? Is it possible to provide a measure of variance to assess the feasibility of this method?
- There are only six categories for N. Why not train the model by a classification task? In situations where the labels are not stable, the classification task seems to be able to maintain a relatively high level of accuracy.
- The synthetic images do not include images with 0 crowd count. Does this method have the capability to handle datasets that consist of a large portion of (background) images with no people, such as NWPU?
- How does the computational cost of generating synthetic images using the diffusion model compare to that of other unsupervised counting models?
- There are some repetitions in the references.
- Figure 6 illustrates that the features exhibit an underlying crowd-count-based ordering. However, it would be more convincing if features from supervised counting models could be provided for comparison.
- In Table 3, the methods proposed in the paper actually include ImageNet pretraining. What is the performance when combining ImageNet pretraining with intra-image ranking?
- Does the ranking loss merely train the model to distinguish between real and synthetic images?

### Questions
-  Figure 6 illustrates that the features exhibit an underlying crowd-count-based ordering. However, it would be more convincing if features from supervised counting models could be provided for comparison.
- In Table 3, the methods proposed in the paper actually include ImageNet pretraining. What is the performance when combining ImageNet pretraining with intra-image ranking?
- Does the ranking loss merely train the model to distinguish between real and synthetic images?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on the unsupervised crowd counting task, a critical yet challenging task. To achieve this goal, the authors use latent diffusion models to create two types of synthetic data and then utilize the ranking image pairs for pre-training and fit a linear layer to the noisy synthetic images using these crowd quantity features. Experiments conducted on five datasets demonstrate the effectiveness of the proposed method.

### Strengths
(a) Using stable diffusion to generate the crowd dataset is a good idea, providing a new perspective for this area. 
(b) This paper is written well and easy to follow

### Weaknesses
1. For the fully supervised part, the authors only discuss the density-based crowd counting methods. In other words, many localization-based methods should be discussed, making the related work more comprehensive.

2. The authors have pointed out that the prompt count is not reliable but using it as the GT count directly during the training phase. It makes me confused. I think it would be better to rank the generated 60 images using the pre-trained backbone first. Secondly, fine-tune the GT count according to the ranking results. Specifically, image A and image B are generated using the same prompt count 20. However, ranking results present that image A contains fewer persons than image B, so the GT count of image A could be fine-tuned to be smaller than the GT count of image B.

3. I understand that the input of the generation process is complete images without cropping, but the inference process uses image patches as input. There may be resolution gaps. How about cropping the original images into patches in the generation process instead?

4. There is a lack of quantitative analysis about the reliability of the generation process. Specifically, the authors can sample n source images for generation and statistics on the percentage of images where the objects were successfully removed.

5. The authors think the ranking information is reliable, and the prompt count is relatively unreliable. Thus, the authors pre-train the backbone using the ranking information and freeze the backbone during the training phase to resist the prompt count noise. I agree that the ranking information is more reliable. However, I am not sure it is necessary to fix the backbone as only fine-tuning the linear layer may limit the learning potential on the prompt count, which is considered ground truth. There could be an ablation study on fine-tuning the backbone during the training phase.

6. Since the current method is still significantly lower than CrowdCLIP, the authors think the early stop used in CrowdCLIP might be unfair. So I would like to know the performance under early stop.

7. The motivation to synthesize the ranking crowd image is still unclear since one can utilize the existing datasets to generate the ranking image pairs, like CrowdCLIP.

### Questions
see weakness

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
