# MGD$^3$: Mode-Guided Dataset Distillation using Diffusion Models

- Decision: Reject
- Scores: 3, 3, 6, 8

## Abstract
Dataset distillation aims to distill a smaller training dataset from a larger one so that a model trained on this smaller set performs similarly to one trained on the full dataset. Traditional methods are costly and lack sample diversity. Recent approaches utilizing generative models, particularly diffusion models, show promise in capturing data distribution, but they often oversample prominent modes, limiting sample diversity.
To address these limitations in this work, we propose a mode-guided diffusion model. Unlike existing works that fine-tune the diffusion models for dataset distillation, we propose to use a pre-trained model without the need for fine-tuning. Our novel approach consists of three stages: Mode Discovery, Mode Guidance, and Stop Guidance. In the first stage, we discover distinct modes in the data distribution of a class to build a representative set. In the second stage, we use a pre-trained diffusion model and guide the diffusion process toward the discovered modes to generate distinct samples, ensuring intra-class diversity. However, mode-guided sampling can introduce artifacts in the synthetic sample, which affect the performance. To control the fidelity of the synthetic dataset, we introduce the stop guidance. 
We evaluate our method on multiple benchmark datasets, including ImageNette, ImageIDC, ImageNet-100, and ImageNet-1K; 
Our method improved $4.4\%$, $2.9\%$, $1.6\%$, and $1.6\%$ over the current state-of-the-art on the respective datasets.
In addition, our method does not require retraining of the diffusion model, which leads to reduced computational requirements. 
We also demonstrate that our approach is effective with general-purpose diffusion models such as Text-to Image Stable Diffusion, showing promising performance towards eliminating the need for a pre-trained model in the target dataset.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed a generative prior methods called MGD for dataset distillation tasks. This paper follows the idea of the baseline MiniMaxDiff Gu et al. (2024) to enhance the diversity of the generated synthetic data. MGD influences the generation process by leveraging DiT models without requiring re-training or fine-tuning. Specifically, the authors propove to utilize the so-called mode to regularize the generation of synthetic data. However, the formulation for calculating these modes is not clearly explained. Based on Figure 2, my understanding is that the modes are the cluster centers of the original dataset. Additionally, the paper lacks theoretical proof to support the effectiveness of the proposed mode-guided approach. The demonstration in Figure 1 selects only four data instances to illustrate diversity improvement, which seems highly subjective.

### Strengths
1. The authors consider the soft-label protocol and hard-label protocol, which are important for fair comparison in dataset distillation. We can see the difference between two the protocols in Table 10. 

2. The performance improvements reported in this paper are significant.

### Weaknesses
1. It is good that the authors clarify the the soft-label protocol and hard-label protocol. However, what protocol is used in Table 1, 2, 3? If the soft-label protocol is used, what are the parameters of valiation epochs, teacher networks, and the data augmentation methods? 

2. I do not see a clear formulation explaining the derivation of the modes. Only Section 3.2 (lines 307 to 319) discusses the application of modes. My main concern is with the method used to select the modes; specifically, specially designed parameters for generating these modes could significantly impact the final performance.

3. Based on Figure 2, my understanding is that the modes are the cluster centres of the original dataset. This approach is very close to the Dream method. Please tell more details about the difference between the two methods. 


4. The abstract could be more concise. For example, the limitation mentioned from lines 12 to 20 can be condensed into two sentences.  The description of your proposed method could be more generalized. Additionally, the caption of Figure 1, and the related works could be more concise as well. 

5. The authors should emphasize more about the derivation, and formulation on the modes. However, most of the introduction and related work are telling the basic information of the previous methods. I cannot find a strong motivation or intuition to develop the mode-guided approach. Also, i doubt the performance enhancement is highly affected by the parameters in obtaining the modes. 

6. The random method achieves a very high performance as stated in Table 1. What if the set is constructed by dataset pruning method, such as [2], and is evaluated by the soft-label protocols? 

7. Although the authors list five contributions in this paper, points 1, 3, 4, and 5 seem redundant, essentially representing the same idea. Additionally, point 2 merely reiterates a widely acknowledged finding from previous works—that diversity is beneficial.

[1] Liu, Yanqing, et al. "Dream: Efficient dataset distillation by representative matching." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

[2] He, M., Yang, S., Huang, T., & Zhao, B. (2024). Large-scale dataset pruning with dynamic uncertainty. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 7713-7722).

### Questions
As stated in weakness part.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper adapts the pretrained diffusion model for dataset distillation. Specifically, with a pretrained diffusion model, the authors introduce mode guidance in the early denoising stages. The modes for guidance are discovered from the target data distribution with VAE encoder. Experiments show that the new method outperforms some diffusion model baselines and dataset distillation methods.

### Strengths
1.	The idea of mode guidance for target-distribution synthesis is reasonable and easy to implement. 

2.	Extensive experiments and study have been provided.

### Weaknesses
1.	The writing can be improved, especially the logic and causality in introduction. The citation format is unsuitable. Some words/phrases have inconsistent capitalization. 
2.	Some statements are not rigorous:
a)	The authors claim “… diffusion models … do not suffer from mode collapse” in introduction. Is it theoretically or empirically proved in previous work? It also has conflicts with the claims in other paragraphs. 
b)	“We validate this by addressing the following question: Given a pre-trained diffusion model, can a distilled dataset be extracted from this model, as it has learned the data distribution?” As claimed in the abstract, the diffusion model is pre-trained by others on some datasets. It is not guaranteed that the diffusion model “has learned the data distribution” of “a distilled dataset”. 
3.	The listed five “contributions” are mostly repeated and trivial. 
4.	According to Table 1, the new method is better than some diffusion baselines, while obviously worse than the classic dataset distillation methods, e.g., DM 2023. 
5.	Though images from target distribution are synthesized by diffusion model, there is no connection to dataset distillation, in which data/knowledge should be distilled/condensed.

### Questions
No.

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
This paper proposes a mode-guided diffusion model that generates synthetic datasets using pre-trained models without the need for fine-tuning. The method operates through three key stages: mode discovery, mode guidance, and stop guidance. These stages ensure both enhanced data diversity and high sample quality. Furthermore, the approach is versatile, making it applicable to various diffusion models. Experimental results demonstrate that the proposed method surpasses existing techniques across multiple datasets, effectively addressing the issue of limited mode diversity in generated data.

### Strengths
- Ensuring dataset sample diversity has long been a challenge in the field of dataset distillation. This paper addresses this by employing mode guidance to generate as diverse samples as possible for each class, minimizing redundancy and significantly enhancing intra-class diversity in the generated dataset.

- The paper utilizes pre-trained diffusion models to generate datasets without the need for additional fine-tuning, relying only on guidance during the denoising process, which simplifies the approach and improves efficiency.

- The stop guidance mechanism strikes a balance between sample diversity and quality, ensuring diverse samples while maintaining high quality, and preventing potential negative effects from excessive guidance.

### Weaknesses
- The mechanisms of mode and stop guidance are clear but lack strong theoretical support.

- The method is easy to understand but could be optimized, such as by automating the adjustment of $t_{SG}$ and improving the mode discovery algorithm.

- The approach is still fundamentally about image generation via diffusion models, with insufficient exploration of its contribution to dataset distillation.

### Questions
- Could you go beyond the traditional framework of diffusion model-based image generation and further explain the relationship between your method and dataset distillation?

- I’m curious about the resource consumption of $MGD^3$, such as runtime and memory usage. Could you provide more details on this?

- How do you ensure that the modes obtained using the K-means clustering algorithm are meaningful in the context of dataset distillation? Have you tried other algorithms for mode discovery in each class?

- Given the increase in sample diversity, I would like to see a comparison of cross-architecture evaluations with other diffusion + DD methods. Could you include more network architectures? The paper only uses three networks for evaluation.


If you can address all or most of my questions, I would consider giving a higher score.

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
This paper proposes a mode guidance method in the reverse process of a pretrained diffusion model to enhance the diversity of synthetic images generated for dataset distillation task. They calculate the mode by kmeans clustering on the original dataset, then calculate the mode guidance score which is added to the noise function at appropriate time steps during the reverse process of the diffusion model. This approach achieves both the representativeness and diversity in the synthetic images.

### Strengths
1. The quantitative results on ImageNet-1k and its subsets show improvement across all tables compared to both the baseline and state-of-the-art methods at various ipc. 
2. The pretrained diffusion model generates distinct samples that ensure intra-class diversity with the help of the guidance signal in reverse process.
3. Training time is reduced as the pretrained diffusion model does not require fine-tuning.

### Weaknesses
1. The image quality, the information loss and the recovery of data distribution rely on the diffusion model heavily.
2. The mode simply calculated by kmeans may represent the original data distribution insufficiently and the author does not compare it with other cluster methods.

### Questions
1. Can you please tell if the results of CIFAR10/100 and tinyImageNet have also improved?
2. Have you tried other cluster methods in experiments to check if they influence performance?

### Soundness
3

### Presentation
3

### Contribution
3
