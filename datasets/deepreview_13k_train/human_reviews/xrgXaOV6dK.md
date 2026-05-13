# Can External Validation Tools Improve Annotation Quality for LLM-as-a-Judge?

- Decision: Reject
- Scores: 5, 3, 8, 6

## Abstract
Pairwise preferences over model responses are widely collected to evaluate and provide feedback to large language models (LLMs). Given two alternative model responses to the same input, a human or AI annotator selects the “better” response. This approach can provide feedback for domains where other hard-coded metrics are difficult to obtain (e.g., quality of a chat interactions), thereby helping measure model progress or model fine-tuning (e.g., via reinforcement learning from human feedback, RLHF). However, for some domains it can be tricky to obtain such pairwise comparisons in high quality - from AI and humans. For example, for responses with many factual statements or complex code, annotators may overly focus on simpler features such as writing quality rather the underlying facts or technical details. In this work, we explore augmenting standard AI annotator systems with additional tools to improve performance on three challenging response domains: long-form factual, math and code tasks. We propose a tool-using agentic system to provide higher quality feedback on these domains. Our system uses web-search and code execution to ground itself based on external validation, independent of the LLM’s internal knowledge and biases. We provide extensive experimental results evaluating our method across the three targeted response domains as well as general annotation tasks, using RewardBench data (incl. AlpacaEval and LLMBar), as well as three new datasets for areas where pre-existing datasets are saturated. Our results indicate that external tools can indeed improve AI annotator performance in many, but not all, cases. More generally, our experiments highlight the high variability of AI annotator performance with respect to simple parameters (e.g., prompt) and the need for improved (non-saturated) annotator benchmarks. We share our data and code publicly.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes the use of external tools to create higher quality AI annotation systems and introduces a tool using AI annotator that use web-search and code execution to improve annotations. After establishing that existing annotation benchmarks are saturated, they introduce 3 new annotations datasets for fact checking, coding and mathematics. They demonstrate the efficacy of their tool-based AI annotator, by showing better performance on the 3 new datasets over SoTA AI annotators, while performing roughly on par with existing annotation benchmarks.

### Strengths
1. While the use of tools in AI-based applications is fairly commonplace now, there use for annotation system is an interesting and novel idea and the paper demonstrates fairly well that it works for a few domains at least. 
2. The paper is well-written and presents fair experimental backing to its claims. 
3. The paper introduced 3 novel datasets for evaluating domain specific annotation capabilities of Language models

### Weaknesses
1. While the use of toolings for AI annotators is interesting, in the current iteration of the work, it is not very clear if it will scale with more custom toolings. In the agent evaluator discussed in the paper, eventhough it defaults to existing annotations for the no-tool use cases, the system shows a degradation in performance for RewardBench, the only OOD dataset evaluated. This makes me concerned about the generalizability of the system.
2. Two of the proposed benchmarks don't have baseline human annotation scores, making it hard to quantify the degree of hardness of the datasets.
3. It is not very clear what are the advantages of using the agentic architecture compared to something like tool-calling API by OpenAI.

### Questions
1. For the generalizability issue, one suggestion would be to experiment with more recent and challenging open domain datasets like RMbench (https://arxiv.org/pdf/2410.16184) and external domain specific datasets like RMMath ( https://arxiv.org/pdf/2410.01729) to verify if the RewardBench results are an exception or a fundamental limitation of the technique- helping verify the robustness of the system.
2. Can the authors compare function calling API based tool-calling system with the existing implementation?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a tool-augmented (i.e., web search engine and code compiler) method to provide pairwise AI feedback, with a focus on three specific domains: long-form factual, math, and coding tasks. Specifically, for each incoming pairwise response, it would first determine its domain and then select the corresponding tool for quality judgment. Experiments are conducted on three pairwise datasets sourced from LongFact, APPS competition subset, and GSM8K hard subset. Results indicate that by tool-augmentation, AI feedback improves in most, but not all, cases on these three subsets. While on a general pairwise benchmark Rewardbench, AI feedback slightly decreases.

### Strengths
1. clear paper writing
2. Classifying the input domain and selecting tools accordingly makes sense.
3. Substantial improvements on certain subsets, particularly APPS.

### Weaknesses
1. My main concern is novelty. Several highly related (i.e., tool-augmented AI feedback), published papers have not been cited and clearly discussed [1,2]. "Novel framework" sounds overclaim.
2. Studying pairwise feedback in domains with clear objective correctness (e.g., fact, code, math) is unjustified.
3. Mixed results. Performance slightly decreases on general domains (rewardbench) and math when the base model is stronger (e.g., GPT-4o).

### Questions
1. Why choose a subset from GSM8K rather than selecting more general benchmarks (e.g., AIME, MATH)?
2. Can you also present experiment results on open-source models?

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
4

### Summary
This paper introduces the concept of external validation of ground truth information during pairwise judgements -- that is, when judging pairs of responses to a given prompt, before using an automated annotator to judge which response is better, tools are first used to validate pieces of the outputs (code execution & correctness, mathematical reasoning, and factuality) and this information is then provided as additional information to the annotator. On datasets with ground truth information (i.e. pairs where one is confirmed to be better than the other), their method noticeably improves performance on factuality and coding tasks, and has less clear performance gains on math tasks.

### Strengths
This paper proposes a reasonable and interesting framework for improving pairwise judgements using automated annotators. Recent work has shown the strength of strong, automated pairwise annotators, and this work is a valuable extension of that, showing that ground truth information in the responses (that traditional LLM-only systems might not always pick up on) is valuable for making these decisions.

### Weaknesses
While this paper shows strong results on annotation accuracy, it is unclear how well this improves downstream performance. I don't think this is a hard requirement for this work, but I'd be interested to see how model performance changes using this method to either generate preference data, or do best-of-n ranking for model outputs. I do not think this is required for this paper to be accepted, however.

### Questions
I have one question, and one suggestion:
* Did you check the correctness of the GSM8K hard answers? GSM8K has a small but noticeable subset (<5%) that have incorrect labels, so without any validation, the instances that GPT4o gets "wrong" may be mislabeled. I'd recommend checking this, and if some are mislabeled, this may be the source of the mixed results you see on math reasoning. If so, I'd recommend thinking about harder math datasets (like MATH), though this may be more complicated for code execution.
* I'd be interested to see how this affects best-of-n ranking when using LLMs as a judge for ranking n model outputs -- I'd assume this would noticeably help performance on the domains tested. This may be expensive depending on the setup though, so this is also a reasonable follow up work instead.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates whether augmenting LLM-as-a-judge with external validation tools can improve their annotation quality for pairwise feedback. They propose a framework that routes a model response to external tools such as  fact-checking, code execution, and math execution. The outputs of these tools are then collated to inform the final decision of the LLM judge.

To evaluate their proposed framework, the authors constructed benchmarks from existing datasets such as LongFact, APPS, and GSM8k. They measure the **percentage agreement of the LLM judge to the ground-truth annotations of these datasets.** They find significant improvements from baseline annotators on long-form fact checking and coding, but mixed results on math.

The main contributions of this work are as follows:
A framework for augmenting LLM judges with external tools to improve judgments on verifiable / objective domains.
Extension of Rewardbench subsets to create more challenging test sets for fact-checking, coding, and math.

### Strengths
- [S1] The contribution is **timely** due to the prevalence of using synthetic preferences from LM judges.
- [S2] The proposed framework is **interesting** as it provides an approach to ground an LLM judge’s annotations to verifiable and objective facts/ground-truth, using existing and off-the-shelf tools today. 
- [S3] I also appreciate the effort to **extend subsets of RewardBench to create more challenging test sets** due to the saturation of the said benchmark.

### Weaknesses
 - [W1] One con for this work is the **insufficiency of experiments to show the accuracy / reliability of specific components of the framework.** For example, how reliable is the “Initial domain assessment” component for routing responses to specific tools? It's unclear how often the domain assessment correctly identifies the need for a specific tool, and what happens when it misclassifies a task. A more detailed analysis of the domain assessment's precision and recall for each tool is needed. This should include not just overall accuracy, but also a breakdown of performance on different types of inputs. 
    - [W1.1] In addition, showing the robustness of the framework as new tools are added to the agent can help strengthen the use-case of this framework. The paper should investigate how the framework's performance changes with the addition of new tools, and whether the initial domain assessment component can effectively handle the increased complexity. For example, how does the system perform when a new tool is added that overlaps in functionality with an existing one? Does the system correctly choose the most appropriate tool, or does it lead to confusion and decreased performance?

- [W2] **Lack of motivation** as to why the specific tools (SAFE, OpenAI code, OpenAI math) were chosen for each component. Were there any other components tested? The paper lacks a clear explanation of why these specific tools were chosen over other alternatives. For example, why was the SAFE method chosen for fact-checking instead of other fact-checking APIs or methods? Similarly, why were the OpenAI code and math interpreters selected, and were any other code or math execution environments considered? A more thorough discussion of the tool selection process, including any alternatives that were tested and the reasons for their rejection, is needed. How sensitive are the reported results to these tools? It is important to understand the sensitivity of the results to the specific tools used. If the performance is highly dependent on the specific tools, this limits the generalizability of the findings. The paper should include an analysis of how the results change when using different tools or different versions of the same tools.

- [W3] The are some **claims that have shallow to no evidence** (a few notable examples):
    - Section 4.3.2 (Observation 4): The claim is that complexity (e.g., in the form of tools) does not always yield better results. The only evidence so far is ArenaHard outperforming the agent framework, but we also see that other simpler methods like pick-best and AlpacaEval underperformed against the agent framework. Perhaps there are other confounders, and there’s a need to disentangle what complexity means. The paper needs to clarify what is meant by complexity and provide a more nuanced analysis of the relationship between complexity and performance. The current analysis does not sufficiently isolate the effect of complexity from other factors. It is also important to define what constitutes a 'complex' method, and how this is measured. Is it the number of tools, the number of tokens, or the computational cost? 
    - Section 4.3.3 (Observation 6): There is a claim that baseline annotators have bias towards incorrect GPT-4 responses, and it was explained as self-enhancement bias. It was further claimed that the agent framework’s code execution path overcame this bias. The only evidence so far is the empirical results, but how much of this was due to the code-execution tool and how much was from AlpacaEval (baseline annotator)? The paper should provide a more detailed analysis of the source of this bias and how the agent framework mitigates it. It's not clear if the improvement is due to the code execution tool or some other aspect of the framework. A controlled experiment is needed to isolate the effect of the code execution tool. Finally, I think it’s important to show how each component contributed to the performance of the overall framework. For the strongest results (Math and Fact-checking), how much of the performance is attributed to the tool and how much was from AlpacaEval? The paper should include an ablation study to determine the contribution of each component to the overall performance. This is especially important for the math and fact-checking tasks, where the agent framework shows the strongest results. It is important to understand how much of the performance gain is due to the tools themselves, and how much is due to the overall framework.

### Questions
Questions
- [Q1] Were there any tests on non-benchmark preference training datasets (e.g., Anthropic-HH, Helpsteer2, ChatArena), and the effect of the agent framework on the downstream reward model / policy model performance? 

Comments/Suggestions (these are nits that don’t weigh a lot in my scoring but I’d appreciate if addressed as it can improve the manuscript):
- [C1] There are some non-formal words used throughout the text that I would appreciate if corrected:
Page 6, bullet point #2, last sentence: “till we have failing solutions” -> “until…”
- [C2] The term agentic was introduced suddenly in p.2 without any introduction / contextualization as to what it means.

### Soundness
2

### Presentation
2

### Contribution
3
