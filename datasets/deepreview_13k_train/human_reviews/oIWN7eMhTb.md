# CityBench: Evaluating the Capabilities of Large Language Models for Urban Tasks

- Decision: Reject
- Scores: 8, 6, 6, 5, 10

## Abstract
Large language models (LLMs) with powerful generalization ability has been widely used in many domains. A systematic and reliable evaluation of LLMs is a crucial step in their development and applications, especially for specific professional fields. In the urban domain, there have been some early explorations about the usability of LLMs, but a systematic and scalable evaluation benchmark is still lacking. The challenge in constructing a systematic evaluation benchmark for the urban domain lies in the diversity of data and scenarios, as well as the complex and dynamic nature of cities. In this paper, we propose \textit{CityBench}, an interactive simulator based evaluation platform, as the first systematic evaluation benchmark for the capability of LLMs for urban domain. First, we build \textit{CitySim} to integrate the multi-source data and simulate fine-grained urban dynamics. Based on \textit{CitySim}, we design 7 tasks in 2 categories of perception-understanding and decision-making group to evaluate the capability of LLMs as city-scale world model for urban domain. Due to the flexibility and ease-of-use of \textit{CitySim}, our evaluation platform~\textit{CityBench} can be easily extended to any city in the world. We evaluate 13 well-known LLMs including open source LLMs and commercial LLMs in 13 cities around the world. Extensive experiments demonstrate the scalability and effectiveness of proposed \textit{CityBench} and shed lights for the future development of LLMs in urban domain.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper releases a new systematic benchmark to evaluate LLM and VLM capabilities on geospatial urban data, including interactive and non-interactive tasks that test semantic understanding as well as reasoning.

### Strengths
**(S1)**: A comprehensive benchmark with multiple interactive and non-interactive tasks. The authors provide a benchmark that has a good diversity of tasks to evaluate VLM and LLM capabilities. The tasks that form this benchmark are valuable to the research community and for future LLM developers.

**(S2)**: Extensive evaluations with popularly used large language models. The experiments break down the performance for each task for multiple LLMs with sensible metrics. (although I think Llama 405B is missing).

**(S3)**: Publicly released code and API for running the evaluation. It is good that the authors already have the code and API ready for this benchmark, which should aid reproducibility and adoption for CityBench.

Overall, I think the benchmark provided in this paper is valuable to the research community for the diversity of tasks it includes. The paper is well-written and presented, and so I lean towards acceptance.

### Weaknesses
 **(W1)**: Template based questions. The authors specify in section 3.3.1 that they use LLMs to generate instructions for tasks and also use LLMs to filter out low-quality data. More details are needed here, such as which LLMs are used, whether a mixture of LLMs are used, and how much this biases the downstream benchmark performance in favor of certain models. In general, more specific details on the quality control process are required (eg: how much low-quality data was generated, how much was manually curated etc.). Specifically, the lack of clarity on the LLM used for question generation and filtering introduces a potential confound. If a single LLM, such as GPT-4o, was used, the benchmark might inadvertently favor models that align well with its biases, leading to an overestimation of their true capabilities. The absence of quantitative metrics on the amount of low-quality data generated, filtered, and manually curated makes it difficult to assess the robustness of the benchmark.

**(W2)**: Not enough geographic diversity. While the authors do make an effort to collect data for 13 cities across the globe, as they note in Figure 5, the performance on less renowned cities is worse for most LLMs. I think for a more comprehensive benchmark, the authors could consider including a larger diversity of cities for more fine-grained analysis on LLM capabilities. The current selection of 13 cities, while diverse, may not be sufficient to capture the full spectrum of urban environments and their associated challenges. A more extensive set of cities would enable a more robust evaluation of LLM generalization capabilities across diverse geographical contexts.

**(W3)**: Missing comparisons with human baselines. I am curious to know how well humans perform on some of these interactive tasks and it would be good to include a baseline for human-level performance within the benchmark. Without a human baseline, it is difficult to gauge how close LLMs are to achieving human-level performance on these tasks. This makes it challenging to determine the potential for further improvement and the practical applicability of these models.

### Questions
**(Q1)**: Figure 5: Why is the performance on New York so low, considering it is a very well-known city. Are there any hypotheses for this case?

**(Q2)**: How exactly are satellite/street-view images sampled for the dataset? What is the distribution of these images per city in the benchmark?

**(Q3)**: On examples where the model always provides an answer (i.e. not ones where it refuses to answer), how do the different models compare?

**(Q4)**: Did you try evaluating few-shot performance for these models? How does LLM performance scale with in-context examples?

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
5

### Summary
This paper introduces CityBench, a systematic benchmark for evaluating the capabilities of large language models (LLMs) in urban research. The authors develop CityData and CitySim to integrate diverse urban data and simulate urban dynamics, constructing CityBench with eight representative tasks. The findings indicate that while advanced LLMs excel in understanding human dynamics and semantic inference in urban images, they struggle with complex tasks requiring specialized knowledge and high-level reasoning, such as geospatial prediction and traffic control. These insights offer valuable perspectives for the future application and development of LLMs.

### Strengths
1. Open Source: The authors have developed CityBench and CitySim, which involve a substantial amount of engineering effort, and have also made the codebase open-source. This is beneficial for future research in this domain.
2. Rich geographic diversity: CityBench covers 13 cities, providing a rich geographic diversity.

### Weaknesses
1. Figure presentation issues: The left panel of Figure 5 aims to showcase differences in performance across cities, but lacks a legend to identify different cities.
2. Experiment: 1) Incomplete and lacking insight in Error Analysis: The error analysis section only provides insights into LLM errors, with no analysis of VLM errors. Additionally, the LLM error analysis merely highlights general issues common across benchmarks, such as instruction-following limitations and hallucinations, without offering task-specific insights relevant to CityBench’s urban-focused tasks. A more robust analysis could involve systematically sampling each model’s errors on individual tasks, with detailed analysis and conclusions. 2) Incomplete test results: Both Table 2 and Table 3 present CityBench results. While Table 2 omits LLM results due to the visual input requirement, Table 3 involves purely language-based tasks, making it feasible to test VLMs as well. Including VLM results for these tasks would provide a more comprehensive evaluation.
3. Method：1) Transparency of CityBench data volume: Table 1 provides extensive data details for CityData; however, the main text does not include specific data quantities for CityBench. Additionally, the appendix lacks clear information on the exact number of tasks, providing only approximate figures. 2) Unclear task setup: The distinction between testing LLMs and VLMs separately for the Outdoor Navigation and Urban Exploration tasks is not well-explained. According to the descriptions, these tasks are similar, both involving decision-making. However, only LLMs are tested in one task and VLMs in the other, without a clear rationale.

### Questions
1、Vague description of data processing: The quality control section mentions the role of human annotators and states that the authors participated in data filtering and rewriting. However, the standards and proportions for filtering and rewriting are not specified. Including these details would make CityBench more transparent and easier to understand.

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
This paper targets the limitations in current explorations of large language models (LLMs) within the urban domain. It creatively introduces an interactive simulator to construct a multi-task, multi-dimensional benchmark and conducts extensive, comprehensive experiments, yielding intriguing conclusions. The authors release their code to foster the development of the community.

### Strengths
1. It’s exciting to see the promising potential of methods based on interactive simulators in the field of LLMs for urban applications; this work can provide a meaningful boost to community development.

2. The workload is substantial, covering a wide range of tasks with detailed and thorough experiments.

### Weaknesses
1. The paper provides a somewhat vague description of the pipeline. For example, in Section 3.3.1, what are the criteria for identifying low-quality data? What are the standards for filtering and rewriting? Specifically, how is 'low-quality' defined for the GeoQA task, and what specific metrics or heuristics are used to determine if data should be filtered or rewritten? The description of the manual checking process is also unclear; what constitutes 'meaningful' context, and how is this assessed by the authors, especially when they are unfamiliar with a given city or region? Furthermore, the process of regenerating cases is not well-defined; what criteria determine when regeneration is necessary, and how many new cases are generated to fill the gaps?

    In Section 3.1 CityData, the authors state that OSM data is unsuitable for city data construction and introduce a globally applicable rule-based map construction tool. However, there is no specific description of this tool, which leaves readers uncertain about its details and limits understanding of its functionality. What are the specific rules used for lane topology recovery, relationship recognition, and intersection reconstruction? How are these rules implemented, and what are their limitations? The lack of detail makes it difficult to assess the robustness and generalizability of this tool.

2. A suggestion: the name 'CitySim' is already in use[1], so choosing a different name might help reduce potential ambiguity.

3. In the construction of the Human Activities Data in Section 3.1, data from the literature published in 2016 was used. Can data from a paper published eight years ago accurately reflect the current state of human activities in cities?

4. There is another work CityEval in [2] published in June 2024, which also evaluates the capabilities of LLMs in urban spaces, and some tasks are similar to those in this work. Has the author considered comparing and discussing the differences between the two?

### Questions
Please see weakness.

### Soundness
3

### Presentation
2

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
The submission presents a framework to evaluate the capabilities of a series of foundation models, including some text-based LLMs and some multi-modal, say, image-text, models, in city-related tasks. It starts from data collection, data processing, and fianally carrying out tasks and benchmarking. It is no doubt the utility of LLM (in the broad sense including multi-modal) in analyzing human activities and city tasks is interesting. This could potentially shape the future research in LLM at large and the development of city-related LLM. However, the paper have not done a good job in providing concrete enough evidence in the underlying causes and lessons learnt. In addition, some experimental designs are flawed.

### Strengths
a. the utility of LLM for city-related tasks is an interesting point to explore
b. the benchmarking was done in a somewhat broad dataset with cities in different continents and a number of models are tested
c. the categorization of tasks is interesting and useful

### Weaknesses
a. the underlying causes of the good or bad performance of the models in different settings in terms of cities, models, tasks, are not discussed, only with vague and shallow discussions. This is supposed to be the key point to benefit future research and development. It could be ok that we do not push too much on novelty for this submission (more or less should be a major point for iclr though). However, the shallow explanations of the model performance and their comparison are disappointing. For instance, what is the root cause(s) of the unpleasant performance of LLM in regression tasks?

Indeed, the authors mentioned that LLM some cities do not have as good performance as other cities. The cause here is only “lesser-known”, without presenting any evidence of the underrepresentation. Other aspects, eg socio-economical, morphological, linguistic aspect, are not discussed.

The benchmarking paper can be benefitted a lot from deeper analysis and discussion. This is supposed to be the key.
b. LLM is in many ways not as good as, or only on par with conventional end-to-end or task specific methods. This somehow is interesting for developments in urban computing. But what is the lesson learnt here is rather sparsely mentioned.
c. the citydata module is only the introduction of datasets used, and it should not be listed as as a contribution brought up by this paper.

### Questions
a. the foursquare data is from 2016. Why not use more current data? Will the old dataset affect the findings? 
b. it is unclear why the five qualities (the paper then interpreted the theory as six qualities) in “the image of the city” are used for GeoQA. The five qualities are proposed for guiding urban design practices. Could you elaborate on the relation between the five qualities and benchmarking GeoQA?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper introduces **CityBench**, an innovative platform designed to evaluate the capabilities of large language models (LLMs) and visual language models (VLMs) in solving diverse urban tasks. CityBench integrates three core components: **CityData**, which collects and processes geospatial, visual, and human activity data; **CitySim**, a simulator that models urban dynamics like individual mobility, visual environments, and microscopic traffic behavior; and **CityBench**, which offers a comprehensive evaluation of eight urban tasks in two categories — perception & understanding and planning & decision-making.

The authors conducted extensive experiments involving 30 LLMs and VLMs across 13 global cities, evaluating tasks such as geospatial prediction, image geolocalization, traffic signal control, and mobility prediction. The results highlight the potential of LLMs and VLMs in handling urban tasks that require commonsense reasoning and semantic understanding, while also exposing challenges in tasks requiring precise professional knowledge and high-level reasoning, such as geospatial prediction and traffic control.

The paper contributes significantly by providing a scalable and systematic evaluation framework, uncovering strengths and limitations of current LLMs/VLMs in urban settings, and paving the way for further development and application of these models in real-world urban scenarios.

### Strengths
1. **High Level of Innovation**:
    - The paper introduces **CityBench**, a highly innovative and comprehensive evaluation platform. CityBench stands out by integrating multi-modal data and interactive simulations to systematically evaluate the performance of LLMs and VLMs in urban tasks, filling a significant gap in the evaluation benchmarks for urban research.
    - The combination of **CityData** and **CitySim** offers researchers a robust tool that simulates fine-grained dynamics across 13 cities. This large-scale, multi-city, multi-modal simulation environment sets CityBench apart from previous work, which has not addressed this level of complexity and scale.

2. **Comprehensive and Detailed Experiment Design**:
    - The experiment design is meticulous, covering both perception tasks (such as image geolocalization and infrastructure inference) and decision-making tasks (such as traffic signal control and mobility prediction). This creates a thorough evaluation framework that includes both straightforward perception tasks and more complex decision-making scenarios.
    - The authors conducted extensive experiments with 30 different LLMs and VLMs, providing a rich dataset and thorough result analysis, validating CityBench as an effective benchmark for urban research.
    - Additionally, the **error analysis and geospatial bias analysis** demonstrate a deep understanding of model behavior across different environments, offering valuable insights for future improvements.

3. **Practicality and Forward-looking Approach**:
    - The paper goes beyond theory by offering an open-source evaluation platform with easy-to-use APIs, significantly increasing its usability and scalability for further urban research applications.
    - It explores the potential of LLMs in urban research, particularly in dynamic and interactive environments, showcasing the future applications of LLMs in urban planning, traffic management, and other real-world urban scenarios.

### Weaknesses
1. **Limited Task Diversity**:
    - While the paper has designed a rich set of urban tasks, there is room for further expansion to include tasks that cover broader social, economic, and environmental aspects of urban research. Future iterations could consider incorporating more tasks related to community planning, disaster response, or even economic activity modeling, which would enhance CityBench’s applicability across a wider range of urban research domains. For example, the current benchmark lacks tasks that evaluate models on their ability to predict or understand urban socio-economic dynamics, such as housing affordability or job accessibility, which are critical for comprehensive urban analysis.

### Questions
1. **Task Diversity**: One of the paper’s key strengths is the wide range of urban tasks included in CityBench. However, do the authors have plans to extend CityBench to cover tasks related to more social or environmental aspects of urban life, such as community planning or disaster response? Expanding the diversity of tasks could further enhance the platform’s applicability across various urban domains.

2. **Geospatial Bias**: The paper highlights the geospatial bias present in VLMs when evaluated across different cities. Could the authors provide further insight into why this bias exists? Specifically, what are the potential underlying factors (e.g., differences in urban morphology, data availability) contributing to this bias, and are there plans to mitigate it in future iterations of CityBench?

3. **Model Performance Variability**: The variability in performance across different LLMs and VLMs was an interesting finding, particularly the fact that larger models did not always outperform smaller ones. Could the authors elaborate on potential causes for this? Do the authors believe this is due to task complexity, model architecture, or data-specific issues?

4. **Error Handling**: The error analysis was quite revealing, especially the frequency of formatting and logic errors in certain models. Are there any specific strategies the authors would suggest to mitigate these types of errors in future deployments of LLMs and VLMs within urban tasks?

### Soundness
4

### Presentation
4

### Contribution
4
