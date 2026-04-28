# Rethinking the role of frames for SE(3)-invariant crystal structure modeling

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
Crystal structure modeling using geometric graph neural networks is important in various machine learning applications in materials science. In these applications, capturing SE(3)-invariant geometric features in crystal structures is a fundamental requirement for these networks. One approach is to model with orientation-standardized structures through structure-aligned coordinate systems called `frames.' However, unlike molecules, determining frames for crystal structures is not trivial due to their infinite and highly symmetric nature. In the search for effective frames for crystals, we point out that existing work assumes a statically fixed frame for each structure based solely on its structural information, regardless of the task under consideration. Here, we rethink the role of frames, *questioning whether such simplistic alignment with the structure is sufficient*, and propose the concept of *dynamic frames*. While accommodating the infinite and symmetric nature of crystals, these frames give each atom its own dynamic view of the structure, focusing only on those atoms actively interacting with it. We demonstrate this concept by utilizing the attention mechanism in a recent transformer-based crystal encoder, developing a new encoder architecture called  CrystalFramer. Extensive comparisons with conventional frames and crystal encoders show the superior performance of the proposed method in various crystal property prediction tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors change the fixed, static frames for SE(3)-invariant modeling in crystal structures into dynamic frames that adapt to each atom's local environment through the network's attention mechanism, then integrate into a new architecture **CrystalFramer**. Experimental results on large-scale datasets (JARVIS, MP, OQMD) demonstrate that **CrystalFramer** with dynamic frames outperforms models using static frames in several material property prediction tasks.

### Strengths
1. The proposed method is straightforward and presented with commendable clarity.
2. The shift from static to dynamic frames enables atom-specific adjustments, significantly enhancing SE(3) invariance handling in highly symmetric crystal structures. Furthermore, the extensive evaluations on multiple datasets (JARVIS, MP, OQMD) highlight the effectiveness of dynamic frames, with the "max frames" variation demonstrating particular superiority.

### Weaknesses
### Major
How do the "max frame" construction and its usage within the networks differ from those proposed in [1], [2], [3], and [4]? In particular, [1] and [4] use similar atomic local frames to address equivariance in molecular structures. A comparative discussion of these methods would be valuable to clarify whether the proposed approach is a direct adaptation from molecular modeling to materials or if there are novel insights beyond those methods.

### Minor
Using frame-based techniques will hinder the model's continuity, potentially affecting its generalization capabilities, as noted in [5]. Does the proposed model address this limitation? It will be valuable to discuss the continuity of the proposed dynamic frame approach and empirically analyze if this affects generalization in the experiments.

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

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
This paper proposes CrystalFramer and dynamic frames to capture SE(3)-invariant geometric features for crystal property prediction. Unlike using static frame in previous work, this work use dynamics frames to give each atom its own dynamics view of the structure, focusing only on those atoms actively interacting with it, meanwhile also accommodating the infinite and symmetric nature of crystal structures. The experiment shows superior performance of the proposed method in several prediction tasks.

### Strengths
- This work proposes dynamic frames for crystal features modeling, which can dynamically accounting for the atoms actively engaged in learned interactions in each interatomic message-passing layer.
- The proposed method achieves superior performance on several commonly used benchmarks in crystal property prediction.

### Weaknesses
 - Previous relevant frame-based method ComFormer also provides equivariant version. I am wondering if this method can also be easily extended to SE(3)-equivariant? There’re are many other equivariant properties for the materials such as force or high-order tensors. I would like to see the performance of equivariant version of this method if the extension is straightforward. Even for the invariant properties, it’s interesting to know whether equivariant network can help invariant properties prediction.


### Questions
- Please refer to the weakness part.

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
4

### Summary
The paper proposes a new method for modeling crystal based on dynamic frames that are based on the local neighborhood of each atom in the crystal structure. The crystal frames are then processed by a transformer based architecture called CrystalFramer. The paper starts by motivating the utility of geometric deep learning methods that can capture relevant physical inductive biases, such as invariance. Previous work captured such geometric information using frame averaging, which is based on taking canonical frames of the entire structure. By contrast, the paper proposes dynamic frames which are based on the local coordinate system of a given atom. Section 2 then outlines relevant preliminary details with relevant mathematical definitions, including the description of a crystal structure, how transformers have been applied to crystal structure modeling and prior work on frame averaging for molecular and materials modeling.  

Section 3 introduces and defines the concept of dynamic frames, which is the main part of the proposed new method. This includes the frame definitions in Section 3.1 and the CrystalFramer architecture in Section 3.2 that is based on Gaussian basis functions. This is followed by a description of related work on invariant features, frames and equivariant features in Section 4. 

Section 5 outlines the main experiments in the paper, including materials property prediction and an efficiency analysis . The results generally show that the proposed dynamic frames improve Crystalformer modeling performance across all datasets while achieving best performance in most cases. The efficiency analysis shows that CrystalFramer incurs an extra compute cost. Section 6 provides a visual analysis of the dynamic frames, as well as discussion on limitations along with suggestions for using dynamic frames for equivariant prediction and molecular modeling.

### Strengths
* The idea of dynamic frames proposed in the paper is a novel and effective way to include relevant inductive biases for crystal structure modeling.
* The paper is well written with relevant details described and convincing experiments followed by detailed analysis.
* The paper candidly discusses advantages and limitations of the proposed method.

### Weaknesses
 * The paper could be further with additional discussion of related work for machine learning potentials. The current focus of the study is mainly on properly modeling, so this would probably fit as potential future work. There be advantages and disadvantages of using CrystalFramer in such a context. Similarly, the paper can also discuss potential application to modeling of crystals with surfaces, such as catalyst.
* The dynamic frames provide a new dimension for analysis for how local neighborhoods interact in geometric deep learning. The paper could be strengthened by discussing the frames across different materials and/or different stages of the training process.

### Questions
* Could you talk more about scalability of your method? This would be especially relevant when modeling larger supercell that have more atoms.
* Did you notice an evolution of the dynamic frames as training progressed? Are there consistencies across some types of materials?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work explores an alternative, more powerful version of frame averaging networks and applies it to crystal property prediction tasks. Instead of using a fixed lattice frame or one calculated from the PCA of the moment tensor of the atoms, the authors propose to learn "dynamic frames" for each individual atom. They propose two methods to do this: Either by calculating the PCA from weighted atoms or constructing the frames by greedily choosing the highest weighted atoms, where the weights in both cases are equal to the attention weights in their transformer architecture. They show that this results in significant performance gains and that the model exhibits intuitive, sensible behaviour, where the earlier layers attend to closer atoms, and later layers attend to further away atoms.

### Strengths
Crystal property prediction is an important topic, and (stochastic) frame averaging is a promising direction for the task. Using the novel idea of dynamic frames, the proposed method improves stochastic frame averaging for crystal property prediction by a large margin. Therefore, the contribution seems significant and novel. It is believable that the proposed "dynamic frames" make the model more expressive, although I find it hard to get an intuitive understanding of what the angles between the learned frames and direction vectors could learn or why they could represent useful features. The experimental results show strong improvements on two datasets and against the base model (Crystalformer) and other state-of-the-art models.

### Weaknesses
The biggest weakness of this paper is, in my opinion, the writing. Many sentences are grammatically incorrect or use strangely constructed, overly long sentences. This makes it much harder to read the paper than it should be. A non-exhaustive list of examples:

Line 121: "... are linear projects of current state x, σi is a tail-length variable
of Gaussian distance-decay attention adaptively derived from xi, ψij(n) is geometric position
embedding that encodes interatomic". This misses several articles, and I assume the authors mean "projections" not "projects"

Line 198: "... and local view of entire crystal ..." misses the article "the"

Line 234: "This perturbation scheme is considered to implement the stochastic FA" I am not sure what this sentence means

I strongly recommend that the authors use a grammar tool like Grammarly or an LLM to help streamline their writing.

### Questions
In the runtime comparison, Table 4: How can PotNet take only 43s/epoch to train but 313ms for inference, while CrystalFramer takes almost double the time to train with 74s but is nearly ten times faster during inference? Can you explain this large discrepancy?

In line 298: The model uses the cosine of the angles. This would map pi/2 and -pi/2 to the same value 0. Have you considered using a concatenation of both sine and cosine of the angles as features? It might make the model more expressive.

### Soundness
3

### Presentation
3

### Contribution
3
