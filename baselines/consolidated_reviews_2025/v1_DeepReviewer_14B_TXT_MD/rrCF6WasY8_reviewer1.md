### Summary

This paper proposes Secure Distributed DP-Helmet, a non-interactive distributed learning algorithm with differential privacy. The main idea is to have each party run a local learning algorithm, add noise, and use secure summation to aggregate the local models. The authors specifically consider two learning algorithms: SVM and softmax-SVM. The authors provide both theoretical and empirical results for the proposed method.

### Soundness

2 fair

### Presentation

1 poor

### Contribution

2 fair

### Strengths

The proposed method is simple and practical. The authors consider two different settings where each party contributes one data point or small datasets. The theoretical and empirical results consider both settings. The empirical results are promising.

### Weaknesses

#### Some Related Works


#### comment

The main weakness of this paper is the presentation. I find this paper hard to follow. There are many notations, but they are not easy to keep track off or remember. For example, there are multiple definitions of sensitivity. In Definition 1, the sensitivity is for datasets, while in Lemma 2, it is for the learning algorithm. The sensitivity in Lemma 13 is different from the previous two. The authors should simplify the presentation and make it easier to follow.

The authors claim that output sensitivity suffices for strong privacy results. However, all the sensitivity definitions in this paper are input sensitivity. Moreover, the claim that a fraction of honest users is not new. It has been considered in prior work such as Jayaraman et al., 2018. So, the first contribution is not valid.

The threat model is not clear. In the threat model, the authors assume an honest majority. Then, the authors also assume the adversary has full knowledge about each user’s dataset except for one point. This seems to give the adversary too much information.

I am concerned about the correctness of Theorem 8. The authors claim it is computational DP, but I do not see where the computational aspect comes from. The theorem seems to be statistical DP. Moreover, the theorem relies on the secure summation protocol, which has not been introduced yet. The term nu is also not defined.

The utility results for SVM converge in the limit, which is not ideal. It would be better to have convergence rates that are not asymptotic.

The experiments only consider pre-trained models, which makes the results less meaningful. It would be more interesting to have experiments with models trained from scratch.

### Suggestions

The paper's presentation needs significant improvement to enhance clarity and readability. The current notation system is cumbersome, with multiple definitions of sensitivity that are not clearly distinguished. A more streamlined approach is needed, perhaps by introducing a unified sensitivity definition that encompasses all the different cases. The authors should also consider using a consistent notation style throughout the paper, avoiding the use of multiple similar symbols (e.g., $\mathcal{S}, \mathcal{V}, \bar{\mathcal{S}}, \bar{\mathcal{V}}$). Furthermore, the paper would benefit from a more intuitive explanation of the key concepts, such as the secure summation protocol and the notion of computational differential privacy. The authors should provide concrete examples to illustrate these concepts and make them more accessible to the reader. A table summarizing the key notations and definitions would also be beneficial.

The claim regarding output sensitivity needs to be clarified and justified. The current definitions of sensitivity are all based on input sensitivity, which contradicts the claim. The authors should either provide a clear definition of output sensitivity and demonstrate how it is used in their analysis, or rephrase their claim to accurately reflect the input sensitivity framework. The threat model also requires further clarification. The assumption of an honest majority is reasonable, but the additional assumption that the adversary has full knowledge of each user's dataset, except for one point, is overly strong and unrealistic. This assumption should be justified or relaxed. The authors should clearly define the adversary's capabilities and limitations, and explain how these assumptions impact the security analysis.

The concerns about Theorem 8 need to be addressed. The authors should clearly explain the computational aspect of the differential privacy guarantee and how it arises from the secure summation protocol. The term nu needs to be defined, and the connection between the theorem and the secure summation protocol should be made explicit. The utility results for SVM should be strengthened by providing non-asymptotic convergence rates. This would provide a more practical understanding of the algorithm's performance. Finally, the experimental section should be expanded to include experiments with models trained from scratch, not just pre-trained models. This would provide a more comprehensive evaluation of the proposed method's performance and its applicability to real-world scenarios.

### Questions

Please address the questions in the weakness section.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
