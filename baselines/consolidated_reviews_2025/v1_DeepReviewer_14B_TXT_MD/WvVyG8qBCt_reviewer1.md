### Summary

This paper proposes a method for sequence prediction with differential privacy guarantees. The proposed method incorporates two techniques, Phantom Clipping and Re-Attention Mechanism. Phantom Clipping is a gradient clipping method designed to compute the clipped gradient without the need for per-sample gradient information, thus enhancing the efficiency of the learning process. The Re-Attention Mechanism is proposed to mitigate the unintended attention distraction within the attention mechanism. Experiments on real-world datasets demonstrate the efficiency and effectiveness of the proposed method.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper tackles the important problem of privately learning Transformer models, which have become popular in various applications.
2. The proposed Phantom Clipping and Re-Attention Mechanism are designed to address the challenges of heavy computation overhead and attention distraction, respectively.
3. The paper provides empirical results on real-world datasets to demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide any theoretical guarantees for the proposed method. It would be beneficial to include a theoretical analysis that justifies the privacy and utility guarantees of the proposed method.
2. The paper does not compare the proposed method with existing baselines. It would be helpful to include a comparison with relevant baselines to demonstrate the advantages of the proposed method.
3. The paper does not provide sufficient details about the experimental setup, such as the choice of hyperparameters and the evaluation metrics. More comprehensive experimental details are needed to ensure the reproducibility of the results.

### Suggestions

The lack of theoretical guarantees is a significant weakness. While the paper introduces Phantom Clipping and Re-Attention Mechanism, it does not provide any formal analysis of how these techniques affect the differential privacy guarantees. A rigorous theoretical analysis should include a proof that the proposed method satisfies differential privacy, possibly by bounding the privacy loss using techniques like R\'enyi differential privacy. Furthermore, the analysis should also address the utility of the proposed method, providing bounds on the error introduced by the privacy mechanisms. This would involve analyzing how the Phantom Clipping and Re-Attention Mechanism affect the convergence and generalization properties of the model. Without such theoretical underpinnings, it is difficult to assess the reliability and robustness of the proposed method.

The absence of a comparison with existing baselines makes it difficult to evaluate the contribution of this work. The paper should compare the proposed method with other differentially private methods for sequence prediction, especially those that are based on Transformer models. This comparison should include both the privacy-utility trade-off and the computational efficiency. For example, the paper could compare the proposed method with differentially private variants of BERT or other Transformer-based models. The comparison should be performed on the same datasets and using the same evaluation metrics. This would allow the reader to understand the advantages and disadvantages of the proposed method compared to existing approaches. Furthermore, the paper should also compare the proposed Phantom Clipping with other gradient clipping techniques used in differentially private training, such as per-sample clipping, to demonstrate its effectiveness.

The experimental section lacks crucial details that are necessary for reproducibility. The paper should provide a detailed description of the datasets used, including the size of the training, validation, and test sets, as well as the preprocessing steps applied to the data. The paper should also provide a complete list of the hyperparameters used for training the models, including the learning rate, batch size, and the number of training epochs. The paper should also specify the evaluation metrics used for each task. Furthermore, the paper should provide details about the implementation, such as the deep learning framework used and the hardware used for training. The paper should also include a discussion of the sensitivity of the results to the choice of hyperparameters. Without these details, it is difficult to reproduce the results and to assess the validity of the claims made in the paper.

### Questions

1. What is the privacy guarantee of the proposed method?
2. What is the baseline used in the experiments?
3. How does the performance of the proposed method compare with the baseline?

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
