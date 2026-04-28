# Context-Parametric Inversion: Why Instruction Finetuning May Not Actually Improve Context Reliance

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
A standard practice when using large language models is for users to supplement their instruction with an input context containing new information for the model to process. However, models struggle to reliably follow the input context, especially when it conflicts with their parametric knowledge from pretraining. 
In-principle, one would expect models to adapt to the user context better after instruction finetuning, particularly when handling knowledge conflicts. 
However, we observe a surprising failure mode: during instruction tuning, the context reliance under knowledge conflicts initially increases as expected, but then \emph{gradually decreases as instruction finetuning progresses}. This happens while the performance on standard benchmarks keeps on increasing far after this drop. We call this phenomenon \textbf{context-parametric inversion} and observe it across multiple general purpose instruction tuning datasets such as TULU, Alpaca and Ultrachat, across different model families like Llama, Mistral, and Pythia. We perform various controlled studies and theoretical analysis to show that context-parametric inversion occurs due to examples in the instruction finetuning data where the input context provides information that aligns with model's parametric knowledge.
Our analysis suggests some natural mitigation strategies with limited but insightful gains, and serves as a useful starting point in addressing this deficiency in instruction finetuning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work explores the context-reliance failure in instruction tuning, that is observed during the instruction finetuning of large language models. While finetuning is expected to improve a model's adherence to input context, the study finds that context reliance decreases as the training goes. The authors examine this behavior across several datasets (TULU, Alpaca, Ultrachat) and model families (Llama, Mistral, Pythia), and conduct comprehensive controlled studies to isolate the causes. The paper further provides theoretical analysis and suggests potential mitigation strategies.

### Strengths
- The identification and analysis of the context-parametric inversion phenomenon could contribute to our understanding of LLM behavior during instruction tuning. The findings in this work are helpful for future work in this direction.

- The analysis is conducted across multiple datasets and model families, ensuring the robustness of the findings. The paper includes controlled studies to rule out simple hypotheses, contributing to a deeper understanding of the phenomenon.

- The theoretical analysis provides a solid foundation for understanding the observed behavior and suggests potential mitigation strategies.

### Weaknesses
The learning rate also has a non-trivial impact on performance. What are the considerations for selecting 1e-4 and 1e-5 as learning rates? What are the trends across different learning rates?

### Questions
Typo: Line 311 seems to need changing to Figure 3c?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies an interesting phenomenon during instruction fine-tuning, in which context reliance first increases but later decreases as the model increasingly leverages parametric knowledge. Using three knowledge-conflict datasets to measure counterfactual accuracy and parametric accuracy during instruction finetuning, the authors demonstrate this phenomenon experimentally, across a few combinations of LLMs and instruction-tuning datasets. The paper includes a theoretical argument that aligns with the observation that removing data points where the context aligns with the parametric knowledge mitigates this phenomenon. Finally, the authors explore several strategies for mitigating this context-parametric inversion.

### Strengths
- The authors conduct a series of experiments that (1) demonstrate this context-parametric inversion is a persistent phenomenon, (2) test (and rule out) various hypotheses, (3) show that non-context-critical data points (data points where the context aligns with the parametric knowledge) are likely to blame, and (4) reveal the shortcomings of existing data augmentation or training approaches. These experiments are comprehensive and intuitively presented.

- The theoretical argument and justification for why this phenomenon occurs are reasonably easy to follow and sufficiently rigorous, certainly helping to validate the experimental results presented in Fig. 3(c).

### Weaknesses
 - A few sections could use a bit of refinement for clarity. For instance, additional discussion on how counterfactual and parametric accuracy are measured on the context-parametric conflict datasets would be helpful beyond what is present at the beginning of Sec. 3. Another topic that could use a bit more explanation is the context-based filtering of Alpaca.

- Additional analysis on counterfactual data augmentation would be nice to have. The difference in results between Alpaca and TULU suggests that the ratio of counterfactual data included in the fine-tuning data mix is somewhat impactful. Additional ablations on this ratio would be interesting.

- I’m slightly concerned with the quality of the constructed context-parametric conflict datasets, given that most of the experimental results center around these datasets. For instance, for the CF_BIO task, the authors apply entity substitutions algorithmically rather than using an entity-substitution model as previous works have done in order to avoid “an incoherent context and an inaccurate estimate of the context-reliance”. Yet, looking at the provided examples reveals these inconsistencies are still present. For example, in the second CF_BIO example on pg. 19 line 993, “William Shakespeare” was correctly substituted with “Julius Caesar” at the beginning of the context, but later occurrences (particularly of just the last name “Shakespeare”) were left unchanged (see lines 997 and 1001). When measuring counterfactual accuracy, the context for the question “What is the name of the author who wrote Hamlet, Romeo and Juliet, Macbeth?” should not include the phrase “Shakespeare’s big break came with the success of Romeo and Juliet”.

### Questions
- Could you verify that the inconsistencies in the constructed context-parametric conflict datasets (see weaknesses above) are isolated incidents not present in the vast majority of the instances? Specifically for the CF_BIO task, was substitution only done for full entity names or did you make some attempt to catch analogous or shortened entity names?

- In Sec. 4.1 line 292, what do you mean by test set? The three context-parametric conflict datasets? If so, maybe another term besides “test set” can be used since “test set” implies that it’s drawn from distribution as the training set, which would not be the case between these context-parametric conflict datasets and instruction-tuning datasets.

- Related to Sec 4.2, can you expand on the filtering done on the Alpaca dataset to produce the context-only Alpaca dataset? How do you decide if an instance has “some input context”? Likewise, in Sec 4.3, is the perplexity loss computed using the base model (e.g., Llama-7b for Alpaca-7b)?

- Can you explain the setting in Fig. 4(d)? The title seems to indicate that it’s comparing your standard finetuning configuration to the QK finetuning configuration discussed in Sec. 6, but the legend indicates that those results only use the QK finetuning configuration on different datasets (Alpaca vs Alpaca context-only).

- In figs 5, 6, 7 in A.1 and figs 8 and 9 in A.2, is “ID Accuracy” the same as “Standard Benchmarks Performance,” or is there some nuanced difference that I’m missing?

- Are the training runs done with a fixed learning rate? Could decaying the learning rate during training diminish the prevalence of the context-parametric inversion by scaling down the large gradients from the non-context-critical data points?

Other comments not factored into my decision assessment:
- Sec A.4, line 903 (Fig 12 caption): “fullfinetuning” -> “full finetuning”

I am willing to raise my score if my questions/concerns are adequately addressed.

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
The paper investigates a phenomenon termed context-parametric inversion in large language models (LLMs), where LLMs' instruction following ability reduced after fine-tuned on a certain amount of instruction data despite a increase at the beginning. This study reveals that while fine-tuning initially increases the model's reliance on input context, it eventually shifts back toward using its internal, parametric knowledge, leading to context-related errors or hallucinations.

### Strengths
By examining multiple model families (Llama, Mistral, Pythia) and instruction datasets (TULU, Alpaca, UltraChat), the authors provide robust evidence for the findings in the paper.
This paper offers a theoretical framework explaining how gradients from context-critical and non-context-critical points interact during fine-tuning. This framework gives a deeper insight into why the inversion happens, moving beyond empirical results to provide a conceptual basis for future research.

### Weaknesses
Inconsistent x-axis in the figures, some of them do not start from 0 and lack of explanation on these x-axis. Inconsistent or unexplained x-axis scales can indeed impact the interpretability and robustness of the findings in the paper.

Typo in line 311, it should be Figure 3c instead of Figure 3b.

Missing reference: Instruction-following Evaluation through Verbalizer Manipulation. Li, S., Yan, J., Wang, H., Tang, Z., Ren, X., Srinivasan, V., & Jin, H. In 2024 Annual Conference of the North American Chapter of the Association for Computational Linguistics, 2024.

### Questions
Can you give a detail explain on the x-axis for each figure?

### Soundness
2

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
This paper reveals a counterintuitive phenomenon where LLMs become less reliant on contextual information despite being finetuned to enhance their ability to follow instructions and context. Through empirical studies and theoretical analysis, the authors identify the cause of this "context-parametric inversion" and propose mitigation strategies, offering valuable insights into improving LLM performance in context-dependent tasks.

### Strengths
This is a very interesting paper that identifies an obvious flaw in instruction fine-tuning and gives preliminary mitigation methods.

The experimental and theoretical analysis of the paper is solid.

### Weaknesses
There are no obvious weaknesses in the paper.

### Questions
I have a few questions for the authors：
1. Whether the “context-parametric inversion” phenomenon can be mitigated by using a smaller learning rate.   
2. Would a parameter-efficient fine-tuning method like LoRA have the same problem?  
3. Since the curve goes up and then down, does this mean that it is better to use a small amount of fine-tuning data rather than a large amount of fine-tuning data to enhance the context-following ability of the model.

### Soundness
4

### Presentation
4

### Contribution
4
