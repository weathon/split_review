# Unified Neural Network Scaling Laws and Scale-time Equivalence

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 6, 3, 3

## Abstract
As neural networks continue to grow in size but datasets might not, it is vital to understand how much performance improvement can be expected: is it more important to scale network size or data volume? Thus, neural network scaling laws, which characterize how test error varies with network size and data volume, have become increasingly important. However, existing scaling laws are often applicable only in limited regimes and often do not incorporate or predict well-known phenomena such as double descent. Here, we present a novel theoretical characterization of how {\em three} factors --- model size, training time, and data volume --- interact to determine the performance of deep neural networks. We first establish a theoretical and empirical equivalence between scaling the size of a neural network and increasing its training time proportionally. Scale-time equivalence challenges the current practice, wherein large models are trained for small durations, and suggests that smaller models trained over extended periods could match their efficacy. It also leads to a novel method for predicting the performance of large-scale networks from small-scale networks trained for extended epochs, and vice versa. We next combine scale-time equivalence with a linear model analysis of double descent to obtain a unified theoretical scaling law, which we confirm with experiments across vision benchmarks and network architectures. These laws explain several previously unexplained phenomena: reduced data requirements for generalization in larger models, heightened sensitivity to label noise in overparameterized models, and instances where increasing model scale does not necessarily enhance performance. Our findings hold significant implications for the practical deployment of neural networks, offering a more accessible and efficient path to training and fine-tuning large models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper put forward the hypothesis that increasing the training time model is in direct relationship with the model size: a small model trained for a long time is functionally equivalent to a larger model trained for a shorter time. The authors devise a simple theoretical model where this behavior can be analytically shown. They also experimentally show how this can be empirically verified in neural network training, and how their theory fits in the double descent phenomenon. The experimental results are achieved with MLPs and CNNs on computer vision benchmarks such as SVHN, CIFAR-10 and MNIST.

### Strengths
1. The idea of functional equivalence between models at different scales is potentially very attractive for modern practices of neural network training, where the (training) compute-optimal trade-offs have to be balanced with the potential benefits of having a smaller model at inference time. 

2. The idea of formalizing the relationship between training time and scale is also interesting from a theoretical perspective. In gradient descent, training time has been linked to various forms of explicit regularization, and theoretically investigating its connection to model scale is especially interesting in the context of neural scaling laws.

### Weaknesses
I think that despite the captivating and well-posed questions, the paper fails to deliver on several aspects. Namely:

1. The authors claim to theoretically demonstrate that scaling the size of a neural network is equivalent to increasing its training time. The connection between the model studied here and neural networks is unclear/misleading, and some design choices are not thoroughly explained. The theoretical model has the unusual structure of equation 2, which has no connection to theoretical models for neural networks. Also, the model is linear. Also, why are $r,p,P$ all different? Why couldn’t you only have a large dimensional ambient space and a constant-sized low-rank subspace?

2. I would have appreciated it if the connection to neural networks were toned down, and the proposed model motivated in its own right. I do not understand why the authors haven't studied more established settings, where for instance the double descent phenomenon has been shown, or where scaling laws have been tractably derived. Starting from there, it would be nice to understand which (and why) additional assumptions have to be made. With this respect, why haven’t the authors approached the problem from more standard settings in neural network theory (e.g. teacher-student [1] or random feature models [2])?

3. The concept of *minimal capacity to fit the data to a certain loss level* is crucial here, but never satisfiably addressed. In fact, an underlying assumption that is never made by the authors is that the model can fit the data at any scale (only stating “Consider a large $P$ dimensional model”). Otherwise, it would not be possible for a small model to match the performances of a large model, no matter how long the small model has been trained (e.g. imagine training a model with very small width on complicated datasets).

4. The definition of **model scale** as $N^{1/3}$ ($N$ is the number of parameters) put forward by the authors is a heuristic, which is not convincing enough given its importance in the experiments on neural networks. More concretely, the authors define the model scale as "the maximum number of training points that can be fit by the network", which is set to $N^{1/3}$. The number of training points that can be fit by a model is a well-studied and hard problem. For arbitrary data points, the complexity of a function class determines how many data points can be fit. In general, it depends on the data's complexity and the model's flexibility. I find that the cube root of the number of parameters is arbitrary and ignores the data dependence. As the authors detail in the “experimental details” Section in the appendix, *“The width parameter was set to values of 1, 2, 5, 10, 20, 50, and 100. When we refer to ”model scale”, we quantify this as the cube root of the number of network parameters rather than the value of the width parameter.”* In the current form, the scale-time equivariance narrative heavily relies on the cubic root assumption, and the heuristic argument provided is insufficient considering its importance in the paper’s narrative. 

5. In section 5.3, it is assumed that larger models have a smaller time to interpolation threshold. However, in the experiment of Figure 5, it appears that interpolation has not happened yet, as there are no U-shaped curves, which are the footprint of double descent. It would be nice to reproduce some of the results on double descent both in model size and training time to better substantiate some of the claims. In this sense, we would expect the interpolation threshold (peak of double descent curve) to vary with model size and training time predictably according to the scale-time equivariance theory. 

6. The authors only test two learning rates, which makes it impossible to establish whether the chosen learning rate is optimal. Also, usually the optimal learning rate shifts with scale, and this is not addressed by the authors. 

7. It is well-known that there is a correspondence between training time and regularization strength (e.g. [3]). The proposed theory put forward the interesting hypothesis of a similar connection between training time and model scale. I would say that mentioning this line of work would better help this paper’s positioning in the current literature. 

8. In lines 367-269 a few articles “the” missing: If noise components →  if the noise components, etc..

### Questions
See weaknesses.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper analyzes a simple proxy model for neural network optimization, gradient flow on a random feature model. It theoretically shows that under certain conditions, particularly on the complexity of the objective function and Lipschitz continuity of the gradients and second derivative, the speed of convergence depends on the product of the model size and time. The authors interpret this result as an equivalence of time and scale in optimization. The paper experimentally explores whether this relation holds for very small scale MLPs and conv-nets on simple vision tasks like MNIST and CIFAR. They then use time-scale equivalence to offer additional insights into double descent in terms of training time, parameter count and dataset size.

### Strengths
- An interesting theoretical take on scaling and double descent.
- Mostly well written, clear figures.

### Weaknesses
 - The claims made in the paper seem too strong. The abstract mentions theoretical characterization of deep neural networks multiple times but the paper only theoretically analyzes simple proxy models. It also mentions large scale neural networks but all experiments in the paper are performed on small MNIST / SVHN / CIFAR networks. The same goes for the claims in the contribution list in the introduction.
- The paper does not sufficiently discuss its limitations (e.g. in terms of the weaknesses mentioned here).
- The neural network experiments are done on very small scale vision tasks which is typically not where neural scaling laws are valuable.
- The applicability of the random feature model analysis to neural networks is not sufficiently justified.
- Some parts of the paper are not very clear (see below).

**Edit: The authors have promised changes that I believe would sufficiently address these weaknesses. Conditioned on those changes I no longer have significant concerns and have raised my score.**

### questions:
 S3.1: I think this section in general is not very clear and could benefit from additional explanations and better arguments for the applicability to neural networks.

L130: Neural networks with SGD often converge to flat minima when trained with a high learning rate. However, I am not sure the projection K would be fixed throughout training nor that a gradient flow model can capture the same behavior.

L139: Here you give an example of how a small neural network can be seen as a subnetwork of a larger model. This would likely imply setting various weights to zero or one for identity and so on. This would likely not be a random matrix that looks anything like R.

L152: Why can you assume that eta is not a function of p? In actual neural network training the learning rate often varies with the width and depth of the network being trained (see e.g. various muP literature).

L209: What do you mean by “minimum amount of training time required to achieve non-zero generalization”?

L244: The cube root argument should also be justified in the main body along with its applicability to neural networks. The model this is derived for seems a lot closer to the previous theoretical model than neural networks so only applying it to neural networks feels odd.

L252:  Why not tune your learning rates in general? As mentioned before, the learning rate often varies with the network width and depth. Using a fixed rate seems unprincipled.

S4: This section is very light on details. Overall the paper feels a bit crammed, trying to cover more material than can be done well on 10 pages.

### Questions
S3.1: I think this section in general is not very clear and could benefit from additional explanations and better arguments for the applicability to neural networks.

L130: Neural networks with SGD often converge to flat minima when trained with a high learning rate. However, I am not sure the projection K would be fixed throughout training nor that a gradient flow model can capture the same behavior.

L139: Here you give an example of how a small neural network can be seen as a subnetwork of a larger model. This would likely imply setting various weights to zero or one for identity and so on. This would likely not be a random matrix that looks anything like R.

L152: Why can you assume that eta is not a function of p? In actual neural network training the learning rate often varies with the width and depth of the network being trained (see e.g. various muP literature).

L209: What do you mean by “minimum amount of training time required to achieve non-zero generalization”?

L244: The cube root argument should also be justified in the main body along with its applicability to neural networks. The model this is derived for seems a lot closer to the previous theoretical model than neural networks so only applying it to neural networks feels odd.

L252:  Why not tune your learning rates in general? As mentioned before, the learning rate often varies with the network width and depth. Using a fixed rate seems unprincipled.

S4: This section is very light on details. Overall the paper feels a bit crammed, trying to cover more material than can be done well on 10 pages.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper aims to build a theoretical model for the scaling laws of neural networks as a function of model size, training time and data volume. The focus of the paper is to show the existence of “scale-time equivalence”, meaning that in the training of a neural network, one can trade off parameters for training smaller models on more data. The authors also analyse double descent in the framing of their linear model, proposing that epoch-wise double descent happens when small models learn noisy features first from the data.

### Strengths
The paper studies an interesting phenomenon, relevant to practitioners and in line with the current trend in literature of scaling laws: can we train smaller models on more data without sacrificing performance? The authors also test their claims empirically on multiple datasets and architectures.

### Weaknesses
To begin with, in Section 3.1, the authors introduce a random subspace model as a toy setting to study their scaling argument. Could the authors explain why this model is a good approximation for what happens in the case of a neural network, as well as provide citations to prior works using a similar model (i.e. in line 127)? For example where does the input data get used in this model? What is the loss used to train model? It would help for the authors to expand with more details the setup they are working with.

My biggest critique however is that it seems to me that the bound that the authors get in Equation (4) is vacuous, for the following reason. Naively, the rhs of (4) seems to be dominated by $e^{pt}$ term. Thus, if we increase the number of parameters (or the training time, or both), the distance between $\alpha_t$ and $A_{pt}$ is upper bounded by a quantity that grows exponentially fast. Could the authors explain more what they mean in this case? Following the proof, I do not understand where $A_{pt}$ appears from in Eq. (36). Could the authors please elaborate?

It would be very helpful if the authors could provide more information with respect to the empirics. Several plots tend to be vague i.e. “darker lines indicate a smaller error threshold” - what is the actual value?, “darker lines indicate more data” - same question.

Continuing to Section 4, Figure 3 Column 2 seems to have incomplete traces for the “predicted” (dashed) lines. Could the authors explain what happened in this case?

In Section 5, the analysis of the linear model seems very similar to the analysis done in the seminal work of Advani and Saxe. While the authors rightfully cite this work, it is not clear to me what their analysis provides on top of the existing work.

Conceptually, I am unsure of the claim in line 505: “model scale and training time can be traded off with each other.” Suppose I take an overparameterized model with $p$ parameters that is able to interpolate the data in a fixed number of training steps $t$. Based on this claim, I should be able to make $p$ much smaller, up to the point of making the model underparameterized, if I increase $t$ proportionally - however, in this case, my model will not be able to train to convergence. It seems that the authors are claiming that the capacity of the model is determined by the product $pt$, which is not standard in the literature. If $p < D$ (where $D$ is the intrinsic dimension of the data), then the model will not be able to fit the training data, regardless of how large $t$ is.

### Questions
What are the empirical details used to run Figure 4?

Conceptually, I am unsure of the claim in line 505: “model scale and training time can be traded off with each other.” Suppose I take an overparameterized model with $p$ parameters that is able to interpolate the data in a fixed number of training steps $t$. Based on this claim, I should be able to make $p$ much smaller, up to the point of making the model underparameterized, if I increase $t$ proportionally - however, in this case, my model will not be able to train to convergence. 

If the authors are open to discussion and to provide more details on their setup, I am willing to increase my score.

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
3

### Summary
This work presents theoretical and empirical characterizations of how the model size, training time and data size affect the performance of neural networks. The authors first establish a scale-time equivalence in a linear model trained with gradient flow. They then conduct simulations on MNIST to verify their finding. Moreover,  the authors combine the scale-time equivalence with an analysis of the linear model to provide new interpretations of previously unexplained phenomena in double descent. Simulation results on CNN and MLP corroborate their interpretations.

### Strengths
The paper provides novel explanations to double descent and other unexplained phenomena based on analysis of linear models.

### Weaknesses
The theoretical derivations in this work are limited to simple linear models. It is unclear to what extent these observations hold in large models and other optimization settings.

* For example, Theorem 1 assumes the model is trained via gradient flow (which is close to full-batch GD), while in practice it is recommended to use one-pass SGD/Adam. Theorem 1 seems to lack a characterization of how the sample size correlates with the training time. This differs from the setting under which the authors conduct the simulations (mini-batch SGD).

* Also, the scaling laws (eq 9,10) are derived for linear models. However, the discussions in section 5.2-5.5 are for more general models, and are heuristically built upon these equations and some implicit assumptions on the signal and noise components. There lack precise and rigorous characterizations of the test error for nonlinear models/neural networks.

* Lack a discussion of more recent works on explaining neural scaling laws: e.g., [1,2]. In particular, [1] studied the scaling laws in linear model trained via one-pass sgd. I wonder how results in [1] reconcile with Theorem 1 in your work.

* I would appreciate an explicit discussion of the limitations of this work.

### Questions
Apart from the points in weakness, here are my additional questions.

* In Figure 2, how is the batch size chosen? Would different choices of batch size affect the result?

* How is eq 10 derived from eq 9? My understanding is that M can be interpreted as the model size in linear models. Thus, eq 10 corresponds to the case $M\to\infty$ and it is unclear what the parameter size $p$ is.

### Soundness
2

### Presentation
3

### Contribution
2
