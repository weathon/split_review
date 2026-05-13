# LongLLaVA: Scaling Multi-modal LLMs to 1000 Images Efficiently via a Hybrid Architecture

- Decision: Reject
- Scores: 5, 5, 5, 8

## Abstract
Expanding the long-context capabilities of Multi-modal Large Language Models~(MLLMs) is crucial for video understanding, high-resolution image understanding, and multi-modal agents. This involves a series of systematic optimizations, including model architecture, data construction and training strategy, particularly addressing challenges such as \textit{degraded performance with more images} and \textit{high computational costs}. In this paper, we adapt the model architecture to a hybrid of Mamba and Transformer blocks, approach data construction with both temporal and spatial dependencies among multiple images and employ a progressive training strategy. The released model \textbf{LongLLaVA}~(\textbf{Long}-Context \textbf{L}arge \textbf{L}anguage \textbf{a}nd \textbf{V}ision \textbf{A}ssistant) is the first hybrid MLLM, which achieved a better balance between efficiency and effectiveness. LongLLaVA  not only achieves competitive results across various benchmarks, but also maintains high throughput and low memory consumption. Especially, it could process nearly a thousand images on a single A100 80GB GPU, showing promising application prospects for a wide range of tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents LongLLaVA, a novel solution to enhance the long-context capabilities. Architecture-wise, it combines Mamba (pseudo attention) and token compression.  It can process >1000 images on a single A100 80GB GPU. Experimental results show good performance in multi-modal long-context understanding tasks, surpassing many models in MileBench and VNBench. It also demonstrates strong application potential in healthcare and science domains

### Strengths
LongLLaVA can handle up to 1173 images on a single 80GB GPU, showing excellent processing power of handling more images, enabling more spatial and temporal information.

The proposed efficient hybrid architecture improving throughput and reducing memory usage while maintaining good performance in both ICL and VLM benchmarks. 

The enhanced data construction and progressive training strategy guide the model to distinguish temporal and spatial dependencies among images.

### Weaknesses
My main concern for the paper is that the motivation is not clearly justified. LongLLaVa aims to enable more frames (tokens) for Vision Language Models (VLM) and thus explores a Mamba-based architecture. However, the reason for choosing a hybrid architecture is confusing. Lines 127-128 mention the Mamba model's in-context learning (ICL) capability as indispensable. Is there any evidence or literature to support that this is a weakness of the Mamba architecture itself rather than a result of training data? Additionally, Cobra in Table 5 only has results with a 3B size model, while other models are 9B–13B. This is not a fair comparison and doesn't convincingly justify the choice of a hybrid architecture.

While supporting over 1,000 images on an A100 GPU looks promising, the performance is not satisfying. LongLLaVa-9B-MoE (with actual parameters of 53B) shows a significant performance degradation compared to LongVILA (VideoMME Average drops from 50.5 to 43.7). The 13B MoE model is also not comparable with LongVA (released in July and cited in the paper but not compared). Furthermore, what is the performance of LongLLaVa on regular VLM benchmarks like DocVQA, ChartQA, and MMMU? The results in Table 4 and Figure 5 are from different models than those in Tables 4 and 5, and the comparison is incomplete.

Furthermore, the design choices are not well-ablated. For example, why does the training pipeline (Figure 4) train the model sequentially? Many previous VLM works like LongVA, VILA, and InternVL mix most data in one stage instead of feeding it sequentially. Another point is the architecture design: why blend transformer and Mamba in a 7:1 ratio and only apply MoE in Mamba? Do other blending ratios hurt the performance or lead to less memory saving? Could you provide ablations and share the thoughts behind the design choices?

### Questions
Needle in a haystack benchmark missing? What is retrival rate for LongLLaVa

How the model (in Figure 2) is initialized for later VLM training?

L123-124: ring-attention and sequence parallel are actual same technique with different naming. 

L125: why sp or ring-atten introduce extra overhead? What is the comparison baseline here?

L127: Mama model … ICL capability … indispensable. Any evidence to support this is weakness from mamba arch itself rather than training data? Does this weakness exists in VLM or both LLM and VLM?

The paper titled LongLlava, seems to be like an extension of llava series work. But the architecture and training scheme have been both changed drastically.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents LongLLaVA, a MLLM designed for efficient long-video understanding. The proposed design applies a hybrid architecture inspired by Jamba that combines Mamba and Transformer layers, with 2D pooling applied for image token compression, and follows a progressive multi-stage training strategy. The paper conducts experiments in various benchmarks, including retrieval, counting, and video analysis tasks, while maintaining efficient resource use on an 80GB GPU for long video inference.

### Strengths
- The integration of Mamba and Transformer layers enables LongLLaVA to achieve quasi-linear computational complexity while supporting in-context learning. This design is well motivated to deal with long videos.
- Detailed experimental results, ablation studies, and diagnostic evaluations have been conducted on benchmarks like MileBench, VNBench, and Video-MME, showcasing that LongLLaVA has reasonable performances on multi-image and video tasks.
- LongLLaVA maintains a lower computational cost compared to full-attention counterparts, showing its potential in cost-effective deployment.

### Weaknesses
 - The use of LongLLaVA-9B from Expert-0 in the Mamba (Jamba) MoE Layer appears unorthodox and lacks sufficient justification. The VLM's capabilities are heavily dependent on its underlying LLM, and it's unclear how well Jamba expert-0 performs as an LLM. The paper should provide a more thorough analysis of why this specific expert was chosen, especially given the potential for performance variations across different experts within the MoE architecture.
- The evaluation baselines are outdated and not sufficiently competitive. While LongVA-7B is mentioned, it's not directly compared against, and several newer 7B VLMs with superior performance are excluded. Although fair comparisons are challenging due to varying training data mixtures and model backbones, the authors should provide a more comprehensive overview of existing VLMs of similar size, including LongVA-7B at the least. The lack of direct comparison with LongVA-7B, a model specifically designed for long-context video understanding, is a significant oversight.
- More rigorous experimental design is needed to demonstrate that the hybrid architecture doesn't compromise VLM performance. While Tables 4 and 5 show LongLLaVA-9B outperforming LLaVA-1.5-13B and LLaVA-1.6-13B, this comparison is skewed since Jamba already outperforms LLaMA2-13B (and likely Vicuna-1.5) in LLM benchmarks [1]. Additionally, the VLM training data mixtures differ. To validate that the hybrid architecture matches traditional full-attention LLM performance as a VLM backbone, LLMs models in those two architectures with similar capabilities (e.g., Zamba-2-7B [2] and LLaMA3.1-8B) should be trained using the LongLLaVA training recipe. The current comparisons do not isolate the impact of the hybrid architecture from the inherent differences in the base LLM models.
- The training strategy lacks sufficient ablation studies, particularly regarding the impact of removing replay data. The paper needs to explore the effect of removing replay data on both single-image and multi-image tasks, as well as the impact of varying the amount of replay data used during training. This is crucial for understanding the contribution of replay data to the final model performance.
- Tables require additional context. Tables 2 and 3 should include model sizes for open-source baselines. While PFLOPs indicates model efficiency, model sizes are crucial for understanding expected performance. The absence of model size information makes it difficult to assess the trade-offs between model size, computational cost, and performance.

### Questions
- What does 1D Pooling in table 4 specifically refer to?
- What does LLaVA-1.5-13B + Jamba in table 4 mean? Is it just replacing LLaVA-1.5-13B’s LLM with Jamba? Are those both trained with the LongLLaVA recipe?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The work introduces LongLLaVA, a multimodal large language model that aims to solve challenges related to scaling up the number of in-context images in similar models as well as study design choices in the architecture, data, and training recipe of multimodal LMs. The challenges and motivations are outlined clearly and the authors choose to explore a hybrid architecture inspired by recent work around state space models, token compression through 2D pooling, and various data augmentation strategies. The authors evaluate the work on three multi-image benchmarks and show strong performance against open-source baselines and comparable performance to some closed models, despite being much more efficient to serve. The authors run an ablation study on the architecture choices and showcase additional interesting applications for this new model.

### Strengths
- The motivations are outlined very clearly and the way the authors chose to address the challenges presented makes sense
- Hybrid architecture efficiency analysis
- Ablation of architecture choices
- Multiple model scales presents some scaling analysis
- Many experiments, including additional applications to healthcare and science

### Weaknesses
 - There is no ablation study showcasing the 3-stage finetuning vs a typical 1-stage finetuning step with all of the data across the three stages mixed in.

### Questions
- Are there any qualitative examples where this method performs better or worse than the baselines? Are there certain subtasks that this method is particularly well-suited for?
- As a result of pooling are there any tasks that suffer as a result? It could be helpful to include OCR or fine-grained image recognition tasks
- Does this new architecture show improved many-shot ICL performance (https://arxiv.org/abs/2404.11018) as opposed to finetuning?

### Soundness
2

### Presentation
2

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
The paper focuses on enhancing the long-context capabilities of Multi-modal Large Language Models (MLLMs), essential for tasks like video understanding, high-resolution image analysis, and multi-modal agents.

 The authors address key challenges, such as performance degradation with increased image inputs and high computational demands. They introduce a hybrid model architecture combining Mamba and Transformer blocks, optimize data construction to account for temporal and spatial dependencies, and use a progressive training strategy. 

The resulting model, LongLLaVA (Long-Context Large Language and Vision Assistant), demonstrates competitive performance on multiple benchmarks, while also being memory-efficient and capable of processing nearly a thousand images on a single A100 80GB GPU, highlighting its potential for various applications.

### Strengths
1.The paper presents a comprehensive set of optimizations, including model architecture, data construction, and training strategy, showcasing a well-rounded and complete approach.

2.It features clear and well-structured illustrations alongside a compelling and coherent narrative.

3.The work addresses the urgent and impactful need for scaling up the number of images and handling long video generation, which is crucial for advancing the capabilities of MLLMs.

4.Extensive ablation studies are conducted, comparing the proposed model with both open-source and proprietary models across various benchmark datasets, including rigorous long-context tests like the Needle-In-A-Haystack evaluation.

### Weaknesses
1.The paper does not provide a comprehensive comparison of maximum throughput and latency profiles between the hybrid-structured model, pure Transformer-based models, and Mamba-based models, leaving a gap in understanding the performance trade-offs.

2.The extension of an existing, widely-used hybrid architecture to a new use case may reduce the perceived novelty of the work, as the contribution could be seen as incremental rather than groundbreaking.(see more details at questions)

### Questions
1. Could the authors provide a detailed comparison of system performance, specifically two graphs/tables maximum throughput and latency's relation on one/multiple GPUs, between the hybrid model, Transformer-based model, and Mamba-based model at a similar parameter size? This would give readers a clearer understanding of the efficiency gains and trade-offs associated with the proposed hybrid architecture.

2. I wonder if the authors could further emphasize the differences—such as model architecture, training methods, and other relevant aspects—between this work and Jamba, as well as other hybrid structured models, to better highlight the novelty of this paper.

### Soundness
3

### Presentation
3

### Contribution
2
