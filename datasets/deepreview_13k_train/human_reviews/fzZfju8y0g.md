# In-Context Neural PDE: Learning to Adapt a Neural Solver to Different Physics

- Decision: Reject
- Scores: 3, 3, 3, 5, 3

## Abstract
We address the problem of predicting the next state of a dynamical system governed by *unknown* temporal partial differential equations (PDEs) using limited time-lapse data. While transformers offer a natural solution to this task through in-context learning, the inductive bias of temporal PDEs suggests a more tailored and effective approach. Specifically, when the underlying temporal PDE is fully known, classical numerical solvers can evolve the state with only a few parameters. Building on this observation, we introduce a large transformer-based hypernetwork that processes successive states to generate parameters for a much smaller neural ODE-like solver, which then predicts the next state through time integration. This framework, termed as *in-context neural PDE*, decouples parameter estimation from state prediction, offering closer alignment with classical numerical methods for improved interpretability while preserving the in-context learning capabilities of transformers. 
Numerical experiments on diverse physical datasets demonstrate that our method outperforms standard transformer-based models, reducing sample complexity and improving generalization, making it an efficient and scalable approach for spatiotemporal prediction in complex physical systems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces an in-context neural PDE framework that leverages a transformer-based hypernetwork to generate parameters for a neural ODE-like solver, effectively predicting the next state of dynamical systems governed by unknown temporal PDEs with limited time-lapse data. The authors claim that this approach decouples parameter estimation from state prediction, enhancing interpretability and outperforming standard transformer-based models in terms of generalization.

### Strengths
+ The proposed idea is straightforward.
+ The paper is well presented and easy to follow.
+ Results show the effectiveness of the model based on specified experimental settings.

### Weaknesses
 - The major weakness lies in novelty. The model simply results from the stacking of well-known NN modules in the context of numerical integration. I don’t see any novelty compared with many other models reported recently in the literature.
- The examples considered to verify the efficacy of the model are too simple. The performance of the model should be at least tested on 3D datasets (e.g., 3D NS, 3D RD, etc.) to support the current conclusion. In addition, spatiotemporally coarser datasets should be considered.
- The baseline models are out of date. More recent neural PDE solvers (e.g., pre-trained PDE solvers) should be compared. 
- The prediction horizon considered in the paper is too short (e.g., 32 steps). The model is only useful only long-term rollout prediction with high accuracy is retained.
- The literature review section is generally weak.

### Questions
Please see the weaknesses above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces the "in-context neural PDE" framework, which decouples parameter estimation from state prediction for improved interpretability and generalization in predicting dynamic systems governed by unknown PDEs.

### Strengths
1. The research tackles a problem of high practical importance, which has significant potential for real-world applications in computational physics and engineering.
2. The paper is overall well written and easy to read.

### Weaknesses
1. The paper's related work section does not fully address similar settings explored in other articles, such as [1, 2], which use contrastive learning techniques to extract physical information from unknown PDE sequences for prediction. Furthermore, the authors claim that methods like [3, 4] lack inductive bias for physics and require a large amount of data to generalize, but the paper does not provide experiments to substantiate this claim.

2. The paper refers to "inductive bias for physical systems," but it lacks a clear definition. It's not evident how this bias is integrated into the model or how it influences the predictions for various physical systems. Does the term "inductive bias" solely refer to the use of rollouts with a small step size?

3. The paper claims its work is applicable to "DIFFERENT PHYSICS," but it does not sufficiently emphasize the specific physical quantities that vary across different PDEs, such as parameters, external forces, or boundary conditions, in the dataset descriptions (Table 1).

4. The experimental section only compares the proposed method with AViT, lacking comparisons with other baselines, particularly those that are also suitable for multi-physics scenarios.

5. The authors only demonstrate that the extracted representations have physical significance in the experiment shown in Figure 5, which is relatively straightforward, as there is a noticeable difference between fluids with viscosity coefficients of 0.1 and 0.01. It would be more compelling if the authors validated the physical meaning of their extracted representations in more challenging and diverse settings, similar to the studies referenced in articles [1, 2].

### Questions
Please see the weaknesses part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work tackles the task of spatiotemporal forecasting for PDEs governed by different unknown physics; each trajectory is thus described by a specific equation or set of coefficients. To build a neural solver able to generalize to trajectories described by different physics, the authors advocate the use of in-context learning to adapt a cheap neural ODE solver via a transformed-based hypernetwork. The hypernetwork uses preceding T successive states for adapting the forecaster network to each unknown physics. The method is evaluated on a wide range of datasets and performs better or is competitive with existing baselines. It is also has been adapted to new physics via fine-tuning.

### Strengths
The paper is well written and easy to follow throughout and the motivations well explained.

The tackled task is important. Most of the times, machine learning approaches for solving PDE consider that a large number of trajectories are available for one single PDE equation with fixed parameters. In practical scenarios, multiple and unknown physics are expected, leading to very different dynamical behaviors, which need to be captured by a single neural network.

The forecaster network is more interpretable than existing data-driven approaches via a neural ODE using a simple CNN. The authors connect it to classical numerical methods.

### Weaknesses
Novelty:
- the technical contribution is relatively low. Adapting neural ODE-solver to different physics has already been explored. The use of hypernetworks for adapting neural networks has been well studied in the meta-learning litterature. it has also been used for dynamical systems to condition a neural-ode like solver [1]. The differences with [1] is 1) that environments are supposed known, each environment describing a specific physic, while here, the environments would correspond to the first T states. 2) the use of ICL against weights updates.
- icl works on quantized tokens in text, its use for continuous vectors and physical data is not straightforward. This has not been really well introduced in the paper. The authors notably justify their approach is close to [2], which employs a transformer approach for learning multiple physics using past states as input. It does not imply that [2] has ICL properties to me, as stated in the paper.

Evaluation:
- empirical results: while the method is competitive to AViT, it should have been compared to more related works. The method is presented as a meta-learning framework and comparison with respect to these approaches are thus important and should be included, to justify the strength of ICL compared to existing meta-learning strategies [1, 3, 4, 5, 6].

Choice of title:
- the title is not really appropriate: It sounds like the network is able to adapt to new physics (new equations) without fine-tuning, only by explicitly giving a new context, but the network needs to be fine-tuned as some layers of the network are specific to each dataset. I don't really understand why the authors decided to train a network on different PDEs simultaneously for leveraging the capacities of ICL, if fine-tuning is still needed for unseen PDEs.

### Questions
To me, when I think of ICL in text, arbitrary sized examples can be given to adapt the language model to a new task. Can your method be applied to arbitrary sized sequences, i.e., can the hypernetwork adapt the integrated network given N past states, where N can vary at inference ?

In the umap visualisation, at epoch 0, the points seem to be already very well clustered. How do you explain that?

I am bit concerned with the choices of the datasets. First, qualitatively, it is hard to see very big changes from t=0 to t=32. But more importantly, the designed task is to adapt the network to different unknown physics. It is not clearly stated in the paper. How much different physics are present ? Are the pde coefficients used during training the same during inference or test is done on new coefficients?

Concerning the NRMSE results, you presented results at specific time-steps. Do the results correspond to NRMSE for that specic frame at time T or for average score from time 0 to T? It would have been nice to include an average score over the full trajectory.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
This paper presents a novel method, in-context neural PDE, for predicting the next state of a dynamical system governed by unknown PDEs. The approach employs a large transformer-based hypernetwork to process successive states and generate parameters for a smaller neural ODE-like solver, which then predicts the next state via time integration. Numerical experiments validate the effectiveness of the proposed method.

### Strengths
(1) Combining the ICL approach with differentiable PDE solvers for spatiotemporal prediction is a promising direction.

(2) The paper is well-written, making it easy to read and understand.

### Weaknesses
(1)  The selection of numerical schemes should be more diverse. The current reliance on a single Runge-Kutta 4 scheme limits the exploration of the method's performance across different discretization approaches. This is particularly relevant given that different PDEs and initial conditions can exhibit varying degrees of stiffness, where a fixed scheme may not be optimal. For instance, implicit methods might be more suitable for stiff systems, while lower-order methods could be sufficient for smoother solutions. 

(2)  Since the proposed method involves ICL and numerical schemes, what is the computational complexity? Is the model sufficiently robust? The paper lacks relevant explanations on these aspects. The computational cost of the transformer-based hypernetwork and the subsequent neural ODE solver is not analyzed, making it difficult to assess the method's scalability. Furthermore, the robustness of the method to variations in initial conditions, noise in the data, and the length of the time integration is not discussed, which are crucial factors for real-world applicability.

### Questions
Refer to weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes the IC-NPDE framework for predicting future states in dynamical systems governed by unknown PDEs. Leveraging In-Context Learning (ICL), it employs a transformer-based hypernetwork to estimate parameters for neural ODEs, which use CNNs as vector fields. Experimental results demonstrate that IC-NPDE can operate effectively across multiple datasets, with the information bottleneck enhancing its generalization performance.

### Strengths
- The writing in this paper is good. The logic is clear, and the background and preliminaries are well-explained, making it highly enjoyable to read.
- The motivation is thoroughly articulated, effectively establishing the relevance and importance of the proposed IC-NPDE framework. This well-defined motivation makes the contributions and experimental results both meaningful and easy to appreciate.
- A significant strength of IC-NPDE is its ability to be directly trained on multiple different PDEs, showcasing its versatility and robustness. This capacity for multi-PDE training expands its applicability in real-world scenarios where multiple physical processes often interact.

### Weaknesses
- A notable limitation of the paper is the limited contribution and novelty. Generally speaking, the key techniques utilized in this work are already well-studied and very common in the community of modeling dynamical systems. For instance, the application of Neural PDEs is explored in works such as "NeuralPDE: modelling dynamical systems from data" [1] and "Neural partial differential equations for chaotic systems" [2]. Similarly, the concept of using neural networks to predict the parameters of ODEs is discussed in "Generative ode modeling with known unknowns" [3]. Furthermore, context-based learning for dynamical systems has been investigated in "Generalizing to new physical systems via context-informed dynamics model" [4].
- Although some related works may have different settings, this paper would benefit from expanding the related work section to provide a more thorough review of existing methodologies. Specifically:
  - Other Neural PDE Approaches: including [1, 2, 6]
  - Multiple Environment Settings: including [4, 5]. They should also be used as baselines in Section 4.4, single dataset training.
  - Predicting ODE Parameters with Neural Networks: [3]
- In lines 126-127, the author mentioned that the spatial dimension n ranges from 1 to 3; however, all experiments in the paper are limited to 1D and 2D PDEs, with no inclusion of 3D PDEs. Extending the experiments to cover 3D and even higher-dimensional PDEs would provide a more comprehensive evaluation of IC-NPDE’s scalability and performance across spatial complexities. Specifically, testing on 3D Navier-Stokes or other complex fluid dynamics simulations could reveal the framework's ability to handle higher-dimensional state spaces and more intricate spatial dependencies.
- All experiments in the paper are conducted on simulated data, with no evaluation on real-world applications. The inclusion of real-world datasets, such as those from climate science, would significantly enhance the paper's impact. For example, applying IC-NPDE to climate prediction in different areas could demonstrate its practical utility and robustness to noisy, real-world data.
- The experimental evaluation would be strengthened by including additional baseline models, even if multi-PDE settings are less common. Baselines that focus on learning individual PDEs or on learning within the same PDE with varying parameters should be incorporated to provide a more comprehensive benchmark in Table 3 and Table 5, respectively. For instance, comparing against models that are specifically trained on a single PDE could highlight the trade-offs between generalization and specialization.

### Questions
- The expression "much smaller neural PDE solver" in lines 66-67  is a little weird. IC-NPDEs are based on the Neural ODE architecture. Typically, in Neural ODEs, the neural network defines the vector field, while standard numerical ODE solvers perform the integration.
- The authors mention in lines 221–222 that Transformers are used as hypernetworks due to their auto-regressive properties. However, original Transformers with softmax attention are not inherently auto-regressive; it is only with modifications, such as those in [7], that Transformers adopt an auto-regressive structure.
- I am a bit unclear on why the authors chose RK4 as the ODE solver, given that it is a fixed-step-size solver. Adaptive-step-size solvers like Dopri5 are generally more common in the Neural ODE community. With an adaptive solver, the ablation study on step size might be unnecessary.

**References**:

[7] Katharopoulos, Angelos, et al. "Transformers are rnns: Fast autoregressive transformers with linear attention." *International conference on machine learning*. PMLR, 2020.

### Soundness
4

### Presentation
4

### Contribution
1
