# Hybrid Classification-Regression Adaptive Loss for Dense Object Detection

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
For object detection detectors, enhancing model performance hinges on the ability to simultaneously consider inconsistencies across tasks and focus on difficult-to-train samples. Achieving this necessitates incorporating information from both the classification and regression tasks. However, prior work tends to either emphasize difficult-to-train samples within their respective tasks or simply compute classification scores with IoU, often leading to suboptimal model performance. In this paper, we propose a Hybrid Classification-Regression Adaptive Loss, termed as HCRAL. Specifically, we introduce the Residual of Classification and IoU (RCI) module for cross-task supervision, addressing task inconsistencies, and the Conditioning Factor (CF) to focus on difficult-to-train samples within each task. Furthermore, we introduce a new strategy named Expanded Adaptive Training Sample Selection (EATSS) to provide additional samples that exhibit classification and regression inconsistencies. To validate the effectiveness of the proposed method, we conduct extensive experiments on COCO test-dev. Experimental evaluations demonstrate the superiority of our approachs. Additionally, we designed experiments by separately combining the classification and regression loss with regular loss functions in popular one-stage models, demonstrating improved performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a hybrid classification-regression adaptive loss function called HCRAL (Hybrid Classification-Regression Adaptive Loss) to improve the performance of the target detection model. HCRAL includes two modules: RCI (Classification and IoU Residual) module and CF (Conditional Factor) module. The RCI module is used for cross-task supervision and resolves task inconsistencies, while the CF module is used to focus on samples that are difficult to train in each task. In addition, the paper also proposes a new strategy called EATSS (Expanded Adaptive Training Sample Selection) to provide additional samples to optimize the loss function.

### Strengths
This paper proposes a novel loss function, Hybrid Classification-Regression Adaptive Loss (HCRAL), along with a new sample selection strategy, Expanded Adaptive Training Sample Selection (EATSS), for improving the performance of object detection models. The proposed HCRAL loss function consists of two modules: Residual of Classification and IoU (RCI) and Conditioning Factor (CF). The RCI module addresses inconsistencies between classification and regression tasks, while the CF module focuses on difficult-to-train samples within each task. The EATSS strategy provides more effective positive samples to optimize the loss function.

### Weaknesses
The innovation of this paper is limited, and the two parts proposed, HCRAL and EATSS, are relatively independent. At the same time, a large number of hyperparameters are introduced, which will increase the difficulty of hyperparameter adjustment in the experiment. The final experiment also shows that with the same backbone (R-101-RCN), the results of this paper's method are basically the same as VFL, and it does not bring significant improvement, which also makes me doubt the effectiveness of this method.

### Questions
- The experiments in this article are limited to the COCO data set, retinanet and FCOS. Experiments should be done on more detectors and data sets to verify the effectiveness of the method.
- While the paper provides some ablation studies on the individual components of the proposed approach, a more comprehensive analysis of the impact of each component on the overall performance would be beneficial.
- The motivation of equation 8 is very clear, but the article does not seem to detail the reasons for this design. It can be explained in more detail whether this RCI_reg is optimal when the conditions are met, and whether there is a clearer theoretical proof.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method which re-weights the classification and regression loss adhering to desired behaviour such as higher classification loss for high IoU samples etc. This is achieved through handcrafted functions to produce the weights. The authors also propose a method EATSS to increase the number of positive samples. The experiments are conducted on COCO using FCOS+ATSS and RetinaNet.

### Strengths
The strengths of this paper lie in the authors ability to highlight the subtle benefits of reweighing the losses according to the desired behaviour such as having high weights on classification for a box with large IoU and high regression weights if the class is correct. This enables the method to improve final performance.

### Weaknesses
 * One of the main weaknesses is the presentation, I found it quite hard to follow due to it being quite verbose, for instance the numerous equations that are introduced quite abruptly. I would suggest the authors take a high level narrative approach to the paper, rather than diving into the specifics straight away.
* The experiments are fairly limited, the only dataset used is COCO. There are many more available, the authors should be evaluating on them.
* The only networks the method is demonstrated on is FCOS+ATSS and RetinaNet. For a loss adaptation like this, the authors should be demonstrating on as many as possible.
* Taking up half a page to demonstrate hyper-parameter values is a significant proportion of the paper, this should be in the Appendix
* Why would ATSS 'omit certain samples characterized by high scores and high IoU that hold promise'? This isn't clear to me. Moreover, is this even an issue? I can see that the improvement is marginal.
* Why is Res2Net not applied to VFL? This isn't a fair comparison.
* Where do the quoted improvements of 1.1 and 1.2 mAP over VFL and GFL come from?
* Where are the error bars?
* Table 5, why do you see a decrease in mAP_50 when adding HCRAC? To me this shows it negatively affecting regression quality

### Questions
* Why would ATSS 'omit certain samples characterized by high scores and high IoU that hold promise'? This isn't clear to me. Moreover, is this even an issue? I can see that the improvement is marginal.
* Why is Res2Net not applied to VFL? This isn't a fair comparison.
* Where do the quoted improvements of 1.1 and 1.2 mAP over VFL and GFL come from?
* Where are the error bars?
* Table 5, why do you see a decrease in mAP_50 when adding HCRAC? To me this shows it negatively affecting regression quality

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes HCRAL to tackle the inconsistency problem between classification and localization. The methods mainly involve classification loss, regression loss, and label assignment. All the proposed modules follow the key idea of hard example mining to focus more on the difficult-to-train samples within each task. The presentation lacks clarity. The experimental results are not state-of-the-art.

### Strengths
Further study on the inconsistency problem between classification and localization is meaningful.

### Weaknesses
1. The proposed methods introduce many hyper-parameters, which must be tuned carefully. This undermines the generality of the methods. The method designs are technically complicated, involving both loss functions and label assignment. I suggest the author simply the method. The extensive hyperparameter tuning required, especially with the introduction of multiple parameters within the RCI and CF modules, raises concerns about the method's practical applicability and generalization to unseen datasets. The lack of a clear strategy for setting these parameters, beyond empirical search, further exacerbates this issue. The method's complexity, stemming from the combination of loss function modifications and label assignment strategies, makes it difficult to isolate the impact of each component and hinders interpretability.

2. The presentation of the experiment section is poor. What is the baseline in Tables 1,2,3 and 4? Also, Table 2 is weird since you report the results for various $\gamma$ in HCRAC, however, it is $\mu$. Where do you mention Table 5 in the context? It loses the connection. What is the baseline in Table 5? It is hard to believe that FCOS+ATSS got a 41.2 AP score. The experimental section lacks clarity and sufficient detail. The baselines for Tables 1-4 are not explicitly stated, making it difficult to assess the significance of the reported improvements. The inconsistent use of parameters ($\gamma$ vs $\mu$ in Table 2) creates confusion. The connection between Table 5 and the rest of the experiments is not clearly established, and the reported baseline AP of 41.2 for FCOS+ATSS seems unusually low, raising concerns about the experimental setup and the validity of the results.

3. The motivation is somewhat unclear. Why did you choose to design the three rules in Sec. 3.1.1 and Sec. 3.1.2? The rationale behind the specific design choices in Sections 3.1.1 and 3.1.2, particularly the three rules for classification and regression, is not well-explained. The connection between these rules and the overall goal of addressing the inconsistency between classification and localization is not clearly established, making it difficult to understand the underlying motivation for the proposed approach.

4. There are many highly related works that aim to solve the inconsistency problem between classification and localization missing comparison and reference, e.g. AutoAssign [1], OTA [2], DW [3]. Particularly, the proposed method does not surpass DW on the COCO test-dev set, which is auxiliary-module-free. The paper fails to adequately compare the proposed method with highly relevant works that address the inconsistency between classification and localization, such as AutoAssign [1], OTA [2], and DW [3]. The lack of comparison with these methods, especially given that the proposed method does not outperform DW on the COCO test-dev set, raises questions about the novelty and effectiveness of the proposed approach.

5. The improvement is almost non-existent. And more importantly, the reported SOTA results of previous methods are lower than the reference. As shown in Table 7, under the backbone R50, HCRAL only achieves 44.4 vs VFNet 44.8 [4] and GFLv2 44.3 [5]. Under the backbone R101, HCRAL 46.1 vs VFNet 46.7 and GFLv2 46.2. Under R101-DCN, HCRAL 49.3 vs VFNet 49.2. The reported performance gains are marginal, and the comparison with state-of-the-art methods is not favorable. The fact that the proposed method does not consistently outperform existing methods, such as VFNet [4] and GFLv2 [5], across different backbones, casts doubt on its practical significance.

6. There is a mistake in the proposed method. In the last paragraph of page 5, "the coordinates are partitioned into two regions based on $y(Score) = x(IoU) + \alpha$. In region 1, where samples exhibit higher scores compared to IoU values..." Clearly, $\alpha<0$. The samples just between the red line and the yellow line do not exhibit higher scores compared to IoU values. The description of the coordinate partitioning in the last paragraph of page 5 contains a logical error. The statement that samples in region 1 exhibit higher scores compared to IoU values is incorrect, particularly for samples falling between the red and yellow lines, where the score is not necessarily higher than the IoU, given that $\alpha < 0$.

7. The quality of the paper writing is low. It is difficult to understand the proposed method. Some variables are described before their formal appearance, e.g., "c is the diagonal length of the smallest enclosing box..." in Sec. 3.1.2.

    The appearance of the term $\mathcal{R}_{DIoU}$ is also very strange. It is not used in the previous equations. Besides, the description of EATSS in Sec. 3.2 is hard to understand. You'd better write down equations and variables, especially steps 4 and 6 in the algorithm.

    What is the "consensus matrix" mentioned below Eqn. 5?

    In the abstract, you can say "In object detectors, ..."

    On page 5, there is a typo "The the properties 1 and 2..."

    In the last paragraph of page 6, "to optimize RCI for every **ground** truth". And "...so as to find the biggest boundary to find a positive sample, ." Remove the comma. The paper suffers from several writing issues that hinder understanding. Variables are introduced before being formally defined, such as the description of 'c' in Section 3.1.2. The sudden appearance of $\mathcal{R}_{DIoU}$ without prior context is confusing. The description of EATSS in Section 3.2 is unclear, lacking the necessary equations and variable definitions, especially for steps 4 and 6. The term 'consensus matrix' below Eqn. 5 is not defined. There are also several grammatical errors and typos, such as "The the properties" and an unnecessary comma in the last paragraph of page 6, which further detract from the paper's readability.

### Questions
see weaknesses

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel classification loss, regression loss, and positive anchor sample strategy. The losses are designed based on both the classification and regression quality on the anchors. The proposed method is evaluated on the coco validation dataset with FCOS+ATSS and RetinaNet.

### Strengths
The designed losses use an RCI and a CF module to supervise classification and regression consistently on "difficult-to-train" samples.  An anchor selection strategy is proposed to find more optimizable samples.

### Weaknesses
 - There are many parameters involved in the loss, such as theta, mu, alpha, ep, gamma, and l in EATSS, which makes the design complicated and has low generalization ability.
- Compared with the state-of-the-art methods, the performances are not strong enough. As the results shown in Table 8 and Table 9, the improvement is about 0.2 (37.6 vs. 37.4 for Retina, 40.4 vs. 40.2 QFL, 37.4 vs. 37.2 F-EIoU, 40.2 vs. 40.0 GIoU).
- The EATSS seems to have a small influence on the results (41.3 vs. 41.2 AP). 
- Can the method be applied to more advanced detectors, like the two-stage Faster RCNN, and transformer-based DETR? Since the detector architecture FCOS, ATSS, and RetinaNet is classical but old, the proposed method will be more solid if the loss is valid on the recent stronger detector.

### Questions
see the "Weakness"

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
