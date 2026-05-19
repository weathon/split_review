### Summary

This paper proposes an autoregressive model that decomposes molecular generation into a sequence of discrete and interpretable steps using molecular fragments as units. The generation of the molecular structures can be biased toward desired chemical properties.

### Soundness

2

### Presentation

2

### Contribution

1

### Strengths

* The background is introduced clearly, and the problem is well motivated.
* The proposed method is reasonable. It is interesting to decompose molecular generation into a sequence of discrete and interpretable steps using molecular fragments as units.

### Weaknesses

#### Some Related Works

[1] Fragment-based molecule generation and optimization with recurrent neural networks
[2] Fragment-based deep generative models for drug discovery
[3] A Hierarchical Graph Variational Autoencoder for Molecule Generation

#### comment

 * The novelty of this work was not clearly explained.
* Some key related works were missing, which seem to propose a very similar idea. See the following Questions section for details.
* The experimental section is weak. Only the proposed method is evaluated, and the evaluation metrics are limited.

### Suggestions

The authors should more clearly articulate the novelty of their approach in the context of existing fragment-based molecular generation methods. While the use of fragments as building blocks is not new, the specific way in which these fragments are selected and assembled could be a novel contribution. The authors should explicitly compare their method to existing approaches, highlighting the specific differences in the fragment selection process, the training methodology, and the overall architecture. For example, if the method uses a transformer architecture, this should be explicitly stated and compared to the RNN-based approaches in the literature. Furthermore, the authors should clarify how their method addresses the limitations of existing methods, such as the computational cost of exploring the fragment space or the ability to generate molecules with specific chemical properties. A more detailed explanation of the novelty will help to justify the contribution of this work.

The experimental section needs significant improvement. The authors should include comparisons to other state-of-the-art methods for molecular generation, not just their own method with different configurations. This should include both fragment-based and non-fragment-based approaches. The evaluation metrics should also be expanded to include metrics that are relevant to the specific task of molecular property prediction. For example, if the method is designed to generate molecules with specific solubility or toxicity properties, the evaluation should include metrics that measure the accuracy of these predictions. The authors should also provide more details about the datasets used for training and evaluation, including the size and diversity of the datasets. A more comprehensive evaluation will help to demonstrate the effectiveness of the proposed method and its advantages over existing approaches.

Finally, the authors should address the issue of missing related works. The papers mentioned in the review should be discussed in detail, highlighting the similarities and differences between the proposed method and the existing approaches. This discussion should be included in the related work section of the paper. The authors should also consider including a table that compares the proposed method to existing methods across various dimensions, such as the fragment representation, the generation process, and the training methodology. This will help to clarify the novelty of the proposed method and its contribution to the field. The authors should also consider including an ablation study to evaluate the impact of different components of their method on the overall performance.

### Questions

* This sentence in the Introduction section: ``Similarly, we enforce chemical validity during the generation process, and, like JTNN and HierVAE, we use a coarse-graining procedure to extract molecular fragments.'' was not clearly explained. What do ``coarse-graining procedure'' and ``extract'' mean? Could you rephrase this sentence to make it clearer?
* The key idea of this paper seems to be similar to those in the following papers. However, these papers were not cited or discussed in the related work section.
    * Liu, Yutong, et al. "Fragment-based molecule generation and optimization with recurrent neural networks." Molecular AI 2.1 (2019): 124-135.
    * Kim, Yunsang, et al. "Fragment-based deep generative models for drug discovery." Journal of chemical information and modeling 62.11 (2022): 2775-2787.
    * Jin, Dijiang, et al. "A Hierarchical Graph Variational Autoencoder for Molecule Generation." Advances in Neural Information Processing Systems 33 (2020).
* The Introduction section was too long. It would be helpful to include some highlights of the contributions to help the readers understand the key points of this work.
* The Experimental section was too weak. Only the proposed method was evaluated, and the evaluation metrics were limited.
    * Were there any baseline methods for comparison? For example, the three papers mentioned above.
    * What evaluation metrics were used? For example, if the generation was biased toward the desired chemical properties, how well was this achieved?

### Rating

3

### Confidence

4

**********
