# Improving the efficiency of conformal predictors via test-time augmentation

- Decision: Reject
- Scores: 6, 5, 6, 6, 3, 3

## Abstract
In conformal classification, the goal is to output a _set_ of predicted classes, accompanied by a probabilistic guarantee that the set includes the true class. Conformal approaches have gained widespread traction across domains because they can be composed with existing classifiers to generate predictions with probabilistically valid uncertainty estimates. In practice, however, the utility of conformal prediction is limited by its tendency to yield large prediction sets.  We study this phenomenon and provide insights into why large set sizes persist, even for conformal methods designed to produce small sets. Using these insights, we propose a method to reduce prediction set size while maintaining coverage. We use test-time augmentation to replace a classifier's predicted probabilities with probabilites aggregated over a set of augmentations. Our approach is flexible, computationally efficient, and effective. It can be combined with any conformal score, requires no model retraining, and reduces prediction set sizes by up to 30\%. We conduct an evaluation of the approach spanning three datasets, three models, two established conformal scoring methods, and multiple coverage values to show when and why test-time augmentation is a useful addition to the conformal pipeline.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper adresses the problem of producing large prediction sets commonly seen in current approaches of conformal prediction, by applying test-time augmentation to the computation of conformal scores. To compute the conformal score of a sample, the proposed method uses a linear combination of estimated probabilities given by the base classifier on the original data vector and its augmentations. The weights of this linear combination are either uniform or learned by minimizing the cross entropy loss on the calibration set, giving rise to two algorithmes correspondingly referred as TTA-Avg and TTA-Learned. 

An extensive empirical study was carried out to show the effectiveness of test-time augmentation in reducing the prediction set size. The superiority of TTA-Learned over TTA-Avg is notably observed for the expanded augmentation policy where some augmentations not used in the training step are introduced in the calibration step.

### Strengths
- This paper is well organized and easy to follow.

- Empirical evidence is provided to demonstrate the efficiency of the proposed method in reducing the size of the prediction set.

- A comprehensive empirical discussion is given to shed light on the behavior of the proposed method, and to explain intuitively its efficiency.

### Weaknesses
 - Some of the technical claims might need further explanation (see Questions).

- The efficiency of the proposed method depends heavily on the applicability of test augmentation.

- My biggest question about this work is on the assumption of data exchangeability in TTA-Learned. As the weights of augmentations in TTA-Learned are obtained by minimizing the cross entropy loss on the *calibration set*, there is a statistical dependence between the data in the calibration set and the learned weights of augmentations that are used to compute the conformal score. This means that calibration data and unseen exemples are not exchangeable with respect to the computation of conformal score. So I do not see how the assumption of exchangeability is preserved. If this point could be clarified, I would be willing to reconsider my score.  


- As pointed out by the authors, it is understandable that TTA-Learned works better than TTA-Avg for the expanded augmentation policy as it allows the adjustment of the weights associated to the augmentations not included in the training. Meanwhile the results using APS reported in Table~4 show a close match between TTA-Learned and TTA-Avg. Could the authors provide some intuition behind that?

### Questions
- My biggest question about this work is on the assumption of data exchangeability in TTA-Learned. As the weights of augmentations in TTA-Learned are obtained by minimizing the cross entropy loss on the *calibration set*, there is a statistical dependence between the data in the calibration set and the learned weights of augmentations that are used to compute the conformal score. This means that calibration data and unseen exemples are not exchangeable with respect to the computation of conformal score. So I do not see how the assumption of exchangeability is preserved. If this point could be clarified, I would be willing to reconsider my score.  


- As pointed out by the authors, it is understandable that TTA-Learned works better than TTA-Avg for the expanded augmentation policy as it allows the adjustment of the weights associated to the augmentations not included in the training. Meanwhile the results using APS reported in Table~4 show a close match between TTA-Learned and TTA-Avg. Could the authors provide some intuition behind that?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The proposed approach is conceptually simple and uses test time augumentation to improve the predictions of the underlying classifiers which in turn imporves the conformal scores which then results in smaller (more efficient) prediction sets. This has the benefit that the model does not need to be retrained thus maintaining the flexibility of CP and increasing applicability. The authors compare 4 variants based on learned vs. simple average of the augmentations, and simple vs. expanded policy. Since this approach is orthogonal to any improvements in the score function it can be applied on top of different scores (e.g. RAPS or APS). 

The authors also investigate some of the reasons behind the improvement and identify that e.g. one reason is due to the the improved top-$k$ accuracy. The evaluation w.r.t. datasets such as iNaturalist that contain an order of magnitude more classes than ImageNet is appreciated.

### Strengths
I think the simplicity of the approach is its biggest stregth. It is easy to implement, easy to understand, and it still seems to yield consistent improvements across different settings and datasets.

The experimental evaluation is reasonably detailed and the ablation analysis (e.g. simple vs. expanded, learned vs. average) is informative.

### Weaknesses
The biggest weakness of the approach is that the conformal guarantee is broken, or at least it has not been formally proved to hold for the learned setting.

The author state that "We learn these weights using the calibration set by learning a set of weights that maximizes classifier accuracy by minimizing the cross-entropy loss computed between the predicted probabilities and true labels". However, it is not clear whether this yields valid coverage. Since the resulting classifier $\hat{g}$ uses calibration data to learn the weights $\Theta$ the exchangeability between the calibration set and the test set is broken -- this is easy to see because information from the calibration set "leaks" into the weights $\Theta$. To see this differently: if you swap one calibration point with one test point the learned weights will be different. This is equivalent to why we cannot use one dataset to both train and calibrate the base classifier $f$ and why we need to either use Split CP, or use the full conformal approach. To maintain validity 3 datasets are necessary under the split framework: one for training, one for learning the augmentation policy, and one for the final calibration. However, this comes at a trade-off were we have to use smaller sets which is the same trade-off that standard split CP suffers from.

Note, the validity of the average variant is correct since here the exchangeability is maintained.

Note also that the fact that the emprical coverage matches the nominal coverage is not a proof.

The statement "We learn these weights using the calibration set by learning a set of weights that maximizes classifier accuracy by minimizing the cross-entropy loss computed between the predicted probabilities and true labels" shows the second weakness. The weights are trained to maximize the accuracy. However, this is not necessarily alligned with the actual goal of CP. It has been shown that we obtain the smallest prediction sets when the predicted probabilities (for all classes) match the ground-truth oracle probabilities (see e.g. [1] or APS).  However, the cross-entropy loss leads to over-confidence for the true class and does not encourage that the rest of the probabilities are well calibrated. Using a different loss such as e.g.  the one proposed by Stutz et al. (2022) which is mentioned in the related work or [1] is likely to lead to further improvements. Given the limited technical contributions such further experimental analysis is warranted.

Given that the learned weights were anyways close to 0 as reported, using fixed weights is another solution that maintains validity.

### Questions
1. Can you provide a rigorous proof that using the calibration set for learning the augmentation weights mantains validity, or fix the experiments using 3 seprate sets as outlined in the weaknesses section?

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the challenge in conformal classification where it often produces excessively large prediction sets. To tackle this, the authors introduce an approach leveraging test-time augmentation (TTA). This method replaces a classifier's predicted probabilities with those aggregated over various augmentations. Notably, this approach is flexible, doesn't require model retraining, and has shown to reduce prediction set sizes by up to 30%. The paper's robust experimental evaluation spans multiple datasets, models, and conformal scoring methods, underscoring the effectiveness and applicability of their TTA-based solution.

### Strengths
Strengths:

The paper proposes an interesting approach to the existing challenge in conformal classification of producing large prediction sets. The idea of utilizing test-time augmentation (TTA) to address this is both innovative and timely.

The approach is model-agnostic, which makes it potentially widely applicable.

The paper provides insights into the conformal classification's tendency to yield large prediction sets, which can deepen understanding in the area.

The evaluation spans multiple datasets, models, and conformal scoring methods, suggesting a thorough empirical investigation.

### Weaknesses
While the paper preserves the assumption of exchangeability, it would be helpful to discuss any potential impacts or corner cases where this might not hold true.

How does the addition of test-time augmentation impact the computational efficiency of predictions, especially in real-time applications?

The paper claims the approach is flexible. However, is there a range or type of augmentation that works best for certain kinds of datasets or problems?

### Questions
How did the authors decide on the specific augmentations for the test-time augmentation? A more detailed breakdown would help the reader understand the decision-making process.

Could the authors provide more real-world scenarios or case studies where their approach would be particularly beneficial?

It would be helpful if the authors could discuss any potential limitations of their method, and how they might be addressed in future iterations or research.

While the paper provides an evaluation of the proposed approach, a more direct comparison with other recent methods aiming to reduce prediction set sizes in conformal classification would be beneficial.

### Soundness
3 good

### Presentation
3 good

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
The paper describes a data-augmentation approach to improve the efficiency of CP prediction sets.  Instead of evaluating a single model prediction, the conformity measure depends on a set of predictions through a trainable aggregation function. The authors show empirically that training the aggregation function through a cross-entropy loss improves the efficiency of the resulting prediction intervals.

### Strengths
The idea is simple but looks powerful. The amount of empirical evidence provided is notable.

### Weaknesses
The authors should clarify why their idea is different from replacing the underlying model with an ensemble method. The difference would be clear if the aggregation weights were trained by optimizing the CP efficiency directly. But the learning strategy is "minimizing the cross entropy loss with respect to the true labels on the calibration set". The link between the cross-entropy loss and the size of the prediction sets is not explicit.

### Questions
- An ablation study is run to compare different underlying models. It would be interesting to see what happens if the underlying model is an ensemble method, e.g. a random forest algorithm.
- The aggregation function is trained by "minimizing the cross entropy loss with respect to the true labels on the calibration set". Does this preserve the marginal validity of the prediction sets?  
- Have you compared with any adaptive CP approaches like [1]?

[1]  Romano, Yaniv, Matteo Sesia, and Emmanuel Candes. "Classification with valid and adaptive coverage." Advances in Neural Information Processing Systems 33 (2020): 3581-3591.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces test-time augmentation (TTA) to significantly improve the efficiency of conformal predictors. In particular, by simply adapting TTA and learning a weight over augmentations, the produced augmentation-aggregated classifier provides a good scoring function that contributes to an efficient conformal predictor. The claim is empirically supported on the evaluation over three datasets and one baseline with various architectures.

### Strengths
This paper proposes a simple yet effective way to improve the efficiency of conformal predictors. In particular, this paper introduces TTA into the conformal prediction community.

### Weaknesses
I have a major concern on this paper. To my understanding, it is well-known that a better classifier (as a scoring function) provides smaller prediction sets in size (e.g., Table 1 of Angelopoulos et al., 2022 — I only chose papers with deep learning experiments); without these examples, it is clear that if we have a perfect classifier, the expected prediction set size is the smallest value (which is one).

Also, TTA with learnable parameters is at least firstly introduced in Shanmugam et al., 2021, which can be seen as making a better classifier from a base classifier by augmentations with learned weights over augmentations.

Given these, this paper revisited that a better classifier provides a more efficient prediction set, which is not new to me.


As an additional concern, this paper uses a calibration twice for learning weight parameters for augmentation in (5) and choosing a threshold for conformal prediction. This “double-dipping” should be avoided. I believe the results would not change too much but please use a calibration only once for choosing the threshold for conformal prediction.

### Questions
The following includes questions, which summarizes Weaknesses.

* It is not easy to accept the paper’s claim that this paper found a novel way to improve the efficiency of conformal prediction via TTA – it is well-known that a better classifier provides efficient conformal predictors. Also, a provided way of using TTA is not new. Please highlight novel points of this paper. 
* For experiments, please conduct experiments by using a calibration set only once.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a test-time augmentation methods to construct a stronger base model, which benefits conformal prediction in achieving better efficiency.

### Strengths
1) Efficiency of CP is an important problem.

2) Evaluation results look good.

### Weaknesses
(1) Lack of novelty: the paper mainly propose

(2) Lack of explanation: the idea is pretty simple but quite effective by looking at results, but the paper does not fully explain why this kind of method works so well. Simple test time augmentation does not bring so much improvement to me. I suggest providing top-k accuracy and adding more explanations on why it benefits conformal prediction so much accordingly.

(3) Lack of evaluation: I suggest adding comparisons to baselines of ensemble conformal prediction, mentioned in the related work. They also attempt to construct a stronger base model. It is essential to provide comparisons to them.

(4) Presentation: a) typo: $k_{reg}$ in the related work part; b) in section 3, indexing from 0 to N should induce N+1 samples; c) a large part in Section 4 is preliminary of conformal prediction, which should be introduced in Section 3 or a separate preliminary part.

### Questions
1) Can we analytically write out the optimal aggregation weights based on the empirical utility of each augmentation? (quite feasible to me) For example, augmentation with higher accuracy should have a larger aggregation weight. If that is the case, there is no need for optimization of those weights.

2) Why don't you parameterize the augmentations and also optimize the weights of augmentations?

3) Do you think about directly optimizing the efficiency objective (i.e., set size) as conformal training papers?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
