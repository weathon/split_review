### Summary

This paper presents a method for node classification with very few labeled nodes that are randomly selected and not necessarily provided for each class. The proposed method, Estimating Label Information (ELI), leverages unsupervised learning to infer label information and use it to guide the labeled node selection process and improve existing semi-supervised learning (SSL) baselines. The authors show that ELI can improve the performance of SSL baselines by 10-20% in this challenging setting.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The authors propose a new and challenging task, Sparse Label Node Classification (SLNC).
2. The authors propose a new method, Estimating Label Information (ELI), for the SLNC task that leverages clustering to improve label propagation.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed ELI method seems to be a combination of existing methods.
2. The improvement of the proposed method is marginal.
3. The paper is poorly written.

### Suggestions

The paper needs to clearly articulate the novelty of the ELI method beyond simply combining existing techniques. While the authors claim that ELI is not just a combination of existing methods, the paper does not provide a detailed analysis of how the individual components are modified or adapted to fit the sparse label setting. The paper should include a section that explicitly discusses the limitations of existing methods when applied to the SLNC task and how ELI addresses these limitations. For example, the paper could discuss how the clustering approach is specifically tailored to handle the sparse label scenario, and how the key node selection process differs from standard clustering techniques. A more detailed explanation of the optimization process for label distribution incorporation is also needed, highlighting the differences from standard label propagation methods. Without this detailed analysis, the reader is left with the impression that ELI is simply a combination of existing methods with minimal adaptation.

Furthermore, the paper should provide a more thorough evaluation of the proposed method. While the authors claim a 10-20% improvement over baselines, the paper does not provide sufficient detail on the experimental setup. For example, the paper should include a more detailed description of the datasets used, the specific parameters used for each method, and the evaluation metrics used. The paper should also include a more thorough comparison with other state-of-the-art methods for semi-supervised learning, not just the baselines used in the paper. The paper should also include an analysis of the sensitivity of the proposed method to different parameters and datasets. The current evaluation is not sufficient to demonstrate the effectiveness of the proposed method. The authors should also consider including a comparison with other methods that use clustering for semi-supervised learning, to better understand the contribution of the proposed method.

Finally, the paper needs significant improvement in terms of writing quality. The paper is currently difficult to follow, with many grammatical errors and unclear sentences. The paper should be revised to improve the clarity and readability of the text. The authors should also consider using more visual aids, such as diagrams and flowcharts, to help the reader understand the proposed method. The paper should also include a more detailed explanation of the mathematical notation used in the paper. The current writing style makes it difficult to understand the proposed method and its contribution. The authors should also consider using a professional editor to improve the writing quality of the paper.

### Questions

1. How does ELI differ from existing methods?
2. Can you show ELI's performance compared to other methods using more widely accepted metrics?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
