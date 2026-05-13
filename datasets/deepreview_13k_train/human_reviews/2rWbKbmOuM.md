# MEGA-Bench: Scaling Multimodal Evaluation to over 500 Real-World Tasks

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
We present \benchmark, an evaluation suite that scales multimodal evaluation to over 500 real-world tasks, to address the highly heterogeneous daily use cases of end users.
Our objective is to optimize for a set of high-quality data samples that cover a highly diverse and rich set of multimodal tasks, while enabling cost-effective and accurate model evaluation.
In particular, we collected 505 realistic tasks encompassing over 8,000 samples from 16 expert annotators to extensively cover the multimodal task space. Instead of unifying these problems into standard multi-choice questions (like MMMU, MMBench, and MMT-Bench), we embrace a wide range of output formats like numbers, phrases, code, \LaTeX, coordinates, JSON, free-form, etc. To accommodate these formats, we developed over 40 metrics to evaluate these tasks. 
Unlike existing benchmarks, \benchmark offers a fine-grained capability report across multiple dimensions (e.g., application, input type, output format, skill), allowing users to interact with and visualize model capabilities in depth. We evaluate a wide variety of frontier vision-language models on \benchmark to understand their capabilities across these dimensions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presents a new benchmark for multimodal LLMs. The authors attempt to create a novel, diverse, comprehensive benchmark for vision-language reasoning using a several-stage process for designing the benchmark, refining the questions, and developing appropriate metrics. The authors conduct a comprehensive large-scale evaluation of current SOTA multimodal models using the benchmark.

### Strengths
# Overall assessment

This work presents an interesting contribution in a much-needed space (benchmarks for multimodal large models). To address the current scattershot approach to multimodal model benchmarking, the authors attempt to create a single, highly diverse, comprehensive benchmark for a variety of image-language tasks (including video). To construct the benchmark the authors develop and refine a task taxonomy, but some details around the taxonomy and its construction are unclear. I have concerns about how the benchmark would be used in practice related to the 40 different evaluation metrics, and the distribution over various attributes (number of images, task type, etc.) but am willing to increase my score based on discussion with authors and other reviewers.

# Major comments

* The quality of the benchmark ultimately relies on the authors' proposed taxonomy, as this forms the basis for all data collection. However, I found the description of the annotation process somewhat disappointing; it effectively amounts to "the Feynman Method" (write down the problem, think hard about it, write down the solution). Critically, the authors provide no discussion or framing around the "conceptualization stage" for how they identified the top levels of the taxonomy (perception, planning, reasoning), nor how the annotators were selected or why they are representative of the whole of relevant multimodal knowledge (the sample of annotators could also bias the coverage in various ways). Please provide a clear discussion of (a) what the levels of the taxonomy are (please give the full list) and (b) how these levels were identified and why they comprise a holistic benchmark and (c) the disciplines of the annotators (since the authors state they are graduate or above from diverse disciplines).

* The diversity of output formats is an interesting contribution. However, the diveristy of evaluation metrics (over 40 metrics?!) also makes this benchmark somewhat unwieldy, and raises concerns about usability. These issues arise even in the authors' main findings, stated at the end of Section 1. For example, it is very difficult to understand what it means that GPT-4o is 3.5% better than Claude 3.5? What makes this a "significant margin"? If Qwen2-VL is 10% better than other open source models, what does this mean? T

* It is not clear whether all tasks in the benchmark have a single, objective answer. This makes it difficult to assess models' capabilities (for example, failure to write a latex equation may simply be due to a difference in formatting; writing a story containing two animals hinges on many different criteria which are difficult to assess).

* The advantages of a single, diverse, high-coverage benchmark are outlined nicely in the introduction. However, the paper's contribution hinges on whether it does indeed  achieve strong coverage of a "diverse" suite of tasks. Ultimately, this is nearly impossible to assess, but I have some concerns about the "concepttualization" process above that make me unsure that this benchmark is as comprehensive as the authors claim. On the other hand, the existing benchmarks are also imperfect (and a direct comparison to existing benchmarks in terms of content and task design would make it easier to assess whther the benefits of the new benchmark outweigh the potential downsides and complexity).

* It is unclear why certain task distributions are set as the authors designed them in the benchmark. For example, why are only 4% of tasks 6-8 images, while 8% are 9+ images? Why are 16% of tasks open-ended while 22% are structured? These design decisions can have significant effects when averaging over benchmarks, as will likely occur with this benchmark.

* The empirical study is useful, appears comprehensive, and leads to some interesting conclusions.

* It seems unlikely that the benchmark will last very long by relying on GPT-4o as judge. Is it possible to substitute the LLM judge in the benchmark if a future best frontier model emerges?


# Minor comments

* Another relevant multimodal baseline the authors may want to reference: Bitton, Yonatan, et al. "Visit-bench: A dynamic benchmark for evaluating instruction-following vision-and-language models." Advances in Neural Information Processing Systems 36 (2023): 26898-26922.

# Typos etc

* "these models have shown great potential to solve any desired task with a well-designed prompt" - this is editorlaizing somewhat; please revise.

* L111-113: "comprehensive studies...have discovered" passive voice, consider revising

### Weaknesses
see above

### Questions
see above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents MEGA-BENCH, a comprehensive multimodal benchmark scaling up to over 500 real-world tasks, designed to assess the diverse capabilities of vision-language models. It offers a fine-grained analysis across various dimensions, including application, input type, output format, and skills, and provides customized metrics for different output formats. The benchmark reveals significant performance variations among state-of-the-art models, emphasizing the importance of task diversity over increasing examples per task for insightful model evaluation.

### Strengths
1. MEGA-BENCH has a large scale and coverage, containing over 500 diverse real-world tasks, which allows for an in-depth assessment of multimodal models across various applications and skills.

2. It offers a sophisticated, fine-grained analysis capability by categorizing tasks along multiple dimensions, providing a nuanced understanding of model performance in specific areas and revealing strengths and weaknesses that aggregate scores might obscure.

3. The benchmark's design emphasizes cost-effectiveness and efficiency, demonstrating that increasing task diversity is more valuable for gaining performance insights than simply adding more examples per task.

### Weaknesses
1. While MEGA-BENCH offers a vast array of tasks, its large scale may lead to increased computational costs and complexity in evaluation, potentially limiting its accessibility for further research and extensive exploration.
2. MEGA-BENCH's focus on breadth may result in some tasks being too specific or niche, which could limit the generalizability of the benchmark results to a broader range of multimodal problems and applications.

### Questions
1. Could you explain more about the background of your 16 annotators and how you make sure for all task instances, the instruction and solution align with each other?
2. For the open-ended tasks, you mentioned using an LLM-assisted metric. How do you handle the potential for bias in the evaluation process, given that the scoring is dependent on a proprietary LLM? If we use different LLM as judges, will their ratings differ a lot from each other?
3. What are the considerations and challenges you preview when scaling MEGA-BENCH even further? How do you plan to maintain the benchmark's relevance and diversity as new multimodal tasks emerge?

### Soundness
4

### Presentation
4

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
The paper presents Mega Bench, a comprehensive benchmark for evaluating multimodal models on over 500 tasks. Mega Bench features a wide range of output formats and uses multiple metrics for evaluation. It includes a detailed capability report for popular language and vision models. The benchmark's assessment of leading models reveals significant performance differences and the importance of task diversity.

### Strengths
S1: The proposed open-source benchmark includes a large number of diverse tasks for LLMs that can potentially address the limitations of existing benchmarks. It provides valuable resource for the community.

S2: The paper also provides an extensive experiment and analysis of popular LLMs using Mega Bench. It yields many interesting findings.

S3: This paper is well-written and easy to read.

### Weaknesses
### Major weaknesses

W1: The rationale behind the task taxonomy tree is not well-explained. Section 3.1 can be strengthened by discussing the design considerations for the draft taxonomy tree. For example, why do we want perception, planning, reasoning? Are these the limitations of existing benchmarks? How do we know this taxonomy is comprehensive and reflects the real usage of LLMs? The paper should elaborate on how the chosen categories (perception, planning, reasoning) were derived, and how they relate to the limitations of current benchmarks. A more detailed discussion of the existing benchmarks and their shortcomings would help justify the need for this specific taxonomy. For instance, are existing benchmarks lacking in evaluating planning capabilities, and how does this taxonomy address that gap?

W2: The introduction highlights Mega Bench's contributions in multimodal tasks. However, there is limited information regarding non-text tasks in Section 3. I recommend adding a few non-text tasks in Figure 4 and discussing the image and video tasks included in Mega Bench in Section 3. The paper needs to provide more concrete examples of non-textual tasks. While the paper mentions multimodal tasks, it lacks specific examples of image and video-based tasks within the benchmark. Expanding Figure 4 to include examples of image/video inputs and their corresponding outputs would be beneficial. A more detailed description of these tasks in Section 3 is also needed to fully understand the multimodal aspect of the benchmark.

W3: It is unconvincing that Mega Bench makes significant contributions over existing benchmarks. In the introduction, the paper lists four limitations of existing benchmarks: (1) limited output diversity, (2) lack of task coverage, (3) expensive inference cost, and (4) unmanageable setups. Section 3 and 4 explain how Mega Bench address limitations (1) and (2), but (3) and (4) remain unaddressed in the paper. I recommend discussing what makes Mega Bench less expensive and easier to run compared to other popular benchmarks. The paper should provide a detailed comparison of the inference costs and setup complexity of Mega Bench compared to other benchmarks. For example, what is the average inference time per task in Mega Bench, and how does it compare to benchmarks like MMBench or VQA? Similarly, what are the specific steps required to set up Mega Bench, and how do they compare to the setup procedures for other popular benchmarks? A quantitative analysis of these aspects would strengthen the claims of reduced cost and improved manageability.

### Minor weaknesses

M1: Replace $ (L83).

M2: The claim that "many examples or tasks are highly similar in the capabilities that they assess" requires evidence to back it up (L83-83).

M3: The tasks in Mega Bench have a lot in common with those in Big Bench. A detailed comparison to Big Bench would be beneficial.

### Questions
Q1: There are many different input/output formats and metrics in Mega Bench. How does Mega Bench address the challenge of "Unmanageable Setups" mentioned in the introduction?

Q2: Are there any copyright / privacy concerns for the tasks in the bench mark?

### Soundness
3

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
4

### Summary
The paper introduces MEGA-BENCH, a comprehensive multimodal evaluation suite that encompasses over 500 real-world tasks, addressing the diverse daily use cases of end users. Its goal is to optimize for high-quality data samples that cover a wide range of multimodal tasks while facilitating cost-effective and accurate model evaluation. The authors have compiled 507 realistic tasks with over 8,000 samples from 16 expert annotators, embracing various output formats and developing over 40 metrics to accommodate these formats. MEGA-BENCH provides a fine-grained capability report across multiple dimensions, enabling in-depth interaction with and visualization of model capabilities. The paper also evaluates various state-of-the-art vision-language models using MEGA-BENCH, revealing significant performance variations among models that were previously thought to be similar.

### Strengths
The creation of MEGA-BENCH is an original contribution to the field of multimodal AI evaluation. It scales up the number of tasks to an unprecedented level, offering a comprehensive assessment of model capabilities across a vast array of real-world applications. The approach of embracing diverse output formats and developing over 40 metrics to accommodate these is innovative, moving beyond the limitations of traditional multi-choice question-based benchmarks.

The quality of the work is evident in the meticulous construction of the benchmark. With 507 realistic tasks and over 8,000 samples collected from 16 expert annotators, the dataset is both extensive and rich in diversity. The rigorous annotation process, including the development of an annotation GUI and a taxonomy tree, ensures high-quality data that is well-suited for evaluating multimodal models.

The paper is well-structured and clearly articulated. The figures and tables are effectively used to convey complex information in a digestible manner. The taxonomy tree and the breakdown of tasks across different dimensions are particularly clear, aiding the reader in understanding the scope and organization of MEGA-BENCH.

### Weaknesses
The paper presents a snapshot of model performance but does not address how these benchmarks might be used to track performance over training time. A good benchmark should be verified by scaling laws. Furthermore, the paper lacks a discussion on the potential biases present in the dataset. Given that the data was collected from 16 expert annotators, there is a possibility of annotator-specific biases influencing the benchmark. This could lead to skewed performance evaluations, where models might overfit to the specific annotation styles rather than generalizing to the underlying tasks. The paper also does not delve into the difficulty levels of the tasks included in the benchmark. While the tasks are diverse, it is crucial to understand the inherent difficulty of each task to properly assess model capabilities. Without this analysis, it is hard to determine if a model's performance is due to its actual capabilities or the simplicity of the tasks it is evaluated on.

### Questions
Has the authors' team conducted any analysis on the environmental impact of the computational resources required for the benchmarking process? If so, could they share some insights?

Are there plans to release the annotation tools, pre-processing pipelines, and evaluation metrics as open-source to facilitate community-wide reproducibility and further development?

Could the authors discuss how the tasks in MEGA-BENCH map to real-world applications? Are there any tasks that are particularly relevant to current industry needs or future technological trends?

### Soundness
2

### Presentation
3

### Contribution
3
