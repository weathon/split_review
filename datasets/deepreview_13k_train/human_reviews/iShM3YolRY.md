# On the Tool Manipulation Capability of Open-sourced Large Language Models

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Recent studies on software tool manipulation with large language models (LLMs) mostly rely on closed model APIs. The industrial adoption of these models is substantially constrained due to the security and robustness risks in exposing information to closed LLM API services.
In this paper, we ask \emph{can we enhance open-source LLMs to be competitive to leading closed LLM APIs in tool manipulation, with practical amount of human supervision}. 
By analyzing common tool manipulation failures, we first demonstrate that open-source LLMs may require training with usage examples, in-context demonstration and generation style regulation to resolve failures. 
These insights motivate us to revisit classical methods in LLM literature, and demonstrate that we can adapt them as model alignment with programmatic data generation, system prompts and in-context demonstration retrievers to enhance open-source LLMs for tool manipulation.
We demonstrate that our techniques can boost leading open-source LLMs by up to $90\%$ success rate, showing capabilities competitive to OpenAI GPT-4 in $4$ out of $8$ \snact\  tasks.
We show that such enhancement typically requires about one developer day to curate data for each tool, rendering a recipe with practical amount of human supervision.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates how open-source LLMs can be improved to match the tool manipulation capabilities of proprietary, closed-API models like OpenAI's GPT-4. The authors identify three main challenges faced by open-source LLMs: incorrect API naming, improper argument values, and non-executable outputs. To address these issues, authors experiment with model alignment via programmatic data generation, in-context demonstration with retrieval, and system prompts, and adapt them for tool manipulation. They evaluate these methods using ToolBench, a benchmark they created consisting of various software tools, and find that their approaches can significantly enhance open-source LLM performance.

### Strengths
* New Benchmark: The creation and utilization of the new ToolBench benchmark for a diverse range of software tools allow for a thorough and systematic evaluation of the tool manipulation capabilities of various LLMs. This provides a soliid foundation for comparison and progress tracking in future research.
* Focus on open source models: The paper successfully applies novel techniques like model alignment, system prompts, and retrieval augmented in-context demonstration to enhance the capabilities of open-source LLMs.

### Weaknesses
Scalability concerns: the paper does not adequately adderess how the necessary amount of human supervision would scale with the increasing complexity of tasks or with different types of tasks beyond those tested.

### Questions
Can you add ReAct style prompting to the set of baselines?

In Section 4, how do you ensure that the system prompt used to regulate generation does not suppress the creativity of language models, which can be crucial for generating novel solutions to programming problems? Could this constraint inadvertently limit the model’s ability to generate innovative API usages that have not been programmed into its training data?

In section 5.1, you note that the benchmark involves tasks that require a different number of API functions, ranging from 2 to 108, to achieve the goal. Could you provide some performance metrics that would correlate with the number of API functions required to fulfill each goal?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper analyzed the tool manipulation capability of open-source LLMs and pointed out some common failure types: 1) open-source LLMs struggle with accurately recognizing API names, 2) in the absence of few-shot demonstrations, open-source LLM often incorrectly populate API arguments, 3) open-source LLMs usually produce natural language descriptions rather than executable code. Based on these failure types, the author investigated the benefit of three techniques: 1) instruction-tuning LLM with samples about API calling, 2) retrieve demonstrations for in-context learning, and 3) adding a system prompt tailored to guide the model's outputs. To evaluate these techniques, the author proposed a new benchmark suite called ToolBench that covers eight different API usage scenarios. According to the experiments, the author found that the fine-tuning step boosts the tool-use capability of open-source LLM significantly, while system prompt and in-context learning robustify the LLMs for further improvement.

### Strengths
The paper is nicely written and has good value for practitioners. The three techniques the paper studied are reasonable and can effectively boost the LLM's capability in using tools, as suggested in Table 5. The author also conducted ablation study on each technique's relative contribution (Table 6).

### Weaknesses
The novelty is limited because prior works (such as [NeurIPS2023] GPT4Tool) have already shown that instruction-tuning can boost the tool-use capability of open-source LLMs. Other techniques studied by the paper, such as in-context retriever and system message, are also standard prompting methods. The author has not compared ToolBench with other similar benchmarks like the GPT4Tools dataset and the APIBench proposed in Gorilla (https://arxiv.org/abs/2305.15334).

### Questions
1. Coding models seem to perform better at API tasks. However, the author has not compared with CodeLLaMA (https://huggingface.co/codellama).
2. The author gave an example about advanced reasoning in Table-4. In this example, the model needs to understand that in a Google Sheet, the cell that contains the beef's price is "C2". However, what if the column that contains Price is column "D" rather than column "C"? Did you gave additional context to the LLM?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Tool learning is a rising topic with the emergence of powerful closed LLMs (e.g., ChatGPT). However, there still remains a large gap between closed LLMs and open-source LLMs. To reduce the gap, this paper explores how to enhance the capability of open-source LLMs in tool utilization. More specifically, authors argue three challenges for improving open-source LLMs, including usage examples, in-context demonstration, and generation style regulation. To address these, this paper attempts to augment the practical amount of supervision and enhance LLMs by using model alignment, in-context demonstration retriever and system prompt. Moreover, this paper introduces a ToolBench benchmark to address this problem. Experimental results demonstrate that the proposed method can improve the capability of open-source LLMs in tool utilization.

### Strengths
1. This paper analyzes the mistakes of current LLMs in API usage.
2. This paper introduces a benchmark, called ToolBench, to investigate the potential of open-source LLMs in tool use. Moreover, authors also introduce API complexity to examine the challenge of the proposed ToolBench.
3. Experimental results demonstrate the effectiveness of the proposed method.

### Weaknesses
1. This paper involves human-curated templates to build model alignment. However, such a stage may raise some problems:

+ The curated examples mainly cover 6 - 8 scenarios. So what happens if we extend to another different scenario? Does it require us to produce more curated data? The generalization of these curated examples needs to be verified.
+ Since the curated data are involved, are there any experiments to validate the connection between the quality of curated data and final results (e.g., model alignment)? We need to confirm how curated data affect model performance to what extent. If the value of the proposed method could be reduced if it heavily relied on human-curated data,

2. This paper applies a demonstration retrieval to obtain the most related demonstrations. However, just as aforementioned, such a stage requires us to have some demonstration in before. So what happens if we do not have relevant demonstrations for a request?

### Questions
1. Recently, there also have some benchmarks like another ToolBench [1]. Can authors compare or describe the differences among these works?
2. Improving model performance by fine-tuning LMs is not surprising. It is necessary to validate the generalization of tuning LLMs. For example, tuning LLMs on a subset of the dataset (e.g., Open weather) and then evaluating it on the remaining parts (e.g., Virtual Home).

One minor question about the presentation:
1. Can authors check the latex format of the submitted version? It seems that the font style is different from the standard version of the ICLR submission.

[1] ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to enhance open-source Large Language Models (LLMs) for tool manipulation. The study addresses the limitations of closed APIs in terms of security and robustness by proposing techniques, such as model alignment with programmatic data generation, system prompts, and in-context demonstration retrievers. Through evaluation on ToolBench, a diverse benchmark of tools, the authors demonstrate that their approach can significantly improve open-source LLMs, achieving up to a 94% success rate and competitive performance with OpenAI GPT-4 in four out of eight tasks.

### Strengths
1. Focus on a timely problem for evaluating the LLM's ability of tool usage.

2. The introduction of ToolBench, a benchmark consisting of diverse software tools for real-world tasks, strengthens the paper's contributions.

3. Diagnosis of existing tool-use LLMs to highlight their strengths, weaknesses, and potential improvements.

### Weaknesses
1. Missing comparison with closely related works. I would like to inquire about the absence of a comparative analysis with Toolbench, ToolQA and Gorilla (see [1,2,3] for references). An exploration of potential distinctions between the two approaches would provide valuable insights.

2. The retrieval quality in this study appears to be not very good. In practice, I have observed that the retrieved demonstrations often lack meaningful relevance. Such limitations can significantly impact overall system performance.

3. Lacking substantial enhancements tailored specifically for open-source large language models. Have the authors considered the exploration of other decoding strategies or innovative approaches to improve the overall system performance and capabilities?

4. The template of the paper seems to be incorrect for ICLR. Please fix it in the camera-ready version.

5. It is **not appropriate** to include the conference name 'neurips2023' in your GitHub repo. I believe this is the submission site for ICLR 2024, not NeurIPS 2023. Also, it is recommended to use the anonymous github for submitting code.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
