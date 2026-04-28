# Efficient Gradient Estimation via Adaptive and Importance Sampling

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 3

## Abstract
Machine learning problems rely heavily on stochastic gradient descent (SGD) for optimization. The effectiveness of SGD is contingent upon accurately estimating gradients from a mini-batch of data samples. Instead of the commonly used uniform sampling, adaptive or importance sampling reduces noise in gradient estimation by forming mini-batches that prioritize crucial data points. Previous research has suggested that data points should be selected with probabilities proportional to their gradient norm. Nevertheless, existing algorithms have struggled to efficiently integrate importance sampling into machine learning frameworks.
In this work, we make two contributions. First, we present an algorithm that can incorporate existing importance functions into our framework. Second, we propose a simplified importance function that relies solely on the loss gradient of the output layer. By leveraging our proposed gradient estimation techniques, we observe improved convergence in classification and regression tasks with minimal computational overhead. We validate the effectiveness of our adaptive and importance-sampling approach on image and point-cloud datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors proposes an sampling strategy that depends on gradient of the loss for training machine learning problems, with both importance and adaptive sampling. It was tested on several classification as well as regression tasks with results that look promising. It demonstrates that by focusing more attention to samples with critical training information, one might be able to speed up convergence without adding computational cost.

### Strengths
1. I especially like the visualization of the importance sampling in Figure 1, where 800 data-point are presented with a transparency proportional to their weight according to our method for a classification task. It clearly shows how the algorithm works intuitively.

### Weaknesses
The paper can be improved in several ways:

1. The way the authors cite the references sometimes is confusing. It is hard to distinguish the main context from the reference. Please consider use paper numbers only or use parenthesis version.

2. The paper lacks discussions of related paper. For example, https://arxiv.org/pdf/2104.13114.pdf also considers the importance sampling problem by sampling data points proportionally to the loss, instead of norm of gradient.

For another example, https://arxiv.org/pdf/2306.10728.pdf also proposes adaptively sampling methods for dynamically selecting data points for mini-batch. I'd love to see the authors discussed more about these papers.

3. I'd like to see the authors elaborate more on the algorithms. For example, ComputeSampleImportance is mentioned in line 13 without further explained in this section.

4. There seem to be many typos for the math in the paper. For example,

$$\mathcal{L}_{\text {cross-ent }}=-\sum_i y_i \log s_i,$$
 where $s_i=\frac{\exp \left(m\left(x_i, \theta\right)_l\right)}{\sum_l^J \exp \left(m\left(x_i, \theta\right)_l\right)}$. Please correct the subscripts from (8) - (11).

For another example, the explanation after (4) is a bit confusing: where $m\left(x_i, \theta\right)$ is an output layer, $x$ is the input data and $J$ means the number of classes. Try to directly use $x_i$ instead of $x$.

One more example, why does both $x_i$ and $x$ exist in (6)?

$$\left\|\frac{\partial \mathcal{L}(x)}{\partial x}\right\|=\left\|\frac{\partial \mathcal{L}(x)}{\partial m\left(x_i, \theta\right)} \cdot \frac{\partial m\left(x_i, \theta\right)}{\partial x}\right\|$$

5. It is hard to tell the algorithm performance differences for some figures. For example, in Figure 5 (left), the authors claim that at equal epochs (left), our methods (Ours IS & AS) show improvements compared to LOW Santiago et al. (2021) and DLIS weights. It is really invisible to see the difference. The authors may consider plotting the log scale results.

6. There is no reference number to the figure in page 9.

### Questions
1. I feel a bit confused in Ours IS vs Ours AS. Does Ours IS mean that you set $w(x) =1 / p(x)$  and Ours AS mean that you set$w(x) =1 / N$? If so, why do you claim your adaptive sampling approach subsumes the adaptive weighting of Santiago et al. in page 3? I think they are different because Ours AS just do the sampling with non-uniform distribution and there is no weighting.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a gradient expectation estimation based on adaptive sampling and samples weighting approach. The presented framework is flexible to any function calculating the samples importance. However, the authors propose an efficient importance function based on the loss gradient of the output layer.

### Strengths
The presented approach is interesting and is sound. 
The overhead required for calculating the weights for the resampling is relatively low making the approach attractive given the shown gain in the overall training time.

### Weaknesses
The title of the paper sounds problematic from grammatical point of view as the word adaptive is an adjective unlike importance. 
While the sampling scheme is well founded, it seems that the presented approach can suffer from overfitting issues. The authors explicitly propose to add an \epsilon to the value of the importance to avoid focusing on a small set of the data points. This suggests a potential instability in the sampling distribution, where a few data points could dominate the gradient estimation if the epsilon is not carefully tuned. The method's reliance on a memory of data importance, proportional to the dataset size, also raises concerns about scalability and applicability to streaming data scenarios. The need to store and update this memory introduces a computational overhead that may not be negligible, especially for large datasets. Furthermore, the non-uniform data sampling, while potentially beneficial for convergence, could lead to slower data loading times due to non-contiguous memory access patterns.

While the presented experiments confirm faster convergence in most cases, it is relatively limited and further discussion on potential drawbacks of the proposed sampling, e.g., robustness to label noise and generalization would have been helpful. The lack of analysis on how the method performs under noisy label conditions is a significant omission. The authors make reference to a paper they presented earlier which should have been avoided given the double blind review process: "Recently, We propose an efficient algorithm and an importance function which when used for importance or adaptive sampling, shows significant improvements."

### Questions
What is meant with the sentence: In this method, as outlined in eq. (3), each data point’s weight, denoted as w(xi), remains constant at N. ?

Beyond the weight calculation overhead what are limitations and potential drawbacks of the proposed method?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Post rebuttal: I'm raising my score to acceptance. The paper can be strengthened by some theoretical backing, as the paper currently reads that it is a cheaper approximation to Katharopoulous and Fleuret, but doesn't describe _what_ the method actually models. 

-----------------------

The paper unifies approaches on importance and adaptive sampling. For this the paper proposes a simple importance function that is logit gradients for which there exists a close form expression for classification networks. They keep track of the importances of the samples across epochs and use that importance to sample the data and compute the weight function $w(x)$. 
On multiple varieties of problems like image Classification, image regression, point set classification they show that they converge faster than prior works on importance sampling and adaptive sampling.

### Strengths
The paper is well motivated and placed within the literature. The method is intuitive, and the paper is generally written well (see comments below). The biggest strength is the experiments where the authors show wall-clock speedups of their algorithm, instead of some hypothetical quantity. The experiments cover the usual set of benchmarks.

### Weaknesses
The only issue I see is with the specific motivation of the proposed importance function. I had a very tough time parsing the text below Eq 5 on page 5. For eg: The gradient norm in eq has two quantities $x$ and $x_i$. Also, the lipschitz constant is written as $l_{m(x, \theta)}$ indicating that the constant of the network is input dependent. Is this intended? Additionally, this bound on the gradients is not informative about the chosen importance function. Eqn 6 makes it seem that the proposed importance function is valid only for Lipschitz neural networks. Is my understanding correct? If so, the proposed method is limited in its applicability. 

A discussion on the theoretical properties of the importance function is needed: why is this importance function better than the one in DLIS? In the absence of this, it is tough to attribute the successes of this method. For eg: the way the importances are tracked in Algorithm1 (Lines 13, 14) and the subsequent sampling in Line 7 (instead of the more involved update process in DLIS paper) may be more "implementation friendly" and thus the noticed performance improvements. 

Finally, the experiments are limited in the range of experiments covered. The paper covers experiments on MLPs and CNNS. It would interesting to see how the method performs on modern transformers.

### Questions
In addition to the comments on the importance function, I have the following questions:
* What is cost of first epoch to estimate a starting importance function? Does that mean that you run a standard SGD loop and track $q$ without any other sampling? 
* What is value of $\alpha$ used in Eqn 7? How important is it? 
* Why is the DLIS performance on Oxford flowers getting worse after a point? What is sparsity of dataset? 
* Last figure on page : there is a reference to "difference between various weighting strategies and the full gradient norm": What is full gradient norm here? 

## Minor
* In page 2: paragraph on importance sampling: what is "inherently multivariate" mean? 
* Same as above: What is good compromise between optimization quality across all dimensions simultaneously mean? What dimensions? 
* The next para, last sentence is incomplete: `Recently, We....`
* Page 3. $N$ is used before it is introduced. Change to $|\Omega|$. 
* Last figure on page 9 is uncaptioned. 

Overall, I think its a very interesting contribution with good practical use. If the authors can provide a convincing rebuttal, I would be willing to raise my scores.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Rather than the usual uniform sampling for stochastic gradient descent, this paper considers adaptive and importance sampling to perform variance reduction by attributing higher sampling probabilities to more important data points. The challenge with implementing adaptive and importance sampling in practice is that computing or even approximating the optimal sampling probabilities for importance sampling essentially requires computing the full gradient, at which point one might as well perform the full gradient descent. 

This paper proposes an algorithm that approximates the probabilities for adaptive/importance sampling and then considers a specific approach that uses the cross-entropy loss gradient, e.g., for the purposes of classification tasks.

### Strengths
+ Variance reduction in stochastic gradient descent is an important research direction with significant implications and high relevance to the ICLR community.

+ The proposed algorithm improves on uniform sampling in the provided experiments.

+ Experiments conducted on a large number of datasets.

### Weaknesses
 - Sufficient details have not been provided to formally understand the guarantees of the subroutines in Algorithm 1, such as ComputeImportanceSampling. The description of this subroutine is too abstract, making it difficult to assess its computational complexity and impact on the overall algorithm's performance. For instance, it's not clear what specific operations are performed within this subroutine, and how these operations scale with the size of the dataset or the dimensionality of the input.

- No convergence analysis is provided for Algorithm 1 and thus it is difficult to ascertain under what conditions the importance sampling probabilities can be quickly approximated. Without a formal convergence proof, it's unclear whether the proposed method will consistently converge to a good solution, or if it might get stuck in a suboptimal region. Furthermore, the rate of convergence is also unknown, making it difficult to compare the proposed method with other optimization techniques. The lack of theoretical guarantees makes it challenging to understand the limitations of the approach.

- It is not clear to me what the general framework in Section 4 is proposing, perhaps additional pseudocode would be helpful. The description of the framework is too high-level, and it's not clear how it can be applied to different loss functions and network architectures. It would be helpful to provide a more concrete example of how the framework can be used in practice, including the specific steps involved in computing the importance sampling probabilities for a given task. The connection between the analytical derivation for cross-entropy loss and the generalization to regression tasks is not clearly explained.

- There are a large number of popular methods for either acceleration or variance reduction for SGD that should be compared for a thorough empirical evaluation (for instance, any number of the references in the related work section). The experimental evaluation is not comprehensive enough, and it is not clear how the proposed method compares to other state-of-the-art techniques. For instance, methods like Adam or variants of stochastic gradient descent with momentum could provide a more robust baseline for comparison. The current evaluation is limited to a few datasets and does not explore the performance of the proposed method under different conditions.

### Questions
- Is there any analysis you can provide for convergence?

- After the approximate probabilities for importance sampling are obtained, how does the algorithm efficiently use these values to sample a data point? That is, are the sampling probabilities organized into a data structure of some sort that maps each real number (possibly implicitly through a set of intervals) to a specific data point?

Update: I acknowledge receipt of the author updates through the discussion phase. I will maintain my score for now but I appreciate the efforts made to improve the quality of the paper.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
