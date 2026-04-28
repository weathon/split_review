# Evaluating the Evaluators: Are Current Few-Shot Learning Benchmarks Fit for Purpose?

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 8, 3

## Abstract
Numerous benchmarks for Few-Shot Learning have been proposed in the last decade. However all of these benchmarks focus on performance averaged over many tasks, and the question of how to reliably evaluate and tune models trained for individual tasks in this regime has not been addressed. This paper presents the first investigation into task-level evaluation---a fundamental step when deploying a model. We measure the accuracy of performance estimators in the few-shot setting, consider strategies for model selection, and examine the reasons for the failure of evaluators usually thought of as being robust. We conclude that cross-validation with a low number of folds is the best choice for directly estimating the performance of a model, whereas using bootstrapping or cross validation with a large number of folds is better for model selection purposes. Overall, we find that existing benchmarks for few-shot learning are not designed in such a way that one can get a reliable picture of how effectively methods can be used on individual tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims at rethinking how we could better evaluate the performance of few-shot learning methods and how we could select models in few-shot settings. The authors measure the estimated accuracy from different estimators to show that they all have non-negligible gaps from the oracle estimator. Also, the authors investigate different ranking strategies for model selection in few-shot learning. Finally, the authors provide insights that existing evaluation approaches are all not competent enough. Future works may need to design specialized evaluation procedures for evaluating few-shot learning performance.

### Strengths
++ This paper provides some interesting analysis and viewpoint on the evaluation, model selection for few-shot learning tasks. It could bring researchers to take a step back and reconsider the essential parts in few-shot learning, like what is a more proper way to evaluate models, and how to select models that can be better used in real-world cases.

++ The experimental results are comprehensive, involving various meta-learning datasets and meta-learning algorithms, which enhances the soundness of the conclusions from this paper.

### Weaknesses
-- I am uncertain about how useful in real application would the conclusion from this paper be. After all the experimental investigation and analysis, the suggestion given by the authors is that every few-shot setting should design specialized evaluation procedure. This would be laborious and complicated for future works which makes this suggestion infeasible. Also, there is no example given by the authors about how to design the evaluation procedure based on certain specific tasks. The lack of concrete guidance on how to develop these specialized evaluation procedures significantly limits the practical applicability of the paper's findings. It's unclear what specific steps researchers should take beyond simply acknowledging the need for task-specific evaluation. The paper does not address the computational cost associated with developing and implementing these specialized evaluation procedures, which could be a significant barrier for many researchers.

-- I assume "CV" is short for "cross-validation" and "CV LOO" means "cross-validation leave-one-out", right? However, there is no explanation in the paper about what they mean, which causes confusion. The paper should explicitly define these terms, especially considering that different variations of cross-validation exist. The lack of clarity on these fundamental concepts undermines the accessibility of the paper, particularly for readers who might not be intimately familiar with all the nuances of cross-validation techniques.

-- From the results in Tab. 1, it seems that all estimators generally have under-estimated accuracy compared with the oracle method, so all of them should be pessimistic. However, in the conclusion section, it seems that only some of the estimators like LOO-CV and Bootstrapping are pessimistic estimators. I am wondering whether there exist an inconsistency or I have misunderstood the results in Tab. 1 and the conclusion on "Performance Estimation". The distinction between the general underestimation and the specific claim about pessimistic estimators (LOO-CV and Bootstrapping) is not clearly explained. The paper needs to clarify whether the term 'pessimistic' is used in a general sense (underestimation) or in a more specific sense (lower variance and underestimation) and provide a more detailed explanation of the statistical properties of each estimator.

### Questions
-- From the results in Tab. 1, it seems that all estimators generally have under-estimated accuracy compared with the oracle method, so all of them should be pessimistic. However, in the conclusion section, it seems that only some of the estimators like LOO-CV and Bootstrapping are pessimistic estimators. I am wondering whether there exist an inconsistency or I have misunderstood the results in Tab. 1 and the conclusion on "Performance Estimation".

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores the reliability of evaluation methods for few-shot learning (FSL) models. The authors investigate how well current benchmarks and validation strategies predict the performance of FSL models on individual tasks. They find that cross-validation with a low number of folds is best for direct performance estimation, while bootstrapping or cross-validation with a large number of folds is more suitable for model selection purposes. However, they conclude that with current methods, it is not possible to get a reliable picture of how effectively methods perform on individual tasks.

### Strengths
+ The paper addresses an underexplored and realistic aspect of few-shot learning—task-level validation. 
+ This paper is easy to read. 
+ It provides an extensive experimental analysis across different datasets and evaluators, offering a comprehensive view of the current state of FSL benchmarks.
+ The paper identifies the best performing evaluation method, which is useful for future research and practical applications.

### Weaknesses
Firstly, it is hard for me to estimate the novelty and contributions of this paper. The paper is more like an analysis paper but the conclusions are not clear. From the end of the introduction, all three conclusions are weak. Moreover,
- I don't fully understand the part related to the first question: all three evaluations (hold-out, cross-validation, and Bootstrapping) are widely used for few-shot evaluations. The only difference is using the support set only. But if we treat the support set as the whole set, there are no obvious differences. 
- Secondly, I cannot agree with the hypnosis in Figure 1, since the oracle set is larger than the estimate set and, there are a lot of variances for each estimate set, it is not surprising that the performance on the oracle set is more stable. 

A few other minor weaknesses include: 
- Even the best evaluation strategy identified is not entirely reliable, indicating that current evaluation benchmarks may be inadequate for individual task performance prediction.  
- Regarding few-shot learning, besides the standard few-shot evaluation benchmarks, more few-shot evaluations are flexible -- in a lot of papers they also show the performance under a few-shot setting with different synthetic or real-world benchmarks, even for open-vocabulary images/videos. They are also not limited to the standard query-support evaluation. How can the conclusion drawn from this paper inspire those types of work?

### Questions
A few minor questions: 
- (Section 3, AE)"We observe that in a true FSL setting, this is an unrealistic assumption." --> Why this is not a realistic setting? For few-shot in practice, we want to tune a model with a few samples and that model can handle a lot of samples, which means the query set is much larger. 
- (Section 3, TLE) "Moreover, in realistic situations there is no labeled query set for evaluating a model, so both the model fitting and model evaluation must be done with the support set." --> Again, query and support set split is some data processing. If we treat the support set as the whole labeled set, the held-out strategy is essentially the same as the query-support split, right?
- (Section 4.1) What are the evaluators? They should be clearly defined. Moreover, there are a lot of similar terminologies used in this paper, e.g. estimators, and oracle accuracy, which sound not general enough for an audience out of FSL.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the problem of validating the performance of few-shot learning (FSL) algorithms, on a given task (or episode), given only the small number of example in that task's train set (support set). This is a different endeavour than the aggregated performance usually reported to compare few-shot learning algorithms in general: it is usually estimated over many episodes, on much larger test sets (query sets) to reduce variance.

Experiments compare different estimator of the generalization accuracy that only depend on the support set (hold-out, 5-fold and leave-one-out cross-validation, bootstrapping), against the accuracy as measured on the larger query set. They observe a large difference, which show none of these methods are reliable enough to be used as estimates of the generalization performance on a given task. Moreover, there is not much correlation between _rankings_ of models (or hyper-parameter values) on validation and test. However, these validation methods are usually _underestimating_ the test accuracy, so they may be useful as a lower bound (as the train error is usually an upper bound).

### Strengths
Originality
--------------
The question of a validation procedure is often neglected in few-shot learning, and proponents of a new algorithm often only focus on the aggregate test performance. This is an issue when trying to apply these algorithms to new, specific small datasets, and trying to determine the best learner (and hyperparameters) for them.

Estimators of generalization errors considered are not new (this was much more popular in machine learning when all datasets were much smaller than today), but systematically investigating them in the context of FSL is new, as are the observations on leave-one-out in that context.

Quality
----------
The research questions are clear, and explore well different aspects of the main problem (task-level validation for FSL), which is well motivated.
The investigation is well done, experiments align with the research questions.
The span of experiments, across datasets, models, and estimators make sense, and the results support the conclusions.

Clarity
---------
The paper is quite clear and reads well. Often questions or remarks coming to my mind when reading a sentence were satisfactorily addressed in the next one or a paragraph later.
Visualization and presentation of results are mostly clear.

Significance
-----------------
Although some of the conclusions may read like negative results, which are usually harder to "sell" as significant, I think this investigation is reveals really important points for any application of FSL to real world small-scale datasets. The issues exposed would affect anyone needing to validate the performance of a few-shot learner without access to a large labeled query set.
Episode-level hyper-parameter selection is also a pretty open problem, and it's good to have it explored.

### Weaknesses
1. One thing that could be explored further is the reliance of some learners on the assumption of a balanced support set. MAML seems to be particularly sensitive, as shown in Fig. 3 for CV LOO. This makes me wonder if maybe the "Oracle" accuracy would only be valid or accurate for balanced, N-ways k-shot support sets, and CV LOO or bootstrapping estimators might actually be closer to the performance of these few-shot learners on unbalanced support sets.
2. If class balance is an assumption that can be made (based on the composition of a given task), then maybe estimators could be adapted to have splits respect that constraint. Cross-validation could have leave-one-shot out (the support set would be balanced, k-1 shot and the valid set would have one example of each class), sampling for bootstrapping could also be aware of classes. If it works, this might be a practical contribution.
3. The class balance assumption, used in all datasets considered (as far as I can tell), may be too restrictive when developing procedures for real-world datasets.

### Questions
1. Could you also report training accuracy, for the different estimators (incl. oracle)? Or is it almost always 100% and there's no signal there?
2. Is it the case that all the estimators actually underestimate the test accuracy (up to statistical noise)?
3. If we can assume that tasks of interest have balanced training sets, can class-aware splits provide a better estimation? (see point 2 in "Weaknesses" above?
4. If class balance cannot be assumed in general (as I'd think would be the case in real world applications), maybe it would be worth doing experiments on episodes with un-balanced support sets, either from other benchmarks, or altering the composition of episodes from usually-balanced ones.

Update after reply
------------------------
The author reply did not add much information, confirming observations and repeating points made in the paper, but did not provide additional insight, theoretical arguments, or observations. Therefore I'm maintaining my score.

### Soundness
3 good

### Presentation
3 good

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
The paper aims to investigate 3 main research questions about the effect of evaluation approach on 1) predicting task-level performance, 2) validity of the ranking of various FSL methods and 3) model selection and FSL performance. Among other things, they concluded that performance is substantially different than the performance estimated by the validation procedures used in the paper. Among them, 5-fold CV is better than the others. For model selection LOO-CV is the best approach.

### Strengths
The paper is about a topic that hasn’t gotten much attention in the past.

### Weaknesses
Different methods use different backbone networks. Backbone network has a confounding effect that makes comparison between methods difficult.
Oracle estimator is not properly described.
My main concern is about the significance of the results and their usefulness and impact in real-world. For example, I am not sure to what extent it can be justified to do LOO-CV for model selection and then 5-old CV for performance estimation. The paper does not provide sufficient justification for this choice of evaluation protocol, and it is unclear why one would not use the same evaluation approach for both model selection and performance estimation. Furthermore, the paper does not explore the impact of different splits of the data for the cross-validation procedures. The stability of the results across different data splits is not investigated, which could lead to unreliable conclusions.

### Questions
See above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
