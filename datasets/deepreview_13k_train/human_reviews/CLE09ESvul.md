# What should a neuron aim for? Designing local objective functions based on information theory

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
In modern deep neural networks, the learning dynamics of the individual neurons is often obscure, as the networks are trained via global optimization. Conversely, biological systems build on self-organized, local learning, achieving robustness and efficiency with limited global information. We here show how self-organization between individual artificial neurons can be achieved by designing abstract bio-inspired local learning goals. These goals are parameterized using a recent extension of information theory, Partial Information Decomposition (PID), which decomposes the information that a set of information sources holds about an outcome into unique, redundant and synergistic contributions. Our framework enables neurons to locally shape the integration of information from various input classes, i.e.\,feedforward, feedback, and lateral, by selecting which of the three inputs should contribute uniquely, redundantly or synergistically to the output. This selection is expressed as a weighted sum of PID terms, which, for a given problem, can be directly derived from intuitive reasoning or via numerical optimization, offering a window into understanding task-relevant local information processing. Achieving neuron-level interpretability while enabling strong performance using local learning, our work advances a principled information-theoretic foundation for local learning strategies.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors claim that modern deep neural networks focus on global optimization and the learning objective for individual neurons are obscure, whereas real-life biological neurons grow with local learning objectives with limited global information. Based on this intuition, the authors propose a biologically inspired neural network that enhances interpretability of the learning dynamics of individual neurons. The authors leverage Partial Information Decomposition (PID) in information theory to formulate objective functions on the individual neuron level, and these neurons are termed “infomorphic neurons”. This novel formulation is able to achieve comparable performance to backpropagation on MNIST and CIFAR10 datasets, showing preliminary signs of utility. Besides, the proposed framework allows for interpretability analysis on the partial information components which is quite unique and interesting.

### Strengths
1.	The topic of biologically inspired neural networks has attracted great attention in the recent years. Proposing alternative solutions to the long-dominating backpropagation method is also interesting and profoundly influential. I encourage the authors to work along these lines.
2.	Overall this is a paper very rich in content.
3.	The visualizations in Figure 1 and 2 are very helpful for understanding the partial information components in partial information decomposition.
4.	The performance on MNIST and CIFAR10 are quite promising. From what I read, the proposed method achieved beyond 98% accuracy on MNIST and 94.4% accuracy on CIFAR10.
5.	The parameter importance assessment is thoughtful and informative.

### Weaknesses
1.	While I believe we should not expect super comprehensive experiments from a paper that initially introduce a novel concept or paradigm, it might be even improve the soundness of this paper if the authors can also include the performance on slightly more challenging datasets. If standard large datasets such as ImageNet are too computationally expensive, the authors could consider variants that are decently big and challenging, such as TinyImageNet. The current evaluation is limited to MNIST and CIFAR10, which, while standard, do not fully demonstrate the scalability and robustness of the proposed infomorphic networks. Specifically, the CIFAR10 results, while showing promise, are not yet at a level that would definitively establish the method's effectiveness on more complex image recognition tasks. The absence of results on a dataset with more classes, higher resolution images, or more complex object variations makes it difficult to assess the generalizability of the approach.
2.	For demonstration of experimental results, while I like the richness of Figure 3B and I do notice Figure 8 in the appendix, I would personally argue it would be more straightforward to include a “less exiting” bar and whiskers plot of backprop as well as different variants of bivariate and trivariate models. I suspect the authors left the performance of the bivariate model to the appendix to avoid overcrowding the results, but this omission from the main text might trigger confusion from the audience. Again, a good old bar and whisker might be a valid solution. The current presentation of results, while detailed, makes it difficult to quickly compare the performance of the different models. A more direct comparison, such as a bar plot with error bars, would allow the reader to easily assess the relative performance of the proposed infomorphic networks against standard backpropagation and different infomorphic variants. The lack of this direct comparison in the main text hinders a clear understanding of the method's advantages and disadvantages.


### Questions
1.	Please refer to Weakness 2. Would the authors consider the “less existing” representation of the quantitative results or provide some other alternative that are similarly straightforward?
2.	I still have a hard time understanding how the partial information components are realized in actual implementation. It would be good for the authors to provide a brief explanation on how that is done or point to the relevant text in the paper.
3.	It is a bit uncommon to have “Related Works” and “Limitations and Outlook” as part of the Discussion section. Is that intentional or is it just a typo?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
Based on the concept of partial information decomposition in the information theory, this work formulates a learning framework that allows the implementation of per-neuron goal functions and neuronwise interpretability. In an ANN setup for classification tasks, the goal function is optimized via parameters of the ‘informorphic’ neurons, with neuron-level interpretation, good performance (comparable to the same ANN trained with bp) and insights into the local computational goals. Examples with bivariate and trivariate informorphic neurons are demonstrated where the three-input classes unlock the potential of information theoretic learning, validating the abovementioned advantages in comparison with classical information composition.

### Strengths
The use of partial information decomposition in a learning framework with bivariate and trivariate implementations enables interpretable information processing at the per-neuron level, which is also new. The discussion based on a comparison between heuristic and optimization approaches demonstrates the potential of the interpretability of local learning framework in a task-relevant context and without the loss of performance compared to ANN trained with bp.

### Weaknesses
The title ‘What should a neuron aim for’ is broader than the scope explored in the current work, where a single-layer bivariate and trivariate local learning framework is studied. There is still a large gap between the interpretability of the model here and that of the neuron. The advantage of interpretability from an application perspective is not demonstrated or discussed, which is expected to be very limited by the single-layer simplicity here. Specifically, the work does not address how the learned neuron-level objectives translate to higher-level network behavior or how these objectives might be useful in a practical setting. The current implementation, limited to a single layer, does not provide a clear path for scaling these methods to more complex, multi-layered architectures, which is crucial for real-world applications. The interpretability is also constrained by the fact that the analysis is limited to the parameter space of the goal function, rather than the actual information processing performed by the neurons in the context of the task.

### Questions
How do we understand the performance presented in Fig. 3B by considering that at Nhid = 100, there is a convergence for all results? Why a sparse lateral outperform a dense lateral under large Nhid conditions? What are the computational and memory costs?
What does the extraction of high-effect parameters mean, and would this be useful to construct networks with higher performance, or understand the nature of the problems under training?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a local learning framework for neural networks by introducing a local training objective inspired by partial information decomposition (PID) in information theory.
It trains each neuron individually by a local goal function that is a linear combination of PID atoms, which decomposes the information that three input signals 
(feedforward, context, and lateral) provide about the neuron's output. The weights of the combination can be chosen heuristically or optimized on validation data. The weights represent 
how information in the inputs contribute to the neuron's output and are human-interpretable. Experiments on a single-hidden-layer network show that the proposed learning method 
can achieve similar performance to conventional training by cross-entropy loss, yet providing interpretable learning process of individual neurons.

### Strengths
The idea of using information-theoretic loss functions to train individual neurons is interesting, with nice connection to biological neural networks and neuroscience. 

The novelty of adding a third input class representing lateral connections between neurons is intuitive and interesting and demonstrates better empirical performance than the bivariate model.

The overall method and motivation are clearly presented.

The experiments are well designed. Nice ablation study on the goal parameters. Good interpretation of "important" PID atoms identified by goal parameter optimization.

### Weaknesses
Some parts of the methodology are not clear. Please see questions below.

The PID-based goal functions and infomorphic neurons were originally proposed by Makkeh et al. 2023, and the contribution of this work is to introduce lateral connections as a third input class.
However, in the Introduction, the authors claim the PID goal function to be one of the main contributions of this paper. The authors should explain more clearly the difference between this work and Makkeh et al. 2023, 
and define their contributions more accurately.

Experiments were performed on neural nets with single hidden layer, which limits the scope of the paper. It is unclear whether the observations and insights can generalize to deeper neural networks.

Questions related to numerical computation of PID atoms:
- To compute the PID atoms during training, the authors empirically evaluated the joint probability mass function of the aggregated inputs and output of each neuron. Since the input is high-dimensional, is a large batch size 
needed for such numerical estimation to be accurate and stable? For example, the input dimension is at least 28^2 = 784 for MNIST, and each dimension is discretized to 20 levels. Is the batch size of 1024 sufficient?

- The authors mentioned that the shared-exclusion redundancy and thus the PID atoms are differentiable with respect to the probability distribution. However, in my understanding, the empirical probability mass function 
of a discrete random variable is not differentiable w.r.t. its samples. Then the goal function will not be differentiable w.r.t. a neuron's weights, which is needed for training. Could the authors clarify this point?
In particular, how is the empirical probability mass function differentiated w.r.t. the output (and subsequently the weights) of the neuron?

There seems to be a gap between the claimed "neuron-level interpretability" and the proposed learning framework. 
Usually, interpretability means understanding how a trained network makes predictions and what the network has learned.
However, the method proposed in this paper only provides interpretation for the learning objective, rather than insight of what the model and each neuron has learned. 
Furthermore, the interpretability is still global, not neuron-level, as the goal parameters are shared across all neurons, i.e., the interpretation for all neurons are the same. 
Finally, the cross-entropy loss and the backpropagation process are quite human interpretable, in my opinion.
Could the authors comment on this?

"For the supervised classification task at hand, the function ... has been chosen ... This ensures that the network performs similarly during training, when context and lateral inputs are provided, and for evaluation, 
where the context signal is withheld." It seems that the given activation function is for training, since it uses the context (label) as input. Can the authors define clearly what the activation function during testing is?

"One promising path towards constructing deeper networks is using stacked hidden layers that receive feedback from the next layer, similar to setup 3." 
It is a bit unconvincing to replace label feedback by feedback connection from the next layer. In the latter, the neuron's learning goal is to capture the part of the feedforward signal that agrees with the next layer's output, which is less intuitive than 
capturing the part that agrees with the label.

Figure 8, comparision with bivariate model: Since the goal is to compare trivariate with bivariate, it might be better to put trivariate and bivariate on the same axis. If it'd be too crowded, 
maybe group the results by "Heuristic"/"Optimized".

In "Goal parameters" paragraph in Experiments, it might be better to state that "heuristic goal function" is $\Pi_{ \{ F\} \{C\} }$. Although it can be inferred from Fig. 4, it's better to define it in the text as well.

In Fig. 4, is the difference in validation accuracy defined as "after setting to 0 - before"?

### Questions
Questions related to numerical computation of PID atoms:
- To compute the PID atoms during training, the authors empirically evaluated the joint probability mass function of the aggregated inputs and output of each neuron. Since the input is high-dimensional, is a large batch size 
needed for such numerical estimation to be accurate and stable? For example, the input dimension is at least 28^2 = 784 for MNIST, and each dimension is discretized to 20 levels. Is the batch size of 1024 sufficient?

- The authors mentioned that the shared-exclusion redundancy and thus the PID atoms are differentiable with respect to the probability distribution. However, in my understanding, the empirical probability mass function 
of a discrete random variable is not differentiable w.r.t. its samples. Then the goal function will not be differentiable w.r.t. a neuron's weights, which is needed for training. Could the authors clarify this point?
In particular, how is the empirical probability mass function differentiated w.r.t. the output (and subsequently the weights) of the neuron?

There seems to be a gap between the claimed "neuron-level interpretability" and the proposed learning framework. 
Usually, interpretability means understanding how a trained network makes predictions and what the network has learned.
However, the method proposed in this paper only provides interpretation for the learning objective, rather than insight of what the model and each neuron has learned. 
Furthermore, the interpretability is still global, not neuron-level, as the goal parameters are shared across all neurons, i.e., the interpretation for all neurons are the same. 
Finally, the cross-entropy loss and the backpropagation process are quite human interpretable, in my opinion.
Could the authors comment on this?

"For the supervised classification task at hand, the function ... has been chosen ... This ensures that the network performs similarly during training, when context and lateral inputs are provided, and for evaluation, 
where the context signal is withheld."
It seems that the given activation function is for training, since it uses the context (label) as input. Can the authors define clearly what the activation function during testing is?

"One promising path towards constructing deeper networks is using stacked hidden layers that receive feedback from the next layer, similar to setup 3."
It is a bit unconvincing to replace label feedback by feedback connection from the next layer. In the latter, the neuron's learning goal is to capture the part of the feedforward signal that agrees with the next layer's output, which is less intuitive than 
capturing the part that agrees with the label.

Figure 8, comparision with bivariate model: Since the goal is to compare trivariate with bivariate, it might be better to put trivariate and bivariate on the same axis. If it'd be too crowded, 
maybe group the results by "Heuristic"/"Optimized".

In "Goal parameters" paragraph in Experiments, it might be better to state that "heuristic goal function" is $\Pi_{ \{ F\} \{C\}}$. Although it can be inferred from Fig. 4, it's better to define it in the text as well.

In Fig. 4, is the difference in validation accuracy defined as "after setting to 0 - before"?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces trivariate infomorphic neuron model to develop an interpretable and biologically-inspired local objective function for training artificial neural networks. This abstract neuron model is based on Partial Information Decomposition (PID) framework, which decomposes information into unique, redundant, and synergistic components (atoms). Local objective (goal) function is constructed as a linear combination of these PID information atoms. Neural network models with one hidden layer and various configurations (e.g. sparse lateral connectivity, different context signal) are trained with the proposed loss function on MNIST and CIFAR10 classification tasks, demonstrating promising results.

### Strengths
* The problem is well-stated in the introduction.

* Section 3 and Section 4 effectively introduce the PID framework and explain how it is used to develop local objective functions for training neural networks.

* The shared code is well-structured, which aids the reproducibility of the work.

* MNIST results seem promising.

### Weaknesses
The paper has a few areas that could benefit from further clarification or expansion. Please see the following points and the Questions section for more details.

*  If I did not overlook it, the consistency equations for the trivariate infomorphic neuron model are not included in the paper.

* The discussion of weight updates is limited. It is mentioned that either autograd or the analytical formulation in (Makkeh et al. 2023) can be used. However, the analytical approach in (Makkeh et al. 2023) applies to  bivariate informorphic neuron model. Although the weight update derivation is potentially a similar approach, the absence of an explicit derivation raises a concern. Without this, I am uncertain if the resulting learning is biologically plausible.

* It is mentioned that (line 308) the $\gamma$ parameters can be derived from intuitive notions. However, unless I overlooked something, the explanation for determining these parameters is not provided in detail beyond a brief note in the caption of Figure 2.D.

* I am concerned that plug-in estimation of the information atoms based on empirical probability mass functions may face challenges in high-dimensional settings due to the difficulty of density estimation. While MNIST may be manageable despite being high-dimensional, this could be an issue in more complex settings.

* Lines 511-515 mention that deeper networks were trained and achieved comparable or better accuracy results; however, these results are not shown. The paper only includes experiments with a single hidden layer.

* The algorithm in Function 2 (Appendix A.1) requires quantities labeled 'isx_redundancies' and 'pid_atoms' (lines 732 and 733), but it is not specified how these quantities are computed.

* According to Appendix A.3, the proposed method requires a lot of computational power even for MNIST. This raises concerns about its scalability to more complex datasets.

* I think the abbreviation IM in Table 1 likely stands for "infomorphic networks," but this is not clarified in the paper.

**Minor Comments:**

* In line 907, the word 'function' is repeated.

* I think Figure 9 is neither referenced in the text nor is it fully interpreted beyond the caption. Given its complexity, more discussion could make it easier to understand.

### Questions
* Is the activation function in line 283 commonly used? How the $\alpha_i$ and $\beta_i$ (for $i = 1, 2$) values are determined for this activation function?

* Regarding lines 293-297, which mention that lateral connections introduce recurrence, how did you determine that presenting the same input twice is sufficient? For more complex datasets, more iterations may be needed. I am curious if the output converges after two presentations.

* Is there any particular heuristic or rationale for using 20 equally sized bins in the algorithms in Appendix A.1?

### Soundness
2

### Presentation
2

### Contribution
3
