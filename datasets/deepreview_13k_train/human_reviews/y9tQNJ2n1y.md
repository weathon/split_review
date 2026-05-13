# CASE-Bench: Context-Aware Safety Evaluation Benchmark for Large Language Models

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Aligning large language models (LLMs) with human values is essential for their safe deployment and widespread adoption. Current LLM safety benchmarks often focus solely on the refusal of individual problematic queries, which overlooks the importance of the context where the query occurs and may cause undesired refusal of queries under safe contexts that diminish user experience. Addressing this gap, we introduce CASE-Bench, a Context-Aware Safety Evaluation Benchmark that integrates context into safety assessments of LLMs. CASE-Bench assigns distinct, formally described contexts to categorized queries based on Contextual Integrity theory. Additionally, in contrast to previous studies which mainly rely on majority voting from just a few annotators, we recruited a sufficient number of annotators necessary to ensure the detection of statistically significant differences among the experimental conditions based on power analysis. Our extensive analysis using CASE-Bench on various open-source and commercial LLMs reveals a substantial and significant influence of context on human judgments ($p<$0.0001 from a z-test), underscoring the necessity of context in safety evaluations. We also identify notable mismatches between human judgments and LLM responses, particularly in commercial models within safe contexts. Code and data used in the paper are available at https://anonymous.4open.science/r/CASEBench-D5DB.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
- The paper develops a benchmark for evaluating LLMs’ refusal accuracy for problematic queries. The key point of differentiation is that the authors focus on “context.” This is the idea that auxiliary information might change whether or not an LLM should refuse to answer a query.  
- The paper evaluates a range of LLMs on this benchmark, and finds that LLMs are generally over-moderated.
- They also conduct an extensive survey of individuals to measure how context influences perceptions regarding when LLMs should refuse to answer.

### Strengths
- Overall the paper is extremely well-written and clear.
- The core idea tackled by the paper–understanding how context might (or should) affect answer/decline decisions by LLMs–is interesting.
- The study methodology is extremely rigorous. 
- The experiments are also well-done and interesting.

### Weaknesses
 - The paper tries to ground in the formal framework offered by contextual integrity (CI) theory. Section 2 and 3.1 spend time discussing CI and mapping it to LLMs. But its not obvious why CI is helpful here or the extent to which CI is even used in the construction of the benchmark? As best I can tell, CI is explained in the prompt used to generate conversational contexts. But it isn’t clear whether that’s necessary, or whether GPT-4o is even using that information. And the paper also mentions that all contexts were revised by the authors themselves.
- The primary contribution (from a data perspective) would seem to be the different contexts the authors define–especially as the queries themselves come from existing work. The paper doesn’t really discuss what these contexts look like, how they were crafted, or how often they repeat across the different queries?

### Questions
- Do the authors have any information on the identities/demographics of their human annotators? Ignoring settings where LLMs should decline to respond because of legal liability, the choice of whether an LLM should respond/decline seems entirely subjective. Different individuals will have different assessments, because of their personal politics, religious beliefs, cultural backgrounds, and more. So largely, this benchmark would seem to measure acceptance/decline accuracies grounded against the specific human pool the authors surveyed. Having more information about this pool would be helpful!   
- The underlying message of the paper is that context matters in determining whether an LLM should respond to a query. For instance, an LLM intended to train medical professionals should probably respond to medical questions. Why is it fair, then, to evaluate LLMs like GPT-4o-mini or Claude, which are intended to be used in the “layperson chatbot” context? I’m not sure I see why merely providing a “context” to these chatbots should actually alter their behavior. Given that a prevailing concern with these models is that users might employ deception to elicit responses from the models that developers do not desire (i.e., via jailbreaking or prompt-engineering)–shouldn’t these LLMs also decline to respond when the context is provided? The argument that these LLMs should respond when context is provided presumes that users will always be truthful when providing information in the prompt. 
- Could the authors share more information on the contexts?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper puts forth CASE-Bench, a Context-Aware Safety Evaluation Benchmark which integrates context into subsequent safety assessments of LLMs. The benchmark boasts 900 distinct contexts with queries from 45 different categories.

### Strengths
- extensive benchmark collection, with 900 distinct contexts with queries from 45 different categories.
- the inheritance of contextual integrity theory is interesting and well motivated
- over 47K human annotations from over 2K annotators, resulting in a high quality dataset

### Weaknesses
 - the data was created with gpt-4o, bringing into question the potential for commercial use
- explanation of limitations is lacking, would be good to delve into potential areas for improvement or future work

### Questions
1. How reproducible is the automatic content generation with an open source model? Have you tried this?
2. Manual revision process appears to be expensive. Were there attempt to automate this? If so, with what level of success?

### Soundness
2

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
This paper introduces CASE-Bench, a context-aware benchmark for evaluating LLM safety. The main innovation is incorporating context into safety assessments using Contextual Integrity theory. The study validates the significant impact of context on safety judgments through large-scale human annotation (2000+ annotators) and evaluates several open-source and commercial LLMs on this benchmark.

### Strengths
1. The paper identifies a key issue in current LLM safety evaluations: too much focus on rejecting single queries without considering context, which can lead to LLMs over-rejecting legitimate requests.
2. The research methodology is solid, using Contextual Integrity theory to formalize context, power analysis to determine annotator numbers, and various statistical methods to verify result significance.
3. The dataset creation process is thorough, with 900 query-context pairs, 21 annotators per task, and robust quality control measures.

### Weaknesses
1. I wonder how the authors address this potential issue: many current jailbreaking techniques [1,2] actually work by creating "safe-looking" contexts to trick LLMs into generating dangerous content. Could context-based safety evaluation create new security risks?
2. Regarding metrics, the paper mainly uses basic measures like accuracy and recall. Have the authors considered adding more detailed analysis, like measuring the impact of different types of errors?
3. From a practical standpoint, I'm curious about the authors' thoughts on how to integrate this context-based evaluation approach into real-world LLM safety mechanisms?

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the problem of understanding whether a prompt/prompt reply is problematic or not given a particular context. It proposes that not all responses are problematic and some responses are problematic only if they are in a particular context. As such, it creates a dataset on 45 different categories, all with positive and problematic context. The dataset is used to evaluate state of the art models and also alignment/agreement with human annotators.

### Strengths
A thorough analysis of the influence of context in deciding whether a prompt/prompt response is problematic
A dataset that may be useful for other research

### Weaknesses
I'm personally not convinced that the context should dictate the perceived harm in a prompt/prompt response. A malicious actor could always fake a positive intent/context to get the information they want and create harm. As such, I find the premise/motivation of the work weak.

### Questions
1. In which use-cases you find the differentiation by context important/useful?
2. How can malicious actors that fake positive intent could be detected?
3. In the results in Fig. 3, if I understand correctly, some unsafe contexts lead some categories to rated by humans as safe. That's unexpected and counterintuitive (categories between 10-20 on the x axis). Do you have an explanation for this? Can you share some examples from this category (I couldn't find any)?

### Soundness
3

### Presentation
2

### Contribution
2
