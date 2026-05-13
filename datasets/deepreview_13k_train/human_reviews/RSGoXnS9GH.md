# FairMT-Bench: Benchmarking Fairness for Multi-turn Dialogue in Conversational LLMs

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
The growing use of large language model (LLM)-based chatbots has raised concerns about fairness, particularly in multi-turn dialogues where context accumulation can lead to biased or harmful responses. While existing fairness benchmarks mainly focus on single-turn interactions, multi-turn scenarios present greater challenges due to conversational complexity and potential bias accumulation. In this paper, we propose a comprehensive fairness benchmark for LLMs in multi-turn dialogue settings. We categorize common multi-turn attack techniques and develop a three-tier hierarchical evaluation framework to assess fairness. Using data from HolisticBias, RedditBias, and Jigsaw, we construct a dataset that includes stereotypes and toxicity across seven demographic groups. GPT-4 is employed for generating and evaluating multi-turn dialogues, alongside bias classifiers and human validation to ensure robustness. This benchmark offers a novel approach to assessing and improving fairness in LLMs within more realistic, multi-turn dialogue contexts.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a fairness benchmark designed for multi-turn dialogues, called FairMT-Bench. Then, it detailed the experiments and analysis with multiple SOTA LLMs across dimensions like tasks, dialogue turns, bias types and attributes. It carefully analyzed the results and pointed out the areas where LLMs fail to maintain a stable fairness. For example, LLMs tend to perform worse on fairness in multi-turn dialogues than single turn. Moreover, the paper proposes a more challenging fairness evaluation dataset, FairMT-1K, that contains examples LLMs perform worst on.

### Strengths
1. The paper contributes a novel fairness benchmark specifically for multi-turn dialogues, while current benchmarks primarily focus on single-turn dialogues.

2. The paper extensively benchmarks on most popular LLMs, and provides detailed results and analysis across many dimensions, like tasks, dialogue turns, bias types and attributes. The paper comprehensively demonstrates each LLM's performance, and pinpoints the areas where fairness is challenging to LLMs. The results show that fairness, especially in multi-turn dialogues, is still a challenging task for LLMs.

3. The paper has great presentation. The figures are very illustrative and insightful.

### Weaknesses
1. A few factors can make the evaluation computationally expensive: (1) using GPT-4 as the evaluator (2) the multi-turn nature of the data and the evaluation process (3) the data size. It would be great if the paper can include some discussion on evaluation cost.

2. While the paper discusses diverse sources and dimensions of bias, it does not discuss potential mitigation strategies. Offering even preliminary solutions or suggestions for future research directions would be valuable.

3. As fairness and quality can be contradictory metrics, models that perform well on fairness might sacrifice its quality. Therefore, it'd be better to add a model quality dimension in the analysis, for a more comprehensive and insightful comparison of the models.

4. The distribution of different tasks needs more clarification. I couldn't find the numbers of each task in the paper. Could the authors point me to the numbers if they are present in the paper, or add this information if they are absent?

### Questions
1. When constructing the more challenging subset (FairMT 1K), the six models may diverge in scores. So how did you use the model results to select the examples?

2. Typos:
  1) Line 368, should be "multi-turn dialogues generally show higher bias rates"?
  2) Figure 4, (a) and (b) look the same, which I assume is not intended?

3. As mentioned above, could the authors clarify the number of examples allocated to each task in the FairMT-10K dataset?

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
4

### Summary
This paper introduces "FairMT-Bench," a comprehensive benchmark to evaluate fairness in LLMs, specifically in multi-turn dialogue scenarios. Addressing a gap in fairness assessments, which have primarily focused on single-turn interactions, the paper provides a dataset (FairMT-10K) and tasks that target fairness across three stages of dialogue complexity: context understanding, user interaction, and instruction trade-offs. The authors also present a distilled, challenging subset, FairMT-1K, and use both GPT-4 and Llama-Guard-3 classifiers, alongside human validation, to benchmark fairness in 15 LLMs, revealing substantial limitations in current model fairness across multi-turn interactions.

### Strengths
1. Novel Focus on Multi-Turn Fairness Evaluation: The paper addresses the crucial gap of multi-turn dialogue fairness, reflecting real-world complexities in conversational AI use cases.
2. FairMT-Bench and its datasets (FairMT-10K and FairMT-1K) cover a wide array of bias types and attributes, providing a rich resource for fairness research.
3. By evaluating 15 prominent LLMs, the paper provides a robust, comparative analysis of model fairness, offering valuable insights for future LLM alignment improvements.
3. Employing both GPT-4 and Llama-Guard-3 as fairness evaluators, along with detailed experimental setups, enhances reproducibility and contributes essential tools for future fairness research.

### Weaknesses
1. While the multi-turn focus is novel, the evaluation method largely depends on established LLM tools (e.g., GPT-4 as a judge), which may limit innovation in developing new fairness detection methodologies. Specifically, relying on GPT-4, a model known to exhibit its own biases, introduces a potential confound in the evaluation process. The paper does not sufficiently address how the inherent biases of GPT-4 might skew the fairness assessments, particularly when GPT-4 is used both for generating synthetic data and evaluating model responses.
2. The paper does not thoroughly explore why certain attributes (like gender and race) showed consistently poor performance across models, missing an opportunity to deepen the community’s understanding of these biases. It is not clear if the observed performance discrepancies are due to data distribution issues within the benchmark or if they reflect fundamental limitations in how current LLMs handle these sensitive attributes. A deeper analysis of the error patterns and specific failure cases is needed to understand the root causes.
3. Relying heavily on GPT-4 for generating synthetic dialogue data could introduce bias from the generative model itself, which might impact the generalizability of FairMT-10K and FairMT-1K to real-world scenarios. The paper does not provide a detailed analysis of the potential biases introduced by GPT-4 during data generation, nor does it explore alternative methods for generating more diverse and less biased dialogue data. This reliance on a single generative model raises concerns about the robustness and representativeness of the benchmark.

### Questions
1. How do you ensure that biases from GPT-4, which is used to generate and evaluate responses, do not affect the fairness outcomes, particularly given GPT-4's role as both data generator and evaluator?
2. Can you clarify if the performance discrepancies across bias attributes are due to data distribution differences or model-specific limitations?
3. Lack of comparison with existing evaluation, such as S-Eval or more recent fair-related work.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work highlights the motivation of studying fairness in multi-turn dialogue scenarios and pinpoint the current scarcity of relevant research and resources in this domain. To address these limitations, the authors construct a comprehensive multi-turn dialogue benchmark to evaluate LLM fairness capabilities across two bias types and six bias attributes. Through detailed experiments and analysis, the paper reveal fairness shortcomings in current LLMs.

### Strengths
1. **Valuable Resources**
This paper first presents a fairness benchmark in multi-turn dialogue scenarios, covering diverse bias types and attributes.
2. **Extensive Experiments**
Conduct comprehensive experiments on current SOTA LLMs across six designed tasks.
3. **Reliable Evaluation**
Use GPT4 as a Judge, alongside bias classifiers including Llama3-Guard-3 and human validation.
4. **Comprehensive Analysis**
Analyze evaluation results of single-turn and multi-turn dialogue across different models, tasks, and groups.
5. **Valuable Insights** 
Reveal two distinct bias defense mechanisms for current LLMs, which target defense implicit biases and explicit biases respectively.

### Weaknesses
 **Ambiguous Task Taxonomy**
In Section 3.2, two taxonomies about fairness tasks are primarily discussed: comprehension-focused tasks VS. bias-resistance tasks (Line 318-320) and implicit biases VS. explicit biases (Line 322-323). These taxonomies are clear and reasonable. However, the taxonomy outlined in section 2.1 lacks clarity and mention. The naming of "interaction fairness" class is somewhat confusing, and the boundaries between this class and the other two are not clearly defined. Specifically, the distinction between 'Interaction Fairness' and 'Fairness Trade-off' is not immediately apparent. Both seem to address the model's ability to handle bias, but the specific criteria that differentiate them are not sufficiently explained. For instance, it's unclear what specific types of interactions would fall under 'Interaction Fairness' but not 'Fairness Trade-off', and vice versa. This lack of clarity makes it difficult to understand the purpose and scope of each category, and how they contribute to the overall evaluation of fairness in multi-turn dialogues.

### Questions
**Consider Maintaining Consistency Between the Taxonomy Definition Section and the Analysis Section**
In my opinion, the taxonomy outlined in Section 2.1 is less clear than the two taxonomies presented in Section 3.2. I suggest adopting a more straightforward and understandable classification for tasks definitions. If modifying the definitions is not feasible, at the very least, please ensure consistency between the classifications used in the definition and analysis sections.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents the first fairness benchmark Fair-MT  for multi-turn dialogues because prior works can only consider single-turn scenarios.

This benchmark includes two bias types (Stereotype and Toxicity) and six bias attributes (gender, race, religion, race, etc.) and up to 10K items.  The authors first collected source data from RedditBias, SCIB, and HateXplain.  Then, the authors use GPT-4 to construct the dataset for the identified six tasks ( 2 tasks per LLM capacity). Finally, the authors mainly use GPT-4 to evaluate the fairness of LLM candidates.

### Strengths
1. This work has a well-defined task taxonomy, which is clear and comprehensive.
2. Unlike previous single-turn works, this work presents the first multi-turn fairness benchmark. Multi-turn has more practical significance and research value.
3. Six multi-turn dialogue tasks are proposed to detect the fine-grained fairness of LLMs.
4. LLMs can automatically accomplish most tasks related to dataset construction and evaluations. 
5. Very detailed evaluation using the proposed FairMT-10K.
6. A more efficient FairMT-1K is also proposed.

### Weaknesses
1. This work has carefully designed two tasks for each LLM capability.   Although each task has a considerable amount of space to introduce, there is a lack of specific formal definitions for each task in the main paper. 

2. Continuing from the first point, the main paper of this work has ignored many necessary details in the main paper in the remaining parts. 

3.  This work does not involve enough human annotation in both the dataset construction stage and the evaluation stage.  There is only a small-scale human-annotation test in the Appendix.

4. LLMs play the role of both the dataset constructor and the evaluation referee. Is this configuration really convincing?

5. This work only focuses on the evaluation.  The author needs a more detailed discussion on what improvement directions can be brought to the subsequent researches through experimental findings.

### Questions
Questions:

1. See my weaknesses 4.

Minor Issues:

1. Line 130:  three stages of interaction with users`: :`
2. Line 732:  The prompt given to GPT-4 is shown in Figure `??`

### Soundness
3

### Presentation
3

### Contribution
3
