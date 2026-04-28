# Perplexity Trap: PLM-Based Retrievers Overrate Low Perplexity Documents

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 6, 5

## Abstract
Previous studies have found that PLM-based retrieval models exhibit a preference for LLM-generated content, assigning higher relevance scores to these documents even when their semantic quality is comparable to human-written ones. This phenomenon, known as source bias, threatens the sustainable development of the information access ecosystem. However, the underlying causes of source bias remain unexplored. In this paper, we explain the process of information retrieval with a causal graph and discover that PLM-based retrievers learn perplexity features for relevance estimation, causing source bias by ranking the documents with low perplexity higher. Theoretical analysis further reveals that the phenomenon stems from the positive correlation between the gradients of the loss functions in language modeling task and retrieval task. Based on the analysis, a causal-inspired inference-time debiasing method is proposed, called $\textbf{C}$ausal $\textbf{D}$iagnosis and $\textbf{C}$orrection (CDC). CDC first diagnoses the bias effect of the perplexity and then separates the bias effect from the overall estimated relevance score. Experimental results across three domains demonstrate the superior debiasing effectiveness of CDC, emphasizing the validity of our proposed explanatory framework. Source codes are available at https://anonymous.4open.science/r/Perplexity-Trap-D6FE.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the causes for source bias in PLM-retrievers. It explores the underlying architectural relations between perplexity and relevance scores and proposes an inference-time mitigation method that decouples the perplexity bias from the retrieval task.

### Strengths
- A clear technical description of the source bias issue, experimentation for cause and architectural relation, clear presentation of results and limitations.
- The linear model fit for perplexity given document and semantic variables strengthens the argument presented by the causal graph.
- Human annotation for verifying synthetic correctness.
- I appreciate the acknowledgment and inclusion of semantic nuance of documents as another variable in your experiments.
- The offering of a mitigation method with CDC strengthens the argument presented in your study and is an appreciated contribution.

### Weaknesses
 - The focus on small and older models like BERT and RoBerta is slightly exclusive of more recent LLMs and SLMs.
- Similarly, there is some lack of cross-model experiments for models used to generate data and for the retrieval task, popular closed- and open-source models could demonstrate very different results (A more inclusive experimental setup would be more convincing that your argument generalizes and isn’t overfit to your experiments).
- There might be a limitation with closed models where training data is unknown for the CDC methodology.

### Questions
- How relevant do you think your study will remain given the rise of synthetically trained models, given the effects of low ppl and high relevance on LLM-generated data by majorly human-data trained retrieval models in your experiments?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this article, the authors propose a thorough study of the "Perplexity Trap," a phenomenon previously observed: when using embeddings from pretrained language models for retrieval tasks, documents written by LLMs tend to be ranked higher. The main hypothesis is that this occurs because generated texts tend to have lower perplexity due to the generative process, which in turn affects document/query similarity. The authors aim to confirm this hypothesis through three experimental studies (one providing a contribution to mitigate this bias) and one theoretical study. All results seem to confirm the perplexity hypothesis.

### Strengths
Very important topic to study, including a consensual hypothesis for the “perplexity trap” that was still underexplored

Both experimental (correlation 3.1 and causality 4.1) and theoretical findings are (quite) convincing explanation of the link between perplexity and IR document relevance

The proposed method for bias mitigation is relevant, new and effectively reduce bias on several dataset and LLMs.

### Weaknesses
My main concern is the theoretical development in section 4.2. It lacks formalism, some notations are badly introduced or not at all. This leads to some aspect (either details or important things) either difficult to understand and follow, or that seem false. I’ll developpe everything in the questions section below.

The rewriting approach appears to be sound but lacks experimental support to show that the semantic content was not changed. See a more detailed comment below.

Specifically, the assumption that “document semantics remain unchanged during rewriting,” is not sufficiently verified. Using high temperature during sampling could lead to texts with different semantic content, potentially introducing noise or altering the core meaning. The article lacks a thorough experimental verification using LLM-based evaluation, human evaluation, LSA/LDA-based approaches, or non-LLM embedding similarity measures. The question asked to the human evaluator in E.2.1 only evaluates relevance, and not semantic equivalence, and evaluates only 20 triplets. Additionally, increasing temperature might lead to hallucination, mechanically decreasing the relevance of the document. These aspects should be evaluated more rigorously.

Notations should be formally introduced to ease the readability, such as \textbf{d} or dimensions of matrices (e.g. W). As notations are not that consensual, this is important to ease the reader work. Such grey zones led to several questions/interrogation that I list here.

Line 312, d_{emb} is an L \times N matrix, and is assumed to have a l2 norm of 1. What does it mean here for a matrix? Are you constraining the spectral norm, which is the formal equivalent of L2 norm for matrices? Could you please clarify.

Following the explanations, W is the matrix that maps a vector in \mathbb{R}^n to the vocabulary space, so of dim N by D.
1) It cannot be orthogonal but only semi orthogonal as it is not a squared matrix
2) I don’t understand how the conditions can be verified for most PLM as imposing orthogonality is really hard. Could you clarify? I might have missed something in the formalization of the problem, but it seems to be nowhere explained and motivated.

Last assumption (fine tuning conserve the inversion property) is not discussed and motivated. With large learning rate, I don’t see how this can be verified.

Line 810 is losing the reader. You are summing over N, if d^{emb}W is of dimension L \times D, so k is a vector of dimension L ? More importantly, I don’t get the justification for it having only positive values. If dW contains non-positive values, linear normalization does not provide guarantee that k is positive and that norm of d is 1 (again, which norm?). Although it relies on undisclosed assumptions that should be made clearer.

QM-AM states that the quadratic mean is greater than the arithmetic mean. K is n times the arithmetic mean, so you can’t say that this is lower than the quadratic mean (it is lower than  n times the QM though).

Overall, I find it misleading to use k, as it is a constant that does not depend from d_emb, that may lead to thinking that k is fixed for all d_emb.

Eventually, the sign of k will modify the dependency type and could contradict the assumption of the work.

Again, all these might come from a misunderstanding of the nature of matrix W, but anyway, this should be clarified in the documents.

ANCE is used before being introduced line 264 (e.g. line 145 )
Shouldn’t MLM task loss divided by L only rather than L \times D ?

### Questions
## On the rewriting method
“Specifically, we manipulate the sampling temperatures during generation to obtain LLM-generated documents with different PPLs but similar semantic content.” and “Since document semantics remain unchanged during rewriting,”. 
-> This is a strong assumption, that is, in my opinion, not verified. Using high temperature could lead to texts with different semantic content. The article lacks an experimental verification using LLM based eval, human eval, LSA/LDA based approaches or Non LLM embedding similarity. The question asked to the human evaluator in E.2.1 only evaluate relevance (author should provide the complete question asked to the annotator) and not semantic equivalence, and evaluates only 20 triplets. Additionally, increasing temperature might lead to hallucination, mechanically decreasing the relevance of the document. These should be evaluated properly. Could you elaborate on this?

## On the theoretical section 4.2 and appendix

Notations should be formally introduced to ease the readability, such as \textbf{d} or dimensions of matrices (e.g. W). As notations are not that consensual, this is important to ease the reader work. Such grey zones led to several questions/interrogation that I list here. 

Line 312, d_{emb} is an L \times N matrix, and is assumed to have a l2 norm of 1. What does it mean here for a matrix? Are you constraining the spectral norm, which is the formal equivalent of L2 norm for matrices? Could you please clarify. 

Following the explanations, W is the matrix that maps a vector in \mathbb{R}^n to the vocabulary space, so of dim N by D. 
1) It cannot be orthogonal but only semi orthogonal as it is not a squared matrix 
2) I don’t understand how the conditions can be verified for most PLM as imposing orthogonality is really hard. Could you clarify? I might have missed something in the formalization of the problem, but it seems to be nowhere explained and motivated. 

Last assumption (fine tuning conserve the inversion property) is not discussed and motivated. With large learning rate, I don’t see how this can be verified. 

Line 810 is losing the reader. You are summing over N, if d^{emb}W is of dimension L \times D, so k is a vector of dimension L ? More importantly, I don’t get the justification for it having only positive values. If dW contains non-positive values, linear normalization does not provide guarantee that k is positive and that norm of d is 1 (again, which norm?). Although it relies on undisclosed assumptions that should be made clearer.

QM-AM states that the quadratic mean is greater than the arithmetic mean. K is n times the arithmetic mean, so you can’t say that this is lower than the quadratic mean (it is lower than  n times the QM though). 

Overall, I find it misleading to use k, as it is a constant that does not depend from d_emb, that may lead to thinking that k is fixed for all d_emb.

Eventually, the sign of k will modify the dependency type and could contradict the assumption of the work.  

Again, all these might come from a misunderstanding of the nature of matrix W, but anyway, this should be clarified in the documents. 

## Minor

ANCE is used before being introduced line 264 (e.g. line 145 )
Shouldn’t MLM task loss divided by L only rather than L \times D ?

### Soundness
3

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
The paper studies why PLM-based retrievers are biased towards LLM-generated content and hypothesize that it is due to a causal effect between document perplexity and relevance score estimation. Based on the analysis, the paper further proposes a correction method, CDC, to separate the bias effect. Experiments include controlled experiments to demonstrate the causal effect, and experiments on 3 IR datasets, using existing MLM-based PLM retrievers, where the effect of using CDC is demonstrated.

### Strengths
1. Performing a deeper understanding on the PLM retriever is biased towards AIGC is an interesting topic and can be interesting to some from the IR community. The paper provides reasonable illustrations via causal analysis and proposes a debiasing method accordingly, which is a complete work in terms of the story.

2. The analysis of MLM vs IR loss function is interesting and provides more insights into the problem.

### Weaknesses
1. Limited to PLM-based retrievers. One may argue that a well behaved retriever, or existing retrievers do not possess this issue. Or there're more standard ways to address this such as by standard training. One may argue that this topic is not of general interest to the ICLR community as it is more SIGIR focused, as the setting is specific and not widely acknowledged.  

2. Analysis is limited to MLM, while MLM is becoming less and less relevant. Indeed, the retrievers used in the paper are relatively old (most recent 2022). The proposed method also shows more effect on older PLMs than more recent ones. This again raises the concern about how relevant the paper is to the broader ML community. How about models trained with CLM? 

3. The causal analysis and approach leveraged in the paper is conventional. This is not necessarily a "weakness" but it does not make the paper a stronger case.

### Questions
Would not "document semantic" be explained away?

Please list the statistics of each dataset used.

### Soundness
3

### Presentation
3

### Contribution
2
