# Temporally Equivariant Contrastive Learning for Disease Progression

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
Self-supervised contrastive learning methods provide robust representations by ensuring their invariance to different image transformations while simultaneously preventing representational collapse across different training samples. Equivariant contrastive learning, on the other hand, provides representations sensitive to specific image transformations while remaining invariant to others. By introducing equivariance to time-induced transformations, such as the anatomical changes in longitudinal medical images of a patient caused by disease progression, the model can effectively capture such changes in the representation space. However, learning temporally meaningful representations is challenging, as each patient's disease progresses at a different pace and manifests itself as different anatomical changes. In this work, we propose a Time-equivariant Contrastive Learning (TC) method. First, an encoder projects two unlabeled scans from different time points of the same patient to the representation space. Next, a temporal equivariance module is trained to predict the representation of a later visit based on the representation from one of the previous visits and from the time interval between them. Additionally, an invariance loss is applied to a projection of the representation space to encourage it to be robust to irrelevant image transformations such as translation, rotation, and noise. The representations learned with TC are not only sensitive to the progression of time but the temporal equivariant module can also be used to predict the representation for a given image at a future time-point. Our method has been evaluated on two longitudinal ophthalmic imaging datasets outperforming other state-of-the-art equivariant contrastive learning methods. Our method also showed a higher sensitivity to temporal ordering among the scans of each patient in comparison with the existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes time-equivariant contrastive learning (abbreviated TC by the authors) and applies this method to longitudinal medical image analysis. A key component of TC is an equivariance module. Given two unlabeled scans of the same patient as well as the time difference between them, this equivariance module is trained to predict the later later scan's representation using the earlier scan and the time duration from the earlier scan to the later scan's time. TC outperforms various equivariant contrastive baselines on two longitudinal ophthalmic imaging datasets.

### Strengths
- The medical application considered is compelling.
- The proposed method appears to achieve highly competitive accuracy scores compared to the baselines evaluated.
- I found Figure 1 very helpful.

### Weaknesses
 - The exposition currently is quite muddled. For example, already in Section 1, I find there to quickly be a lot of unnecessary details making it difficult to tease out what exactly the key takeaways are. For Section 1 anyways, I'd suggest reworking the exposition to more clearly get at what the key ideas of the proposed method are, and what limitations of existing work the proposed method aims to address.
- In the first paragraph, the text says that "However, sensitivity to some of these transformations may be crucial for specific downstream tasks, such as color information for flower classification or rotation for traffic sign detection." This is in reference to, if I understand correctly, how data augmentation is used standardly in contrastive learning (e.g., SimCLR, supervised contrastive learning). However, when using such contrastive learning approaches, it is standard to make sure that the random perturbations/transformations used for data augmentation only consist of changes that the model shouldn't care about whereas the ones that we actually want the latent embedding representation to learn should not be used in data augmentation. Am I missing something here?
- How does the proposed method TC relate to steerable equivariant representation learning (Bhardwaj et al 2023)?
- Please update the experimental setup so that error bars could be reported (such as running experimental repeats with different random seeds and reporting mean/std dev of different achieved evaluation scores).
- Overall I would like to see a much more detailed discussion of precisely why the authors think that the proposed method at times outperforms existing 3 equivariant contrastive methods.
- There is a large body of literature on medical image registration. I think some discussion of this literature would be helpful --- do state-of-the-art methods from this literature simply not work well for the problem setup considered here?
- There are many English issues. Please proofread carefully.
- Please use \citet and \citep appropriately.
- Much more cleanly delineating what already exists vs what the innovations of this paper are would be extremely helpful.

### Questions
Please see "weaknesses".

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors propose an approach towards contrastive learning that allows for learning representations across time in images that represent disease progression. From this they propose modifications to contrastive objectives to ensure that the learned representations identify what remains static versus what changes longitudinally in order to help predict disease progression.

### Strengths
- This paper has clear clinical significance and as a result the modification to the image-based contrastive objectives is clear.

 - The addition of the regularizing term to prevent collapse is interesting and the effectiveness of it is demonstrated in experimental results

### Weaknesses
 - It is unclear how the hyperparameters are selected. Specifically, for VICReg, hyperparameters are selected to bring the magnitude of the loss terms in the same range. What does this mean? What happens when you use the hyperparameters from the original VICReg implementation?

 - The authors note that the displacement term needs to be larger than 0 in order to prevent collapse. However, in many medical settings it is possible that there is no change. However, it looks like this model requires a small amount of change. Since the severity of the disease is monotonically non-decreasing, it seems like it is also the case here. If that is true, this method seems very limited in its application.

 - I believe that the introduction could be improved. Certain elements seem to be out of order. This makes it difficult to understand what the specific issue is that you’re trying to address.

### Questions
- How were hyperparameters selected? Specifcally, could you provide some intuition for why you selected the hyperparameters you chose?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a Time-equivariant Contrastive Learning (TC) method aimed at achieving temporally-sensitive representations within a contrastive learning setting. This is especially targeted at disease progression in longitudinal medical images. The method uses an encoder to project scans from different time points into a representation space and employs a temporal equivariance module that can predict future representations using existing ones. Unlike other methods, this approach directly transforms medical image representations in time, capturing irreversible anatomical changes, like those due to degenerative diseases. The authors introduced a regularization loss term to maintain the sensitivity of the time parameter and constructed contrastive pairs from different patient visits to learn patient-specific features. The method outperforms other equivariant contrastive methods on two temporal eye scan datasets, emphasizing the importance of temporal sensitivity for assessing disease progression risk. The TC method's main limitation is its reliance on irreversible diseases with scans acquired at discrete intervals.

### Strengths
S1. The paper presents an approach in the realm of contrastive learning. By introducing the Time-equivariant Contrastive Learning (TC) method, the authors tackle the challenge of capturing irreversible anatomical changes, particularly in the context of disease progression. 

S2. The proposed TC method has been tested and has demonstrated superior performance against other state-of-the-art equivariant contrastive techniques. This is evident from its application on two temporal datasets related to eye scans, which solidifies its robustness and reliability.

S3. The paper does a good job of articulating the need and significance of the proposed method. The clear presentation of the challenges associated with degenerative diseases, especially the irreversible nature of certain anatomical changes, underscores the importance and timeliness of the TC method.

S4. The potential ramifications of the TC method in the medical field is highlighted. Its ability to predict disease progression and effectively assess a patient's risk of advancing to more severe stages of a disease can be a game-changer in patient care and medical diagnosis. This predictive capability is not just about identifying risk but also about enabling timely and personalized interventions.
S5. The TC method's ability to generate future representations without needing corresponding patient scans showcases its versatility. This feature is particularly beneficial for medical scenarios where timely scans might not be available but predictions are essential for patient care.

### Weaknesses
W1. While the TC method introduces a promising approach for handling irreversible diseases with discretely acquired scans, its utility seems confined to this specific scenario. The real world of medical conditions is vast, and many diseases do not follow a strictly irreversible path. The narrow scope potentially limits the method's broader applicability across the diverse landscape of medical imaging and conditions. The method's reliance on a specific disease progression pattern, namely irreversible changes, restricts its use to a limited set of medical conditions, potentially excluding a large number of diseases that exhibit more complex temporal dynamics.

W2. The method heavily relies on the assumption that degenerative diseases follow a monotonic non-decreasing function over time. This is a strong assumption that might not hold across all conditions or datasets. Diseases can have varying trajectories, with periods of stability, rapid progression, or even temporary reversal. Basing a method on this assumption might lead to inaccuracies in real-world applications. The assumption of monotonic progression may not be valid in cases where treatments or other factors cause temporary reversals or plateaus in disease progression, which are common in many chronic conditions. This could lead to inaccurate predictions and unreliable representations.

W3. Although the paper claims superior performance against other methods, a deeper comparative analysis, considering a broader range of conditions, datasets, and variability, would be more convincing. A comprehensive comparison would provide clarity on the margin and conditions of this outperformance. The performance gains over the baselines are not substantial, and a more rigorous comparison with a wider array of methods and datasets is needed to validate the robustness and generalizability of the proposed method. The current evaluation does not sufficiently demonstrate a clear advantage over existing approaches.

W4. Medical images are notorious for their variability and potential anomalies, especially given the variation between patients, imaging equipment, and acquisition protocols. The paper does not delve deeply into how the TC method would handle potential anomalies, outliers, or inconsistencies in the longitudinal medical images. The method's robustness to common medical image artifacts, such as motion blur, noise, and variations in image acquisition parameters, is not addressed. These factors can significantly impact the quality of the learned representations and the reliability of the model's predictions.

W5. While the paper alludes to reduced complexity in comparison to other models, a more explicit discussion or breakdown of computational costs, resource requirements, and scalability considerations is conspicuously missing. For real-world application, especially in clinical settings, understanding computational overhead is crucial. A detailed analysis of the computational complexity, including the number of parameters, training time, and memory requirements, is needed to assess the feasibility of deploying this method in clinical settings. The lack of this information makes it difficult to evaluate the practical applicability of the proposed method.

W6. The paper mentions that temporal medical datasets are costly to obtain and challenging to release publicly. This heavy reliance on hard-to-obtain datasets can be a significant bottleneck for the practical application and scalability of the TC method. Additional experiments with non-medical images would provide beneficial to applicability of this model into other fields and since it already has the potential, lack of its presence is a weakness in the paper. The reliance on specialized medical datasets limits the generalizability of the method and makes it difficult to evaluate its performance on more diverse datasets. The lack of experiments on non-medical datasets also restricts the potential applicability of the method to other domains.

W7. The introduction of a regularization loss term, crucial for maintaining time parameter sensitivity, is presented without an in-depth rationale or derivation. A clearer explanation of this term's derivation, its impact on the model's performance, and sensitivity analyses would provide more confidence in the method's robustness. The paper lacks a detailed explanation of the regularization loss term, including its mathematical formulation, its impact on the model's performance, and a sensitivity analysis to determine the optimal value of the regularization parameter. This lack of clarity makes it difficult to understand the inner workings of the method and its robustness.

W8. There are only 3 baselines tested for the experiments and for these the performance improvement is minor. Error bars should be added to identify whether these performance improvements are significant and how robust to different random seeds is the model compared to the other baselines.

### Questions
Q1. How does the Time-equivariant Contrastive Learning (TC) method handle highly irregular intervals between patient visits?

Q2. How is the contribution of different loss terms in your overall total loss change throughout training? Do each component monotonically decrease? Additional analysis of these should be added to the appendix.

Q3. How does the model handle potential anomalies in the data, such as imaging artifacts or errors?

Q4. Have you considered extending the application of the TC method to other medical imaging modalities or even non-medical datasets?

Q5. What are the computational complexities involved in the TC method, especially when applied to large-scale datasets?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To incorporate the element of time into image transformation, the researchers introduced the Time-equivariant Contrastive Learning (TC) technique. This method involves training a temporal equivariance module, ensuring that the model captures representations across various timesteps. As a result, the model gains the capability to anticipate future image representations within a consistent time frame. Empirical evaluations conducted on two image datasets have demonstrated the effectiveness and robust performance of the proposed approach.

### Strengths
+ The employment of an equivariance module allows the model to directly predict the transformation of representations in correlation with image transformations, facilitating the generation of future image representations.
+ A regularization loss term has been incorporated, applied to the predicted displacement map, ensuring the time parameter invariance is upheld.
+ By constructing contrastive pairs for each patient visit, the dataset is enriched, promoting smooth training of the model.

### Weaknesses
 -  Regarding equation 4, the regularization term: Would utilizing a normal L2 loss on the MLP, adjusted by a coefficient τ, be feasible? The rationale behind adding a constant 1 in this equation is unclear. It is not clear how this term prevents the displacement map from collapsing to zero, and what the effect of the constant 1 is.
- The structure of ψ in equation 2 needs elaboration. Given its crucial role in predicting future representations, it seems unlikely to be just an MLP. The exact architecture and the reasoning behind the choice of this architecture should be further explained. The current description is too vague to understand the module's capacity.
- Additional experiment results showcasing the impact of different loss item coefficients are necessary. Solely omitting one does not provide a thorough comparison. A more comprehensive ablation study is needed to understand the contribution of each loss term.
- It would be beneficial to display some prediction results based on past image representations, possibly comparing actual images from a patient’s last visit to predicted ones over a set time period. This would provide a qualitative assessment of the model's predictive power. Visualizations of predicted displacement maps would also be helpful.
- Would utilizing negative time in training, aiming to predict previous images given a current one, contribute to enlarging the dataset? This could potentially provide additional training signal, but the feasibility of inverting the transformation is not discussed.

### Questions
- Could you clarify the definition of 'time' in this context? In scenarios where a healthy individual undergoes multiple scans, the images might appear identical, whereas for a patient, variations are expected. This could potentially lead to the collapse of the time equivariance module with limited patient data.
- Is there a scope for the model to handle both 3D scans and 2D images as inputs? This might enable the model to learn a richer set of representations.
- Could you please explain the term "CIn testing" mentioned in section 6? It appears to be a novel concept without a provided definition.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
