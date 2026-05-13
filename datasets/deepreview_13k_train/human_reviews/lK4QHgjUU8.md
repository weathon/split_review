# SteinDreamer: Variance Reduction for Text-to-3D Score Distillation via Stein Identity

- Decision: Reject
- Scores: 3, 5, 6, 6

## Abstract
Score distillation has emerged as one of the most prevalent approaches for text-to-3D asset synthesis.
Essentially, score distillation updates 3D parameters by lifting and back-propagating scores averaged over different views.
In this paper, we reveal that the gradient estimation in score distillation is inherent to high variance.
Through the lens of variance reduction, the effectiveness of SDS and VSD can be interpreted as applications of various control variates to the Monte Carlo estimator of the distilled score.
Motivated by this rethinking and based on Stein's identity, we propose a more general solution to reduce variance for score distillation, termed \textit{Stein Score Distillation (SSD)}. SSD incorporates control variates constructed by Stein identity, 
allowing for arbitrary baseline functions. This enables us to include flexible guidance priors and network architectures to explicitly optimize for variance reduction.
In our experiments, the overall pipeline, dubbed \textit{SteinDreamer}, is implemented by instantiating the control variate with a monocular depth estimator.
The results suggest that SSD can effectively reduce the distillation variance and consistently improve visual quality for both object- and scene-level generation.
Moreover, we demonstrate that SteinDreamer achieves faster convergence than existing methods due to more stable gradient updates.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces an interpretation of score distillation sampling by integrating the Stein identity. This interpretation underscores the significance of selecting appropriate control variates for reducing variance to achieve efficient convergence during training. The authors propose the use of a monocular depth estimator for efficiency and demonstrate that their method effectively reduces variance during updates, leading to faster convergence compared to other score distillation sampling techniques.

### Strengths
- The paper is well-written and easy to understand.
-The adoption of a monocular depth estimator is a simple yet effective approach to reducing variance in text-to-3D synthesis.

### Weaknesses
 **Limited novelty**
- It is noted that the primary focus of this paper is to interpret score distillation sampling using the Stein identity and to reduce variance through the incorporation of monocular depth estimation. However, Kim et al [1] have already discussed a similar interpretation of the Stein identity and the importance of baseline function selection for convergence and efficiency. Although the specific focus of Kim et al. is different (visual editing), the core inspiration appears to be similar. Therefore, it is recommended for the authors to acknowledge and discuss the already incorporated findings of Kim et al. In this context, while the inclusion of monocular depth estimation for efficient text-to-3D synthesis is intriguing, the novelty of the proposed method may be considered weak. Thus, given the similarities in findings and interpretation, the distinguishing factor appears to be only the choice of baseline functions for specific tasks, the adoption of a monocular depth estimator as the control variate. 

**Lack of Quantitative Evaluation**
- To support their claims of qualitative improvement over Score Distillation Sampling (SDS) and Variational Score Distillation (VSD), the authors should provide a quantitative evaluation. Although the video demonstration provided by the authors indicates some improvement, issues such as the "Janus problem" in the dog statue are still present. While Figure 5 does demonstrate a reduction in variance compared to other methods, it does not necessarily guarantee improved quality. Figure 5 suggests that SSD reduces variance during training when compared to other methods, which may lead to fewer artifacts at similar training iterations, especially in comparison to ProlificDreamer. However, quality improvements are not guaranteed after fully training ProlificDreamer until convergence, as fine-tuning the diffusion model may require more computational time. Hence, it is recommended that the authors claim that the proposed method effectively reduces variance during training, which ensures better quality at an “early stage” not overall quality improvements. This concept is also supported by Figure 7 (although additional figures may be necessary for validation, just one example is severely not enough), clearly indicating that the reduced variance achieved by the proposed method results in faster convergence rather than overall quality improvement.
- Additionally, the comparison in the paper appears to be based on a limited number of samples. It is beneficial to conduct experiments with a broader range of prompts to assess the robustness of the proposed method in reducing variance.

### Questions
As demonstrated in the Weaknesses section, the authors should make a comparison with the prior work of Kim et al. and discuss any differences if there exists new interpretation.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a variance reduction method for training text-to-3d synthesis models based on pretrained diffusion models. The authors first point out that prior work in this domain share the the same gradient in expectation, but differs in the Monte Carlo estimator. Then, they show that the performance difference can be explained by the variance of the estimator. Given this observation, they proposes a new variance reduction technique based on Stein's identity that generalizes the estimator in a previous work (SSD). The new estimator is shown to have lower variance and improve the visual quality of 3d scenes in experiments.

### Strengths
* The proposed method is well-motivated. Given the observation that prior gradient estimators have the same expectation and the performance is highly dependent on variance, it is very sensible to investigate better variance reduction techniques for this approach.

* The method is shown to have less variance than prior methods in experiments. 

* The generated 3d scenes are visually better than prior methods (e.g., in Figure 3).

### Weaknesses
 * Introducing another network for variance reduction increases the training cost per iteration, which might outweigh the benefit brought by having lower variance per iteration. It would be more convincing to include a wall-clock time comparison between different methods.

* One biggest weakness of this work is the insufficient empirical evaluation. The variance plot is one face of the story. However, it would greatly strengthen the work if the authors can show the 3d synthesis model learned by SSD is quantitatively better than the baselines given the same compute. In Figure 7, the improvement is very marginal considering the additional cost of training the control variates.

* The work can be positioned better in the literature. Sticking the landing  is not cited. The citations on Stein's identity can be improved. The generalized form of the Stein's identity in (7) is first introduced in Gorham & Mackey (2015).

### Questions
I would potentially raise the score if the wall-clock time comparison is included.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work propose a novel regularization term to help SDS achieve low variance, named Stein Score Distillation (SSD). The proposed SSD is based on Stein's identity, which is natually zero-means to serve as variance control. The method starts from the insights that lower variance produces better performance with emprical results from DreamFusion and ProfilicDreamer. The experimental results demonstrate better shape, texture, and details on object and scene level generation.

### Strengths
- originality: the proposed method for text-to-3d generation is relatively novel, with inspiration from Stein's identity to reduce the variance in  the training process of text-to-3d.
- quality: this work starts from the emprical insights and combine with the proper mathematical solution to promote text-to-3d application. The experimental results outperform the previous reprsentative works, such as DreamFusion and ProfilicDreamer.
- clarity: the presentation of this work is good, with clear formluation and structure organization. It is reader friendly.
- significance: this work is of significance, especially in an age of AIGC.

### Weaknesses
 - The experimental results are not as extensive as ProfilicDreamer. Compared with 10 object and 8 sence level generated content on https://ml.cs.tsinghua.edu.cn/prolificdreamer/, there are only 6 object and 4 sence level in this work and supplementary demo.
- Looking at the Figure 5, there existing the following confusions: 1) DreamFusion seems not converge for some cases, especially for "A Car made out of Sushi." and "A Lion Fish". Maybe DreamFusion needs more iterations? 2) The proposed SteinDreamer can be overfitting after ~120k training steps, with gradually increasing variance. How could this happen?
- Also, for comparing the convergence speed, it is much better to compare when all the methods are fully converged, especially for DreamFusion and ProfilicDreamer.
- Possible typos: 4th para. in Inroduction, 'aligns with with that' --> 'aligns with that'

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a more general solution to reduce variance for score distillation, termed Stein Score Distillation (SSD). SSD incorporates control variates constructed by Stein identity, allowing for arbitrary baseline functions. The experiment results demonstrate the effectiveness of the proposed method.

### Strengths
1. The paper is well-written.
2. The experiments show that the results are better than the baselines.
3. This work proposes to rethink the SDS/VSD in the way of variance, which is interesting.
4. The idea is novel.

### Weaknesses
1. My main concern is that why a lower variance during optimization is helpful for the final quality? Although there are some empirical results in Sec 3 show that there are some corelation between variance and generated quality, I think a more convincing justification should be given. Maybe a more detailed theoretical or intuitive explanation should be given.
2. No quantitative results are given to compare the proposed method and baselines in terms of the visual quality.

### Questions
1.  How will the baseline function effects the final results? Since the Stein identity always holds, what is the relationship between the baseline function and the final performance?
2. Can you show a 2D experiment? (Using SSD to directly optimize an image.) This will strengthen the effectiveness of SSD.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
