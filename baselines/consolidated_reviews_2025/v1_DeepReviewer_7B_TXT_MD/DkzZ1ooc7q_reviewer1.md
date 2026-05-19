### Summary

This paper addresses the task of sound separation with multi-modal queries (e.g., text, image, audio, etc.). The authors propose OmniSep, a model that separates sound into target and interference components using a unified framework. The model is trained using imagebind embeddings for audio, image, and text. The authors also introduce a negative query approach to remove unwanted sounds and a query augmentation method for open vocabulary sound separation using unrestricted natural language descriptions. The experiments show state-of-the-art performance in text, image, and audio-queried sound separation tasks.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The experiments are comprehensive and demonstrate strong performance across different modalities.
- The introduction of negative queries and query augmentation enhances the model's flexibility and open-vocabulary capabilities.

### Weaknesses

#### Some Related Works


#### comment

 - The authors should compare their approach with the latest methods in the field, such as those presented in "Open-World Sound Separation with Diffusion Models" (ICLR 2024) and "Neural Operator for Universal Sound Separation in the Wild" (arXiv 2024).
- The authors should provide more details on the training and inference settings, as well as the computational resources required. This information is crucial for reproducibility and understanding the practical applicability of the proposed method.
- The authors should discuss the limitations of their approach, such as the potential for interference information to be encoded in the imagebind embeddings, and how this might affect the performance of the model.

### Suggestions

The paper would benefit from a more thorough comparison with recent state-of-the-art methods in sound separation. Specifically, the authors should benchmark their approach against methods that utilize diffusion models for open-world sound separation, as these models have shown significant advancements in the field. A detailed comparison should not only focus on quantitative metrics but also discuss the qualitative differences in the separated sound components, highlighting the strengths and weaknesses of each approach. Furthermore, the authors should clarify how their method handles complex scenarios with multiple overlapping sound sources, and how it compares to diffusion-based methods in terms of computational cost and memory requirements. This would provide a more comprehensive understanding of the proposed method's performance relative to the current state-of-the-art.

To enhance the reproducibility and practical applicability of the proposed method, the authors should provide a detailed description of the training and inference settings. This should include specific information on the hardware used (e.g., GPU model, CPU type), the software environment (e.g., operating system, deep learning framework), the batch size, learning rate, optimization algorithm, and the number of training epochs. Additionally, the authors should specify the exact preprocessing steps applied to the audio data, such as normalization, resampling, and any other transformations. The authors should also provide a detailed explanation of how the imagebind embeddings are used in the model, including the specific layers and parameters that are used. This level of detail is essential for other researchers to replicate the results and build upon this work.

Finally, the authors should address the potential limitations of using imagebind embeddings, particularly concerning the encoding of interference information. While the authors mention that imagebind embeddings are pre-trained on diverse datasets, they should provide a more in-depth analysis of how this pre-training might influence the model's ability to separate target sounds from interference. For example, they should discuss whether the imagebind embeddings are biased towards certain types of sounds or if they can be easily confused with interference. The authors should also explore alternative embedding methods or training strategies that could mitigate these limitations. A more thorough discussion of these limitations would provide a more balanced and realistic assessment of the proposed method's capabilities.

### Questions

- How does the proposed approach compare to the latest methods in the field, such as those presented in "Open-World Sound Separation with Diffusion Models" (ICLR 2024) and "Neural Operator for Universal Sound Separation in the Wild" (arXiv 2024)?
- What are the computational resources required for training and inference, and how do they compare to other state-of-the-art methods?
- How does the model handle complex scenarios with multiple overlapping sound sources, and how does it compare to diffusion-based methods in terms of computational cost and memory requirements?

### Rating

5

### Confidence

4

**********
