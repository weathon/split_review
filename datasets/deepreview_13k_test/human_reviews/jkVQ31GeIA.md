# Auto-RAG: Autonomous Retrieval-Augmented Generation for Large Language Models

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Iterative retrieval refers to the process in which the model continuously queries the retriever during generation to enhance the relevance of the retrieved knowledge, thereby improving the performance of Retrieval-Augmented Generation (RAG).
Existing work typically employs few-shot prompting or manually constructed rules to implement iterative retrieval.
This introduces additional inference overhead and overlooks the remarkable reasoning capabilities of Large Language Models (LLMs).
In this paper, we introduce \textbf{Auto-RAG}, an autonomous iterative retrieval model centered on the LLM's powerful decision-making capabilities. 
Auto-RAG engages in multi-turn dialogues with the retriever, systematically planning retrievals and refining queries to acquire valuable knowledge. This process continues until sufficient external information is gathered, at which point the results are presented to the user.
To this end, we develop a method for autonomously synthesizing reasoning-based decision-making instructions in iterative retrieval and fine-tuned the latest open-source LLMs.
The experimental results indicate that Auto-RAG is capable of autonomous iterative interaction with the retriever, effectively leveraging the remarkable reasoning and decision-making abilities of LLMs, which lead to outstanding performance across six benchmarks. 
Further analysis reveals that Auto-RAG can autonomously adjust the number of iterations based on the difficulty of the questions and the utility of the retrieved knowledge, without requiring any human intervention.}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed a new method to automatically refine RAG retrieval query with reasoning. It showed that it can induce multi-step retrieval queries for multi-hop questions, and refine queries for simple questions, based on cases in Figure 1 and Figure 8. The authors fine-tuned Llama-3-Instruct-8B for the reasoning process, and used Qwen1.5-32B-Chat for crafting the query re-writing process. The performances of the new methods are better compared with other naive methods, single-time retrieval methods an iterative retrieval methods based on the results in the paper.

### Strengths
- The paper clearly described the methods with examples
- The paper employed recent open-source models like llama3-8b

### Weaknesses
- lack of comparison with GPT-4, GPT-4o or other closed AI models
- lack of case comparison with other RAG algorithms on multi-hop questions, in particular, for questions requiring a lot of reasoning process

### Questions
- Although the author provided reasoning examples in Figure 1, it did not compare with other RAG algorithms in case study section. Based on the case study part in Figure 8, the Auto-RAG refined the input query from "When was the first Ford F-150 produced" to "When was the first Ford F-150 model introduced". This is a relatively minor refinement on the query wording, instead of reasoning. If the authors can show more examples about reasoning in particular for multi-hop questions, comparing with other RAG methodologies, that would be great. The question in Figure 1 is an example multi-hop question. Some other similar questions can be found in relevant papers like "The Argentine PGA Championship record holder has won how many tournaments worldwide?" in the paper "Multi-hop Question Answering" https://arxiv.org/abs/2204.09140
- Can you also compare the performances with closed AI models, like GPT-4, GPT-4o etc.? For example, in the paper of "From Local to Global: A Graph RAG Approach to Query-Focused Summarization", it uses GPT-4 for the RAG solution.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Auto-RAG, an autonomous iterative retrieval model leveraging large language models’ (LLM) decision-making capabilities. Auto-RAG engages in multi-turn dialogues with the retriever, methodically planning and refining queries to acquire necessary external knowledge. This iterative process continues until sufficient information is gathered, at which point the results are provided to the user. The authors propose a method to autonomously generate reasoning-based decision-making instructions in iterative retrieval and fine-tune the latest open-source LLMs to enhance performance.

### Strengths
- The model effectively adapts iteration count for optimized performance.
- This work opens a promising new direction in automating retrieval-augmented generation (RAG).

### Weaknesses
- Novelty seems to  limited, as automated iteration in prompt-based systems has been explored in other works, including ReACT, Tool-LLM, and Chameleon (https://arxiv.org/abs/2304.09842). The approach to fine-tuning also appears similar to Alpaca.

- Critical baselines are absent, such as BeamAGGR (https://arxiv.org/pdf/2406.19820), Self-CRAG, and Open-RAG (https://arxiv.org/abs/2410.01782)—though the latter is concurrent and could be considered optional.

- Some reported results raise questions. For instance, on the TQA dataset, Self-RAG reports a 66+ accuracy using Llama 2, yet Auto-RAG with Llama 3.1 only achieves 38, while the baseline is 55.7. Similar discrepancies are noted for other datasets, like PQA.

- Section 5.5’s evaluation method of Self-RAG is unclear. Although these models say they process top-k retrievals in parallel but for arguments even if we consider the processing is individually to generate multiple answers, speed should theoretically scale with the number of retrievals. Figure 7 is therefore confusing: why does Self-RAG demonstrate slower speeds with fewer retrievals (e.g., in 2 Wiki)?

- Algorithms 1 and 2 are insufficiently clear. For example, in Algorithm 1, line 9’s method for determining if d contains a sub-answer of X is ambiguous. Additionally, the writing from line 216 onward does not consistently align with the notations in Algorithms 1 and 2 (e.g., maximum iterations are denoted as T vs. K). Improving and synchronizing these algorithmic and training details would benefit clarity.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

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
This paper presents Auto-RAG, an autonomous iterative retrieval model that engages in multi-turn dialogues with the retriever. It systematically plans its retrievals and refines queries to gather valuable knowledge. In addition, they develop a method for autonomously synthesizing reasoning-based decision-making instructions in iterative retrieval and fine-tuned the latest open-source LLMs. The experimental results show that Auto-RAG can engage in autonomous iterative interactions with the retriever, effectively utilizing the impressive reasoning and decision-making capabilities of large language models, resulting in excellent performance across six benchmarks.

### Strengths
(1)They have conducted thorough research and organization of the work in the area of iterative retrieval within the RAG field.
(2)They proposed an effective data synthesis method utilizing large language models specifically for this direction, enabling fine-tuning based on this approach.
(3)The entire Auto-RAG process is efficient, with clear and coherent language expression throughout.

### Weaknesses
(1)The contribution of “parametric knowledge” to the overall reasoning process is not clearly articulated. Could you provide concrete examples of how parametric knowledge influences the model's reasoning or decision-making?
(2)The overall approach does not seem to present significant innovations compared to previous work, such as self-rag; it primarily enriches the prompt content.
(3)The whole pipeline relies on the presence of the word "answer" in the generated content to determine when to conclude the retrieval process. This method may be susceptible to the model's "hallucinations."

### Questions
(1)In the inference phase of Auto-RAG, why is the utilization of parametric knowledge placed later in the process? Would it not be more beneficial for overall efficiency to incorporate it before retrieval? Additionally, further analysis is needed to quantify the contribution of parametric knowledge to the final generation. Could you provide empirical evidence or reasoning for why they chose this particular ordering of parametric knowledge utilization?
(2)In the results presented in Table 1, why does Naive Gen perform better on 2Wiki than nearly all the baselines? Is it possible that the baselines were not provided with appropriately configured prompts to elicit suitable answers?
(3)Why are the performance metrics for Iter-RetGen not displayed in Figure 7?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces an autonomous iterative retrieval framework for retrieval-augmented generation. By designing appropriate prompts, the authors automatically synthesize instruction-finetuning data, which is used for the model finetuning. Experimental results validate the viability and effectiveness of the proposed framework, demonstrating performance improvements across six benchmarks.

### Strengths
1. This paper is well-written and well-organized.
2. The authors propose an autonomous iterative retrieval framework that, in my opinion, not only demonstrates performance improvements but also offers an efficient approach to addressing the long-context limitations of current LLMs' context windows.
3. Extensive experiments demonstrate its effectiveness, and the provided prompts used to synthesize instruction-finetuning data are valuable to this community.

### Weaknesses
1. Although the authors provide a detailed description of the prompts used to synthesize the dataset, the paper lacks essential information on the training process, which weakens its overall impact (see my questions for specifics).

2. The authors used Llama-3-Instruct-8B to synthesize the data and subsequently fine-tuned the same model with the generated dataset. While synthesizing data with larger models like GPT-4 or Claude would likely yield better results, the choice of an open-source model is understandable due to cost constraints. However, it raises the question of why larger Llama models, such as 70B or even 405B, weren’t used. Larger models could produce higher-quality data, potentially enhancing the training outcomes.

3. Some experimental results using GPT-4 or Claude should be provided, even if only on one dataset. While it's not expected for the finetuned Llama-3-Instruct-8B to outperform these models, such comparisons would give a clearer sense of the performance gap, better illustrating the value of fine-tuning smaller-scale language models.

### Questions
1. In Section 3.2, please clarify the specifics of the input $x_t$ and the output $y_t$ in Equation 3. Although $x_t$ and the output $y_t$
may seem intuitive, the synthesized datasets described in Line 17 of Algorithm 1 do not explicitly define these variables. Providing a clear description of $x_t$ and the output $y_t$ would improve understanding.

2. Could you explain what is meant by "d contains a sub-answer of X"? I wasn’t able to find the criteria used to determine this. Some examples, especially related to Natural Questions (NQ) and multi-hop question answering (HQA), would be helpful for understanding your approach.

3. In Lines 5 through 10, if the condition in Line 9 is not met after iterating over all queries in 𝑄, then $Q_k$ and $D_k$ remain undefined, which could lead to issues in Line 11. Could you clarify how this situation is handled?

4. How do you determine the value of K? Is there a risk that the context length might exceed a manageable size? If so, do you have a method for truncating context to ensure efficiency?

5. What does it mean "if no information need in R then" in Line 12 of Algorithm 1, please provide an accurate definition for that?

### Soundness
3

### Presentation
4

### Contribution
3
