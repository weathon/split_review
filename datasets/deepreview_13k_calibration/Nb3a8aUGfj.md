# Text2PDE: Latent Diffusion Models for Accessible Physics Simulation

- Decision: Accept
- Avg Score: 5.33
- Scores: 6, 5, 6, 6, 6, 3

## Abstract
Recent advances in deep learning have inspired numerous works on data-driven solutions to partial differential equation (PDE) problems. These neural PDE solvers can often be much faster than their numerical counterparts; however, each presents its unique limitations and generally balances training cost, numerical accuracy, and ease of applicability to different problem setups. To address these limitations, we introduce several methods to apply latent diffusion models to physics simulation. Firstly, we introduce a mesh autoencoder to compress arbitrarily discretized PDE data, allowing for efficient diffusion training across various physics. Furthermore, we investigate full spatio-temporal solution generation to mitigate autoregressive error accumulation. Lastly, we investigate conditioning on initial physical quantities, as well as conditioning solely on a text prompt to introduce text2PDE generation. We show that language can be a compact, interpretable, and accurate modality for generating physics simulations, paving the way for more usable and accessible PDE solvers. Through experiments on both uniform and structured grids, we show that the proposed approach is competitive with current neural PDE solvers in both accuracy and efficiency, with promising scaling behavior up to \(\sim\)3 billion parameters. By introducing a scalable, accurate, and usable physics simulator, we hope to bring neural PDE solvers closer to practical use.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
this paper introduce framework for text to simulation use latent diffusion models, enables condition on language, initial conditions. this work generate a entire trajectories for improved accuracy without error accumulation.

### Strengths
- apply latent diffusion models to physics simulation with mesh encoder/decoder provide a scalable solution. 
- a new text conditioned PDE simulation framework. 
- supporting both structured and unstructured grids, and shows promising results on different types of PDE problems

### Weaknesses
 -  it's unclear the benefits and why doing text-conditioned simulation generation
- I find paper's contribution is more on using latent diffusion for pde simulation, not the text to PDE generation.
-  it's unclear how the text conditioning is implemented and what specific aspects of the simulation it controls. For example, does the text influence initial conditions, boundary conditions, or the underlying PDE parameters? This lack of clarity makes it difficult to assess the true impact of the text conditioning.


### Questions
- what is re-solved trajectory referred to in line 394?
- why doing text-conditioned simulation generation, is the pde type pre-defined for each model? How important is the training data text caption?
- how does text-conditioning help the simulation results or they are dis-entangled.

### Soundness
2

### Presentation
2

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
The paper introduces a framework called TEXT2PDE, which employs text-conditioned latent diffusion models (LDMs) to model spatio-temporal PDE trajectories. The authors introduce a mesh autoencoder that can encode and decode physical fields on arbitrary meshes. Spatio-temporal trajectories are generated using a conditional denoising process of an LDM with the initial conditions and boundary conditions of the PDE imposed into the conditioning sequence of the denoising backbone. A main novelty is the introduction of text conditioning, by employing a pre-trained transformer encoder. The authors argue that using natural language as a conditioning modality can improve the interpretability and usability of neural PDE solvers.

### Strengths
1. Thanks to the encoding of arbitrary meshes, the authors are able to apply their method to complex geometries – an important use case for the application of PDEs.
1. The main strength of the paper is the introduction of text conditioning for generation of PDE trajectories. The idea is novel and opens up a new research direction.
However, it would be still interesting to see more specific motivating examples of where text conditioning could be useful in real-world use cases of PDE solvers.

### Weaknesses
1. The evaluations seem lacking when assessing the text conditioning capability of the Text2PDE model. Firstly, the initial and boundary conditions of the cylinder dataset can be entirely encoded using just three real numbers, making the expressiveness of natural language excessive for this case. Secondly, the smoke dataset appears to be a poor fit for text-based description, as the smoke plumes are too unconstrained and unstructured to be accurately captured by language. The initial conditions for the smoke dataset are generated from a mixture of Gaussians, which are inherently difficult to describe with natural language. The text prompts used for the smoke dataset seem to primarily capture the initial density distribution, which is then evolved by the PDE solver. This raises concerns that the model might be memorizing the initial condition rather than truly understanding the text prompt. (See also the question 1.)

2. In my opinion, evaluating text conditioning would require a new dataset with more regular shapes placed in general positions. The configurations should be rich enough to necessitate natural language for description, but constrained enough that a short text can accurately describe the image. Currently, it seems that the TEXT2PDE system is limited to using text conditioning to generate only the initial condition. This could be achieved more directly by combining text-to-image techniques and then running a standard (neural) PDE solver. The added benefit of using a combined system is not clear. It could be more interesting (and useful) if the PDE dynamics were also informed by natural language—perhaps through a text-encoded equation. The current approach does not clearly demonstrate the advantage of an end-to-end model over a decoupled approach.

### Questions
1. As the text prompts appear to accurately capture the first frame of the reference (as shown in Table 2 and Figure 4 in Appendix A), I wonder if the model is memorizing and retrieving the smoke plume from the training dataset that most closely matches the input. For the existing prompts, would it be possible to display the most similar first frame from the training set?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors introduce a new approach to physics simulations using latent diffusion models. Their method is anchored by (i) the use of mesh autoencoders, (ii) full spatio-temporal modeling to avoid autoregressive error accumulation, and (iii) conditioning on text prompts.

### Strengths
- Latent space modeling for physics simulations. By using latent diffusion models, the authors effectively compress and encode high-dimensional physics data into a lower-dimensional latent space. Such latent space approaches contribute to more adaptable and faster simulations, making it a powerful alternative to traditional numerical solvers. There is a surge of latent space PDE models, this paper fits well into this paradigm. The full spatio-temporal diffusion modeling conditioned on text prompts and the subsequent decoding stands out as unique modeling approach.

- Text prompts for simulation control. Text2pde is an interesting direction since it allows users to define simulation parameters or initial conditions using simple, interpretable text commands. The potential for language-based input makes physics simulations more accessible and generalizable. Yet it is not clear what is the difference to simple parameter modulation, the nice capturing of the initial condition is cool.

- Application to mesh-based dynamics.

### Weaknesses
 - Text2pde seems to be hard to scale to larger problems. To avoid confusion: scalability here refers to input representations. The mesh autoencoder is a good direction, yet the latent space is a latent grid, which if going to 3D is fundamentally limiting. Also for larger 2D grids, a tokenized representation might be preferable. Secondly, the generation of the full trajectory is storage intensive, and for 3D problems would result in a 4D tensor, which is computationally infeasible. Most turbulent problems, where neural surrogates might shine are 3D, presenting a drawback of the applicability of the method.
- Text conditioning in this framework seems to be a slightly sophisticated parameter conditioning / parameter modulation. The nice feature so far is the generation of the initial mesh, initial condition. It would greatly help to make these differences clearer. Further the text prompt part needs to be adapted for each problem individually. It should be clarified how the text part can maybe be used across settings? Is this even possible?

### Questions
- Autoregressive vs entire solutions. It is not clear whether producing an entire solution trajectory is really beneficial. First of all it doesn’t scale to 3D problems or larger 2D problems. Secondly, it might be unphysical. Do the authors have insights on this?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Very new paper. I support this because it actually works, I appreciate the authors working! Just like language model for catalyst. But I just do not see why people need this as they need for catalyst-gpt. The authors know fluid, they do not need this even they can make this fluid-gpt. For people do not know fluid, why they need it?

### Strengths
It is first time people to get-like fluid sequence generation, to combine llm with diffusion is good.

### Weaknesses
The motivation is lacking. The flow simulation is not physical. The authors should write down more about when, who will need this method to do what. And the flow past cylinder data seems under-resolved. The mesh is too coarse, can we make it finer?

### Questions
The author should write down more about when, who will need this method to do what. And the flow past cylinder data seems under-resolved. The mesh is too coarse, can we make it finer?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a surrogate neural network model that solves PDE problems. The authors claim innovations in three parts: mesh en/decoder, latent physics solver, and conditioning. The mesh en/decoder unifies differently discretized solution data achieved from various numerical solvers. Unlike an autoregressive model, the latent physics solver utilizes a diffusion model and predicts a full spatiotemporal solution. For the conditioning, two mechanisms, i.e., state-based and text-based methods, are proposed.

### Strengths
Under the aim of developing a surrogate neural PDE solver, the paper claims three major novelties (also with their strengths) of the proposed model.

1. En/decoding PDE data via a uniform spatiotemporal latent grid: Regardless of discretization, the PDE data is first encoded into the uniform grid via a weighted sum using a learned parameterized kernel. Its architecture unification is beneficial, and thanks to the benefit, the conventional CNN can outperform GNN and Neural Fields in training an autoencoder for irregular data.

2. Latent diffusion model for entire solution trajectory prediction: Instead of a state prediction of the autoregressive model, the proposed neural PDE solver aims to predict the trajectory given initial and boundary conditions. This generative model can mitigate error accumulation, and the work compares with other models.

3. Text conditioning: In addition to the traditional physics-state initial and boundary conditions, the paper proposes to use natural language as a means of conditioning. The authors claim that this can be a promising direction for PDE simulators.

Overall, with the combination of these novelties, the paper claims their surrogate PDE solver outperforms the other models such as GINO, OFormer, FNO, ACDM, etc.

Additionally, thanks to the accompanying codes, the results should be reproducible (although I did not run the codes myself).

---

***During the discussion,*** the authors clarified my concerns; thus I raised my score to 6 from 5.

### Weaknesses
As the title "text2pde" stands for, the paper proposes a text-based conditioning for PDE. Although it is an interesting direction to investigate, the practical benefit of the current model is not fully convincing to me. If I am not wrong, the text-based conditioning of the proposed method eventually relies on a set of extracted values that are necessary to set up the initial condition, and this is only for conditioning a single initial frame. In my view, this can be easily and more precisely defined with a script-based (or template-based) initialization. Arguably, the text-based approach may rather be an ambiguous means to use in this context. Moreover, this part looks independent of the solver; it tackles how to generate an image (i.e., a PDE state in this context) from a text, which looks closer to text2image rather than text2pde.

The validation of the proposed solver could be further improved. Only two examples of N.-S. equations were investigated. The proposed entire-trajectory prediction was only evaluated for 25 steps in the cylinder flow case with low turbulence, which is relatively less complex, and 48 steps in the buoyancy-driven flow. Further experiments for the multi-step trajectory prediction would improve the validation.

### Questions
The example of Cylinder Flow describes that the physical variables are velocity and pressure. Do the reported L1 Loss values take into account both variables? If so, the errors of both variables should be discussed more thoroughly.

Similarly, it would be worth having further clarification of the error for two variables (velocity and density) in the Buoyancy-driven Flow example.

In Buoyancy-driven Flow, the samples vary with not only initial conditions but also buoyancy factors. Does the model get conditioned with the buoyancy factor? I guess not. Then, the trajectories (evolved with different buoyancy factors) represent somewhat different physics. In this case, I am not sure how the model has learned the underlying physics.

It would be valuable to see how the radius of a spatio-temporal ball affects the model performance.

It would be helpful to clarify how to define/train the kernel $\kappa(\cdot)$.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work presents a more accessible physics simulation by introducing the language model so that the physics solver can be interacted by using the test, called text2PDE. The proposed method is verified cylinder flow and buoyancy-driven flow although they cannot demonstrate enough the claimed effect.

### Strengths
1. The developed framework encodes and decodes arbitrary PDE data into a latent space to generate unstructured physics solutions.
2. The language model is applied in the framework to make the PDE solver more accessible.
3. The paper applies two experiments to demonstrate the superior performance of the proposed method.

### Weaknesses
1. The reviewer raises doubts about the novelty and contribution of the work, seemingly only using the encoding of the language model as a condition to generate solutions of PDEs.
2. Why do the two experiments adopt different baselines and lack baselines such as FNO for cylinder flow?
3. From line 047 to 050, while this statement may seem obvious, it's not a scientific issue. It is necessary to have physics and numerical knowledge to build PDE solvers. At the same time, approaches based on FNO, DeepOnet and similar numerically-driven methods can learn accurate PDE solvers without requiring physics knowledge.
4. From line 053, this work deviates from the challenges described above, and there are concerns about potential overclaiming. Based on the author's two experiments, the proposed model only works in specific PDEs, spatiotemporal dimensions, and simple scenarios where the required physics knowledge is quite basic. In other words, the authors failed to address a crucial question: for complex PDE systems, how to represent the system using language, when mathematical formulas are clearly more suitable, while it is the main challenge the reviewer understand from the previous paragraph.
5. Spatial and temporal resolution is crucial for PDE solvers. How does this work handle different spatial resolutions? Specifically, how does this method distinguish between initial conditions with different resolutions within the same system?
6. Could you provide more details about the autoencoder in Sec. 3.1? This part is quite abstract and difficult for readers to understand intuitively. Please briefly explain the autoencoder's architecture, input/output structure, and training methodology. Additionally, during the diffusion model training, is the encoder trained simultaneously or are its parameters fixed?
7. In line 235, the decoder appears to be CNN-based, which imposes constraints on the spatial dimensions of the output solutions. Furthermore, interpolation operations can lead to inaccuracies in the results, even when solutions on regular grids are accurate.
8. In the method section, the authors have placed too many crucial details in the appendix, like Appendix C.2, B.1, B.2, D, making it impossible to understand the method without referring to the appendix.
9. The selected parameters for cylinder flow are overly simplistic, only covering laminar flow cases. Generally, the Kármán vortex street phenomenon is more common in cylinder flows, yet the authors did not include this scenario.
10. All data used is 2D, and it's unclear whether this model can handle 1D and 3D experiments. The lack of such experiments significantly reduces the persuasiveness of the work.
11. Without knowing the scale of the data, reporting only L1 loss makes evaluation difficult. Could authors additionally report the relative L2 loss?
12. As the authors acknowledge, the inference time of diffusion models limits their application, which is confirmed by the statistical results. The authors should consider using inference acceleration methods such as DDIM and verify that the method remains effective under DDIM sampling.

### Questions
1. The reviewer has some doubts about the selected generative model. For such prediction and simulation tasks, diffusion models are not always effective due to their SDE features. Flow matching, which is based on ODEs, appears more suitable for PDE solvers. Could the authors discuss the application of both models for PDE solvers and explain why they chose diffusion models over flow matching?
2. In line 229, "we find that GANs and perceptual guidance can in certain cases improve reconstruction performance, but for simplicity, we omit them in our main results." The author said GANs can improve the performance, but why you do not apply GANs?
3. In Figure 5, the middle two figures do not show turbulent flow, making this characterization inaccurate. Specifically, the second figure clearly shows laminar wake flow, and while the third figure shows vortices, it has not yet reached turbulent conditions.

### Soundness
3

### Presentation
2

### Contribution
2
