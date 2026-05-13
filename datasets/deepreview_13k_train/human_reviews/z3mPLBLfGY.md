# Generalist Equivariant Transformer Towards 3D Molecular Interaction Learning

- Decision: Reject
- Scores: 5, 8, 5, 6

## Abstract
Many processes in biology and drug discovery involve various 3D interactions between molecules, such as protein and protein, protein and small molecule, etc.
Given that different molecules are usually represented in different granularity, existing methods usually encode each type of molecules independently with different models, leaving it defective to learn the various underlying interaction physics. 
In this paper, we first propose to universally represent an arbitrary 3D complex as a geometric graph of sets, shedding light on encoding all types of molecules with one model.
We then propose a Generalist Equivariant Transformer (GET) to effectively capture both domain-specific hierarchies and domain-agnostic interaction physics. To be specific, GET consists of a bilevel attention module, a feed-forward module and a layer normalization module, where each module is E(3) equivariant and specialized for handling sets of variable sizes. Notably, in contrast to conventional pooling-based hierarchical models, our GET is able to retain fine-grained information of all levels.  
Extensive experiments on the interactions between proteins, small molecules and RNA/DNAs verify the effectiveness and generalization capability of our proposed method across different domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a generalist equivariant Transformer architecture for learning 3D molecular interactions. The proposed GET model is composed of bilevel attention networks, feed-forward networks, and layer normalization modules, all of which are all equivariant to E(3)-equivariant transformations. The GET model is able to simultaneously learn both the atom- and block-level information.

### Strengths
+ The paper is clearly written. The problem is well motivated.
+ The paper proposes a universal representation for molecular complexes. This approach has the potential to streamline and unify various interaction studies across different molecular domains.
+ The GET model ensures that all modules are E(3)-equivariant and also allows capturing interactions at block and atom scales, potentially leading to richer and more informative interaction modeling.
+ The experiments across small molecules, proteins, and nucleic acids suggest that GET has strong generalization capabilities.

### Weaknesses
 - The reliance on domain-specific knowledge for the construction of building blocks may limit the universality of the proposed GET model (e.g., each residue in the proteins is one node). This may render the comparison with hierarchical models (e.g., GVP) a bit unfair. Specifically, the choice of using residues as nodes in proteins, while intuitive, might not be the optimal representation for all interaction types, potentially biasing the model towards protein-centric interactions and limiting its effectiveness in scenarios involving other types of molecular entities. The lack of a systematic exploration of alternative block construction methods, beyond domain-specific ones, further exacerbates this concern.
- The paper would be strengthened by a more thorough comparison with state-of-the-art methods, e.g., GemNet, Equiformer, EquiformerV2, and LEFTNet. The current comparisons are insufficient to establish the superiority of the proposed method. A more rigorous evaluation, including a wider range of tasks and datasets, is needed to fully assess the performance of GET against these established baselines. The absence of detailed comparisons on specific metrics and the lack of ablation studies on key components of the model make it difficult to pinpoint the source of performance gains.
- The experiments conducted on PPA and PBA datasets may not fully demonstrate the effectiveness of the proposed model, given their relatively small scale. These datasets may not be sufficiently complex to fully evaluate the model's ability to generalize to more challenging real-world scenarios. The limited size of the datasets raises concerns about the statistical significance of the results and the robustness of the conclusions drawn from them. It is also unclear how the model would perform on larger and more diverse datasets.
- I do not see a particular design of modeling molecular interactions in the GET architecture. It appears that it is also possible to evaluate the GET model on a broader range of molecular settings, especially bare molecules. The current focus on molecular complexes may overlook the model's potential applicability to other molecular tasks, such as property prediction of individual molecules. The absence of experiments on bare molecules limits the assessment of the model's versatility and generalizability.
- The equivariant transformers and attention mechanisms raise potential concerns for practical application due to their high computational complexity, as noted in Table 9. The computational cost associated with these mechanisms may hinder the model's scalability and applicability to large-scale molecular systems. The lack of a detailed analysis of the computational bottlenecks and potential optimization strategies further limits the practical relevance of the proposed method.

### Questions
- Including the graphical illustration (Figure 4) within the main text could provide readers with a more immediate and clear understanding of the architecture and operational flow of GET.
- Adding statistics for the PDBBind benchmark within the paper would offer a more concrete assessment for readers unfamiliar with the benchmark.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a bilevel representation that can represent small molecules and large ones (e.g. proteins) in a unified manner. The core is to cluster the complex into a set of blocks, where intra-block connections are dense while inter-block connections are sparse. Based on this representation, the authors propose a Generalist Equivariant Transformer (GET) that captures both domain-specific hierarchies and domain-agnostic interaction physics.

### Strengths
1. The proposed representation and GET are reasonable and novel.
2. The paper is structured well and clearly written.
3. The authors conduct extensive experiments to support their claim, and the results are good.

### Weaknesses
I do not see obvious weaknesses in the proposed method and the experiments. Below are some small flaws:
1. How to construct the bilevel representation should be elaborated (e.g., what is the K of the KNN graph?). 
2. Typo: (In Sec. 1) "In this paper, we approache ..."

### Questions
1. Compared to KNN, are there better ways to construct a block?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a unified representation of molecules as geometric graphs of sets, by performing all-atom analysis via hierarchical processing.
The model is based on the Transformer architecture where atom-level cross-attention is performed between the atoms of the same block (a subset of atoms) and where another attention is then applied at the block level. Equivariant layer norm and feed-forward layers are applied to maintain the equivariance of the coordinates. 
Several experiments on molecular interactions show the superiority of the method.

### Strengths
1. The paper is original in its hierarchical approach and equivariant design.
2. The overall performances are significant

### Weaknesses
1. The paper is not clear: what makes the contributions' novelty hard to understand. Please see Question 1.

Equation (3) is not well defined (the MLP/RBF used) it seems closely related to Shnet or Physnet [2]. Also, learning/refining the self-attention has been investigated (e.g. [1]).

Unclear how (5) is different from (Jin and al.)'s pooling.

There is some lack of motivation as to why one needs to keep track of the coordinates (which requires all the equivariant design of the non-self-attention layers) rather than working with equivariant measures such as the interatomic pairwise distances as most works do (and using other metrics too, e.g. C-RMSD [3,4]).

It is unclear (at least at first sight without looking at the appendix) how equation (10) is E(3)-equivariant (especially rotation).

Most importantly (and that's related to question 2), it's unclear (given the well-known properties of Transformers with long-range dependencies processing) why hierarchical processing is better than atom-level analysis.

2. The assessment is not informative. Please see Question 2.

In order to have a good comparison with the baselines, one should add the models' complexity and capacity comparison.
Thus, while comparing to old baselines such as Shnet or Dimenet++ (Tables 2 and 3), one should compare the difference in capacity and complexity of the models which still perform well and should be much more efficient.

### Questions
The paper needs refinement in order to be clearer by providing motivations and explanations and most importantly better emphasize the technical contributions of the work.

1. Clarity:

Equation (3) is not well defined (the MLP/RBF used) it seems closely related to Shnet or Physnet [3]. Also, learning/refining the self-attention has been investigated (e.g. [1]).

Unclear how (5) is different from (Jin and al.)'s pooling.

There is some lack of motivation as to why one needs to keep track of the coordinates (which requires all the equivariant design of the non-self-attention layers) rather than working with equivariant measures such as the interatomic pairwise distances as most works do (and using other metrics too, e.g. C-RMSD [3,4]).

It is unclear (at least at first sight without looking at the appendix) how equation (10) is E(3)-equivariant (especially rotation).

Most importantly (and that's related to question 2), it's unclear (given the well-known properties of Transformers with long-range dependencies processing) why hierarchical processing is better than atom-level analysis.

2. Assessment: 

In order to have a good comparison with the baselines, one should add the models' complexity and capacity comparison.
Thus, while comparing to old baselines such as Shnet or Dimenet++ (Tables 2 and 3), one should compare the difference in capacity and complexity of the models which still perform well and should be much more efficient.

[1]  Geometric transformer for end-to-end molecule properties prediction.

[2]  PhysNet: A Neural Network for Predicting Energies, Forces, Dipole Moments, and Partial Charges

[3] Molecular geometry prediction using a deep generative graph neural network
[4] Diffusion-based molecule generation with informative prior bridges

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a Generalist Equivariant Transformer (GET) to develop a universal representation of 3D molecular complexes and the GET model for capturing domain-specific hierarchies and domain-agnostic interaction physics.

### Strengths
* The paper is well-motivated and well-written.
* The proposed geometric graph of sets can be applied to various types of molecules, unifying the encoding process across different molecular structures.

### Weaknesses
Related concerns are discussed in the questions section.

* The paper includes comparisons with several models, such as SchNet, DimeNet++, EGNN, and ET. However, there are other models that exhibit superior performance, including GemNet, NeurIPS, Allegro, MACE, etc. The paper would benefit from a more comprehensive comparison with existing methods. While the experimental results demonstrate the effectiveness of the proposed method, a more detailed comparison with other state-of-the-art models would strengthen the paper's claims. Additionally, it is important to cite these related works, as they are highly relevant to the topic of equivariant GNNs.
* Can the authors discuss the implications in practical applications?
* Typo: The model compared with GET is TorchMDNet (ET), not TorchMD.

### Questions
* The paper includes comparisons with several models, such as SchNet, DimeNet++, EGNN, and ET. However, there are other models that exhibit superior performance, including GemNet, NeurIPS, Allegro, MACE, etc. The paper would benefit from a more comprehensive comparison with existing methods. While the experimental results demonstrate the effectiveness of the proposed method, a more detailed comparison with other state-of-the-art models would strengthen the paper's claims. Additionally, it is important to cite these related works, as they are highly relevant to the topic of equivariant GNNs.
* Can the authors discuss the implications in practical applications?
* Typo: The model compared with GET is TorchMDNet (ET), not TorchMD.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
