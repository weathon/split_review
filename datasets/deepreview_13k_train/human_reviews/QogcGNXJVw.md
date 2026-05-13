# The Computational Complexity of Circuit Discovery for Inner Interpretability

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
Many proposed applications of neural networks in machine learning, cognitive/brain science, and society hinge on the feasibility of inner interpretability via circuit discovery. This calls for empirical and theoretical explorations of viable algorithmic options. Despite advances in the design and testing of heuristics, there are concerns about their scalability and faithfulness at a time when we lack understanding of the complexity properties of the problems they are deployed to solve. To address this, we study circuit discovery with classical and parameterized computational complexity theory: (1) we describe a conceptual scaffolding to reason about circuit finding queries in terms of affordances for description, explanation, prediction and control; (2) we formalize a comprehensive set of queries that capture mechanistic explanation, and propose a formal framework for their analysis; (3) we use it to settle the complexity of many query variants and relaxations of practical interest on multi-layer perceptrons (part of, e.g., transformers). Our findings reveal a challenging complexity landscape. Many queries are intractable (NP-hard, $\Sigma^p_2$-hard), remain fixed-parameter intractable (W[1]-hard) when constraining model/circuit features (e.g., depth), and are inapproximable under additive, multiplicative, and probabilistic approximation schemes. To navigate this landscape, we prove there exist transformations to tackle some of these hard problems (NP- vs. $\Sigma^p_2$-complete) with better-understood heuristics, and prove the tractability (PTIME) or fixed-parameter tractability (FPT) of more modest queries which retain useful affordances. This framework allows us to understand the scope and limits of interpretability queries, explore viable options, and compare their resource demands among existing and future architectures.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies the computational challenges surrounding the fields of circuit discovery and mechanistic interpretability. Achieving circuit discovery or accurate and precise interpretability at scale is a major empirical challenge for deep learning today. This paper sheds light on why that goal might be computationally out of reach by showing that many of the tools we use today end up having to solve computationally hard problems. Some of the specific problems the paper studies computational complexity of are:

1. Sufficient circuit – finding a small sub-circuit which reproduces the behavior of the network on a specific input or all inputs.
2. Gnostic neurons – a set of neurons with maximally distant activations of certain subsets of inputs we are trying to classify between.
3. Circuit Ablation and Clamping
4. Circuit patching
5. Circuit robustness
6. Sufficient reasons

For all these different problems, the paper studies the computational hardness of the general problem, fixed-parameter tractability, hardness of approximation (additive, multiplicative and probabilistic).
They show that while some of these problems are solvable in poly time (like gnostic neurons) most remain hard even to approximate. However, some are NP-complete and have reductions from 3SAT which leaves the promise of SAT-solver heuristic being applicable for these problems.
In addition, for some problems the results show a separation between local notion of interpretability (which captures a certain property only on a small set of inputs) and a global notion (which captures the property over the entire input range). Such separations are proposed as a reason for why local explanations of faithfulness in the past have been shown to be at times fickle.

### Strengths
-	The paper tackles an important conceptual question facing empirical deep learning today. Although its results are theoretical and computational complexity has faced criticism in the past of being overly pessimistic, it is nevertheless a stellar guiding light as to what problems are tractable and might be solvable without requiring any additional assumptions.
-	The paper provides some transformations/additional assumptions with which some of the problems to be solved start becoming tractable.
-	The paper is quite comprehensive in its coverage of different notions and tools used in mechanistic interpretability literature.
- Even if computational hardness for many of the problems being studied is to be expected by theorists, it is important to compile the results and clearly state the message as it might help guide practitioners search for tractable notions of interpretability.

### Weaknesses
 - 	Computational complexity of PAC learning MLPs is a well-studied problem by the learning theory community and has connections to many of the results you study here. A comparison to some of the hardness results already known there is in order. Specifically, the paper should discuss how the hardness results for finding circuits within a trained network relate to the hardness of learning the network itself. For instance, are there reductions that can be made between these problems or are they fundamentally different? A discussion of the landscape of known hardness results in learning theory is needed to contextualize the presented results.
- 	The assumption of applying a step function on the output is quite stringent. It is known that being able to see a real-valued output rather than a Boolean output can make some learning problems on neural nets tractable [1]. The results of the paper would be stronger and more significant if they hold without the step function being applied at the end. The reliance on a step function may limit the applicability of the results to more realistic scenarios where outputs are continuous. Furthermore, the paper does not explore the impact of different activation functions on the complexity results. Could using different activation functions, such as sigmoid or tanh, change the computational hardness of the studied problems?
- 	For most of the interpretability tasks, the notion of approximation considered to measure the quality of the sub-circuit found allows for some amount of flexibility in capturing the output behavior. This axis of approximation doesn’t seem to be addressed in your work (apologize if I missed it). Could the landscape change for any of the problems when considering such an approximation. For example, if we allow the sub-circuit to only approximately match the behavior of the original circuit, might some of the NP-hard problems become tractable or admit polynomial-time approximation schemes?

### Questions
-	What is the valid criticism of zero-ablation? (line 285)
-	Can you add a brief discussion on how your results relate to some computational hardness results known for PAC-learning variants of neural networks. In particular, I’m curious to understand if any of your results follow more directly from some of the hardness reductions considered in these works. Some example works (a non-exhaustive list) are cited below ([1-3]).
-	What happens if we relax the assumption of having a step function at the output layer? Would most of the problems studied continue to remain intractable. (note that now we can also allow for an approximation in the quality of the output. i.e. the sub-circuit doesn’t have to exactly match the behavior of the original circuit, it can be approximately close)


1. On the computational efficient of training neural nets. Livni et. al.
2. On the complexity of learning neural networks. Song et. al.
3. Learning deep neural networks is fixed-parameter tractable. Chen et. al.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors frame a large number of circuit discovery problems in mechanistic interpretability as a set of formally defined queries about computational graphs.
They identify and prove the complexity classes for each of these queries. They also find the fixed-parameter complexity classes and the complexity of several types of approximations to the optimal algorithms.

### Strengths
This is the first formal characterization of the complexity of circuit discovery that I am aware of. It is very useful for the field to formalize problems such that they can be reasoned about with clarity. The formal characterization is also useful to clearly enumerate all the types of circuit queries that mechanistic interpretability researchers might want to perform to understand networks.

The paper is extremely thorough in covering a wide range of queries. The proofs that I read in detail (Appendix B on Minimum Locally Sufficient Circuits) appeared to be correct.

### Weaknesses
It is unclear to what extent these results should be major considerations for applied circuit discovery in real models. Heuristics such as gradient magnitude may be powerful enough to achieve close to optimal solutions with simple algorithms. The authors should include discussions of this to clarify.

The paper is primarily of use to researchers in mechanistic interpretability. Yet many researchers in the field will struggle to quickly understand much of the paper due to terse explanations of basic concepts in complexity theory. To some extent this is unavoidable as it would be arduous to include extensive tutorials on basic concepts from complexity, but a few well-chosen explanations could go a long way to bridge the gap for researchers who have some background in computer science. For example, more intuitive definitions of fixed parameter complexity, W[1]-hard and $\Sigma^{p}_{2}$-hard could be fairly concise and save many readers from needing to search for external resources.

Further, it would be useful to spell out more explicitly for less familiar readers how each proof connects to real world applications of circuit discovery. For example, since transformers contain MLPs, the proofs of complexities of queries on MLPs also apply to neuron level circuit discovery in transformers. Similarly, since binary vectors are a subset of the possible inputs to a real model, some proofs apply to models which are not constrained to binary inputs.

Since real models do not have binary activations, it is almost impossible for a circuit to achieve perfect faithfulness. In practice, we want our circuits to produce outputs that are sufficiently close to the full model output. But the problems considered by the authors ask for circuits that are perfectly faithful. So the authors should discuss whether their results apply in practice to realistic circuit discovery requirements.

Some smaller nitpicks:
- In Table 2: The notation “ “ is unclear because it looks like it could mean the same value as the previous row. It would be clearer to use a faded font or simply leave the box empty.
 - In Table 2: There is no explanation of "Coverage In" vs "Coverage Out".
 - I don’t understand why the coverage out of local circuits is empty.
 - In Appendix A.3 there is no explanation of function g(k).
 - In Appendix A.4.1 the variable I (instances) should be explained in the first paragraph.
 - In Appendix B, in the definition of MLSC, it’s unclear what the purpose of the constant c is.
 - In Appendix B, in Table 5, the third column is not labeled.
 - In Appendix B.2 make it clear which parts of proofs are being repeated from earlier parts.

### Questions
Some proofs rely on step functions being applied to neuron activations. To what extent do these proofs apply to neural networks with only ReLU activation functions? I believe that ReLU MLPs can approximate step functions, but not implement them exactly. Alternatively, could you extend your proofs such they don't rely on step functions?

### Soundness
4

### Presentation
2

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
This paper presents a framework for examining the computational complexity of generating various types of "interpretability queries" within the field of mechanistic interpretability. Unlike previous work that explored the complexity of post-hoc explanations for different ML models, primarily focusing on explanations in the input domain, this paper extends these findings by providing similar forms of explanations (specifically for neural networks) at the neural level rather than the input level. The paper also introduces complexity results for different mechanistic interpretability queries, demonstrating the intractability of some queries while proving that others are tractable, especially under certain relaxations.

### Strengths
The paper's primary strength lies in bridging two distinct areas of interest: (1) the formal analysis of the computational complexity involved in generating various forms of explanations (as explored in [1] and [2]), which often fall under the sub-domain known as "formal explainable AI," and (2) the more contemporary field of mechanistic interpretability. While prior work has proposed using the computational complexity of post-hoc explanations to shed light on interpretability (e.g., [1], [2]), this paper extends that concept by linking it to mechanistic interpretability queries. I believe this approach has the potential to inspire further research in both domains, facilitating a more rigorous analysis of mechanistic interpretability, an area that is currently somewhat underexplored. Additionally, this work offers a thorough categorization of different mechanistic interpretability queries, providing a solid foundation for future studies.

[1] Model Interpretability through the Lens of Computational Complexity (Barcelo et. al, Neurips 2020)

[2] Local vs. Global Interpretability: A Computational Complexity Perspective (Bassan et. al, ICML 2024)

### Weaknesses
1. The paper does not clearly discuss its limitations. I would be interested in hearing from the authors what they consider to be the main limitations of their work. While the paper focuses on neuron-level explanations, one evident (potential) limitation is the lack of clarity around the definition of the input space domain. From my understanding, it appears to be binary, but is that correct? Or is the input space discrete or continuous? Given that this research centers on neural networks, rather than simpler models where binary or discrete domains are more common, it would be reasonable to also consider more complex domains, such as continuous ones. Additionally, transitioning to continuous input settings could have significant implications for the complexity of the problem. This should (at the very least) be discussed by the authors.

2. Many of the proofs presented in the paper appear to be relatively straightforward, and I’m not fully convinced of the *technical* significance of this work. It would be beneficial to clearly indicate when a proof is trivial versus when it is non-trivial. Additionally, specifying when a result confirms well-known folklore assumptions, and when it is genuinely surprising would enhance clarity. This distinction was not always evident in the paper.


3. Some of the "folklore" concepts that this paper seeks to rigorously prove are somewhat unclear. For instance, the explanation of this idea could be improved:

This result establishes a formal separation
 between local and global query complexity that partly explains ‘interpretability illusions’ (Friedman
 etal.,2024;Yuetal.,2024a) arising in practice due to local but not global faithfulness.

the meaning of "interpretability illusions" is not clearly defined.

4. I'm not entirely convinced by the rigid distinction between "interpretability" as being neuron-level and "explainability" as being input-level. Naturally, the efficiency of providing explanations at the input level is also closely tied to the model's interpretability, not just its neuron-level explanations. Perhaps a more appropriate way to differentiate between the outcomes here and those in previous studies is to describe them as explanations or interpretations at the "input level" versus the "neuron level," both of which contribute to the model’s overall interpretability.

5. The main table is excellent and offers a clear summary of the results. However, a more concise version of this table might be preferable for the main text, with the larger, detailed version included in the appendix.

6. The paper suggests that problems “contained” within NP can be efficiently addressed using SAT solvers. However, this is not always the case—when it comes to neural networks, especially for continuous domains, neural network verification models often serve as more appropriate optimization tools. These are usually not based on SAT solvers, but rather on SMT-based solvers, or branch-and-bound methods.

### Questions
1. Over what type of input domain are the results defined (binary, discrete, or continuous)? 

2. What non-trivial proofs are presented in the paper?

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
4

### Summary
The paper formalizes several problems along the lines of finding the minimal subcircuit in a deep network that matches its computation; this is motivated by finding a small interpretable subcircuit. They show that this and several variants of this problem are intractable (either NP-hard or \Sigma_2^2. For several variants they all show that there is no PTAS.

### Strengths
Interpreting formalization and complexity study of several problems motivated by interpretability of deep networks.

### Weaknesses
The hardness results are not surprising. The area of finding small circuits is in general very hard (see for example: https://www.cs.uwyo.edu/~jhitchco/papers/npcmcsp.pdf even though it is a related but very different problem). The reduction from CLIQUE is simple.

The worst case hardness may not capture the average case complexity for real world distributions. I do understand proving hardness results for probabilistic settings is more difficult. But the impossibility results may not imply hardness of interpretability in practice.

### Questions
The paper is well written and gives nice clean formalization of several problems motivated by interpretability.

In several of the problem formalizations you are trying to find the minimal sub-circuit for a given input x. If the problem is a boolean classification problem then in many circuits there might be some trivial tiny sub-circuits that give the correct output for that given x -- in your reduction you have avoided that by choosing a carefully crafted worst case circuit. Wouldn’t it make more sense to look at a distribution of inputs? I would have expected that one would get a much stronger inapproximability hardness result if you took a set of inputs and insisted that the sub-circuit should output correctly for all inputs which you are doing problem 8.

What is the takeaway here for interpretability in practice? Do you think interpretability is essentially intractable? Please expand on potential practical approaches to interpretability in light of these hardness results with scenarios and reasons as to why interpretability might still be feasible despite the worst-case intractability.

### Soundness
4

### Presentation
3

### Contribution
2
