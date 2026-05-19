### Summary

The paper proposes a distributed learning algorithm that achieves a similar utility-privacy tradeoff to centralized training with only one invocation of secure summation. The key idea is to let each user train a model locally and then average the models via secure summation. The authors provide theoretical analysis of the proposed algorithm and experimental results on CIFAR-10 and CIFAR-100 datasets.

### Soundness

3 good

### Presentation

2 fair

### Contribution

3 good

### Strengths

The paper proposes a novel distributed learning algorithm that achieves a similar utility-privacy tradeoff to centralized training with only one invocation of secure summation. The authors provide theoretical analysis of the proposed algorithm and experimental results on CIFAR-10 and CIFAR-100 datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is not well-written and hard to follow. There are many notations, but they are not easy to keep track off or remember. For example, there are multiple definitions of sensitivity. In Definition 1, the sensitivity is for datasets, while in Lemma 2, it is for the learning algorithm. The sensitivity in Lemma 13 is different from the previous two. The authors should simplify the presentation and make it easier to follow.

2. The authors claim that output sensitivity suffices for strong privacy results. However, all the sensitivity definitions in this paper are input sensitivity. Moreover, the claim that a fraction of honest users is not new. It has been considered in prior work such as Jayaraman et al., 2018. So, the first contribution is not valid.

3. The threat model is not clear. In the threat model, the authors assume an honest majority. Then, the authors also assume the adversary has full knowledge about each user’s dataset except for one point. This seems to give the adversary too much information.

4. I am concerned about the correctness of Theorem 8. The authors claim it is computational DP, but I do not see where the computational aspect comes from. The theorem seems to be statistical DP. Moreover, the theorem relies on the secure summation protocol, which has not been introduced yet. The term nu is also not defined.

5. The utility results for SVM converge in the limit, which is not ideal. It would be better to have convergence rates that are not asymptotic.

6. The experiments only consider pre-trained models, which makes the results less meaningful. It would be more interesting to have experiments with models trained from scratch.

### Suggestions

The paper needs significant improvements in clarity and presentation. The current notation is confusing, with multiple definitions of sensitivity that are not clearly distinguished. The authors should provide a clear and consistent definition of sensitivity, and explain how it relates to the different components of their algorithm. For example, they should clarify the difference between input sensitivity and output sensitivity, and how these concepts are used in their analysis. Furthermore, the paper should clearly define all terms and notations before they are used, and provide a table summarizing the key notations. The authors should also consider using a more intuitive and accessible writing style, avoiding overly technical jargon where possible. The current presentation makes it difficult to understand the core ideas and contributions of the paper.

The authors should also address the concerns about the threat model and the privacy guarantees. The assumption that the adversary has full knowledge of each user's dataset, except for one point, is unrealistic and needs to be justified. The authors should clearly define the adversary's capabilities and limitations, and explain how these assumptions impact the security analysis. Furthermore, the authors should clarify the computational aspect of the differential privacy guarantee in Theorem 8. They should provide a detailed explanation of how the secure summation protocol ensures computational DP, and how the term nu is defined and used in the analysis. The current description is vague and does not provide sufficient detail to assess the validity of the claim. The authors should also clearly state the assumptions about the secure summation protocol, and how these assumptions affect the overall privacy guarantees.

Finally, the authors should provide more comprehensive experimental results. The current experiments only consider pre-trained models, which limits the practical relevance of the findings. The authors should include experiments with models trained from scratch, to demonstrate the effectiveness of their algorithm in more realistic scenarios. Additionally, the authors should provide more details about the experimental setup, including the specific parameters used, the training procedure, and the evaluation metrics. This would allow other researchers to reproduce their results and assess the practical implications of their work. The authors should also provide a more detailed analysis of the convergence rates for the SVM algorithm, and discuss the limitations of their approach.

### Questions

Please see the weakness section.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
