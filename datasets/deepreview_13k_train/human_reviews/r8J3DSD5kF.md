# Stick-breaking Attention

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
The self-attention mechanism traditionally relies on the softmax operator, necessitating positional embeddings like RoPE, or position biases to account for token order.
But current methods using still face length generalisation challenges.
We propose an alternative attention mechanism based on the stick-breaking process:
For each token before the current, we determine a break point $\beta_{i,j}$, which represents the proportion of the remaining stick to allocate to the current token.
We repeat the process until the stick is fully allocated, resulting in a sequence of attention weights.
This process naturally incorporates recency bias, which has linguistic motivations for grammar parsing \citep{shen2017neural}.
We study the implications of replacing the conventional softmax-based attention mechanism with stick-breaking attention.
We then discuss implementation of numerically stable stick-breaking attention and adapt Flash Attention to accommodate this mechanism.
When used as a drop-in replacement for current softmax+RoPE attention systems, we find that stick-breaking attention performs competitively with current methods on length generalisation and downstream tasks.
Stick-breaking also performs well at length generalisation, allowing a model trained with $2^{11}$ context window to perform well at $2^{14}$ with perplexity improvements

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper does a thorough evaluation of stick-breaking attention (also known as geometric attention) for synthetic test tasks and natural language tasks, showing its effectiveness at capturing a preference for locality, as is natural and correct for natural language tasks. The paper examines a fast, numerically stable implementation of stick-breaking attention in Triton, which enables larger scale experiments.

### Strengths
- The paper provides thorough and useful experimental results on the performance of stick-breaking attention, providing good exploration of its effectiveness for artificial and natural language tasks, for length generalization, etc. The experimentation seem well thought through and well done.
- The paper is generally clear and easy to read.
- The paper is very honest about what it contributes and what it uses from prior work.
- The paper provides useful and new empirical results on different forms of attention on different tasks.
- The paper examines building an efficient, numerically stable Triton implementation of stick-breaking attention.
- It's good to include comparisons to Gemma2-2B and Qwen1.5-4B so that people can easily see that the results are decent, even though the papers own results are the apples-to-apples comparisons.

### Weaknesses
 - The paper lacks originality in machine learning ideas. Stick-breaking attention has been previously explored by Yikang Shen (in multiple papers) and especially by Csordas et al. (2021), the latter under the name "Geometric attention". "Stick-breaking attention" is a better name for the model used, but the model is exactly the same as in these prior works, limiting the originality of this paper. The value is mainly in the more extensive experimentation, including showing performance on larger scale, standard natural language benchmarks.
- This paper lacks somewhat in significance because of this. It does have some significance, since it is really good to see that these ideas really do give gains on standard NL tasks like ARC, Hellaswag or RACE, but the basic correctness of the idea had already been established.
- The differences between many models in Table 2 are fairly small and nothing is said about the detailed validation of the results. Are these from single runs rather than averages from 3-5 runs with different random initialization? How much variance would there be here, how confident can we be that a result of 63.4 is better than 63.1 for Winogrande on Softmax vs. SB w/o remainder correction, for example?
- How to produce an efficient, numerically stable Triton kernel basically follows the methods of FlashAttention and standard good practice (using log(1 + exp(x)), etc.)

### Questions
- The differences between many models in Table 2 are fairly small and nothing is said about the detailed validation of the results. Are these from single runs rather than averages from 3-5 runs with different random initialization? How much variance would there be here, how confident can we be that a result of 63.4 is better than 63.1 for Winogrande on Softmax vs. SB w/o remainder correction, for example?
- I took the text around lines 101-107 as suggesting that things should work better doing stick-breaking with remainder, but the actual results go the other way. It would be good to provide more understanding of why this harms rather than helping.
- For the paper, you should explain lines 300-301. This isn't a question. I figured it out, but the text of the paper should explain MQRAR better for people who haven't seen it.

### Soundness
4

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
The paper introduce an alternative attention that includes a form of positional embeddings, avoiding the need to add PE techniques such as RoPE. The method is based on the stick-breaking process, which means for each token in the context (keys), they assign a break point that represents the remaining stick to the current token. This means that if 2 tokens have equal logits, the one closer to the current token will receive more stick value, representing the positional order.
Conducting this process through out the entire context results in a sequence of attention weights in lieu of traditional attention weights.
The paper suggests this process incorporate recency bias in nature without PE.
Experiments done show that the new method is better at length generalization in perplexity compared to attention+RoPE.

### Strengths
- The paper presents a novel addition to the zoo of "attention alternatives" by leveraging the stick breaking process, which performs both "attention" and positional embeddings intrinsically. The mechanism has a recency bias, meaning a token can prefer to allocate all its "energy" to few recent tokens, but it can also skip over and only attend to far-away tokens.
- The paper also include details implementation in Triton for flash-attention style efficiency and speed-up optimization, which is hugely appreciated, especially when nowadays efficiency and scalability is valued more for massive training of LLMs.
- The paper conducted diverse range of experiments, from throughput (only 20% slower than flash attention), perplexity and language modeling tasks (MMLU, ARC-c, hellaswag...), which all shows promising results.
- The main driver of this work is to solve the length generalization challenge of LLMs, which show good results.

### Weaknesses
 - Method can be explained more clearly with diagrams, formulation should be defined more thoroughly.


### Questions
- What is $\sigma$ function? It is never defined. is it sigmoid ?

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
4

### Summary
This paper is about stick-breaking or geometric attention, an alternative to softmax that has a built-in bias towards more recent tokens. Given a query position j, each key/value position i < j computes a probability of "yes" or "no", and the attention weight on i is the probability that position j is "yes" but all intervening positions are "no".

Stick-breaking/geometric attention was introduced in previous work. It makes position embeddings unnecessary and can be computed in O(log n) parallel time. This paper presents an improved implementation, and shows that stick-breaking/geometric attention improves performance on the multi-query associative recall task and various benchmarks.

### Strengths
This softmax alternative is simple and induces a bias towards attending to recent positions in a very natural way.

The experimental results all look strong.

### Weaknesses
As far as I can tell, stick-breaking attention is exactly the same as geometric attention (Csordas et al 2021), and stick-breaking was previously introduced by Shen et al (2023). Both papers are cited in the introduction, and the introduction concludes with an accurate list of the novel contributions of the paper. However, 
- The paper's short title "Stick-Breaking Attention" may give the impression that this is the first paper about stick-breaking attention.
- The abstract does not mention previous work; on the contrary, it says "We propose an alternative attention mechanism."
- The introduction, probably inadvertently, could be mis-read as saying that geometric attention only has one parameter ("Geometric attention, named after the Geometric distribution, which only has one parameter").

Eq. (2): Putting the remainder of the attention onto position j itself does not seem like the right choice. Probability $(1-\beta_{i,j})$ is the probability of pushing the attention to the left of position i, so $\prod_i (1-\beta_{i,j})$ is the probability of pushing the attention all the way to the left. So it's not surprising that this turned out not to work well. Letting the attention weights sum to less than one (or equivalently, putting the remainder of the attention onto the zero vector) seems like the most sensible thing to do.

The Flash Attention-like implementation of stick-breaking attention is 20% slower than Flash Attention.

### Questions
What is the exact relationship of stick-breaking attention to geometric attention (Csordas et al 2021) and the stick-breaking attention of Shen et al (2023)?

Eq (1):
- I'd suggest not using \cdot, as it might be misinterpreted as an inner product in this context.
- The first summation only goes up to i-1, so a position cannot attend to itself, which is different from usual future masking. I didn't see this decision discussed; what's the reason for it?

Line 94: typo, should be $z_{i,j} = z_{i',j}$? 

Eq (4): I don't know if it matters, but you could use log1p(exp(z)) instead of log(1+exp(z)).

It may be interesting to node that while softmax with a temperature factor (α = softmax (z/T)) as T -> 0 approaches average hard attention, which is used in many theoretical studies of transformers (e.g., https://arxiv.org/abs/1901.03429, https://arxiv.org/abs/2106.16213), stick-breaking attention (β = σ(z/T)) as T -> 0 approaches strictly future-masked rightmost hard attention, which is the kind of attention studied by https://arxiv.org/abs/2310.13897.

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
4

### Summary
This paper presents a new type of attention mechanism called "stick-breaking attention". It is meant to have a bias for attending to recent positions. Instead of using dot-products between keys and queries as logits and renormalizing them using a softmax to form the attention weights, the dot-products are each passed through the logistic function and then used as the probabilities in a stick-breaking process. In other words, the model first decides how much to attend to the current token, *then* decides how much of the remainder to allocate to attending to the previous token, and so on. It is a generalization of geometric attention proposed in prior work, where the probabilities at each timestep can be different. The authors discuss details for implementing it efficiently. They test it against standard scaled dot-product attention on a simple synthetic task that advantages recency bias, and on a variety of natural language benchmarks. Stick-breaking attention gets better scores on most tasks.

### Strengths
1. The experiments include a variety of natural language benchmarks.
1. The authors include a thorough comparison to similar prior work.
1. The results as presented show that stick-breaking attention outperforms standard attention on a variety of benchmarks.
1. Their new attention mechanism is reasonably fast, and further optimizations are possible.

### Weaknesses
1. Their implementation relies on a very rough approximation of the exponential function to avoid overflow (Eq 5), so their method is implementing a function that is quite different from what is proposed. I think this can be avoided (see Questions), and I am curious to see if using an exact solution affects the results.
1. To improve the readability of the paper, a more intuitive explanation of stick-breaking would be useful, for those who are not familiar with the term. For starters, why is it called stick-breaking?
1. Although the results are encouraging in Section 5.3, it is not clear to me that there was much hyperparameter tuning on the baselines. I would like to see more discussion of this.
1. I would like to see more discussion of *why* recency bias helps on the natural language benchmarks tested (see Questions).
1. Since there are no positional encodings, is it the case that stick-breaking attention transformers can't distinguish the same token type at different positions at all?
1. Does your baseline softmax attention transformer not use any positional encodings? I think that baselines both with and without positional encodings should be compared against. How do you know the reason length generalization improves is not the removal of the positional encodings?


### Questions
1. The keys and queries do not have positional encodings, but the values still do, right? Does the lack of PEs on queries and keys reduce the model's expressivity (i.e., are there certain functions that it can no longer implement because of the loss of PEs)? 474: Stick breaking attention doesn't completely get rid of PEs, right?
1. Although I intuitively understand the motivation for using stick-breaking, can you make a more rigorous case as to *why* stick-breaking has a recency bias? Is it not true that both softmax and stick-breaking attention can implement arbitrary attention patterns?
1. Related to the above, did you verify that the model actually attends to more recent tokens? Does this happen in wikitext?
1. 096: I'm not sure what this discussion is trying to say. Can you explain this more?
1. 094: I think $z_{i,j} = z_{i,j}$ is a typo.
1. Instead of using Eq 5, which is an inexact approximation, why not use the identity $\log(1 + \exp x) = c + \log(\exp(-c) + \exp(x - c))$, where $c = \max(0, x)$? This would solve the overflow problem while being an exact solution.
1. 208: Doesn't this make your method much less parallelizable than standard attention? I think you can actually get the same parallel time complexity using a variant of parallel prefix sum -- have you considered using that?
1. 304: How much of each sequence is devoted to the initial set of pairs, and repeated pairs?
1. Table 2, Figure 6: Why do you suppose stick-breaking attention helps on these tasks? It even gets slightly lower perplexity on wikitext, which is not a task that is specifically advantageous for recency-biased models. Can you spend more time discussing what kind of capability each natural language benchmark represents? Why do we expect recency bias to help with them? Do the gains come from recency bias, or is it more about length generalization thanks to the use of relative PEs?
1. Why does stick-breaking attention do better at length generalization on RULER if the retrieved data is not necessarily recent? I don't see why stick-breaking would be advantageous here.
1. Why does stick-breaking attention eventually fail on RULER at longer lengths? What is the failure mode?

### Soundness
3

### Presentation
3

### Contribution
3
