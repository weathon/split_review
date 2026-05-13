# Tool Decoding: A Plug-and-Play Approach to Enhancing Language Models for Tool Usage

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Despite the significant advancements in large language models (LLMs), their tool-use capabilities remain limited. This limitation stems from the fact that existing approaches often merely adapt strategies designed for basic natural language tasks, overlooking the specific challenges inherent in tool usage, such as precise tool selection, strict predefined formats, and accurate parameter assignment.
To bridge this gap, we conduct a fine-grained analysis of the tool usage process, breaking it down into three critical stages: tool awareness, tool selection, and tool call. Our analysis reveals that most failures stem from selection errors, format violations, and parameter mis-assignments.
Building on these insights, we propose \textbf{Tool Decoding}, a novel, training-free approach that directly incorporates tool-specific information into the decoding process. Tool Decoding employs constrained decoding to ensure format correctness and eliminate hallucinations, while leveraging order consistency to improve parameter accuracy through structured sampling and a majority-voting mechanism. This approach effectively addresses many common tool-use errors in a plug-and-play manner, allowing for seamless generalization to new tools as long as they are accompanied by well-structured documentation to guide the decoding process. 
Experimental evaluations on benchmarks like API-Bank and BFCL V2 • Live show that Tool Decoding leads to significant improvements across a diverse set of more than 10 models, including both generalist and tool-finetuned models. Almost all models demonstrate performance gains exceeding 70\% on both benchmarks. Among the 7B-level models, five outperform GPT-3.5 on key tasks, with two even surpassing GPT-4.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses the limitations of LLMs in tool usage. Previous works often overlook the specific requirements of tool selection, format adherence, and parameter accuracy. The authors propose a training-free approach called "Tool Decoding," designed to improve tool-use precision through constrained decoding. Experimental results demonstrate that Tool Decoding achieves improvements in tool-use accuracy across benchmarks (API-Bank and BFCL V2), with open-weight models performing comparably to GPT-4 in some cases. However, the paper lacks a thorough comparison with other existing methods (only compared with beam and greedy search) and provides no report on latency, which could be important for practical applications.

### Strengths
- Achieved comparable results to GPT-4 for open-weight models with the help of Tool Decoding on the API-Bank and BFCL V2 benchmarks.
- The method does not require any training and primarily relies on constrained decoding to ensure format correctness and eliminate hallucinations.

### Weaknesses
 - Comparison with other methods? The authors compare their method only with Beam Search and Greedy Search. Are there no other methods available, such as those in https://arxiv.org/pdf/2401.06201 (01.2024), trained models, etc.?
- For the error analysis section, I believe it does not sufficiently acknowledge that other researchers have reported similar problems. It is written as though this paper is the first to report them. For example, the API-Bank [paper](https://arxiv.org/pdf/2304.08244) provides a thorough analysis at a similar level of granularity in Section 7.3, which I believe has not been adequately acknowledged.

### Questions
- Value errors increased in most scenarios after applying Tool Decoding (add to Limitation section); on the other hand, key errors are not a major challenge. Tool Decoding primarily addresses format errors and partially resolves selection errors. I understand how it can help with selection errors by decoding tool names under constraints. However, for format errors, the example in Table 1 shows a missing parenthesis. How would Tool Decoding help in this case?

- Another important factor in decoding tools is latency in seconds, but I did not find any comparison. Although there is no major comparison with other methods, some latency figures for the tool itself would be beneficial.

### Soundness
3

### Presentation
3

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
The paper presents Tool Decoding, a training-free approach to improve LLMs’ tool-use capabilities, addressing common errors in tool awareness, tool selection, and tool call. By using constrained decoding for format accuracy and order consistency for parameter correctness, Tool Decoding significantly boosts tool-augmented performance on benchmarks e.g. API-Bank and BFCL V2 • Live, even surpassing GPT-4 in some cases. This adaptable approach enhances LLMs' effectiveness in real-world tool use without requiring additional training.

### Strengths
1. The paper presents Tool Decoding a novel, training-free approach to enhancing large language models (LLMs) in tool use. Unlike conventional methods relying on extensive fine-tuning, this plug-and-play solution integrates tool-specific data into the decoding phase. Tool decoding approach includes constrained decoding and order consistency modules, which is shown to effectively mitigate different tool errors e.g. Key error, Value error, and Format error.

2. The paper conducts an error analysis across three stages of tool usage—Tool Awareness, Tool Selection, and Tool Call. The analysis is done, using both API-Bank and BFCL V2 • Live datasets, which are benchmark datasets well-suited to assessing tool-augmented LLMs.

3. They showed the effectiveness of Tool Decoding by applying it to a variety of both general-purpose and tool-specialized models, evaluating them on the API-Bank and BFCL V2 • Live benchmarks. The experimental results show that Tool Decoding substantially improves performance across all models. Nearly all models achieve performance gains above 70% on both benchmarks. Among the 7B parameter models, five surpass GPT-3.5 in critical tasks, with two even outperforming GPT-4.

### Weaknesses
1. Limitation of Novelty as a long paper: constrained decoding for tool usage in LLMs has been employed in several prior works (e.g., [Domino](https://arxiv.org/abs/2403.06988): is proposed to optimize for general constrained text generation tasks with a focus on grammar and token alignment, [TOOLDEC](https://arxiv.org/pdf/2310.07075): eliminates syntax errors by constraining token choices using FSMs, focusing on maintaining tool syntax), and the specific approach to constrained decoding in this paper does not differ significantly.  As a result, the primary novelty of this paper lies in the order consistency mechanism, which offers only a limited improvement (Table 6).

2. Missing Baselines: The tool-finetuned models presented in the results table are outdated, and more recent, more powerful models (e.g., [Hermes Function Calling](https://github.com/NousResearch/Hermes-Function-Calling) and [Gorilla](https://github.com/ShishirPatil/gorilla)) are not included for comparison.

### Questions
1. Can you please further describe the differences of your approach (specially constrained decoding module) to previous work on constraint decoding for tool calling in LLMs?

2. Is there any technical reason that more recent tool-fine tuned models are not added for comparison?

### Soundness
3

### Presentation
4

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
This paper introduces a method to improve LLMs' tool-use capabilities with constrained decoding. They claim that current LLMs struggle with tool awareness, tool selection, and tool call. To address these, the author uses constrained decoding to reduce selection and format errors, moreover they also use order consistency to enhance parameter accuracy with structured sampling and majority voting. 
This plug-and-play approach enables seamless adaptation to new tools only with the api documentation.
Experimental results on API-Bank and BFCL V2 Live benchmarks show high performance improvements across different models.
This work demonstrates the effectiveness of specialized decoding methods tailored to tool usage.

### Strengths
1. This work introduces an innovative, training-free approach to address tool-use challenges in language models. With constrained decoding and order consistency, the LLM can have much better performance over the two benchmark.
2. The paper is well-organized and uses clear figure to present the ideas, like constrained decoding. The figures break down workflows and methods, which helps improve readability.
3. This method provide a way to improve the LLM tool ability without training. This method may be important across diverse applications, enabling more efficient and versatile LLM deployment in real-world settings.

### Weaknesses
1. The author only compares to standard methods like greedy and beam search. However, I believe the author should do more comparison with recent tool-use improvement methods, such as state-tracked constrained decoding and reranking method or other in-context learning methods.
2. The models involved in the paper are mostly under 7B, (only dicuss 7B > models in the Figure 2), yet discussion about 30B, or even 70B model is limited in the paper. I am wondering whether the method still works or how much the method will improve when the model gets larger.
3.  Since the method involves structured sampling and majority voting, maybe the author can discuss its computational efficiency compared to baseline. This would give a more picture of its practical trade-offs in real-time applications.

### Questions
See questions in Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a constrained decoding workflow to improve LLMs' utilization of external tools. LLMs need to recognize when to enter tool mode, which tool to select, and how to invoke the tool with the appropriate arguments. Errors in any of these steps can result in an incorrect response. To address this, the authors introduce a constrained decoding approach that restricts the output vocabulary to include only tool names when the LLM enters tool mode. After a tool is selected, multiple candidate arguments (key-value pairs) are generated by varying the parameter order, and majority voting is used to select the final value for each parameter. The tool is then called, and the LLM continues generating its response. The authors evaluate their tool decoding method on the API-Bank and BFCL datasets across several LLMs, finding that their approach outperforms standard greedy and beam search decoding techniques.

### Strengths
The main benefit of the proposed constrained tool decoding approach is that it is training-free, making it easier to integrate into existing inference pipelines. 
Constrained decoding provides a significant accuracy boost over greedy and beam search methods in terms of tool usage. 
The authors conduct an error analysis to examine the impact of different error types across various LLMs, helping to identify key bottlenecks. 
Additionally, the idea of generating multiple values for each parameter by varying the order is a compelling approach.

### Weaknesses
The proposed constrained decoding method increases latency, so it would have been beneficial to include a comparison in terms of latency impact. Additionally, incorporating some naive baselines, such as those using alternative search strategies like epsilon sampling or prompt engineering, would add value. As noted in the related work section, other constrained decoding algorithms are available, so a comparison to existing methods would have been interesting. Furthermore, the absence of stronger instruction-tuned LLMs as base models is a limitation. The evaluation also lacks a detailed breakdown of the success rate at each stage (awareness, selection, tool call) with and without constrained decoding, making it difficult to pinpoint where the gains are most significant. The choice of reporting error reduction rather than absolute accuracy in Table 3 makes it harder to interpret the actual performance levels achieved by the models. Finally, the statement about tool call accuracy in Section 2 could be misleading as it does not accurately reflect the performance of all models.

### Questions
Could you please address the below questions:
1. Why UltraTool is used in Figure 2, while API-Bank is used in Figure 3?
2. Why the awareness error changes between the configurations with and without tool decoding in Figure 6?
3. Why LLM is used to generate optional parameters instead of supplying them directly, as is done with required parameters?
4. Provide a more detailed explanation on how accuracy is computed in the paper?
5. Report the success rate with and without constrained decoding, specifically indicating the proportion of samples with correct awareness, selection, and tool call?

Additional comments:
1. Figure 5 is missing accuracy numbers for Gemma.
2. Reporting accuracy numbers in Table 3 rather than error reduction might provide easier interpretation.
3. “Notably, tool call presents the greatest complexity, with even powerful models like Qwen1.5-72B achieving less than 60% accuracy in this stage” is a bit misleading because just by reading the text it appears that none of the model is able to achieve greater than 60% accuracy, which is not true because 32B model achieve around 70% accuracy. Maybe you can consider re-phrasing it to “Notably, tool call presents the greatest complexity, with the best performing model achieving around X% ”

### Soundness
3

### Presentation
3

### Contribution
3
