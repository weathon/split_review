### Summary

This paper introduces a novel approach called Retrieval-Augmented Test-Time Adaptation (RA-TTA) for vision-language models (VLMs). The authors address the challenge of distribution shifts between pre-training data and test data, which can degrade the performance of VLMs. Existing test-time adaptation (TTA) methods rely solely on the internal knowledge encoded within the model parameters, which are limited by the pre-training data. To overcome this limitation, RA-TTA incorporates external knowledge from a web-scale image database to adapt VLMs to the test distribution. The method utilizes the bi-modal nature of VLMs, employing fine-grained text descriptions for both retrieving relevant external images and refining the model's predictions. The authors demonstrate the effectiveness of RA-TTA through extensive evaluations on 17 datasets, showing that it outperforms state-of-the-art methods by an average of 2.49-8.45%. The paper highlights the potential of leveraging external knowledge to enhance the adaptability of VLMs in real-world scenarios.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach, RA-TTA, which combines retrieval-augmented generation with test-time adaptation for vision-language models. This is a creative solution to the problem of distribution shifts, and the use of external knowledge is a significant departure from existing methods that rely solely on internal model knowledge.
2. The paper is well-structured and clearly written. The authors provide a detailed explanation of the RA-TTA method, including the description-based retrieval and adaptation processes. The use of figures and examples helps to illustrate the key concepts and the workflow of the proposed approach.
3. The authors conduct extensive evaluations on 17 datasets, which provides strong empirical evidence for the effectiveness of RA-TTA. The results show that RA-TTA outperforms state-of-the-art methods by a significant margin, demonstrating its practical value.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not extensively discuss the limitations of the RA-TTA method. For example, the reliance on a web-scale image database for retrieval may not be feasible in all scenarios, and the quality of the retrieved images can significantly impact the performance of the method. The paper could benefit from a more thorough discussion of these limitations and potential solutions. Specifically, the paper lacks a discussion on the potential for bias in the retrieved images, which could stem from the web-scale database itself. This bias could lead to skewed predictions, especially if the test data distribution differs significantly from the retrieval database. Furthermore, the paper does not address the computational cost associated with retrieving and processing images from a large-scale database, which could be a practical limitation in real-world applications.
2. The paper could benefit from a more detailed comparison with existing retrieval-augmented methods for VLMs. While the authors mention some related work, a deeper analysis of the similarities and differences between RA-TTA and these methods would provide a clearer understanding of the contributions of this work. The comparison should include a discussion of the specific retrieval mechanisms, the types of external knowledge used, and the adaptation strategies employed by other methods. A more granular comparison would help to highlight the unique aspects of RA-TTA and its advantages over existing approaches.
3. The paper does not provide a detailed analysis of the computational cost of the RA-TTA method. The process of retrieving external images and adapting the model at test time could be computationally expensive, and a thorough analysis of the time and memory requirements would be valuable for practical applications. The paper should include a breakdown of the computational cost associated with each step of the RA-TTA process, including the image retrieval, text encoding, and model adaptation. This analysis should also consider the scalability of the method with respect to the size of the retrieval database and the number of test samples.

### Suggestions

The paper should include a more detailed discussion of the potential biases introduced by the web-scale image database used for retrieval. The authors should explore methods to mitigate these biases, such as using a more diverse retrieval database or employing techniques to re-weight the retrieved images based on their relevance and representativeness. Furthermore, the paper should investigate the impact of the quality of the retrieved images on the performance of RA-TTA. This could involve experiments with different retrieval strategies or the use of image quality assessment metrics to filter out low-quality images. A sensitivity analysis of the method's performance with respect to the quality of the retrieved images would provide valuable insights into its robustness and limitations. The authors should also consider the computational cost of the retrieval process and explore techniques to optimize it, such as using approximate nearest neighbor search or caching retrieved images.

To enhance the comparison with existing retrieval-augmented methods, the authors should provide a more detailed analysis of the specific retrieval mechanisms, the types of external knowledge used, and the adaptation strategies employed by other methods. This analysis should include a discussion of the strengths and weaknesses of each approach and highlight the unique aspects of RA-TTA. For example, the authors could compare RA-TTA with methods that use text-based retrieval or those that rely on a fixed set of external images. A more granular comparison would help to clarify the contributions of this work and its advantages over existing approaches. The authors should also discuss the potential limitations of RA-TTA compared to other methods, such as its reliance on a large-scale image database and the computational cost of the retrieval process.

The paper should include a detailed analysis of the computational cost of the RA-TTA method, including a breakdown of the time and memory requirements for each step of the process. This analysis should consider the scalability of the method with respect to the size of the retrieval database and the number of test samples. The authors should also explore techniques to optimize the computational cost of RA-TTA, such as using more efficient retrieval algorithms or parallelizing the adaptation process. A thorough analysis of the computational cost would be valuable for practical applications and would help to assess the feasibility of deploying RA-TTA in real-world scenarios. The authors should also discuss the trade-offs between computational cost and performance and provide guidelines for selecting the appropriate parameters for different applications.

### Questions

1. How does the performance of RA-TTA vary with the size and quality of the external image database? Are there any minimum requirements for the database to achieve the reported performance gains?
2. What are the potential biases introduced by the web-scale image database used for retrieval, and how can these biases be mitigated?
3. How does RA-TTA compare to other retrieval-augmented methods for VLMs in terms of performance, computational cost, and robustness to distribution shifts?
4. Can the RA-TTA method be extended to other types of models or tasks beyond vision-language models? What are the potential challenges and opportunities for such extensions?

### Rating

6

### Confidence

4

**********
