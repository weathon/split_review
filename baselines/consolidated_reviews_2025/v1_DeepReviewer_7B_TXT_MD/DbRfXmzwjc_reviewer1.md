### Summary

The authors propose a new method to generate molecular graphs in an all-at-once fashion. Instead of generating predefined molecular motifs, the proposed method first generates a set of "shapes", which are just binary matrices representing connectivity, and then atom types and bond types are generated conditioned on the shape. The shapes are generated in a coarse-to-fine manner, starting with the overall structure of the molecule and then progressively adding finer details. The authors demonstrate the effectiveness of the proposed method on standard molecular generation benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed method is well-motivated, and the coarse-to-fine generation of the molecular shape is an interesting idea.
- The authors provide a comprehensive set of experiments that demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works

[1] Learning molecular representations using chemical language game
[2] Geometric and physical modeling of 3d molecular structures with graph diffusion models

#### comment

 - The proposed method is essentially a hierarchical variant of existing motif-based methods, such as JT-VAE and MoLeR. The only difference seems to be that the proposed method generates the shapes in a coarse-to-fine manner, whereas existing methods typically generate motifs in a bottom-up fashion. While this approach is interesting, it is not clear to me that it is fundamentally different from existing methods. It would be helpful if the authors could provide more justification for this design choice and explain why this approach is expected to be more effective.

- The authors claim that the proposed method is a graph-based model, but it still requires a pretrained language model to generate atom and bond labels. This makes the proposed method more similar to existing motif-based methods than to pure graph-based methods such as GraphAF and DiGress. It would be helpful if the authors could provide more justification for this claim and explain how the proposed method differs from existing motif-based methods in terms of its graph-based nature.

- The authors should consider comparing their method to more recent graph-based baselines, such as GeoMol [1] and Graph-Diffusion [2]. These methods have demonstrated strong performance on molecular generation benchmarks and would provide a more comprehensive evaluation of the proposed method.

- The authors should consider comparing their method to more recent motif-based baselines, such as MolDiff [3].

- The authors should consider comparing their method to other shape-based methods, such as Shape2Vec [4].

### Suggestions

The core idea of generating molecular shapes in a coarse-to-fine manner is interesting, but the paper needs to provide a more compelling justification for its novelty and advantages over existing motif-based approaches. The authors should elaborate on the specific mechanisms that make their hierarchical shape generation superior to bottom-up motif assembly. For example, they could discuss how the coarse-to-fine approach allows for better control over the structural diversity of generated molecules, or how it avoids the limitations of fixed or predefined motifs. A more detailed analysis of the differences in the search space explored by the proposed method and existing methods would be beneficial. Furthermore, the authors should provide a more rigorous comparison of the computational cost and efficiency of their method compared to existing motif-based methods, as the hierarchical generation might introduce additional overhead.

While the authors claim that their method is graph-based, the reliance on a pretrained language model for atom and bond label generation raises questions about its true graph-based nature. The authors should clarify how their method fundamentally differs from existing motif-based methods in terms of its graph representation and manipulation. A more detailed explanation of how the generated shapes are converted into actual molecular graphs, including the atom and bond assignments, would be helpful. The authors should also discuss the limitations of their approach in terms of graph-based operations, such as bond breaking and formation, and how these limitations might affect the quality of generated molecules. It would be beneficial to explore alternative approaches that do not rely on a pretrained language model for label generation, or to provide a more thorough analysis of the impact of this component on the overall performance of the method.

Finally, the authors should expand their experimental evaluation to include more recent and relevant baselines, particularly in the areas of graph-based and shape-based molecular generation. Comparing against methods like GeoMol [1], Graph-Diffusion [2], and MolDiff [3] would provide a more comprehensive assessment of the proposed method's performance. The authors should also consider including Shape2Vec [4] as a baseline to further demonstrate the advantages of their shape-based approach. Additionally, the authors should provide a more detailed analysis of the generated molecules, including their structural diversity, novelty, and chemical validity. A more thorough evaluation of the method's ability to generate molecules with specific properties would also be valuable.

### Questions

- What is the key difference between the proposed method and existing motif-based methods? Why is the coarse-to-fine generation of shapes expected to be more effective than the bottom-up motif assembly?

- Why is the proposed method considered a graph-based model, given that it still requires a pretrained language model to generate atom and bond labels?

- How does the proposed method compare to more recent graph-based and shape-based baselines?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
