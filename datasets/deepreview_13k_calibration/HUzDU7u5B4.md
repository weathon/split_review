# On-Policy Fine-grained Knowledge Feedback for Hallucination Mitigation

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
Hallucination occurs when large language models (LLMs) exhibit behavior that deviates from the boundaries of their knowledge during the response generation process.
Previous learning-based methods focus on detecting knowledge boundaries and finetuning models with instance-level feedback, but they suffer from inaccurate signals due to off-policy data sampling and coarse-grained feedback.
In this paper, we introduce \textit{\b{R}einforcement \b{L}earning \b{f}or \b{H}allucination} (RLFH), a fine-grained feedback-based online reinforcement learning method for hallucination mitigation.
Unlike previous learning-based methods, RLFH enables LLMs to explore the boundaries of their internal knowledge and provide on-policy, fine-grained feedback on these explorations.
To construct fine-grained feedback for learning reliable generation behavior, RLFH decomposes the outcomes of large models into atomic facts, provides statement-level evaluation signals, and traces back the signals to the tokens of the original responses.
Finally, RLFH adopts the online reinforcement algorithm with these token-level rewards to adjust model behavior for hallucination mitigation.
For effective on-policy optimization, RLFH also introduces an LLM-based fact assessment framework to verify the truthfulness and helpfulness of atomic facts without human intervention.
Experiments on HotpotQA, SQuADv2, and Biography benchmarks demonstrate that RLFH can balance their usage of internal knowledge during the generation process to eliminate the hallucination behavior of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper, proposes a novel approach called RLFH (Reinforcement Learning for Hallucination) to reduce hallucinations in Large Language Models (LLMs) by fine-grained, token-level  reward. RLFH leverages an online reinforcement learning framework and was tested across multiple datasets and showed improved fact-based accuracy compared to existing hallucination mitigation strategies.

### Strengths
1. **Fine-Grained Feedback:** RLFH's use of atomic fact decomposition and token-level rewards enables precise correction of hallucinated responses, surpassing the efficacy of previous, more coarse-grained approaches.

2. **Automated Fact Assessment:** The model employs an LLM-driven feedback mechanism to evaluate truthfulness and informativeness, potentially eliminating human intervention and thus increasing scalability.

### Weaknesses
1. **Unsuitable Baselines:** The paper selects "advanced aligned models" such as Zephyr, Orca, Llama2 Chat, and Vicuna 1.5 as baselines (line 311). However, this comparison is unsuitable, as these models differ not only in alignment methods but also in their underlying architectures and training parameters. For a fair comparison, the authors should have evaluated different alignment and hallucination mitigation methods on a consistent model architecture rather than comparing across varied pre-trained models. Specifically, the variations in pre-training data, model size, and attention mechanisms across these models introduce confounding variables that make it impossible to isolate the effect of the proposed RLFH method. A more rigorous approach would involve using a single base model and then applying different alignment and mitigation strategies on top of it.

2. **Unsignificant effect:** Despite the methodological novelty, the empirical results indicate only marginal improvements in factuality compared to some baseline methods. The reported gains, although statistically significant, may not justify the increased computational complexity and reinforcement learning setup of RLFH, especially given the modest FactScore improvements (e.g., +2.0% on some benchmarks). This raises questions about the practical advantages of RLFH over simpler, less resource-intensive approaches. The small improvements in FactScore, while statistically significant, may not translate to meaningful real-world improvements, especially when considering the computational overhead of the reinforcement learning process. A more detailed analysis of the trade-offs between computational cost and performance gains is needed.

3. **Dependence on External Knowledge:** The model’s reliance on external datasets and existing knowledge boundaries raises concerns about its adaptability in real-world scenarios where such data may not be readily available or up-to-date. The reliance on external knowledge sources for factual verification limits the applicability of the method in scenarios where such resources are not available or are unreliable. This dependence also raises questions about the model's ability to handle novel or rapidly changing information, as it would be constrained by the limitations of the external knowledge base.

### Questions
Could the authors replace the current baseline models with a consistent model architecture and compare only different alignment and hallucination mitigation methods?
 This would provide a clearer evaluation of RLFH’s effectiveness by removing confounding factors related to model architecture and pre-training differences.

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
The paper introduces Reinforcement Learning for Hallucination (RLFH), an innovative approach aimed at reducing hallucination in large language models (LLMs). It focuses on instance-level feedback and relies on off-policy data sampling, RLFH provides fine-grained, on-policy feedback at the token level. This method decomposes responses into atomic facts and applies statement-level evaluations to assign feedback to specific tokens in the output, guiding the model to reduce hallucinations. To facilitate on-policy optimization, RLFH includes an automated fact assessment framework to evaluate the truthfulness and helpfulness of these facts. Experimental results on HotpotQA, SQuADv2, and Biography datasets show that RLFH effectively mitigates hallucination in LLMs by balancing their use of internal knowledge during response generation.

### Strengths
1.RLFH provides a novel approach to feedback by breaking down outputs into atomic facts and assigning token-level rewards, which allows for a more precise correction of hallucination errors.

2.By using on-policy data sampling, RLFH ensures that the feedback provided is more aligned with the model’s real-time behavior, improving the relevance and effectiveness of the adjustments made to the model.

3.the experimental results have shown the effectiveness of the proposed approach.

### Weaknesses
1.the proposed method is not a fully reliable on-policy method, as the feedback is provide by the LLM itself, not trustworthy feedbacks. Thus, it is hard to say after multi-turn iteration, if the model will be better, and maybe the wrong knowledge will accumulate.

2.the compared baselines should involve RLHF-based methods, i.e, DPO and RLAIF. Although these methods are not specially designed for on-policy optimization, it is necessary to show how they will perform under this occasion, to verify the motivation in the introduction part.

3.the writing of this paper needs to be polished. There are several typos: e.g., "Turning" -> "Turing"

### Questions
Please refer to the weaknesses

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
3

### Summary
This paper presents RLFH, a method that decomposes the output of large language models into atomic facts and validates them with reference documents. Then the sentence-level evaluation feedback is provided. After that, RLFH traces the feedback back to the original response and builds a token-level reward signal. Finally, an online reinforcement algorithm with these signals adjusts the model behavior to alleviate the illusion. The main contribution is to propose an online reinforcement algorithm based on fine-grained feedback signals and a non-manual, LLM-driven reward model.

### Strengths
1.The motivation of the paper is reasonable, and the problems to be solved are relatively important.

2.The model adjusts the model itself based on the evaluation feedback of the results, rather than just modifying the results. The method is interesting.

3.The analysis of the experimental results is detailed. Both the overall summary analysis and some detailed research are given.

### Weaknesses
1.The paper fails to fully solve the problem it raises. Evasive ignorance, for example, is a type of illusion that can't be detected or changed.

2.The model simply gives feedback on the correctness of each sentence based on the original answer. If the original answer itself has information missing, the model will not be able to correct and give feedback.

3. Please discuss the potential challenges or benefits of extending their method to other LLMs.

### Questions
For page 5 line 267: “Table ??” , please specify which table you are referring to.

### Soundness
3

### Presentation
3

### Contribution
2
