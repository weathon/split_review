# A Theory for Token-Level Harmonization in Retrieval-Augmented Generation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Retrieval-augmented generation (RAG) utilizes retrieved texts to enhance large language models (LLMs). Studies show that while RAG provides valuable external information (benefit), it may also mislead LLMs (detriment) with noisy or incorrect retrieved texts. Although many existing methods attempt to preserve benefit and avoid detriment, they lack a theoretical explanation for RAG. The benefit and detriment in the next token prediction of RAG remain a 'black box' that cannot be quantified or compared in an explainable manner, so existing methods are data-driven, need additional utility evaluators or post-hoc. This paper takes the first step towards providing a theory to explain and trade off the benefit and detriment in RAG. First, we model RAG as the fusion between distribution of LLM’s knowledge and distribution of retrieved texts. Then, we formalize the trade-off between the value of external knowledge (benefit) and its potential risk of misleading LLMs (detriment) in next token prediction of RAG by distribution difference in this fusion. Finally, we prove that the actual effect of RAG on the token, which is the comparison between benefit and detriment, can be predicted without any training or accessing the utility of retrieval. Based on our theory, we propose a practical novel method, \textbf{Tok-RAG}, which achieves collaborative generation between the pure LLM and RAG at token level to preserve benefit and avoid detriment. Experiments in real-world tasks using LLMs such as OPT, LLaMA-2, and Mistral show the effectiveness of our method and support our theoretical findings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In RAG settings, retrieved passages may contradict the parametric memory of an LLM (obtained during the LLM training process). The paper explores how to reason and trade-off between the two sources of information in a more optimal manner compared to existing methods. The authors provide a theoretical framework for understanding this in terms of a latent concept variable $z$ and later connect it to a practical method that relies on calculating some of the required quantities by peeking inside the transformer architecture. Without any additional training or models, but with a whitebox approach, the method is able to outperform other RAG baselines that attempt this task.

### Strengths
The paper has a fair bit of novel theoretical underpinnings for thinking about retrieved knowledge in terms of a latent concept variable. And if sound and practical, there is significance to the findings especially when it comes to merging two sources of information. The writing is overall clear (except for the items in weaknesses) and quality is fair as well.

### Weaknesses
The paper tries to do two things at once, provide both theoretical and practical justification. However, the theoretical justification is at best very convoluted and at worst incorrect. The practical justification is a good start, but the authors test on QA datasets with factoid answers potentially hiding the fact that their method may not generalize outside of this setting. It would be more convincing if the authors did one thing (either theoretical or practical) in a sound and convincing manner rather than attempting both but being unconvincing. In its current form, even if correct and significant, this paper isn't at the acceptance threshold for ICLR. I am willing to change my score if I'm convinced about at least one aspect (theoretical or practical) and that is highlighted in the paper. 

1. The theoretical justification needs to be more rigorous and clear (see questions). There are many places where new quantities are defined in an unclear manner which make the proofs hard to follow. There are a couple of assumptions that are likely incorrectly applied or unclearly defined. And terms like "approximate positive correlation" appear in a theorem which to the best of my understanding isn't a standard term. While I suspect the final conclusion that authors draw (Eqn 12) could be practically correct, I am not convinced that the theoretical justification for it is sound. 

2. While the authors do not need an external model or a separate training process, they do make a whitebox assumption, i.e. the underlying language model is a transformer and they have access to the layers and logits. This needs to be made the abstract/intro where they downplay other methods but do not mention this limitation of their method. 

3. Central to the practical implementation of their method are Eqn 19 and the authors measure performance on factiod QA tasks where the attention distributions are likely to be low entropy (peaky) because one passage likely has the answer and has a strong lexical overlap with the question. However, it isn't clear how much their practical implementation generalizes beyond factiod QA where the attention distribution could be complex and not clearly delineated. For instance, in lines 322-323 the authors claim that "LLMs use the selected knowledge at the maximum point for distribution fusion to predict $x_i$, the attention shifts from $R$ to prefix $x_{1:i-1}$" which seems like pure speculation about the mechanism as we don't have any justification for it and we also don't know that this speculated mechanism generalizes beyond QA tasks. 

4. Why do the the authors claim "distribution completion" = "benefit" and "distribution contradiction" = "Detriment"? It could be that the LLM was trained on data that was considered true at the time, but has changed since. In which case the distribution contradiction is beneficial and desirable. The claim about benefit vs detriment is orthogonal to the point of the paper and should be avoid.  

5. There is no way a reader can understand this paper without reading the appendix. At least the important assumptions need to be elevated to the main paper, even if the math isn't.

### Questions
1. The one question that completely blocked me from understanding the paper was the definition of $p_R$. It first appears in Eqns 36, 37 and is defined as "$p_R(·)$ is the distribution of the retrieved texts". Can the authors more rigorously define this quantity? What is the probability over? i.e. is $p_R(r_i)$ the probability of $r_i$ being retrieved? if $p$ stands for probability of an event, then is it simply $p(r_i)$? Could it just be a uniform distribution then? If not, is there a "retriever" conditioned on a "query" that determines this distribution? In which case, $p_R(r_i) = p(r_i | q)$. And neither of these definitions make sense for Eqn 42, where $p_R(x_i|x_{1:i−1})$ appears. What does it even mean? " distribution of the retrieved texts where the event is x_i conditioned on the previous tokens"? This blocked me from making sense of the proofs beyond Theorem 1. 

2. Assumption 1 implies that there exists **some** hidden state $h$ lower bounds it that $p(x|h, z^∗) > c_1 > 0$. Then how is the variable used $c_1$ used in the denominator of Eqn 29 where the sum is over all $h$? If the **some** $h = h^*$, then the denominator can be said to be $c_1 * p(h^*| R, z^*)$ (note the lack of a summation), but this quantity can be arbitrarily small as a function of $z^*$ and $R$. Thus bringing into question the $O(1)$ claim that is made in Eqn 33.

3. Assumption 2 is even more unclear in the definition. Until now there was no mention of the form of $R$ and this is the first time delimiters are introduced. What is the "delimiter hidden state" precisely? Are there any assumptions on input format of $R$. Ideally, in a theoretical justification, the format of the variables should make no difference. It is also very unclear how this assumption leads to $O(1)$ in line 765. 

4. It took me a while to understand how Eqn 33 could be potentially derived from Eqn 32. It would be prudent to be more rigorous here for future readers. 

5. Even if I assume theorem 1 is correct, in theorem 2, authors claim "approximate positive correlation", but I don't think this is a standard or well defined term. In lines 978 - 983, the authors go from upper and lower bounds to the claim on "approximate correlation" which doesn't seem theoretically sound. 

6. Just do double check, is Eqn 29 the same as Eqn 30?

Overall, the paper would be a lot easier to understand and review if there weren't so many leaps of logic in the proofs.

### Soundness
3

### Presentation
2

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
This paper provides a theory to explain and trade off the 'benefit' and 'detriment' in next token prediction of RAG. Specifically, the author uses the distribution of the LLM's knowledge and the distribution of retrieved texts to calculate the distribution difference, which can trade off the 'benefit' and 'detriment'. Then, the author employs a series of theoretical analyses and some experiments to explain how to compare the values of 'benefit' and 'detriment'. Finally, the author proves the effectiveness of the method and supports the theoretical findings with experiments.

### Strengths
1. This paper connects theory with practice, and the formula derivation is logically clear. Most of the papers are well written and explanatory, and are supported by experiments.
2. The standpoint of this paper is novel, using the perspective of latent variable models to explain RAG, and analyzing the distribution differences between LLM and external knowledge.

### Weaknesses
1. In Equation 2, it seems a bit forced to split it into two terms, even though we know that distribution fusion is not a simple addition of distributions. The representation of the fusion as a direct sum is a simplification that may not accurately reflect the complex interactions between the LLM's internal knowledge and the retrieved text. This could lead to an oversimplified model of the actual fusion process.
2. From Equation 4 to 5, the symbol is used incorrectly; An equal cannot be used. The transition from Equation 4 to 5 requires a more precise mathematical justification, as the current notation implies a direct equality where a proportionality might be more appropriate.
3. In Equation 7, the $P_r$  is not explained. Is it $p_R(r)$? The lack of clarity regarding the notation $P_r$ introduces ambiguity and makes it difficult to understand the precise meaning of the equation. This needs to be explicitly defined for the reader.
4. In Section 3.1, during the exploratory experiments on the distribution of retrieved texts $p_R(x_i|x_{1:i-1})$, it is mentioned that this distribution can be approximated using Equations 15 and 16. However, the calculation of the $Att$ score is not clearly explained. It still uses the QKV matrix from LLM? Appendix H only compares different LLMs and datasets, lacking a discussion on the calculation of the $Att$ score. Similarly, the hidden layer state $h$ in Equation 13 also originates from the pre-trained LLM itself. The reliance on the LLM's internal parameters for calculating the attention scores raises concerns about the independence of the retrieved text distribution from the LLM's knowledge. The method for calculating the $Att$ score needs to be more transparent and justified.
5. The paper does not evaluate Tok-RAG on LLMs with 33B and 65B scales. Since Tok-RAG generates texts in parallel, it means that two models need to be run at the same time, which may lead to a sharp increase in the demand for computing resources, especially when using larger-scale LLM. The lack of evaluation on larger models limits the generalizability of the findings and raises questions about the practical applicability of the method in resource-constrained environments.

Others:
1. In Equation 2, it is better to write the right side of the equation as $ = p(..) + \int .. dz$ to avoid misunderstandings. The current notation could be misinterpreted, and using an integral sign would clarify that the second term involves integration over a latent variable.
2. There is a mismatch in the notation of log, $ z*$ in Equation 7 compared to Equations 6 and 8. They should be standardized and modified to use $log$ and $z^*$. Consistency in notation is crucial for clarity and should be maintained throughout the paper.
3. About table format, the titles of the tables should be placed above the tables. Additionally, the sequence of the tables in the paper goes directly from Table 1 to Table 3. The order of the tables should be revised accordingly. The current table formatting and sequencing detract from the overall presentation of the results.

### Questions
1. For the calculation of the $Att$ score, it appears that the LLM is used for inference, and then the $Att$ score is computed for each layer. Essentially, it is still based on the $Wq$ and $W_k$ trained by the LLM itself? This suggests that the distribution of retrieved texts $p_R(x_i|x_{1:i-1})$ has a certain correlation with the knowledge distribution of the LLM $p(x_i|x_{1:i-1})$, and the same applies to word similarity. Is it possible to provide a more rigorous proof of the relationship between  $p_R(x_i|x_{1:i-1})$ and the LLM? For instance, analyzing the relationship between the knowledge distribution $p(x_i,x_{1:i-1})$ of LLM A itself and the retrieval texts distribution $p_R(x_i|x_{1:i-1})$ of LLM B when LLM B performing RAG.
2. In Equation 16, $p_R(x_i|x_{1:i-1})$ is approximated using element-wise multiplication of $Att$ and $WordSim$. Are there other methods that could be used to combine $Att$ and $WordSim$ that could improve the estimation of $p_R(x_i|x_{1:i-1})$. For example, using element-wise addition. You could provide experimental or theoretical explanations.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores an interesting and important problem of detecting the benefit and detriment of RAG from a theoretical perspective and propose a method called token-RAG. The authors first develop a theory to understand the benefit (retrieval can find valuable external information) and detriment (retrieved documents can be misleading or noisy) at token level. They find that the benefit and detriment can be compared by measuring the relative value of D and M, which is easily calculated in practice. However, calculating p_R for D and M is hard. The authors then introduce a heuristic method to use the attention score and word embedding similarity inside some specific LLM layers to estimate p_R. They finally conduct experiments on several datasets to demonstrate the effectiveness of the proposed token-RAG.

### Strengths
- The paper provides a theory to understand the benefit and detriment of the retrieved documents in RAG.
- The paper introduces a method called token-RAG to leverage benefit and prevent detriment.
- The authors conduct experiments on several datasets.

### Weaknesses
 - The meaning of some notations is not well explained. What is z*?

- Some formulations may be incorrect. Is there any problem with Eq.(2)? Given that p(z|R,x1:{i-1}) is a continuous function, how can you get the term corresponding to p(z|R,x1:{i-1}) out from the integral?

- Why can you go from (4) to (5)? I believe it should not be “=”. Why p(R,x1:{i-1}|z*) is a constant?

- The estimation of p_R(x_i|x_1:{i-1}) seems to be based on heuristics. I am not persuaded that this method can generalize to different datasets and domains. The use of attention scores and word embedding similarities within specific LLM layers is an indirect proxy for the true probability distribution, and it's unclear how well this approximation holds across diverse text types and model architectures. The method lacks a rigorous justification for why these specific layers and similarity measures are chosen, and it does not address potential biases or limitations introduced by this heuristic approach.

- In (17) and (18), why use the average word embedding rather than use the real predicted probability of the words? The latter seems to be naturally describing p in M and D. Using average word embeddings may obscure important nuances in the predicted probability distributions, potentially leading to inaccurate estimations of benefit and detriment. This approach seems to oversimplify the complex relationships between word probabilities and the overall quality of the generated text.

- The exact token-RAG method is not very clear. From (19), does it mean that if benefit wins, token-RAG will generate the token predicted by RAG, otherwise by LLM directly without RAG?

### Questions
See the weakness section.

### Soundness
3

### Presentation
2

### Contribution
3
