# MamKO: Mamba-based Koopman operator for modeling and predictive control

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
The Koopman theory, which enables the transformation of nonlinear systems into linear representations, is a powerful and efficient tool to model and control nonlinear systems. However, the ability of the Koopman operator to model complex systems, particularly time-varying systems, is limited by the fixed linear state-space representation. To address the limitation, the large language model, Mamba, is considered a promising strategy for enhancing modeling capabilities while preserving the linear state-space structure.
In this paper, we propose a new framework, the Mamba-based Koopman operator (MamKO), which provides enhanced model prediction capability and adaptability, as compared to Koopman models with constant Koopman operators. Inspired by the Mamba structure, MamKO generates Koopman operators from online data; this enables the model to effectively capture the dynamic behaviors of the nonlinear system over time. A model predictive control system is then developed based on the proposed MamKO model. The modeling and control performance of the proposed method is evaluated through experiments on benchmark time-invariant and time-varying systems. The experimental results demonstrate the superiority of the proposed approach. Additionally, we perform ablation experiments to test the effectiveness of individual components of MamKO. This approach unlocks new possibilities for integrating large language models with control frameworks, and it achieves a good balance between advanced modeling capabilities and real-time control implementation efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors propose MamKo, combining Koopman operator theory (projecting nonlinear systems into a high-dimensional linear space) with Mamba (a LLM based on state-space models) for accurate and efficient modeling of time-varying systems. Furthermore, based on the derived model, a model-based control approach is proposed. Simulations with different, time-varying systems demonstrate that MamKo can be superior to other SOTA methods. 

The main contribution is combining these two methods (with some minor modifications), creating a powerful framework for time-varying systems.

### Strengths
- The paper is well written, the ideas are clearly formulated, and the results are well presented.
- To the best of my knowledge, it is the first time that these two methods have been combined and applied to model time-varying systems. Thus, it's a novel and original approach.
- The simulation results are quite convincing that the proposed method can significantly improve the modeling and control of time-varying systems.

### Weaknesses
 - The simulation is limited to learning method but ignores "classic" system identification. There is a rich literature on identifying time-varying parameters in dynamical systems. In particular, for the cart pendulum example, a comparison to classic system identification would strengthen the paper.
- Maybe I missed the part but how is the optimal dimension of the linear space, i.e. the dimension of A_k in (5) determined?
- In the introduction, the computational time of other koopman based approaches is discussed. However, there is no proper discussion/evaluation/theory on the training/inference time with the proposed framework.

### Questions
See weaknesses

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
5

### Summary
the paper MamKO leverages Mamba architecture to generate koopman operators  with projected benefits towards model predication capability and adaptability relative to koopman models with constant koopman operators.  MamKO generates the Koopman Operator from realtime data making the model learn nonlinear behavior over time. To demonstrate capability the MamKO model is applied to model predictive control (MPC).  The modeling and control performance of the proposed method is evaluated through experiments on benchmark time-invariant and time-varying systems.
Four claims are made as advancing the state of the art
1. Matrix generation using Mamba structure
2. approach can handle unstable and time varying systems
3. Computationally efficient MPC is developed based on the MamKO approach
4. Experiments are provided in support. 
Overall, the paper is well written and the developments are clear and error free.  While the authors have not demonstrated the results against any real world practical system, they do provide adequate development for a practitioner to adopt into real world problems and study applicability.  In that regard I think this work is worth publishing so the SOTA in Kooman based approaches   can continue to be explored for real world use.

### Strengths
the paper has several strengths
1. Leveraging Mamba for generating time-varying Koopman operators to address the limitations of fixed linear state-space models is innovative.
2. The authors  effectively incorporate MamKO into an MPC framework and demonstrate practical applications.  ability to formulate the control problem as a convex optimization task adds to the framework's appeal for real-time applications.
3. The experimental validation (although all simulations)  is based on multiple benchmark systems (e.g., CartPole, Gene Regulatory Networks, and CSTRs). Results demonstrate the advantages of MamKO over traditional methods like Deep Koopman Operator (DKO) and MLP-based models. 
4. Real-Time Adaptability: By generating matrices in real-time, MamKO addresses the challenge of modeling time-varying systems efficiently. The proposed method's performance on rapidly changing systems highlights its practical utility.
5. Supplemental material allows reproducibility

### Weaknesses
The framework assumes that the Mamba-generated matrices adequately capture the dynamics of the underlying system. This assumption may not hold for highly nonlinear systems where matrix representations could become unstable or inaccurate. Specifically, the method's reliance on a linear time-varying state-space representation, even with Mamba-generated matrices, may struggle with systems exhibiting strong nonlinearities, such as chaotic behavior or bifurcations, where a linear approximation may be insufficient even locally. The paper does not provide a clear analysis of the limitations of this linear approximation in the context of highly nonlinear systems. 

Experimental results do support the claims of improved performance. However, the paper could enhance its rigor by including statistical analyses (e.g., confidence intervals or hypothesis tests) to demonstrate the significance of the results. The current presentation of results, without statistical measures of variance, makes it difficult to assess the robustness of the method and to determine if the observed improvements are statistically significant or simply due to random variations in the simulation runs. For example, it is not clear if the performance gains are consistent across different initial conditions or parameter settings.

Authors do acknowledge that their method may not generalize to all real-world systems, but a more explicit discussion on the boundaries of applicability (e.g., systems with extremely high-frequency dynamics) would add value. The paper lacks a detailed discussion on how the method would perform in systems with very fast dynamics, where the sampling rate might not be sufficient to capture the system's behavior accurately, or where the Mamba architecture might not be able to generate appropriate matrices quickly enough. The authors should also discuss the limitations of the method in systems with significant measurement noise or disturbances.

Comparison: The benchmark methods used have all been solved using classical/modern control methods, yet the author did not include any non data-driven solutions for comparison. This may be a useful addition to the paper.

### Questions
Recommended fixes:
which provides enhanced model predictability and adaptability, as compared to Koopman models with constant Koopman operators -- you mean prediction capability  ?
Since time scales are important , figures should include time , instead of time steps ( or epochs) , Fig 8 just has  "t" with no units,  Please provide unit son all figure axes where possible   

Claims requiring more evidence:  
MamKO achieves good balance between advanced modeling capabilities and real-time control implementation efficiency --> 
This claim in RT implementation needs more support hence actual time units are needed.  The RSCP problem has a scale of hours and is therefore generally very slow.  It will be good to see clearly the range of problems in time scale and frequency scale to understanding capability against system dynamics. 

Theoretical:  The paper could use more rigorous theoretical analysis or proofs to back the claims of stability and effectiveness in capturing time-varying dynamics. For example, formal proofs of the convergence properties of the Mamba-based Koopman operators or bounds on the error in approximating nonlinear systems would greatly increase the paper’s credibility.

Equation (5): The transition from a time-invariant to a time-varying state-space model is theoretically justified but lacks a rigorous mathematical proof. The paper relies heavily on empirical evidence, perhaps some theoretical discussion may be help support eth generalizability of the method.

CELU Activation: The use of the negative CELU function is an interesting choice to handle instability. The mathematical justification provided for this choice seems reasonable, but more in-depth analysis of how it impacts model stability across different systems would strengthen the claim.

### Soundness
3

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
4

### Summary
The paper investigates complex dynamical systems and aims to address limitations in modeling these systems using Koopman operators. It explores the application of large language model (LLM) technology to manage the nonlinear and time-varying characteristics of dynamic systems. The work introduces a framework combining Mamba with Koopman operators, leveraging Mamba’s matrix generation capabilities to predict the future states of time-varying systems. This approach preserves a linear state-space structure while enhancing the model’s predictive accuracy and adaptability, creating a linear invariant state-space model. The paper is well-structured and logically organized, presenting innovative ideas with strong experimental support and highlighting the potential impact of this approach on complex dynamical system modeling and control.

### Strengths
1. The paper provides comprehensive experimental steps, data, and ablation analyses to validate the superiority of the MamKO model.
2. Through experiments on multiple benchmark systems, the paper demonstrates the advantages of MamKO in handling time-varying systems.
3. The paper shows that MamKO modeling relies on multi-step prediction, enabling the model to scale to complex systems with multi-step dependencies effectively.
4. Based on the MamKO model, the paper develops an MPC (Model Predictive Control) scheme, emphasizing its computationally efficient optimal control for nonlinear systems.

### Weaknesses
1. The paper does not provide quantitative metrics to justify why the Mamba model was chosen over other models, nor does it include comparative experiments with other LLM models.
2. All experiments on time-varying systems were conducted in simulated environments, lacking consideration of real-world physical factors. Thus, there are questions regarding the actual performance of the MamKO model.
3. Although the paper emphasizes solving time-varying problems in control systems, it lacks an analysis or discussion of the control scheme’s stability and robustness.
4. The proposed approach uses multi-step historical data but needs to address the accumulation of errors that this may cause, which significantly affects the rigor of the model.
5. While the paper aims to apply the MamKO framework to time-varying systems to address related issues, it does not explicitly discuss the delay errors present in time-varying systems or propose corresponding solutions.

### Questions
1. The paper chooses the Mamba model as the basis for the overall approach but needs to provide quantifiable evidence supporting this choice. Could the authors provide relevant data to clarify the rationale for choosing the Mamba model?
2. All validation experiments were conducted on a simulation platform, with no hardware experiments presented. Simulation results are not a substitute for results from real-world experiments. Could the authors conduct hardware experiments to verify the feasibility and effectiveness of the approach?
3. The proposed framework aims to solve time-varying issues in time-varying systems but needs more discussion of delay errors and accumulated multi-step prediction errors, as well as the effects these errors may have on system stability and robustness. Did the authors consider these issues in the initial design phase? If not, could they now provide evidence to show the approach can address these issues?
4. The paper indicates that MamKO relies on multi-step prediction to achieve scalability for complex systems. Could you provide a detailed comparison of the computational overhead between MamKO and other methods? For instance, do quantitative data on computation time or hardware resource consumption for equivalent tasks exist to demonstrate the efficiency of MamKO?

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
4

### Summary
The paper innovatively combines the Mamba architecture with Koopman operators, introducing the MamKO framework - the first application of a large model architecture to Koopman modeling and control. The authors effectively leverage Mamba's capabilities in time-varying modeling and improve the matrix generation mechanism by replacing the negative exponential function with CELU activation function, enabling the model to handle unstable systems. Furthermore, based on the generated time-varying Koopman operator, they designed an MPC controller that significantly enhances modeling and control performance while maintaining computational efficiency. In the experimental section, the authors demonstrate MamKO's practical performance across multiple application scenarios (such as CartPole and chemical processes) and compare it with other control methods (like SAC) to validate its superiority.

### Strengths
- Innovation: First-time integration of Mamba architecture with Koopman operators, introducing the MamKO framework, pioneering a new application of large models in control theory.

- Performance: Demonstrated superior performance of MamKO-MPC across multiple practical application scenarios, with effective comparisons against existing control methods.

- Model Enhancement: Improved the matrix generation mechanism in Mamba through CELU activation function, enabling the handling of unstable systems and enhancing model robustness.

- Computational Efficiency: The designed MPC controller maintains high computational efficiency while improving modeling and control performance, reducing the computational burden associated with traditional online Koopman methods.

### Weaknesses
The paper has a clear overall structure, but lacks sufficient depth in key areas, particularly in justifying the choice of Mamba over other sequence model architectures. Furthermore, the limited explanation of theoretical background makes it challenging for readers to fully understand the design rationale and advantages of the MamKO framework. Specifically:

Theoretical Analysis Needs Strengthening:
- Lacks in-depth theoretical analysis of system stability and convergence. As a control method incorporating deep learning, it should provide more comprehensive theoretical guarantees for system stability

Insufficient Model Selection Justification:
- While the similarity between Mamba's SSM structure and Koopman operators is mentioned, a detailed mathematical comparison between the Mamba SSM structure and Koopman operators lacks and reasons for choosing Mamba over other sequence model architectures based on SSM (like S4, H3) inadequate

Limited Control Task Types:
- Control tasks primarily focus on setpoint tracking, missing evaluation of other control tasks (trajectory tracking, disturbance rejection, energy optimization)

Experimental Evaluation Metrics Need Expansion:
- Lacks systematic evaluation of control performance metrics (overshoot, steady-state error), recommend including more control performance indicators to comprehensively demonstrate MamKO-MPC's advantages

### Questions
To enhance the impact and persuasiveness of this work, the following questions merit consideration:

1. A detailed analysis or proof regarding the theoretical stability and convergence properties of the MamKO framework would be valuable.

2. Validation of selecting the Mamba structure over other SSM-based models (such as S4, H3) would strengthen the paper, along with elaboration on Mamba's mathematical advantages and rationale in control tasks.

3. Could more evidence about the MamKO framework's generalization ability and robustness when handling systems with different dynamic characteristics be supported by experimental data?

### Soundness
3

### Presentation
3

### Contribution
4
