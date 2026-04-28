# On Harmonizing Implicit Subpopulations

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Machine learning algorithms learned from data with skewed distributions usually suffer from poor generalization, especially when minority classes matter as much as, or even more than majority ones. This is more challenging on class-balanced data that has some hidden imbalanced subpopulations, since prevalent techniques mainly conduct class-level calibration and cannot perform subpopulation-level adjustments without subpopulation annotations. Regarding implicit subpopulation imbalance, we reveal that the key to alleviating the detrimental effect lies in effective subpopulation discovery with proper rebalancing. We then propose a novel subpopulation-imbalanced learning method called Scatter and HarmonizE (SHE). Our method is built upon the guiding principle of optimal data partition, which involves assigning data to subpopulations in a manner that maximizes the predictive information from inputs to labels. With theoretical guarantees and empirical evidences, SHE succeeds in identifying the hidden subpopulations and encourages subpopulation-balanced predictions. Extensive experiments on various benchmark datasets show the effectiveness of SHE.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to solve the subpopulation imbalance problem. The authors propose a new method named Scatter and HarmonizE (SHE), which discovers and balances the latent subpopulation in training data. Specifically, it builds on the principle of optimal data partition from information theory, which approximately uncovers the hiddle subpopulations and assigns data to subpopulations. Then, it achieves subpopulation-balanced predictions by simply applying a LogSumExp operation. Theoretical analyses are provided to support the validity of the method. Finally, experimental results illustrate the superiority of the proposed method SHE.

### Strengths
First of all, I have to admit that I am not an expert in the area of subpopulation imbalance, and may miss some related work.
## Originality
* To my knowledge, the data partition method for subpopulation recovery based on information theory is somewhat novel although these techniques have been widely used in other sub-fields of machine learning.
## Quality
* The proposed method is reasonable. Extensive experiments illustrate its superiority. Besides, theoretical results are also provided to support the validity of the method. 
## Clarity
* Overall, this paper is well-written and the motivation is very clarified.
## Significance
* The proposed method can contribute to the community of subpopulation imbalance.

### Weaknesses
## Originality
* There are also many works inspired by the information theory to guide the design of training objectives in machine learning. More discussions can be added.

## Quality & Clarity
* The proposed method SHE heavily depends on the number of subpopulations $K$, which is unknown in practice.
* For the equation at the end of Section 3.1, the goal to minimize the error rate of a specific test dataset is not proper because it should be the expected error rate w.r.t. the distribution, and the one for a specific test dataset is only its unbiased estimator.

## Significance
* The proposed method may have little effect on other sub-fields of machine learning.

### Questions
1. In Table 1, what is the formal definition of imbalance ratio IR? I have carefully checked this paper and have not found it.

2. From the perspective of computational cost, what about the proposed method SHE against other baselines?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work addresses the subpopulation imbalance problem where the training data consists of multiple subpopulations and their proportion is imbalanced. A novel approach, referred to as scatter and harmonize, to identifying the subpopulations and minimizing risk for each subpopulation is proposed. The authors provide a theoretical analysis of the proposed approach and demonstrate its utility through extensive experiments.

### Strengths
- Considering a practically important problem with clear motivation.
- Well-written and easy to follow.
- Supported by extensive experimental results.

### Weaknesses
 - I find that this study is relevant to various problems/applications. It could be informative if the authors can clarify the relationship to the existing work, including domain generalization, algorithmic fairness, or such.
- Some details could be improved for completeness: e.g., the subpopulation imbalance problem makes sense only if $p(\boldsymbol{x},y|s)$ differs by subpopulation $s$. Specifically, it would be helpful to see a more formal definition of the subpopulation $s$ and how it relates to the joint distribution $p(x,y)$.
- I might have missed the detail, but I am not sure if the (optimal) data partition approach is completely novel. Could the authors clarify it? If not, could the authors kindly provide what approaches have been proposed? (maybe for some other problems)
- Even if the authors focused on the subpopulation imbalance problem, domain generalization and subpopulation shift problems seem highly relevant to this work. Could the authors kindly clarify the relationship between the existing methodologies to tackle the domain generalization and subpopulation shift and the subpopulation imbalance problem? Also, this work is somewhat relevant to algorithmic fairness as well. It might be helpful for future readers to relate the problems conveniently.
- For Thm 3.3, could the authors elaborate on why minimizing $\hat{\mathcal{R}}$ results in maximizing $I(X;Y,\nu(X,Y))$? It seems like it is true asymptotically but not sure with finite samples. The connection between the empirical risk minimization and the mutual information maximization should be more clearly explained, especially regarding the finite sample case.
- Is it possible to establish an inequality between the (empirical) risk of SHE and that of ERM under the subpopulation-balanced distribution? It would be beneficial to understand the theoretical guarantees of the proposed method in a balanced setting.
- This work seems to be similar to [Lahoti et al. (2020)](https://proceedings.neurips.cc/paper/2020/hash/07fc15c9d169ee48573edd749d25945d-Abstract.html), which ensures fairness with respect to maximal heterogeneity. Might be interesting to investigate the differences and similarities. 
- Could the authors kindly explain why no method other than the proposed one outperforms the ERM across all datasets? It would be helpful to understand why the proposed method is more robust and consistent than other methods.

### Questions
- I might have missed the detail, but I am not sure if the (optimal) data partition approach is completely novel. Could the authors clarify it? If not, could the authors kindly provide what approaches have been proposed? (maybe for some other problems)
- Even if the authors focused on the subpopulation imbalance problem, domain generalization and subpopulation shift problems seem highly relevant to this work. Could the authors kindly clarify the relationship between the existing methodologies to tackle the domain generalization and subpopulation shift and the subpopulation imbalance problem? Also, this work is somewhat relevant to algorithmic fairness as well. It might be helpful for future readers to relate the problems conveniently.
- For Thm 3.3, could the authors elaborate on why minimizing $\hat{\mathcal{R}}$ results in maximizing $I(X;Y,\nu(X,Y))$? It seems like it is true asymptotically but not sure with finite samples.
- Is it possible to establish an inequality between the (empirical) risk of SHE and that of ERM under the subpopulation-balanced distribution?
- This work seems to be similar to [Lahoti et al. (2020)](https://proceedings.neurips.cc/paper/2020/hash/07fc15c9d169ee48573edd749d25945d-Abstract.html), which ensures fairness with respect to maximal heterogeneity. Might be interesting to investigate the differences and similarities. 
- Could the authors kindly explain why no method other than the proposed one outperforms the ERM across all datasets?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studied the subpopulation imbalance problem in machine learning. The setting can be described as follows: let the dataset being consist of groups $S$, and under uniform sampling, the probability $\Pr(S=s)$ varies for different realizations of $s$. If the functions $f_s: \mathcal{X}\rightarrow \mathcal{Y}$ are quite different across different groups, the machine learning algorithm that assumes a uniform $f$ would overlook the groups that contain a small number of samples. 

To overcome the issue, the paper proposed a method to incorporate the subpopulation annotation in the loss function. In particular, the paper proposed the information-theoretic objective to maximize the term of $I(X;Y| v(X,Y))-I(X;Y)$, where $v(X, Y)$ is the random variable for the subpopulation annotation. To learn the optimal partition function that minimizes the term, the paper used the ‘empirical’ version of the entropy terms as the loss function, and proved that the term convergence with an additive error of $O(1/\sqrt{N})$ to the actual information ‘’gain’’ $I(X;Y| v(X,Y))$. Therefore, if we minimize the objective, we are essentially maximizing $I(X;Y| v(X,Y))-I(X;Y)$ given that the joint distribution of $(X,Y)$ is fixed. 

The paper then conducted experiments on several real-world datasets to compare the proposed method with the benchmark algorithms. Experimental results show that their proposed method could outperform the benchmark algorithms in a majority of the settings, albeit the improvements are marginal.  

I have a mixed feelings about this paper. On one hand, it studied a well-motivated problem, and proposed an objective function with some solid theoretical guarantees. On the one hand, the exposition of the objective and the main theorem has some non-trivial problems, and the experiment performance only offers slight improvements over the baselines. As such, I would recommend a ‘’weak accept’’ due to the pros and cons.

### Strengths
I think the paper studied a well-motivated problem in machine learning. Subpopulation imbalance can be viewed as an extension of the class-imbalance problem in machine learning, and the problem is harder since the ‘imbalance’ is not easily visible from the dataset. Using a training-based method is a natural idea, and essentially, the core of the paper is to train an annotation algorithm $v(X,Y)$. The paper also contains the novelty in the design of the loss function, which resorts to the tools in information theory.

The design of the objective function is justified by a theoretical analysis. Although the proofs are mostly standard applications of information theory and concentration inequalities, I appreciate the fact that they are properly written. Due to a hectic review timeline, I did not get time to verify all the calculations in Appendix B. I believe the proofs are correct with a high-level read-through.

The experiments are conducted on various datasets, and a bulk of benchmark algorithms are used in the comparison. I do appreciate the report on the error range, which justifies that the improvement is not due to statistical fluctuations.

### Weaknesses
A main criticism I have for this paper is that many assumptions are not explicitly stated, and the quantifiers are not properly stated in the settings and theorems. Furthermore, the paper provided no intuition on how the analysis is conducted. These problems gave me a hard time parsing the result. For instance, my first impression was that mutual information is *not* the correct notion that should be used to measure the gain for ‘subpopulation harmonization’. In particular, if $f$ is a *deterministic* function of $x$ or even a randomized function whose randomness is *independent of* $x$, then $I(X;Y)$ and $I(X;Y| v(X,Y))$ are essentially the same. (Btw $v(X,Y)$ is a random variable, which I believe you never mentioned.) I think the key in your model is that $y$ is a randomized function of $x$, and the randomness is *dependent* on the choice of $s$. However, such a fact is only clear after carefully reading the proof (!), and the whole thing reads quite confusing at first. 

Additional (hidden) assumptions for the theorem in this paper include the fixed distribution of $(X,Y)$ and a fixed number of groups of subpopulations. Apart from being sloppy and not stated properly, the assumption of a fixed number of groups of subpopulations also implies we should have considerable knowledge of the dataset.

A concern about the experiment is that the improvements compared to the baseline, especially w.r.t. the very basic ERM, are too marginal. I understand that getting the SOTA performance in experiment-based machine learning is an interesting problem, however slight the improvement is. But for this specific problem, the small margin of improvement (which itself is in a low accuracy range) might have low impacts on practice. 

Minor: 
- In Table 1, the meaning of $p(\cdot)$ is overloaded – the ‘’class-imbalance’’ distribution is supported on the labels, while the ‘’subpopulation-imblance’’ distribution is supported on the groups of the subpopulations. I’d suggest using a different notation. 

- In theorem 3.3, the Rademacher complexity of $G$ is not properly defined. Instead of simply pointing at the literature, I think the notion should be defined in the appendix with the proper quantifiers.

- Inequality (16) uses McDiarmid’s inequality, but this technical tool was never introduced. :(

### Questions
Most of the questions are in the ''weakness'' section. A less technical question is as follows. For the toy example in Figure 2, the original (overall) dataset is quite balanced, and an extremely skewed sampling process obtains the imbalanced training data. I understand this is important to test the performances for classification under imbalanced settings. However, can you give practical motivations to consider such a setting where we could have obtained a balanced dataset but, for some reason, have to use a very imbalanced subsampling process for the training dataset?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an approach (SHE) to learning a classifier that performs well for a set of latent subpopulations that are not uniformly represented in the training data. The approach is to learn subpopulation structure through an “optimal data partition” with maximal conditional entropy of the label given the learned subpopulations, effectively identifying subpopulations with balanced label distributions. Evaluation is conducted with respect to a balanced marginal distribution over the subpopulations. An extensive empirical evaluation is conducted using the COCO, CIFAR-100, and ImageNet datasets. The experiments involve comparisons to alternative approaches and ablation studies.

### Strengths
* The presentation of the toy example in Figure 2 is clear and compelling for motivating the problem.
* The theoretical analysis in section 3 is sound (to the best of my knowledge) and the method straightforward to implement.
* The empirical evaluation is extensive, with comparisons to several baseline approaches in several settings, including on computer vision datasets that have been variably rebalanced, and in the context of fine-tuning large multimodal foundation models.

### Weaknesses
The paper is challenging to read, and borders on unreadable at times, due to numerous grammatical errors and unusual choices of terminology, particularly in the abstract and the first two sections. As a reader, I was not able to understand the problem that this paper aims to solve until reviewing the mathematical presentation in section 3. While I like this paper overall, this is enough for me to argue that this paper should not be published without substantial revision.

It is not clear how model complexity and finite-sample considerations interact with the core arguments of the work. For example, the toy example in Figure 2 relies on the use of a linear model for the ERM and subpopulation-specific models. However, a more complex, non-linear ERM model could still, in-principle, fit the data well, even if it might not due to data insufficiency for the underrepresented subpopulations. It’s not obvious how this consideration surfaces in the theoretical presentation nor in the experiments.

### Questions
* How does SHE compare to baselines in-domain, i.e., in cases when both the training and testing data are imbalanced? If I understand correctly, the claim of Proposition 3.2 is that SHE should not underperform ERM (in the limit) but it seems that this is not evaluated in the experiments because of the focus on balanced test distributions.
* SHE is motivated to address a particular distribution shift problem where there is subpopulation shift over a set of subpopulations with balanced label distributions. How would SHE perform under other notions of subpopulation shift, where it is not assumed that the label distributions are balanced within subpopulations?
* Could SHE be extended to handle an arbitrary specified target distribution over the latent subpopulation? Would this be as simple as weighting the subpopulation components of the LogSumExp operation?
* Is there a reason why the model-based $V$ variant of SHE could not depend on both $X$ and $Y$? My interpretation of the method was that $V$ is not used at test time, so this might allow for a scalable model-based subpopulation mapping that matches the performance of the full $N$x$K$ matrix.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
