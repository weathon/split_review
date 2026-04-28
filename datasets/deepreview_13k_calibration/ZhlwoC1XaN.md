# From Zero to Turbulence: Generative Modeling for 3D Flow Simulation

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 5, 8, 8

## Abstract
\looseness=-1
  Simulations of turbulent flows in 3D are one of the most expensive simulations in \CFD{}.
  Many works have been written on surrogate models to replace numerical solvers for fluid flows with faster, learned, autoregressive models.
  However, the intricacies of turbulence in three dimensions necessitate training these models with very small time steps, while generating realistic flow states requires either long roll-outs with many steps and significant error accumulation or starting from a known, realistic flow state—something we aimed to avoid in the first place.
  Instead, we propose to approach turbulent flow simulation as a generative task directly learning the manifold of all possible turbulent flow states without relying on any initial flow state.
  For our experiments, we introduce a challenging 3D turbulence dataset of high-resolution flows and detailed vortex structures caused by various objects and derive two novel sample evaluation metrics for turbulent flows.
  On this dataset, we show that our generative model captures the distribution of turbulent flows caused by unseen objects and generates high-quality, realistic samples amenable for downstream applications without access to any initial state.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a novel modeling method of turbulence flow based on generative models. It consists in learning the distribution of turbulent flow states without the need to be tied to the initial flow state. The proposed model is augmented with Dirichlet boundary conditions to learn physically meaningful turbulent flow representations.

### Strengths
1/ Originality and significance:
Turbulence modelling is a crucial task in many engineering applications. However, the problem is still open and challenging. In the litterature several methods have been proposed to tackle the problem from different points of views but the proposed solutions are either expensive/ intractable in practice or are very complex to set. In this work, the originality of the work is in its simplicity of usability while providing good turbulent flow results in a raisonnable time. Hence, the proposed model is scalable.
Moreover, it is based on a generative model (diffusion model  DDPM) that has achieved significant leaps in a wide spectrum of applications. Augmenting DDPM with physics constraints like Dirichlet enables generating 3D turbulent flows of good quality. The strength of the proposed model is related to the fact it learns a manifold of turbulent flow states without being tied to the initial flow state.

2/ Quality:
The methodology of the proposed work is rigorous. A targeted 3D turbulent flow dataset is generated specifically to assess the capabilities of the proposed generative turbulent flow model in the appropriate conditions. Moreover, data and task dependent metrics are introduced to evaluate to the model in physical way.

3/ Clarity:
The paper is very clear and simple to follow. It is well structured.

### Weaknesses
The proposed work lacks of ablation studies and baselines both quantitative and qualitative analysis. Diving into the different blocks of the architecture to understand their impact/contribution is of great importance and can give more insights. Especially that the proposed model is a combination of sophisticated blocks: DDPM, U-NET, transformers. One would like to understand how these blocks cohabitate to generate good quality of turbulent flow.

Figure and the details on the architecture are not sufficient.

Invariance to meshing / discretization scheme has not been discussed.

### Questions
1/ Have you tested the proposed model on unstructured data like graph-meshes and cloud of points ? to what extent, it is applicable ? turbulent flow are irregular, regular grids can hide some patterns

2/ What are the capabilities of the proposed model at the boundary layers ? do you have any metrics on the surface of the geometry ? (most challenging part)

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a generative model based on a diffusion process for one-shot generation of solutions to turbolent flows.
The approach is remarkable in his simplicity and potential applicability.

### Strengths
The approach of using a one-shot generation for solutions to turbolent flow is quite remarkable, as well as the fact that results seem to be rather impressive on such a small data regime.
The experiments show training on 27 airfoils, 9 for val and 9 for testing. It is indeed surprising the model can generalize in such a small regime, perhaps indicative of the fact that the model can pool information across all cells/volumes, thus perhaps capturing somehow the intrinsic physics of the problem.

### Weaknesses
There is no mention of releasing the data-set and the source-code. This is a major issue for reproducibility.
The size of the data-set is also surprisingly small. While it's quite remarkable the model seem to capture the essence of the problem is such a small data-regime, I am also quite puzzled by that.
It would be great to scale to deep-learning type of sample size (10^5 samples - of course what's a sample in the CFD case is a bit up to interpretation).

I also agree the limitations of A#F are palpable: especially the lack of equivariance and the geometry limitations are quite important.

Of course this also means the architecture has much to grow, once such limitations are addressed, but this also points to the fact this is likely an initial work, and possibly not ready yet for primetime publishing in top venue like iClear.

Finally, the speedup is somewhat disappointing: the nominal 30x achieved is really not so important when considering that A100 vs Xeon-2630 is probably already 50x faster (depending on workloads).

### Questions
Q1: plans to release code and database
Q2: plans to scale up experiments
Q3: why does it generalize in such a small data regime? any thoughts?

### Soundness
3 good

### Presentation
4 excellent

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
Methods
- The paper focuses on the topic of 3D turbulence generation, by modeling it as a generative task to overcome the roll-out dilemma of autoregressive models.
- The paper derives an appropriate generative diffusion model and the discretization on 3d domain for the 3D turbulence generation. Dirichlet conditions are handled in the model. Cell types are handled via learned cell type embeddings.
- The network is based on denoising diffusion probabilistic models (DDPMs). The network architecture employed in the diffusion model extends the U-Net framework into the 3D domain, incorporates a transformer (after 4 level of down-sampling) to enable global communication across the simulation domain.

Experiments
- The paper provides a new 3D turbulence dataset, consisting of 45 simulations of an incompressible flow in 192 × 48 × 48 grid cells.
- 9 out of 45 samples from the dataset are used to validate the method. From the results, the proposed method is able to generate realistic 3D-flow samples that can capture the turbulent flows caused by unseen objects.
- The paper proposes metrics for evaluating the quality of the generated flows by utilizing properties of fluids, including turbulent kinetic energy, marginal velocity, vorticity and pressure distribution, and the location of the strongest turbulent vortices.
- The method is compared with two autoregressive models (Turbulent Flow Net and DilResNet) and each with two different settings to convert them to generative models, showing good performance compared with them.

### Strengths
- This paper leverages generative diffusion models, which are more commonly associated with image and video tasks, for turbulence simulations, providing a new approach for 3D turbulence generation.
- In the experiment section, the metrics are well designed to capture the characteristics of fluids, and the proposed method shows good performance in terms of both accuracy and runtime.
- The paper gives a good discussion regarding the challenges of employing autoregressive models for 3D turbulence generation.
- In addition to the method, the paper introduces a new 3D turbulence dataset that can benefit further research in the field of turbulence generation.

### Weaknesses
 - It would be good (but not necessary in this paper) to see how the method performs on learning and generating more complex fluid phenomena, such as fluid interactions with air, and generating classical fluid phenomena like the Karman vortex street.


### Questions
- In Fig5 and Fig6, what’s the value that is visualized? the norm of velocity? pressure?
- Would it help to pre-processing the data, e.g. rotations, flips to augment the dataset?
- Is it relatively easy or hard to apply this method to more complex turbulent generation, e.g., with fluid–solid interaction? 
- The grid size used for generating dataset is 192 × 48 × 48. In fluid simulations, larger grid size are often used to achieve higher accuracy. Is this grid size chosen due to performance limitation of the CFD solver?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper concerns simulation of 3D turbulent flows and replacing direct numerical solvers with autoregressive, learned models. The authors argue that turbulent flows are substantially harder to model properly in 3D than in the 2D case which many papers previously have targeted. They then propose a generative model for flow simulation that is independent of the initial state but still able to capture the distribution of fluid states with high-resolution in complicated settings with various objects affecting the flow.

### Strengths
- well-written and clearly presented paper
- important problem and method that can potentially have impact
- targets 3D instead of 2D and argues that flow simulations in this case is substantially harder
- works in challenging situations with boundary effects and objects influencing the flow

### Weaknesses
 - while the paper presents a new method that is different from the generative flow methods in the literature, it is quite related to previous approaches and thus provide a somewhat incremental - but still important - contribution

Specifically, the claim that the paper circumvents the "roll-out dilemma of autoregressive models" by modeling the marginal distribution  E_t[p((u, p)t | u0, p0)] warrants further scrutiny. The removal of the initial state dependency and the expectation in the subsequent paragraph requires a more detailed explanation. While the stochastic process perspective is acknowledged, the precise manner in which this work deviates from existing approaches in terms of handling the initial state and the expectation needs clarification. The current presentation lacks sufficient detail to fully understand the novelty in this aspect.

Minor points:
- some parts need proofreading, e.g. "We conclude that many use cases can be solved by independent snapshots of possible flow states as well as by a classical numerical simulation. We conclude that many use cases can be solved by independent snapshots of possible flow states just as well as with a classical numerical simulation."

### Questions
- I think it is a little unclear that you write "Thus, we propose to circumvent the roll-out dilemma of autoregressive models by modeling the marginal distribution E_t[p((u, p)t | u0, p0)] directly, capturing the distribution of turbulent flows with a generative model.", but then in the next paragraph remove the dependence on the initial state and remove the expectation. As far as I can see, the stochastic process perspective has been used previously (e.g. ref Yang and Sommer), and what is done here is removing the condition on the initial state. I'm note sure where the expectation comes in.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
