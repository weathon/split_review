# Unleashing the Power of Deep Dehazing Models: A Physics-guided Parametric Augmentation Net for Image Rehazing

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5, 5

## Abstract
Image dehazing faces significant challenges in real-world scenarios due to the large domain gap between synthetic and real-world hazy images, which often hinders dehazing performance. Collecting real-world datasets is particularly difficult, as hazy and clean image pairs must be captured under identical conditions. To address this, we propose a Physics-guided Parametric Augmentation Network (PANet) that generates realistic hazy and clean training pairs, enhancing dehazing performance in real-world applications. PANet consists of two components: a Haze-to-Parameter Mapper (HPM), which projects hazy images into a parametric space representing haze characteristics, and a Parameter-to-Haze Mapper (PHM), which converts resampled haze parameters back into hazy images. By resampling individual haze parameter maps at the pixel level in the parametric space, PANet generates diverse hazy images with physically explainable haze conditions that are not present in the training data. Our experimental results show that PANet effectively enriches existing hazy image benchmarks, significantly improving the performance of current dehazing models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the real data-scarcity issue for dehazing: that real-world haze is often dense and non-homogeneous, which is difficult to synthesize using traditional image formation models. The proposed haze data augmentation technique (PANet) adopts a hybrid approach, combining the strengths of both data-driven or physics-based methods. It first estimates haze parameters from clean-hazy image pairs using Haze to Parameter Mapper. In the Parameter to Haze mapper: it leverages physics-guided scattering model to generate initial hazy images. It further incorporates a Data-driven Haze Refiner (DHR) to refine this initial hazy images to enable better realism and accuracy.

### Strengths
The paper addresses a practical problem in dehazing: real-world haze is often dense and non-homogeneous, which is difficult to synthesize purely using physical scattering image formation models.

The HPM+PHM cyclic approach for unsupervised learning of intermediate haze parameters is practically effective.

Applying the proposed augmentation on selected Dehazing methods leads to notable improvement in dehazing quality on real images and few synthetic test images.

The approach is data efficient, in which it can be trained on a small dataset of as few as 50 images. The hybrid formulation leads to fewer unwanted artifacts than GAN based augmentation approaches.

### Weaknesses
Limited technical novelty: The approach is derived from existing, established methods for cyclic image-to-image mapping, specifically built upon CycleGAN. The core idea of using a cyclic mapping between haze parameters and hazy images, while practically effective, lacks significant innovation beyond the existing framework.

Dataset limitations: The analysis and evidence for validating the idea are limited, as the validation relies on a small real-world dataset (NH-Haze20) for training, with only 50 training pairs and 5 testing pairs. This limited dataset size may restrict the generalizability and effectiveness of PANet in handling the diversity of real-world haze conditions. The cross-dataset evaluation, while helpful, does not fully address the concern that the model's performance may be tightly coupled to the characteristics of the NH-Haze20 dataset. The lack of a large-scale real-world dataset for training and validation is a significant limitation.

Computational footprint and scalability: PANet is a relatively complex architecture with multiple components, including encoders, decoders, a depth refinement module, and a data-driven haze refiner. This complexity requires significant FLOPs and increases the computational cost and training time compared to simpler augmentation techniques. Additionally, the paper does not thoroughly discuss how well PANet scales to larger datasets (on the order of 10^4 to 10^6 images), which is a critical consideration for practical applications. The memory requirements for training and inference are also not clearly defined, which is important for reproducibility and adoption.

Few writing quality issues: There are some quality issues in writing, such as an equation reference error on line 238 and typos like “pixel-wisely” on line 307. These issues, while minor, detract from the overall clarity and professionalism of the paper.

Outdoor vs. indoor image improvement: The improvement on outdoor hazy images appears to be higher than on indoor hazy images. This observation should be discussed further, with an analysis of why the method performs differently in these two scenarios. The paper should explore the potential reasons for this discrepancy, such as differences in haze characteristics or image content.

Qualitative results clarity: It is not clear which of the three dehazing models was used to generate qualitative results, such as those in Figs. 6 and 7. The lack of clarity makes it difficult to assess the effectiveness of the proposed augmentation technique across different dehazing models.

Choice of augmentations: Some choices of augmentation, such as “reverse its haze location,” seem less realistic, as they are opposite to the general nature of haze (which typically increases with distance). It would be interesting to analyze the effect of excluding such augmentations and whether they contribute to improved performance or introduce artifacts.

Dependency on DHR: The results in Table 3 suggest that the entire approach fails if the Depth Haze Refiner (DHR) is not included, which is surprising and questions the method’s utility. There should be an analysis with quantitative and qualitative results on the effect of the Depth Estimator and DRM on the performance. Additionally, extensive visualizations showing the outputs of the depth estimator, DRM, beta(z), and final t(z) are recommended. The strong dependency on DHR raises concerns about the robustness of the overall approach.

Reliance on pre-trained depth estimator: PANet relies on a pre-trained depth estimator (RA-Depth) to estimate depth maps from clean images, which may pose a potential weakness. This estimator may not generalize well to unseen images, especially those with characteristics different from its training data. This generalization issue may not always be addressable by training a DRM, which could lead to inaccurate depth estimations and negatively impact the accuracy of the physical scattering model used in PANet, affecting the realism of the generated hazy images. The paper should include an analysis of the sensitivity of the method to the quality of the depth maps.

Baseline model performance: The results of three baseline dehazing models on real images from the RTTS dataset appear to be quite poor, with significant artifacts. It would be interesting to know whether any existing dehazing model can yield reasonable results on the RTTS dataset. The paper should investigate why the baseline models perform so poorly and whether this is a limitation of the models themselves or the dataset.

Selection of dehazing models: How were the three dehazing models selected? Additionally, it might be interesting to analyze any improvements observed when using other recent dehazing models. The paper should justify the choice of these specific models and explore the potential benefits of using more advanced dehazing techniques.

Risk of overfitting: The potential for overfitting needs to be carefully considered. While PANet shows improvements in dehazing performance on a few similar datasets and one additional real dataset, the use of augmented data can increase the risk of overfitting, especially with a limited original dataset. The paper should include a more detailed analysis of the potential for overfitting and how it is mitigated.

Additional metrics: Including additional no-reference metrics, such as FADE, BRISQUE, NIMA, and US, for the RTTS datasets would enable a fuller comparison with RIDCP (Wu et al., 2023). The paper should provide a more comprehensive evaluation using a wider range of metrics.

Evaluation on popular benchmarks: The proposed approach could also be evaluated on popular dehazing benchmarks like the SOTS-Outdoor and SOTS-Indoor datasets. This would provide a more standardized comparison with existing methods.

Evaluation under challenging conditions: Optionally, it might be interesting to test PANet under extremely challenging haze conditions, such as dense fog or heavy smog. This would demonstrate the robustness of the method under more extreme conditions.

### Questions
Please address weaknesses above.

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
5

### Summary
This paper introduces the Physics-guided Parametric Augmentation Network (PANet), designed to improve real-world image dehazing. 

PANet combines physics-based modeling with data-driven techniques to generate diverse hazy images, aiming to bridge the gap between synthetic and real-world hazy datasets. 

By mapping haze characteristics into a parametric space, PANet can resample parameters and generate new, physically realistic hazy images.

### Strengths
- physics-guided + data-driven make sense. 

- The physics-guided and parametric approach to generating realistic hazy images also makes sense.

### Weaknesses
 - The progress of daytime dehazing or defogging has been significant over the past 10 years. These methods can handle many problems, particularly when the haze or fog is relatively thin. Non-uniform haze/fog is also not a significant issue, as many methods can handle it well. (If there is any disagreement, the paper should provide evidence of existing methods failing to deal with non-uniform haze.) The main challenge of dehazing arises when the haze/fog is significantly thick. Unfortunately, the proposed method does not address this thick haze/fog problem specifically, as evidenced by the results. Moreover, the proposed method has no specific mechanism or treatment in dealing with the thick haze/fog and its characteristics.

- The qualitative experimental results do not show that the proposed method outperforms the existing methods. 
In Fig. 1 and 6, when the fog/haze is thick, the method still suffers from it and suffers from colour shift.

- The proposed method does not have any specific features that differentiate it from existing methods in terms of the haze/fog problem it aims to solve. The results presented in the paper could be achieved by existing methods, including non-deep learning methods, with comparable quality.

- Missing citation and dataset in [1]
[1] Structure Representation Network and Uncertainty Feedback Learning for Dense Non-Uniform Fog Removal

### Questions
1. For the colour shift issue, what is the reason?

2. It seems for the sky, white object and road, the results are not promising, what is the reason?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Collecting real-world hazy-clean image pairs is particularly difficult and the authors tried to address this issue by proposing PANet. PANet can generate realistic hazy and clean training pairs, thus enhancing dehazing performance in real-world applications.

### Strengths
1. the key idea of performing parametric augmentation to generate additional haze patterns is good.
2. the experimental results are promising.
3. the paper is well-prepared and easy to follow.

### Weaknesses
1. the depth refinement module (DRM) is employed to refine the initial depth map, which means the depth estimation is not accurate enough in some cases. Have the authors attempted to utilize other methods of depth estimation which are more accurate? The reliance on a pre-trained depth estimator introduces a potential bottleneck, as the accuracy of the generated haze is directly tied to the quality of the initial depth map. Furthermore, the DRM is trained on a specific dataset, raising concerns about its generalization capability to diverse real-world scenarios. It is unclear how well the refined depth maps capture the actual depth variations in complex scenes, and this could lead to unrealistic haze synthesis.
2. the choice of baseline method lacks convincingness. The three baseline models, DW-GAN, Dehamer, and FocalNet are primarily utilized for synthetic data (i.e., SOTS-indoor, SOTS-outdoor). Can this method be applied to real-world dehazing models (e.g., RIDCP DAD)? The selection of baseline methods appears to favor models trained on synthetic data, which may not accurately reflect the performance of the proposed method in real-world conditions. The lack of comparison with state-of-the-art real-world dehazing models raises doubts about the practical applicability of the proposed approach. Specifically, the absence of comparisons with methods explicitly designed for non-homogeneous haze is a significant oversight.
3. Comparisons with methods such as RIDCP DAD PTTD, which are oriented towards real image dehazing, are lacking. In addition, by observing the images, the qualitative results in Figure 7 contain some artifacts. The qualitative results, while showing some improvement, still exhibit visible artifacts, especially in regions with complex textures or fine details. This suggests that the generated haze, despite the refinement, might not be entirely realistic and may introduce distortions in the dehazed images. The lack of comparison with real-world dehazing methods makes it difficult to assess the true effectiveness of the proposed approach.
4. the parametric augmentation of haze is not flexible, can the value of $\alpha$ be continuous? What's the range of values for $\alpha$? What parameters were used in the experiments section? The parametric augmentation strategy, while promising, lacks detailed explanation regarding the range and continuity of the parameters used. The absence of specific information regarding the values of $\alpha$ and other relevant parameters used in the experiments makes it difficult to reproduce the results and assess the robustness of the method. It is also unclear how the method handles different types of haze, such as non-uniform or color-dependent haze.
5. the experiments section is not sufficiently comprehensive. For real-world hazy environments, only RTTS is tested and only NIQE and PIQE are adopted as the metrics. The experimental validation is limited in scope, with only one real-world dataset (RTTS) being used for evaluation. The reliance on only two metrics, NIQE and PIQE, which may not fully capture the perceptual quality of dehazed images, raises concerns about the robustness of the findings. The lack of a more comprehensive evaluation, including additional real-world datasets and metrics, limits the generalizability of the conclusions.
6. some typos: e.g., Ln237.

### Questions
Please check the weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a Physics-guided Parametric Augmentation Network (PANet) to address the domain gaps between synthetic and real-world haze data. PANet is designed to generate real haze images along with their corresponding clean pairs. It consists of two components: the Haze-to-Parameter Mapper (HPM), which projects hazy images into a parametric space, and the Parameter-to-Haze Mapper (PHM), which maps haze parameters back to hazy images.

### Strengths
1. The paper tries to address a meaningful problem: bridging domain gaps between synthetic and real-world data. 
2. The structure and presentation of the paper are clear and well-organized.

### Weaknesses
1. The authors do not account for the idealized assumptions of the physical scattering model, which may lead to inaccuracies in haze removal. Specifically, the model assumes a homogeneous atmosphere and neglects complex scattering effects, which are often present in real-world scenarios. This simplification can lead to a mismatch between the synthetic haze generated by the model and the actual haze found in natural images, limiting the effectiveness of the proposed augmentation technique.
2. The importance of using real-world natural haze images, beyond the non-homogeneous haze created by fog machines, is overlooked. The fog machine generates haze with a specific particle size distribution and density, which may not accurately represent the diverse range of atmospheric conditions and particle compositions found in real-world haze. This discrepancy can result in a model that is biased towards the characteristics of the fog machine-generated haze, hindering its ability to generalize to real-world scenarios.
3. The proposed approach heavily relies on existing datasets, which lack diversity (environment, light condition, etc.). The limited variations in environmental conditions and lighting within the existing datasets constrain the ability of the model to learn robust haze representations. This lack of diversity can lead to overfitting to the specific characteristics of the training data, limiting the model's performance when applied to images with different environmental and lighting conditions.

### Questions
1. The physical scattering model is an idealized approximation and may not accurately represent real-world haze, which can still cause domain gaps. Have the authors considered this limitation, and are there any solutions to mitigate it?
2. The training dataset NH-Haze20 is generated using a fog machine, which creates domain discrepancies between these images and those with natural real-world haze. Even with the proposed augmentation method, this gap may persist. Do the authors have any explanations or proposed solutions for this issue?
3. In Figures 6 and 7, all qualitative results appear to be zoomed-in versions. Could the authors provide full images, particularly for real-world natural images with dense haze? These images should represent natural haze rather than artificial fog.
4. The augmented dataset is based on NH-Haze20 and similar real-world datasets, which are limited and lack diversity (e.g., environmental and lighting conditions). How do the authors plan to address the reliance on these existing datasets?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a data augmentation pipeline specifically designed for real-world dehazing. This method utilizes a physical scattering model of haze, adjusting model parameters estimated by neural networks. For each real-world training patch, the approach can generate an arbitrary number of new patches with varying haze densities. The authors validate the proposed method by demonstrating its capacity to enhance the real-world dehazing performance of three state-of-the-art dehazing techniques across four datasets.

### Strengths
This work possesses several strengths:

- It effectively enhances the richness of real-world dehazing training data, thereby improving the real-world dehazing performance of existing methods.

- It allows users to create an arbitrary number of new patches with varying haze densities.

### Weaknesses
However, the work exhibits several shortcomings:

- The contributions appear insufficient. Although it shows slight improvements over [1], the core concept remains quite similar. The claimed distinctions, such as the GAN structure and global haze adjustment, can be categorized as engineering problems rather than scientific advancements. The proposed method, which employs simple ResBlocks and pixel-wise haze adjustment, may be viewed as incremental. The use of ResBlocks, while effective, is a standard practice, and the pixel-wise haze adjustment, while providing fine-grained control, does not introduce a fundamentally novel approach to haze manipulation. The method's reliance on a physical scattering model, while grounded in theory, is not a unique contribution, as many dehazing methods leverage similar models. The novelty of the approach is further diminished by the fact that the parameter estimation is done by a neural network, which is a common practice in the field.

- The proposed method has not been compared with existing data augmentation techniques for dehazing via DeHamer and DW-GAN on the other three datasets. While such augmentation methods could enhance existing dehazing approaches, it is essential to assess the generalizability of these improvements. However, the work neglects to compare its method against these data augmentation techniques for more general cases. This lack of comparison makes it difficult to ascertain the true advantage of the proposed method over existing augmentation strategies. The absence of these comparisons raises concerns about whether the observed improvements are specific to the datasets used or if they represent a more generalizable enhancement.

- The manuscript requires revision. For instance, L237 references Eq. ??. Additionally, Figures 2 and 3 are nearly identical, differing only in minor content details. The lack of clarity in the manuscript, particularly with the incorrect equation reference, undermines the credibility of the work. The redundancy of Figures 2 and 3 suggests a lack of careful presentation, which detracts from the overall quality of the paper.

- The work evaluates visual performance on RTTS, which is designed for haze detection. It would be beneficial to conduct experiments on dehazing in the context of object detection to assess how real-world dehazing after data augmentation impacts downstream object detection tasks. The current evaluation on RTTS does not directly measure the impact of the proposed method on downstream tasks, which is a critical aspect of real-world dehazing applications. The absence of object detection experiments limits the practical relevance of the results.

- According to Table 5, a larger number of augmented data pairs improves dehazing performance, yet the authors stop at 600. It would be useful to evaluate the convergence of dehazing performance relative to the number of augmentations. The lack of a thorough analysis of the convergence behavior of the proposed method with respect to the number of augmented data pairs leaves a gap in understanding the method's optimal performance and its practical limitations.

### Questions
The questions have been outlined in the section on weaknesses. Considering the aforementioned strengths and weaknesses, I would recommend a borderline reject, with the potential for reconsideration if the listed issues are adequately addressed.

### Soundness
2

### Presentation
3

### Contribution
2
