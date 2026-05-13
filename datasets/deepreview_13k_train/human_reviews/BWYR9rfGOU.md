# SATE: A Two-Stage Approach for Performance Prediction in Subpopulation Shift Scenarios

- Decision: Reject
- Scores: 5, 6, 3, 3

## Abstract
Subpopulation shift refers to the difference in the distribution of subgroups between training and test datasets. When an underrepresented group becomes predominant during testing, it can lead to significant performance degradation, making performance prediction prior to deployment particularly important. Existing performance prediction methods often fail to address this type of shift effectively due to their usage of unreliable model confidence and mis-specified distributional distances. In this paper, we propose a novel performance prediction method specifically designed to tackle subpopulation shifts, called Subpopulation-Aware Two-stage Estimator (SATE). Our approach first estimates the subgroup proportions in the test set by linearly expressing the test embedding with training subgroup embeddings. Then, it predicts the accuracy for each subgroup using the accuracy on augmented training set, aggregating them into an overall performance estimate. We provide theoretical proof of our method's unbiasedness and consistency, and demonstrate that it outperforms numerous baselines across various datasets, including vision, medical, and language tasks, offering a reliable tool for performance prediction in scenarios involving subpopulation shifts.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors tackle the problem of estimating model performance under subpopulation shift. They propose SATE, which estimates test-set group proportions by representing the mean test-set embedding as a convex combination of mean training subgroup embeddings. The test-set accuracy is then a convex combination of the per-group model accuracies. The authors evaluate their method on typical subpopulation shift datasets, finding that they outperform the baselines.

### Strengths
- The method is intuitive and easy to understand.
- The authors evaluate their method on the common subpopulation shift benchmarks.

### Weaknesses
1. My main concern is regarding the significance of the method. To me, the problem of estimating model performance under subpopulation shift is largely trivial, as it is just a matter of estimating group proportions on the test set. If group labels are provided in the training domain as the authors assume, it is even simpler, and also a much more restrictive problem setup, which limits the applicability of the method. Given that the method is only theoretically bounded when subpopulation shift is the only shift that occurs (Assumption 1), and does not take e.g. the variation of sample difficulty within each subpopulation into account, I am not convinced that this method is useful.

2. It is not surprising that the proposed method outperforms other performance prediction methods (Figure 4), as these baselines are not specific to subpopulation shift, and do not even utilize the training set attributes. There are several other intuitive baselines that the authors could consider, e.g. learning per-group clusters on the training set, learning a debiased group predictor on the training set, or directly learning a model to predict the errors of the original model.

3. The authors should also show the predicted group proportions versus the actual proportions in the appendices.

4. To improve the significance of the work, the authors should consider evaluating their method on domain generalization benchmarks such as DomainBed [1] or WILDS [2].

### Questions
1. When computing the test-set group proportion $w$ in Algorithm 1 Step 10, how is it enforced that $w$ should sum to 1?

2. In the result showing augmentations on the y=x line (Figure 2), has the model been trained with the same data augmentations? It seems like this would be an important factor.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces SATE (Subpopulation-Aware Two-stage Estimator), a novel method for predicting model performance under subpopulation shift scenarios, where the distribution of subgroups differs between training and test datasets. SATE's two-stage approach first estimates subgroup proportions in the test set by expressing test embeddings as a linear combination of training subgroup embeddings, then predicts accuracy for each subgroup using augmented training data to produce an overall performance estimate. Experiments show improvement when compared SATE with baselines such as ATC-MC and DoC.

### Strengths
1. Novel contribution: First performance prediction method specifically designed for subpopulation shift scenarios and first to address unsupervised performance prediction in NLP tasks.

2. Theoretical foundations: Authors provide proofs of unbiasedness and consistency under certain conditions.

3. Empirical evaluation:  Experiments across multiple domains (vision, medical, NLP) and demonstrates superior performance compared to baselines.

### Weaknesses
1. Knowledge of group annotations: the method requires attribute annotations for the training data, which may not always be available or could be costly to obtain.

2. Scalability: The method may struggle with scalability when dealing with a large number of subgroups.

3. Linear decomposition: the method relies on linear decomposition assumption for test set embeddings, which might not always hold. Specifically, the assumption that test embeddings can be expressed as a linear combination of training subgroup embeddings may be violated in cases where the test distribution exhibits non-linear shifts relative to the training data. This is a strong assumption that limits the applicability of the method to scenarios where the shift is primarily due to changes in subgroup proportions, and not more complex distributional changes.

4. Discussions of limitations: there is no clear discussion of failure modes or performance under noisy/incomplete attribute annotations. Furthermore, the method's reliance on the column full rank assumption of the embedding matrix is not thoroughly examined. The impact of near-collinearity among subgroup embeddings on the accuracy of subgroup proportion estimation is also not discussed.

### Questions
1. How sensitive is the method to violations of the linear decomposition assumption for test set embeddings?

2. What are the specific conditions required for the theoretical guarantees to hold?

3. What is the memory requirement for storing subgroup embeddings?

4. How robust is the linear equation-solving step when subgroup embeddings are nearly collinear? What happens when some subgroups have very few training samples?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes SATE, a method for predicting test performance under subpopulation shift scenarios. The approach assumes access to test data but not to test set labels. SATE follows a two-stage process: in the first step, it calculates subgroup ratios by linearly expressing the average embedding of test data using the average embeddings of each subgroup in a subgroup-labeled training set. In the second step, it estimates subgroup performance using a subgroup-labeled augmented set (or validation set). The final predicted test accuracy is obtained by calculating a weighted sum of subgroup performance from step 2, using the subgroup ratios from step 1. The effectiveness of SATE is demonstrated on both image and language tasks.

### Strengths
The paper is clearly written and presents experiments across diverse benchmarks.

### Weaknesses
[W1] The rationale for predicting average accuracy based on the test distribution rather than evaluating using worst group accuracy is not clear. Is there a realistic scenario that motivates this? From a group robustness perspective, an ideal model should perform well across all subgroups. For this reason, group robustness studies typically evaluate models using worst-group accuracy or the average performance across subgroups (unbiased accuracy). However, this paper appears to prioritize sample average accuracy, aligned with the test environment distribution, rather than worst-group or unbiased accuracy. The reasoning behind this choice is not well-justified.

[W2] Along with W1, using the labeled set $S'_i$ to measure subgroup performance seems more like conducting a test evaluation than performance prediction. Does assuming access $S'_i$- a labeled set considered unseen from the model’s perspective- appear to be an overly strong assumption?

[W3] For the experiments in Table 1, is the training dataset also composed of corrupted data?

[W4] This method seems to handle only seen subgroups. How does it address unseen subgroups? If the goal is performance prediction, it should ideally be able to handle unseen subgroups as well.

[W5] Obtaining subgroup labels is often costly, and thus many studies have long focused on learning methods that do not require subgroup labels. Requiring a labeled training set for performance prediction appears to set up an unrealistic scenario. This is especially relevant given that even the DFR method used in this paper does not require training set labels during learning.

[W6] How would the approach perform if evaluated using a retrieval-based method? A straightforward solution, for example, could be KNN with $S'_i$.

[W7] Some terms appear in formulas without clear definitions (e.g., $P_{T-emb}$, $P_{g-emb}$, $H_S$)

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses how to predict the performance of an unlabeled test set in the presence of subpopulation shifts between the training and test sets. The authors propose a two-stage method. First, they estimate the proportions of different subpopulations in the test set by leveraging the average feature representation of all test samples and comparing it with the prototype features of each subpopulation in the training set. Next, they evaluate the performance of each subpopulation individually using a data-augmented version of the training set. Finally, the predicted overall test set performance is obtained by computing the weighted average of the subpopulation performances. The authors validate this approach with experiments on image and NLP datasets.

### Strengths
1. The study of performance prediction methods robust to distribution shifts is practical and meaningful. 
2. The method proposed by the paper is straightforward and reasonable.
3. The authors provide the source code, which is highly commendable.

### Weaknesses
1. The writing of the paper should be improved, as the flow of logic is unclear in several parts. For example, the logic between the first four paragraphs of the introduction is confusing, and the same lack of clarity is present in the four paragraphs of section 4.1.
2. If I understand correctly, the terms subpopulation, subgroup, group, and subset in the paper are used interchangeably to convey the same meaning. This inconsistent terminology further increases confusion for the readers.
3. The theoretical part of the paper is trivial, lacking valuable insights in both the proof process and the results presented. I suggest that this part should not occupy such a significant portion of the manuscript and could potentially be removed from the main text altogether.
4. I have some concerns about the effectiveness of using a data-augmented training set. Modern image classification models typically employ a wide range of data augmentation techniques to enhance model performance. Therefore, the model should also perform well on augmented training images, especially given the simple geometric transformations like Crop, Flip, and RandomRotation used in the paper. I briefly reviewed the source code provided by the authors, and if I understand correctly, these augmentation techniques do not seem to be incorporated into the training process. This implies an assumption that appears to be rather unrealistic.
5. The baseline methods mentioned in Section 2, such as Distribution Discrepancy-based and Model Agreement-based approaches, do not appear to be compared in the experiments.
6. The authors emphasize spurious correlation in the motivation section, which raises a question for me: is the method aimed at addressing all types of subpopulation shifts, or is it specifically targeting spurious correlations? Based on my understanding, the former is correct. Therefore, what is the purpose of highlighting spurious correlation in this context?

### Questions
My questions that need clarification are included in the weaknesses section.

### Soundness
3

### Presentation
1

### Contribution
2
