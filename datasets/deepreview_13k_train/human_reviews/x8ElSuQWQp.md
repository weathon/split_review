# IW-GAE: Importance weighted group accuracy estimation for improved calibration and model selection in unsupervised domain adaptation

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
Distribution shifts pose significant challenges for model calibration and model selection tasks in the unsupervised domain adaptation problem---a scenario where the goal is to perform well in a distribution shifted domain without labels. In this work, we tackle difficulties coming from distribution shifts by developing a novel importance weighted group accuracy estimator. Specifically, we present a new perspective of addressing the model calibration and model selection tasks by estimating the group accuracy. Then, we formulate an optimization problem for finding an importance weight that leads to an accurate group accuracy estimation with theoretical analyses. Our extensive experiments show that our approach improves state-of-the-art performances by 22\% in the model calibration task and 14\% in the model selection task.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors investigate the importance weighting technique for simultaneously addressing model calibration and model selection in the context of unsupervised domain adaptation (UDA). The authors propose a novel importance-weighted group accuracy estimator, in which the importance weight is determined through a novel optimization problem. The effectiveness of this method is validated through theoretical analysis and experiments with one UDA method on one UDA dataset.

### Strengths
**(+)** The problems of model calibration and model selection, addressed in this paper, hold great significance for transfer learning applications.

**(+)** The IW-GAE method relies on importance weighting, a sound technique extensively validated by prior research on model calibration and model selection.

**(+)** A thorough analysis appears to provide theoretical support for the effectiveness of the proposed method IW-GAE.

### Weaknesses
 **(-)** The contribution's novelty is limited. The paper employs importance weighting to simultaneously address both the model calibration and selection problems. However, similar works, such as (You et al., 2019) for model selection and (Wang et al., 2020; Park et al., 2020) for model calibration, have been previously published. The primary difference between this paper and previous works appears to be the introduction of bin-wise importance weighting, as proposed in (Park et al., 2022). In summary, this paper mainly replaces the use of importance weighting in prior works with a more recent advanced importance weighting technique.

 **(-)** The empirical evaluation is inadequate, rendering the conclusion less reliable. The paper only examines one UDA method, MDD, on a single UDA dataset, Office-Home, for assessing the proposed method, IW-GAE. This limited scope does not provide sufficient empirical evidence for the effectiveness of IW-GAE. It is recommended to expand the experiments to encompass more UDA methods and datasets, following relevant works (Wang et al., 2020; You et al., 2019). In conclusion, the paper lacks the necessary empirical support for IW-GAE.

 **(-)** The proposed method may not be effective and practical, significantly diminishing the paper's contribution. While the empirical evaluation in the main text demonstrates the effectiveness of IW-GAE with MDD, the evaluation in the appendix reveals that IW-GAE does not outperform TransCal (Wang et al., 2020) with CDAN. Moreover, IW-GAE is considerably more complex, as it involves multiple hyperparameters compared to the hyperparameter-free TransCal (Wang et al., 2020) and DEV (You et al., 2019). IW-GAE requires at least three sensitive hyperparameters to be configured: temperature, the number of accuracy groups, and the number of bins, which does not guarantee its suitability for the model selection problem. In conclusion, the current, albeit insufficient experiments suggest that IW-GAE is not competitive and practical when compared with existing solutions.

 **(-)** The paper's presentation lacks clarity due to weak organization and missing information, particularly when compared to the well-structured writing in two highly relevant importance-weighting works (Wang et al., 2020; You et al., 2019) in the context of UDA. The current submission includes excessive background and proofs while omitting essential details about the algorithm and empirical evaluations. Furthermore, the motivation and novelty of this paper in comparison to existing importance-weighting works on model calibration and model selection remain unclear.

### Questions
Kindly see the weaknesses for specific questions and suggestions.

### Soundness
2 fair

### Presentation
2 fair

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
This paper concentrates on addressing model calibration and model selection issues within an Unsupervised Domain Adaptation (UDA) context, where a domain shift between source and target data is present. The authors have developed an importance-weighted group accuracy estimator to effectively handle distribution shifts. Numerous experiments on UDA benchmarks demonstrate the method's superior performance in both model calibration and selection tasks, compared to other baseline methods.

### Strengths
1. The paper concentrates on the critical and challenging aspects of model calibration and selection issues within the realm of unsupervised domain adaptation.
2. Unlike other model selection methodologies, this paper employs an optimization problem to determine the importance weight estimation from its Clopper-Pearson, aiming for precise group accuracy estimation.
3. The estimation of group accuracy in the distribution-shifted domain is supported by a solid theoretical analysis.

### Weaknesses
1. The legend and meaning in Figure 1 are unclear and difficult to comprehend. The annotation for Figure 1 is excessively lengthy and could benefit from moving some sections to the main body of the paper as illustrative examples.
2. The experiments conducted in the main paper don't sufficiently verify the proposed method's effectiveness. Other datasets, such as DomainNet, and other baselines in Unsupervised Domain Adaptation (UDA), should be incorporated. The current experiments lack diversity in terms of both datasets and baseline methods, making it difficult to assess the generalizability of the proposed approach. Specifically, the paper should consider including more challenging domain adaptation scenarios and compare against state-of-the-art UDA techniques.
3. Several analyses and discussions residing in the appendix are crucial to demonstrating your method's effectiveness. It is advised to relocate these sections to the main body of the paper. The current organization makes it hard to follow the core arguments and fully appreciate the method's strengths. For instance, the detailed analysis of the optimization error and its correlation with group accuracy estimation errors should be in the main text.
4. The paper asserts that the proposed method is not applicable to fixed large-language models in IW-GAE. Thus, a more comprehensive discussion and additional experiments are recommended. The limitations of the proposed method regarding large language models are not sufficiently explored. The paper should provide a more in-depth analysis of why the method is not directly applicable and potentially explore alternative approaches or modifications to address this limitation.

### Questions
Please refer to the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method named IW-GAE that uses estimated importance weight to measure the group accuracy, and use the measured group accuracy in the task of model calibration and the task of model selection in UDA setting.

### Strengths
1. This paper seems to be both theoretically solid and experimentally sound. 
2. This paper is well-motivated.

### Weaknesses
 For the current submitted version, I vote a boardline accept score and below are my remaining concerns.

(1) This paper proposes to achieve calibrated accracy from the perspective of group accuracy. However, it seems to me that intuitively, group accuracy is more coarse-grained than the accuracy of each individual. Thus, I am curious that, will this direction of group accuracy leads to a lower upper limit than the other branches of method?

(2) Secondly, if I am not wrong, the logic of this paper's proof seems to be, (1) the proposed optimization algorithm can optimize over the upper bound of source group accuracy estimation error. (2) the source group accuracy estimation error serves as a upper bound of the target group accuracy estimation error. Thus, because of (1) and (2) one by one, the proposed optimization algorithm works. My question w.r.t. this is that, are your two upper bounds tight enough to make the thing theoretically meaningful? Taking Eq. 5 as an example, while I do not check the math very carefully, it seems that the target group accuracy estimation error is upper bounded by the source group accuracy estimation error multipled with both M and the other item in the bracket. Thus, both these two items, if large to a certain scale, while make the optimization over the upperbound sub-meaningful. I understand that the authors have discussed that they will tighten the bound by "bound the maximum and minimum values of IW". However, I think this part should be elaborated as the tightness of the bound is important from my perspective. Besides, I also appreciate if the other impacts of this "bound the maximum and minimum values of IW" operation can be discussed. For example, will this operation hurt the current theoretical flow?

(3) The last small question I have is that, the authors claim in their conclusion that, applying their model on large language model does not get improvement. They thus conclude that, "the pre-trained large-language model is less subject to the distribution shifts". Can another potential reason behind this observation be that the proposed method is poorly scalable to larger models? I hope either discussion or experiments can be made on the scalability of the proposed method.

### Questions
For the current submitted version, I vote a boardline accept score and below are my remaining concerns.

(1) This paper proposes to achieve calibrated accracy from the perspective of group accuracy. However, it seems to me that intuitively, group accuracy is more coarse-grained than the accuracy of each individual. Thus, I am curious that, will this direction of group accuracy leads to a lower upper limit than the other branches of method?

(2) Secondly, if I am not wrong, the logic of this paper's proof seems to be, (1) the proposed optimization algorithm can optimize over the upper bound of source group accuracy estimation error. (2) the source group accuracy estimation error serves as a upper bound of the target group accuracy estimation error. Thus, because of (1) and (2) one by one, the proposed optimization algorithm works. My question w.r.t. this is that, are your two upper bounds tight enough to make the thing theoretically meaningful? Taking Eq. 5 as an example, while I do not check the math very carefully, it seems that the target group accuracy estimation error is upper bounded by the source group accuracy estimation error multipled with both M and the other item in the bracket. Thus, both these two items, if large to a certain scale, while make the optimization over the upperbound sub-meaningful. I understand that the authors have discussed that they will tighten the bound by "bound the maximum and minimum values of IW". However, I think this part should be elaborated as the tightness of the bound is important from my perspective. Besides, I also appreciate if the other impacts of this "bound the maximum and minimum values of IW" operation can be discussed. For example, will this operation hurt the current theoretical flow?

(3) The last small question I have is that, the authors claim in their conclusion that, applying their model on large language model does not get improvement. They thus conclude that, "the pre-trained large-language model is less subject to the distribution shifts". Can another potential reason behind this observation be that the proposed method is poorly scalable to larger models? I hope either discussion or experiments can be made on the scalability of the proposed method.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the problem of calibration in unsupervised domain adaptation.
 The proposed method is built on the importance sampling principle. The data is split into groups and an importance weight is defined for each group. The optimal scaling temperature is defined as the one that minimizes the difference between two source domain accuracy estimations.

### Strengths
The paper address an important problem in which there isn't still a satisfied solution.
I think the research direction proposed by the paper has a merit.  However, the paper needs to be better written and should include a clear motivation and justification for the proposed method.

### Weaknesses
The paper is not clearly written. An algorithm box that states the steps of the proposed algorithm can improve a lot the paper readability.
The groups are defined in section 4.2 are exactly the groups which are defined by the ECE measure based on the confidence values.  You can use this to simplify the presentation.
In eq 8 (and eq 34) it is not clear how the optimized function depends on the temperature t?  As far as I understand the only thing  that is modified by t is the group arrangement of the target data.
My my concern is the justification of the proposed method. The algorithm looks for a temperature  that  minimizes the difference between two source domain accuracy estimations (one direct Monte-Carlo based estimation (MC) and one using importance sampling (IW)). It is not clear to me why a temperature that minimizes this accuracy estimation difference, is the one that yields improved calibration?

### Questions
hy a temperature that minimizes this accuracy estimation difference, is the one that yields improved calibration?

In eq 8 (and eq 34) it is not clear how the optimized function depends on the temperature t?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
