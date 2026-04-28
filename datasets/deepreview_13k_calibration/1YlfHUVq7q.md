# Error Broadcast and Decorrelation as a Potential Artificial and Natural Learning Mechanism

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 8, 5

## Abstract
We introduce the Error Broadcast and Decorrelation (EBD) algorithm, a novel learning framework that addresses the credit assignment problem in neural networks by directly broadcasting output error to individual layers. The EBD algorithm leverages the orthogonality property of the optimal minimum mean square error (MMSE) estimator, which states that estimation errors are orthogonal to any nonlinear function of the input, specifically the activations of each layer. By defining layerwise loss functions that penalize correlations between these activations and output errors, the EBD method offers a principled and efficient approach to error broadcasting. This direct error transmission eliminates the need for weight transport inherent in backpropagation. Additionally, the optimization framework of the EBD algorithm naturally leads to the emergence of the experimentally observed three-factor learning rule. We further demonstrate how EBD can be integrated with other biologically plausible learning frameworks, transforming time-contrastive approaches into single-phase, non-contrastive forms, thereby enhancing biological plausibility and performance. Numerical experiments demonstrate that EBD achieves performance comparable to or better than known error-broadcast methods on benchmark datasets. The scalability of algorithmic extensions of EBD to very large or complex datasets remains to be explored. However, our findings suggest that EBD offers a promising, principled direction for both artificial and natural learning paradigms, providing a biologically plausible and flexible alternative for neural network training  with inherent simplicity and adaptability that could benefit future developments in neural network technologies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new learning framework for neural networks that directly broadcasts output error to individual layers. The main idea is to minimize the correlation between the layer activations and output errors, which is based on the orthogonality property of minimum mean square error estimators developed by Papoulis&Pillai 2002 [1]. The framework is implemented on MNIST and CIFAR10 benchmark tasks for MLP and CNN.

### Strengths
1.	The paper proposes a novel idea that uses the orthogonality property of the optimal MMSE, which avoids weight symmetry problem in conventional backpropagation.
2.	Compared with direct feedback alignment (DFA) method, the proposed EBD method provides better theoretical illustration and the results in MNIST and CIFAR-10 tasks are better.

### Weaknesses
1. The method still faces the critical issue of scaling up, as most of non-BP learning frameworks exist.
2. The experiments show EBD is only slightly better than DFA, while it is not comparable with other SOTA biologically plausible methods (e.g. Hebbian base method [2])


See the above weaknesses. Moreover:

1.	Why does BP in Table 2 show such a low performance? Did the authors try to use a different CNN architecture to get a better performance?  
2.	The MMSE estimator-based derivation looks great, but in terms of network training, is optimal MMSE estimator the best objective of an arbitrary defined network? (since different tasks might have different loss functions)

### Questions
See the above weaknesses. Moreover:

1.	Why does BP in Table 2 show such a low performance? Did the authors try to use a different CNN architecture to get a better performance?  
2.	The MMSE estimator-based derivation looks great, but in terms of network training, is optimal MMSE estimator the best objective of an arbitrary defined network? (since different tasks might have different loss functions)

Ref:

[1] Athanasios Papoulis and S Unnikrishna Pillai. Probability, Random Variables, and Stochastic Processes. 2002

[2] Journe et.al., Hebbian deep learning without feedback, ICLR 2023

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
3

### Summary
In this paper, the authors introduce the Error Broadcast and Decorrelation (EBD) algorithm as a novel method for implementing gradient descent in deep neural networks. This approach addresses the limitations of traditional backpropagation (BP), which requires biologically unrealistic components such as weight transport and symmetric feedback pathways. The EBD algorithm builds on a key theorem from minimum mean square error (MMSE) estimation, which states that the output error of an optimal estimator is orthogonal to any function of the input. Leveraging this property, the authors propose that the activations in each layer, as functions of the input, be orthogonal to the output error. This orthogonality condition forms the basis for their weight update rule, which aims to decorrelate activations and output errors at each layer. The proposed EBD framework demonstrates competitive performance with BP on benchmark datasets like MNIST and CIFAR-10, particularly in fully connected and simpler architectures. The authors also explore potential extensions to the algorithm, including regularization techniques and forward projection of activations, to enhance stability and performance.

### Strengths
1. **Compelling Biological Motivation**: Exploring error broadcasting and feedback alignment as methods for implementing gradient descent in neural networks holds significant promise for biological plausibility. These approaches circumvent the weight transport problem by directly transmitting error signals to deeper layers. This work introduces an innovative algorithm within this framework, which exhibits improved performance compared to previous error broadcasting methods.

2. **Normative Approach and Theoretical Foundation**: The algorithm’s development, rooted in the theoretical orthogonality property of an optimal MMSE estimator, is intriguing. Framing this method as a normative approach that leverages optimal predictor properties is commendable. However, as noted below, a potential misuse of this theorem raises concerns.

3. **Practical Demonstration with Numerical Results**: The empirical findings showcase the proposed algorithm's practicality, albeit with limitations. Its reported performance on benchmark datasets suggests that it is competitive with state-of-the-art alternatives under certain conditions.

### Weaknesses
1. **Theoretical Assumptions and Interpretation**: The reliance on the theorem regarding the orthogonality of an optimal estimator’s error to any function of its input, while foundational, is problematic when extended in reverse. The paper does not adequately explain the consequences of requiring orthogonality between output error and hidden layer activations. Furthermore, in most applications and architecture, the dimensionality of the hidden layers is very large. Constraining a solution to be orthogonal to a single direction is weak, and its benefits are poorly defined. This gap leaves uncertainty regarding how orthogonality aids learning or inference. Thus, the theoretical basis appears tenuous and potentially misapplied.

3. **Ambiguity in Performance Implications**: Although the algorithm performs well on real datasets, this success might stem from something other than the stated theoretical premise. The observed gains could be attributed to a different mechanism, such as orthogonal representations of different classes, rather than the error signal’s orthogonality. It would be valuable for the authors to test whether the performance improvement is due to orthogonalized class representations or if it is indeed a result of their premise. A comparative baseline using local class orthogonalization with an SGD-trained readout on the penultimate layer would provide insights into the true contribution of the proposed mechanism.

4. **Biological Plausibility of Batch Learning**: The paper’s claim of biological relevance is weakened by the batch learning requirement, which necessitates retaining and normalizing the entire batch at each layer. While replacing weight transport and feedback pathways with error broadcast is a step toward biological realism, the reliance on batch-based updates undercuts this claim. The authors should consider the feasibility of online, more biologically plausible approaches and address whether the proposed method truly enhances biological plausibility. Alternatively, the paper can focus on the mathematical foundation of error broadcasting and not on biological realistic implementations of gradient descent.

5. **Lack of Clarity in Possible Extensions**: In Section 4, the authors introduce several extensions to the EBD algorithm. The first involves regularization techniques aimed at preventing layer collapse. While preventing collapse is essential for maintaining active and diverse representations, the specific normalization methods proposed are neither novel nor particularly informative. Their inclusion does not substantially enhance the originality of the work.
   The second extension discussed is the forward projection of neural activations onto the output or penultimate layer, followed by an orthogonalization process at that stage. The rationale behind this step remains unclear. The manuscript provides no compelling biological basis for this projection mechanism, suggesting that its primary motivation is performance optimization rather than biological plausibility. Notably, the statement in line 448—“This projection facilitates the optimization of the decorrelation loss by adjusting the parameters of the final layer”—is ambiguous. It lacks a clear, rigorous mathematical explanation that would elucidate how this projection supports the training process. A more detailed formulation or analysis is necessary to justify the inclusion and clarify the impact of this component on the algorithm’s overall functionality.

6. **Performance Analysis on Complex Architectures**: The results presented in Section 5 show that the algorithm's performance is almost on par with backpropagation. However, demonstrating performance close to BP on simpler datasets, such as MNIST or fully connected networks trained on CIFAR-10, is not sufficiently informative. While useful as initial proof-of-concept validations, these comparisons do not substantiate the broader claims of the algorithm’s novelty or practical utility. Combined with the previously mentioned theoretical limitations, the results fall short of convincingly demonstrating the value and distinct advantages of the proposed EBD approach.

### Questions
1. The premise of this work hinges on the orthogonality of the error of the optimal estimator to the neural representations. However, the reverse is not addressed: a vector that is orthogonal to a set of functions of the input is not necessarily indicative of an optimal estimator, and functions orthogonal to the estimator may not be meaningful. Could you clarify the theoretical foundation of your algorithm and its precise connection to the theorem you reference?

2. To strengthen your claims, it would be helpful to demonstrate that the performance improvements are not solely due to orthogonalizing representations in each layer. Your experimental results primarily focus on training fully connected networks on MNIST and CIFAR-10, raising the possibility that similar gains could be achieved through layer-wise orthogonal class representations with SGD applied only at the output. Can you comment on this possibility or provide additional evidence?

3. Is there a potential for an online version of your algorithm that eliminates the need for batch learning? If so, how would this be implemented?

### Soundness
2

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
The authors propose a method for training neural networks based on decorrelating layer activities with the output error. This method avoids the need for backpropagation and is a potential solution to the weight transport problem.

### Strengths
- the text is generally well written
- the theoretical building block in which this is built - that optimal nonlinear MMSE estimators hvae error orthognoal to functions of input - is interesting and in my view certainly deserves the attention given by the authors. Its implementation - and therefore this paper - should be of value to both ML and neuroscience researchers.
- it is clear the authors have a good grasp of the theory and technical details of the models considered, and the approach in general seems well thought out
- relevant literature appears to be duly cited and compared, though I am a non-expert in this field
- the numerical results presented in section 5 appear impressive, though I would prefer they were elaborated upon a bit more.

### Weaknesses
 - The paper is rather dense, and I worry that it harms its accessibility. It seems to me some of the technical details/results can be sacrificed to the appendix in place of more motivation/clarification. For example, section 3.2, and the relationship to corinfomax in general, is very difficult to grasp. The motivation seems to be that corinfomax is a biologically plausible model, but I don't understand why corinfomax-EBD is more biologically plausible than the implementation in 2.3. What was the original implementation lacking that corinfomax-EBD addresses?
- As per above, I would appreciate any more insight into the results and comparison vs other models. E.g. do you have any intuition as to why EBD outperforms NN-GEVB and MS-GEVB? For the corinfomax models it seems that the benefit of EBD is that it avoids the two-phases (?), but is there a reason it makes significantly improvements on the CIFAR-10 dataset?
- the notation can sometimes be sloppy (see below)

- in line 156 is N_k the size of layer k? this should be specified
- that g can be any nonlinear function seems a powerful result. How much did you explore its possibilities? It seems a big hyperparameter to choose but I didn't get a feel for what it should be
- the error epsilon is a vector so why is it not in bold? (it currently appears as a scalar)
- for non-linear networks the error landscape is typically non-convex and has many local optima which are found during learning instead of one global optimum. How does the main theoretical results (lemmas A.1/A.2 tie in with this?
- for the equation in line 199 R is defined recursively, but what is R[0]?
- does the forgetting factor lambda lie in [0,1]?
- In section 2.3 what do W_1, W_2 mean? Do they directly related to W (e.g. the first/second column). I presume not given equations 6/7 but if they don't they should be called something else
- to what extent does EBD depend on batch size? It seems like it would require large batches to get a good correlation estimate, but this doesn't seem to fit in with the biological plausibility of the algorithm?
- Why is EBD a 3-factor learning rule but not backprop? is it not possible to consider the post-synaptic/modulatory signal as the error gradient with respect to the pre-synaptic neuron?
- in 3.2 why are the corinfomax equations which involve determinants etc biologically plausible? It's not clear to the non-expert reader. Given there are lateral connections, are we also dealing with RNNs instead of feedforward nets now?
- in algorithm 1 why are activations H and errors E and bias B now in caps? Also the link to the corinfomax equations above is not clear to me at all
- In section 4 line 393 it's written that these extensions are 'building on the CorInfoMax-EBD algorithm', but I don't understand why they can't also be applied to standard MLP?
- Could the power normalization equation in 4.1.1 not be written as a norm over the batch. I personally find the notation with [n] confusing
- out of interest is 4.1.2 itself bio-plausible?
- typos: line 398: period after stability; line 709: linear -> non-linear.

### Questions
- in line 156 is N_k the size of layer k? this should be specified
- that g can be any nonlinear function seems a powerful result. How much did you explore its possibilities? It seems a big hyperparameter to choose but I didn't get a feel for what it should be
- the error epsilon is a vector so why is it not in bold? (it currently appears as a scalar)
- for non-linear networks the error landscape is typically non-convex and has many local optima which are found during learning instead of one global optimum. How does the main theoretical results (lemmas A.1/A.2 tie in with this?
- for the equation in line 199 R is defined recursively, but what is R[0]?
- does the forgetting factor lambda lie in [0,1]?
- In section 2.3 what do W_1, W_2 mean? Do they directly related to W (e.g. the first/second column). I presume not given equations 6/7 but if they don't they should be called something else
- to what extent does EBD depend on batch size? It seems like it would require large batches to get a good correlation estimate, but this doesn't seem to fit in with the biological plausibility of the algorithm?
- Why is EBD a 3-factor learning rule but not backprop? is it not possible to consider the post-synaptic/modulatory signal as the error gradient with respect to the pre-synaptic neuron?
- in 3.2 why are the corinfomax equations which involve determinants etc biologically plausible? It's not clear to the non-expert reader. Given there are lateral connections, are we also dealing with RNNs instead of feedforward nets now?
- in algorithm 1 why are activations H and errors E and bias B now in caps? Also the link to the corinfomax equations above is not clear to me at all
- In section 4 line 393 it's written that these extensions are 'building on the CorInfoMax-EBD algorithm', but I don't understand why they can't also be applied to standard MLP?
- Could the power normalization equation in 4.1.1 not be written as a norm over the batch. I personally find the notation with [n] confusing
- out of interest is 4.1.2 itself bio-plausible?
- typos: line 398: period after stability; line 709: linear -> non-linear.

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
4

### Summary
This work proposes a novel optimization method called the “Error Broadcast and Decorrelation” (EBD) algorithm. This algorithm attempts to obtain the optimal minimum mean square error (MMSE) estimator by meeting its core criteria: that at optimum, there is zero correlation between an error signal and non-linearly transformed encodings of data. This enables a new perspective on error broadcasting which attempts to capture correlations between errors and neural network layer activations and uses this correlation (covariance) structure to propagate and thereafter minimise correlation. This effectively results in a decorrelation between error and layer-wise activations once converged. This method is combined with a number of additions to stabilize network activity norms and encourage activation entropy within network layers, as well as being integrated into the CorInfoMax framework. This method is finally tested by training of multilayer perceptrons and convolutional networks with the MNIST and CIFAR10 tasks.

### Strengths
- This work contributes a new perspective for measurement of a final optimum of network training based upon the MMSE estimator in a principled manner based upon the orthogonality of error and layer-activations.
- The paper describes this method and its drawbacks within the methods section at length and covers a set of failure modes and extensions.
- Detailed descriptions of the mathematical steps and hyperparameters of models tested are given.

### Weaknesses
 - Of major and significant concern are the claims of this paper in comparison to existing work by Clark et al. 2021. Specifically, the results of this paper are presented in direct comparison to trained models in earlier work (Clark et al.) while claiming outperformance. However, this paper integrates a number of elements to the training scheme that are not present in the original comparison work. For example, the code and tables of this paper suggest that among other additions this work makes use of a learning rate scheduler, as well as potentially using many more epochs of training (unclear). In comparison, the original work by Clark et al. has no learning rate scheduler and far fewer training hyperparameters in general. This suggests that the comparison is entirely inappropriate. To provide a genuine comparison, I would encourage the authors to carry out a reimplementation and rigorous test against existing methods (at least against BP) in which the same degree of parameter searching/sweeping is carried out for all methods compared. Otherwise comparison is uninformative at best, and misleading at worst. For these reasons, the results in Tables 1 and 2 cannot in their current form be trusted to provide understanding of the relative efficacy of training methods.
- This paper claims to provide a novel biologically plausible learning mechanism (even in the title), however to make this method work, a power normalizing and entropy encouraging mechanism is added to network dynamics. It is not discussed whether these are reasonable mechanisms within a biologically plausible context. Furthermore, the method relies on batch-based updates for the calculation of the entropy regularizer, which is not biologically plausible. The use of batch statistics for normalization and entropy calculation requires storing and processing information across multiple data samples, which is unlikely to be implemented in biological neural networks. This undermines the claim of biological plausibility.
- The current set of simulations results are sufficiently limited that it is not clear whether this method would scale. In particular, biologically-plausible rules can succeed at tasks such as MNIST or  CIFAR-10 level but fail completely at large scale (see Bartunov et al. 2018, Neurips). Currently, there are no explanations of how well this method might do when scaled to harder datasets, or even how well it scales when network width or depth is modified. Without measures of performance across network scale and task complexity, it is not possible to know whether this method’s performance is robust to depth/task-complexity.
- The description of this work’s method is comprehensive but requires a reader to go back and forth to understand it well. For example, the added extensions to EBD, which are used during training, are described with some distance after the main method (in Section 4) making it difficult to understand all moving parts of the simulation in a single read. Furthermore, the paper in general is too heavy on the methods aspects leaving zero room for interpretation of results and discussion. A refactoring of the paper in these respects would greatly help its readability and contribution as well as enabling a more complete discussion on the implications of the work.

### Questions
The weaknesses section above contains most of my concerns which should be addressed for an increased score. Here a few additional questions are posed.
- How might the mechanisms for power normalization and layer entropy be a plausible addition to biological neural networks?
- Can this framework be extended beyond the MSE loss case? In practice, loss functions in the deep neural network literature are often very different than an MSE loss. In Appendix E.2, correlation curves are shown for the Categorical Cross Entropy loss, however it is unclear if this was used in practice to train networks. Clarity would be appreciated.
- The computational complexity of the method and the proposed additional learning of correlation structures is not much discussed. How much might such a method cost in this regard?

### Soundness
2

### Presentation
2

### Contribution
2
