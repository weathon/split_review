# Unified Generative Modeling of 3D Molecules with Bayesian Flow Networks

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
Advanced generative model (\textit{e.g.}, diffusion model) derived from simplified continuity assumptions of data distribution, though showing promising progress, has been difficult to apply directly to geometry generation applications due to the \textit{multi-modality} and \textit{noise-sensitive} nature of molecule geometry. 
This work introduces Geometric Bayesian Flow Networks (GeoBFN), which naturally fits molecule geometry by modeling diverse modalities in the differentiable parameter space of distributions. GeoBFN maintains the SE-(3) invariant density modeling property by incorporating equivariant inter-dependency modeling on parameters of distributions and unifying the probabilistic modeling of different modalities. 
Through optimized training and sampling techniques, we demonstrate that GeoBFN achieves state-of-the-art performance on multiple 3D molecule generation benchmarks in terms of generation quality (90.87\% molecule stability in QM9 and 85.6\% atom stability in GEOM-DRUG\footnote{The scores are reported at 1k sampling steps for fair comparison, and our scores could be further improved if sampling sufficiently longer steps.}). GeoBFN can also conduct sampling with any number of steps to reach an optimal trade-off between efficiency and quality (\textit{e.g.}, 20$\times$ speedup without sacrificing performance).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Bayesian Flow Networks (BFN) are a recently proposed generative model, which uses diffusion in the inference process (like diffusion models), but for the generative process maintains a latent distribution parameters over the data, and updates these with Bayesian updates. These models have as advantage that they can handle discrete and discretized variables, besides continuous variables.

The authors propose to use BFNs to sample molecules, consisting of a collection of atoms, each with a continuous position and discrete atom type (or discretised atom charge). As the authors use a prior equivariant neural network, the resulting sampler is invariant to rotations (and to translations via centering). The authors show state-of-the-art performance in several unconditional and conditional sampling tasks.

### Strengths
- The method shows strong performance, exceeding prior methods.
- It's great to see a molecular sampling method used that handles the continuous positions and discrete atom types so naturally.
- The method improves consistently when more compute (=sampling steps) is used.

### Weaknesses
 - I'm not so convinced about the translational equivariance of theorem 3.1. The concept "Zero of Mass" is not defined in the cited [1]. I suppose this is the space where $x$ has a zero center of mass. How does this affect $	heta$ and $y$? [2] gives a detailed analysis about how to handle translation invariance in diffusion, but it's not so clear to me how this applies immediately to a BFN. The proof of theorem 3.1 in the present manuscript says nothing about translations.
- The proposed method has limited novelty, as it combines a sampling method with an equivariant neural network to create an invariant sampler, as has been done many times previously, without other significant methodological innovation.

If the authors clear up the translational equivariance, I'll increase my score.

### Questions
- The boldness in the $V \times U$ and Novelty columns of table 1 appears incorrect.
- There appears to be an inconsistency in the definition of $p_U$ in Eq (5) of the manuscript and Eq (6) of [3]. Is the $y$ sampled from $p_O$ as the manuscript states, or from $p_S$ as [3] states?
- The authors write "For Conditional Molecule Generation, we implement a conditional version GeoBFN with the details in the Appendix", but I can't find this in the appendix.
- I'm quite surprised that sampling the charges via the discretized method outperforms sampling as discrete atom types. The atomic charge doesn't seems much like a continuum to me. Could the authors elaborate on this? Is it because the hydrogen / not hydrogen distinction is most important, which the discretized method is sensitive to?
- The results of EDM in table 1 seem worse than those reported in the EDM paper. Why is this?

Typo:
- Thm 3.1: transitional -> translational

Refs:
- [1] Köhler, Jonas, Leon Klein, and Frank Noé. 2020. “Equivariant Flows: Exact Likelihood Generative Learning for Symmetric Densities.”  http://proceedings.mlr.press/v119/kohler20a/kohler20a.pdf.
- [2] Xu, Minkai, Lantao Yu, Yang Song, Chence Shi, Stefano Ermon, and Jian Tang. 2021. “GeoDiff: A Geometric Diffusion Model for Molecular Conformation Generation,”https://openreview.net/forum?id=PzcvxEMzvQC.
- [3] Graves, Alex, Rupesh Kumar Srivastava, Timothy Atkinson, and Faustino Gomez. 2023. “Bayesian Flow Networks.” http://arxiv.org/abs/2308.07037.


---- 
Score raised following the discussion and the positive opinions of the other reviewers.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors apply a very recent generative modeling framework, [1], to the context of modeling biological molecules, and demonstrate improved performance on established molecular generation benchmarks.

------ Post-rebuttal ------

I believe my concerns about the theoretical presentation and clarity have been resolved. I believe this work is a solid contribution to the field, and I recommend its acceptance.

[1] Bayesian Flow Networks. https://arxiv.org/pdf/2308.07037.pdf

### Strengths
- The authors propose a novel model that conceptually simple to understand: the Bayes Flow Network introduced in [1] is applied to the context of molecular modeling by incorporating the equivariant structure of 3D molecular geometries.
- The empirical capabilities of the model, and its improved performance over existing works, is vetted with established baselines for molecular generation tasks.

### Weaknesses
 -  There appears to be some significant issues with the formulation of the model. First, key equations are not derived or justified in the text or appendix. For example, how is the variational bound of the probabilistic model (Eq. 8) derived? Specifically, how do the terms in the KL divergence arise, and how does the expectation over the approximate posterior distribution $q$ lead to the sum of KL divergences in the subsequent expression? Furthermore, how does it lead to Eq. 19? What is $L_\infty$? Is this the supremum norm? Why does minimizing this value lead to the correct parameters for the proposed model? It is difficult to verify the mathematical consistency of the model without these derivations. Second, the proof of Theorem 3.1 and Proposition 3.2 appear to be incomplete. For example, the proof of Theorem 3.1 ends mid-sentence. Moreover, I do not see anywhere a proof of translation invariance, only rotation invariance via the matrix $\mathbf{R}$. Additionally, how does Lemma C.1 establish Eq. 23? There appears to be major steps that are skipped in this proof. 

- It is not entirely clear why Bayesian Flow Networks improve the performance of modelling 3D tasks (or perhaps specifically molecular generation tasks). The authors attempt to provide some intuition but I am not entirely convinced (see Questions).

### Questions
I could not find the definition of the subscripts $GeoBFN_{50}, GeoBFN_{100}, \dots, GeoBFN_{2k}$ in Table 1, Section 4. Where are these defined?

Can the authors clarify the meaning of this sentence in the last paragraph of Section 3.3: "The underlying reason lies in the fact that the marginal of θi in GeoBFN is in an entropy-increase procedure, e.g., from δ distribution(θ0) to the data distribution(θn). While in diffusion-based models, the marginal is in an entropy-decrease fashion, e.g., from a high-variance Gaussian distribution N (0, I ) to the data distribution." This sentence is very unclear to me. Additionally, the reasoning does not entirely connect for me. Isn't $\theta$ obtained from $\mathbf{y}$, which is an inherently noisy variable (i.e. Eq. 2)? So why do the authors claim that it has low entropy?

Are there any architectural / data preprocessing differences between the diffusion models (e.g. EDM) and the proposed GeoBFN? Are all improvements in performance attributable to the new training / sampling algorithm given by the Bayesian Flow Networks formulation [1]? Though the derivation is different, the training loss (Eq. 19) ultimately looks very similar to a diffusion model loss.

Can the authors provide a clear formulation of the training algorithm (e.g., via a latex algorithmic block) so it is more clear what is being calculated?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors apply Bayesian Flow networks (BFN) to the problem of modelling the 3D coordinates of molecules. The authors show how to make the BFN SE(3) equivariant and incorporate an SE(3) equivariant GNN into the BFN architecture for this. Strong performance is obtained on QM9 and GEOM-drugs. Additionally the model allows for flexible specification of the number of steps for sample generation - allowing trading off accuracy for speed.

### Strengths
- This paper is the first to apply BFN, a new class of generative models, to molecule generation.
- Good results: On both QM9 and GEOM-drug BFN outperform diffusion models which are a strong baseline. 
- It is demonstrated that BFN achieve a better trade-off of sample quality vs sampling speed than diffusion models. 
- The lower variance of the parameter space that BFN operate (relative to diffusion models which operate in sample space) seems advantageous - this is nicely visualised in Figure 3.

### Weaknesses
 - I found the text inside the section "Overcome Noise Sensitivity In Molecule Geometry" unclear (see Questions below).


### Questions
In section 3.3 the text says
> Hence, GeoBFN implies an objective with smoother information changes.
What does "objective" refer to here? The text seems to be referring to sample generation (rather than training) but "objective" seems to imply a training objective? 
Additionally the link between the marginals following an entropy increasing procedure implying an objective with smoother information changes is unclear to me - could the authors please elaborate?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes the use of newly formulated Bayesian Flow Networks for use in generating small molecules.

### Strengths
- The authors provide a very readable and accessible introduction to Bayesian Flow Networks.
- Well-formulated mathematical foundations for the proposed method.
- The authors compare to a large variety of benchmarks, showing improvement compared to all of them.
- The authors have run ablation studies that clarify the different design choices made.

### Weaknesses
 - The noise-sensitivity section (3.3) is not very clear, the authors should describe in more detail the issue and why a variance-increasing versus variance-decreasing sampling procedure is an important design decision. The claim of "smoother information changes" especially seems intuitive yet subjective. Specifically, the authors should clarify how the addition of noise affects the interatomic distances and how this relates to the preservation of chemical information. A more rigorous explanation of how the noise impacts the point cloud representation and the resulting chemical validity is needed. 
- The authors should explain how the objective is changing in equation 21, as it is not clear to me how this is improving the issue with sparser sampling of the center buckets. It is not clear how the weighted average and subsequent nearest neighbor selection addresses the issue of center bucket sparsity. A more detailed explanation of the mathematical justification and how this relates to the training objective is required.

### Questions
- Could you expand why larger numbers of generation steps seems to decrease novelty of the molecules?
- Is it fair to say that atom stability is easier (requires less generation steps) than molecular stability?
- Is it clear why the validity of the DRUG database samples seems to decrease with the number of generation steps, and is overall lower than some of the baselines? Is there something special about this dataset?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
