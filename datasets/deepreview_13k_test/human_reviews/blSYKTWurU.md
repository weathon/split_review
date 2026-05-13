# Decomposed Direct Preference Optimization for Structure-Based Drug Design

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
Diffusion models have achieved promising results for Structure-Based Drug Design (SBDD). Nevertheless, high-quality protein subpocket and ligand data are relatively scarce, which hinders the models' generation capabilities. Recently, Direct Preference Optimization (DPO) has emerged as a pivotal tool for aligning generative models with human preferences. In this paper, we propose \method, a structure-based optimization method aligns diffusion models with pharmaceutical needs using multi-granularity preference pairs. \method introduces decomposition into the optimization objectives and obtains preference pairs at the molecule or decomposed substructure level based on each objective's decomposability. Additionally, \method introduces a physics-informed energy term to ensure reasonable molecular conformations in the optimization results. Notably, \method can be effectively used for two main purposes: (1) fine-tuning pretrained diffusion models for molecule generation across various protein families, and (2) molecular optimization given a specific protein subpocket after generation. Extensive experiments on the CrossDocked2020 benchmark show that \method significantly improves model performance, achieving up to 95.2\% Med. High Affinity and a 36.2\% success rate for molecule generation, and 100\% Med. High Affinity and a 52.1\% success rate for molecular optimization.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose to apply DPO to structure-based drug design. Authors formulate the DPO objective for diffusion models and suggest to apply it separately to different molecular fragments. Besides, authors propose to use the linear scheduling of the DPO regularization. Finally, authors incorporate physically-constrained optimisation to improve the geometry of the generated molecules. Overall, in my opinion, the work has interesting ideas and suggestions. However, the chosen evaluation methodology and the current results do not prove that the proposed techniques are beneficial at all. I discuss the weaknesses in details below, and believe there is a substantial scope for improvement. I will be happy to reconsider my decision after the rebuttal.

### Strengths
I find the proposed idea on the local DPO for molecular fragments very interesting and original and can potentially help in specific tasks. I also like the idea about constrained optimisation and believe it can be used in diffusion models in general to imporve the quality of the molecules. Overall, applying DPO to improve specific properties of the generated molecule makes total sense and can help generate high-quality molecules in cases when the quality of the training data is not sufficiently high.

### Weaknesses
**Major issues:**
1. LocalDPO looks like the main contribution of this paper. However, the evaluation of this component does not prove that the proposed mechanism is crucial for sampling molecules with optimised properties. In fact, based on Table 4, it looks like the model without LocalDPO solves the task equally well (the differences in the scores are too small). I can imagine that the chosen evaluation method does not highlight the advantages of the LocalDPO and its unique feature – locality. So my main question for which I struggle to find an answer in the paper: why would I use LocalDPO instead of the global one?

2. The same applies to the physical constrained optimisation. Tables 5 and 6 suggest that DPO doesn't improve the geometry of the molecules.

3. I am also confused about utilisation of different objectives in LocalDPO and GlobalDPO. In the implementation details, authors mention that they use QED, SA, and Vina Minimize Score. Does it apply to both local and global DPO components? If yes, then I do not understand the point of LocalDPO since neither QED nor SA are additive by fragments. If not, then all the main results concern only Vina optimisation, and I would recommend to make it more clear.

4. I am not entirely convinced by the claim regarding the improvement of molecular conformers in terms of energy (lines 428 - 458). First, in my opinion, the difference between distributions of values of DecompDiff and DecompDPO in Figures 4 (right), 5 and 6 is too small to say that DecompDPO is better. Second, why would it be better? The only geometric properties the model is optimized for are bond distances and bond angles. But I believe that having "correct" (i.e. within the distribution of the real data) bond distances and angles is only the necessary condition for the low conformational energy, but not sufficient. Besides, it is clear from Tables 5 and 6 that DecompDPO doesn't outperform DecompDiff in this regard. Therefore, the argument for improved molecular conformation feels unsubstantiated.

5. Single objective optimisation section (and Table 3) confuses me a lot:
* 5.1 Why do authors discuss improvements of QED and SA of the model that was optimized for affinity score only? How can these improvements be explained?
* 5.2 Why not to optimise separately for SA and for QED and then show how these scores improve after the corresponding optimisation? I believe that it is important to demonstrate the consistent ability to optimise different unrelated scores in separate experiments.
* 5.3 How does connectivity and validity depend on the fact that the model is optimised for Vina scores? To me this effect looks arbitrary and doesn't have any rationale behind (similar to what I discussed in 4.1). I agree that it is a good idea to discuss validity and connectivity, but I would suggest to do it in a different context – as a sanity check that demonstrates that the molecules generated by DecompDPO are in general adequate (for example, as an Appendix table).

**Minor comments and suggestions:**
1. Figure 4 (left) is not very informative – in my opinion it can be put to the appendix.
2. For clarity of the made arguments and to improve the overall structure of the paper, I believe that it would be beneficial to have another table in the main text with the key geometric scores: i.e. JS divergence between distances (values from the Figure 4 (left) legend), JS between angles, avg. conformer energies. At least, in my opinion, some comparison of angles should be in the main text, since authors provide equation (12).
3. Maybe we cannot see the DPO effects on bond distances and angles because $3\sigma$ (in equations 11 and 12) is a very loose threshold? What if to try just $\sigma$?
4. Line 472: Table 4 -> Table 3
5. Docking evaluation:
* 5.1. I believe that reporting scores after minimization or docking may not fully align with the goal of the proposed model, which is to generate 3D molecular structures that inherently adopt good binding conformations. Rather than presenting redocked and minimized structures, I would suggest evaluating the number of steric clashes between proteins and ligands, as this could provide a more direct assessment of the generated conformations’ suitability for binding.
 * 5.2. Due to the high correlation between the docking scores and molecule sizes, I would recommend reporting binding efficiency scores (i.e. docking score divided by the number of heavy atoms). I believe it provides a better signal of the potency of the generated molecules.
6. I would be curious to look at the validity and connectivity metrics - as an overall quality assessment of the DecompDPO molecules. Also would interesting to see the percentage of the samples that pass PoseBusters filters.

### Questions
1. Figure 4 (right): what does fragment size on x-axis mean? (Average?) number of atoms in the fragments? Or (average?) number of fragments in the molecules?
2. How are the fragments without rotatable bonds computed (in the section about MMFF evaluation)?
3. It would be interesting to look at the distributions of the scores in winning and loosing examples in the created dataset for preference alignment.
4. Do I understand correctly that linear $\beta$-schedule means that in cases when t is large enough (i.e., closer to the beginning of the denoising trajectory) the DPO loss is scaled by a large number? And does it mean that effectively the model learns to align only the later stages of the denoising process?
5. Did authors try to use (11) and (12) as penalties while training the diffusion model itself? Looks like it is a nice additional penalty in general
6. How do authors select the size of the sampled molecules? Is the distribution of sizes in samples the same with and without DPO?

### Soundness
1

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
4

### Summary
In this paper, the authors propose DecompDPO, a method that applies Direct Preference Optimization (DPO) in a diffusion model for structure-based drug design (SBDD). In addition to the global DPO loss, which focuses on binding affinity as evaluated by AutoDock Vina, the paper introduces local DPO and a bond angle penalty to complement global DPO, aiming to improve ligand-protein binding affinity. DecompDPO achieves competitive performance on vina results compared to other selected baselines.

### Strengths
Thanks for the good work on exploring the DPO method in decomposed diffusion for SBDD. I found the work to have the following strengths:
1) The method achieved decent performance on vina score, vina min, and vina dock without significantly compromising on QED and SA scores compared with the baselines selected in the paper.
2) The paper is clearly written, easy to follow, and has well-designed figures.
3) The paper introduces the use of Local DPO for optimization, which goes beyond global DPO.

### Weaknesses
1. Performance claims in the paper

DecompDPO did outperform all selected baselines in terms of vina score, vina min, and vina dock, as mentioned in the paper. However, the paper did not benchmark against some other existing works that demonstrate better performance in improving the conditional sampling of diffusion models for SBDD. For example, KGDiff[1], a guidance-based method, has better performance on vina score, vina min, and vina dock. Both KGDiff and DecompDPO were benchmarked on the same test set with 100 test pockets and 100 samples per pocket. While I understand that vina results are not a precise measure of binding affinity and that not being SOTA in vina results does not necessarily mean the method is not good, I would still be cautious in stating that "DECOMPDPO achieves the highest score in Vina Minimize, Vina Dock, High Affinity, and Success Rate among all generative methods" in the paper.

2. Performance on Vina Score

DecompDPO shows good performance on vina min and vina dock, but the marginal improvement on vina score is small. Vina score directly reflects the quality of the sampled pose, while vina dock evaluates the quality of the pose sampled by the model and then optimized by AutoDock Vina. The results in the paper indicate that the improvement in the pose directly sampled from the generative model is minimal.

3. Effectiveness of Local DPO

Although local DPO is a novel idea compared to global DPO (e.g., AliDiff), Table 4 shows that the improvement brought by local DPO is marginal compared to global DPO. This raises questions about the effectiveness and real contribution of local DPO toward the overall improvement of local+global DPO.

Reference:
[1] KGDiff: towards explainable target-aware molecule generation with knowledge guidance

### Questions
Could the authors please provide the complete rates for the DecompDPO and DeompDiff baseline molecules? When running AutoDock Vina, in 100 samples for a pocket, only the successfully reconstructed molecules (usually fewer than 100 and sometimes around 50–60/100 for larger pockets) proceed to the vina docking process. This means the vina results in the table for all methods are actually calculated from fewer than 10,000 samples. It would be helpful to benchmark the method using this complete rate alongside the vina results. Thanks!

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a new diffusion model for structure-based drug design that improves molecular properties (docking score, drug-likeness score, and synthesizability score) of a base model using Direct Preference Optimization (DPO). In addition to straightforward application of diffusion-DPO on the molecular level, the authors propose to apply a more fine-grained version at the fragment level to further improve their results. 
The method's performance is assessed in a multi-objective fine-tuning experiment as well as a target-specific optimization setup.

### Strengths
### Motivation & ideation

I believe user preference-guided optimization of generated molecules is an important frontier in structure-based drug design. The presented work is a promising extension of the capabilities of recent machine learning models for this task. It builds on various ideas established in prior works on decomposed diffusion models [1], decomposed molecule optimization [2], and preference optimization for molecules [3], and is a sensible extension thereof. Applying the diffusion DPO loss at a substructure level for decomposable objectives makes sense and likely leads to more efficient training. Some benefits of this approach are also shown empirically in this study (Table 4).
Furthermore, to the best of my knowledge the paper represents one of the first applications of DPO to small molecule design (together with Ref. [4]) and thus provides a novel view on the drug design problem.


### Experimental setup

The chosen experimental setup looks reasonable to me and includes useful comparisons and baselines.
It also already contains most relevant ablation studies, including local (substructure) DPO vs purely global DPO and the proposed schedule for the regularization parameter $\beta$.
The presented results are consistent with the underlying hypotheses and support the proposed preference alignment strategy for molecular diffusion models.


### References

[1] Guan, Jiaqi, et al. "DecompDiff: diffusion models with decomposed priors for structure-based drug design." arXiv preprint arXiv:2403.07902 (2024).

[2] Zhou, Xiangxin, et al. "DecompOpt: Controllable and Decomposed Diffusion Models for Structure-based Molecular Optimization." arXiv preprint arXiv:2403.13829 (2024).

[3] Zhou, Xiangxin, et al. "Antigen-Specific Antibody Design via Direct Energy-based Preference Optimization." arXiv preprint arXiv:2403.16576 (2024).

[4] Gu, Siyi, et al. "Aligning target-aware molecule diffusion models with exact energy optimization." arXiv preprint arXiv:2407.01648 (2024).

### Weaknesses
### Empirical results

While the conceptual arguments for the proposed techniques are strong and well-motivated, the empirical results are currently less convincing. The performance improvement compared to the base model is only moderate in most reported metrics (e.g. QED and SA scores in Table 1). Here, it would be useful to put these results into perspective somehow. The authors could, for example, discuss potential ways to increase the performance gap between base model and optimized model. It would be natural to ask if more DPO fine-tuning iterations/epochs can further increase the optimized scores. If that is not the case, it would at least be interesting to know why.

Moreover, when directly optimizing a limited number of target metrics, it is easy to "break things". The evaluation should therefore include additional sanity checks for the generated molecules. The reported _Complete Rate_ is a good first step but a larger set of diverse metrics and checks (e.g. PoseBusters filters as mentioned in the questions below) would increase my confidence in the findings.

### Baselines

The main benchmark in Table 1 contains a representative set of popular structure-based drug design models. However, I would consider these baselines rather weak in this context as most of them were trained to reproduce the training data distribution whereas DecompDPO directly aims to optimize Vina score, QED and SA. More relevant baselines are only considered in the _Molecule Optimization_ section.
Maybe the authors could consider including the same or similar baselines methods in Table 1 as well.

Given the arguably low bar, I find it surprising that DecompDPO does not show larger improvements compared to the presented baseline methods. To give a concrete example, by simply matching the SA values from the dataset (_Reference_) Pocket2Mol seems to achieve better SA scores than DecompDPO which includes SA in its preference alignment scheme.


### Ablation studies

The paper already investigates the impact of many design choices. However, I would also like to see how longer DPO training affects the results. It is currently unclear why the models are only fine-tuned for one epoch. Would longer training improve results or only degrade other molecular properties?
The paper also introduces a physics-inspired constraint on bond and angle geometries and makes claims such as "The physics-informed energy term penalizing the reward is beneficial for maintaining reasonable molecular conformations during optimization" (Conclusion section), but no empirical evidence is provided.

The ablation of the multi-objective optimization approach produced another unexpected result. QED and SA values in the single-objective case (only optimizing for Vina score) are as good or even better than in the multi-objective setup. 
It would be good to see an attempt at explaining this outcome and/or a discussion of the implications for the multi-objective approach. 

### Discussion

Given some of the surprising results stated above, I believe the paper would benefit from a more in-depth discussion of its empirical findings. It would certainly help to better understand the current limitations of the method.

### Questions
- Why is the model only fine-tuned for one epoch? How does longer training affect the target metrics and other molecular properties?

- Is there a trade-off between the target metrics and other molecular properties? Does the general molecular quality degrade when the reward is optimized more aggressively? The PoseBusters [5] filters are widely accepted criteria to perform general sanity checks for molecules, and could be used to answer this question.

- What molecular fragmentation method is used? I could not find this important methodological detail in the paper.

- I would advise to add an ablation study to systematically evaluate the contribution of the physics-informed reward term.

- Optionally, a more extensive evaluation could also include methods like REINVENT [6] or other reinforcement learning/GFlowNets-based approaches that typically do not model molecules explicitly in 3D but can still optimize binding oracles implicitly and are usually strong baselines for molecule optimization tasks.



### Minor comments
- Figure 1: all symbols should be explained in the Figure legend
- lines 177-178: all symbols need to be defined ($\mu_{1:K}$, $\Sigma_{1:K}$, $H$); it would also be useful to describe the data-dependent priors in more detail
- Section 3.1: this section introduces loss components $L_t$ per time step but, in my opinion, should also provide the overall loss function that involves sampling and aggregation of time steps
- Figure 2: font size of axis labels should be increased
- Table 1: in my opinion, the most interesting comparison is the one between the base model, DecompDiff*, and the fine-tuned model to assess the effect of the proposed preference alignment approach. It would be easier to compare the metrics if these two models were presented right below one another in the table.
- When discussing baselines in Section 4.1, it would be interesting to know what rewards RGA and DecompOpt are optimizing for. This would help put the results discussed later into perspective.
- Line 472: the referenced table should be _Table 3_
- Equation 9: sign$(x>y)$ is quite unconventional. I recommend to use sign$(x-y)$ instead
- Equations 8 and 9: the definition of $M_t^+$ and $M_t^-$ as the union of $M^{(i)}$'s can be moved out of the expectation index


### References

[5] Buttenschoen, Martin, Garrett M. Morris, and Charlotte M. Deane. "PoseBusters: AI-based docking methods fail to generate physically valid poses or generalise to novel sequences." Chemical Science 15.9 (2024): 3130-3139.

[6] Loeffler, Hannes H., et al. "Reinvent 4: Modern AI–driven generative molecule design." Journal of Cheminformatics 16.1 (2024): 20.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
DecompDPO introduces substructure decomposition into the Direct Preference Optimization of a diffusion model for structure-based drug design. It has two primary uses: fine-tuning diffusion models across various protein families and secondary optimization post-generation. DecompDPO also directly aligns itself with preferences using two forms of DPO: Global over molecule pairs and Local over substructures. DecompDPO was benchmarked on existing CrossDocked2020 benchmarks.

### Strengths
Overall, DecompDPO shows a well-done approach to taking complex decomposed molecule diffusion models and optimizing them for easy-to-calculate chemical properties. Many components of the DPO optimization are specific to the way DecompDiff frames the arms and scaffolds of molecule generation. The work in Appendix D.2 is really interesting and would suggest being a primary focus of the paper as this is where the most novelty as it pertains the DPO setup is.

- DecompDPO shows 8% improvement over base model DecompDiff due to DPO fine-tuning with a single epoch of  63K pairs with a pretraining dataset of 100K.
- DecompDPO brings in several innovations from prior methods, including DecompDiff and the bond-first noise schedule, into a single model.
- DecompDPO adds structural queues from bond distances and angles to derive the DPO reward
- From Table 2, it is clear that fine-tuning for multi-objective preferences improves base unaltered predicted structure compared to prior optimization methods on top of DecompDiff.

### Weaknesses
Overall, the paper combines many techniques from prior works, but the benchmarking is quite sparse regarding critical ablations. Many architectural and DPO-specific optimization choices are not ablated, although the proposed novelty is such. As a result, it's hard to understand where the method works and why.

- Relevant prior work [1] is not included, which discusses [3] and CrossDocked Benchmark implications and diffusion multi-objective optimization. 
- Vina Dock, as it randomizes all torsions to start, has little bearing on the strength of the structure aspect of the generative model. 
  - [2] demonstrated that an LLM without 3D information can achieve a success rate of 86.4% and an average Vina Dock of -10.27 kcal/mol by optimizing for docking score directly 25.6x faster than DecompOpt.
  -  The molecular properties like QED and SA are also improved by leveraging a pretrained LLM that only guides Vina Dock, whereas the property-aware optimization of DecompDPO does not yield significant gains.
-  The ground truth CrossDocked2020 data was generated with SMINA docking, and as a result, most of the cross-docked ligands (i.e., non, co-crystal) do not exhibit the desired protein-ligand interaction. As a result, benchmarks such as PoseCheck [3] allow for a better but still imperfect comparison but are not included.
- Given that the structures generated from the AliDiff model have better affinity according to the Vina Score, the fact that DecompDPO structures could be optimized with external force fields or dynamic torsion sampling is not all that valuable compared to non-diffusion methods. 
   - **Q:** Why does the multi-objective DPO fair worse than the energy-focused version of AliDiff? Could the regressions stem from the IPDiff vs DecompDIff underlying architecture and training? A deeper study of the underlying DPO method agnostic to the architecture would be very interesting as unless one is to use DecompDiff can someone use DecompDPO?
  -  If Vina Dock, QED, and SA score are desired, there are prior methods that are much faster to achieve that [2]. 
- The complete rate is the lowest of all tested methods, which is the first and most important benchmark as it shows how well the model can function beyond whether the molecules are good or not.
  -  **Q:**  Is there a deeper analysis as to why 35% of the generated molecules are not connected and/or valid? 
  - This seems unexpected as the bond diffusion schedule that was used was specifically chosen to generate connected molecules. 
  - **Q:**  For evaluation, does this mean that of the 100 molecules generated, the benchmarks are calculated over the 65 valid molecules?
- A lot of focus is put on adding energy terms to improve the molecule's conformation, but DecompDPO has worse bond distances than DecompDiff for 5/8 bond types and 6/7 bond angles. 
  - **Q:**  Does this part of the reward add anything of value if it hurts the generated structures?
- Overall, it is clear DecompDPO is better than DecompOpt, but more ablations are needed to understand where the improvements and regressions are coming from.
  - **Q:**  Could a similar DPO scheme be applied to TargetDiff, and would similar regressions occur?

[1] PILOT: Equivariant diffusion for pocket conditioned de novo ligand generation with multi-objective guidance via importance sampling https://arxiv.org/abs/2405.14925

[2] EvoSBDD: Latent Evolution for Accurate and Efficient Structure-Based Drug Design https://openreview.net/pdf?id=sLhUNz0uTz

[3] PoseCheck: Benchmarking Generated Poses: How Rational is Structure-based Drug Design with Generative Models? https://arxiv.org/abs/2308.07413

### Questions
For most questions, see weaknesses.

- DecomDPO performs iterative DPO, optimizing the model for each target protein in the test set. Does this mean a new model is trained for each test set pocket? If so, what happens if you only do standard DPO fine-tuning as done in AliDiff?

- On line 350 it appears to describe that DecompDPO samples 500 molecules per 100 test pocket for table 1. Do the benchmarks reflect the average over all 500 or is it some filtered subset? 

- What is the inference time, and how does it compare to prior methods factoring in the complete rate?

- What happens if you fine-tune TargetDiff on the DPO fine-tuning dataset as done in AliDiff? It would be interesting to see of the decomposed objective yields better training data.

- Where are results showing fine-tuning pretrained diffusion models for molecule generation across various protein families (line 21-22)? There is no notion of protein families discussed in existing CrossDocked2020 benchmarks.

Nit: Line 77 says DecompDPO was the first, but line 80 says AliDiff was the first to use preference alignment.

### Soundness
2

### Presentation
2

### Contribution
1
