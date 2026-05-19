### Summary

This paper proposes an active probabilistic drug discovery method to reduce the number of docking computations and wet experiments. The method first clusters molecules based on the Tanimoto similarity of the morgan fingerprint and then selects representative molecules from each cluster based on the accumulated pairwise probability. The method then adopts active learning to select molecules for wet experiments to refine the model. The authors demonstrate the effectiveness of the method on the DUD-E and LIT-PCBA datasets in terms of reducing the number of docking computations and wet-lab experiments.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

1 poor

### Strengths

The method is clearly described, and the code is provided.

### Weaknesses

#### Some Related Works


#### comment

The method is clearly described, and the code is provided.

The paper does not meet the bar of ICLR. The paper uses many well-known methods, such as Tanimoto similarity, and the active learning part is also quite simple and lacks novelty. The authors just combine different methods without proposing new methods or any new insights. The experimental results are also not strong enough to show the superiority of the proposed method. The authors only compared the proposed method with Vina Enumeration (VE). There are many other active learning methods, and the authors should compare the proposed method with these methods.

### Suggestions

The paper's core weakness lies in its incremental approach, combining existing techniques without introducing significant novelty or demonstrating substantial improvements over existing methods. The use of Tanimoto similarity for clustering, while common, is not inherently novel, and the paper does not explore alternative similarity measures or justify the choice of Tanimoto similarity in this specific context. The active learning component, which selects molecules for wet experiments, also lacks sophistication. The authors should have explored more advanced active learning strategies, such as those based on uncertainty sampling or Bayesian optimization, and provided a clear rationale for their chosen approach. Furthermore, the paper fails to adequately address the limitations of the proposed method, such as its sensitivity to the choice of fingerprints or the potential for bias in the selection of representative molecules.

To improve the paper, the authors should focus on demonstrating the novelty and effectiveness of their approach. This could involve comparing their method against a wider range of active learning algorithms, including those that are specifically designed for drug discovery. The authors should also provide a more thorough analysis of the experimental results, including a discussion of the limitations of their method and the potential for future improvements. For example, they could investigate the impact of different fingerprint types on the performance of their method or explore the use of more sophisticated clustering algorithms. Additionally, the authors should provide a more detailed explanation of the experimental setup, including the specific parameters used for each method and the criteria for selecting molecules for wet experiments. This would allow other researchers to reproduce their results and build upon their work.

Finally, the authors should consider exploring alternative approaches to active learning that may be more suitable for drug discovery. For example, they could investigate the use of reinforcement learning to optimize the selection of molecules for wet experiments or explore the use of graph neural networks to predict the binding affinity of molecules. These approaches could potentially lead to more efficient and effective drug discovery pipelines. The paper should also include a more detailed discussion of the potential impact of their work, including the potential for reducing the cost and time required for drug discovery. This would help to justify the significance of their work and highlight its potential benefits for the field.

### Questions

The proposed method is only compared with Vina Enumeration (VE). There are many other active learning methods, and the authors should compare the proposed method with these methods.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
