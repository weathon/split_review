# Disentangled Representation Learning for Parametric Partial Differential Equations

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 3, 8

## Abstract
Neural operators (NOs) have demonstrated  remarkable success in learning mappings between function spaces, serving as efficient approximators for the forward solutions of complex physical systems governed by partial differential equations (PDEs). However, while  effective as black-box solvers, they offer limited insight into the underlying physical mechanism, due to the lack of interpretable representations of the physical parameters that drive the system. To tackle this challenge, we propose a new paradigm for learning disentangled representations from neural operator parameters, thereby effectively solving an inverse problem. Specifically, we introduce DisentangO, a novel hyper-neural operator architecture designed to unveil and disentangle the latent physical factors of variation embedded within the black-box neural operator parameters. At the core of DisentangO is a multi-task neural operator architecture that distills the varying parameters of the governing PDE through a task-wise adaptive layer, coupled with a hierarchical variational autoencoder that disentangles these variations into identifiable latent factors. By learning these disentangled representations, our model not only enhances physical interpretability but also enables more robust generalization across diverse physical systems. Empirical evaluations across supervised, semi-supervised, and unsupervised learning contexts show that DisentangO effectively extracts meaningful and interpretable latent features, bridging the divide between predictive performance and physical understanding in neural operator frameworks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a model based on a neural operator architecture, integrating an encoder-decoder structure to derive interpretable representations and address multiphysics problems by disentangling data into distinct factors.

### Strengths
The paper effectively presents a clear motivation and a well-organized introduction. 

To the best of my knowledge, the theoretical contribution addressing the identifiability issue is both novel and significant.

### Weaknesses
The methodology section would benefit from additional clarification in the following areas.

1. In lines 189 and 204, the term “parameters” referred to both the parameters within the differential equation and those within the neural operator, which may introduce ambiguity. While the authors have distinguished these parameters through notation, we kindly request that the authors revise the manuscript to adopt distinct terminology for each set. This revision would further enhance clarity in distinguishing between the two. Specifically, the term 'parameter' is overloaded, referring to both the physical parameters of the PDE (e.g., material properties) and the trainable weights of the neural network. This dual usage makes it difficult to follow the precise meaning in certain contexts, particularly when discussing identifiability. For instance, when discussing the identifiability of parameters, it is crucial to be explicit about whether the discussion pertains to the physical parameters or the neural network weights.

2. In Theorems 1 and 2, separating the assumptions from the main theorem statements could enhance readability. The current formulation may be somewhat challenging to follow, and presenting the assumptions outside each theorem could help clarify their interpretation. For instance, the authors might consider defining all relevant assumptions -- such as density smoothness, invertibility, conditional independence, and linear independence -- at the beginning of Section 3.2. These assumptions could then be referenced as needed throughout the related theorems. Additionally, the authors may wish to discuss the importance and validity of each assumption to support the theoretical framework. The current presentation makes it difficult to assess the scope and limitations of the theoretical results. For example, the smoothness assumption on the density of the latent variables is not discussed in detail, and it is unclear how this assumption might affect the applicability of the theorems to real-world scenarios. Similarly, the linear independence assumption, while common in identifiability analysis, requires further justification in the context of the specific problem being addressed.

3. The term "latent supervision" appears to denote a semi-supervised learning context (SC2) in the paper. Using consistent terminology throughout the paper would enhance readability and facilitate understanding. If our interpretation is accurate, we kindly request that the authors consistently use "semi-supervised learning when referring to SC2 throughout the paper.

### Questions
1. Theorem 1 addresses the identifiability issue up to an invertible transformation, which may not depend on the differential equation parameters. Could the authors clarify the source of this identifiability issue, and specify what guarantees the theorem provides regarding distribution uniqueness despite this transformation? (While Theorem 2 confirms identifiability even without such a transformation, further elaboration could be beneficial.)

2. In the proposed neural operator model, shared parameters are introduced to reduce degrees of freedom. While the architecture appears sufficient to support the presented theorems, could the authors clarify whether this model structure is indeed minimal? For instance, in line 314, the authors parameterize the posterior distribution $q$ with projection weights $\mathcal{P}$, possibly because the weights in $\mathcal{P}$ are fewer than those in $\mathcal{Q}$ or the intermediate layer. Is this reduction the primary rationale behind the model’s design? We would greatly appreciate further details on the trade-offs in using additional weights in $\mathcal{Q}$ or the intermediate layer for parameterization and how this choice impacts the model's overall performance and interpretability.

3. In line 210, the statement that parameters in the equation cannot be learned under zero Dirichlet boundary conditions is intriguing. Could the authors briefly elaborate on this point?

4. Is it possible to empirically validate one of the assumptions in Theorems 1 and 2, such as linear independence, within the simulation? Although these assumptions may be reasonable based on literature in line 302, empirical support could further strengthen the argument.

5. Tables 2 and 3 indicate that increasing the latent dimension improves prediction results. Is there a specific reason, such as computational constraints, for selecting a latent dimension smaller than 30? The authors might consider including experiments with higher latent dimensions to explore this effect further.

6. In Table 1, MetaNO, which is applied solely to forward problems, utilizes fewer parameters than other models. Could the authors clarify the rationale behind this choice? Additionally, could the author provide the inference time or total training time for each model with the specified number of parameters to enable a more thorough comparison?

7. Could the authors briefly explain how parameter classification information was utilized in NIO and FNO within the latent supervision setting in Table 1?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce DisentangO, a novel neural operator architecture based on a variational framing that aims to perform both physics modeling (e.g. forward PDE solving) and governing physics discovery (e.g. inverse PDE solving). The authors provide theoretical analysis showing when the true physical factors can be identified from the learned representations. The effectiveness of the method is demonstrated in supervised, semi-supervised, and unsupervised learning settings. Additionally, the authors demonstrate that the learned VAE embedding space corresponds to physically meaningful properties on the Mechanical MNIST benchmark.

### Strengths
- The paper investigates an important question, interpretability in PDE learning, which has been underexplored in the literature.
- The authors provide interesting theoretical results regarding when physical parameters can be uniquely identified.
- The empirical results are promising:
  - Especially in the supervised and semi-supervised settings, the proposed method is shown to match or outperform existing SOTA neural operator models.
  - Furthermore, the distinction of supervised vs. semi-supervised vs. unsupervised learning in the setting of neural operators is interesting, and the proposed architecture is one of the few which can engage with all three regimes.

### Weaknesses
 - The main weakness of the paper is that the empirical results regarding the claims of interpretability are somewhat limited. The authors do not propose clear metrics for evaluating interpretability:
  - MMNIST: the authors show that the latent space clusters data based on digit (Fig 3, 7, 8) and that the latent space can be interpolated (Fig 6). However, these seem to be standard properties of VAEs, and it's unclear whether meaningful physical interpretability is being achieved. Specifically, while clustering by digit is shown, there's no demonstration that the *specific* latent dimensions correspond to *specific* physical properties of the digits (e.g. stroke width, curvature, etc.). Interpolation in the latent space also doesn't guarantee physical interpretability unless the interpolation path corresponds to a physically meaningful transformation.
  - Heterogeneous material learning: the authors show that a DisentangO with a latent dimension of 3 is able to associate a different physically-meaningful characteristic with each of its dimensions. However, this problem is quite toy, and it's unclear whether these insights transfer to larger problems/networks. The material properties are also quite simple (e.g. a single material parameter per dimension), and it's not clear how this would generalize to more complex, spatially-varying material properties.
- The paper's writing clarity could be improved in places:
  - The proposed architecture is described in the intro/abstract/conclusion as a "hyper-neural operator" and "hierarchical variational autoencoder", but these terms are not clearly defined in the pape. In particular, the term "hierarchical VAE" seems to be used differently from the typical definition in the literature [1], which involves partitioning latent variables into disjoint groups and modeling conditionally ($\prod_l p(z_l \mid z_{< l})$). The model used in the paper seems to be a standard VAE, if I understand correctly.
  - Similarly, the intro mentions that DisentangO learns from "multiple physical systems", when it seems the paper focuses on different instances of the same PDEs/physical systems. It is unclear what constitutes a distinct physical system, and the examples provided seem to be variations of the same underlying physics.
  - In general, the model architecture could be more clearly described in Section 3.1. A clearer caption in Figure 1 could also be helpful. The description of the encoder and decoder networks is vague, and it's not clear how the latent space is connected to the neural operator.
  - Tables 2 and 3 would be clearer if model names were included in the table rather than the abbreviation number.
- The existing empirical results could be clarified: see questions.

### Questions
- Interpretability: is there any way to systematically validate that the latent factors learned by DisentangO correspond to actual physical parameters, especially in the unsupervised setting with large latent dimension?
- In Table 1, it is shown that a MetaNO with half as many parameters as DisentangO matches on forward problem error. How does the comparison look with a parameter-matched MetaNO? Similarly with Table 3.
- How does the choice of neural operator architecture (IFNO for the DisentangO vs. other architectures as baselines) affect the results? How would IFNO compare on the supervised setting, and could the model be improved by using MetaNO's architecture for DisentangO?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces DisentangO, a novel variational hierarchical neural operator designed to solve forward and inverse problems simultaneously. The authors present theoretical results to substantiate the method, which is further evaluated through numerical experiments on various benchmark datasets.

### Strengths
- The paper presents an innovative architecture that combines a hierarchical variational autoencoder (VAE) with a Fourier neural operator (FNO) to address inverse problems.
- The authors also provide a theoretical analysis on the component-wise identifiability of the model.
- The proposed method outperforms the baselines in the supervised settings.

### Weaknesses
 - The presentation lacks clarity.
- The experiments conducted on semi-supervised and unsupervised datasets are insufficient, with a notable absence of comparisons to baseline algorithms.
- The learning process does not adequately incorporate information from the partial differential equations (PDEs).

### Questions
1. Presentation
- The overall architecture presented in Figure 1 is not sufficiently informative. The meaning of each arrow in the figure is unclear, as some appear to represent feed-forward computations while others do not.
- Additionally, every notation should be clearly defined upon its first introduction; this paper lacks clarity in this regard.
- What are the first decoder and second decoder in Figure 1?
- How did you computed $\theta_P^{\eta}$ from the input? This is not explained in the manuscript. 
- How did you reconstructed $b^\{\eta}$ from $z$ for the semi-supervised and unsupervised settings? 

2. Experiments
- The authors conducted experiments on several benchmark datasets. What baseline algorithms, aside from neural operators and variational autoencoders (VAEs), were used for these datasets? Additionally, could you provide the test errors for the traditional methods?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduce DisentangO, a novel architecture that disentangles latent physical factors from neural operator parameters. The model is capable of solving forward and inverse problems at the same time. By combining a multi-task model with a VAE-based approach, DisentangO improves physical interpretability and generalization across PDE-driven systems. The paper offers theoretical guarantees to support the effectiveness of their method.

### Strengths
1) The authors present a novel approach based on VAEs that addresses both forward and inverse problems simultaneously.

2) They offer theoretical guarantees to support the effectiveness of their method.

3) The approach is evaluated against MetaNO and basic VAEs.

4) The paper is well-written and mathematically rigorous.

### Weaknesses
(1) The work has the potential to be highly impactful. However, several papers that take a similar approach are not cited in this work [1][2][3]. I believe these papers should be acknowledged and their contributions recognized.

(2) The networks used in the benchmarks are relatively small. For example, the FNO architecture that you used in supervised settings has only 8 modes and a width of 26, which is quite modest. This raises concerns about the model's capacity to capture complex physical phenomena and its ability to generalize to more challenging scenarios.

(3) The architecture used for baseline VAEs' encoders and decoders are simple MLPs. I believe that more appropriate and strnoger baselines would be convolutional VAEs, for example. This choice of baseline might not be sufficiently competitive to demonstrate the advantages of the proposed method, especially given the spatial nature of the data.

(4) The model is not compared to the state-of-the-art approaches such as [1][2][3]. The work done in [1][3] could be easily adapted to experiments in the paper.

### Questions
1) Why do you use simple MLPs for VAE architectures as baselines and not more advanced architectures?

2) Why are relatively small models, like the 0.7M FNO, being used?

### Soundness
2

### Presentation
3

### Contribution
2
