# SimDiffPDE: Simple Diffusion Baselines for Solving Partial Differential Equations

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5

## Abstract
We showcase good capabilities of the plain diffusion model with Transformers (SimDiffPDE) for general partial differential equations (PDEs) solving from various aspects, namely simplicity in model structure, scalability in model size, flexibility in training paradigm, and universality between different PDEs. Specifically, SimDiffPDE reformulates PDE-solving problems as the image-to-image translation problem, and employs plain and non-hierarchical diffusion model with Transformer to generate the solutions conditioned on the initial states/parameters of PDEs. We further propose a multi-scale noise to explicitly guide the diffusion model in capturing information of different frequencies within the solution domain of PDEs. SimDiffPDE achieves a remarkable improvement of +51.4% on the challenging Navier-Stokes equations. In benchmark tests for solving PDEs, such as Darcy Flow, Airfoil, and Pipe for fluid dynamics, as well as Plasticity and Elasticity for solid mechanics, our SimDiffPDE-B achieves significant relative improvements of +21.1%, +11.3%, +15.2%, +25.0%, and +23.4%, respectively. Models and code shall be released upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents SimDiffPDE, a diffusion model with Transformers for solving various partial differential equations (PDEs). It highlights the model's simplicity, scalability, and flexibility, reformulating PDE-solving as an image-to-image translation problem. The model employs a multi-scale noise strategy to enhance information capture across different frequencies. SimDiffPDE achieves a +51.4% improvement on the Navier-Stokes equations and notable relative improvements on benchmarks for fluid dynamics and solid mechanics

### Strengths
1.The paper employs a multi-scale noise strategy that enhances the capabilities of diffusion models in PDE solving. 
2.SimDiffPDE achieving consistent top results across multiple datasets and grid types with an average performance improvement of 22.0%.

### Weaknesses
1.In Algorithm 1, the multi-scale noise is actually a linear combination of interpolations across standard Gaussian noise at different spatial scales and hierarchical levels. This linear combination is then subjected to a standard deviation constraint, which means the resulting multi-scale noise does not adhere to a standard Gaussian distribution or even to a Gaussian distribution at all. This raises a question: does the sampling process start with standard Gaussian noise or multi-scale noise? If it begins with standard Gaussian noise, then the final distribution of the noise in the forward process does not match the initial distribution in the sampling process. Additionally, as multi-scale noise is not Gaussian, there may not even be a closed-form expression for q(x_t|x_0). Could you provide an explanation for this? On the other hand, if it starts with multi-scale noise, how can we ensure that the final distribution of the noise in the forward process aligns with the initial distribution in the sampling process?
2.The paper should include a curve showing error propagation over time to illustrate the model's performance.
3.The paper lacks a comparison with traditional methods at different resolutions. Specifically, it is unclear how the proposed method scales compared to established numerical solvers as the grid resolution increases, which is a critical aspect for practical PDE solving.
4.It should include a comparison of training time, inference time, and model parameter counts for different baselines. The absence of this information makes it difficult to assess the practical trade-offs of the proposed method compared to existing approaches.

### Questions
1.Regarding Test-Time Estimate, the paper suggests that, compared to simply averaging ensemble predictions, multiple predictions should ideally converge under a certain scale and shift parameter. This assumption might need more theoretical explanation and justification. Furthermore, the process of finding the optimal scale and shift introduces an iterative optimization problem. While regularization terms have been added, is this optimization straightforward to solve? Is it time-consuming? And does it offer a significant advantage over simple aggregation averaging in the final results? A comparison would be appreciated.
 
2.For the comparison of experimental results, could you highlight the differences in inference time between the diffusion model and other deterministic surrogate models? Additionally, please specify which sampling algorithm was used.

3.The experiment should also compare the model with other high-performing models on the Navier-Stokes equations, such as DeepONet, PeRCNN, PDERefiner, LI, and TSM.

4.The paper currently uses statistical metrics alone; however, for NS problems, it would be more appropriate to introduce physically meaningful metrics, such as probability density functions (PDF) and energy spectrum curve, to evaluate the model's performance.

5.For NS problems, does the model apply only to simple datasets like those used by Li et al.? Could the Kolmogorov flow generated by JAX-CFD (Kochkov et al.) be used for long-term prediction? Error propagation plots, correlation curves, should also be used to demonstrate the model's superiority in this context. Once the model is trained, can it adapt to changes in certain conditions, such as Reynolds number and external force terms?

6.Additionally, can the proposed model be applied to 3D problems?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes SimDiffPDE, as a simple diffusion model for solving PDEs. The main innovations include multi-scale noise and test time ensemble, but I have some questions about this. The results show that the SimDiffPDE performs very well on various benchmarks.

### Strengths
1. The results show that this method is quite valid in diverse PDE benchmarks.
2. The multiscale noise is reasonable, as the Gaussian noise is added to the ground truth PDEs, the low-frequency components may be phased out as the noise is added independently on pixels/meshes.

### Weaknesses
1. In my opinion, solving PDEs is a partial theoretical problem, and this work is a bit like directly using the diffusion model to solve PDEs. I think it is necessary to explain the reason for this through theory.

2. I have some problems with training and infer time noise, you use multiscale noise as the training, can you certify that the multiscale noise has the same properties as simple Gaussian noise? Such as after T steps you could obtain a standard Gaussian $\mathcal{N}(0, I)$.

3. About the test-time ensemble, can I regard that you got better results by doing additional calculations after the output? I'm not sure that's a fair comparison to the alternatives. Furthermore, can you explain more about this ensemble setting?

4. There is a typo in equation 3. Is there a problem with the subscript of $y$.

### Questions
1. I have some problems with training and infer time noise, you use multiscale noise as the training, can you certify that the multiscale noise has the same properties as simple Gaussian noise? Such as after T steps you could obtain a standard Gaussian $\mathcal{N}(0, I)$.
2. About the test-time ensemble, can I regard that you got better results by doing additional calculations after the output? I'm not sure that's a fair comparison to the alternatives. Furthermore, can you explain more about this ensemble setting?
3. There is a typo in equation 3. Is there a problem with the subscript of $y$.

I may not fully understand some key points, please answer them for me, I will re-evaluate the article after understanding.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to use a plain diffusion model for PDE solving. Specifically, this paper formulates the PDE-solving problem as the image-to-image translation problem, and a conditional diffusion model can thus be applied. This paper also proposes a multi-scale noise to capture information of different frequencies better. The experiments show the superior performance of SimDiffPDE over previous works.

### Strengths
The paper is easy to read. The proposed method is quite simple and seems effective.

### Weaknesses
- The proposed method is a direct application of common diffusion models to PDE data. Except for the multi-scale noise, there are no technical contributions.
- There is no comparison of the inference efficiency between SimDiffPDE and the baselines. Considering that a test-time ensemble method is employed, the inference overhead of SimDiffPDE should be much larger than baselines.
- The motivation of utilize a diffusion model for PDE solving is not clear. In Line 307-308, the authors claim that "different initial noises $y_t$ tcan lead to varying solutions, which allows SimDiffPDE to simulate the nonlinear dynamics of PDEs". However, based on my understanding, the datasets included in this paper does not exhibit any inherent stochasticity, and the mapping from the initial values/PDE parameters to the solution should be deterministic rather than stochastic. Therefore, it would be beneficial to compare the performance of the model to a *plain Transformer model* utilizing exactly the same model architecture as SimDiffPDE, but with the same input as other baselines rather than random noise, to verify that the *nonlinear dynamics of PDEs* do propose significant challenges to neural networks so that a diffusion model must be applied to tackle the fitting challenges.

- The flexibility to various resolutions is not well explained. How is the model able to handle different resolutions? Do you train a single model on a specific resolution and test it on other resolutions or train different models for different resolutions? For either method, what adaptation do you make to the model to handle different input resolutions?
- This paper tries to formulate the PDE-solving process as a image-to-image translation task. However, this paper also include tasks with point cloud data as input, and more general PDE solving tasks also involve irregular meshes rather than regular grids only. This paper provides no explanation as to the implementation details on the Elasticity benchmark. Is the input data reorganized into regular grids? If so, it cannot be claimed that SimDiffPDE can handle irregular and unstructured data. If not, then such kind of data structure contradicts to your claim that the PDE solving process is an image-to-image translation problem.

### Questions
See weaknesses.

### Soundness
2

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
4

### Summary
The paper moves from common learning-based PDE solvers, which are deterministic, to propose SimDiffPDE, which is a generative approach based on diffusion. Diffusion models can guarantee more robust and better generalising pipelines, addressing a major shortcoming of most learning-based PDEs, which require varied, large and descriptive datasets to have well-generalising pipelines. SimDiffPDE is problem agnostic, which means it does not require domain-specific knowledge. 

SimDiffPDE is tested over three different geometry types (point clouds, structured meshes and regular grids), demonstrating to be a flexible model, and over 6 benchmarks, reporting state-of-the-art results, especially for larger versions of SimDiffPDE (L and XL).

SimDiffPDE, while not being the first diffusion-based approach to PDEs, is the first one that uses a Transformer architecture and introduces the concept of multi-scale noise to corrupt data in the forward diffusion process.

### Strengths
The key strength of this paper are the results presented. SimDiffPDE beats many architectures over a diverse range of tasks and data formats. I feel results are not only good, but also very well presented and corroborated by thorough examples. All the tables were neat and nicely explained.

The overall pipeline is simple, which is always a great thing to have.

Fig. 8 is interesting and useful - I would move it in the main body instead. Make sure to either add labels (1), (2) and (3) on the image or to reference them differently (top row, middle row, bottom row). 

The approach of using diffusion for PDEs, while not entirely new, is also one of the earliest examples in the literature.

The claims of simplicity, feasibility and flexibility of the pipeline are well addressed in the text.

I am happy to increase my score in case the questions and concerns raised in the weaknesses sections are addressed.

### Weaknesses
I am not convinced about the rigorousness of the contextualisation of this paper. The authors do a good job at reviewing the state of the art of PDE solvers, but very few references on diffusion models are included. Most notably, DiffusionPDE by Huang et al., 2024, also tackles the same problem (PDE solution) with diffusion, but it is not mentioned. I am unsure whether the authors thoroughly reviewed the relevant literature on the matter. The paper would benefit from a review of such methods, too, otherwise the reader might be biased in thinking that this is the first approach that uses diffusion for PDEs.

I am also not convinced about the novelty of the contribution. DiffSimPDE is an application of a diffusion architecture already existing to a specific problem. The main contribution would be the first example of PDE solution via Transformer-based diffusion (and not the first example via diffusion in general) and the multi-scale noise scheduler. I have two issues with the multi-scale noise:

1) I feel that the issue of grasping features at multiple scales is not really an issue, since a U-Net-based diffusion already does that for you (see for example Saxena et al., 2024, that introduce DDVM for optical flow - optical flow is a quantity that is historically regressed by taking into account multiple scales, since objects move at different distances from the camera. DDVM does not require an explicit pyramidal structure that takes care of the multiple scales of optical flow since U-Net is in itself multiscale). The novelty of the multi-scale gaussian noiseapproach might then be limited to this specific architecture in the diffusion space. 

2) I am not convinced by Remarks 3.3.1 and 3.3.2 and Fig. 4. How can noise not "destroy" data?. If noise is added following Eq. 1, how is it possible that based on the high/low frequency patterns in data some inputs can be degraded and some cannot? Also, from Fig. 4, it seems to me that 100 steps of multi-scale noise still fails for columns 2 and 3, since no Gaussian noise can be seen?

I am unsure whether the good results stem from an original, creative approach to the problem or just because diffusion in general works great in a lot of problems and it's an easy win over deterministic approaches.

In general, I find the writing style of the manuscript rather unrefined. I understand that results are promising, but I feel the presentation is not up to standard and the quality of the results suffer from it.  For example:

- a better definition of $x$ and $y$ for the problem setting is required (e.g. does $x$ contain multiple "snapshots" of the PDEover time?).
- $x_g$ and $x_u$ are introduced but not explained.
- the whole paper uses “Guassian” 27 times and “Gaussian” 28 times
- grammar: - The two designed…improves
- line 104: inconsistency - you use SimDiffPDE-X, but in Fig 1. You use X-SimDiffPDE
- line 107: sentence structure - SimDiffPDE showcases the good feasibility to various PDE equations —> SimDiffPDE showcases good feasibility for various PDE equations
-line 140: grammar: Neural operators establish instead of establishes
-line 424: conducted instead of conduct

### Questions
Line 86: “By adding multi-scale noise in the forward process, are more explicitly required to learn to denies multi-scale noise to ..” Isn’t multi-scale in diffusion normally handled via the architecture, e.g. a U-Net has in itself the concept of multi-scale? Why not using that over the transformer block?

Line 102: “To be more specific, one can easily control the model size by stacking different number of diffusion transformer layers and increase or decrease feature dimensions” - how does that guarantee scalability with the input size?

Line 178: what’s $x_g$, $x_u$ and $y$, in practice? What’s geometric inputs and observed quantities? Inputs and outputs feel too generic. 

Line 180: do $N$ mesh points represent a square domain of $\sqrt{N} \times \sqrt{N}$? The problem seems to be 2D in Figure 2 but 1D from the notation in line.

Figure 6: I feel scalability refers also to the ability of the model to handle larger input size. Could you provide more insight in terms of number of parameters or speed of SimDiffPDE to have a better feel of how it compares? How does the computational complexity of the model scales with input size?

### Soundness
3

### Presentation
1

### Contribution
2
