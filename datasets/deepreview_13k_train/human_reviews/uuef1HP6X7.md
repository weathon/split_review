# IDIV: Intrinsic Decomposition for Arbitrary Number of Input Views and Illuminations

- Decision: Accept
- Scores: 5, 8, 8, 6, 6

## Abstract
Capturing geometric and material information from images remains a fundamental challenge in computer vision and graphics. Traditional optimization-based methods often require hours of computational time to reconstruct geometry, material properties, and environmental lighting from dense multi-view inputs, while still struggling with inherent ambiguities between lighting and material. On the other hand, learning-based approaches leverage rich material priors from existing 3D object datasets but face challenges with maintaining multi-view consistency.
In this paper, we introduce IDVI, a diffusion-based model designed to perform intrinsic decomposition on an arbitrary number of images under varying illuminations. Our method achieves highly accurate and multi-view consistent estimation on surface normals and material properties. This is made possible through a novel cross-view, cross-domain attention module and an illumination-augmented, view-adaptive training strategy. Additionally, we introduce ARB-Objaverse, a new dataset that provides large-scale multi-view intrinsic data and renderings under diverse lighting conditions, supporting robust training.
Extensive experiments demonstrate that IDVI outperforms state-of-the-art methods both qualitatively and quantitatively. Moreover, our approach facilitates a range of downstream tasks, including single-image relighting, photometric stereo, and 3D reconstruction, highlighting its broad applicability in realistic 3D content creation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a diffusion-based method that uses color images as input to predict material properties, including albedo, normal, metallic, and roughness. By leveraging the predicted material information and multi-view images, the method can support various applications such as relighting, material editing, photometric stereo, and inverse rendering. However, the proposed attention mechanism shows substantial similarity to prior work (Wonder3D), and the dataset lacks sufficient novelty and contribution.

### Strengths
1. This paper trains a diffusion model to predict material properties from color images, demonstrating strong performance compared to previous methods.

2. Extensive experiments validate the approach, showcasing its effectiveness across various applications.

3. The paper is well-organized and easy to follow.

### Weaknesses
1. The primary contribution of this paper is extending the original stable diffusion model from single-view, single-domain to multi-view, multi-domain processing. To accomplish this, the authors introduce a cross-view, cross-component attention mechanism. However, this attention method bears a strong resemblance to the multi-view, multi-domain attention proposed in the CVPR 2024 paper *Wonder3D*, which also extends stable diffusion to predict multiple domains. The authors have not cited or discussed *Wonder3D*, making such discussion necessary.

2. Given the similarities between the cross-view, cross-component attention in this work and *Wonder3D*, the other key contribution is a synthetic dataset designed for intrinsic image decomposition tasks. However, the dataset’s objects are sourced from Objaverse and rendered under various lighting conditions, a technique widely used in other studies. This limits the dataset’s novelty, making it challenging to consider it a significant contribution.

3. The supplementary video provides only two samples, offering limited insight. It would be highly beneficial to include additional comparisons.

### Questions
1. The process of 3D reconstruction from the generated multi-view images with material properties needs further elaboration. Providing more details on the reconstruction workflow, including how the material data (e.g., albedo, normal, metallic, roughness) contributes to the 3D recovery, would strengthen the clarity.

2. The functionality of the cross-view, cross-component attention mechanism also requires a more in-depth explanation. Figure 2 presents only a limited structural overview, so further details on the components and interactions within this attention scheme would greatly enhance understanding.

### Soundness
2

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
The paper proposes a method for intrinsic decomposition of object-centric images from single view or multi-view observations under varying lighting conditions, via training a diffusion model which is adapted to predicting intrinsic modalities via text prompt as switches, as well as utilizing cross attention mechanism between noised image latents of different modalities and views. The attention mechanism allows for the method to exploit dependency and consistency between intrinsic modalities and views, to achieve improved consistency and better disambiguate. The method is trained and evaluated on a new dataset rendered from Objaverse with physically-based materials and lighting, as well as real-world instances. The paper also includes ablation on model design, and applications to downstream applications.

### Strengths
[1] Novelty of the proposed method. The method borrows from previous methods on adapting diffusion models for intrinsic decomposition, but advances on improving the multi-view consistency by incorporating additional cross-attention mechanisms into the denosing UNet. Despite previous works which use similar attention mechanisms across multi-view inputs, the method is novel in its adaptation of the mechanism in this specific task, and is able to employ the mechanism to both cross-view and multi-task image latents.

[2] Impressive results on object centric intrinsic decomposition. The paper showcases impressive results in this task compared to some of the very recent works, demonstrating the effectiveness of the proposed attention mechanism. Moreover, special training strategy has been designed to avoid overfitting to multi-view inputs (VS single-view), and to improve quality by switching the noise scheduler. 

[3] Applications to downstream applications. The paper showcases applications in downstream applications to enable relight and material editing, and application as prior for optimization-based methods.

### Weaknesses
[1] Limited novelty. The major novelty of the paper is in its cross-attention module, which is nodel in this formulation but not entirely new due to applications in other tasks (e.g. LRMs) by previous methods. In this case, the theoretical contribution of the attention model is limited, and the pipelines offers few other contributions besides the attention module.

[2] Limited evaluation samples. The paper offers limited account of samples in evaluation, which do not cover challenging situations including (1) scenes of high secularity (e.g. a model car); (2) multi-view images of extreme lighting variation; (3) scenes with few views. More importantly, re-rendering results are not provided as a criterion to determine the challenging modalities including roughness and metallic, which in some cases may look correct but a slight error will contribute to artifacts in re-rendered results.

[2] Evaluation on more datasets. Indoor inverse rendering has been a particular challenging domain than object-centric settings. It would be great to see evaluations on indoor setting (e.g. RGBX), if the authors are able to access sufficient indoor inverse rendering data for training.

### Questions
[1] Please include results of re-rendering in all of the samples using estimated intrinsic modalities, as well as more samples especially in challenging conditions. 

[2] Failure cases are to be included as well.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces IDVI, a diffusion-based multi-view model to decompose the intrinsic properties of the scanned subjective in a view-consistent manner. It leverages the commonly used Stable-Diffusion model and upgraded it with a cross-view attention and cross-domain attention to align the latents across the view/domains. The model is trained on the also proposed dataset: ARB-Objaverse, a large scale datasets rendered from Objaverse assets using multiple lighting conditions,  and achieves impressive performance in various settings.

### Strengths
The results from the experiments cases looks impressive and thoroughly conducted. The model can produce high fidelity normal/albedo/material decomposed that outperforms the baselines by a large margin.

The model is designed in a good shape, by leveraging the power of cross-view and cross-domain attention which are proven to be very effective in previous works.

The proposed ARB-Objaverse can largely benefit to the inverse rendering community, if it will be released to the public.

### Weaknesses
Issues (Ranked by priority):

The model architecture of this work is somewhat a combination of attention modules that proposed by previous works (such as GeoWizard). While the combination of cross-view and cross-domain attention is effective, the novelty of the architecture is limited since it largely reuses existing components. The paper could benefit from a more in-depth analysis of how these attention mechanisms are adapted and optimized for the specific task of intrinsic decomposition, rather than simply combining them.

Reproducibility: The model is trained on the proposed dataset ARB-Objaverse, which is rendered in a large scale. It will be hard for the community to reproduce the training if the dataset is not publicity available. The paper should include more details about the rendering process, such as the specific software, lighting conditions, and camera parameters used to generate the dataset. This information is crucial for other researchers to replicate the results and build upon this work.
 
All of the experiments are conducted on object-centric cases only. While the model is trained by object data, it is also important to see how it can generalizes to other domains, for example indoor scenes (from which the RGB<->X is trained). The lack of evaluation on more diverse datasets limits the assessment of the model's robustness and generalizability.

The Attention Block part in figure 2 is a bit confusing, a few comments that might make it more intuitive: 
	(1) Add captions to explain what the images correspond to in the cross-component attention and cross-view attention (I would assume they are RGB/normal/material, and view 1/2/3 respectively)
	(2) Since the model is a combination of attention modules applied in different dimensions, the figure 2. in the paper of Group Normalization might be a good example of how to illustrate the operation in a very intuitive manner. 
	(3) It is not clear how the attentions are assembled in the block. Is it follow by the order of: cross-component attention->cross-view attention->cross attention-> feed forward? If so, please clarify it in the figure.

Figure 7: Please use consistent color tones to represent good / bad performance. i.e. inverse the color map of metallic and roughness comparison.

Missing Citations: 
	A couple of previous works such as NeRD, NeROIC, Neural-PIL also focuses on intrinsic decomposition on images under various illuminations; These works are also highly related to the proposed model.

### Questions
Overall, I think this paper is a complete work and has good performance. While it provides limited contributions on the technical part, it is a good practice of scaling up the system in the task of object intrinsic decomposition. I’m leaning to accept this paper. In addition to that, I’m happy to raise my score to a higher one if: 1) The authors will release the dataset/model and 2) The authors can show more comparisons on other domains.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents IDVI, a diffusion-based model for intrinsic decomposition that accurately estimates surface normals and material properties from multiple images under varying illuminations. It introduces a novel cross-view attention module and a new dataset, ARB-Objaverse, enabling robust training and demonstrating superior performance on various tasks, including single-image relighting and 3D reconstruction.

### Strengths
A new dataset is contributed. 
The paper presentation is good, with figures helpful for understanding. 
The results are pretty good.

### Weaknesses
1. The method mainly targets single objects, limiting the applications to scenes. How about performance on scenes? Could you please discuss whether the method can apply on scenes? Does it need re-training? What kind of scenes (indoor, outdoor, 360 scenes, or multi-object scenes) that it can solve, with some examples to demonstrate?
2. The method highly relies on supervised training data, while many other prior works are unsupervised/self-supervised. Could you please discuss and compare the pros/cons against self-supervised ones, and compare with them. E.g., DyNeRFactor, IntrinsicNeRF. 
3. Methods to compare are too few. There are many diffusion models to estimate normal, which should also be compared. Standard benchmarks such as MIT-Intrinsic should be tested to check whether the model is overfitted on training data. E.g. StableNormal. 
4. Figure 4 is compared to synthetic data, likely from the same dataset with training. That would be unfair to other methods. 
I am hesitant to give a positive score mainly because with a supervised method training on a proposed synthetic dataset, it seems to have limited technical contributions. Though the results are good, experiments and evaluations could be improved.

### Questions
See above.

### Soundness
3

### Presentation
3

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
This paper proposes to utilize diffusion priors for BRDF estimation from arbitrary number of images of an object. The key technical contributions including a novel transformer that uses attention mechanism to model relations between images across different views and different intrinsic components and a new training dataset that can be used for high-quality BRDF estimation. Experiments on several popular synthetic dataset show that the proposed method achieves very impressive inverse rendering results. Moreover, those results are multi-view consistent and can be used to optimize a high-quality relightable 3D model.

### Strengths
1. This is a technically sound paper with clear technical contributions. The novel dataset is built in a reasonable and thoughtful way. The novel attention module can successfully capture multi-view information and multi-channel information and shown to achieve better performance on synthetic datasets. 

2. From the results shown in the paper, the proposed method achieved very impressive inverse rendering results, with shadows and highlights being fully removed from the material parameters while preserving all texture details. In addition, the roughness and metallic values are piecewise smooth. It avoids the artifacts of only low roughness values near the specular highlights, which usually can observe in the optimization-based methods. 

3. Given that inverse rendering is a highly ill-posed problem, it makes a lot of sense to use a generative model to sample more visually appealing and higher quality results. I believe this paper is a solid and predictable step forward compared to RGB-X paper which only considers a single image.

### Weaknesses
1. Experiments on real data.

My major concern of this paper is lacking real-world data experiments. I specifically recommend Stanford-ORB dataset and , where we can easily get all the comparisons with state-of-the-art dense-view reconstruction methods, including geometry and relighting accuracy. Without that experiment, it is very difficult to verify if the proposed method actually generalize well to real-world data.

2. The method section can be improved with more necessary details.

I had a little bit difficulties to under Method 3 and Figure 2. I believe I eventually understood it but felt some modifications can make it easier to read.

In Figure 2, I assume D equal to 3 and presents the number of intrinsic components. This can be explicitly explained in Figure 2. The blue, green, dark green blocks look a bit too similar and we may consider using color with stronger contrast. Also the two attention matrix has very different color and it is unclear what the colors represent. For the top half of Figure 2, it is unclear how the image latents are combined with noisy triplet latents. I assume it is a concatenation. Also for the noisy triplet latent, it may be more informative to keep some original image information so we know what it represents.

Line 246: Here, it is mentioned that each triple latent is concatenated with the Gaussian noise. Do we actually mean "added" instead of concatenated?

Illumination-augmented training: it is a bit weird to me what we sent images with different illumination to the diffusion model as during real-world data capture, we usually assume the lighting is unchanged. I wonder how this training strategy may influence the generalization on real data.

3. Quality of reference should be improved.

For the optimization-based inverse rendering, authors skipped a large number of recent works solving this problem, such as Nerfactor, NeRD, Neural-PIL, nvidffrec, nvdiffrecmc, MII, Neural-PBIR  and also many recent relightable 3D Gaussian papers. For learning-based inverse rendering, there are also many more SVBRDF estimation, lighting estimation, intrinsic decomposition papers that should be cited.

### Questions
Overall I like this paper and hope that it can be accepted. My major question about the paper is experiments on real data. I hope this paper can include experimental results on Stanford-ORB and Objects with lighting datasets to verify the trained model's generalization ability.

### Soundness
3

### Presentation
2

### Contribution
3
