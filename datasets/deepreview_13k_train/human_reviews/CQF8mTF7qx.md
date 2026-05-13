# Simplicity Bias of SGD via Sharpness Minimization

- Decision: Reject
- Scores: 6, 5, 8, 5

## Abstract
The remarkable generalization ability of neural networks is usually attributed to the implicit bias of SGD, which often yields models with lower complexity using simpler (e.g. linear) and low-rank features (Huh et al., 2021). Recent works have provided empirical and theoretical evidence for the bias of particular variants of SGD (such as label noise SGD) towards flatter regions of the loss landscape. 
Despite the folklore intuition that flat solutions are 'simple', the connection with the simplicity of the final trained model (e.g. low rank) is not well understood. 
In this work, we take a step towards bridging this gap by studying the simplicity structure that arises from minimizers of the sharpness for a class of two-layer neural networks.
We show that, for any high dimensional training data and certain activations, with small enough step size, label noise SGD always converges to a network that replicates a single linear feature across all neurons; thereby implying a simple rank one feature matrix. To obtain this result, our main technical contribution is to show that label noise SGD always minimizes the sharpness on the manifold of models with zero loss for two-layer networks. 
Along the way, we discover a novel property --- a local geodesic convexity --- of the trace of Hessian of the loss at approximate stationary points on the manifold of zero loss, which links sharpness to the geometry of the manifold. This tool may be of independent interest.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the implicit bias of SGD on two-layer neural networks. The paper theoretically proves that:
1. A variant of SGD (with label noise) converges to the global minimizer with zero loss under a small learning rate;
2. The converged global minimizer has a globally minimal trace of Hessian among all global minimizers of the network;
3. At the converged point, for each data, the pre-activations are the same among all hidden neurons.
Note that 2 and 3 together imply that the flattest minimum (i.e., with the smallest Hessian trace) is also the "simplest" minimum in the sense of having a rank-one feature matrix. Thus, the simplicity bias and sharpness minimization bias suggest the same solution in this setting.

### Strengths
1. Using a very clean framework, this paper theoretically justifies two popular conjectures: 1) sharpness-reduction implicit bias implies simplicity bias in neural networks; 2) label noise SGD converges to the global minimizers of the sharpness on the manifold of zero loss.

2. This paper considers a much more general framework than existing work, i.e., a two-layer neural network (with arbitrary width and fixed output weights.

### Weaknesses
1. The assumption of fixed output weights avoids a key difficulty in analyzing neural networks --- symmetry in the output space. Such symmetry renders the global minimal to form a connected plateau. Also, excluding the output weights in optimization space also avoids dealing with variable coupling. This simplification unavoidably loses some important nature in neural network training. Specifically, by fixing the output weights, the analysis bypasses the non-convexity introduced by the output layer's weights, which is a crucial aspect of the optimization landscape in neural networks. This simplification makes the theoretical results less applicable to practical scenarios where all weights are optimized simultaneously, and the interplay between different layers is essential for the overall learning dynamics.

2.  The assumption of a larger input dimension than the number of samples deviates a lot from practical settings. In particular, such an assumption (together with the choice of activation) ensures the realizability of the model (i.e., zero minimal loss) regardless of the network width. However, in most practical settings, the input dimension is much smaller than the number of data samples, and the realizability is usually achieved by sufficient network width. This assumption essentially guarantees that the data is linearly separable in the input space, which is rarely the case in real-world problems. By assuming a high-dimensional input space, the paper sidesteps the challenges associated with under-parameterization and the need for the network to learn complex feature representations, which are key aspects of neural network training in practice.

### Questions
Other questions and concerns: 

1. There are a number of typos. For example, on page 4: "Equation equation 1", "non=degeneracy", "equipp".

2. Page 4: "This is mainly for the ease of exposition and our results generalize to any fixed choice of weights of the second layer, in which the φ′′ image of the feature matrix becomes rank one." I don't understand why this is related to φ′′ (I suppose this is the second-order derivative of φ).

3. Page 5: "In Lemma 15, we show that θ(t) remains in a bounded domain along the gradient flow, which means having the weaker assumption that φ′, φ′′′ > 0 automatically implies Assumption 1 for some positive constants ρ1 and ρ2." I am not fully convinced by this claim. Lemma 15 is also established based on Assumption 1. Thus, if we do not have positive lower bounds on φ′, φ′′′, Lemma 15 may not hold and θ(t) may not stay in a bounded region.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper under study presents results on the link between sharpness minimization and the simplicity bias that has been observed many times throughout neural networks training tasks.

More precisely, they study the result of the Trace of Hessian minimization program proposed by Li et al. (2021), on a problem parametrized by a one hidden layer neural network with fixed to 1 outer layer. 
They show that such a simplicity bias happens.

### Strengths
A strength  of the paper is that the result is clear: for the specific prediction function, the asymptotic flow described in Li et al. (2021), shows a simplicity bias and converges.

### Weaknesses
 The results and the way the paper is articulated lacks clearness and some parts are largely overclaimed. Here is a list of potential improvement regarding these:

- First, *it has to be clear that the authors consider* the Li et al. asymptotic flow for granted. They study it in a particular setting of the neural network with frozen outer layer and specific activation. Let me reming the authors that the result of Li et al is only asymptotic and the regime of label noise + step size + time scale that is described in this is not general at all. In other words, they should clarify this explicitly when stating their result (eg theorem 1).

- Second, the authors claim that *for the ease of the exposition*, they set the second layer to one. If there is not clear proof of the fact that the result can be adapted from this, I do not believe it it an easy step to adapt their result to such a setup. Even though I do not expect things to change qualitatively.

- Third, the Assumptions 1 and 3 on the activation function seems very restrtictive: relu, sigmoid or tanh, which are the popular ones do not seem to be covered.   

- Finally, even though the Theorem 1 is informative, there is a need for more precision at this stage. To be concrete, there is  no clear definition of label noise SGD, no quantitative dependency on the step size and the noise of SGD… and for a fact: Li et al. result is asymptotic and non quantitative in essence.  Any quantitative and non-asymptotic result on this program is significantly difficult to obtain, see e.g.  **Label noise (stochastic) gradient descent implicitly solves the Lasso for quadratic parametrisation**, L. Pillaud-Vivien, et al. COLT 2022 on a specific prediction function.

On the simplicity bias and the label noise structure the authors might want to look at the following paper: **Sgd with large step sizes learns sparse features**. M Andriushchenko, et al., ICML 2023.


### Questions
See above for improvements.

Here is a list of typos:

- page 2: linearly converges
- Page 2: manifolds of minimisers
- Page 3 the paragraph with ‘the novelty of our approach’ has many typos and is not clear. Try to use ‘the’, 
    - we characterise the convergence on the manifold…
    - Far com the stationary points of the Hessian trace optimization problem
    - We show that this implies
    - There is no convexity —> convexity of what ? 
- Page 4: 
        - twice equation equation 1, 
        - non=degenerecy 
- Page 5: 
        - assumptions 1 and 1
        - Assumption 1 and 2 should be 1 and 3.
- Page 6 : problem with assumptions again

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
This theory paper studies the relationship between flatness and simplicity.   Prior works have shown that label noise SGD and 1-SAM have an implicit bias towards flat minimizers (where flatness is quantified using trace of Hessian), but have not engaged with the question of what small Hessian trace implies about the network itself.  This paper has basically two main contributions.   First, they prove that for two-layer networks in a high-dimensional setting, under a certain assumption on the activation function, all of the flattest global minimizers admit a rank-1 feature matrix on the training dataset.  That is, all of the neurons are effectively identical as far as the training set is concerned.  This is a strong form of simplicity.  Second, they characterize the rate of convergence of label noise SGD to this set of flattest global minimizers.

### Strengths
It's an important open problem to understand the relationship between flatness and complexity.  This paper takes what I think is a good step in that direction by proving that, in a certain setting, all of the flattest global minimizers yield a rank-1 feature matrix.

### Weaknesses
The main weaknesses of the paper are the unrealistic assumptions:

1.  The paper assumes that the data dimension is larger than the number of data points, which means that a linear regressor could fit the dataset perfectly.  This is an unrealistic assumption and it presumably makes a lot of the theory easier (e.g. I assume this assumption is what enables the authors to prove the global convergence of label noise SGD for narrow nets on arbitrary data from arbitrary initializations; barring this assumption on the data dimension, global convergence is ordinarily not provable even for vanilla gradient descent, let alone label noise SGD, right?).  On the positive side, the authors show _empirically_ that a version of the simplicity bias does seem to exist even for the practical low-dimensional setting.  I think it would be very interesting to characterize this simplicity bias in more detail, even if it cannot be accompanied by a global convergence proof.

2.  The paper assumes that the third derivative of the activation function is strictly positive, which I believe rules out most real activation functions.  It would be interesting if the authors could discuss what kind of results could be established even in the absence of this strong assumption on the activation function.  From skimming the proofs, it seems that this assumption is needed in order to invert the second derivative of the activation function, but could we say anything interesting about an activation like tanh where the second derivative is not completely invertible but is invertible up to sign?

### Questions
- As discussed above, how far could you get without making the assumptions about (1) high data dimension and (2) third derivative positivity?  Let's say we didn't care about proving global convergence, or global convergence rate, and just cared about understanding the structure of the flattest global minimizers.

- The conclusion says: "we show that by initializing the neurons in the subspace of high-dimensional input data, all of the neurons converge into a single vector."  But, I can't find any part of the text that discusses either this special initialization, or the result that the neurons converge to a single vector.  By contrast, the main text proves that for _any_ initialization, all the neurons _agree entirely on the training dataset_, which is weaker than saying that all neurons are identical.  I think I do understand why the sentence in the conclusion follows from this: if the neurons are initialized within the span of the input data, then since they always move within the span of the input data, they must end up within the span of the input data; and there is only one possible set of weights that both lies within the span of the input data and matches the necessary targets, and this is a pseudoinverse.  But the paper did not discuss this explicitly.

  - If you added weight decay, would it be true that for any initialization, all the neurons converge to a single vector?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors build on the work of Li, Wang, and Arora in ICLR 2022 (which they reference by means of its version in arXiv 2110.06914), in particular its result that SGD with label noise and infinitesimal learning rate traverses the manifold of zero loss in parameter space as the gradient flow that minimises the trace of the Hessian of the loss.  They investigate theoretically this gradient flow further for two-layer networks in which the second layer is fixed, and the derivative of the activation function is strictly positive and strictly convex; and for data points which are linearly independent and hence of cardinality not greater than their dimension.  There are two main results: first, that the first-order and global optima of the trace of the Hessian of the loss on the zero-loss manifold coincide, and are such that the projection of every first-layer weight vector in every such optimum onto the subspace spanned by the data points is a unique vector determined by the data, the network width, and the invertible activation function; and second, that gradient flow on the zero-loss manifold converges to such an optimum exponentially fast.  The theoretical results are supplemented by numerical experiments that explore weakening the assumption of data to allow cardinality greater than the dimension.

### Strengths
The theoretical results are proved in the appendix, which also contains helpful background material on manifold, tangent spaces, vector fields, covariant derivatives, etc.

The technique used to prove the convergence result is non-trivial, and the insight that it yields is potentially of wider interest: that the gradient on the zero-loss manifold being small implies that the trace of the Hessian of the loss has a positive semi-definite Hessian on the manifold, or equivalently it is locally geodesically convex.

### Weaknesses
The most involved part of the paper, Section 4.3, is hard to read. The proof sketch for the first claim of Theorem 3 is split in two, with the proof sketch for the second claim being in the middle. This makes the logical flow difficult to follow, especially since it is not immediately clear how the two parts of the proof sketch for the first claim relate to each other. The functions $g$ and $\gamma$ do not seem to be defined in the main text, which adds to the confusion. Further, it is not clear how the local g-convexity property is used to obtain the convergence rate.

The paper contains various typos, LaTeX issues, English issues, and small errors: Assumption 2 is referred to as Assumption 1, the font of "NN" in $r_{\theta, \mathsf{NN}}$ is not consistent, the sentence "The novelty of our approach..." on page 3 does not completely parse, the definition of $\mathcal{M}$ in Section 4.1 should be in terms of the labels $y_i$, etc. Those are some examples, I recommend to the authors to proof-read the whole paper.

Apparently no code is submitted as a supplement to the paper, which makes reproducing the numerical experiments harder.

### Questions
The assumptions on the activation function (Assumptions 1 and 3) are relatively strong.  Where exactly are they needed in this work, and what would be the obstacles to considering e.g. the ReLU activation?

It seems to me that the projections of the first-layer weight vectors onto the subspace orthogonal to the data points stay fixed throughout the training?  If that is the case, then this orthogonal subspace basically plays no role in the paper, so why not simply assume that $n = d$?  That would also make the optima in parameter space (in Theorem 2) unique?

What would constitute interesting future work?  The conclusion (Section 5) does not seem to contain any suggestions.

How related is the paper "Sharpness-Aware Minimization Leads to Low-Rank Features" by Maksym Andriushchenko, Dara Bahri, Hossein Mobahi, and Nicolas Flammarion in arXiv 2305.16292?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
