# The Implicit Bias of Stochastic AdaGrad-Norm on Separable Data

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 6, 6

## Abstract
This paper explores stochastic adaptive gradient descent, i.e., stochastic AdaGrad-Norm, with applications to linearly separable data sets. For the stochastic AdaGrad-Norm equipped with a wide range of sampling noise, we demonstrate its almost surely convergence result to the $\mathcal{L}^{2}$ max-margin solution. This means that stochastic AdaGrad-Norm has an implicit bias that yields good generalization, even without regularization terms.
We show that the convergence rate of the direction is $o({1}/{\ln^{\frac{1-\epsilon}{2}}n})$. Our approach takes a novel stance by explicitly characterizing the $\mathcal{L}^{2}$ max-margin direction. By doing so, we overcome the challenge that arises from the dependency between the stepsize and the gradient, and also address the limitations in the traditional AdaGrad-Norm analysis.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
For the stochastic AdaGrad-Norm equipped with am affine variance noise, the authors demonstrate that its almost surely convergence result to the L2 max-margin solution, considering the classification problem with the cross-entropy loss on a linearly separable data set.

### Strengths
For the stochastic AdaGrad-Norm equipped with am affine variance noise, the authors demonstrate that its almost surely convergence result to the L2 max-margin solution, considering the classification problem with the cross-entropy loss on a linearly separable data set.

### Weaknesses
Although the authors explore a broader noise model, the underlying motivation for the proposed model appears to be somewhat lacking in strength. The pertinent reference to the affine variance noise model is missing. It remains uncertain whether this noise model is practical within the simple model classification problem studied in this paper, and also the existing deep learning datasets or architectures.

The authors study the classification problem with the cross-entropy loss on a linearly separable data set, but the motivation of the paper is to understand the implicit bias of algorithms in training deep neural networks model, which has some extra benign testing phenomenon. 

No numerical experiments are provided to complement the derived theory. Particularly, whether the intriguing phenomenon happens in Adagrad-Norm optimization on training deep learning model is unclear to me.

As claimed by the authors, for deterministic AdaGrad-Diagonal, (Soudry et al., 2018; Gunasekar et al., 2018; Qian & Qian, 2019) claim that it does not converge to the L2 max-margin solution as the non-adaptive methods do (e.g. SGD, GD). Thus, investigating the implicit bias of Adagrad-Norm may not be so important. 

It looks to me proof techniques relies on (Jin et al. 2022), and (Soudry et al., 2018; Gunasekar et al., 2018; Qian & Qian, 2019; Wang et al. 2021b).  It would be beneficial to distinctly highlight the main novelties of their methods. Also the comparisons with the existing work (Wang et al. 2021b) is unclear to me.

### Questions
see the above

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper mainly concerns with the implicit bias property of the stochastic AdaGrad (normed variant) algorithm on linear classification problem. In particular, its main result shows that for linearly separable data, AdaGrad-Norm converges in direction to the $L_2$ maximum-margin solution. Furthermore, a second result gives a convergence rate to the solution induced by the implicit bias of AdaGrad-Norm.

### Strengths
This result (if true, see below), would be a nice addition to the study of implicit bias of various optimization algorithms. In the literature, the stochastic setting is considered quite difficult. And the normed version of AdaGrad should be much more challenging than the diagonal variant because the scale matrix $S$ (more commonly referred as $G$ in literature) is no longer separable in coordinates. Thus, it is nice to see the authors attempted this more difficult problem.

### Weaknesses
However, I do not believe the results are correct. There are some fatal and elementary errors and the paper shows no sign of proof-reading.

First, the result does not pass an eye test. In [1, 2], the implicit bias of the diagonal variant of AdaGrad depends on various factors such as initialization. Therefore, it is very surprising that the more complex normed version variant would have an implicit bias that do not depend on such conditions.

Then, there are several extremely elementary mistakes:

1. In the equation block in the "Intuition of the theorem" part of Section 4, what is the second gradient taken with respect to? If it is taken wrt $\theta_n$, then the author clearly forgot to apply the chain rule to $\theta_n / \lVert {\theta_n} \rVert$. Also, the value of $i_n$ is in general not unique.

2. In the second equation of the proof of Theorem 4.3, the gradient of $\lVert \theta \rVert^\alpha$ is computed incorrectly, again seemed to be an omission of chain rule. Also, the dimensions in the middle and right expressions do not match.

Next, the formatting of the paper is wrong. It seems that the author put most of the paper into a enumerate block, thus affect the indentation throughout the paper. It is clear to me that no proof-reading was done.

With these observations in mind, I am convinced that this paper is deeply flawed and I cannot trust the author's claims.

Additionally, there are some minor mistakes that further hurt the quality of the paper.

3. Many quantities were not adequately defined before they were being used. For instance, Lipschitzness of $\nabla g$ was not mentioned until Section 4. In the same equation block I pointed to in my first comment, $k_n$ was not defined. In equation (3), $\hat{c}$ was not defined.

4. The first two sentences in Section 4 seems to suggest that Theorem 4.1 is original, but it is in fact not. They need to be rephrased to not confuse the readers.

5. Lemmas A.8 and A.10 where invoked in Section 3 without being stated first. And in Lemma A.8, the term "margin vector" was not defined.

6. The set defined at the top of page 4 is not rigorous. In fact, the global minimum is simply not attainable.

### Questions
None, I think a complete overhaul would be needed.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper examines the implicit bias of Stochastic Adagrad within the framework of linear separable data. Specifically, the authors consider linear classification applied to data that can be linearly separated, aiming to determine the hyperplane that correctly classifies the data. Out of all hyperplanes that correctly separate the data, the authors center their attention on the maximum-margin vector, which optimally widens the gap between positive and negative data points. The main contribution of the paper lies in establishing that once Stochastic Adagrad-Norm is coupled with the logistic loss, convergence towards the maximum-margin vector is achieved.

### Strengths
Achieving convergence towards the maximum-margin vector is a crucial objective for the sake of generalization, as emphasized in prior research. Additionally, Stochastic Adagrad norm is a widely utilized method in practical applications. From this perspective, it is an interesting question whether Stochastic Adagrad norm exhibits implicit bias in favor of the maximum-margin maximizer. Furthermore, the technical contributions of the paper are nicely presented in the main part of the paper and they seem to admit an interesting technical depth (I have not checked the appendix in detail though).  Finally, the paper effectively extends the recent findings of [1] demonstrating that Adagrad norm converges towards a margin vector that however may not correspond to the maximum-margin solution.


[1]  On the convergence of mSGD and AdaGrad for stochastic optimization, Jin et al., ICML 2022

### Weaknesses
As also noted by the authors, prior studies within the same context have already established implicit biases for methods like Gradient Descent and SGD. From this perspective, I find the presented results somewhat unsurprising, leading to doubts about their significance. Specifically, while the paper demonstrates convergence to the maximum-margin solution using Stochastic Adagrad-Norm with logistic loss, the core mechanism driving this behavior might not be fundamentally different from what's observed in simpler methods. The paper's contribution, therefore, feels incremental rather than transformative. Additionally, I find the established convergence rate to be a weak point. As far as I comprehend, Theorem 4.3 suggests that Stochastic Adagrad-Norm requires $O(2^{1/\epsilon})$ iterations to converge to an $\epsilon$-optimal solution for the respective logistic regression problem. This exponential dependence on the desired accuracy \epsilon is concerning and significantly limits the practical applicability of the theoretical results. This slow convergence rate raises questions about the practical relevance of the findings, especially when compared to other optimization methods with polynomial convergence rates. Another less important concern pertains to the fact that the provided convergence results are based on the best-iterate rather than the last-iterate of Stochastic Adagrad Norm. This distinction is important because in practice, we typically use the last iterate, and convergence guarantees for the best iterate do not directly translate to guarantees for the last iterate. Finally, the lack of a formal definition for the "margin vector" is a noticeable oversight, especially given its central role in the analysis. This imprecision makes it harder to fully grasp the technical details and implications of the results.

### Questions
1. As far as I understand, Assumption 3.1 holds for the standard estimator that samples data points uniformly at random. If this is the case I think it would be better to remove Assumption 3.1 and provide a Lemma stating that the assumption is satisfied for the standard estimator.

2. Are you aware of a first-order method that does not exhibit implicit bias to max-margin solutions in such linear classification problems? In the case there is such a method, I think it would be worth mentioning it so as to emphasize that implicit bias is not a general property of first-order methods.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper authors provide analysis for the stochastic AdaGrad-Norm method, applied to binary classification problem with linearly separable data. The main motivation of the authors is as follows. Due to the specific nature of stochastic AdaGrad-Norm, the existing techniques, used to analyse other stochastic or deterministic first-order methods, is inapplicable in this case. Firstly, they show that this method converges to max-margin solution almost surely. Secondly, they get the almost surely convergence rate of max-margin vector. To obtain these results authors assume, that the variance of the stochastic gradient is upper-bounded by squared norm of the full gradient, and if loss function is upper-bounded, then its stochastic gradient is also upper-bounded. This is a more general assumption, then existing assumption about regular sampling noise.

### Strengths
1. The problem of existence of implicit bias of optimization methods for binary classification problem with separable data is being studied since 2017-2018. In this paper authors extend this theory on stochastic AdaGrad-Norm method.
2. Authors clearly describe, why existing analysis does not work for this method.
3. Authors provide a sketch for long proof of one of the theorems and provide its intuition.

### Weaknesses
Lack of experimental results. It worths to show numerically, that indeed AdaGrad-Norm converges to zero error for this problem.

Questions:
1. Proof of Lemma A.4. Could you please describe in more details, why $\|\nabla^2 g(\theta)\| = \Theta(\|\nabla g(\theta)\|)$ in the neighborhood of the stationary point?

Also I have some minor remarks.
1. Maybe move problem formulation to introduction, because it is rather hard to understand the introduction part, if you are not very familiar with topic.
2. Page 2. You haven't introduced $f$ and $g$.
3. Page 2, row 8. Seems like, you forgot $\mathbb E$ sign in front of $\frac{\alpha_0}{\sqrt S_n} f(\theta_n) \nabla g(\theta_n)$
4. Same place, you forgot transpose sign
5. Page 2, last paragraph before **Related Works**. Change $\zeta$ to $\xi$
6. Page 3, **Contributions**, second part, fourth line. Probably, you forgot "*" over $\theta$-s in the second term under the norm.
7. Page 3, **Contributions**, second part, sixth line. You forgot second "|" in the closing gap of the norm
8. Page 4. Probably, it is better to remove "and Main Results" from the name of the 3rd section.
9. Page 4, Main Results, first paragraph. Since Theorem 4.1 is from another paper, I think, it is better to remove "Our" from first line of the paragraph.
10, Page 5, **Intuition of theorem**. What do you mean by "(requiring additional validation)"?
11. Page 5. Maybe remove index $n$ in $\psi_{n,i}$, because it does not depend on $n$ and only makes equations messier.
11. Page 6, Lemma 4.1, first line. Probably, there should be "there is a vector $x_\theta$".
12. Page 6, Lemma 4.1. What is $U(..., ...)$? It seems like you meant $\delta_0$-neighborhood, but still define it earlier, please.

### Questions
Questions:
1. Proof of Lemma A.4. Could you please describe in more details, why $\|\nabla^2 g(\theta)\| = \Theta(\|\nabla g(\theta)\|)$ in the neighborhood of the stationary point?

Also I have some minor remarks.
1. Maybe move problem formulation to introduction, because it is rather hard to understand the introduction part, if you are not very familiar with topic.
2. Page 2. You haven't introduced $f$ and $g$.
3. Page 2, row 8. Seems like, you forgot $\mathbb E$ sign in front of $\frac{\alpha_0}{\sqrt S_n} f(\theta_n) \nabla g(\theta_n)$
4. Same place, you forgot transpose sign
5. Page 2, last paragraph before **Related Works**. Change $\zeta$ to $\xi$
6. Page 3, **Contributions**, second part, fourth line. Probably, you forgot "*" over $\theta$-s in the second term under the norm.
7. Page 3, **Contributions**, second part, sixth line. You forgot second "|" in the closing gap of the norm
8. Page 4. Probably, it is better to remove "and Main Results" from the name of the 3rd section.
9. Page 4, Main Results, first paragraph. Since Theorem 4.1 is from another paper, I think, it is better to remove "Our" from first line of the paragraph.
10, Page 5, **Intuition of theorem**. What do you mean by "(requiring additional validation)"? 
11. Page 5. Maybe remove index $n$ in $\psi_{n,i}$, because it does not depend on $n$ and only makes equations messier.
11. Page 6, Lemma 4.1, first line. Probably, there should be "there is a vector $x_\theta$".
12. Page 6, Lemma 4.1. What is $U(..., ...)$? It seems like you meant $\delta_0$-neighborhood, but still define it earlier, please.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
