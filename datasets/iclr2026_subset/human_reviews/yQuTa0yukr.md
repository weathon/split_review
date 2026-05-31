## Human Reviewer 1

### Summary
The authors propose IsingFormer, a Transformer trained on equilibrium configurations of Ising systems to generate entire spin configurations conditioned on temperature. Integrated into Parallel Tempering (PT) — a standard MCMC approach — these learned global proposals act as rapid, uncorrelated moves, which are then verified or rejected by the Metropolis criterion. This combination, termed Transformer-Augmented Parallel Tempering (TAPT), preserves PT’s theoretical guarantees while improving its efficiency by replacing thousands of local updates with a few learned global ones.
Empirical results show that IsingFormer reproduces key thermodynamic observables and generalizes to unseen temperatures in the 2D Ising model, significantly reducing equilibration time. When applied to harder optimization problems such as 3D spin glasses and integer factorization encoded as Ising systems, TAPT consistently finds lower-energy solutions and generalizes to unseen problem instances.

### Strengths
The paper is clearly and well written, with a well-organized structure that makes it easy to follow. The related work section is particularly useful, as it not only provides an overview of prior research but also clearly explains how the proposed approach differs from existing methods. The problem addressed — improving the mixing efficiency of standard MCMC methods and accelerating sampling and optimization — is highly relevant on its own. Moreover, the authors go a step further by applying their framework to combinatorial optimization problems via the Ising model, thereby broadening the potential impact and applicability of their work.

### Weaknesses
From my understanding of the paper, I have the feeling the novelty is more limited than what the authors claim. 
Specifically, the authors propose a transformer-based autoregressive framework, conditioned on the inverse temperature $\beta$ capable of generating configurations at different temperatures. Furthermore, the combine this with Parallel Tempering to reach a far more efficient sampling routine.  Furthermore, limitations of the proposed method are currently not thoroughly discussed explicitly in the paper. 

However, both these novelties seem to have been proposed in the past, see for example:
- [Temperature steerable flows and Boltzmann generators](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.4.L042005)
- [Skipping the Replica Exchange Ladder with Normalizing Flows](https://arxiv.org/abs/2210.14104)
- [Conditional normalizing flow for Markov chain Monte Carlo sampling in the critical region of lattice field theory
](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.107.014512)

### Questions
- Related to the weaknesses pointed above, I'd kindly ask the authors to elaborate more about their framework and its unique property which makes it different, and potentially more performant, compared to the approaches listed above. 
- The conditioning of the transformer on the inverse temperature seems to suggest that it is only able to interpolate between different values of $\beta$. Nevertheless, [prior works](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.107.014512) seems to report that extrapolation is also possible. I was therefore wondering if this is an inherent limitation of transformers or if the authors have not tried extrapolation at all. 
- Why do the authors picked an autoregressive transformer as a generative model instead of a Diffusion model, autoregressive neural network (e.g., PixelCNN) or a normalising flow?
- This approach requires data for training while approaches like Boltzmann generators are data free. What is the advantage then?
- Section 4 mostly focus on the metropolis step within the TAPT algorithm which ensure to retain detailed balance and other properties typical of MCMC methods. The analysis therein seems very similar to the idea proposed by [Nicoli et al. (2020)](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.101.023304). Am I seeing it right or does your method bring some innovation there?
- Current experiments only compare standard PT with TAPT. It would be interesting to see how other deep generative models perform for the same benchmark. I still believe established flow-based (or autoregressive networks) based approaches would lead to substantially similar (if not better) results. 
- An analysis of computational time for PT and TAPT (including generating training data and training of the model) would very important to complement the analysis and assess the advantages of the model compared to standard MCMC approaches.

### Soundness
3

### Presentation
3

### Contribution
1

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This work introduces Transformer-Augmented Parallel Tempering (TAPT) which uses a decoder-only Transformer (called IsingFormer) to autoregressively generate proposals for Parallel Tempering that are conditioned on the inverse temperature. The problem settings investigated are sampling and optimization problems on Ising spin systems. The methods relies on a training phase based on samples at different temperatures. Training samples are, however, limited to the high-temperature regime. It is demonstrated that TAPT can interpolate within the range of training temperatures. Once trained, TAPT accelerates sampling and optimization substantially and demonstrates generalization capabilities on a factorization problem.

### Strengths
- The graphical presentation of results is well done.

- The integer factorization problem is interesting and appears novel in the machine learning community.

### Weaknesses
- Reliance on MCMC samples. Comparison of this method to MCMC methods like in Fig. 2 b and c are not insightfuls since they compare a method that was trained on ground truth samples (TAPT) to a method that is not trained on any samples and which has to generate such samples only based on the energy function. Concretely, in Fig 2c  one step of TAPT is compared to one step Gibbs sampling. Such a comparison is problematic since it neglects the costs for generating the MCMC samples on which TAPT was trained and the training costs. This reliance on training data limits TAPT to high temperatures and at low temperatures where sampling becomes increasingly hard the method actually switches to pure PT (see l293 ff). In l364 the authors acknowledge this shortcoming of not accounting for the TAPT training time when comparing optimization performances; they do, however, not mention the costs of generating the training data. They then claim that this is the case for "many neural optimizers" which is arguably wrong. A substantial amount of the work in neural combinatorial optimization is (1) generalizing over problems and (2) not using training data (see for instance, the two cited works by Sanokowski et al. and the references therein). Accordingly, the authors fail to correctly represent this aspect in section 2.2 where they write "These methods often directly optimize to find low-energy states and retrain models for different instances of a problem.". This is an imprecise or even miss-leading statement since actually, most works in the ML community do generalize over problems, e.g. the cited works by Sanokowski et al. and references therein.
The authors should factor in all costs of TAPT and do fair comparisons that investigate with which number of drawn samples it is more efficient to use TAPT than regular PT.

- In 2.1 it is claimed that: "Importantly, flows, diffusion models, RBMs, or alternative autoregressive samplers complement our approach: gains in generator fidelity will translate directly into higher acceptance and more effective nonlocal moves.". Why is this claim not underpinned by experiments? 

- Unfortunately, the related work section misses any discussion of other works that augment MCMC like PT or SMC with neural samplers. Recent examples in the continuous domain are Chen, 2024 or Zhang 2025, the later of which is conceptually extremely close since it also augments PT.

- The results in Fig. 2 a indeed represent generalization capabilities, but it is entirely unclear how to judge these results: the method is not compared to any other machine learning method. It is not clear which degree of generalization is sufficient for downstream applications, i.e. these results lack meaningful context.

- Unbiasedness: the authors state in section 4 about TAPT that: "This rule is theoretically valid if the transformer samples from the Boltzmann distribution at β_r". If the prerequisite is that TAPT can yield unbiased samples at each temperature why is PT then needed at all? The authors state that: "Because the IsingFormer can compute the precise probability Pmodel(m) for any given state m due to its autoregressive nature, it enables the use of the full Metropolis-Hastings (MH) correction". This is given as a reason to use the autoregressive approach which is, of course, very expensive. But actually, the MH correction is not even applied since it is not needed for optimization. So the whole reasoning appears inconclusive: the method is not really a MCMC method with according asymptotic sampling guarantees since it does not mitigate biases via MH correction and hence it is not clear why the expensive autoregressive approach is used.
The impact of MH correction should be investigated in the optimization and the sampling scenario.

- The methods should be compared to other neural optimization methods on common sampling and optimization benchmarks, like the ones used in the cited papers by Sanokowski. 

Chen, J., Richter, L., Berner, J., Blessing, D., Neumann, G., & Anandkumar, A. (2024). Sequential controlled langevin diffusions. arXiv preprint arXiv:2412.07081.

Zhang, L., Potaptchik, P., He, J., Du, Y., Doucet, A., Vargas, F., ... & Syed, S. (2025). Accelerated Parallel Tempering via Neural Transports. arXiv preprint arXiv:2502.10328.

### Questions
- Autoregressive spin-wise sample generation: does TAPT use one forward-pass for each individual proposed spin?

- In l365 it is stated that: "As expected, acceptance diminishes at the cold end beyond the training β range...". Is this shown anywhere?

- Was the generalization of TAPT over $\beta$ also investigated for the 3D Ising problem?

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
5

---

## Human Reviewer 3

### Summary
A transformer is trained on equilibrium spin configurations. It is used to propose global moves that aim to improve Parallel Tempering (PT) and evaluated on a simple spin-glass model and an Ising-encoded factorization task.

### Strengths
The idea of using a transformer as a global proposal generator in PT is interesting and conceptually sound. It is relevant to test whether such models can learn meaningful structure, and applying it to both a simple spin glass and a more applied factorization problem is a reasonable choice.

### Weaknesses
The presentation is unclear. The description of the transformer and how it is integrated into PT is scattered, and architectural details appear only later in the paper (Appendix F), after results are already discussed in Section 3.

The experiments do not convincingly show that the transformer learns structural correlations beyond global thermodynamic properties.

The benefit of the transformer appears limited. As shown in Figure 7, adding context reduces performance, suggesting that the model generates only global thermodynamically consistent proposals without capturing the spatial correlations present in the training data.

Benchmarks are limited: few problem instances, no comparison to other global or learned-move algorithms, and no study of scaling with problem size.

The ablation studies are not fully convincing. The influence of architectural parameters (number of layers, heads, width) is not analyzed.

There appears to be no control replacing transformer proposals with random global perturbations. Without such tests, it is unclear whether improvements come from learned structure or simply from periodic global resets.

### Questions
1) The model is trained on equilibrium samples to learn the equilibrium distribution, but only for higher temperatures. The claim is that low-temperature data are not helpful. Could you show performance (e.g., residual energy after fixed steps) as a function of the lowest temperature where the transformer is applied? Does performance saturate at a certain temperature depth, and does that correspond to the spin-glass transition or deeper in the glassy regime?

2) How does the transformer architecture affect performance? Please report results versus number of parameters, hidden size, attention heads, and layers.

3) A useful ablation study would be to replace the transformer’s global move by a random global perturbation? This would test whether the transformer learns something meaningful or merely acts as a reset. To isolate the benefit of learned structure, include controls using random or β-conditioned global resets at identical frequency.

4) For the combinatorial optimization experiments, computing residual energy on planted instances (e.g., as in arXiv:1906.00275) would provide an unambiguous ground-state reference.

5) The appendix derivation of the 2D Ising free energy appears to reproduce classical results rather than new material. Please clarify whether this is included only for completeness or if any modification is introduced ?

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper is proposing  a new strategy to improve parallel tempering (PT) algorithm, based on using a transformer model
in order to propose global moves to high temperatures replicas of PT.
The method is demonstrated  on small size Ising 2D, a 3D spin glass model and an integer factorization problem.

### Strengths
- the sampler is able to generalize at intermediate unseen temperatures without retraining and shows good performances with respect to PT in optimization tasks.

### Weaknesses
- Novelty: The paper claims the application of a new Generator-Verifier framework to sampling and combinatorial optimization problems. However it looks quite similar to already proposed architectures[1,2] (except for the Transformer architecture part), yet not applied to optimization tasks, which also involve auto-regressive models to perform  global moves. The novelty of the present method with respect to those resides essentially in the use of a transformer for the autoregressive model.
 - clarity: some details (is there any available repository for the implementation?) are missing to understand what the transformer is actually doing, some specification are given in appendix but not much explained,  in particular how the spins are tokenized is not clear. Also the training method of the transformer model is not clearly stated, so it is not clear how to reproduce the results.
- Evaluation: the sampling method is only compared against vanilla PT. The impact of the architecture of the auto-regressive model could be assessed by  comparing to[1,2]. Also in terms of computational efficiency, the methods is likely very heavy, and no comparison is given.   

References:
[1] Causer L, Rotskoff GM, Garrahan JP. Discrete generative diffusion models without stochastic differential equations: A tensor network approach. Physical Review E. 2025 Feb;111(2):025302.
[2] Del Bono LM, Ricci-Tersenghi F, Zamponi F. On the performance of machine-learning-assisted Monte Carlo in sampling from simple statistical physics models. arXiv e-prints. 2025 May:arXiv-2505.

### Questions
More specifically I have the following questions:

 - Is there some specificity to the framework proposed that makes it different from proposing global moves to intermediate temperatures of a PT sampling scheme ?  
 - How is training performed: is there a tokenization taking place at some point ? Is a specific ordering of the spins used ? 
 - In the plain text, it is mentioned that Metropolis-Hasting corrections are performed (L 278-285). However, lines 10-11 of Algorithm 1 clearly perform this step,  and L 050 of the main text include the MH step as part of the verifier. Is the MH step actually performed or not? If not, what are the guarantees of actually sampling the equilibrium  distribution of the model ? For instance for the reports of the free energy per spin in Table 1, since the model is Ising 2d, it is made of two potential wells with the exact same depth,  so the goodness of the free energy per spin only ensures that a local convergence at least one of the well is obtained but it does not tell whether perfect balance between the two wells was obtained. Stated differently, mode dropping could occur without notice in this case.
 - how does the algorithm scale with size? for instance the size 50x50 is very small compared to what can be done with a dedicated algorithm like Wolff algorithm which is also able to  propose global moves by flipping clusters of spins. Is it possible to obtain reasonable scaling function and critical exponents by varying the size of the system on the 2D Ising with the proposed algorithm  for instance?
 - how good are the performances in the optimization, could we have some elements of comparison with dedicated solver in terms of precision and computational time?
 
I would suggest to have more extensive tests (rather than on the 2D Ising model, which is not so informative) to validate that the generator actually learn equilibrium physics in particular on multi-modal dataset with not necessarily well balanced modes.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4