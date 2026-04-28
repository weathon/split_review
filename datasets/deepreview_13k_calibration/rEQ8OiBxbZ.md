# 3D Molecular Pretraining via Localized Geometric Generation

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
Self-supervised learning on 3D molecular structures has gained prominence in AI-driven drug discovery due to the high cost of annotating biochemical data. 
However, few have studied the selection of proper modeling semantic units within 3D molecular data, which is critical for an expressive pre-trained model as recognized in natural language processing and computer vision.
In this study, we introduce \textbf{L}ocalized G\textbf{e}ometric \textbf{G}enerati\textbf{o}n (LEGO), a novel approach that treats tetrahedrons within 3D molecular structures as fundamental building blocks , leveraging their simplicity in three-dimension and their prevalence in molecular structural patterns such as carbon skeletons and functional groups.
Inspired by masked language/image modeling, LEGO perturbs a portion of tetrahedrons and learns to reconstruct them in pretraining.
The reconstruction of the noised local structures can be divided into a two-step process, namely spatial orientation prediction and internal arrangement generation.
First, we predict the global orientation of the noised local structure within the whole molecule, equipping the model with positional information for these foundational components.
Then, we geometrically reconstruct the internal arrangements of the noised local structures revealing their functional semantics.
To address the atom-bond inconsistency problem in previous denoising methods and utilize the prior of chemical bonds, we propose to model the graph as a set of nodes and edges and explicitly generate the edges during pre-training.
In this way, LEGO exploits the advantages of encoding structural geometry features as well as leveraging the expressiveness of self-supervised learning.
Extensive experiments on molecular quantum and biochemical property prediction tasks demonstrate the effectiveness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a novel pre-training approach for 3D molecular datasets, building upon TokenGT. By augmenting TokenGT with 3D attributes, the proposed method harnesses 3D molecular data to enhance its generalization capabilities across various tasks.

### Strengths
1. Segmenting 3D structures into distinct local components is an insightful approach.

2. The reconstruction method for these local structures is intriguing and presents a unique strategy.

3. There is a marked novelty in the concept of pre-training 3D molecules through local structures, despite the base model being a straightforward extension of TokenGT enhanced with 3D coordinates.

### Weaknesses
1. The base model's simple strategy of appending 3D features to token embeddings may compromise the essential equivariance of 3D molecules. Specifically, the direct concatenation of 3D coordinates to node embeddings, without considering rotational or translational invariance, could lead to a model that is sensitive to arbitrary orientations of the input molecule. This is a critical concern for molecular property prediction, where the underlying physics should be invariant to such transformations.

2. The description of the training objective section lacks clarity. It is unclear how the local structure reconstruction is implemented. The paper mentions separate mask indicators for center atoms, edges, and leaf atoms, but it does not specify how these are used to generate the reconstruction targets. It is also not clear how the loss function is computed across these different reconstruction tasks, and whether they are weighted differently. A more detailed explanation of the loss function and the reconstruction process is needed.

3. Given that the model is training on the reconstruction of molecular conformations, it would be beneficial to disclose the reconstruction accuracy on the pretraining dataset to demonstrate the model's learning efficacy. Without this, it is difficult to assess whether the model is effectively capturing the 3D structural information. The lack of this metric raises concerns about the model's ability to learn meaningful representations from the 3D data.

4. The experimental comparisons should encompass additional 3D molecular datasets such as QM9 and GEOM-drug, considering the model's pretraining on 3D structures. Nonetheless, the paper confines its reporting to the OGBLSC-PCQM4Mv2 dataset and the observed performance significantly lags behind SOTA methods. The explanation provided for this underperformance does not sufficiently account for these results. The lack of evaluation on diverse 3D datasets makes it difficult to assess the generalizability of the proposed method.

5. The layout of the paper requires revision. The Algorithm should be positioned before page 10 or on a separate page designated as an appendix, rather than following the references on page 12.

### Questions
1. What exactly constitutes the input for TokenGT-3D? Is it the original molecules, or do you utilize each local structure segmentation after masking and perturbation? Or is it the masked and perturbed local structure segmentations of a single molecule, or something else entirely?

2. Given the proposed method centers on pre-trained representation learning, what form do the learned representation embeddings take for downstream tasks?

3. Could you elaborate on how the local structures are reconstructed? What serves as the input for this process: a single embedding from the TokenGT-3D output, or a collection of embeddings from local structure segmentations within a single molecule?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a self-supervised pre-training strategy for 3D molecular structures, based on partitioning molecular structure into tetrahedra that can then be masked and reconstructed.

### Strengths
The empirical performance is OK for some of the fine tuning tasks, although still not consistently solid.

### Weaknesses
The geometrical justification of tetrahedra as simplest polyhedron might make sense, but in chemistry it makes a lot less sense. The authors literally show benzene in Figure 1b, which has 120-degree bonding pattern (so called planar-trigonal in chemistry) that is NOT a tetrahedron at all, and has very different local symmetries.
The ablation studies are unconvincing. Why not evaluate the role of the actual innovations introduced ? Tetrahedra vs. point-wise generation. Evaluate the role of edge information ? 
What happens for atoms with more than 4 bonds (sulfur, phosphorous, etc) ?

"We attribute this to the different 3D structures molecules exhibit in liposome compounds." What does this mean ? What are these structures different ? 
All the biochemistry prediction tasks are actually properties of the graph, not the 3D structure, What 3D structure is being used ?

### Questions
"We attributethistothedifferent3Dstructuresmoleculesexhibitinliposomecompounds." What does this mean ? What are these structures different ? 
All the biochemistry prediction tasks are actually properties of the graph, not the 3D structure, What 3D structure is being used ?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper describes a pretraining process on the 3D structure of small molecules. The method splits a molecule into tetrahedrons of a few atoms each and learns to reconstruct them in 3D using knowledge of the graph structure of the input molecule. The authors apply the model on downstream property prediction tasks and compare to public benchmarks.

### Strengths
The main method in the paper is interesting conceptually and somewhat original as it combines a graph token representation with a decomposition of a small molecule into smaller 3D structural units. The downstream application on MoleculeNet is significant, and the application on the open graph benchmark is useful for context, although the particular table 2 is misleading. The introduction is reasonably clear, however, other parts of the paper have problems with the language or formalism.

### Weaknesses
The paper can use a lot of rewriting in the methods and experimental results sections.


Table 1 does not correctly highlight the best and second best results (see column for BACE when 2 of the 2D models perform better than LEGO).  Table 2 is missing the vast majority of best performing models from the opengraph benchmark large scale challenge.  Interestingly, the comparison in table 2 misses the top two entries which are models included in Table 1; if I count correctly the LEGO model would rank 9th in the validation metric with a substantial gap compared to unimol published in last year's ICLR.  It would be useful if the authors submitted their model to the benchmark to see the performance on the test set.

The text has a lot of rushed / unclear sentences.  The first sentence on page 8 ("All this baselines involves...") does not make sense as written.  Small errors and lack of clarity starts earlier in page 5 (undefined d_p), page 6 ("way to increase the and generalizability"), page 7 ("... is enough to valid our method", "...graph representation an pass it...", "...an important properties...", "...proved to be close related..."), probably more.

The ablation study is not helpful: the perturbation of the model is too limited, and table 3 suggests strongly that the parameters are actually not optimal.  The random perturbation pretraining of table 4 is not described in a clear enough fashion.

### Questions
Although the current method is not directly inspired by this work, I believe that the RL reconstruction of molecular geometries from 3D fragments in Flam-Shepherd et al (https://arxiv.org/abs/2202.00658) relates closely to the core inspiration of this method and might warrant discussion in the intro. (In contrast, some of the discussion of the atom-bond inconsistency problem is potentially possible to skip as it doesn't add meaningful insights.) Did the authors think of extending their tetrahedral segmentation approach to use a similar fragment-based approach instead?

Can the authors comment on the disparity of the approach of their validation scores on moleculeNet vs those on the large-scale challenge?  

The ablation study is not helpful: the perturbation of the model is too limited, and table 3 suggests strongly that the parameters are actually not optimal.  The random perturbation pretraining of table 4 is not described in a clear enough fashion.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a 3D molecular self-supervised learning approach that leverages the geometric information of molecular local structures, in the way of orientation prediction and arrangement generation. The atom-bond inconsistency issue has been identified and tackled through a joint modeling of the graph as a set of nodes and edges. The method has been benchmarked on MoleculeNet and OGBLSC-PCQM4Mv2 datasets to verify the efficacy of proposed designs.

### Strengths
1. The paper is well-motivated through the concept of molecular local structure and the introduced approach yields good novelty.

2. The presentation is mostly clear and the method is easy to follow.

### Weaknesses
1. The experimental results seem to be insufficient to support the empirical superiority of the proposed approach. In particular, the method could be further improved either through a more careful design of the backbone or enhancements of the training objective to make the results stronger.

2. If the results are difficult to improve, the authors may also be suggested to try other benchmarks or setups, e.g., QM9, MD17, where a better utilization of the 3D structural information would bring more benefits. In the current shape the quality of the experimental evaluations may not meet the bar of ICLR.

### Questions
Q1. I am curious whether the proposed SSL objective can be combined with other backbones or even other pretraining objectives. If so, it would be interesting to see how the method can benefit different backbones which may be an evidence of the extensibility of the approach.

Q2. How does the method perform on datasets like QM9?

Q3. For the ablation study, it would also be interesting to see how the proposed 3D TokenGT helps to boost the performance since one of the claim in the paper is that the atom-bond inconsistency problem is tackled by modeling graph as a set of nodes and edges.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
