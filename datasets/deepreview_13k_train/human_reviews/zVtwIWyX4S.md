# MaxSup: Fixing Label Smoothing for Improved Feature Representation

- Decision: Reject
- Scores: 5, 8, 5, 5

## Abstract
Label Smoothing aims to prevent Neural Networks from making over-confident predictions and improve generalization.
Due to its effectiveness, it has become an indispensable ingredient of the training recipe for tasks such as Image Recognition and Neural Machine Translation. Despite that, previous work shows it encourages an overly tight cluster in the feature space, which `erases' the similarity information of individual examples, resulting in impaired representation learning. By isolating the loss induced by Label Smoothing into a combination of a regularization term and an error-enhancement term, we reveal a previously unknown defect, i.e., it indeed encourages classifiers to be over-confident, when they make incorrect predictions. To remedy this, we present a solution called Max Suppression (MaxSup), which consistently applies the intended regularization effect during training, independent of the correctness of prediction. By visualizing the learned features, we show that MaxSup successfully enlarges intra-class variations, while improving the inter-class separability. We further conduct experiments on Image Classification and Machine Translation tasks, validating the superiority of Max Suppression. The code implementation is available at [anonymous repository](https://anonymous.4open.science/r/Maximum-Suppression-Regularization-DB0C).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a label regularization method called Max Suppression. It shows that vanilla label smoothing has two components: regularization and error-enhancement term. The error enhancement term has negative effects, and the paper proposes an alternate formulation that mitigates its effect by replacing z_gt with z_max.

### Strengths
1. The paper is easy to read and well-written.
2. Evaluation is performed on multiple modalities to show its application.
3. An in-depth analysis of the problem of label smoothing was done.

### Weaknesses
1. The paper fails to explain the reason behind why replacing z_gt with z_max is the optimal choice.
2. The targets created by the approach are not a probability, and hence, using it with cross-entropy loss may not be correct.
3. Figure 2 is very confusing and difficult to understand.
4. The paper compares the approach across different modalities but should also include results with multiple datasets from the same modality and various architectures (Like done in OLS [2] and Zipf [3])). A lot of the tables could be easily merged to make space for more results.
5. Label Smoothing is known to affect semantic class relationships [1]. The baseline approaches (OLS [2], Zipf [3]) also formulate their loss function to mitigate this, but it is not handled in the proposed approach.
6. In Tables 4 and 5, comparison is only done with the vanilla label smoothing. The improvement is minimal. It would be interesting to see the results of baseline approaches on them.

### Questions
1. In the ablation (Table 1), The paper showed removing the Error-Enhancement is beneficial. Why is that not compared/proposed as inplace for replacement?
2. Why is the error-enhancement term having a huge negative impact? The logits of the correct class are generally higher while training.
3. How does it impact the inter-class relationship?

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
This paper analyses the effect of label smoothing for image classification. By analysing the loss they find that label smoothing  (compared to vanilla cross entropy) encourages the model to be more confident when it is incorrect. Based on this finding they propose MaxSup, a similarly simple regularisation approach that penalises the max logit rather than the logit corresponding to the ground truth label. They then demonstrate consistent improvements over label smoothing in terms of test accuracy on a range of experiments.

### Strengths
- The paper presents interesting analysis into a deeper understanding of label smoothing, which I appreciate. This understanding is then leveraged to propose a new approach.
- The proposed approach is very simple, and seems to perform well empirically, making it a strong candidate for a drop-in replacement/improvement on label smoothing. The **simplicity is a big plus**, as it has the potential for wider adoption and impact. Moreover, the supporting analysis seems to be solid, reducing the likelihood of the performance failing to generalise beyond the experiments in the paper.

### Weaknesses
Although I have tried my best to cover the content in enough detail, due to time constraints, I may have misunderstood/missed aspects of the paper. I encourage the authors to correct/clarify this if it is the case. I also welcome the authors to challenge me if they disagree with some of the more subjective points I make. I will actively engage during the rebuttal period.

1. Positioning relative to existing/concurrent work. Overall, the paper lacks appropriate acknowledgement to existing work relating to label smoothing.
    1. The empirical notion that label smoothing results in more confident errors has been around since 2022 [1], whilst the authors claim this to be a completely novel revelation. Moreover, the type of analysis performed in this paper is also present in [2]. Although [2] is not peer reviewed, and addresses a different problem, it contains substantial overlap with section 3 of the paper. In particular how the logits are suppressed differently depending on whether a prediction is likely to be correct or not. Note that I do not suspect any plagiarism, however, as existing/concurrent work, the above references should be clearly acknowledged and contextually placed in relation to this work. Although it is somewhat grey, I would deem [2] to be concurrent work as it is not published, but has been available on arxiv since March of this year. The authors should accordingly temper any claims of  "previously unknown/novel".
    2. The authors also do not reference a number of relevant background work investigating label smoothing in the context of knowledge distillation [3,4,5], which are particularly concerned with the "erasure of knowledge". [6], which empirically shows label smoothing degrades transfer learning and also empirically measures increased tightness and separation of feature clusters, is an especially important reference but is also missing. Similarly, works that investigate the effect of LS on neural collapse also measure these empirical properties [7,8]. The authors should add these papers to the related work. [6] also examines a regulariser that minimises the l2-norm of the logits (logit penalty), which is conceptually similar to MaxSup since the l2-norm tends to be dominated by the max logit (or MaxSup is like minimising the infinity-norm). Ideally, this would be added to Tabs. 2 and 3 although at the least it should be clearly referenced and discussed in the paper.
2. Lacking analysis. Although it is somewhat intuitive that encouraging confidence on errors would hurt generalisation, the additional analysis that is performed is somewhat lacking.
    1. The authors analyse the inter-class separability and intra-class variation of feature representations, however, they use only the illustrative plots found in [9], which are not very scientific. Since [9] was published in 2019 there have been a number of works that directly quantify separability/variation (e.g. [6,7]). It would greatly strengthen this part of the work if the authors were to provide such numerical measures over the training and test datasets. Moreover, there is a lack of comparison to vanilla CE, which should be the real baseline.
    2. The discussion in Sec. 3.3 is somewhat handwavy. As the visualised data is primarily *training* data, better class separation doesn't necessarily mean better accuracy on *test* data. There is also no reference/experiment to support the claim that greater intra-class variation leads to improved representation learning. The authors should use [6] as a reference in the context of these claims, as in [6] they indeed show empirical results similar to the authors claims by comparing the test accuracy vs transfer linear probing (representation learning) performance of label smoothing. Additionally, the submission would be strengthened with a transfer learning experiment (like in [6] Tab. 1). It would be great if it can be shown that MaxSup is able to improve test accuracy without sacrificing transfer performance (unlike label smoothing). The semantic segmentation experiment seems to do this, however, it is unclear whether or not the downstream segmentation loss also includes MaxSup/LS and the experiment lacks a vanilla CE baseline (which the authors should include).
    2. It is not really clear how the behaviour in Sec 3.3 follows from the analysis in 3.1/3.2. The authors ideally should be able to link the theory with regards to the different training losses to the difference in observed separation/variation. This, again, would greatly improve Sec 3.3.
    2. The paper would benefit from some additional explicit discussion on how increasing confidence on training errors would lead to worse generalisation in terms of top 1 test accuracy. Although it seems to make sense superficially, in my mind there is still a gap in reasoning. For example adding a sentence like: LS weakens the strength of supervision to the GT class on errors, when a model really should be learning to correct itself rather than being regularised to prevent overfitting. 
3. Presentation, missing information and clarity.
    1. The alpha schedule in Tab. 6 comes out of nowhere. It seems to be referenced after Eq. 7 even though it does not appear there. This seems to just be sloppy writing and needs to be clarified properly. Although Tab. 6 suggests that an alpha schedule is generally beneficial, it is orthogonal to the main body of the paper. I think the paper would benefit either from an expanded (and separate) discussion and analysis on the alpha schedule, or just simply from its removal from the paper.
    2. The wording and notation in Sec. 3.1 is confusing. From line 124 onwards the use of "cross entropy", "label smoothing" and "loss" are combined in different ways to refer to distinct things that are easily confused. For example, the "cross entropy loss with label smoothing" is not the same thing as the "label smoothing loss" or the "cross entropy between two distributions" but all are related and interlinked. I would like to see the authors improve the clarity of Sec 3.1 with updated wording and maybe some additional underbraces to the equations (like in Eq. 6). Sec 3. could also benefit from an illustrative figure for LS vs MaxSup (e.g. using a bar chart to represent logits), although this is not essential.
    3. Fig. 2. is difficult to interpret. It is hard to compare when it is not clearly labelled on the figure which row is LS and which is MaxSup. The decision boundaries arguably don't contribute to the takeaways so the diagrams may be easier to interpret if they are omitted. The choice of showing test and training data together on the same plot without easily being able to tell the difference without pixel peeping is also poor (and this also doesn't contribute to the takeaways about variation/separation). Finally, I am generally lukewarm on these plots (as mentioned in 2.) as their axes can easily be linearly scaled to visually tell different stories and it is hard to normalise for this scaling (for example Muller [9] scale their axes but the authors in this paper do not). As mentioned before, numerical measures [6,7] may convey the point more clearly.
    3. Although I like the CAM figures, the authors should add a comparison to the baseline cross entropy model as well. The figures would also benefit from subcaptions describing what to look out for, e.g. "label smoothing fails to consider the tail of the monkey".
    4. Overconfidence in the context of model calibration and overconfidence in the sense of error enhancement are not clearly delineated. LS often reduces the former [9,10], but in this paper the authors show that LS increases the latter. The authors should make clear the difference between the two definitions of overconfidence to avoid confusion. This is important since LS is widely known to reduce calibration overconfidence [9,10].
    5. Generally speaking, there are a number of grammar and spelling errors. The authors should use an automated grammar checking tool to correct these.
4. Choice of Deit as a model. This choice of model as a baseline to perform ablations and analysis is odd. Deit uses hard label distillation on an additional token during training. Although this doesn't necessarily conflict with the theory presented in the paper, it does add unnecessary complexity to the experiments in my opinion. Additionally, it is unclear when and where Mixup/Cutmix are used. To me it makes a lot more sense to perform a simple analysis of vanilla CE vs label smoothing, rather than also throwing in all the additional label augmentations that come with Deit by default that may muddy the results (cutmix, mixup, hard-label distillation). Although this is a comparatively minor complaint, I would prefer it if the authors simply used ResNet-50 for Tab. 1 and Fig. 2.. Alternatively, the authors can add the Deit distillation into the theory/discussion of Sec 3.

I'd like to note that I think the **core of the paper is strong**, especially the proposed MaxSup, and am **keen to increase my score**. However, I believe that there are many issues with the manuscript in its current state that need to be addressed before it is ready for publication. I look forward to updates from the authors. Hopefully, the paper will improve via the review process.

**Edit: after extensive discussion with the authors and a substantially revised manuscript, I believe the submission has improved considerably and I am happy to raise my score from 5 to 8.**

**Edit 2: I will leave an additional comment here as it is past the deadline for discussion. I believe I have found a potential flaw in MaxSup, that exists outside of the scope of this paper (and thus may be addressed in future work). In the case of soft training targets (e.g. knowledge distillation) MaxSup may lead to potential instability. For example, for a uniform target presented by a teacher model, the penalisation of the max logit may prevent the student from stably also producing a uniform softmax output. The constant downward gradient on the max logit may jump around as the max logit varies as the softmax fluctuates locally around the uniform target. This does not affect my score as the paper does not consider training with soft targets, however, it does point to potential space for improvement in the future.**

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper advances the Label Smoothing technique and presents a Max Suppression method. Extensive experiments on image classification and neural machine translation tasks verify the effectiveness of the proposed method. Also, this work provides several theoretical analyses to introduce the proposed method.

### Strengths
1.	This work reports both CV and NLP results, which is a positive aspect.
2.	This method sounds sensible.
3.	This work presents several theorems to introduce the proposed method.

### Weaknesses
1.  While the method proposed in this work offer some novel ideas, the overall contribution seems to be more of an engineering refinement.

2.  The experimental results (e.g., Tables 3 and 4) do not show a substantial improvement over existing approaches. 

3.  In my opinion, the primary reason for these experimental results is that only a minor enhancement was made to the Label Smoothing technique, without fundamentally overcoming its inherent limitations or proposing a more robust method. To advance in this direction, the focus should be on exploring the relationships between categories to derive more accurate soft-label encodings for each category, thereby addressing the inherent limitations of Label Smoothing.

4.  Providing two specific examples of Eq. (1) and Eq. (8) would help in understanding the difference between Label Smoothing and Max Suppression.

5.  Lines 299-302: Providing the quantitative results regarding inter-class separability and intra-class variation would be beneficial in better elucidating Figure 2.

Small issues:

1.  Line 87: calibrated classifiers M¨uller et al. (2019). -> calibrated classifiers (M¨uller et al. 2019).

2.  Which dataset was used in Figure 2?

### Questions
See weakness for details.

### Soundness
3

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
This paper reveals that Label Smoothing Loss can be decomposed into two opposing components: a regularization term and an error-enhancement term. Preliminary studies confirm that the performance improvements from Label Smoothing Loss are solely due to the regularization term. Based on this insight, MaxSup is proposed to eliminate the error-enhancement term for incorrect predictions. Experiments are conducted on Image Classification and Machine Translation.

### Strengths
1. Decomposing the Label Smoothing Loss to two terms is interesting and removing the error-enhancement term sounds reasonable. 

2. The experiments show that MaxSup is better than the LS, validating the effectiveness.

### Weaknesses
1. The motivation of MaxSup is not entirely clear. In Section 3.1, the decomposition of Label Smoothing Loss into a regularization term and an error-enhancement term is presented. Preliminary studies suggest that using only the regularization term is effective. However, if minimizing the regularization term alone is sufficient, it is unclear why MaxSup is necessary. A more thorough explanation of why the error-enhancement term needs to be specifically addressed, rather than simply minimizing the regularization term, would strengthen the paper's motivation.

2. The potential for incorrect prediction samples to introduce noise during the optimization of MaxSup needs further investigation. Specifically, how does the method handle cases where the model is confidently incorrect? Does this lead to instability or degraded performance in certain scenarios? A more detailed analysis of the noise impact and potential mitigation strategies would be beneficial.

3. The results of using only the regularization term are not provided in Table 2 and Table 3. Including these results would allow for a direct comparison with MaxSup and provide a clearer understanding of the contribution of each component.

4. Figure 2 showcases samples correctly classified by the proposed method but incorrectly classified by the baseline. However, to provide a balanced perspective, it would be helpful to also include examples where the baseline outperforms the proposed method. This would allow for a more comprehensive evaluation of the strengths and weaknesses of MaxSup.

5. Some notations are confusing:
    a. The definition of $q$ in Lemma 3.2 is not immediately clear. While it is mentioned to be found in the Appendix, explicitly stating its meaning within the main text would improve readability.
    b. The absence of $\lambda$ in Eq. (7) is concerning. Its role and potential impact on the equation should be clarified.

6. There are some typos that need to be addressed, e.g., Line 266, "Similarity:"

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
