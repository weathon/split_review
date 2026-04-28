# Implicit regularization of multi-task learning and finetuning in overparameterized neural networks

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 8, 3

## Abstract
It is common in deep learning to train networks on auxiliary tasks with the expectation that the learning will transfer, at least partially, to another task of interest. In this work, we investigate the inductive biases that result from learning auxiliary tasks, either simultaneously (multi-task learning, MTL) or sequentially (pretraining and subsequent finetuning, PT+FT). In the simplified setting of two-layer diagonal linear networks trained with gradient descent, we identify implicit regularization penalties associated with MTL and PT+FT, both of which incentivize feature sharing between tasks and sparsity in learned task-specific features. Notably, our results imply that during finetuning, networks operate in a hybrid of the kernel (or "lazy") regime and the feature learning ("rich") regime identified in prior work. Moreover, PT+FT can exhibit a novel ``nested feature learning'' behavior not captured by either regime, which biases it to extract a sparse subset of the features learned during pretraining. In ReLU networks, we reproduce all of these qualitative behaviors. We also observe that PT+FT (but not MTL) is biased to learn features that are correlated with (but distinct from) those needed for the auxiliary task, while MTL is biased toward using identical features for both tasks. As a result, we find that in realistic settings, MTL generalizes better when comparatively little data is available for the task of interest, while PT+FT outperforms it with more data available. We show that our findings hold qualitatively for a deep architecture trained on image classification tasks. Our characterization of the nested feature learning regime also motivates a modification to PT+FT that we find empirically improves performance. Overall, our results shed light on the impact of auxiliary task learning and suggest ways to leverage it more effectively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the implicit regularization effects of multi-task learning (MTL) and pretraining followed by fine-tuning (PT+FT) in overparameterized neural networks. It makes a valuable contribution to our understanding of how auxiliary task learning influences neural network training. It offers practical insights for improving fine-tuning performance and provides a novel perspective on the dynamics of feature learning in overparameterized networks.

### Strengths
1. Novel Contribution: The paper introduces a novel concept of "nested feature learning," which is not captured by existing regimes ("lazy" or "rich") in the context of multi-task learning (MTL) and pre-training followed by fine-tuning (PT+FT). This new insight contributes to a deeper understanding of how neural networks operate in complex learning scenarios.

2. Inductive Biases in Different Scenarios: The authors explore the inductive biases in both linear and non-linear scenarios, providing a comprehensive analysis. This part looks good to me.

3. Real-world Experiment setting: The authors employ a combination of theoretical analysis and empirical experiments, including the use of real-world networks like ResNet-18 and challenging benchmarks like CIFAR-100. This ensures that the findings are grounded in practical relevance.

### Weaknesses
1. Sample Size and Repetition: The paper would benefit from addressing the potential limitation regarding sample size and repetition in the experiments. It is essential to clarify whether the results, as shown in Figure 3(f), are robust across different samples. The authors should consider repeating the experiments with various samples multiple times and reporting the mean performance along with confidence intervals. As it stands, it appears that the experiments were conducted only once, which may raise concerns about the reliability and generalizability of the findings. A more comprehensive analysis of the impact of different samples on the results would strengthen the paper's credibility and reliability.

2. Lack of Visualization and Evaluation Metrics: The paper could benefit from a more comprehensive presentation of results. It lacks visualization techniques to visually illustrate these biases. Visual representations can provide a clearer and more intuitive understanding of the observed phenomena.

### Questions
1. Regarding the experimental repetition, it's not clear why the author relies on results from a single experiment. Is this choice due to concerns about potential bias in the sampled data, or are there other reasons for not conducting multiple experiments to ensure robustness and reliability of the findings?

2. The paper mentions using "1024" samples for different testing scenarios. Could the authors provide more context on the rationale behind this sample size? What happens when the sample numbers are significantly larger? Are the "1024" samples allocated for each task, or is it 1024 samples shared among all tasks? 

3. The figures corresponding to samples seem to lack clarity. The x-axis is labeled with "32 samples" and "256 samples," but it's not entirely clear which parts of the figures represent actual experimental results. Could the authors consider visually highlighting the data points with dots and connecting them with lines to provide a more explicit representation of the experimental results, making it easier for readers to interpret the findings?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper provides a theoretical analysis characterizing the implicit regularization effects of multi-task learning (MTL) and pretraining + finetuning (PT+FT). The main contributions are:

- Derives analytical expressions for diagonal linear networks quantifying the implicit regularization biases of MTL (l1,2 norm) and PT+FT (Q norm) that encourage feature sharing and sparsity.
- Validates that MTL and PT+FT exhibit these regularizer-like behaviors for both linear and relu neural networks. 
- Identifies a "nested feature learning" regime unique to PT+FT that enables sparse reuse of pretrained features. Proposes techniques to leverage this.
- Shows PT+FT is more flexible in "soft" feature sharing than MTL, leading to tradeoffs based on dataset size.
- Demonstrates applicability of theoretical insights on CIFAR-100 for improving auxiliary task learning.

Overall, this work provides novel theoretical analysis of the under-studied problem of characterizing implicit regularization in MTL and PT+FT. The paper opens promising new directions for better understanding and improvement of auxiliary task learning techniques widely used in deep learning.

### Strengths
- The paper focuses on an important open problem in deep learning theory. Using PT+FT is the de-facto go to tool for creating a modern DNN both in MLP and CV. Comparison to MTL with auxiliary task is a good way to analyze the available alternatives.
- Provides analytical characterization of implicit regularization in MTL and PT+FT for diagonal linear networks 
- Validation of theory through experiments on synthetic and CIFAR100
- Identifies unique "nested feature learning" regime of PT+FT
- I think the experiments on the correlated features and the heterogeneous feature sharing are great, as this is probably the more relevant case for the real world applications.

### Weaknesses
 - I would like to see more practical experiments that demonstrate the theoretical findings. In the given experiments the main task is 2 classes on CIFAR100 but it is not clear how the choice of the classes was made and weather it makes any difference which classes taken. I understand this is not the main focus of the paper but I think this section could be improved.
- The main focus of paper is on MSE loss, I think adding the CE loss focus could improve the paper.

### Questions
See weaknesses

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
For two-layer diagonal linear networks, the current paper studies the implicit regularization of finetuning and multi-task learning. It derives norm-based measures that are implicitly minimized, and interprets them as inducing reuse of the auxiliary task weights and sparsity.

In the context of finetuning, the implicit regularization can be seen as an interpolation between L1 (rich) and L2 (kernel) regularizations, which under suitable parameter scaling leads to a form of “nested feature-learning,” whereby finetuning extracts salient weights from those learned by the pretrained model. Motivated by this observation, a heuristic of scaling down pretraining model parameters is suggested.

Experiments with shallow diagonal linear neural networks and ReLU networks corroborate the theoretical analysis.

### Strengths
The implicit regularization of finetuning and multi-task learning is a timely subject, given the popularity of these paradigms in practice compared to their limited formal understanding. Furthermore, despite their simplicity, two-layer diagonal linear networks exhibit non-trivial optimization dynamics, and have therefore been the focus of numerous studies. As such, I believe there is potential in investigating the implicit regularization brought forth by finetuning and multi-task learning for these models. 

Unfortunately, the paper suffers from major issues in terms of novelty and significance of its contributions, as well as clarity of presentation. I therefore believe that it falls below the bar of acceptance. My concerns are specified in the weaknesses portion of the review below.

### Weaknesses
 **Novelty and Significance:** The main contributions of Sections 4.1 and 4.2 are slight variations of known results. In particular, the characterization for the finetuning setting (Section 4.1) is a slight variation of Theorem 1 in [1], and the characterization for multi-task learning (Section 4.2) is a slight variation of Theorem 2 in [2]. Thus, beyond existing knowledge, the paper mostly provides interpretations of the sparsity inducing implicit regularization for diagonal linear neural networks. Such interpretations can be valuable, yet the setting considered is quite limited:

1. The analysis disregards the role of the auxiliary task data and objective, which are crucial in practice. In fact, the considered multi-task setting is equivalent to a single task with multiple outputs. Hence, the analysis inherently cannot provide insight as to how the implicit regularization of training with auxiliary tasks differs from single task training. Due to the substantial overlap between the results of Section 4 and prior work, I suggest as a promising direction forward to investigate how the effects of auxiliary task data and objective come into play.

2. The comparison between the implicit regularization of finetuning and multi-task learning is not an “apples to apples” comparison. For finetuning, the implicit regularizer is derived for gradient flow with the square loss, whereas for multi-task learning the L2 representation cost is considered, although it is not clear whether gradient descent/flow indeed leads to minimal L2 norm solutions in this case.

With regards to the empirical evaluation:

1. I find the empirical demonstration of the proposed heuristic (scaling down weights) to be insufficient. The evaluation includes only a single model (ResNet18) and a single dataset (variant of CIFAR100) with an oddly small number of training samples. Although the paper is mostly of theoretical nature, I still believe this does not meet the extent of evaluation expected when proposing a practical guideline.

2. Claims of an implicit regularization towards sparsity are measured in experiments only through sample complexity, as observed when plotting the loss against the number of samples. It would be more informative to measure the sparsity levels directly.

**Presentation:** The presentation severely lacks clarity. Claims are made without laying out their exact statements and under which assumptions they are proven. Specifically, in Section 4.1 it is not specified what the minimized objective is, what the optimization algorithm is, nor what the auxiliary weights stand for and how they are obtained. The appendix does not provide much clarity either, though after close examination it seems to prove a slight variation of Theorem 1 in Azulay et al. 2021 for the implicit regularization of diagonal linear networks optimized with gradient flow from a certain initialization.

**Additional Comments:**

1. A contributing factor to the lack of clarity is the use of undefined terminology, whose meaning is not obvious (at least to me). For example, what does “read-out weights” refer to in the context of diagonal linear neural networks? Furthermore, what does “linear probing” refer to? An additional fully connected linear layer? Training only $w^2_+$ and $w^2_-$?

2. In my opinion, the use of “feature-learning” is unconventional and can be misleading. Feature learning typically refers to learned representations based on which prediction is done, whereas here it refers to sparsity patterns in the weights of a linear predictor. Linear predictors are usually the prime example of a model that does not have a feature learning component. Perhaps “feature selection” is a more suitable term?

3. The reference to Lyu & Li, 2020 at the beginning of Section 4.2 is imprecise. They showed that for homogeneous neural networks, which include diagonal linear networks, convergence is in direction to a KKT point of a max-margin objective. This does not necessarily imply convergence to the exact minimizer. Theorem 4 in [3] does prove it though under some technical conditions.

### Questions
\-

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
