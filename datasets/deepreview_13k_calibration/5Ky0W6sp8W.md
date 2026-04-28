# The Buffer Mechanism for Multi-Step Information Reasoning in Language Models

- Decision: Reject
- Avg Score: 6.25
- Scores: 5, 6, 8, 6

## Abstract
Large language models have consistently struggled with complex reasoning tasks, such as mathematical problem-solving. Investigating the internal reasoning mechanisms of these models can help us design better model architectures and training strategies, ultimately enhancing their reasoning capability. In this study, we constructed a symbolic dataset to investigate the mechanisms by which Transformer models employ vertical thinking strategy based on their inherent structure and horizontal thinking strategy based on Chain of Thought to achieve multi-step reasoning. We introduced the concept of buffer mechanism: the model stores various information in distinct buffers and selectively extracts them through the query-key matrix. We proposed a random matrix-based algorithm to enhance the model's reasoning ability, resulting in a 75\% reduction in the training time required for the GPT-2 model to achieve generalization capability on the PrOntoQA dataset. These findings provide new insights into understanding the mechanisms of large language models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper studies the 'buffer mechanism' in transformers for solving a in-context multi-hop reasoning task. The task requires chaining associations present in the context (e.g. "a->b, b->c") to perform multi-hop reasoning (e.g. "a->c"). Inspired by the copying + induction head mechanisms found in prior work, the authors hypothesize that transformers trained to perform this task sequentially look up the necessary reasoning steps and form intermediate answers at the last token position, so that the second layer looks up the first hop, the third layer looks up the second hop, etc. By default the intermediate representations persist in the residual stream at the last token; to prevent the intermediate representations for one hop from interfering with those for a later hop, the authors hypothesize that the intermediate representations are kept in separate 'buffers', i.e. linearly isomorphic subspaces that are disjoint from each other.

The authors empirically test the hypothesis by measuring the alignment of certain weight matrices in a 3 layer transformer trained to do 2-hop reasoning. Further, the authors proposed a parametrization of the attention weight matrices that biases the network towards forming these disjoint subspaces that reduce interference. They find that this parametrization reduces the number of training steps needed for a 12-layer transformer to learn the ProntoQA task.

### Strengths
- Multi-hop reasoning in language models is an important problem to study
- The figures are beautifully made
- The observation that multihop reasoning can generalize to unseen tokens because the embeddings at initialization already have the required properties is neat

### Weaknesses
 - The paper centers its analyses on small transformers trained on synthetic tasks. It is not clear if any finding can be transferred to practical language models trained on text. Prior work has already studied two-hop reasoning in practical language models in more realistic tasks --- a more convincing demonstration of the buffer mechanism is to identify it in these settings.

Overall, the empirical analyses are weak and can benefit from more careful experimental techniques. In particular:
- In sec 3.1, the authors argue that a particular transformer that they trained exhibit the buffer mechanism by comparing metrics about how aligned certain weight matrices are. This is much weaker and more circumstantial than directly performing causal interventions on the activations to verify their claims. The weight alignment phenomena they highlight could arise from various training dynamics and might not be specific to the proposed buffer mechanism. For example, the observed alignment between $W^{QK}$ and $W^{VO}$ could be a byproduct of the optimization process rather than a deliberate mechanism for multi-hop reasoning. Furthermore, the authors do not demonstrate that these weight matrices are individually non-diagonal, but their composition is, which would be more compelling evidence.
- Further, the authors did not empirically compare the buffer mechanism with any competing mechanisms. Off the top of my head, I imagine one competing explanation would be that instead of storing intermediate representations in distinct buffers, maybe the transformer instead learns to overwrite stale representations with new representations. Such a mechanism could conceivably still possess similar weight alignment patterns as the buffer mechanism. The authors need to provide evidence that the proposed buffer mechanism is more likely than the overwrite mechanism. Specifically, they should specify how the kernel or matching scores would differ between the two mechanisms and provide experimental evidence to support their claim.
- Exacerbating this, the authors only performed this analysis on a 3-layer transformer, whereas their diagram (Fig. 3) and their theoretical construction would work for arbitrarily deep models. It is conceivable that interesting divergences between the buffer mechanism and the overwriting mechanism may only appear at deep enough models.


### Questions
- I can understand the idea behind matching score, but can you provide motivation for the kernel score? Why is there a factor of $n$ in the numerator? My understanding is that Ker should be a $d_m \times d_m$ matrix, so it's mystifying to me why $n$ is there. It's also really hard to interpret this quantity. In comparison, I think your matching score is makes a lot more sense, because the softmax constrains it to [0,1], and so I know how to interpret values. My personal guess is that operator norm of the difference between the kernel and identity would be a good metric, but I'd be curious to hear the reasoning behind your choice.
- Do you perform hyperparameter sweeps for the results in sec. 5? If not, the finding that RMBA speeds up training could simply be because the parametrization some how matches the default hyperparameters you use, and not because of any real gains. I believe at the very least you should sweep learning rate for each of the 3 methods and record the best result.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a "Buffer Mechanism" that could be used by Transformers to perform reasoning tasks.  For a specific synthetic reasoning task, the authors give a concrete mathematical description of how the proposed Buffer Mechanisms might implement vertical-style reasoning (through the layers of a Transformer), and horizontal-style reasoning (like Chain-of-Thought).  The authors also suggest a tweak (arising from their Buffer Mechanism formulation) by which the performance of Transformers might be enhanced.

### Strengths
The proposed Buffer Mechanism makes sense, though its description seems a little obfuscated.  The paper sets an ambitious and laudable goal : Understanding of how Transformers can implement the learning of reasoning.  The experiments included demonstrate that, when measured using benchmarks chosen by the authors, the method suggested is effective.  The performance-enhancing tweak suggested makes sense in the context of making reasoning mechanisms more learnable overall - certainly an interesting direction.

### Weaknesses
The paper proposes a "Buffer Mechanism" that could be used by Transformers to perform reasoning tasks.  For a specific synthetic reasoning task, the authors give a concrete mathematical description of how the proposed Buffer Mechanisms might implement vertical-style reasoning (through the layers of a Transformer), and horizontal-style reasoning (like Chain-of-Thought).  The authors also suggest a tweak (arising from their Buffer Mechanism formulation) by which the performance of Transformers might be enhanced.

The proposed Buffer Mechanism makes sense, though its description seems a little obfuscated.  The paper sets an ambitious and laudable goal : Understanding of how Transformers can implement the learning of reasoning.  The experiments included demonstrate that, when measured using benchmarks chosen by the authors, the method suggested is effective.  The performance-enhancing tweak suggested makes sense in the context of making reasoning mechanisms more learnable overall - certainly an interesting direction.

The paper make the bold assumption that the "Buffer Mechanism" that is described is the specific mechanism that Transformers are using to perform reasoning.  Before being proven, this seems like it should be treated more like a hypothesis.  And the experiments given do not prove anything in general, rather point towards this mechanism being plausible for their particular set-up.  For example:
* L079 : "Specifically, we found that Transformers utilize a Buffer Mechanism when engaging in complex reasoning".  As far as this reviewer can ascertain, this was not proven, even experimentally.  
* L091 : "We discover the buffer mechanism employed by language models" - again this is a very broad claim, given the evidence shown.
* etc...

So perhaps, it would be better to restate quite a few of the claims made...
* L501 : "we investigated the buffer mechanism employed by Transformer models" -> "we investigated how Transformers might implement a buffer mechanism"

In the section around L248 : "This indicates that the model has learned the underlying patterns in the data."  This seems like a statement about a property of model training, whereas the result indicated by Eqn 11 depends on L238 ("When same-token matching happens") - which appears to be circular logic.  (i.e. given that it has learned X, then it has learned X')

Minor things:
* Figure 1 : Testing each LLM on the same question 9 times, and listing out the results (rather than, for instance, showing a histogram) really emphasised how little the performance of these LLMs was investigated
* Figure 2 : "Serialized Reprentation" -> "Serialized Representation"

### Questions
Would it be reasonable to have a mental model of the Buffer Mechanism as being the result of there being a basis (~L209) in which the layer-wise transformations/matching for the Transformer internal representations are approximately block-diagonal (these sub-representations being the buffers)?

Figure 5a : Why does the test accuracy go down before epoch 50?  And then leap up?  What happens at epoch 50?

How are the embeddings of the tokens learned (in particular the OOD tokens)?  

Doesn't Appendix D indicate that "The Buffer Mechanism" presented in the body of the paper is likely only a partial explanation of what is actually being performed by Transformers?

### Soundness
3

### Presentation
4

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
This paper proposes a mechanistic analysis of multi-step reasoning in language models. In particular, the authors design a synthetic task that requires the model to construct an n-step deductive reasoning chain. In this setting, the authors show that a decoder-only single-head transformer implements what they term a “buffer mechanism”: the attention weight matrices W_q and W_k act as information-extractors that retrieve information from a set of buffers implemented by the W_v and W_o matrices. This framework is first formally explained, then empirically verified. The authors then connect this result to the horizontal computation involved in CoT reasoning. Additionally, the paper proposes an approach to modify the attention weight matrices in such a way to create an additional buffer, and presents evidence showing its effectiveness both on the synthetic task designed by the authors and on ProntoQA.

### Strengths
- The problem address is Interesting and relevant.
- Solid experimental evidence support the hypothesized mechanism.
- The authors use insights on the model's internal mechanics to propose a method for improving training, which is show to be effective.

### Weaknesses
The link to CoT reasoning is somewhat tenuous. Although the authors demonstrate how a 2-layer transformer could theoretically implement a multi-step reasoning algorithm for the synthetic task, this does not imply that a transformer-based language model uses the same approach to perform CoT reasoning. The statement, “in Fig. 6 we illustrate how the Transformer model employs CoT for multi-step reasoning” (lines 341-342), feels overly assertive and lacks supporting empirical evidence. The core claim that CoT leverages repeated overwriting of a single buffer, as opposed to forming multiple buffers in vertical reasoning, is not sufficiently supported. While the paper shows a model trained on 13-step reasoning can predict tokens beyond the 13th position, this observation alone doesn't prove the buffer overwriting mechanism. The paper needs more direct evidence to support this claim, such as analyzing the attention patterns and value transformations during CoT inference, to show that the same buffer is indeed being reused across steps.

### Questions
Can the authors provide empirical evidence about the hypothesized CoT mechanism?

### Soundness
3

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
3

### Summary
This paper analyzes the internal reasoning mechanisms of Transformers, from the perspective of vertical and horizontal thinking on a symbolic multi-step reasoning dataset. They analyze the concept of Buffer Mechanism, by which the model stores information and retrieves it through the query-key matrix. They explain how the model is leveraging this mechanism enhance the model’s multi-step reasoning capability. Finally, they show how their method reduces the cost of generalization.

### Strengths
1. Insightful Findings. The paper presents interesting findings on how the Transformers make use of the Buffer Mechanism. 
2. Great Contribution. RMBA show that the authors can leverage the Buffer Mechanism to provide better efficiency. 
3. Rigorous experimentation. The analysis and experiments show a careful detail and understanding of the processes.

### Weaknesses
1. Poor Presentation: The paper is hard to read in general. There are few explanation to the equations and Figures. The presentation of the work does not follow a good format. I believe the paper can have a much greater impact if the more attention is given to the paper writing and presentation. 
2. Presentation of experiment results: The paper does clearly define the metrics to compare the results from IMBA and RMBA, which makes it hard to understand at first reading. For example, in Figure 7, they show that the IMBA model is unable to achieve a good test accuracy, but they do not quantify it or provide any further analysis. 
3. Better Math Descriptions: Equations and Formulas are introduced without a former introduction and explanation.

### Questions
Some questions about the paper: 
1. Can you explain why you claim 75% when compared to the baseline? I see the plots on Figure 8, but I cannot see the numbers to quantify this generalization myself. 
2. Does the RMBA have some drawback during training? I assume the training process might be more unstable due the randomness of the matrix, is such behavior observed?

In general more clarity and better description of the experiments can help understanding the paper better. I miss a clear structure of the paper to understand it better the first time. 

Some recommendations: 
- Figure 2: It is missing an explanation of what (a) and (b) figures represent and what are the takeaways from those figures. 
- Figure 5,6: Both are hard to read and not display the axes. I can deduct their meaning after reading the paper. But more clarity can help other readers. 
- Figure 4: How does it provide a better understanding of the analysis?

### Soundness
3

### Presentation
3

### Contribution
3
