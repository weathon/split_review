# Exploring channel distinguishability in local neighborhoods of the model space in quantum neural networks

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
With the increasing interest in Quantum Machine Learning, Quantum Neural Networks (QNNs) have emerged and gained significant attention. These models have, however, been shown to be notoriously difficult to train, which we hypothesize is partially due to the architectures, called ansatzes, that are hardly studied at this point. Therefore, in this paper, we take a step back and analyze ansatzes. We initially consider their expressivity, i.e., the space of operations they are able to express, and show that the closeness to being a 2-design, the primarily used measure, fails at capturing this property. Hence, we look for alternative ways to characterize ansatzes by considering the local neighborhood of the model space, in particular, analyzing model distinguishability upon small perturbation of parameters. We derive an upper bound on their distinguishability, showcasing that QNNs with few parameters are hardly discriminable upon update. Our numerical experiments support our bounds and further indicate that there is a significant degree of variability, which stresses the need for warm-starting or clever initialization. Altogether, our work provides an ansatz-centric perspective on training dynamics and difficulties in QNNs, ultimately suggesting that iterative training of small quantum models may not be effective, which contrasts their initial motivation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The study presents the authors' work on evaluating the expressivity of different ansatzes, while trying to propose novel measures and metrics to capture the behaviour of QNNs during training.

### Strengths
The paper looks from a different angle to the well-known problem of training QNNs and presents new approaches to assessment of quantum model expressivity while discussing the need to develop architectures suitable for QML. This seems like an important work for the QML community.

### Weaknesses
The paper did not explain what particular elements or spatial organisation of gates of ansatzes may be the most contributing to expressivity or trainability issues observed in QNNs. Specifically, the study lacks a detailed analysis of how different gate types (e.g., single-qubit rotations, CNOTs, parameterized gates) and their arrangement within the ansatz affect the ability of the network to explore the relevant Hilbert space. For instance, are certain gate combinations more prone to barren plateaus, or do specific connectivity patterns lead to better expressivity? The paper also does not explore the impact of the depth of the ansatz on these issues, which is a crucial aspect of QNN design. Furthermore, the work does not delve into the nuances of parameter initialization strategies and their potential influence on the observed expressivity and trainability. A more thorough investigation into these architectural and optimization-related factors is needed to provide actionable insights for the QML community.

### Questions
Do the authors envision that researchers in the field would be able to leverage their findings to build better application-specific models? Could standard architecture search approaches be coupled with suitable distinguishability metrics to build better ansatzes?

What proportion of the expressivity issues observed with QML models are related to the ansatz vs the data encoding?

As all experiments seem to be classical simulations, do the authors have an idea how much will noise when executing the model on a device contribute to expressivity issues?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper considers methods of characterising the variational ansätze represented within quantum neural networks. The paper argues against the use of so-called 2-designs as a measure for expressivity that have been used in previous works. The work goes on to introduce a notion of channel sensitivity, which considers how much (in terms of a so-called diamond norm, a norm used more in Quantum Information theory) a unitary changes under perturbation of variational parameters. Bounds for the channel sensitivity are derived by consideration of Taylor series expansions and used to argue against the distinguishability of ansätze with few variational parameters on parameter perturbation. Numerical studies then investigate the notions introduced above in terms of both random perturbations of variatonal parameters, and also perturbations introduced during a training loop.

### Strengths
1. The introduction and background material are particularly well-written and offer a broader ICLR readership a succinct way of learning about quantum neural networks. However, it is possible that too much space has been allocated within this area at the expense of a fuller exposition of novel aspects of the work.
2. The work takes aim at foundational issues in variational quantum circuits and the points made are widely applicable to QNNs as a whole.
3. The proposed channel sensitivity metric based on diamond norms seems to be aiming at something principled, in that it seeks to characterise the action of a unitary on any state. Its application to variational quantum circuits, to my knowledge, is novel.

### Weaknesses
1. Sections 3 and 4 feel like they should be the main contributions of the paper, but they squeezed into about a single page. For example, precise mathematical definitions of the how the quantum states in Eq (4) are missing from the main text, which makes it hard to follow.
2. The work as a whole considers expressivity of a variational quantum circuit as a problem of the ansatz and does not give any weight to the importance of feature encoding into the quantum circuit. It is known that the spectral representation of a QNN is directly given by the feature encodings ([Schuld, 2021](https://arxiv.org/abs/2008.08605)).
3. The diamond norm under parameter change seems like an interesting metric, but it remains unclear what can be done with it.
4. Similarly, the bound on the channel distinguishability under small perturbations seems not to be useful. It seems natural that the QNNs will only change gradually under small parameter perturbations such as those encountered during training, so what use is an upper bound?
5. The main points of the work seem somewhat incongruous: the criticism of the 2-design as an expressivity metric seems like it should give way to an alternative expressivity metric. However, the channel distinguishability metric proposed does not provide an expressivity metric.

### Questions
Question:

1. My understanding is that the diamond norm is derived to provide a channel distinguishability based on a single measurement of the state. Does this translate to distinguishability of a QNN model, where i) we might make use of several measurements and ii) one might make use of a specific measureable (e.g. single qubit magnetisation) rather than the whole state?
2. What can be done with the proposed channel distinguishability metric? The fact that it can be bounded from above for small perturbations does not seem useful. All neural networks (classical or quantum) typically won't change too much in a single training step---why is upper bounding this change in terms of some norm useful to a practitioner?

Suggestions:

2. I think section 3 and 4 can be elaborated on more. In particular, the criticism of 2-designs as a measure of expressivity is hard to read without going back and forth between the main text and the appendix several times.
3. Elaborating on section 3 and 4 would probably need more space. Some of the figures can be moved to the appendix, e.g. the three rows of figure 2 are conveying a similar message, so perhaps two of the rows can be placed in the appendix? Same with figure 3. The conclusions and discussion could be shortened as well.
4.  Ensure that all figures are included in a vector format or lossless format. Maybe I'm not seeing things right, but the quality of the figures seems a little bit off.
5. A minor point unrelated to the core contributions of the paper. But amplitude encoding of features into a QNN feels like a non-standard way of conducting the numerical experiments. Apart from amplitude encoding not being near-term friendly, the resulting QNN will not be particularly expressive. I.e. one will end up with something like `<PCA|Hermitian|PCA>`, which, since the PCA is a linear combination of features, will result in a sum of pairwise interactions with no zeroth, first or cubic and higher order terms. Encoding PCA components into single-qubit rotations would be a more standard approach, to my knowledge.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper studies quantum neural network expressivity and model distinguishability. The aim is to better understand, at least for small architectures, the model space of so-called Hardware Efficient Ansatzes (HEAs) for quantum neural networks. To do this, the authors first argue why 2-design is an inadequate measure for model expressivity.  Then they define channel sensitivity to measure the effect of parameter changes on quantum neural network output using the diamond-norm from the literature. A Taylor-expansion-based argument allows to provide a natural upper bound on channel sensitivity. Moreover, the paper conducts an extensive numerical study to experimentally measure channel sensitivity for standard HAE quantum neural networks. As its main message, the paper states that its results ultimately suggest that iterative training of small quantum models may not be effective.

### Strengths
Overall, the proposed research question appears relevant, as a theoretical understanding of quantum neural networks is, to a large extent, still missing. The paper is mostly clearly structured and well-presented. Although limited to small architectures, the considered setting is still of interest, given the hardware limitations. Numerical study considers several important combinations of architectures.

### Weaknesses
Some of the key conclusions drawn from the numerical results are only partially justified by what is presented in the paper, weakening the overall significance of the reported results. More specifically:

- Some important details regarding the setup of numerical experiments (employed optimizer, optimizer hyperparameters) and results (confidence level for confidence intervals) are currently missing in the paper. Also, it appears that robustness with respect to choice of optimizer / hyperparameters has not been studied. The authors claim that their experimental results support the theoretical bounds, which are independent of the optimizer. However, the experimental results are still influenced by the choice of optimizer and hyperparameters, even if the theoretical bounds are not, and this needs to be examined. The experimental results could be significantly different with other optimizers or hyperparameters, and this needs to be addressed to strengthen the validity of the conclusions.
- The upper bound on channel sensitivity is an upper bound, not an equality. Some of the conclusions drawn in the discussion/abstract/introduction would only be valid in case of equality. For example, in the Discussion section, the paper states that channel sensitivity "scales with (1) the magnitude of changes and (2) the number of parameters." This statement is true for the upper bound, but not necessarily for the channel sensitivity, as the upper bound is very loose (as the experiments show) and no lower bound seems to be available. Similarly, the introduction the authors write as one of their four main contributions: "we introduce a measure for the distinguishability of an ansatz upon parameter update and provide an upper bound. It shows that many parameters are required to be able to distinguish the two operations, contrasting with the initial framework." This would be true in case of an equality, but an upper bound (which is loose, as the experiments show) does not seem sufficient to support such a claim. The authors should clarify that their conclusions are based on the upper bound and not the actual channel sensitivity, and also provide a discussion on the implications of this distinction.
- As one of their four main contributions, the authors state "We provide numerical evidence that each ansatz is hardly distinguishable from itself". This seems to be based on Figure 3. Since Figure 3 also shows the (loose) upper bounds, the different scale of bounds and channel sensitivities in Figure 3 makes it impossible to see this solely from the figure. The authors should provide a separate plot without the upper bounds to support this claim.
- Terminology is slightly confusing: in Holmes et al (2021) the term expressibility was used. For classical neural networks, expressivity refers to their capability of approximating arbitrary given unknown functions. This is a fundamental property for choosing which neural network architecture to use, but does not seem to be discussed in the paper. The authors should clarify why they chose to use the term expressivity instead of expressibility, and also discuss the relationship between the expressivity of the quantum neural networks and their ability to approximate arbitrary functions.

### Questions
1.	Which optimizer (and optimizer hyperparameters) did you use in the experimental results? 
2.	How do the empirical results depend on the choice of optimizer and its hyperparameters?
3.	Where does the factor $\frac{1}{2}$ in (30) come from? Inserting (25) into (29) would give (30), but without additional factor $\frac{1}{2}$.
4.	Why do you use mean-squared loss, even though you are solving a classification problem?
5.	From its definition, the diamond norm seems to depend on number of qubits. How does an increase in number of qubits affect the diamond norm? 
6.	Can you provide an additional figure, which is the same as Figure 3 but without the upper bounds? 
7.	The reported results are averaged over architectures with the same number of parameters. Can you be more specific about what type of "confidence intervals" you show in the plots?
8.	For comparison reasons, it would be very insightful to analyse channel sensitivity of a non-entangled circuit. For example, for a circuit applying an $R_X$ gate to each qubit independently, what channel sensitivity do you get for $1,2,3,4$ qubits?
9. How do the results depend on your choice of input-encoding?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors introduce an "expressivity" measure of quantum neural network (QNN) architectures that they argue is more natural than those previously explored in the literature. One example of the latter is a difference measure between the given QNN architecture when randomly initialized and a $t$-design (for some small $t$); the authors show that having a large expressivity according to such a measure does not necessarily indicate that the model explores a large subspace of Hilbert space. This motivates their introduced definition, which is a sensitivity measure in diamond norm of the quantum network upon perturbing the network parameters. The authors then perform some numerical experiments indeed demonstrating that this measure tracks with how one would intuitively expect "expressivity" to behave (it grows with the number of layers and trainable parameters per layer, and so on).

### Strengths
Understanding measures of expressivity for QNNs is important for understanding the to-date loosely-defined "expressivity-trainability trade-off" known to exist in quantum networks (see, e.g., arXiv:2312.09121 and arXiv:2406.07072). The authors, in a very clear fashion, describe shortcomings of certain previously-introduced measures of quantum network expressivity; given these shortcomings, the authors then introduce a novel, natural notion of expressivity that circumvents these shortcomings.

### Weaknesses
Though not the fault of the authors, the introduced measure of expressivity has the unfortunate side-effect of being difficult to estimate; this limits the scope of their numerical experiments. It also makes the relative advantage of the authors' introduced expressivity measure over an expressivity measure based on closeness to the Haar measure (rather than a small-$t$ $t$-design) unclear, given both are difficult to estimate. Specifically, the diamond norm calculation, which is central to the authors' proposed measure, scales poorly with the number of qubits, similar to the computational complexity associated with calculations involving the Haar measure. This raises concerns about the practical applicability of the proposed measure for larger quantum systems, as both approaches face significant computational hurdles. The authors do not provide a clear comparison of the computational scaling of their proposed measure with that of Haar-based measures, leaving the reader to wonder if the introduced measure offers any practical advantage in terms of computational tractability.

### Questions
Is there a natural reduction of certain, previously-explored measures of expressivity to the authors' introduced measure of expressivity? For instance, I believe demonstrating that having large expressivity based on a measure of closeness to the Haar measure, and showing this implies a large expressivity according to the authors' definition (averaged over parameter space), would strengthen this work.

Furthermore, what relative advantages do the authors' introduced expressivity measure have over expressivity measures based on closeness to the full (i.e., not $t$-design) Haar measure? This impacts the broader reach of this work, as to me it is currently unclear what the relative merits are of the introduced measure to this previously-studied measure.

### Soundness
4

### Presentation
4

### Contribution
3
