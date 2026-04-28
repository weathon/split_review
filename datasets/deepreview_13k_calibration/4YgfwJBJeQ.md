# StructChart: Perception, Structuring, Reasoning for Visual Chart Understanding

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Charts are common in literature across different scientific fields, conveying rich information easily accessible to readers. Current chart-related tasks focus on either chart perception which refers to extracting information from the visual charts, or performing reasoning given the extracted data, e.g. in a tabular form. In this paper, we aim to establish a unified and label-efficient learning paradigm for joint perception and reasoning tasks, which can be generally applicable to different downstream tasks, beyond the question-answering task as specifically studied in peer works. Specifically, StructChart first reformulates the chart information from the popular tubular form (specifically linearized CSV) to the proposed Structured Triplet Representations (STR), which is more friendly for reducing the task gap between chart perception and reasoning due to the employed structured information extraction for charts. We then propose a Structuring Chart-oriented Representation Metric (SCRM) to quantitatively evaluate the performance for the chart perception task. To enrich the dataset for training, we further explore the possibility of leveraging the Large Language Model (LLM), enhancing the chart diversity in terms of both chart visual style and its statistical information. Extensive experiments are conducted on various chart-related tasks, demonstrating the effectiveness and promising potential for a unified chart perception-reasoning paradigm to push the frontier of chart understanding.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a StructChart methodology for extracting information from visual chart data to enhance downstream perception and reasoning tasks. To achieve this, the authors initially transform the chart data from Linearized Comma-Separated Values Tokens (LCT) into the proposed Structured Triplet Representations (STR), thereby establishing a connection between chart perception and reasoning. To qualitatively evaluate the chart perception tasks, the authors also introduce a Structuring Chart-oriented Representation Metric (SCRM). This metric evaluates the extracted chart data using Intersection over Union (IoU). Additionally, the authors construct a synthetic chart dataset called SimChart9K, which is helpful for downstream tasks. The numerical experiment shows the efficiency of the proposed method. However, I have some concerns about this paper. My detailed comments are as follows.

### Strengths
1. The authors seek to transform the chart information from LCT to STR, which bridges the gap between chart perception and reasoning.
2. The authors construct a synthetic dataset named SimChart9K by leveraging an LLM-based self-inspection data production scheme.
3. Experimental results on the ChartQA and PlotQA datasets demonstrate the effectiveness of the proposed StructChart method.

### Weaknesses
1. This paper emphasizes that STR reduces the task gap between chart perception and reasoning. However, the reasoning process is based on the black box GPT-3.5, which cannot find the relationship between STR and the reasoning process. More explanations are required. 
2. As shown in Eqn. (2), the SRT splits each element in LCT as one unique sample. However, SRT may destroy the intrinsic relationship between the original elements, making them independent. 
3. In Equation (3), the authors introduce the Entity Match method, which employs Intersection over Union (IOU) to compare predictions with ground-truth entities. Do the authors consider the order of the entity strings during the matching process? Ordinarily, aligning the strings in the correct order is essential for accurate matching. However, Equation (3) lacks a detailed explanation of how this matching process is carried out. More discussions are required.
4. The authors adopt STR to make each entity independent. How do the authors determine the correspondence between predictions and specific ground-truth?
5. In Table 2, it's noteworthy that the authors have not included a comparison with Matcha[1] and Deplot[2] on the Chart2Text[3] dataset. An explanation for this omission is needed.
6. In Table 2, the comparisons between StructChart and the compared methods (Matcha and Deplot) somewhat is unfair. StructChart leverages powerful GPT-3.5 as the reasoning model, whereas Matcha is based on Pix2Struct[4] and Deplot relies on Codex or GPT-3. Thus, the disparities in performance between StructChart and the compared methods could potentially stem from the utilization of different reasoning models (i.e., GPT-3 and GPT-3.5).
7. In Table 4, the authors conduct a comparison of StructChart with various baseline methods using the Exact Match metric. It's important to note, however, that the authors have omitted a direct comparison with Deplot, which outperforms StructChart with a higher score (i.e., 76.7 compared to 65.3). In this way, StructChart has no advantage compared with Deplot even if it uses more powerful GPT-3.5.
8. In Table 2, the ‘merging’ is confusing. Does it merge the ChartQA with the SimChart 9K?

### Questions
Please refer to the Weaknesses

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel approach known as the integrated perception and reasoning paradigm, designed to enhance the comprehension of visual charts. Initially, StructChart transforms chart data from the common tabular format, such as linearized CSV, into the newly introduced Structured Triplet Representations (STR). Concurrently, we present the Structuring Chart-oriented Representation Metric (SCRM) for a quantitative assessment of performance. Additionally, we investigate the potential of utilizing the capabilities of a Large Language Model (LLM) to expand the training dataset, specifically the SimChart9K dataset.

### Strengths
1) The paper introduces a new Structured Triplet Representation (STR) instead of CSV format.
2) The Structuring Chart-oriented Representation Metric (SCRM) is suitable for various tasks related to chart perception.
3) This paper provides the SimChart9K dataset, which leverages Large Language Models (LLM) to enhance chart datasets for training purposes.
4) The paper demonstrates good writing quality, encompassing recent literature developments and technical aspects. Notably, Table 1 is informative, and the related work section has covered relevant areas. Additionally, Figure 1 is thoughtfully organized and imparts valuable insights.
5) The experiments are well-considered, offering comprehensive results and insightful ablation studies.
6) The potential impact is substantial, given the practical utility of the proposed method, which addresses challenges not effectively addressed by ChatGPT or existing solutions.

### Weaknesses
1) The approach itself is a bit straightforward as it is not totally end-to-end. However, I don't think it is a drawback, especially given its novel setting compared to other literature.
2) Some typos: e.g. 4.3 ACHIEVING 100% PERFORMANCE BY ONLY 20% REAL DATA. The ending stop shall be removed.

### Questions
Can you compare your method with GPT-4V or other general multi-modality tools?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors claim that they proposed a unified and label-efficient learning paradigm for joint perception and reasoning tasks, which can be generally applicable to different downstream tasks, beyond the question-answering task as specifically studied in peer works.

### Strengths
The authors claim that they proposed a unified and label-efficient learning paradigm for joint perception and reasoning tasks, which can be generally applicable to different downstream tasks, beyond the question-answering task as specifically studied in peer works.

### Weaknesses
1. The experiments should focus on the generalizability of the conclusions/findings derived from the powerful transformer-based models, and it remains a concern.

2. What is the relation and difference with the current popular benchmark (e.g., FigureQA[1])?

### Questions
Please refer to Weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
