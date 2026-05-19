### Summary

This paper introduces a large-scale dataset of 15,625 WRN-style architectures trained with adversarial training. The authors provide a comprehensive evaluation of these architectures, including clean and robust accuracies, training statistics, and metrics like stable accuracy and empirical Lipschitz constant. The dataset aims to facilitate research in neural architecture search (NAS) for adversarial robustness.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The dataset is the first to comprehensively evaluate WRN-style architectures for adversarial robustness, providing a valuable resource for the community.
- The experiments are thorough, with detailed analysis and insights into the relationship between architecture and robustness.
- The authors provide pre-trained checkpoints and extensive metrics, making the dataset accessible for further research.

### Weaknesses

#### Some Related Works


#### comment

 - The dataset is limited to WRN architectures, which may restrict its applicability to other types of models.
- The evaluation is conducted on CIFAR-10, which may not generalize to larger datasets like ImageNet.
- The paper could benefit from a more detailed discussion on the practical implications of the findings for designing robust architectures.

### Suggestions

The authors should consider expanding the dataset to include other popular architectures beyond WRNs, such as ResNets or even more recent architectures like Transformers. This would significantly increase the dataset's utility and allow researchers to explore the interplay between different architectural choices and adversarial robustness. For example, the dataset could include a range of Transformer variants with varying numbers of layers, attention heads, and embedding dimensions. This would enable a more comprehensive understanding of how architectural factors influence robustness across different model families. Furthermore, the inclusion of diverse architectures would allow for more generalizable conclusions and facilitate the development of robust design principles applicable to a wider range of models.

To address the limitation of using only CIFAR-10, the authors should perform a more rigorous analysis of how the observed trends in their dataset translate to larger, more complex datasets like ImageNet. This could involve training a subset of the architectures on ImageNet and comparing the robustness trends observed on CIFAR-10 with those on ImageNet. Specifically, the authors should investigate whether the correlations between stable accuracy, Lipschitz constant, and adversarial robustness observed on CIFAR-10 hold true on ImageNet. If the trends do not directly translate, the authors should investigate the reasons behind these discrepancies and provide guidance on how to adapt the findings to larger datasets. This could involve analyzing the impact of dataset complexity, image resolution, and the number of classes on the relationship between architecture and robustness. Such an analysis would significantly enhance the practical value of the dataset.

Finally, the paper should include a more in-depth discussion of the practical implications of the findings for designing robust architectures. The authors should provide concrete guidelines on how to leverage the dataset to identify robust architectural patterns. For example, they could analyze the dataset to identify specific architectural configurations that consistently exhibit high robustness across different adversarial attacks. They could also explore the relationship between architectural parameters and robustness, providing insights into which parameters are most critical for achieving robustness. This discussion should go beyond simply stating that stable accuracy and Lipschitz constant are correlated with robustness; it should provide actionable guidance on how to use these metrics to design more robust architectures. The authors should also discuss the limitations of their findings and suggest future research directions to address these limitations.

### Questions

- How do the findings generalize to other datasets beyond CIFAR-10?
- Can the authors provide more insights into the relationship between stable accuracy, Lipschitz constant, and adversarial robustness?
- How can the dataset be used to develop new NAS algorithms for finding robust architectures?

### Rating

6

### Confidence

4

**********
