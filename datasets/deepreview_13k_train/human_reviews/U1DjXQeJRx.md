# Poisson-Dirac Neural Networks for Modeling Coupled Dynamical Systems across Domains

- Decision: Accept
- Scores: 5, 8, 6, 8, 6

## Abstract
Deep learning has achieved great success in modeling dynamical systems, providing data-driven simulators to predict complex phenomena, even without known governing equations.
  However, existing models have two major limitations: their narrow focus on mechanical systems and their tendency to treat systems as monolithic.
  These limitations reduce their applicability to dynamical systems in other domains, such as electrical and hydraulic systems, and to coupled systems.
  To address these limitations, we propose Poisson-Dirac Neural Networks (PoDiNNs), a novel framework based on the Dirac structure that unifies the port-Hamiltonian and Poisson formulations from geometric mechanics.
  This framework enables a unified representation of various dynamical systems across multiple domains as well as their interactions and degeneracies arising from couplings.
  Our experiments demonstrate that PoDiNNs offer improved accuracy and interpretability in modeling unknown coupled dynamical systems from data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present a new architecture, specifically they integrate some clever ideas of Dirac structure in order to unify the port-Hamiltonian and Poisson formulations from geometric mechanics.  Both nice innovations for physics-constrained neural networks.

### Strengths
The integration of physics-based principles is always welcome in the dynamical systems world.  The authors have a very nice contribution to make here potentially as the integration of physics principles into neural networks is very important.

### Weaknesses
The models used seem to be all linear: which begs the question about simple linear model regressions such as dynamic mode decomposition, dynamic mode decomposition with control and time-delay embedded DMD which models missing/coupled physics.  These more baseline (non-NN) methods are simply not talked about or considered and I think they should be.

There are statements that are simply not true:  "two key limitations remain in modeling dynamical systems, especially those described by ordinary differential equations (ODEs). The first limitation is the narrow focus on mechanical systems."  This suggests the authors don't know the field well and it is a concern.  People are modeling all kinds of dynamical systems with ML/AI architectures well beyond mechanical systems.

Further: "The second limitation is that most methods treat the system as a single, monolithic entity."  This is also not true.  Many people are working on coupled systems where time-delay embeddings are often used to gather information for missing, coupled and unmeasured variables.  Again, it is odd that these statements exist in the paper which suggests the authors are not aware of the great body of work on model discovery and dynamical systems methods with ML/AI for systems which are not mechanical and which indeed have coupling.

### Questions
The models considered all seem to be linear.  Is that correct?  If so, more standard system ID or linear methods should be considered instead of all this sophisticated ML/AI architectures.  

Can this generalize to nonlinear models?  Or simply be applied to nonlinear models with success?  Although you did Fitzhugh-Nagumo and  Chua's model, these are only "slightly" nonlinear and system ID models can work pretty well with those.

What have you not considered non-neural network methods like DMD... or system ID methods like mamba/S4 not been compared?

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
4

### Summary
This work targets the dynamical system identification using observation data, which is a hot topic and essential application. The key differences with respect to existing works are clearly stated: 1) identifying unknown physics rather than predefined symbolics, 2) considering the coupling behaviors in the system or interactions when the problem covers multiple domains rather than single mechanical systems.

### Strengths
•	As the reviewer summarizes above, key limitations are correctly identified such that the contributions of this work are clear. To the best of the reviewer’s knowledge, this work is new.

•	The theoretical analysis is solid, where the definitions and theorems clearly show how the Dirac structure encapsulates internal and external component couplings. Moreover, the corresponding examples of different dynamical systems are well-explained to differentiate the proposed method from existing methods like HNN and NODE.

•	The results on multiple systems look promising, where various experiment scenarios and evaluation metrics are comprehensive to validate PoDiNNs’ capabilities.

### Weaknesses
Some technical details, as well as the claimed capabilities, are unclear, which might be because the reviewer is unfamiliar with all kinds of multi-domain dynamical systems. The confusions are listed below.

•	The capability to deal with multi-physics problems is claimed several times in the paper. Specifically, Remark 1 explains the representation of inter-coupling using a bivector element (which is also an NN, right?) Remark 4 with Table 2 briefly demonstrates the scenarios to capture coupled physics in multiple domains. The reviewer would like to know how PoDiNNs represent such interactions.  Is it the same way as the traditional simulation tool, e.g., through iterative refinement of two (or more) simulations of a single domain or system? 

•	The proposed work targets unknown physics/dynamics, which is quite challenging as there are no predefined physical symbolics in PINN-alike works. How to ensure the PoDiNNs capture the correct physics without causing overfitting problem or continuous good performance in extrapolation?

•	Moreover, PoDiNNs focus on behaviors that may not be captured by generic models, e.g., NODE, which seem to need intensive resources. Especially, the couplings in multi-physics usually require heavy computation in traditional simulations. The more fine-grained, the heavier. What is PoDiNNs’ capability in this aspect?

•	For the last paragraph of Sec. 3.4, an example of electric circuit is used. Could the reviewer further explain with more details: why ODEs or using NODE alone cannot capture the current flow and balanced voltage level? Subsequently, how does PoDiNN mitigate the issue of limited representation? A toy example with mathematical derivations or diagram will be helpful.

### Questions
Please refer to the bullet points in Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This work studies the application of deep neural networks for data-driven physics simulation. Over the recent years, several neural network simulation models have been proposed among which Hamiltonian Neural Networks (HNNs) and Lagrangian Neural Networks. Although these models are formulated along physics principles and consequently enjoy improved stability of their simulations, two key limitations remain: (1) they focus on mechanical systems, as opposed to for example electric circuits or magnetic fields, and (2) they consider the system as a single monolithic entity. To alleviate these limitations, this work proposes Poisson-Dirac Neural Networks (PoDiNNs), which unifies the port-Hamiltonian and Poisson representations, and explicitly represents the coupling between internal and external components. The empirical evaluation shows that PoDiNNs enjoy stability over longer simulation horizons and in general achieve lower errors than Neural ODE or variants of HNNs.

Unfortunately, I am missing too much of the mathematics and physics background that is required to understand the paper, so I am unable to provide an informative review.

### Strengths
**S1:** The empirical results show that PoDiNNs achieve lower errors and provide stable predictions for longer than Neural ODEs and HNN variants. As such, the method seems effective for the tasks for which it was designed.

### Weaknesses
 **W1:** The content might be difficult to digest for the audience of ICLR, since a specific mathematical and physics background is required to understand the work. In my impression, most ML researchers will lack this background, and also a substantial part of the AI4Science community might find it difficult to understand the paper. Specifically, the paper relies heavily on concepts from differential geometry and port-Hamiltonian systems, which are not commonly part of the standard machine learning curriculum. The abstract discussions of bivectors and Poisson structures, while important for the theoretical framework, may obscure the practical implementation details for many readers. The paper does not provide sufficient context or intuitive explanations for these concepts, making it challenging to grasp the core ideas without prior expertise. Furthermore, the connection between the abstract mathematical formulation and the actual neural network architecture is not immediately clear, which further hinders understanding for those without the necessary background.

### Questions
-

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper introduces a new method for stable deep-learning based modelling of dynamical systems. Neural ODEs were originally found to have significant limitations in modelling dynamics long-term due to a lack of physical guarantees (e.g. conservation laws) leading to error accumulation. To address this, Hamiltonian NNs incorporate Hamiltonian mechanics (modelling the hamiltonian through a NN). This paper contributes a generalization of Hamiltonian NNs; Poinsson-Dirac Neural Networks (PoDiNNs) to combine both port-hamiltonian and poisson systems for mechanics, enabling learning of coupled dynamical systems across multiple domains, their interactions and degeneracies. This  constitutes a unification of previous works that address/leverage specific properties of dynamical systems like energy dissipation and external inputs. Authors show that this approach moreover allows for the identification of the specific coupling patterns between interacting dynamical systems. The experimental results show clear and consistent improvements over previous approaches in a range of systems with degenerate dynamics (e.g. constraints), dissipation and external inputs.

### Strengths
- The paper is well-written and concise. The modelling choices made by the authors are well-motivated; the incorporation of Dirac structure into a DL-based solving method for mechanics has a lot of possible benefits regarding guarantees and interpretability of the learned functions.
- The experimental results are very convincing; in the chosen experimental setups the proposed framework outperforms all baseline methods consistently.
- The experiments on identifying coupling patterns are fascinating, these results show that the proposed framework is indeed able to recover the underlying coupling in a very interpretable manner.

### Weaknesses
 - The paper is quite dense, making some of the reasoning and motivation hard to follow. Although in places authors elaborate on their arguments with examples, I think it would be good to provide some more visual guidance. For example, figure 1 contains a very high-level overview of the concept of PoDiNNs, but I think it would be good to expand this diagram and clearly indicate what parts of this system the method proposes to replace with learned functions (NNs) and relate it to e.g. eq 5, def 3. I think this would greatly help with readability.
- The experiments chosen by the authors are examples of systems that fit the modelling criteria set by the authors for their framework. In these settings, the proposed framework outperforms previous approaches. However, I think it would also be good to consider/experiment with settings that do not exhibit e.g. degeneracy just to gauge how well this generalized method works in the settings that the originally proposed HNN and LNN are validated on. Would it for example be possible to show performance of your model vs baselines on eg double pendulum (as in HNN or LNN paper)?
- For completeness I think it is important to compare your method against the baselines also in terms of computational complexity / overhead. Currently, no details on the computational complexity or time complexity on either training or inference of the proposed method are given. Please provide these details.
- An arguable weakness of the method is the reliance on specifying problem-specific constraints, i.e. the number of components is a model hyperparameter, but as shown in the last experiment / Appx E it is important to specify this to at least the number of underlying components in the system, or performance will be significantly impacted. Overspecifying is possible of course, and does not seem to have negative impact, but induces additional computational complexity.

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a novel neural network architecture, the Poisson-Dirac Neural Network (PDNN), which combines Hamiltonian and Poisson formulations. The PDNN leverages the Dirac structure to model coupled dynamical systems across various domains.

### Strengths
1) The paper provides a solid theoretical foundation for the proposed PDNN architecture.

2) The authors conduct extensive experiments to demonstrate the effectiveness of the PDNN in various applications.

### Weaknesses
1) While the paper's theoretical contributions are significant, additional background material, such as differential geometry, etc, in the supplementary information would enhance its accessibility to a broader audience. Specifically, the paper assumes a strong familiarity with concepts such as symplectic manifolds, Poisson brackets, and Dirac structures, which are not universally known within the machine learning community. A more detailed explanation of how these concepts are applied in the context of the proposed PDNN architecture would be beneficial. For instance, a concrete example illustrating the construction of a Dirac structure for a simple mechanical system would greatly improve understanding. Furthermore, the connection between the abstract mathematical framework and the practical implementation of the neural network could be made more explicit.

2) The paper lacks a direct comparison with state-space models (SSMs) or neural operators, which are also used for learning dynamical systems. While the authors mention that neural operators are primarily designed for PDEs, the argument that SSMs reduce to NODEs is not entirely convincing, as SSMs can also model systems with observable states. The absence of a comparative analysis makes it difficult to assess the relative strengths and weaknesses of the proposed PDNN architecture in the broader context of existing methods for learning dynamical systems. A quantitative comparison on a common benchmark dataset would be valuable.

### Questions
1) While the PDNN shows promising results, it would be interesting to compare its performance with state-space model (SSM) based neural operators on the datasets used in this paper.

2) To make the paper more accessible to a broader audience, the authors could consider adding an appendix to provide additional explanations and visualizations of the key concepts and techniques.

### Soundness
3

### Presentation
2

### Contribution
3
