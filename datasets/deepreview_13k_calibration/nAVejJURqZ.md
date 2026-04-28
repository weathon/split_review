# TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning

- Decision: Accept
- Avg Score: 5.80
- Scores: 6, 6, 3, 6, 8

## Abstract
Multimodal Large Language Models (MLLMs) have demonstrated impressive performance in short video understanding. However, understanding long-form videos still remains challenging for MLLMs. 
This paper proposes \textbf{TimeSuite}, a collection of new designs to adapt the existing short-form video MLLMs for long video understanding, including a simple yet efficient framework to process long video sequence, a high-quality video dataset for grounded tuning of MLLMs, and a carefully-designed instruction tuning task to explicitly incorporate the grounding supervision in the traditional QA format.
Specifically, based on VideoChat, we propose our long-video MLLM, coined as VideoChat-T, by implementing a token shuffling to compress long video tokens and introducing Temporal Adaptive Position Encoding (TAPE) to enhance the temporal awareness of visual representation. 
Meanwhile, we introduce the TimePro, a comprehensive grounding-centric instruction tuning dataset composed of 9 tasks and 349k high-quality grounded annotations. 
Notably, we design a new instruction tuning task type, called Temporal Grounded Caption, to perform detailed video descriptions with the corresponding timestamps prediction. This explicit temporal location prediction will guide MLLM to correctly attend on the visual content when generating description, and thus reduce the hallucination risk caused by the LLMs.
Experimental results demonstrate that our TimeSuite provides a successful solution to enhance the long video understanding capability of short-form MLLM, achieving improvement of \textbf{5.6\%} and \textbf{6.8\%} on the benchmarks of Egoschema and VideoMME, respectively.
In addition, VideoChat-T exhibits robust zero-shot temporal grounding capabilities, significantly outperforming the existing state-of-the-art MLLMs.
After fine-tuning, it performs on par with the traditional supervised expert models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces TimeSuite, a set of designs to adapt short-form video multimodal large language models (MLLMs) for long video understanding. It includes a new framework for processing long video sequences, a high-quality dataset (TimePro) for grounded tuning, and an instruction tuning task to incorporate grounding supervision. The proposed model, VideoChat-T, uses token shuffling for compression and Temporal Adaptive Position Encoding (TAPE) for enhanced temporal awareness. A new task type, Temporal Grounded Caption, is introduced to improve video descriptions and timestamp prediction. Experimental results show significant improvements on benchmarks and robust zero-shot temporal grounding capabilities.

### Strengths
1. This work is highly complete. The contributions are multiple folds: VideoChat-T framework, TimePro dataset, Temporal Grounded Caption task, and extensive experiments and analysis.

2. Significant improvements on long video processing shown in Table 2.

3. Interesting TAPE, utilizing zero-padding anchors and gradual transmission of relative temporal positional encoding.

### Weaknesses
1. The VideoChat2 baseline shows a weak performance with 39.5 accuracy in VideoMME. It would be more convincing to use a stronger 7B model for evaluation, such as onevision-7B, which achieves 58.2 accuracy. The choice of a weaker baseline makes it difficult to ascertain whether the improvements are due to the proposed method or simply a result of using a more capable model. A more robust comparison would involve evaluating against state-of-the-art models with similar parameter counts to ensure a fair assessment of the proposed approach's effectiveness.

2. The short-term performance on MVbench drops require a deeper investigation rather than mere explanations. The explanation provided does not fully address the underlying reasons for this performance drop. It is crucial to analyze the specific characteristics of the MVBench dataset and the model's behavior on short-term videos to pinpoint the cause of the degradation. A more detailed analysis of the model's attention patterns, feature representations, and temporal modeling capabilities on short videos is needed to understand this behavior.

3. Instead of using implicit TAPE, consider implementing a more explicit solution like 3D RoPE (e.g., Qwen2-VL) and conduct an ablation study. The current approach of using TAPE, while novel, lacks a direct comparison with established methods for temporal encoding. An ablation study comparing TAPE with a more explicit method like 3D RoPE would provide valuable insights into the effectiveness of TAPE and its advantages or disadvantages compared to existing techniques. This would also help to understand if the implicit nature of TAPE is truly beneficial or if a more explicit approach would yield better results.

### Questions
Could training the model on both temporal and non-temporal grounding data mitigate performance loss in short-term videos? Why does temporal grounding data lead to accuracy loss in short-term videos? Despite this, why is short-term accuracy on VideoMME still improved?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces TimeSuite, a collection of designs focusing on efficient architecture, high-quality data, and a novel instruction-tuning task. Building on TimeSuite, the authors propose a long-video multimodal large language model (MLLM) named VideoChat-T, which demonstrates robust zero-shot temporal grounding capabilities and significantly outperforms existing state-of-the-art MLLMs. After fine-tuning, it performs comparably to traditional supervised expert models.

### Strengths
1. The paper is well-written. The proposed method is well-illustrated and easy to follow.
2. The contributions include a strong video LLM (VideoChat-T) and a temporal-centric instruction-tuning dataset (TimePro), both of which are substantial advancements in the field.
3. The authors conduct a thorough evaluation and ablation study to validate the effectiveness of the proposed model.

### Weaknesses
While I do not see major flaws in this paper, I note that the technical novelty is relatively limited. 

There are two main modules in VideoChat-T: (1) the VL-connector with token shuffling, and (2) temporal adaptive position encoding (TAPE). 
However, the VL-connector's approach of concatenating tokens in the channel dimension and then compressing the channel dimension with a linear layer has been previously utilized in Qwen2-vl (I am unsure who proposed this operation first; please correct me if you know). For TAPE, the design of the position embedding is derived from CPVT. These factors somewhat limit the technical novelty of this work.

### Questions
1. Why is the operation of “concatenating tokens in the channel dimension and then compressing the channel dimension with a linear layer” referred to as “token shuffle”?
2. Can you use the same training data (e.g., TimePro) to train other VideoLLMs (e.g., TimeChat) and then compare their performance? This would help eliminate the impact of training data, allowing for a clearer assessment of how performance is associated with model design.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces TimeSuite, a framework designed to enhance Multimodal Large Language Models (MLLMs) for long video understanding. It proposes a new long-video MLLM called VideoChat-T, featuring token shuffling and Temporal Adaptive Position Encoding (TAPE) for better temporal awareness. TimeSuite includes a specialized instruction tuning dataset, TimePro, comprising 349,000 annotations across nine tasks, with a focus on Temporal Grounded Captioning for accurate video descriptions with timestamps. Experiments show that TimeSuite improves long video comprehension, achieving notable performance gains on benchmarks and demonstrating strong zero-shot grounding capabilities, rivaling traditional supervised models after fine-tuning.

### Strengths
- This paper propose TimeSuite, a collection of new designs to improve the long video understanding capability of the existing short-form MLLMs

### Weaknesses
 - The paper does not adequately compare its results against notable existing works, such as Qwen2-VL and Llava-OneVision. A comprehensive comparison would help contextualize the contributions and highlight any advantages or shortcomings.
- The dataset used in the experiments, TimePro is highly imbalanced (Figure 3). It is unclear whether the authors have explored different data ratios or configurations. Investigating this aspect could provide insights into the robustness of the proposed method and its adaptability to varying data distributions.

### Questions
See weaknesses

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents TimeSuite, a novel approach designed to enhance the understanding of long-form videos using existing short-form MLLMs. TimeSuite includes an efficient framework for processing long video sequences, a high-quality dataset for grounded tuning, and a new instruction tuning task to integrate grounding supervision in a traditional QA format. Experimental results demonstrate the advantage of  the proposed method.

### Strengths
The proposed method is both systematic and effective. The experiments are comprehensive and detailed, and the results of the method are convincing.

### Weaknesses
Although the proposed method includes specific designs tailored to the problem, the novelty is limited. It is a relatively engineering-focused paper. The systematic description is quite detailed, but it lacks a deeper discussion of the underlying ideas, theories and principles. Additionally, due to the design of auxiliary tasks and datasets, the comparison with baseline methods may be somewhat unfair.

### Questions
It would be beneficial to include a more in-depth discussion of theories and principles in the manuscript.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces TimeSuite, a novel framework designed to enhance the capabilities of Multimodal Large Language Models (MLLMs) for understanding long videos through grounded tuning. TimeSuite comprises three key components: a token shuffling scheme to compress visual tokens, reducing computational load; Temporal Adaptive Position Encoding (TAPE) to boost the temporal sensitivity of visual representations; and a new instruction tuning task, Temporal Grounded Caption, which integrates timestamp prediction to guide MLLMs to focus on relevant visual content. The authors also present TimePro, a high-quality dataset with 349k grounded annotations across 9 tasks, aimed at improving MLLMs' temporal perception. Experiments demonstrate that TimeSuite significantly improves performance on long video understanding benchmarks like Egoschema and VideoMME, with improvements of 5.6% and 6.8% respectively, and exhibits robust zero-shot temporal grounding abilities, outperforming existing MLLMs. The paper concludes that TimeSuite provides effective designs for MLLMs to enhance their performance on temporal grounding and long video question answering.

### Strengths
- **Originality**: The paper introduces TimeSuite, a novel framework that enhances Multimodal Large Language Models (MLLMs) for long video understanding through grounded tuning. It proposes creative solutions like Token Shuffle and Temporal Adaptive Position Encoding (TAPE), which are innovative approaches to compress visual tokens and enhance temporal awareness in video representations.

- **Quality**: The research demonstrates high quality through rigorous experimentation and ablation studies, showing significant improvements over existing benchmarks like Egoschema and VideoMME. The paper also presents a comprehensive dataset, TimePro, with 349k high-quality annotations.

- **Clarity**: The paper is well-structured and clearly articulated. Complex concepts such as Temporal Grounded Caption and TAPE are explained with clarity, making the paper accessible to readers. Figures and tables are effectively used to convey key results and comparisons.

- **Significance**: The proposed solutions for temporal grounding could have broad implications for video understanding tasks, and the zero-shot capabilities of VideoChat-T are particularly noteworthy, showing the potential to rival supervised expert models.

### Weaknesses
 - **Generalization**: The paper primarily focuses on video datasets that are thematically similar. It is unclear how well TimeSuite generalizes to videos with significantly different content or from other domains, such as OpenEQA and CinePile. Expanding the dataset to include more diverse domains, particularly those with different temporal dynamics and visual characteristics, could strengthen the paper's claims. The current evaluation may not fully capture the model's ability to handle out-of-domain videos, which is crucial for real-world applications.

- **Scalability and Efficiency**: The computational requirements for processing long videos are high. The paper could provide more insights into the scalability of TimeSuite and its efficiency, especially when dealing with very long videos or a large number of frames. Details on memory consumption, processing time per frame, and the impact of video length on performance are needed to assess the practical applicability of the proposed method. The paper should also discuss the limitations of the token shuffling mechanism when dealing with extremely long sequences.

- **Longitudinal Performance**: The paper does not address how the model's performance degrades over time or with an increasing amount of video data. It would be beneficial to include studies on the long-term sustainability of the model's performance. Specifically, how does the model's accuracy and temporal grounding ability change as the video length increases significantly, and are there any mechanisms to mitigate performance degradation over very long sequences?

- **Qualitative Analysis**: While quantitative results are provided, a deeper qualitative analysis of the model's outputs, especially in cases of failure, could offer actionable insights into the model's reasoning process and areas for improvement. The paper should include examples of failure cases, analyze the reasons for these failures, and discuss the limitations of the model in handling complex temporal reasoning tasks.

### Questions
1. **Token Shuffle Mechanism**: Could the authors elaborate on the decision to use a token shuffling mechanism over other compression techniques, and provide a comparison of its performance against alternatives in terms of temporal consistency and computational efficiency?

2. **Temporal Adaptive Position Encoding (TAPE)**: It would be beneficial if the authors could discuss the potential limitations of TAPE in handling videos with highly variable or complex temporal dynamics, and whether there are any specific domains where TAPE excels or falls short.

3. **Data Diversity and Model Generalization**: How does the choice of datasets for TimePro impact the model's generalization capabilities? Are there any biases introduced by the current dataset composition that could limit the model's applicability to unseen video domains?

4. **Zero-Shot Performance vs. Fine-Tuning**: The paper mentions robust zero-shot capabilities. Could the authors provide insights into why there is a performance gap between zero-shot and fine-tuned models, and what aspects of the model or training process could be improved to bridge this gap?

5. **Long-Video Understanding Limitations**: Are there specific scenarios or types of long videos where VideoChat-T struggles? If so, could the authors suggest potential improvements or future work to address these limitations?

6. **Integration of Expert Model Capabilities**: The authors propose a future direction of integrating expert model capabilities into MLLMs. What are the authors' thoughts on the feasibility of this approach, and what challenges need to be overcome to achieve a unified generalist MLLM?

7. **Complex Output Formats**: For tasks requiring complex outputs, such as highlight detection, how can MLLMs be adapted to handle multiple discrete timestamps and saliency scores effectively? Are there plans to modify the model architecture or training process to better accommodate such tasks?

### Soundness
2

### Presentation
2

### Contribution
2
