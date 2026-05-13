# PINNsFormer: A Transformer-Based Framework For Physics-Informed Neural Networks

- Decision: Accept
- Scores: 8, 8, 5, 5

## Abstract
Physics-Informed Neural Networks (PINNs) have emerged as a promising deep learning framework for approximating numerical solutions to partial differential equations (PDEs). However, conventional PINNs, relying on multilayer perceptrons (MLP), neglect the crucial temporal dependencies inherent in practical physics systems and thus fail to propagate the initial condition constraints globally and accurately capture the true solutions under various scenarios. In this paper, we introduce a novel Transformer-based framework, termed \ourmethod, designed to address this limitation. \ourmethod can accurately approximate PDE solutions by utilizing multi-head attention mechanisms to capture temporal dependencies. \ourmethod transforms point-wise inputs into pseudo sequences and replaces point-wise PINNs loss with a sequential loss. Additionally, it incorporates a novel activation function, \texttt{Wavelet}, which anticipates Fourier decomposition through deep neural networks. Empirical results demonstrate that \ourmethod achieves superior generalization ability and accuracy across various scenarios, including PINNs failure modes and high-dimensional PDEs. Moreover, \ourmethod offers flexibility in integrating existing learning schemes for PINNs, further enhancing its performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes PINNsFormer, a novel Transformer-based framework for Physics-Informed Neural Networks (PINNs). PINNs are used to numerically solve partial differential equations (PDEs) but struggle to capture temporal dependencies inherent in physics systems. PINNsFormer addresses this by generating pseudo input sequences from pointwise inputs and using a Transformer encoder-decoder architecture to model temporal dependencies. The main contributions are: 1) A new framework called PINNsFormer that equips PINNs with the ability to capture temporal dependencies through generated pseudo sequences and Transformer architecture. 2) A novel activation function called Wavelet designed to anticipate Fourier decomposition. 3) Extensive experiments showing PINNsFormer outperforms PINNs on problems involving failure modes and high-dimensional PDEs. 4) Demonstration of flexibility to incorporate PINNs optimization schemes for enhanced performance.

### Strengths
1. **Novelty**: This is the first work I'm aware of that integrates Transformers with PINNs to capture temporal dependencies,  which is a novel and promising direction. Adapting Transformers designed for sequences to point-wise PINNs is non-trivial, thus the innovations in pseudo-sequence generation and loss formulation are important contributions.

2. **Contributions**: The results on problems like convection and 1D-reaction demonstrate clear benefits in preventing temporal propagation failures that cripple vanilla PINNs. In addition, this work shows that modeling inter-timestep dependencies appears highly effective in maintaining accuracy across the domain rather than just near initial conditions.

3. **Methodology**: The model components are well-motivated - the pseudo-sequence generation and Transformer encoding seem natural yet powerful ways to incorporate temporal modeling into PINNs.

4. **Writing**: The paper is very clearly written, laying out both the background and proposed methodology comprehensively.

### Weaknesses
1. The lack of published code or detailed hyperparameters makes reproducibility difficult. Providing an implementation would strengthen the paper's contributions.

2. While the overall approach is promising, some ablation studies would help determine the impact of different components like the pseudo-sequence generation and Wavelet activation. Specifically, the sensitivity of the model to the number of pseudo-sequence points ($k$) and the time discretization ($\Delta t$) should be analyzed.

3. Since PINNs are notoriously slow in training, the computational overhead of PINNsFormer could be prohibitive for some large-scale applications. Analysis of model complexity and efficiency could help elucidate this issue. A more detailed breakdown of the computational costs associated with the Transformer architecture and the pseudo-sequence generation would be valuable, including memory requirements.

4. The reliance on introducing a discrete timestep risks undermining the automatic differentiation advantage of PINNs. Justification for this design choice could be expanded. The impact of this discretization on the accuracy of the gradients and the overall solution should be more thoroughly discussed, especially considering how it might affect the convergence of the optimization process.

### Questions
1. One major advantage of PINNs is that, it leverages automatic differentiation rather than relying on finite difference approximations. On the other hand, the use of discrete pseudo-sequences means temporal dependencies are modeled in the fashion of finite difference approximations rather than pure automatic differentiation. Would it create any difficulties in picking parameters for this differentiation (e.g., the Δt)? 

A relevant thought: The impact of the timestep granularity Δt seems worth further analysis. Is there a study on model sensitivity to this parameter? Does the performance degrade if Δt is too small or large? Are there any guidelines for setting Δt?

2. It may be worth trying the causal-attention transformers (decoder-based, e.g. LLM) instead of the encoder-decoder architecture. It does not seem to have particular reasons to adopt current sequence-to-sequence architecture.

3. Other sampling schemes may also play an important role [1], especially for mitigating the temporal propagation failure in PINNs. Since PINNFormer relies on discretization on temporal dimensions, I am curious how PINNFormer can adapt to non-fixed sampling. I believe the transformer architectures have such flexibility.

[1] Daw, Arka & Bu, Jie & Wang, Sifan & Perdikaris, Paris & Karpatne, Anuj. (2022). Rethinking the Importance of Sampling in Physics-informed Neural Networks. 10.48550/arXiv.2207.02338.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The manuscript describes a novel architecture for PINNs where a sequence with  even time steps is created.. This forms a sequence that can be used as an input to a transformer. The first layer of the neural network has a special "wavelet" non-linearity that can be seen as a spectral type of embedding of the data, with trainable parameters for the amplitudes and the frequency. An additional projection is made before the encoder and decoder. and the final output is generated with fully connected layer.

An attention mechanism is trained to produce the function value at   $ \hat u( x , t_i + k \Delta t )$ from the values   $ \\{ \\hat u( x , t_i + j \Delta t ) \\}_{j\in \\{1,..,k-1 \\}} $ 

The described architecture is tested against a set of baselines with impressive results.

### Strengths
Impressive results.  Clear representation.

### Weaknesses
The system is using a time discretised set of function values to predict the next time step. This reminds me of the finite difference method, In this case the stencil is 100 elements long, so the optimum stencil would have a very high order in accuracy. 

The reason why very large stencils are not used is that these bear a computational cost, and the same happens in using attention, although most of the computing is parallel.

Now the manuscript does not provide a baseline using a normal, discrete PDE solver, of course,  on the par with the  computational load that the attention mechanism is requiring . Of course, having an analytical, although complicated, solution for a problem has its advantages compared to a set of discrete nodal values.

I would like that the authors would address this in their submission for better rating.

### Questions
See the weakness part.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces PINNsFormer, a novel transformer-based framework for Physics-Informed Neural Networks (PINNs) to approximate solutions to partial differential equations (PDEs). PINNsFormer addresses the limitation of conventional PINNs in neglecting temporal dependencies within PDEs. Comprehensive experiments show PINNsFormer outperforms PINNs and variants in addressing failure modes and high-dimensional PDEs.

### Strengths
PINNsFormer addresses a key limitation of PINNs by explicitly learning temporal dependencies, crucial for real-world physics systems. This significantly improves PINNs' generalization ability.

The proposed pseudo sequence representation and transformer architecture are clever approaches to adapt PINNs for sequential models.

Ablation studies provide insights into design choices and integration of existing PINNs schemes.

### Weaknesses
While the Wavelet activation function is theoretically justified to approximate arbitrary solutions, its advantages over other activations like ReLU, sigmoid, etc. require further empirical analysis and validation on practical problems. Conducting detailed empirical studies to evaluate Wavelet against various state-of-the-art activations under different settings can provide better insights into its benefits and limitations. This is important to fully understand its behavior and assess its effectiveness.

The paper only considers isotropic problems which have constant properties in all directions. However, most real-world physics systems exhibit anisotropic and nonlinear characteristics. Extending PINNsFormer to handle anisotropic problems modeled by direction-dependent PDEs, as well as nonlinear problems involving variable coefficients, would significantly broaden its applicability and demonstrate the approach's versatility. 

No quantitative analysis was performed to evaluate important design choices like the pseudo sequence length and number of levels in coarsening. Without such ablation studies, it is difficult to justify critical hyperparameters and understand their impact on the model's performance as well as computational efficiency. These quantitative studies would provide further insights to validate the architectural design of PINNsFormer.

Although various benchmark problems were tested, stronger validation would involve demonstrating the approach's effectiveness in entirely new physical domains beyond the existing test cases. Without such generalization to unseen problem classes, the claims regarding PINNsFormer's broad applicability remain partially unsubstantiated.

While efficient on smaller problems, the inherent quadratic complexity of self-attention may pose scalability challenges for extremely large spatiotemporal datasets. Developing techniques to alleviate this computational limitation would enhance the method's practicality when dealing with massive real-world physics simulations.

### Questions
see weakness above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a method to utilize the well-known transformer architecture in PINNs. Unlike PINN’s point-to-point processing, the proposed method produces multiple outputs in a forward pass by injecting multiple input coordinates. The authors used a ‘pseudo-sequence generator’, which constructs a sequence of input coordinates consisting of a spatial coordinate and multiple time coordinates. The following transformer module models the dependency between input coordinates to generate the final outputs. They also introduce wavelet activation function that shows the effectiveness. The authors have tested on three different PDEs, and it shows the comparative performance.

### Strengths
1. Using transformers in PINN training is a promising research area. I appreciate the authors’ attempt to incorporate it into PINNs.
2. The idea of processing multiple coordinates seems interesting and original.

### Weaknesses
1. I respectfully disagree with the author’s argument that the original PINN neglects temporal dependency. PINN takes temporal coordinates and spatial coordinates together and generates the output. By going through multiple layers in MLP, the time coordinate will definitely affect the features from the spatial coordinates. I agree that the suggested method might be able to model time dependency more explicitly. However, the argument that the original PINN is not capable of modeling time dependency is too strong.

2. As a follow-up comment, we sample many random collocation points at each iteration, and MLP can see many time coordinates with spatial coordinates during training. Hence, I believe the original PINN is capable of modeling time dependency.

3. Is delta t fixed? if yes, then it might be a not trivial limitation, considering different time granularity at different time coordinates.

4. If I understand correctly, it seems that Spatio-Temporal Mixer is just one layer MLP. I might have missed something, but the technical details are not properly described in explaining each component. The formal definition of each module would be appreciated.

5. The proposed Wavelet activation function seems to be a simplified version of the positional encoding. In addition, IMHO, the sine activation function, followed by MLP, which attaches weights to each neuron, could do the same thing. cos function can also be easily expressed by a bias term from the previous layer e.g., sin(x) = cos(90-x).

6. My main concern is a weak experimental setup and results. The authors presented the results of simple three PDEs, which already have been tackled by numerous works. And, there are many previous works that achieved better results (lower relative errors) [1]. 
The authors highlighted ‘very low loss’ values. Loss depends on loss function and hyperparameters, which cannot be a fair metric.
The Navier-stokes experiment used in this paper is too simple. Please consider using examples tested in [2] and [3].

### Questions
Questions are embedded in the section above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
