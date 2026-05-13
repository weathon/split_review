# Deep Learning Alternatives Of The Kolmogorov Superposition Theorem

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
This paper explores alternative formulations of the Kolmogorov Superposition Theorem (KST) as a foundation for neural network design. The original KST formulation, while mathematically elegant, presents practical challenges due to its limited insight into the structure of inner and outer functions and the large number of unknown variables it introduces. Kolmogorov-Arnold Networks (KANs) leverage KST for function approximation, but they have faced scrutiny due to mixed results compared to traditional multilayer perceptrons (MLPs) and practical limitations imposed by the original KST formulation. To address these issues, we introduce ActNet, a scalable deep learning model that builds on the KST and overcomes some of the drawbacks of Kolmogorov's original formulation. We evaluate ActNet in the context of Physics-Informed Neural Networks (PINNs), a framework well-suited for leveraging KST's strengths in low-dimensional function approximation, particularly for simulating partial differential equations (PDEs). In this challenging setting, where models must learn latent functions without direct measurements, ActNet consistently outperforms KANs across multiple benchmarks and is competitive against the current best MLP-based approaches. These results present ActNet as a promising new direction for KST-based deep learning applications, particularly in scientific computing and PDE simulation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents an alternative formulation for a trainable network based on the KST. 

The paper presents the theoretical property of the model and experimentally validates the performance as an approximation function of PINN, on 3 PDEs.

### Strengths
The paper is clear and justify its contribution, and put in context with the current state of art

The paper justifies the change in the KAN architecture and its relationship. The connection with the multi-head transformer is a bit stretched tho. 

The paper provides some experiments to show the potential of changing the representation of the KST.

### Weaknesses
The exposition is very good, the experiments show the advantage with respect to other KST architecture.

There is only the evaluation in the PINN context. It would be nice to have more experiments, for example against some neural operators and training from data.

### Questions
I would like to see, even in the annex, the behavior against Neural Operators.

is there other choices of the b(t) functions that works well?

How do you choose the hyper-parameters (N,m)?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Based on a new formulation of the Kolmogorov Superposition Theorem (KST), this paper introduces a neural network ActNet to solve PDEs. ActNet is proposed as a global approximation in solving PDEs, which is similar to PINN. The authors demonstrate ActNet's theoretical properties, including universality, and validate it on a range of PDE benchmarks, showing improved performance over KAN and SIREN.

### Strengths
1. The authors provide a solid theoretical foundation for ActNet, detailing its universal approximation capabilities and presenting a well-motivated formulation based on KST. This paper compares the complexity of different formulations well.
2. Three 1D examples and two 2D examples are included to demonstrate that ActNet can achieve better performance. 
3. This paper compares the model performance with other open-source JaxPi frameworks to enhance reproducibility and fairness.

### Weaknesses
1. The selected examples primarily use sinusoidal forcing terms, including equations like Poisson, Helmholtz, and Allen-Cahn. The proposed model uses sine functions as basis functions, which justifies its improved performance over the spline basis functions used in KAN. In Figure 12, we can see that SIREN can have the best performance. Therefore, comprehensive benchmarks should be included for challenging 2D and 3D problems, including the Navier–Stokes equations and turbulence cases. The current benchmark suite does not adequately demonstrate the model's robustness to non-smooth solutions or complex physical phenomena, which are critical for real-world applications. The reliance on sinusoidal forcing terms, while useful for initial validation, limits the generalizability of the conclusions.

2. As this paper emphasizes the comparison between MLP and KAN, it is essential to include a general MLP model for performance evaluation alongside SIREN. The absence of a standard MLP baseline makes it difficult to isolate the performance gains specifically attributable to the ActNet architecture versus the inherent advantages of sinusoidal activation functions. A more comprehensive comparison should include MLPs with common activation functions such as ReLU, tanh, or GELU to provide a more complete picture of the model's relative performance.

3. This paper presents a novel approach for solving PDEs, similar to PINN. However, since the PDEs are known, why not use traditional numerical methods, such as FEM or FVM, on GPUs? A fair comparison is needed, focusing on accuracy, efficiency, and implementation complexity. The paper lacks a quantitative comparison against established numerical solvers, which are often highly optimized and readily available. This makes it difficult to assess the practical advantages of the proposed method, especially in terms of computational cost and accuracy for standard forward problems. The comparison should include metrics such as wall-clock time and memory usage.

4. How does the proposed method address high-dimensional input problems? The paper does not provide sufficient detail on how the method scales with increasing input dimensionality. While the theoretical foundation might extend to higher dimensions, empirical validation is needed to demonstrate its practical applicability. The computational cost and memory requirements for high-dimensional problems should be discussed.

5. Line 161: Why is the pathological behavior of the inner function relevant to the exact representation rather than the approximation? The explanation of the inner function's pathological behavior is not clear and its relevance to the approximation capabilities of the network is not well-established. The discussion should clarify how the smoothness or non-smoothness of the inner functions affects the overall approximation quality.

6. Table 2: A relative L2 error should suffice for accuracy comparison, so why include the residual loss? Additionally, why does the Allen-Cahn example in Table 2 lack a consistently best-performing model? The inclusion of residual loss alongside L2 error is not well-justified, and the lack of a consistently best-performing model for the Allen-Cahn example raises questions about the robustness of the method. The paper should provide a clear rationale for including both metrics and investigate the reasons for the inconsistent performance in the Allen-Cahn case.

### Questions
1. This paper presents a novel approach for solving PDEs, similar to PINN. However, since the PDEs are known, why not use traditional numerical methods, such as FEM or FVM, on GPUs? A fair comparison is needed, focusing on accuracy, efficiency, and implementation complexity.
2. How does the proposed method address high-dimensional input problems?
3. Line 161: Why is the pathological behavior of the inner function relevant to the exact representation rather than the approximation?
4. Table 2: A relative L2 error should suffice for accuracy comparison, so why include the residual loss? Additionally, why does the Allen-Cahn example in Table 2 lack a consistently best-performing model?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper investigates alternative approaches to the Kolmogorov Superposition Theorem (KST) for neural network design, addressing practical limitations of the original KST formulation, such as its complexity and lack of structural insights. Kolmogorov-Arnold Networks (KANs) utilize KST for function approximation but have shown inconsistent performance compared to traditional multilayer perceptrons (MLPs). The authors introduce ActNet, a scalable model that builds on KST while mitigating some of its original limitations. Evaluated within the Physics-Informed Neural Networks (PINNs) framework for PDE simulation, ActNet consistently outperforms KANs and competes well with leading MLP-based methods, marking it as a promising direction for KST-based deep learning in scientific computing.

### Strengths
1. **Originality**: The paper brings a fresh perspective to neural network design by leveraging alternative formulations of the Kolmogorov Superposition Theorem (KST). Introducing ActNet, based on Laczkovich's theorem, reflects a novel approach to overcoming the limitations of Kolmogorov-Arnold Networks (KANs), making KST more applicable to practical deep learning tasks, particularly within Physics-Informed Neural Networks (PINNs).

2. **Quality**: The research is thorough, with ActNet being tested across multiple benchmarks against established models like KANs and MLPs, demonstrating its advantages in function approximation and handling PDE simulations. Theoretical foundations are strong, with proofs of ActNet’s universal approximation properties, and empirical results consistently show ActNet’s improved performance in accuracy and stability.

3. **Clarity**: The paper is well-structured, presenting a clear motivation for the need for alternative KST formulations, followed by detailed descriptions of ActNet’s architecture and its theoretical underpinnings. The explanations of mathematical concepts and the positioning of ActNet within current scientific computing challenges are accessible and well-supported with illustrative figures and tables.

4. **Significance**: ActNet addresses critical limitations in applying KST to neural networks, opening new possibilities for KST-based models in scientific computing and PDE simulation. The model's competitive performance against leading MLP-based approaches highlights its potential impact on advancing scientific machine learning, particularly in low-dimensional function approximation and complex simulations, where existing architectures struggle.

### Weaknesses
1.  Although ActNet performs well on PINNs, its comparisons are limited to specific benchmarks and do not consistently compare against the latest models for PINNs. Specifically, the comparisons do not include a thorough evaluation against recent state-of-the-art methods that incorporate adaptive residual connections and physics-informed initialization, which have shown significant performance gains in similar problem settings. This lack of comparison against the most advanced techniques limits the ability to fully assess ActNet's relative performance and contribution.
2. The paper lacks detailed ablation studies on critical design choices within ActNet, such as the basis functions used or the impact of ActLayer depth. Without these studies, it is difficult to understand the sensitivity of the model to these parameters. For example, the choice of basis functions could significantly impact the model's ability to approximate different types of functions, and the depth of the ActLayer could affect both the model's capacity and its training stability. Including these analyses would clarify the sensitivity of ActNet’s performance to these parameters and help guide future implementations or adaptations of the model.
3. While the paper offers rigorous theoretical grounding, some sections—particularly those detailing the inner workings of the ActLayer—may be dense for readers unfamiliar with KST. The explanation of how the specific choice of basis functions interacts with the overall approximation capabilities of the network could be expanded, providing more intuitive understanding of the model's mechanisms.

### Questions
1. As you mentioned about JAXPI, Why you didn't compare with their latest result which is Piratenet [1] that has been pubilshed Feb 2024 rather than Causal PINN that from 2022. Also I saw that you have cited this paper as well.
2. What happen if you apply ActNet into more chaotic system, for example Navier–Stokes equations. is ActNet still performs better?
3.

[1] PirateNets: Physics-informed Deep Learning with Residual Adaptive Networks

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes ActNet, a novel neural network architecture based on Kolmogorov Superposition Theorem (KST), as an alternative to Kolmogorov-Arnold Networks (KANs). The authors use the Laczkovich version of KST to develop their architecture instead of the original KST emplyoed in KANs. They prove universal approximation properties and propose an initialization scheme for their method which they assures stability of network activations. 

Empirically, they evaluate their model on PDE simulation tasks using a PINN framework. They compare their model to KANs and MLPs on a range of PDE equations such as Poisson, Helmholtz, Allen-Cahn and Kuramoto-Sivashinsky. Their method has comparable accuracy to the benchmarks chosen for comparison.

### Strengths
1. I find the paper to be well-written. The exposition of KST and of the ActNet architecture are clearly presented. The contributions made by this work is also clearly outlined.
2. As far as I am aware, the technical contributions in this paper are novel. The proposed architecture outperforms other similar models (KST variants such as KANs and MLPs) on the chosen tasks, has better parameter efficiency and seems to benefit from good theoretical guarantees (universal approximation properties for a two layer network).
3. I found the experimental section of the paper to be strong. Information about implementation and the considered PDEs is clearly given either in the main paper or in the appendix. Multiple ablations are conducted to validate the model. The choice of experimental framework is well motivated and the code is publicly available on Github.

All in all, I find this paper presents an interesting alternative to KANs.

### Weaknesses
1. Although interesting when compared to KANs and other MLPs, this method is not competitive when compared to SoTA ML informed solvers which use more sophisticated inductive biases such as [1,2,3,4] for example.
2. I find the theoretical contribution of the paper to be a bit weak. Although an interesting result, it seems trivial to me that a method based on Superposition Theorems for representing multivariate functions would benefit from universal approximation properties. Moreover, it is not clear to me why the property presented in Theorem 3.4 is a selling point of your method. Even if this property didn't hold, we could simply use some form of LayerNorm to enforce this. Also, in the context of modelling physical equations, it is not clear to me that inputs would be distributed following a $(0,1)$ Normal distribution in the first place.
3. There are a few typos/minor mistakes in the proofs. I will list them by point below.

Comments about the proof of Theorem 3.3:
* Line 868: typo, I believe you meant $poly_g$ not $pol$.
* "by making $\sum \lambda \phi (x)$ sure that is at most $δ$ far from the approximation $\sum \lambda \hat{\phi} (x)$". You do not introduce/define this approximation before mentioning it here, I think it would make this step clearer if you defined what this approximation is.

Comments about the proof of Theorem 3.4
* "After properly initializing the $β$ and $λ$ parameters (detailed in Appendix F)" this is not detailed in the appendix. Thus, when defining the expectation and second moment of these variables, it is not clear where the values you obtain come from (around lines 981 and 1006 )
* Do you consider the that $p=0$ and $\omega \sim \mathcal{N}(0,1)$ for this proof? If so, the eq. at line 984 is not clear to me. Same for the step between lines 1006 and 1009.

Also here are some minor comments you may want to address for the final version: 
* "Table 1" not "table 1" (line 67 for instance).
* $m$ in Table 1 is not described until section 3. It would be nice to know (at least in big O) what this value is in terms of $d$ when looking at this table.
* $\beta$ should be bolded since it is a matrix, not a scalar (line 237).
* Inconsistent use of $\epsilon$ and $\varepsilon$ (around line 295 theorem 3.3 def 3.2).
* The grid size considered for the experiments is not reported in main paper and generally hard to find.
* The "Discussion" section appears to be more of a conclusion to me than a discussion of results.

### Questions
* The original KAN paper boasts interpretability of the learnt network. Does your method offer any interesting results in terms of interpretability?
* Do you have any experiments out-of-distribution (OOD) regime? It would be interesting to see how the model reacts to change in initial conditions or boundary conditions for example.
* Why didn't you test on the function approximation tasks as presented in the original KAN paper? Given your method is a direct competitor to the KAN architecture, such results would be interesting to have.
* How does your method perform given a different function basis?
* Are $p$ and $\omega$ trainable parameters?
* My understanding of the proof of Theorem 3.3 is that you use Weierstrass theorem to create polynomial bases which approximate both i) the sum of $g$s ii) the weighted sum of $\phi$s up to the desired precision $\epsilon$. However, the link between this and the architecture is not immediately clear to me.

    From what I gather, each polynomial approximation can be represented by an ActLayer with a polynomial basis of size $N_g$/$N_q$ and well chosen $\beta$ values. Is my reasoning correct here? I think it would improve clarity if you mentioned how your proof relates to the proposed architecture.

### Soundness
4

### Presentation
3

### Contribution
3
