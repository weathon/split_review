### Summary

This paper proposes a multi-resolution HuBERT, which extends HuBERT by incorporating multi-resolution masked unit prediction with a hierarchical Transformer architecture. The proposed model aims to encode speech representations across multiple resolutions within a single model. The authors show that the proposed model outperforms the original HuBERT on various benchmarks, including the LibriSpeech dataset and the Speech Universal PERformance Benchmark (SUPERB).

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed multi-resolution HuBERT (MR-HuBERT) introduces a novel hierarchical framework for multi-resolution pre-training of speech representations. The model is pre-trained using multi-resolution masked unit prediction objectives, which are integrated with HuBERT-style clustering units. This approach allows the model to encode speech information across multiple resolutions in a single model.
- The authors provide extensive experimental results demonstrating the effectiveness of the proposed model. They show that MR-HuBERT achieves substantial performance improvements over baseline SSL models across various benchmarks, including different subsets of the LibriSpeech dataset, SUPERB, and ML-SUPERB.
- The authors have made the implementation of MR-HuBERT and the pre-trained models available as open-source resources on Fairseq and S3PRL. This allows other researchers to easily access and utilize the proposed model in their own research.
- The authors also discuss the ethical implications of their work, highlighting the potential for misuse of the model's capabilities and emphasizing the importance of responsible use.

### Weaknesses

#### Some Related Works


#### comment

 - The authors could provide more details on the computational cost of the proposed model compared to the original HuBERT. This would help readers understand the trade-offs between performance and computational resources.
- It would be beneficial if the authors provided more insights into the specific downstream tasks where the proposed model performs particularly well or poorly. This would help readers understand the strengths and limitations of the model.
- The authors could also discuss the potential limitations of their approach and suggest directions for future research. This would help readers understand the broader context of the work and its potential impact on the field.

### Suggestions

The paper would benefit from a more detailed analysis of the computational overhead introduced by the multi-resolution architecture. While the authors mention the performance gains, a thorough comparison of training and inference times, as well as memory consumption, is crucial for practical adoption. Specifically, providing a breakdown of the computational cost associated with each resolution stream (high and low) would be valuable. This should include not only the overall training time but also the time spent on specific operations like the masked unit prediction at each resolution. Furthermore, it would be helpful to compare the number of parameters and FLOPs of the proposed model with the original HuBERT model to quantify the increase in computational complexity. Such an analysis would allow readers to better assess the trade-offs between performance gains and computational resources, which is essential for real-world applications.

To further strengthen the paper, the authors should provide a more granular analysis of the model's performance across different downstream tasks. While the overall performance on benchmarks like LibriSpeech, SUPERB, and ML-SUPERB is reported, it is important to understand the model's behavior on specific tasks within these benchmarks. For example, does the model perform better on tasks that require fine-grained temporal resolution, or does it excel in tasks that rely on more abstract speech representations? A detailed analysis of the model's performance on tasks such as speech recognition, speaker identification, emotion recognition, and speech translation would provide a more comprehensive understanding of its strengths and weaknesses. This analysis should also include a discussion of the specific characteristics of the tasks where the model underperforms, which could provide insights into the limitations of the proposed approach and guide future research directions.

Finally, the authors should delve deeper into the limitations of their approach and suggest concrete avenues for future research. For instance, the current multi-resolution approach uses a fixed set of resolutions. It would be interesting to explore adaptive resolution strategies, where the model dynamically adjusts the resolution based on the input speech signal. Another potential limitation is the reliance on a specific clustering algorithm for unit prediction. Investigating alternative clustering methods or even exploring unsupervised unit discovery techniques could lead to further improvements. Furthermore, the authors could discuss the potential impact of the choice of the hierarchical Transformer architecture on the model's performance. Exploring different architectural choices, such as using different types of attention mechanisms or incorporating other types of hierarchical structures, could be a valuable direction for future research. Addressing these limitations and suggesting specific future research directions would significantly enhance the paper's impact and contribute to the advancement of the field.

### Questions

- How does the proposed model perform on low-resource languages or dialects? Does the multi-resolution approach help in capturing the nuances of different languages and dialects?
- What are the potential applications of the proposed model beyond the tasks mentioned in the paper? Could it be used for other speech-related tasks such as speech synthesis or speech enhancement?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
