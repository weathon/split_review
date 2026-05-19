### Summary

This paper presents a multi-modal large language model (MLLM) that is able to understand images in 3D space. It introduces a large-scale pretraining dataset for 2D and 3D understanding, called LV3D, which combines multiple existing 2D and 3D recognition datasets under a common task formulation of multi-turn question-answering. The paper also introduces a new MLLM named Cube-LLM, which is pre-trained on LV3D and shows strong 3D perception capability without any 3D specific architectural design or training objective. Cube-LLM exhibits intriguing properties similar to LLMs, such as chain-of-thought prompting, instruction following, and visual prompting. The paper evaluates Cube-LLM on various benchmarks, such as refCOCO for 2D grounding and VQAv2, GQA, etc. for complex reasoning, and shows that it significantly outperforms existing baselines in 3D grounded reasoning and complex reasoning about driving scenarios.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper presents a novel approach to 3D visual understanding by combining multiple existing 2D and 3D recognition datasets under a common task formulation of multi-turn question-answering. 
- The paper introduces a new MLLM named Cube-LLM, which is pre-trained on LV3D and shows strong 3D perception capability without any 3D specific architectural design or training objective. 
- Cube-LLM exhibits intriguing properties similar to LLMs, such as chain-of-thought prompting, instruction following, and visual prompting.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the limitations of the proposed approach. For example, it would be useful to discuss the potential challenges in scaling up the proposed approach to larger datasets and more complex 3D scenes. 
- The paper does not compare the proposed approach with other state-of-the-art methods for 3D visual understanding. For example, it would be useful to compare the performance of Cube-LLM with other MLLMs on the same benchmarks. 
- The paper does not provide a detailed analysis of the computational cost of the proposed approach. For example, it would be useful to discuss the training time and memory requirements of Cube-LLM.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed approach, particularly regarding scalability. While the authors mention the potential for scaling up, they do not delve into the specific challenges that might arise when dealing with significantly larger datasets or more complex 3D scenes. For instance, how would the performance of Cube-LLM be affected by an increase in the number of objects, the diversity of object categories, or the complexity of the scene geometry? A detailed analysis of these factors would provide a more realistic assessment of the approach's practical applicability. Furthermore, it would be beneficial to explore potential strategies for mitigating these challenges, such as data augmentation techniques or more efficient training algorithms. The paper should also discuss the potential impact of data quality and biases on the performance of Cube-LLM, especially when dealing with real-world datasets.

In addition to a more detailed discussion of limitations, the paper should include a more comprehensive comparison with other state-of-the-art methods for 3D visual understanding. While the authors compare Cube-LLM with some existing methods, a more thorough comparison with other MLLMs on the same benchmarks would be valuable. This comparison should not only focus on overall performance but also on specific aspects such as the ability to handle occlusions, variations in viewpoint, and the accuracy of 3D bounding box predictions. It would also be useful to compare the computational cost and memory requirements of Cube-LLM with other MLLMs. This would provide a more complete picture of the strengths and weaknesses of the proposed approach and help to identify areas for future improvement. The paper should also discuss the potential for combining Cube-LLM with other techniques, such as depth estimation or surface reconstruction, to further enhance its 3D understanding capabilities.

Finally, the paper should provide a more detailed analysis of the computational cost of the proposed approach. While the authors mention the training time and memory requirements, a more detailed analysis of the computational complexity of the model would be beneficial. This analysis should include a breakdown of the computational cost of different components of the model, such as the visual encoder, the language model, and the 3D projection layer. It would also be useful to discuss the potential for optimizing the model for efficiency, such as through model compression or quantization techniques. The paper should also discuss the potential impact of the choice of hardware on the training time and memory requirements of Cube-LLM. A more detailed analysis of the computational cost would help to make the proposed approach more accessible to a wider range of researchers and practitioners.

### Questions

- How does the performance of Cube-LLM vary with different input resolutions? 
- How does the performance of Cube-LLM compare with other state-of-the-art methods for 3D visual understanding? 
- What are the potential applications of Cube-LLM in real-world scenarios?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
