# AtomSurf: Surface Representation for Learning on Protein Structures

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 5, 8, 6

## Abstract
While there has been significant progress in evaluating and comparing different representations for learning on protein data, the role of surface-based learning approaches remains not well-understood. In particular, there is a lack of direct and fair benchmark comparison between the best available surface-based learning methods against alternative representations such as graphs. Moreover, the few existing surface-based approaches either use surface information in isolation or, at best, perform global pooling between surface and graph-based architectures. 
    
    In this work, we fill this gap by first adapting a state-of-the-art surface encoder for protein learning tasks. We then perform a direct and fair comparison of the resulting method against alternative approaches within the Atom3D benchmark, highlighting the limitations of pure surface-based learning. Finally, we propose an integrated approach, which allows learned feature sharing between graphs and surface representations on the level of nodes and vertices \textit{across all layers}.
    
    We demonstrate that the resulting architecture achieves state-of-the-art results on all tasks in the Atom3D benchmark, while adhering to the strict benchmark protocol, as well as more broadly on binding site identification and binding pocket classification. Furthermore, we use coarsened surfaces and optimize our approach for efficiency, making our tool competitive in training and inference time with existing techniques

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper aims to improve our understanding of surface-based learning for protein representations. This is achieved by first adapting the surface encoder from the graphics literature for protein-learning tasks, which is then compared against other representation modalities (graphs, convolutions, equivariance etc). Following this the authors consider learning on bipartite graphs comprising structure and surface, allowing information to be shared at every layer of learning, compared to previous multi-scale approaches. 

Experiments on the Atom3D benchmark showcase the improved performance of the method on PPI (Protein-Protein Interaction), MSP (Mutation-Stability Prediction), and PSR (Protein-Structure Ranking) tasks, while using a much smaller model. A further experiment on binding site classification sees the method performance favorably compared to previous surface-learning based approaches.

### Strengths
1. There is very limited work on understanding representation learning with protein surfaces, even though it is universally agreed upon as being a suitable choice for many tasks. In that light, the paper is original in its attempt to dissect and improve representation learning with protein surfaces, and their integration with other modalities.

2. The quality of this work is good, showing a careful study of protein surfaces, adapting existing encoders to capture biological mechanisms, and experimental performance with relevant baselines on a well-known (albeit old) benchmark. The text is also clearly written, and generally easy to follow. For experiments, both the experimental comparisons against other representation modalities, and the experiments on antibodies are interesting and promising. 

3. Ablation studies are also performed for the different experimental choices, which further helps improve our understanding of protein-surface learning.

### Weaknesses
 **Experiments**

1. Atom3D is an old benchmark, without known issues with regards to the strategies used for splitting datasets. There has been some recent efforts [1] in curating tasks and datasets and evaluating structure based protein learning methods. While I understand carrying out an evaluation with this is not feasible within the scope of the current rebuttal timeline, it would be very handy to have this in a future revision of the paper. Specifically, the lack of rigorous evaluation on more challenging datasets with different splitting strategies (e.g., based on structural similarity rather than sequence identity) limits the generalizability claims of the proposed method. The current evaluation might not fully capture the model's ability to handle novel protein structures, which is crucial for real-world applications.

[1] Evaluating Representation Learning on the Protein Structure Universe

2. For the BindingSite Identification experiment, there is a missing baseline from dMaSIF which also achieves a 0.87 AUROC. The absence of this direct comparison makes it difficult to assess the true advancement of the proposed method in this specific task. A more comprehensive comparison, including all relevant state-of-the-art methods, would provide a clearer picture of the method's performance.

3. For most of these tasks, the dataset sizes available are typically limited. This makes it paramount to include uncertainty estimates, measured across 3 experimental runs. The lack of uncertainty quantification makes it difficult to assess the robustness of the results and the statistical significance of the observed improvements. Reporting only point estimates without confidence intervals or standard deviations hinders the reliability of the conclusions.

**Presentation**
The experiments section should include the corresponding table for the ribosomes (rather than in the appendix), or reorder the sections such that it falls under Ablation studies. This would improve the readability and flow of the paper.

### Questions
1. Could the author(s) include the uncertainty estimates, measured across 3 experiment runs. I presume running these would not be out-of-scope for the rebuttal timeline, given the small size of the model and the datasets. 

2. For the different benchmark tasks, it would be very beneficial to understand / detail how the training splits were constructed. A common practice is to construct splits based on sequence similarity, but these don't capture the structural nuances / differences which are more relevant for OOD generalization.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes a hybrid approach combining surface and graph-based encoders, an improved DiffusionNet architecture tailored for protein surface analysis, a comparison of protein surface-based representations against protein as graph-based representations and enhanced computational efficiency with residue graphs and coarsened meshes.

### Strengths
1. The proposed method shows superior empirical performance on Protein Interaction Prediction (PIP) and Mutation Stability Prediction (MSP) tasks compared to existing methods.
2. The paper is easy to follow.
3. The code is provided.

### Weaknesses
I believe the main weakness of the paper is that, in terms of the proposed method, the paper does not provide a significant novel contribution. While the authors argue that direct comparisons between protein surface representations and other forms of representation have not yet been conducted, the idea of using protein surface representations is not new. Additionally, the results for the Protein Structure
Ranking (PSR) task in the Atom3D benchmark demonstrate comparable performance with other approaches that incorporate different representations, such as GearNet and ProNet.



### Questions
1. The authors modified the design of the DiffusionNet architecture, which is typically used with geometric representations like triangle meshes or point clouds, and applied it at each point (or vertex). Initially, the protein surface was computed using MSMS, which generates a surface by rolling a virtual sphere (representing a solvent molecule, usually water) over the protein's atoms. Were traditional geometric CV surface reconstruction methods, such as Poisson surface reconstruction, considered to enhance compatibility with the adapted approach (DiffusionNet)?
2. "We choose to use residue graphs for computational efficiency: each node in this graph represents an amino-acid residue and edges are introduced between pairs of atoms that are within a 12 $\unicode{x212B}$ radius cutoff. For each residue, we add a one hot encoding of its type, its secondary structure annotation and its hydrophobicity. We also compute sequence embeddings using the ESM-650M (Rives et al., 2021) pretrained model and include them as node features." How were ESM embeddings used for amino acid residue atoms?
3. The surface encoder is based on the DiffusionNet architecture, which is applied to vertices (either from a point cloud or mesh). However, a more intuitive approach for capturing surface representation could be to use a triangulated mesh-based encoder defined on edges of the surface, such as MeshCNN. While DiffusionNet outperformed MeshCNN in the original study, it would be interesting to include an analysis of MeshCNN's performance within the protein domain.
4. The ablation study lacks a comparison between random representations and ESM residue representations.
5. Table 2 presents the number of parameters and indicates if pretraining was performed. If Atomsurf uses ESM embeddings, why it was not indicated as pretrained?

### Soundness
3

### Presentation
3

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
## Analysis of surface representations methods in protein representation learning

This paper studies the utility of a diffusion kernel based surface representation ideas, introduced in DiffusionNet (Sharp et al. 2020 preprint, 2022 published) for protein representation learning. The authors update the original DiffusionNet formulation to (1) allow for batching and (2) initialising the diffusion time parameters around a meaningful value in proteins (10 Angstrom). 

This protein-adapted version of DiffusionNet is then studied (1) in isolation and (2) in combination with residue graph-based representation learning on a handful of protein representation learning tasks:

Evaluated are the protein interaction prediction (PIP), mutational stability prediction (MSP) and protein structure ranking (PSR) tasks of the Atom3D benchmark, as well as an antibody-antigen interaction prediction and a protein-ligand binding site prediction task.

The contributions of this work are:
- (1) *Modelling contributions*: The above mentioned (batching, initialisation) adaptations to DiffusionNet and, for the models that work on both surface and residue graph level representations, a layer-wise cross-communication between surface & graph representations via cross attention.
- (2) *Insight contributions (ablations and benchmark comparisons)*: The authors ablate the use of DiffusionNet-style surface representation learning versus other surface based approaches, as well as combining surface and graph level approaches. They compare to adequate baseline representatives of each approach that are common in the literature. They find that in their hands & on the above mentioned benchmarks their DiffusionNet-style approach together with a residue graph representation based approach outperforms the other methods.

### Strengths
1. Writing: The paper was very well written overall and I enjoyed the read. Statements were clearly made and easy to follow -- well done on the writing and thank you for spending time on it!

2. Benchmarks select relevant baselines: The authors selected relevant baselines (e.g. GearNet for graph-level representation learning, HoloProt for graph-surface combinations, MaSIF for surface based representation learning) that I would have expected to see in such a work. 

3. Interesting case of cross-domain method transfer: The authors transfer the DiffusionNet method from the general surface representation learning literature to the protein representation learning literature. As someone from the protein community I was not previously familiar with the DiffusionNet work and found this a valuable bridge and interesting comparison. While the adaptations to the DiffusionNet approach for proteins were minor (essentially constrained to the update of sampling the t values at 10 Angstrom) this adaptation was well reasoned and makes sense from a domain-level perspective.

4. Ablations: I found the ablations to be informative and well constructed and described.

### Weaknesses
1. Clarity in benchmark comparisons: When seeing the comparison to the benchmark methods, I was left with the question whether the authors re-ran training on the same datasets & splits for each method, or whether these numbers were quoted from a table? What are the levels of variation for each? (e.g. +/- resulting from 3-5 different runs). Were all approaches 'tuned' with equal attention to hyperparameters? I would have expected a short discussion of these points.

2. Limitation of these benchmarks: This is less of a direct critique of this paper, and more of the underlying benchmarks that were used (that I believe should be updated). Protein structures tend to not be rigid, and as a consequence surfaces tend not to be rigid either. While at a coarse grained level there is likely less variation (unless there are global conformation shifts), at a 3-8A level there can be significant reorganisation of side chains - relevant for ligand binding and polar interactions. Interaction prediction should therefore be done on 'relaxed' surfaces that were not extracted from protein complexes (as some of the benchmarks do) and holdout sets should be constructed in particular also based on structural similarities of surfaces rather than just sequence homology. I would highly recommend the authors to look into the pinder & plinder datasets & benchmarks, but I do acknowledge that these were just published briefly before this work was submitted. A comparison on these in the rebuttals would be of much interest. Without comparisons like these I doubt the real-world applicability of such surface representations for most practical tasks in biology.

### Questions
C.f. weaknesses above.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a new model for protein structure representation learning and property prediction. The main idea is to take as input both the 3D point cloud graph as well as surface mesh, jointly process both modalities within the network with information sharing among them, and then use the joint representation to perform prediction tasks per residue or globally. Experimental results show improvements or match state of the art results on all benchmarks evaluated.

### Strengths
- The general ideas of share information across the various representations of a biomolecule is simple and appealing. Implementing a tighter coupling between the graph and surface track in the newly proposed networks is a sensible idea. The results support all these design decisions well. I think the community will find the ideas and results in the paper to be useful.

- Well written and well presented overall.

### Weaknesses
 - There has been a recent focus in the community on purely sequence-based approaches and protein language models (see the last ICLR for several works on structure-aware pLMs). I would have been interested to see empirical comparisons to at least ESM2 or perhaps more recent structure-aware pLMs. In principle, the sequence contains all the information that represents a protein and pLMs could implicitly be able to learn surface representations. I would at least have liked to see an ablation on the use of ESM2 embeddings in the model.
    - (In other words: Could the performance gain be coming from the use of ESM2 embeddings as node features? Perhaps yes, as these pLM embeddings have been shown to already be very strong at learning structural representations and for structure-based tasks: https://openreview.net/forum?id=sTYuRVrdK3, ICLR 2023.)

 - Are the tables missing more recent results on ATOM3D? Eg. Table 1 only shows the results from the proposed models as well as the original ATOM3D benchmark. But there have been many other papers which have outperformed the original benchmark results. Is the rationale for not including them that they do not strictly conform to the benchmark protocol?

- I realise that the results on all the benchmarks show improvements and each table has the new model in bold -- this is good -- but how relevant are some of the ATOM3D and other tasks in the current state of the field? Eg. Tasks like PSR seem irrelevant in the post AlphaFold 2 era. For RNA segmentation: I personally don't think this is relevant for real-world problems, but I am  happy to be shown wrong here.

--- 

Minor comments:
- Line 287: typo 'embed'

### Questions
- Are the tables missing more recent results on ATOM3D? Eg. Table 1 only shows the results from the proposed models as well as the original ATOM3D benchmark. But there have been many other papers which have outperformed the original benchmark results. Is the rationale for not including them that they do not strictly conform to the benchmark protocol?

- I realise that the results on all the benchmarks show improvements and each table has the new model in bold -- this is good -- but how relevant are some of the ATOM3D and other tasks in the current state of the field? Eg. Tasks like PSR seem irrelevant in the post AlphaFold 2 era. For RNA segmentation: I personally don't think this is relevant for real-world problems, but I am  happy to be shown wrong here.

---

Minor comments:
- Line 287: typo 'embed'

### Soundness
4

### Presentation
4

### Contribution
2
