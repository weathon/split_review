# Breaking Neural Network Scaling Laws with Modularity

- Decision: Accept
- Scores: 5, 8, 3, 8

## Abstract
Modular neural networks outperform nonmodular neural networks on tasks ranging from visual question answering to robotics. These performance improvements are thought to be due to modular networks' superior ability to model the compositional and combinatorial structure of real-world problems. However, a theoretical explanation of how modularity improves generalizability, and how to leverage task modularity while training networks remains elusive. Using recent theoretical progress in explaining neural network generalization, we investigate how the amount of training data required to generalize on a task varies with the intrinsic dimensionality of a task's input. We show theoretically that when applied to modularly structured tasks, while nonmodular networks require an exponential number of samples with task dimensionality, modular networks' sample complexity is independent of task dimensionality: modular networks can generalize in high dimensions. We then develop a novel learning rule for modular networks to exploit this advantage and empirically show the improved generalization of the rule, both in- and out-of-distribution, on high-dimensional, modular tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper (1) constructs a simplified theoretical model of generalization (focused on the case of linear regression from what I believe to be a set of not-strictly-defined features), (2) provides empirical demonstrations that, at least in broad strokes, a sine wave regression task follows the predictions made by that model, (3) argues that in cases where the simple problem under consideration is modular (here meaning that it has k modules of size b which interact, rather than a full set of P features), better sample complexity can be obtained by using an explicitly modular parameter structure, and (4) provides some empirical support for this generalization behavior on another set of (this time modular) sine wave regression tasks.

### Strengths
- The paper focuses on an empirical task that lets them validate their ideas, but is realistic in terms of scope 
- The paper engages with an interesting problem of the structure of weights that allow for better generalization

### Weaknesses
 - The paper's notation, particularly in the initial presentation of the theoretical model, was confusing and felt under-explained. In particular I was confused by feature matrix (how did it get constructed from the inputs? What assumptions are being made about it? Why is it a matrix to begin with rather than a feature vector), and this confusion made it hard to understand future claims made in the paper (especially since the central claim was about the effect on generalization of _input_ dimension, which is mediated by the function implied in this feature matrix)
- The forms of the expected training and test loss could have been broken down in a clearer and more intuitive way, rather than simply being presented as not-very-comprehensible formulas 
- This paper assumes that the only way to benefit from the generalization behavior of modularity is to have explicitly modular structure; it would have been interesting if it had also engaged with whether modular data gives you generalization benefits without a parallel parameter structure (since in practice modern models seem to generalize well without the benefit of this)
- I'm still confused about how attention is a modular architecture by your definition of modularity, since, while attention mechanisms share weights between sequence elements, they do not have the property of modularity described here where the input features are explicitly subdivided and passed to different components
- While the authors have added more detailed explanation of both the confusing formulation of the feature matrix and the training/test loss in the comment here, the paper itself does not seem to have had these clarifications added, so my issue with the paper on that front still stands. I realize that this feature matrix formulation might be standard for those with specific familiarity with the Jacot paper mentioned, but I believe it is still quite unintuitive to the average ML researcher or practitioner, and without explanation this conceptual merging of features and parameters will continue to be confusing (if the feature matrix already has an output dimension of d, what is the W matrix doing? Is it just a dxd matrix mapping within output space? The shape of W is not explicitly stated, making this unclear).

### Questions
- What is the explicit definition of modularity being used? This concept was referenced without ever being really explicitly defined in a general-but-still-technical sense (and attention was given as an example). I ended up being confused about whether the focus was on independently functioning parts of a network, or shared weights in a more general sense .
- As mentioned in "Weaknesses": what assumptions are made in general about the structure of the feature matrix? It is indicated in the modular version of the model that arbitrary nonlinear transforms of the input are considered as valid feature matrices, but this isn't clarified for the first treatment of the model 
- Do the benefits cited require being correct about the number (k) of modules in the underlying data? How much do positive results depend on being correct in your choice of k relative to what is present in the underlying data?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper shows that the sample complexity associated with training modular neural networks is independent (under certain conditions) of the input dimensionality and does not follow the same exponential increase with input dimension as in the case of monolithic or traditional neural networks (NNs). 

First, the authors present a derivation of training and test error in monolithic NNs when the task is non-modular. The task and the NN are modeled linearly based on features generated using the input. The authors then, empirically validate that NNs with different architectures (loosely) match the theoretical trends when varying the input dimension, number of samples and the number of parameters. Note that the task considered for this experiment is modular. 

The authors then theoretically compute the training and generalization errors of modular NNs given that the underlying task is also modular with the same structure. Each module is associated with a small NN (modeled linearly) and an input projection mechanism that reduces the module input dimensionality. The task is also modeled in the same way where the parameters are randomly initialized. 

The resulting closed form solution shows that the training error is independent of the input dimension and the test error under the condition of under-parametrization is also independent of the input dimension. This result hinges on the input projection associated with each module, where the dimensionality associated with the overall input is reduced. The authors then propose a method to initialize (or learn) the parameters associated with the input projections. Once initialized the modular NNs are trained end-to-end. 

Empirical results show that modular NNs that are learned using the proposed initialization mechanism achieve significant improvements over monolithic NNs and modular NNs conventionally trained.

### Strengths
The theoretical derivations are sound and very well done, and the paper is well written. The authors did a good job showcasing how modular networks can be related to monolithic networks (based on certain linear assumptions).

Intuitively, modeling of the data, and learning of parameters related to module input bottlenecks make sense. This is similar to learning the connectivity associated with module input or limiting the number of module inputs to avoid module collapse. 

The experiments show a clear trend that the input projection mechanism results in better performance and sample complexity, as compared to monolithic NNs and end-to-end trained modular NNs.

### Weaknesses
The major weakness of the paper is the consideration of a single layer of modules and data generating system. In such a system the output is a linear composition of the module outputs. This may not be true for many real world systems where multiple such modular layers can exist in a hierarchy. The analysis and experiments are limited to a shallow modular architecture, which does not reflect the complexity of real-world modular systems that often exhibit hierarchical structures. This significantly limits the applicability of the theoretical results and the empirical findings. The assumption of a linear combination of module outputs is also a strong constraint, as many real-world systems involve non-linear interactions between modules. 

Continuing with the previous weakness, the algorithm to learn or initialize the input projection parameters may not work in such a case as it is dependent on the initial module NN weights. The proposed initialization method for input projections relies on the initial weights of the module networks. This creates a potential issue when extending to deeper modular networks, as the initial weights of modules in deeper layers would be influenced by the outputs of previous layers, making the initialization less effective. The method's dependence on the initial module weights makes it potentially unstable and less generalizable to more complex architectures.

For individual tasks considered, there appears to be a large amount of tuning of methodology to train the modular NNs and the module input projections. (Referring to appendix)

### Questions
Continuing with the previous weakness, the algorithm to learn or initialize the input projection parameters may not work in such a case as it is dependent on the initial module NN weights. 

The generalization performance for the compositional CIFAR-10 experiment can be divided into input class permutations present in the training data vs. not present in the training data to further dissect the difference between monolithic NNs and modular NNs. The sample complexity experiments with compositional CIFAR-10 tasks are not present and should be added to further strengthen the claims. 

For individual tasks considered, there appears to be a large amount of tuning of methodology to train the modular NNs and the module input projections. (Referring to appendix)

How would the solution to training and test errors change if the input projections from each module were removed, and the modules considered the input x in its entirety? This is consistent with the current mixture-of-exert (MoE) models. 
 
Is there a validation set used for the experiments or is the generalization performance reported from the last training iteration?

Do the modular NNs treat the number of modules as a hyper-parameter and tune it to improve the performance. Or is it an architectural characteristic such as the width or depth in monolithic NNs that is fixed ? 

The CIFAR-10 experiments are run only for a single epoch, will increasing the number of epochs result in better performance for networks? 


Minor: Equations are referred to the appendix when they are also present in the main part of the paper.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present both theoretical and algorithmic results regarding the generalization ability of a particular form of modular architectures. They first highlight theoretical results on generalization results showing exponentially large sample complexity as a function of the input dimension. Then they present a particular class of modular architectures as a sum of experts and assume that the training data was generated by this same architecture. They show that thanks to each module making a low-dimensional projection before processing the data, the scaling behavior is better behaved. Then they present a kernel-style algorithm to initialize such an architecture, to be then fine-tuned by usual supervised learning and SGD. Finally, they show results on a toy 1-dim sine-wave regression task and on the recently introduced compositional MNIST task.

### Strengths
Much remains to be understood about the generalization behavior of neural nets, especially the types that have a modular architecture, so advances on the theory (in special cases) that are presented do seem useful.

### Weaknesses
 (1) the theoretical results are not suprising: projecting the m-dim input to several b-dim low-dimensional representations unsurprisingly reduces the exponential badness from m to b. The theory is also of fairly limited scope, with lots of unreasonable assumptions (e.g., of linearity wrt parameters) that may not tell us as much as we would like for more general forms of modular architectures.

(2) the proposed algorithm is unlikely to scale well in terms of computational efficiency beyond small-size problems and into frontier AI, given the use of kernel methods in the novel part of the method

(3) the fact that all modules are initialized independently and using the same (randomized) procedure suggests that a significant part of the advantage could come from an ensemble effect (which always helps generalization)

(4) the paper seems to overclaim in multiple places, e.g., suggesting that their results tracks empirical behavior of modern neural nets (even the empirical comparisons don't match the theory, e.g., fig 2 bottom right).

(5) I did not find numerical comparisons against benchmark results from other papers, and when I look at Jarvis et al 2023, their figures show much lower errors. Hence the experimental results may not be that good after all.

### Questions
(1) I was confused by the results in figure 1, whereby test error INCREASES with larger datasets. This seems incompatible with empirical observartions and traditional statistical analyses of generalization.

(2) I did not understand in what sense the y_j could be considered independent (and what is the random variable), after eq 3.

(3) eqn 4 seems wrong: on the LHS y is a function of the linear projection U x, whereas on the RHS U and x only interact via the presumably non-linear function phi.

(4) why should we expect eqn 15 to give the minimum norm solution? (i.e. why is it a solution and why is it minimum norm, from what class)

(5) You should add the citation of the original mixture of expert papers (e.g. Jacobs et al 1991).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors study modular neural networks and their ability to learn functions that are themselves modular insofar as they have either a compositional nature or a modular composition in their statistics. The authors first provide a theorem outlining expected scaling laws for sample complaxitiy and trainign accuracy in a curated linear task setup. They then corroborate the predictions from this theorem with numerical experiments. Following this, they present a task setup with explicit ground-truth modular structure and prove a second theorem outlining similar sclaing propoerties for this novel tasks setup along with a particual modular NN architecture. The result is reduced scaling complexity for tusch tasks when NNs are appropriately modular. The authors then propose an initialization scheme for NNs which first learn module initialization in a self-supervised fashion using task statistics. Finally, the authors show that this approach behaves as expected on non-trivial tasks such as compositional CIFAR, and that the proposed method works well on other modular architectures beyond the one used for their theoretical results.

### Strengths
This paper presents an excellent set of theoretical results outlining expected scaling laws for modular networks when task have a modular structure. It also presents a practical initialization scheme for potential models that is based on self-supervised alignment with task statistics. Lastly, it validates predictions with non-trivial and relevant experiments with architectures that go beyond the ones used for theory, outlining the potential generality of the result.

### Weaknesses
The paper is sound. There are potntials for improvements in two key areas:

1. In experiments, it is unclear if the generalization advanatage of the modular networks remain if one factors in the pre-training (i.e. learning module initialization). In other words, for the same total compute, would a monolithic model do as well as the modular one for which some of the compute budget went toward initialization? My apologies if I missed it, but this is a key point that would factor into real-world scaling laws.

2. What happens if there is a missmatch between the task modularity and the NNm odule count? In experiments, the models could accurately recover tasks modularity when the number of modules is known. In contrast, in other tasks, this is not known a priori. How would the models behave in this mismatched environment? To be fair, the authors acknowledge this issue, but I wonder if some rapid experiments could outline expected behaviors in this case. Once again, apologies if this has been explored and I missed it.

3. While this is no doubt very relevant for the field, it's overall impact with respect to modern architectures remains unclear. Some discussion about the use of such methods in modern settings such as in the prsence of attention could greatly enhance the scope of the result. This is not necessary however, as this is a good paper in the current scope.

### Questions
See above

### Soundness
4

### Presentation
4

### Contribution
3
