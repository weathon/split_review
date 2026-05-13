# Unleashing the Power of Annotation: Enhancing Semi-Supervised Learning through Unsupervised Sample Selection

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
With large volumes of unlabeled data and limited annotation budgets, Semi-Supervised Learning (SSL) has become a preferred approach in many deep learning tasks. However, most previous studies have primarily focused on  utilizing labeled and unlabeled data for model training to improve performance, while the efficient selection of samples for annotation under budgetary constraints has often been overlooked.To fill this gap, we propose an efficient sample selection methodology named Unleashing the Power of Annotation (UPA). By adopting a modified Frank-Wolfe algorithm to minimizing a novel criterion $\alpha$-Maximum Mean Discrepancy ($\alpha$-MMD), UPA selects a representative and diverse subset for annotation from the unlabeled data. Furthermore, we demonstrate that minimizing $\alpha$-MMD enhances the generalization ability of low-budget learning. Experiments show that UPA consistently improves the performance of several popular SSL methods, surpassing various prevailing Active Learning (AL) and Semi-Supervised Active Learning (SSAL) methods even under constrained annotation budgets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method for selective a representative as well as a diverse subset for expert annotation. The idea is to weight the terms in MMD-squared distance between the target and the desired subset, such that the trade-off between diversity and representativeness can be explicitly controlled. The weighted distance can be minimized using Frank-Wolfe/Kernel-herding techniques. The kernel-herding algorithm is modified so that samples are not repeated. Error bound for this modified algorithm is presented under certain conditions (Theorem 3.2).

When the proposed criteria is used for AL in context of SSL algorithms, empirically it is shown that the methodology outperforms AL and SSAL baselines. (table 2)

### Strengths
1. The idea of \alpha-MMD^2 and its interpretation in (5) are clear and suitable for the AL tasks.

### Weaknesses
1. The basic methodology essentially selects a representative and diverse subset. There are many methodologies for such a diverse subset selection. e.g., [1*]-[3*]. None of such methods have been discussed nor have been empirically compared with. This makes it difficult to evaluate the significance of the proposal.

2. The weighting idea and corresponding algorithm details are more or less straightforward. (Mainly because it is a simple modification of MMD).

3. Reg. table2. Since UPA is employed above SSL (flexmatch/freematch), it may be important to compare against baseline/SOTA AL criteria when employed with flexmatch/freematch. Then the advantage of the proposed criteria would be explicit. Now it is not clear whether the imporvement is because of flexmatch/freematch or because of the proposed criteria.

### Questions
1. In the proof of theorem3.2, "j" is defined as argmin over i=1to n\I_p for some objective. But in the proof the following is used: f_{I_p}(x_j_{p+1}) <= f_{I_p}(x_j). Is this correct?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents the method of selecting instances for annotation, based on the MMD (Max Mean Discrepancy) principle. According to the principle, the method aims to minimize the distance between the full unlabeled dataset, and the sampled instances. An additional parameter $\alpha$ is introduced to tradeoff sample representativeness with diversity. The Kernel Herding algorithm is used to iteratively find the target set of points.

### Strengths
Selecting an optimal subset for annotation is an important problem in scenarios where labels are costly to get. The main contribution of the paper is the demonstration that minimizing MMD for such scenarios helps improve underlying classification accuracy. While there is a clear parallel with the coreset constriction idea, the paper gives a theoretical result which relates the two approaches. The experimental section provides a set of comparisons with the baselines which demonstrate advantages of using MMD.

### Weaknesses
Introducing the parameter $\alpha$ doesn’t seem to have enough theoretical or experimental grounding. From the theoretical standpoint, the trivial case $\alpha=1$ makes all bounds tighter than for any other alpha. This is concerning because the core motivation for introducing $\alpha$ is to balance representativeness and diversity, yet the theoretical analysis doesn't seem to support any value other than $\alpha=1$. From the experimental part, the only ablation analysis of $\alpha$ is given in table 3, it doesn’t fully convince that using any other value except $\alpha=1$ is any better. Specifically, the results for $\alpha=1$ and "optimal" $\alpha=1-1/\sqrt{m}$ are quite close, and measured only on 3 datapoints for one dataset. The lack of a more comprehensive analysis of the impact of $\alpha$ on various datasets and with different values makes the choice of $\alpha=1-1/\sqrt{m}$ seem arbitrary. More experimental grounding for motivating the choice $\alpha=1-1/\sqrt{m}$ over $\alpha=1$ would help.

Without taking $\alpha$ into consideration, there is not much novelty in the introduced methods. Overall, the paper provides good justification of using MMD for sample selection.

### Questions
In the experimental section, it would be great to have the results of a supervised classifier (not SSL) trained on the selected set of instances, and see at what subset size the accuracy would match the accuracy of a classifier trained on the whole training set.

### Soundness
3 good

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper suggests a maximum mean discrepancy approach to select data for annotation. The approach, referred to as UPA, attempts to capture representative and diverse set of point to improve on active learning. Some theoretical results are presented based on a similar approach to Coarset (Sener et al.) to reduce the risk on the labelled set by selecting a coareset.
Empirical validation is presented for a few benchmarks and comparison with a few  active learning approaches and SSAL.

### Strengths
1.	An approach the optimizes both diversity and representativeness has advantage
2.	Some theoretical results support the advantage of the method.
3.	Empirical results show some advantage over Random baseline and for cifar 10 clear advantage to using flexMatch with UPA

### Weaknesses
1. The soundness of the paper is poor: 
 
a. mostly the empirical validation is lacking additional datasets to support the advantage of the method

b. improvement over random baseline is too modest in my view, 0.5 precent improvement when the STD is at 0.5 is not convincing

c. we are missing a simple ablation study: if you show results of flexMatch+UPA, you have to show also results of just flexMatch, otherwise it is not clear if the advantage is due to FlexMatch or the addition of UPA.

d. 3 independent runs is not enough

e. Why are you selecting the particular m values for each data set? why is it different for each data set? I would much prefer seeing a graph over a range of values.

f. Not enough method are used in the comparison, what about BADGE by Ash et al -  it is a classical diversity and uncertainty approach that could also be compared to show that representativeness and diversity is better (if it is indeed so…)

2. The requirement that m/n <=0.2 is quite weak and unrealistic, sometimes 0.2 can be a huge data set to annotate! How does that work with Active learning setting in which the budget is limited.
3. Clarity is also poor:

a. There is no pseudo code describing the method, or at least a set of steps

b. What is the input space over which the method is used? Is it the actual data? For coreset is it the penultimate layer representation, what are you using?

c. Remark 1 is rather confusing, if you present Thm 3.1 and then claim that thm 3.1 doesn’t always work

d. Figure 1 can not be deciphered with out a basic explanation\legend for the colors

e. Equation 6: is f_I_p(x_i) why is it defined only for x?

f. In equation (8) what is K in B=2K?

4. The computational complexity of O(mn) should be better explained? Wouldn’t the kernel construction cost more?

5. Overall Im not convinced at all that the approach of diversification and representativeness is an optimal one. There are other important trade offs in active learning such as exploration-exploitation, which can outperform this UPA approach, in my view.

### Questions
1.	Please see the questions above in the ‘weaknesses’
2.	Please explain what does the flexMatch method do , and why you chose it for your UPA approach.
3.	Why do you think the diversification and representativeness is the best one for AL?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper at hand proposes a sampling approach for selecting a smaller but still representative and diverse set from a large dataset. This is applied to the task of semi-supervised learning where the subset selection is applied to unlabeled data which is to be labeled later on.

### Strengths
+ relevant problem

### Weaknesses
 - limited comparison to other sampling methods (only random sampling)
- marginal improvement over random sampling (Tab. 1 overlapping confidence intervals)
- not clearly and convincedly presented advantages of the method (e.g., Fig. 2, it's hard to see the claimed benefits)
 
Honestly speaking ,I'm not sure that the chosen application is the right one. I would recommend focusing on the selection step to approximate the distribution (estimated from the large dataset) with few examples. Compare the proposed approach to related work, discuss pros and cons. Finally sketch various applications (including SSL) briefly which will benefit.

### Questions
How does the approach scope with low and high dimensions?
How does the approach scope with different distributions (overlapping, clusters well separated, etc.)?
What are limitations?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
