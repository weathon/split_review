# Learning Arbitrary Logical Formula as a Sparse Neural Network Module

- Decision: Reject
- Avg Score: 4.40
- Scores: 3, 3, 8, 3, 5

## Abstract
NeSy (Neuro-Symbolic) predictors are hybrid models composed of symbolic predictive models chained after neural networks. Most existing NeSy predictors require either given symbolic knowledge or iterative training. DSL (Deep Symbolic Learning) is the first NeSy predictor that supports fully end-to-end training from scratch, but it learns a look-up table rather than arbitrary programs or formulas. We propose the Logical Formula Learner framework, a general framework of network modules that explicitly equate a logical formula after convergence. We then propose 3 novel designs within the LFL framework with different levels of combinatorial search freedom: LFL-Type1 learns arbitrary logical formula, LFL-Type2 learns a look-up table, and LFL-Type3 has combinatorial search freedom between them. LFL-Type1 and LFL-Type2 show improvements over previous designs, and all three types can be wrapped into NeSy predictors. To our knowledge, LFL-Type1-based NeSy predictor is the first NeSy predictor that supports fully end-to-end training from scratch and explicitly learns arbitrary logical formulas.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Summary:
The authors propose a Neuro-Symbolic(NeSy) method that can learn rules from perception in an end-to-end fashion. The paper aims to improve upon recent lines of work in this direction, and proposes new designs and symbol selection strategies, with different levels of noise and distributions. The paper also proposes a gradient shortcut strategy to improve the training and convergence. The paper also show experiments on synthetic MNIST based NeSy benchmarks --- widely used to test NeSy frameworks.

### Strengths
- The general idea of having membership functions for symbols is interesting, and is potentially an elegant abstraction of ideas from DSL. 
- The idea of learning rules from perception in general is very interesting, and is of significant importance in NeSy.

### Weaknesses
 - Clarity: I think the paper is very unclear. This can be significantly improved by adding a running example, and potentially moving the comparison (3.1) and parts of section 4 to the Appendix. However, the general writing of related works and introduction is not quite clear. I would suggest the authors to arrive at the main message of the paper at earlier stage in the introduction.

- Section 2.1 is well written, and well-motivated. However, 2.3 and 2.3 (in my understanding the main contributions of the paper) are not clearly presented. It is not clear why Concrete distributions help?

- Figure 3's explanation is quite unclear and imprecise.

- I am not sure, how novel the idea of gradient shortcuts is --- see questions.

### Questions
- Please summarily explain why concrete distributions help compared to $\epsilon$-greedy?
- How does your new trick compare to [1]?

[1] Simple and Effective Transfer Learning for Neuro-Symbolic Integration. Daniele et al. 2024

### Soundness
1

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work proposes a logic formula learner framework, which comprises of three components: LFL-Type1 learns arbitrary logical formula, LFL-Type2 learns a look-up table, and LFL-Type3 has combinatorial search freedom between them. This frame work is end-to-end differentiable, can converge in a single run, and can learn arbitrary logic formula with the symbolic module.

### Strengths
Originality: 2.5/5

Compared to the existing work DSL, this approach offers the ability to explicitly learn the logic equation. It introduces a Concrete distribution alongside the Godel t-(co)norm proposed in DSL, which adds noise to the soft symbolic values.

Quality: 2/5

Pros: The context and mathematical formulations are well presented.

Cons: Scalability is a significant concern, as the number of neurons correlates with the number of internal states. While DSL has demonstrated scalability up to a 1000-digit sum, this work does not address its own scalability. How complex can this approach effectively scale? In the experimental section, the random seed is fixed at 42, which is unexplained.

Clarity: 2/5

Pros: The introduction provides a clear and convincing narrative.

Cons: The figures do not effectively support comprehension. For example, while Figure 1 illustrates the different outcomes of EQL and AFL, fully understanding it requires a detailed study of both paradigms. Figure 3 is even more challenging, as the components are not well explained in the caption, and there are many variants with minor changes. Figure 4 lacks sufficient details for understanding the experiments and data fully. 

Significance: 2/5

Scalability is the primary limitation impacting the influence of this work on the neurosymbolic community.

### Weaknesses
See strengths above.

### Questions
1.  How complex can this approach effectively scale to? 
2. In the experimental section, the random seed is fixed at 42, which is unexplained.

### Soundness
2

### Presentation
2

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
The paper introduces the LFL (Logical Formula Learner), an architecture that entails and expands prior work, in particular DSL (Deep Symbolic Learning) and dNL (differentiable Logic Network) . Both prior works feature learnable logical representations. LFL proposes an architecture that includes both DSL and dNL, but within LFL the user can choose more or less representational freedom. This architecture also includes MLPs as loss shortcuts and several loss terms to control convergence.

Evaluation is done on multi-digit MNist addition, MNist-addition and on 3-layer logical formula.

### Strengths
Very well written, clearly presented.

The problem is interesting, as learning logical formulae opens many doors for NeSy learning.

The approach seems to be mostly original: The foundations (DSL and dNL) were clearly acknowledged and delineated from original contributions by the authors.

### Weaknesses
Figure 4(d) seems a bit dishonest. Apparently DSL's poor performance is down to solely training mode settings. This should be presented more clearly and transparently, e.g. by showing test performance.

The paper could use a comparison to some of the competing branches of related work, e.g. differentiable/neural ILP.

Various typos:
Typo achieved / archived bottom of page 1.
Fig 3's caption: references to "such as [9] and [16]" should probably read "such as Equations [9] and [16]".
"In these networks we also constrain**t**" -> "In these networks we also constrain".

### Questions
It is not completely clear to me to what degree other approaches rely on the same amount of practical/engineering tricks to achieve proper convergence. I'm under the impression that e.g. ILP does not need this as heavily, but I also have to admit to not being an expert on logic formula learning.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors study three variants of differentiable inductive logic programming to both learn end-to-end neural classifiers and rules in a NeSy predictor setup. The architecture is based on a form of fuzzy operators with added stochasticity.

### Strengths
The task of learning both rules and classifiers is quite challenging, and the addition of noise via the Concrete distribution could be a good solution to this.

### Weaknesses
Currently, the paper is hard to follow, with a lot of abbrevations (it is difficult to remember what LFL-Type1-3 are!). The problem setup is not well-defined. I could infer it from my background, but this should be clear. I found it difficult to follow exactly how the 5 models (dNL, DSL and LFL-Type-i) fit in. The different LFL types are poorly motivated, and just are defined separately. Finally, the paper misses some critical related work, limiting the novelty of the paper.

The paper is limited in evaluation. It is only evaluated on a single task (MNIST Addition) and has a major problem in dataset setup which I will discuss below. Some different datasets, ideally also with different visual datasets than MNIST, would help with convincing that this model can properly learn.

- The paper is missing several existing works on learning end-to-end learning: [1-5], of which [1-4] also learn proper logic rules. Furthermore, [4-6] are papers that also use an MLP loss / 'gradient shortcut' to (pre-)train the classifiers, which is critical to getting these systems to work. This is therefore not a new trick.  
- I understand the relation to EQL, and it's good to cite it, but outside of inspiration, these two methods are not that directly related? It seems like LFL is more like differentiable inductive logic programming in the sense of [7] than symbolic regression. 
- The footnote 2 is not correct: Scaling these weights does more than scaling the learning rate as it changes how close to 0.5 the average values of g(w_i) are. This means the derivatives of other parts of your system will change.
- The 'LFL' framework is not clearly and formally defined. What are the constraints on the different choices of the functions?
- The motivation for the linear reconstruction model is not clear to me. Is this purely for debugging? 
- The data in MNIST Addition is not binary, so why is a binary cross-entropy loss used? 
- What is the motivation for the label loss? 
- Figure 3 can be trimmed significantly: A single one of these 4 images should suffice by just denoting what is optional. 
- The architecture for multi-digit MNIST Addition in DSL (which I think is copied here) is highly specific to this task - How would this extend to different tasks?
- An experiment on data different than MNIST would be nice - MNIST is easily clusterable, making the MLP shortcut a useful signal, but this isn't the case for all data. 
- The dataset setup for MNIST Addition is not correct and uses infinite data, while the canonical setup in the community is to take the training images, and randomly create a partition of them for different sums, giving finite data. The dataset is then about 60.000/2N in size - making the problem harder to train for larger multi-digit problems. This should be fixed.
- The relevance of experiment 3.1.1 could be clearer
- Experiment 3.2: I don't understand this result. There is nothing wrong with different training vs inference behaviour and this is standard in many DL layers. The label on Figure 4.d is unclear: This is _test_ accuracy under _training_ mode, right? 

Minor
- The writing contains some typos. Eg: 052: Archived by - achieved by, 519: Conclution -> conclusion
- Be careful with quotes '', they should be different when opening

### Questions
- The paper is missing several existing works on learning end-to-end learning: [1-5], of which [1-4] also learn proper logic rules. Furthermore, [4-6] are papers that also use an MLP loss / 'gradient shortcut' to (pre-)train the classifiers, which is critical to getting these systems to work. This is therefore not a new trick.  
- I understand the relation to EQL, and it's good to cite it, but outside of inspiration, these two methods are not that directly related? It seems like LFL is more like differentiable inductive logic programming in the sense of [7] than symbolic regression. 
- The footnote 2 is not correct: Scaling these weights does more than scaling the learning rate as it changes how close to 0.5 the average values of g(w_i) are. This means the derivatives of other parts of your system will change.
- The 'LFL' framework is not clearly and formally defined. What are the constraints on the different choices of the functions?
- The motivation for the linear reconstruction model is not clear to me. Is this purely for debugging? 
- The data in MNIST Addition is not binary, so why is a binary cross-entropy loss used? 
- What is the motivation for the label loss? 
- Figure 3 can be trimmed significantly: A single one of these 4 images should suffice by just denoting what is optional. 
- The architecture for multi-digit MNIST Addition in DSL (which I think is copied here) is highly specific to this task - How would this extend to different tasks?
- An experiment on data different than MNIST would be nice - MNIST is easily clusterable, making the MLP shortcut a useful signal, but this isn't the case for all data. 
- The dataset setup for MNIST Addition is not correct and uses infinite data, while the canonical setup in the community is to take the training images, and randomly create a partition of them for different sums, giving finite data. The dataset is then about 60.000/2N in size - making the problem harder to train for larger multi-digit problems. This should be fixed.
- The relevance of experiment 3.1.1 could be clearer
- Experiment 3.2: I don't understand this result. There is nothing wrong with different training vs inference behaviour and this is standard in many DL layers. The label on Figure 4.d is unclear: This is _test_ accuracy under _training_ mode, right? 

Minor
- The writing contains some typos. Eg: 052: Archived by - achieved by, 519: Conclution -> conclusion
- Be careful with quotes '', they should be different when opening


[1] Li, Zenan, et al. "Neuro-symbolic learning yielding logical constraints." Advances in Neural Information Processing Systems 36 (2024).

[2] Wang, Po-Wei, et al. "Satnet: Bridging deep learning and logical reasoning using a differentiable satisfiability solver." International Conference on Machine Learning. PMLR, 2019.

[3] Cunnington, Daniel, et al. "The role of foundation models in neuro-symbolic learning and reasoning." International Conference on Neural-Symbolic Learning and Reasoning. Cham: Springer Nature Switzerland, 2024.

[4] Aspis, Yaniv, et al. "Embed2Rule Scalable Neuro-Symbolic Learning via Latent Space Weak-Labelling." International Conference on Neural-Symbolic Learning and Reasoning. Cham: Springer Nature Switzerland, 2024.

[5] Daniele, Alessandro, et al. "Simple and Effective Transfer Learning for Neuro-Symbolic Integration." International Conference on Neural-Symbolic Learning and Reasoning. Cham: Springer Nature Switzerland, 2024.

[6] Aspis, Yaniv, et al. "Embed2Sym: scalable neuro-symbolic reasoning via clustered embeddings." Kern-Isberner G, Lakemeyer G, Meyer T, editors. Proceedings of the 19th International Conference on Principles of Knowledge Representation and Reasoning (KR2022); 2022 Jul 31-Aug 5; Haifa, Israel.[California]: IJCAI Organization; 2022. p. 421-31.. International Joint Conferences on Artificial Intelligence Organization, 2022.

[7] Evans, Richard, and Edward Grefenstette. "Learning explanatory rules from noisy data." Journal of Artificial Intelligence Research 61 (2018): 1-64.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposed a general framework of network modules that explicitly equate a logical formula after the convergence of another neural network. The model is end-to-end differentiable, and training all modules from scratch achieving joint convergence in a single run, and explicitly learning arbitrary logical formulas (within limited complexity) with its symbolic module.

However, I think this work is borderline rejected because of the following reasons:
1. Some notations are not defined clearly and are used wrong. 
2. The structure of the manuscript is too messy to determine which part is the novelty and which is the preliminaries.

### Strengths
The authors conduct experiments with multiple settings to learn rules from a CNN model. The authors open their source code for the reference.

### Weaknesses
1. The structure of the paper is not clear to present which part is the novel contribution and which part is the preliminary work. For example, Sections 2.2.1 and 2.2.2 describe the Differentiable Neural Logic Network (dNL) Deep Symbolic Learning (DSL), these statements should be listed together in Preliminaries, not the contribution section. Furthermore, the terminology in Sections 2.2.1 and 2.2.2 should have citations. 
2. Some formats do not fit the standard such as ‘define in 6’ in line 156 and ‘16 is also’ in line 241.  
3. Some definitions are not very clear such as the ‘binary data’ in 103. The term 'binary data' is used without specifying whether it refers to binary classification labels, binarized input features, or some other form of binary representation. This lack of clarity makes it difficult to understand the scope and applicability of the proposed method. 
4. The authors only compare performance with Deep Symbolic Learning (DSL) proposed by Daniele et al., 2022. I think there should be more benchmarks to prove the performance of the proposed methods experimentally. The lack of comparison with other relevant methods in the literature makes it difficult to assess the true novelty and effectiveness of the proposed approach. The experimental results are not convincing enough to show the advantage of the proposed method.

### Questions
1. There is no formal definition of ϵ-greedy policy in line 171, page 4. 
2. There is no formal definition or citation for Gödel t-(co)norm in line 215 page 4. 
3. The input of the softmax function is a vector. However, the input of the softmax function defined in Equation (9) line 173 page 4 is a real number, which is hard to be understood by readers.

### Soundness
2

### Presentation
1

### Contribution
3
