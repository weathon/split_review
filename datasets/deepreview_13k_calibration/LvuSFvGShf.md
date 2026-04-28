# House of Cards: Massive Weights in LLMs

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 8, 5, 3

## Abstract
Massive activations, which manifest in specific feature dimensions of hidden states, introduce a significant bias in large language models (LLMs), leading to an overemphasis on the corresponding token. In this paper, we identify that massive activations originate not from the hidden state but from the intermediate state of a feed-forward network module in an early layer. Expanding on the previous observation that massive activations occur only in specific feature dimensions, we dive deep into the weights that cause massive activations. Specifically, we define \emph{top-$k$ massive weights} as the weights that contribute to the dimensions with the top-$k$ magnitudes in the intermediate state. When these massive weights are set to zero, the functionality of LLMs is entirely disrupted. However, when all weights except for massive weights are set to zero, it results in a relatively minor performance drop, even though a much larger number of weights are set to zero. This implies that during the pre-training process, learning is dominantly focused on massive weights. Building on this observation, we propose a simple plug-and-play method called \texttt{MacDrop} (\textbf{ma}ssive weights \textbf{c}urriculum \textbf{drop}out), to rely less on massive weights during parameter-efficient fine-tuning. This method applies dropout to the pre-trained massive weights, starting with a high dropout probability and gradually decreasing it as fine-tuning progresses. Through experiments, we demonstrate that \texttt{MacDrop} generally improves performance across zero-shot downstream tasks and generation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper reveals that large language models (LLMs) have a bias towards specific tokens due to massive activations in their hidden states, which stem from the intermediate state of early layer feed-forward network modules. The authors define top-k massive weights as those with the greatest impact on these activations and propose MacDrop, a method that employs dropout on these weights during fine-tuning to reduce their influence. By starting with a high dropout rate and gradually decreasing it, MacDrop improves LLM performance on zero-shot tasks and generations, offering a parameter-efficient fine-tuning strategy that enhances model robustness.

### Strengths
1. The paper identifies a new and critical phenomenon in LLMs where specific feature dimensions in hidden states exhibit massive activations, leading to an overemphasis on certain tokens. This discovery contributes to a deeper understanding of potential biases within LLMs.
2. The authors provide detailed experiments and analysis on massive activations and massive weights, in various LLMs.
3. MacDrop is introduced as a plug-and-play method that applies curriculum dropout to pre-trained massive weights during fine-tuning, which is an innovative approach to reducing reliance on these dominant weights.

### Weaknesses
1. Novelty.

1.1 In this paper, the massive weights are rows in weight matrics related to the massive activations. It is similar to Wanda-sp proposed in [1], which is modified from [2]. From this perspective, the novelty of this paper is limited.

1.2 Moreover, the proposed fine-tuning method MacDrop is similar to LoRA. The only difference is that MacDrop uses a curriculum strategy to gradually reduce the dropout rate of the massive weights. However, the improvement of MacDrop over LoRA is less significant.

2. As the authors discovered, different models have different robustness to the massive weights and the phenomenon of massive weights is not as universal as massive activation [3]. It might also imply that MacDrop only works on models that are sensitive to massive weights, e.g. Llama-3-8B and Mistral-7B.

3. The experiments are not sufficient, for example,

3.1. Does the choice of the dataset have any influence on the massive activations and massive weights?

3.2. This paper illustrates the Llama-3-8B model shows the phenomenon that the bos token always has massive activations, regardless of its position. Do other models share the same phenomenon?

### Questions
Please refer to those in the Weakness section.

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
4

### Summary
This paper analyzes the phenomenon of massive weights in LLMs. These weights are related to previously-observed massive activations. The authors find that massive weights are critical for model performance. They introduce a novel dropout method, called MacDrop, which reduces reliance on massive weights and improves performance.

### Strengths
- This paper includes an in-depth analysis of massive weights in LLMs and their relationship to massive activations.
- The investigation builds upon previous observations around massive activations and attention sink tokens. Rather than previous work which focused on token location, this work explores how the bos token, no matter its location in the sentence, emerges as an attention sink.
- The authors present a set of ablation studies demonstrating the effects of preserving the top k massive weights and removing the rest, or dropping the top k massive weights and keeping the remaining weights. They compare these results to baselines on several relevant tasks.
- The MacDrop method performs dropout to weights on a curriculum. The aim of this method is to reduce the dependence on massive weights and therefore achieve higher performance on downstream tasks. These ideas are validated through experimental results.

### Weaknesses
 - MacDrop’s inability to improve performance on generation tasks.
- There does not seem to be any analysis validating the hypothesis that there are fewer massive weights when training with MacDrop. Some demonstration of this would be nice.

### Questions
- What is the additional computational cost of performing MacDrop?

### Soundness
3

### Presentation
4

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
This paper examines the massive weights in LLMs and investigates their significance. Through targeted interventions, the authors demonstrate that these weights, while constituting only a small fraction of the total, are crucial for model performance. Building on these findings, they introduce a parameter-efficient algorithm for fine-tuning LLMs.

### Strengths
The experiments in Section 2 are very insightful. The paper's motivation is based on the empirical analysis massive activations, and then shifts to the relation between massive activations to massive weights, making the motivation very good.

### Weaknesses
1. The analysis of the influence of massive weights is very empirical, limiting the paper's contribution and novelty. To enhance rigor and generalizability, the authors should include a more solid mathematical analysis to better elucidate the roles of massive weights.

2. In Tables 2 and 3, the authors compare their approach with only a single vanilla LoRA/DoRA baseline, which appears insufficiently comprehensive.

3. In Table 3, the performance improvements with "w/ MacDrop" are marginal compared to the LoRA/DoRA baseline.

### Questions
Please see the Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper investigates the phenomenon of “massive activations” in large language models (LLMs), identifying specific “massive weights” in the intermediate layers that significantly impact model performance. The authors show that these massive weights, although few in number, are highly influential during the pre-training process. To leverage this insight, the paper introduces a method called “Massive Weights Curriculum Dropout” (MacDrop), which applies dropout specifically to these massive weights during fine-tuning. By starting with a high dropout probability and gradually reducing it, MacDrop reduces the model’s reliance on massive weights, leading to improved performance on zero-shot downstream tasks and modest improvements in generation tasks. Through extensive experiments across different models and tasks, the paper demonstrates MacDrop’s effectiveness as a simple, parameter-efficient fine-tuning technique that can be easily integrated into existing workflows.

### Strengths
1. Practical and Simple Method: MacDrop is presented as a straightforward, plug-and-play approach that can be applied with minimal modifications to fine-tuning pipelines.
2. High-Quality Writing and Visuals: The paper is well-written and supported by clear figures, making the complex concepts and experimental findings accessible and visually engaging.
3. Clear Experimental Results: The paper provides comprehensive experimental results across various LLM architectures and tasks.

### Weaknesses
1.  Insufficient Comparative Analysis with Other Techniques
The paper does not provide sufficient comparisons between MacDrop and other dropout or regularization techniques, such as Deja Vu[1] and N:M Sparsity[2]. Without such comparisons, it is difficult to assess whether MacDrop offers any distinct advantages over existing approaches. Including these baselines would make the findings more robust and allow for a clearer understanding of MacDrop’s relative performance.
2. Lack of Theoretical Justification for Massive Weights' Impact. 
The paper identifies the phenomenon of massive weights and their importance, but it lacks a strong theoretical explanation as to why these weights have such a significant influence on the model’s performance. Establishing a deeper theoretical foundation could enhance the credibility and understanding of why massive weights dominate model behavior.
3. Unclear Robustness Improvement Claims
Although MacDrop aims to reduce dependence on massive weights, the paper lacks an analysis of whether this actually leads to improved robustness. For example, evaluating the model’s performance under adversarial attacks or noisy inputs would provide evidence of whether MacDrop indeed enhances the robustness of the model. This is crucial to establish the value of MacDrop beyond improving performance in specific tasks.
4. Lack of Practical Implications for Deployment
The paper does not adequately discuss the practical implications of the identified massive weights and the MacDrop method for real-world deployment. For instance, how does the presence of massive weights affect the robustness of models in production settings? Are there potential risks for using such models? Addressing these concerns would help bridge the gap between theory and practical application.
5. Discrepancy between Perplexity and Auto-eval Scores: In Table 1, the paper reports a significant loss in perplexity with MacDrop, while auto-evaluation scores show minimal loss or slight improvement on certain metrics, which is unusual and warrants further investigation to understand the divergence in these evaluation metrics. For example, based on Llama-3-8B, the ppl of "top-5 retaining" is as large as 20.95, with which the model can't even generate a logical diaglogue  in my experimental experimence, while its average score is 71.0 (only drop 2.0), is it possible?
6. Limited Generalizability of BOS Token Magnitudes: Figure 2 shows that the magnitudes associated with the BOS token do not generalize to other tokens, which contradicts the underlying assumption of MacDrop, potentially limiting its effectiveness across different tokens and contexts.

### Questions
1. Discrepancy between Perplexity and Auto-evaluation Scores: There is a significant loss in perplexity with MacDrop, while auto-evaluation metrics show only minimal losses or slight improvements for some tasks. Could the authors provide further analysis on why these two metrics diverge so drastically? Additional clarification on this point could help to interpret the overall impact of MacDrop on model performance.
2. Generalizability of BOS Token Findings: As shown in Figure 2, the magnitudes associated with the BOS token do not appear to generalize to other tokens. This observation seems to contradict the underlying principle of MacDrop, which relies on massive weights associated with the BOS token to generalize across the model. Can the authors explain or justify how MacDrop remains effective given this discrepancy? Further explanation could strengthen the validity of the method across diverse contexts.
3. Using in Long Context: Specifically, when adapted to long context area, the tokens near EOS tokens usually has differential feature distrubutions compared with BOS tokens, is this case, will MacDrop still work?
4. Reproduction: Will the authors make the code for MacDrop publicly available? I would appreciate it if the code could be made accessible before the next review round.

### Soundness
1

### Presentation
3

### Contribution
2
