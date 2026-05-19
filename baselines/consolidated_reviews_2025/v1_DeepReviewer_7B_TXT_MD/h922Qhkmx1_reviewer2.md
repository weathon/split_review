### Summary

This paper proposes a multi-source diffusion model for simultaneous music generation and source separation. The model is trained to learn the joint distribution of the sources and the mixture. The paper also proposes a novel Dirac likelihood function to improve the performance of the model. The paper demonstrates the effectiveness of the proposed method on the Slakh2100 dataset.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper proposes a novel multi-source diffusion model for simultaneous music generation and source separation. The model is able to perform both tasks simultaneously, which is a significant contribution to the field.
2. The paper proposes a novel Dirac likelihood function to improve the performance of the model. The proposed method is shown to outperform existing methods in terms of SI-SDR.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear explanation of the novelty of the proposed method. The authors should clarify the differences between their method and existing methods.
2. The paper does not provide a detailed analysis of the performance of the proposed method. The authors should provide more quantitative results to demonstrate the effectiveness of the proposed method.
3. The paper does not provide a discussion of the limitations of the proposed method. The authors should discuss the potential drawbacks of the proposed method and suggest future research directions.

### Suggestions

The paper needs to more clearly articulate the novelty of its approach compared to existing multi-source diffusion models. While the simultaneous generation and separation of music sources is a valuable goal, the paper should explicitly highlight what makes its method unique. For example, the paper should discuss how the proposed Dirac likelihood function differs from other likelihood functions used in diffusion models, and why this specific choice is advantageous for music source separation. A more detailed comparison with existing methods, including a discussion of their limitations, would also be beneficial. This should include a discussion of how the proposed method addresses the challenges of modeling the complex dependencies between musical sources, and how it improves upon existing approaches in this regard. Furthermore, the paper should clarify the specific architectural choices made in the model and how these choices contribute to the overall performance.

To strengthen the evaluation, the paper should include a more comprehensive set of quantitative results. This should include metrics beyond SI-SDR, such as PESQ and STOI, to provide a more complete picture of the model's performance. The paper should also include a more detailed analysis of the model's performance across different types of music and different source separation scenarios. For example, the paper should investigate how the model performs on music with varying levels of complexity, or with different types of instruments. The paper should also provide a more detailed analysis of the model's performance in terms of both generation quality and separation accuracy. This should include a discussion of the trade-offs between these two aspects, and how the proposed method balances these competing objectives. Additionally, the paper should include a more detailed analysis of the computational cost of the proposed method, and compare it to existing methods.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method. This should include a discussion of the potential drawbacks of the proposed method, such as its sensitivity to hyperparameter settings, or its performance on out-of-distribution data. The paper should also discuss potential avenues for future research, such as exploring alternative likelihood functions, or incorporating additional prior knowledge into the model. This should include a discussion of how the proposed method could be extended to handle more complex musical scenarios, such as polyphonic music or music with overlapping sources. The paper should also discuss the potential ethical implications of the proposed method, such as the generation of music that is indistinguishable from human-composed music.

### Questions

1. How does the proposed method compare to existing methods in terms of computational cost and memory usage?
2. How does the proposed method perform on music with varying levels of complexity?
3. How does the proposed method perform on music with different types of instruments?

### Rating

5

### Confidence

3

**********
