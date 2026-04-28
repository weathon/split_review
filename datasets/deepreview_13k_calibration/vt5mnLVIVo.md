# Grokking as the transition from lazy to rich training dynamics

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 3, 8, 8

## Abstract
\looseness=-1 We propose that the grokking phenomenon, where the train loss of a neural network decreases much earlier than its test loss, can arise due to a neural network transitioning from lazy training dynamics to a rich, feature learning regime. To illustrate this mechanism, we study the simple setting of vanilla gradient descent on a polynomial regression problem with a two layer neural network which exhibits grokking without regularization in a way that cannot be explained by existing theories. We identify sufficient statistics for the test loss of such a network, and tracking these over training reveals that grokking arises in this setting when the network first attempts to fit a kernel regression solution with its initial features, followed by late-time feature learning where a generalizing solution is identified after train loss is already low. We find that the key determinants of grokking are the rate of feature learning---which can be controlled precisely by parameters that scale the network output---and the alignment of the initial features with the target function $y(x)$. We argue this delayed generalization arises when (1) the top eigenvectors of the initial neural tangent kernel and the task labels $y(x)$ are misaligned, but (2) the dataset size is large enough so that it is possible for the network to generalize eventually, but not so large that train loss perfectly tracks test loss at all epochs, and (3) the network begins training in the lazy regime so does not learn features immediately. We conclude with evidence that this transition from lazy (linear model) to rich training (feature learning) can control grokking in more general settings, like on MNIST, one-layer Transformers, and student-teacher networks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this submission, the authors proposed a simple regression model that exhibits the grokking phenomenon, that is, good generalization is achieved long after the decay of training error. The studied model is a polynomial regression problem, where the teacher model is a quadratic single-index model, and the student model is a neural network with degree-2 activation function. It is predicted that under suitable training set size and initialization scale, grokking occurs in the intermediate phase between the NTK regime and the feature learning regime.

### Strengths
The proposed toy model is interesting and relevant to the ICLR community. Most existing works on grokking considered modular arithmetic tasks, or measured the classification error rather than the surrogate loss used in training. In contrast, the authors studied the regression setting where grokking is manifested in the $L_2$ error, and the training procedure does not involve $\ell_2$ regularization. Also, the connection between grokking and the transition from lazy to rich regime is to my knowledge novel, and it opens up new directions for theory research to rigorously characterize such phenomenon.

### Weaknesses
I have the following concerns.

1. Given the idealized setting (Gaussian data with identity covariance, single-index target), it is rather underwhelming that the authors did not provide any quantitative characterization of the training dynamics to prove the existence of grokking. Instead, the proposed explanation is only verified empirically, which limits the contribution. The lack of theoretical analysis, such as a derivation of the gradient flow trajectory, leaves the underlying mechanisms of grokking unclear. Specifically, a more rigorous treatment would involve analyzing how the weight matrices evolve over time and how this evolution leads to the observed generalization behavior. The empirical verification, while useful, does not provide a deep understanding of why grokking occurs in this specific model. Can the authors comment on the technical challenges in analyzing the gradient flow trajectory for this quadratic model?

2. Connection to prior results needs to be further elaborated.

* (Nichani et al. 2022) also studied the transition from the NTK to the feature learning regime, and established improved sample complexity for learning low-degree + sparse high-degree polynomials. For the current model, does the sparsity of the higher-order term (that is, whether the quadratic component of the target function span more than one direction) play a role in the presence of grokking?   
(Nichani et al. 2022) *Identifying good directions to escape the NTK regime and efficiently learn low-degree plus sparse polynomials.*

* The target function is a single-index model with information exponent 2 (Ben Arous et al. 2021). It is known that for such target function, gradient descent on the population loss will start from an approximate saddle due to the random initialization. Is this observation related to the test loss plateau in grokking? And do we expect similar findings when the information exponent is larger than 2?   
(Ben Arous et al. 2021) *Online stochastic gradient descent on non-convex losses from high-dimensional inference.*

* The quantity describing the difficulty of target function $y^	op K^{-1} y$ has been extensively studied in the kernel literature. See (Arora et al. 2019) for the analysis of NTK.  
(Arora et al. 2019) *Fine-grained analysis of optimization and generalization for overparameterized two-Layer neural networks.*

* (minor) The cited references on the quadratic sample complexity lower bound for kernel estimators such as (Ghorbani et al. 2019) do not rigorously cover the case of Gaussian data.

### Questions
See Weaknesses above.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes that the "grokking" phenomenon—where a neural network's test loss decreases significantly after the training loss—is due to a shift from initial "lazy" training to subsequent "rich" feature learning. Through a polynomial regression study with a two-layer network, the authors show that grokking occurs when the network moves from fitting data with its initial features to learning new features for better generalization. They suggest that the rate of feature learning and the initial feature alignment are key to this delayed generalization, a concept potentially applicable to more complex neural networks.

### Strengths
This paper studies the grokking phenomenon in deep learning, which is a recent hot topic and very relevant to ICLR. This paper proposes that grokking can be triggered by the transition from kernel regime to feature learning regime. Though this is already known even before the grokking paper by Power et al, 2022, e.g., the example of quadratically overparametrized linear model in Section 6 of Li et al., 2021, the novelty here is that this paper focuses on vanilla GD. In contrast, the transition between kernel and feature learning regime, Li et al., 2021, is triggered by sharpness minimization implicit bias of label noise SGD, which makes the analysis significantly easier.  This paper also performed some new experiments on various tasks to support this theoretical intuition.

*Reference:*

Li, Zhiyuan, Tianhao Wang, and Sanjeev Arora. "What Happens after SGD Reaches Zero Loss?--A Mathematical Framework." arXiv preprint arXiv:2110.06914 (2021).

### Weaknesses
1. The definition of grokking seems to be very different than that in literatue. In Power et al., 2022, **Groking** refers to the phenomena that "long after severely overfitting, validation accuracy sometimes suddenly begins to increase from chance level toward perfect generalization". While this paper describes grokking in their introduction as "train loss of a neural network decreases much earlier than its test loss". 
	
	It is ok to me that this paper only focuses on the regression setting and talks about MSE loss. But the original grokking phenomenon is much more "suprising" and rare in the sense that it requires the test loss/error to get higher than random guess only after reaching almost zero training loss/error. Moreover, the original definition of grokking requires almost perfect generalization in the end of training.

2. The theoretical explanation presented in this paper only works for the new definition of grokking, but not the original definition of grokking in Power et al., 21. For the most experiments in this paper where the authors claim grokking happens, two criterions of original definition of grokking are not met: 1. when test loss starts to decrease before training loss gets small; 2. the eventual test loss is still high. Figure 5(b) is an example.

3. There is no end-to-end theorem about grokking. Given the modified definition of grokking, explanation using transition from kernel regime to feature learning regime seems quite straight forward. It should be very standard to show that there exists a period of time where training loss can decrease but test loss has a lower bound due to live in the kernel regime. Still this paper lacks such precise and rigorous statement.

4. I find it difficult to understand the math derivation for the toy model in section 11. In the paragraph above section 11.2, the authors write that kernel method can learn $|x|^2$ at D sample sizes and the full target function at $D^2$ sample sizes. How is this gap in sample complexity related to the sepration of timescale in a single run?

5. The first paragraph of Introduction does not sound correct. For example, the authors write that "Typically, one assumes that a model’s performance on its training set will be a reliable indicator of its generalization capabilities on unseen data". This is in general not true, especially in deep learning where models are often overparametrized. And it is exactly because training loss and test loss can have a large gap in practice, people are studying generalization in machine learning. Also it is not clear to me that why using models which groks in training will cause any safety issue. I would like the authors to elaborate on this or at least provide an example. Intuitively, grokking as a training behavior has nothing to do with the performance of the model when used for inference.

6. As mentioned in the strengths, the explanation of grokking using transition from kernel to feature learning regime (Li et al., 2021) is known even before the original grokking paper (Power et al., 2022). Though this paper is novel in the sense that it focuses on vanilla GD, which is more natural than Li et al., 2021, the theoretical result in this paper is also not as clean as that in Li et al., 2021.

### Questions
See weakness

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work hypothesizes that grokking may happen as a transition from lazy to feature learning regime. It also shows that grokking is not inherently associated with an increasing norm and the use of weight decay -- which advances our understanding.

### Strengths
I think the paper is clean and the point being made is sufficiently important. Also, I find the experiments sufficiently convincing. 

Crucially, it advances our understanding of the grokking phenomenon. The shortness of the review only reflects the fact that I do not much much criticism for this work.

### Weaknesses
Nothing major.

### Questions
One point I think worth being clarified is the role of weight decay. I think we have a pretty good understanding of how weight decay changes the kernel. Essentially, weight decay almost always changes the NTK at the speed of $\kappa$, which is the strength of weight decay. The time scale for the effect of weight decay to take place is nothing but $1/\kappa$. Therefore, if $1/\kappa$ is far larger than the time scale of lazy training, one has a separation of time scale, where lazy training happens first, and feature learning induced by weight decay happens later. I think the authors should make more discussion on this point as it constructively adds to the paper.



------

This part is updated to acknowledge that I have read the author response.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the grokking phenomenon and argues that the drop in test loss (after the drop in train loss) coincides with the network transitioning from the lazy to the rich regime. Grokking would then happen when the NTK at initialization is ill-aligned with the task, leading to a large test error in the lazy regime, however after the transition to the rich regime, the `right' features are learned.

They study a simple model of shallow nets that can fit linear and quadratic function, with a hyper-parameter that allows one to tune how much stronger the alignement of the initial NTK with the linear modes than quadratic ones. For a quadratic true function, one can ensure a bad alignement between the NTK and task, thus leading to grokking.

Finally this theory is tested on more practical examples (MNIST with a MLP and arithmetic with a transformer architecture).

### Strengths
There has been a lot of work studying grokking in different settings, but we are still lacking a complete understanding of under which condition it appears (model, training method, task). I think that the lazy/rich transition is the right idea to understand grokking.

Under this interpretation, we expect grokking to appear in tasks that are adapted to the rich regime but not the lazy regime. Furthermore, we need models that exhibit both rich and lazy regimes, and finally we need a training method where the model switches from lazy to rich regime in the middle of training.

The authors identify a simple theoretical model that exhibits grokking, and its simplicity allow for some theoretical results. The numerical experiments suggest that their interpretation applies to more realistic setups.

### Weaknesses
The theoretical and experimental evidence given in the paper is not particularly strong: in spite of the simplicity of the model considered, the theoretical results are very limited (just a decomposition of the loss into three terms with relevant interpretations); conversely most empricial results are done on this simple model, with just three experiments done on more complex data.

You argue in a few different places that grokking when the NTK is ill-aligned to the task, but it feels to me that another condition is that the task needs to be well adapted to the rich regime (which I understand is much harder to characterize). There are tasks where neither the lazy nor the rich regime generalize, in which case one expects no grokking.

In section 6.1 you select a true function that is explicitely ill-aligned with the initial NTK to induce a grokking phenomenon, but the grokking phenomenon disappears when using too small eigenvalues. You argue that this is because there is not enough data, did you test this hypothesis? Could it also be the case because the eigenfunctions corresponding to small eigenvalues are hard to learn regardless of the regime (as I propose above)?

### Questions
You argue in a few different places that grokking when the NTK is ill-aligned to the task, but it feels to me that another condition is that the task needs to be well adapted to the rich regime (which I understand is much harder to characterize). There are tasks where neither the lazy nor the rich regime generalize, in which case one expects no grokking.

In section 6.1 you select a true function that is explicitely ill-aligned with the initial NTK to induce a grokking phenomenon, but the grokking phenomenon disappears when using too small eigenvalues. You argue that this is because there is not enough data, did you test this hypothesis? Could it also be the case because the eigenfunctions corresponding to small eigenvalues are hard to learn regardless of the regime (as I propose above)?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
