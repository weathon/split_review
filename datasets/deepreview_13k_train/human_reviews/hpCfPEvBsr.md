# MixEval-X: Any-to-any Evaluations from Real-world Data Mixture

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
Perceiving and generating diverse modalities are crucial for AI models to effectively learn from and engage with real-world signals, necessitating reliable evaluations for their development. We identify two major issues in current evaluations: (1) inconsistent standards, shaped by different communities with varying protocols and maturity levels; and (2) significant query, grading, and generalization biases. To address these, we introduce \eval, the first any-to-any, real-world benchmark designed to optimize and standardize evaluations across diverse input and output modalities. We propose multi-modal benchmark mixture and adaptation-rectification pipelines to reconstruct real-world task distributions, ensuring evaluations generalize effectively to real-world use cases. Extensive meta-evaluations show our approach effectively aligns benchmark samples with real-world task distributions. Meanwhile, \eval's model rankings correlate strongly with that of crowd-sourced real-world evaluations (up to 0.98) while being much more efficient. We provide comprehensive leaderboards to rerank existing models and organizations and offer insights to enhance understanding of multi-modal evaluations and inform future research.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces MixEval-X, a large benchmark which can be used for evaluating large multimodal models in large number of multimodal tasks, ranging from understanding to generation. The paper also shows an extensive evaluation of several existing approaches to the considered tasks, providing a reference for future works. It also introduced a carefully designed pipeline for the evaluation of different models.

### Strengths
- The evaluation provided in the paper is extensive, both considering the number of tasks and models evaluated. This paper can really become a reference for many future works.
- The tasks considered are handling very different modalities, which can foster the adoption of this dataset from different AI sub-communities.
- The user studies are carefully designed and involved a high number of annotators.

### Weaknesses
The paper is very solid, with few weak points. It presents several contributions. This can make it somewhat challenging to read due to the frequent cross-references throughout the document. However, I see this as a minor issue, largely due to the richness of the content.

The discussion about dynamism and contamination is not very clear (L153). Could the authors clarify this?

### Questions
- The discussion about dynamism and contamination is not very clear (L153). Could the authors clarify this?

### Soundness
4

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
This paper focuses on introducing reliable evaluation methods to guide the development of multimodal large language models (LLMs). The authors extend MixEval to cover a wider range of tasks and incorporate additional modalities by proposing a multimodal benchmark mixture and adaptation-rectification pipelines to better reflect real-world task distributions. Furthermore, the paper benchmarks multimodal LLMs on their capabilities across text-to-X, X-to-text, and agent tasks, where X represents modalities such as images, videos, and more.

### Strengths
1. This approach is simple yet effective for creating a benchmark that encompasses a wide range of tasks.

2. The benchmark has been shown to align closely with the distribution of real-world datasets.

### Weaknesses
1. Missing Any-to-Any Models: Several relevant and popular any-to-any models have been omitted from the benchmark, such as:

    CoDi: Any-to-Any Generation via Composable Diffusion

    NExT-GPT: Any-to-Any Multimodal LLM

    Including these models would provide a more comprehensive evaluation.

2. Discussion of Limitations: Although not mandatory, a discussion on the limitations of the study would be valuable. It could provide context for the results and suggest areas for future research.

3. Clarity of Benchmark Creation: The process of creating the benchmark is very difficult to follow. Including a diagram or visual representation would greatly aid understanding and improve the overall readability of the paper. Additionally, the method for generating the hard dataset is not well explained, and providing more detail would improve comprehension.

### Questions
1. Ensuring Accuracy of Web Queries: How is the accuracy of information retrieved from web queries verified or ensured?

2. Handling Temporal Shifts: Given that accurate information can change over time (e.g., updates in data or events), how does the system handle these temporal shifts to maintain reliability?

3. Preventing Data Leakage: How does the benchmarking process ensure that there is no data leakage, especially considering that LLMs may have been pretrained on data sourced from the web?

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
This paper introduces MixEval-X, a new any-to-any capability benchmark for assessing performance of frontier multimodal models across a diverse set of tasks and input-output modality combinations. The paper proposes to use the framework introduced in MixEval to perform benchmark mixtures from pre-existing benchmarks to construct a well-curated benchmark that is more generic and follows real-world task distributions.

### Strengths
- This is a very comprehensive piece of work that is very well motivated and provides a significant step in unifying multimodal frontier model evaluation going forward.

- There is a substantial amount of empirical evaluations and analyses conducted on the benchmark and its constituent sub-benchmarks to showcase its real-world utility.

- In particular, the combination of figs 36-39 + fig 9 is particularly striking. It can clearly help model developers assess which benchmarks are probing which particular capabilities to guide model development.

### Weaknesses
 - A key limitation of the work is the lack of any discussion surrounding model evaluation costs. I believe it is important to provide details on how much it costs to evaluate any frontier models on the benchmark, i.e. both the cost of running models / APIs on the benchmark tasks but also the cost of using LLMs as judges.

- It is not clear which set of sub-benchmarks use automated LLMs-as-judges, humans as annotators and which others use pre-existing ground-truth information for evaluating models. It might well be that each sub-benchmark uses a combination of these, but I believe it would be useful to augment Tab 1 with this information on what set of ground-truths and evaluation strategies each sub-benchmark uses (i.e. LLM-as-judge, preferences, ground-truth etc).

- The challenge of test-set contamination: From the construction of the benchmark, it is not made abundantly clear how the proposed benchmark alleviates the problem of test-set contamination---as I understand, it is merely a combination of pre-existing benchmark samples in a principled manner by aligning with the real-world task distribution? If this is the case, it does indeed ensure a more robust distribution in the evaluation splits as well as better alignment to real-world usage, but it does not actually alleviate the concern of test-set contamination. A broad discussion point on this would be useful.

### Questions
- Where are the actual web-queries being mined from? Would it possible to add some details around this mining strategy as well as add a few of these web-queries to give a feel of what the real-world task distribution looks like?

- For the non-hard version of the benchmarks, the best models already perform quite well (76.9%, 74.2%, 62.7%). Does this mean that this version of the benchmark is quite easy for current frontier models already, and has a lower saturation ceiling? Could the authors please comment on this.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
MixEval-X extends MixEval to support multiple modalities beyond text, comprising eight new subsets (excluding the original MixEval) categorized into three types: multi-modal understanding (MMU), multi-modal generation (MMG), and agent tasks.

- **Benchmark Creation**: The creation process differs for each type. For MMU tasks (Text2Text, Image2Text, Audio2Text), a benchmark mixture pipeline aligns web queries with similar tasks from existing benchmarks, similar to MixEval. For MMG and agent tasks, an adaptation-rectification pipeline standardizes real-world queries, though the exact adaptation-rectification process requires further clarification.
- **Evaluation**: Grading methods are customized for each task type. MMU and agent tasks are evaluated with LM-based parsers, with smaller models for MMU and Frontier LMs for agent tasks. MMG tasks, harder to automate, rely on crowd-sourced evaluation.
- **Intuition & Interesting Claim**: MixEval-X retains MixEval's core philosophy: simulating web-distributed questions as a proxy for real-world questions, forming a compressed benchmark for efficient evaluation. Image2Text outputs in MixEval-X show a high correlation with Vision Arena, supporting this approach. A key finding indicates that Judge models in multimodal-generation tasks often diverge from human preferences.

Overall, this work offers a comprehensive evaluation of models across diverse multimodal tasks.

### Strengths
- **[Important] Comprehensive Analysis & Leaderboard**: MixEval-X offers extensive benchmarks and detailed leaderboards to rerank existing models and organizations. I appreciated the thorough, high-standard benchmarks applied across modalities and communities.
- **[Important] Clarity**: The paper effectively motivates the setting for readers unfamiliar with the topic. It is easy to understand, with clearly stated contributions, proposed methods that address the defined problem, and well-presented and interpreted results. However, some sections may feel dense due to space constraints in the 10-page limit.

### Weaknesses
I have a few concerns asked in Questions section. However, note that I could not find major weaknesses specific to this work, which did not apply for the general MixEval framework.

Overall, the method is a compelling and substantial extension of MixEval, with sound intuition and strong performance demonstrated through extensive comparisons. I would be pleased to see this paper presented at ICLR, but note that I am not a domain expert -- looking forward to seeing the other reviews and discussions with the authors.

### Questions
Q1. **Automatic Benchmark Creation & Grading for Agent Tasks**
- a) Creation: Could you clarify if there are any specific checks and balances in place to ensure the action set was complete and the context made sense, especially if these tasks were primarily generated by models?
- b) Grading: Since the grading appears to be automated, was there any human oversight to detect and correct potential errors in this pipeline or checks to indicate what fraction of inputs/model behaviour intermediate was erroneous/undefined and not caught by the grader? Ensuring clarity here would be valuable, as automated grading might lack nuanced understanding.

Q2. **Scalability and Applicability of Automatic Evaluation**
- The paper claims scalability and automated evaluation, but these seem to primarily apply to MMU tasks. For MMG tasks, wouldn’t repeated sampling from new prompts or models require costly human annotation? It seems to me that the scalability only extends to certain tasks, does this align with the broader goals and spirit of the paper?

### Soundness
3

### Presentation
3

### Contribution
3
