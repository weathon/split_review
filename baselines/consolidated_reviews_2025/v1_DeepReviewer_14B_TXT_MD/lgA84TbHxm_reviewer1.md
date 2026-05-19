### Summary

This paper proposes a temperature scaling method for contrastive learning. Specifically, the authors derive a temperature function with positive and negative slopes in the positive and negative halves of the cosine similarity vs. temperature plane, respectively, and then adopt a cosine function of the cosine similarity as the temperature function. Experimental results show that the proposed framework outperforms the state-of-the-art SSL frameworks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed temperature function is well motivated and the paper is well written.
2. The experimental results are strong.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed temperature function is well motivated and the paper is well written.
2. The experimental results are strong.

1. As shown in Figure 1, the distribution of cosine similarity of TP, FN, and TN pairs after pre-training is different from that at random initialization. Therefore, the assumption of a fixed distribution for cosine similarity may not be valid.
2. The authors claim that the cosine function does not violate the four criteria mentioned in Section 3.4. However, it is not clear how the cosine function satisfies these criteria. It would be better to provide a more detailed explanation or analysis of how the cosine function meets each of the four criteria.
3. The proposed temperature scaling function introduces additional hyperparameters (e.g., the minimum and maximum temperature values). It is not clear how sensitive the performance is to these hyperparameters and what the optimal values are.
4. The paper does not provide a theoretical analysis of the convergence properties of the proposed method. It would be beneficial to include a discussion or analysis of the convergence behavior of the temperature scaling function.
5. The paper lacks a comparison with other temperature scaling methods. It would be helpful to compare the proposed method with existing temperature scaling techniques to demonstrate its advantages.

### Suggestions

The paper introduces an interesting temperature scaling method for contrastive learning, but several aspects could be strengthened to enhance its impact and clarity. First, the assumption of a fixed distribution for cosine similarity, as highlighted by the differences between Figure 1(a) and 1(b), needs further justification. While the authors argue that the distribution is fixed during the derivation of the temperature function, the practical implications of this assumption should be addressed. Specifically, it would be beneficial to analyze how the changing distribution of cosine similarities during training affects the performance of the proposed method. For instance, a study on the sensitivity of the method to the initial distribution of cosine similarities could provide valuable insights. Furthermore, it would be useful to explore adaptive temperature scaling functions that can adjust to the evolving distribution of cosine similarities during training. This could potentially lead to more robust and effective contrastive learning models.

Second, the explanation of how the cosine function satisfies the four criteria in Section 3.4 needs to be more detailed. While the authors claim that the cosine function meets these criteria, a more rigorous analysis is required. For each criterion, the authors should provide a mathematical justification or a clear intuitive explanation of how the cosine function satisfies it. For example, for the first criterion, which states that the temperature should be high for false negatives, the authors should explain how the cosine function ensures this property. Similarly, for the other criteria, the authors should provide a detailed explanation of how the cosine function meets the requirements. This would significantly improve the clarity and understanding of the proposed method. Additionally, it would be beneficial to explore other functions that satisfy these criteria and compare their performance with the cosine function. This could provide a more comprehensive understanding of the design choices for the temperature scaling function.

Finally, the paper should include a more thorough analysis of the hyperparameters introduced by the proposed temperature scaling function. Specifically, the authors should investigate the sensitivity of the method to the minimum and maximum temperature values. This could involve conducting experiments with different values of these hyperparameters and analyzing their impact on the performance of the model. Furthermore, the authors should provide guidelines for selecting the optimal values of these hyperparameters. This would make the proposed method more practical and easier to use. Additionally, a comparison with other temperature scaling methods would be beneficial to demonstrate the advantages of the proposed method. This could involve comparing the performance of the proposed method with existing techniques on various datasets and tasks. This would provide a more comprehensive evaluation of the proposed method and its contribution to the field.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
