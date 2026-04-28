# Efficient Integrators for Diffusion Generative Models

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 8, 6

## Abstract
Diffusion models suffer from slow sample generation at inference time.
  Therefore, developing a principled framework for fast deterministic/stochastic sampling for a broader class of diffusion models is a promising direction.
  We propose two complementary frameworks for accelerating sample generation in pre-trained models: \textit{Conjugate Integrators} and \textit{Splitting Integrators}. Conjugate integrators generalize DDIM, mapping the reverse diffusion dynamics to a more amenable space for sampling. In contrast, splitting-based integrators, commonly used in molecular dynamics, reduce the numerical simulation error by cleverly alternating between numerical updates involving the data and auxiliary variables. After extensively studying these methods empirically and theoretically, we present a hybrid method that leads to the best-reported performance for diffusion models in augmented spaces. Applied to Phase Space Langevin Diffusion [Pandey \& Mandt, 2023] on CIFAR-10, our \emph{deterministic} and \emph{stochastic} samplers achieve FID scores of 2.11 and 2.36 in only 100 \gls{NFE} as compared to 2.57 and 2.63 for the best-performing baselines, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Very sorry for the late review! I hope the authors will find my advice helpful! As the review is late, I think this is more like a piece of advice for the authors about how to improve this idea and submission. Please feel free to tell me if you have concerns about some of my suggestions!

This paper is based on a novel and fundamental idea, which has not been explored previously. I am supervised by the authors when they present their ideas, as it is a so fundamental and elegant formulation while I have not thought of it previously.

The authors propose to study the integral in a projected space, where the new variable has a stable homeomorphism with the original variable. Under this setting the original integral is equivalent to the new integral, while under careful design, the new integral could be much more easy and fast to compute. Almost all accelerating methods, as I can recall, can fit in this formulation, which means it can generally define the theory insights of all acceleration methods. It could be a good idea to simplify and extend the definition in this paper to a more generalized form. While this paper only considers linear projections, I think it is enough to cover most cases.

The authors then split the new integrals into multiple components, which earns further accelerations. The authors give enough discussions about the error analysis. Extensive studies on small datasets are used to fairly evaluate the proposed methods.

### Strengths
1. The formulation of the problem is fundamental and sound. Very promising direction of future research

2. Theory analysis about the stability and error is solid.

3. The method can extend to many familiar sampling techniques, providing a unified and novel insight for all of them.

### Weaknesses
1. I don't know whether I deviate too much from the author's experiences. In my experience, in most cases, 25-step DPM-solver sampling could produce good enough sampling results for large models like StableDiffusions on large diverse image distribution; and less than 15-step DPM-solver sampling could produce good enough results for small diffusion models in small data domain. Please tell me if you observe a different phenomenon, and I will be happy to test it. Getting back to the subject, are the 100 and 50 NFEs considered by this paper a bit redundant?

2. In eq 1, the authors actually simplify the original diffusion process to linear ones, and replace the f(z_t) function to linear map F_t z_t, so do please kindly mention that in the corresponding place. Otherwise, it may cause confusion. I care about the scope of this simplification, could it be applied to generation diffusion processes? Especially those in large-scale datasets and models? For example, 

3. The stability analysis seems to avoid the key points? I would like to know a two-phase conclusion: first, when will matrix A_t stability have an inverse, this is the key to the stable conjuncture; second, under the condition that A_t is inversible and stable, when will eq 7 and 8 as ODE solvers be stable? Theorem 2 seems like a naive application of ODE stability conditions, and gets rid of the key part. A_t is an integral of multiple components, so we may not directly assume it to be stably invertible. But you also do not assume it stable anyway (minimum eigenvalue larger than some positive constant). It would also be helpful if the authors could explain in what reality settings those conditions can be satisfied.

4. Theorem 3 gives error analysis based on h, I have concerns about its error with respect to the original t. After the projection is to solve the original problem, measuring the error in a projected space could be less meaningful. This is the same problem in the DPM-Solver paper, they only analyze errors when lambda is stably transformed from t, but in reality is often not the case. But DPM-Solver performs great generally so I am not criticizing it. Just point out that error analysis with respect to t variable is preferred for typical ode numerical analysis.

5. This work, also reminds me of the DPM-Solvers. DPM-Solver could be viewed as a special case, it also projects the integral to another space, the lambda space in fact. It uses a prediction-correction (PC) method to achieve much higher accuracy in the projected space. So I care about two things: first how the dpm-solver will formulate under your settings and when will your method outperform it? Second, can your method benefit from PC? While this work does not compare with DPM-Solver, considering the huge influences of and similarity with DPM-Solver, it could be better if the authors could compare with it.

6. Improvements seem not to be good enough, especially considering speed. Large datasets and models are also not considered.

### Questions
how the dpm-solver will formulate under your settings and when will your method outperform it? 

Sorry for the late review, hope you will find those points useful.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose two complementary frameworks for accelerating sample generation in pre-trained models: 'Conjugate Integrators' and 'Splitting Integrators'. Conjugate integrators generalize DDIM, mapping the reverse diffusion dynamics to a more amenable space for
sampling. In contrast, splitting-based integrators reduce the numerical simulation error by alternating between numerical updates involving the data and auxiliary variables. The authors test these approaches as well as combinations of these methods on different benchmark datasets.

### Strengths
- The theory is interesting and opens up many potential paths for future investigations. 
- For some datasets and low-medium number of total integration steps the aforementioned hybrid model shows excellent generative capabilites and outperform many well-known state of the art methods. 
- The writing is clear and the paper is well structured.

### Weaknesses
 - Combinations between datasets and methods are not consistent. For example in Figure 5, EDM is not tested on CelebA-64. Furthermore, these methods must be tested in more complex distributions such as ImageNet. 
- The training of each pretrained model and the size of the model is not specified in the main paper. Are these models identical and trained for the same amount of time?
- In Collorary 1, the authors show a connection between stability and the parameter $\lambda$ (which should evolve with time?), however it is not clear how this hyperparrameter is chosen. Furthermore, Corollary 1 does not explain the behaviour of $\lambda$-DDIM-II, which performs best.

### Questions
- Do the authors have an explanation why some methods outperform CSPS-D for very small numbers of NFE? (Figure 5, up-left plot). 
- Have the authors measured the total integration time? If the generation speed is our main objective, then such results should be provided as well.
- How is $m_0$ defined during the training of 'Conjugate Symplectic Euler' and 'Conjugate Velocity Verlet'? That is, what is the generated $m_{\epsilon}$. In my opinion, the paper would be improved if corresponding training algorithms to Algorithms 2 and 3 would be added. On a related note, does the transformation along the position dimensions $x_t$ remain a diffeomorphism in the augmented setting? If not, this could have negative implications about density estimation, and mode coverage in generation.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes two frameworks for improving integrators in generative diffusion models, conjugate integrators and splitting integrators, and it proposes a hybrid method combining the two. The integrators are developed from previous use in physics simulation, e.g. molecular dynamics, and they are applicable to augmented diffusion models, for example when including momentum. The authors provide intution behind the integrators and investigate theoretical properties. Finally, they demonstrate experimentally the power of the integrators.

### Strengths
- very clear and well-written paper
- very clever application of numerical integration methodology for generative diffusion models
- potentially high impact in improving results for fixed computational budgets

### Weaknesses
no apparent weaknesses

### Questions
no questions

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper...
- proposes conjugate integrators and splitting integrators for accelerating diffusion sampling,
- introduces practical changes to splitting integrators for efficient sampling ("reduced" samplers),
- combines conjugate and splitting integrators to achieve competitive performance in CIFAR-10, CelebA-64, and AFHQ-64 sampling.

### Strengths
- Studies conjugate and splitting integrators, which were relatively unexplored in diffusion sampling.
- Proposed samplers generalize previous diffusion integrators, such as DDIM.
- Clearly explains the advantages of conjugate and splitting integrators, and how they contribute in orthogonal ways.

### Weaknesses
While the paper has clear strengths, I think the paper needs a major revision. Specifically, I am inclined to give "reject" for the following reasons:

**Weakness 1 : Difficult to figure out the "main" contribution**
- There are too many proposed integrators, and it is difficult to figure out which one is / ones are the "main" contribution of the paper. More specifically, it is difficult to see in which situation we should prefer one integrator over the other. To me, it seems like the authors are taking a very unclear stance on their "main" sampler : the authors are proposing a whole arsenal of samplers, and picking results which happened to beat some baselines results under very specific dataset+sampler+hyper-parameter combinations.
- For instance, what is the rationale behind choosing $B_t = \lambda I$ and $B_t = \lambda 1$? When should we prefer DDIM-I over DDIM-II and vice versa? While there is a theorem on DDIM-I, I don't see any theorem on DDIM-II, which could clarify differences between DDIM-I and DDIM-II. The choice of $B_t$ seems arbitrary, and the lack of theoretical justification makes it difficult to understand the practical implications of each choice. Specifically, the paper lacks a clear explanation of how the spectral properties of $B_t$ affect the stability and convergence of the proposed integrators.
- Also, readers could expect conjugate+splitting integrators to out-perform conjugate/splitting integrators, as they combine the best of both worlds. However, we don't see this trend in Table 2, where we see Reduced OBA out-performing Conjguate OBA. The authors hypothesize "this might be due to a sub-optimal choice of $B_t$" -- I think this kind of explanation only confuses the readers, as it does not provide any guide on when we should and should not use conjugate splitting. The paper needs a more rigorous analysis of the conditions under which conjugate splitting is beneficial, and when it might be detrimental.
- I think one factor that makes this paper confusing is the lack of theoretical results -- the authors rely mostly on numerical results to judge the performance of integrators. A theorem comparing, e.g., truncation error of proposed samplers would greatly improve the strength of the paper. The current truncation error analysis is limited to specific cases and does not provide a general framework for comparing all proposed integrators. A more comprehensive theoretical analysis is needed to justify the design choices and provide a clear understanding of the trade-offs between different integrators.

**Weakness 2 : Incomplete / questionable baseline results**
- The authors claim if $B_t = 0$, conjugate integrator is equivalent to DDIM. But, if we see Figure 2 (a), FID for DDIM ($\lambda$-DDIM with $B_t = 0$) is too poor, compared to results in the original DDIM paper. For instance, in the original DDIM paper, DDIM achives FID 13.36 with NFE=10 while in Figure 2 (a), we see FID > 50. This discrepancy raises serious concerns about the correctness of the implementation or the experimental setup. The authors need to clarify why their DDIM baseline performs so poorly compared to the original paper.
- Result for EDM + pre-conditioning is missing in Figure 5. Why do the authors add pre-conditioning for their methods, but not for EDM? Is it because EDM + pre-conditioning out-performs the proposed integrators? For instance, EDM + pre-conditioning achieves 1.97 FID with NFE=35, which beats the best result in this paper, 2.11 FID with NFE=100. The absence of a direct comparison with EDM + preconditioning makes it difficult to assess the true performance of the proposed methods. The authors should include this baseline for a fair comparison.

**Weakness 3 : Incomplete evaluation**
- Results on higher-dimensional data is missing. I would like to see additional results on $\geq 512$ resolution images. The lack of results on high-resolution images limits the applicability of the proposed methods in real-world scenarios. The authors should demonstrate the scalability of their methods to higher resolutions.
- Results on conditional generation is missing. I would like to see additional results on e.g., class-conditional and text-conditional generation. The absence of results on conditional generation limits the scope of the paper. The authors should evaluate their methods on conditional generation tasks to demonstrate their versatility.

### Questions
- The relative behavior of stochastic (SPS-S, CSPS-S) and deterministic samplers (CSPS-D) is un-intuitive. Common knowledge is that deterministic samplers outperform stochastic samplers in the low-NFE regime, and vice versa in the high-NFE regime. But, we observe a reverse trend in Figure 5 bottom. Can the authors clarify why this happens?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
