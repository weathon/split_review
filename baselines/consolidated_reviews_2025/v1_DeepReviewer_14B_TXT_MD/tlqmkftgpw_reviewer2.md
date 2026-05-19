### Summary

This paper proposes a new method called DBRNet for estimating individual-level continuous treatment effects. The authors claim that their method is the first to precisely adjust for selection bias in continuous treatment settings, and they provide theoretical proofs to support their claim. They also conduct extensive experiments on synthetic and semi-synthetic datasets to demonstrate the effectiveness of their method. Overall, the paper makes a significant contribution to the field of causal inference and provides a valuable tool for researchers and practitioners working with continuous treatment data.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a new method called DBRNet for estimating individual-level continuous treatment effects.
2. The authors claim that their method is the first to precisely adjust for selection bias in continuous treatment settings, and they provide theoretical proofs to support their claim.
3. They also conduct extensive experiments on synthetic and semi-synthetic datasets to demonstrate the effectiveness of their method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide any information about the availability of the code or data used in the experiments. This makes it difficult to reproduce the results and evaluate the method's performance.
2. The paper does not discuss the limitations of the method or potential areas for future research. It is important to acknowledge the limitations of any proposed method and to suggest directions for future work.
3. The paper does not compare the proposed method to other state-of-the-art methods for estimating individual-level continuous treatment effects. It is important to compare the proposed method to existing methods to demonstrate its advantages and disadvantages.

### Suggestions

The lack of code and data availability is a significant impediment to the reproducibility of the results. To address this, the authors should provide a link to an anonymous repository containing the code, along with clear instructions on how to run the experiments. Furthermore, the data used in the experiments should also be made available, or the authors should provide a detailed description of how the data was generated, including the specific parameters used. This would allow other researchers to verify the results and build upon the proposed method. Without this, the practical impact of the work is limited, and the community cannot fully assess the method's strengths and weaknesses.

Regarding the limitations, the authors should discuss the assumptions underlying their method and how violations of these assumptions might affect the results. For example, what happens if the treatment assignment is not strongly ignorable? What are the implications of the specific functional form chosen for the dose-response relationship? A discussion of these points would provide a more complete picture of the method's applicability and potential pitfalls. Furthermore, the authors should suggest specific directions for future research, such as extending the method to handle more complex treatment regimes or incorporating uncertainty quantification. This would help guide future work in this area and highlight the potential for further advancements.

Finally, a more thorough comparison to existing methods is needed. The authors should not only compare their method to existing methods on the same datasets but also discuss the theoretical differences between the methods. For example, how does the proposed method compare to tree-based methods or other machine learning approaches in terms of bias, variance, and computational complexity? A detailed comparison would help the reader understand the advantages and disadvantages of the proposed method and its suitability for different applications. This comparison should also include a discussion of the computational cost of the proposed method compared to other methods, which is an important factor in practical applications.

### Questions

1. Can you provide a link to the code and data used in the experiments?
2. What are the limitations of the proposed method, and what are the potential areas for future research?
3. How does the proposed method compare to other state-of-the-art methods for estimating individual-level continuous treatment effects?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
