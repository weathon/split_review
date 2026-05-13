# Chemistry-Inspired Diffusion with Non-Differentiable Guidance

- Decision: Accept
- Scores: 5, 6, 5, 8

## Abstract
\vspace{-1em}
Recent advances in diffusion models have shown remarkable potential in the conditional generation of novel molecules. These models can be guided in two ways: (i) explicitly, through additional features representing the condition, or (ii) implicitly, using a property predictor. However, training property predictors or conditional diffusion models requires an abundance of labeled data and is inherently challenging in real-world applications. We propose a novel approach that attenuates the limitations of acquiring large labeled datasets by leveraging domain knowledge from quantum chemistry as a non-differentiable oracle to guide an unconditional diffusion model. Instead of relying on neural networks, the oracle provides accurate guidance in the form of estimated gradients, allowing the diffusion process to sample from a conditional distribution specified by quantum chemistry. We show that this results in more precise conditional generation of novel and stable molecular structures. Our experiments demonstrate that our method: (1) significantly reduces atomic forces, enhancing the validity of generated molecules when used for stability optimization; (2) is compatible with both explicit and implicit guidance in diffusion models, enabling joint optimization of molecular properties and stability; and (3) generalizes effectively to molecular optimization tasks beyond stability optimization.

\vspace{-1em}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes CHEMGUIDE, a approach that uses non-differentiable guidance for the conditional generation of molecular structures in diffusion models. CHEMGUIDE use quantum chemistry oracles as guidance, providing gradients for sampling distributions. The method applies zeroth-order optimization to enhance molecule stability by minimizing atomic forces. Experiments demonstrate CHEMGUIDE’s effectiveness on two datasets.

### Strengths
1. CHEMGUIDE’s use of quantum chemistry as a non-differentiable oracle in conditional diffusion models is meaningful.
2. The paper reports improvements in stability and force metrics over baselines.
3. Implementing zeroth-order optimization in a diffusion context is well-justified.

### Weaknesses
1. The paper could enhance its rigor by comparing CHEMGUIDE with more baseline models, such as MolGAN, and more importantly, other existing guidance methods. The current comparisons seem limited. It would also be comprehensive to experiment with more datasets.
2. While GFN2-xTB is a reasonable compromise, comparing CHEMGUIDE results against high-accuracy methods like DFT more extensively could help validate the chemical accuracy of generated molecules.
3. The paper lacks a thorough discussion on the limitations of using a non-differentiable oracle, such as the potential difficulty in handling certain molecular configurations or diverse chemical spaces. 
4. The use of the GFN2-xTB method and bilevel optimization adds computational complexity, which could restrict practical usage. And The guidance scale parameter lacks an adaptive mechanism. Exploring automated scale scheduling would improve usability.
5. Code is not provided.

### Questions
Please see Weaknesses

### Soundness
3

### Presentation
3

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
The authors propose CHEMGUIDE, a sampling algorithm to guide pre-trained (latent) diffusion models for molecule design with the goal to optimize for stable molecules indicated by smaller force norms when evaluated using the xTB oracle functions. As the xTB oracle function, which outputs the forces per atom in a molecule, is non-differentiable, the authors make use of known gradient approximation from random pertubation theory to approximate the gradients suitable for guidance during the diffusion sampling trajectory. The authors also suggest how their non-differentiable guidance can be combined with neural regressors as commonly done in the diffusion models literature. The authors show that they non-differentiable guidance when applied on GeoLDM leads to generated molecules with lower force norms compared to the samples when GeoLDM is used without the proposed guidance, indicating that their method works for the models trained on common benchmark datasets such as QM9 and GEOM-Drugs.

### Strengths
The usage of approximate gradients from non-differentiable oracles in diffusion guidance for molecule design is novel and interesting.
To evaluate their proposed method, the authors run a suite of multiple experiments showing that on the two common benchmarks the generated samples based on their sampling algorithm have improved evaluation metrics compared to the baselines.

### Weaknesses
The guidance component from the non-differentiable oracle shows small improvement on the QM9 and GEOM-Drugs dataset. While the idea is interesting, a stronger baseline to compare against is to use the samples generated from Baseline GeomLDM and perform a relaxation using xTB. As the authors mention in their appendix A - Implementation Details, the sampling time for 100 molecules is quite slow with 6 hours and 18 minutes if they perform their proposed guidance in the last 400 diffusion timesteps using xTB as oracle.
How does the GeoLDM baseline (right column) in Table 1 and 2 compare if xTB is used using a pre-defined number of relaxation steps?

Furthermore, I found it hard to read the paper as Section 3 Methodology contains sections 3.1 and 3.2 which are not the author's contribution but already existing methods. I would move these Section 2 within the preliminaries.

Is there a typo in the numerator in Eq. 15 when approximating the gradient? It should say $\frac{ \mathcal{F}[z_{x,t} + c U, z_{h,t}] - \mathcal{F}[z_{x,t} - c U, z_{h,t}] )}{2c}$.

In Algorithm 1, the approximated gradient g_{t-1} has a dependency to the state at time $t=0$. Is this is a typo, since Eq. 15 does not refer to the clean data prediction.

### Questions
Is there a typo in the numerator in Eq. 15 when approximating the gradient? It should say $\frac{ \mathcal{F}[z_{x,t} + c U, z_{h,t}] - \mathcal{F}[z_{x,t} - c U, z_{h,t}] )}{2c}$.

In Algorithm 1, the approximated gradient g_{t-1} has a dependency to the state at time $t=0$. Is this is a typo, since Eq. 15 does not refer to the clean data prediction.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper studies how to achieve derivative-free molecular optimization with diffusion models. The main motivation for this work is that many real-world molecular properties are sophisticated and can only be evaluated through expensive experiments or non-differential simulations. In this paper, a zero-order optimization method is constructed by perturbing the input molecular conformation and the effect on the molecular properties. The effectiveness of the proposed methods is validated on a set of quantum mechanical properties for small molecules.

### Strengths
* This paper studies an important and timely problem, how to move beyond generative models (randomly sample from learned distributions) to efficient search and optimization over the space with guidance is a pressing question in molecular generation. 
* Derivative-free guidance is very well-motivated and I agree that it is of great importance to problems in real-world molecular discovery process.

### Weaknesses
I have several concerns about this paper, mostly coming from the claim, related work, and experiments. 

* First of all, the idea of derivative-free guidance is not new, in molecular optimization, evolutionary algorithms have been used [1], twisted sequential Monte Carlo for protein design [2], twisted SMC for large language model inference [3], and stochastic optimal control method for music generation [4]. I believe the claim for this work to be the first of its kind is inappropriate, neither for derivative-free guidance nor in molecular design.

* Given this is not new, the related work section in the Appendix only discusses the general molecule generation literature and part of the guided diffusion model literature, but misses the critical relevant literature both in molecular generation and other domains.

* The experimental results are weak, even if I agree on the general motivation of derivative-free guidance, (1) there are works such as simple evolutionary algorithms [1] and twisted SMC [2] available for comparison; even if you do not want to compare against them, you need to compare with gradient-based method --- if you think about the experiment budget, you can always construct a classifier by the samples you have evaluated, e.g. a trained neural network. Despite this may not generalize OOD or perform badly, but you may still include them as baselines. For more potential baselines to compare against, you can check this benchmark [5].

### Questions
Most of my questions are about experiments, I feel the current experimental comparisons are too weak (only comparing with unconditional generation), see weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose ChemGuide, a method for estimating diffusion guidance (i.e. gradients) from a non-differentiable property predictor. The goal is to eliminate the need for labeled training data typically required for property prediction networks. They demonstrate their approach in the context of 3D molecular generation. ChemGuide enables an unconditional diffusion model to generate more stable 3D molecular structures by incorporating guidance from quantum chemistry calculations (GFN2-xTB) that serve as a non-differentiable oracle.

### Strengths
- **Strong and relevant contribution**: The idea proposed in the paper has clearly relevant applications in a number of domains (i.e. any field with expensive oracles) and naturally extends existing efforts in the field of diffusion models. 
- **Novelty**: The method is conceptually simple yet novel, opening the door for various applications which could benefit from the guidance of a non-differentiable oracle.
- **Thorough empirical evaluation**: The paper presents thorough empirical analysis, effectively demonstrating both the strengths and limitations of the proposed method. The experiments span multiple datasets (QM9 and GEOM), various molecular properties, and different guidance approaches (explicit, implicit, and combined).
-  **Extensive analysis**: the empirical observations are grounded in real-world chemistry insights, with careful analysis of failure cases and performance trade-offs.
- **Clarity of presentation**: the paper is well-written and includes many relevant and well-designed figures.

### Weaknesses
 - **Justification of the zeroth-order optimization and comparison to other non-gradient optimization methods**: The paper lacks clear justification for choosing SPSA as the zeroth-order optimization method. Section 3.2 would benefit from a discussion of alternative approaches (e.g., finite differences, evolution strategies) and justification for their specific choice in terms of computational efficiency and accuracy trade-offs, and suitability for this particular application of guiding molecular diffusion models. A short pragaraph would suffice here.

- **Assessing the quality of the gradients obtained with ChemGuide vs a differentiable regressor** While the paper shows final performance metrics, it lacks direct analysis comparing the gradients estimated via zeroth-order optimization to those from a differentiable regressor. Such comparison could provide insights into how reliable are CHEMGUIDE's estimated gradients compared to differentiated gradients. For example, the authors could plot the cosine similarity between CHEMGUIDE's estimated gradients and those from a differentiable regressor across different timesteps of the diffusion process

- **Explain which guidance method is suitable for which property**:  The authors observe that noisy and clean guidance methods appear complementary, with properties poorly optimized by one often well-optimized by another (e.g., α vs ∆ϵ). However, the paper would be more practically useful if it provided explanations for these differences, helping practitioners choose the appropriate method for their specific use case.

### Questions
**clarifications**
- Can you clarify which aspects of your method implement SPSA? Equation 15 combines two ideas: 1) introducing random perturbations for atom coordinates from a standard normal distribution, and 2) using these perturbations in a finite-difference approximation of the gradient. It would be helpful to explicitly state which of these constitutes SPSA and how it differs from standard finite differences.

- What are the theoretical requirements for SPSA convergence? The paper mentions continuity of z as a requirement, but are there other conditions (e.g., smoothness, bounded variance) needed for the gradient estimates to be reliable?

**suggestions**
- Given the extensive appendix (sections A-K), adding a table of contents at its beginning would improve navigation.

- Consider adding a brief discussion of computational overhead introduced by SPSA compared to standard finite differences.

**nitpicks**
- Stability' is unnecessarily capitalized on page 6, section 4.2

### Soundness
4

### Presentation
4

### Contribution
3
