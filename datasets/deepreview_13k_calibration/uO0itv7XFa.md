# Disentangling Reasoning Tokens and Boilerplate Tokens For Language Model Fine-tuning

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5

## Abstract
When using agent-task datasets to enhance agent capabilities for Large Language Models (LLMs), current methodologies often treat all tokens within a sample equally. 
However, we argue that tokens serving different roles—specifically, reasoning tokens versus boilerplate tokens (e.g., those governing output format)—differ significantly in importance and learning complexity, necessitating their disentanglement and distinct treatment. 
To address this, we propose a novel Shuffle-Aware Discriminator (SHAD) for adaptive token discrimination.
SHAD classifies tokens by exploiting predictability differences observed after shuffling input-output combinations across samples: boilerplate tokens, due to their repetitive nature among samples, maintain predictability, whereas reasoning tokens do not.
Using SHAD, we propose the Reasoning-highlighted Fine-Tuning (RFT) method, which adaptively emphasizes reasoning tokens during fine-tuning, yielding notable performance gains over common Supervised Fine-Tuning (SFT).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the challenge of fine-tuning Large Language Models (LLMs) for agent capabilities by introducing a novel approach to token differentiation during training. The authors observe that in agent-task datasets, tokens serve different roles - specifically reasoning tokens (which contain task-specific logic) and boilerplate tokens (which handle output formatting and standard transitions). The authors' empirical analysis shows that their method effectively identifies reasoning tokens and enhances their learning while maintaining performance on boilerplate tokens, leading to improved overall agent capabilities in LLMs while preserving generalization ability.

### Strengths
This paper demonstrates notable strengths across several dimensions. In terms of originality, it introduces a fresh perspective on token differentiation in agent training through its novel SHAD method and adaptive weighting mechanism, being the first to explicitly address the distinction between reasoning and boilerplate tokens. The quality of the work is evident in its comprehensive evaluation across multiple benchmarks, well-designed ablation studies, and clear empirical evidence supported by thorough loss analysis and effective visualizations. The clarity of the paper is commendable, featuring a well-structured presentation, clear explanations supported by helpful diagrams, accessible mathematical formulations, and illuminating examples and case studies. The significance of the work is substantial, as it addresses a fundamental challenge in agent training, demonstrates meaningful improvements over existing methods, offers a practical and implementable approach, and provides insights that could extend beyond agent training. What makes this paper particularly strong is how it combines novel conceptual insights with practical implementation, all while maintaining clarity and reproducibility in its presentation.

### Weaknesses
While the shuffle-based discrimination method is innovative, it lacks theoretical foundations and formal guarantees, with arbitrary thresholds for token classification. There's also a noticeable absence of qualitative analysis demonstrating how improved reasoning manifests in actual outputs.

### Questions
Could you provide a qualitative analysis demonstrating how improved reasoning manifests in actual outputs?

### Soundness
3

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
This paper proposes to enhance LLM fine-tuning by disentangling the reasoning and boilerplate tokens, implemented by discriminating the two types of tokens with loss differences first, then adaptively optimizing the differential weights of different tokens. Experimental results on several tool-use datasets show that the proposed strategy can outperform naïve SFT.

### Strengths
1. Introducing token-wise loss to LLM agents and fine-tuning with differential weights are interesting, and empirical results on some datasets demonstrate the initial premise.
2. The paper's writing is well and easy to understand.

### Weaknesses
1. Apart from the concrete definition of different token types, there is no ground truth data for classifying the reasoning and boilerplate tokens. It would be convincible if the authors could showcase the accuracy of the token classifier, displaying a few cases that are not that universal. The authors should provide a quantitative evaluation of the token classification accuracy, even if it's on a small, manually annotated subset of the data. This would help establish the reliability of their token differentiation method. The current lack of such evaluation makes it difficult to assess the validity of their core premise.
2. As the author presented in lines 74-76 shuffling can cause reasoning tokens mismatching, however, there are no proofs for such a statement. The claim that shuffling causes reasoning token mismatching needs more rigorous justification. The authors should provide a more detailed analysis of how shuffling specifically disrupts the relationship between questions and reasoning tokens, perhaps through a statistical analysis of token co-occurrence patterns before and after shuffling.
3. There are only 8B models for empirical evaluation, the proposed approach should be validated on larger models to demonstrate the generality. The evaluation of the proposed approach is limited by the exclusive use of 8B models. The authors need to demonstrate the effectiveness of their method on larger models to ensure its general applicability. The current results may not be representative of the performance on larger models with different architectures.
4. Not enough explanation for different experimental results and ablation studies. The paper lacks detailed explanations for the observed experimental results and ablation studies. The authors should provide a more thorough discussion of the results, including an analysis of why certain ablation settings performed better or worse. This would help in understanding the underlying mechanisms of the proposed approach.
5. There are typos, such as “Classifiying” in line 211, and the order repeated error in the Compared paragraph.

### Questions
1. Why agent capabilities (i.e., multi-step reasoning and tool-use) are relevant to the reasoning tokens? Sometimes, the instructions and their corresponding tools can be viewed as a kind of commonsense knowledge rather than reasoning.
2. In Figure 1, the authors colored the reasoning and boilerplate tokens for a given instance, however, it confused me. How to choose boilerplate and reasoning tokens for shuffling? And why “find the most popular genre”, “analyze the”, “currently”, and “the most” tokens are reasoning tokens? These tokens are also crucial for reasoning and can be considered as reasoning tokens.
3. Are these training losses in Figure 5-right from LLaMA-3-8B? Such a phenomenon cannot prove the adaptivity of other models.
4. How many conversation data were sampled from ShareGPT and what is the ratio of general conversation and reasoning data? As ShareGPT has already included a lot of reasoning data, it may affect the SFT performance.
5. It seems that RFT loss and SFT loss eventually overlapped after 2000 training steps, and SFT loss decreases faster, but the evaluation accuracies of these methods are way from each other, why did that happen?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper observes that reasoning tokens and boilerplate tokens (also known as format tokens) should be treated differently during fine-tuning; otherwise, models may easily overfit to boilerplate tokens. To address this issue, the authors propose a method called SHuffle-Aware Discriminator (SHAD), which is a data-driven approach designed to automatically identify boilerplate and reasoning tokens from the training set.

Building on the classification results obtained from SHAD, they further developed Reasoning-Highlighted Fine-Tuning (RFT), a variant of standard fine-tuning that assigns larger weights to reasoning tokens.

The proposed methods were tested on agentic benchmarks, particularly on function-calling benchmarks, to demonstrate their effectiveness.

### Strengths
1. The observation is interesting, but it haven't been verified in a larger scale, i.e., whether the differentiation of both tokens till mater when we scale up the diversity of the dataset. 

2.  The authors compared with a very comprehensive list of baselines to demonstrate their effectiveness. 

3. The idea of using probability changes to identify boilerplate tokens is simple, yet effective.

### Weaknesses
1. Related Work Discussion: Some related works should be discussed more thoroughly. One major contribution claimed by the authors is the intention to "emphasize the differences in learning difficulty and importance between reasoning and boilerplate tokens for agent learning." However, this concept has been discussed in previous research, such as Chen (2024b), but not adequately addressed in Section 2.1. Specifically, the related work section lacks a detailed comparison of how the proposed method's approach to differentiating token types compares to existing methods. The authors should clarify whether previous works also consider template-connecting tokens as part of boilerplate tokens, and how the proposed method's focus on automatically disentangling these tokens differs from existing approaches, which might focus on converting agent data into a standard conversational format.

2. Effectiveness and Motivation Concerns: I have doubts regarding the effectiveness and motivation behind differentiating these tokens during training. As noted in the Limitations section, the effectiveness of the proposed approach relies on boilerplate tokens remaining consistent across different samples, as in the used training and evaluation datasets. This limitation could significantly impact the broader applicability of the proposed methods, as their effectiveness may diminish when scaling up the data. The authors should provide statistical evidence demonstrating that even in high-quality human-collected datasets, a substantial proportion of boilerplate tokens persist, and/or show that the model maintains robust performance despite these characteristics. Could the authors conduct additional experiments to investigate this issue further?

3. From the right side of Figure 5, it appears that the proposed method sacrifices the learning of boilerplate tokens to enhance the learning of reasoning tokens. I am concerned that as we scale up the data—assuming we have sufficient diversity for both token types—this approach may ultimately harm overall performance. The authors should investigate whether the performance gains from emphasizing reasoning tokens outweigh the potential loss of learning for boilerplate tokens when the diversity of both token types increases.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2
