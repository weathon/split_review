# Neutral residues: revisiting adapters for model extension

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
We address the problem of extending a pretrained large language model to a new domain that was not seen at training time, like adding a language for which the original model has seen no or little training data.  
Popular solutions like fine-tuning or low-rank adaptation are successful at domain adaptation, but formally they do not add any extra capacity and degrade the performance in the original domain. 

Our paper analyzes this extension problem under three angles: data, architecture and training procedure, which are advantageously considered jointly. In particular, we improve adapters and make it possible to learn an entire new language while ensuring that the output of the neural network is  almost unchanged in the original domain. 
For this purpose, we modify the new residual blocks in a way that leads each new residual block to output near-zeros in the original domain. 

This solution of \emph{neutral residues}, which borrows architectural components from mixture of experts, is effective: with only 20\% extra learnable weights compared to an original model trained on English, we get results that are significantly better than concurrent approaches (fine-tuning, low-rank or vanilla adapters) in terms of the trade-off between learning a new language and not forgetting English.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes neutral residues, an improvement on adapters that allows for domain adaptation while preserving the model performance in the original domain. Neutral residues are additional feed-forward gated adapter blocks added to the model, which are optimized such that the if the input is in the pretraining distribution, the adapter output is sparse. The paper studies the effect of factors such as percent of data from the original distribution, adapter architecture, adapter initialization, and adapter training loss.

In experiments for English and multilingual models with French and German finetuning datasets, neutral residues show some improvement over other domain adaptation approaches (full fine-tuning, LoRA, and vanilla adapters) in terms of the trade-off between retaining the model's original knowledge (English perplexity and benchmarks) and learning the new domain (French/German perplexity and benchmarks).

### Strengths
- The experiments show some improvement on the trade-off between the original domain and the adaptation domain.
- The idea of optimizing for sparse output if the input follows the training distribution is interesting and seems like a plausible way to maintain the original model performance.

### Weaknesses
 - Other than the use case provided in the experiments, when is this approach useful instead of something like LoRA or fine-tuning? It seems like the application in the experiments is for a very specific use case where one large domain adaptation would need to be applied, but in real-world settings there are often multiple downstream tasks that would need to be adapted to. The paper does not sufficiently explore the applicability of this method in more complex scenarios involving multiple domain adaptations or task-specific fine-tuning after domain adaptation.
- The additional 20% of parameters seems very high, especially for larger model sizes. It would be valuable to see the results for other domain adaptation methods with varying numbers of additional parameters in Table 3 to provide stronger evidence for the method. Specifically, it's unclear if the performance gains are due to the method itself or simply the increased parameter count. A comparison with LoRA and adapter methods using a similar parameter budget is needed to isolate the effectiveness of the proposed approach.
- The experiments would be strengthened by timing comparisons during training and inference. It is not clear to me what the computational cost of this approach is when compared to the other domain adaptation approaches. The paper should include a detailed analysis of training and inference time, including the overhead of the gating mechanism and sparsity loss, to provide a complete picture of the computational trade-offs.

### Questions
- It would be useful to clarify the introduction and method section to make it more clear what the exact contributions are. Especially in the method section, it is unclear which aspects of the approach are novel.
- A variety of architecture choices were made based on preliminary experiments that are not shown in the paper. It would be useful to include these results in the appendix to support these decisions.

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
This paper proposes a new training recipe, with data, architecture, and loss innovations, for adapting a pretrained language model to a new language.

### Strengths
The paper addresses an important question: how do we extend a pretrained language model to a new language, without hurting original performance.

### Weaknesses
1. More languages are needed to validate the claims. Currently the extensions considered are French and German, which are arguably much more similar to English, syntax- and lexicon-wise, than many other human languages. To show the effectiveness of the proposed method, the authors should consider evaluating on languages that are known to be under-represented (_e.g._, tasks from the XTREME-UP dataset). Specifically, the current evaluation does not sufficiently demonstrate the method's robustness across diverse linguistic structures and vocabularies. Languages with different word orders, morphological complexity, or writing systems could reveal limitations not apparent in the current set of experiments. For example, languages with agglutinative morphology or those using non-Latin scripts could pose significant challenges to the proposed adaptation method.
2. The assumption of access to a 'similar [pretraining] distribution' (Sec 3) is unrealistic in many cases. The paper does not clearly define what constitutes a 'similar distribution', making it difficult to assess the general applicability of the method. Furthermore, the method's reliance on this assumption is a significant limitation, as access to the original pretraining data distribution is often not feasible in practice. This lack of clarity and the practical constraint it imposes raise concerns about the method's real-world applicability. The authors should evaluate whether approaches that mitigate forgetting with anchors are effective.

### Questions
What are the languages and datasets used to train 'Transformer Multilingual' described in Appendix A?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
this paper proposes a new adapter architecture that is designed to extend a pretrained model to new domain/language by continue training on new data mixture while freezing the backbone model. The goal is to improve the model performance on new language while incurring minimal forgetting on the pretraining domain/language. The adapter contains several gating mechanism as seen in Figure 2 of the paper. Experiments are done comparing to LoRA, vanilla adapters, full fine-tuning on both open-sourced and closed-sourced models which shows that the proposed method has the best trade-off.

### Strengths
1. this paper addresses the problem of efficient adaptation of LLMs to new knowledge without forgetting, which is an important problem for practical usages of these models.
2. the proposed architecture is relatively novel, although the presentation is lacking.
3. The paper includes thorough evaluations of factors like initialization, data mixing, and architecture choices.

### Weaknesses
1. this paper is not very well-written so it is difficult to fully asses the content. Section 3 discusses adapter gating and local loss, but I still don't fully understand what each component is like. It is better to write down how the input is transformed through the adapter layer using math formulas.
2. there are some architecture choices that are not clearly explained. Why did you use Silu and Elu activations? 
3. on line 315 the authors mentions that the training batch size is 64 and 8, which is quite small. This might make full fine-tuning more unstable. This might not be a fair comparison between different methods. 
4. In table 8 the authors show the trade-off between different learning rates, but it's not clear what data mixture it's using. The percentage of new data can affect the conclusion too.

### Questions
1. is there ablations about different activation choices?Why did you use Silu and Elu activations? 
2. does your method still works best if the amount of training data is less than what's used in the experiments?

### Soundness
1

### Presentation
1

### Contribution
3
