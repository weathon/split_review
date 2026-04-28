# Towards Realistic Data Generation for Real-World Super-Resolution

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 6, 5

## Abstract
Existing image super-resolution (SR) techniques often fail to generalize effectively in complex real-world settings due to the significant divergence between training data and practical scenarios. To address this challenge, previous efforts have either manually simulated intricate physical-based degradations or utilized learning-based techniques, yet these approaches remain inadequate for producing large-scale, realistic, and diverse data simultaneously. In this paper, we introduce a novel Realistic Decoupled Data Generator (RealDGen), an unsupervised learning data generation framework designed for real-world super-resolution. We meticulously develop content and degradation extraction strategies, which are integrated into a novel content-degradation decoupled diffusion model to create realistic low-resolution images from unpaired real LR and HR images. Extensive experiments demonstrate that RealDGen excels in generating large-scale, high-quality paired data that mirrors real-world degradations, significantly advancing the performance of popular SR models on various real-world benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces an unsupervised learning framework designed to generate realistic LR images for real-world SR. This paper utilizes a decoupled approach for content and degradation extraction, incorporating them into a diffusion model to produce paired data that closely represents real-world degradations. Experimental results indicate that the proposed method improves the generalization and performance of SR models across various real-world benchmarks.

### Strengths
- The paper is well-structured, making the methodology and findings easy to understand.
- The paper achieves competitive SR results under an unpaired setting, which is practical and advantageous in real-world applications.

### Weaknesses
 - The paper argues that content and degradation can be decoupled by content and degradation extractor. 
However, it is unclear how the content extractor’s encoder is guaranteed to capture only pure content information.

- Equation (5) utilizes X_{hr}, but no explanation or justification is provided for its use in the main manuscript.

- The paper would benefit from a comparison of the total parameters of RealDGen with those of other methods, as this would provide additional context on scalability.

### Questions
Please refer to the Weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents a novel approach for generating realistic data for real-world image super-resolution (SR) tasks, addressing the limitations in the generalization of SR models due to the divergence between training data and real-world degradations. The authors propose a new framework called Realistic Decoupled Data Generator (RealDGen), which leverages unsupervised learning to decouple content and degradation from real low-resolution (LR) and high-resolution (HR) images. This decoupling is integrated into a diffusion model, allowing the generation of paired training data that more accurately reflects real-world conditions. The paper claims that RealDGen significantly improves the generalization ability of SR models across various backbone architectures.

### Strengths
1. The paper identifies the challenges in SR, particularly the gap between the synthetic degradations used in training data and the degradations in real-world images. By positioning the problem within the existing literature, the authors provide a strong motivation for their approach.
2. The core idea of the paper lies in decoupling content and degradation in real-world images to generate realistic data for SR, which is a novel approach for this task. The proposed approach, RealDGen, provides a scalable and adaptive solution for generating large-scale, realistic datasets. 
3. The authors conduct comprehensive evaluation of RealDGen across multiple SR models on different datasets. The results show consistent improvements in both PSNR-oriented and perceptual-oriented SR models, demonstrates the robustness of the proposed approach across a variety of settings.

### Weaknesses
1. The paper does not clearly define Real-world LR. Through experiments, we can see that the work is more focused on the SR problem in real-world photography, but the authors do not clearly define or explain it in the paper. This makes Figure 2 (b) somewhat difficult to understand. Specifically, the paper lacks a rigorous definition of what constitutes a 'real-world' low-resolution image, leading to ambiguity in the scope of the proposed method. The experiments seem to focus on photographic images, but the paper does not explicitly state whether the method is intended to generalize to other types of real-world LR data, such as those from surveillance or medical imaging. This lack of clarity makes it difficult to assess the true applicability of the method.
2. The overall presentation of this paper shoude be improved. The symbols in the formula do not correspond well to the figures. Eq.5 is not reflected in Figure 2. The colors used in Figure 1 (b) is somewhat confusion. The representation of 'G', 'S' in Figure 1 (a) should be 'N', 'K'. X_hr in Eq.5 is not explained. Line 179, 'for an HR image'. The inconsistencies between the text, figures, and equations hinder the reader's understanding of the proposed method. For example, the lack of correspondence between the symbols in the equations and the elements in the figures makes it difficult to follow the technical details of the approach. The use of confusing colors in Figure 1(b) further complicates the interpretation of the diagram. Furthermore, the missing explanation of X_hr in Eq. 5 leaves a crucial detail undefined, and the phrase 'for an HR image' at line 179 is vague and lacks context.

### Questions
How far is the performance of the model trained using the simulated data from that of the model trained using real collected data?

### Soundness
3

### Presentation
2

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
The authors present a new framework, Realistic Decoupled Data Generator (RealDGen), to generate realistic, large-scale data for real-world image super-resolution. The framework includes a contrastive learning-based degradation extractor and a reconstruction-based content extractor, enabling the effective capture of authentic degradation patterns and content features from real-world data. Utilizing the pre-trained extractors, the authors decouple the degradation and content features of given real low-resolution (LR) images, which are subsequently used as conditioning inputs for a Decoupled Diffusion Probabilistic Model (DDPM) to reconstruct the given images. Finally, by leveraging unpaired LR and HR datasets, the trained DDPM is able to generate realistic LR images, which exhibit degradation patterns closely resembling those found in real-world data. Extensive experiments across various SR models demonstrate that RealDGen consistently enhances SR performance on multiple real-world benchmarks. Detailed comments are listed below.

### Strengths
1. The proposed RealDGen framework effectively separates content and degradation features using a diffusion model, facilitating the generation of realistic low-resolution images that more accurately replicate real-world degradation patterns.
2. By utilizing a well-designed contrastive learning approach for degradation extraction and a reconstruction-based method for content extraction, the proposed RealDGen framework effectively decouples degradation and content features, thereby enhancing data realism and adaptability across different models.
3. Extensive experiments on multiple real-world SR benchmarks show that RealDGen consistently enhances the performance of various SR models, highlighting its practical effectiveness for real-world applications.

### Weaknesses
1. What is the technical contribution of the proposed method RealDGen? It seems that the effectiveness of the proposed methods mainly comes from the powerful diffusion model, and a similar idea of separating the degradation and content features has been investigated by previous methods [A]. Specifically, the novelty of the degradation and content extractors is not clearly articulated beyond the use of contrastive learning and reconstruction losses, which are not novel in themselves. The paper needs to better highlight the specific architectural or algorithmic innovations that enable superior performance compared to existing methods.
2. During the training phase of DDPM, the authors finetune partial parameters of the extractor. However, it is unclear the motivation and the effect of finetuning partial parameters. Please provide more discussions on why only partial parameters are finetuned and what impact this has on the learned representations. A more detailed analysis of the impact of this fine-tuning strategy on the quality of the generated images is needed.
3. The proposed method is tested on several SR benchmarks, but more experiments on diverse data with various types of degradation (e.g., motion or defocus blur [B, C]) would better showcase the framework’s generalization ability and robustness in a wider range of real-world scenarios. The current experiments are limited to a specific type of degradation, and it is unclear how the method would perform under different types of real-world degradations.
4. The proposed RealDGen relies on a large real LR dataset, which may be a potential limitation for scenarios where collecting such data is difficult or infeasible. It would be useful to investigate the effect of different amounts of real LR data on data generation. The paper should include an analysis of how performance degrades with reduced amounts of real LR data, providing a practical understanding of the data requirements.
5. The authors use a contrastive learning approach for the degradation extractor but do not provide enough detail on how different contrastive learning configurations (e.g., different negative sampling strategies) could affect the performance of data generation. It would be better to conduct more additional ablations to investigate the effect of different contrastive learning methods, such as [D]. Specifically, the paper should explore the impact of different negative sampling strategies and loss functions on the quality of the extracted degradation features.
6. Since the proposed method requires training a DDPM from scratch, the data generation cost is substantially high. Please provide a cost comparison with other existing methods to facilitate a clearer understanding of the computational demands and efficiency of the proposed approach. A detailed comparison of training time, memory usage, and inference time with other methods is necessary to assess the practical feasibility of the approach.

### Questions
What is the technical contribution of the proposed method RealDGen?

### Soundness
2

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
In this approach, a generative model is introduced to synthesize realistic low-resolution images, which are subsequently used as a training dataset to improve the performance of conventional super-resolution networks. In particular, unlike traditional methods, the proposed generative model is trained in an unsupervised manner using an unpaired training dataset, thus eliminating the dependency on high-quality ground truth images during the inference phase-a novel aspect of this approach. Furthermore, experimental results show that the generated low-resolution images exhibit improved accuracy compared to those produced by conventional methods, leading to superior performance in downstream tasks such as super-resolution.

### Strengths
This work introduces a novel generative model that eliminates the need for paired high-resolution and low-resolution images captured in real-world scenarios. Instead, by utilizing a synthetically generated training dataset from RealESRGAN, the proposed model effectively trains two key modules, E_deg and E_cont, which are designed to separate degradation and content in the given low-resolution (LR) images. This allows the model to generate realistic LR images using only a single LR input image, without the need for a corresponding high-resolution ground truth, setting it apart from conventional approaches. Given that collecting a large volume of real-world paired datasets is both time-consuming and costly, the proposed method, which bypasses the use of such paired real-world datasets, offers a significant advantage over traditional methods. Moreover, experimental results quantitatively and qualitatively demonstrate the superior performance of the generative model, further validating its efficacy compared to traditional approaches.

### Weaknesses
Although the proposed method removes the reliance on paired real-world datasets for both the training and inference phases, it still has limitations in fully demonstrating its performance. Specifically, the work lacks comprehensive experiments and detailed analysis. For further clarification, please refer to the questions outlined below.

Minor point: 
In line 87, the method by Park et al. is incorrectly described as a GAN-based approach. It actually utilizes normalizing flows for generation, and this should be revised accordingly.

### Questions
1.	The proposed method seems to share several ideas with Syndiff (Yang et al.). Could you please clarify the key contributions and differences between the two approaches?
2.	To train the E_deg and E_cont modules, the paper utilizes paired synthetic images generated by RealESRGAN. However, real-world low-resolution (LR) images can vary significantly from these synthetic images, which may hinder the accurate separation of degradation and content, potentially leading to suboptimal super-resolution (SR) performance on external datasets, as observed in Table 6. Could you clarify whether the proposed method is limited by the degradation distribution of RealESRGAN?
3.	Additionally, E_deg and E_cont are fine-tuned during the training of ReadDGen. As a result, real-world LR images presented at test time could bypass these modules and be directly passed through to the output. It would be useful for the authors to explain how these LR images differ from the ground truth (GT) LR images, and to demonstrate that the proposed generator can synthesize diverse LR samples. Moreover, more results before and after fine-tunign would be also beneficial.
4.	What would happen if a single, non-pretrained encoder were used instead of the E_deg and E_cont modules? Could you discuss the impact of this change to see whether separation of content and degradation is necessary?
5.	The SR results presented in the tables are somewhat lower than expected. Were these SR networks trained for 4x super-resolution (SR)? Please specify the scale factor. Additionally, it would be helpful to include more SR results using bicubic LR images for the baseline, as well as SR results trained on real-world SR datasets as oracles.
6.	While the adaptability of the proposed method is emphasized in the paper, the evidence provided to support this claim seems insufficient. It would be beneficial for the authors to include additional analysis and results to further substantiate this claim.

### Soundness
3

### Presentation
3

### Contribution
3
