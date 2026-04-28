# Lowering Data Diversity can Accelerate Training: Case Studies in Synthetic Tasks

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 1, 3, 5

## Abstract
We identify a loss plateau at the start of training in the three synthetic settings of in-context linear regression, sparse parity, and fact memorization. While careful tweaks to the optimization algorithm can mitigate these plateaus, we find that a simpler orthogonal approach of *lowering the data diversity*, and in doing so, biasing the training distribution *away* from the test distribution, counter-intuitively also speeds up training. This connection between data diversity and training speed holds for three different diversity-*reducing* interventions across our varied synthetic settings. Our findings offer a new perspective on data filtering and curriculum learning for training machine learning models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors conduct a controlled set of experiments on three synthetic settings. They observe the loss plateau and find that by biasing the training distribution away from the test distribution to reduce data diversity at the start of training, one can accelerate training. Results from various simple and counterintuitive data interventions interventions suggest that simpler data filtering techniques can match or outperform complex optimization methods.

### Strengths
- The paper is overall clearly written.
- The observations are indeed interesting and surprising especially since the interventions improve training without discriminating between datapoints.

### Weaknesses
 - From a loss landscape perspective, the initial speedup seen upon reducing data diversity suggests that the parameters are getting stuck in a local suboptimal minimum that may lie near the initialization. However, numerous methods have been developed to avoid getting stuck in such minima such as adding regularization, introducing learning rate schedulers, etc. Therefore, while reducing data diversity may seem to help speed up, it may not contribute to finding a better generalization solution at all. 
- The paper claims that a purely data-driven approach can have the same speedup as optimization methods; however, low similarity and high variance are also often associated with sharp minima in the loss landscapes. Therefore, the authors could consider comparing methods like sharpness-aware minimization, momentum, etc. in this context. Moreover, PCGrad is designed for training across multiple tasks, that are expected to have potential interference. However, I wonder how scalable it would be in a single-task setup for increasing model size, even though it does improve training speed.  
- While the authors mention that their synthetic settings are simple, I think finding the "optimal" amount of biasing needed for initial speedup can be quite challenging on real data, as it may require an extensive search over hyperparameters. I wonder if the authors could suggest any potential strategies for finding the optimal amount of biasing in real-world scenarios.

### Questions
- Fig 5, is there a reason why $\alpha=1$ performed best in all cases?
- It would be interesting to have some theoretical justification for why the interventions, especially the power law sampling, lead to increased training speed.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper demonstrates with experiments that lowering training data diversity accelerates training. In 3 experiment setups with synthetic data---in-context linear regression in transformers, learning sparse parity functions with MLP, and fact memorization in transformers---the authors argue that a variety of interventions can accelerate training (e.g. interventions on the gradient updates or on the training dataset).

### Strengths
The paper presents experiments on different setups, involving both transformers and MLPs that are used in practice. There has been recent interest in using transformers/MLPs to learn sparse parities [1, 2] and in-context linear regression [3, 4], which the paper studies. The general problem in the paper: of accelerating training is of interest to the ML community. The paper takes approaches this problem from the lens of data curation goes back to Curriculum Learning [5].

[1] Barak, B., Edelman, B., Goel, S., Kakade, S., Malach, E., & Zhang, C. (2022). Hidden progress in deep learning: Sgd learns parities near the computational limit. Advances in Neural Information Processing Systems, 35, 21750-21764.

[2] Edelman, B. L., Goel, S., Kakade, S., & Zhang, C. (2022, June). Inductive biases and variable creation in self-attention mechanisms. In International Conference on Machine Learning (pp. 5793-5831). PMLR.

[3] Garg, S., Tsipras, D., Liang, P. S., & Valiant, G. (2022). What can transformers learn in-context? a case study of simple function classes. Advances in Neural Information Processing Systems, 35, 30583-30598.

[4] Zhang, R., Frei, S., & Bartlett, P. L. (2023). Trained transformers learn linear models in-context. arXiv preprint arXiv:2306.09927.

[5] Bengio, Y., Louradour, J., Collobert, R., & Weston, J. (2009, June). Curriculum learning. In Proceedings of the 26th annual international conference on machine learning (pp. 41-48).

### Weaknesses
## Motivation
The paper aims to accelerate training for the sake of optimization only, but that is not the central goal in learning. In fact, research in ML optimization techniques serve to fulfill the **central goal of generalizing to the test distribution**. Moreover, the paper frequently finds in their experiments that faster training (using the methods they present) often leads to worse generalization, so I doubt the benefits of the proposed methods.

**In fact, the authors mention this exact severe limitation in line 52.** I'd find insights into generalization more helpful than just focusing on training optimization.

## On reducing data diversity to optimize faster
It is not shown that accelerating training by reducing data diversity leads to increased generalization to the test distribution. I think that would be a good argument for "reduce data diversity -> thus train faster -> thus generalize to test distribution better". As an example, consider the setting where we want to learn the target function $f(x) = x^2$ given a finite number of training samples $x_1, ..., x_n$. We can forget about the target (test distribution) and instead sample from the function $g(x) = 1$, _just for the sake of low data diversity_. Optimizing on samples to learn $g$ is faster, but this is far from the goal of learning the target $f$.

On another note, decreasing the number of training tasks/samples to reduce training data diversity should intuitively lead to overfitting. Figure 4 shows this exact phenomena, so I'm not convinced that accelerated training with the paper's data curation methods is actually helping in learning.

## Techniques
In Section 3, the paper argues that biasing batch gradients can accelerate training. Isn't this technique the same as SGD with momentum or an adaptive gradient method like AdaGrad or Adam? I'm not sure this is a novel contribution.

Finally, the paper dos not conduct data-diversity experiments on real-world problems such as image classification (even on well-studied datasets like CIFAR or MNIST) and language generation. I appreciate that the authors mention this limitation in Section 6 and 7, but I believe the current version of the manuscript is severely lacking with just synthetic data experiments.

## Writing
The paper needs numerous citations in the introduction to substantiate claims. Several typos and clarifications needed:
1. Citations for lines 41-44.
2. Line 96. It's verbose to call the task $f_w$ when we can simply write $w^T x + \epsilon$ as used in Line 93. Lines 96-105 can be written in 3-5 lines at max.
3. Line 297. The paper conflates "faster optimization" with "learning". The model trains faster, but does not generalize (or "learn") better or faster.

Moreover, the statement "low data diversity accelerates training" is repeated throughout the paper (paraphrased in many ways), making the paper more verbose than necessary. I understand that it is the paper's main argument, but it is overly used in my view.

### Questions
# High-level questions
1. Section 2.2. There is a notion of "task" in linear regression and fact memorization problems. What is a task in the sparse parity problem?
2. Section 2.2. Why study 3-layer MLP here but transformers for the other two problems?
3. Line 165. What is the $i^th$ token $d_i$? If these are the elements $s, r, n_1, ..., n_{k_noise}$, it doesn't make sense to have the transformer predict noise token $n_t$ given $s, r, n_1, ..., n_{t-1}$ since the noise tokens are drawn independently. If I'm reading this wrong, what is the tokenization procedure here?

# Low-level questions
1. Line 32: "followed by abrupt learning to low loss". What does this question mean? Are the authors pointing to the "grokking" line of work [1]?
2. Line 93. Typo: $x$ is in $\mathbb{R}^d$ but $(x, y)$ is not.
3. Equation 3. What is $\tau$?
4. Line 132. What is $\mathcal{D}$ here? Uniform distribution over the $d$-dimensional hypercube?
5. Line 162. What is the ICL-LR setting? It is likely the 1st problem, but this abbreviation is introduced here for the first time.

[1] Power, A., Burda, Y., Edwards, H., Babuschkin, I., & Misra, V. (2022). Grokking: Generalization beyond overfitting on small algorithmic datasets. arXiv preprint arXiv:2201.02177.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper argues that convergence using SGD can be more efficiently obtained, in some cases, by using a training data distribution that has less in common with the test distribution. This argument is of course counterintuitive, and it disagrees with a wide body of fundamental research in the field around how an ideal training dataset is one that has more in common with the general distribution, not less.

### Strengths
The authors take a stance that, to my knowledge, has not been studied before in machine learning. If this were a well understood, real phenomenon, I think it could be impactful.

### Weaknesses
Overall I found this paper’s argument unconvincing, as they experiment only on three synthetic settings and provide no arguments as to why this effect might occur. Of course, this effect cannot be shown forever, and eventually this skewing of the training distribution will have a negative effect on test performance. When and why does this happen, and what can be gleaned from this work about more conventional model training? 

As the authors write themselves in the limitations section, they do not have an understanding of when or why this occurs, and do very limited evaluation and show preliminary results. I realize this section was written to get ahead of criticism they anticipate to this effect, but the work seems very incomplete with these questions left unanswered. The future work in the discussion section, for example, is very much in-scope, and should be part of the paper the authors are writing.

At this time, I feel that the presented investigation is not thorough enough to meet the bar for publication in ICLR.

### Questions
1. There is a wide body of work on generalization through a theoretical lens, typically taking advantage of both model complexity and train/test distribution similarity. How does this work fit into this literature?

2. Does this happen in more conventional language modeling (or non language modeling tasks)?

3. Why does this effect happen at all? I don't see any justification of this phenomenon, only a few demonstrations of it.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper examines methods to accelerate training by reducing data diversity, focusing on synthetic tasks like in-context linear regression, sparse parity, and fact memorization. Traditional approaches typically improve training by adjusting optimization algorithms to mitigate plateaus; however, this study found that simple interventions in data sampling, such as reducing task diversity or sampling with non-uniform distributions, can achieve similar benefits. These findings provide insights into data filtering and curriculum learning approaches, suggesting that less diverse but strategically chosen training data could enhance model efficiency.

### Strengths
The paper presents a clear experimental setup, demonstrating how intentional data biases can speed up learning in synthetic tasks.

The use of visuals makes its findings easier to understand.

This research is useful in situations where training efficiency is a priority.

### Weaknesses
The application scope is narrow to meet real-world needs, and it lacks an explanation for the observed phenomena.


### Questions
Your approach and optimization algorithms can achieve the same goal, so how would you convince others to use your method instead of an optimization algorithm? 

Would combining your approach with other optimization algorithms lead to more significant performance improvements?

### Soundness
3

### Presentation
3

### Contribution
2
