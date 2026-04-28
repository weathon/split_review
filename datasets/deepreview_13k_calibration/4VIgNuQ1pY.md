# Stable Neural Stochastic Differential Equations in Analyzing Irregular Time Series Data

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Irregular sampling intervals and missing values in real-world time series data present challenges for conventional methods that assume consistent intervals and complete data. Neural Ordinary Differential Equations (Neural ODEs) offer an alternative approach, utilizing neural networks combined with ODE solvers to learn continuous latent representations through parameterized vector fields. Neural Stochastic Differential Equations (Neural SDEs) extend Neural ODEs by incorporating a diffusion term, although this addition is not trivial, particularly when addressing irregular intervals and missing values. Consequently, careful design of drift and diffusion functions is crucial for maintaining stability and enhancing performance, while incautious choices can result in adverse properties such as the absence of strong solutions, stochastic destabilization, or unstable Euler discretizations, significantly affecting Neural SDEs' performance. In this study, we propose three stable classes of Neural SDEs: Langevin-type SDE, Linear Noise SDE, and Geometric SDE. Then, we rigorously demonstrate their robustness in maintaining excellent performance under distribution shift, while effectively preventing overfitting. To assess the effectiveness of our approach, we conduct extensive experiments on four benchmark datasets for interpolation, forecasting, and classification tasks, and analyze the robustness of our methods with 30 public datasets under different missing rates. Our results demonstrate the efficacy of the proposed method in handling real-world irregular time series data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the challenges posed by irregular sampling intervals and missing values in real-world time series data. The authors propose three classes of Neural Stochastic Differential Equations (Neural SDEs) to improve robustness under distribution shifts in time series data. The proposed Neural SDEs include Langevin-type SDE, Linear Noise SDE, and Geometric SDE. The study demonstrates the robustness of these Neural SDEs theoretically and through extensive experiments, showing their effectiveness in handling real-world irregular time series data and maintaining excellent performance under distribution shifts due to missing data.

### Strengths
The authors provide a solid theoretical foundation for the proposed Neural SDEs, including the existence and uniqueness of solutions. 

The robustness section in the paper provides valuable insights into the proposed Neural SDEs' resilience against distribution shifts and input perturbations. 

 The paper conducts extensive experiments to validate the effectiveness of the proposed Neural SDEs. The models are tested on various datasets, and their robustness is analyzed under different missing rates, providing a comprehensive evaluation.

### Weaknesses
I didn’t identify major weakness in this paper; however, there are a few minor concerns that I would like to address:

1. Section 3.4 could be more explicit in detailing how the controlled path is incorporated into the Neural SDEs. The current description lacks clarity on how the neural network $\zeta: \mathbb R_+ \times \mathbb{R}^{d_z} \times \mathbb{R}^{d_x} \rightarrow \mathbb{R}^{d_z}$ is specifically utilized to produce $\overline{\mathbf{z}}(t)$ by concatenating the latent variable $\mathbf{z}(t)$ and the controlled path $X(t)$. Providing a more detailed mathematical formulation or a diagrammatic representation of this process would significantly enhance the understanding of the model's architecture and functionality.

2. While section 3.3 discusses the robustness of the proposed Neural SDEs under distribution shifts, it might benefit from a more thorough exploration or comparison with other neural SDEs' robustness aspects in related works. For instance, a comparative analysis of how the proposed models perform against existing Neural SDE architectures under similar distribution shift scenarios would be valuable. This could involve evaluating the stability and performance degradation under controlled perturbations or missing data patterns.

3. What is the $\| \sigma_\theta  \|$ in Theorem 3.6 ? Is it a constant or does it vary with time? A clear definition and its implications on the stability analysis would be beneficial.

4. In the experiments of missing data (Table 4), the proposed Neural SDEs show only marginal improvements when compared to the Neural CDE model. This raises questions about the practical significance of the proposed models in scenarios with high missing rates. How do the theoretical bounds in Theorems 3.5 and 3.6 relate to the robustness of the Neural SDEs in practical implementations? Are these bounds tight or rather loose in actual application scenarios? A discussion on the tightness of these bounds and their implications for practical performance would be insightful.

5. The implementation code is not provided, making it difficult to reproduce the results and verify the experimental setup. Providing the code would enhance the transparency and reproducibility of the research.

### Questions
The details of the proposed models seem unclear.  Can you clarify which neural networks are used in the diffusion and drift functions of each Neural SDE?  

Additionally,  how are the proposed neural SDEs solved, especially the neural GSDE?   Do you employ numerical solvers for the Neural SDEs? If so, which specific solver was utilized, and was there any ablation study conducted to evaluate its effectiveness?

How much computational time is required for training the proposed Neural SDEs, and what is the complexity of these models?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces three stable classes of Neural SDEs (Langevin-type SDE, Linear Noise SDE, and Geometric SDE) to capture complex dynamics and improve robustness under distribution shifts in time series data. Theoretically, this paper shows the existence and uniqueness of the solutions of these SDEs, and presents their performance guarantee under distribution shifts. Extensive experiments are conducted to validate the good performance.

### Strengths
Topic-wise, modeling time series data with irregular sampling intervals and missing values is an essential research topic and of great importance in practice.

Theory-wise, this paper proves the existence and uniqueness of the solutions of the proposed three SDEs, and shows their robustness to input data. 

Additionally, extensive numerical results are presented to compare the proposed method with existing algorithms for time series modeling.

### Weaknesses
The computational complexity of the proposed method is certainly high.

This paper lacks sufficient details on the implementation of the method, especially when there are irregular time steps and missing data in the series.

For time series data, in addition to interpolation and classification tasks, it would also be meaningful to consider forecasting tasks as well, which seems to be absent in this paper.

### Questions
Detailed discussions on the training procedure are needed, especially for dealing with irregular time steps and missing data. For instance, with different irregular time steps across different sample time series, is it still possible to train the algorithm using mini-batch optimization; and is there a way to improve the computational efficiency in practice? When there is missing data in the sequence, how do we deal with missing values in the training phase -- are these missing values being imputed or ignored during the pre-processing step?

More explanations are needed for Figure 1 — line (i) exhibits a constant loss, and in fact, most of the loss trajectories are not satisfactory, with unstable trends and not decaying with the increase of epochs.
 
From Table 5, it is a bit confusing why there is no result for LSDE, LNSDE, and GSDE-‘+Z’.

The downstream tasks considered in this paper are interpolation and classification; it could also be meaningful and worthwhile to consider the prediction task for time series data as well.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The problem of learning neural stochastic differential equations (NSDE) to solve classification/interpolation tasks in the context of (irregularly sampled) time series data is considered. The authors focus on the analysis of theoretically well-defined SDE classes that exhibit desirable properties in terms of parameterization of drift and diffusion coefficients by neural networks, e.g., in so-called NSDEs. In contrast to naive NSDEs, which can (theoretically) learn almost arbitrary classes of functions, the authors restrict themselves to classes of SDEs for which (i) a (uniquely) strong solution exists, (ii) which can be approximated in a numerically stable manner, and (iii) which remain robust to input perturbations. In addition, they build on concepts from the field of controlled differential equations, which are known to improve model performance on irregularly sampled time series data.  Extensive experiments with established benchmark data sets are included. These provide empirical evidence for the proposed improvements.

### Strengths
I appreciate the idea of taking a step back from the state of unlimited expressiveness in NSDE and instead concentrating on sub-classes of SDEs that have favorable properties that combine well with the functional class properties of neural networks. The authors reveal shortcomings associated with the use of unrestricted parameterization of drift and diffusion coefficients by standard neural networks. In turn, an ablation study empirically supports the assumption that careful design of drift and diffusion coefficients is indeed reflected in improved model performance.
The content of the paper is well organized, original to the best of my knowledge and shows no obvious spelling or grammatical flaws.
Last but not least, I enjoyed the theoretically analysis of robustness under distribution shift.

### Weaknesses
1. I don't see the necessity to include the details on Neural ODE and CDE into the main manuscript. However, thats more ore less a 
matter of taste.
2. (Section 4.2) Comparing such a rich variety of models is challenging. The main difficulty arises due to major differences in model structure. E.g., vanilla RNN based methods are by nature not capable to process irregularly sampled time series. As reported, data imputation strategies must be applied additionally. Another challenge arises from comparing methods that include a control mechanism (e.g., Neural CDE) with methods that do not (e.g., NSDE). The former are able to continuously correct the sampled trajectories over time during learning, while the latter can largely only adjust the initial state. However, the authors elaborate on the latter problem in Table 11, where the proposed methods nevertheless showed their advantage. However, I can't escape the impression that the built-in control mechanism is a big part of the success; because Neural CDE often takes the closely followed second place.

### Questions
1. For example, to evaluate robustness empirically, *explicit Euler* is used for all experiments (see page 25). What are the reasons for this choice? I am very curious about the impact of different numerical solution methods on these and other results. Can you explain this in more detail?
2. Are you planning to release your Code which would unlock reproducibility of the results?

Minor:

3. Aren't the initial state in the Eq. (2) and (3) supposed to be vectors and therefore should be bold?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
