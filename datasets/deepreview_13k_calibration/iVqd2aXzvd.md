# Automata Learning for Neural Event ODEs: An Interpretable Model of Piecewise Dynamics

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 5, 3

## Abstract
Discrete events within a continuous system cause discontinuities in its derivatives.
Given event specifications and state update functions,
ODE solvers can integrate until an event, apply the update function, and restart the integration process to obtain a piecewise solution for the system.
However, in many real-world scenarios,
the event specifications are not readily available or vary across different black-box implementations.
We present a method to learn the dynamics of a black-box ODE implementation that uses abstract automata learning and Neural Event ODEs.
Without prior knowledge of the system, the method extracts the event specifications and state update functions, and generates a high-coverage training dataset
through abstract automata learning.
Additionally, our approach introduces a significantly more efficient training process for Neural Event ODEs that slices training trajectories into temporally consecutive pairs within continuous dynamics.
Both contributions ensure well-posed initial values for each ODE slice.
A~proof-of-concept implementation captures event specifications in an interpretable automaton and uses the trajectories from automata learning to efficiently train a simple feed-forward neural network by solving well-posed, single-step IVPs.
During inference, the implementation detects the events and solves the IVP piecewise.
Preliminary empirical results show significant improvements in training time and computational resource requirements while retaining all advantages of a piecewise solution.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a method for learning the behavior of continuous systems with discrete events using abstract automata learning and Neural Event ODEs. It enables the extraction of event specifications and state update functions from black-box ODE implementations, significantly improving training efficiency. This approach aims to reduce training time and computational resources while maintaining the advantages of piecewise solutions for systems with discontinuities.

### Strengths
- The paper presents an innovative approach to learning the behavior of continuous systems with discrete events, addressing a challenging problem in the field of modeling and simulation.
- By using abstract automata learning, the method not only captures event specifications but also makes the resulting models interpretable. This is important for understanding complex systems, even when their behavior is initially unknown or represented as black-box ODEs.
- The paper introduces a more efficient training process for Neural Event ODEs by removing discontinuous training pairs. This improvement can lead to reduced training time and computational resource requirements, making it practical for real-world applications.
- The use of the bouncing ball example illustrates the method's effectiveness in simplifying complex systems into interpretable models, making the paper more accessible to a broad audience.

### Weaknesses
 - The paper mentions preliminary empirical results, but it may lack a comprehensive evaluation of the method's performance on a diverse set of real-world problems. While the paper highlights the relevance of the proposed method for real-world scenarios, it could benefit from concrete examples or case studies demonstrating its application in practical settings.
- The paper might not thoroughly discuss the assumptions and limitations of the proposed method, which is important for understanding its scope and potential constraints.

### Questions
More discussions on the bottleneck of the proposed method would further strengthen the paper.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose an extension of the famous L* algorithm for learning deterministic finite automata. The authors adapt this learning algorithm to learn automata for neural event ODEs, which is novel and interesting. A toy example of a bouncing ball is used as a running example to illustrate the approach.

### Strengths
The use of L* (or grammatical inference more broadly) to learn automata in the context of neural ODEs is an interest domain.

### Weaknesses
The paper misses a description of the actual learning algorithm. It seems to be a variant of L*, but too many details are left to the reader to decipher. The use of L* in the context has also been explored, in particular as part of the reinforcement learning literature, and should be cited. For example, see the references below. As it stands the paper is not sufficiently self-contained or understandable to be recommended for publication. The paper would also greatly benefit from additional experiments.

The core issue is the lack of clarity regarding how the L* algorithm is adapted for learning automata from neural event ODEs. While the formalism provides a foundation, the paper does not sufficiently detail the specific modifications or abstractions required to apply L* in this context. The membership query mechanism, which is crucial for L*, is not clearly explained, particularly how it interacts with the neural ODE and how the outputs are interpreted to determine membership. The paper also lacks a clear explanation of how the observation table is constructed and updated during the learning process, given the continuous nature of the ODE outputs. The connection between the continuous dynamics of the neural ODE and the discrete transitions of the learned automaton remains vague.

Furthermore, the paper does not adequately address the challenges of applying L* to continuous systems. For example, the standard L* algorithm assumes a discrete alphabet, but the inputs and outputs of a neural ODE are continuous. The paper needs to clarify how these continuous values are discretized or abstracted to fit the L* framework. The paper also does not discuss the potential issues of noise or approximation errors in the neural ODE outputs and how these might affect the convergence and correctness of the learned automaton. The lack of experimental validation beyond a toy example further weakens the claims of the paper.

### Questions
How is L* being adapted for your setting? I assume it is not a straightforward application of L*. A lot of the formalism provides a foundation for L*, but it is difficult to see how L* has a novel adaptation in this domain.

Minor comments:
* "between the them" -> "between them"
* At the bottom of page 2, you need a space between "define" and "\mathcal{L}(M)}".

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an automata learning-based approach to learn piece-wise ODE functions. It defines a set of predicates and builds an abstract model of the system by descritizing the time steps. It detects the discontinuity in the dynamics based on a predicate change detector, slices the trajectories, build the abstract model. Then it learns an abstrct event model and construct an event specification. To learn the piecewise Neural ODE, the paper uses the learned event specification to train a nonlinear transformation to map the last state in prefix to the initial state in the suffix at the discontiuity time.

### Strengths
* `Originality`: This paper is original in that it learns piecewise Neural ODE by utilizing a learned event specification.

* `Quality`: There is no technical issue.

### Weaknesses
 * `Weakness 1`: The proposed approach seems to hinge on whether the human designer has a decent knowledge of the dynamics of the plant so that the designer can provide the predicate for the automata learner to capture the event change. 

* `Weakness 2`: The author did not illustrate the specification construction approach in organized manner. All the procedures are described in the pattern of "what I did' rather than explaining the motivation first. There is no soundness and completeness analysis for the automata learning approach in the paper. Let alone the query complexity and efficiency. If the proposed approach can be reduced from the L* algorithm, author should at least illustrate and prove it.

* `Weakness 3`: There is no numerical experiments for the proposed approach. There is no qualitative nor quantitative evaluation for the proposed approach.

### Questions
Please address my concerns in the `Weakness` field.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, authors have presented a hybrid approach for inferring an interpretable specification of a system showing piecewise dynamics. Authors used automata learning to infer an abstract model of a possibly black-box system’s behavior and a neural network to learn its continuous dynamics. Automata learning is polynomial in the size of inputs and the number of congruency classes in the target language. Next, authors demonstrated a more effective training scheme for neural networks learning continuous dynamics in the presence of discontinuities. Through a step-by-step analysis using the bouncing ball, authors demonstrated that the proposed approach can efficiently learn interpretable models of piecewise dynamics with significantly fewer data points and computational resources compared to current state-of-the-art Methods.

### Strengths
Compared with previous methods, the authors propose a new method for solving the EDP which does not require prior knowledge about the events and solves the EDP on a subset of training data only if it is required. It also learns an automaton to interpret the system's dynamics. The proposed method is mostly original and potentially is an improvement over previous methods. 

The paper is written and organized well. Sufficient previous papers are cited and compared.

### Weaknesses
1) This paper is still in its preliminary form. It is shorter, compared with other submissions to a major conference. Authors only demonstrate the evaluations on the dataset of bouncing ball, which is a toy example in neural event ODE. The lack of experiments on more complex datasets limits the conclusions that can be drawn about the method's general applicability. The bouncing ball example, while useful for initial validation, does not sufficiently demonstrate the method's ability to handle the complexities of real-world piecewise dynamical systems. For example, the method's performance on systems with higher dimensionality or more intricate switching conditions remains unclear.

2) A lot of previous methods are mentioned and cited, but they are not compared numerically compared with the proposed method, such as LatentODE and LatSegODE. Also, ablation studies are missing, and performance comparisons should be conducted for the proposed methods with different choices of important parameters. The absence of numerical comparisons with established methods makes it difficult to assess the true novelty and effectiveness of the proposed approach. Furthermore, the lack of ablation studies prevents a thorough understanding of the impact of individual components and parameter choices on the overall performance. For instance, the sensitivity of the method to different automaton learning parameters or neural network architectures is not explored.

3) Authors claim that the proposed method has reduced computational cost. But convincing experimental evidence needs to be shown. Neural event ODE methods always have significant computational cost, including the proposed method, so its comparison with previous methods is needed. The claim of reduced computational cost is not substantiated by empirical evidence. A detailed analysis of the computational resources required by the proposed method, compared to existing approaches, is necessary to validate this claim. This analysis should include metrics such as training time, memory usage, and inference speed, across different dataset sizes and complexities.

### Questions
1) Authors propose to use L* for automaton learning. Why to choose this method? Is there any better choice? The motivation should be presented more.

2) Since the automaton learning algorithms always need a lot of data to cover all the possible prefixes, can authors provide some complexity analysis on the minimum amount of necessary training data? 

3) Can the proposed method handle the situation of noisy data? Can the automaton still be learned from noisy data? 

4) please provide more experimental evaluation to verify the framework.

5) please include comparison with alternative methods to verify the improvements over state of art.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
