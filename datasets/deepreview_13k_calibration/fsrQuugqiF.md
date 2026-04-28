# Tensor-Var: Variational Data Assimilation in Tensor Product Feature Space

- Decision: Reject
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Variational data assimilation estimates the dynamical system states by minimizing a cost function that fits the numerical models with observational data. The widely used method, four-dimensional variational assimilation (4D-Var), has two primary challenges: (1) computationally demanding for complex nonlinear systems, and (2) relying on state-observation mappings, which are often impractical. Deep learning (DL) has been used as a more expressive class of efficient model approximators to address these challenges. However, integrating such models into 4D-Var remains challenging due to their inherent nonlinearities and the lack of theoretical guarantees for consistency in assimilation results. In this paper, we propose *Tensor-Var* to address these challenges using kernel Conditional Mean Embedding (CME). Tensor-Var improves optimization efficiency by characterizing system dynamics and state-observation mappings as linear operators, leading to a convex cost function in the feature space. Furthermore, our method provides a new perspective to incorporate CME into 4D-Var, offering theoretical guarantees of consistent assimilation results between the original and feature spaces. To improve scalability, we propose a method to learn deep features (DFs) using neural networks within the Tensor-Var framework. Experiments on chaotic systems and global weather prediction with real-time observations show that Tensor-Var outperforms conventional and DL hybrid 4D-Var baselines in accuracy while achieving efficiency comparable to the static 3D-Var method.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes an innovative Tensor-Var method, which integrates kernel conditional mean embedding with 4D-Var data assimilation to address computational efficiency and convergence issues in the optimization of nonlinear dynamical systems.

### Strengths
The Tensor-Var method is proposed, applying kernel conditional mean embedding to 4D-Var data assimilation, significantly improving the optimization efficiency of nonlinear dynamical systems.

### Weaknesses
Although the method shows remarkable performance on simulated data, its validation on real-world datasets is relatively limited. Additional tests in practical application scenarios could be supplemented.

### Questions
see Weaknesses

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Tensor-Var, a novel data assimilation (DA) framework that uses Conditional Mean Embeddings (CME) in conjunction with deep learning based nonlinear feature maps ("deep features", DFs) to linearize observed nonlinear dynamics in feature space, addressing issues of the traditional 4D-Var data assimilation problem. Tensor-Var achieves both competitive accuracy and efficiency compared to 4D-Var and other baselines in chaotic dynamics and numerical weather prediction benchmarks.

### Strengths
- The authors use known and established methods in the field of deep learning and nonlinear dynamics (CME, DFs, delay embeddings, overcomplete autoencoders) to substantially improve over existing DA methods.
- The paper is generally well-written
- The authors clearly motivate each and every modification to the final employed algorithm they propose and provide plenty of theoretical justifications

### Weaknesses
 - A lot of compartments of the approach have deep roots in dynamical systems theory (DST), which the authors do not seem to touch upon:
1. using a history of observations to better model the state of the underlying dynamical system is connected to the method of delay embeddings, often used for attractor/state space reconstruction in nonlinear dynamics [1, 2]. This field has ample literature, including (optimal) heuristics to create these embeddings, from choosing time lag between history time stamps to number of lags/dimension of the embedding [3]. This literature might provide better ways of finding an optimal representation of the underlying system state and might a reasonable alternative to costly cross-validation to find the optimal history length. All this could be discussed when introducing the history method in section 3.1.
2. Mapping nonlinear dynamics in (infinite) higher dimensional spaces with the aim to linearize the dynamics in this space is the core idea of Koopman Operator theory [4]. However, I am not familiar with KKL-observer theory (which the authors address in the paper). These fields might be strongly connected. Anyhow, at least a brief connection to this large field of research is missing in the manuscript.

- As the authors point out in their limitations: The feasibility of the framework in real-world applications is questionable due to the ground-truth state data demand. However, a more elaborate discussion on how Tensor-Var yields any improvement in this data setting compared to traditional DA methods would be welcome to guide future research.

Minor Details:
- ll. 173-174: “Equation equation 1”
- ll. 356-357: “global optimal” should be “global optimum”
- Author Contributions and Acknowledgments on p. 10 seem to contain the sample text of the ICLR template.

### Questions
- Is the entire loss objective of Tensor-Var really convex if the DFs are jointly learned with the linear operators/CMEs? Since the feature maps are parameterized by nonlinear NNs, the optimization should still be non-convex, no?
- Is there an intuitive reason why the NRMSE distributions of Latent 4D-Var are a lot more spread compared to Latent 3D-Var and Tensor-Var?
- Can the authors comment on the optimization of loss (7)? Learning the inverse feature map $\phi^\dagger_{\theta'_s}$ in this form comes down to an overcomplete autoencoder, which, when trained with a simple reconstruction loss, can often fall short in learning useful features and may easily overfit. Did the authors face any problems when training this architecture? And how does the regularization weight w influence the performance of Tensor-Var?
- A linear approximation of nonlinear dynamics can only be approximate, and hence, especially in chaotic systems, longer roll-outs will lead to qualitative and quantitative differences in the learned linear dynamics compared to the true dynamics (i.e. a linear model of nonlinear dynamics can not reproduce the “climate” or long-term behavior of the underlying system). Can the authors comment on this in the context of their DA approach?

I'm happy to increase my score if the authors appropriately address my comments and questions.

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
3

### Summary
This work presents *Tensor-Var*, an efficient 4D-Var computational framework. The key component of the framework are the linear representations of the dynamical systems and state-observation mappings obtained by kernel Conditional Mean Embedding. These transform the nonlinear state and observation models into a linear, convex framework, alleviating the need of nonlinear optimization. The framework is benchmarked against competitive variational DA baselines on two chaotic systems and a numerical weather prediction task.

### Strengths
- *Originality*: This work stands out as original as it avoids the DL trend and looks for an approximated solution which preserves theoretical guarantees. 
- *Quality & Clarity*: Thorough background as well as theoretical analysis of the framework is provided; proving the existence of linear dynamics with consistent convergence between the original and feature space solutions.
- *Significance*: The work addresses a core task, forecasting of dynamical systems, and provides improvement in efficiency and accuracy over evaluated settings.

### Weaknesses
 - *Baseline choices*: The authors describe many DL approaches suggested for the task and it is unclear why the performance of the chaotic system is evaluated only with respect to Frerix et al., 2021, neglecting the more recent attempts (e.g. Bocquet et al. 2024) and avoiding the Latent-x-Var baseline considered in the NWP task. 
- *Efficiency claims*: The framework is compared to variational approaches which rely on GPU acceleration via JAX (Bradbury et al., 2018) however runtime was evaluated on CPU making the comparison misleading and unfair. To address this the authors can either run each framework on most suitable hardware or state this evaluation limitation in the main text. A final alternative is to provide a GPU compatible *Tensor-Var* implementation.
- *Evaluation on synthetic data*: As mentioned by the authors, showcasing performance on simulated data is a limitation of the current work. It makes it hard to evaluate the applicability and performance over real world applications. 
- *Poorly written*: The paper is hard to read, it contains many grammatical errors, unclear sentences, and many repetitions. For example, lines 164-166 repeat definition mentioned a few times and contain grammatical inconsistencies, Lines 270-271 contain errors, and the entire conclusion section can be improved.
(**minor; remaining paragraphs from the template on page 10).

### Questions
In light of the above weaknesses, it will be valuable if the authors would:
(1) clarify baseline choices as well as runtime evaluation;
(2) showcase a more realistic application;
(3) proofread the manuscript to improve readability.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper utilizes the CME method to improve the efficiency of 4D-Var; Several toy scenarios are used to study the assimilation ability of the TENSOR-VAR in chaotic systems and global weather forecasting. Observations are simulated by sampling the dataset, rather than using true observations, for the assimilation of the background field. Ultimately, this work achieves a toy assimilation model with limited significance.

### Strengths
The article thoroughly discusses how the Conditional Mean Embedding (CME) method can further improve the efficiency of 4D-Var. It presents the mathematical principles of the method clearly, albeit with some redundancy, and employs several toy scenarios to compare various assimilation approaches.

### Weaknesses
1. The resolution is too low, and it seems that all observations are located at grid points (If not, please correct it), which greatly simplifies the problem.

2. Real observations are not used in assimilation:

(1) Real observations are often not randomly distributed and typically exhibit some certain patterns.
(2) The ERA5 dataset is already a reanalysis dataset (incorporating numerous observations and numerical simulations). Using random samples from ERA5 to simulate assimilation means that the model assimilates only one type of data, which differs significantly from reality. This article does not address or explain the assimilation of multiple sources of observations.
(3) A key aspect of assimilation is real-time processing (unlike data fusion), and the experimental design of this paper does not explore online operational scenarios.

In summary, I believe this work is still far from real assimilation applications. The research method and experimental design are relatively detached from real-world conditions, which significantly reduces the study's relevance and value. It creates some barriers to understanding. The article may not be particularly accessible to readers in physics-related fields, such as atmospheric science, complex systems, and general physics.

### Questions
In weaknesses part.

### Soundness
2

### Presentation
2

### Contribution
3
