# Density Ratio Estimation-based Bayesian Optimization with Semi-Supervised Learning

- Decision: Reject
- Scores: 6, 6, 3, 6

## Abstract
Bayesian optimization has attracted huge attention from diverse research areas in science and engineering, since it is capable of efficiently finding a global optimum of an expensive-to-evaluate black-box function. In general, a probabilistic regression model is widely used as a surrogate function to model an explicit distribution over function evaluations given an input to estimate and a training dataset. Beyond the probabilistic regression-based methods, density ratio estimation-based Bayesian optimization has been suggested in order to estimate a density ratio of the groups relatively close and relatively far to a global optimum. Developing this line of research further, supervised classifiers are employed to estimate a class probability for the two groups instead of a density ratio. However, the supervised classifiers used in this strategy are prone to be overconfident for known knowledge on global solution candidates. Supposing that we have access to unlabeled points, e.g., predefined fixed-size pools, we propose density ratio estimation-based Bayesian optimization with semi-supervised learning to solve this challenge. Finally, we show the empirical results of our methods and several baseline methods in two distinct scenarios with unlabeled point sampling and a fixed-size pool and analyze the validity of our proposed methods in diverse experiments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an extension to bayesian optimisation (BO) using density rato estimation (DRE) to tackle the problem of overconfidence in the estimators used.  Specifically, the authors suggest using semi-supervised learning (transduction) to increase the accuracy of the model (overcome the difficulties typically caused by the imbalance between dataset sizes above and below the threshold).

### Strengths
The paper is very well written.  I quite like the underlying idea, and the implementation appears reasonable.

### Weaknesses
One doubt I have with this paper perhaps stems from unfamiliarity with semi-supervised algorithms in general.  My understanding of such approaches is that they tend to assume that the unlabelled training points are nevertheless generated from the underlying x distribution.  In most applications of BO, however, this concept is nonsensical: the only x distribution is the points sampled by BO, which are (in some sense) arbitrary (depending on the acquisition function they may cluster around the optimum as time passes, but not necessarily).  Am I missing a key point here?

### Questions
See weakness section.

### Soundness
3 good

### Presentation
3 good

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
The paper proposes a novel method called DRE-BO-SSL which combines SSL with DRE-based BO.
The intention is to improve the exploration-exploitation trade-off as previous DRE-based BO (BORE and LFBO) tends to focus on exploitation due to the over-confident classifiers.
The paper explores two types of SSL method (label propagation and label spreading).
Empirical results show that the proposed method work better than competitive BO methods on a wide range of tasks.

### Strengths
**originality** The proposed method is novel.

**quality** The proposed method is sound and the empirical results are promising.

**clarity** The technical part of the paper is good.

**significance** The proposed method is a good contribution to DRE-based BO and can be potentially useful to solve the over-confidence problem in DRE in general.

### Weaknesses
The presentation could be improved.
Specifically, the focus on over-confidence in the beginning is confusing and I only understand the main point until I read section 3.1 where the relation to exploitation is mentioned.
Perhaps this should be moved towards the front.

Some limitations of the work should be explicitly mentioned/discussed.
For example, assumption 4.1. seems to imply that the method is only intended to work on smooth functions.

Some related work is missing; see questions below.

### Questions
The over-confident problem of DRE is recently studied by [1,2]. 
Can the author(s) comment on how the construction of auxiliary distribution in these work is related to the sampling distribution of DRE-BO-SSL?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper extends the binary classifier-based Bayesian optimization such that the classifier is trained in a semi-supervised manner. The authors argue that the semi-supervised classifier expands the region of ${\bf x}$ associated with high probability $P(y \leq y^\dagger | {\bf x}, \mathcal{D})$, which leads to more efficient exploration of black-box optimization. 
Proposed method, called DRE-BO-SSL, is compared with the ordinary BO as well as DRE-BO with sueprvised classification approaches for function optimization as well as hyperparameter tuning tasks.

### Strengths
The idea sounds sensible to incorporate semi-supervised learning for encouraging the exploration of DRE-based Bayesian optimization method. 
Figure 1 illustrates how the search space is explored by the proposed framework. 
With that said, the figure needs more explanation for better comprehension of its content. 
For example, the color bar is labeled as *Class Probability*, which suggests something like $p(y \leq y^\dagger | {\bf x}, \mathcal{D})$.
However, in the text most probability is shown as the distribution over the input such as $p({\bf x} | y \leq y^\dagger, \mathcal{D})$. 
What does the figure specifically illustrate?

### Weaknesses
The presentation of current manuscript is problematic in that many things are uncertain from the text. 
See *Questions* part below for details. The reviewer believes this information is necessary to better understand the method and enhance the reproducibility of results.

Unfortunately, the efficacy of proposed method in the performance of optimization over iterations is hardly distinguishable in Figs. 5 or 6. 
I acknowledge a clear victory is not so common in comparisons of black-box optimization methods. 
The bigger problem is that it is unclear  from the text on what condition and why the proposed method outperforms the existing approaches.

### Questions
1. Truncated normal distribution for sampling unlabeled data points. 

How is matrix ${\bf A}$ designed? What covariance is taken for this disbiribution, for what? 
What are lower and upper bounds ${\bf l}$ and ${\bf u}$? 
Are they boundaries of search space $\mathcal{X}$? Is it assumed to be rectangular?

2. Fixed-size pool. 

Does *fixed-size pool* scenario mean some finite number of candidate points ${\bf x}_i$ are selected in advance and that optimized over these points? 
If true, is the set of points dynamically updated or fixed in advance? 

3. Definition of simple regret. 

What is the definition of simple regret? 
Is it $f({\bf x}_n) - f^*$ in the $n$th iteration, where $f^*$ is the minimizer of function $f$. 
I am wondering why the regret is monotonically decreasing in Fig. 2. 
Does this plot $\min_n f({\bf x}_n) - f^*$?

4. What is dimensionality of ${\bf x}$ in four benchmark tasks in Fig. 2. 

Are they all two? This is crucial information on the difficulty of black-box optimization problems. 

5. Hyperparameter optimization of Fig. 6

How do you define the distance $\|{\bf x}_i - {\bf x}_j \|$, especially when categorical values are involved such as activation function and learning rate schedule.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to use semi-supervised learning methods for Bayesian optimization (BO). The idea is to use an alternative paradigm for BO instead of fitting a regressor to the observed data. The authors suggest to use density ratio estimation BO instead. In DRE-BO one uses a classifier as the model to guide the search and the acquisition function is computed in terms of the class probability ratios. The authors suggest to strengthen the classifier accuracy by using semi-supervised learning techniques. The method is compared to other strategies in synthetic and real problems.

### Strengths
Extensive experimental evaluation.

### Weaknesses
The introduction is poor. It does not introduce properly the problem addressed in the paper.

In general the writing of the paper has to be improved a lot. It does not introduce the concept of DRE-based BO right. If the reader is not familiar with it, they cannot understand it properly. The authors have failed in this task.

It is not clear what is the motivation for DRE-based BO. It is also unclear how the threshold value y^t is chosen.

The authors have to better explain DRE-based BO, why does it work, why is it interesting and why it is better than regression based BO.

Figure 1 is not explained properly.

The proposed method is not very well motivated. It seems it is simply using a better classifier. The authors claim that they use semi-supervised learning techniques to train the classifier. However, the semi-supervised data seems to be generated by sampling from a truncated Gaussian and then label propagation is used to generate the associated labels. Therefore, the proposed method can be understood simply as using a better classifier. Given this, I do not find that much novelty in the proposed method.

### Questions
Please, explain better figure 1 and why it illustrates the over-confidence problem.

Please, explain how the threshold value y_t is chosen.

Please, explain why the proposed method needs to sample from a truncated multivariate Gaussian distribution.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
