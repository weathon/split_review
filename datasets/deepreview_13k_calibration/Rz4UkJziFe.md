# Medium-Difficulty Samples Constitute Smoothed Decision Boundary for Knowledge Distillation on Pruned Datasets

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 3, 8

## Abstract
This paper tackles a new problem of dataset pruning for Knowledge Distillation (KD), from a fresh perspective of Decision Boundary (DB) preservation and drifts. Existing dataset pruning methods generally assume that the post-pruning DB formed by the selected samples can be well-captured by future networks that use those samples for training. Therefore, they tend to preserve hard samples since hard samples are closer to the DB and better characterize the nuances in the distribution of the entire dataset. However, in KD, the limited learning capacity from the student network leads to imperfect preservation of the teacher's feature distribution, resulting in the drift of DB in the student space. Specifically, hard samples worsen such drifts as they are difficult for the student to learn, creating a situation where the student's DB can drift deeper into other classes and make incorrect classifications. Motivated by these findings, our method selects medium-difficulty samples for KD-based dataset pruning. We show that these samples constitute a smoothed version of the teacher's DB and are easier for the student to learn, obtaining a general feature distribution preservation for a class of samples and reasonable DB between different classes for the student. In addition, to reduce the distributional shift due to dataset pruning, we leverage the class-wise distributional information of the teacher's outputs to reshape the logits of the preserved samples. Experiments show that the proposed static pruning method can even perform better than the state-of-the-art dynamic pruning method which needs access to the entire dataset. In addition, our method halves the training times of KD and improves the student's accuracy by 0.4% on ImageNet with a 50% keep ratio. When the ratio further increases to 70%, our method achieves higher accuracy over the vanilla KD while reducing the training times by 30%.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This manuscript introduces a dataset pruning method to enhance the efficiency of knowledge distillation (KD) by retaining a strategically selected subset of samples and reshaping logits to better align with the teacher’s knowledge. 

The authors propose that selecting medium-difficulty samples strikes a good balance and helps in preserving samples that are neither too easy nor too difficult. This in turn helps to increase the efficiency and accuracy of models.

Further, they introduce a logit reshaping technique that uses global distribution information to counteract biases that dataset pruning might introduce.

The proposed method is evaluated on two benchmark datasets CIFAR-100 and ImageNet with multiple teacher-student architectures, demonstrating consistent improvements over existing pruning techniques.

### Strengths
1. The paper introduces a compelling approach to dataset pruning. This method looks interesting focusing on selecting medium-difficulty samples for distillation, which strikes a balance between easy and hard examples and leads to better generalization in the student model.

2. The proposed logit reshaping method effectively mitigates the distributional shift caused by pruning. This can be a key to enhancing distillation performance on pruned datasets.

3. The technique is thoroughly evaluated across multiple benchmark datasets (CIFAR-100, ImageNet) and different teacher-student architectures.

4. The proposed pruning method significantly reduces training time without sacrificing performance. This can give us with some really good solutions for real world use and even we can use this method for time consuming computationally large datasets.

5. The proposed method outperforms existing static pruning techniques (e.g., Herding, Forgetting, MoDS) and achieves comparable or superior performance to dynamic methods like InfoBatch.

### Weaknesses
1. The article does not provide a detailed analysis of how sensitive the method is to hyperparameter tuning. The authors should try out with different keep ratios or distillation losses. Specifically, the paper lacks a systematic exploration of how the performance varies with different pruning ratios, and it does not explore the impact of different distillation loss functions beyond the standard knowledge distillation loss. This makes it difficult to assess the robustness of the method under different configurations.

2. This article compares with static pruning techniques but a more in-depth comparison with other knowledge distillation methods, especially self-knowledge distillation, would strengthen its position and give us a more in-depth analysis. The comparison with existing knowledge distillation methods is limited, and it does not explore the potential benefits of combining the proposed pruning method with more advanced distillation techniques, such as feature-based distillation or attention-based distillation. A more comprehensive comparison would help to better position the proposed method within the broader landscape of knowledge distillation.

3. The approach is evaluated on CIFAR-100 and ImageNet, but it remains unclear how well it would scale with more complex models like ResNet family and Wide ResNets (WRN). While the paper demonstrates results on CIFAR-100 and ImageNet, the experiments do not include a thorough evaluation on more complex architectures, such as deeper ResNets or Wide ResNets. This raises concerns about the scalability and applicability of the method to more challenging real-world scenarios that often involve these more complex models.

### Questions
I have some queries regarding the article----

1. How does the proposed logit reshaping method handle potential conflicts between preserving class-specific distributions and mitigating the variance of logits in a highly imbalanced dataset? Could the method be further optimized for such cases? Can I get some explanations for this?

2. In the context of medium-difficulty sample selection, how does the method ensure that the pruned dataset retains enough diversity to avoid overfitting, especially when dealing with high-dimensional feature spaces in complex models?

3. Given that the pruned dataset relies on teacher feedback to rank sample difficulty, could this process introduce potential biases in class relationships, and how might this be addressed if the teacher's knowledge is imperfect or misaligned with the pruned subset?

4. Can the authors provide some tSNE figures for better understandings.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In the paper, the authors addresses the challenge of efficient knowledge distillation (KD) on pruned datasets. The authors propose a static pruning method that focuses on selecting medium-difficulty samples, as opposed to traditional methods that prefer hard or easy samples. The method aims to mitigate decision boundary drift caused by the student's limited capacity to mimic the teacher's feature distribution. Additionally, the paper introduces a logit reshaping technique to reduce distributional shift in the pruned dataset by leveraging the teacher's global logit information. Experimental results demonstrate that the proposed method outperforms existing dynamic and static pruning techniques across various benchmarks, achieving notable efficiency and performance gains.

### Strengths
1. **Clear Motivation**: The authors clearly articulate the problem of decision boundary drift and how hard or easy samples influence KD differently. This sets a strong foundation for their proposed solution.
2. **Methodical Innovation**: The selection of medium-difficulty samples for KD and the use of global logit reshaping are novel concepts. The visualizations of decision boundaries and empirical evidence support the validity of these innovations.
3. **Comprehensive Evaluation**: The paper presents results from multiple datasets (CIFAR-100, ImageNet) and various teacher-student configurations. Ablation studies and comparisons with other pruning methods provide a holistic understanding of the approach’s effectiveness.
4. **Efficiency Gains**: By achieving better student performance while significantly reducing training times, the proposed method demonstrates practical utility, especially for resource-constrained settings.

### Weaknesses
1. **Theoretical Justification of Medium-Difficulty Samples**: 
Despite the novelty of using medium-difficulty samples, the overall methodological advances feel incremental. The authors should need more rigorous theoretical analysis to make the proposed methodology convince to the reader of the underlying mechanisms driving performance improvements.

   - **Explicit Analysis**: The authors should provide a rigorous mathematical analysis that formalizes how medium-difficulty samples contribute to smoother decision boundaries. This could involve deriving relationships between sample difficulty, gradient stability, and boundary smoothness. For example, a formal analysis of the loss landscape and how different sample difficulties affect the convergence properties of the student network is needed. Specifically, the authors should investigate how the Hessian of the loss function changes with respect to different sample difficulties and how this impacts the generalization capabilities of the student model. 
   - **Statistical Modeling**: Conduct an empirical risk analysis or use statistical measures to model the impact of medium-difficulty samples on decision boundary drift. For example, the authors could analyze the variance of gradients during training for different difficulty levels and quantify how medium-difficulty samples stabilize learning. This could be done by computing the trace of the covariance matrix of the gradients for each difficulty level and showing that medium-difficulty samples lead to a lower trace, indicating more stable learning. Furthermore, the authors should also consider analyzing the Fisher information matrix to understand how different difficulty samples contribute to the information content of the model parameters.
   - **Geometric Insights**: The authors can use tools from computational geometry to offer insights into how medium-difficulty samples influence class separability. Visualizing the feature space evolution with respect to class overlap during training could also strengthen their argument. For instance, the authors could measure the distance between class centroids in the feature space and show how this distance changes during training with different difficulty samples. Additionally, the authors could analyze the curvature of the decision boundaries and demonstrate that medium-difficulty samples lead to smoother, less complex boundaries.

2. **Deeper Analysis of Logit Reshaping**:
   - **Impact Study on Logit Distribution**: Perform a sensitivity analysis on the logit reshaping process. Specifically, the authors can quantify how reshaping logits using the teacher’s global information affects the student’s performance across classes, especially in cases of class imbalance or noisy labels. This analysis should include metrics such as the Kullback-Leibler divergence between the teacher and student logit distributions for each class, and how this divergence changes with and without logit reshaping. Furthermore, the authors should investigate how the reshaping parameters (e.g., the standard deviation adjustment and mean logit alignment) affect the performance of the student model across different classes.
   - **Ablation of Reshaping Components**: Break down the logit reshaping mechanism and assess the impact of each component (e.g., the standard deviation adjustment and the mean logit alignment) to isolate what contributes most to performance gains. This should involve systematically removing each component and measuring the resulting performance drop. For example, the authors could train the student model with only the standard deviation adjustment, then with only the mean logit alignment, and then with both, to quantify the contribution of each component. This analysis should also consider the interaction between these components.
   - **Bias and Overfitting Analysis**: Evaluate whether the logit reshaping method introduces bias or overfitting. This could involve testing the method on datasets with varying distributions and comparing generalization performance on unseen data. Specifically, the authors should measure the performance of the student model on both the training and validation sets and analyze the gap between these two performances. A large gap would indicate overfitting, and the authors should investigate how the logit reshaping method contributes to this. Additionally, the authors should consider using techniques such as adversarial training to assess the robustness of the student model trained with logit reshaping.

3. **Quantitative Analysis of Decision Boundary Dynamics**:
   - **Boundary Drift Measurement**: The authors can introduce or provide a metric or framework for quantifying decision boundary drift in the student network. This could involve computing the alignment of decision boundaries between the teacher and student models using tools like mutual information or boundary discrepancy measures. The authors should also consider using other metrics such as the Hausdorff distance between the decision boundaries of the teacher and student models to quantify the discrepancy. Additionally, the authors should analyze how the boundary drift changes during training and how this change is affected by the proposed method.
   - **Difficulty Spectrum Analysis**: Assess how the performance changes as samples are divided across a spectrum of difficulties, rather than just hard, medium, or easy categories. This can help establish a more granular understanding of why medium-difficulty samples are optimal. The authors should consider using a continuous measure of sample difficulty, such as the cross-entropy loss of the teacher model on each sample, and then analyze the student performance as a function of this difficulty measure. This would provide a more detailed understanding of the relationship between sample difficulty and student performance.

4. **Generalizability and Scalability Experiments to Other KD frameworks on other modalities?**:
The method’s effectiveness on more diverse datasets or in non-vision tasks remains unexplored. The authors should test out the method on a range of datasets beyond vision (e.g., NLP or time-series data) to demonstrate the versatility of the approach. This would help clarify if the medium-difficulty sample selection has domain-specific benefits or if it generalizes well.

### Questions
1. **Logit Reshaping Justification**: How sensitive is the logit reshaping method to variations in the teacher’s predictions? Could this technique inadvertently introduce bias in scenarios with highly imbalanced classes?
2. **Generalizability Across Domains**: What challenges do the authors anticipate in adapting the propsoed method to other domains of say NLP and time-series?
3. **Efficiency vs. Performance Trade-off**: Can you elaborate on the practical trade-offs between training time and accuracy? Are there specific scenarios where maximizing efficiency might not justify the associated performance loss?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper aims to investigate experimentally how to select a balanced subset of a training set, based on a pretrained teacher, so as to reduce the training time needed to train students in the knowledge distillation (KD) framework while controlling the performance degradation of distilled students as much as possible, where the distilled students are trained on the balanced set. The proposed method consists of two phases. In phase 1, all samples in the original whole training set are sorted in the decreasing order of their corresponding cross entropy losses given by the pretrained teacher, those located in the middle range are selected, and the average of the standard deviation of a logit vector over all logit vectors within each class is computed and recorded. In phase 2 (corresponding to the training stage in KD), the logit vector of each selected sample from the pretrained teacher is first reshaped by the recorded average standard deviation of the class that the selected sample belongs to and  then passed to the KD objective function. To maintain balance, the sorting and sample selection can be carried out on a per class basis, as implied in the first paragraph of Section 4.3. Experiments were carried out on CIFAR 100 and ImageNet for several teacher-student pairs to verify the effectiveness and generalizability of the proposed method.

### Strengths
1. The paper is generally well written. 

2. The methodology is easy to follow and simple to implement.

### Weaknesses
1. The value proposition in terms of the accuracy vs time savings is kind of weak in this line of research. First, the intended time savings is for the KD training phase, not for the inference phase. Time savings for the inference phase is more important. Second, there is always accuracy degradation when the training dataset is pruned. When the ratio of kept sample is high, the training time savings is small. To have a meaningful training time savings, the ratio of kept sample has to be much smaller, which, however, results in significant, unacceptable accuracy performance degradation.

2. In comparison with Moderate Dataset Selection (MoDS) and reshaping techniques proposed in the literature, the novelty of the proposed method is kind of limited.

3. Experiments are insufficient to demonstrate the universality of the proposed method with respect to different students with variety of learning capability. The proposed method is mainly motivated by the learning gap between the pretrained teacher and students. What would happen if the learning capability of the student is close to, or very far away from that of the pretrained teacher? If the pruned training dataset works only for certain students, but not for others, the method won't fly since finding which student fits by experiments also takes significant amounts of training time.

4. Experiments are insufficient to demonstrate its competitiveness with another technique called data distillation.

### Questions
1. How are the shaping methods in the literature applied in the setup for Table 2? The comparison in Table 2 seems  like apple vs orange, and may be not fair.

2. More experiments are needed to show the value of the proposed method. 

3. The few shot cases considered in the paper ``BAYES CONDITIONAL DISTRIBUTION ESTIMATION FOR KNOWLEDGE DISTILLATION BASED ON CONDITIONAL MUTUAL INFORMATION'' by L. Ye (ICLR 2024) can also be used to reduce the KD training time. Please compare the performance of the proposed method with the few shot case in that paper in terms of accuracy vs training time to see if the proposed method in this paper is orthogonal.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper deals in data pruning for knowledge distillation. While previous observations show that random pruning is superior over other pruning methods, the authors proposed to retain medium difficulty samples for distillation. The motivation is that these samples are closer to the median distances between class centers.

### Strengths
- The explanation the authors suggest for the question of why a student model is sub-optimal when performing hard-sample based pruning methods is interesting and looks like it is the main novelty of the paper.  Also, The visualization in Figure 3 is clear and insightful.

- Experimental results are encouraging and look promising.

### Weaknesses
 - In Figure  2 the authors show “a large accuracy gap” between the teacher and the student. The figure which indeed shows “Large accuracy gap” does not clearly demonstrate the specific degradation of the student’s accuracy due to the dataset pruning used. An accuracy gap between teacher and student is what we typically see in knowledge distillation in general. What does it mean “large accuracy gap”? Maybe the authors better show accuracy plots for easy, medium and hard pruning. Currently, Figure 2 is out of context.   


- Equation (3), the M_DIF is computed to score hard samples. It is not quit clear why the M_DIF is defined here and what is the context? Is it another form of data pruning algorithm? (in figure 5, various data pruning are compared by the authors). Or it severs only the discussion in section 3.2? I would clarify the motivation.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
