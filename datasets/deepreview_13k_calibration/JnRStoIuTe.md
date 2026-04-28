# Repeated Random Sampling for Minimizing the Time-to-Accuracy of Learning

- Decision: Accept
- Avg Score: 5.20
- Scores: 6, 8, 3, 3, 6

## Abstract
Methods for carefully selecting or generating a small set of training data to learn from, i.e., data pruning, coreset selection, and data distillation, have been shown to be effective in reducing the ever-increasing cost of training neural networks. Behind this success are rigorously designed strategies for identifying informative training examples out of large datasets. However, these strategies come with additional computational costs associated with subset selection or data distillation before training begins, and furthermore, many are shown to even under-perform random sampling in high data compression regimes. As such, many data pruning, coreset selection, or distillation methods may not reduce `time-to-accuracy', which has become a critical efficiency measure of training deep neural networks over large datasets. In this work, we revisit a powerful yet overlooked random sampling strategy to address these challenges and introduce an approach called \emph{Repeated Sampling of Random Subsets} (RSRS or RS2), where we randomly sample the subset of training data for each epoch of model training. We test RS2 against thirty state-of-the-art data pruning and data distillation methods across four datasets including ImageNet. Our results demonstrate that RS2 significantly reduces time-to-accuracy compared to existing techniques. For example, when training on ImageNet in the high-compression regime (using less than 10\% of the dataset each epoch), RS2 yields accuracy improvements up to 29\% compared to competing pruning methods while offering a runtime reduction of 7$\times$. Beyond the above meta-study, we provide a convergence analysis for RS2 and discuss its generalization capability. The primary goal of our work is to establish RS2 as a competitive baseline for future data selection or distillation techniques aimed at efficient training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work empirically investigated a strong baseline called Repeated Sampling of Random Subsets (RSRS, or RS2), in the context of dataset pruning/distillation. The authors found that this sampling scheme, which has been overlooked by the literature, served as a very strong baseline in terms of many metrics, such as end model accuracy and *time-to-accuracy*.

The authors did intensive experiments that compare RS2 with up to 24 existing dataset pruning/distillation methods and observed the superiority of RS2 under all of the above metrics. The authors called for attention from the community on this strong but overlooked baseline.

### Strengths
+ The highlight of an overlooked baseline in the context of dataset pruning/distillation.
+ Intensive experiments over so many baselines. This provides a very good benchmark and starting point for the following works, which I find really appreciable.

### Weaknesses
 - The RS2 without replacement is exactly the same as reducing the number of training epochs but with tuned learning rate scheduling. The new term is not helping to make the concept clear but more confusing. This also means that the theoretical analysis in Section 4 did not make actual contributions over previous work.

- In my opinion, a type of dataset pruning methods, which generate static subsets before real training starts, are up to a slightly different point from RS2. While we all know that the more data used for training the better, these methods try to find a coreset that is essential for good generalization. Therefore, it is important that the pruned data are not seen during the training process later (thus static subset). This reduces the storage cost which is not possible with RS2 because RS2 still requires access to the full training set.

- RS2 with replacement has been adopted in a few more works in the context of efficient training like [Ref-1, Ref-2].

### Questions
N/A

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a novel approach to improve time-to-accuracy of deep learning model training by using a fraction of the full dataset in each training epoch. 

The paper discussed the limitations of two commonly used methods in this domain, (1) Data Pruning: Selecting the most informative examples to train more efficiently. (2) Dataset Distillation: Creating synthetic examples that represent the larger dataset to train quickly.

The paper proposes Repeated Sampling of Random Subsets (RS2), which simplifies the process by randomly selecting different data subsets for each training epoch, promoting broader learning and efficiency. RS2 has been shown to outperform State-of-the-Art methods, achieving near-full dataset accuracy with significantly reduced training time on various datasets, including large scale image benchmarks like ImageNet. 

It is interesting to note that the paper achieves very close performance to models trained on complete datasets with just 10\% of the datapoints for large scale benchmarks like ImageNet.

### Strengths
1. The paper presents a simple but novel approach to achieve significant reductions in time-to-accuracy while training on a fraction of the full dataset per epoch of model training.
2. The paper also presents detailed theoretical properties that support the faster convergence of the model as compared to existing approaches in the domain.
3. The paper demonstrates results on four image datasets including large scale image benchmarks like ImageNet wherein it achieves State-of-the-Art (SoTA) performance (accuracy) with just 10 \% of the data samples in the complete dataset.
4. The paper also demonstrates SoTA performance on auxiliary tasks like data distillation, noisy label classification and pretraining of large language models.

### Weaknesses
 1. Although the experimental results are exemplary (primary contributor to my decision), the method RS2 itself is an incremental update over random sampling. The paper must call out the clear difference with SoTA methods (please refer to questions for more details). Specifically, while the paper mentions that existing methods use importance-based sampling, it does not clearly articulate why random sampling with replacement, as done in RS2, is superior. The paper needs to provide a more nuanced discussion on the specific limitations of importance-based sampling that RS2 overcomes. For example, does importance sampling lead to a lack of diversity in the selected subsets, causing the model to overfit to a narrow set of examples? This needs to be explicitly stated and supported with evidence or theoretical arguments.
2. All experiments demonstrated in the paper adopt canonical benchmarks which are well curated, while lacking experiments on datasets (eg: MedMNIST (Yang et al., 2021), CUBS-2011 (Wah et al., 2011)) with large intra-class variance and class-imbalance wherein data pruning might underperform. The absence of such experiments limits the generalizability of the findings. Datasets with high intra-class variance and class imbalance often pose unique challenges for data pruning methods, as the most 'informative' samples might not be representative of the overall data distribution. This can lead to biased models that perform poorly on underrepresented classes. The paper should include experiments on these types of datasets to demonstrate the robustness of RS2.
3. The paper does not show any relation between the theoretical properties of RS2 (convergence rate and bounds on generalization error) and the conducted experiments. While the paper presents theoretical analysis, it fails to connect these theoretical results to the empirical findings. For instance, the paper should discuss whether the observed convergence rates in the experiments align with the theoretical bounds derived. Furthermore, the paper should analyze whether the generalization error observed in the experiments is consistent with the theoretical bounds. This lack of connection between theory and experiments weakens the paper's claims.

### Questions
1. The subset selection strategy of RS2 without replacement is unclear in section 3. A suggestion would be to replace the textual description in this section with Algorithm 2 in section D of the appendix.
2. The variables $n$ and $N$ are used interchangeably in section 4.
3. The term ‘selection ratio’ and ‘pruning ratio’ has been used interchangeably and should be fixed in the paper.
4. As mentioned in the ‘weaknesses’ of the paper, experiments on real-world class-imbalanced settings ((eg: MedMNIST (Yang et al., 2021), CUBS-2011 (Wah et al., 2011))) would be an effective demonstration of the application of RS2.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper compares approaches to reducing the training time by curating a smaller representative dataset like data pruning, coreset selection, and dataset distillation to a simple random sampling-based approach termed Repeated Sampling of Random Subsets (RS2).  Results show that prior adaptive approaches fail to beat RS2 on four image datasets in both final accuracy and time-to-accuracy when accounting for overhead associated with active selection.  Owing to the properties of random
sampling, RS2 comes with convergence and generalization guarantees.  The authors highlight the importance of evaluating approaches based on time-to-accuracy and the need for more complex approaches to beat a simple baseline like RS2.

### Strengths
- The authors point out important considerations missing in prior work on speeding up training with adaptive dataset subset selection.  First, whether there is a need to restrict data to a fixed subset in the first place if similar accuracy can be achieved by training with a compressed learning rate schedule on fewer epochs.  Second, the importance of including overhead associated with data selection when evaluating training compute efficiency of an approach.

### Weaknesses
 - As I understand, RS2 without replacement is effectively the same as training on the full dataset with the learning rate schedule compressed into fewer epochs.  RS2 with replacement is a slight variant to that but still highly resembles standard training with shuffling between epochs just with a condensed training window. This is not discussed anywhere but brings into question the whole exposition of proposing RS2 as a sampling method.  An even simpler baseline is training as usual on the full dataset with the condensed schedule.  I would wager such a baseline would yield similar performance as RS2.
- The paper is light on experimental details for how prior methods are evaluated in particular for case where samples are reselected based on latest model weights.  I am surprised the results in Table 1 right are worse than that for Table 1 left when selecting a new subset with updated model weights can expand the number of samples seen during training.  The poor performance of AL approaches like Entropy and Margin also contradicts the experimental results from Park et al., 2022 where AL outperformance other subset selection methods.

### Questions
- What model weights are used for computing the static subsets of approaches like Entropy, Margin, Least Confidence, etc in Table 1 left?
- How often are importance scores recomputed for adaptive methods in Table 1 right?
- How does random with fixed subset perform on the tasks studied?
- How does training on full dataset with the same LR schedule and training window as that used for RS2 perform?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper revisits the utility of random selection when it comes to speeding up the training. The paper considers two types of random sampling, random sampling with and without replacement. The paper surprisingly shows that these two samplings can easily outperform the popular data subset selection baselines (adaptively or static) when it comes to comparing the time to achieve the same accuracy. Moreover, the authors show that for many training budgets, it outperforms famous baselines, demonstrating the efficacy of uniform random  selection.

### Strengths
The paper conducts experiments across several baselines, including active learning and dataset distillation. In addition, the paper provides an analysis of the convergence of the RS2 algorithm, which I am not sure is how novel is it, in terms of proof technique, but it's a good contribution to have in any data subset selection paper. Lastly, I think robustness and LLM pretraining results are also interesting making the overall comparisons spanning different modalities and scales.

### Weaknesses
- RS2 w/o replacement is the same as training on a reduced number of epochs. For the cases where RS2 achieves the same accuracy in significantly less amount of time, I think the main issue was not tuning the epoch/learning rate hyperparameter of the full dataset baseline. Therefore making the RS2 w/o replacement results less exciting. 

- Can authors provide a plot #unique examples seen throughout training? It could be the case that certain baselines are not exploring the full dataset, due to possibly inadequate hyperparameter search on them. 

- I am very confused about Table 1, where we allow the model to update the subset after every round. I request authors provide a clear description for every baseline for both cases, where the distribution is allowed to change over time. The notion of RC and RS has to be made clear for each of the baselines. 

- Why is RC's performance extremely worse in certain baselines such as GraNd? In general, why is there a strong dip in the performance of all the baselines, when switched to RC? 

- For the baselines that sample set based on submodular function, what does it mean to have a distribution? How are authors defining the distribution over each set of size "k"? If that is the case, how are they sampling? If not, what is the heuristic?

- I think it is not correct to compare active learning baselines to subset selection schemes that look at  - (1) all the dataset, but the reduced number of iterations, and (2) assume labels for all the data points, since AL does not assume labels. 

- Each of these baseline papers has comparisons against random, on the other hand here the authors break the baselines by mere random selection. What is the reason for this discrepancy?  

- Can authors please point to the hyperparameter tuning for each of the baselines? Submodular functions often work well if tuned properly, therefore it is important to see if enough hyperparameter tuning was done to make sure the function is good. 

- For the submodular methods if the corresponding greedy gain was used to sample sets (distribution defined using gains), it should be noted that if the function saturates, then greedy gains do not provide any useful information (yet another reason to provide hyperparameter search grids).

### Questions
Can authors also add a comparison to more recent versions of CRAIG such as CREST [1]? 

[1] Towards Sustainable Learning: Coresets for Data-efficient Deep Learning (ICML'23)

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper revisits a rather simple subset selection strategy for efficient deep learning. The authors claim that repeated sampling of random subsets (RS2), that is, only randomly sample subsets at each round, can be a powerful baseline strategy. RS2 is competitive against most of the sampling strategies as well as dataset distillation methods developed previously. Besides, there is no additional computation cost extracting the coreset using RS2, so RS2 reaches the best acceleration under the same sample budget.

### Strengths
1.	Selecting the coreset for efficient deep learning is important for machine learning practices. The paper may be valuable to the community trying to address this problem. To the best of my knowledge, this is the first paper to formally discuss the repeated random sampling strategy.

2.	The paper is clearly written, the authors do a good job in presenting their intuitions, and the analysis is convincing. 

3.	Extensive experiments are conducted to show the effectiveness of RS2.

### Weaknesses
1.	The paper considers only the low data regime (<30% data). RS2 performs well in this regime as it will not reshape the underlying data distribution. Actually, I think whether RS2 can outperform other strategies depends on the subset size and the property of the original dataset itself. In the data-abundance regime,  I believe selecting "harder" samples benefits model training. More discussion on this will greatly strengthen the paper. 

2.	In the theoretical analysis, only RS2 without replacement is considered. I wonder if the result changes for RS2 with replacement.

### Questions
Please see the weakness part above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
