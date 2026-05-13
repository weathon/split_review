# Latent Abstractions in Generative Diffusion Models

- Decision: Reject
- Scores: 3, 6, 6, 6

## Abstract
In this work we study how diffusion-based generative models produce high-dimensional data, such as an image, by implicitly relying on a manifestation of a low-dimensional set of latent abstractions, that guide the generative process. We present a novel theoretical framework that extends \gls{NLF}, and that offers a unique perspective on \acrshort{SDE}-based generative models. 
The development of our theory relies on a novel formulation of the joint (state and measurement) dynamics, and an information-theoretic measure of the influence of the system state on the measurement process. 
According to our theory, diffusion models can be cast as a system of \acrshort{SDE}, describing a non-linear filter in which the evolution of unobservable latent abstractions steers the dynamics of an observable measurement process (corresponding to the generative pathways). In addition, we present an empirical study to validate our theory and previous empirical results on the emergence of latent abstractions at different stages of the generative process.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors prove the mathematical equivalence between diffusion models and nonlinear filtering, where a stochastic process Y is controlled by an unobserved variable X. The authors show that diffusion generative modeling is related to inference of X using Y. If this is the case then the internal representations of denoiser networks must reflect our belief in X. They have empirical results demonstrating when certain latent statistics emerge during generation.

### Strengths
They rigorously define the connection between nonlinear filtering and diffusion.

### Weaknesses
The paper asks the reader to spend hours understanding their notations and results before describing the motivation in section 4. The paper is very challenging to read as is and I strongly recommend the authors clearly and succinctly describe their contributions before the technical details, which should also mostly be moved to the appendix. 

While a connection between two mathematical frameworks is challenging to derive, it is only interesting if it leads to a deeper understanding of either technique. The fundamental claim of the paper -- that denoising networks must internally represent latent abstractions -- is seemingly obvious given that these networks are trying to predict the denoised state of Y. I would appreciate it if the authors could clearly articulate what they've learned about diffusion models in the language people currently use to describe diffusion models (if this paper is about diffusion models, by the way, perhaps the whole notation should be in terms of a diffusion model, not NLF).

### Questions
See weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a theoretical framework that extends Nonlinear Filtering (NLF) to explain the emergence and influence of latent abstractions in diffusion-based generative models. Through the lens of stochastic differential equations (SDEs), the authors model the dynamics of observable and latent variables, showing how latent abstractions emerge hierarchically during the generative process. The study derives an information-theoretic measure to quantify the influence of these latent factors and validates the theory with experiments demonstrating distinct jumps in this measure, supporting the proposed model.

### Strengths
* Well-motivated introduction, situating the work within existing literature and highlighting its contributions.
* The structure is logically organized, and the mathematical formulations are rigorous, enhancing the soundness of the theory.
* The proposed information-theoretic measure effectively captures changes in latent abstractions during generation, with experiments showing jumps in the measure that align with theoretical expectations.

### Weaknesses
I have no significant weaknesses to report. Please see questions for minor points of clarification.

### Questions
* Lines 228-233: could you expand on the claim regarding hierarchical emergence of latent factors? For instance, would an experiment focusing on local details, such as grain on texture, further validate this? If the mutual information of these details increased later in the process, it would support this hierarchical perspective.
* For the mutual information estimation process on line 476, could you clarify the final numerical approach used to approximate this measure during the generative process?

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
This work offers a new way to theoretically understand the generative process of diffusion models using nonlinear filtering. In particular, the authors interpret the generative process in diffusion model as simulating the NLF dynamics, where an unobservable latent abstraction drives observable outcomes in the generative process. Second, the authors propose a concrete method to compute the mutual information between measurement processes and latent abstractions, measuring the extent to which a certain latent variable has been constructed at different stages of the generative process. Third, experiments have been conducted using the standard denoising diffusion model on the Shapes3D data with 6 attributes (floor hue, wall hue, object hue, scale, shape, orientations) as labels. Apart from mutual information, the authors also use the log likelihood (using a trained classifier network) and the entropy in a forking experiments, as proxies for latent variable abstraction.

### Strengths
The NLF viewpoint on diffusion model is to my knowledge new, and potentially interesting. The use of mutual information measurement is also helpful in quantifying the effect of noising/denoising on the latent variables (here labels). The experiments seem carefully carried out.

### Weaknesses
The methodology is sound provided that the datasets can be understood as being dictated by a low-dimensional set of latent variables, and that it is possible to understand the generative process as inferring the latent variables in a Baysian way. The experiments are also conducted solely on such a synthetic dataset, with each sample having a predetermined set of labels. Either the including of a theoretical discussion on this underlying basic assumption, or devising experiments on more diverse datasets, preferably both, will make the relevance of the work more convincing.



### Questions
1. The work by Scolocchi et al that is cited in the manuscript seems to contain many similar claims and the forward-backward experiments there seem similar to the forking experiments here, though the theoretical methods are different. Can the authors comment more on the differences and similarities and possible relations between the two works in the paper? 
2.  The caption of Figure 2 (noise with intensity $\tau$) seems to contradict ths figure? 
3. In line 405, do you mean "$\pi_3$ contains the same information... as the whole ...."? 
4. The results such as those shown in Figure 3 are given as a function of $\tau$, but I assume the meaning of which depends on the noising schedule chosen for the diffusion model. Wouldn't it give more insight to discuss them with respect to intrinsic quantities such as the signal-to-noise ration instead of the "time" $\tau$?

### Soundness
3

### Presentation
3

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
This work studies the role of latent abstractions in the stochastic general process of diffusion models by extending the nonlinear filtering (NLF) framework. More specifically, this work proves that the generative process can be viewed as a switch process between $Y_t$ and $\pi_t$, which corresponds to the image and latent abstractions space. Furthermore, the synthetic and real-world experiments support their theoretical results.

### Strengths
1.	The link between the NLF and diffusion models is really interesting.
2.	This work includes theoretical and empirical parts, which help us understand the role of latent abstractions.

### Weaknesses
1.	There are many theorems in the introduction part, which makes it hard to find the most important results of this work. It would be better to polish the presentation of this work. More specifically, I think it would be helpful to present Eq. (10) and Figure 1 and introduce the relationship between Eq. (10) and the classic stochastic process.
2.	It would be better to discuss the relationship between the experiment part and the theoretical part. It seems that the only connection is the mutual information estimation part.

### Questions
Please see the Weakness part.

Q1: Could this NLF framework be extended to the deterministic sampling process?

### Soundness
3

### Presentation
2

### Contribution
3
