# Elliptic Loss Regularization

- Decision: Accept
- Avg Score: 5.50
- Scores: 3, 8, 6, 5

## Abstract
Regularizing neural networks is important for anticipating model behavior in regions of the data space that are not well represented. In this work, we propose a regularization technique for enforcing a level of smoothness in the mapping between the input space and the loss. We specify the level of regularity by requiring that the loss of the network satisfies an elliptic operator over the data domain. To do this, we modify the usual empirical risk minimization objective such that we instead minimize a new objective that satisfies an elliptic operator over points within the domain. This allows us to use existing theory on elliptic operators to anticipate the behavior of the error for points outside the training set. We propose a tractable computational method that approximates the behavior of the elliptic operator while being computationally efficient. Finally, we analyze the properties of the proposed regularization to understand the performance on common problems of distribution shift and group imbalance. Numerical experiments empirically confirm the promise of the proposed regularization technique.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a new regularisation scheme, elliptic loss regularisation, based on optimising a pseudo loss surface which is the solution a Dirichlet boundary value problem. This regularisation scheme is designed to increase the robustness of models to data shift and imbalance. The authors perform experiments to verify some of their claims which shows that elliptic loss regularisation increase performance over other regularisation schemes like mixup in several settings.

### Strengths
* I believe the paper proposes quite an original way to perform loss regularisation by defining and basing the regularisation on a pseudo loss surface. I also think the way they define this loss surface as the solution to a boundary value problem is an interesting perspective. 

* I think that the paper covers a wide range of experimental settings, from data imbalance to distribution shift. Additionally, across most of these settings elliptic loss regularisation has good performance compared with the given baselines.

### Weaknesses
 * I think the greatest weakness of the paper is the lack of clarity and motivation around the actually implemented approach. If this can be fixed I will likely increase my score. I have listed below a few specific points about clarity.
    * The most significant part of this lack of clarity is how they define the boundary of their pseudo loss surface. I can find nowhere where it is precisely defined and from my understanding for a Dirichlet boundary value problem to be solvable and hence for their theorical motivation to be true the boundary needs to satisfy certain conditions. By reading the paper it seems to me that the authors either assume the boundary to be the set of training data points or the edge of the convex hull of the training points. However, if the boundary is just the training points, then it is discontinuous and to the best of my knowledge not really a boundary in the sense used in defining the Dirichlet boundary value problem. While if it is the edge of the convex hull of the training data then you do not generally have the value of the loss for the whole boundary and hence can’t use it.
    * In section 5.1 they correctly point out that their approximation needs to be motivated by showing that it maintains the important properties of the true solution. However, I could not find anywhere a justification of why their approximation is accurate. This justification should be clearly presented in the paper to see how near the actual method is to the theory. 
    * There seems to be an overloading of the word ‘loss’, to make the paper clear I think there needs to be a clear distinction between the true loss and the pseudo loss surface created by the method. 
    * Another weakness is that a lot of the theory proved about the robustness of elliptic loss regularisation is only about the pseudo loss surface. However, except at the boundary, no connection is made between this loss surface and the true loss. This currently makes a large part of the theory lack practical use and I think a clear theoretical justification for why the pseudo loss surface will model the true one needs to be given. For example, at the moment, I could propose my own loss surface, perhaps a constant function with its value being the mean of the training loss, and prove similar propositions to propositions 1 to 3 while knowing that my loss surface is not similar to the true one at all. 

* While the predictive performance of a model using elliptic loss regularisation is shown to be good, I could not find mention of the computational cost of the method. It seems to me that the method could be quite computationally costly compared to other methods and hence I think a mention of the computational cost of elliptic loss regularisation should be given.

* One final weakness is that the baselines compared to in the paper a relatively old and there are perhaps better ones to use. However, I am not sure what they are and hope that my other reviewers can point out relevant newer baselines, if they exist.

### Questions
****1.**** In the experiments are standard data augmentations used in combination with elliptic loss regularisation and the baselines?

****2.**** Is there a typo on line 166 as $u$ there is defined as a function with the first argument being $f(X)$ not $X$. 

****3.**** Eq 6. is confusing to me, specifically the term inside the second expectation seems to be constant over the second expectation, is this a typo or am I missing something?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a novel regularizer for machine learning problems. The key insight is to construct a training objective (a “loss landscape”) that solves an elliptic PDE with boundary conditions specified by the unregularized loss’ values at the training points. This ensures that the regularized objective cannot be too large away from the training data: In particular, the loss landscape obeys a maximum principle, which implies that the regularized loss is upper-bounded by the maximum of the unregularized loss at the training points.

As it is impractical to exactly solve a PDE in each training iteration, the authors propose a numerical scheme to approximate the loss landscape. This scheme amounts to sampling pairs of training samples within each minibatch with importance weights inversely proportional to their distance, and then evaluating the training loss along paths connecting these pairs of points. The authors then prove two propositions to illustrate how the properties of the loss landscape can be used to predict the behavior of their regularized loss under affine distribution shift and data imbalance. They finally conduct a range of experiments which show that their regularizer performs comparably to baseline methods on problems without group imbalance or distribution shift, better than one-stage but often worse than two-stage baselines in settings with unbalanced populations and domain shift, and significantly better than baseline methods in class-imbalanced problems.

### Strengths
- Elliptic loss regularization is a neat and well-motivated method for obtaining generalization guarantees via a maximum principle.
- I appreciate the authors including examples of how one might use the properties of their loss landscape function to predict the effects of distribution shifts and class imbalances.
- The experiments are thorough and adequately study the performance of elliptic loss regularization in a variety of plausible settings.
- The paper is well-written and generally easy to follow.

### Weaknesses
My main critique of elliptic loss regularization is that it results in sometimes marginal performance improvements (such as in Table 5) over simpler and cheaper baselines. The authors could further strengthen the case for their regularizer by showing that using their numerical scheme, the computational cost of elliptic loss regularization is not much greater than that of simple mixup baselines.


### Questions
- Why use Brownian bridges to connect pairs of training samples in the numerical procedure detailed in Sec 5.1? Is there any practical advantage to Brownian bridges compared to simply sampling along line segments connecting pairs of training samples (as with mixup)?
- As I understand, the training algorithm essentially amounts to sampling pairs of nearby training points (distant pairs are presumably sampled with negligible probability), and evaluating the training loss along paths connecting these pairs. If this is correct, is it reasonable to view elliptic loss regularization as a variant of mixup where the interpolated points are more likely to remain on the data manifold? This seems like an intuitive perspective on why one might expect this method to perform well on manifold-supported data embedded in high-dimensional space, which is true of much real-world data under the manifold hypothesis.
- How costly is elliptic loss regularization relative to simpler baselines like mixup? The proposed method’s performance improvements over baselines are sometimes marginal (see e.g. Table 5), and I wonder if the additional cost of the numerical scheme to approximate the regularized training objective is worth the marginal improvements in such problems.
- Why are worst-case results not reported for the Camelyon17 dataset in Table 4?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new regularizer based on elliptic loss landscapes. The high-level idea is to imbue the loss landscape of a model with a certain kind of smoothness that allows the loss to be bounded in unseen regions of the landscape. This allows the loss to be bounded under data distribution shifts and data imbalance. In practice, the regularizer works by training on the loss evaluated on paths between data points. Experiments show the experiment is effective on CIFAR, TinyImagenet and distribution shift tests.

### Strengths
**Originality**

The paper seems quite original- I don't believe previous works have considered using elliptic loss landscapes and the resulting bounds one can derive (in Proposition 1) seem quite powerful. There are previous works exploring other forms of data augmentation (such as mixup) to improve generalization, but I believe few have the strong theoretical guarantees of the proposed method.

**Quality**

Overall, the quality of the paper is strong: the theory looks sound and experiments seem adequate.

**Clarity**

The main text of the paper is adequately written and figures and tables are well-illustrated.

**Signifiance**

The paper proposes a new way to bound the loss on unseen points far from any previously observed points, which is generally a very challenging problem. As such, I expect the theory proposed in this paper alone to have great significance to researchers finding ways of improving generalization, and I expect future work would build on the theory in this paper.

### Weaknesses
Regarding the theory, the practical algorithm requires sampling which would likely lead to a gap between the true elliptic loss and the computed loss. Can the authors comment on whether Proposition 1 would theoretically still hold under the sampling technique? Ideally, the error resulting from the sampling process can be bounded.

Also, unfortunately, it seems that the improvement of the method over previous techniques (particularly mixupE) seem small for CIFAR which raises questions about how effective it is at in-distribution generalization. Similarly, the results for domain shift in Table 4 and Table 5 do not seem conclusive in favoring the proposed regularizer.

Clarity-wise, the introduction of elliptic loss landscapes and the proposed algorithm seem a bit confusing due to the complexity of the technique. I would suggest adding an additional figure in the main paper illustrating the nice properties of the loss landscape described by eqns 1 and 2. I would also suggest including an algorithm in the main paper to accompany section 5.1

### Questions
Can the authors bound the error of the sampling procedure?
Can the authors explain why the performance of the method is worse in some-cases than other baselines (such as mixupE)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work proposes a regularization technique for a loss landscape where ideas are taken from Partial Differential Equations (PDEs) so that one can impose properties on the landscape. The loss landscape satisfies an elliptic operator allowing thus to bound it on the interior of the domain using the observed points. By doing so one can anticipate the behaviour of the error for points outside the traing set and thus addressing  two important problems : Data shifts and Data imbalance.
In this context, a tractable computational method that approximate the elliptic operator is proposed and various experiments are done trying to show its efficiency.

### Strengths
This paper addresses an important problem in machine learning : data shift and data imbalance

### Weaknesses
Although the addressed problem is important the proposed technique to tackle it is not clear nor justified.
First the related work is poor and it's not related to what is proposed in the paper. Thus, after some enumeration of past work on mixup, it's just stated that "these findings motivate our work where we consider a different type of regularization and its implication on the loss values". This should be motivated and explained.  
Then, ERM vs TRM is introduced by saying that the latter may cover more of D depending on how \phi is chosen, but nothing is said on the price to pay for that.
The equation (1) (line 171) is not explained nor justified and as  this equation is the core of the proposed approach, it would be beneficial to explain its derivation
How the equation (1) leads to equation (3) ? the derivation is not clear and there is no details in the appendix
After that, the generalization of the operator through equations (4) and (5) is not clear and the Appendix does not help for that

### Questions
1) How the PDE can be justified here ? Why not using OOD technique (for data imbalance) and domain adaptation (for data shift) ?
2) there is a reference to the Dirichlet problem in the introduction but nothing is said about it in the rest of the paper.
3) Why you did not compare to a recent Mixupe approach as Yingtian Zou (2023) (see the last reference).
4) Experiments reflect Mean and Worst, why just these two metrics and not for instance the Best ?

### Soundness
2

### Presentation
2

### Contribution
2
