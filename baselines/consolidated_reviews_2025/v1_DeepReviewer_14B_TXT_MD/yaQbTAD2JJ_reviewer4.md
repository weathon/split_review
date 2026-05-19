### Summary

This paper presents a large-scale pretraining dataset for 2D and 3D called LV3D by combining multiple existing 2D and 3D recognition datasets under a common task formulation: as multi-turn question-answering. Then, it introduces a new multi-modal large language model named Cube-LLM and pre-train it on LV3D. The experiments on outdoor benchmarks demonstrate that Cube-LLM significantly outperforms existing baselines by 21.3 points of APBEV on the Ttc dataset for 3D grounded reasoning and 17.7 points on the DLM dataset for complex reasoning about driving scenarios, respectively.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper is well-written and easy to follow.
2. The proposed dataset is large-scale and comprehensive, which can be used for future research.
3. The proposed method is effective and achieves SOTA performance on multiple benchmarks.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is based on LLaVA-1.5, which is not the most recent version of LLaVA. It would be better to use the latest version of LLaVA to ensure the state-of-the-art performance.
2. The proposed method is not very novel. It mainly combines existing datasets and uses a standard pretraining approach. The core contribution seems to be the dataset itself, but the method for leveraging it is quite standard.
3. The paper does not provide a detailed analysis of the limitations of the proposed method. For example, it would be useful to discuss the potential challenges in scaling up the proposed approach to larger datasets and more complex 3D scenes. Specifically, the paper lacks discussion on how the model's performance might degrade with increased scene complexity, such as more cluttered environments or a higher density of objects. Furthermore, the paper does not address the potential for overfitting to the specific types of 3D scenes present in the training data, and how this might affect generalization to unseen environments.
4. The paper does not compare the proposed approach with other state-of-the-art methods for 3D visual understanding. For example, it would be useful to compare the performance of Cube-LLM with other MLLMs on the same benchmarks. A comparison with methods that explicitly model 3D geometry, such as those using point clouds or depth maps, would be particularly valuable. The paper should also include a comparison with other MLLMs that have been trained on similar datasets, to better understand the relative strengths and weaknesses of the proposed approach.
5. The paper does not provide a detailed analysis of the computational cost of the proposed approach. For example, it would be useful to discuss the training time and memory requirements of Cube-LLM. The paper should provide a breakdown of the computational resources required for training and inference, including the number of GPUs, training time, and memory usage. This information is crucial for assessing the practicality of the proposed approach, especially for researchers with limited computational resources.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed approach, particularly regarding scalability. While the authors mention the potential for scaling up, they do not delve into the specific challenges that might arise when dealing with significantly larger datasets or more complex 3D scenes. For instance, how would the performance of Cube-LLM be affected by an increase in the number of objects, the diversity of object categories, or the complexity of the scene geometry? A detailed analysis of these factors would provide a more realistic assessment of the approach's practical applicability. Furthermore, it would be beneficial to explore potential strategies for mitigating these challenges, such as data augmentation techniques or more efficient training algorithms. The paper should also discuss the potential impact of data quality and biases on the performance of Cube-LLM, especially when dealing with real-world datasets. For example, how would the model perform if the training data contains noisy or incomplete 3D information? Addressing these questions would strengthen the paper's analysis and provide a more comprehensive understanding of the proposed method's capabilities and limitations.

In addition to a more detailed discussion of limitations, the paper should include a more comprehensive comparison with other state-of-the-art methods for 3D visual understanding. While the authors compare Cube-LLM with some existing methods, a more thorough comparison with other MLLMs on the same benchmarks would be valuable. This comparison should not only focus on overall performance but also on specific aspects such as the ability to handle occlusions, variations in viewpoint, and the accuracy of 3D bounding box predictions. It would also be useful to compare the computational cost and memory requirements of Cube-LLM with other MLLMs. This would provide a more complete picture of the strengths and weaknesses of the proposed approach and help to identify areas for future improvement. The paper should also discuss the potential for combining Cube-LLM with other techniques, such as depth estimation or surface reconstruction, to further enhance its 3D understanding capabilities. This would provide a more comprehensive evaluation of the proposed method and its potential for real-world applications.

Finally, the paper should provide a more detailed analysis of the computational cost of the proposed approach. While the authors mention the training time and memory requirements, a more detailed analysis of the computational complexity of the model would be beneficial. This analysis should include a breakdown of the computational cost of different components of the model, such as the visual encoder, the language model, and the 3D projection layer. It would also be useful to discuss the potential for optimizing the model for efficiency, such as through model compression or quantization techniques. The paper should also discuss the potential impact of the choice of hardware on the training time and memory requirements of Cube-LLM. A more detailed analysis of the computational cost would help to make the proposed approach more accessible to a wider range of researchers and practitioners.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
