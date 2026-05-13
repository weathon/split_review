# A Deep Generative Learning Approach for Two-stage Adaptive Robust Optimization

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
Two-stage adaptive robust optimization (ARO) is a powerful approach for planning under uncertainty, balancing first-stage decisions with recourse decisions made after uncertainty is realized. To account for uncertainty, modelers typically define a simple uncertainty set over which potential outcomes are considered. However, classical methods for defining these sets unintentionally capture a wide range of unrealistic outcomes, resulting in overly-conservative and costly planning in anticipation of unlikely contingencies. In this work, we introduce AGRO, a solution algorithm that performs \underline{a}dversarial \underline{g}eneration for two-stage adaptive \underline{r}obust \underline{o}ptimization using a variational autoencoder. AGRO generates high-dimensional contingencies that are simultaneously adversarial and realistic, improving the robustness of first-stage decisions at a lower planning cost than standard methods. To ensure generated contingencies lie in high-density regions of the uncertainty distribution, AGRO defines a tight uncertainty set as the image of ``latent'' uncertainty sets under the VAE decoding transformation. Projected gradient ascent is then used to maximize recourse costs over the latent uncertainty sets by leveraging differentiable optimization methods. We demonstrate the cost-efficiency of AGRO by applying it to both a synthetic production-distribution problem and a real-world power system expansion setting. We show that AGRO outperforms the standard column-and-constraint algorithm by up to $1.8\%$ in production-distribution planning and up to $11.6\%$ in power system expansion.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces AGRO, a novel method for two-stage adaptive robust optimization (ARO) using a variational autoencoder (VAE) to generate adversarial and realistic uncertainty sets. The authors demonstrate that AGRO reduces planning costs in ARO tasks, outperforming classical approaches.

### Strengths
1. The proposed AGRO framework is innovative, embedding a VAE within a column-and-constraint generation (CCG) scheme to achieve high-dimensional adversarial generation with cost efficiency.
2. It seems that the empirical results highlight an over 10% cost reductions over classical methods.

### Weaknesses
1.	The introduction lacks a comprehensive motivation for using a VAE for uncertainty sets over other generative models. The authors should justify why a VAE was chosen and discuss the potential advantages over alternatives, like GANs or normalizing flows, which may also be suitable. Specifically, the paper should address the trade-offs in terms of training stability, sample quality, and computational cost, and how these considerations influenced the choice of VAEs.
2.	The discussion on the choice of the VAE bottleneck dimension (parameter L) could be expanded. The authors should provide more insight into how different L values affect the uncertainty set’s coverage and the balance between computational cost and model fidelity. It is unclear how the bottleneck dimension impacts the adversarial nature of the generated samples, and whether a lower dimension might lead to overly conservative or under-conservative uncertainty sets.
3.	While the experiments are detailed, there is no mention of computational time for VAE training or comparison with other ARO solutions. Including such results would enhance transparency about AGRO’s feasibility in larger-scale applications. The paper should include a breakdown of the computational cost associated with the VAE training, sampling, and the overall ARO optimization process, and compare these costs with classical ARO methods.
4.	The paper does not explore alternative formulations for the adversarial subproblem. A comparison with different optimization methods or a discussion on the limitations of projected gradient ascent could further clarify AGRO's robustness. The authors should investigate whether other optimization techniques, such as interior-point methods or specialized solvers for bilinear problems, could offer improved performance or convergence guarantees for the adversarial subproblem.

### Questions
1.	Why did you choose a VAE over other generative models (e.g., GANs, normalizing flows) for constructing uncertainty sets in AGRO? Would these models offer any advantages or limitations compared to VAEs in this application?
2.	How does the bottleneck dimension (L) influence the overall performance and reliability of AGRO? Could you elaborate on any trade-offs between computational cost and uncertainty set coverage as L varies?
3.	The paper discusses using VAE-based uncertainty sets to achieve tighter approximations. Could you clarify how you ensure these sets are both realistic and adversarial? Are there any specific quantitative or qualitative metrics that assess the accuracy of these generated uncertainty sets?

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
2

### Summary
This paper presents a novel deep generative approach using Variational Autoencoders (VAE) to tackle two-stage adaptive robust optimization (ARO) under high-dimensional uncertainty. Traditional ARO approaches for constructing the uncertainty set $\mathcal{U}$ tend to be overly conservative, often leading to excessive resource allocation in scenarios with high-dimensional and irregularly distributed uncertainties. The proposed AGRO method mitigates this issue by incorporating VAE embedding and column-and-constraint generation (CCG). The method also uses projected gradient ascent to solve the formulated subproblem. Experiments on two problems demonstrate the advantages of this method over conventional CCG approaches.

### Strengths
The primary contribution of this work is the innovative application of VAE to construct a tighter uncertainty set, thereby reducing over-conservatism in high-dimensional decision-making, which is then addressed through CCG. The paper is clearly presented, with informative visuals such as Figure 2, and well-organized notation and formulations. The experimental results highlight the promise of the proposed method.

### Weaknesses
The proposed approach involves training a VAE, whose performance might be sensitive to hyperparameters, computational resources, and the amount of available training data. Additional experiments and discussion could enhance the paper’s applicability. Please see the following questions for further details.

- In Figure 1, the authors use two 3D visualizations to illustrate the two-stage operations on $\mathcal{U}$ and $\mathcal{Z}$. Could the authors provide a brief description of the specific main problem addressed here to give the audience a better understanding?

- In the experiment on the production-distribution problem, the authors observed a reverse effect of the bottleneck dimension in the low-dimensional case of $|\mathcal{J}|=3$. Could the authors elaborate on possible reasons for this?

- Based on the experiments, could the authors provide practical guidelines for selecting the appropriate bottleneck dimension for VAEs according to the dimensionality or complexity of the uncertainty set?

- For tabular results such as those in Figure 3 (left) and Table 1, could the authors also report the standard deviation across trials? This would help readers understand the robustness of AGRO in different practical scenarios.

- Could the authors provide more details on the VAE architecture and training settings used in each experiment? Such as layer dimensions, normalization, optimizer, and learning rate,  for better reproducibility.

### Questions
- In Figure 1, the authors use two 3D visualizations to illustrate the two-stage operations on $\mathcal{U}$ and $\mathcal{Z}$. Could the authors provide a brief description of the specific main problem addressed here to give the audience a better understanding?

- In the experiment on the production-distribution problem, the authors observed a reverse effect of the bottleneck dimension in the low-dimensional case of $|\mathcal{J}|=3$. Could the authors elaborate on possible reasons for this?

- Based on the experiments, could the authors provide practical guidelines for selecting the appropriate bottleneck dimension for VAEs according to the dimensionality or complexity of the uncertainty set?

- For tabular results such as those in Figure 3 (left) and Table 1, could the authors also report the standard deviation across trials? This would help readers understand the robustness of AGRO in different practical scenarios.

- Could the authors provide more details on the VAE architecture and training settings used in each experiment? Such as layer dimensions, normalization, optimizer, and learning rate,  for better reproducibility.

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
This paper addresses the two-stage adaptive robust optimization (ARO) problem, where a key challenge is constructing an effective uncertainty set. The authors propose using a deep generative model to learn the uncertainty set, aiming to avoid overly conservative optimization. The method is evaluated on a synthetic production-distribution problem and a regional power system expansion problem.

### Strengths
1. The paper is well-written and clear.

2. Leveraging deep generative models to learn the uncertainty set is a promising approach.

### Weaknesses
1. The Projected Gradient Ascent (PGA) method does not guarantee convergence to the worst-case uncertainty realization. Although the authors propose randomly initializing PGA with different samples of $z$ for empirical performance, providing some theoretical analysis on the approximation error would be beneficial.

2. The performance improvement of the proposed method is minimal.

### Questions
1. The paper suggests that the framework is general and could also be applied to diffusion models. However, diffusion model training involves matching the score of the noised distribution, and samples cannot be easily obtained during training. Could you elaborate on how diffusion models would integrate with your proposed framework?

2. How do you ensure the uncertainty set learned by the VAE is sufficiently tight? When optimizing over the latent space, are there any constraints? If not, is there a risk that the algorithm could select an overly conservative worst-case realization?

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
4

### Summary
This paper proposes the AGRO algorithm, which performs adversarial generation for two-stage adaptive robust optimization using a variational autoencoder. By decomposing the optimization problem to solving the 'main' problem and the adversarial subproblem iteratively, AGRO can provide tighter uncertainty estimation and lead to better optimization outputs.

### Strengths
1. The paper is well-written, easy to follow, and understand.

2. With VAE-learned uncertainty, the proposed AGRO method does tighten the uncertainty bounds and leads to better optimization outcomes. An intuitive example in Figure 2 and experimental results clearly demonstrate this.

### Weaknesses
1. In Section 3.2, the author proposes a projected gradient ascent heuristic method to optimize $q$. Although this PGA method is well-explained in the article and I understand why the author uses it, I still expect an ablation study on directly optimizing $q$ to show if PGA could still guarantee some level of optimization quality and if there are any speed improvements.

2. Although the proposed AGRO method is an improvement based on the CCG method, in the experiments section, the author should compare with more baselines for the two-step optimization problem, which I believe is a well-studied problem with many methods proposed to solve it.

### Questions
My main question for this work is: Is the optimization problem the author wants to solve exactly a linear optimization problem (see Eq. 1, 7, 9, 10)? If so, there are already many tools for solving linear optimization problems, so why is the proposed method better than those?

If not, what kind of optimization problem does AGRO solve? Only convex?

### Soundness
2

### Presentation
3

### Contribution
3
