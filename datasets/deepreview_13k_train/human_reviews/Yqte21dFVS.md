# Evaluating Graphical Perception of Large Multimodal Models

- Decision: Reject
- Scores: 3, 6, 5, 3, 3

## Abstract
Despite the promising results of large multimodal models (LMMs) in various vision-language tasks, recent benchmarks reveal that these models can struggle with low-level chart perception tasks that require precision.
However, since existing benchmarks primarily focus on end tasks that evaluate models' knowledge and reasoning abilities all together, they provide limited fine-grained insights into how the models' perception abilities affect their performance in chart tasks.
To address this gap, we leverage *the theory of graphical perception*, an approach used to study how humans decode visual information encoded on charts and graphs, to develop an evaluation framework for analyzing gaps in LLMs' perception abilities in charts. With automated task generation and response evaluation designs, our framework enables comprehensive and controlled testing of LMMs' graphical perception across diverse chart types, visual elements, and task types.
We apply our framework to evaluate the perception capabilities of state-of-the-art LMMs at three granularity levels (chart, visual element, and pixel). Our findings underscore several critical limitations of current state-of-the-art LMMs, including GPT-4o: their inability to (1) generalize across chart types, (2) understand fundamental visual elements, and (3) cross reference values within a chart.
These insights provide guidance for future improvements in perception abilities of LMMs.
The evaluation framework and labeled data will be publicly available upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This study investigates the graphical element perception capabilities of Multi-modal Language Models (MLLMs) in chart understanding tasks. Through performing evaluations on several top-performing models on the framework, this study finds that these models struggle to generalize in chart-related tasks and even have difficulty understanding basic visual elements in chart. This study also clarifies the direction for future automation in synthesizing relevant visual chart data to improve the graphical perception and general low-level visual reasoning of MLLMs.

### Strengths
1. This paper presents an evaluation framework that conducts a highly detailed analysis and exploration of the reasons why current MLLMs perform poorly on chart-related tasks.  It also offers three interesting insights to guide future improvements of multi-modal large models in chart-related tasks.

2. This paper is well-organized and clearly written. The proposed pipeline data creation approach and the new dataset would benefit further research.

### Weaknesses
1. The paper indeed identifies the deficiencies of MLLMs in understanding table-related capabilities and provides a very detailed analysis. However, I believe that, building on these findings, there should be a deeper exploration into the essence of the holy grail problem—specifically, why MLLMs perform poorly in recognizing visual elements of chart. This could involve further analysis in terms of interpretability, training data, and model architecture. Additionally, this study should propose at least one method for automatically constructing such data to address the issues with MLLMs introduced in this paper.

2. I notice that the paper mentions that an increase in chart visual elements leads to model performance degradation. Could you further explore the impact of reasoning about relationships among multiple visual elements in charts on the performance of MLLMs, as well as their relationship to the understanding of individual visual elements?

### Questions
1. I noticed that the data source includes domains such as sports, news, finance, and health. Do MLLMs perform differently on similar tables across different domains? Additionally, for the same table, do different instructions significantly impact the understanding of these visual elements?

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
3

### Summary
The paper explores chart understanding - one of the pain-points of modern VLMs and proposes a comprehensive evaluation framework, rooted in theory of graphical perception and targeting different levels of perception. The paper tests a mix of open and closed models and concludes that the models struggle with generalization across chart types and element patterns, and imprecisely located important regions related to a query.

### Strengths
- Problem - The problem is intuitively well-known, however there is a lack of benchmarks that target specific failures in understanding versus QA, thus the paper is a significant contribution to the field.
- Diversity of tasks - The tasks cover a wide range of needs and can reasonably be expected to evaluate predicted normal usage.
- Selection of Models - Good mix of open and closed models

### Weaknesses
 - Heavy reliance on GPT for evaluation, especially in an area where LLMs are known to struggle and lack of human evaluation.
- Lack of verification of Vega-Lite outputs, since some existing datasets are known to have wrongly generated charts in them, potentially throwing all subsequent steps under question.
- Lack of case studies, makes it hard for the viewer to understand actual performance of the models.

### Questions
- Have you had a chance to examine the dataset in greater detail, and whether the quality of the samples?
- Any insights on how these findings would translate to real or more complex charts?
- Would you expect any differences in the results when using a more/less popular tool (compared to Vega-Lite)?

### Soundness
3

### Presentation
3

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
This paper argues that existing benchmarks do not provide fine-grained insights into the performance of LMMs on chart-related tasks. To address this, it proposes an evaluation framework with automated task generation and response evaluation. The framework assesses LMMs at the chart, visual element, and pixel levels, revealing certain limitations of current state-of-the-art LMMs.

### Strengths
This paper explores the basic graph perception capabilities of current LMMs and presents several interesting observations. It emphasizes the limitations of current LMMs on simple graph perception tasks and highlights the substantial impact of annotations on model performance.

### Weaknesses
Dataset description: The dataset details are vague; providing more comprehensive statistics would improve clarity.

Limited contribution: Although the paper aims to design the simplest possible tasks for evaluation (line 96-100), prior work (e.g., [1]) already includes similar tasks, such as descriptive questions on information extraction and enumeration. A detailed comparison with other graphical perception benchmarks would clarify the core differences.

Lack of in-depth analysis:
1.In Section 4, the authors mention that “the addition of redundant visual elements often hurts model performance.” This is a counterintuitive yet interesting observation. More experiment analysis is needed to interpret it.

2.The paper underscores the impact of annotation on performance.However, the role of visual elements remains unclear.
It would be insightful if the authors analyzed more samples that are accurately classified without annotation. This may provide more insights into the contributions of various visual elements.

### Questions
refer to weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Propose a benchmark for graphical perception abilities of large multimodal models (LMMs). The benchmark is able to eval LMMs' graphical perception in chart, visual element, and pixel levels.

### Strengths
The paper designed a benchmark, which has source data coupled with code to Generate the chart, enable future research to modify the code for differnt use and benchmarking

The paper systematically answered three research questions:
1. Can LMMs generalize to different chart types, the answer is No. The author also finds that numerical annotations are very important for LMMs to understand charts
2. Can LMMs learn generalizable graphical perception? The answer is No. LMMs merely follow specific and superficial perception patterns for common charts such as scatter and bar
3. Where LLMs bad at pixel-level perception? The answer is that LMMs fail to cross reference the specific values

### Weaknesses
1. The proposed benchmark is toy-level, not diverse enough. Though the authors aim to create a simple benchmark with better flexibility. I am afraid that only limited insights are gained with with new benchmark.
2. All three findings are not surprising, a lot of work in this field has revealed the poor perception of LMMs like MMVP, Blink. It is even harder for LMMs to reason in a Chart.
3. Given the fact that LMMs do not have a vision reasoning capability is so obvious. I think it is more improtant if the authors can come up with some methods to help LMMs with it, like the cross reference problem can be probably solved by some visual-COT methods.

### Questions
In summary, I appreciate the systematically analysis about the chart understanding questions. But given the fact that all findings are not surprising, and also quite explored in the wider vision community, I think the contribution is limited. What's more, apart from those analysis, author do not try anything on solving those problem, this also limits the contribution

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper provides an in-depth evaluation of the LMMs'  graphical perception ability utilizing the theory of graphical perception. They first create a dataset encompassing different types of charts and different questions with the help of GPT4o . Then, they test the SOTA LMMs with the help of an accurate GPT4o evaluation. Their results reveal several limitations, including generalizing across chart types, understanding fundamental visual elements, and reference values within a chart.

### Strengths
1. This paper conducts thorough analyses to assess the impact of various combinations of visual elements, chart types, and annotations on the same data.
2. This paper highlights several limitations of current LMMs and can guide future LMM designs.
3. This paper proves a data generation pipeline that can be applied to generating diverse test cases focusing on different abilities of chart understanding.

### Weaknesses
1. This paper tests only four LMMs. However, these models are trained on different data and resolutions, making a direct comparison impossible. They should evaluate more LMMs to enhance the reliability of their results.

2. Section 5.1 lacks many essential details, such as the threshold used to measure the LMM's ability to correctly identify important chart regions and how to annotate the ground truth region. The method may also have several flaws. For example, the importance of specific regions does not necessarily mean removing them will harm understanding. For instance, you can omit the label 2010 in Figure 4, and people will still understand that the middle bar represents the year 2010. 

3. Although the paper provides some experiment results, this paper gives far more claims than the results can support. For example, in line 289, the paper claims that lightweight LMMs have weaker generalization abilities than larger models when faced with charts lacking explicit numerical cues. However, testing only one lightweight LMM means you cannot guarantee that this result can be generalized to other models.

4. Typo: line 179 LLaVa should be LLaVA.

### Questions
1. How can you combine position, length, and size in a bar chart at line 319? The toy chart is similar to the bar chart  that only uses position and length. Additionally, I couldn't find an example in Figure C2 that demonstrates a chart combining position, length, and size.  
2. In line 414, how do you define the ground truth labeled regions and check whether the model correctly identifies a region? Do you do it by checking IoU above a threshold?
3. In Figure 5, the region containing 0.827 also shows a large correspondence with the response; how can you explain this phenomenon? Is it consistent with your analyses?

### Soundness
2

### Presentation
2

### Contribution
2
