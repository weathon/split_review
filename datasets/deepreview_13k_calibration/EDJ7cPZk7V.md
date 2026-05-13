# Forgetting Order of Continual Learning: What is Learned First is Forgotten Last

- Decision: Reject
- Avg Score: 6.40
- Scores: 8, 3, 6, 5, 10

## Abstract
Catastrophic forgetting poses a significant challenge in continual learning, where models often forget previous tasks when trained on new data. Our empirical analysis reveals a strong correlation between catastrophic forgetting and the learning speed of examples: examples learned early are rarely forgotten, while those learned later are more susceptible to forgetting. We demonstrate that replay-based continual learning methods can leverage this phenomenon by focusing on mid-learned examples for rehearsal. We introduce Goldilocks, a novel replay buffer sampling method that filters out examples learned too quickly or too slowly, keeping those learned at an intermediate speed. Goldilocks improves existing continual learning algorithms, leading to state-of-the-art performance across several image classification tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper analyzes the forgetting discrepancies among different examples and provides a theory that the examples that are learned the first and last are the least prone to forgetting. The paper also proposes a practical algorithm for sample selection for the replay buffer where it removes the examples that are learned first or last.

### Strengths
- The paper demonstrates simplicity bias in neural networks.
- The paper proposes an effective replay buffer sample selection algorithm that outperforms uniform in many cases and also other subsampling algorithms in some cases.

### Weaknesses
 - Completeness: Table-1 should also include CIFAR-100-5, CIFAR-100-20 and Tiny-ImageNet.
- Limitation: The conclusion may depend on the training time on each task. For example, if the number of epochs is small, then the hardest to learn examples have not been learned, then it may also need to stay in the replay buffer. The paper has also acknowledged that the method may not be suitable for stream learning in its limitation section. However, it would be better if the paper can give guidance on the number of epochs required for the proposed method to work well.
- Hyperparameters: The algorithm may rely on selecting hyperparameters (e.g. s and q) for removing the slowest and fastest examples. And it might be unclear how that parameter varies across different datasets. If choosing a hyperparameter repetitive experiments, then it may defeat the premise of continual learning.

### Questions
- I wonder if the authors can provide experiments on other datasets, and show how hyperparameters will vary across different datasets.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, the authors present an empirical study that reveals a strong correlation between catastrophic forgetting and the learning speed of examples. They found that the examples that are learned early in the continual learning process are rarely forgotten, while those learned later are more susceptible to forgetting. Leveraging this finding, they introduced a new replay buffer sampling method - Goldilocks that filters out examples learned too quickly or too slowly, keeping those learned at an intermediate speed. On several low to mid-complexity image classification tasks, they showed the efficacy of their proposed method.

### Strengths
Strength: 

* The analysis of learning speed and catastrophic forgetting in continual learning is new. 
* The authors presented the idea clearly. 
* Illustrations and figures - especially the binary classification matrix plots are very useful in understanding the concept of the paper.

### Weaknesses
Weaknesses:
* The observed correlation between example learning speed and catastrophic forgetting is empirical, with no theoretical analysis provided, hence of limited significance.
* Empirical analysis provided to establish the correlation is not sufficient. For example, learning dynamics depend on various factors such as learning rate, network architecture, optimizer, regularization etc. One of the major issues with the current paper is that it does not explore these dimensions to establish the correlation between example learning speed and catastrophic forgetting.
* How learning rate for different tasks (initial tasks and later tasks) impact the correlation? If we use a smaller learning rate for later tasks how do forgetting dynamics change? A detailed study is missing here.
* How does the correlation change if plain SGD, Adam, Ada-Grad, etc. optimizers are used?
* The paper only explores ResNet and its smaller variants for the analysis. For other architectures such as transformers, VGG net, etc do the same conclusions stand?
* Gridlock is evaluated on low-to-mid complexity image classification tasks only. Detailed analysis on higher complexity classification tasks on ImageNet is missing.
* As stated in the limitation section, the method does not apply to online CL settings and is only limited to classification tasks.

### Questions
See the Weakness section above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores a strategy for selecting examples to include in a replay buffer for continual learning. The main idea is to exclude two sets of examples: those that are learned too easily and those that are difficult to learn, with the aim of improving generalization across a sequence of classification tasks.

### Strengths
The authors take this fairly simple idea and run a series of tests.  These experiments cover a range of datasets and settings for the size of the buffer of replayed examples. They also explore two different task orderings and show that the results are consistent across them. Most of the experiments focus on a sequence consisting of just a pair of tasks, but there are some results with a more extensive set of tasks.  The experimentation and reporting of results is clear and fairly complete, especially with the standard error discussion and class incremental results presented in the Appendix.

### Weaknesses
The chief weakness is a lack of significance.  The paper is mostly an exploration of whether a type of simplicity bias can be used to guide the selection of examples in the replay buffer. It does not advance a substantive new method or analysis, but seems like a straightforward application of existing ideas.  The results show a consistent but not whopping win for this approach,

A second weakness is a lack of analysis of the types of examples that fit into the too-easy and too-hard categories. Showing that the examples that are learned earlier are forgotten less and those that are learned later are forgotten more is not surprising, as it fits well with various studies such as the simplicity work (as acknowledged by the authors).

As well there is quite a bit of variation across the datasets and experimental conditions, such as buffer size, in terms of the relative performance of different percentages of the too-small and too-fast sets that should be excluded.  There is no analysis of this, which begs the question of how to set these hyperparameters in a new setting.

### Questions
I'd recommend that the authors make the method more practically applicable by showing how it can be deployed in a few new settings (e.g., combination of dataset and replay buffer size). One way to address this would be to demonstrate that a small amount of data and experimentation can be used to determine a set of hyperparameters that exhibit strong performance.

One minor question concerns the title, which doesn't quite fit the primary message of the paper.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In Continual Learning, the methods that have worked best are memory-based. These methods work by sampling a percentage of the training set of each task that is then used in the training of subsequent tasks to ‘remember’ past tasks. In this paper, the authors analyse the best examples to populate the buffer. They analyse the learning speed, showing how it affects performance when sampling from the training set by leaving out the top slower or quickest-to-learn samples. The authors show that items learned quickly are the least forgotten, and conversely, items learned more slowly are the first to be forgotten. With this insight, the authors present a new methodology for populating memory called ‘Goldilocks’. Empirically, the authors show that sampling only from items with an intermediate learning speed can have comparable or better results than current methods for populating memory across different benchmarks.

### Strengths
- The authors' motivation for presenting the problem is evident in their approach, which aids in understanding the problem and its relevance. 
- An analysis is presented that helps to understand the method before it is presented. Multiple experiments show the usefulness of eliminating the very fast and slow-to-learn examples, to sample only intermediate ones.

### Weaknesses
 - Despite the authors' thorough analysis, no explanation or intuition is provided as to why medium learning speed items are the most useful for populating memory. It would be good if the authors provided a rationale beyond the empirical results. This rationale could be based on intuition or other work.
- The results shown are limited to a small group of scenarios. The analyses performed are only based on CIFAR10 and CIFAR100 divided into 2 tasks. A better analysis should emphasize a broader set of scenarios and benchmarks to ensure the generalisability of the performance.
    - Other works have shown that performance can change drastically as the number of tasks increases.
    - The analysis shown is with the Task-Incremental learning scenario, I recommend considering the class-incremental scenario as it is a more widely accepted scenario. The authors mention that the analysis is in the Appendix, but I did not find corresponding results.
    - This may affect figures such as Fig2a, where you can see that the forgetting is not as drastic as in class incremental and even a slight increase is seen near epoch 150.
- Although the authors show, both in their analysis and with their method, that the results achieved are better than other alternatives, the benefit is only marginal. Often even less than the standard deviation.
    - During the analysis, the difference is often at most 2%, between all removal combinations slowest/quickest. This shows that the margin of improvement is very slight compared to uniformly populating the memory.
- Some arguments and comments in the paper are difficult to extract from the results.
    - One example is in line 397: 'We find that regardless of the similarity or dissimilarity between subsequent tasks and the original task, the optimal replay buffer composition remains largely independent and consistent'. Nowhere does it show how different or similar the tasks they use are, and they base this only on experiments in CIFAR100.

### Questions
- A score called c-score [1] seeks to explain how consistent an example is during training. Can learning speed be related to this score?
- The same order of classes is always used, which may affect the conclusions drawn. Is there a reason for this?
    - Each seed used to run the experiments commonly brings a new class order. This helps to not bias the results to a particular order that may benefit one method over another.
- In line 212, the authors mention using an experience replay strategy that alternates batches of data from the new task and the replay buffer. Why use this and not the standard approach of mixing samples from the current task and the buffer in a 50-50 way?
- Can the learning rate chosen affect the results and conclusions? 
    - For example, in fine-tuning, it is recommended to use a small learning rate so as not to modify the old weights significantly.
- Do the authors have results for different CL methods with different strategies to populate the memory? The methods are usually independent of how the data is sampled, so a complete comparison of how much sampling methods affect different memory-based methods can be done.
- I understand using 500 examples for CIFAR10 and CIFAR100, but in TinyImagenet, this means less than 3 elements per class, which can strongly affect the sampling methods used. Do you have experiments with a higher number? It would also be essential to mention the reference to the 'original work' in line 466.

[1] Jiang, Ziheng, et al. "Characterizing Structural Regularities of Labeled Data in Overparameterized Models." International Conference on Machine Learning. PMLR, 2021.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The authors claim & show that examples that are learned first (simple examples), are in general not forgotten, while examples that are the hardest are forgotten quickly. They propose a replay sampling method that attempts to counter-balance this phenomenon by replaying only samples that are of medium difficulty.

### Strengths
- The authors make an interesting observation that could have strong impact in understanding the learning process of neural networks and improving the replay-based continual learning methods.
- Strong evidence is brought on CIFAR100, using different tools (Figure 2), among which training of multiple networks and consistent observation across these networks that learning speed is strongly correlated with forgetting rate.
- They obtain consistent improvements when applying their sampling method on top of existing methods, and across datasets (CIFAR 100 , CIFAR 10 and TinyImagenet)
- The results are clearly presented using several demonstration tools and the designed method is simple, the ablation of the number of quickly learned samples and slowly learned samples is comprehensive and easy to read.

### Weaknesses
 - **W1** Maybe a bit more attention could be given to the engineering of class-incremental learning results to make them comparable to the sota one. Right now they are only given on CIFAR100-2 with buffer size of 500. Would be interesting to have them on CIFAR100-10 with bs of 1k or 2k for instance, and maybe applying some anti task-recency bias method or simply probing the representations to show whether the probed representation from the model using the new sampling method is better.

### Questions
- **Q1** It is good that results for both CIL and TIL are presented, but for the CIL, they are way less furnished. Would it be possible to have the same than Figure 2 for the CIL in the appendix ?

### Soundness
4

### Presentation
4

### Contribution
4
