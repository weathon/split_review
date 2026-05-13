# SysBench: Can LLMs Follow System Message?

- Decision: Accept
- Scores: 6, 3, 6

## Abstract
Large Language Models (LLMs) have become instrumental across various applications, with the customization of these models to specific scenarios becoming increasingly critical. System message, a fundamental component of LLMs, is consist of carefully crafted instructions that guide the behavior of model to meet intended goals. Despite the recognized potential of system messages to optimize AI-driven solutions,  there is a notable absence of a comprehensive benchmark for evaluating how well LLMs follow system messages. To fill this gap, we introduce SysBench, a benchmark that systematically analyzes system message following ability in terms of three limitations of existing LLMs: constraint violation, instruction misjudgement and multi-turn instability. Specifically, we manually construct evaluation dataset based on six prevalent types of constraints, including 500 tailor-designed system messages and multi-turn user conversations covering various interaction relationships. Additionally, we develop a comprehensive evaluation protocol to measure model performance. Finally, we conduct extensive evaluation across various existing LLMs, measuring their ability to follow specified constraints given in system messages. The results highlight both the strengths and weaknesses of existing models, offering key insights and directions for future research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a benchmark  for evaluating how well LLMs follow `system messages.` The authors study three dimensions: 1) constraint violation, 2) instruction mis-judgement/ill-following, and multi-turn (in)stability. The work includes a dataset of 500 system messages with 5-round conversations each, and an evaluation protocol. The authors study 16 LLMs and provide a detailed analysis for the performance.

### Strengths
- (to-date) First systematic benchmark for system message following capabilities that appears in the submission. The research seems well-motivated by real-world applications and security concerns.
- Good task type and domain coverage (Figure 3, Table 1), and three-level granularity metrics (CSR, ISR, SSR) for evaluation. The dataset seems to have a balanced distribution. 
- Offers an overview of performance comparison across models on different types of sys message constraint types. (Figure 4).

### Weaknesses
 - While the paper throughly evaluates how well LLMs follow system messages and identifies various issues (constraint violations, instruction misjudgment, and multi-turn instability), it doesn't translate these findings into (potential) practical guidelines for practitioners. If for (Figure 4), that the Style constraints tend to be worse followed than other types; or that the performance degrades over multiple turns, I believe the audience usually expect some attempts to provide mitigation strategies or recommendations. 

- Missing justification or citations for line 194--195, and the reliance on GPT-4o as the sole verifier: 
> For instance, GPT-4o (OpenAI, 2024) verifier achieves over 94% consistency with human evaluations. 
I wonder is this statistics based on your own human study? I found this sentence unclear.

Generally, reliance on GPT-4o as verifier raises concerns, where works identified biases [1] [2]. Is there cases where the verifier may fail? Inclusion of strong open-source models like Llama3.1-405B could be a major inclusion. Human verification could also be valuable.

### Questions
- Do you see degradation in multi-turn conversations is due to the accumulation of errors or genuine forgetting of system constraints?
- Given your findings about instruction alignment, what recommendations would you make for designing system messages that are more robust against misaligned instructions?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper creates SysBench, a collection of 500 system prompts collected from the web to test the ability of different LLMs to follow system prompts. An evaluation is conducted on 16 open and proprietary LLMs. Results show bigger / proprietary models show better performance. Additionally, the paper explains the cause of the failure, by the lack of attention given to the system prompt.

### Strengths
1. system messages are of increasing importance, especially in applications. Chat applications from big techs (Chatgpt, Claude, etc.) come with very long system messages to make them function in desired behaviors. The paper proposes a benchmark to evaluate such capability which may direct the interest of the research community towards system message following LLMs. 

2. the paper makes effort to explain the performance gap between language models by analyzing the attention layer of different models.

### Weaknesses
1. In section 3.2, the paper mentions, “We initially collect thousands of system messages from online logs, and filter out duplicate and noisy data based on heuristic rules and clustering.” more explanation should be provided on the dataset construction process. Examples of " annotation guidelines designed by experts" and demographics of the 21 trained data annotators may be provided in the appendix to support this. 

2. In section 3.2, the paper mentions that each system message is related to 2-3 system constraints, hence presenting a moderate level of complexity.  However, compared to page-long system prompts often used from big techs, 2-3 system constraints look a bit short. 

3. The paper lacks a detailed analysis on the performance of different models. Figure 3 breaks down the dataset into different domains, but this does not seem to be reflected in the evaluation.

4. Another widely used application for system messages is safety. Chat applications often want the model to refuse to respond to some user instructions. The benchmark could have been better by including such examples. 

5. Analysis between attention distribution and performance is very interesting. However, the paper only presents if for three models. It would have been insightful if the results for other models were also included in the appendix. 

6. An error analysis on when models fail can be added to provide more insight on improving models in system message following.

### Questions
see weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presents SysBench - a collection of 500 conversations with different system prompts used to evaluate whether models adhere to constraints laid out in the system prompt. The authors break this dataset into two categories: parallel and dependent. In parallel cases, each turn of the conversation could be modeled separately while in dependent cases later responses depend on earlier turns of conversation. The authors then evaluates a wide range of Language Models on their adherence to the system prompt constraints, using GPT-4o to judge constraint adherence. The aggregate these GPT-4o decisions into 3 metrics based on individual constraint adherence (termed CSR), turn-level complete constraint adherence (termed ISR), and conversation level adherence (termed SSR). Finally, they analyze how adherence varies across different types of constraint, as the conversation progresses, and how attention correlates with adherence to prompt constraints.

### Strengths
- Most chatbots are used in multi-turn settings and coherence to system prompts across these seems to be a reasonable extension to work such as IFEval. The authors correctly identify that benchmarking and evaluation in this space seems somewhat lacking v.s. single turn evaluations by comparison.

- If I assume reliability of the LLM-as-a-judge procedure, the investigative analyses in section 4.5 are quite interesting, especially those showing that the distinction between system and user prompt seems to be minimally impactful on results. Understanding at a deeper level what leads to adherence to system prompt instructions seems to be a meaningful basis for developing improvements to adherence.

### Weaknesses
Post Discussion Update: Thanks to the authors for their efforts running the cross-model bias comparison and responding to my other points. These responses and additional experiments indeed improve the work. My primary concern is that there still is not statistical significance testing, but overall I think this work is a relatively sound contribution to the space and generally would lean towards an accept decision.

- This benchmark is relatively small size and many of the metrics rely on chains of LLM inference to compute. Combined, these factors seem likely to risk many of the results in the work might not be statistically significant. However, at present the authors don't perform any significance testing on the results.

- The metrics in this work rely entirely on an LLM as a Judge procedure without evaluating or reporting how well correlated the procedure is with human judgement in this context. Furthermore, the work uses only a single closed-source model for this judge which is likely to be biased to specific factors of LLM responses. Without confirmation that these results are either strongly correlated with human judgement or that these results are consistent across LLM Judges from different model families, it doesn't yet seem to have been showed that this evaluation returns a consistent and meaningful metric.

- The description of the data generation process does not explicitly lay out many key details. The source of the original prompts, the mechanisms used to verify data, and the level of synthetic data generation in the creation process is all somewhat vague. I've placed concrete questions in these topics below.

### Questions
- How much does the ordering of models depend on the choice of LLM as a Judge and the prompt provided? For example, is the benchmark self correlated if you use any other model (e.g. Claude/Llama/Qwen/Gemini) rather than GPT-4o as the judge?

- In the dependent setting, how do assure that "User" responses are appropriately contextualized to be dependent on what the system responded? If they are also just static responses from the initial data collection, this seems a mismatch to the expectations of the "dependent" setting.

- Section 3.2 " All data are checked independently by multiple experts in multiple rounds to ensure quality." What are the agreement metrics amongst different annotators who checked these independently? How were disagreements resolved? How many annotators checked each example? This will give readers empirical measures of how robust and consistent the decisions made in constructing these datasets were. Reporting an agreement measure such

- In Section 3.2, you reference "from online logs". Where exactly do these come from? Is it from LmSysChat or some other public resource? Since these are the foundation of your dataset, explaining their origin and the data gathering process seems essential.

- Section 3.2 "For each system message, we collect corresponding user conversations and use GPT-4o to assist in generating conversations." This is unclear to me. Are the conversations collected from users or generated by GPT-4o? If they were not generated by GPT-4o, what level of assistance did this model provide? Again, this data is the foundation of all the following results so explaining how and where GPT-4o was used for assistance is critical.

- Section 3.3. " To ensure that LLMs can objectively and accurately assess the constraint satisfaction conditions, we manually annotated evaluation checklists". What was the agreement between the LLM-as-a-judge and the manual annotations? What metric shows that the LLM as a judge procedure is reliable in this setup?

### Soundness
3

### Presentation
3

### Contribution
3
