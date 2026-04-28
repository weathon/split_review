# RelChaNet: Neural Network Feature Selection using Relative Change Scores

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
There is an ongoing effort to develop feature selection algorithms to improve interpretability, reduce computational resources, and minimize overfitting in predictive models. Neural networks stand out as architectures on which to build feature selection methods, and recently, neuron pruning and regrowth have emerged from the sparse neural network literature as promising new tools.
We introduce RelChaNet, a novel and lightweight feature selection algorithm that uses neuron pruning and regrowth in the input layer of a dense neural network. For neuron pruning, a gradient sum metric measures the relative change induced in a network after a feature enters, while neurons are randomly regrown. We also propose an extension that adapts the size of the input layer at runtime.
Extensive experiments on nine different datasets show that our approach generally outperforms the current state-of-the-art methods, and in particular improves the average accuracy by 2\% on the MNIST dataset.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces RelChaNet, a novel feature selection algorithm leveraging neural networks. Key innovations include neuron pruning and regrowth mechanisms focused on the input layer. The pruning process uses a "relative change score", measuring the impact each feature has on the network's structure and function after its inclusion. Unique to RelChaNet is the flexibility to adapt input layer size dynamically during runtime, enhancing the algorithm's adaptability to varied datasets.

The method was benchmarked against other state-of-the-art feature selection algorithms on nine datasets, showing superior performance in terms of predictive accuracy, especially on datasets with more samples than features, achieving a 2% improvement on MNIST. However, RelChaNet exhibits comparable performance on datasets with more features than samples. Notably, it also offers competitive computational efficiency, making it a robust alternative for neural network-based feature selection tasks

### Strengths
- Given the ever-increasing computational demand in the deep learning field, RelChaNet addresses the critical need to reduce this load by proposing a novel deep learning feature selection method.
- The authors conduct experiments across a broad range of competing feature selection methods and a diverse set of data domains.
- RelChaNet (flex) demonstrates strong performance and robustness by outperforming other evaluated methods on 7 out of 9 datasets.

### Weaknesses
The primary weakness of this paper, as I see it, is that it evaluates RelChaNet on datasets that do not intrinsically demand the non-linear feature selection capabilities that deep learning methods like RelChaNet are designed to offer. For example, MNIST is a well-understood dataset where simpler, linear methods often perform exceptionally well. Linear methods like PCA, for instance, achieve 98.0% accuracy on MNIST with K=25 features when using the SVC downstream learner, notably outperforming RelChaNet’s ~93% accuracy. This raises questions about whether RelChaNet’s deep learning-based approach is meaningful for such datasets and whether it would generalize well to more complex, non-linear datasets (e.g., CIFAR-10, Imagenet).

To demonstrate the effectiveness of RelChaNet, the evaluation should focus on datasets with complex, non-linear relationships where simpler methods struggle.

### Questions
How do RelChaNet and other competing feature selection methods perform on complex datasets such as CIFAR-10, CIFAR-100, and Imagenet?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new algorithm for feature selection using Multi Layer Perceptron and a prune and regrowth strategy for the neurons from the input layer. The empirical evaluation shows that the proposed method outperforms several state-of-the-art baselines in a substantial number of scenarios.

### Strengths
S1) The proposed method is novel.

S2) Random neuron regrowth likely helps reduce bias in the final ranking of input features.

S3) The proposed method obtains a beneficial performance improvement on top of the state-of-the-art as illustrated on several datasets.

### Weaknesses
W1) The paper is somewhat difficult to read. Particularly, Section 3 is a bit hard to read due to too much text and details. The description of the algorithm lacks a clear, step-by-step breakdown, making it challenging to follow the logic of the neuron pruning and regrowth process. The lack of mathematical formalism in the main text makes it hard to understand the exact operations performed on the input layer and how the feature selection is achieved.

W2) The paper needs careful proofreading. Some statements are unclear or inaccurately phrased. E.g., lines 44-45, Mocanu et al. 2018, Evci et al. 2020, employed connections pruning and regrow directly, while neuron pruning, and regrowth become rather an indirect output; lines 124 -> this is rather structured sparsity. The distinction between weight pruning and neuron pruning is not clearly articulated, leading to confusion about the novelty of the approach. The description of how neurons are regrown is vague, and it is unclear how the random selection of neurons for regrowth is implemented and what impact it has on the final feature selection.

### Questions
Q1) Can you try to enhance Section 3 by describing it with a proper mathematical formalism?

Q2) Which is better the main algorithm proposed in Section 3 or its extension from Section 3.1? Proposing two new algorithms which perform relatively similar is confusing.

Q3) Is it the case that the proposed approach underperforms on the widest dataset (about 50k features) because the random growth needs more training epochs to explore this very large search space? Did you try to train longer in a systematic manner for this dataset? Perhaps by creating an artificial dataset you may be able to perform a more granular analysis on how well the proposed method scales with the number of features and samples?

Q4) The computational analyze from Section 4.2 seems a bit forced. Probably, it would be fairer to try using relatively similar network sizes for all methods and report of course also their accuracies. Also, the sparse networks are really sparse or simulated with binary masks?

Q5) As far I was able to understand the work is about supervised feature selection. Can you please clarify?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel feature selection method designed for dense neural networks. RelChaNet leverages neuron pruning and random regrowth at the input layer, selecting features based on a relative change score calculated from gradient sums over multiple mini-batches. Experiments across nine datasets demonstrate that RelChaNet generally outperforms existing feature selection techniques, particularly enhancing accuracy by 2% on MNIST. The paper also introduces an adaptive extension, “RelChaNet flex,” which adjusts the input layer size dynamically based on validation loss trends.

### Strengths
The paper presents extensive results across diverse datasets, showing superior performance over baseline feature selection methods and emphasizing improvements in interpretability and computational efficiency.

### Weaknesses
 - The applicability of this method is uncertain. In some cases, neurons may exhibit monosemanticity (e.g., in a neural network performing simple arithmetic tasks, where each neuron has a clear, isolated role). However, in other cases, groups of neurons may collectively capture shared or complex features. This method seems most effective when monosemanticity is prevalent in the dataset, and it may struggle with datasets that contain intricate concepts requiring shared neuron activation.
- The experiments focus primarily on datasets with more cases than features (“long” datasets). To strengthen the evaluation, RelChaNet should be tested on additional “wide” datasets to assess its performance on high-dimensional data. Additionally, the current experiments use relatively simple datasets. Expanding the evaluation to include more complex datasets, such as ImageNet, would help demonstrate the method’s robustness in handling challenging data.
- The paper lacks a theoretical explanation for the random neuron regrowth process. Without a clear rationale, the consistency and predictability of the feature selection results may be affected.

### Questions
- How does RelChaNet perform on very high-dimensional data with more features than samples? Although the algorithm shows effectiveness on “long” datasets, further validation on “wide” datasets would provide a more complete view of its generalizability.
- What impact does the randomness in neuron regrowth have on feature selection stability? Since neurons are randomly regrown, it would be useful to understand how this randomness affects the repeatability of selected features and model accuracy.
- How does the algorithm’s computational efficiency compare with other pruning-based feature selection methods? Given its relative complexity, a comparison of runtime across similar algorithms would be helpful in evaluating RelChaNet’s scalability.
- Could hyperparameters like cratio and nmb be optimized for specific types of datasets? Insights into parameter tuning would provide valuable guidance for applying RelChaNet in various contexts, especially for practitioners without prior knowledge of optimal settings.

### Soundness
2

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
The primary focus of this paper is on feature selection algorithms in neural networks. Thus they  introduce RelChaNet, a feature selection algorithm that uses neuron pruning and regrowth in the input layer of a dense neural network.

### Strengths
The method proposed in this paper is very simple and easy to implement.

### Weaknesses
1、The solutions in this paper are almost identical to methods like dropout, pruning, and regularization in neural networks to prevent overfitting, making it difficult to identify the novelty of the proposed approach.
2、The effectiveness of the proposed method is also not better than the state-of-the-art (SOTA) results.
3、The threshold C_ratio  in the feature selection algorithm lacks theoretical guidance or a defined method for setting it.
4、The quality of English writing in the paper needs improvement.
5、The paper lacks an evaluation and summary of related work, as well as an explanation of the challenges present in the problem.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2
