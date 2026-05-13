# ToolGen: Unified Tool Retrieval and Calling via Generation

- Decision: Accept
- Scores: 5, 5, 5, 8

## Abstract
As large language models (LLMs) advance, their inability to autonomously execute tasks by directly interacting with external tools remains a critical limitation. Traditional methods rely on inputting tool descriptions as context, which is constrained by context length and requires separate, often inefficient, retrieval mechanisms. We introduce ToolGen, a paradigm shift that integrates tool knowledge directly into the LLM's parameters by representing each tool as a unique token. This enables the LLM to generate tool calls and arguments as part of its next token prediction capabilities, seamlessly blending tool invocation with language generation. 
Our framework allows the LLM to access and utilize a vast amount of tools with no additional retrieval step, significantly enhancing both performance and scalability. Experimental results with over 47,000 tools show that ToolGen not only achieves superior results in both tool retrieval and autonomous task completion but also sets the stage for a new era of AI agents that can adapt to tools across diverse domains. 
By fundamentally transforming tool retrieval into a generative process, ToolGen paves the way for more versatile, efficient, and autonomous AI systems.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes ToolGen, a finetuned LLMs that can use various tools during the conversations with the users. ToolGen incorporates new 47K tokens for tools into the Llama-3-8B. Through the tool virtualization, tool memorization, retrieval training, and end-to-end agent tuning, ToolGen correctly select the right tools in the context on  the ToolBench evaluation, achieving better performance than retrieval and end-to-end baselines.

### Strengths
- [S1] ToolGen outperform or achieves competitive performance among retrieval and end-to-end baselines on ToolBench.
- [S2] ToolGen can natively invoke 47K tools following the context.

### Weaknesses
 - [W1] The technical novelty is limited. Using special tokens for tools and incorporating them into the original vocabularies are widely-known approach (e.g. Toolformer: https://arxiv.org/abs/2302.04761, ToolkenGPT: https://arxiv.org/abs/2305.11554). The contribution of this paper is scaling this up to 47K tools, but it's very straight forward and I'm not confident if the ICLR community would be interested in it.
- [W2] Releted to [W1], the results of ToolLlama-3 in Section 5 is unclear to me. Why ToolLlama-3 is not as good as ToolGen, even using the same data and models? Could you clarify the difference between two?
- [W3] How about retrieving tools by LLMs itself (without retriever)? For instance, if we use the LLM with millions of extremely long context (such as Gemini), we may not need to rely on neural retrievers. It would be interesting to include long-contect LLMs as a baseline.
- [W4] It would be important to compare other capability of LLMs before/after tool token incorporation. Current draft seems to lack the analysis after combining 47K tokens to LLMs.
- [W5] In Figure1, I didn't understand the distinction between ToolGen's Retrieval Task and Agent Task. Both have the input "I want some popular video games." How are they differentiated?

### Questions
See the Weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces ToolGen, a novel framework that aims to enhance the interaction between large language models (LLMs) and external tools. ToolGen shifts away from traditional tool retrieval methods and instead integrates tool knowledge directly into the LLM's parameters. This is achieved by representing each tool as a unique token, allowing the LLM to generate tool calls and arguments seamlessly as part of its text generation process.

### Strengths
1. ToolGen elegantly combines tool retrieval and execution into a single generative process, eliminating the need for separate retrieval mechanisms. This streamlines tool interaction and enhances efficiency, particularly as the number of tools increases.
2. The use of constrained beam search during inference effectively restricts the output to valid tool tokens, significantly reducing the generation of nonexistent tools, a common issue in LLM-based agents.
3. ToolGen demonstrates its capacity to effectively handle a large repository of over 47,000 real-world tools, highlighting its scalability compared to existing methods that struggle with vast tool sets.
4. The authors spend good amount of effort comparing different indexing method, and the result is clear.

### Weaknesses
1. The advantage of ToolGen which combines tool retrieval and execution into a single generative process introduces limitation together with its efficiency. Since the tools are integrated into the system as tokens, the extension of new tools become inefficient. For every new tool/API, new token need to be added and the documentation finetuned into the model. Also, consider the case that when the tool/APIs get updated, the maintenance of all the tool/APIs, making sure they are up to date is a quite challenging task. On the contact, with a retriever would make adding and maintaining tool/APIs very easy.

2. The paper highlights the efficiency of atomic indexing due to each tool being represented by a single token. However, as the number of tools grows significantly larger, could this approach lead to vocabulary explosion issues? 

3. In the current setting, the vocabulary consists of 128K regular token and 47K tool/API tokens already, how does it affect the performance of LLM itself?

4. How does the performance of ToolGen vary with the size and complexity of the underlying LLM? Would a larger model lead to better generalization ability?

### Questions
1. The paper highlights the efficiency of atomic indexing due to each tool being represented by a single token. However, as the number of tools grows significantly larger, could this approach lead to vocabulary explosion issues? 
2. In the current setting, the vocabulary consists of 128K regular token and 47K tool/API tokens already, how does it affect the performance of LLM itself?
3. How does the performance of ToolGen vary with the size and complexity of the underlying LLM? Would a larger model lead to better generalization ability?

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
3

### Summary
The paper introduces ToolGen, a novel framework designed to address the limitations of LLMs in interacting with an extensive array of external tools. This framework shifts existing paradigms by embedding knowledge about various tools directly into the LLM’s vocabulary, using unique tokens to represent each tool. This allows the model to generate tool calls and arguments as part of the language generation process, eliminating the need for separate tool retrieval systems and seamlessly integrating tool usage within LLM capabilities. ToolGen incorporates a three-stage training process to enable the LLM to learn how to use tokenized tools.

The main contribution of this paper is introducing the ToolGen framework including training and inferencing, and proving that ToolGen have comparable result with current tool retrieval systems.

### Strengths
**Originality:**
The paper introduces a novel approach to tool retrieval by representing each tool as a unique virtual token directly integrated into the LLM’s vocabulary. This method eliminates the need for auxiliary retrievers, making the retrieval process more seamless and efficient. The concept of transforming tool retrieval into a generative task is novel and presents a possible solution to the scalability challenges faced by some existing methods.

**Quality:**
The authors have conducted a comprehensive set of experiments to validate their claims, showing thoroughness in their evaluation. These experiments include various comparisons and detailed ablation studies to assess the impact of different components of their approach. The robustness of their methodology enhances the credibility of their results and conclusions.

**Clarity:**
The paper is well-structured and written in a clear and concise manner. It systematically outlines the problem, the proposed solution, and the experimental validations. Each section transitions smoothly into the next, making it easy for the reader to follow the logic and understand the contributions of the work.

**Significance:**
The research addresses a critical issue in the field of LLM agents: managing and retrieving tools from a large set of tools efficiently. Given the increasing complexity and number of tools available, the proposed method provides a solution. This work has implications for the development of more autonomous and efficient AI systems, potentially benefiting some applications where tool interaction is essential.

### Weaknesses
 **Substantive Assessment of Weaknesses:**

**Cost and Efficiency Claims:**
The key claim of "significantly less cost and higher efficiency" does not hold up under scrutiny. The authors have not substantively demonstrated that their framework is less costly or more efficient than existing methodologies. The ToolGen framework necessitates a three-stage training process, which does not inherently suggest reduced costs. Furthermore, the paper lack data or experiments to substantiate the claim regarding efficiency improvements over other approaches. The paper needs to provide concrete metrics, such as training time, inference latency, and computational resources used, to support the claim of reduced cost and higher efficiency. Without these, the claim remains unsubstantiated.

**Role of the Memorization Stage:**
In Section 4.4, the table shows that the memorization stage plays a relatively minor role in the three-stage training process. However, the authors assert that this stage is beneficial for generalization, with further discussion supposedly found in Appendix F. There is, however, no such discussion present in Appendix F. I would recommend authors to do more experiments to validate the significance of the memorization stage and its impact on generalization. The current evidence does not sufficiently justify the inclusion of the memorization stage, and the lack of detailed analysis in the appendix further weakens this claim. The authors should provide a more rigorous analysis of the memorization stage's contribution, including its impact on performance with varying amounts of training data and across different tool sets.

**Hallucination Comparison:**
Section 5.4 contains statements that do not fully make sense. The claim that ToolGen experiences no hallucination is primarily due to the use of a constrained decoding strategy. Theoretically, it is impossible to encounter hallucination, as defined by the authors, under this constraint. This does not constitute a fair comparison with other frameworks. The authors should either provide results without this constraint and compare them or demonstrate why other frameworks are unable to implement a similar strategy. The comparison is flawed because it does not account for the inherent differences in decoding strategies. The authors need to either compare performance under similar constraints or provide a detailed justification for why other methods cannot adopt the same constrained decoding approach.

**Performance Benchmarking:**
ToolGen is not currently the best-performing framework. Several baselines in the paper outperform ToolGen in various categories, as shown in Table 1 and Table 4. Notably, even the proposed but ultimately unused semantic tokenization approach outperforms the authors' current method, as shown in Table 2. This discrepancy confuses me.

### Questions
- As stated earlier, why don't take the semantic representation approach as your final approach as it performs better (5 wins / 4 loses in table 2) than atomic approach? Saving tokens might not be a sufficient reason. Chain-of-thought reasoning process should produce a lot more than what atomic approach can save here.

- In Table 1: "For ToolGen in the In-Domain setting, we allow the generation space to include all tokens, which is a more challenging scenario compared to other models." What if you don't include all tokens? Since ToolGen can't outperform IterFeedback in the In-Domain setting currently, will it be able to outperform it without this additonal challange?

- In section 4.4,  the authors are assessing the impact of different training stages, but the table shows "−memorization", "−retrieval training", "−constraining". If I understand correctly, constraining is an decoding strategy used in inference stage, while the third training stage "end-to-end agent-tuning" does not show up.

Please also pay attention to the questions and suggestions in the "Weaknesses" part.

### Soundness
1

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
This paper proposes ToolGen, a generative tool/function calling framework. The concrete methods are: (1) virtualizing tools by virtual tokens; (2) memorizing tools with training data of (tool docs, tool virtual tokens); (3) learning tool retrieval with training data of (user queries, tool virtual tokens); (4) and finally, finetuning tool agent with tool calling trajectories. Experimental results with over 47,000 tools show that ToolGen not only achieves superior results in both tool retrieval and autonomous task completion but also sets the stage for a new era of AI agents that can adapt to tools across diverse domains.

### Strengths
Overall, I like this paper very much.  

1. ToolGen is now paradigm for fundamentally transforming tool retrieval into a generative process, which is a very important topic for function calling or LLM-based agents.  
2. The methods are sound and resonable; the paper presentation is clear.  
3. The experimental results show that the methods are effective compared with several strong baselines.

### Weaknesses
1. Traditional retrieval and generation methods for function calling can handle dynamic tools. If the tool set is changing, could ToolGen be used (without retraining)?

2. A few reltated works are not mentioned or compared. For example, TPTU and TPTU-V2 [1,2,3,] used demo retriever and fintuner besides the tool retrieval, which may be more powerful than the traditional retrieval and generation methods. They can be a strong baseline for comparision.  

3. It seems that ToolGen uses a more complex process (i.e., (1) virtualizing tools by virtual tokens; (2) memorizing tools with training data of (tool docs, tool virtual tokens); (3) learning tool retrieval with training data of (user queries, tool virtual tokens); (4) and finally, finetuning tool agent with tool calling trajectories) to prepare for tool calling. Therefore, the suprior of ToolGen may come from more training of LLMs? Could the authors give more explination on this?

### Questions
see the above.

### Soundness
3

### Presentation
3

### Contribution
4
