### Summary

This paper proposes a new framework for human motion generation and control. The framework consists of three components: DoubleTake, ComMDM, and DiffusionBlending. DoubleTake is a method for generating long motion sequences by iteratively generating short sequences and merging them. ComMDM is a method for generating two-person motions by training a slim communication block with few data. DiffusionBlending is a method for fine-grained control by blending fine-tuned models. The proposed methods are evaluated on HumanML3D and BABEL datasets and show promising results.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed methods are novel and effective. DoubleTake is a simple yet effective method for generating long motion sequences. ComMDM is a novel method for generating two-person motions with few data. DiffusionBlending is a novel method for fine-grained control.
2. The proposed methods are evaluated on two datasets, HumanML3D and BABEL, and show promising results. The authors also provide qualitative results to demonstrate the effectiveness of the proposed methods.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The authors use a fixed MDM trained on HumanML3D for all tasks. It would be interesting to see how the proposed methods perform with other MDMs.
2. The authors compare their method with TEACH for long sequence generation. However, TEACH is trained on BABEL, while the authors train MDM on BABEL for a fair comparison. It is unclear if the performance gains are due to the proposed method or the dataset used for training.
3. For two-person motion generation, the authors only use 3DPW for training and evaluation. It would be better to evaluate the proposed method on other datasets to demonstrate its generalization ability. The lack of evaluation on diverse datasets makes it difficult to assess the robustness of the method.
4. For fine-grained control, the authors only compare with the original MDM. It would be better to compare with other methods that enable fine-grained control. The comparison is limited, and it is not clear how the proposed method compares to state-of-the-art techniques in fine-grained motion control.

### Suggestions

The paper presents a novel framework for human motion generation and control, but several aspects could be improved to strengthen the claims and demonstrate broader applicability. First, while using a fixed MDM simplifies the experimental setup, it also limits the understanding of the proposed methods' generalizability. The authors should explore how their methods perform with different motion diffusion models, such as those trained on different datasets or using different architectures. This would provide a more comprehensive evaluation of the proposed techniques and their robustness to variations in the underlying motion prior. For example, evaluating with a model trained on a dataset with different motion characteristics (e.g., more exaggerated or stylized motion) would be beneficial. Furthermore, it would be valuable to see how the proposed methods perform when the MDM is trained on a dataset with a different motion capture system, as this could reveal potential biases or limitations of the approach.

Second, the comparison with TEACH for long sequence generation needs further clarification. While training MDM on BABEL for a fair comparison is a good step, the authors should also consider the impact of the training data on the final performance. It is crucial to isolate the contribution of the proposed method from the dataset used for training. One way to address this would be to train both MDM and TEACH on the same dataset and then compare their performance. Additionally, the authors should provide a more detailed analysis of the failure cases of both methods, which could provide insights into the limitations of each approach. A more thorough analysis of the transition quality between generated motion segments would also be valuable, perhaps using metrics that capture the smoothness and continuity of the motion. It would also be beneficial to explore the sensitivity of the proposed method to the length of the input sequences, as this could reveal potential limitations in generating very long motion sequences.

Finally, the evaluation of the two-person motion generation and fine-grained control methods should be expanded. For two-person motion, the authors should evaluate on more datasets, including those with different types of interactions and motion characteristics. This would provide a better understanding of the method's generalization ability. For fine-grained control, the authors should compare with other state-of-the-art methods that enable similar control capabilities. This would provide a more comprehensive evaluation of the proposed method's performance and its advantages over existing techniques. Furthermore, the authors should provide a more detailed analysis of the limitations of their fine-grained control method, such as the types of motions that are difficult to control and the trade-offs between control and motion quality. It would also be beneficial to explore the sensitivity of the proposed method to the complexity of the control signals, as this could reveal potential limitations in generating very complex motions.

### Questions

1. How does the proposed method perform with other MDMs?
2. How does the proposed method compare with other methods that enable fine-grained control?
3. How does the proposed method perform on other datasets for two-person motion generation?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
