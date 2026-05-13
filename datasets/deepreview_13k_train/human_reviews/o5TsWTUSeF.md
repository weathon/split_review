# ChartMoE: Mixture of Diversely Aligned Expert Connector for Chart Understanding

- Decision: Accept
- Scores: 6, 5, 8, 8

## Abstract
Automatic chart understanding is crucial for content comprehension and document parsing. Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities in chart understanding through domain-specific alignment and fine-tuning. However, current MLLMs still struggle to provide faithful data and reliable analysis only based on charts. To address it, we propose ChartMoE, which employs the Mixture of Expert (MoE) architecture to replace the traditional linear projector to bridge the modality gap. Specifically, we train several linear connectors through distinct alignment tasks, which are utilized as the foundational initialization parameters for different experts. Additionally, we introduce ChartMoE-Align, a dataset with nearly 1 million chart-table-JSON-code quadruples to conduct three alignment tasks (chart-table/JSON/code). Combined with the vanilla connector, we initialize different experts diversely and adopt high-quality knowledge learning to further refine the MoE connector and LLM parameters. Extensive experiments demonstrate the effectiveness of the MoE connector and our initialization strategy, e.g., ChartMoE improves the accuracy of the previous state-of-the-art from 80.48% to 84.64% on the ChartQA benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces ChartMoE, a novel approach that leverages a Mixture of Expert (MoE) architecture to improve automatic chart understanding with Multimodal Large Language Models (MLLMs). ChartMoE addresses the limitations of existing MLLMs by using specialized linear connectors for diverse expert initialization, coupled with a unique dataset, ChartMoE-Align, containing nearly one million chart-related quadruples. This setup significantly enhances data interpretation from charts, pushing the accuracy on the ChartQA benchmark from 80.48% to 84.64%, showcasing a substantial improvement over previous methods.

### Strengths
S1. Innovative Methodology: The introduction of the ChartMoE method, which utilizes a Mixture of Experts (MoE) architecture, represents a significant innovation in the field of automatic chart understanding. This approach addresses the modality gap effectively and could potentially set a new direction for future research in multimodal learning systems.

S2. Comprehensive Dataset: The creation of the ChartMoE-Align dataset is commendable. Its large scale and diversity are well-suited for robust pre-training in chart alignment tasks. This dataset not only serves the immediate needs of the study but also provides a valuable resource for the broader research community to explore complex multimodal tasks involving charts and text.

S3. Extensive Experimental Validation: The paper presents extensive experiments that demonstrate the effectiveness of the ChartMoE approach. The thoroughness of these experiments, which include a variety of scenarios and detailed performance metrics, establishes a strong benchmark for future comparative studies.

S4. Clear Writing: The manuscript is exceptionally well-written, providing clear explanations and methodical presentation of the concepts and methodologies involved. This clarity enhances the reader's understanding and appreciation of the work's contributions to the field.

### Weaknesses
W1: Details on Dataset Construction

The paper lacks critical details on the dataset construction process. Clarifications are needed regarding the criteria used to select and filter charts for inclusion in the dataset. Specifically, the process for generating meta CSV data via Large Language Models (LLM) requires more transparency. 
More details on which LLMs were used and the code templates for different types of charts are missing. Such information is crucial for reproducibility and for understanding the dataset's applicability to other multimodal tasks.
The manuscript should discuss the steps taken to ensure the quality of the data, including any validation mechanisms or controls used during dataset assembly.

W2: Clarification of Experiment Results

The paper briefly mentions that the proposed method shows weaknesses in some settings compared to baselines, as detailed in Tables 2 and 3. However, these points are not adequately addressed or explained. A more thorough analysis of why ChartMoE underperforms in these instances would be valuable for readers and for future improvements to the method.

### Questions
Q1: Modality-Specific Contributions

It would be beneficial for the paper to elaborate on the unique contributions of different representations (JSON, code, and chart) in the context of chart-related tasks. Understanding how each representation impacts the model's learning and performance could provide insights into optimizing future models for similar tasks.


Q2: Necessity and Efficiency of Large-Scale Alignment Dataset

The heuristic approach to generating a large-scale dataset raises questions about the efficiency and necessity of such a volume of data. Is there potential to achieve similar performance with a smaller, possibly more curated dataset? This exploration could lead to more resource-efficient training processes and better generalization in practical applications.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces ChartMoE, a multimodal large language model  that enhances automatic chart understanding through a MoE architecture. Unlike traditional linear connectors, ChartMoE uses diverse expert connectors aligned with specific tasks (chart-table, chart-JSON, and chart-code) to bridge the gap between visual encoders and large language models. The paper also presents ChartMoE-Align, a dataset with nearly 1 million chart-table-JSON-code quadruples for training.

### Strengths
1. ChartMoE’s use of task-specific expert connectors in a Mixture of Experts (MoE) framework provides a  solution to multimodal chart understanding.

2. ChartMoE-Align, a large-scale dataset with varied chart alignments (table, JSON, code).

3. The three-stage training paradigm increass its accuracy in extracting and interpreting numerical data.

### Weaknesses
1. The use of MOE in MLLMs is not particularly novel, as several prior works have already explored MoE structures to enhance model performance. From an innovation standpoint, this reliance on MoE does not introduce a distinctly new approach and could be considered a weakness in terms of contribution.

2. The multi-expert structure, along with the diverse alignment tasks, adds significant complexity to ChartMoE’s architecture. Also, the training data, being mostly synthetic, might limit the model’s ability.

### Questions
see above

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces ChartMoE, a multi-task aligned and instruction-tuned MLLM designed for complex chart understanding and reasoning. The key contribution is the replacement of the traditional linear connector with the Mixture of Expert (MoE) architecture, which improves chart understanding by bridging the modality gap. Additionally, a new dataset called ChartMoE-Align is introduced, containing nearly 1 million chart-table-JSON-code quadruples for alignment training. The proposed three-stage training paradigm and high-quality knowledge learning approach result in significantly improved performance compared to the previous state-of-the-art on various benchmarks.

### Strengths
This paper incorporates a Mixture of Expert architecture to bridge the gap between charts and language models and offers a valuable insight for the expert initialization manner. The creation of the ChartMoE-Align dataset with nearly 1 million chart-table-JSON-code quadruplets is a significant contribution to the field, allowing for detailed and meticulous chart alignment pre-training.

The paper is clear and well written in general, is well motivated, and comes with an extensive and comprehensive ablation study.

### Weaknesses
The paper focuses on conducting experiments on a single Vision Encoder and Large Language Model, which limits the generalizability of the proposed method. It would be beneficial to test the effectiveness of ChartMoE on a diverse set of MLLMs, including those with different architectures and pre-training datasets, to ensure its applicability across different models and scenarios. For example, evaluating on models with varying vision encoders (e.g., ViT, Swin) and language models (e.g., different sizes of LLaMA, or models like Flan-T5) would provide a more robust assessment of the method's effectiveness. The current experiments do not explore the sensitivity of ChartMoE to the choice of base MLLM, which is a crucial factor for practical deployment.

The paper does not thoroughly discuss potential limitations or challenges that may arise when implementing ChartMoE in practical applications. For instance, the computational cost of training and inference with the MoE architecture, especially with a large number of experts, should be addressed. The paper also lacks a discussion on the potential for overfitting to the specific alignment dataset, and how this might affect performance on out-of-distribution charts. Furthermore, the robustness of ChartMoE to noisy or incomplete chart data is not explored, which is a critical consideration for real-world applications.

### Questions
1. In line 369, the error analysis suggests that many errors stem from the limitations of the evaluation metric, namely string matching. Are other comparison models also limited by this?
2. Can you provide more detailed explanations of the data construction process, such as how code templates for different types of charts were obtained? Were they manually constructed?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposed ChartMoE, which employs the Mixture of Expert (MoE) architecture to replace the traditional linear projector to bridge the modality gap.

### Strengths
1. First introduce MoE MLLM for chart task, the model architechture design which using MoE in connector is novel.
2. Detailed experiments and analysis, extensivequantitativeandqualitativestudies.
3. Introduced a large dataset for chart pre-train data.

### Weaknesses
1. limmited innovation: MoE on multimodal language models has been explored in other domains. There's a trade-off between the performance gain and the increase of model parameters and inference time. The paper does not sufficiently address the novelty of applying MoE specifically to the connector in the context of chart understanding, especially given prior work in other modalities. The performance gains should be more thoroughly contextualized against the increase in computational cost, including both parameter count and inference latency. A more detailed analysis of the specific benefits of this architectural choice over other possible MoE implementations is needed.
2. The contributions of MoE module is unclear, more theoretical analysis is needed such as the knowledge in the routing to differnernt experts. The paper lacks a rigorous analysis of how the routing mechanism within the MoE contributes to the model's performance. It would be beneficial to understand what specific types of inputs or chart features are routed to each expert and why. Without this analysis, it is difficult to assess the true impact of the MoE module beyond a simple increase in model capacity. The paper should provide a more in-depth exploration of the learned representations within each expert and how they contribute to the overall chart understanding.

### Questions
Have you ever tried training on your alignment data with random initialization of expert parameters and balanced loss from scratch? It will better prove the significance of this work.

### Soundness
3

### Presentation
3

### Contribution
3
