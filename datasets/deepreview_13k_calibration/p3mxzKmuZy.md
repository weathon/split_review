# A Benchmark for Semantic Sensitive Information in LLMs Outputs

- Decision: Accept
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Large language models (LLMs) can output sensitive information, which has emerged as a novel safety concern. Previous works focus on structured sensitive information (e.g. personal identifiable information). However, we notice that sensitive information in LLMs’ outputs can also be at the semantic level, i.e. semantic sensitive information (SemSI). Particularly, simple natural questions can let state-of-the-art (SOTA) LLMs output SemSI. Compared to previous work of structured sensitive information in LLM’s outputs, SemSI are hard to define and are rarely studied. Therefore, we propose a novel and large-scale investigation on SemSI for SOTA LLMs. First, we construct a comprehensive and labeled dataset of semantic sensitive information, SemSI-Set, by including three typical categories of SemSI. Then, we propose a large-scale benchmark, SemSI-Bench, to systematically evaluate semantic sensitive information in 25 SOTA LLMs. Our
finding reveals that SemSI widely exists in SOTA LLMs’ outputs by querying with simple natural questions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the concept of semantic sensitive information (SemSI) in large language model outputs. The author differentiate SemSI from structured sensitive information e.g., PII, phone number, email etc., which has clear structure for regex extraction. SemSI focuses on information that could be harmful at a semantic level and unstructured. The authors define a taxonomy for SemSI, and devyelop SemSI-Set, a dataset of non-adversarial simple natural prompts from various source of news articles. The authors also use this benchmark to evaluate 25 LLMs' propensity to generate such content using three metrics: occurrence rate, toxicity score, and coverage. Their evaluation reveals that SemSI is prevalent across modern LLMs, with around 30-50% of outputs containing semantic sensitive information even without explicit prompting. The work provides a systematic framework for measuring and understanding semantic sensitivity in LLM outputs.

### Strengths
The paper introduces a new viewpoint of LLM safety by investigating into the subtle but potentially harmful semantic information in the LLM outputs. The paper provides a taxonomy and definition of SemSI, and constructs a benchmark dataset with non-adversarial simple natural questions, and evaluate and analyze a wide range (25) state-of-the-art LLMs with a set of newly defined metrics. The analysis reveals how easily LLMs can generate potentially harmful content even in he everyday usage (non-adversarial setting).

### Weaknesses
1. The definition of the taxonomy categorization is not clear enough. Overall I think the categorization is good, but I think section 2.2 mostly focuses on why these categories are important rather than define exactly what they are. For example, sensitive identity attributes, how can we differentiate from structured sensitive information? And how can we differentiate it from very well known fact which should not be sensitive information?
2. The validity of the evaluation outcome is questionable. The main concern is as the following:
    - The quality of human annotation is not discussed at all. The paper tries to use human annotation to validate the accuracy of GPT4. However, given the under-specified definition of each of these categories, the human annotation quality need to investigated and discussed. For example, what is the inter annotator agreement? Is that good enough? How the scores are aggregated from 5 annotators? etc.
    - The accuracy of using GPT4 as judge for final evaluation is questionable. I appreciate authors try to valid how GPT4 compare to human in section 3.3, however, I don't think the validation is done with actual (and diverse) LLM output. Directly apply GPT4 as judge for 25 downstream LLMs raise the concern about the validity of the results.
I would encourage authors to expand on the human verification section, coz this is where we prove the final evaluation results are trustworthy. 
3. The paper claim one of the contribution (line 466) is to have a compressed benchmark (SemSI-cSet) to save money and time, however, the procedure on the compressing is completely missing from the paper. How is the compressing done? What is the impact on various of LLMs (besides GPT3.5 and GPT4 in Table2)? Why only validate on these two LLMs?

### Questions
1. How do we differentiate the information already known to public (e.g., Joe Biden is US president) from the actual privacy? This seems to be under-specified in the paper. 
2. For Table 3, on what sets are you computing the alignment between human and GPT-4o? Since  you have "priori" annotation and "posteriori" verification annotation, which of them corresponding to which metrics?
3. How do you make the core set of the benchmark? Random sampling or something else?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the issue of semantic sensitive information in LLMs' responses to natural questions, which is harder to detect compared to traditional notion of sensitive information such as PII. The paper introduces a labeled dataset of semantic sensitive information and provides a benchmark to evaluate leakage in SOTA LLMs. 

The authors suggest that there are a few key issues with semantic sensitive information, including the lack of definition, lack of labeled datasets, and contextually dependent nature of the ground truth. The authors propose 3 categories of semantic sensitive information: Sensitive identity attributes, Reputation-harmful contents, and Incorrect hazardous information, and 3 metrics for measuring LLM outputs: occurrence rate, toxicity score, and coverage.

### Strengths
1. This paper provides a straightforward pipeline to develop an automatically labeled dataset for semantically sensitive information in LLM responses and manually validate the quality of the automatic labels on 100 samples. The dataset could be a helpful resource for future work.

2. The paper proposed a set of fine-grained metrics for semantic sensitive information leakage based on a taxonomy, focusing on the presence, toxicity, and lengths of sensitive information. 

3. The paper thoroughly benchmark existing LLMs on the proposed metrics and found that existing models are bad at safeguarding against sensitive information.

4. The paper provides comprehensive analysis on the benchmarking results by metrics and data sample content categories.

5. The paper's organization is straightforward and easy to read.

### Weaknesses
 1. As the authors pointed out in the introduction, it is extremely hard to define semantically sensitive information. But the human verification results in Table 1 is surprisingly high. This makes me question the difficulty of the labeling task. It would be helpful to provide inter-annotator agreements on for both the a priori labeling and a posteriori verification to contextualize the accuracies provided in Table 1.

2. The analysis sections (4.3 and 4.4) report and summarize results. What is the main claim/finding? The analysis is aiming to get at the causes of the SemSI, but the claims are mostly speculations and are not convincing or rigorously supported by the results. More detailed explanations and insights into the results would strengthen the point of the paper.

3. Finding 4 is not surprising since T is defined to be 0 when B=0. I am not sure what is the point of this claim.

4. Finding 5: the explanations provided seem weak. The existence of lawsuits could be relevant, but the correlation of metrics could be due to multiple other factors, such as labeler bias. The second part about the high occurrence of I-SemSI in older models can also benefit from better explanations. E.g. "I-SemSI is found to occur with higher frequency in models released before the timestamp of the hot news in the prompt, validating the benchmark's ability to detect incorrect and hazardous information."

5. Overall, there are some typos and ambiguous sentences in the paper that requires further editing, see Questions section.

### Questions
1. > "Compared to structured sensitive information which focuses on fragmented or granular phrases, it concentrates on highlighting its semantic substance." (ln. 096-097)
    - This sentence is confusing, what is "it" and what is "its"?

2. > "SemSI is a new, less concerned, but serious safety issue in today’s LLMs outputs." (ln.100)

    - What does less concerned mean? Do you mean underexplored?

3. Taxonomy of SemSI: is this taxonomy grounded in prior theory? How do you make sure that it is comprehensive? If this list is not meant to be comprehensive, it should not be called a taxonomy.

4. > "public figures suffer the most from SemSI" (ln. 402)

    - It is worth discussing if it is information on a public figure, then should SemSI be defined differently?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors introduce an evaluation framework designed to assess the presence and relevance of sensitive information within the outputs generated by Large Language Models (LLMs). The authors aim to address critical concerns regarding privacy, ethics, and bias that are inherent when LLMs produce content which might contain sensitive data. This benchmark is crucial for ensuring that these models adhere to ethical standards and legal requirements in various applications such as healthcare, finance, and law. The contributions of this paper include the development of a systematic methodology for identifying and measuring semantic sensitivity in text outputs from LLMs. It likely outlines specific metrics or indicators that can be used to evaluate how sensitive information is handled by these models.

### Strengths
1. The paper maintains high clarity throughout, making it accessible to both researchers familiar with the field and those who are new to it. The authors have provided clear definitions for all terms used, which helps in understanding their context-specific meanings. 

2. The authors have conducted extensive research into existing benchmarks and methodologies for evaluating LLMs.

### Weaknesses
1. The innovative aspect of the proposed method appears to be somewhat constrained, as numerous studies have already been conducted on diverse evaluation tasks. Despite the authors' extensive experimentation, there is a noticeable absence of substantial contributions to the evaluation methodology itself.


### Questions
How do the results of Llama3-8B compare to those of the 70B model?

### Soundness
3

### Presentation
3

### Contribution
2
