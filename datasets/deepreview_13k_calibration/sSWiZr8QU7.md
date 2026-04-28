# A Hybrid Simulation of DNN-based Gray Box Models

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 1, 5, 5, 3

## Abstract
Simulation is vital for scientific and engineering disciplines, as it enables the prediction and design of physical systems. However, the computational challenges inherent to large-scale simulations often arise from complex device models featuring high degrees of nonlinearities or hidden physical behaviors not captured by first principles. Gray-box models that combine deep neural networks (DNNs) with physics-based models have been proposed to address the computational challenges in modeling complex physical systems. A well-crafted gray box model capitalizes on the interpretability and accuracy of a physical model while incorporating deep neural networks to capture hidden physical behaviors and mitigate computational load associated with highly nonlinear components. Previously, gray box models have been constructed by defining an explicit combination of physics-based and black-box models to represent the behavior of sub-systems; however this alone cannot represent the coupled interactions that define the behavior of the entire physical system. We, therefore, explore an \emph{implicit} gray box model, where both DNNs (trained on measurement and simulated data) and physical equations share a common set of state-variables. While this approach captures coupled interactions at the boundary of data-driven and physics-based models, simulating the implicit gray box model remains an open-ended problem. In this work, we introduce a new hybrid simulation that directly integrates DNNs into the numerical solvers of simulation engines to fully simulate implicit gray box models of large physical systems. This is accomplished by backpropagating through the DNN to calculate specific Jacobian values during each iteration of the numerical method. The hybrid simulation of implicit gray-box models improves the accuracy and runtime compared to full physics-based simulation and enables reusable DNN models with lower data requirements for training. For demonstration, we explore the advantages of this approach as compared to physics-based, black box, and other gray box methods for simulating the steady-state and electromagnetic transient behavior of power systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this work, author try to augment simulator with DNN to learn hidden non-linear dynamics not captured by first principle solver. 
prior work explicitly define a system of simulator + DNN learned residual. 
this work propose an implicit combination of simulator and dnn modules, integrate a dnn into the numerical solver.

### Strengths
- introduce hybrid simulation engine that integrate DNN into numerical methods to enable reusable and data-efficient learned modules. 
- hybrid method with more accuracy grounding 
- speed up simulation by model complex part with DNN

### Weaknesses
demonstrate on relative simple physics-based model, not sure how this work for more complex system with non-linear/complex physics-based simulator.

### Questions
- could this framework be integrated into other simulation engines, are there any constraints on this?
- since here one need to backpropagation through the DNN within the numerical solver, would it be a bottleneck for large system?
- how does it work for complex simulation on meshes?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper proposes a hybrid simulation approach that integrates neural networks with physics-based models to enhance accuracy and efficiency. It introduces an implicit gray-box model, where deep neural networks (DNNs) and physical equations share state variables. This implicit integration captures complex coupled interactions and reduces training data requirements. The effectiveness of this approach is demonstrated through simulations of steady-state and transient behaviors in power systems.

### Strengths
This paper presents an implicit hybrid model method for physics-based models and NN-based models. The NN-based models can help extract sensitivity terms and help with the convergence.

### Weaknesses
1. Although the motivation of this paper is good, it is hard to know whether the proposed method is effective in more general and challenging problems. Only the power system example is not sufficient. More challenging and 3D transient examples are needed. Strong and clear examples with enough evidence are required.
2. This paper claims to focus on large-scale systems, but there are no descriptions of the degrees of freedom of the demonstration example. 
3. The literature review is not comprehensive. Only PINN (line 123) is mentioned in the paper. A comprehensive literature is needed, such as Fourier neural operator, DeepONet, JAX-CFD, and other physics-informed machine learning methods.
4. Typo: Lin369, there is no Figure 11.

### Questions
1. Since the NN-based model is used for computing Newton-Raphson and integrated with the physics-based model for internal optimization, the accuracy can be better (Figure 3 and Table 1). How about the performance of the traditional physics-based model in Figure 3 and Table 1? 
2. How to deal with noisy data with the proposed method? How to effectively separate noise and real hidden physics? This will strongly influence the optimization of NN.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work suggests a hybrid simulation method called implicit gray box model which combines physics and deep neural networks. The gray-box model shows enhanced accuracy and reduced runtime in power grid simulations.

### Strengths
* The gray box model successfully calculate both current values and sensitivities.
* This approach provides simulation  results with more realistic and feasible results that satisfy physical constraints.

### Weaknesses
 * The experimental example is limited to a single 14-bus network. It would be beneficial to include more standard benchmarks used in previous literature. Specifically, the IEEE 30-bus, 57-bus, and 118-bus systems are commonly used for validation in power system simulation, and their inclusion would strengthen the paper's claims.
* The benchmark results are also limited, comparing only the PQ model, hybrid simulation, and ground truth. A more comprehensive comparison should include other state-of-the-art simulation techniques, such as those based on time-domain simulation or other hybrid methods, to properly contextualize the performance of the proposed approach.
* This work does not provide an in-depth analysis of how the model scales with increasing network size or complexity. The computational cost and memory requirements as a function of the number of buses and the complexity of the network components (e.g., number of generators, loads, and transmission lines) should be investigated and reported.

### Questions
* The figures should be presented more neatly. For example, a general caption for Figure 1 would be helpful. In Figure 2, the legend colors do not match the actual colors in the graphs.
* The standard table format should be followed. e.g. no vertical lines

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors propose a grey-box model for physical simulation that combines DNN and physics-based modeling. They propose to use a parallel grey box architecture where the physical and the DNN equations share the same/similar state variables, requiring their simultaneous solution. The authors claim that this combination leads to improved accuracy of physical simulation compared to the state-of-the-art.

### Strengths
The idea of using the new equation (equation 3) for grey box simulation is interesting and novel. The paper is well written and does not suffer from grammatical issues.

### Weaknesses
1. The motivation behind equation 3 is not clear. Why are the physical and the neural network equations being summed up? The physical equation calculates its own value as it is supposed to be the complete picture of the device/system, and the neural network equation also calculates its own value and is supposed to be a complete picture of the device/system. Previous work by Menesklou et al., "Grey box modeling of decanter centrifuges by coupling a numerical process model with a neural network," as a reference in this paper, utilized a summation because the neural network part provides a correction to the physics-based model. The authors need to explain clearly why the two values are being summed up if no error correction is being made.  The current explanation lacks a clear justification for the additive coupling of the physical and neural network components. It's not immediately obvious why these two distinct models, each potentially capable of representing the system, should be combined in this manner without a clear error correction or a specific physical interpretation of their interaction. The summation implies a direct superposition of effects, which needs a more rigorous explanation, especially when both models are intended to capture the same underlying system dynamics. This approach could lead to an over-parameterization of the model, making it difficult to interpret the contribution of each component. Furthermore, the lack of a clear physical basis for the summation raises concerns about the generalizability of this approach to other systems. 

2. The example used in "5.1 VALIDATING JACOBIAN ELEMENTS OF THE IMPLICIT DNN-BASED GRAY BOX MODELS" looks like a simple sinusoidal. A neural network learning the sinusoidal function does not seem very impressive. A more complicated system should be chosen to convince me. The use of a simple sinusoidal function as a validation case is insufficient to demonstrate the capabilities of the proposed method. A sinusoidal function is easily approximated by various methods, including simple curve fitting techniques, and does not showcase the ability of the neural network to capture complex, non-linear dynamics. The choice of this example raises questions about the method's applicability to real-world systems that exhibit more intricate behavior. A more complex, multi-dimensional system with non-linear interactions would be more appropriate to evaluate the effectiveness of the proposed approach. The current example does not provide sufficient evidence to support the claim that the method is capable of handling the complexities of real-world physical systems.

3. The advantages of the methods are not convincing. The experimental results show that the method works but does not compare it to other methods. The lack of comparison against other state-of-the-art methods makes it difficult to assess the true value of the proposed approach. While the experimental results demonstrate that the method is functional, they do not provide any evidence that it outperforms existing techniques. A thorough comparison against established methods, including both physics-based and purely data-driven approaches, is necessary to validate the claimed advantages. Without such a comparison, it is impossible to determine whether the proposed method offers any significant improvements in terms of accuracy, computational efficiency, or generalizability.

### Questions
None

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a hybrid simulation framework to simulate implicit gray-box models for power systems by embedding DNNs into numerical solutions for Jacobian matrix calculations.

### Strengths
The paper addresses a relevant problem by aiming to balance computational efficiency with accurate modeling of complex physical systems.

### Weaknesses
1. Lack of Novelty. The proposed method lacks significant novelty, as leveraging deep learning models to accelerate or enhance simulations has been widely explored. Specifically, the use of DNNs for Jacobian matrix computation via PyTorch’s autograd is functional but does not represent a novel or impactful contribution relative to established techniques in the field. The core idea of using automatic differentiation to compute Jacobians for hybrid models is not new, and the paper does not sufficiently demonstrate how their specific implementation offers a substantial advancement over existing approaches. The paper needs to clearly articulate what makes their approach unique beyond a straightforward application of existing tools.
2. Limited Comparison over Well-Established Techniques. The experimental analysis is limited primarily to power system simulations, with insufficient benchmarking against state-of-the-art hybrid or physics-informed neural network methods across other domains. The paper does not adequately compare the performance of the proposed method against established techniques such as traditional numerical solvers with adaptive time-stepping or other hybrid modeling approaches that combine data-driven and physics-based models. The lack of a comprehensive comparison makes it difficult to assess the true value and potential of the proposed method.
3. Formatting and Clarity Issues. The paper has formatting and clarity issues that impact readability, with Figure 1 being a notable example. The figure lacks clarity and is poorly formatted. The overall presentation of the method and results needs to be improved to ensure that the core ideas and contributions are easily understood by the reader. The paper should also include a more detailed description of the implementation details, including the specific architectures of the DNNs used and the training procedures.

### Questions
Please see Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1
