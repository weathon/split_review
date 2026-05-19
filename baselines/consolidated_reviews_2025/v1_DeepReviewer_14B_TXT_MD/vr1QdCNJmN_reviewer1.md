### Summary

In this work, the authors Iyer & Bilmes (2012b) considered Bregman divergences on discrete domains using submodular functions as generating functions, the discrete analogs of convex functions. In this paper, we further generalize this framework to cases where the generating function is neither submodular nor supermodular, thus increasing the flexibility and representational capacity of the resulting divergence, which we term the difference-of-submodular Bregman divergence. Additionally, we introduce a learnable form of this divergence using permutation-invariant neural networks (NNs) and demonstrate through experiments that it effectively captures key structural properties in discrete data. As a result, the proposed method significantly improves the performance of existing methods on tasks such as clustering and set retrieval problems.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

The submodular-Bregman divergence (Iyer & Bilmes, 2012b) is the first to tackle this problem with the theory of submodular set functions. It is based on the fact that subgradients and supergradients can be defined for any submodular function. Therefore, a Bregman-like divergence can be defined through a submodular function f in the way analogous to the standard Bregman divergence (1). 
Although the submodular-Bregman divergence is quite natural and intuitive, it is not clear whether it satisfies the definition of divergences. This problem comes from identifiability of the divergence: D(x, y) = 0 => x = y in Definition 1.1. In the usual Bregman divergence (1), the strict convexity is required for f to guarantee the identifiability. Similar to the usual Bregman divergence, the subgradients or supergradients are insufficient to make it a divergence; it may be necessary to assume the existence of strict subgradients or strict supergradients. 
Another issue in the submodular-Bregman divergence is that the choice of the submodular function is ad-hoc. Although Iyer & Bilmes (2012b) introduces several concrete examples of the submodular function, the resulting divergences are again the forms with respect to simple set operations. So it is unclear whether they actually overcome the difficulty of the classical metrics between sets. Therefore, a more flexible framework for handling the submodular-Bregman divergence is necessary, and it would be even better if we could extend the capability of submodular-Bregman divergence.

### Weaknesses

#### Some Related Works


#### comment

I do not think this paper is a good fit for this conference. The main contributions of this paper are theoretical and methodological, which are independent of learning theory and practice. The experimental section is weak and does not provide any insights for the learning community. I would recommend the authors to consider submitting to a more appropriate venue, such as ICLR, ICML, or a related machine learning conference.

### Suggestions

The paper's core weakness lies in its limited connection to practical machine learning problems, which is crucial for a conference like ICLR. While the theoretical framework of difference-of-submodular Bregman divergence (DBD) is interesting, the paper does not adequately demonstrate its utility in real-world learning scenarios. The experiments, while present, are not compelling enough to show the advantages of the proposed DBD over existing methods. For instance, the clustering and set retrieval tasks lack a thorough comparison with state-of-the-art techniques, and the performance gains are not convincingly attributed to the unique properties of DBD. The paper would benefit significantly from more extensive experiments that showcase the practical advantages of DBD, such as its ability to handle high-dimensional discrete data or its robustness to noisy inputs. Furthermore, the current experiments do not explore the sensitivity of the method to hyperparameter choices, which is a critical aspect for practical applications.

To improve the paper's relevance to the learning community, the authors should focus on demonstrating how the proposed DBD can be effectively integrated into existing learning pipelines. This could involve showing how DBD can be used as a loss function or a distance metric in various learning tasks, such as classification, regression, or reinforcement learning. The paper should also explore the computational complexity of the proposed method and provide insights into its scalability for large datasets. A detailed analysis of the computational cost of calculating the DBD, especially in comparison to other divergence measures, would be valuable. Additionally, the authors should consider providing a more thorough discussion of the limitations of their approach and identify potential areas for future research. This would help the readers understand the scope and applicability of the proposed method and its potential for further development.

Finally, the paper needs to provide a more concrete justification for why the proposed DBD is superior to existing divergence measures in specific learning contexts. The current theoretical analysis, while rigorous, does not provide sufficient insights into the practical benefits of DBD. The authors should consider providing a more intuitive explanation of how the difference-of-submodular structure enables DBD to capture complex relationships in discrete data. This could involve providing visualizations or illustrative examples that highlight the unique properties of DBD. Furthermore, the paper should explore the potential of DBD for addressing challenging machine learning problems, such as few-shot learning or domain adaptation. By demonstrating the effectiveness of DBD in these contexts, the authors can significantly enhance the paper's impact and relevance to the learning community.

### Questions

Please see above.

### Rating

3

### Confidence

5

**********
