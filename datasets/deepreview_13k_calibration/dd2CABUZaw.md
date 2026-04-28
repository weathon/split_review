# ChartBench: A Benchmark for Complex Visual Reasoning in Charts

- Decision: Reject
- Avg Score: 5.80
- Scores: 5, 6, 6, 6, 6

## Abstract
Multimodal Large Language Models (MLLMs) have shown impressive capabilities in image understanding and generation. However, current benchmarks fail to accurately evaluate the chart comprehension of MLLMs due to limited chart types and inappropriate metrics. To address this, we propose ChartBench, a comprehensive benchmark designed to assess chart comprehension and data reliability through complex visual reasoning. ChartBench includes 42 categories, 66.6k charts, and 600k question-answer pairs. Notably, many charts lack data point annotations, which requires MLLMs to derive values similar to human understanding by leveraging inherent chart elements such as color, legends, and coordinate systems. We also design an enhanced evaluation metric, \textit{Acc+}, to evaluate MLLMs without extensive manual or costly LLM-based evaluations. Furthermore, we propose two baselines based on the chain of thought and supervised fine-tuning to improve model performance on unannotated charts. Extensive experimental evaluations of 18 open-sourced and 3 proprietary MLLMs reveal their limitations in chart comprehension and offer valuable insights for further research. Code and dataset are publicly available at {\url{https://chartbench.io}}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The ChartBench benchmark addresses limitations in existing MLLMs’ chart comprehension by introducing a dataset with 42 chart types across 66.6k charts and 600k question-answer pairs. This benchmark requires models to interpret chart elements (e.g., color, legends, coordinate systems) without relying on data point annotations. ChartBench also introduces the Acc++ metric, designed to prevent models from making correct answers based on chance, by introducing similar query structures with slight variances in values. Two baseline approaches are presented to improve model performance on these complex, unannotated charts.

### Strengths
1. The benchmark includes a wide array of chart types beyond conventional bar and line charts, enhancing its utility for complex visual reasoning evaluation.

2. Acc++ mitigates the limitations of earlier metrics by reducing model reliance on chance, providing a refined tool for measuring comprehension accuracy.

3. Baseline Models and Task Variety: The paper provides two baseline models based on chain-of-thought and supervised fine-tuning, which effectively highlight the limitations in current MLLMs’ performance when applied to unannotated chart reasoning tasks.

### Weaknesses
1. The value extraction metric based on Acc++ does not make sense. Since the metadata has the full CSV annotation of the chart data, an effective method to evaluate the ability of MLLMs should be the comprehensive recognition of all elements in the chart. A binary classification for the value extraction task cannot fully demonstrate the visual understanding capability of MLLMs.

2. The template-based generation of instruction data somehow lacks diversity. As illustrated in Figure 3(c), the distribution difference between ChartBench and other benchmarks is less significant than the other two dimensions.

3. The generation pipeline of ChartBench lacks sufficient novelty compared with other benchmarks, e.g., ChartX.

### Questions
1. In Table 1, ChartX also seems to be visually grounded. Could you further check it?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper makes several contributions to the field of chart understanding in VLMs. The introduction of ChartBench represents a substantial advancement in benchmarking capabilities. Its comprehensive coverage of 42 chart types, 66k charts, and 600k instruction pairs significantly expands upon existing benchmarks such as ChartQA, MMC, ChartX, etc. What sets ChartBench apart is its emphasis on unannotated charts, which forces models to rely on visual reasoning through elements like colors, legends, and coordinate systems rather than simple OCR - a scenario more aligned with real-world applications.

The authors' refinement of the evaluation metric, introducing ACC++, bridges the gap between existing assessment methods. By generating negative queries through random value substitution from the same meta table, they've developed a more robust evaluation system that effectively reduces the likelihood of lucky guesses. 

The paper also contributes through two baseline methods: chain of thought and supervised fine-tuning. These approaches provide a foundation for improving models' understanding of unannotated charts, offering valuable insights for future research directions. The extensive experimental evaluation, covering 18 open-source and three closed-source models, provides comprehensive insights into the current limitations of VLMs in chart comprehension.

### Strengths
1. This paper is well-structured and presented, with a logical flow that makes it accessible to readers across different expertise levels.
2. The paper's major contribution lies in its comprehensive dataset construction. The inclusion of 9 major categories and 42 subcategories of charts represents an advancement in chart understanding. This extensive coverage substantially surpasses existing benchmarks and provides a more realistic evaluation framework for VLMs.

### Weaknesses
Besides the strength, I find several aspects of this paper warrant discussion.

1. While the work expands the range of chart types and introduces the ACC++ evaluation metric, the technical innovation appears somewhat limited beyond these contributions. This raises questions about the proposed benchmark's overall novelty.
2. A more fundamental concern relates to the dataset generation approach. The authors utilize standard chart plotting libraries, which generate relatively straightforward visualizations. However, real-world charts and infographics often feature sophisticated design elements and custom modifications. This disparity raises essential questions about the dataset's representativeness and alignment with actual chart distributions encountered in practice.
3. The core challenge in understanding tasks, particularly chart comprehension, lies in generalization capabilities. The sustantial gap between synthetic and real data distribution poses a critical question: Can the robust generalization abilities of VLMs effectively bridge this gap? The heavy reliance on synthetic data potentially diminishes the benchmark's effectiveness in evaluating real-world performance.
4. To address these concerns, I recommend incorporating additional experiments that demonstrate the practical utility of this work. Specifically, experiments showing how models trained on ChartBench's synthetic data perform on real-world charts would be valuable. Such experiments would help validate whether the synthetic training data enhances models' ability to tackle real-world chart understanding problems.
5. Some personal opinions:
	- a. The baseline models should be more systematically categorized. Specialized models optimized for OCR and document understanding (like mPLUG-Owl and DocOwl) warrant separate evaluation from general-purpose VLMs (such as Qwen-VL).
	- b. the experimental evaluation would be more comprehensive with the inclusion of *recent* top-tier VLMs like InternVL

### Questions
Please check previous sections

### Soundness
3

### Presentation
4

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
This paper introduce a large-scale dataset, which contains over 66,000 charts across 42 different types and 600k qa pairs, without data point annotations, which requires models to derive values through visual elements like colors, legends, and coordinate systems . The benchmark introduces an enhanced evaluation metric called Acc++ to assess models' true understanding while avoiding lucky guesses. The paper also provides valuable baselines through Chain-of-Thought (CoT) and supervised fine-tuning approaches  to improve model performance on unannotated charts.

### Strengths
1、By introducing a large-scale dataset with unannotated charts, this work advances visual understanding research that more closely aligns with real-world applications.

2、The proposed strategies of CoT and SFT are effective in the tasks.

3、The experiment of the paper is comprehensive.

### Weaknesses
1、There seems to be little innovation or discovery in this pipeline, the proposed baseline methods (Chain-of-Thought and supervised fine-tuning) are well-established techniques in the field.

2、How does the data generation pipeline differ from other chart-related datasets?

3、Have you considered testing the models' generalization ability on charts from completely different domains or visual styles not present in the training data?

4、Some recent strong baseline models do not appear to have been evaluated，such as InternVL2、Qwen-VL2.

### Questions
Please see Weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses an important gap in multimodal evaluation by introducing ChartBench, a large-scale chart comprehension benchmark.  The benchmark encompasses more diverse chart types than existing data, covering both annotated and unannotated charts. The authors also refine the Acc+ metric, enabling efficient and stricter evaluation. The authors conduct comprehensive evaluations using various models and provide detailed analysis of the results.

### Strengths
- The authors focus on an important aspect MLLM evaluation that existing works lack, and address the problem by proposing a new dataset covering more diverse chart types
- The authors conduct thorough evaluations using various MLLMs on different chart version - the effort is noteworthy. The insightful analysis on model performances also provides valuable insights of capabilities and limitations of current models. 
- The authors also enhance the existing Acc+ metrics by proposing Acc++, making the metric more robust.

### Weaknesses
 - I'm not fully convinced that the designed question types and data collection methods are substantially different compared to existing works. It would be nice to see some arguments on why evaluating on this benchmark substantially address the limitations of existing datasets.


### Questions
- How evaluating on this benchmark directly address the limitations on existing datasets? For example, any side-by-side comparison examples?
- Is there any effort in ensuring that the collected questions/instructions is diverse?
- Since the benchmark is relatively large, any comments on the compute/time resources required to conduct the evaluation? Are there any potential subsets that could be representative in any way of the full dataset?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents ChartBench, a chart-related benchmark that is created to evaluate the chart comprehension abilities of the existing VLM models. It comprises 42 categories, 66.6K charts, and 600K question-answer pairs, with a focus on complex visual reasoning, especially for charts without data point annotations. Besides, the authors introduce an evaluation metric, Acc++, to accurately evaluate the performance of VLM models. Experiments are conducted on the proposed ChartBench and ChartQA datasets to show the effectiveness of the proposed dataset and the chain of thought and supervised fine-tuning baselines.

### Strengths
- ChartBench contains a vast amount of visual chart data and chart QA data. 

- This manuscript is well-organized and well-presented. Besides, the appendix of this paper is also well-written, showcasing numerous visual examples, quality inspection, additional experimental results and analyses, making the content comprehensive.

- The authors employ 200 question templates when constructing QA pairs to ensure diversity, which is an advantage.

### Weaknesses
 - 1) This work is clearly written and organized, but I feel that its biggest drawback is its technical contribution: a) The Acc++ proposed in this paper mainly derives from MME's Acc+, and the main difference between Acc+ and Acc++ lies in the random replacement of the ground truth. I feel that the improvement seems insufficient to serve as a standalone technical contribution for ICLR submission; b) The chain of thought and supervised fine-tuning baselines proposed by the authors are also common techniques in LLM and VLM community, and please provide the detailed comparisons and design considerations between state-of-the-art techniques and the proposed chain of thought or supervised fine-tuning baselines during the rebuttal period.

- 2) The authors emphasize that the chart dataset they constructed does not have data point annotations. However, I believe that data point annotations for chart-related tasks are important, due to the following reasons: a) Data point annotations can serve as auxiliary information for QA tasks, thereby improving the interpretability of QA task predictions; b) Data point annotations can facilitate research on chart information extraction tasks, such as the recent GOT [Ref A]. Please explain the reason for excluding data point annotations.

- 3) Considering that the authors reported the results on ChartQA dataset, it is necessary to validate the effectiveness of the proposed ChartBench **training set** on the ChartQA dataset. For example, you could conduct an additional experiment by comparing a selected VLM (such as InternLM-XComposer-V2) and the VLM fine-tuned your proposed training set (such as InternLM-XComposer-V2 fine-tuned results), and the models should be tested on ChartQA testset as reported in Table 3.

- 4) It is recommended to include some of the latest work on VLM models for comparison in Tables 3 and 4, such as Qwen2-VL, or DeepSeek-VL, etc.

- 5) It is suggested to discuss the usefulness of the ChartBench dataset in real-world scenarios, such as in time series prediction tasks.

### Questions
- 1) By observing Figure 3, there is a significant difference in the distribution of charts, CSVs, and queries between ChartBench and ChartQA. Is this difference due to the fact that the ChartBench dataset is primarily simulation-based? Please explain this reason during the rebuttal.

### Soundness
3

### Presentation
3

### Contribution
2
