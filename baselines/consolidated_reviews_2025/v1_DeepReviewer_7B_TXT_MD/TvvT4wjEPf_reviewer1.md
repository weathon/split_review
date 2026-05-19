### Summary

This paper presents a method for evaluating RNNs over encrypted data using fully homomorphic encryption (FHE). The authors propose an overflow-aware activity regularization (OAR) technique to address the overflow issue that arises from the large domain sizes in FHE operations. The proposed approach is evaluated on the MNIST dataset, showing improved accuracy and latency compared to plaintext and other FHE-based evaluations.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper addresses the important problem of evaluating RNNs over encrypted data, which has practical implications for privacy-preserving machine learning applications.

- The use of overflow-aware activity regularization (OAR) is a novel approach to mitigating the overflow issue in FHE-based RNNs.

- The experimental results demonstrate the effectiveness of the proposed method, showing improved accuracy and latency compared to plaintext and other FHE-based evaluations.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on the MNIST dataset, which may not be representative of more complex real-world applications. The performance of the proposed method on more challenging datasets, such as CIFAR-10 or ImageNet, is not evaluated. This limits the generalizability of the findings.

- The paper does not provide a detailed analysis of the computational overhead of the proposed method, particularly in terms of memory usage and energy consumption. This information is crucial for assessing the practical feasibility of the approach.

- The paper lacks a thorough comparison with existing FHE-based RNN evaluation methods, such as those presented in the cited works [1, 2, 3]. A more comprehensive comparison would help to better contextualize the contributions of the proposed method.

- The paper does not discuss the potential impact of the proposed method on the security of FHE-based RNN evaluations. It is important to consider whether the proposed method introduces any new vulnerabilities or increases the risk of side-channel attacks.

### Suggestions

The authors should evaluate their method on more complex datasets, such as CIFAR-10 or ImageNet, to demonstrate its applicability to real-world scenarios. This would involve adapting the current architecture to handle higher-resolution images and more complex classification tasks. Furthermore, the evaluation should include a detailed analysis of the computational cost, including memory usage, energy consumption, and runtime, to provide a comprehensive understanding of the practical feasibility of the proposed method. This analysis should be compared against existing FHE-based RNN evaluation methods to highlight the advantages and disadvantages of the proposed approach. The authors should also consider the impact of different FHE parameters on the performance and efficiency of the proposed method, such as the plaintext modulus and the ciphertext modulus, and provide guidelines for selecting appropriate parameters for different applications.

To strengthen the paper's contribution, the authors should provide a more detailed comparison with existing FHE-based RNN evaluation methods, such as those presented in the cited works [1, 2, 3]. This comparison should not only focus on accuracy but also on other relevant metrics, such as latency, memory usage, and energy consumption. The authors should clearly articulate the novel aspects of their approach and how it improves upon existing methods. For example, they could discuss the specific advantages of their overflow-aware activity regularization (OAR) technique compared to other regularization methods used in FHE-based RNNs. A more thorough comparison would help to contextualize the contributions of the proposed method and highlight its unique value.

Finally, the authors should address the potential security implications of their proposed method. This includes analyzing whether the OAR technique introduces any new vulnerabilities or increases the risk of side-channel attacks. The authors should also discuss the limitations of their approach and identify potential areas for future research. For example, they could explore the possibility of using more advanced FHE techniques or developing more efficient algorithms for RNN evaluation. A thorough discussion of the security aspects would help to ensure the robustness and reliability of the proposed method.

### Questions

- How does the proposed method scale to more complex datasets and RNN architectures?

- What are the computational overheads of the proposed method, particularly in terms of memory usage and energy consumption?

- How does the proposed method compare to existing FHE-based RNN evaluation methods in terms of accuracy, latency, and security?

### Rating

3

### Confidence

4

**********
