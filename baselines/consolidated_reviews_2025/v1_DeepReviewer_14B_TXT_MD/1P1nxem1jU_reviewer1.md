### Summary

The paper proposes a spectral approach to graph data augmentation, which aims to better understand the spectral behavior of graph modifications and their interplay with inherent graph properties. The key idea is to preserve essential graph properties while diversifying augmented graphs by only changing the high-frequency part of the spectrum of graphs. The proposed Dual-Prism (DP) augmentation strategies include DP-Noise and DP-Mask. The authors provide extensive experiments to demonstrate the effectiveness of the proposed methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of using the spectral approach for graph data augmentation is interesting.
3. The authors provide extensive experiments to demonstrate the effectiveness of the proposed methods.

### Weaknesses

#### Some Related Works


#### comment

1. The authors provide some spectral analysis insights. However, some of the observations are well-known in spectral graph theory literature. The authors are encouraged to discuss how their observations are connected to the existing results and what are the differences.
2. The proposed methods are based on the assumption that the low-frequency part of the spectrum is more important than the high-frequency part. It is better to provide some theoretical justification for this assumption.
3. In the experiments, the authors only compare the proposed methods with some simple baselines. It is necessary to compare with the state-of-the-art (SOTA) augmentation methods.

### Suggestions

The paper would benefit from a more rigorous discussion of the novelty of the spectral insights. While the idea of using spectral analysis for graph augmentation is interesting, the paper needs to clearly articulate how the specific observations made about the impact of edge flips on different frequency components are novel and not simply a restatement of well-established principles in spectral graph theory. For instance, the observation that low-frequency components are more resilient to edge alterations should be contextualized within existing literature on spectral graph theory, perhaps by discussing specific theorems or results that relate graph structure to the spectral properties. The authors should provide a more detailed analysis of how their findings extend or differ from these existing results, rather than simply stating that the observations are consistent with previous findings. A more in-depth discussion of the specific conditions under which these observations hold, and any limitations of these observations, would also be beneficial.

Furthermore, the assumption that low-frequency components are more important than high-frequency components for preserving graph properties needs more theoretical backing. While the empirical results might support this assumption, a theoretical justification would significantly strengthen the paper. The authors should explore existing theoretical frameworks that link the different frequency components of the graph spectrum to specific graph properties. For example, they could investigate how the low-frequency eigenvalues relate to graph connectivity, diameter, or other relevant properties. A theoretical analysis could involve showing that perturbations in the low-frequency spectrum have a more significant impact on these properties compared to perturbations in the high-frequency spectrum. This could involve using tools from spectral graph theory, such as eigenvalue interlacing or perturbation bounds, to provide a more rigorous foundation for their approach. Without this theoretical justification, the method appears somewhat ad-hoc.

Finally, the experimental evaluation needs to be significantly strengthened by including comparisons with state-of-the-art graph augmentation methods. While the authors compare their method with some simple baselines, it is crucial to demonstrate that the proposed approach outperforms existing methods that are specifically designed for graph data augmentation. The authors should include a wider range of augmentation techniques, including those that operate in the spatial domain and those that use more sophisticated spectral techniques. This would provide a more comprehensive evaluation of the proposed method's effectiveness and allow for a better understanding of its strengths and weaknesses compared to existing approaches. The comparison should also include a discussion of the computational cost of the proposed method compared to the baselines, as this is an important factor in practical applications.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
