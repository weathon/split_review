### Summary

This paper proposes a generalized CTM framework that can be trained to translate between arbitrary distributions. The authors provide a theoretical analysis of the proposed framework and demonstrate its effectiveness in various image manipulation tasks.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

1. The proposed framework can be trained to translate between arbitrary distributions, which is a significant advancement over traditional CTMs that are limited to Gaussian to data translation.
2. The authors provide a theoretical analysis of the proposed framework and demonstrate its effectiveness in various image manipulation tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is not well written and is very hard to follow. For example, the authors use a lot of mathematical notations without proper introduction or explanation. The lack of clear definitions for symbols and terms makes it difficult to understand the proposed method. Specifically, the introduction of the generalized ODE and its relation to the original CTM is not well motivated. The paper would benefit from a more intuitive explanation of the core concepts before diving into the mathematical details.
2. The authors claim that the proposed framework can be trained to translate between arbitrary distributions, but the experiments are limited to image manipulation tasks. It is not clear how the framework would perform on other types of data, such as audio or text. The paper lacks a discussion on the limitations of the proposed approach and its potential challenges in different domains. The authors should provide a more comprehensive evaluation of the framework's generalizability.
3. The authors do not provide a comparison with other related works, such as iCTM. The absence of a direct comparison with existing methods makes it difficult to assess the novelty and effectiveness of the proposed framework. A thorough comparison with state-of-the-art techniques is necessary to establish the contribution of this work. The paper should include a quantitative comparison with iCTM and other relevant methods to demonstrate the advantages of the proposed approach.

### Suggestions

The paper needs a significant revision to improve its clarity and accessibility. The authors should start by providing a more intuitive explanation of the generalized ODE and its connection to the original CTM. This could involve a step-by-step breakdown of the mathematical derivations, with clear definitions of all symbols and terms. The authors should also consider including illustrative examples to help readers understand the proposed method. Furthermore, the paper should include a more detailed discussion of the limitations of the proposed approach and its potential challenges in different domains. This would help readers understand the scope of the work and its potential for future research. The authors should also consider providing a more comprehensive evaluation of the framework's generalizability by including experiments on other types of data, such as audio or text. This would help to demonstrate the versatility of the proposed method and its potential for broader applications.

To address the lack of comparison with related works, the authors should include a thorough quantitative comparison with iCTM and other relevant methods. This comparison should include a variety of metrics and should be performed on a common set of datasets. The authors should also provide a detailed discussion of the advantages and disadvantages of their proposed method compared to existing techniques. This would help to establish the contribution of this work and its potential impact on the field. The authors should also consider including a qualitative comparison with other methods, such as visual comparisons of generated samples. This would help to provide a more comprehensive understanding of the performance of the proposed method.

Finally, the authors should consider providing a more detailed explanation of the training procedure for the proposed framework. This should include a discussion of the loss function, the optimization algorithm, and the hyperparameter settings. The authors should also consider providing a more detailed analysis of the convergence properties of the training procedure. This would help to ensure that the proposed method is robust and reliable. The authors should also consider providing a more detailed explanation of the experimental setup, including the datasets used, the evaluation metrics, and the implementation details. This would help to ensure that the results are reproducible and that the claims made in the paper are well-supported.

### Questions

1. How does the proposed framework handle the case where the source and target distributions have different dimensionalities?
2. What are the computational costs associated with training and inference using the proposed framework?
3. How does the proposed framework compare to other related works, such as iCTM, in terms of performance and computational efficiency?

### Rating

5

### Confidence

3

**********
