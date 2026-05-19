### Summary

This paper proposed noise regularization method for Deep Canonical Correlation Analysis (DCCA) to address the model collapse issue. The authors show that the weight matrices in DNNs tend to be low-rank, which affects the quality of representations. The proposed NR-DCCA enforces the correlation with random data to be invariant before and after the transformation, which is defined as the Correlation Invariant Property (CIP). Theoretical analysis shows that the Correlation Invariant Property is the key to preventing model collapse. Experiments on both synthetic and real-world datasets demonstrate the consistent outperformance and stability of the developed NR-DCCA method.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1.	The paper is well written and easy to follow.
2.	The paper provides rigorous theoretical proofs to demonstrate that CIP is equivalent to the full-rank weight matrix.
3.	The proposed NR approach is simple and can be applied to other DCCA-based methods.

### Weaknesses

#### Some Related Works


#### comment

1.	The novelty of the paper is limited. The model collapse issue observed in DCCA is similar to the mode collapse issue in Generative Adversarial Networks (GANs), and the proposed noise regularization approach resembles the methods used in GANs to mitigate mode collapse. The paper fails to articulate the specific differences between the observed collapse in DCCA and the well-studied mode collapse in GANs. It is unclear if the proposed noise regularization addresses the root cause of the collapse in DCCA or if it is simply a workaround that happens to improve performance. The authors should provide a more in-depth analysis of the underlying mechanisms causing the collapse in DCCA and how their method specifically addresses those mechanisms, rather than just showing empirical results.
2.	The significance of the paper is unclear. The authors claim that the model collapse issue hinders the wide adoption of DCCA-based methods, but there are not enough evidence to support this claim. The paper does not provide a comprehensive review of the current usage of DCCA and its variants. It is not clear how widespread the use of DCCA is in practical applications, and the authors need to provide more evidence to support the claim that the model collapse issue is a significant barrier to adoption. The authors should also discuss the limitations of existing methods and how their proposed approach overcomes these limitations in a significant way.
3.	The paper only focuses on CCA as a theoretically sound approach and does not discuss why CCA is preferred over other methods in Multi-view Representation Learning (MVRL). The paper lacks a comprehensive comparison of CCA with other MVRL techniques, such as multi-view deep learning methods. The authors should justify their choice of focusing solely on CCA and discuss the advantages and disadvantages of CCA compared to other methods. The paper should also address the limitations of CCA and how the proposed method overcomes these limitations.

### Suggestions

The authors should provide a more detailed comparison between the model collapse in DCCA and the mode collapse in GANs. This should include a theoretical analysis of the underlying causes of each type of collapse, highlighting the key differences. For example, the authors could investigate whether the low-rank weight matrix issue in DCCA is analogous to the discriminator overfitting in GANs, or if it stems from a different mechanism. A more thorough analysis of the gradient dynamics during training could also be beneficial to understand how the proposed noise regularization affects the optimization landscape and prevents the collapse. Furthermore, the authors should explore the impact of different noise regularization techniques, such as adding noise to the input data or to the hidden layers, and compare their effectiveness in preventing model collapse. This would provide a more comprehensive understanding of the proposed method and its relationship to other regularization techniques.

To better establish the significance of their work, the authors should provide a more thorough review of the current applications of DCCA and its variants. This should include specific examples of how DCCA is used in various domains, and the limitations that the model collapse issue imposes on these applications. The authors should also discuss the alternative methods that are currently used to address these limitations, and how their proposed approach offers an improvement over these existing solutions. For example, the authors could compare their method to early stopping, weight decay, or other regularization techniques, and demonstrate the advantages of their approach in terms of both performance and stability. Furthermore, the authors should discuss the computational cost of their method and how it compares to other methods. This would help to establish the practical relevance of their work and its potential impact on the field.

The authors should also provide a more detailed justification for their focus on CCA and discuss its limitations compared to other MVRL techniques. This should include a comparison of CCA with methods such as multi-view deep learning, and a discussion of the advantages and disadvantages of each approach. The authors should also address the limitations of CCA, such as its sensitivity to non-linear relationships between views, and how their proposed method overcomes these limitations. Furthermore, the authors should discuss the potential of extending their method to other MVRL techniques, and how this could broaden the impact of their work. This would help to clarify the contribution of their work and its relevance to the broader field of multi-view representation learning.

### Questions

1.	Why is the model collapse issue in DCCA similar to or different from the mode collapse issue in GANs? How is the proposed noise regularization approach different from the methods used in GANs to mitigate mode collapse?
2.	Is DCCA widely used in practice? What are the current challenges in adopting DCCA-based methods? How significant is the model collapse issue in hindering the adoption of DCCA-based methods?
3.	Why is CCA preferred over other methods in Multi-view Representation Learning (MVRL)? What are the limitations of CCA compared to other MVRL techniques? How does the proposed method address the limitations of CCA?

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
