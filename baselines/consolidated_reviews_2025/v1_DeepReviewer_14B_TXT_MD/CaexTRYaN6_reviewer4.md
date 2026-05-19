### Summary

This paper proposes a novel method for dataset distillation using diffusion models, which incorporates concepts from large language models (LLMs) to enhance the quality of the distilled datasets. The method, termed CONCORD, leverages the rich conceptual knowledge of LLMs to guide the diffusion process, ensuring that the generated images are not only visually realistic but also semantically meaningful. The authors demonstrate the effectiveness of their approach through extensive experiments on ImageNet-1K and its subsets, showing state-of-the-art performance in terms of both image quality and downstream task performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to dataset distillation by incorporating concepts from LLMs, which is a significant advancement over existing methods that primarily focus on imitating dataset-level concept distributions.
2. The proposed method is theoretically sound and well-motivated, with a clear explanation of how the conceptual information from LLMs is integrated into the diffusion process.
3. The experimental results are comprehensive and convincing, showing significant improvements over state-of-the-art methods across various benchmarks and settings.
4. The authors provide a detailed analysis of the method's performance, including ablation studies and visualizations, which helps in understanding the contributions of different components of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

1. The method's reliance on LLMs for concept acquisition might limit its applicability in scenarios where LLMs are not readily available or where computational resources are constrained. Specifically, the computational overhead of querying LLMs for each category, especially for large datasets with numerous classes, could be substantial. Furthermore, the quality of the concepts derived from LLMs is not guaranteed to be perfectly aligned with the visual features relevant for image generation, potentially introducing noise or biases into the distilled dataset.
2. The paper does not extensively discuss the potential limitations or failure cases of the proposed method. For instance, it would be beneficial to analyze scenarios where the LLM-derived concepts are ambiguous or misleading, leading to poor image generation. The paper should also explore the sensitivity of the method to the quality of the LLM's output, and how this impacts the final distilled dataset.
3. The generalizability of the method to other data modalities beyond images is not explored. The current approach is heavily reliant on the visual nature of images and the ability of LLMs to provide descriptive text. It is unclear how this method could be adapted for other data types, such as audio, video, or time-series data, where the concept acquisition process would require a different approach.

### Suggestions

The authors should investigate methods to reduce the computational cost associated with using LLMs for concept acquisition. This could involve techniques such as caching LLM outputs for frequently used categories, or exploring more efficient methods for concept retrieval that do not rely on expensive LLM queries. Furthermore, the authors should consider incorporating a mechanism to evaluate the quality of the concepts retrieved from LLMs, and potentially filter out or refine concepts that are deemed unreliable or irrelevant. This could involve using a secondary model or a human-in-the-loop approach to validate the concepts before they are used to guide the diffusion process. The authors should also explore the use of smaller, more efficient LLMs or knowledge distillation techniques to reduce the computational burden.

To address the lack of discussion on failure cases, the authors should conduct a more thorough analysis of scenarios where the proposed method performs poorly. This should include a detailed examination of the types of images that are difficult to generate using the LLM-guided diffusion process, and the reasons why these images are challenging. For example, the authors could analyze cases where the LLM-derived concepts are too abstract or ambiguous, or where the diffusion model struggles to translate these concepts into realistic images. The authors should also investigate the impact of noisy or misleading concepts on the quality of the distilled dataset, and explore methods to mitigate these issues. This could involve techniques such as using multiple LLMs or incorporating a feedback mechanism to refine the concepts based on the generated images.

Finally, the authors should explore the potential for extending their method to other data modalities. This could involve investigating how to adapt the concept acquisition process for non-visual data types, such as audio or time-series data. For example, the authors could explore the use of audio transcription models or time-series analysis techniques to extract relevant concepts from these data types. The authors should also consider how the diffusion process could be adapted to generate data in these modalities, and whether the proposed approach can be generalized to handle the unique characteristics of these data types. This would significantly broaden the applicability of the proposed method and demonstrate its potential for a wider range of applications.

### Questions

1. How does the method handle cases where the LLM-derived concepts are ambiguous or misleading? Are there any mechanisms in place to mitigate the impact of such cases on the quality of the distilled dataset?
2. Can the proposed method be extended to other data modalities beyond images, such as audio or video? If so, what modifications would be necessary to adapt the method to these modalities?
3. What is the computational overhead of using LLMs for concept acquisition, and how does it compare to the computational cost of other dataset distillation methods? Are there any strategies to reduce this overhead?

### Rating

6

### Confidence

4

**********
