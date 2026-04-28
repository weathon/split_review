# Just How Flexible are Neural Networks in Practice?

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6

## Abstract
It is widely believed that a neural network can fit a training set containing at least as many samples as it has parameters, underpinning notions of \emph{overparameterized} and \emph{underparameterized} models.  In practice, however, we only find solutions accessible via our training procedure, including the optimizer and regularizers, limiting flexibility.  Moreover, the exact parameterization of the function class, built into an architecture, shapes its loss surface and impacts the minima we find. In this work, we examine the ability of neural networks to fit data in practice.  Our findings indicate that: (1) standard optimizers find minima where the model can only fit training sets with significantly fewer samples than it has parameters; (2) convolutional networks are more parameter-efficient than MLPs and ViTs, even on randomly labeled data; (3) while stochastic training is thought to have a regularizing effect, SGD actually finds minima that fit more training data than full-batch gradient descent; (4) the difference in capacity to fit correctly labeled and incorrectly labeled samples can be predictive of generalization; (5) ReLU activation functions result in finding minima that fit more data despite being designed to avoid vanishing and exploding gradients in deep architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces the notion of Empirical Data Capacity (EDC) and study empirically how it behaves across different architectures, optimizers, and data distributions, among others. Informally, EDC is the largest subset of training data that can be correctly classified/interpolated by the neural network when trained without augmentation. Unlike the complexity of the hypothesis space, such as the VC dimension, EDC factors into account the entire training protocol. Borrowing intuition from linear classifiers, it extends the notion of parameter count. 

The authors present many interesting findings and insightful discussions. For instance, the authors find that the difference between EDC on true labels and EDC on random labels to be a strong predictor of generalization ($<-0.8$ Pearson correlation coefficient). They also find that the scaling recipe in EfficientNet also improves EDC. Also, more classes make fitting data harder with semantic labels but easier with random ones, and so on. Overall I think it's a good empirical study but would benefit a lot from a more precise discussion/explanation in several places.

### Strengths
- The paper is well-written overall and easy to follow. The breadth of the analysis is commendable. The paper additionally presents many interesting results.

### Weaknesses
 - First, the notion of EDC is identical to the Effective Model Complexity (Nakkiran, et al. 2021), which the authors cite but do not really compare with. Both correspond to the largest subset of training data that is interpolated by the model. However, the authors exercise caution when using it (e.g. by checking the norm of the gradients and the flatness of the loss curve, etc) to make sure that the models are not undertrained. I would recommend that the authors refrain from claiming novelty in the notion of EDC and simply center their contribution around the empirical investigation of the Effective Model Complexity, instead.

- The second primary weakness in my opinion is the lack of clarity about the experimental details in a few places.
  * When comparing different architectures such as CNNs and ViTs, how did the authors ensure that the architectures are compared fairly? For example, there is no mention of the number of parameters used in each architecture. Even if those architectures share the same parameter count, the shape of the architecture can have a big impact as the authors themselves study for CNNs. It's not clear if one can conclude, for example, that CNNs are more parameter efficient than ViTs. There aren't enough details in the paper for the reader.
  * The authors mention repeatedly that ReLU improves EDC even though they "were introduced to neural networks to prevent vanishing and exploding gradients." I do not see the discrepancy here. ReLU were introduced to prevent training instability issues so I would expect ReLU to improve training and improve EDC as a result. It is unclear why the authors highlight that the impact of ReLU on EDC is surprising.
  * When the authors compare different datasets, like CIFAR10/100, MNIST, and ImageNet, they use these results to argue for the impact of the input distribution. However, those datasets have different number of classes. One way to fix that issue is to fix the number of random labels in all datasets. There is no discussion of this in the paper and it seems that the authors kept the label space unchanged. The problem is that it is not clear (again) when the input distribution matters much when accounting for the differences in the number of classes.
  * In many figures, the authors average log(EDC). Is it reasonable to average them? Wouldn't the average EDC be dominated by what happens to large models? Perhaps it would be better to report the raw results without averaging.
 
- Some minor comments: 
  * The author should provide precise definitions of some of the terms they use. For example, what is "parameter-efficient"? My understanding is that it is EDC divided by the parameter count. Is this the case?
  * The figures are not presented in the same order they appear in the main text. 
  * Figure 2(b) is very difficult to understand. Are the authors here scaling a single dimension at a time using EfficientNet scaling recipe and reporting the average results?
  * Page 6: typo in "we three neural network"
  * It would be interesting to see of the scaling laws derived for ViT [1] would also increase EDC, similar to the analysis that was done on EfficientNet.

### Questions
- Can you please clarify how the comparison across different architectures was done? Did you ensure that all architectures have the same size? How were the shapes selected? Are they based on some standard shapes, such as those used in the original ViT and EfficientNet papers? What about MLP?
- When using random labels, did you fix the label space in all datasets (e.g. binary classification) or was the same label space used in each dataset (e.g. 10 classes in CIFAR10 but 100 classes in CIFAR100)?
- Can you please clarify Figure 2(b)?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the practical data-fitting capabilities of neural networks, challenging the widely held belief that a neural network can fit a training set as long as it has a sufficient number of parameters. The authors find that the training procedure, including the optimizer and regularizers, as well as the network's specific parameterization and architecture, significantly influence the model's ability to fit data.

### Strengths
I think the paper attempts to answer an interesting direction of understanding what makes Neural Networks work in practice an interesting direction of research.

### Weaknesses
The paper could benefit from deeper theoretical exploration. While the metric's motivation isn't thoroughly convincing, there's an intriguing mention of PAC-Bayes and VC dimension. It would be valuable to elaborate on how their selected measure aligns with the current theory. While I appreciate the importance of experiment-driven papers, it appears that the conclusions were drawn post-results, rather than being based on predefined hypotheses derived from established theory. The relevance of model architectures to random labels remains unclear, and the frequent references to the linear model are perplexing, especially given that large parameterized neural networks don't typically align with traditional models—consider the double descent phenomenon and their tendency to yield smoother functions [1]. Additionally, section 5's presentation could be improved; its current format reads like a data dump rather than a cohesive exploration of the central theme of 'flexibility'.

### Questions
-	The description of the EDC and how it relates to quantifying capacity seems a little bit loose I am not sure why it is a good metric for capacity. Furthermore, it would be good if you could split out step by step the computation. 
-	Could you clearly define what you mean by flexibility or an intuitive understanding I found it hard to find a clear definition of what you mean.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the flexibility of neural networks, which is defined as the maximum number of training samples that a neural network can accurately classify under sufficient training. The paper analyzes through experiments flexibility as a function of the optimizer, neural network architecture, as well as the dataset. On top of these factors, the paper also considers a large number of variations such as regularization, scaling law, random features and labels, and activation functions. Based on the experimental results, the paper makes several logical conclusions that summarize their findings.

### Strengths
1. The topic studied in this paper differs from previous works and has great practical implications. In particular, previous works studying expressiveness solely consider the impact of the number of parameters and the architecture. On the contrary, in this paper, a more fine-grained (and thus more practical) analysis is performed by considering more decisive factors in the training.

2. Some conclusions of the paper are quite interesting. For instance, they found that i). there is a correlation between the increase in EDC going from random labels to semantic labels, and the generalization ability, ii). neural networks are worse than linear models at fitting random labels, and iii). ReLU activations result in higher flexibility though originally designed to mitigate vanishing and exploding gradients, etc.

### Weaknesses
1. The measurement of EDC may have some flaws:

    a). The paper takes the strategy of gradually increasing the number of training samples. However, the paper does not discuss how many different trials are run for each setting, and no error bars are plotted. In the very extreme case, there can be some unlucky bad initialization of the neural network that prevented a model from fitting training samples thus causing the EDC to stop growing for that setting. However, this rare case may not be representative of what happens in most cases.

    b). I am not sure why the paper performs the sanity check that each training reached a minimum rather than a saddle point. Since an important consideration of the paper is to evaluate EDC based on the performance of different optimizers, whether the optimizer stopped at a local minimum, global minimum, or saddle points should be a property of the optimizer and it should not be influenced by the experiment design.

2. The paper stops at observation at the surface and does not investigate deeper reasons. For instance, while it is interesting to observe that neural networks are worse than linear models at fitting random labels, the paper should really investigate what is the reason behind such a phenomenon, and potentially answer the question of whether we should really care about this property of NN and linear models in practice. This issue also holds for other conclusions of the paper.

3. Some conclusions of the paper are questionable:

    a). ”Flexibility across modalities”. Is the result that tabular datasets have larger EDC a consequence of simpler tasks?

    b). ”CNN has larger EDC than MLP”. It seems that the experiments are performed only on vision tasks, which makes the conclusion trivial. Does the same result hold on other tasks?

4. Experimental settings are questionable:

    a). I am more sure, when investigating the influence of architecture and over-parameterization, what optimizer settings are the paper using. Is the paper fixing an optimizer, or is the paper trying all optimizers and picking the best-performing one?

    b). Regarding the experiment of scaling up the image sizes, is the filter size also scaled up accordingly?

5. The fact that labels are fit to 100% accuracy may affect the conclusion of some experiments related to generalization since there can be outliers that negatively affect the generalization ability.

### Questions
Other than the question I raised in the ”Weaknesses” section, I also want to ask the following: from Figure 1 (right) we see that a larger EDC improvement implies a better generalization ability. Figure 2(b) shows that scaling width under a fixed over-parameterization results in the largest EDC improvement. Do these two results imply that scaling the width leads to the best generalization?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
