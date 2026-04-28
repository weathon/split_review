# Experimental Design for Nonstationary Optimization

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Traditional methods for optimizing neural networks often struggle when used
to train networks in settings where the data distributions change, and plasticity
preservation methods have been shown to improve performance in such settings
(e.g. continual learning and reinforcement learning). With the growing inter-
est in nonstationary optimization and plasticity research, there is also a growing
need to properly define experimental design and hyperparameter search protocols
to enable principled research. Each new proposed work typically adds several
new hyperparameters makes many more design decisions such as hyperparame-
ter selection protocols, evaluation protocols, and types of tasks examined. While
innovation in experiment design is important, it is also necessary to (1) question
whether those innovations are leading to the best progress and (2) have standard-
ized practices that make it easier to directly compare to prior works. In this paper,
we first perform an extensive empirical study of over 27,000 trials looking at the
performance of different methods and hyperparameters across different settings
and architectures used in the literature to provide an evaluation of these methods
and the hyperparameters they use under similar experimental conditions. We then
examine several core experiment design choices made by the community, affirm-
ing some while providing evidence against others, and provide concrete recom-
mendations and analysis that can be used to guide future research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this paper, the authors study the experimental design in non-stationary optimization. They explore various aspects of experiment design, from hyper-parameter selection protocols to the number of seeds needed for hyper-parameter selection. The paper contains some interesting results about hyper-parameter selection, number of seeds, experiment protocols, etc.

### Strengths
This work is novel because there has not been any explicit focus on empirical design in plasticity research. It could be an important contribution to the community as it could speed up progress and provide a more unified focus for the field. 

The studies about hyper-parameter selection protocol are useful as they could help develop methods that overfit less.

Results show that the community needs to focus on test plasticity, which is interesting and needs to be evaluated further.

The study about the number of seeds needed for hyper-parameter selection and evaluation of a method is good, and it could save computation on many future experiments.

### Weaknesses
The paper is not well-written and contains a lot of small errors, which reduces my confidence in the quality of the paper and the results presented therein. For example, there are no labels in Figure 3, and line 424 says "Figure 5b and 5b", a typo in the title of section 4.4, among many others. I suggest the authors spend some more time on writing (maybe by using Grammarly) and making sure the presentation is up to the mark.

The experiments with ResNet and permuted CIFAR are not useful. When inputs are permuted, all the spatial information in the image is lost. In such a case, convolutional networks like ResNet-18 are not useful. These experiments have not been done in the community either, people have only used feed-forward networks with Permuted Input experiments. The ResNet experiments on Permuted CIFAR-100 should be removed from the paper.

What is plotted in Figure 2? Is it the performance of the best hyper-parameter configuration or the average performance across hyper-parameters? And what does "best" mean? Highest training accuracy or test accuracy or train for Figure 2a and test for Figure 2b? 

The results presented in Figure 4 are used to argue that "improving training does not end up correlating with ... improving model performance" (lines 370-371). But that is not what the figure shows. Figure 4a clearly shows that there is a positive correlation between training accuracy and test accuracy. What Figure 4b shows is that for the best hyper-parameters, there is a weak or no correlation between the two. That just means that after a point, trainability does not improve generalizability. But that does not mean "improving training does not ... correlating ... improving model performance". The claim on lines 370-371 and the 3rd bullet point in section 5 need to be changed. 

In the introduction and Section 4.5, the paper asks, "How many tasks do you need to include in your training sequences?" The answer should be infinity because we are in a lifelong learning setting. Do the authors mean, "How many tasks do you need to include in your training sequences **for tuning hyper-parameters**?" or does that statement mean something else?

### Questions
What are the labels for both lines in Figure 3?

What happens if you plot training loss and test loss in Figure 4? I suspect that could reveal more correlation. Particularly for ResNet in Figure 4b, as it gets to 100% train accuracy in most cases. 

In Figure 5d, do you mean p(Method ranking **does not** change) instead of p(Method ranking changes)?

### Soundness
2

### Presentation
2

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
The authors investigate the experimental procedures that are used to evaluate algorithms in continual learning settings.
The submission points out that these practices are usually unaddressed or only implicitly addressed in current experimental work in continual learning.
By focusing on a well-curated set of datasets, nonstationarities, methods and architectures, the submission poses a critical analyses of these practices and implicit assumptions.
A few interesting conclusions include that maintaining trainability may not be indiciative of generalizability, and that several tasks may be needed to evaluate a set of hyperparameters for continual learning.

I am currently rating this paper as marginally below acceptance. However, I am willing to increase my score if some of the concerns below are addressed.

### Strengths
- The problem being addressed in this submission is timely, understudied and important. 
- Empirically, the submission poses and answers several important questions regarding best practice for non-stationary optimization.

### Weaknesses
 - While most of the paper provides concrete takeaways which question current practice, there are some inconclusive results that could use further clarification
- Several of the results aggregate performance across several different categories of methods (e.g., architectural(crelu), regularization and resetting). A few analyses on individual methods, non-aggregated, would improve the empirical results and add clarity.
- The presentation of the paper is mostly good, but with room for improvement (see below).

- Figure 2 (presentation): It is difficult to infer conclusions from this plot due to the number of baselines and settings being compared in a single graph. I wonder if this information is not better represented in a table, because the relative ordering of the settings (on the x-axis) and the placement of MLP next to ResNet does not have any semantic meaning in the presentation of these results.

- Figure 2 (results): I am surprised that there is so much variation in the results for different combinations of methods and nonstationarities. One thing potential problem is that the ranking is too sensitive to statistically insignificant performance differences. Do you know how these results would look like if average test accuracy was reported instead?

- Figure 3: The lines in these graphs are not labelled, I assume one is for protocol 1 and the other is for protocol 2? If that is the case, I do not see that large of a difference between the two (except on shuffled CIFAR-10). Thus, I am uncertain about the conclusion that "protocol 2 transfers better to the unseen data". The conclusion suggested at the end of Section 4.1 does not seem well-supported by this data.

- Clarification for statistical bootstrapping: what exactly is being resampled for the estimate? It is not clear how "resampling the seeds" means, because bootstrapping usually involves resampling from some data to construct an estimator.

- Clarifying seeds in Section 4.1: Why are the total number of seeds quoted (n=20) unequal between protocol 1 and 2? It seems like that the seeds are partitioned between model selection and evaluation? As I understand the second paragraph, 10 seeds are used for model selection and 10 seeds are used for evaluation, yielding the total of 20? But in that case, why does protocol 2 only use 5 seeds?

- There seems to be no clear takeaway in Section 4.2: it would be helfpul to also investigate the contributing factors for generally well-performing methods. For example, are the methods performant because they are more robust to hyperparameters (and hence, protocol 2 can easily identify good hyperparameters)? I do not think Appendix C answers this question.

- Section 4.3: The strong conclusion here is valuable. I wonder if this conclusion depends on the plasticity-preserving method. I am not able to tell from Figure 4, but presumably some methods may better correlate train and test accuracy, which would be hidden in this combined analysis.

- Section 4.4: Again, I wonder if the number of seeds needed to identify a good hyperparameter configuration depends more strongly on the method used for training, rather than the aggregate analysis.

** Minor Comments
- Many instances of "boostrapping" should be replaced with "bootstrapping"

### Questions
- Figure 2 (presentation): It is difficult to infer conclusions from this plot due to the number of baselines and settings being compared in a single graph. I wonder if this information is not better represented in a table, because the relative ordering of the settings (on the x-axis) and the placement of MLP next to ResNet does not have any semantic meaning in the presentation of these results.

- Figure 2 (results): I am surprised that there is so much variation in the results for different combinations of methods and nonstationarities. One thing potential problem is that the ranking is too sensitive to statistically insignificant performance differences. Do you know how these results would look like if average test accuracy was reported instead?

- Figure 3: The lines in these graphs are not labelled, I assume one is for protocol 1 and the other is for protocol 2? If that is the case, I do not see that large of a difference between the two (except on shuffled CIFAR-10). Thus, I am uncertain about the conclusion that "protocol 2 transfers better to the unseen data". The conclusion suggested at the end of Section 4.1 does not seem well-supported by this data.

- Clarification for statistical bootstrapping: what exactly is being resampled for the estimate? It is not clear how "resampling the seeds" means, because bootstrapping usually involves resampling from some data to construct an estimator.

- Clarifying seeds in Section 4.1: Why are the total number of seeds quoted (n=20) unequal between protocol 1 and 2? It seems like that the seeds are partitioned between model selection and evaluation? As I understand the second paragraph, 10 seeds are used for model selection and 10 seeds are used for evaluation, yielding the total of 20? But in that case, why does protocol 2 only use 5 seeds?

- There seems to be no clear takeaway in Section 4.2: it would be helfpul to also investigate the contributing factors for generally well-performing methods. For example, are the methods performant because they are more robust to hyperparameters (and hence, protocol 2 can easily identify good hyperparameters)? I do not think Appendix C answers this question.

- Section 4.3: The strong conclusion here is valuable. I wonder if this conclusion depends on the plasticity-preserving method. I am not able to tell from Figure 4, but presumably some methods may better correlate train and test accuracy, which would be hidden in this combined analysis.

- Section 4.4: Again, I wonder if the number of seeds needed to identify a good hyperparameter configuration depends more strongly on the method used for training, rather than the aggregate analysis.

** Minor Comments
- Many instances of "boostrapping" should be replaced with "bootstrapping"

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents an empirical study comparing various existing methods to mitigate plasticity loss in continual learning. The paper makes two contributions: (1) a comparison of existing methods under a unified setting, and (2) an evaluation of and suggestions for hyperparameter selection protocols, number of seeds, and train vs. test accuracy evaluation.

### Strengths
Continual learning is a rapidly growing and important research area. An independent comparison of existing algorithms under a unified setting aids in identifying the most effective techniques, thereby guiding future research.

### Weaknesses
The study setting has significant limitations and is far from realistic for continual learning. My main concern is the relevance of the proposed recipes to more realistic continual learning scenarios. Below, I summarize different ways in which the study’s setting is limited.  

- Distribution shifts: The paper uses simple forms of distribution shifts, namely pixel permutation, label permutation, and noisy labels. Although these methods are frequently used in existing literature, they are highly unrealistic. Pixel permutation, for example, never occurs in real-world scenarios (and the use of CNNs for these types of images is questionable). Moreover, these distribution shifts are simple to address, as they can be resolved by adjusting weights in the first or last layer. While benchmarking is an unresolved problem for continual learning and good benchmarks are still limited in the literature, more realistic distribution shifts have been proposed in other works (e.g., see the first three environments studied in Dohre et al., 2024), which could be used in the current paper.  

- Test/Train sets: In a realistic continual learning setting, there is no separate test or train set. Instead, there is a single, continuous stream of incoming data, to which a model adapts. Cumulative online loss serves as the primary performance measure.  

- Random seeds: True continual learning settings do not involve random seeds for the same reason discussed above, especially in scenarios with sufficiently long data streams.  

- Hyperparameter selection:  Continual learning is best achieved through continual optimization, which includes algorithms for continual hyperparameter optimization. Here, hyperparameters (e.g., learning rate) are optimized and updated at every training step, over the whole lifetime of agent. See, for example, IDBD, Hypergradient Descent, and MetaOptimize.  

I understand that these limitations are also present in many existing works. While evaluations in limited settings are acceptable in experimental sections for papers introducing new algorithms, such limitations are insufficient for an empirical study aiming to provide guidelines for future research.  

Lastly, the scale of the experiments and models used is relatively small for a fully empirical study.

### Questions
Could the authors conduct experiments on more realistic benchmarks from the literature or propose a new, more realistic benchmark?    

In Fig. 9, the Online baseline (with no LoP technique) outperforms some LoP algorithms. What is the reason for this? Could it be due to insufficient hyperparameter tuning?  

The paper suggests that test accuracy rankings differ significantly from train accuracy rankings. Could the authors quantify this gap for different algorithms? Although the rankings change, the actual performance difference might be minor.  

How would CReLU perform compared to other methods if it used the same number of weights?  

What do the two curves in Fig. 3 represent? There are no legends.  

There are also a few typos on page two.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper conducts several experiments on selecting hyperparameters from the previous literatures for nonstationary optimization and demonstrates that using multiple streams of tasks for hyperparameters selection is the best approach among the commonly used protocols.
It also gives insight on finding configurations with good performance under low resource budget.
In addition, it shows that maintaining the training accuracy does not relate to a better generalizability in nonstationary optimization settings.

### Strengths
* Provides an evidence that, there is no correlation between trainability and generalizability.
* Shows large number of seeds are not necessary for finding good hyperparameters.
* Provides direction on resource-constrained experiments.

### Weaknesses
 - The paper is not well written
    - Line 142: Duplicate of 'the added'. Same line, duplicate of 'be' in 'Should be actually be used'
    - Line 153, there is no obvious connection between this and the next sentence.
    - Line 283: 'used for selection' which I think you are referring to 'used for evaluation' instead?
    - Line 375: 'HOW MANY SEEDS DO YOU TO EVALUATE A METHOD',  miss a 'need'?
    - Line 722:  Missing the batch size for resnet-18.
    - Figure 2 is hard to interpret. One possible improvement is to add different line shapes.
    - Figure 3 does not have the legend.
    - Figure 4's line is hard to differentiate the methods. Same as figure 2, maybe add different line shape.
- The protocol 3 is considered to be critical to do lifelong learning. But there is no comparison between this protocol and the other protocols to prove that statement.

### Questions
Why is the number of seeds and tasks different in different type of networks, same for the gradient steps?

### Soundness
2

### Presentation
2

### Contribution
2
