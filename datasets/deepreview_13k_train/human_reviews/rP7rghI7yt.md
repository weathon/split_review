# PHI-S: Distribution Balancing for Agglomerative Models

- Decision: Reject
- Scores: 5, 3, 8, 5

## Abstract
Various visual foundation models have distinct strengths and weaknesses, both of which can be improved through heterogeneous multi-teacher knowledge distillation without labels, termed "agglomerative models." We build upon this body of work by studying the effect of the teachers' activation statistics, particularly the impact of the loss function on the resulting student model quality. We explore a standard toolkit of statistical normalization techniques to better align the different distributions and assess their effects. Further, we examine the impact on downstream teacher-matching metrics, which motivates the use of Hadamard matrices. With these matrices, we demonstrate useful properties, showing how they can be used for isotropic standardization, where each dimension of a multivariate distribution is standardized using the same scale. We call this technique "PHI Standardization" (PHI-S) and empirically demonstrate that it produces the best student model across the suite of methods studied.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a modification to the AM-RADIO multi-task distillation framework (Ranzinger et al.) to improve its performance on downstream tasks. More specifically, it focuses on the problem of normalizing the output distributions of different tasks/teachers before distilling them into a single student. The paper performs ablations on different normalization techniques such as simple mean/std global normalization, whitening, Hadamard whitening and then proposes a modified normalization technique called PHI-S which is rotation invariant. The experiments suggest that PHI-S, on average, is a better normalization for AM-RADIO compared to the other normalizations considered in the experiments.

### Strengths
+ The proposed PHI-S normalization is easy to be applied to the existing AM-RADIO framework.
+ PHI-S on average performs better than the other normalization techniques considered in the paper.
+ I would also like to appreciate the inclusion of recent similar techniques (such as UNIT and UNIC) in the related works.

### Weaknesses
 **Contribution:**

The paper proposes a new normalization technique to be applied to teacher distributions in multi-teacher distillation settings. Although the importance of normalization has been previously studied in the literature and sufficiently covered in the related works by the authors, the proposed method targets a specific framework, namely AM-RADIO. To me the main finding of the paper is the importance of such normalization for this framework and introduction of the PHI-S normalization technique. However, normalization for AM-RADIO has been also recently explored (such as Theia as also acknowledged by the authors). This makes the paper an experimental follow up by introducing a new type of normalization for which I expected to see stronger experimental results (see below).

**Experimental results**:

The main contribution of the paper is the introduction of the PHI-S normalization with the goal of improving the existing AM-RADIO pipeline. Most experiments in the paper focus on ablating and comparing PHI-S with simpler normalization techniques. Particularly, I found it hard to find a fair comparison between AM-Radio with and without PHI-S and with other existing related works. Table 2 and Table 18 try to provide such a comparison, but the settings are not apple to apple (i.e. using different models, different training, image resolutions, etc for different methods). This makes it hard to verify the main claim of the submission. Please see the questions sections for additional questions/comments.

**Paper organization/presentation:**

I suggest the authors consider re-organizing the paper. A significant portion of the main paper (page 3, page 4, and page 5) goes over the details of the previously known methods and normalization techniques . This can be greatly summarized and/or moved to the supplementary, freeing up some space for discussing the main contributions of the paper and including important experimental results.

### Questions
1) Table 2 suggests that the performance of the AM-RADIO zero-shot/few-shot image classification reduces when PHI-S normalization is applied. However, I see that the baseline and the proposed approach are using different models. Is the reduction in performance caused by using a different backbone or it is caused by the proposed PHI-S normalization. Does your method still hurt AM-RADIO if you switch to ViT-H? Adding apple-to-apple comparisons between the proposed method, AM-RADIO and previous approaches can help understanding the effectiveness of the proposed normalization.

2) Table 2 reports PHI-S-RADIO-L to have an ImageNet-1K accuracy of 81.01 and 84.68 on zero-shot and kNN respectively. However, Table 18 reports 80.45 and 84.57 for the same model (PHI-S-RADIO-L) and the same dataset to my understanding. What is the difference between these two experiments?

3) According to the reported experiments in the paper, the proposed PHI-S normalization almost always hurts the performance on the SAM COCO instance segmentation, even compared to the simple MSE baseline without normalization. Is there a specific reason for this observation? An analysis can help the reader to better understand the shortcomings of the proposed normalization.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses the problem of learning a unified agglomerative model for vision - by distilling knowledge from multiple vision foundation models, used as teacher models. This work builds upon AM-RADIO (Ranzinger et al. (2024)) and identifies a possible limitation that could arise from the differences in the distributions of the features from different models, With this motivation, the paper explores different statistical normalization techniques to improve the teachers' features. Specifically, the paper introduces PCA-Hadamard Isotropic Standardization (PHI-S) that is claimed to produce the best student model compared to prior baselines and other feature standardization techniques.

### Strengths
- The problem of distributional differences identified by the paper with regards to the AM-RADIO work is well motivated and can be useful not just for agglomerative foundation models but also for other problems involving distillation of multiple features. 
- The presentation of the different standardization techniques and the theoretical analysis of their error properties is good.

### Weaknesses
 - The problem of distributional differences identified by the paper with regards to the AM-RADIO work is well motivated and can be useful not just for agglomerative foundation models but also for other problems involving distillation of multiple features.
- The presentation of the different standardization techniques and the theoretical analysis of their error properties is good.

 - The experiments initially focus on the teacher-matching metrics, for example the MSE loss to different teachers in Table 3. However, it is not clear if the a decreasing the MSE loss to a specific teacher necessarily brings downstream benefits. For example, consider the Cosine method for the DFN-CLIP teacher. Its MSE loss is 10-25 times higher than all the other methods (the Cosine method is also the worst for SigLIP). DFN-CLIP and SigLIP are the only strong performing models in zero-shot Imagenet classification (see Table 1 in [1]). One would expect higher MSE for DFN-CLIP and SigLIP to result in poorer performance in zero-shot Imagenet classification. But the finding is to the contrary - the Cosine method performs best in zero-shot Imagenet classification among non Ada- methods (see Table 13). If the initial MSE loss is mainly resulting from the difference in feature norms, then the experiments that depend primarily on the MSE loss do not make sense. This raises concerns about the validity of using teacher-matching loss as a primary metric for evaluating the effectiveness of the proposed standardization techniques.
- The empricial comparison of PHI-S to AM-RADIO in Table 2 is not a fair comparison as the teacher models used are different between the 2 works. So, this comparison is not a fair demonstration of the benefits obtained by using the feature standardization proposed in this work. Specifically, the change from OpenAI CLIP to SigLIP introduces a significant variable that is not controlled for, making it difficult to isolate the impact of the proposed standardization method.
- The empirical performance on downstream tasks are presented in the main paper based on average ranks on different groups of tasks. This makes it difficult to get a clear understanding of the performance and does not provide a clear comparison between the different methods. Looking at the performance metrics in Tables 13-17, the performance of PHI-S is only on par with other baseline methods or the improvement is too marginal to be considered as a significant improvement. The presentation in terms of ranks is also somwhat misleading when the performance difference between the ranks are so small/insignificant. For instance, one could argue that adding the AdaLoss to MSE brings consistent and significant improvements across all tasks (Ada-MSE vs MSE) but the performance difference between the other methods are comparatively insignificant. This raises the question of whether the usage of Hadamard matrices for standardization (which is claimed to be one of the contributions of the paper) is actually effective. The reliance on average ranks obscures the fact that the performance differences between methods are often marginal, making it hard to assess the true impact of PHI-S.
- The paper is heavily reliant on AM-RADIO [1]. The proposed standardization solution is not completely new [3, 4] but it can still be interesting to show that it can be useful in new applications. However, the effectiveness of the proposed solution is not sufficiently demonstrated in this paper. The lack of clear, substantial improvements over existing methods, especially when considering the marginal gains in downstream tasks, weakens the overall contribution.
- DINOv2 also brings additional benefits like transfer learning, domain generalization and robustness properties. The paper lacks analysis of other such beneficial properties of the teacher models. This can be a worthy addition that is not explored in [1] either. The absence of such analysis limits the understanding of how the proposed method affects the broader capabilities of the distilled model.

- Minor: Inconsistent notations can be avoided - in lines 127-133, the different teachers are indexed by $(t)$ whereas in section 2.2 they are indexed by $k$.
- Minor: The readability of the paper can be improved by formatting the references appropriately in parentheses when they are not part of the sentence.

### Questions
- Adding the AdaLoss to MSE significantly improves over MSE results in Tables 13 and 14 on ALL tasks. Have you experimented with adding the AdaLoss to some other methods that perform well on dense tasks such as Hyb SmL1 or Standardize?
- Different teacher models also normalize the features in different ways during the pre-training step. For example, the features in the DINO head are L2 normalized and lie on a unit hypersphere. Some models use LayerNorms on the output features. Could there be a benefit in taking into account the normalizations used during pre-training while selecting appropriate feature standardization?
- What is the correlation between the teacher-matching loss and the downstream performance? For example, if the loss to a specific teacher is minimized, should that lead to the resultant model displaying properties most similar to that teacher? If the goal is to demonstrate the effectiveness of the feature standardization and its effect on downstream tasks, would it make more sense to consider teacher models which are distinctly good at specific tasks but significantly worse at other tasks? This might enable one to more clearly evaluate the downstream impact of different teachers and minimizing their losses.

Update after rebuttal (2024-11-24 AOE): I have reviewed the rebuttal from the authors and since my earlier concerns are mostly unaddressed, I would like to keep my score.

### Soundness
2

### Presentation
2

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
This paper presents a comprehensive study for training agglomerative models, that is to distill multiple diverse teacher models into a student model without labels by collectively "matching/aligning" the activation distributions, where the teacher models' activations are often significantly different from each other.  This paper is built on a prior art, the AM-RAIDO method and explores, from  the perspective of statistical normalization,  many different  designs of normalizing the activations of teacher models in the distillation loss functions. Based on the Hadamard matrices,  the identified PHI (PCA-Hadamard Isotropic) standarization method works the best in terms of training the best student model across different tasks. In experiments, the proposed method is tested in distilling a diverse set of foundation models (DFN CLIP, SigLIP, DINOv2 and SAM) into ViT-B/16 and ViT-L/16.

### Strengths
+ The proposed method is built on a solid empirical observation by accounting for the diverse distributions of different teachers' activations. 
+ The paper is well written and easy to follow.
+ The proposed empirical study is comprehensive in seeking the ``best" activation alignment space. 
+ The identified PHI standarization method works well in experiments compared to baseline approaches.

### Weaknesses
 - The motivation of distilling multiple foundation models into a student model could be elaborated. Although it is an interesting problem, what is the long-term vision? Will it be practically possible to train a student model that is smaller than all teacher model, yet works comparably well in a broad sense. For example, DINOv2 can produce meaningful latent features that are useful in many downstream tasks beyond those tested in the paper.  Will the distilled student be able to retain those? 
- The proposed method is trained without labels. It might be useful to discuss what effects the training datasets could have considering that different teacher models have been trained with diverse datasets. 
- It might be useful to investigate the effects of batch sizes in computing the PHI-S in distillation. Specifically, how does the batch size affect the estimation of the covariance matrix used to derive the PHI-S transformation, and what are the implications for the stability and convergence of the distillation process? 
- Although the propose method shows competitive performance using ViT-B/L models in comparisons to the ViT-H trained by AM-RADIO, it might be useful to train a ViT-H using the proposed method for a broader understanding of the competitiveness. 
- The proposed method is computational expensive (e.g. 14080 total GPU hours for the ViT-B/16 model). It might be useful to compute the overhead of the propose PHI-S in comparisons. What is the computational cost of calculating the PHI-S transformation, both in terms of time and memory, and how does this overhead scale with the dimensionality of the teacher activations and the number of teachers?

### Questions
Overall, this is a good paper. The reviewer would like to see the authors' rebuttal on the general questions listed in the weaknesses.

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
2

### Summary
The paper is interested in improving the agglomerative model distillation, a setting in which several teachers with different heterogenous representations are used to distilled a single student.

In this context, the author identify the fact that the representations of each teacher can be widely different, having different distribution and variances. This causes challenges on the optimization side, as the losses coming from a few different teachers might have a disproportionate effect on the overall summed loss, biasing the distillation toward those few teachers (the other ones being ignored).

To alleviate this, the authors propose a new normalization technique to apply on the target representations of the teachers, PHI-S, for PCA Hadamard Isotropic Standardization, that is invariant to data rotations (contrary to standard normalization). When equipped with this normalization, the authors report that the distillation is less biased toward SAM representations (which have the largest variance) and produces more balanced results on downstream tasks than the standard MSE loss.

The authors also compare their PHI-S normalization to the other normalization schemes that could be applied on the target teacher representations.

The benchmarks include:
* Zero shot classification
* Segmentation
* VQA 
* Probe 3D

### Strengths
* In depth analysis of the effect of different normalization schemes on representations
* Building the PHI-S normalization, and great illustration of its effect and its invariance to rotation
* A solid list of benchmarks, from various truly heterogenous teachers

### Weaknesses
The main weakness of the paper is the lack of real performance improvement coming from PHI-S when compared to more standard normalization schemes.

In Table 4, on ViT-L/16, where the authors mention that PHI-S is more dominant, we can see that the average rank of PHI-S places it as one of the best normalization technique. However, the ranks hide the fact that most differences are tiny and not very significant.
* When we look at Table 16, we see that rank 1 on classification is only due to 0.01% difference with standard standardization
* When we look at Table 17, we see that all normalization techniques are within less than 0.3% for most benchmarks

What those table seems to show (to me) is that in general normalization is really important, but the type of normalization used itself is not that impactful.

Overall, I think this normalization technique is interesting but the application to heterogenous teacher distillation is not that impactful.

### Questions
n/a

### Soundness
2

### Presentation
2

### Contribution
1
