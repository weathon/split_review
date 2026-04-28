# Efficiently Parameterized Neural Metriplectic Systems

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
Metriplectic systems are learned from data in a way that scales quadratically in both the size of the state and the rank of the metriplectic data.  Besides being provably energy conserving and entropy stable, the proposed approach comes with approximation results demonstrating its ability to accurately learn metriplectic dynamics from data as well as an error estimate indicating its potential for generalization to unseen timescales when approximation error is low.  Examples are provided which illustrate performance in the presence of both full state information as well as when entropic variables are unknown, confirming that the proposed approach exhibits superior accuracy and scalability without compromising on model expressivity.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this work, the authors present a neural network model (NMS) for learning the dynamics of metriplectic systems from trajectory data. It is based on a parameterization of certain scalar- and matrix-valued fields using neural networks that differs from prior works that enforce hard constraints on the degeneracy condition of metriplectic systems and results in a model size that scales quadratically in the system dimenion. The proposed method is demonstrated empirically to perform well in the learning of two low-dimensional metriplectic systems compared to prior methods.

### Strengths
The proposed neural network model for parameterizing the metriplectic system is novel to my knowledge, and it is well-motivated by the theoretical results on metriplectic operators and approximation errors presented in Section 3.2 and 3.4. Compared to several methods from prior literature, the proposed NMS method holds an advantage in terms of model size as well as empirical performances. The writing of the paper is clear overall.

### Weaknesses
 **Physics background and relation to Hamiltonian systems:** Having relatively little prior knowledge about metriplectic systems, I would appreciate an expanded introduction of its physical motivation and some concrete examples for illustrating the general governing equation on the top of Page 2. For example, what do L and M look like in the two examples used for the numerical systems, or in general Hamiltonian systems -- will L be the "J" matrix in Hamiltonian systems (padded with zeros for the extra dimensions) and lose its independence on the state x? It would be beneficial to clarify the physical significance of the entropy variables and how they interact with the observable states within the metriplectic framework. A more detailed explanation of how metriplectic systems generalize Hamiltonian systems, particularly regarding the role of dissipation and entropy, would be valuable for readers unfamiliar with the topic.

**On the decoupled block-wise structure:** The authors mentioned prior works such as Ruiz et al. (2021) and Xu et al. (2022 & 2023) which proposed to parameterize metriplectic systems assuming a decoupled block-wise structure and discussed their inability to express general metriplectic dynamics. But I would appreciate some examples of these more general metriplectic systems encountered in practice. In particular, do the two systems studied in Section 5 admit the decoupled block-wise structure? If so, it would be reasonable to expect that those more restrictive methods are also tested in the experiments as baselines. It would be helpful to understand the specific limitations of the block-wise parameterization in the context of the considered examples, and why the proposed method is necessary to capture the full dynamics.

**Comparison with Hamiltonian learning:** If one ignores the entropy states and focuses only on the observable states (positions and momenta), it looks like the two examples in Section 5 can just be learned as Hamiltonian systems. In that case, does the NMS method reduce to e.g. the Hamiltonian Neural Network (HNN) from [1]? If not, perhaps HNN should also be added as a baseline method to compare against in Table 2. A more thorough discussion on the differences between the proposed NMS method and Hamiltonian learning approaches, especially when applied to systems with both observable and entropy states, would be beneficial. It would be useful to clarify whether the NMS method can recover a Hamiltonian system in the limit of zero dissipation.

**Choices of the initial unobserved states:** Regarding the initial unobserved states in batch-wise training. The authors mentioned two interesting strategies to handle the missing initial unobserved entropy states (first question: which one was used in the experiments whose results are reported in the main text?), one of which is to assume that the entropy values increase linearly in time. Is there a justification behind this? (A further question seems to be: are the entropy states and their dynamics uniquely determined by the observable states?) Besides the two strategies considered by the authors, the initial state optimization proposed in [2] for learning Hamiltonian systems might also be an alternative to consider. It would be helpful to understand the sensitivity of the NMS method to different initializations of the entropy states and how this affects the learning process.

**Test systems are low-dimensional:** Another limitation, as acknowledged by the authors, is that the empirical performance of NMS on larger-scale, realistic metriplectic systems has not yet been demonstrated.

A minor issue: misplaced parentheses for citations on Page 1 (probably due to mixing up \citep with \citet).

### Questions
See questions in the "Weaknesses" section above regarding physics background, training strategy, and alternative methods.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
Metricplectic systems model systems that satisfy energy conservation as well as entropy constraints and can used to model thermodynamic and other system that require such constraints. In the context of machine learning it is of interest to learn such systems from data.
Prior methods like GNODE exchange the problem of enforcing degeneracy constraints with the problem of enforcing symmetry constraints which underdetermines the problem and at the same time have a redundant parameterization of the problem which leads to high (cubic) complexity.
The proposed method exploits structure in the tensor fields to reduce the number of parameters.
The paper demonstrates structure in the degeneracy constraints beyond what can be captured by symmetry constraints leading to a lower parameter parameterization.
A further result shows that the proposed formulation universally approximates metricplectic systems that are non-degenerate and shows a generalization result.

### Strengths
The proposed approach appears to be novel and more general than prior work and allows for all metriplectic data to be approximated simultaneously. Prior work assumes special forms to satisfy the constraints on entropy and energy. This allows the method to model a greater class of systems. The modeling assumptions are also quite mild and only require non-zero gradients for energy and entropy.

The claims and objectives of the paper are clear. The literature review is quite extensive and the experiments treat a number of prior baseline and validate the claims of the paper of better generalization at lower complexity.

### Weaknesses
The paper is difficult to read and there is not a lot of intuition to understand the source of the complexity reduction in Lemma 3.2 and Theorem 3.4 for a non-expert.



### Questions
Besides lower complexity the method achieves better loss values compared with all the other methods. Why is that even on the simple two-gas problem the other methods, say GNODE, do not achieve the same accuracy even with full state information? Is it due to a restrictive parameterization assumption?  Some intuition would be useful.

### Soundness
3

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
The paper presents a new parameterization scheme for learning metriplectic systems. The parameterization is constructed based on computations using properties of the exterior algebra. The constraints can be seen as hard constraints instead of soft constraints. Proof of the construction and proof of universal approximation are provided as well as proof of growth rate of error with respect to time. An algorithm has been proposed, and numerical experiments are carried out to justify the effectiveness of the proposed scheme.

### Strengths
1. The subject being investigated is of significant importance in AI for Science. The topic is closely related to the so-called structure-preserving machine learning. The paper is in general well written.

2. The idea of the proposed parameterization is novel. The construction of the parameterizations that satisfy the hard constraints is obtained through exterior algebra computations. The construction can be seen as obtained by orthogonal projection, which is quite natural. In Theorem 3.4, the statement is "if and only if", which is a nice result for machine learning purposes. There are universality analysis and growth rate of error analysis, which are theoretically convincing.

3. The numerical experiments are carried out quite extensively, together with comparisons with other machine learning schemes in the literature.

### Weaknesses
The main weakness of the paper is that, some of the remarks and claims are not clearly explained. The reviewer will state the details in the "Question" session.

0. How original is the approach to using exterior algebra to parameterize hard-constrained structures? The reviewer believes some papers that deal with structure preservation using exterior algebra exist in the literature. If the authors also know such papers, the authors could have remarked on that.

1. In Remark 3.5, it is claimed that "the proposed parameterizations for L, M are not one-to-one but properly contain the set of valid nondegenerate metriplectic systems". Are the authors trying to say that the proposed parameterizations are not injective but subjective onto the set of possible nondegenerate metriplectic systems? I think so from the proof. The author could clarify what they mean by "properly contain".

2. Again in Remark 3.5, the authors said that the Jacobi identity is not enforced in the algorithm, which causes the parameterization to be not one-to-one. It is not clear to the reviewer how are these related. From the reviewer's viewpoint, the parameterization is not one-to-one because the construction is via orthogonal projection, then of course there will be more than one parameterizations that give the same metriplectic system. However, it is unclear how this is linked to the Jacobi identity not being enforced. The author should clarify this point. Besides, in the last sentence of Remark 3.5, it is said that the structure and energy conservation cannot be simultaneously preserved, which, as far as the reviewer knows, applies in the case of symplectic integrators, but here the context is not symplectic integrators. The authors could clarify this point.

3. In page 6, it is claimed that "the exterior algebraic expressions in Lemma 3.2 require less redundant operations than the corresponding metricized expressions from Theorem 3.4, and therefore the expressions from Lemma 3.2 are used when implementing NMS". The author should clarify how the construction in Lemma 3.2 requires less redundant operations.

4. On top of page 8 (lines 381-382), the first strategy to deal with unobserved states is to assume a line between the all 0 vector to the all 1 vector. Can this be justified?

5. In Algorithm 1, the input, xs = x(ts, μs), but what is μs? It seems that it is not introduced.

6. There is a typo "Lemmata" in line 641.

7. The algorithm in the end still needs structure-preserving integration, which means for each system under consideration, a structure-preserving integrator needs to be applied. In the numerical experiment, how are the integrators chosen?

### Questions
0. How original is the approach to using exterior algebra to parameterize hard-constrained structures? The reviewer believes some papers that deal with structure preservation using exterior algebra exist in the literature. If the authors also know such papers, the authors could have remarked on that.

1. In Remark 3.5, it is claimed that "the proposed parameterizations for L, M are not one-to-one but properly contain the set of valid nondegenerate metriplectic systems". Are the authors trying to say that the proposed parameterizations are not injective but subjective onto the set of possible nondegenerate metriplectic systems? I think so from the proof. The author could clarify what they mean by "properly contain".

2. Again in Remark 3.5, the authors said that the Jacobi identity is not enforced in the algorithm, which causes the parameterization to be not one-to-one. It is not clear to the reviewer how are these related. From the reviewer's viewpoint, the parameterization is not one-to-one because the construction is via orthogonal projection, then of course there will be more than one parameterizations that give the same metriplectic system. However, it is unclear how this is linked to the Jacobi identity not being enforced. The author should clarify this point. Besides, in the last sentence of Remark 3.5, it is said that the structure and energy conservation cannot be simultaneously preserved, which, as far as the reviewer knows, applies in the case of symplectic integrators, but here the context is not symplectic integrators. The authors could clarify this point.

3. In page 6, it is claimed that "the exterior algebraic expressions in Lemma 3.2 require less redundant operations than the corresponding metricized expressions from Theorem 3.4, and therefore the expressions from Lemma 3.2 are used when implementing NMS". The author should clarify how the construction in Lemma 3.2 requires less redundant operations.

4. On top of page 8 (lines 381-382), the first strategy to deal with unobserved states is to assume a line between the all 0 vector to the all 1 vector. Can this be justified?

5. In Algorithm 1, the input, xs = x(ts, μs), but what is μs? It seems that it is not introduced.

6. There is a typo "Lemmata" in line 641.

7. The algorithm in the end still needs structure-preserving integration, which means for each system under consideration, a structure-preserving integrator needs to be applied. In the numerical experiment, how are the integrators chosen?

### Soundness
3

### Presentation
2

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
This paper introduces a novel framework for learning metriplectic dynamics, which describe systems that conserve energy while generating entropy. The key contribution of the proposed approach lies in its design, which ensures both energy conservation and entropy stability. Mathematically, the paper presents a parameterization method that employs neural networks to model four functions, $L$, $E$, $M$, and $S$, such that $L \nabla S = M \nabla E = 0$. Here, $L$ is an antisymmetric matrix-valued function, $M$ is a symmetric matrix-valued function, and $E$ and $S$ are scalar functions.

Under the assumption that $\nabla E,\nabla S\neq 0$, the proposed parameterization of metriplectic systems requires less learnable scalar functions than existing methods. Numerical results show that  the proposed approach exhibits superior accuracy that existing methods for  learning metriplectic dynamics from data.

### Strengths
1.  The emphasis on energy conservation and entropy stability is crucial for modeling realistic physical systems. The authors demonstrate that their approach maintains these properties, which is essential for ensuring that the learned models are physically meaningful and applicable to real-world scenarios

2. The proposed parameterization of metriplectic systems requires less learnable scalar functions than existing methods. 

3. The paper is well-structured and clearly written, making complex concepts accessible to a broader audience. The examples and comparisons with previous methods help to illustrate the advantages of the proposed approach effectively.

### Weaknesses
1. Although the paper presents empirical results demonstrating the model's performance, the range of examples may be limited. Specifically, in both examples, the entropy is given by $S = s_1 + s_2$, resulting in a constant gradient $\nabla S = 0 $. This contradicts the core assumption in the paper that $ \nabla S \neq 0 $. 

2. The requirement that the metriplectic system being approximated is nondegenerate—i.e., the gradients of energy and entropy must not vanish ($\nabla E, \nabla S \neq 0$)—may limit the applicability of the method. Although this is claimed to be a mild condition, both of the examples considered in the paper contradict this core assumption. In addition to the entropy $S$ having a zero gradient ($\nabla S = 0$), the energy in the investigated examples is also degenerate. From the reviewers' understanding, steady-state is a fundamental concept in physical systems, characterized by the energy reaching an extremum, meaning the energy gradient is zero ($\nabla E = 0$). The reviewers are not aware of any physical systems with non-zero energy gradients. To better demonstrate the applicability of the proposed method, the reviewers recommend that the paper provide a detailed discussion of systems that satisfy the key non-degeneracy assumption. Additionally, it would be beneficial to include examples that adhere to this assumption to validate the effectiveness of the algorithm.



### Questions
1. While it is evident that the proposed parameterization requires fewer learnable scalar functions, this alone does not directly imply superior performance. Could the paper provide an explanation of why the proposed approach achieves higher accuracy?

2. The paper claims that the core advantage of the proposed method is its efficiency. Could the paper provide evidence demonstrating that the method requires less computational time or other resources, such as memory?

3. Could the paper provide that specific formula of metric use to compare the performance?

4. As the true governing functions (the right hand side of the ODE) are known, could the paper show the results of learning these governing functions?

### Soundness
4

### Presentation
4

### Contribution
3
