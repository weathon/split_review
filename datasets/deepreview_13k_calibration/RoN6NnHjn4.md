# Vec2Face: Scaling Face Dataset Generation with Loosely Constrained Vectors

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 5, 6

## Abstract
This paper studies how to synthesize face images of non-existent persons, to create a dataset that allows effective training of face recognition (FR) models. 
Two important goals are (1) the ability to generate a large number of distinct identities (inter-class separation) with (2) a wide variation in appearance of each identity (intra-class variation).
However, existing works 1) are typically limited in how many well-separated identities can be generated and 2) either neglect or use a separate editing model for attribute augmentation. 
We propose Vec2Face, a holistic model that uses only a sampled vector as input and can flexibly generate and control face images and their attributes. Composed of a feature masked autoencoder and a decoder, Vec2Face is supervised by face image reconstruction and can be conveniently used in inference. Using vectors with low similarity among themselves as inputs, Vec2Face generates well-separated identities. Randomly perturbing an input identity vector within a small range allows Vec2Face to generate faces of the same identity with robust variation in face attributes. It is also possible to generate images with designated attributes by adjusting vector values with a gradient descent method. 
Vec2Face has efficiently synthesized as many as 300K identities with 15 million total images, 
whereas 60K is the largest number of identities created in the previous works.
FR models trained with the generated HSFace datasets, from 10k to 300k identities, achieve state-of-the-art accuracy, from 92\% to 93.52\%, on five real-world test sets. For the first time, our model created using a synthetic training set achieves higher accuracy than the model created using a same-scale training set of real face images (on the CALFW test set). 
Code link: \blue{\url{https://haiyuwu.io/vec2face.io/}}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a novel Vec2Face generative framework for generating identity-specific synthetic face images suitable for training deep recognition models. To this end, the authors rely on a feature Masked Auto-Encoder (fMAE) architecture, which is trained to produce face images of a desired identity based on input features extracted from a pretrained Face Recognition (FR) model. However, these identity features are first projected and expanded to 2D feature maps to suit the nature of the fMAE architecture. Training is performed with four objectives, including the standard reconstruction and perceptual loss functions, along with an identity-based loss, which enables better identity consistency, and a GAN loss that utilizes a patch-based discriminator to ensure sharper images. During inference, the approach utilizes PCA for sampling unique identity vectors, upon which perturbation is performed to obtain diverse samples of a specific identity. Additionally, the approach also supports control over the pose and quality, through guided vector perturbation. The authors showcase the suitability of their approach through extensive experiments across multiple datasets, with a focus on training deep face recognition models with the generated synthetic data. The proposed approach outperforms existing state-of-the-art methods in terms of the accuracy achieved with a trained recognition models on standard verification benchmarks. Importantly, Vec2Face also enables better scalability than existing approaches, thus allowing the generation of diverse datasets of up to 20 million images, compared to existing datasets of 500 thousand images. Furthermore, the authors also perform sufficient ablation studies for supporting the various choices of their particular solution.

### Strengths
The submitted paper is writte well and presents the problem and proposed solution in a concise and clear manner. The proposed approach improves on the state-of-the-art with a unique fMAE architecture, differentiating itself from existing diffusion and GAN-based solutions. Differently, it also proposes to utilize guided perturbation during inference, to not only achieve higher intra-identity diversity of samples but also allow for control over the pose and quality of images, which is crucial for generating large-scale datasets suitable for training recognition models. As a result, the recognition model trained on the generated data of Arc2Face even achieves better results on the Cross-Age LFW benchmark than when training with the real CASIA-WebFace dataset. This represents a tremendous achievement as existing approaches typically achieve worse performance. The proposed approach also enables scaling the generated datasets without drastically impacting inter-class separability, in turn achieving significantly larger dataset sizes than existing approaches. Overall, the paper is suitable for the conference and will likely highly influence future research on the generation of synthetic biometric datasets.

### Weaknesses
Despite the many strengths of the paper, there are a few areas where the paper could be further improver. The evaluation of the approach mainly revolves around the accuracies achieved with trained recognition models on existing benchmarks (apart from Table 4 and Figure 5). While this focus is understandable, it would be beneficial to also analyse other aspects of the data.  

1.	Face Image Quality Assessment (FIQA) measures could provide additional insight as they are specifically designed for evaluating the quality of face images and their suitability for recognition tasks. Examples of recent FIQA measures with publicly available implementations include CR-FIQA (Boutros et al., CVPR 2023) and DifFIQA (Babnik et al., IJCB 2023). It is crucial to assess not only the recognition performance but also the inherent quality of the generated images, which directly impacts their utility for training robust models. Specifically, metrics like sharpness, blur, and noise levels should be evaluated to ensure the generated images are not only diverse but also of sufficient quality for downstream tasks.

2.	Comparison with the state-of-the-art (e.g. Table 4) could also be expanded with metrics that measure fidelity and diversity separately could also be utilized to provide a deeper understanding of the generated datasets, e.g., improved precision and recall (Kynkäänniemi et al., NeurIPS 2019).  While the current evaluation focuses on recognition accuracy, a more granular analysis of the generated data itself is needed. Metrics like precision and recall, when applied to the image generation task, can reveal the trade-off between the fidelity of the generated images to the input identity features and the diversity of the generated samples. This would provide a more complete picture of the strengths and weaknesses of the proposed approach.

3.	In the supplementary material when comparing genuine and imposter distributions it would also be beneficial to provide results obtained with a real-world dataset to provide the baseline of desired distributions suitable for training face recognition models. Without a baseline comparison to real-world data, it is difficult to assess whether the generated distributions are truly representative of the data that a face recognition model would encounter in practice. This comparison is crucial for determining the suitability of the generated data for training models that generalize well to real-world scenarios.

4.	The utilized verification benchmarks are of a rather small scale (roughly 3000 genuine and imposter pairs). It might be beneficial to evaluate the approach on a more complex and larger-scale set, e.g. the IJB-C verification benchmark. There the difference performance improvements of the Vec2Face method could be further highlighted. The current benchmarks, while standard, might not fully capture the performance of the model in more challenging real-world conditions. Evaluating on a larger and more diverse benchmark like IJB-C would provide a more robust assessment of the model's capabilities.

Lastly, Despite the detailed nature of the paper, the utilized patch-based discriminator is rather poorly explained. More information should be added to the paper or at least to the supplementary material. For example, what sort of architecture does it utilize? Is it initialized with a pretrained model? The formulation of perceptual and GAN loss functions could also be provided.

### Questions
1.	Despite the statement provided in Section 3.4., the novelty introduced with this paper remains slightly unclear. The overall paper gives the impression that the fMAE is novel, however, Section 3.4. does not seem to point this out. Can you perhaps elaborate more on the novelty of the fMAE? Does it share similarities or draw inspirations from previous works, namely [1]? Is the novelty perhaps the projection and expansion of input features to 2D feature maps? 

[1] Hu, Junhao, et al. "Features Masked Auto-Encoder-Based Anomaly Detection in Process Industry." 2023 IEEE 12th Data Driven Control and Learning Systems Conference (DDCLS). IEEE, 2023.

2.	When discussing the influence of inter-class separability on the accuracy of trained recognition models, it is observed that a too large separation does not benefit the performance. However, this might not be a unique finding, as results in [2] also showcase that well-separated synthetic identities actually result in lower verification performance. Can you comment more on this phenomenon? Does this mean that future research will have to determine the best balance between inter-class separability and intra-class variation?

[2] Boutros, Fadi, et al. "IDiff-Face: Synthetic-based face recognition through fizzy identity-conditioned diffusion model." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper by using a Masked AutoEncoding on the feature space and a separate FR system, Pose Estimator and Face Quality assessment network authors introduced a pipeline for sampling identities to generate synthetic face dataset for training FR systems.

### Strengths
* The paper is well written and the experiments are exhaustive and insightful both in the appendix (especially the analysis of the attributes of the synthetic data) and the main content.
* Applying MAE on the feature space and formulating it to work with the sampling of the random vectors is quite interesting.

### Weaknesses
 * As the main point of the paper is to generate a synthetic FR dataset, my main concern is that the authors have used the FR model trained on MS1MV2 and Glint360K, and a large subset of the WebFace4m for training/sampling from their method. Training an FR model on  these datasets will probably outperform the FR model trained on the CASIA-WebFace (this dataset used for comparison in Table.1 and Table .2). Later by generating the datasets in a controlled manner they still did not perform as good as a model trained on the CASIA-WebFace, although they are close in most of the benchmarks, so what is the main problem that the authors trying to solve? Why we can not use the CASIA-WebFace, Glint360K, MS1MV2, or the subset of the large WebFace4M that authors used for training their method which probably performs better? Is it trying to address the privacy issues? Are the generated identities different from the ones presented in the dataset used? 
Authors may consider the goal of synthetic dataset generation, especially when their approach assumes the existence of a high-quality FR system or a large-scale dataset already available for training their methodologies.
I will consider raising my score if the authors can argue a benefit of this work over the datasets and models they used for training their methodology

* Maybe evaluation using more benchmarks like TinyFace might be needed.
* There is a good amount of studies that show the InceptionV3 trained on the Imagenet is not a good candidate for reporting Frechet Distance:
   [1] The role of Imagenet classes in Frechet inception distance: https://arxiv.org/pdf/2203.06026

   [2] Exposing flaws of generative model evaluation metrics and their unfair treatment of diffusion models: https://proceedings.neurips.cc/paper_files/paper/2023/hash/0bc795afae289ed465a65a3b4b1f4eb7-Abstract-Conference.html

* Some minor Typos: 
  [366] surround the pose with braces to appear in the subscript.
  
  APP[188] five test sets -> Five Synthetic Data methods maybe?

### Questions
* There was no reproducibility section in the paper do the authors plan to publish their code/ dataset?
* I was wondering if the authors considered using random perturbed vectors instead of features from an FR model in the training phase. 
* As the authors used the subset of WebFace4M (50K identities) for training their method, have authors considered using an FR system trained on this dataset for the ID loss in their proposed method? In this case, one of the weaknesses that I mentioned would be in some extent addressed, if authors can observe the same trend in the results. 
* The authors used an FR system trained on MS1MV2,  Glint360K, in their training objective prior, it would be informative if the authors could add the performance of such a system in Table 2.
* In Table.2, I am curious to see what will happen if we add more synthetic images to the CASIA, let’s say CASIA+HSFace200K.
* [392] As the improvement is on the order of 0.1% could this be also the case if authors changed the network, seed, or margin loss?

### Soundness
1

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
5

### Summary
The paper introduces a novel method called Vec2Face to synthesize large-scale, high-quality face images for training face recognition models. This method addresses the limitations of existing techniques by:
1. Generating a vast number of distinct identities: Vec2Face can generate up to 300,000 unique identities, significantly surpassing previous methods.
2. Controlling intra-class variation: The model can generate diverse variations of the same identity by perturbing the input vector, enabling realistic appearance changes.
3. Manipulating attributes: Vec2Face allows for the generation of images with specific attributes by adjusting the input vector using gradient descent.

### Strengths
1. The pipeline presented in the paper is simple and efficient.
2. The use of a feature-masked autoencoder is somewhat novel.

### Weaknesses
1. Limited Scale of Synthetic Data: While the paper proposes a method for generating synthetic faces, the number of identities generated (300K-400K) is comparable to existing real-world datasets used to train facial recognition (FR) models. This raises concerns about the practical benefits of generating synthetic data at this scale. The marginal increase in identity count compared to datasets like CASIA-WebFace, which contains approximately 500K identities, is not substantial enough to justify the complexity of a synthetic generation pipeline. Furthermore, the paper does not address the potential for diminishing returns in FR model performance as the number of synthetic identities approaches the scale of real-world datasets.
2. Lack of Comparison with Larger Datasets: The paper lacks experiments comparing the effectiveness of the generated synthetic data with larger-scale real-world datasets like Glint360K. This comparison is crucial to demonstrate the advantages of the proposed approach in scenarios where abundant real data is available. The absence of such a comparison makes it difficult to assess whether the proposed method offers a significant improvement over simply using existing large-scale datasets. A rigorous evaluation should include a direct comparison of FR model performance when trained on the synthetic data versus training on established datasets like Glint360K, especially given the computational cost of generating synthetic data.
3. Unclear Practical Motivation: The authors do not provide a compelling reason for generating a synthetic dataset with a similar or smaller scale than commonly used real-world FR training datasets. It is essential to clarify the specific use cases and advantages of this approach, particularly when real data is readily accessible. The paper needs to articulate a clear motivation beyond simply generating synthetic data. For example, if the goal is to address privacy concerns, the paper should explicitly demonstrate how the generated data mitigates these concerns compared to using real-world data. If the goal is to improve model robustness, this should be empirically validated.
4. Missing Citation: The paper omits a key citation: "Vec2face: Unveil human faces from their black box features in face recognition" (CVPR 2020). This work appears relevant to the paper's methodology and should be properly acknowledged.

Misleading Novelty Statements: Certain claims of novelty in the paper are potentially misleading.  (See the next questions section for more details.)  It is crucial to ensure that all claims are accurate and supported by evidence.

### Questions
1. Choice of Pre-trained FR Model:
    a. You've chosen to use ArcFace-R100 pre-trained on Glint360K. Could you elaborate on the reasons behind this specific choice?
    b. Are there any limitations to using a smaller pre-trained FR model trained on a smaller dataset? It seems that requiring a large-scale, pre-trained FR model could limit the applicability of your approach, especially in scenarios where such a model isn't readily available. This creates a potential "chicken-and-egg" problem where generating synthetic data requires access to large-scale real data. Could you address this potential limitation?

2. Number of Identities:
    a. Is there a specific reason for limiting the number of generated identities to 300K or 400K?
    b. Given that your filtering process removes only 1.7% of generated images, is it possible to generate a larger number of identities (e.g., 500K or 1M)? If so, what are the potential challenges or trade-offs involved?

3. Attribute Control During Inference:
    a. You mention that your method "seamlessly supports attribute control during inference." However, it seems that this relies on three external models: pre-trained pose, quality, and FR models. Could you clarify what you mean by "seamless" in this context?
    b. Does relying on these external models introduce any constraints or complexities in practice?

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
5

### Summary
This paper proposes VEC2FACE to synthesize facial images from a sampled identity vector for synthetic face recognition. It utilizes a GAN solution to reconstruct the image at the training stage and adopt the decoder for inference. High intra-class variation is ensured by Perturbing identity vectors. comprehensive experiments are conducted to demonstrate the effectiveness of the method.

### Strengths
1. The proposed method achieves good performance compared to the listed literature.
2. It can generate as many novel identities as possible.
3. The experiments are sufficient.
4. Using GAN to achieve such results is inspiring.

### Weaknesses
 1. [Major] lines 219-220, the authors state 'Following (Papantoniou et al., 2024), PCA is used to sample vectors.'. This brings a concern that the contribution of generating as many novel identities as possible is benefited from the previous work Arc2Face. Additionally, adopting pure identity embedding to generate a facial dataset is demonstrated in the related literature, ID3.

 2. [Major] After attribute OP, how do you make sure the generated image preserves the identity, Do you have experiments to prove it? The attribute operation is also introduced in ID3.

 3. [Major] line 314, Vec2Face training set is WebFace4M, the PCA is carried on MS1MV2, the feature extraction model is from Glint360K. This counters the privacy concerns, as the dataset original MS1M dataset is recalled by its creator. And the whole training requires a lot of face recognition dataset, which is a disadvantage over DCFace/ID3.

 4. [Major] In addition, the training dataset is webface4m (1M with 50k identities ), which is significantly larger than CASIA-WebFace (500k images with 10k identities) adopted by the competitors DCFace/ID3, making the comparison with previous methods unfair. 

 5. [Major] The authors state they achieve state-of-the-art results. However, the SOTA result is 92.30 (on 0.5M volume) and 93.07  (on 0.5M volume), achieved by CemiFace[1].

 6. [Minor]How to generate the image is not clear. For example, how do you obtain the identity feature, randomly generated or from the image? 

 7. [Minor] A study about alternative pretrained FR model should be conducted, as the proposed method uses ArcFace pretrained from Glint360k, DCFace adopted model pretrained from WebFace4M.

 8. [Minor] Line 243, ‘too few profile head poses’. Do you have statics results?

 9. [Minor] Eq. 5 is trained with the GAN?

 10. Long-page discussions might be better if positioned in the appendix.

### Questions
Please see the weakness. 

Overall, I believe the novelty of this paper is incremental, and improvement is good but does not achieve state-of-the-art. Furthermore, privacy issues arise as this paper adopts a lot of labelled face recognition datasets.

### Soundness
3

### Presentation
3

### Contribution
2
