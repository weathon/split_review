# Eliminating Position Bias of Language Models: A Mechanistic Approach

- Decision: Accept
- Scores: 5, 8, 6, 8, 6

## Abstract
Position bias has proven to be a prevalent issue of modern language models (LMs), where the models prioritize content based on its position within the given context. This bias often leads to unexpected model failures and hurts performance, robustness, and reliability across various applications. Our mechanistic analysis attributes the position bias to two components employed in nearly all state-of-the-art LMs: causal attention and position embedding. 
Based on the analyses, we propose to \textbf{eliminate} position bias (e.g., different retrieved documents' orders in QA affect performance) with a \textbf{training-free zero-shot} approach. Our method changes the causal attention to bidirectional attention between documents and utilizes model attention values to decide the relative orders of documents instead of using the order provided in input prompts, therefore enabling \textbf{P}osition-\textbf{IN}variant inferenc\textbf{E} (\textbf{\model}) at the document level.
By eliminating position bias, models achieve better performance and reliability in downstream tasks, including LM-as-a-judge, retrieval-augmented QA, molecule generation, and math reasoning. Notably, \model~is especially useful when adapting LMs for evaluating reasoning pairs: it consistently provides $8$ to $10$ percentage points performance gains, making \texttt{Llama-3-70B-Instruct} perform even better than \texttt{GPT-4-0125-preview} and \texttt{GPT-4o-2024-08-06} on the RewardBench reasoning set.
$^1$ University of Illinois Urbana-Champaign, $^2$ Harvard University, $^3$ Texas A\&M University. Contact: \texttt{ziqiw9@illinois.edu}}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors introduce a method to de-bias a positional dependence for concatenated documents in the context of a LM and prove its supremacy against other de-biasing baselines.

They also compare against vanilla inference, but I cannot tell whether the numbers are actually beneficial.

### Strengths
- very relevant problem
- the recency and primacy biases are interesting.

### Weaknesses
 - Figure 2 is confusing, since the documents change color when you move them (in the right plot). So it looks like the $D_3$ in the first row is the tokens [2,3], but in the second assignment iteration suddenly $D_3$ is [4,5]? It seems inconsistent with the last row, where importance ordering is $D_2 > D_3 > D_1$, but they are not ordered in that way.
- I don’t think you can claim that you pinpointed the causes of positional bias in transformers. Everybody knows what those are.
- Please Correct me if I am wrong here.
The proof in App B shows that the softmax term is invariant under inter-document permutation before the ordering takes place, but Lemma 1 takes the QKV invariance as a given.
How I think Lemma 1 and the proof should go:
Lemma 1: “The PINE algorithm makes $H_{Pine}$  document-position invariant”
Proof: “The algorithm sorts the documents by a document-position invariant metric and concatenates them. Therefore, the resulting concatenation  is invariant. $H_{Pine}$ is only a function of that concatenation, therefore $H_{Pine}$ is invariant. Proof ends”.
- I can’t tell if the numbers are good. The method outperforms other methods of debiasing, but it does not seem to do super well against Vanilla (shuffle) in Figure 4 for instance. Given that you shuffle reward bench, is Vanilla in Table 2 also implicitly Vanilla (shuffle)? It is overall confusing to me, but I admit that this is an opinion.

### Questions
- Please discuss the relationship to NoPE (https://arxiv.org/pdf/2305.19466) in your related work
- I find the importance measure that you introduce a little bit weird if you make it independent of positional bias, since you will later calculate attention with positional bias in there, which might change the importance quite a bit. Have you found your measure of document importance, without positional bias, to be monotonic with an importance measure that calculates the attention with positional bias, but putting each document candidate at the same position, right before the currently decoded document for instance?
- I am overall confused by the introduction of bidirectional attention. Given that you calculate importances independently of relative document-position, and you reorder anyway, why do you have to have an attention in the forward direction, instead of simply always putting the document you are decoding at the last position? I might have understood this wrong, the first half of Page 5 is a little confusing to me. When following the concrete example in the proof, there is no bidirectional attention, right?
- Can you comment on the downsides of making keys query dependent (L235)? This seems like you will loose parallelism, at the very least the option to KV-cache.
- Can you comment on your intuition as to why SP and PCW are worse than your approach?
- You say you introduce two other debiasing baselines, permutation and calibration. Is permutation the same as Vanilla (shuffle) in Figure 4? Why are the numbers for it not in any tables?
- Table 2: I don’t fully understand the baselines. IIUC, the GT is either at A or at B, which is why you say 50% random guess baseline, i.e. there is no position C. Why is Vanilla (without qualifier) worse than both Vanilla (GT at A) and (GT at B)? it is not always one of the two, which would lead to some kind of average?
- what do you mean by reasoning “pairs” in 418ff?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Positional bias is a major problem for language models. Several proposals have been made in literature towards mitigating this issue. This paper proposes one method by making the inter-document attention bidirectional. Specifically, they propose their own order such that the effects of order dependence in positional encoding is minimized.

### Strengths
- I like this paper. they propose a bidirectional attention in the input documents to achieve input order independent attention. 
- Their results are solid. For order dependent benchmarks, they do achieve significant gains.
- While the paper is solid, I would like the authors to revise their claims of position invariance to input-position invariance.

### Weaknesses
 - I like this paper. they propose a bidirectional attention in the input documents to achieve input order independent attention. 
- Their results are solid. For order dependent benchmarks, they do achieve significant gains.
- While the paper is solid, I would like the authors to revise their claims of position invariance to input-position invariance.

 - I tried understanding Figure 2 many times, it was not clear to me. Please see question below. The only sensible explanation is that the attention is simulating the document under question being placed at the end of the sequence, with nearness being provided by importance scores.
- What about the n^2 importance score computations per set of n documents. How to do this when there are multiple documents?
- The position invariance is quite misleading. The correct term I believe would be importance dependent position weighting. i.e. You know the documents far away to the current document under consideration have higher likelihood of error, and hence you place them far away, such that the impact of position is mitigated. 
- Here is a counterexample for position invariance: Let us take a query which involves multi-hop retrieval. The query asks: Retrieve the home pages of all the professors working in the CS department of X university, and list out their topics of interest. Here the retrievals may be all nearly equally important. A full position invariance would require an independence with order whereas that cannot be achieved through this method. What you instead do is to rank documents by importance order and then mitigate positional dependence by placing them in that order of closeness for attention. This is not "invariance". My major concern is with the nomenclature, which claims invariance, and eliminating position bias.
- Lemma 1 may need a revision: sorting by computed importance scores introduces an implicit positional bias. While the function \( f(\text{input order}, \text{content}) \rightarrow \text{output permutation order} \) maintains input order invariance if \( f(\text{io1}, \text{content}) = f(\text{io2}, \text{content}) \) for all input orders \(\text{io1}, \text{io2}\), it imposes a new order-dependent bias in the output, meaning true position invariance is not achieved. Thus, while input-position invariance is maintained, true positional invariance is not achieved, as the sorting process introduces a new, order-dependent bias in the output.

### Questions
- Figure 2, I understood the last row. 8 is at its original place and (4,5)> (6,7) > (2,3). 
    - Rows 6 and 7 -- (6,7) is at its original place and (2,3) > (4,5)
    - Rows 4 and 5 -- (4,5) should be at their original place, but (6,7) is! Why revise the position of this document to the end when both the documents can be (equally) at small distance from the document under consideration?
- I only understood Figure 2 after going through paragraph 2 in lemma 1. Please consider revising the write up with the document order for computation of each of the rows of the attention.

### Suggestions:
- Move paragraph 2 from Lemma 1 proof from appendix to main paper to explain your method.
- Consider revising the words position invariant to input-position invariant. Please also consider revising the claim that the position bias of LLMs is eliminated (in the title of the paper). From my best understanding, it is mitigated through a reordering and not eliminated.

### Soundness
2

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
The paper presents a modification to the causal attention mechanism of decoder-based transformers. The proposed mechanism adds bidirectional attention to each document, in order to make representations position-invariant. New bidirectional attention terms are added in blocks (for the tokens corresponding to each document), which are ordered according to their importance to the document on the diagonal. The proposed importance score is based on a version of the standard attention calculation that ignores positional differences. The paper proves positional invariance and evaluates the empirical performance of the new method on a set of tasks.

### Strengths
1. The paper is well-written and the graphics are appealing.
2. Position-invariant representations are nice, and you obtain them without k! overhead.
3. The positional bias on RewardBench appears significant and adds credibility to your argument that position bias is an important problem.
4. Strong results for the Qwen models on RewardBench.
5. Strong results for Llama on the reasoning subset of RewardBench.

### Weaknesses
 1. You compare your method to other mechanistic methods with different goals: for example, PCW helps extend the context window; NIA gives a speed boost by making the attention computation sub-quadratic. Thus, these are both *approximate* methods. Your method, by contrast, introduces extra overhead compared to standard sampling. For a fair comparison, it is important to look for methods that are more resource-intensive than standard sampling (for example, if your method has 8x overhead, a simple baseline could involve sampling 8 permutations of the documents and running vanilla sampling 8 times, followed by some aggregation scheme like majority voting).

2. I appreciate the analysis shown in Figure 4b) but I would also like to see an analysis of the choice of importance score (see question 1. below).

3. On both RAG-QA and RewardBench, PINE does not seem to improve over vanilla sampling with the Llama models. To see this, note that the average of the GT-A and GT-B scores should give the expected performance for vanilla sampling (with randomized ordering of the two documents -- please correct me if I am wrong). On molecular generation and math reasoning, you switch between evaluating the Llama and Qwen models, which does not inspire confidence; I would like to see the same list of models evaluated for each task. Overall, your selection of tasks seems somewhat contrived. See question 2. below.

### Questions
1. Your method gives position invariance as long as the attention orderings for each document depend only on the content of the documents rather than their positions. Thus, mathematically you can consider any function that maps a list of k documents to a permutation on k-1 documents (k-1 since the document on the diagonal is always in the last position). This class of functions is large and includes special cases like variants of your importance score (e.g., variants regarding the choice of normalization). It seems important to assess the sensitivity of PINE with respect to the choice of ordering function.

2. If position bias is as big a problem for our field as the paper argues, it should be possible to show gains on mainstream benchmarks. Consider the generic position-dependent biases in few-shot prompting, as identified by Zhao et al. in their contextual calibration paper. Could you improve, say, the recency bias of few-shot prompting with your approach? If yes, it would be nice to see this demonstrated on a mainstream LLM benchmark.

3. I am not very familiar with the Qwen series of models. Since your method yields essentially no gains for Llama on RewardBench (as noted above – please correct me if my analysis is mistaken), I wonder if the strong performance on the Qwen models has something to do with the architecture of these models. After looking into the matter, I wonder if the Qwen models’ use of sliding window attention could be the reason why the extra bi-directional attention from your method yields a benefit. What do you think? 

4. The ability to permute documents gives you a way to estimate the variance of vanilla sampling performance. Given the wide disparity between the GT-A and GT-B performances on RewardBench, did you look into randomizing the order of premises on R-GSM? This seems especially important because there are so few samples (only 95) in this data set.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Proposed work introduces PINE, an attention mechanism that computes the attention scores in a positionally invariant manner. The method does not require any training and can be plugged into an transformer inference setup with minimal costs. Improved results in multiple benchmarks show the effectiveness of the approach.

### Strengths
- The approach does not require any extra training, and can be used by any attention mechanism.
- Remarkable improvements on rewardbench evals.
- Comparison with relevant baselines and experiments with multiple models performed.
- Positional invariancy is thoroughly ascertained through empirical and theoretical explanations.

### Weaknesses
 - Regarding,
> Hsieh et al. (2024) assumes that the position bias and real relevance are linear combinations and propose solutions accordingly. Different from them, we aim to eliminate the position bias from the mechanical perspective without any assumption at a reasonable cost.

Although it is claimed that this solution is better motivated than the cited one, a comparison is still required since both papers are solving the same problem and show very good improvements in similar yet different tasks.


- [This](https://openreview.net/pdf?id=gEMLMMG0m9) work debiases positional bias in the attention matrix by averaging attention values of documents at different positions. A mention of why such simple methods to debias are less relevant or a comparison is required.


- Regarding line 288,
> the extra big O computation complexity to obtain hidden states is O(nk log k),

From my understanding, for an end-to-end inference time overhead calculation, this should be multiplied by #layers in the model. And further with #heads if computation across heads is not parallelized. The equation does not capture this.
Hence for lines 518-519,
> we find the wall time of PINE is ~2x and ~8x of the vanilla inference

These numbers should depend on the size of the models being considered. Can you tabulate this for each model separately to give a better picture of overhead time? This is significant as benchmarks tend to use large models as evaluators and an inference time $\propto $ #layers limits the practical applicability of the work.

### Questions
<none>

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work addresses the position bias problem in language models (LMs), where models prioritize information based on its order in the input, affecting performance and reliability across applications. Through a mechanistic analysis, the study identifies causal attention and relative positional encodings as primary contributors to this bias. To mitigate it, the authors introduce Position-INvariant InferencE (PINE), a zero-shot approach that replaces causal attention with bidirectional attention between documents and uses attention values to determine document order. PINE effectively enhances model performance in tasks like QA, molecule generation, and math reasoning, showing notable gains in reasoning benchmarks where it surpasses even state-of-the-art models like GPT-4 in specific evaluations.

### Strengths
1. This paper proposes a simple yet effective and novel method to mitigate the postion bias problem in LLMs.

2. Extensive experiemnts on Llama-3 and Qwen demostrate the effectiveness of the proposed method.

### Weaknesses
1. The ablation study of the strategy of re-assign positions is required to better discuss the potential of further improving the method.

2. There is no baseline comparison with other calibration based methods.

### Questions
1. Do different position assigning strategies have a big effect on the downstream performance?

### Soundness
3

### Presentation
3

### Contribution
3
