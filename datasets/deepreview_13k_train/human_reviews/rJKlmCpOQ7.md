# Removing Multiple Shortcuts through the Lens of Multi-task Learning

- Decision: Reject
- Scores: 3, 5, 6, 6, 6

## Abstract
We consider the problem of training an unbiased and accurate model using a biased dataset with multiple biases. This problem is challenging since the multiple biases cause multiple undesirable shortcuts during training, and even worse, mitigating one of them may exacerbate another. To address this challenge, we introduce a novel method connecting the problem to multi-task learning (MTL). Our method divides training data into several groups according to their effects on the model bias and defines each task of MTL as solving the target problem for each group. It in turn trains a single model for all the tasks with a weighted sum of task-wise losses as the training objective, while optimizing the weights as well as the model parameters. At the heart of our method lies the weight adjustment algorithm, which is rooted in a theory of multi-objective optimization and guarantees a Pareto-stationary solution. In addition, we also present a new real-image dataset with multiple biases, dubbed MultiCelebA, for evaluating debiased training methods under realistic and challenging scenarios. Our method achieved the state of the art on three datasets with multiple biases including MultiCelebA, and demonstrated superior performance on conventional single-bias datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work addresses the problem of avoiding that models use _several_ biases (or spurious correlations) from the data to perform predictions, whereas previous work has focused in avoiding a _single_ bias. To this end, the authors relate the problem of debiasing a model with multitask learning (MTL) and proposed to group the dataset into different groups/tasks based on their proposed grouping criteria. Then, they propose to train the MTL model by introducing learnable convex task weights that are regularized to reduce the norm of the loss gradient. Finally, the authors introduce a dataset based on CelebA that contains multiple biases, and use it to compare their proposed approach with a number of previous methods. Moreover, the authors also compare their method in different single-bias experiments and ablate the different components of the proposed solution.

### Strengths
- The problem of addressing several biases in the dataset (rather than a single one) is interesting, and a sensible middle-ground between single-bias settings and settings with no annotations.
- The proposed approach to divide the dataset into groups is also pretty interesting and novel, to the best of my knowledge.
- The paper is well-written and easy to follow.
- The empirical results are quite positive, and they also shed light on the behaviour of existing methods when multiple biases are present in the data.

### Weaknesses
 - W1. While MultiCelebA is interesting and useful, selling it as a "new dataset" is too much of a stretch for my taste.
- W2. Saying that this is the first work connecting "unbiasing" with MOO or MTL (which is quite freely interpreted) is arguable at best. First, one could argue that even importance-weighting approaches are already interpreting the problem as MOO, but there are even works such as FairGrad [4] that connect biases (this one, in the context of fairness, which does not necessarily imply data-imbalance) which adaptively scale gradients.
- W3. Statements about MOO and Pareto Optimality in the manuscript makes me worry about whether the authors have fully understood these concepts. For example:
  - I don't understand what it means to "address spurious correlations based on a theory of MOO".
  - "Finding _the_ Pareto-optimal parameter". There are _many_ Pareto-optimal parameters.
  - The goal is that "performance should not be biased towards a certain group". Pareto-optimality does not guarantee this. Indeed, MGDA is known to be biased towards tasks with low magnitudes. The concept the authors refer to is known as "task impartiality" in MTL (see, e.g., [1, 2]).
  - Saying that MoCo is the SotA of MOO is quite a stretch to say the least.
- W4. The arguments towards "finding a flat optima" are rather hand-wavy and unconvincing.
- W5. Related with W3, it is quite unclear to me what makes the proposed method work at all:
  - MGDA minimizes in each iteration the regularizer in Eq. 3, and it is biased towards dominated tasks (which is observed in Table 5). However, the proposed approach (which is an interpolation between ERM and MGDA, similar to CAGrad [3]) works well. Is it the interpolation? Or learning $\alpha$ using along the parameters?
  - It is rather intriguing that the grouping policy does not work well on its own. In principle, I don't see why the grouping and the training approach should not be independent.
- W6. Experiments lack statistics like standard deviations, making the effectiveness of some design choices (e.g. the update frequency $U$) quite unclear.
- W7. The results in UrbanCars are quite different from those that can be found in other works. Just as an example, the worst variant of ERM recorded in [Papers with code](https://paperswithcode.com/sota/out-of-distribution-generalization-on) has a gap of -15.4, while the one reported in the paper is of -69.2 (worse than any result of the PwC table).

### Questions
-Q1. When using MGDA in Table 5, does it mean that $\alpha$ is tuned as in Eq. 3 but only with the regularization? Or is $\alpha$ fully solved in each iteration?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors address the challenge of mitigating multiple spurious correlations. They introduce a novel dataset splitting method and construct a multi-task learning problem based on the split dataset. Their proposed algorithm identifies a Pareto-stationary parameter within this multi-task learning setup, which then becomes the model's resultant parameter. Additionally, they created the MultiCelebA dataset to benchmark the issue of multiple spurious correlations. Experimental results show that their method surpasses existing approaches in mitigating spurious correlations across three multi-bias and three single-bias datasets.

### Strengths
1. The paper is articulate and well-structured, making it accessible to readers.

2. The authors provide comprehensive experimental comparisons between their approach and existing methods. These results convincingly establish that the proposed method is superior in specific aspects, underscoring its advantages.

### Weaknesses
1. The rationale behind the algorithm design remains ambiguous. Although the authors mention that a Pareto-stationary point with a flat loss landscape helps resolve between-group conflicts, the underlying logic is not evident. Rigorous definitions of spurious correlations and the conditions under which they are fully eliminated would benefit readers. Specifically, the paper lacks a formal definition of what constitutes a 'spurious correlation' in the context of their multi-task learning framework. It's unclear how the proposed method guarantees the model will learn features that are truly invariant to the identified spurious attributes, rather than simply finding a different, potentially equally spurious, correlation. The connection between the Pareto-stationary point and the elimination of these correlations needs more rigorous justification.

2. The MultiCelebA dataset appears inadequate in distinguishing between spurious and non-spurious correlations. The authors have not elaborated on the dataset's construction, even in supplementary materials. Furthermore, while they label certain correlations between target attributes and specific attributes as spurious, the these correlations seem to compose of the spurious and non-spurious ones.  An isolated evaluation of spurious correlations is essential for gauging the efficacy of methods designed to counteract them. Thus, relying on experiments with the MultiCelebA dataset might be questionable. The paper does not provide a clear methodology for how they disentangle spurious correlations from genuine ones within the dataset. Simply observing correlations is insufficient; a more rigorous approach to identifying and isolating spurious relationships is needed to validate the dataset's utility for this task. It is not clear if the 'spurious' correlations are truly independent from the target variable in a causal sense.

3. Tables 2-4 present diverse evaluation metrics, raising concerns about potential cherry-picking to favor the proposed method. Without including metrics both UNBIASED and WORST consistently, the experiments might come off as biased and not entirely objective. The lack of consistent reporting across all tables makes it difficult to ascertain the method's robustness. It is essential to include both UNBIASED and WORST metrics for all experiments to provide a complete picture of the method's performance across different bias scenarios. The current presentation leaves room for doubt about whether the method truly achieves a balance between overall accuracy and worst-case performance.

4. The credibility of evaluating spurious correlations using the MultiCelebA dataset is questionable, as mentioned above. While results derived from Multi-Color MNIST might be more reliable, the proposed method's minimum group-wise accuracy is lower than that of GroupDRO. This undermines the claim that the proposed method is superior to GroupDRO. The fact that GroupDRO, a method specifically designed for worst-group performance, outperforms the proposed method on this metric raises concerns about the practical utility of the proposed method. The paper needs to clarify under which specific conditions the proposed method is expected to outperform GroupDRO and other related methods, and if the proposed method is only superior in average metrics.

### Questions
1. What underpins the expectation that the proposed method will effectively address multiple spurious correlations?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper points out the challenge of training an unbiased and accurate machine learning model using a biased dataset containing multiple biases, which lead to undesirable shortcuts during training. Connecting this problem to a multi-task learning problem, this work proposes a novel debiased training algorithm. In particular, the method optimizes both the weights and model parameters by training a single model for all tasks with a weighted sum of task-specific losses. Also, they built a new real-image multi-bias dataset (MultiCelebA) for this problem. that divide the training data into several groups based on the effects of biases on the model and define each task in MTL as solving the target problem for each group.

### Strengths
- This paper associates multiple biases issue in a biased dataset with a multi-task learning problem.
- The proposed new multi-bias dataset for debiased training is crucial for this area.
- Extensive experiments demonstrate the superiority of the proposed method.
- The paper is well-written and easy to understand.

### Weaknesses
 - The relationship between multiple biases issue and multi-task learning is intriguing. However, the absence of comparisons with traditional multi-task learning (MTL) methods raises a question. If traditional MTL methods can also effectively optimize the problem, it would strengthen the connection between multiple biases issue and multi-task learning. Specifically, while the paper frames the problem as a multi-task learning scenario, it does not explore how existing multi-objective optimization (MOO) techniques perform when applied to the defined tasks. The paper should include a comparison with standard MOO baselines to demonstrate the advantage of the proposed method.


### Questions
- GradNorm [1] also adopts the gradient of loss weight to optimize the loss weight. Could you please discuss the relation and the difference between your algorithm and GradNorm? In addition, GradNorm is an important reference for this paper.
- Could you please conduct additional comparisons with traditional MTL methods to solidify the connection between multiple biases issue and multi-task learning?

[1] Chen et al. GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks. In ICML 2018.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper effectively highlights the challenge of training models on biased datasets and the potential pitfalls of spurious correlations. The proposed method based on multi-task learning (MTL) is an innovative approach to addressing the problem of multiple biases in training data. This introduces a new perspective on debiased training. The introduction of a new real-image dataset, MultiCelebA, is a valuable contribution. It allows for evaluation under more realistic and challenging scenarios compared to existing synthetic-image datasets.

### Strengths
1. Application of multitask learning in the context of multiple shortcuts is a novel idea.
2.  MultiCelebA dataset can be instrumental for future research on evaluating shortcut learning algorithms.

### Weaknesses
Limitation:
1. No related works on shortcuts. Relevant literature can be found in
Discover and Cure: Concept-aware Mitigation of Spurious Correlation Wu et al. ICML 2023.

2. The paper is not easy to follow. The writing could have been better.

3. No code, so limited reproducibility.

4. The major issue with the approach is knowing so many different subgroups a priori. In a more challenging setting, it is almost impossible to know all possible different subgroups beforehand to design the training strategy. I would like see an experiment where out of 3 subgroups the authors include two in their training, leaving one unidentified and how their method performs.

5. There is a recent notion of difficulty in shortcuts. For example, some shortcuts are easy to learn, and some are difficult to learn. If the authors are using different subgroups to design multitask losses, the losses should be weighted corresponding to the shorcut difficulty. For example, a hard shortcut loss will be penalized less than an easy shortcut loss, as the mode is more prone to latching on the easy shotcut. The paper on shortcut difficulty is as follows:
Beyond Distribution Shift: Spurious Features Through the Lens of Training Dynamics. Murali et al. TMLR 2023.

This setting will be more realistic.

6. The dataset MultiCelebA is good for evaluation, but I would like to see a more realistic dataset like NIH-chesttube in the shortcut paper in #5.

7. Also, with multiple groups involved in the multitask loss, the overall performance may drop.

8. This is related to #4. All the possible groups may not be a shortcut. In this regard, can the shortcut discovery be aligned with the notion of slice discovery (ex DOMINO) to detect if really a spurious correlation going on before applying their method? This is a nice-to-have comment. I request the authors to think about this as a future work.

### Questions
See the weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the problem of training an accurate unbiased model using a dataset with multiple biases. Conventional training methods (e.g. ERM) lead to undesirable shortcuts in the model due to the spurious correlations in the dataset. To counter this, debiased training algorithms have been proposed but most of them focus on a single bias at a time. Hence, this work focuses on the problem of multiple biases in a dataset, which is more practical. They first divide the dataset into multiple groups such that each group exerts the same bias on model training, using labeled bias attributes. They formulate the problem in terms of multi-task learning (MTL) where the model has to learn to handle each group correctly. Towards this, they derive a multi-objective optimization algorithm to dynamically update task weights so that model parameters can converge to a Pareto-stationary point. For experiments, they re-purpose the CelebA dataset (called MultiCelebA) using multiple attributes that are spuriously correlated with the target class. On MultiCelebA and other benchmarks, they achieve state-of-the-art performance for both multiple bias and single bias settings.

### Strengths
* The interpretation of debiased training as an MTL problem seems interesting and novel.

* The proposed method is simple, intuitive, and effective.

* The paper is fairly well-written and easy to follow.

### Weaknesses
 * Debiased training as MTL
    * Debiased training actually seems closer to multi-domain learning (MDL) [W1] rather than MTL. Because MTL clearly means learning different tasks (i.e. task labels are different) as the paper also mentions on Page 2. 
    * On the other hand, MDL involves the same target classes but data coming from different domains, and the goal is to achieve good performance on all domains simultaneously. The core issue in debiased learning, as presented, is that the model learns spurious correlations that are specific to certain groups within the data, which aligns more closely with the domain shift problem in MDL. For example, if a model learns to associate 'blond hair' with 'female' in a biased dataset, this is analogous to a domain-specific shortcut rather than a distinct task. Also it seems like debiased training has a lot in common with long-tailed learning [W2]. For example, upweighting and upsampling baselines are also employed in long-tailed learning, where the goal is to improve performance on underrepresented classes. The connection here is that bias groups can be seen as underrepresented or overrepresented depending on the spurious correlation. 
    * Overall, I wonder why MTL is chosen over these other two. Also, it might be interesting to see how more advanced techniques from MDL or long-tailed learning perform when adapted to debiased training. For example, domain adversarial training or re-weighting strategies based on class or group frequencies could be explored.
    * Note: the above two references are just examples, there are many more papers in both sub-topics.

* Regarding dataset contribution
    * It is unclear how MultiCelebA is a new dataset compared to CelebA. There are no new images or new labels. Even the choice of attributes is based on the analysis from a prior work. The authors are essentially creating a specific experimental setup by grouping existing data based on pre-defined attributes. This is more akin to a data processing step rather than a new dataset contribution. 
    * The contribution of a new dataset seems misleading, only a new experimental setting based on an existing dataset is proposed.

* Design choices
    * The design choices for the main algorithm are not well explained. Please see questions for more details.

* Practicality and significance of dataset
    * Simple methods like upsampling and upweighting give very good improvements over the ERM baseline and are quite close to even the proposed method (Table 1). This raises a question on whether the proposed MultiCelebA is practical or challenging enough to provide new insights into evaluating debiased training methods. The fact that these simple baselines perform so well suggests that the dataset might not be complex enough to truly differentiate between various debiasing methods. 
    * See questions for more details.

### Questions
* Please also see the weaknesses section.

* Regarding practicality and significance of datasets and debiased training
    * Ideally, one would expect new datasets or benchmarks to improve over existing datasets by providing more challenging scenarios (or at least more data). While the overall accuracy numbers of MultiCelebA seem lower than UrbanCars (but similar to Multi-Color MNIST), upsampling and upweighting are consistently good on all three datasets. 
    * So MultiCelebA seems similar in terms of difficulty compared to existing datasets (i.e. there seems to be no advantage to having real images over synthetic images in the other datasets).
    * Another question is whether complicated debiased training methods (like the proposed method) themselves provide any significant improvements to be deemed of practical significance. This is because we observe a similar trend where upsampling and upweighting perform very well compared to all the supervised debiased learning methods.

* Regarding design choices (Algorithm 1)
    1. Why is $\theta$ updated again (outside the "for loop") after updating it for $U$ number of times?
    2. Why do $\bar{\alpha}$ and $\lambda$ need to be updated once every $U$ iterations and not every iteration?
    3. Also, why not have $\bar{\alpha}$ and $\lambda$ updates be at different frequencies like every $U_1$ and every $U_2$ iterations instead of together after $U$ iterations?
    * These design choices need to be explained and justified since this is the core idea being proposed.

* Minor comments
    * Page 3 (5th line of “Fairness with MTL” paragraph): use \cite instead of \citet
    * Sec. 3.1 (first paragraph): mention dimensions of $\theta$, should be $\mathbb{R}^n$ as per usage in Definition 2.
    * Fig. 3: x-axis title has typos: “interation” → “iteration”.
    * Page 10: Citation for Fernando et al. (MoCo) is incorrect, it should be ICLR 2023 and not ICLR 2022.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
