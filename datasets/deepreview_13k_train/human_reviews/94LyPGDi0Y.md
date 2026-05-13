# On Pre-training of Multimodal Language Models Customized for Chart Understanding

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Recent studies customizing Multimodal Large Language Models~(MLLMs) for domain-specific tasks have yielded promising results, especially in the field of scientific chart comprehension.
These studies generally utilize visual instruction tuning with specialized datasets to enhance question and answer~(QA) accuracy within the chart domain.
However, they often neglect the fundamental discrepancy between natural image-caption pre-training data and digital chart image-QA data, particularly in the models' capacity to extract underlying numeric values from charts.
This paper tackles this oversight by exploring the training processes necessary to improve MLLMs' comprehension of charts.
We present three key findings: (1)~Incorporating raw data values in alignment pre-training markedly improves comprehension of chart data.
(2)~Replacing images with their textual representation randomly during end-to-end fine-tuning transfer the language reasoning capability to chart interpretation skills.
(3)~Requiring the model to first extract the underlying chart data and then answer the question in the fine-tuning can further improve the accuracy.
Consequently, we introduce \ours, an MLLM tailored for in-depth chart comprehension.
\ours effectively interprets various types of charts, including unannotated ones, while maintaining robust reasoning abilities.
Furthermore, we establish a new benchmark to evaluate MLLMs' understanding of different chart types across various comprehension levels.
Experimental results show that \ours exhibits strong performance in understanding both annotated and unannotated charts across a wide range of types.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a pipeline to create a comprehensive dataset for fine-tuning the proposed MLLM, CHOPINLLM for chart understanding. It highlights that incorporating raw data values during pre-training, substituting images with textual data in fine-tuning, and prioritizing data extraction before answering questions significantly improve performance. Additionally, a benchmark dataset is developed to evaluate MLLMs’ comprehension of various chart types across different complexity levels.

### Strengths
1. The paper introduces efficient training techniques that significantly enhance chart comprehension.
2. CHOPINLLM, a model for chart understanding, demonstrates strong performance with various chart types.
3. A benchmark is established to evaluate MLLMs' comprehension of different chart types, aiding future research.
4. The data generation pipeline uses text-only Large Language Models to efficiently create diverse datasets, reducing costs and complexity.

### Weaknesses
1. CHOPINLLM did not achieve state-of-the-art (SOTA) performance in Table 4. While the authors claim that higher-performing models benefited from using more data and annotated datasets, there is no evidence showing that the proposed synthetic data offers performance gains when combined with existing datasets. Demonstrating that such a combination improves results would strengthen the contribution of the synthetic data. Otherwise, the benefit of using only synthetic data to build an underperforming model appears limited. (this is my major concern)
2. The paper lacks comparisons with a broader range of SOTA MLLMs that are not specifically tailored for chart understanding, such as InternVL2 and Phi-3.5-V.
3. It omits comparisons with proprietary SOTA models like GPT-4o and Claude-3.5-Sonnet, which would help illustrate performance differences between open-source and proprietary models.

### Questions
In addition to the weaknesses:

1. What is the difference between annotated data and synthetic data that could be the major cause of the performance gap between CHOPINLLM and ChartAst-13B? What challenges exist in create synthetic data in comparable quality? 
2. Can the data generation method be generalized to other domains where annotated data is harder to obtain? Demonstrating this would help justify the advantage of using only synthetic data for training and emphasize its broader applicability.

### Soundness
2

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
The paper investigates the design space of chart understanding pretraining of multimodal LLMs along with a fully automatic synthetic data generation pipeline to resemble real-world charts. The resulting model, ChopinLLM, when pretrained on a mixture of LLaVA pretraining data and the synthetic data and fine-tuned on a mixture of LLaVA QAs and the synthetic QAs, achieves competitive performance on its own chart understanding benchmark and decent performance on a variety of other chart understanding benchmarks. The authors well documented the data generation pipeline and mappings between data usage at different stages and model performance.

### Strengths
- Investigating ways to improve chart understanding of MLLMs from the “pretraining” (e.g., aligning the connector with captioning data) perspective is rarely explored, which sets this work apart from others that focus on chart understanding in supervised finetuning of the full model on chart QAs. Experiments demonstrate that having a curated chart understanding dataset for pretraining can significantly enhance the model’s performance when later supervised finetuned on the same set of visual QA dataset.
- The paper is clearly written and examples of data and the data curation process are well documented in the supplementary materials.
- The experiments on the effectiveness of different types of chart understanding data are well investigated, where the major contribution factor toward the performance boost is to learn to translate the entire chart into textual data sources and learn to use the pattern for inference.

### Weaknesses
 - A main argument from the paper seems to be that existing models could learn a shortcut that uses chart annotations to analyze the chart and answer questions (L73), while your methods result in a model that has less reliance (L478). Yet, there are no controlled experiments from the paper to support either claim.
- Lack of discussions and/or ablations on the effectiveness of orthogonal data and code generation compared to first generate the data then code. Generating code without knowing the data distribution/patterns limits the variations of the charts and may also create suboptimal layout of the charts. For example, if the data generator chooses to generate data that grows exponentially while the code generator chooses to create the corresponding axis in a linear scale, this can make the plot look awkward and it will also be hard to learn/interpret data from both human/model’s perspective. Some discussion and experiments on these scenarios (and how they could affect training) would be beneficial.
- Cost-effectiveness of data in terms of training is rarely discussed or compared with. While authors proposed a data pipeline that is cost-effective in synthesis, how much a fixed amount of data (or a fixed amount of compute) helps models learn chart understanding is not ablated. For example, when reducing ChartAst’s data to 5M, does model trained on your data perform better? Similarly, you can also reduce the amount of your training data to match the amount in ChartLlama, MMC or ChartInstruct and compare the performance.
- Adding chart-specific data to the pertaining dataset makes chart understanding data over-represented. As most multimodal LLMs tend to be used to solve a diverse range of tasks (i.e., not limited to chart understanding), it is unknown if such data imbalance affects models’ performance on other tasks that require visual perception and reasoning.
- I noticed that the most significant improvement of the performance on your benchmark happens when you add the same types of questions in stage-2 training, yet the performance gain on ChartQA is very small — which could indicate that your literal/inferential/reasoning QAs have a narrow and biased distribution. From a benchmarking perspective, this means that someone can easily gain huge performance boost by scaling up the amount of synthetic data under this distribution (which is easy to scale and can be fully automated as you documented), yet the models’ utility in real-world chart understanding can still remain low. I wonder if authors can provide some discussions on the validity of the numbers reported from your benchmark in terms of real-world chart understanding utility.

### Questions
- Line 300: The reference seems to be wrong (should be section C instead of 3.3?).
- Line 274: The “chart variation” terminology can be misleading without reading additional context e.g., it refers to having multiple styles of chart for the same data instead of the visual diversity of the charts. 
- Line 478: I wonder if a formal ablation is conducted with respect to reliance on numerical annotations. A stronger performance on unannotated chart images does not necessarily indicate that the model doesn’t rely on numerical annotations. There are many possible reasons, such as questions on unannotated chart images tend to be easier, etc. A formal controlled study is warranted for the suggestion that your methods rely less on numerical annotations compared to a well-controlled baseline.
- LLaVA 1.5 only supports resolution up to 336^2. Have you considered the resolution bottleneck for your training experiments and evaluations. Does training on your data become more effective if you scale up the training resolution?
- Line 522: there is one typo.
- Line 342: I interpret Data-driven QAs as the finetuning data for model to generate the JSON before giving the answer, and Data Prompting is a natural language prompt applied during inference time to elicit generation of the JSON before giving the answer. Is my interpretation correct? Does the model generate the JSON when there is no explicit prompting but when there are data-driven QAs?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
To enhance MLLM's ability to understand charts, the authors propose a process for generating charts and QA data and create a large training dataset. Based on this data, they introduce CHOPINLLM, a fine-tuned LLaVA-like model. Additionally, they propose a benchmark to evaluate the model's performance.

### Strengths
1. The authors present a clear and easy-to-understand workflow.
2. They provide a Chart instruction dataset that includes raw data and QA. The dataset creation process and its characteristics are well explained.
3. The authors offer a comprehensive summary and recommendations regarding MLLM training in the chart domain, particularly on instruction data selection and mixing.

### Weaknesses
1. Training aligned with raw data is already widely adopted (e.g., ChartAst, ChartReformer). Similarly, extracting chart data before QA has been explored (e.g., OneChart). 
2. The authors emphasize that their model handles unannotated charts well, but there is no specific design for addressing it. Furthermore, results on unannotated charts are not provided. Benchmarked datasets like PlotQA are overly simple and repetitive, while others such as MMC, ChartBench, and ChartX (all are provided in Table 1) include higher-quality unannotated charts and QA, yet the authors do not report results on them.
3. Although the authors claim their method is MLLM-based fine-tuning, it’s unclear which base model they fine-tuned, making it difficult to evaluate the effectiveness of their data and training approach.
4. The experimental comparisons are insufficient. Some recent works like TinyChart, OneChart, and those mentioned in related works (e.g., ChartGemma) are not included in the comparative tables. Based on the numbers reported in those papers, CHOPINLLM’s results do not appear to be significant.

### Questions
1. The motivation for introducing the benchmark is unclear, as it appears similar in structure and evaluation to MMC without offering additional insights or conclusions.
2. The introduction needs smoother transitions; while the motivation and insights are understandable, it is difficult to follow how the problem is specifically addressed.
3. The authors should better clarify their contributions. While the workload is evident, the innovation is not, making the paper feel more like a technical report. For instance, if one contribution is the training method, does it generalize to other MLLMs like LLaVA, InternXC, Qwen, etc.?
4. After training heavily on chart-specific data, does the model's performance on other MLLM tasks (e.g., those in MME or SEED) degrade? How did the authors balance these aspects? Or is CHOPINLLM solely focused on chart-based QA?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new Multimodal Large Language Model (MLLM), named CHOPINLLM, designed to enhance chart comprehension, especially in scientific and complex data visualizations. The model is tailored to bridge the gap between typical image-caption training data and chart-specific data, aiming to improve MLLM capabilities in extracting underlying numeric values from both annotated and unannotated charts. Furthermore, the paper also introduces a novel data generation pipeline to automaticaly produce large-scale pairwise data about chart understanding tasks. Finally, the paper construct a new benchmark comprising a diverse array of chart types and question-answering levels for robustly evaluate the chart understanding capabilities of MLLMs.

### Strengths
**Relevance**: The paper addresses a important task in MLLMs (Chart Understanding). The paper should be of interest that transcends the vision & language community to the broader research community.

**Novelty**: 

- **Innovative Training Techniques**: The paper pioneers a set of training strategies (Three stages), notably using raw data in visual-language alignment, integrating text-only chart representations, and data-first reasoning in Q&A. These approaches contribute to making CHOPINLLM more adept at extracting and interpreting unannotated chart data, a significant advance over existing methods.
- **Data Generation Pipeline**: The paper propose a data generation pipeline, which addresses the challenge of obtaining diverse and high-quality chart data by using automated processes involving language models like GPT-4, which generate both the raw chart data and the Python code to produce chart images. 

**Significance**:  This paper introduces a novel approach to training MLLMs, enabling accurate comprehension and reasoning over complex, unannotated charts, which significantly advances AI's ability to autonomously interpret data visualizations.

### Weaknesses
My primary concern about this paper is the performance of CHOPINLLM in chart understanding:

**Baselines**: This paper uses ChartAst [1] as its primary baseline. However, some baselines, such as TinyChart [2], ChartGemma[3], etc are being ignored. After going through and comparing these baselines on Chart QA, I don't find a significant performance advantage with CHOPINLLM. 

**General MLLMs:** I don't get the practical significance of CHOPINLLM, the paper trained an MLLM by proposing a complex THREE STAGES TRAINING STRATEGY. For Stage 1, it's common to add CHART DATA to the image-text pair alignment stage, which has been used by several general MLLMs, e.g., LLama 3[4]. In Stages 2 and 3 (visual instruction tuning), adding chart QA data, cf. the above baselines is common. Therefore, I don't understand the significance of Contribution 1 shown in the Paper. 

**Data Generation Pipeline:** By comparing with TinyChart, the automated pipeline proposed in the paper generates 5M of synthetic data, but the synthetic data generated by TinyChart is about 1M, and there is a big gap between the two in terms of performance on ChartQA (71.39 vs 82.88). This makes it hard to convince me that the data generation pipeline proposed in the paper is more efficient.

### Questions
Please see my feedback and suggestions above. I think the benchmark for CHART UNDERSTANDING presented in the paper is something that does promote the field, but for the first two contributions in the article, I don't see the obvious significance.

### Soundness
3

### Presentation
3

### Contribution
3
