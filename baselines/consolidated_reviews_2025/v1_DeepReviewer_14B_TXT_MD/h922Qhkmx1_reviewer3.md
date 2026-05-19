### Summary

This paper presents a diffusion-based generative model that can perform both music synthesis and source separation. The authors introduce a novel inference method for the separation task based on Dirac likelihood functions. The model is trained on the Slakh2100 dataset and shows competitive results in both generation and separation tasks. The method is the first example of a single model that can handle both generation and separation tasks, representing a step towards general audio models.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to music generation and source separation by using a single diffusion-based generative model. This is a significant contribution to the field of music information retrieval.
2. The proposed method is evaluated on a standard dataset and shows competitive results compared to existing methods. The authors also provide qualitative results to support their claims.
3. The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed method and its applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be helpful to compare the computational cost of the proposed method with existing methods.
2. The paper does not discuss the limitations of the proposed method. It would be helpful to discuss the potential challenges and limitations of the proposed method, such as its performance on different types of music or its sensitivity to hyperparameter settings.
3. The paper does not provide a detailed analysis of the qualitative results. It would be helpful to provide a more in-depth analysis of the generated music and separated sources, including examples of both successful and unsuccessful cases.

### Suggestions

The paper should include a more thorough analysis of the computational demands of the proposed method. Specifically, the authors should provide a breakdown of the computational cost associated with each stage of the diffusion process, including the forward and reverse passes, as well as the overhead of the Dirac likelihood function. This analysis should be compared against the computational cost of existing methods for both music generation and source separation, using metrics such as FLOPs, wall-clock time, and memory usage. Furthermore, the authors should investigate the scalability of their method with respect to the length of the audio samples and the number of sources being separated. This would provide a clearer understanding of the practical limitations of the approach and its suitability for real-world applications. For example, it would be useful to know how the computational cost scales with the number of diffusion steps and the dimensionality of the latent space.

In addition to computational cost, the paper should also address the limitations of the proposed method in more detail. The authors should investigate the performance of the model on different types of music, such as classical, jazz, and electronic, to assess its generalizability. It would also be beneficial to analyze the model's sensitivity to hyperparameter settings, such as the learning rate, the number of diffusion steps, and the architecture of the neural network. The authors should provide a discussion of the potential failure modes of the model, such as the generation of artifacts or the incorrect separation of sources. Furthermore, the authors should explore the impact of the training data on the performance of the model, and whether the model can generalize to unseen musical styles or source combinations. This analysis should include a discussion of the potential biases in the training data and how they might affect the model's performance.

Finally, the paper should include a more detailed analysis of the qualitative results. The authors should provide a more in-depth analysis of the generated music and separated sources, including examples of both successful and unsuccessful cases. This analysis should include a discussion of the musical characteristics of the generated samples, such as the melody, harmony, and rhythm, as well as the quality of the separated sources. The authors should also provide a subjective evaluation of the generated music, such as a listening test, to assess its musicality and coherence. Furthermore, the authors should provide a visual analysis of the separated sources, such as spectrograms, to help understand the model's behavior. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed method and its potential for real-world applications.

### Questions

1. Can you provide a more detailed analysis of the computational cost of the proposed method compared to existing methods?
2. Can you discuss the limitations of the proposed method in more detail, such as its performance on different types of music or its sensitivity to hyperparameter settings?
3. Can you provide a more detailed analysis of the qualitative results, including examples of both successful and unsuccessful cases?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
