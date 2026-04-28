# Human-like Episodic Memory for Infinite Context LLMs

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 8, 5, 5

## Abstract
Large language models (LLMs) have shown remarkable capabilities, but still struggle with processing extensive contexts, limiting their ability to maintain coherence and accuracy over long sequences. In contrast, the human brain excels at organising and retrieving episodic experiences across vast temporal scales, spanning a lifetime. In this work, we introduce EM-LLM, a novel approach that integrates key aspects of human episodic memory and event cognition into LLMs with no fine-tuning, enabling them to handle practically infinite context lengths while maintaining computational efficiency. EM-LLM organises sequences of tokens into coherent episodic events using a combination of Bayesian surprise and graph-theoretic boundary refinement in an online fashion. When needed, these events are retrieved through a two-stage memory process, combining similarity-based and temporally contiguous retrieval for efficient and human-like access to relevant information. Experiments on the LongBench and $\infty$-Bench benchmarks demonstrate EM-LLM's superior performance, consistently outperforming the state-of-the-art retrieval model InfLLM across various baseline LLMs. In addition, EM-LLM outperforms its popular counterpart, RAG, in a wide range of tasks, while requiring similar resources. Notably, EM-LLM's performance even surpasses full-context models in most tasks, while successfully performing retrieval across 10 million tokens -- a scale computationally infeasible for such models. Finally, our analysis reveals strong correlations between EM-LLM's event segmentation and human-perceived events, suggesting a bridge between this artificial system and its biological counterpart, thereby offering a novel computational framework for exploring human memory mechanisms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this work, the authors proposed a framework, termed EM-LLM, for LLMs to store previously seen sequences of tokens as memory and then utilize the stored information to improve the performance of newly encountered problems. Specifically, inspired by human episodic memory, the authors suggested a method based on Bayesian surprise and graph-theoretic refinement to parse the sequences into events. Later, these store events were retrieved depending on content similarity and temporal contiguity. Experiments were conducted to demonstrate the performance improvements. In addition, a comparison was conducted to show that the parsing of events by the proposed method was similar to the results of humans, suggesting a potential link to the underlying mechanism in the brain.

### Strengths
Memory is a key function in biological brains that helps organize experiences and use them to guide future behaviours.  The lack of memory function in the  LLM is a major aspect that needs to be addressed. The authors have proposed a framework inspired by the biological memory system for LLMs, which is desirable and may stimulate further investigations in this direction.  Overall, the paper was clearly written, showing comprehensive experimental results.

### Weaknesses
 "Human-like Episodic Memory" is an overstatement. First, episodic memory combines multimodal information into a coherent recollection of experiences, with key aspects including when, where, what, how and with who a event happened. To store a sequence of tokens does not necessarily reflect such a memory. Second, parsing of events in human memory depends heavily on the content, e.g., change of location or context. The Bayesian surprise measure may be a useful proxy to approximate such separation, but it does not by itself suggest a common mechanism, nor support the claim of "human-like". Third, the retrival rule of similarity is generic for memory, not specific for EM.

Another concern is that the memory-based frawmork has been previously proposed (cited as Xiao et al, 2024a in the current paper). The present work is an refinement of the framework, which somewhat limits its noverty.

### Questions
1. I would suggest the authors to better explain the differrence in comparison with Xiao et al. 2024a, and explain why it is an important conceptual advance, instead of an incremental improvement. 
2. To better justify the claim that the mechanism is EM-related with further analyses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces EM-LLM, a novel architecture that enhances the memory capabilities of LLMs by integrating design elements of human episodic memory. EM-LLM employs surprise-based event segmentation, similarity-based, and contiguity-based retrieval to enable LLMs to manage long contexts with computational efficiency. Tokens are organized into episodic events by dynamically detecting boundaries using a surprise metric and further refines these boundaries with graph-theoretic measures. This episodic structure allows EM-LLM to recall information from both the current context and prior temporally contiguous events. Experiments on long-context benchmarks show that EM-LLM outperforms InfLLM and RAG. Additionally, the segmentation results are aligned with human-perceived event structures, suggesting EM-LLM as a computational model of human episodic memory.

### Strengths
Originality: EM-LLM’s incorporation of episodic memory features, particularly surprise-based segmentation, similarity-based, and contiguity-based retrieval, is a novel approach within the domain of LLMs. Using LLM surprise to model event cognition and to approximate episodic memory is original for cognitive modeling. This work not only extends the long-context capability of LLMs but also bridges machine learning and cognitive science, presenting a unique computational framework for studying memory and event cognition.
Quality: The paper demonstrates EM-LLM’s performance on recognized long-context benchmarks. The experiments highlight the model’s improvements in accuracy and efficiency over competing methods, including InfLLM and RAG.
Clarity: The paper clearly presents the concept of episodic memory in LLMs, with a logical breakdown of memory segmentation, refinement, and retrieval mechanisms. The figures generally illustrate the processes well.
Significance: EM-LLM has potential significance in advancing LLM capabilities for long-context tasks, a critical area of LLM development. Beyond practical applications, EM-LLM contributes to interdisciplinary research, providing insights into cognitive science by modeling elements of human episodic memory within an LLM framework.

### Weaknesses
- In Table 1, the performances of S, SM, and SM+C methods are difficult to directly compare since different base LLMs are used in each row. I know the comparison is (partially) in Fig. 4-7 but they are not mentioned in the main text. It would be helpful if explicitly mentioned/referenced in the main text.  
- Although InfLLM is a primary benchmark comparison, it is absent from Figure 1. Including InfLLM in Figure 1 would provide a more complete comparison. The absence of InfLLM in this figure makes it harder to assess the relative performance of EM-LLM against this key baseline, particularly in the context of the other methods presented.
- It’s unclear from the current paper how the number of retrieved events and the number of evicted tokens influence performance. Any plot showing the model’s performance as a function of these parameters would be helpful. The paper lacks a systematic ablation study on the impact of varying the size of the retrieved buffer and the number of evicted tokens, which are critical parameters for the model's efficiency and accuracy. Without this analysis, it's difficult to understand the trade-offs involved in choosing specific values for these parameters, and how they interact with the context length of the input.
- In Formula (1), notations (\mu_{t-\tau:t}) should be corrected, keeping consistent across the context.
- Certain figures would benefit from clarification, as detailed in questions.

### Questions
- Can the authors discuss the feasibility and potential advantages of end-to-end training of networks for event segmentation, refinement, and retrieval, compared to these hand-designed algorithms? As a comparison, these algorithms are implemented by neural circuits in the brain.
- Can the authors discuss how might other features of human episodic memory, such as the hierarchical organization of events (human episodic memory structures can have multi-level segmentation of experiences), benefit EM-LLM’s design in terms of performance? 
- Clarifications for Figures:
In Figure 1, does the data reflect results from S, SM, or SM+C? 
In Figure 2, the memory units seem to have variable sizes, different from the fixed size in InfLLM? Additionally, how are the bars normalized?
In Figure 4A, S appears closer to human segmentation than SM or SC, contrasting with Figure 4B. 
In Figure 4, what does SC stand for? Does "C" refer to the continuity buffer or represent something else?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces EM-LLM, a method for extending the context window of LLMs by incorporating principles from human episodic memory and event cognition. The method segments input sequences into episodic events using a combination of Bayesian surprise and graph-theoretic boundary refinement. It implements a two-stage memory retrieval process that combines similarity-based and temporally contiguous retrieval. The authors evaluate their method on LongBench and InfiniteBench benchmarks, comparing against state-of-the-art retrieval models like InfLLM and RAG.

### Strengths
The paper proposes the idea of equipping LLMs with cognitive science principles (episodic memory and event cognition), which aligns well with current challenges in long-context processing;  
The use of Bayesian surprise for dynamic event segmentation in LLMs is novel, moving beyond simple fixed-length segmentation used in prior work like InfLLM;  
The method achieves 100% accuracy on Passkey.Retrieval task with sequences up to 5M tokens, demonstrating practical scalability;  
The paper provides a scalable alternative to both RAG and full-context approaches, outperforming them on most tasks while maintaining computational efficiency, increasing its practical value.

### Weaknesses
1.The paper claims surprise-based segmentation is superior to fixed-length approaches (like InfLLM), but lacks theoretical justification for why this should be effective. While Figure 4 shows some empirical correlation with human segmentation, there's no analysis of why this leads to better LLM performance. The authors should provide a theoretical analysis showing why this metric captures semantically meaningful boundaries better than alternatives.  
2.The boundary refinement process (Algorithm 1) lacks convergence analysis. Given that it's iteratively adjusting boundaries based on modularity/conductance metrics, it is important to establish guarantees about stability and convergence.  
3.The two-stage memory retrieval process (Section 3.4) introduces ks and kc parameters for similarity and contiguity buffers, but it does not justify the choice of values or analyze their trade-offs.  
4.Although Table 1 shows some improvements over InfLLM, the improvements on most tasks may not be statistically significant.  
5.The human correlation study in Section 4.2 relies on 3 short podcasts, which is insufficient to make broad claims about alignment with human event segmentation. The authors should expand the section to a larger, more diverse dataset of human annotations.  
6.Section 4.4 discusses the impact of contiguity but does not properly ablate different buffer sizes or analyze the trade-off between similarity and contiguity buffers.

### Questions
1.How sensitive is the method to the choice of the surprise threshold parameter? What is the process for tuning this parameter?  
2.How do you ensure the stability of the boundary refinement process? Are there cases where it fails to converge?  
3.Does the issue of needing to query too many matching events still exist when the context window is too long?  
4.If we use the Surprise-based method to segment the context into a RAG format, will the performance remain the same?  
5.How does the method handle dynamic changes in context relevance over time?

### Soundness
2

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
2

### Summary
This paper introduces EM-LLM, a novel approach that integrates key aspects of human episodic memory and event cognition into LLMs with no fine-tuning, enabling them to handle practically infinite context lengths while maintaining computational efficiency

### Strengths
They introduced EM-LLM, a flexible architecture that integrates key aspects of human episodic memory and event cognition into Transformer-based LLMs. Their approach enables existing LLMs to effectively process vastly extended contexts without the need for pre-training. They perform successful passkey retrieval across 5M tokens, a length which is computationally infeasible for current full-context models

### Weaknesses
1. As you mentioned, almost all the methods used in your paper appear to have been proposed by others. Could you clarify what specific innovations you are introducing?

2. You stated that your method outperforms others, but in Table 1, I did not see the impressive results you described. It seems that your method may not be as effective as claimed.

3. Do you apply Eq. (1) to each token individually? If so, I imagine this would require substantial processing time. How do you address this issue?

4. In Eq. (2), could you explain how you derive the key vectors?

5. You employ k-NN in the MEMORY RETRIEVAL stage—does this significantly increase computation time?

6. I found Figure 4 difficult to understand. Could you provide additional explanation to clarify it?

### Questions
The same to Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
