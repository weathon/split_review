### Summary

The authors propose a diffusion model that can perform both music generation and source separation. The model is trained on Slakh2100, and the authors show that the model can perform both generation and separation tasks. The authors also introduce a new inference method for separation based on Dirac delta functions.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The idea of modeling the joint distribution of sources is interesting.
- The authors propose a new inference method for separation based on Dirac delta functions, which seems to improve performance.
- The authors provide a detailed analysis of the results, including both quantitative and qualitative evaluations.

### Weaknesses

#### Some Related Works


#### comment

 - The model is only evaluated on Slakh2100, which is a relatively small dataset. It would be interesting to see how the model performs on other datasets, such as MUSDB18 or MusicCaps.
- The authors do not compare their model to other state-of-the-art models for music generation and source separation. It would be useful to see how the proposed model compares to other models in terms of both performance and computational efficiency.
- The authors do not provide any analysis of the limitations of their model. It would be helpful to understand the types of music or source combinations that the model struggles with.
- The evaluation of the generation task lacks a comparison to other generative models, making it difficult to assess the novelty and performance of the proposed approach in this domain. The authors should consider comparing their model to other state-of-the-art generative models for music, such as those based on transformers or GANs.
- The paper does not explore the impact of different architectural choices on the performance of the model. For example, it would be interesting to see how the performance changes with different numbers of layers or different types of activation functions.

### Suggestions

The authors should consider expanding their evaluation to include more diverse datasets, such as MUSDB18 and MusicCaps, to better assess the generalizability of their model. This would provide a more comprehensive understanding of the model's strengths and weaknesses across different musical styles and recording conditions. Furthermore, a comparison against other state-of-the-art models for both music generation and source separation is crucial to establish the novelty and performance of the proposed approach. This comparison should include both quantitative metrics and qualitative analysis, such as listening tests, to provide a more complete picture of the model's capabilities. The authors should also investigate the computational efficiency of their model compared to other approaches, as this is an important factor for practical applications.

To further improve the paper, the authors should conduct a more detailed analysis of the limitations of their model. This should include identifying specific types of music or source combinations that the model struggles with, as well as analyzing the reasons for these limitations. For example, does the model perform worse on music with complex harmonies or dense textures? Does it struggle with separating sources that have similar frequency content? Understanding these limitations will help guide future research and development. Additionally, the authors should explore the impact of different architectural choices on the performance of the model. This could include varying the number of layers, the size of the hidden layers, and the type of activation functions used. This analysis would provide valuable insights into the design choices that are most important for achieving good performance.

Finally, the authors should consider including a more detailed analysis of the generated music. This could include metrics such as the diversity of the generated samples, the coherence of the generated music, and the presence of artifacts or distortions. A qualitative analysis, such as listening tests, would also be beneficial to assess the musicality of the generated samples. This would help to better understand the strengths and weaknesses of the proposed approach for music generation. The authors should also consider exploring the use of different evaluation metrics that are more specific to music generation, such as metrics that measure the musical structure or the emotional content of the generated music.

### Questions

- How does the model perform on other datasets, such as MUSDB18 or MusicCaps?
- How does the model compare to other state-of-the-art models for music generation and source separation?
- What are the limitations of the model? What types of music or source combinations does it struggle with?
- How does the performance of the model change with different architectural choices, such as the number of layers or the size of the hidden layers?
- How does the model perform on the task of generating accompaniments given a lead instrument?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
