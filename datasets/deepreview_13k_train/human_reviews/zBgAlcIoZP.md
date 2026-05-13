# Dynamic Mode Decomposition-inspired Autoencoders for Reduced-order Modeling and Control of PDEs : Theory and Design

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
Modeling and controlling complex spatiotemporal dynamical systems driven by partial differential equations (PDEs) often necessitate dimensionality reduction techniques to construct lower-order models for computational efficiency. This paper studies a deep autoencoding learning method for controlling dynamical systems governed by spatiotemporal PDEs. We first analytically show that an optimization objective for learning a linear autoencoding reduced-order model can be formulated, yielding a solution that closely resembles the result obtained through the $\textit{dynamic mode decomposition with control}$ algorithm. Subsequently, we extend this linear autoencoding architecture to a deep autoencoding framework, enabling the development of a nonlinear reduced-order model. Furthermore, we leverage the learned reduced-order model to design controllers using stability-constrained deep neural networks. Our framework operates without prior knowledge of the governing equations of the underlying system, relying solely on time series data of observations and actuations. Empirical analyses are presented to validate the efficacy of our approach in both modeling and controlling spatiotemporal dynamical systems, exemplified through applications to reaction-diffusion systems and fluid flow systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a method that uses a learned reduced-order model to control PDEs. The paper first shows a close connection between the solution from a linear autoencoder and that of dynamic mode decomposition with control. The paper then extends it to the nonlinear domain and introduce a method for control. Experiments demonstrate the effectiveness of the method.

### Strengths
Significance: the paper addresses the important problem of modeling and controlling PDEs. The proposed method is effective. 

Novelty: the method seems to be novel within the field of neural PDEs. I'm not sure if similar methods (nonlinear autoencoding and control) have been proposed in the robotic control. The component that encourages the model to be exponentially stable is important and novel.

Soundness: the method is demonstrated to outperform the important baseline of deep Koopman and DeepROM.

### Weaknesses
Soundness:

For controlling PDEs, it may be important to compare with other classes of baselines, including backpropagation + surrogate model (e.g., [1]), RL-based (e.g., [2]), and predictor + controller methods (e.g., [3]). These are not required, but a more diverse comparison could strengthen the paper as a strong method within the field of PDE control.

Related works:

There are many neural PDE methods that model the PDE using learned reduced-order models (albeit without control), and may have connections to the proposed method, e.g., [4-8]. The authors are encouraged to state their similarities and differences in the related works section.

### Questions
N/A

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper devises a new method to develop ROMs for both linear and nonlinear control problems using autoencoding techniques. To guarantee its performance, the model encourages DMDc-like solutions on linear problems by designing a loss taking both dynamics prediction error and reconstruction error into consideration whereas nonlinear ones are tackled similarly by replacing all trainable components in the linear version into DNN.

### Strengths
1) Clarity: The exposition is basically clear. The description of the proposed method, the datasets involved and the baselines are detailed.
2) Quality: The math derivation seems sound.

### Weaknesses
1) Lack of ablation study. The paper mainly focuses on a new reduced-order approach (DeepROM) to model the system’s dynamics and adopts an existing method NI4C(Saha et al., 2021) to learn the control. Thus in the experiment, the original full-order NI4C should be compared, as an ablation study for DeepROM. However, in current experiments, only LQR controls are compared.

2) Insignificant performance improvement. The performance of the DeepROC on the vortex-shedding task seems to be worse than LQR baselines (Figure 3(b,c)).  The overall idea of reduced-order control is not new, thus the performance improvement is an important measure of contribution.

3) Lack of higher dimensional and more complex datasets. In the abstract, the authors state that: "Controlling complex PDEs often necessitates dimensionality reduction for computational efficiency." However, the experiments are about 1D reaction-diffusion and 2D N-S(with low Re). Such systems can be learned and predicted efficiently via full-order neural networks, such as simple FNN, DeepONet, FNO, PINN, and their variants. More complex datasets, such as 2D/3D N-S with turbulence or shock are needed to show the necessity of reduced-order models.

### Questions
The major questions are listed in the Weakness part. Here are some minor questions about network details:

1) How to choose tunable hyperparameter $\beta_{1,2,3}$?
2) Does adding a decoder and a reconstruction loss for control $u$ affect performance?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a framework for autoencoder-based modeling and control learning for PDE-driven dynamical systems. Traditional linear encoder and decoder are replaced by nonlinear parametrization with neural networks. The dynamic is also modeled by a neural network. The authors present numerical examples to validate their method.

### Strengths
The presentation of the paper is clear. I am not an expert in this area but I can clearly understand this work.
In the numerical results, the authors compare their method with existing methods. The method proposed in this paper has similar error performance but less cost due to a dimension reduction.

### Weaknesses
The idea of replacing linear encoder and decoder with neural networks is simple. There is not much innovation in this paper.

### Questions
About the learning of the control. Since the control is of feedback type, can we use a simple supervised learning from the observed data instead of loss (15)?
Page 6 middle. In the integration, it should be t instead of t_i?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a deep autoencoding learning method for modeling and controlling spatiotemporal systems driven by partial differential equations (PDEs). The authors introduce a linear autoencoding model, then expand to a nonlinear framework using deep autoencoding. This framework aids in designing controllers using stability-constrained neural networks, without needing prior system equation knowledge. Its efficacy is demonstrated on reaction-diffusion and fluid flow systems using time series data. Empirical results are promising, when compared to existing DMD based methods.

### Strengths
This is a theoretically sound paper for learning a reduced order model for PDE systems. Empirical results are very promising when compared to existing DMD based methods.

### Weaknesses
The paper only compared to DMD based methods, however, transformer based VAEs like VQ-VAEs and VQ-GANs have achieved SOTA performances on video data. It would be very beneficial to see a comparison with these more data-driven methods.

### Questions
N/A

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
