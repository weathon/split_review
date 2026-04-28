# MMFakeBench: A Mixed-Source Multimodal Misinformation Detection Benchmark for LVLMs

- Decision: Accept
- Avg Score: 6.60
- Scores: 8, 6, 6, 5, 8

## Abstract
Current multimodal misinformation detection (MMD) methods often assume a single source and type of forgery for each sample, which is insufficient for real-world scenarios where multiple forgery sources coexist.
  The lack of a benchmark for mixed-source misinformation has hindered progress in this field. To address this, we introduce MMFakeBench, the first comprehensive benchmark for mixed-source MMD. MMFakeBench includes 3 critical sources: textual veracity distortion, visual veracity distortion, and cross-modal consistency distortion, along with 12 sub-categories of misinformation forgery types. We further conduct an extensive evaluation of 6 prevalent detection methods and 15 large vision-language models (LVLMs) on MMFakeBench under a zero-shot setting. 
  The results indicate that current methods struggle under this challenging and realistic mixed-source MMD setting. Additionally, we propose an innovative unified framework, which integrates rationales, actions, and tool-use capabilities of LVLM agents, significantly enhancing accuracy and generalization.
  We believe this study will catalyze future research into more realistic mixed-source multimodal misinformation and provide a fair evaluation of misinformation detection methods. 
  \label{abstract}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper looks at creating a multimodal misinformation dataset called MMFakeBench that can be used to evaluate detection methods and Large-Vision Models (LVLMs) under a zero-shot setting. For the dataset a validation set is created for hyperparameter selection and also used to conduct a human evaluation of the proposed MMFakeBench dataset. Utilizing the MMFakeBench dataset, 15 LVLMs are evaluated on the test set of the dataset and highlights the shortcomings of these LVLMs when compared to the human evaluation results.

### Strengths
* Utilizing a human evaluation helped strengthen the claim that currently LVLMs models have room for improvement when it comes to tackling the tasks proposed with the MMFakeBench dataset.
* Table 2 was a well thought out table that coverages a wide range of LVLMs
* The proposed dataset is unique as it proposes different tasks related to mixed-source multimodal misinformation detection, as it shows in Table 1 the difference between its dataset and previous multimodal misinformation datasets.

### Weaknesses
 * Currently the dataset size seems somewhat low when comparing it to other datasets mentioned in the paper. However I do recognize that this is specifically meant to be an evaluation dataset.

### Questions
* Can the authors possibly give further examples of evaluation type datasets that look at evaluation in a zero-shot setting for misinformation detection.

### Soundness
3

### Presentation
4

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
This work proposes the first benchmark in mixed-source multimodal misinformation detection (MMD). The authors provide comprehensive evaluations and analysis under the proposed evaluation settings, providing a new baseline for future research.

### Strengths
1. It is important to create such a benchmark and baseline for the detection of multi-source fakes.

2. The proposed three types based on the sources of falsified content are new to the field and technical sound.

3. The designed MMD-Agent is well-designed and novel.

### Weaknesses
1. Lack of comparison with related detection methods: This work includes two detectors within the visual veracity distortion (VDD) field, both relying solely on visual modules for detection. Why not include comparisons with recent methods that integrate both visual and language modules, which are more directly relevant to this research?

2. Insufficient comparison with deepfake detection methods: If "misinformation" encompasses any fake content, it would be beneficial for the authors to compare their method with established deepfake detectors. Given the high profile and potential danger of deepfakes, adding such comparisons would strengthen the paper’s impact and comprehensiveness.

3. Lack of intuitive visualizations for the proposed method: It is recommended that the authors use visualization tools like GradCAM to provide clearer, more intuitive insights into their detection results. Additionally, the current t-SNE visualizations could be improved to more clearly convey their underlying meaning.

### Questions
1. What is the precise scope of this work? For example, does deepfake detection fall within its scope? If so, how does the work address multi-modal detection challenges, such as face reenactment or face swapping?

2. How do Vision-Language Models (VLMs), which incorporate both language and vision modules, perform within the proposed benchmark?

More questions can be seen in the "Weakness" part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce MMFakeBench, presented as a benchmark for evaluating mixed-source multimodal misinformation detection (MMD). They develop a multi-class evaluation metric and conduct evaluations of six state-of-the-art detection methods and 15 large vision-language models on MMFakeBench. Additionally, the authors propose an LVLM-based framework, MMD-Agent, which is intended to enhance detection performance in mixed-source MMD tasks.

### Strengths
The paper offers relatively comprehensive coverage of misinformation types, utilizes a diverse set of detection methods, and includes clear figures explaining the dataset and workflow.

### Weaknesses
1. The contributions of this work are relative limited. Compared to prior benchmarks like DGM4, the primary difference lies in the use of large models to generate data, without introducing novel, highly deceptive misinformation generation methods. Additionally, the proposed MMD-Agent framework contributes minimally to the field, relying heavily on the use of LVLMs.

2. The dataset size is relatively small. While recent benchmarks like DGM4 contain over 200k samples, MMFakeBench includes only about 10k. This raises concerns about whether each misinformation type is represented with enough diversity to support model generalization.

3. It is unclear whether the misinformation types included are meaningful. For example, the Cross-modal Consistency Distortion example in Figure 2 — “An old man reading a book on a park bench” versus “An old man reading a newspaper on a park bench” — lacks practical relevance. Emphasis should be placed on edits involving named entities, such as celebrities, to ensure sufficient impact and deception. Similarly, the Visual Veracity Distortion example with “Veracious Text & AI-generated Image” lacks sufficient misleading potential; the reader’s first impression might be that the image is obviously edited, which fails to show it can lead viewers into perceiving falsified content as authentic.

### Questions
1. For detecting outputs from generative models, a CNN often achieves better detection performance than an LVLM. Consider including performance results using foundation models paired with a fine-tuned network.

2. Some details in Table 1 are unclear. For instance, why do MEIR and DGM4, which involve text editing, lack Textual Veracity Distortion? Edited texts are essentially a type of rumour.

Based on the clarification regarding the proposed dataset as an evaluation resource and the additional explanations provided, I believe you have addressed most of my concerns and I have decided to raise my rating to 6. However, as MMFakeBench is mix-sourced, compared to NewsCLIPpings, which focuses on OOC detection, more data is needed to achieve sufficient diversity and ensure the validity of experimental results. I look forward to your future work.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed a new benchmark of multimodal misinformation detection, and the authors constructed a multimodal misinformation data generation pipeline by integrating characteristics from previous multimodal misinformation benchmarks. Additionally, the authors proposed a novel framework named MMd-Agent, which decomposes the multimodal misinformation detection task into three sub-tasks based on the three critical sources (textual veracity distortion,visual veracity distortion, and cross-modal consistency distortion) identified in this paper and processes them in a step-by-step manner, this method finally achieved good results.

### Strengths
1.	From a mixed-source perspective, this paper proposes a new benchmark for multimodal misinformation detection, addressing some weaknesses in existing datasets.
2.	The authors proposed a novel framework named MMd-Agent, which achieved impressive performance.
3.	The paper is written in an easily understandable manner, and the experimental evaluations are thorough.

### Weaknesses
1.	This paper did not present the existing high-impact multimodal misinformation detection benchmarks or compare them to the proposed benchmark concerning the three critical sources.. Could the authors list some relevant multimodal misinformation benchmarks, multimodal misinformation benchmarks detection methods, and SOTA?
2.	This paper did not present a summary of mainstream methods for detecting multimodal misinformation and summarize the classifications of these methods?
3.	The experimental analysis lacks depth; for example, it only addresses some performance limitations of LLaVA-1.6-34B and GPT (as mentioned in the Error Analysis), while other models are evaluated solely on their performance. I hope the authors can conduct a more thorough analysis of the experimental section and consider analyzing the shortcomings of larger models as well.
4.	The novelty of the proposed MMd-Agent is somewhat limited.

### Questions
1.	What’s the distinction between Natural Rumor and Artificial Rumor? 
2.	Do the definitions of the three critical sources apply to other publicly available datasets?
3.	The generation style of the visual veracity distortion data is relatively uniform. Does this meet the benchmark's intended purpose?
4.	Whether the accuracy of all GPT-generated rumors has been manually verified is necessary.
5.	Has the impact of dataset imbalance (between real and fake, as well as imbalances among different subclasses) been validated? This makes it difficult to reuse the dataset.
6.	The authors should provide further analysis of the experimental results in Figure 5, comparing their performance differences to better illustrate the distinctions between different categories(Natural Rumor, Artificial Rumor and GPT-generated Rumor).
7.	I believe that mixing human-generated and LLM-generated misinformation is very meaningful; however, other datasets, such as Twitter and GossipCop, also contain three critical categories. How are the limitations of the different datasets in Table 1 assessed?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposed MMFakeBench, a benchmark for multimodal disinformation detection from mixed sources. Unlike existing benchmarks focusing on single-source forgery, MMFakeBench approximates the real-world by encompassing three key sources: textual truthfulness distortions, visual truthfulness distortions, and cross-modal consistency distortions. complex disinformation. The benchmark contains 12 sub-categories of forgery types, totaling 3300 samples. The authors evaluate 6 current state-of-the-art detection methods and 15 LVLMs in a zero-shot setting, revealing the challenges faced by current methods in this mixed-source environment. To improve the detection accuracy, they propose MMD-Agent, which is based on the framework of LVLMs and divides the detection process into 2 phases, i.e., Hierarchical decomposition and Integration of internal and external knowledge.

### Strengths
1. Originality: The introduction of MMFakeBench addresses a previously unexplored field of multimodal false information detection, making it more representative of real-world scenarios.

2. Quality: The benchmark is carefully constructed, covering 12 types of forgery under three main categories, providing a robust evaluation platform.

3. Clarity: The structure of the paper is reasonable, and the categories included in the benchmark, the evaluation process, and the explanation of the proposed framework are clear and concise.

4. Significance: By revealing the limitations of current detection methods and proposing new frameworks, the paper has the potential to drive future research and improvement in this field.

### Weaknesses
1. Limited exploration of external knowledge sources: The paper acknowledges that reliance on sources such as Wikipedia is a limitation but can further explore its impact on detection performance and possible solutions.

2. Evaluation depth: Although the paper evaluated multiple models, it mainly focused on the zero-shot setting. If fine-tuning models or more ablation experiments are added, the experimental results may be more convincing.

3. The handling of rumors generated by GPT: The paper points out the challenges of detecting rumors generated by GPT, but further analysis or solutions can be proposed. There is no analysis of why GPT-generated Rumor is closer to Natural Rumor, or in other words, why is GPT-generated Rumor about as difficult to detect as Natural Rumor? After all, Artificial Rumor is also written by humans, so it should be about the same difficulty as Natural Rumor, but the experimental result is that Natural Rumor is the easiest to detect.

4. It is suggested to discuss and compare more related works such as [1] in this paper.

### Questions
1. External knowledge sources: Have you considered other external knowledge bases besides Wikipedia to enhance the detection of complex rumors?

2. Model tuning: Have you attempted to fine tune LVLMs on a subset of MMFakeBench to observe their performance improvement?

3. Practical application: How does MMD Agent perform in real-time detection scenarios? What is its computational requirement?

4. Scalability: Can your method be extended to other modalities, such as audio or video, to address more complex types of false information?

### Soundness
3

### Presentation
4

### Contribution
3
