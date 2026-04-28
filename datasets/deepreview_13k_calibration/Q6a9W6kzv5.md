# PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
Understanding the physical world is a fundamental challenge in embodied AI, critical for enabling agents to perform complex tasks and operate safely in real-world environments. While Vision-Language Models (VLMs) have shown great promise in reasoning and task planning for embodied agents, their ability to comprehend physical phenomena remains extremely limited.
To close this gap, we introduce PhysBench, a comprehensive benchmark designed to evaluate VLMs' physical world understanding capability across a diverse set of tasks. 
PhysBench contains 100,000 entries of interleaved video-image-text data, categorized into four major domains: physical object properties, physical object relationships, physical scene understanding, and physics-based dynamics, further divided into 19 subclasses and 8 distinct capability dimensions.
Our extensive experiments, conducted on 39 representative VLMs, reveal that while these models excel in common-sense reasoning, they struggle with understanding the physical world---likely due to the absence of physical knowledge in their training data and the lack of embedded physical priors.
To tackle the shortfall, we introduce PhysAgent, a novel framework that combines the generalization strengths of VLMs with the specialized expertise of vision models, significantly enhancing VLMs' physical understanding across a variety of tasks, including an 18.4\% improvement on GPT-4o.
Furthermore, our results demonstrate that enhancing VLMs’ physical world understanding capabilities can significantly help the deployment of embodied agents, pushing the boundaries of machine intelligence in comprehending and interacting with the physical world. We believe that PhysBench and PhysAgent offer valuable insights and contribute to bridging the gap between VLMs and physical world understanding. Project site: [https://anoy1314.github.io/](https://anoy1314.github.io/)

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a comprehensive benchmark for evaluating VLMs for physical world understanding. The authors identify four major dimensions comprising of Object Property, Object Relationships, Scene Understanding, and Dynamics and create 100k entries covering these categories. Further, the paper introduces PhysAgent as a solution to aid VLMs in gaining physical world understanding which improves performance for Embodied AI applications as well.

### Strengths
- Paper identifies key issue of missing physical world understanding in VLMs and release a comprehensive benchmark for evaluation and training (Table-1).
- Fig.4 experiment explains the difference of physical world understanding against the common VQA benchmarks which is very insightful.
- The method PhysAgent reuses existing foundation models and gains a shows a significant performance boost on the benchmark.
- The cross-task ability of PhysBench for embodied AI makes the benchmark very useful.

### Weaknesses
 - The test set of PhysBench is derived from the similar set of images as train. This ensures that any fine-tuning would result in performance improvement. Did the authors test PhysAgent against out of distribution images that are labeled for physical undersatnding?
- L443: 'PhysAgent first classifies the question and activaets task-specific prompts'. Does that mean that PhysAgent is dataset dependent? Also, how does it support the claim made at L90 "PhysAgent retrains the strong generalization abilities of VLMs and their capacity to solve open-ended problems"? It would be good to see an experiment supporting the L90 claim in the paper.
- Nit: The appendix should have been kept concise. I appreciate the details but a concise appendix makes it more approachable.

### Questions
- Is the PhysAgent using the DepthAnything, SAM and DINO outputs as input to LLMs or these individual model's outputs are used to get a textual insight which is the sole input to VLMs?
- Please refer to weakness section. I am open for discussion and changing my score.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors collect a human-annotated dataset to test physical reasoning in MLMs. They demonstrate that MLMs struggle to reason about physics in images by showing a gap between human and MLM performance. They further collect annotations to analyze why MLMs fail and identify perceptual errors and a lack of knowledge as the main reasons why they fail. Then, they incorporate some specialist vision models to infer depth, objects, etc., to further help the MLMs and show improved performance. They finally show that fine-tuning on their benchmark also helps an object manipulation task in simulation.

### Strengths
- The topic is very relevant and interesting since numerous works also show that MLMs lack spatial and physical reasoning and these are crucial skills for embodied AI. 
- Their dataset seems varied and tests a lot of fundamental physical skills. 
- The annotation of why MLMs are failing is interesting. 
- The fact that PhysBench fine-tuning helps an object manipulation task is a good way to show that physical reasoning helps downstream applications.

### Weaknesses
 - I am a bit confused about the correlation matrix in Figure 4a.  I am assuming the last 4 rows are PhysBench splits? In that case, the bottom right half seems to indicate that that performance on their benchmark doesn't correlate on the other existing VLM benchmarks (since the left part of the bottom 4 rows are blue). This can imply improving on their benchmark doesn't improve on other vision-language benchmarks? I am also not sure what part of that figure to look at for their claim in Section 3,4 that their benchmark is correlated to MMMU.

- More details on the PhysAgent would have been helpful. What is the base model for PhysAgent - is it an MLM? If so, which one? They outline a 3-step pipeline:
    1. asking task-specific prompts: How does it learn to ask these questions? Is it tuned to do so or in-context? If so, how is the tuning done? 
    2. Incorporating VLM predictions: How exactly do they incorporate depth, grounding etc? The figure 8 and supplementary makes it seem like a  JSON-like format or a list. Where does the knowledge memory come from? Can the PhysAgent interpret such a format without any fine-tuning?
    3. How is PhysAgent prompted to do COT? Does it do it zero-shot or, is it taught to do the chain of thought using some training examples? If so, how are the COT training examples made?

- The results in Table 9 are confusing - what the individual columns? They do not match the names with the splits in PhysBench in Table 3. PhysAgent improves on PhysBench, but does it at least retain performance on some other similar benchmarks?

### Questions
See weaknesses. 

I like the direction of the paper and believe the benchmark would be impactful. However, the details presented are not clear. Hence, I will be willing to increase my score if the authors can clarify my doubts above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a large-scale benchmark to evaluate VLMs' capability to understand the physical world. The benchmark covers diverse domains such as daily life images and videos, robot manipulation, and autonomous driving. The benchmark takes thousands of hours for data annotation and multi-round quality review, ensuring quality. The extensive experiments test 39 representative VLMs and reveal the limitations of such models' abilities to understand the physical world. To enhance VLMs' physical world understanding abilities, the authors propose a unified approach named PhysAgent to leverage visual foundation models into a chain-of-thought protocol. Since there are existing works that aim at evaluating VLMs' ability in spatial reasoning and physical common senses, this paper claims that the benchmark can enhance the VLMs' abilities on embodied tasks. However, the experiments on embodied tasks are very limited and unfair in demonstrating the role of this benchmark in the era of VLA models.
In summary, the paper proposes an important benchmark and proposes a large-scale, diverse, and high-quality benchmark to evaluate VLMs' abilities to understand the physical world. The authors also propose a new framework to enhance VLMs' performance on this benchmark.

### Strengths
1. Dataset Scale and Quality: The scale and quality of the dataset are promising. The paper provides thorough details regarding data annotation and quality control processes, which enhance the benchmark's credibility and reliability.
2. Scalability and Error Analysis: The paper offers valuable insights by analyzing the scalability of the model, data, and framework. Notably, it presents an in-depth examination of error types encountered by commercial VLMs on the benchmark, which is critical for advancing the development of VLMs.
3. Impact of Fine-tuning: The results demonstrate that fine-tuning on a subset of PhysBench significantly improves performance on embodied tasks compared to the zero-shot performance of the PhysAgent framework, highlighting the value of task-specific adaptation.

### Weaknesses
1. Discussion of Related Work: The paper lacks a comprehensive discussion of related works. The proposed benchmark aims to evaluate and enhance the ability of VLMs to understand the physical world at both the object and scene levels. However, it is crucial to emphasize that understanding 3D spatial relationships at the scene level is a fundamental capability for VLMs. To strengthen the discussion, the authors should compare this work with other 3D spatial VQA benchmarks such as SQA3D [1], OpenEQA [2], EmbodiedScan [3], MMScan [4], and MSQA [5]. These benchmarks offer direct evaluations of VLMs’ understanding of 3D scenes through interleaved 2D or 3D representations, providing valuable context and highlighting gaps or overlaps with the proposed approach.

2. Comparison of Embodied Tasks: The comparison between zero-shot models (such as existing VLMs and PhysAgent) and fine-tuned models trained on PhysBench raises concerns about fairness. PhysBench, in its current form, is relatively simplistic and may not provide a robust or balanced evaluation. To ensure fair comparisons, the authors should either (1) incorporate more challenging tasks or datasets in PhysBench to match the capabilities of fine-tuned models, or (2) highlight the limitations of comparing zero-shot performance with fine-tuned results to avoid misleading conclusions.

### Questions
I appreciate the authors' efforts in developing a benchmark for physical world understanding and evaluating its impact on embodied agents. Recently, several open-source VLA models have emerged, such as OpenVLA [1], Embodied-COT [2], and Octo [3]. Did the authors consider comparing the fine-tuned VLMs with other VLA models on the proposed manipulation tasks? Additionally, is there a way to assess the benchmark’s role in advancing the development of VLA models? Such comparisons and evaluations would further highlight the benchmark’s contribution to the field.

[1] OpenVLA: An Open-Source Vision-Language-Action Model

[2] Robotic Control via Embodied Chain-of-Thought Reasoning

[3] Octo: An Open-Source Generalist Robot Policy

### Soundness
3

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
4

### Summary
The work proposes PhysBench, which serves as a comprehensive benchmark to evaluate VLM's understanding of physics. PhysBench mainly includes four types of physical questions: Property, Relations, Scene, and Dynamics, and each type has many sub-classes, resulting in 19 different tasks. The work also proposes PhysAgent to improve VLM's ability of physical reasoning.

### Strengths
- Compared to all previous works on physical reasoning benchmarks, this dataset is the most comprehensive one to my knowledge. PhysBench includes many different types, which can well evaluate VLM's general physical understanding ability.

- The data sources for videos are various, instead of mainly simulation-based generation. This can further diversify the video data if the dataset has been well-cleaned and filtered. 

- Experiments are also extensive, which are conducted across 39 VLMs. The authors also well analyze the reasons why VLMs are still struggling with physical reasoning.

- Further experiments on the transferability of real-world tasks are sound.

### Weaknesses
 - The article is quite lengthy, so it is really important to improve its logical flow to enhance readability. Using appropriate formatting elements, such as bold text for key points, can help guide readers through the content and make it easier for them to locate the information they are looking for. It is difficult for me to find my questions when reading this paper. 

- There is a lack of consistency in the article's formatting. For example, task names are referred to in multiple ways, and similar tables or images are styled differently across various sections, which may confuse readers. Specifically, Table 9a labels the four main types as Property/Spatial/Envir./Phe., whereas other sections refer to them as Property/Relations/Scene/Dynamics. Are they describing the same thing? Also, styles for Tab 16-20 are different, and what is the last column of Tab 20? The labels above Figure 4 are misaligned with the ticks, and extra ticks appear at the bottom. I believe these ticks should likely be placed on the left side instead. It is better to re-organize the whole paper.

- How do questions design for each video? The paper mentions, "For videos annotated with physical principles, we generate physics-related questions using both manual design and GPT-4o, following predefined rules.". But I cannot find further details on it. What are the question templates? How do humans design questions? What is the procedure of question generation by GPT-4o? The authors may comment on more details on this matter. 

- How is the human evaluation in Tab 3 (or other possible places) conducted? Also, how do human annotators contribute to the dataset? I can only find the GUI description for this matter. The authors may comment on more details, such as how many people are engaging in each part and so on. 

- What is the detailed performance on 19 tasks among PhysAgent and baselines of Fig 9a, since the distribution of the dataset is not balanced.

### Questions
- Are there any reasoning steps included in each question?

### Soundness
4

### Presentation
2

### Contribution
4
