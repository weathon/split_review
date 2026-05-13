# De novo Protein Design Using Geometric Vector Field Networks

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
Innovations like protein diffusion have enabled significant progress in \textit{de novo} protein design, which is a vital topic in life science.
These methods typically depend on protein structure encoders to model residue backbone frames, where atoms do not exist. Most prior encoders rely on atom-wise features, such as angles and distances between atoms, which are not available in this context. Thus far, only %a few basic
several simple 
encoders, %like
such as 
IPA \citep{jumper2021highly}, have been proposed for this scenario, exposing the frame modeling as a bottleneck. In this work, we %introduce
proffer 
the Vector Field Network (VFN), %that
which 
enables network layers to perform learnable vector computations between coordinates of frame-anchored virtual atoms, thus achieving a higher capability for modeling frames. The vector computation operates in a manner similar to a linear layer, with each input channel receiving 3D virtual atom coordinates instead of scalar values. The multiple feature vectors output by the vector computation are then used to update the residue representations and virtual atom coordinates via attention aggregation. Remarkably, VFN also excels in modeling both frames and atoms, as the real atoms can be treated as the virtual atoms for modeling, positioning VFN as a potential \textit{universal encoder}. In protein diffusion (frame modeling), VFN exhibits an impressive performance advantage over IPA, excelling in terms of both designability (\textbf{67.04}\% vs.\ 53.58\%) and diversity (\textbf{66.54}\% vs. 51.98\%). In inverse folding (frame and atom modeling), VFN outperforms the previous SoTA model, PiFold (\textbf{54.7}\% vs.\ 51.66\%), on sequence recovery rate. We also propose a method of equipping VFN with the ESM model 
\citep{lin2022language}, which significantly surpasses the previous ESM-based SoTA (\textbf{62.67}\% vs.\  55.65\%), LM-Design \citep{zheng2023lm_design}, by a substantial margin.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce a new architecture (VFN) for processing protein structures, which allows to represent residue positions with many virtual atoms. This allows for more fine-grained modeling of residue interactions. The proposed VFN architecture is shown to outperform standard architectures in both protein generation using diffusion models and inverse folding tasks.

### Strengths
I agree with the authors that there has been an over-reliance on IPA in the literature for protein tasks. It makes a lot of sense to investigate improvements to it, so the paper does target a very important problem in my eyes.
Introducing effectively more data channels into the model to increase its capacity is also very sensible. Importantly the model is shown to improve the results on the most common and important protein modeling tasks.

### Weaknesses
The general reasoning of why the proposed architecture works better and should be constructed the way it is lies on the concept of atom representation bottleneck. But this bottleneck is not really introduced or investigated in a rigorous manner. Maybe the authors can at least give concrete theoretical counter examples of what problem can be modeled with VFN but not IPA. At least an experimental ablation on varying the virtual node count would be interesting to see how the performance changes.

It would also be nice if authors could show the theoretical expressivity of their proposed construction. E.g. is there something it cannot model or is it provably universal.

General GNNs have seen some improvements on modeling equivariant structures, e.g. [1, 2, 3] which in some ways have some similarities to the current work (e.g. higher dimensional embedding in frame averaging is a bit like virtual nodes here). It would be nice to see how the proposed VFN architecture stacks up to those general GNN constructions. Although admittedly, those papers usually test their models on molecular and other physics-inspired 3D tasks, but not proteins tackled in this paper. However the extension, especially in case of frame averaging or the multi-channel EGNN, would be trivial. Note that there are also many more improved 3D GNNs, especially in molecule domain that could be applied to this problem. I would like to see the authors test against at least a few of these options, especially frame-averaging as it has been used for proteins a couple of times now [4, 5] and would tackle a similar problems as the proposed model in a very general way.

Speaking of proteins, in the abstract authors say that only basic encoders such as IPA have been proposed for proteins so far. E.g. [4] applies frame averaging [2] to antibodies, with a quite intersting non-relational architecture for antibody design. While its restricted to a certain protein family it's still worth mentioning that 'less simple' encoders do exist, at least in specific cases.
 
[1] Du, Weitao, et al. "A new perspective on building efficient and expressive 3D equivariant graph neural networks."

[2] Puny, Omri, et al. "Frame averaging for invariant and equivariant network design." 

[3] Levy, Daniel, et al. "Using Multiple Vector Channels Improves E (n)-Equivariant Graph Neural Networks."

[4] Martinkus, Karolis, et al. "Abdiffuser: Full-atom generation of in-vitro functioning antibodies."

[5] Jin, Wengong, et al. "Unsupervised Protein-Ligand Binding Energy Prediction via Neural Euler's Rotation Equation."

### Questions
I would mainly like the authors to provide a more detailed theoretical and/or experimental analysis of the introduced atom representation bottleneck, as I mentioned in the weaknesses.


-------
### After Rebuttal
Thank you for the extensive rebuttal. I read through all the reviews and all the answers and I think the work has noticeably improved.
It's a bit strange the authors have not updated the paper itself with all the new results, but I trust that they will for the final version.
I now recommend acceptance.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes vector field network to model to better model local frames. Building on this VFN, this paper constructs two sequential models, respectively targeting at designing protein structures and generating protein sequence based on given protein backbone structure.  The paper achieves a new SOTA score on CATH 4.2 on inverse folding task and performs better than FrameDiff on protein structure design.

### Strengths
The proposed model achieves a new SOTA score on the CATH 4.2 benchmark.

### Weaknesses
1. **The architecture design lacks some novelty:** It seems for the protein structure design part (VFN-Diff) borrows some ideas from FrameDiff, while for the inverse folding part (VFN-IF), the virtual atom is similar to that of PiFold and the node interaction (Equation 4, 5, 6) is similar to the node gating mechanism in PiFold.

2. **The problem setting is unfair:** In the first paragraph of section 4, the author mentioned "In the protein diffusion part, the protein structure is designed and represented using backbone frames T. Subsequently, these backbone frames are fed into the inverse folding network to obtain the corresponding protein sequence for the designed structure." If I didn't understand wrongly, this means the author first design the protein structure  and then generate protein sequence based on the designed structures.  Therefore, it's kind of like a pipeline. However, in Table 1, for the sequence design task, the author only compared with the inverse folding models, say sequence design based on real structure instead of designed structures. I think a more fair comparison should compare to baseline like structure design model plus inverse folding model, such as FrameDiff + ProteinMPNN, RFDiffusion [1]+ProteinMPNN and also some structure-sequence co-design model like ProtSeed [2]. 

[1] De novo design of protein structure and function with RFdiffusion. Nature 2023.

[2] Protein Sequence and Structure Co-Design with Equivariant Translation. ICLR 2023.

3.**Lack of baselines:** The paper lacks some important baselines. For example, [2] for sequence part. For structure design part, the author only compares with FrameDiff, while the current SOTA protein structure design model is RFdiffusion [1]. Also, there is some other protein structure design model like SCMDiff [3], 

[3] DIFFUSION PROBABILISTIC MODELING OF PROTEIN BACKBONES IN 3D FOR THE MOTIF-SCAFFOLDING PROBLEM. ICLR 2023.

[4] Generating Novel, Designable, and Diverse Protein Structures by Equivariantly Diffusing Oriented Residue Clouds. ICML 2023.

4. **The writing is unclear:** The author may need to use a unified annotation system, like sometimes {i, j} sometimes k is confusing while they mean the same thing. Additionally, the author may need to provide an overall graph of the architecture to help reader understand this paper.

### Questions
1. In figure 2, $T_{i\rightarrow j}$ means T_j to T_i, while in line below Equation 1, it means T_i to T_j. What does this term really mean?

2. Why he range of H can be negative, say -200 A?

3. $d_q$ is the number of channels in $g_{i,j}$. Does that mean the number of virtual atoms between node i and node j? What is the specific value used in this paper?

4. Are the MLP in equation 7 and 4 are the same one?

5. Using the ESM as initialization and then testing the model on CATH benchmark may have data leakage issues. How did the author deal with this problem?

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a frame-based architecture for operating on protein structure. The key idea is to parameterize a set of virtual atoms within each residue frame. For each pair of interacting frames, the coordinates of both sets of virtual atoms in the destination frame are used to compute attention weights and message values. The aggregated message is then used to update the node features and virtual atom coordinates. In experiments, the authors swap out the architectures of PiFold and FrameDiff and achieve significantly improved performance under identical experimental settings.

### Strengths
* The paper establishes a new entry in the design space of residue frame-based architectures, an exciting direction for protein representation learning.
* The experimental results are quite strong and establish that VFN could be used as a drop-in replacement for alternative SOTA architectures.
* The non-exchangeable treatment of virtual atoms (unlike IPA) leaves open the possibility of using the framework for real sidechain atoms.

### Weaknesses
* The thesis of the paper would be improved by better contextualization relative to IPA. The authors should not shy away from acknowledging significant similarities, but highlight the key changes and the insights behind them. I would suggest a side-by-side algorithmic comparison.
* The paper could be further strengthened by additional comparisons with IPA. Particularly, if we replace IPA in AlphaFold/ESMFold with VFN, does the performance persist? It should not be too hard to run this experiment since the structural module is not very large.
* The claims about a "universal encoder" are not well-supported. It would be nice to see actual experiments where sidechains are also involved.
* From the novelty standpoint, an argument can be made that the architecture is similar enough to IPA and / or PiFold to count against its technical significance.

Justification for score: I think this is a good paper and am happy to recommend acceptance if the Questions are fully addressed.

### Questions
* Please describe more details on how the VFN-IF+ training split is constructed.
* Table 5 shows results for FrameDiff+ProteinMPNN vs VFN-Diff+VFN-IFE. What was the exact setting for reporting these numbers reported here, relative to Table 4? Are there equivalent results for FrameDiff+VFN-IF or VFN-Diff+VFN-IF? Please show these for all experimental settings in Table 4.
* In Figure 1, why does FrameDiff suffer in scTM more on medium-length proteins than the longest proteins?
* Why was it necessary to retrain FrameDiff, as claimed in the appendix?
* Please clarify if the PiFold and FrameDiff numbers are taken directly from the respective papers. Please affirm that the results and claims made here are indeed under *identical experimental conditions* relative to PiFold and FrameDiff, or if they have been modified, please be very direct about these modifications.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
