# CSGO: Content-Style Composition in Text-to-Image Generation

- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 6, 5, 5, 6

## Abstract
The diffusion model has shown exceptional capabilities in controlled image generation, which has further fueled interest in image style transfer.
Existing works mainly focus on training free-based methods (e.g., image inversion) due to the scarcity of specific data.
In this study, we present a data construction pipeline for content-style-stylized image triplets that generates and automatically cleanses stylized triplets. 
Based on this pipeline, we construct a dataset IMAGStyle, the first large-scale style transfer dataset containing 210k image triplets, available for the community to explore and research.
Equipped with IMAGStyle, we propose CSGO, a style transfer model based on end-to-end training, which explicitly decouples content and style features employing independent feature injection. 
Our CSGO implements image-driven style transfer, text-driven stylized synthesis, and text editing-driven stylized synthesis.
Extensive experiments demonstrate the effectiveness of our approach in enhancing style control capabilities in image generation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper was well written with clear structure and easy to understand. The paper firstly proposes a high quality and carefully cleaned dataset with 210k Content-StyleStylized Image Triplets.  Then, the paper proposes a new style transfer framework CSGO, which uses independent content and style feature injection modules to achieve high-quality image style transformations. Finally, a new score matrix named CAS was introduced to measure content loss after content-style transferred.

### Strengths
The open-source dataset of the article is valuable to the community. The experimental results reflected in the article are good.

### Weaknesses
The method proposed in the article is relatively simple and tends to be stacked. Although the author claims that this is an end-to-end approach, its innovation is insufficient. The feature injection amplification mentioned in the article are common methods, except for inject style features into Controlnet. What is the principle explanation for the operation mentioned in the paper —“The insight of this is to pre-adjust the style of the content image using style features making the output of the Controlnet model retain the content while containing the desired style features.” Actually, I can't see its importance from Fig 9. (2) W Content Control W/O style injection in ControlNet. More ablation study need to be supplemented with style similarity (CSD) and content alignment (CAS) Matrix.

### Questions
The feature injection amplification mentioned in the article are common methods, except for inject style features into Controlnet. What is the principle explanation for the operation mentioned in the paper —“The insight of this is to pre-adjust the style of the content image using style features making the output of the Controlnet model retain the content while containing the desired style features.” Actually, I can't see its importance from Fig 9. (2) W Content Control W/O style injection in ControlNet. More ablation study need to be supplemented with style similarity (CSD) and content alignment (CAS) Matrix.

### Soundness
1

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
4

### Summary
This paper presents a method for reference-based image stylization method. To achieve this goal, a style encoder and an image encoder are presented. Features are injected into the diffusion backbone through selected layers. Meanwhile, a 210K (image, style, stylized image) triplet dataset was built and used for training the proposed model. In the experimental results, content similarity and style similarity were evaluated. Comparisons were made between the proposed method and other SOTA methods. Ablation studies are informative and comprehensive.

### Strengths
1. The paper is pretty complete, including a solid dataset, training details, evaluation comparisons and ablation studies. 
2. The proposed dataset is useful for future related work

### Weaknesses
1. The overall training method is not new, which follows the lines of research like IP-adapter, InstanceID, InstanceStyle, and the usage of Ada-In is common too in stylization research. Specifically, the injection of style features into the diffusion model via selected layers, while effective, is a well-trodden path. The novelty of this approach is therefore limited, as it largely reuses existing architectural components and training strategies. The use of AdaIN for style transfer, while a standard technique, does not introduce any significant innovation in this context.
2. In the dataset, the stylized image is fixed while given a content image and style image, a stylized image can be various based on preference. Since the extent to which the content image is stylized is fixed, the proposed network fits to that, which reduced the potential capacity to adapt. I understand there's control factor to adjust to be more stylized or less, but the upper bound is the dataset. This pre-determined stylization limits the model's ability to generalize to a broader range of stylization effects, as it is essentially trained to reproduce a specific, fixed transformation rather than learning a more flexible style transfer function. The model's capacity to adapt to varying degrees of stylization is therefore constrained by the dataset's inherent limitations.

### Questions
Can you show some failure cases?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This study proposes a diffusion-based stylized image generation method. The authors claim that the lack of paired data for training models limits the performance of popular stylization methods. To this end, the authors propose an augmented dataset by training various LoRAs for different contents and styles. Then, an IP-adaptor style framework is trained on the collected dataset.

### Strengths
Overall, the reviewer feels the motivation is valid. Given that many image-generation tasks are ill-posed and lacking ground truth, trying to find the paired data for supervised learning is valid. Also, the reviewer would like to express appreciation for the efforts in collecting the dataset, which may be quite time-consuming. The proposed CSGO is reasonable and easy to follow.

### Weaknesses
- The authors claim that the performance of image style transfer is limited because of the lack of a large-scale stylized dataset, which makes it impossible to train modes end-to-end. However, the proposed dataset is learned by training and combining different LoRAs, which means the generated stylized data is not the real ground truth for end-to-end training. In fact, the whole framework seems to try to distill the generated dataset in one adaptor. The use of LoRA-generated data introduces a potential bias, as the stylized images are inherently constrained by the LoRA models' capabilities and may not represent the full spectrum of possible styles or content variations. This raises concerns about the generalizability of the learned style transfer model to unseen, real-world data.
- Most image generation tasks are ill-posed and lack ground truth. A similar idea goes to ''Identity-Preserving Face Swapping via Dual Surrogate Generative Models.''  Face-swapping methods try to fuse one source image with one target image. Similar to the setting of image style transfer, no ground truth information could be collected as image style transfer tasks for face-swapping tasks.  Thus, the authors of [r1] tried to generate the <source, target, results> triplets. A more careful analysis of the pros and cons of using such generated data is given in [r1]. However, in this study, the author claims that style transfer lacks a larger-scale stylized dataset without careful analysis or support. The authors should provide a more thorough justification for why their approach of generating stylized data is superior to other methods, especially considering the potential for artifacts and biases introduced by the LoRA models. 
The proposed method, CSGO, is just a combination of many existing techniques. For content control, the two strategies are the combination of ControlNet and IP-Adaptor. For style control, they employ Perceiver Resampler structure as Alayrac et al. to project the style features and then do some trivial modifications to controller or ip-adaptor. The reviewer understands that the authors need to verify the usefulness of the proposed dataset. However, such a method could not make a good contribution to ICLR. The novelty of the proposed method is limited, as it primarily combines existing techniques without introducing significant innovations in the core algorithms or architectures. The modifications to the controller and IP-adapter are not substantial enough to warrant a strong contribution.
- The proposed evaluation index has the same problem. Using AdaIN for content and style evaluation is common sense in a related field, but it could not be counted as a contribution. The use of AdaIN features from a DINO model, while common, does not provide a novel evaluation metric. The authors should consider using more comprehensive and diverse metrics that can better capture the nuances of style transfer quality, such as perceptual metrics or user studies.
- No user study is conducted. Technical writing should be paid more attention. For example, most of the cross-reference format is wrong (Maybe there is a mistake in using cite citet and citep)

### Questions
Could the collected dataset supplement the training of traditional style transfer methods? For example, the collected pair can be used to tune Stytr or CAST. Using the collected dataset and the training pipeline of traditional style transfer tasks, could the method perform much better than before?

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
5

### Summary
The paper establishes a data pipeline for constructing content-style-stylized image pairs and introduces the IMAGStyle dataset. Additionally, it utilizes this dataset to perform end-to-end training on the proposed CSGO framework, achieving style transfer generation under various input conditions.

### Strengths
- A high-quality dataset composed of content-style-stylized image pairs is proposed, which can be useful for research in style transfer.

- This paper proposes a method for decoupling content and style, injecting them separately into different locations within the U-Net. Additionally, it combines ControlNet for further integration of the injected features. In this approach, both U-Net and ControlNet have fixed parameters, creating an efficient training framework.

- The paper shows many analyses and visualization results of the proposed method, and easy to follow.

### Weaknesses
 - If the dataset and its construction pipeline are one of the contributions of this paper, it is necessary to provide results using this dataset for training on other baseline methods and compare them with the proposed CSGO framework. This would demonstrate the effectiveness of the dataset and the robustness of the CSGO method.

- The proposed method borrows from IP-Adapter and ControlNet. And, the specific inputs for the three proposed Cross-Attention blocks and the method of feature injection have not been clearly explained. It is unclear how the content and style features are processed and integrated within the cross-attention mechanism, and how this differs from the original IP-Adapter implementation. Specifically, the role of each input (query, key, value) in the cross-attention layers needs further clarification, as well as the exact mathematical operations performed during feature injection.

- The quantitative evaluation is relatively limited, additional metrics could be included for assessment. On the other hand, regarding qualitative evaluation, the existing visual results do not intuitively reflect the advantages of this method. (Some additional evaluation metrics, such as FID, Aesthetic Scores, and user studies.) The visual results lack side-by-side comparisons with other state-of-the-art methods, making it difficult to assess the relative performance of the proposed approach. The qualitative analysis should also include a more diverse set of examples, showcasing the method's performance across different content and style combinations.

- Figure 1 serves as the first illustration, and it should be clearly introduced, including the input image, output image, and comparison images, providing visual guidance to facilitate better understanding. This should also include the Figure 1(3) part. The lack of clear labeling and explanation makes it difficult for the reader to understand the different input and output modalities of the proposed method.

- Suggestions for the format: citations need to be changed to conform more to the standard \citet or \citep; the font formatting and size of all similar-level figures in the paper are inconsistent, and the arrangement of images is rough and needs further improvement.

### Questions
- I am curious why the dataset is abbreviated as IMAGStyle and the method is abbreviated as CSGO.

- Can this method be applied to multiple content images or multiple style images as reference images to achieve better results?

- During the data cleaning phase, CAS is used to validate content consistency. How can we ensure that the style generated by LoRA for the images is correct?

- It appears to empirically inject Content into the down block and Style into the UpBlock; could you clarify the rationale behind this choice?

### Soundness
2

### Presentation
2

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
The authors introduce a large dataset, IMAGStyle, consisting of 210k triplets, to train a style transfer model via a simple feature injection technique. To construct IMAGStyle, they collect arbitrary pairs of content and style images, (i) apply style transfer to the content images, and (ii) filter out stylized images that exhibit content leakage from the style images. They propose a straightforward adapter and controlnet based architecture with modification in cross attention and feature injection layers.

### Strengths
(i) The curated dataset, IMAGStyle, encompasses a broad range of content-style images, demonstrating extensive applicability.

(ii) The visual quality of the stylized image samples presented in the paper and appendix is highly satisfactory.

(iii) The concept is straightforward, and the methodology is direct.

### Weaknesses
(i) In the second step of data creation, AdaIN with DINO features is used to filter out images with style leakage. Does this process ensure the removal of style leakage related to factors such as content pose, size, and background? It is necessary to demonstrate that the filtering process addresses various types of style leakage, including texture, color, pose, size, and background. The provided examples and explanation do not fully address the concern that the CAS metric may not be robust enough to filter out content information such as pose, size, and background coming from the style image. A more extensive list of visual examples of filtering cases, without cherry-picking, is needed to demonstrate the effectiveness of the CAS metric in this regard.

(ii) The comparison with existing methods appears to omit several relevant works. There are more recent, well-performing approaches that utilize textual inversion variants, LoRA/DreamBooth variants, and training-free methods.

(iii) There are too many variants of hyper-parameters that affect the quality of image sample: content scale $\delta_c$, another content scale $\lambda_c$, style scale $\lambda_s$, and cfg scale. There needs to be specific hyper-parameter setting that generally leads to satisfactory results.

### Questions
(i) What are the primary differences between the proposed method and existing adapter variants, such as Ip-Adapter (Ye et al., 2023) and StyleAdapter (Wang et al., 2023), which leverage content-style pairs for adapter training? These models are noted for their limited generalizability to style images that were not included in the training data. Does CSGO exhibit the same limitation? Please provide examples using style images that include random cartoon characters not present in the WikiArt dataset.

(ii) In addition to qualitative samples and CSD similarity measurements, please include human evaluation results on randomly sampled stylized images.

### Soundness
2

### Presentation
2

### Contribution
2
