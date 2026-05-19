### Summary

This paper introduces a dataset of 15,625 WRN architectures evaluated under adversarial training. The authors provide a comprehensive analysis of the relationship between architecture and adversarial robustness. They also offer insights into the limitations of existing robust architecture principles and highlight the importance of considering stable accuracy and empirical Lipschitz constants in evaluating robustness.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The experiments are comprehensive. The authors provide a detailed analysis of the relationship between architecture and adversarial robustness, considering various factors such as depth, width, stable accuracy, and empirical Lipschitz constants.

### Weaknesses

#### Some Related Works

[1] B. Kalimeris, et al., Robust Overfitting may be mitigated by properly learned features, ICLR 2021.
[2] S. Zengin, et al., Understanding factors that affect robust overfitting in adversarial training, ICML 2022.
[3] Z. Zhou, et al., How does the number of classes affect adversarial training?, ICML 2022.

#### comment

1. The motivation of the paper is not clear. The authors claim that "advancements in enhancing adversarial robustness (AR) through architectural innovations remain limited." However, there are many papers exploring the impact of architecture on adversarial robustness. The authors also mention that "advancements in enhancing adversarial robustness (AR) through architectural innovations remain limited." However, there are many papers exploring the impact of architecture on adversarial robustness, which seems to contradict the claim that "a comprehensive investigation into how different network architectures can contribute to improving adversarial robustness. We posit that such a large-scale exploration is both timely and critical." If the authors believe that a large-scale exploration is necessary, they should provide a more detailed justification for why this is the case. Specifically, the authors should clarify what specific limitations in existing architectural explorations motivate their work. For example, are existing studies limited in the scope of architectures considered, the scale of the experiments, or the specific adversarial training methods used? Without a clear articulation of these limitations, the motivation for a large-scale dataset remains unclear.
2. The authors claim that NARes can serve as a NAS benchmark dataset. However, the dataset is built on a specific architecture (WRN) and a specific dataset (CIFAR-10), which may limit its generalization to other architectures and datasets. The authors should provide more evidence to support the claim that NARes can be generalized to other architectures and datasets. For example, the authors could conduct experiments on other architectures and datasets to demonstrate the generalizability of NARes. It would be beneficial to see results on architectures beyond WRNs, such as VGG or more recent architectures like Transformers, and on datasets with higher resolution and more complex data distributions than CIFAR-10. This would provide a more robust assessment of the dataset's utility as a NAS benchmark.
3. The authors only consider one type of adversarial training (AT) in building the NARes dataset. However, there are many other AT methods, such as TRADES and MART. The authors should discuss the impact of different AT methods on the generalization of NARes. For example, the authors could analyze how the architecture-robustness relationships observed with PGD AT might differ when using other AT methods. This is crucial because different AT methods may lead to different optimal architectures, and the dataset's usefulness would be limited if it only reflects the characteristics of a single AT method.
4. The authors do not discuss the limitations of the NARes dataset in detail. For example, the authors should discuss the potential biases in the dataset and how these biases might affect the generalization of the dataset. The authors should also discuss the computational cost of building and using the NARes dataset. For instance, what are the computational resources required to train and evaluate models on this dataset, and how does this compare to other similar datasets? A thorough discussion of these limitations is essential for potential users to understand the scope and applicability of the dataset.
5. The authors do not compare NARes with other existing datasets on adversarial robustness. For example, the authors could compare NARes with other datasets on adversarial robustness, such as RobustBench [4], to demonstrate the advantages and disadvantages of NARes. A detailed comparison with existing benchmarks would help to position NARes within the broader landscape of adversarial robustness research and highlight its unique contributions and limitations.
6. The authors do not provide a clear roadmap for future research directions based on the NARes dataset. For example, the authors could suggest specific research questions that can be addressed using NARes. It would be helpful to see concrete examples of research questions that can be explored using this dataset, such as investigating the impact of specific architectural components on robustness, or developing new NAS algorithms that are specifically tailored for adversarial robustness.

### Suggestions

To strengthen the paper, the authors should first clarify the specific gaps in the current understanding of architecture's role in adversarial robustness that their dataset aims to address. While many studies have explored this relationship, the authors need to articulate what limitations exist in these prior works that justify the need for a large-scale dataset like NARes. For instance, are existing studies limited by the scale of their experiments, the diversity of architectures considered, or the specific adversarial training methods employed? The authors should provide a detailed explanation of how NARes overcomes these limitations, making a clear case for its necessity. This could involve a more thorough discussion of the specific research questions that NARes is designed to address, and how these questions differ from those explored in previous studies. Furthermore, the authors should provide a more detailed analysis of the existing literature, highlighting the specific shortcomings that NARes aims to resolve. This would help to establish the unique contribution of their work and justify the resources invested in creating such a large-scale dataset.

Secondly, the authors should address the limitations of the dataset's scope, which is currently restricted to WRN architectures and the CIFAR-10 dataset. To demonstrate the generalizability of NARes, the authors should conduct experiments on a wider range of architectures and datasets. This could include testing on architectures such as VGG, ResNets, or even more recent architectures like Transformers, and on datasets with higher resolution and more complex data distributions, such as ImageNet or TinyImageNet. Such experiments would provide a more robust assessment of the dataset's utility as a NAS benchmark for adversarial robustness. Additionally, the authors should investigate how the architecture-robustness relationships observed in WRNs on CIFAR-10 translate to other architectures and datasets. This would involve analyzing whether the same architectural patterns that lead to robustness in WRNs on CIFAR-10 also lead to robustness in other settings. If the relationships are not consistent, the authors should discuss the potential reasons for these discrepancies and how they might impact the use of NARes as a general NAS benchmark. This analysis would be crucial for establishing the broader applicability of the dataset.

Finally, the authors should address the limitation of using only one adversarial training method (PGD) in constructing the dataset. They should explore how the architecture-robustness relationships might change when using other adversarial training methods, such as TRADES or MART. This could involve retraining a subset of the architectures in NARes using these different methods and comparing the resulting robustness metrics. The authors should also discuss the potential implications of these differences for the use of NARes as a benchmark. If different AT methods lead to different optimal architectures, the authors should consider how this might impact the dataset's utility for NAS algorithms. Furthermore, the authors should provide a more detailed discussion of the computational cost associated with building and using the NARes dataset. This should include an analysis of the computational resources required to train and evaluate models on the dataset, and how this compares to other similar datasets. This information would be valuable for potential users of the dataset, allowing them to assess the feasibility of using NARes for their own research.

### Questions

1. What is the specific motivation for creating a large-scale dataset on adversarial robustness? What are the limitations of existing studies that the authors aim to address with this dataset?
2. How can the authors demonstrate the generalizability of NARes to other architectures and datasets?
3. How do different adversarial training methods affect the generalization of NARes? How can the authors address the limitation of only considering one type of AT in building the dataset?
4. What are the potential biases in the NARes dataset, and how can these biases be mitigated?
5. How does the computational cost of building and using NARes compare to other similar datasets?
6. How does NARes compare to other existing datasets on adversarial robustness, such as RobustBench [4]?
7. What are the specific research questions that can be addressed using the NARes dataset?

### Rating

3

### Confidence

4

**********
