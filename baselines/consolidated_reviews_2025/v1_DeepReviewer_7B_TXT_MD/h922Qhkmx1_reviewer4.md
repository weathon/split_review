### Summary

The paper proposes a method for music generation and source separation by training a single multi-source diffusion model. The model is trained on the Slakh2100 dataset, which contains a large number of music recordings. The model is able to perform both music generation and source separation, and the authors claim that it is the first model to do so. The authors also introduce a novel Dirac likelihood function to improve the performance of the model. The paper presents experimental results on the Slakh2100 dataset, showing that the model performs well in both generation and separation tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper presents a novel approach to music generation and source separation by training a single multi-source diffusion model. This is a significant contribution to the field, as it simplifies the process of generating and separating music sources. The model is able to perform both tasks simultaneously, which is a significant advancement over existing methods that require separate models for each task. The authors also introduce a novel Dirac likelihood function to improve the performance of the model, which is a valuable contribution to the field of diffusion models. The paper is well-written and easy to understand, and the authors provide clear explanations of the model and its components. The experimental results on the Slakh2100 dataset demonstrate that the model performs well in both generation and separation tasks, which is a strong indication of its effectiveness. The authors also provide a detailed description of the model architecture and training process, which is helpful for other researchers who want to build upon this work.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a clear explanation of how the model handles the temporal dependencies in music. Music is a complex, time-varying signal, and it is not clear how the proposed diffusion model captures these dependencies. Specifically, the paper lacks details on how the diffusion process is adapted to handle the sequential nature of audio data, such as the use of temporal convolutions or recurrent layers within the diffusion model. The absence of such details makes it difficult to assess the model's ability to generate coherent musical structures over longer timeframes. 

The paper does not compare the proposed model with other state-of-the-art methods for music generation and source separation. While the paper mentions that the model achieves competitive results with state-of-the-art methods, it does not provide a detailed comparison with other approaches. This makes it difficult to assess the true performance of the model and its advantages over existing methods. A more thorough comparison, including quantitative metrics and qualitative analysis, is needed to establish the model's superiority.

The paper does not discuss the limitations of the proposed model. It is important to acknowledge the limitations of any proposed method, as this helps to set realistic expectations for its performance. For example, the paper does not discuss the model's performance on different types of music or its ability to handle complex musical structures. A discussion of these limitations would help to identify areas for future research.

### Suggestions

The authors should provide a more detailed explanation of how the diffusion model handles the temporal dependencies inherent in music. This should include a discussion of the specific architectural choices made to process sequential audio data, such as the use of temporal convolutional layers or recurrent neural networks within the diffusion model. Furthermore, the authors should elaborate on how the Dirac likelihood function is adapted to capture the temporal structure of music. For example, it would be beneficial to explain how the Dirac function is used to model the temporal dependencies between different musical events and how this contributes to the overall performance of the model. This would help to clarify the technical details of the proposed approach and allow for a more thorough evaluation of its capabilities.

To strengthen the evaluation of the proposed model, the authors should include a more comprehensive comparison with existing state-of-the-art methods for music generation and source separation. This comparison should not only include quantitative metrics, such as SI-SDR and PESQ, but also qualitative analysis of the generated and separated music. The authors should also discuss the computational cost of the proposed model compared to other methods. This would provide a more complete picture of the model's performance and its practical applicability. Additionally, the authors should consider evaluating the model on a wider range of datasets to assess its generalization capabilities.

Finally, the paper should include a more thorough discussion of the limitations of the proposed model. This should include an analysis of the model's performance on different types of music, such as pop, classical, and jazz, and its ability to handle complex musical structures. The authors should also discuss the potential challenges of applying the model to real-world scenarios, such as noisy environments or music with significant variations in tempo and dynamics. This would help to identify areas for future research and to set realistic expectations for the model's performance. Furthermore, the authors should discuss the potential ethical implications of using generative models for music, such as the potential for misuse or the creation of copyrighted material.

### Questions

How does the proposed model handle the temporal dependencies in music? Music is a complex, time-varying signal, and it is not clear how the proposed diffusion model captures these dependencies.

How does the proposed model compare with other state-of-the-art methods for music generation and source separation? A more detailed comparison with other approaches is needed to establish the model's superiority.

What are the limitations of the proposed model? It is important to acknowledge the limitations of any proposed method, as this helps to set realistic expectations for its performance.

### Rating

6

### Confidence

3

**********
