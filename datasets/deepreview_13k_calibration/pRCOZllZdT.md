# Boltzmann priors for Implicit Transfer Operators

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
Accurate prediction of thermodynamic properties is essential in drug discovery and materials science. Molecular dynamics (MD) simulations provide a principled approach to this task, yet they typically rely on prohibitively long sequential simulations. Implicit Transfer Operator (ITO) Learning offers a promising approach to address this limitation by enabling stable simulation with time steps orders of magnitude larger than MD. However, to train ITOs, we need extensive, unbiased MD data, limiting the scope of this framework. Here, we introduce Boltzmann Priors for ITO (BoPITO) to enhance ITO learning in two ways. First, BoPITO enables more efficient data generation, and second, it embeds inductive biases for long-term dynamical behavior, simultaneously improving sample efficiency by one order of magnitude and guaranteeing asymptotically unbiased equilibrium statistics. Further, we showcase the use of BoPITO in a new tunable sampling protocol interpolating ITO models trained on off-equilibrium simulation data and an unbiased equilibrium distribution to solve inverse problems in molecular science.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work looks at predicting molecular dynamics simulations quickly over time, using longer time steps. The authors introduce a method using diffusion models to train on both unbiased and biased MD data. The diffusion model is used to estimate the transition density, with the goal of simulating MD more quickly. BoPITO, using Boltzmann priors, is supposed to be more sample efficient than ITO (Implicit Transfer Operator). In BoPITO, the authors also use pre-trained models of the equilibrium distribution to improve the ITO method. The authors test the method on the 1D Prinz potential and alanine dipeptide.

### Strengths
- This method could enable running MD simulations over much longer timescales
- By incorporating Boltzmann priors into the training process, this could allow more data efficiency and also ensure recovering the Boltzmann distribution over time

### Weaknesses
 - There are many ways to do molecular dynamics simulations. A common way is through methods like machine learning potentials. While the time steps that are taken there are smaller, these potentials are much more accurate and have been used for more diverse systems. It would be helpful if the authors provided some comparison to this method, as well as other methods that also try to directly predict molecular dynamics.

- The authors have only run this on two very toy systems: the 1D Prinz potential and alanine dipeptide. These systems are very far off from getting closer towards practical utility of this method. It would be more convincing if there were other systems studied, such as larger proteins or systems like the polymers or electrolytes system from Fu et al. (2023) TMLR.


- This method does not seem to guarantee important properties such as energy conservation.

### Questions
- I do not fully follow the advantage of BoPITO recovering the unbiased Boltzmann distribution over long time horizons: isn’t this something that only applies to equilibrium distributions? But at the same time, it seems like the authors are saying they can incorporate off-equilibrium data and/or estimate something about off-equilibrium simulations?

- Can the authors compare their method to other machine learning methods for molecular dynamics simulation?

- Is energy being conserved? How can you guarantee physical dynamics?

- Can the authors show that this method has potential to be broadly applicable by seeing if it works for harder systems, such as larger proteins, or polymers?

### Soundness
2

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
The authors point out that a prior work Implicit Transfer Operator (ITO) relies on extensive unbiased simulation, and suggest Boltzmann priors to improve the ability to approximate dynamics. To be specific, the authors first train a score model using the equilibrium data, afterwards fix the score model and only train the time-dependent components with unbiased and possibly off-equilibrium MD data.

### Strengths
The paper applies Boltzmann generators in ITO models to capture modes that have very small probability mass in the Boltzmann distributions.

### Weaknesses
 1. Pre-trained Boltzmann generator (BG)

My main concern with this paper is that it assumes a pre-trained BG. Since BG is trained using the energy function and data samples (more detail in Q2), I am a bit confused about what the authors intended. Is BG only used to generate initial conditions for simulations, for various sampling across the configuration space? It's unclear how the reliance on a pre-trained BG impacts the method's applicability to systems where such a generator is not readily available or easily trained. The paper should discuss the computational cost and data requirements for training the BG, especially for complex molecular systems.

2. Lack of detail of less extensive use of data compared to ITO

One of the important limitations the authors pointed out was the need for extensive,  unbiased molecular dynamics data. However, I do not see any results from the experiment nor analysis that BoPITO succeeds in generating results similar to ITO with less data, especially for Alanine Dipeptide. The paper lacks a direct comparison showing the data efficiency of BoPITO versus ITO. It would be beneficial to see a plot of performance (e.g., error in predicted time-correlation) versus the amount of training data used, for both methods, to clearly demonstrate the claimed improvement in data efficiency. The current results do not sufficiently support the claim that BoPITO requires less data to achieve comparable performance.

3. Limited baselines and molecular systems
    - While the authors claim that ITO can be improved with BG, however, I don’t see enough experimental results to conclude it.
    - Comparison with ITO for molecular systems is done for only Alanine Dipeptide, while ITO has presented qualitative results and quantitative results for the folding process of Chignolin.
    - Comparison of quantitative stationary and dynamic observables to naive molecular dynamics has not been presented, while it has been for ITO for four molecular systems (Chignolin, Trp-Cage, BBA, Villin). To support the claim that BopITO truly predicts time-correlation statistics (dynamic observable), this seems to be needed.
    
    Overall, it seems that the paper does not present enough experiment results to conclude that BoPITO improves compared to ITO [1]. The lack of comparison on diverse molecular systems and the absence of key quantitative observables limits the generalizability of the conclusions.

4. Missing ground truth transition probability for Alanine Dipeptide

One main and important result is the condition transition probability density for Alanine Dipeptide, figure 5. Though the figure shows that BoPITO and ITO (unbiased) show similar results, there are no ground truth data given to compare with. Though I understand it might be impractical to compute the transition densities for alanine dipeptide for 15,000 trajectories of length up to 1 nano-second compared to trajectories of length 500ps as in ITO[1], it would be good if the authors clarified this. The absence of a ground truth comparison makes it difficult to assess the accuracy of the predicted transition densities. Even if computing a full ground truth is infeasible, a comparison with a Markov State Model (MSM) or other approximation techniques would be valuable.

5. Requiring a well-trained Boltzmann generator

Since the proposed method uses Boltzmann generators as priors, a well-trained Boltzmann generator is essential. Although it has rather easily been done for Alanine Dipeptide, it seems that extension to complex molecular systems such as Chignolin is not flexible. The paper needs to address the scalability of training BGs for larger systems, as the current results only show a simple case. The computational cost of training a BG for a system like Chignolin, and the potential impact on the overall efficiency of BoPITO, should be discussed.

### Questions
1. Definition regarding bias and off-equilibrium

The papers uses the term biased & unbiased, off-equilibrium. As far as I understood, the definitions could be summarized as the following:
- Off-equilibrium data: simulation results (trajectories) that did not explore some modes of Boltzmann distribution
- Biased simulation & samples: simulation done & sampled achieved by biased molecular dynamics, e.g. enhanced sampling, a modified version of the naive molecular dynamics
- Unbiased simulations & samples: simulation done & sampled achieved by naive molecular dynamics, possibly may not find some modes if the time horizon is too short

To sum up, is the following a correct summarization for the method in section 3.2 and section 4?
- BG are trained with unbiased and equilibrium data for a score model
- Then the time-dependent components score are then trained with unbiased data, possibly off-equilibrium 
- Section 4.3 presents that BoPITO can approximate long-term dynamics in the above situation
- Section 4.4 shows that the training data for BG are biased, and BoPITO can recover it?

2. Boltzmann generators in prior

Boltzmann generators [1] were trained by combining two modes: training by energy and training by example.
- Training by energy: Generate a distribution in the configuration space from a Gaussian prior using the model, and minimize the difference between Boltzmann distribution using the energy term as weights.
- Training by example: Since training by energy alone tends to focus on sampling on the most stable meta-stable state, they additionally use training by some valid configurations, e.g., trajectories from naive MD simulations.
Now, my question is about section 4.2 of the paper, where “BG is available before data collection” and “BG trained on equilibrium data” seems to be a contradiction. I may have misunderstood something, could the authors please clarify this part?

3. Derivation of parameterization

In Appendix A.3, the authors derive the score of the transition probability. When deriving equation, is $s_{dyn}(\ldots) = s_{eq}(x^{t_{diff}}, t_{diff}) f_\theta(\ldots) + g_\theta(\ldots)$ ?

4. Comparison to ITO

From Figure 3 to Figure 4, the authors compare ITO and BoPITO. As far as I understood, the difference between these two methods is the parameterized epsilon, i.e. score function. They have separated the equilibrium part and time-dependent components, and have additionally trained the score function by fixing the equilibrium part and only updating the time-dependent term. Are all the other components, i.e., model and data, identical?

[1] Boltzmann generators: Sampling equilibrium states of many-body systems with deep learning, Science 2019

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes to combine Boltzmann Generators (BG) with Implicit Transfer Operators (ITOs). ITOs are limited because a lot of unbiased molecular dynamics (MD) data is needed for training. This framework combines ITOs with a BG before being able to sample efficiently and be asymptotically unbiased from the equilibrium distribution. 

From a more practical standpoint, the score function of the Score-based Diffusion Model is separated into an equilibrium contribution (from the BG prior) and the time-dependent component (to tackle off-equilibrium simulations). BoPITO defines an interpolation between models trained on off-equilibrium simulations and the equilibrium distribution, thus making it a more efficient sampler of long-time MD simulations.

### Strengths
- The paper is clearly written and easy to follow. Overall, it represents a pleasant read. 
- The authors made a great effort to make the paper self-contained, including a lot of background sections covering the basics of MD, BGs, ITOs, and diffusion models. 
- Numerical results are convincing in showing advantages compared to ITOs (PRO), although the approach is not compared to other baselines/methods in the literature (CON). This allows us to only partially appreciate the advantages of the algorithm. 
- The authors address the limitations of the current methods and envision possible avenues for future work. 
- The code attached as additional material looks good, properly formatted, and seems to run out-of-the-box

### Weaknesses
 - I find the main weakness of this work being the lack of comparison with other ML-based approaches that can deal with sampling at different time scales (e.g., [3,4]). Specifically, methods like Timewarp [3], which explicitly learns time-coarsened dynamics, or approaches based on Flow Annealed Importance Sampling [4], which can sample from complex distributions, are not considered. This makes it difficult to assess the relative performance and advantages of the proposed BoPITO method. Moreover, it would also be useful to show a ground truth in the plots when possible, e.g., Fig. 5. Adding more baselines would certainly improve the manuscript.
- As a suggestion, rather than a weakness, I feel it would be better to move the discussion to the related work at the beginning of the paper. This would help people to associate some works they may already know with the present work in case they are familiar with the literature. This would represent a useful prior to have before getting into the core of the paper.
- At the bottom of page 4, the authors say that BoPITO improves ITO learning in three different ways. However, in what follows, there are four points. I also believe it would be helpful to list these contributions visually with bullet points.

### Questions
- At the bottom of page 2 the authors write: "As a result, most MD data will be ‘off-equilibrium’, e.g. trajectories exploring one or a few of the modes of $\mu(x)$". Is it correct to interpret 'off-equilibirum' in this case as 'non-ergodic'?
- In line 59-60: " [...] BoPITO, by construction, guarantees asymptotically unbiased equilibrium statistics.". Where do asymptotic guarantees for unbiasedness come from? I presume that reweighting still needs to be enforced in order to have an asymptotically unbiased sampler [1] though it is not immediately clear to me where this occurs. 
- in line 116-117: "BGs are trained either with approximately equilibrated simulation data or with biased simulations, from i.e. enhanced sampling, by employing appropriate reweighting[...]". I think this is not entirely correct, strictly speaking. BGs can also be trained in a data-free manner and a combination of data-informed (biased/unbiased) and data-free losses (see [2]). Did the authors solely rely on negative log-like hood training or also on data-free losses (e.g., Reverse KL)?
- I believe it would be useful to have a reference around line 120 about sampling with reweighting to enforce asymptotic unbiasedness, see e.g., [1]. 
- What do the authors mean by **importance re-sampling**?
- When looking at the results in Fig. 2 I am not sure what is the crystal baseline. Is it some SOTA or how is this obtained?
- As a follow-up, question: are there any other ML-based models that can be used in this case in order to prove the goodness of the proposed method? e.g., some other baselines that are worth comparing here such as naive ITOs, or some sort of BGs able to handle MD at different time steps [3]. 
- Is there an intuitive explanation for having in the top right corner of Fig. 3 the long time scale difference in correlation to be smaller than medium and short?
- What is an intuitive understanding of $N_{\textrm{int}}$? Is that the resolution in the interpolation process between equilibrium and off-equilibrium distribution? In other words, some sort of annealing parameter?
- Are there any baselines to compare against in Fig.5? See also the weakness stated above in terms of lack of comparison with existing methods. For instance, does FAB [4] allow the computation of the same type of dynamics? If yes, how does it compare to BoPITO? If not, why?
- This is more of a general detour question due to my limited knowledge of MD simulations. In line 475 onwards, the authors write: "These approaches, in general, aim to accelerate molecular simulations akin to BoPITO, yet due to the CG operation, the molecular dynamics (kinetics) will be accelerated, and detailed knowledge of the unbiased dynamics are needed to correct this [...]". I am wondering how this can be possible. When coarse-graining a system and running MD at a coarser level, you inevitably lose information on the degrees of freedom at a smaller scale. I am naively wondering if there are ways to rigorously correct for this and still retain asymptotic guarantees in this case. 

- Lastly, I am wondering if the following intuition behind this work is correct: I train a core component of the equilibrium distribution using BGs. Then, I use some biased MD data to refine my backbone model in order to capture rare events, making it an 'ergodic sampler'. The idea is to use the ITOs paradigm to have some smooth interpolation between the equilibrium-off-equilibrium regimes encoded in the model in different ways (BG+biased MD data).


## References
- [1] [Nicoli, Kim A., et al. "Asymptotically unbiased estimation of physical observables with neural samplers." Physical Review E 101.2 (2020): 023304.](https://link.aps.org/accepted/10.1103/PhysRevE.101.023304)
- [2] [Noé, Frank, et al. "Boltzmann generators: Sampling equilibrium states of many-body systems with deep learning." Science 365.6457 (2019): eaaw1147.](https://www.science.org/doi/10.1126/science.aaw1147)
- [3] [Klein, Leon, et al. "Timewarp: Transferable acceleration of molecular dynamics by learning time-coarsened dynamics." Advances in Neural Information Processing Systems 36 (2024).](https://proceedings.neurips.cc/paper_files/paper/2023/file/a598c367280f9054434fdcc227ce4d38-Paper-Conference.pdf)
- [4] [Midgley, Laurence Illing, et al. "Flow annealed importance sampling bootstrap." arXiv preprint arXiv:2208.01893 (2022).](https://arxiv.org/pdf/2208.01893)

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper uses a pretrained Boltzmann Generator to include un-biased equilibrium information into Implicit Transfer Operators (ITOs).
ITOs learn "time coarse grained" transition densities from molecular dynamics (MD) data.
The challenge is that ITOs require (a) unbiased (b) large quanities of MD data to train.
Boltzmann Generators (BG) can approximate the true Boltzmann distribution even if trained with biased data when combined with importance resampling.


The paper suggest three ways to improve ITOs with Boltzmann generators:
1. Sampling of conformations proportional to the equilibrium distribution from the Boltzmann Generator as starting points for trajectories
2. Inductive bias: Separate learning of the transition density into a fixed stationary part (the Boltzmann generator) and learned time-dependent component to improve sample efficiency.
(Based on the spectral decomposition of the transfer operator, where the equilibrium distribution is an eigenfunction with an eigenvalue of one.) An explicit temporal decay of the time-dependent component ensures convergence to the unbiased Boltzmann distribution for long-time horizons.
3. Approximate rare dynamics outside the data, by interpolating between ITOs trained on off-equilibrium data (time-dependent component) and the unbiased equilibrium distribution (Boltzmann generator).

### Strengths
* Temporal coarse-graining of molecular dynamics is of very high relevance to simulate long-horizon observables more efficiently
* Making use of cheaply obtainable off-equilibrium data is a very promising approach to train more scalable models
* Method seems sound and well-founded in physical/statistical principles 
* The results look promising, although somewhat limited due to the small scale experiments

### Weaknesses
 * The paper would benefit from clearer writing and more extensive background sections. It seems to assume that readers are already familiar with the implicit transfer operators framework, which will often not be the case. More explanations and pseudocode (even if it is just in the appendix) would make the paper much easier to read. Specifically, the description of the score function ansatz and its connection to the spectral decomposition of the transfer operator could be significantly expanded. The current explanation is too concise for readers not already deeply familiar with the formalism. A more detailed derivation or at least a more intuitive explanation of how the eigenfunctions are used to derive the score function would be beneficial.
* The experiments are conducted only on small-scale systems, and it is unclear how well this approach would scale to more realistic scenarios. While the authors mention favorable scaling with system size, the experiments are still limited to relatively simple systems. It would be important to see results on more complex molecular systems with a larger number of degrees of freedom to assess the practical applicability of the method.
* In line 139 and 142 it says $\lambda_i = exp(-\tau \kappa_i)$ but also that $-1 < \lambda_i < 1$. How is it possible that $\lambda_i = exp(-\tau \kappa_i) < 0$ though? This seems to be a contradiction that needs clarification.
* I am having some trouble understanding the interpolators section. N_max is the maximum training lag, but then we sample with N_int > N_max. Doesn't that cause out-of-distribution problems? The explanation of how the model implies an interpolator is not clear enough. It is not obvious how sampling with a lag time larger than the maximum training lag can be justified, and how this relates to the dynamic observables used to fit the interpolation parameter. More details on the interpolation scheme and its theoretical justification are needed.
* line 60: How exactly do you define "off-equilibrium" and "biased"? The paper uses these terms without a clear definition, which could lead to confusion. A more precise definition of these terms is needed, especially in the context of molecular dynamics simulations.
* line 191 and following: what is $t_{diff}$?
* Looking at Figure 3, it seems like ITO and BoPITO have very similar performance on short and medium time scales, and BoPITO mostly outperforms ITO on long timescales, presumably due to the enforcement of the Boltzman distribution for long time horizons. I am wondering how often it is precisely the medium time scales that we are interested in though?

### Questions
* The formalism decomposes the operator in a sum of left and right eigenfunctions. Are these eigenfunctions used anywhere in the training objectives directly, or are they solely used to justify/derive the form of the score function ansatz? 
* In line 139 and 142 it says $\lambda_i = exp(-\tau \kappa_i)$ but also that $-1 < \lambda_i < 1$. How is it possible that $\lambda_i = exp(-\tau \kappa_i) < 0$ though?
* I am having some trouble understanding the interpolators section. N_max is the maximum training lag, but then we sample with N_int > N_max. Doesn't that cause out-of-distribution problems? Maybe you could add a bit more explanation in the appendix as to why the given model implies an interpolator. 
* line 60: How exactly do you define "off-equilibrium" and "biased"? 
* line 191 and following: what is $t_{diff}$?
* Looking at Figure 3, it seems like ITO and BoPITO have very similar performance on short and medium time scales, and BoPITO mostly outperforms ITO on long timescales, presumably due to the enforcement of the Boltzman distribution for long time horizons. I am wondering how often it is precisely the medium time scales that we are interested in though? 

## Suggestions
* Include a section that explains the ITO framework in more detail and includes pseudo-code
* line 107 and other places, I find formulations like "few of the modes of μ(x)" are easier to read if written as  "few of the modes of the *Boltzmann distribution* μ(x)"
* line 209 says "improve ITO learning in three ways" but then four points are listed

### Soundness
3

### Presentation
3

### Contribution
4
