# CURIE: Evaluating LLMs on Multitask Scientific Long-Context Understanding and Reasoning

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 6, 8, 6

## Abstract
Scientific problem-solving involves synthesizing information while applying expert  knowledge.   We  introduce  CURIE,  a  scientific  long-Context  Understanding, Reasoning, and Information Extraction benchmark to measure the potential of Large Language Models (LLMs) in scientific problem-solving and assisting scientists in realistic workflows. This benchmark introduces ten challenging tasks curated by experts in six disciplines - materials science, condensed matter physics, quantum computing, geo-spatial analysis, biodiversity, and proteins - covering both experimental and theoretical work-flows in science. We evaluate a range of closed and open LLMs on tasks in CURIE which requires domain expertise, comprehension of long in-context information,and multi-step reasoning.  While Claude-3 shows consistent high comprehension across domains, the popular GPT-4o and command-R+ fail dramatically on protein sequencing tasks. Overall there is much room for improvement for all models. We hope that insights gained from CURIE can guide the future development of LLMs in sciences.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces CURIE, a scientific long-context reasoning and information retrieval (IR) benchmark. It contains ten tasks across six scientific domains, all designed to be challenging yet realistic. A wide range of open-source and closed-source large language models (LLMs) are tested, and Claude-3 consistently outperforms other models, including GPT-4.

### Strengths
- **Dataset Design**: The dataset is well-designed, covering ten complex tasks (even complex for humans) across six scientific fields. It targets the realistic problems faced by scientists.

- **Annotation Process**: The annotation process is thoroughly explained, and the motivation for selecting each sub-task is clearly articulated.

### Weaknesses
 **Dataset Size Too Small**:

- “The CURIE benchmark encompasses 434 examples across ten tasks curated from 273 research papers across six diverse scientific disciplines.” The scale of the dataset is somewhat small. Specifically, tasks like PDB and CEO have only 21 and 19 examples, respectively. This limited size may lack statistical significance when comparing models at the sub-task level, making it difficult to determine the reliability of the results given the small sample sizes. It is particularly concerning that some tasks, such as PDB and CEO, have fewer than 25 examples, which is insufficient for robust statistical analysis. The small number of examples might lead to overfitting during model training and evaluation, making it difficult to generalize the findings to other datasets or real-world scenarios. Furthermore, the lack of diversity within these small subsets might skew the results, favoring models that are particularly good at memorizing the training data rather than truly understanding the underlying scientific concepts.

**Issues with LMScore**:

- As mentioned in Appendix A, GPT-4 is used as the language model (LM) to compute LMScore. It would be better to use an open-source model, as GPT models are constantly being updated, which may alter evaluation scores over time. Even when specifying a GPT version, it may become deprecated, making it hard to replicate the results. The reliance on a closed-source model like GPT-4 for evaluation introduces a reproducibility issue. The model's internal workings are not transparent, and its performance can vary across different versions, making it difficult to ensure the consistency and reliability of the evaluation process. This lack of transparency also hinders the ability of other researchers to independently verify the results and compare them with their own findings. The use of an open-source model would not only address these reproducibility concerns but also promote broader accessibility and collaboration within the research community.

- Additionally, in Figure 9, the results do not convincingly show that LMScore has a high correlation with human judgment. Therefore, it may be challenging to conclude that LMScore can replace ROUGE. The correlation between LMScore and human judgment, as presented in Figure 9, appears to be weak, raising concerns about the validity of using LMScore as a reliable evaluation metric. The lack of a strong correlation suggests that LMScore may not accurately capture the nuances of human evaluation, particularly in tasks that require complex reasoning and understanding. This discrepancy between LMScore and human judgment undermines the claim that LMScore can serve as a replacement for established metrics like ROUGE, especially in tasks where human evaluation is crucial for assessing the quality of the generated responses.

**Presentation Could Be Clearer**:

- It would be beneficial to include a table that specifically lists the number of questions, the number of questions under each task, and the average number of tokens (or words) in queries, documents, and ground truths. Although this information is scattered across Figure 2(b)(c) and Figure 4(c), consolidating it into a table would enhance clarity. The current presentation of dataset statistics across multiple figures makes it difficult to quickly grasp the key characteristics of the dataset. A consolidated table would not only improve the clarity of the paper but also facilitate a more efficient comparison of the different tasks and their respective complexities. This would be particularly helpful for researchers who are interested in using the dataset for their own experiments.

- Line 269: “On the extraction tasks, such as MPV, HFE, GEO, and DFT-S, experts within each domain reviewed each other’s work and reported a high rate of agreement.” It would be better to provide statistics on the inter-agreement between annotators. The lack of concrete inter-annotator agreement statistics makes it difficult to assess the reliability of the annotations. While the authors mention a high rate of agreement, the absence of specific metrics, such as Cohen's kappa or Fleiss' kappa, makes it challenging to quantify the level of consistency among the annotators. Providing these statistics would enhance the credibility of the dataset and demonstrate the rigor of the annotation process.

### Questions
- I don’t fully understand how LLMsim works. If the goal is to identify the number of dictionaries that are correctly retrieved, why not use an exact match or other metrics commonly used for evaluating retrieval, such as nDCG?

- For each paper, is there only one question asked? The paper is not entirely clear on this point, and it raises the question of whether each paper corresponds to only one question or several questions (similar to Qasper).

- In Figure 4(c), does the average length of 954 words refer to the ground truth, or does it refer to the average length of the model-generated responses?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the CURIE benchmark, designed to evaluate large language models (LLMs) on multitask scientific problem-solving, focusing on long-context understanding and reasoning. CURIE encompasses ten challenging tasks across six scientific disciplines. These tasks require comprehension of extensive context and domain expertise.

The authors assess various LLMs, highlighting that while Claude-3 performs well across domains, models like GPT-4o struggle with specific tasks, such as protein sequencing. The study finds that current models still have significant room for improvement.

### Strengths
- The proposed benchmark focuses on long-context understanding and reasoning in scientific domains, which is relatively unexplored and meaningful for advancing AI4science.
- The paper provides many details and discussion towards the tasks and experiments.

### Weaknesses
1. The presentation of this paper is not clear enough. While the authors spent much space introducing the domains and tasks, the input and output (e.g., format, content) are not explicitly defined, which makes it difficult to understand how the authors evaluate the models. Specifically, the lack of clarity on whether the models are expected to generate structured outputs (like JSON) or free-form text, and how these outputs are parsed for evaluation, is a significant concern. The absence of clear examples of input prompts and expected output formats makes it difficult to reproduce the experiments and understand the scope of the benchmark.
2. The evaluation metrics may not fairly show the performance. The reliance on ROUGE-L and BERTScore may not fully capture the complexity of scientific reasoning. While the authors propose metrics like LLMSim and LMScore, how they extract the answers from open-formatted model outputs and compare the potentially heterogenous answers (e.g., different field name, spelling difference, number/string, with/without extra text) with the gold standard is not clear to me. If not carefully handled, the experimental results might not be reliable. The lack of detail on how these metrics handle variations in model outputs, such as different levels of detail or paraphrasing, raises concerns about the robustness of the evaluation.
3. The experiment analysis does not provide many deep and insightful observations. The analysis primarily focuses on overall performance scores, without delving into specific error patterns or failure modes of the models. There is a lack of qualitative analysis to understand why certain models perform better on specific tasks, and what specific challenges each task presents to the models.

### Questions
1. Could the authors explain more about how you define the input and output format?
2. What is your method to evaluate the free-form generation?
3. What are the approaches for quality control?

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
This paper introduces a benchmark called Curie for evaluating Large Language Models (LLMs) on science-related tasks in the disciplines of material science, condensed matter physics, quantum computing, geospatial analysis, biodiversity, and proteins. The benchmark includes 434 examples taken from 273 research papers related to the previously mentioned scientific disciplines. Based on those examples, tasks were created and used to evaluate several LLMs.

### Strengths
- The paper is well-written.
- The paper provides a helpful benchmark for evaluating LLMs in science-related tasks.

### Weaknesses
 - There is no comparison with the baseline case of just inserting the task description into the LLM prompts without providing the paper. It would be useful to see what the results would be in that case.
- Only 6 very specific disciplines (material science, condensed matter physics, quantum computing, geospatial analysis, biodiversity, and proteins) are considered in this dataset. This limits the scientific domain in which LLMs can be tested.
- The dataset construction requires human annotations. This makes scaling up the dataset challenging. 
- Typo line 339: "precison" -> "precision"

### Questions
- Have the authors considered inserting the task description into the LLM prompts without providing the paper? How would that compare with the CURIE method? 
- Have the authors considered adding more tasks from a wider range of disciplines as future work?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces CURIE, a benchmark for evaluating LLMs on scientific problem-solving that requires understanding long-context information and multi-step reasoning across six disciplines: materials science, condensed matter physics, quantum computing, geospatial analysis, biodiversity, and proteins. CURIE includes 434 tasks derived from 273 scientific papers, covering realistic scientific workflows such as information extraction, concept tracking, aggregation, algebraic manipulation, and multimodal understanding. This benchmark evaluates eight state-of-the-art models, revealing significant performance gaps, especially in tasks like protein sequencing. The paper aims to foster advances in LLM capabilities for scientific applications.

### Strengths
1. The paper proposed a new long-context scienceQA benchmark CURIE, containing 434 examples from 273 science literatures in different disciplines. The tasks are carefully collected and benchmarked with the help of domain experts.

2. The paper provided a detailed experimental analysis and many meaningful discussions about the challenges LLMs face in long-context scientific reasoning, especially regarding tasks like protein sequencing and geospatial data extraction, where complex, multi-step reasoning and domain-specific knowledge are crucial. The appendix also included many details for benchmark construction, examples, and case studies, helping readers better understand the annotation process and challenges of the tasks.

3. The paper is well-written and easy to follow. I really appreciate the experts' efforts for annotation and the authors' contribution for conducting this research, and believe this benchmark would be beneficial for both developing better LLMs and better usage of LLM for scientific research.

### Weaknesses
1. I'm not sure if LLMs could have seen some of these research papers, which might affect the effectiveness of evaluation results on CURIE. A figure showing the comparison / correlation of performance between CURIE and other scientificQA / long-context QA benchmark would resolve this concern more clearly.

2. I think one of the challenge of such benchmarks should be the difficulty of scaling up? Due to the static manner and limited scale, public papers might be included within future (or existing) corpus for LLM training. I wonder if the authors considered to somehow automatically scale up the dataset, or keep updating the examples?

### Questions
See "weakness". I've listed my questions there.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new benchmark for long context understanding, reasoning and information extraction of different scientific tasks and evaluates the current state-of-the-art LLMs on it. It has 10 tasks split on 6 disciplines which are labeled by domain experts. 
The authors also introduce a new LLM-based evaluation metric and use it along with evaluation established metrics. They also employed domain experts to evaluate the LLM predictions on a sample of the dataset.

### Strengths
- This work introduces a novel dataset with challenging tasks from different disciplines and evaluates different state-of-the-art LLMs and shows where they lack. I appreciate the effort that has went into building this dataset. I understand that this required time from domain-experts from different disciplines to label it. They have employed domain experts to make sure they have a reliable evaluation on the predictions of the dataset
- Having benchmarks for complex scientific domains is important for the improvement of language models
- The paper is well written and the message is conveyed clearly

### Weaknesses
 - For some tasks there are not many examples
- As you mention, these answers are open-ended and it’s hard to evaluate the model’s output. A model may have a correct output but have used different set of steps or a different notation to answer. Having Latex as the ground-truth will also make it harder to evaluate. This will be less of an issue in the extraction tasks and more of an issue in tasks that require planning/reasoning. I understand that you use ROUGE-L/BERTScore F1, but I still think the performance may be unreliable for some of these tasks
- LLMSim/LMScore which follow LLM as a judge paradigm can also have their shortcomings. I would suggest adding multiple choices where it makes sense in this dataset. Even though you won’t be evaluating the expressiveness of the language model, it will be easier to judge the LLM’s knowledge using accuracy as a score which is interpretable
- Asking for the LLM to come up with an open-ended dictionary will make it harder to evaluate and map the generated dictionary keys to the ground truth keys as you do with LLMSim
- Since this dataset is cross-domain and requires such a specialized knowledge for each domain, it would be challenging to build a good model that performs consistently good across the different domains. Instead, a dataset that is focused on a specific domain and is more thorough would be better

### Questions
- Have you considered making more specific questions? For example, in Figure 3 the DFT example where you ask to identify all the input structures and this expects a big dictionary, can you make multiple questions instead for each key of the dictionary? 
Would it make sense to provide only the keys of the dictionary and ask it to complete?
- When you say 434 examples curated from 273 research papers, what would an example entail? 
- Since this benchmark is also about evaluating models in long contexts, a plot of the model performance as a function of the context length would be interesting  
- Figure 18 needs bigger font size for the axis labels

### Soundness
3

### Presentation
3

### Contribution
3
