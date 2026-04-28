# VFDiff: SE(3)-Equivariant Vector Field Guided Diffusion Model for Target-Aware Molecule Generation in 3D

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8

## Abstract
Structure-based drug design (SBDD) is a key challenge in drug discovery that aims to generate small molecules capable of binding tightly to specific protein pockets. However, current diffusion models have focused on the complementarity of ligand molecules and protein pockets in physical space while ignoring the docking energy requirements,  resulting in only generating suboptimal docking postures. In this paper, we present VFDiff, a novel SE(3)-equivariant diffusion model for 3D molecular generation, guided by vector fields derived from protein-ligand binding energy. In contrast to current diffusion models, VFDiff incorporates energy-based guidance in both forward and reverse processes to ensure ligand molecules are spatially complementary and energetically matched to their target pockets. Our approach includes three fundamental mechanisms: energy-planning, which adjusts diffusion trajectories based on energy gradients; force-guiding, which refines molecular generation; and position-tuning, which improves sampling accuracy. Extensive experiments on the CrossDocked2020 dataset demonstrate that VFDiff outperforms state-of-the-art methods, achieving superior binding binding affinity with an impressive Avg. Vina Score of up to -7.37, while maintaining competitive molecular properties, and diversity. This work introduces a new framework for generating target-specific molecules with improved structural and functional fidelity, offering a significant advancement in SBDD.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes VFDiff, a novel SE(3)-equivariant diffusion model for structure-based drug design (SBDD), focusing on enhancing the binding affinity of generated molecules. VFDiff is guided by a vector field derived from VFNet, a pretrained model learning binding information by predicting atomic positions and Vina Scores from perturbed data. The authors conduct comprehensive experiments against established baselines, showing VFDiff's superior performance in generating high-affinity molecules.

### Strengths
- The paper is well-written and easy to follow.
- Experimental results comprehensively show the effectiveness of VFDiff in improving binding affinity.

### Weaknesses
 - The introduction of a prior guided information in the diffusion process (i.e., energy-planning and force-guiding) is used in previous work and the authors do not point out their unique contributions relative to previous models.


### Questions
1. What is the novelty in Section 4.2 comparing to IPDiff?
2. What is the rationale for scaling the noise added to coordinates in VFNet training with $\eta \sim U(0, 0.5)$?
3. In Figure 10, the conformation of generated molecules appears worse than the reference ligands. Could the authors provide Jensen Shannon divergences of bond angles distributions?
4. Could the authors compare the generation efficiency of VFDiff to baseline methods?

### Soundness
2

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
The authors propose a diffusion model for structure-based drug design endowed with the affinity-based guiding strategy. To do this, authors include three components: force-guiding in diffusion process, and energy-planning and position-tuning in denoising process. Authors demonstrate that the generated molecules have a superior docking scores and perform on par with other methods in terms of other metrics.

### Strengths
1. I find the proposed position-tuning mechanism very interesting and original
2. The generated samples have better Vina scores than other state-of-the-art methods

### Weaknesses
Major:
1. The work looks very similar to IPDiff. Many parts of text, equations, figures and overall structure are almost copy-pasted from the IPDiff.
2. Technical mechanisms like prior-shifting and energy-planning are claimed to be the contributions of this paper, while they are adopted from IPDiff.
3. I believe that the style of this paper can be significantly improved:
- 3.1 The paper contains many instances of unclear language, grammar errors, and vague terminology. For instance, the meaning of the terms "spatial complementarity" (line 524) and "conditional prior" (line 144) is unclear to me.
- 3.2 The authors often use overly promotional language, which may detract from the objectivity of the work. For instance, "contributions" 2 and 3 are details of the method itself, which is already presented as contribution 1. Effectively I see two points to provide here: 1) "new" method with affinity guidance, 2) state-of-the-art performance.
4. Evaluation methodology:
- 4.1 In my opinion, some basic sanity checks like PoseBuster filters are missing. They allow to evaluate the overall adequacy of the generated molecules, checking if they are valid, connected, if the geometry of the molecules is correct, and if molecules don't have steric clashes.
- 4.2 The discussion around QED and SA metrics lacks clarity and seems inconsistent to me. If these metrics are deemed unimportant, it may be more effective to omit them from the discussion altogether. In fact, I believe that there is no reason expect these metrics to exceed the values in the training set. You are training a diffusion model which is supposed to learn the underlying distribution by design, and you are not further optimising for these metrics.
- 4.3 Since you are introducing a diffusion model which primary goal is to learn the underlying distribution, I believe that reporting JS-divergence or Wasserstein distances between training and sampled distributions of a wider range of different metrics would be helpful to understand the distribution learning capabilities of your model. For example, you can additionally compute the distances between different bond angles and atom types. Distributions of some property approximators like QED, SA, logP, etc. could also strengthen the evaluation section. 
5. To me it looks like the only novel contribution of this work is position-tuning. I believe that this component can be helpful, and I like this idea in general. However, I wonder what exactly happens with $X_{0|t}$ upon position-tuning: what is the average error between $\hat{X_{0|t}^{\mathcal{M}}}$ and $X_0$ before and after position tuning in the sampling trajectories? Does it decrease as $t$ approaches to 0? Also, can you experimentally validate the hypothesis you suggest in lines 223-225? A deeper analysis of this component (potentially a separate section in Results) would be very interesting.
6. I found the explanation of position-tuning component in the end of section 4.1 very abrupt and unclear. For example, how is the position-tuning loss (4) is related to training the VFNet and losses (2)?
7. Motivation behind some design choices like introduction (as well as the choice of the values) of scaling coefficients $\eta$ are unclear to me.

### Questions
1. Why do you use "p" in eq 6 and "q" in eq 7?
2. Algorithm 1 (blue part): what is the difference between $\epsilon_1$ and $\epsilon_0$?
3. Algorithm 2 (blue part): why do you multiply by 10 in position-tuning?
4. Technical details: how did you assign bonds? How many molecules per input did you sample? How do you define pocket? What is the size distribution?

### Soundness
3

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
1.	This work introduce By incorporating energy-based guidance in both forward and reverse processes，VFDiff ensure ligand molecules are spatially complementary and energetically matched to their target pockets. VFDiff achieves the SOTA performance in SBDD scenarios.

### Strengths
VFDiff explicitly considers the energy complementarity between protein and ligand during the diffusion process. Therefore, it can generate three-dimensional molecules with better affinity in the process of generating protein-ligand complexes. This innovation is commendable.

### Weaknesses
Recently, many pocket-based three-dimensional molecular generation models have claimed to achieve state-of-the-art (SOTA) levels of affinity between protein and ligand when generating three-dimensional molecules. However, in most targets, the generated molecules often contain substructures that are difficult to synthesize, and collisions between the protein and ligand are very common. The authors did not provide enough molecular examples to demonstrate that these issues have been adequately addressed.

### Questions
1. When predicting forces with VFNet, it is necessary to know specific molecular information such as atom types and bond types. However, during sampling, VFDiff can only clearly provide atom types and bond types at the final step. I believe the authors need to clarify how they can provide accurate force information and position tuning information without knowing the molecular graph information in advance.
2. I look forward to the authors providing the code for reproducing the results during the review period to fairly evaluate whether the molecules generated by VFDiff have issues with synthesis and atomic collisions.
3. The authors should provide relevant results on the sampling efficiency of VFDiff.

### Soundness
3

### Presentation
3

### Contribution
4
