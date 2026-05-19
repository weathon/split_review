### Summary

This paper proposes a novel active learning method for drug discovery. The authors propose to use clustering to group molecules into clusters, select the cluster with the highest probability of containing active molecules, and select the most representative molecules from each cluster to be tested. The authors also propose to use isotonic regression to learn the mapping function from open labeled data to binding probabilities. The authors also propose to use active learning to select the most promising molecules for wet lab experiments. The authors evaluate the proposed method on two benchmark datasets and show that it outperforms the baseline method.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The proposed method is novel and interesting. The authors propose to use clustering, isotonic regression, and active learning to improve the efficiency of drug discovery. The authors also provide a detailed description of the proposed method and the experimental setup.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is not well-written and is difficult to follow. The authors should improve the writing and make it more clear.
2. The authors should provide more details about the baseline method. Specifically, the authors should provide the details of the clustering method, the isotonic regression method, and the active learning method used in the baseline method.
3. The authors should provide more details about the datasets used in the experiments. Specifically, the authors should provide the number of molecules, the number of active molecules, the number of target proteins, and the number of ligands per target protein.
4. The authors should provide more details about the evaluation metrics. Specifically, the authors should provide the definition of the metrics and explain why they are used.
5. The authors should provide more details about the experimental results. Specifically, the authors should provide the mean and standard deviation of the metrics, and the statistical significance of the results.

### Suggestions

The paper needs significant improvements in clarity and detail to be considered for publication. The introduction should be rewritten to clearly articulate the problem being addressed, the limitations of existing methods, and how the proposed approach offers a novel solution. The authors should explicitly state the research question and the specific gap in the literature that their work aims to fill. The motivation behind the proposed method, particularly the combination of clustering, isotonic regression, and active learning, needs to be more clearly explained. The authors should provide a more detailed explanation of how these components interact and why this particular combination is expected to be effective for drug discovery. Furthermore, the paper should include a more thorough discussion of the related work, highlighting the differences and advantages of the proposed method compared to existing approaches. This should include a detailed comparison of the proposed method with other active learning techniques used in drug discovery, and a discussion of the specific advantages of the proposed clustering and isotonic regression methods.

To address the lack of detail regarding the baseline method, the authors should provide a comprehensive description of each component. For the clustering method, the authors should specify the algorithm used (e.g., k-means, hierarchical clustering), the distance metric, and the number of clusters. For the isotonic regression method, the authors should describe the specific algorithm used and any parameters involved. For the active learning method, the authors should specify the acquisition function and any parameters used. The authors should also provide a clear explanation of how these components are integrated into the baseline method. Furthermore, the authors should provide a detailed description of the datasets used in the experiments. This should include the number of molecules, the number of active molecules, the number of target proteins, and the number of ligands per target protein. The authors should also provide a brief description of the chemical properties of the molecules and the target proteins. The authors should also provide a clear definition of the evaluation metrics used, including the specific formulas and the rationale for using them. The authors should also provide the mean and standard deviation of the metrics, and the statistical significance of the results. This will allow the reader to better understand the performance of the proposed method and to compare it with other methods.

Finally, the authors should provide a more detailed analysis of the experimental results. This should include a discussion of the performance of the proposed method under different conditions, such as different numbers of active molecules or different numbers of target proteins. The authors should also discuss the limitations of the proposed method and suggest directions for future research. The authors should also provide a more detailed analysis of the computational cost of the proposed method, including the time and memory requirements. This will allow the reader to better understand the practical implications of the proposed method. The authors should also consider including a case study to illustrate how the proposed method works in practice and to demonstrate its potential benefits for drug discovery.

### Questions

1. What is the difference between the proposed method and the baseline method?
2. What is the difference between the proposed method and other active learning methods used in drug discovery?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
