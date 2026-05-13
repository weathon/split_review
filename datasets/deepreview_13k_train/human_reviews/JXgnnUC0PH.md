# TaskGalaxy: Scaling Multi-modal Instruction Fine-tuning with Tens of Thousands Vision Task Types

- Decision: Accept
- Scores: 5, 5, 8, 6

## Abstract
Multimodal visual language models are gaining prominence in open-world applications, driven by rapid advancements in model architectures, training strategies, and the availability of high-quality training data. However, their performance is often limited by insufficient task-specific data, leading to poor generalization and biased outputs. Existing efforts to increase task diversity in fine-tuning datasets are hindered by the labor-intensive process of manual task labeling, which typically produces only a few hundred task types. Motivated by task diversity and automated processes aimed at saving labor, in this paper we propose TaskGalaxy, a large-scale multi-modal instruction fine-tuning dataset that includes 19,227 hierarchical task types and 413,648 associated samples. TaskGalaxy utilizes GPT-4o to enrich task diversity by expanding from a small set of manually defined tasks, with CLIP and GPT-4o filtering those that best match open-source images, and generating relevant question-answer pairs. Multiple open-source models are employed to filter and ensure high-quality, well-aligned samples. This automated process enhances both task diversity and data quality, reducing manual intervention. Experimental results demonstrate that incorporating TaskGalaxy into the LLaVA-V1.5 and InternVL-Chat-V1.0 model architectures for instruction fine-tuning leads to substantial performance improvements across all 16 benchmarks, highlighting the critical importance of task type diversity. The TaskGalaxy dataset will be publicly released to support future research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed a new instruction tuning dataset generation pipeline and a new dataset consist of ~19K tasks and ~400K samples. Through a hierarchical task defination, it aims to make diverse task types and further enhance diversity of dataset. By instruction tuned on proposed TaskGalaxy dataset, MLLM show improved performance on various benchmarks.

### Strengths
The pipeline proposed by the paper is diverse and scalable. It aims to increase sample diversity of instruction tuning, which is an key problem in relative field. Tuning with proposed dataset brings further improvements of MLLMs.

### Weaknesses
1. As the task type generation is a hierarchical process, provide some examples or statistics of level 2/3 tasks can be more clear. For example, provide a list of tasks with the most/least sample, analysis of image resolutions, distribution of tasks across levels.
2. The diverse task types actually can improve image diversity. However, image sources are still similar with existing datasets, whose diversity maybe limited. Overall review of images sources, such as the proportion of samples from different data sources, is also necessary to understand the dataset.
3. I think the experiments are not convincing enough. As baseline is instruction tuning with LLaVA-665K, TaskGalaxy finetuning actually increase the amount of data, which is shown to be a key factor for model performance. Comparing with baseline LLaVA-Instruct only and TaskGalaxy only with equal amount would be better.
4. Apart from comparison with baseline, there are several high-quality instruction tuning dataset such as LLaVA-OneVision[1], ShareGPT4V[2] and etc. Meanwhile, I think works like ShareGPT4V should be included in related work. Comparison between those works are more important to show effectiveness of TaskGalaxy, performance of models tuned with the same amount of data samples from TaskGalaxy, LLaVA-665K, LLaVA-OneVision and ShareGPT4V is more convincing.
5. To comprehensively present properties of TaskGalaxy, a detailed dataset card is preferred to show more about statistics or usage. Examples can be found at [this link](https://arxiv.org/abs/2204.01075).

### Questions
See in Weakness.

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
4

### Summary
This manuscript introduces a novel multi-modal instruction fine-tuning dataset called TaskGalaxy. TaskGalaxy proposes an automated pipeline comprising five main steps, which leverages robust multimodal model and reduces manual intervention. The proposed TaskGalaxy consists of tens of thousands vision task types and 413k samples to address the limitation of task diversity in existing datasets. The performance of LLaVA-V1.5 and InternVL-Chat-V1.0 model incorporating TaskGalaxy fine-tuning is improved across 16 benchmarks.

### Strengths
1.	The paper is easy to follow. The details of data construction and experiments are clear.

2.	TaskGalaxy contains a rich set of task types, alleviating the impact of limited task types on model generalization ability.

3.	The pipeline of TaskGalaxy can be flexibly expanded to create more high-quality data.

4.	Incorporating this training data, the performances of LLaVA-V1.5-13b and InternVL-Chat-V1.0-7b have been improved.

### Weaknesses
1.	In Hierarchical Task Type Generation, this process resulted in the generation of 19,227 hierarchical task types. But the task types are completely GPT-4o generated, how to ensure that 19,227 task types do not overlap with each other? The diversity of the tasks and data are neither thoroughly nor rigorously studied. There is no in-depth comparison to previous tasks and data. Merely relying on GPT-4o to ensure task diversity is not reliable. The similarity scores between the generated tasks cannot prove any claim about the diversity.

2.	Since the improvements are obtained by training on baseline data + TaskGalaxy data, it is not possible to tell whether the improvements are due to the larger data amount or the larger task number. 

3.	In Match and Filter section, images and task types are encoded by the off-the-shelf CLIP respectively to get the embeddings. As CLIP is trained mostly on data of natural concepts, filtering images with abstract phrases such as task type may be not as effective as expected. 

4.	The performance of the baseline is too weak to prove the validity of the dataset. For example, InternVL-Chat-V1.0-7b only achieved the performance of 35.96% on AI2D and 15.2% on ChartQA. More advanced models, such as LLaVA-V1.6 and InternVL-Chat-V2.0-8B, should be evaluated. The improvements over LLaVA-665K is not as big as expected, since it was proposed one year ago. More state-of-the-art finetuning data should be compared.

### Questions
1.	Typos: In the caption of Figure 1, The spelling of " llustration" is wrong. 

Please address the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a finetuning dataset for Vision-Language finetuning called TaskGalaxy, consisting of 19k hierarchical task types. The data is synthetically generated starting from seed tasks and contains 413k samples.
- First two levels of hierarchy are defined manually, and GPT-4o is prompted to expand the hierarchy
- The task type names are used to match images from multiple open source datasets using CLIP to match the text to images
- Given the top 10 matched task types to a given image, GPT-4o is used to filter out the irrelevant task types
- Based on the image and task types, GPT-4o is prompted to generate question-answer pairs
- Finally, 3 open source models (GLM-4v-9B, InternVL-Chat-V1.5 and InternVL2-26B) are prompted to score the generated question, task type and image with a score of 1 if the question and task type match relative to the image, and 0 otherwise. Samples are filtered through majority voting.
- The generated dataset is used to finetune models on downstream tasks, showing improved performance.

### Strengths
1. The paper proposes a scalable synthetic data generation pipeline across multiple task types from publicly available datasets.
2. Models finetuned with the generated dataset in addition to the original datasets show improved performance, which shows the effectiveness of the proposed dataset.
3. The dataset is ablated well to check the effect of varying the number of task types and number of samples for each task type, with higher number of task types and samples showing better performance, ~5% improvement on average (Table 2 and Figure 6).
4. The paper proposes a multi-stage pipeline for filtering the genearated samples, which can reduce the noise on the generated data.

### Weaknesses
1.  **Check for hallucinations and incorrect responses**
- The paper does not have an explicit check for hallucinations and incorrect responses. Prior LLM generated datasets have had problems with hallucinations, leading to subpar performance on downstream tasks. Upon resolving the problems, the performance on downstream tasks typically increases [1]. While the multi-stage pipeline can potentially eliminate hallucinations, especially when 3 models are used as validators, the method and dataset will be more trustworthy if an explicit check is performed. Specifically, the paper should include an analysis of the types of errors that occur during the question-answer generation process. For example, are there specific task types or image characteristics that are more prone to generating incorrect or nonsensical question-answer pairs? This analysis should also quantify the frequency of such errors before and after the filtering stages to understand the effectiveness of the filtering process.
2.  **Scope and impact**
- In the current form, the proposed dataset and generation pipeline is limited to building a good finetuning/visual instruction tuning dataset.
- The paper does not provide more information about the samples that are rejected during each stage of the filtering pipeline. The rejected samples might provide more insights into the behavior of the generator model and could be potentially valuable for future research into synthetic data generation. Studying this aspect might help broaden the impact of the work.
- For example, the authors could analyze type of question-answer pairs are typically rejected by the three filtering models, or if there is a pattern to which task types are rejected the most.
- This might also partially address Point 1 about hallucinations. Furthermore, the paper should explore the potential for using the rejected samples to improve the data generation process. For instance, could the patterns in the rejected samples be used to refine the prompts used to generate the data or to train a better filtering model? This could potentially lead to a more robust and efficient data generation pipeline.

### Questions
Please refer to the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents TaskGalaxy, a multi-modal instruction fine-tuning dataset. A pipeline for the systematic construction and generation of a diverse range of task types and corresponding high quality instruction Q&A samples is proposed. The fintuning results of LLaVA-V1.5 and InternVL-Chat-V1.0 validate the effectiveness of the proposed dataset.

### Strengths
1. The dataset construction pipeline is elegant and makes sense.
2. 19,227 hierarchical task types and 413,648 associated samples are a lot, I believe it can make contributions to the community.

### Weaknesses
1. As a submission on the area of datasets and benchmarks, the access to data is not provided to reviewers, which is obviously unreasonable.
2. The experiments are insufficient and lack comparison with other similar datasets.

### Questions
1. Compared with other existing similar datasets,  what are the advantages of the proposed dataset?
2. The comparisons of SFT results on various architectures with other similar datasets are suggested to supplement.
3. In the stage of match and filter, which CLIP model is adopted?
4. I wonder how the accuracy changes under the same architecture but with various sizes trained with the proposed dataset.

### Soundness
3

### Presentation
3

### Contribution
3
