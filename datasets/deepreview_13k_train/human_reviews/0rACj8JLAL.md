# BOOD: Boundary-based Out-Of-Distribution Data Generation

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
Harnessing the power of diffusion models to synthesize auxiliary training data based on latent space features has proven effective in enhancing out-of-distribution (OOD) detection performance. However, extracting effective features outside the in-distribution (ID) boundary in latent space remains challenging due to the difficulty of identifying decision boundaries between classes. This paper proposes a novel framework called Boundary-based Out-Of-Distribution data generation (BOOD), which synthesizes high-quality OOD features and generates human-compatible outlier images using diffusion models. BOOD first learns a text-conditioned latent feature space from the ID dataset, selects ID features closest to the decision boundary, and perturbs them to cross the decision boundary to form OOD features. These synthetic OOD features are then decoded into images in pixel space by a diffusion model. Compared to previous works, BOOD provides a more efficient strategy for synthesizing informative OOD features, facilitating clearer distinctions between ID and OOD data. Extensive experimental results on common benchmarks demonstrate that BOOD surpasses the state-of-the-art method significantly, achieving a 29.64\% decrease in average FPR95 (40.31\% vs. 10.67\%) and a 7.27\% improvement in average AUROC (90.15\% vs. 97.42\%) on the Cifar-100 dataset.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new OOD data generation framework that helps the model to more clearly distinguish ID and OOD data by generating OOD samples near the decision boundary. Specifically, this method identifies ID boundary features by minimizing perturbation steps and generates OOD features near the boundary through gradient ascent. Experiments on CIFAR-100 and IMAGENET-100 demonstrate the effectiveness of the proposed algorithm.

### Strengths
1.BOOD is the first framework capable of explicitly generating OOD data around the decision boundary, thereby providing informative functionality for shaping the decision boundary between ID and OOD data.

2.The paper is easy to follow.

3.Experimental results on the CIFAR-100 and IMAGENET-100 datasets show that the BOOD method significantly outperforms existing SOTA methods, achieving substantial improvements.

### Weaknesses
1.BOOD requires calculating the boundary positions of numerous features and generating images through a diffusion model, which may be computationally time-consuming.

2.The  hyperparameter in the paper is crucial for synthesizing high-quality OOD features, it is recommended to provide the basis for its selection.

3.The adversarial perturbation strategy is an important component, it is recommended to provide a comparative analysis with other perturbation strategies to help readers gain a more comprehensive understanding of the experimental setup.

4.Descriptions of the images presented are lacking in the main text.

### Questions
1.List and compare the actual memory requirements of the proposed model.

2.Further comparative studies on different perturbation strategies could be added to help understand the impact of each strategy on the quality of generated data, and to validate the performance variations of the BOOD method under different  hyperparameters.

3.Provide additional descriptions of Figures 2, 3, and 4 in the main text for a more comprehensive evaluation.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes BOOD, a method for synthesizing out-of-distribution images that are closer to the boundary, for enhancing OOD detection performance. It first learns a image encoder whose feature space aligns with class token embeddings, and leverage it as a cosine classifier. Then it picks the images whose features need the fewest number of perturbation steps in the gradient ascent direction to change the cosine classifier’s prediction, and generates OOD images from their perturbed features. It then uses the generated OOD images to regularize the training of an OOD classification model. Experimental results show that BOOD outperforms a variety of existing OOD detection approaches on CIFAR-100 and ImageNet-100 as ID data.

### Strengths
* This paper proposes a new approach for synthesizing out-of-distribution data by performing adversarial perturbation and generating images along the ID boundary. The method is intuitively and technically sound.

* Performance-wise, the gain over existing methods is significant on CIFAR-100 as ID. The synthesized images look reasonable visually as boundary cases. 

* The writing and presentation of the paper are clear.

### Weaknesses
 * The method seems to be bounded by the capability of the stable diffusion model. In cases where ID data are very distinct from stable diffusion's training distribution, e.g. if the ID data is SVHN or texture, or some other domains like medical imaging, etc., or where the classification is very fine-grained, it is uncertain how effective the method would be.

* The performance improvement on CIFAR-100 as ID data is significant but the improvement on ImageNet-100 is only marginal, although both datasets are natural images with 100 classes. This also somewhat raises some uncertainty about how much improvement BOOD can bring over the existing methods in general. It may be helpful to include more in-depth discussion or analysis on in which cases BOOD provides significant gains and in which cases its advantage over prior approaches is less obvious.

* Minor point - there are several typos in the use of parenthetical vs. textual citations: e.g. L047, L179, L232

### Questions
* How necessary is it to synthesize OOD data, as opposed to finding publicly available OOD data and seeing if training with them can generalize to unseen OOD data? How does BOOD compare with methods that use real OOD data for augmentation, such as [1]?

* The method seems to involve various different hyperparameters, including pruning rate r, max perturbation iteration K, and regularization weight beta. How are they selected? If one applies BOOD to a new ID dataset, are there guidelines or general rules of how to select them?

* Given that generation with diffusion models can be computationally expensive, it would be helpful to see more in-depth analysis on computation-performance tradeoffs (e.g. performance vs. the number of images generated per class). 

[1] Hendrycks, Dan, Mantas Mazeika, and Thomas Dietterich. "Deep anomaly detection with outlier exposure." ICLR 2019.

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
This paper proposes a novel framework, named Boundary-based Out-Of-Distribution data generation (BOOD). It first identifies the features closest to the decision boundary by calculating the minimal perturbation steps imposed on the feature to change the model's prediction. Then, it generates the outlier features by perturbing the identified boundary ID features along with the gradient ascent direction. These synthetic features are then fed into a diffusion model to generate the OOD images, enhancing the model’s ability to distinguish ID and OOD data. Extensive experiments show the effectiveness of their method.

### Strengths
1.This paper proposes a novel boundary-based method for generating OOD data, leveraging diffusion models to identify ID data closest to decision boundaries and applying an outlier feature synthesis strategy to generate images located around decision boundaries. This approach provides high-quality and informative features for OOD detection.
2.This paper is technically sound. The ablation experiments, hyperparameter analysis experiments, and visualization experiments are all comprehensive.
3.This paper provides a clear and thorough introduction to the proposed methods and algorithmic procedures. The formulas and notations are well-explained, with detailed definitions for all symbols and terms used.

### Weaknesses
1.One potential drawback is a notation conflict between the additional perturbation steps c (line 287-288) and the earlier use of C for the number of classes. This overlap in symbols could cause confusion, so it might be beneficial to change the symbol for one of these terms to improve clarity.
2.In Table 2, the comparison with state-of-the-art (SOTA) methods could be enhanced by including more recent methods from 2024. This would better highlight the advantages and relevance of the proposed approach in the context of the latest advancements.
3.A limitation of the hyperparameter sensitivity analysis is that it could benefit from experimenting with a wider range of values to better demonstrate the rationale behind the chosen settings. Additionally, more intuitive visualizations could be provided to clearly illustrate the improvements of the proposed method over previous approaches.

### Questions
See Weakness above.

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
4

### Summary
This paper focuses on addressing the OOD detection task by synthesizing outlier samples. To achieve the synthesis of reasonable outlier samples, it first selects out the samples which reside near to boundaries, and then apply the adversarial attack to perturb features of these samples until their classes are changed. Finally, it applies the diffusion model to generate outlier samples from those perturbed features, which are used for training the OOD classifier. Experiments on various datasets demonstrate that the proposed method achieve better performance than existing methods.

### Strengths
- It introduces a new outlier synthesis through selecting out samples close to decision boundaries and distorting them. Outlier samples can be more easily synthesized from these samples compared to other samples.
- Extensive experiments are conducted to validate the effectiveness of the proposed method and core technical components such as the sample selection strategy.
- The paper is well written with clear structure and smooth logic, making it easy for readers to understand its ideas and algorithms.

### Weaknesses
1. The rationale for using adversarial attacks to perturb sample features remains insufficiently justified. Perturbing features to alter their class identities might unintentionally transform them into samples of other in-distribution classes. To address this concern, the authors should provide theoretical or empirical evidence demonstrating that their perturbation method reliably generates features distinct from existing classes. Additionally, a comparison with alternative perturbation strategies would help clarify the unique benefits of the proposed approach.
2. The inquiry into the performance of random feature perturbations, such as adding Gaussian noise or displacing features away from class centroids, is highly relevant. To make this critique more actionable, I recommend requesting an ablation study comparing the proposed perturbation method against these simpler alternatives. Such an analysis would provide concrete evidence of the theoretical and empirical advantages of the method.
3. The paper lacks sufficient detail on the architectures of the image encoder and the OOD classification model. For replication purposes, it is essential to include specifics such as the number and type of layers, activation functions, and other relevant parameters. A detailed description of these aspects would significantly enhance the reproducibility of the proposed algorithm.
4. There is an error in Equation (2), where the denominator should correctly be '\Gamma(y_j)^Tz'. While this observation is helpful, I suggest the authors conduct a thorough review of all equations and mathematical notations throughout the manuscript to ensure accuracy and consistency.

### Questions
1. Clarification is needed regarding the sensitivity of the method to the hyperparameter r. An exploration of this sensitivity, perhaps through a sensitivity analysis, would provide valuable insights into the robustness and reliability of the proposed approach under varying conditions.
2. The method performs significantly worse than NPOS on the OOD dataset Textures, as indicated in Table 2. An explanation for this performance discrepancy would be beneficial. The authors could analyze specific characteristics of the Textures dataset or aspects of their method that may contribute to this outcome.

### Soundness
3

### Presentation
3

### Contribution
2
