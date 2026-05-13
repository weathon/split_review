# Beyond IID weights: sparse and low-rank deep Neural Networks are also Gaussian Processes

- Decision: Accept
- Scores: 6, 6, 8, 5

## Abstract
The infinitely wide neural network has proven a useful and manageable mathematical model that enables the understanding of many phenomena appearing in deep learning. One example is the convergence of random deep networks to Gaussian Processes that allows a rigorous analysis of the way the choice of activation function and network weights impacts the training dynamics. In this paper, we extend the seminal proof of \cite{Matthews_2018} to a larger class of initial weight distributions (which we call \pseudoiid), including the established cases of \iid\ and orthogonal weights, as well as the emerging low-rank and structured sparse settings celebrated for their computational speed-up benefits. We show that fully connected and convolutional networks initialized with \pseudoiid\ distributions are all effectively equivalent up to their variance. Using our results, one can identify the Edge-of-Chaos for a broader class of neural networks and tune them at criticality in order to enhance their training. Moreover, they enable the posterior distribution of Bayesian Neural Networks to be tractable across these various initialization schemes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper extends previous results that showed randomly initialized multi-layer Bayesian neural networks with i.i.d. parameters are equivalent to Gaussian processes at the infinite width limit. The paper improves upon existing results by showing a similar result for a broader class of random parameters, namely pseudo-iid parameters. This class of random variables not only subsume classes of random variables that were included in previous literature (iid, orthogonal), but include new ones such as low-rank and block-sparse random variables. The authors results apply to fully connect networks as well as convolutional neural networks.

### Strengths
- The connections to previous literature and the contributions of the present work in light thereof are clearly stated.
- The writing and exposition is clear and easy-to-follow.
- The new class of random variables for which the authors extend existing results is significantly larger than those investigated previously, and can facilitate future research in multiple directions.

### Weaknesses
 - The paper expands upon existing results in a fairly specific strand of research, and it is not immediately clear why the novel families of random variables that they confirm to constitute Gaussian processes would be practically interesting. Though they provide some justifications in Section 3.3, these ideas are left for future research.
- Their focus on randomly initialized deep neural networks in general, rather than Bayesian neural networks in Matthews et al. 2018 also limits the practical implications of their work. Though the latter were able to examine the implications of BNN-GP's in posterior inference, this is out-of-scope for the current work, limiting its practical implications to initialization schemes.
- Pg. 1, Definition 1: $\mathbf{a}$ is not defined.
- Pg. 2, Section 1.1: It might make sense to mention the focus of some previous work on Bayesian neural networks, and how/why this is not the case in the current paper.
- Pg. 3, Section 2.1: Referring to $N_0$ as the width of the first layer might be confusing, given that the input layer is different than the layer $l=1$, which might also be considered the first layer.
- Pg. 3: What is the significance of the input space being assumed countably infinite?
- Pg. 6, Section 3.1: It would make sense to be more explicit about how each of the following example distributions are not covered by previous research's findings.

### Questions
- Pg. 1, Definition 1: $\mathbf{a}$ is not defined.
- Pg. 2, Section 1.1: It might make sense to mention the focus of some previous work on Bayesian neural networks, and how/why this is not the case in the current paper.
- Pg. 3, Section 2.1: Referring to $N_0$ as the width of the first layer might be confusing, given that the input layer is different than the layer $l=1$, which might also be considered the first layer.
- Pg. 3: What is the significance of the input space being assumed countably infinite?
- Pg. 6, Section 3.1: It would make sense to be more explicit about how each of the following example distributions are not covered by previous research's findings.

===========

Post-rebuttal note: I thank the authors for their feedback. Although the arguments for the paper's contributions being limited have some merit, I still believe the contributions are sufficient to warrant acceptance, and retain my recommendation for doing so.

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
Generalises previous results regarding neural networks with IID initialization becoming Gaussian Processes (GP) in the infinite-width limit to other initialization schemes, such as orthogonal, normalised, low-rank and sparse initialization schemes. Prove the results for both fully connected and CNN networks and provide simulation results for the different initialization schemes.

### Strengths
* The presented PSEUDO-IID framework replaces the IID requirement with centered and uncorrelated  entries, in a row-exchangable and column-exchangable matrix, under some technical conditions to prevent dependencies from changing the results. This is a general alternative to IID, which may be a useful generalisation for other cases as well.
 * Many different initialization schemes are PSEUDO-IID: IID, orthogonal, low-rank, and permuted block-sparse.

### Weaknesses
 * The presented PSEUDO-IID framework replaces the IID requirement with centered and uncorrelated  entries, in a row-exchangable and column-exchangable matrix, under some technical conditions to prevent dependencies from changing the results. This is a general alternative to IID, which may be a useful generalisation for other cases as well.
 * Many different initialization schemes are PSEUDO-IID: IID, orthogonal, low-rank, and permuted block-sparse.

 * The weights of the first layer must be Gaussian IID in all the relevant cases.

### Questions
* Is it correct that the weights of the first layer must be Gaussian IID in all the relevant cases? So the proof work only for PSEUDO-IID weights in all other layers?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors show that when the weights of neural networks are initialized in a "pseudo" i.i.d. manner, as defined by them, the random fields generated by each layer converge to Gaussian processes as the width of all layers goes to infinity simultaneously. They show this for fully connected neural networks and CNNs. 

Their definition of pseudo i.i.d. involves row and column exchangeability, a variance given as a parameter, and bounded higher order moments. They illustrate the generality of their proposed assumption by showing several non IID examples used in practice that fall under their proposed definition. 

Finally, they present numerical simulations for the convergence to Gaussian processes for fully connected networks with widths up to 300, where they examine the variance and joint distributions over a single neuron.

### Strengths
* Their major contribution is showing convergence of pseudo i.i.d. initializations and simultaneous scaling. This appears to be a challenging problem compared to sequential scaling, and their assumption seems quite general because it includes some non i.i.d. ways of initialization, including orthogonal and low rank weights, some of which are also faster in practice. 
* Their contribution also seems like a first step to identify conditions for edge of chaos. 

In general this paper is written very clearly, and the authors have given a good summary that shows exactly where their contribution fits in the existing literature. Moreover, their ideas and the proof technique for fully connected layers is easily understandable.

### Weaknesses
For CNNs, only one existing definition related to orthogonality, by Wang et al. in 2020, fits their pseudo i.i.d regime. Moreover I am not sure about feasibility, but including a numerical simulation for CNNs would make the study complete.

### Questions
Maybe it is referenced in the citations, but how will Gaussian processes in the limit help in developing new network regularisers?

### Soundness
3 good

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
This paper extends the results of Matthews et al. (2018) about the convergence of random deep networks to Gaussian processes, to a wider class of distribution called ``Pseudo-IID".

### Strengths
The strength of this paper is yet another result/evidance about the convergence of random deep networks to a Gaussian process, for broader class of initial weight distributions.

### Weaknesses
The main weakness of this paper is that it seems as though that while the class of initial weight distributions is indeed broader than the Gaussian one Matthews et al. (2018), the techniques used to prove the result are pretty much the same as in Matthews et al. (2018), and the differences are just technicalities (e.g., CLT for exchangeable RVs). Therefore, since the main contribution of this paper is supposed to be for the theoretical study of NN, I believe that the paper is not novel in that sense. Also, there are many grammatical mistakes and in general it feels that the authors did not make an all out effort when writing their paper.

### Questions
Above I discussed my main concern with this paper. Here are some other comments:

1. Definition 2 should come before Definition 1.

2. Each of the elements in Definition 1 must be discussed right away after the definition is given. To the reader, it is almost impossible to understand why these assumptions are either needed or interesting. If it is ``difficult" to explain these at this point in the flow of the paper, then probably those definitions should come after, and keep the introduction clean from technical mathematical definitions. 

3. While I read and understood the proof, it might be a good idea if the authors will explain the novelty and mathematical difficulties as compared to current literature.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair
