# LocDiffusion: Identifying Locations on Earth by Diffusing in the Hilbert Space

- Decision: Reject
- Avg Score: 5.80
- Scores: 6, 6, 8, 3, 6

## Abstract
Image geolocalization is a fundamental yet challenging task, aiming at inferring the geolocation on Earth where an image is taken. Existing methods approach it either via grid-based classification or via image retrieval. The geolocalization accuracy of these methods is constrained by the choice of geographic grid cell sizes or the spatial distributions of the retrieval image/geolocation gallery, and
their performance significantly suffers when the spatial distribution of test images does not align with such choices. To address these limitations, we propose to leverage diffusion models to achieve image geolocalization with arbitrary resolutions. To avoid the problematic manifold reprojection step in diffusion, we developed a novel spherical positional encoding-decoding framework, which encodes points on a spherical surface (e.g., geolocations on Earth) into a Hilbert space of Spherical Harmonics coefficients and decodes points (geolocations) by mode-seeking. We call this type of position encoding Spherical Harmonics Dirac Delta (SHDD) Representation. We also propose a novel SirenNet-based architecture called CS-UNet to learn the conditional backward process in the latent SHDD space by minimizing a latent KL-divergence loss. We train a conditional latent diffusion model called LocDiffusion that generates geolocations under the guidance of images – to the best of our knowledge, the first generative model to address the image geolocalization problem. We evaluate our LocDiffusion model against SOTA image geolocalization baselines. LocDiffusion achieves competitive geolocalization performance and demonstrates significantly stronger generalizability to unseen geolocations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a latent diffusion model called LocDiffusion for image geolocalization, aiming to predict precise geolocation on Earth from images with arbitrary resolutions. It proposes a novel spherical position encoding method, Spherical Harmonics Dirac Delta (SHDD) Representation, which encodes geocoordinates on Earth's spherical surface into a Hilbert space of Spherical Harmonics coefficients. The model then decodes these geolocations via a mode-seeking approach. A SirenNet-based architecture is used to learn the conditional backward process in the latent SHDD space by minimizing a latent KL-divergence loss. Experiments are conducted on the Im2GPS3k and YFCC-26k datasets, with comparisons to state-of-the-art methods like GeoCLIP.

### Strengths
1. This work is the first generative model addressing the image geolocalization problem, offering a fresh perspective to the field.
2. The design of the Spherical Harmonics Dirac Delta (SHDD) Representation is innovative and tailored to the geocoordinate system, which is both novel and meaningful.
3. The paper is well-written and generally easy to follow.

### Weaknesses
1. The performance gains over state-of-the-art methods, particularly GeoCLIP, are not well demonstrated. In Table 1, the proposed method achieves the best results in 5 out of 10 categories across two benchmarks, but the improvements are marginal, with differences of less than 0.5. Additionally, the method significantly underperforms in key categories like Street, City, and Region, raising concerns about its robustness across different geolocalization tasks. The small performance gains, especially when considering the increased complexity of a diffusion model, make it difficult to justify the approach over simpler, more established methods. The lack of substantial improvement in critical categories suggests that the proposed method may not generalize well across diverse geographical contexts.

2. The paper lacks a detailed analysis of computational efficiency, particularly in terms of training and inference speed, compared to existing methods. Since this is the first application of a diffusion model for geolocalization, it is important to understand how it compares to more established models, such as CLIP-based approaches, in terms of scalability and practicality for real-world applications. This could also helping assessing its potential impact and usability. The absence of a thorough analysis of computational costs, such as FLOPs, memory usage, and wall-clock time, makes it difficult to assess the practical feasibility of the proposed method. Without this information, it is hard to determine if the marginal performance gains justify the increased computational burden.

### Questions
1. In Lines 92-93: The paper states, "Performing diffusion on the XYZ coordinates will likely lead to a point that is not on the spherical surface." Can the authors please provide further explanation or supporting evidence for this claim?
2. In Table 1, the method appears to struggle when the distance is below 1/3 or 1/10 of the spatial threshold in the SHDD representations. Could the authors explain why this occurs, especially given the claim that the model works for images with arbitrary resolutions? Does this limitation suggest the model is better suited for coarse-level geolocalization rather than fine-grained predictions?
3. Increasing the parameter $L$ seems to have a significant impact on performance. Could the authors provide more details on the computational resources required as $L$ increases? Understanding the trade-offs between computational cost and performance would offer useful insights into the model's scalability.

### Soundness
2

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
3

### Summary
1. Authors proposed a spherical positional encoding-decoding framework, which encodes points on a spherical surface into a Hilbert space of Spherical Harmonics coefficients.

2. Authors proposed a UNet architecture to learn conditional diffusion by minimizing a latent KL-divergence loss and train a LocDiffusion model that addresses the image geolocalization task via generation.

### Strengths
S1: This article is well-written and easy to understand.

S2: This paper is the first work (to my knowledge) to use a diffusion model for image geolocalization.

(I also suggest that the authors change the word "generative" in the relevant claims to "diffusion ".)

### Weaknesses
W1: This paper has a lot of descriptions of methods, but the experiments are insufficient to support the discussion of the methods. The authors need more ablation experiments. (I can revise the scores based on feedback from the authors.)

W2: Authors have a strong theoretical basis for the design of the method, but unfortunately, the experimental results are not significantly improved, whether it is GeoCLIP compared in the paper or PIGEON, which is not cited.

### Questions
Q1: Can you perform qualitative or quantitative experiments comparing the proposed positional encoding with other methods in the supplementary material?

Q2: Can you provide some ablation experiments?

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
4

### Summary
This paper tries to address the task of image geolocalization that estimates the geographic location where an image was taken. This paper introduces LocDiffusion, a novel generative approach to image geolocalization that leverages diffusion models to predict locations on Earth from images. The key innovation is a new Spherical Harmonics Dirac Delta (SHDD) encoding-decoding framework that enables diffusion in a Hilbert space while preserving spherical geometry. The authors also propose a Conditional Siren-UNet architecture for learning the conditional backward diffusion process.

### Strengths
1.	Creative solution to the manifold projection problem in diffusion models.
2.	Novel SHDD encoding framework that handles spherical geometry.
3.	While the concept of KL-divergence itself is not new, the authors' specific application of it to spherical location generation through SHDD encoding and decoding appears to novel.
4.	The proposed Spherical Harmonics Dirac Delta (SHDD) encoding-decoding framework tackles the challenges of traditional image geo-localization methods by enabling the use of diffusion models for generating locations on the spherical surface of the Earth.

### Weaknesses
1.	Quadratic scaling of SHDD encoding dimension may limit practical resolution. The high dimensionality of the Spherical Harmonics Dirac Delta (SHDD) encoding, scaling quadratically with the degree L, poses a significant challenge for high-resolution location prediction. This could limit the model's ability to discern fine-grained location differences, especially in densely mapped areas. The computational burden associated with the high-dimensional SHDD representation could also hinder real-time applications.
2.	High space complexity and long training process. The computational cost associated with the diffusion process, combined with the high dimensionality of the SHDD encoding, leads to substantial space complexity and extended training times. This makes the model less practical for resource-constrained environments or rapid prototyping. The authors should provide a more detailed analysis of the computational resources required for training and inference.
3.	No ablation study. The lack of an ablation study makes it difficult to assess the contribution of individual components of the proposed model. Without such analysis, it is unclear how much each part of the architecture, such as the Conditional Siren-UNet or the SHDD encoding, contributes to the overall performance. This lack of component-wise evaluation makes it hard to justify the design choices and identify potential bottlenecks.

### Questions
1.	The main purpose of image-based geo-localization is to predict the location of an image. Unlike image retrieval-based localization, can this method predicate the coordinates? 
2.	Unlike using a large model for geo-localization, large model in general (even CLIP), has powerful prior knowledge, and therefore can discern the approximate location when the landmark is given. However, it just only predicts approximate locations, not coordinates. To build such a geographic knowledge base, a huge number of images are needed.
3.	I noticed some tricks in preventing overfitting phenomena, such as a very high dropout rate. Please analyze the overfitting of the proposed method.
4.	the advantages of the SHDD representation are primarily presented at a theoretical level, with limited experimental evidence to fully support the claims, without more experiments or analysis. By the way, there are only three tables in the entire paper, and one of them is still or just an experimental setup. There is no experimental-level evidence of the advantages of model and only a minor improvement in the main experiment.
5.	As shown in Table 1, in YFCC-26k, GeoDecoder has better performance than GeoCLIP in City 25km. I would recommend labeling the strong petitory and marking the improvement over them. Why is the performance so defective in 1km and 25km? The increase in generalization ability is built at the expense of model accuracy, which is hard to accept. I understand the need for generalization ability for this task, but I can only assume that for the previous models are flawed in solving the fitting problem. If the main purpose of this paper is in addressing the generalization ability, it would be more appropriate to analyze this aspect or collect an open-world test set to validate the model.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes a diffusion model for image geolocalization (given an image, estimate where in the world the photograph was taken). Most work in this domain is based on either classification (partitioning the world into bins) or image retrieval. The main claim is that it overcomes limitations in spatial resolution caused by the partitioning scheme or the spatial distribution of gallery images. An encoding space is proposed that enables diffusion modeling on the sphere with the goal of reducing artifacts caused by modeling the sphere as a linear space.

### Strengths
- It's interesting to consider alternative formulations of long-standing problems.
- The proposed approach seems to work well for low-resolution localization.

### Weaknesses
 - The work fails to deliver on its promise of eliminating the spatial resolution issues of previous approaches. Notably, Table 1 shows that it does not outperform approaches from 2016/2017 for low-error thresholds. The challenge is the computational complexity and memory consumption of the proposed approach. While promising, I'd need to see solid evidence that it improves relative to more straightforward approaches.

- L282 seems to be the crux of the problem with this approach, the assumption that the space is infinite. In practical implementations this is truncated, but it's unclear that this space is then the optimal space for the task. Existing approaches allow more data-driven specification of the space (for example, choosing spatial partitioning based on the distribution of the training dataset or implicitly based on the distribution of the gallery). The use of an infinite space and subsequent truncation introduces an arbitrary hyperparameter that is not clearly justified, and may limit the achievable performance.

- L509 makes the claim that retrieval approaches depend heavily on the quality of the gallery, and seems to frame this as a negative. This is similar to saying, "the problem with the ImageNet dataset is that it requires so many images to represent the classes". Of course that's true; we always would love to use fewer images, but it's unclear how the proposed approach overcomes this issue. It still needs a large training dataset to fit the target function and these training images can serve as gallery images. There's clearly a negative to a large gallery, but in practice, it's easy to create indexes across billions of image embeddings using existing libraries. This scales well for practical uses.

- Some previous works have proposed strategies for overcoming the resolution limitations imposed by binning and a small gallery. This includes kernel density estimation in Revisiting IM2GPS in the Deep Learning Era by Nam Vo et al. A more complete assessment of previous attempts at addressing this issue should be included and an evaluation of simpler strategies should be included. Those missing baselines would likely be simpler to implement and might not suffer from the same memory challenges.

- Important related work is missing from CVPR 2024: "PIGEON: Predicting Image Geolocations" by Haas et al. This work proposes a hybrid of classification and retrieval which outperforms the results shown in Table 1 across the board. It notably does not generate poor results for low-error thresholds (which are the settings that most use cases require).

### Questions
I don't have any particular questions, but would be happy to hear discussion regarding the weaknesses identified above.

The writing style made the key contributions and approach difficult to follow. This is a matter of personal style, but here are a few notes / suggestions from my reading of the work:
  - There's quite a bit of mathematical development that seems to obscure the contribution. For example, I found myself skipping over Section 4.1 because it felt like it was being overly mathy without any strong motivation.
  - I'd suggest for a future submission that the authors consider bringing Figure 2 to the forefront and emphasizing the high-level implementation before delving into the detailed mathematics.
  - Figure 1 has the longest caption I've ever seen in a CV/AI/ML paper. Many of those details would have been better presented after the high-level algorithm was clear as opposed to so early in the paper.
  - I find the heavy use of footnotes to be a bad sign for the writing of a paper. It indicates to me that some concepts are being presented out of place.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
"This paper proposes a novel spherical positional encoding-decoding scheme to address non-linearity issues, enabling effective optimization and training for geolocation tasks within a diffusion-based model. Additionally, it introduces a new conditional latent diffusion model, LocDiffusion, which achieves state-of-the-art performance in image geolocalization."

### Strengths
1. This paper introduces a noveldiffusion model to tackle the image geolocalization task, potentially benefiting the field and inspiring new directions.
2. The paper presents a new, learning-free encoder-decoder framework, mathematically demonstrating its robustness against sparsity issues in encoding space. This approach may also be beneficial for other remote sensing or geographical applications.
3. The paper provides solid mathematical proofs to support the properties it aims to achieve, particularly addressing issues of non-linearity and sparsity
4. The proposed approach achieves state-of-the-art results at the Region, Country, and Continent levels.
5. The paper is clear and well-written.

### Weaknesses
1. The ablation study lacks sufficient detail. For instance, it would be helpful to see an ablation on SHDD encoding and decoding—how much improvement does it provide over positional encoding or other encoder-decoder methods? Additionally, is the KL loss significantly more effective than L1 or L2 loss? Further clarification on the contributions of the other proposed modules would strengthen the analysis.

2. The model's performance at the street and city levels is relatively weak and does not achieve competitive results.

3. This method requires huge computational cost, limited to the upbound of L.

4. Need more details about computational cost, training time and inference time.

### Questions
1. In line 321, I noticed that $e_{lm}$ is used, but I couldn’t find a clear definition of it. Is $e_{lm}$ calculated from $F$? Could you clarify this or give the formula?

2. Is it reasonable to interpret the non-linear mapping between the locational embedding and position encoding space in Figure 1 as evidence of SHDD encoding’s superiority over traditional positional encoding? For my perspective, it is unconvincing, as the diffusion model introduces a non-linear mapping between $e$ and the image feature". Can you give more explanation about my confusion?

### Soundness
3

### Presentation
4

### Contribution
3
