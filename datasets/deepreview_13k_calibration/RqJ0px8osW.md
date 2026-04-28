# A unified lightweight complex scenes-oriented network for infrared and visible image fusion

- Decision: Reject
- Avg Score: 6.80
- Scores: 5, 5, 8, 8, 8

## Abstract
Existing infrared and visible image fusion (IVIF) techniques typically integrate the useful information from different modalities within the ideal conditions. Nevertheless, current state-of-the-art IVIF methods are ineffective when facing complex scene interferences such as bad weather, low light, and high noise, and they typically need to be used in conjunction with other de-interference baselines, which inevitably resulting in the high memory costs and error accumulation, thus yielding sub-optimal fusion results. To address these challenges, We propose a unified lightweight real-time IVIF network for multiple complex scenes. We conducted a theoretically thorough analysis of modal degradations in the frequency domain, leveraging the complementary strengths of both modalities to enhance network learning. Our method facilitates the extraction of critical features even amidst significant pixel interference. For reconstructing fusion results, we introduce a spatial domain branching strategy which significantly improves the local detail resolution, thereby mitigating potential omissions from frequency domain analysis. Extensive qualitative and quantitative experiments demonstrate that our framework excels in handling multiple complex scenes, while maintaining real-time computational efficiency for prompt image processing applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper addresses the limitations of current infrared and visible image fusion (IVIF) methods when applied to complex scenes with interferences such as rain, noise, and low-light conditions. The authors propose a unified, lightweight IVIF framework that integrates image restoration and fusion in real time, enabling high-quality fusion without the need for pre-processing. Using Fourier domain techniques, the framework captures amplitude information from infrared and visible images and combines these with spatial domain data to maintain clarity and reduce interference. The paper includes extensive qualitative and quantitative experiments to demonstrate the framework’s efficiency and robustness, with results showing improvements in both computational efficiency and image quality across diverse scenes.

### Strengths
1.	The method combines frequency and spatial domain information, effectively separating critical scene features and suppressing interference by processing amplitude and phase components in the frequency domain. For example, in low-light or adverse weather conditions, the amplitude information of images is often disrupted (e.g., reduced brightness or increased reflections), while the phase information, reflecting structural aspects of the image, remains relatively stable. By using the amplitude of infrared images to guide the restoration of visible images and leveraging the phase information from visible images to enhance infrared images, the method achieves an optimal balance between the two modalities, ensuring clear detail retrieval in noisy scenarios.
2.	The lightweight design of the method allows for real-time processing with minimal computational resources, which is critical for practical applications. The paper highlights that the model processes a 640x480 image in just 0.033 seconds, demonstrating exceptional efficiency. This efficiency makes it suitable for systems requiring real-time processing, such as autonomous vehicles or industrial monitoring, further broadening its potential application scope.

### Weaknesses
1.	The mutual guidance mechanism relies on the complementary characteristics of infrared and visible light, such as using the infrared amplitude to guide the visible amplitude, and vice versa. However, when the data quality of one channel is poor (for instance, when the thermal radiation information of the infrared image is weak), the effectiveness of this guidance mechanism may be significantly limited. In such situations, the original amplitude or phase information might not provide sufficient valuable features to complement the other channel, resulting in suboptimal fusion performance in certain scenes. This is particularly concerning in scenarios where the infrared sensor might be occluded or malfunctioning, leading to a complete lack of useful thermal data, which would render the guidance mechanism ineffective.
2.	The data used in the experiments section was selected from existing datasets (MSRS, AWMM-100k). However, the MSRS training set contains only 1,083 pairs of images, so randomly selecting 1,000 pairs from this limited set seems unnecessary. If the authors intend to augment MSRS, they should uniformly apply Gaussian noise and pixel intensity scaling across the entire MSRS training set. The lack of a clear justification for this specific subset selection raises questions about the representativeness of the training data and the generalizability of the model.
3.	In Table 1, the authors list non-reference evaluation metrics; however, both SF and AG are gradient-based metrics, which are typically highly correlated. The lack of an information theory-based non-reference metric, such as entropy, is notable. In Table 2, the reference-based metrics include SSIM, but SSIM is already incorporated into the loss function during training for all four tasks, which I believe makes the comparison less fair. Additionally, there is insufficient explanation for why the authors used MSEC’s reconstruction structure in the overexposure scenario. The choice of SSIM as a metric, despite its use in training, introduces a potential bias, and the absence of a more diverse set of metrics limits the robustness of the evaluation.
4.	Did the models of the other comparison methods undergo specific training on the dataset proposed by the authors? In fact, other methods are typically trained only on the original MSRS training set. If the evaluation metrics for these comparison methods are obtained by testing their open-source models on the data across these four scenarios, while the authors’ proposed model was specifically trained for each scenario, then I believe the experimental results lack sufficient credibility. The lack of clarity on the training protocols for comparison methods makes it difficult to ascertain if the performance differences are due to the proposed method's superiority or simply a result of a more tailored training regime.
5.	The comparison methods listed in the experiments section require only a single model to handle all four scenarios, while the proposed method requires separate training for each scenario. In real-world applications, however, rain and overexposure could occur simultaneously. In such cases, the other methods can generalize directly using their models, but which model output would the proposed method select as the result? If the model trained for rain is chosen, would it affect the handling of the overexposed areas? This raises concerns about the practical applicability of the proposed method in complex, real-world scenarios where multiple types of degradation can occur concurrently.

### Questions
Please rebuttal according to the weaknesses item by item.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents a unified lightweight network designed for infrared and visible image fusion (IVIF) that aims to address the limitations of existing techniques in complex scene conditions such as bad weather, low light, and high noise. The authors conduct a frequency domain analysis of modal degradations, leveraging the complementary strengths of both infrared and visible modalities. A novel spatial domain branching strategy is introduced to enhance local detail resolution in the fusion results. The paper claims extensive qualitative and quantitative improvements in handling complex scenes while maintaining real-time computational efficiency.

### Strengths
1. The writing of this paper is easy to understand.
2. The description of the methodology is detailed.
3. The motivation of the methodology is detailed.

### Weaknesses
1. The proposed method based on exchanging amplitude and phase lacks novelty.
2. The advantages of the paper are not significant when considering the overall computational cost of the results.
3. The paper should also be compared with other SOTA methods, such as MURF (Xu et al., 2023), SegMiF (Liu et al., 2023), DDFM (Zhao et al., 2023), and EMMA (Zhao et al., 2024).

### Questions
What specific types of degradation were most challenging for previous methods, and how does DSPFusion overcome these issues?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This model adopts a new frequency-domain perspective to solve the IVIF problem in complex scenes, and uses a multimodal information interaction guidance module that not only utilizes frequency-domain information but also integrates spatial information to more comprehensively and effectively extract image details, compensating for the loss of details that may be caused by relying solely on frequency-domain information. The model has been extensively experimentally validated in four complex scenarios, including noise, rainy weather, overexposure, and low lighting, achieving excellent image fusion quality. Its framework integrates image restoration and fusion, avoiding the problems of error accumulation and irrelevant feature introduction that may occur in traditional two-stage processing methods.

### Strengths
1. This paper proposes a multi-modal interactive guidance mechanism that combines frequency domain and spatial domain learning, which effectively enhances the effect of infrared and visible light image fusion in complex scenes. Through mutual guidance, the amplitude of the infrared image and the phase information of the visible light image are used to achieve richer feature extraction and fusion between different modalities.

2. Through a large number of qualitative and quantitative experiments, the article demonstrates the significant performance improvement of this method in removing interference information and restoring image details in complex scenes such as noise, rain, overexposure, and low light. Outperforms existing state-of-the-art methods in multiple metrics.

3. The network design emphasizes lightweight and efficient computing, and can achieve real-time image fusion under limited computing resources, which is a very important advantage in practical applications. Experimental data shows that this method only takes 0.033 seconds for each fusion when processing images of 640×480 size.

### Weaknesses
Although the motivation of this article is relatively clear and attempts to solve the problem of image fusion in harsh environments, there are still some shortcomings as follows:
1. First of all, the method proposed by the author does not seem to have any theoretical innovation. Why does the method in the article achieve better performance than image restoration?
2. Although a combination of frequency domain and spatial domain is proposed to extract key features, this method does not have a clear optimization strategy for how to reduce unnecessary redundant information. In complex scenes, this may cause non-critical pixels to be mistaken for valuable information, thereby affecting the fusion effect.
3. The motivation of the article emphasizes the use of frequency domain learning to enhance information extraction under interference conditions, but does not fully consider the important balance of frequency domain and spatial domain information. In the IVIF task, relying solely on the frequency domain may lead to inaccurate processing of spatial details in complex scenes, thereby affecting the fusion quality.

### Questions
My questions is already stated in the Weaknesses section.

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
This paper proposes a unified and lightweight framework designed for real-time infrared and visible image fusion in environments characterized by complex interferences from a frequency domain perspective. It tackles the issue of complex scenes fusion problems, such as adverse weather, low-light environments, and noisy fusion. Authors introduce a multi-modality information interaction guidance module for multi-modality feature interaction and extraction. Extensive fusion experiments in four complex conditions: noise, rain, overexposure, and low-light, verified the effectiveness of the proposed method in dealing with interfering information.

### Strengths
(1) This paper introduces a unified framework for real-time infrared and visible image fusion in different complex scenes, this is the first work of addressing complex scenes image fusion problems in frequency domain. 

(2) The paper proposes a multi-modality interactive guidance mechanism within the Fourier domain, which efficiently extracts and restores useful features from degraded pixels by leveraging the complementary strengths of different modalities.

(3) The fusion performance of this work is very impressive. Extensive complex scenes fusion experiments cover rain, overexposure, low-light, and noisy demonstrate this method outperforms the state-of-the-art fusion methods in both subject and object evaluations.

### Weaknesses
(1) In the caption of figure 5, it is recommended to add the words “complex scenes”.

(2) Section 4.4 and 4.5 could be combined as one part.

(3) The source code is suggested to be public.

### Questions
n/a

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
This paper proposes a new IVIF method designed to be robust in complex scenes, including rain, noise, and under-exposed conditions. The core concept is that the amplitude component of infrared images and the phase component of visible images provide complementary modal information for IVIF, and interactively fusing these components enhances fusion quality in challenging scenarios. Specifically, the method decomposes the infrared and visible images into amplitude and phase components by applying the Fourier Transform, thus transferring them into the frequency domain. Based on this, a “multi-modality interactive guidance mechanism” is introduced to fuse the frequency-domain information.

### Strengths
+ The idea of using frequency domain information to address IVIF in complex scenes is interesting. 
+ The paper is well-organized, with a logical flow between sections. The language is clear, and the content is presented in an easily understandable manner. 
+ The proposed methods are grounded in theoretical explanations, and the experiments conducted are fair and comprehensive.

### Weaknesses
- Despite the demonstrated effectiveness, similar methods have been widely applied in other fields, such as low-light image enhancement and image denoising. For example, “FourLLIE: Boosting Low-Light Image Enhancement by Fourier Frequency Information” transforms the image into the Fourier domain and utilizes an estimated amplitude map for enhancement. How does the proposed method improve upon or differ from these existing methods in the IVIF task? Specifically, the paper should clarify how the proposed multi-modal interactive guidance mechanism leverages the unique characteristics of infrared and visible light modalities in the frequency domain, beyond what is already achieved in single-modality tasks.
- The authors claim that existing IVIF methods fail in complex scenes because they may misinterpret interference features as valuable. However, the proposed Spatial Domain Module also fails to avoid erroneous features. The convolution operations in this block extract all local features from the input image, including both degradation artifacts and valuable features. This could lead to the mistaken interpretation of degradation artifacts as valuable features, resulting in error accumulation or the introduction of incorrect features during the fusion stage. Max pooling cannot fully address the issue of misextracting degradation artifacts, especially when these artifacts have high intensity, as max pooling may still retain these distracting features as significant ones. More explanation is needed regarding how the network is trained to differentiate between useful features and degradation artifacts within the spatial domain, and how the loss function guides this process.
- The final fusion result is obtained by directly combining the source image information with the feature maps. Wouldn't this affect the fusion results, as interference features might also be added to the final image? The paper needs to discuss the potential for the introduction of artifacts or noise from the source images into the final fused output, and how the proposed method mitigates this issue. A more detailed explanation of how the network learns to selectively combine information from the source images and the feature maps would be beneficial.
- In Figure 5 (“FFT Domain”), “DWT: Discrete Wavelet Transform” is labeled, but I could not locate it in the figure. Furthermore, there seems to be no explanation of DWT in the paper. Please clarify it.
- Minor issues: There is a typo in Line 018: “, We.” Additionally, in the second column of the “Rain” table in Table 2, the value for LRRNet (“0.8050”) should also be highlighted in red.

### Questions
- Same as the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
