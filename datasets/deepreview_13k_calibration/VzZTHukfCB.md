# SeaS: Few-shot Industrial Anomaly Image Generation with Separation and Sharing Fine-tuning

- Decision: Reject
- Avg Score: 5.67
- Scores: 8, 3, 6, 6, 5, 6

## Abstract
Current segmentation methods typically require many training images and precise masks, 
while insufficient anomaly images hinder their application in industrial scenarios.
To address such an issue, we explore producing diverse anomalies and accurate pixel-wise annotations.
By observing the real production lines, we find that anomalies vary randomly in shape and appearance, whereas products hold globally consistent patterns with slight local variations.
Such a characteristic inspires us to develop a Separation and Sharing Fine-tuning (SeaS) approach using only a few abnormal and some normal images.
Firstly, we propose the Unbalanced Abnormal (UA) Text Prompt tailored to industrial anomaly generation,
consisting of one product token and several anomaly tokens.
Then, for anomaly images,
we propose a Decoupled Anomaly Alignment (DA) loss to bind the attributes of the anomalies to different anomaly tokens.
Re-blending such attributes may produce never-seen anomalies, achieving a high diversity of anomalies.
For normal images, we propose a Normal-image Alignment (NA) loss to learn the products' key features that are used to synthesize products with both global consistency and local variations.
The two training processes are separated but conducted on a shared U-Net.
Finally, SeaS produces high-fidelity annotations for the generated anomalies by 
fusing discriminative features of U-Net and high-resolution VAE features.
The extensive evaluations on the challenging MVTec AD and MVTec 3D AD dataset (RGB images) demonstrate the effectiveness of our approach.
For anomaly image generation, on MVTec AD dataset, we achieve 1.88 on IS and 0.34 on IC-LPIPS, while on the MVTec 3D AD dataset, we obtain 1.95 on IS and 0.30 on IC-LPIPS. 
For the downstream task, by using our generated anomaly image-mask pairs, three common segmentation methods achieve an average 11.17\% improvement on IoU on MVTec AD dataset, and a 15.49\% enhancement in IoU on the MVTec 3D AD dataset.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a new method named Seas to solve the few-shot anomaly image generation problem. It leverages the stable diffusion model and VAE to generate anomaly images with accurate annotations. The experiment results show the effectiveness of their method.

### Strengths
1.	Leveraging text prompts to guide the model in decoupling the generation of abnormal regions and objects.
2.	Using VAE to generate high-resolution annotations is a good direction.

### Weaknesses
1.	The relationship between anomaly tokens and training different types of anomalies is not clear.
2.	The paper has not discussed how to control the type of exceptions generated during inference.
3.	The paper does not explain why the U-net used to predict noise in the Refined Mask Prediction branch has a highly discriminative feature.

### Questions
1. I want to clarify the relationship between exception marking and training different types of exceptions.
2. I want to know how to control the types of exceptions generated during inference.
3. I wonder why U-net, which is used to predict noise, has highly discriminative features in the fine mask prediction branch.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a separation and sharing fine-tuning (SeaS) approach with a few abnormal and some normal images to produce anomalies and pixel-wise annotations. An unbalanced abnormal (UA) text prompt is introduced for anomaly generation, which consists of one product token and several anomaly tokens. For anomaly images, a decoupled anomaly alignment (DA) loss is used to bind the attributes of the anomalies to different anomaly tokens. For normal images, a normal-image alignment (NA) loss is used to learn the products’ key features that are used to synthesize products with both global consistency and local variations. Experiments on MVTec AD and MVTec 3D AD datasets (RGB images) show the effectiveness of the proposed method for anomaly image generation and detection.

### Strengths
+ The motivation is good. A shared generation model for multiple anomaly types is proposed to solve the problem of insufficient anomaly images.

+ The generated anomaly images seem more real than other GAN-based methods.

+ Some ablation studies are provided to facilitate the understanding of how the performance benefits from different components, including the DA loss, the NA loss, and the refined mask prediction branch.

### Weaknesses
 - The experimental results are insufficient. Because the ultimate goal of generating abnormal images is to improve the performance of anomaly detection tasks, some SOTA anomaly detection methods should also be compared on image AUROC, pixel AUROC and PRO besides generative model-based anomaly detection methods, e.g., DiAD [1]. Although RealNet [2] is compared in appendix A.5, the proposed method does not significantly outperform RealNet, particularly AUROC, and RealNet does not use any anomaly samples during training.

- Since the proposed method is not specific to the multi-class anomaly detection setting, I would also wonder about the comparison with SOTA methods in the single-class anomaly detection setting, especially supervised/semi-supervised methods, e.g., PRN [3] or BGAD [4], because anomaly samples are used during training of the proposed method. The lack of comparison with single-class methods is a significant gap, especially given the use of anomaly samples during training, which is a common characteristic of many single-class approaches.

- More datasets are required to evaluate the proposed anomaly generation method on image AUROC, pixel AUROC and PRO, such as VisA dataset containing more diverse and tiny anomalies. It is more challenging to generate these anomalies. The current evaluation is limited to MVTec AD and MVTec 3D AD, which may not fully capture the method's ability to generalize to more complex anomaly patterns.

- What does the “unbalanced” mean in Sec. 3.2? The paper does not clearly explain its meaning. The authors should clearly define or explain this term when it is first introduced, and discuss its significance to the overall approach. The lack of clarity around this term makes it difficult to understand the specific design choices of the method.

- In Fig.5, for Wood color, the results generated by the proposed method do not seem better than the results of AnomalyDiffusion. The generated anomalies appear similar to the training data, which raises concerns about the diversity and generalization capability of the proposed method, especially when compared to other methods.

### Questions
1. Because the ultimate goal of generating abnormal images is to improve the performance of anomaly detection tasks, some SOTA anomaly detection methods should also be compared on image AUROC, pixel AUROC and PRO besides generative model-based anomaly detection methods, e.g., DiAD [1]. Although RealNet [2] is compared in appendix A.5, the proposed method does not significantly outperform RealNet, particularly on AUROC, and RealNet does not use any anomaly samples during training.

2. Since the proposed method is not specific to the multi-class anomaly detection setting, I would also wonder about the comparison with SOTA methods in the single-class anomaly detection setting, especially supervised/semi-supervised methods, e.g., PRN [3] or BGAD [4], because anomaly samples are used during training of the proposed method.

3. More datasets are required to evaluate the proposed anomaly generation method on image AUROC, pixel AUROC and PRO, such as VisA dataset containing more diverse and tiny anomalies. It is more challenging to generate these tiny anomalies.

4. What does the “unbalanced” mean in Sec. 3.2? The authors should clearly define or explain this term when it is first introduced, and discuss its significance to the overall method.

5. In Fig.5, for Wood color, the results generated by the proposed method do not seem better than the results of AnomalyDiffusion.  Are there particular challenges with the Wood color anomaly type for the proposed method?

### Soundness
2

### Presentation
3

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
This paper proposes a Separation and Sharing Fine-tuning (SeaS) approach for few-shot industrial anomaly image generation. The proposed Decoupled Anomaly Alignment (DA) loss and Normal-image Alignment (NA) loss achieve the generation of highly-diverse anomalies and globally-consistent products. Moreover, the author designs the Refined Mask Prediction (RMP) module to produce pixel-wise anomaly annotations. Extensive experiments show the effectiveness of the method.

### Strengths
In general, the proposed method is reasonable and the results are fine.

+ Both anomaly image generation and anomaly segmentation are considered.
+ This paper is clearly presented.
+ The proposed method achieves realistic and diverse generation of abnormal samples.

### Weaknesses
 - The word “Unbalanced” in Unbalanced Abnormal Text Prompt is inappropriate. The author believes fixed generic semantic words may fail to align with a few training images that contain specific defect types. Therefore, the text prompt should be expressed as dynamic or learnable, etc. 
- The author should add the results of Baseline in Table 4, such as generation of typical text prompt with fixed generic semantic words. Moreover, the result with different layers in UNet in RMP branch should be discussed. Specifically, the impact of varying the depth and feature map sizes within the UNet architecture on the performance of the Refined Mask Prediction (RMP) module needs to be explored. This includes analyzing how different combinations of encoder and decoder layers affect the accuracy and granularity of the predicted anomaly masks.
- The authors should replace the abnormal synthesis strategy in the existing unsupervised methods with the proposed generation strategy to prove the effectiveness of the proposed method, such as DRAEM, because the methods in the table 2 are not specifically designed for anomaly detection. The comparison should focus on how the proposed generation method impacts the performance of existing anomaly detection frameworks when used as a data augmentation technique.
- Implementation details of inference should be described, such as inference step and guidance scale, which is critical to the quality of the generation. The specific number of diffusion steps, the sampling method used (e.g., DDIM, DDPM), and the classifier-free guidance scale should be clearly stated, as these parameters significantly influence the quality and diversity of the generated anomalies.
- The latest generation method [1] should be compared. It is important to benchmark against state-of-the-art anomaly generation techniques to establish the relative performance of the proposed method.
- More datasets, such as VisA or RealIAD, are suggested to used for further evaluation of the proposed method. The evaluation should be extended to include datasets with different characteristics, such as varying image resolutions, defect types, and dataset sizes, to assess the generalizability of the proposed method.

### Questions
- The word “Unbalanced” in Unbalanced Abnormal Text Prompt is inappropriate. The author believes fixed generic semantic words may fail to align with a few training images that contain specific defect types. Therefore, the text prompt should be expressed as dynamic or learnable, etc. 
- The author should add the results of Baseline in Table 4, such as generation of typical text prompt with fixed generic semantic words. Moreover, the result with different layers in UNet in RMP branch should be discussed.
- The authors should replace the abnormal synthesis strategy in the existing unsupervised methods with the proposed generation strategy to prove the effectiveness of the proposed method, such as DRAEM, because the methods in the table 2 are not specifically designed for anomaly detection.
- Implementation details of inference should be described, such as inference step and guidance scale, which is critical to the quality of the generation.
- The latest generation method [1] should be compared.
- More datasets, such as VisA or RealIAD, are suggested to used for further evaluation of the proposed method.


[1] Few-Shot Anomaly-Driven Generation for Anomaly Detection. 2024.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a network structure for simultaneously generating anomaly images and their corresponding mask annotations. This is achieved through the following elements within a shared U-Net architecture: 1. Specialized text tokens; 2. Distinct loss functions tailored for anomaly and normal images; and 3. A mask prediction module designed for precise anomaly mask generation. Together, these components ensure the randomness of anomalies, the global consistency of products, and high-quality mask refinement.

### Strengths
Originality: The paper presents an innovative approach to industrial anomaly image generation by designing specialized object and anomaly tokens. This allows a shared model to train across multiple objects and anomalies, which is a unique solution in the field.
Quality: The network structure is carefully designed, combining tailored loss functions for anomaly and normal images along with a mask prediction module.
Clarity: The paper is clearly written and easy to follow, with well-organized sections and explanations that make the complex methodology accessible to readers.
Significance: Extensive experiments substantiate the method’s effectiveness, showcasing significant improvements over prior approaches.

### Weaknesses
Clarity in Methodology: The current fixed anomaly token setup (N=4) does not allow explicit control over specific types of anomalies, particularly in mixed anomaly cases (e.g., mixed anomalies in cable). This limitation reduces the flexibility of the model in generating targeted anomaly types.
Effectiveness of the Method: Unlike AnomalyDiffusion [1], which leverages the text inversion technique [2] without needing to fine-tune the U-Net, this method requires U-Net fine-tuning. This approach might reduce the domain gap for anomaly data, potentially contributing to the improved quality of generated images. However, it would be helpful to clarify the effect of freezing versus fine-tuning the U-Net on image quality. Furthermore, the paper does not explore the potential for overfitting to the training anomalies due to this fine-tuning process, which could limit generalization to unseen anomaly types.
Ambiguity in the Inference Process: The inference process in this paper lacks clarity, making it difficult to understand how to specify a particular anomaly type. Specifically, it is unclear how the model handles the generation of mixed anomalies, or if it is even capable of such generation, given the fixed number of anomaly tokens.

### Questions
1. The paper currently sets a fixed number of anomaly tokens (N=4). This appears to limit control over generating specific anomaly types, especially for mixed anomaly cases like those in the "cable" category. Is this interpretation correct, or is there a way to dynamically adjust or control anomaly types within this setup? Further clarification on this point would be very helpful.
2. Since this method requires fine-tuning the U-Net while AnomalyDiffusion [1] uses text inversion [2] without U-Net adjustments, could the authors clarify whether the observed quality improvement in anomaly generation stems from this fine-tuning? A comparison between freezing and fine-tuning the U-Net would be insightful
3. Could the authors provide additional details on the inference process, specifically on how one could specify or target a particular anomaly type during generation?

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
5

### Summary
This paper presents an innovative approach called SeaS (Separation and Sharing Fine-tuning). SeaS is specifically designed to generate high-quality and diverse industrial anomaly images while using a minimal number of training examples. This is particularly important in industrial contexts, where anomaly images are often scarce.

At the heart of the SeaS methodology is a unique strategy that leverages both normal and abnormal images. This is accomplished through an Unbalanced Abnormal Text Prompt, which distinguishes between product tokens and anomaly tokens. This differentiation enables the generation of anomalies with a variety of attributes, enhancing the practical use of these images in real-world situations.

Additionally, the SeaS method incorporates two key loss functions that are essential to its framework. The first, Decoupled Anomaly Alignment loss, aims to increase the diversity of the generated anomalies. The second, Normal-image Alignment loss, ensures that the product images remain consistent and high-fidelity. Together, these elements strengthen the SeaS methodology, making it effective for producing high-quality industrial anomaly images.

### Strengths
1. The SeaS method presents an approach to few-shot learning specifically tailored for the generation of industrial anomaly images, a task that poses significant challenges due to the limited availability of such images. This method addresses the pressing need for effective anomaly generation in industrial settings, where data scarcity can hinder performance and innovation.
2. Central to the SeaS methodology is the introduction of the Unbalanced Abnormal (UA) Text Prompt, along with a systematic separation of anomaly tokens from product tokens. This strategy not only enhances the diversity of the generated anomalies but also improves their fidelity, thereby ensuring that the resulting images are both varied and accurate representations of real-world anomalies.
3. The paper offers an in-depth examination of two key loss functions: Decoupled Anomaly Alignment (DA) loss and Normal-image Alignment (NA) loss. The DA loss is designed to promote greater diversity among the generated anomalies, while the NA loss ensures that the product images maintain their consistency and high quality.

### Weaknesses
1. The examples provided in the article primarily focus on straightforward instances of image generation. They do not explore more complex scenarios, such as the cable swap and cable missing categories found in the MVTec dataset. These intricate examples necessitate a more advanced approach to image generation that can effectively address complicated anomalies and their effects on overall product appearance.
2. The SeaS framework, while innovative in its application of few-shot learning for industrial anomaly image generation, does not fundamentally differ from the AnomalyDiffusion framework. Both aim to tackle the challenge of generating diverse and realistic anomaly images from limited data. However, SeaS introduces distinctive mechanisms, such as the Unbalanced Abnormal Text Prompt and the Separation and Sharing Fine-tuning strategy. These innovations give SeaS an edge in generating anomalies with greater fidelity and diversity. Nonetheless, both frameworks share a common goal of enhancing anomaly generation capabilities, indicating a gradual evolution in the field of generative models for industrial applications rather than a revolutionary shift.
3. While the paper demonstrates the effectiveness of SeaS with simpler anomalies, it would be valuable for the authors to discuss its performance with more complex anomalies, such as the cable swap and cable missing examples from the MVTec dataset. Are there specific challenges or limitations when generating these complex anomalies? If the method has been tested with these examples, presenting those results could significantly strengthen the paper. If not, outlining potential strategies for addressing these complexities would be advantageous.
4. The paper positions SeaS as a superior approach compared to AnomalyDiffusion. What are the key factors that make SeaS more effective in certain aspects of industrial anomaly image generation? Are there scenarios in which AnomalyDiffusion may still offer advantages? A detailed comparative analysis or a side-by-side case study featuring both frameworks could clarify their respective strengths and weaknesses.

### Questions
1. How does SeaS handle generalization to new, unseen anomaly types in industrial images? Does the framework require retraining, or can it adapt to new anomalies using the same training strategy?
2. What are the computational resources needed for training the SeaS model, and how does this compare to existing methods in terms of training and inference times? Are there any optimizations implemented to accommodate large-scale datasets?
3.  How robust is the SeaS framework to variations in image quality, such as changes in lighting conditions, backgrounds, or resolutions? Does the model maintain consistent performance across these variations?

### Soundness
3

### Presentation
3

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
This work proposes a few-shot industrial anomaly generation method named SeaS.  The authors use a technique similar to textual inversion to update the learnable prompt, and then use the prompt and latent diffusion to generate defects. Moreover, this work proposes an alignment (DA) loss to assign different attributes of the anomalies to different anomaly tokens, achieving a high diversity for anomalies generation.

### Strengths
1. This paper is well organized, and easy to follow.

2. Extensive experiments on MVTec AD and MVTec 3D demonstrate the effectiveness of proposed seaS.

3. The decoupled anomaly alignment loss makes sense, which improves the effect of texual inversion.

### Weaknesses
1. The design of "Unbalanced Abnormal Text Prompt" is similar with previous works [1, 2], which compromises the novelty. 

2. While the paper demonstrates strong performance on MVTec datasets, it is unclear how well the SeaS method generalizes to other datasets or different types of unseen anomalies during training.

3. The paper should provide more details on the computational complexity, as the two training processes.

4. The scalability of the SeaS approach to handle a large number of anomaly types or a higher resolution of images is not discussed. It is an important consideration for industrial applications with diverse and high-resolution imagery.

5. As for the part of defect generation, the key lies in whether the generated defect samples can improve the model detection ability, rather than paying attentions on whether the samples are similar to real defects. However, the metrics used  in Table 1 are all about measures on the generated image.  Author should focus more on generating samples to enhance model detection performance. 

6. The author should conduct experiments on more datasets. At present, some high-quality datasets are existing, such as VisA [4] and Real-IAD [3].

### Questions
Please report the time cost of the proposed method. To my knowledge, diffusion-based work takes long time. But in real industry applications, we need lower time cost.

### Soundness
2

### Presentation
3

### Contribution
1
