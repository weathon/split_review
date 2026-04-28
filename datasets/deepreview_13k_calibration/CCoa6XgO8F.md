# A Defense of One-Step Learning: Examining Single-Batch Distillations

- Decision: Reject
- Avg Score: 3.80
- Scores: 5, 3, 5, 3, 3

## Abstract
Dataset distillation produces a compressed synthetic dataset that approximates a large dataset or other learning task. A model can be trained on a distillation in a single gradient descent step. Conventional wisdom suggests that single-step learning is not generalizable and should yield poor performance; yet, distillation defies these expectations with good approximations of full direct-task training for a large distribution of models. In order to understand how distilled datasets can perform one-shot learning, we examine the distilled data instances and the cost surfaces produced by the distilled datasets. We demonstrate that the distilled dataset not only mimics features of the true dataset but also produces cost surfaces such that one-step training leads models from the initialization space into local minima of the true task's cost surface. This shows how one-step learning's counter-intuitive success is not only reasonable but also the expected outcome of dataset distillation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a study that inspects the loss surfaces of distilled datasets. The authors show the results on various tasks, including Atari Centipede and standard image benchmarks.

### Strengths
+ The paper is easy to follow and understand
+ The authors performed relatively though coverage on different domains.

### Weaknesses
 - I'm not sure what the paper is contributing. The distilled datasets can train a model that performs similarly, the results itself hint the loss surface probably shares similar local minima.

- A lot of related works are missing. [1] analyzes the DD task in depth. [2] made multi-step BPTT work in DD. One easy question to ask and study further is, one-step BPTT (used in this paper) underperforms multi-step BPTT[2], what has been changed in the loss landscape when number of steps is increased?

### Questions
See above. I'm not sure what this paper is contributing and the current version seems to be not sufficient. Giving deeper understanding of DD is interesting and the authors should consider further complete the work to submit to another future venue.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This article explores the effectiveness of one-step learning by analyzing distilled data instances and cost surfaces. The experiments demonstrate that the distilled dataset not only replicates the characteristics of the real dataset but also generates suitable cost surfaces, enabling one-step training to guide the model from the initialization space to a local minimum of the actual task cost surface.

### Strengths
1. The experiments encompass a variety of benchmark tasks, including image recognition and reinforcement learning.
2. The article presents a task-agnostic distillation algorithm (Algorithm 1) and thoroughly details the various steps, parameter settings, and selection of loss functions relevant to different tasks in the distillation process. This clarity aids readers in understanding and replicating the experiments.

### Weaknesses
1. **Theoretical Depth**: While the effectiveness of the distilled dataset is demonstrated experimentally, the theoretical framework explaining why an appropriate cost surface emerges during the distillation process is somewhat lacking. The conclusions largely rely on empirical observations. The article primarily documents experimental details and phenomena, missing an in-depth analysis that could better inform the design and application of the methods discussed.
2. **Generality of Experimental Validation**: The authors have chosen algorithms and datasets that are too simplistic and limited. The method selected by the authors targets distillation with single-step training, as they mentioned, single-step learning is the expected outcome for distilling these types of datasets, but what about distillation methods for other categories? There are many new related meta-learning algorithms, as well as many methods outside of meta-learning (e.g., trajectory matching).

### Questions
1. The observations of the cost surface and loss curvature have also been observed, analyzed, and used as a basis for proposing improvement methods in the work of others[1]. They conducted a more detailed analysis of loss curvature. Have you combined your analysis with theirs?
2. The current experiments are too simplistic. To my knowledge, there are several advanced algorithms for dataset distillation that are not very computationally expensive, and these experiments are entirely affordable. Can the authors conduct experiments on more recent works and larger datasets?

[1] Shin, Seungjae, et al. "Loss-curvature matching for dataset selection and condensation.”

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work explores how dataset distillation enables models to achieve effective one-shot learning from reinforcement learning perspective. Despite conventional belief that single-step learning would not generalize well and would perform poorly, distilled datasets allow models to closely approximate the results of direct-task training across a wide range of model architectures. The authors analyze both the distilled data instances and the cost surfaces they generate, finding that the distilled datasets not only replicate features of the original data but also shape cost surfaces that guide models from their initial states into local minima of the true task’s cost surface.

### Strengths
1. The paper provides an in-depth examination of cost surfaces generated by distilled datasets, offering a valuable perspective on how dataset distillation guides models to local minima. By analyzing the distilled instances, the authors demonstrate that the compressed data retains critical task-relevant features, which helps improve interpretability, especially for simpler tasks.

2. To the best of the knowledge, this is the first paper that investigates the dataset distillation in reinforcement learning scenario.

### Weaknesses
 - While the cost surfaces generated by distillations show promising results, the paper does not fully address potential scalability issues when applied to larger models or datasets, which could present computational challenges. Specifically, the paper lacks a discussion on the computational complexity of generating and analyzing these cost surfaces, especially as the dimensionality of the model parameters and the size of the distilled dataset increase. This is a critical concern, as the practical applicability of the method hinges on its ability to scale to realistic scenarios. I suggest the authors provide more theoretical verification for the claim.
- The study relies on one method of distillation, but an evaluation of alternative distillation methods could provide a broader understanding of how different techniques impact cost surfaces and model performance. Methods like DATM, SDC, IDC should also be considered as baselines for further exploration. The current analysis does not explore how different distillation objectives or architectures might influence the learned cost surfaces, which is a significant gap in understanding the generalizability of the findings [1,2,3].
- More complex datasets and benchmarks should also be considered. The experiments mainly focus on relatively simple datasets, such as MNIST and CIFAR-10, as well as cart-pole and Centipede environments. The paper could be strengthened by evaluating the method on more complex tasks, such as high-resolution image datasets or NLP tasks, to assess its scalability. The current evaluation does not sufficiently demonstrate the method's robustness and applicability to real-world problems, which often involve higher dimensional inputs and more intricate relationships.
- This paper does not use the correct ICLR template. Specifically, there is no ''Under review as a conference paper at ICLR 2025'' note in the paper.
- Minor: some notations are wrong. For example, in figure 1, the authors write T0, T_0, and also TO, which generate mistakes. I suggest the authors polish the notations and representation. In line 161, there is a unexpected + symbol.

### Questions
1. How does the proposed approach handle high-dimensional data, such as images with complex structures or datasets with numerous features? It would be beneficial to understand how the technique performs in such scenarios.
2. Given the success in various supervised and reinforcement learning tasks, could this method be extended to other domains, like natural language processing or time-series analysis?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper studies the performance of dataset distillation under the regime of one gradient update under the meta-model matching framework. The study shows that a single step gradient update distilled data can achieve decent task performance, and the distilled dataset having ideal properties with respect to the real data with similar data features and similar loss landscapes towards a specific local minima.

### Strengths
1. Since dataset distillation as a field right now is mostly empirical, the inner-workings on why it works is understudied. This work studies the loss landscape of the distilled data, which can provide important insights for better design of dataset distillation algorithms. 
2. The study on RL datasets cart-pole and centipede is interesting since most of dataset distillation works focuses on image recognition.
3. The paper demonstrate that distilling with one gradient step can achieve decent task performance on CIFAR-10 with accuracy of 28% using fewer than 1 image per class through soft-labeling.

### Weaknesses
1. It is unclear whether findings in this paper will translate to other distillation algorithms, and therefore, how it will fit in the existing body of research. While the paper demonstrates the ability to achieve decent performance with one-step gradient update, the performance is very subpar compared to other distillation algorithms such as BPTT [1], which achieves 49% with 10 examples, or Trajectory Matching [2], which achieves 46% with 10 examples. Specifically, the paper does not explore how the single-step distillation compares to multi-step approaches in terms of the properties of the distilled dataset, such as the diversity of the generated samples or the sharpness of the loss landscape around the learned minima. This makes it difficult to assess the practical relevance of the findings.
2. The method useful to justify why a solution is a local minima is not sound. Visualization through random vectors projection was originally designed to capture the non-convexity of the loss landscape and is insufficient for the understanding the optimization trajectory (section 7.1 of [3]). To better understand the optimization trajectory, visualization with PCA direction proposed in section 7.2 of [3] can be used. To quantitatively justify local minimum, one would have to reason about the sharpness (second derivative/Hessian) of the loss landscape [4]. The current analysis lacks rigor, as it does not provide any quantitative measure of the curvature of the loss landscape, which is crucial for determining whether the solution is indeed a local minimum and not just a saddle point or a flat region.

### Questions
1. Curious towards whether one-step learning generate datasets with different properties compared to multi-step learning approaches such as BPTT. Existing work shown that data distilled with popular algorithm seems to capture early trajectories rather than specific local minimum [1]. Curious whether authors have any insights on whether single-step learning changes this property?
2. One potential issue with visualization through random projections is that every solution will look like a minima with sufficiently large step size. What does the loss landscape look like for CIFAR-10 with smaller step sizes?

[1] Yang, William, et al. "What is Dataset Distillation Learning?." Forty-first International Conference on Machine Learning.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores and tries to understand why extreme dataset distillation, where the number of samples is less than the number of classes and synthetically generated, can be used to train a model and the model can achieve comparable accuracy to a model trained on the full dataset, in the setting where one step learning is used.  This is explored in the MNIST, CIFAR10 supervised image classification task as a well as the cart-pole and Centipede reinforcement learning tasks. The paper suggests that the reason why extreme dataset distillation can perform well is that the models go to a local minima that is in the same space as the full datasets minima. To explore this they plot the loss landscapes of a model trained on the full dataset and the model trained on the distilled dataset, and then compare there loss landscapes made with the distilled and full dataset.  Therefore the overlap between these landscapes, explains the success of extreme dataset distillation and why it is to be expected.

### Strengths
1. Introduction is very clear, engaging and the problem is very well motivated, pleasure to read.

2. Contributions are layout clearly.

3. Two different modalities explored Vision and Reinforcement Learning.

4. The idea to explore why single batch distillations works is very interesting.

### Weaknesses
## Review

### summary:
 This paper explores and tries to understand why extreme dataset distillation, where the number of samples is less than the number of classes and synthetically generated, can be used to train a model and the model can achieve comparable accuracy to a model trained on the full dataset, in the setting where one step learning is used.  This is explored in the MNIST, CIFAR10 supervised image classification task as a well as the cart-pole and Centipede reinforcement learning tasks. The paper suggests that the reason why extreme dataset distillation can perform well is that the models go to a local minima that is in the same space as the full datasets minima. To explore this they plot the loss landscapes of a model trained on the full dataset and the model trained on the distilled dataset, and then compare there loss landscapes made with the distilled and full dataset.  Therefore the overlap between these landscapes, explains the success of extreme dataset distillation and why it is to be expected.

### soundness:
 1

### presentation:
 2

### contribution:
 2

### strengths:
 1. Introduction is very clear, engaging and the problem is very well motivated, pleasure to read.

2. Contributions are layout clearly.

3. Two different modalities explored Vision and Reinforcement Learning.

4. The idea to explore why single batch distillations works is very interesting.

### weaknesses:
 **Clarity**

In the abstract line 13-14: "Conventional wisdom suggests that single-step learning is not generalisable and should yield poor performance" I don't think this to be the case, as this paper [1] shows that stochastic training is not required for generalisation but if one is to use single-step learning, i.e. full-batch gradient decent, with a lot of explicit regularisation can achieve comparable accuracy to using SGD on CIFAR10.  

In Section 2.2: DISTILLATIONS USED IN EXPERIMENTS, only the average result of training 1000 models is reported. Could you also report the standard deviation of these models? Also, why did you select 1000 instead of any other number? Why are the conventional trained models only trained once with the performance reported instead of averaged across 5 models? Why is train accuracy not reported?

**Qualitative Results:**

The comparison of the loss landscapes is poor as no metric is provided; even though the colours are the same, the values are not, making it hard to compare. To compare visually, ensure the images all use the exact colour mapping. With this, the idea of minima-matching needs to be adequately explained, other than stating the model achieves a low loss at/near the centre; however, these loss values are massively different. How are the loss landscapes the same or approximately matched?

**Mismatch between definition and result:**

Line 167-169: "While the CIFAR-10 distillation did not converge well, perhaps due to the model's risk of overfitting, the results demonstrate that even poor distillations function similarly to well-converged ones." There needs to be more evidence to support this claim; the MNIST case performs 14.1% worse than the entire dataset, suggesting that dataset distillation in this case will lead to poor-performing models regardless. I would go as far to say that this goes against the statement in the introduction line 036: "The distillation-trained model should perform comparably to the model trained on the original task." a 14.1% and 35.7% difference in the test accuracy is far from comparable accuracy. This is also the case for the reinforcement learning task with a large difference between Centipede of 1084 and 2D cart-pole: 134.1 

**Figures**

Figure 2: 1-D cart pole. The directions are wrong on the second image; both images say 3.1% left and 96.9% right, irrespective of the direction of the 1-D cart pole. From the caption (Line 236:237: "In 1D cart-pole, the state and labels clearly show that the agent should move in the direction in which the pole is leaning.") it is my understanding that the second figure should have a bigger value on the left than on the right, as the pole is leaning left.  

Figure 3a: The softmax probability of the classes is hard to read- can the values be reported instead of the colour gradient, which is hard to read? 

Figure 4 needs to be explained clearly. It is difficult to tell which direction the trained (rows) and the datasets (columns). Could it be made more apparent?

Figure 8b) It is hard to tell the difference between the initialisation and the distil-trained; it appears that the distil-trained is on a higher part of the loss landscape and that the initialised model is closer to the minima.

Why are the CIFAR10 Single Batch dataset images excluded from the paper? I would have liked to have seen them at least added to the appendix. 
z
**Minor points:**

Lines 48-49 need a citation; this is a bold statement that I would like verified. 

Line 161: Starts with a "+"  

Line 167: Please state the training accuracy instead of "(despite near-perfect training set accuracy)"


**Overall:**

The analysis and experimental setup is lacking, it is not made clear how comparisons are made other than visual inspection- which is warped due to having the colour maps the same even though the ranges are different. It is an interesting idea being explored, however the models do not achieve comparable accuracy, suggesting that the datasets are poor themselves. The hypothesis  does make sense that a good distilled dataset should result in a similar loss landscape to the full dataset, as it adequately captures the distribution of the data such that it is represented, however I do not think this is clearly explored or shown here especially as the loss is so high.

### Questions
Please see the questions and comments in the weakness section with the following more concretely:

The idea of minima-matching needs to be adequately explained; I am unsure what you mean; could you better explain how the loss landscapes are compared? Is it a local or global comparison? Using a metric would make this objective; even something as simple as their absolute difference would be great. 

Why, for the CIFAR10 dataset, do you use the same architecture as the MNIST, given that it does not produce good accuracy when trained conventionally? Why are not more common architectures such as a ResNet[1]  or VGG[2]?  

I need clarification on why there is an attempt at re-framing loss landscapes to cost surfaces- could you elaborate more on why you chose to refer to the spaces as cost surfaces instead of loss landscapes?


[1] He K, Zhang X, Ren S, Sun J. Deep residual learning for image recognition. InProceedings of the IEEE conference on computer vision and pattern recognition 2016 (pp. 770-778).

[2] Simonyan K, Zisserman A. Very deep convolutional networks for large-scale image recognition. arXiv preprint arXiv:1409.1556. 2014 Sep 4.

### Soundness
1

### Presentation
2

### Contribution
2
