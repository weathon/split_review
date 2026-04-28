# CryoFM: A Flow-based Foundation Model for Cryo-EM Densities

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Cryo-electron microscopy (cryo-EM) is a powerful technique in structural biology and drug discovery, enabling the study of biomolecules at high resolution. Significant advancements by structural biologists using cryo-EM have led to the production of \rebuttal{around 40k} protein density maps at various resolutions \rebuttal{on EMDB}\footnote{EMDB~\citep{emdb} is a public repository for cryo-EM density volumes.}. However, cryo-EM data processing algorithms have yet to fully benefit from our knowledge of biomolecular density maps, with only a few recent models being data-driven but limited to specific tasks. In this study, we present \ours, a foundation model designed as a generative model, learning the distribution of high-quality density maps and generalizing effectively to downstream tasks. Built on flow matching, \ours is trained to accurately capture the prior distribution of biomolecular density maps. Furthermore, we introduce a flow posterior sampling method that leverages \ours as a flexible prior for several downstream tasks in cryo-EM and cryo-electron tomography (cryo-ET) without the need for fine-tuning, achieving state-of-the-art performance on most tasks and demonstrating its potential as a foundational model for broader applications in these fields.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces CryoFM, a foundation model for the distribution of high-quality cryo-EM density maps. CryoFM consists of two components: CryoFM-S models local details at high resolution, CryoFM-L models the overall shape at medium to low resolution. Both models are trained with data from EMDB by using flow matching. CryoFM can be combined with experimental data by using a flow posterior sampling method introduced by the authors. The impact of the foundation model is demonstrated for various reconstruction tasks (density modification, denoising, missing wedge problem, ab initio reconstruction) and in a number of ablation studies.

### Strengths
* CryoFM is a foundation model for density maps that can be combined with different types of data. 
* CryoFM achieves state-of-the art performance on a number of reconstruction tasks and is demonstrated to be superior to other baselines.
* CryoFM seems to be faster than other baselines.

### Weaknesses
 * The mathematical derivation of the algorithm seems to be a bit sloppy. 
* Tests with experimental data are missing. 
* No source code is provided (it would also help clarify some of the mathematical shortcomings of the paper). 

__Recommendation__

I recommend a weak accept. The results are quite convincing, although a systematic benchmark with more examples would be desirable. It is unclear how the experimental density maps were selected for pretraining. It would be desirable if the authors reported a list of all PDB entries that went into pretraining. That way it is unclear whether some of the complexes that were used to illustrate the power of CryoFM are already part of the training data. Also the mathematical treatment of the method is sketchy and at times inconsistent.

### Questions
1) Dataset for pretraining: You state that you remove "problematic cases" from the pretraining set. What are these problematic cases? Why are large maps with a length greater than 576 \\AA removed from the pretraining set? Could you please provide a complete list of the maps used for pretraining?
2) You only show 4 examples for the ab initio modeling task, one sample for each problem setting. Can you comment on the success rate? Are the shown approximate posterior samples, the best human selected ones or something we can expect to see on average when using the proposed approach on other data?
3) Lines 375/376: From Fig. 5 it is unclear why and to what extent DeepEMhancer "introduces artifacts and alters the overall shape." The FSC is very good and the visual appearance is similar to your result.
4) How fast is CryoFM compared to the other baselines? 

__Additional feedback__

1) The mathematical explanation of CryoFM should be improved. For example, Eq. (2) states $\\mathbf{x}_t | \\mathbf{x}_0 = (1-t)\\mathbf{x}_0 + t \\mathbf{x}_1$ implying $u(t, \\mathbf{x}_t | \\mathbf{x}_0) =  \frac{d}{dt} \\mathbf{x}_t|\\mathbf{x}_0 = \\mathbf{x}_1 - \\mathbf{x}_0$ and not $\\mathbf{x}_0 - \\mathbf{x}_1$. These sign errors occur at various places throughout the manuscript. 

2) Another problem can be found in line 172 which should read 
    $$\\mathcal{L} = \\mathbb{E}_{t, p_0(\\mathbf{x}_0), p_1(\\mathbf{x}_1)} \\left[ \\| v _{\\theta} (t, \\mathbf{x}_t) - (\\mathbf{x}_1 - \\mathbf{x}_0) \\|^2_2 \\right]$$
    In addition to the sign error, your loss is oversimplified and needs to indicate the expectation over $t \\sim \\mathcal{U}[0,1]$, $\\mathbf{x}_0 \\sim p_0(\\mathbf{x}_0)$, and  $\\mathbf{x}_1 \\sim p_1(\\mathbf{x}_1)$.

3) An error/typo can also be spotted in line 196: 
    $$\\nabla_{\\mathbf{x}_t} \\log p (\\mathbf{x}_t | \\mathbf{y}) \\approx \\nabla _{\\mathbf{x}_t} \\log p (\\mathbf{x}_t) - \\lambda_t 
\\nabla _{\\mathbf{x}_t}  \\| \\mathbf{y} - \\mathcal{A} \\hat{\\mathbf{x}}_0 (\\mathbf{x}_t) \\|_2^2$$
  Your version __adds__ the likelihood term rather than subtracting it, which only makes sense if $\\lambda_t \\leq 0$, but in Algorithms 1 and 3 we have $\lambda_t \\geq 0$.

4) ODE solvers require a time increment $\Delta t$ (explicitly or implicitly) which is missing in your version of Algorithm 1. So Algorithm 1 should read similar to

    \\begin{aligned}
    &\\mathbf{x}_1 \\leftarrow \\mathcal{N}(0, \\mathbf{I}) \\\\
    &\\textcolor{red}{\\Delta t \\leftarrow 1/N} \\\\
    &\\textbf{for }t \\in [1, 1- \\Delta t, 1 - 2\\Delta t, \\ldots, \\textcolor{red}{\\Delta t}] \\textbf{ do} \\\\
    &\\qquad \\mathbf{x}' _{t - \\textcolor{red}{\\Delta t}} \\leftarrow \\mathbf{x} _t  - v _{\\theta}(t, \\mathbf{x} _t) \\textcolor{red}{\\Delta t} \\\\
    &\\qquad l(\mathbf{x} _t) \\leftarrow \\| \\mathbf{y} - \\mathcal{A} \\hat{\\mathbf{x}} _0(\\mathbf{x} _t) \\|^2_2 \\\\
    &\\qquad \\mathbf{g} \\leftarrow \\frac{\\nabla _{\\mathbf{x} _t} l(\\mathbf{x} _t) }{ \\|\nabla _{\mathbf{x}_t } l( \mathbf{x}_t ) \\|_2} \\\\
    &\\qquad \\lambda _t \\leftarrow \\min \\{ \\lambda _{\\max}, t / (1-t) \\} \\\\
    &\\qquad \\mathbf{x} _{ t - \textcolor{red}{\\Delta t} } \\leftarrow  \\mathbf{x}' _{ t - \\textcolor{red}{\\Delta t} }  \\textcolor{red}{ - } \\lambda_t \\mathbf{g} \\\\
    & \\textbf{end for} \\\\ 
    & \\textbf{return } \\mathbf{x} _0
    \\end{aligned}

	Some additional comments on Algorithm 1: 
	* What does $\\mathbf{x} _{t-1}$ mean? Is $t$ an index or the real-valued time $t \\in [0, 1]$? In $\\mathbf{x} _{t-1}$ it seems to be an index, in $\\mathbf{x}_0, \\mathbf{x}_1$ it indicates the time.
	* In your version, we have $t = 0$ in the last integration step such that $\\mathbf{x}_{-\\Delta t}$ is computed. But it does not make sense to decrease $t$ further after reaching the data distribution at $t = 0$. So the loop should end at $t = \\Delta t$. 
	* Increasing the loss $l(\\mathbf{x}_t)$ does not make sense (most likely a typo or subsequent error of line 196). 
	* In Algorithm 3, the same errors occur as in Algorithm 1.

5) Again, please clarify the meaning of $t-1$ in $\mathbf{x}_{t-1}$ and avoid division by 0 in $1/(Nt)$ in the (unnecessary) last iteration.

6) Symbol $\theta$ is overloaded: In most cases, $\theta$ indicates the parameters of the foundation model. But in the discussion of the missing wedge dataset it indicates the tilt angle. 

7) It is confusing to use multiple versions of the flow. We see $v_t(\mathbf x_t)$, $v_\theta(t, \mathbf x_t)$ throughout the paper. Moreover, since the flow is a vector field, it should be bold face according to the ICLR guidelines. 

# Minor comments

1) The specific number of 38,626 cryo-EM structures mentioned in the abstract will most likely be outdated at the time when your paper is published.

2) In line 095, you write "... which is then able to generate a posterior distribution $p(x|y)$." This is incorrect: Sampling with $v_t$ can only __approximate__ the posterior distribution.

3) Typos/grammar: 
	* Page 7: "scaler"
	* Line 525: "We ... leave for future work."

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work is in the field of cryogenic electron microscopy (cryo-EM), a microscopy technique that can be used to study biological structures and macromolecules (e.g. proteins). Cryo-EM produces 2D projections of a structure, which are then used to estimate a 3D map, parametrized as a voxel array, representing the structure.

This paper addresses the problem of how to incorporate knowledge from the large database of existing high-quality 3D cryo-EM density maps into the process of estimating and refining new density maps from cryo-EM data. In the language of inverse problems, this problem translates to the question of how to obtain a prior for cryo-EM density maps.

The authors propose CryoFM, a generative deep learning model that captures the prior distribution of high-resolution cryo-EM density maps. After pre-training the model on a large dataset of cryo-EM density maps, the authors show that it can be used as a prior to regularize inverse problems where a 3D density map must be estimated from corrupted measurements of the underlying object. As examples of such inverse problems, the authors consider 3D denoising tasks and the problem of estimating the 3D density of an object from a few 2D projections of the density. To learn the prior from the data, the authors use techniques from flow matching (similar to denoising diffusion models).

**Recommendation**: In my opinion, the paper is above the acceptance threshold: Judging from the experiments, CryoFM is a good and versatile prior for cryo-EM, and the authors have done good work in the promising direction of learning a cryo-EM prior from data (see "Strengths")! *However*, parts of the paper should definitely be revised before acceptance. I find parts of the paper really hard to understand, and context and details are missing in some places (see "Weaknesses").  
I will raise my score to "Accept" if my concerns related to the paper's clarity (see "Weaknesses") are sufficiently addressed.

**Post-Rebuttal:** I appreciate the authors' additional clarifications and increase my score from 6 to 8. Overall, the paper is an interesting case study of how to learn and use a prior for reconstruction and denoising in cryo-EM.
I also appreciate that the authors have made their training dataset publicly available (see "General Response"). I could not find the figshare link in the paper. I strongly encourage the authors to add the link to the paper, because I consider the dataset to be a valuable resource for future work in the direction of learning priors.

### Strengths
- The idea of learning a prior from data is promising. Work in other domains has shown that priors learned on large datasets can outperform classical, hand-crafted priors that, for example, model assumptions like smoothness or sparsity.
- The authors use the learned prior to solve four relevant inverse problems: two 3D denoising problems, the missing wedge problem (which deals with estimating missing data in the Fourier domain), and ab-initio modeling, which is the problem of estimating a 3D density from 2D projections of Cryo-EM.
- For all four inverse problems, the CryoFM-based approaches perform as well as or better than the baselines (see Table 1, Table 2, Figure 7), suggesting that CryoFM is a versatile and expressive prior.
- For ab-initio modeling, the authors tested CryoFM on two real-world datasets.
- All figures are of high quality.

### Weaknesses
In many places, the paper is hard to understand and details and context are lacking. For example:

- I find the theory of the flow-matching approach for training the prior very difficult to understand. This is especially true for Section 3 and Section 4.3, which together make up about 1.5 pages. In particular, important concepts and equations are not explained, making it difficult to understand their meaning. For example:
	- In lines 159 to 162, the authors state that the learnable vector field generates a probability density path, but I could not find an explanation of what such a path is or how the vector field relates to a probability density function. It's unclear how the vector field, which is a function of time and position, defines a path in the probability density space. The connection between the vector field's output and the evolution of the probability density needs to be made explicit. Furthermore, the concept of a 'path' in probability density space is not standard and requires a more thorough explanation.
	- I could not find a definition or explanation of the variable (or function?) $\hat{\mathbf{x}}_0$ (lines 186-187), which appears many times in the paper and is an important part of the flow posterior sampling (algorithm 1). It is not clear if $\hat{\mathbf{x}}_0$ is a deterministic function of $\mathbf{x}_t$ or a random variable, and how it is computed from the learned vector field. The lack of clarity around this term makes it difficult to follow the posterior sampling algorithm.

 - I cannot judge the novelty of the variant of flow matching used in the paper. If the variant contains novel elements, the authors should explain them and highlight the differences to existing work more clearly. It's not clear if the authors are using a standard flow matching approach or if they have introduced modifications. If modifications exist, they should be clearly stated and justified. The paper should explicitly state the differences between the proposed approach and existing flow matching methods.

- Details and context are missing in some places in the experiments. For example:
	- The authors use EMReady, DeepEMhancer, and spIsoNet as baselines for the experiments in Section 5.1 and Section 5.2. They briefly introduce these baselines in lines 116 - 120, but I find this explanation insufficient to understand what the baselines actually do, why they were chosen, and how they relate to CryoFM. The descriptions of these baselines are too brief and do not provide enough information to understand their underlying mechanisms. A more detailed explanation of each baseline, including their specific algorithms and how they are used for denoising, is needed.
	- In the denoising experiments in Sections 5.1 and 5.2, it is not clear what the test set is. The paper does not specify how the test set was generated or if it is a subset of the training data. The size and composition of the test set should be clearly described.
	- The motivation for studying anisotropic denoising (Section 5.2) is not entirely clear to me. Why does the noise affect "some orientations more than others"? Is this related to the preferred orientation problem, i.e. that some particles adopt certain orientations more often than others?

Other weaknesses:
- The authors propose a novel prior for solving inverse problems related to cryo-EM, but there is no discussion or experiment comparing CryoFM with existing priors, e.g. the Gaussian prior by Scheres et al. mentioned by the authors in line 38. One possible idea is to compare, for example, the Gaussian prior to CryoFM for regularizing ab-initio modeling. The paper should include a comparison with the Gaussian prior, which is a standard approach in cryo-EM. This would help to understand the advantages and disadvantages of CryoFM compared to existing methods.

- In Section 5.4, the authors use CryoFM for ab-initio modeling and compare it to cryoSPARC. It seems to me that cryoSPARC uses 2D projections of the particle directly, while CryoFM uses class averages. This difference in input data could be problematic when comparing the methods. This raises two questions:
	- Why did the authors use cryoSPARC as baseline? 
	- Is there another ab-initio reconstruction method that works with class averages?

### Questions
- In Section 5.4, the authors show that CryoFM can be used for ab-initio modelling where a low-resolution density map is estimated from 2D projections. Can CryoFM also be used to estimate high resolution density maps from projections? Can CryoFM be for example incorporated in the "Refinement" step (done here with cryoSPARC)?


Note that I also raised some questions in the "Weaknesses" sections. They seemed more appropriate there.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study introduces CRYOFM, a foundation model using flow matching to learn and generalize the distribution of high-quality density maps. CRYOFM serves as a flexible prior for multiple tasks in cryo-EM and cryo-electron tomography (cryo-ET), achieving state-of-the-art performance across applications without fine-tuning, underscoring its potential for broad use in these fields.

### Strengths
1. The development of a foundation model for cryo-EM is both significant and novel
2. The use of flow matching to capture the prior distribution, along with the flow posterior sampling method as a flexible prior for various downstream tasks, is technically sound
3. Overall, the paper is well organized

### Weaknesses
1. While CRYOFM serves as a foundation model, it currently lacks demonstrated general applicability and versatility. As noted by the authors, further experiments across diverse tasks, such as 2D-to-3D reconstruction, would be beneficial to substantiate its broader utility. Specifically, the current evaluation focuses on relatively simple tasks like denoising and ab initio modeling from clean class averages. The ability of CRYOFM to handle more complex scenarios, such as heterogeneous datasets or those with significant conformational variability, remains unclear. The absence of experiments directly using raw particle data for 3D reconstruction is a notable gap in demonstrating its practical applicability as a foundation model.
2. CRYOFM relies on synthetic noise for denoising tasks. Testing on real datasets (realistic noise) would be necessary to validate its effectiveness in real-world applications. The use of spectral noise, while a common model, may not fully capture the complexities of real-world noise in cryo-EM data, which can include artifacts from the microscope, ice contamination, and other sources. The evaluation should include a more comprehensive assessment of the model's robustness to various types of noise and artifacts.

### Questions
1. For the ab initio modeling approach, comparisons with established methods such as CryoDRGN2 and CryoFIRE would strengthen the evaluation of CRYOFM’s performance.
2. Regarding Figure 7, it would be interesting to see if using the same dataset with CryoSPARC actually improves performance.
3. Curious about effectiveness of the 2D to 3D reconstruction approach, particularly when only a limited set of 2D views is available

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a flow-based diffusion foundation model for 3D electron density maps of proteins as measured via cryogenic electron microscopy and tomography. This foundation model is then used as a prior for several 3D reconstruction and denoising tasks all framed as inverse problems: 3D density map denoising with spectral noise, 3D density map denoising with anisotropic noise, missing wedge restoration (for cryo-electron tomography), and ab initio reconstruction for cryo-electron microscopy from 2D projections.

### Strengths
There are many downstream protein-related modeling and reconstruction tasks that stand to benefit from an accurate model of the distribution of 3D protein density maps. The paper demonstrates applicability to several such tasks, and there are many more for which the proposed foundation model may be useful.

### Weaknesses
 - The motivation for using a flow-based model is not very clear
- Related work discussion could be improved. I would suggest mentioning Chroma, a foundation model for protein structures that was published in 2023: https://www.nature.com/articles/s41586-023-06728-8. My understanding is that the main difference for the proposed model is that it operates in the space of 3D electron density maps rather than discrete protein models, yet for many cryo-EM tasks either or both models might be useful (e.g. https://arxiv.org/abs/2406.04239 this recent paper uses Chroma as a diffusion prior for several protein inverse problems). The authors might also consider discussing DiffModeler (https://www.nature.com/articles/s41592-024-02479-0), which also proposes a protein diffusion model that can denoise 3D density maps (preprint was posted in January 2024 but the published version was just released a week ago).
- Also pertaining to related work, the paper would benefit from a richer description of the specific baselines that are used for comparison in the experiments. These baselines are introduced in lines 116-120 but there is not enough detail to really judge what is similar and different about the mechanism of each model in the comparison.
- The experiments on anisotropic noise are not clearly motivated. It would seem to be somewhere in between the realistic noise models for cryoEM and cryoET, but both of these are separately considered so I don’t see much added value to consider anisotropic noise unless there is a measurement setting where it arises (that is not already covered by other experiments).
- There are specialized versions of the algorithm used for several of the applications, yet these modified algorithm descriptions are in the appendix rather than the main text. I realize space is limited but it would be preferable to have at least a description of the algorithm modifications in the main text.
- I am very happy to see experiments on ab initio reconstruction, but unfortunately the results in this setting are not all that compelling since the final quality is similar or slightly worse than CryoSPARC. Please refer to some questions about this experiment in the questions section.

Minor points
- The forward operator A is described as a “degradation operator”. In some cases this is accurate, such as when the measurements are noisy, but in other cases (such as ab initial reconstruction) my understanding is that A denotes projection rather than some form of degradation. Calling A a forward model/operator or measurement model/operator would be more consistent with the inverse problems literature.
- There is a typo on line 231; Transformer is misspelled.
- Figure 3: the colors for CryoFM and DeepEMhancer are too similar in the FSC curve. Another strategy would be to change the opacity or style of the lines so that both lines are visible even when they overlap.

### Questions
Most important questions:
- For the ab initio reconstruction experiments: (1) why not use many noisy projections instead of a few averaged/denoised projections? This would be more realistic to modern practice and more similar to CryoSPARC. (2) why not use CryoFM for refinement as well as initialization? Since you have a high-resolution foundation model I expect that you might see improvement by using it at the refinement stage.
- Do the authors plan to release their code and pretrained foundation model to the research community? My preference for paper acceptance assumes that these will be released.

Minor questions:
- Does the FM in the title stand for “foundation model”, “flow matching”, or both?
- Line 209-210 says that proteins with helical structures are removed from the pretraining dataset. Then line 348 says that the proposed method enhances “the resolution of helices and loops”…why were helical structures removed from the pretraining dataset if they will be important in the test dataset?
- What is the motivation behind the specific data augmentations that were used for CryoFM-S and CryoFM-L?
- Figure 9 does not show results for ab initio reconstruction; why?

### Soundness
3

### Presentation
3

### Contribution
3
