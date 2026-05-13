# Optimizer-Dependent Generalization Bound for Quantum Neural Networks

- Decision: Reject
- Scores: 5, 5, 8, 6, 6

## Abstract
Quantum neural networks (QNNs) play a pivotal role in addressing complex tasks within quantum machine learning, analogous to classical neural networks in deep learning. Ensuring consistent performance across diverse datasets is crucial for understanding and optimizing QNNs in both classical and quantum machine learning tasks, but remains a challenge as QNN's generalization properties have not been fully explored. In this paper, we investigate the generalization properties of QNNs through the lens of learning algorithm stability, circumventing the need to explore the entire hypothesis space and providing insights into how classical optimizers influence QNN performance. By establishing a connection between QNNs and quantum combs, we examine the general behaviors of QNN models from a quantum information theory perspective. Leveraging the uniform stability of the stochastic gradient descent algorithm, we propose a generalization error bound determined by the number of trainable parameters, data uploading times, dataset dimension, and classical optimizer hyperparameters. Numerical experiments validate this comprehensive understanding of QNNs and align with our theoretical conclusions. As the first exploration into understanding the generalization capability of QNNs from a unified perspective of design and training, our work offers practical insights for applying QNNs in quantum machine learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this paper, the authors provide generalization bounds using the _stability_ approach for a family of quantum neural networks (QNNs) using data-reuploading strategy and stochastic gradient descent (SGD) as an optimizer by conceptualizing QNNs as a special form of quantum combs. The generalization bound number of trainable parameters, number of times data is reuploaded, dataset dimension, and classical optimizer-dependent parameters, providing guidelines for designing and training QNNs. Numerical experiments to support theoretical claims have been conducted on three classical datasets; e.g. MNIST, Breast Cancer, and FMNIST.

### Strengths
This work makes an interesting connection of QNNs to quantum combs to leverage the rich theoretical framework of the latter to analyze the dynamics of QNNs, although a brief connection of quantum combs to QNNs using data re-uploading strategy was mention in [1].

Provides theoretical guidelines on designing and training near-term quantum machine learning (QML) models--a fundamental question in QML.

[1] Mo, Yin, et al., "Parameterized quantum comb and simpler circuits for reversing unknown qubit-unitary operations", arXiv:2403.03761

### Weaknesses
- Limited novelty in theoretical analysis: In my opinion, the paper heavily borrows proof strategies and techniques from [2] which studies SGD for smooth, Lipschitz and convex problems for deep neural networks. The only novelty is the connection of data reuploading QNNs to quantum combs and then using well-established lemmas from the rich theory of quantum combs. The adaptation of existing techniques to the quantum setting, while non-trivial, does not introduce fundamentally new theoretical insights into generalization bounds beyond what is already known for classical neural networks with similar optimization methods.

- The generalization bounds based on stability especially that of [2] becomes too loose and vacuous as training progresses, even in the practical regime of the training time where deep neural networks are known to generalize well [3]. I believe that as the generalization bound essentially uses the same proof techniques and the technical setting is the same, your bound might also undergo the similar phenomenon. This is a limitation which should be highlighted in the work. The paper should explicitly discuss the limitations of stability-based bounds, particularly their tendency to become uninformative as training progresses, and how this impacts the practical relevance of the derived bounds for QNNs.

- The work also lacks analysis on the robustness of the generalization bound in presence of standard quantum noise models such as depolarizing noise, state preparation and measurement error (SPAM), thermal relaxation, readout error etc. It would be beneficial if the authors can provide analysis of their generalization bounds for one of the above noise models, e.g. for depolarization noise. The absence of such analysis limits the practical applicability of the results, as real-world quantum devices are inherently noisy. A discussion on how noise affects the derived bounds is crucial for assessing the robustness of the proposed approach.

**Minor Issues**:

- Line 161: the definition of CX gate is incorrect.

- Line 164: A more of a pedantic take, apologies if the authors do not agree with me on this: as QNN is a variational quantum algorithm (VQA), I think they comprise of 3 things: ansatz, observable and the classical optimizer. I say this because the design of observables also is related to the presense of barren plateaus. For instance, [4] proves that when you have local observables there is a possibility of absence of barren plateaus (BPs) while for global observables, they prove the presence of BPs.

- In Fig. 2 caption and in the surrounding text, the authors mention the use angle encoding as a classical data encoding scheme, however, this is not correctly depicted in Fig. 2 as there are two RY gates! Please correct this to avoid any confusion.

- Please add reproducibility statement according to the author guidelines of ICLR.

### Questions
- Can your proof techniques be used for proving generalization bounds for data re-uploading QNNs where input-scaling parameters are also trainable? That is, the output function of a data re-uploading QNN is $f(\mathbf{\theta}, \mathbf{\lambda}, \mathbf{x}, \mathcal{M})$, where $\mathbf{\lambda}$ are input-scaling parameters used when data is being re-uploaded and are trainable, e.g. data encoding operation is $U(\mathbf{x}, \mathbf{\lambda})$ instead of $U(\mathbf{x})$. In your current analysis, $\mathbf{\lambda} = \mathbf{1}$ and is not trainable. I ask this because the function $f(\mathbf{\theta}, \mathbf{\lambda}, \mathbf{x}, \mathcal{M})$ is more general and recovers your defintion of $f(\mathbf{\theta}, \mathbf{x}, \mathcal{M})$ and can in principle do a bit more than your data reuploading model.

- Does your definition of stability hold also for memorization algorithm[5]--a learning algorithm which always outputs the function $f(\mathbf{x}_i, \mathbf{\theta}_S, \mathcal{M}) = -1$, except that it alters $f$ in a small number of locations to fit the training set?

- Can you provide any numerical evidence on the how tight is your analysis of generalization bound?

- What properties (or hyperparameters of QNNs) and operations (regularization, weight decay, gradient clipping etc.) induce stability?

- DNNs with random initialization tend to behave like random Gaussian processes (in limit of many neurons)[6] which allows for their characterization of their trainability and generalization. However, this is not the case for randomly initialized QNNs as they instead generally form Wishart processes[7] which give rise to barren plateau phenomenon and exponentially many local poor minima. That being said, does your generalization bound result help to mitigate these issues and if yes, how?

- Why is there a significant difference between the generalization error reported in Fig. 3 with settings [L=8 (purple or violet) with $\eta=0.01$] and Fig. 4 with settings [L=8 with $\eta=0.01$ (red)]. The generalization error should be more or less similar which is not the case if I look at the plots. Can you please explain this phenomenon?

- In the numerical experiments to support your theoretical claims, why do you use parametrized quantum circuits (PQCs) that are not universal and classically simulable? This completely defeats the purpose of using QML, no? Because at the end, we want a quantum model (specified by a PQC) which is expressive (for the domain), trainable, noise robust and can not be classically simulable--holy grail of QML.



[5] Chatterjee, Satrajit, "Learning and Memorization", ICML (2018)

[6] Lee et al., "Deep neural networks as Gaussian processes", ICLR (2018)

[7] Anschuetz, Eric, "A Unified Theory of Quantum Neural Network Loss Landscapes", arXiv:2408.11901

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the generalization properties of quantum neural networks (QNNs) through the lens of learning algorithm stability. The authors establish a connection between quantum combs—a framework for organizing variable subcircuits—and data re-uploading, a technique for iteratively encoding data within quantum circuits. They derive an upper bound on the generalization error, relating it to the number of re-uploading layers, dataset size, parameter count, learning rate, and optimization steps. Experimental results are provided to support the theoretical findings.

### Strengths
1. This study initiates the attempt to establish the optimization-dependent generalization error bound of quantum neural networks by analyzing the stability of optimizing quantum neural networks (QNNs) with SGD.
2. The derived generalization bound offers practical insights for selecting hyperparameters, such as recommending a smaller learning rate when using a large number of parameters, which could be beneficial for optimizing QNNs.
3. Numerical experiments are conducted, providing empirical support for the theoretical results and suggesting that the bounds are valid under various settings.

### Weaknesses
1. While this paper presents a useful framework for optimization-dependent generalization error bounds, its novelty is somewhat limited in both theoretical derivation and implications. Specifically, two of the three main implications have already been observed in Ref. [1], and the third can be derived from Ref. [2], which discusses model stability under different convexity conditions—a result that may be applied to quantum settings as well. The core issue is that the presented stability analysis, while relevant, does not introduce fundamentally new techniques or insights beyond what is already established in the classical machine learning literature. The connection to existing work on stability, particularly in the context of SGD, is not sufficiently differentiated to justify the claim of a novel approach. The paper would benefit from a more detailed comparison highlighting the specific challenges and adaptations required to apply stability analysis to quantum neural networks, rather than simply stating that the extension is non-trivial.

2. Although it is interesting to establish the connection between the quantum comb and the QNNs with data-reuploading structure, the discussion of this connection seems to be separated from the derivation of the generalization error bound. I mean by this the derivation of the generalization error bound does not employ any necessary properties of the quantum comb. This raises questions about the added value of quantum combs in the context of this study. The paper does not clearly articulate why the quantum comb framework is essential for the derived generalization bounds. The analysis appears to proceed independently of the specific properties of quantum combs, making their inclusion seem somewhat superficial. The authors should clarify whether the use of quantum combs offers any unique advantages in the analysis or if the same results could be achieved using a more direct approach.

### Questions
Could you clarify the role of quantum combs in the derivation of the generalization bounds, specifically whether they are essential to the analysis or if the same results could be obtained without them?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper attempts to estimate the generalization error bound for Quantum Neural Networks (QNNs) in terms of the number of trainable parameters, data uploading times, dataset dimension and classical optimizer hyperparameters by converting the QNN into a quantum comb structure and by leverage the uniform stability property of the stochastic gradient descent algorithm. The authors then validate these bounds by means of numerical experiments with the Breast Cancer, MNIST and Fashion MNIST datasets by tracking the generalization error being estimated as the absolute difference between the train and test error across epochs for different values of data uploading times and learning rates. The analysis suggests that a larger learning rate should be balanced by a smaller learning rate to ensure that each step in the learning is small enough to prevent instability that could arise in more complex models and that the learning rate should be set $\mathcal{O}(1/K)$, where $K$ is the fixed number of learning parameters or the number of  should be set as $O(1/\eta)$ for a fixed learning rate.

### Strengths
The main strength of this paper is that it provides useful guidelines to tune the architecture and learning hyperparameters for QNNs based on the general quantum comb architecture. Each quantum comb is equivalent to a causal QNN. The Choi operator of the quantum comb is the Choi operator of the corresponding causal QNN. Corollary 4 is a useful result that ties all the relevant parameters including number of trainable parameters, data uploading times, dataset dimension and classical optimizer hyperparameters to provide a generalization error bound with SGD-based optimization.

### Weaknesses
The main weakness of the paper is the slightly limited experimental evaluation. The choice of datasets (Breast Cancer, MNIST, and Fashion MNIST) are not clearly motivated. It would be beneficial to understand the rationale behind selecting these specific datasets and how they represent a diverse range of challenges for QNNs. Additionally, the experiments only explore a limited number of values for data uploading times $L$ and the learning rate $\eta$. For instance, in the Fashion MNIST experiment (Figure 1), the transition from a stable to an unstable regime appears to occur abruptly between $L = 2$ and $L = 8$. Similarly, in Figure 2, the instability seems to arise suddenly between $\eta = 0.01$ and $\eta = 0.05$. Exploring a finer range of values for these parameters would provide a more nuanced understanding of the stability boundaries. Furthermore, the error bars in Figure 2, which depicts experiments varying the learning rate, are quite large. This makes it difficult to draw definitive conclusions about the impact of the learning rate on stability. It is mentioned that experiments were re-run 5 times, but this might be insufficient to achieve statistically significant results, particularly in the unstable regions.

### Questions
1. Why did you choose the datasets you chose for the experimental evaluation? It would be good to have a table that shows the datasets chosen with the number of training examples.
2. Have you considered the complexity of the learning task (eg. lack of easy separability between the classes) or the number of features in your data as affecting your generalization bounds? How does it factor into your bound provided in Corollary 4 or is it independent of that?
3. For the Fashion MNIST dataset experiment, you may wish to try more values of $L$ for Figure 1 and $\eta$ for Figure 2 because there is rather ubrupt transition from stability to unstability from $L = 2$ to $L = 8$ and from $\eta = 0.01$ to $\eta = 0.05$.
4. The error bounds are rather large for the experiments that vary the learning rate (Figure 2), making the conclusions you are drawing somewhat untenable, you may wish to run more trials to reduce the size of your error bars. I understand you reran 5 times but that maybe too little for some of the experiments. Why did you not do this?

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
2

### Summary
The authors derive a generalization bound of the data re-uploading QNN trained using SGD. They first show the data re-uploading QNNs can be represented by a sequential quantum comb, and study the stability of the data re-uploading QNNs via this representation.

### Strengths
Understanding behaviors of quantum machine learning models is important. This paper focuses on the combination of a quantum machine learning setting and SGD, and analyzes the generalization gap based on the stability. The topic is interesting and relevent to the community.

### Weaknesses
I have several questions and concerns, which are listed below:

- In eq. (10) implies that if we choose a proper hyper parameters, then the generalization gap becomes small as the iteration of SGD proceeds. In many cases, the generalizaiton gap becomes large as the learning process proceeds in an early stage due to the overfitting. On the other hand, the generalization gap may become small after a sufficiently long learning process due to the benign overfitting. Could you comment on the relationship between the proposed generalization bound and this type of practical situations?

- In line 383, the authors instst "the linear dependence of data dimension and data reuploading time not only offers extra insights into understanding the QNN model’s performance but also provides insights into the design of these models". Is it possible to determine an optimal $L$ based on the tradeoff between the expressivity and generalization? Could you explain more about how we can design the models based on the proposed generalization bound?

Minor comments:
- In eq. (6), the number of parameters are denoted as $K$, but the expranation of this notation is in Theorem 3.

### Questions
Minor comments:
- In eq. (6), the number of parameters are denoted as $K$, but the expranation of this notation is in Theorem 3.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the generalization properties of quantum neural networks (QNNs) with data re-uploading strategy. Concretely, they leverages the quantum combs formalism and data re-uploading structure to analyze the stability of QNNs and then give the upper bound of generalization error on such model. They also provide numerical experiments to support the proposed theoretical claims.

### Strengths
1. provide rigorous analysis of generalization performance based on stability of SGD and quantum combs, the upper bound gives some insight to select the hyper-parameters of QML model with data re-uploading.
2. give some basic numerical experiments to support the theoretical claims.

### Weaknesses
As the theoretical analysis and numerics only focuses on the specific ansatz structure (with data re-uploading strategy), it is unclear that the similar theoretical findings also true for other QML models. Specifically, the analysis relies heavily on the structure of data re-uploading, where the same data is repeatedly encoded into the quantum state. This makes it difficult to generalize the results to other quantum architectures, such as those employing different encoding strategies or variational forms. The numerical experiments, while supporting the claims, are limited to a single ansatz, making it hard to assess the broader applicability of the theoretical bounds. For instance, the stability analysis might be significantly different for models that use different quantum gates or a different number of qubits, or even different encoding methods.

### Questions
I have no further questions.

### Soundness
3

### Presentation
3

### Contribution
3
