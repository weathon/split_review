# FreeFlow: Latent Flow Matching for Free Energy Difference Estimation

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 3, 8

## Abstract
Estimating free energy differences between molecular systems is fundamental for understanding molecular interactions and accelerating drug discovery. Current techniques use molecular dynamics to sample the Boltzmann distributions of the two systems and of several intermediate "alchemical" distributions that interpolate between them. From the resulting ensembles, free energy differences can be estimated by averaging importance weight analogs for multiple distributions. Instead of time-intensive simulations of intermediate alchemical systems, we learn a fast-to-train flow to bridge the two systems of interest. After training, we obtain free energy differences by integrating the flow's instantaneous change of variables when transporting samples between the two distributions. To map between molecular systems with different numbers of atoms, we replace the previous solutions of simulating auxiliary "dummy atoms" by additionally training two autoencoders that project the systems into a same-dimensional latent space in which our flow operates. A generalized change of variables formula for trans-dimensional mappings allows us to employ the dimensionality collapsing and expanding autoencoders in our free energy estimation pipeline. We validate our approach on systems of increasing complexity: mapping between Gaussians, between subspaces of alanine dipeptide, and between pharmaceutically relevant ligands in solvent. All results show strong agreement with reference values.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
They propose a method for estimating free energy differences between molecular systems. Traditional free energy estimation methods rely on simulating intermediate states between two systems. FreeFlow addresses this by mapping both systems to a common latent space via autoencoders and applying a neural flow model to estimate free energy differences without intermediate simulations. This latent-space approach leverages flow matching to track density changes between systems, allowing FreeFlow to handle trans-dimensional mappings.

### Strengths
They propose a transdimensional mapping for free energy estimates. Super cool. 
Their theory seems to directly relate to their implementation methods.

### Weaknesses
I would like to see way more comparisons with other methods!
Also in Figure 4, the mean of equidimensional gaussians seems to converge to the true mean, but not for the trans dimensional one. 
In Figure 5, the D(B,B) and D(M(A),B) do not completely overlap. 
Figure 6 is important, but more important is the comparison to existing methods. Free energy estimation is extremely difficult, so it is more interesting to see how much it improves upon other methods vs absolute accuracy.

### Questions
Why do the figures differ as mentioned in weaknesses?
Could you write out the proof of equation 13?
Also, please give at least a toy system code to test the method. Otherwise, it is difficult to interpret accurately.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present FreeFlow, a novel method for learning normalizing flows between distributions of arbitrary dimensions. FreeFlow achieves this using flow matching to learn an invertible map between distributions embedded into a lower dimensional latent space. The authors demonstrate the use-case of FreeFlow in application to estimating free energy differences for molecular systems. Through empirical experiments, FreeFlow is shown to efficiently estimate free energy differences for molecular systems.

### Strengths
This work addresses the challenging problem of estimating free energy differences between molecular systems. In doing so, the authors devise a framework for learning normalizing flows between distributions of arbitrary dimensions. The introduced method (FreeFlow) has two key strengths:
- FreeFlow leverages advancements in flow matching to learn more expressive maps between molecular distributions.
- FreeFlow does not require the use of non-physical modifications on molecules to match dimensions between distributions.

### Weaknesses
A central limitation of this work is that there appears to be a lack of comparisons with existing approaches that estimate free energy differences between molecular systems. Without comparison to other methods, it is hard to assess the validity of some of the claims and contributions of this work. For example:
- The authors argue that FreeFlow learns more expressive maps between molecular distributions compared to previous normalizing flows solutions. It is not clear that this claim is supported in the experiments. What are the previous normalizing flows solutions that FreeFlow is compared against? Specifically, what are the architectural differences that make FreeFlow more expressive, and how is this demonstrated empirically?
- One argued advantage of FreeFlow is that the method does not require the use of non-physical modifications, such as the use of dummy variables on molecules to match the dimensions between distributions.  It is not clear how or if avoiding the use of non-physical modifications leads to improved free energy difference estimation. How does FreeFlow compare to methods that use such non-physical modifications? Likewise, why not compare to other baselines in that address the problem of free energy difference estimation (such as those described in Figure 2)? It would be beneficial to see a comparison against methods that utilize alchemical intermediates, as these are commonly used in free energy calculations.

In addition, there are several areas in the manuscript that contain some unaddressed items (see questions below) that at times make it difficult to follow the work. I believe that adding fair comparison to existing approaches for estimating free energy differences between molecular systems and addressing the questions I outlined below would strongly improve this work.

### Questions
- Lines 232-233: Could the authors provide some explanation/justification an optimal transport map between $\rho_A$ and $\rho_B$ is needed in this setting? What happens if you were to assume independent marginals? 
- Regarding the latent representations:
    -  Do you validate that the auto-encoders are in fact over-fitting? Do you validate that the auto-encoders learn reasonable representations?
    - How did you decide on hyper-parameters for the auto-encoders? 
    - The authors justify choice of MLP for the auto-encoder architecture as "not needing to generalize" (lines 257-259). How do you think the results would change if a different architecture is used, for examples a graph neural network or transformer, which have become de facto architectures for learning molecular representations? 
- In Figure 4.a, is the objective to match the estimated target distribution (green) to the true target distribution (orange)? In which case, it appears this the estimate does not match the target. Is there intuition on why the estimated target distribution is so far from the true target distribution in the Equidimensional Gaussian Energy setting compared to the Transdimensional Gaussian Energy setting? I would assume that the Equidimensional setting should be easier?
- In Figure 5, what is the distribution pairwise distance $D(\cdot, \cdot)$?
- Lines 419-420: How do you observe the distances between $B$ and the mapped sampled $M(B)$? In Figure 5, only $D(A, B)$, $D(B, B)$, and $D(M(A), B)$ are reported.

### Soundness
2

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
In this paper, the authors focus on estimating the free energy difference between two molecular systems. They propose to use a neural network to learn a mapping between these two systems, which can reduce the variance of free energy estimation based on TFEP, providing more accurate result compared to FEP. The experiments on several simple cases demonstrate the effectiveness of proposed method. On the large molecules, the authors also claim that the result from proposed method is close to the reference data.

### Strengths
1. Using neural networks to represent the mapping between different distributions may bring more flexibility to the solution.
2. The authors give a lot of examples that help to understand the proposed method.
3. The writing is good.

### Weaknesses
1. The accuracy of the proposed method is not good enough. In the experiments of large molecules, the MAE between the proposed method and the baseline method is about tens of or even hundreds of kJ/mol. As a comparison, the error of free energy should be within 10kcal/mol (~42kJ/mol) to give a qualitatively correct prediction. Such a large difference means that the proposed method may not be reliable in practice. The authors should consider how to improve the accuracy of the proposed method.
2. The cost of the proposed method is relatively large. The training data includes molecular dynamics simulation of the related systems. Thus, when applying the proposed method to new systems, one should perform additional molecule dynamics simulation to collect training data. Given the poor accuracy of the proposed method, the reviewer believes the training cost is larger than expected.

### Questions
Suggestions are listed in weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a strategy to estimate free energy differences between molecular systems. Their approach relies on performing latent diffusion (flow matching) instead of diffusion in data space. The main advantage is that, due to the change in dimensionality required to match different molecular systems, diffusion in data space requires the addition of dummy atoms. In contrast, diffusion in latent space is dimension-agnostic. The trade-off is the need to track all the change-of-variable factors that come with the steps to match the two distributions: encoding, diffusion, and decoding. 

The authors provide experiments to demonstrate the validity of their approach, using both toy distributions of multi-dimensional Gaussians and more real-world applications.

### Strengths
The paper is well-written with clear and consistent notation, and the topic is of relevance in the field of drug discovery. The authors effectively explain existing methods while clearly stating and motivating their contribution.

### Weaknesses
The paper's main weakness is that it doesn't develop an entirely new method, but rather combines existing methodologies into a framework for free energy difference estimation. In the conclusions, the authors mention plans to apply this methodology to learn a mapping between bound protein-ligand complexes in future work. From a drug discovery perspective, this would be a more significant goal. I wonder if it's feasible for the authors to present the full thermodynamic cycle in this work.

Additionally, while instructive, the experiments are based on a limited set of examples. A broader set of experiments to evaluate their method on a large-scale dataset would definitely improve the paper.

### Questions
- I understand that overfitting the autoencoder for density reconstruction is auxiliary to performing flow matching in latent space. However, I wonder if there could be benefits to learning a "representation learning" autoencoder in the classical sense—one that can generalize and thus be used for all densities rather than requiring separate autoencoders for each molecular system.
- In Figure 4(a), the true target and the estimated target distributions differ significantly. In fact, the true target seems to coincide with the source. Could this be a labeling mistake?
- I'm not entirely clear on the theory (or implications) of the trans-dimensional change of variable. Let's consider a simple case, as depicted in Figure 3 (bottom). We have an encoder (in the paper's terminology) $f:\mathbf{R}^2 \rightarrow \mathbf{R}$, and we'll omit the decoder, leaving only this mapping.
    - The Jacobian is $J_f(x) = (\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2})$, so the volume form is simply the square root (the determinant being irrelevant since this is one-dimensional) of $\sum_i \left(\frac{\partial f}{\partial x_i}\right)^2$, correct?
    - Given these assumptions, is the equation in Figure 3 valid for all x? This seems counterintuitive, as for generic $\rho_A$ and $f$, the mapping won't be lossless. For instance, the equation in the top part of Figure 3 holds if $f$ is a bijection.
    - If that's not the case, what's the most general statement we can make for this scenario (namely, $f:\mathbf{R}^2 \rightarrow \mathbf{R}$ with no decoding)?
    - For a surjective $f$, does the reverse equation hold true? That is, $\rho_B(f(x)) = \rho_A(x) |\det J^T J|^{1/2}$? This seems more plausible, as even if $f$ isn't lossless, I should be able to make a statement about $\rho_B(f(x))$ knowing $f$ and $\rho_A$.

### Soundness
3

### Presentation
3

### Contribution
3
