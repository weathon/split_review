# AugGen: Generative Synthetic Augmentation Can Boost Face Recognition

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
As machine learning increasingly relies on large amounts of data, concerns about privacy and ethics have grown. Recently, methods for generating synthetic data to augment or replace real datasets have emerged to mitigate these concerns. In this paper, we demonstrate improved performance on a discriminative task when training on a mix of real and synthetic data, compared to training solely on the original real data. Our synthetic data is generated using a novel sampling method based on a conditional generative model and a discriminator, both trained exclusively on the original data, with no need for auxiliary data nor pre-trained foundation models. We consider the challenging task of face recognition, which is well known for its privacy and ethical issues. Using our augmented dataset, we demonstrate consistent improvements over the model trained on the original dataset, on various benchmarks including IJB-C and IJB-B by up to 5\% while performing competitively with state-of-the-art synthetic data generation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes training face recognition models on a mix of real data and synthetic data generated with a diffusion model. Given a dataset of faces and identites, the authors learn a class-conditioned generative model, sample from it by interpolating between one-hot class encodings, and mix these samples with real data when training a discriminative model. They demonstrate this procedure leads to improvement with respect to a model trained solely on real data.

### Strengths
The experimental evaluation is the main strength of the paper. Authors test their method on a few benchmarks over multiple seeds and compare to appropriate baselines.

### Weaknesses
The main weakness of the paper is that there is little theoretical justification for what authors are trying to achieve. For synthetic data to significantly improve the performance of a machine learning model, it has to introduce new information. This is the case when the data comes from a rendering pipeline, but expecting significant gains by training a discriminative model on the outputs of a generative model of the same distribution goes against the data processing inequality. It is possible that including generated samples helps in extremely data-impoverished or class-imbalanced scenarios, or improves the training dynamics of the discriminative model, but it cannot lead to major improvements. Indeed, the results in Table 1 show that the observed differences between a model trained on the real data and one trained on the outputs of a generative model are not statistically significant.

The proposed method has been explored before, e.g. by Hong et al. 2023 (Enhancing Classification Accuracy on Limited Data via Unconditional GAN), Besnier et al. 2019 (This Dataset Does Not Exist: Training Models from Generated Images), ane Lomurno et al. 2024 (Stable Diffusion Dataset Generation for Downstream Classification Tasks).

Presentation is a significant weakness of the submission. The descriptions are hard to follow because of convoluted wording, stylistic mistakes, and incorrect punctuation. The manuscript would benefit significantly from a thorough proofread. Frequent explanations of basic concepts (like a random seed) distract from the main ideas of the paper.

### Questions
Have you tried measuring the relationship between the size of the synthetic dataset and downstream metrics?

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
This paper addresses the problem of the need for large-scale datasets to train deep networks by augmenting the original dataset with synthetic data. To this end, the paper trains a conditional generative model to synthesize new examples. The paper argues that, beyond generating new examples from existing classes, it is also beneficial to generate examples of new classes by interpolating the conditional vectors between two different classes.

Both the generative and discriminative models are trained on CASIA-Web datasets, and their performances are compared with models trained on DigiFace 1M, Real DigiFace, DCFace, etc.

### Strengths
The paper addresses the important issue of the need for a large-scale training set.

The paper is generally easy to follow.

### Weaknesses
A concern is the novelty of the method. The idea of interpolating conditional vectors to train a generative model is somewhat incremental. There are multiple works on GANs for face attribute manipulation using continuous features [ref1] or differences in one-hot vectors [ref2].

Additionally, the paper mostly relies on empirical values to justify the idea, with no detailed explanation of why the proposed method of interpolating conditional vectors to synthesize new identities works. Conditioning on a large one-hot vector (e.g., 10,000 for a dataset with 10K identities in the training set) can also be challenging to train, but this issue is not discussed. Specifically, the authors do not address the potential for mode collapse or the generation of unrealistic images when interpolating between distant identity vectors in the latent space. The lack of analysis on the quality and diversity of the generated samples is a significant oversight.

The method is evaluated only on CASIA-Web. It would be beneficial to evaluate on at least one more dataset if relying on empirical values to validate the idea. Furthermore, the evaluation lacks a thorough analysis of the impact of the interpolation strategy on the performance of the downstream face recognition task. It is unclear if all interpolated identities are equally beneficial or if some interpolation strategies lead to better results than others. The paper could have dedicated more space to providing detailed insights into the method rather than spending too much on the basics of generative and discriminative models.

### Questions
A clear articulation of the novelty of methodology, a detailed explanation of why the method works, and experiments on yet another benchmark can change my opinion about the paper.

### Soundness
2

### Presentation
2

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
The paper aims to address privacy and ethical concerns associated with large-scale real datasets while improving the performance of face recognition models using the synthetic data. It employs one single dataset to train both generator and discriminator to eliminate the need for auxiliary data or pre-trained models. Finally, the authors claim that training on a mix of real and synthetic data improves performance on discriminative tasks compared to training on real data alone.

### Strengths
1. The use of synthetic data alleviates privacy and ethical concerns associated with large-scale real datasets.
2. The method does not require additional data or pre-trained models for the generator.

### Weaknesses
1. Using synthetic data to avoid privacy concerns or to enhance the performance of face recognition systems has been explored in several prior methods. This paper claims a distinct advantage in that it does not require additional data or pre-trained models, as it relies on a single dataset for training both the generator and the discriminator.
    - Training a new generator using a dataset of 805M in size incurs substantial costs,
    - The above data appears to differ from that used to train face recognition models, such as CASIA-WebFace, which contains only 0.5M samples. This may impliy the use of additional data, so it would be more illustrative if the authors can explain these details.
    - From the perspective of using a single training dataset, the generator aims to learn the distribution of the input dataset. When sampling, it produces an image that aligns with this distribution, which can be regarded as interpolating the input face images at the identity level. This process is expected to increase the diversity of the original data, thereby contributing to performance improvements. Utilizing other pre-trained models introduces additional dataset diversity to the original data, potentially resulting in even greater gains.

2. The paper lacks comparisons with related methods such as Synface and SFace. Synface, for instance, investigates the integration of synthetic and real data during training, and its identity mixup technique involves combining two distinct identities using varying coefficients, a process similar to Equation 4 in this paper.

3. There are areas where the writing could be refined. For example:
    - On line 65, the text mentions "M_mix," whereas Figure 1 labels it as "M_new"; Figure 2, however, uses "M_mix."
    - On line 164, it states "k pairs of image and label," yet the listed pairs of x and y range from 0 to k, indicating there are actually k+1 pairs.

### Questions
Please refer to the **Weaknesses**.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the challenge of training face recognition models with synthetic data to mitigate privacy and ethical concerns while enhancing model performance. The proposed approach introduces a new sampling method for learning a face generator. During training, both real and synthetic face data are used to train the face recognition model. Experiments are conducted on two small datasets to demonstrate the effectiveness of the proposed method.

### Strengths
- This paper addresses an important challenge in face recognition by exploring the use of synthetic data for model training.

- Experimental results highlight the effectiveness of integrating real and synthetic data for training face recognition models.

### Weaknesses
 - The proposed method continues to depend on large-scale real-world face images for training, which diminishes its impact on addressing privacy and ethical concerns.

- The employed frameworks are similar to several existing methods, but references are missing. For example, [1] Synface: face recognition with synthetic data, 2021; [2] SFace: Privacy-friendly and accurate face recognition using synthetic data, 2022

- Figures 1 and 2 contain excessive overlapping content that could be reduced or eliminated for clarity.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2
