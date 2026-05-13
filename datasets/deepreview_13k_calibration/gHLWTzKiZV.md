# Composing Unbalanced Flows for Flexible Docking and Relaxation

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 6, 8, 8, 10

## Abstract
Diffusion models have emerged as a successful approach for molecular docking, but they often cannot model protein flexibility or generate nonphysical poses. We argue that both these challenges can be tackled by framing the problem as a transport between distributions. Still, existing paradigms lack the flexibility to define effective maps between such complex distributions. To address this limitation we propose Unbalanced Flow Matching, a generalization of Flow Matching (FM) that allows trading off sample efficiency with approximation accuracy and enables more accurate transport. Empirically, we apply Unbalanced FM on flexible docking and structure relaxation, demonstrating our ability to model protein flexibility and generate energetically favorable poses. On the PDBBind docking benchmark, our method FlexDock improves the docking performance while increasing the proportion of energetically favorable poses from 30% to 73%.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a new approach named Flexdock for flexible molecular docking and structure relaxation.  The model is based on Unbalanced Flow Matching (UFM), which relaxes the marginal constraints of FM through a more careful chosen coupling distribution and reduces the modeling complexity. This framework aims to address limitations in existing molecular docking techniques, particularly concerning protein flexibility and the generation of nonphysical molecular poses. From the experimental results on PDBBind benchmark, the proposed method well achieved this goal, especially in generating energetically favorable poses.

### Strengths
* As far as I know, the introduction of unbalanced FM in flexible molecular docking is novel.
* The authors analyze sample efficiency and approximation error with mathematical foundations.
* The introduction of energy-based loss for relaxation is reasonable and seems very useful in generating energetically favorable poses.

### Weaknesses
 * The introduction section lacks necessary citations. For example, in line 43, “Deep learning methods … often force the model to relearn protein folding”. What does “relearn” mean?  Please provide citations for such related work.
* In the related work section, the authors pointed out some related work but didn’t discuss the difference / advantages of their proposed method over related work.
* In methods section, the introduction of Eq3 and Eq4 is unclear. What’s their connection and how are they applied in practice? Specifically, it's not clear how the lower bound in Eq 3 is derived and how it relates to the actual optimization in Eq 4. The connection between the theoretical formulation and the practical implementation is not well-established.
* What is the influence of the choice of threshold c_{relax}? It's unclear how sensitive the method is to this hyperparameter and what the trade-offs are for different values. A more detailed analysis of this parameter's impact is needed.
* Have the authors tried using traditional (non learning based) energy relaxation methods like Rosetta as a step of post processing for baseline models and the basic FlexDock without proposed relaxation? I’m curious how it will perform compared to the proposed relaxation method.

### Questions
(Have already stated in the weakness section)

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
This paper extends Unbalanced Flow Matching (UFM), a novel approach to molecular docking that extends Flow Matching (FM) to better handle protein flexibility and generate physically realistic poses. The main innovation is allowing trade-offs between sample efficiency and approximation accuracy in the transport between distributions. The authors implement this in FLEXDOCK, which chains two UFM components: manifold docking for approximate pose prediction and structure relaxation for refinement. On the PDBBind benchmark, FLEXDOCK improves both docking accuracy and the proportion of energetically favorable poses compared to existing methods.

### Strengths
1. This paper attempts to address two critical limitations found in previous docking methods: the rigid assumption and the generation of non-physical structures.
2. The extensive experiments demonstrate the effectiveness of the proposed method. This paper demonstrates significant improvement in the PB-Valid metric, particularly with the simple yet effective energy loss.
3. The paper analyzes and formulates the flexible docking problem from the perspective of distribution transport, and extends the Flow Matching method specifically for this problem, supported by theoretical derivations.

### Weaknesses
The proposed method and experiments still assume prior knowledge of the binding pocket; despite this known pocket assumption, FLEXDOCK shows no significant improvement in RMSD-related metrics. This suggests that the manifold docking module may not make substantial progress in resolving the approximate pose compared to previous works. Furthermore, while the paper highlights improvements in the PB-Valid metric, it's unclear if this is primarily driven by the intramolecular or intermolecular components of the energy function. A more detailed analysis of these components would be beneficial. The lack of significant improvement in RMSD metrics, particularly All-Atom RMSD, raises questions about the practical impact of the manifold docking module. While the authors address the generation of non-physical structures, the core issue of accurately predicting the approximate pose remains a significant challenge. The paper would benefit from a more in-depth discussion of the limitations of the manifold docking module and its impact on overall performance.

### Questions
1. Is the manifold docking module capable of blind docking, or is it limited to pocket-based docking only? (This is not a request for additional experiments, but rather an inquiry about the capability of this method.)
2. How sensitive is the method to the choice of hyperparameters?
3. What insights do the authors have regarding previous ML-based approaches performing poorly on the PB-Valid metric? Based on the experimental results from diffdock-pocket (rigid), rigid docking methods still generate non-physical structures. Which component predominantly drives the PB-Valid metric in your experiments - intramolecular or intermolecular validity?
4. Compared to PB-Valid metrics, FLEXDOCK demonstrates no significant improvement in RMSD-related metrics. While RMSD remains a crucial indicator for evaluating approximate poses, one must question the necessity of pursuing validity and physicality when RMSD values are still low and approximate pose estimation lacks precision.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose FlexDock, a flow matching-based method for flexible small molecule docking. To address the problem of the limited availability of the bound protein structures, authors formulate Uncoupled Flow Matching, in which they tradeoff the approximation quality of the target distribution and the amount of samples needed from the prior distribution. Authors show that FlexDock outperforms other flexible docking methods in various metrics.

### Strengths
1. The proposed Unbalanced FM framework is a very neat idea and can be very useful in many different applications where the data from one of the distributions is limited
2. FlexDock demonstrates impressive performance across multiple metrics

### Weaknesses
1. In the motivation for the unbalanced flow matching authors say that due to the limited availability of the data points from $q_1$ (i.e. holo structures), the expected length of the flow will be large and the expected OT cost between $q_0$ and $q_1$ will be high. In my opinion, that would be true if there was a certain level of diversity in samples from $q_0$ (i.e. different apo structures) that correspond to a single (available) sample from $q_1$. But is it really the case for protein structures? I have a feeling that the diversity in apo structures of the same protein is not that high. I believe that the proposed method indeed improves learning the transport, as demonstrated in Figure 4. But I think it would be very beneficial to dissect this experiment and look at the flow distances and transport costs for different cutoffs, or even just plot these distributions for your training data. In my opinion, such a deeper analysis will strengthen the motivation a lot.

2. Authors suggest to use the coupling of the form $q(x0,x1) = q_0(x_0)q_1(x_1)\mathbb{I}_{c(x_0, x_1)<cdock}$. 
* 2.1 Does it mean that some examples where conformation change upon binding is significant are completely discarded from the training?
* 2.2 If 2.1 is true, how does the model perform on similar examples (i.e. the ones that change a lot upon binding) from the test set?
* 2.3 Can it be true that "All-Atom RMSD% < 1A = 41.7%" means that around 40% of the test set are proteins that almost don't change upon binding, and the model (trained on couplings with rather strict $c_{dock}$) just doesn't change these structures meaning that it "recovers" holo conformations for these 40% correctly?

**Minor comments:**
1. Lines 40-45: could you please provide the references to the works you’re discussing here?
2. Are the protein states over the trajectory physically-realistic?
3. Could you please provide a more detailed description of y-axis in Figure 4 (include "% of passed predictions" or something like this)?
4. Line 273 - 274 -> I could not find the introduction of the coupling $q(x0, x1) = q(x0)q(x1)\mathbb{I}$ in the previous section. What are you referring to?
5. Line 182 – I am not sure if it is a typo or maybe I am wrong, but to me it looks like (3) is the lower bound of (2).

### Questions
1. It would be interesting to look at some examples of the model predictions (overlaid with the ground truth).
2. It would be helpful to provide the distribution of RMSD on $C_{\alpha}$ positions between apo and holo structures in the training and test data.
3. What is $q_0$ for ligands and how does the Unbalanced FM framework combine with the diffusion model for ligands?
4. What is the actual sampling efficiency of the final model? I.e. how many samples are required on average until the one exceeding the confidence threshold is obtained? Does the Runtime in Table 1 account for it? It would be interesting to look at the dependency of ESS on the selected $c_{dock}$ cutoff.
5. It has been recently shown that the conventional train/test splits of PDBbind (that authors use in this work), have a significant data leakage [1]. Is it possible that majority of 41% successful predictions (in Table 1) overlap with the training data?

[1] Corso G. et al. Deep confident steps to new pockets: Strategies for docking generalization //ArXiv. – 2024.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This papers introduces Unbalanced Flow Matching (UFM), an extension of traditional flow matching, particularly tackling molecular docking problems considering protein flexibility. While traditional molecular docking methods assumed rigid structure for proteins limiting the accuracy, sometimes failing in scenarios including conformational changes of protein. Based on UFM, the authors propose the framework FLEXDOCK that considers flexible docking, and structure relaxation for optimized pose.

### Strengths
1. A new paradigm coined Unbalanced Flow Matching

The proposed objective is an extension of the traditional flow matching. Relaxing the strict marginal conservation allows more efficient and accurate mapping between distributions.

2. Two subtasks for flexible docking

By dividing flexible docking into two subtasks, manifold docking, and structure relaxation, the method results in more physically realistic structures.

3. Empirical results

FLEXDOCK outperforms prior methods on the PDBBind benchmark. Noticeably, this has been done using the same training data and model architecture as DiffDock-Pocket. Ablation studies also verify each component of the proposed method.

### Weaknesses
1. Flexibility and complexity tradeoff

While UFM has strength in flexibility compared to prior works, it inevitably seems to face more complexity than before. Could the authors briefly summarize the complexity compared to the algorithms in the prior works, if possible? Specifically, a detailed comparison of the computational cost, including memory and time complexity, would be beneficial. It is unclear how the introduction of the coupling distribution and the discriminator model impacts the overall computational burden compared to standard flow matching methods. For instance, how does the runtime scale with the size of the protein and ligand, and how does the memory footprint compare to methods that do not employ a discriminator?

2. Choice of coupling

UFM seems to rely much on the coupling distribution. The authors have empirically chosen cutoffs, but this dependency may have problems for generalization. I may have misunderstood the part of choosing the coupling. The choice of a simple cutoff based on RMSD might be overly simplistic and potentially limit the method's ability to handle complex conformational changes. The authors should clarify how sensitive the method is to the choice of this cutoff and whether there are any principled ways to select it. Furthermore, it is not clear how the method would perform with different similarity metrics or more complex coupling strategies. A more thorough discussion on the limitations of the chosen coupling and potential alternatives would be beneficial.

### Questions
1. UFM in extreme cases

Just curious, does UFM succeed even in extreme scenarios where the unbound (apo) and bound (holo) protein structures highly differ?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This paper proposes Unbalance Flow Matching and demonstrates its application to flexible docking, and enhances its performance from 30% to 73%. For those who have attempted the traditional flow on flexible docking or protein domain structural changes, they must have encoutered the same problem addresses in this paper. It offers a good solution backed by theoretical insights and supporting proofs.

### Strengths
- It proposes the Unbalance Flow Matching (UFM), which extends the traditional flow matching with the coupling q by performing some filtering (e.g., RMSD) in practice.
- The proposed two-stage flow matching process, consisting of a rough docking stage called “manifold docking” and a more precise “relaxation” stage, effectively boosts the PB valid benchmark to 73% while maintaining reasonable computational costs.

### Weaknesses
 - I do not see major weakness in this paper, but have several questions as follows.

 - In Section 3, the authors mention challenges in applying flow matching directly to flexible docking:
    
    > In fact, although the different conformational states of the protein do not change significantly upon ligand binding, their relative weights are often notably
    altered.
    > 
    
    What is the **relative weights** meaning?
    
- The proposed second stage is to perform the relaxation by deep learning model. Maybe it is to give an end-to-end solution for more precise docking, as shown in Table 2. But I strongly recommend to conduct the minimisation (relaxation) using force fields instead as what is done in PoseBusters (Section 2.5 and 3.3 in PoseBusters paper). The comparison between PB valid and runtime consumption is preferred.
- For the apo structure, as mentioned in 4.1: 
>given the relative inaccuracy of computational models to sample multiple protein conformations.
> 
I’m wondering why the ensembles generated by, for example, AlphaFlow, is inaccuracy. Since it is sampled from the MD trajectories and, in principle, it should provide more accurate structures than the addition of small Gaussian noise on apo structure.
- The unbalanced pattern is pinned across the training. However, is there a potential risk that, for example, there are some apo structures all have RMSD exceeding 4Å from the holo structures? Under such situation, they are all been filtered out and the sampling would fail. Should the traditional flow and unbalanced flow been given a ratio during the training process (like 5/5)?
- The comparison between AF3 on PB is preferred (extended Data Fig.4).

### Questions
- In Section 3, the authors mention challenges in applying flow matching directly to flexible docking:
    
    > In fact, although the different conformational states of the protein do not change significantly upon ligand binding, their relative weights are often notably
    altered.
    > 
    
    What is the **relative weights** meaning?
    
- The proposed second stage is to perform the relaxation by deep learning model. Maybe it is to give an end-to-end solution for more precise docking, as shown in Table 2. But I strongly recommend to conduct the minimisation (relaxation) using force fields instead as what is done in PoseBusters (Section 2.5 and 3.3 in PoseBusters paper). The comparison between PB valid and runtime consumption is preferred.
- For the apo structure, as mentioned in 4.1: 
>given the relative inaccuracy of computational models to sample multiple protein conformations.
> 
I’m wondering why the ensembles generated by, for example, AlphaFlow, is inaccuracy. Since it is sampled from the MD trajectories and, in principle, it should provide more accurate structures than the addition of small Gaussian noise on apo structure.
- The unbalanced pattern is pinned across the training. However, is there a potential risk that, for example, there are some apo structures all have RMSD exceeding 4Å from the holo structures? Under such situation, they are all been filtered out and the sampling would fail. Should the traditional flow and unbalanced flow been given a ratio during the training process (like 5/5)?
- The comparison between AF3 on PB is preferred (extended Data Fig.4).

### Soundness
3

### Presentation
3

### Contribution
3
