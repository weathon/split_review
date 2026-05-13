# Fundamental Limitations on Subquadratic Alternatives to Transformers

- Decision: Accept
- Scores: 6, 3, 8, 6

## Abstract
The Transformer architecture is widely deployed in many popular and impactful Large Language Models. At its core is the attention mechanism for calculating correlations between pairs of tokens. Performing an attention computation takes quadratic time in the input size, and had become the time bottleneck for transformer operations. In order to circumvent this, researchers have used a variety of approaches, including designing heuristic algorithms for performing attention computations faster, and proposing alternatives to the attention mechanism which can be computed more quickly. For instance, state space models  such as Mamba were designed to replace attention with an almost linear time alternative.

    In this paper, we prove that any such approach cannot perform important tasks that Transformer is able to perform (assuming a popular conjecture from fine-grained complexity theory). We focus on document similarity tasks, where one is given as input many documents and would like to find a pair which is (approximately) the most similar. We prove that Transformer is able to perform this task, and we prove that this task cannot be performed in truly subquadratic time by any algorithm. Thus, any model which can be evaluated in subquadratic time -- whether because of subquadratic-time heuristics for attention, faster attention replacements like Mamba, or any other reason -- cannot perform this task. In other words, in order to perform tasks that (implicitly or explicitly) involve document similarity, one may as well use Transformer and cannot avoid its quadratic running time.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This paper introduces a theoretical perspective on the ability of transformers to solve document similarity tasks. Specifically, by relying on the SETH conjecture, the paper connects complexity theory with transformers, and shows that subquadractic models cannot solve a class of problems that are solvable by transformers, which are quadractic.

### Strengths
Although this is not my area of expertise, I believe the paper's main findings, particularly regarding document similarity tasks, have the potential to impact the literature on architectural development. Additionally, to the best of my knowledge, the paper is well-written, the math is accurate and concise.

### Weaknesses
While the theoretical coverage seems accurate to me, I was disappointed by the lack of empirical evidence supporting the paper's main findings. For instance, experiments demonstrating that subquadratic models cannot solve Max-IP, Min-IP, MSD, and LSD, whereas transformers can, would have been valuable. Specifically, the paper's claims about the limitations of subquadratic models in solving document similarity tasks, while theoretically grounded, lack concrete validation. The absence of experiments showcasing the failure of specific subquadratic architectures on these tasks, and the success of transformer models, makes it difficult to assess the practical relevance of the theoretical results. Furthermore, the paper does not discuss the potential impact of factors such as data distribution, noise, and the specific choice of hyperparameters on the performance of these models, which could significantly affect the empirical outcomes.

### Questions
For MSD and LSD, how relevant are your findings in practical applications, such as recommendation systems? Could varying values of sequence length $n$ and model parameters lead to different practical conclusions?

### Soundness
2

### Presentation
2

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
The paper studies a fundamental issue whether any subquadratic approximations to the transformers' quadratic attention mechanisms can solve perfectly the minimum inner product problem (or its variants (such as the maximum inner product one)) among a set of binary vectors. Built on results about the inherent complexity of such problems, the authors show that such problems can not be solved by any subquadratic approximations due to the complexity mismatch. They also show the problems can be solved by a transformer using the quadratic attention mechanisms by constructing such a network.

### Strengths
The results are theoretical, demonstrating a fundamental limitation of any subquadratic approximations of the transformers' quadratic attention mechanisms. The involved steps seem sound.

### Weaknesses
I believe the results, while rigorous and sound, have almost no connection with the transformers being used in practice. Generally speaking, the transformers are shown to be very capable of solving different kinds of problems empirically. For example, subquadratic approximations try to show that they can perform similarly to the original transformers but more efficiently, which is orthogonal to the results in the paper. Due to the nature of the results, there are no experimental results. But the variants of the transformers being used are mainly justified via results. Furthermore, it is known that at least some of the transformers (such as the decoder-only ones) can not solve counting and copying problems [1] perfectly and the additional impact of the results in the paper to the research on transformers may be very limited.

### Questions
1. Can the results be enhanced to rank different subquadratic approximations?
2. Similarly, can the results be enhanced to quantify the gap between the quadratic transformers and the subquadratic approximations?
3. Are there approximate algorithms for solving the minimum inner product problem or its variants and how would these relate to the subquadratic approximations?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
Attention is a computationally bottleneck of the prominent transformer models used for language modelling. The classic variant is in quadratic (on the input-dimension) complexity class, which is why sub-quadratic variants such as state-space models emerged, to enable e.g. longer document processing.
The authors claim that subquadratic alternatives to transformers face inherent limitations in performing specific NLP tasks, namely document similarity. Its contributions are theoretically based on complexity theory; namely, 1) the prominent SETH problam cannot be solved sub-quadratic, and 2) a constructed transformer can solve SETH.

### Strengths
Finally some more mathematically theoretically founded analysis of the prominent architecture and its limitations.
It analysis seems rigorous and its offering insights that can influence future research on alternative architectures in NLP.

### Weaknesses
minors/ missing discussions:

1.1) The paper would benefit from discussing the practical impacts of its findings. I.p. the bounds of its proof seem to be quite practically relevant and not 'entirely asymptotic' - in praxis it could be more relevant to have 'bad asymptotic with good bounds'. Specifically, the paper should explore the implications of the derived quadratic lower bounds for realistic sequence lengths and embedding dimensions used in practice. It is not sufficient to state that the bounds are asymptotic; a discussion of the concrete values where the quadratic behavior becomes dominant is needed.

1.2) It would be beneficial to explore the performance of alternative architectures i.p. w.r.t. practicability - i am not sure if a state space machine can't handle OVC in a reasonable depth like 10 layers. The paper should investigate the practical limitations of sub-quadratic models, such as state-space models, in handling tasks like document similarity with varying depths. A more detailed analysis of the trade-offs between depth and performance for these models is required, including empirical evidence or theoretical arguments supporting the claim that a prohibitively large depth is required.

1.3) it would be beneficial to discuss a broader range of tasks. While the paper focuses on document similarity, it should also discuss the implications of the findings for other NLP tasks that rely on attention mechanisms, such as machine translation or question answering. The analysis should extend beyond document similarity to demonstrate the broader relevance of the theoretical results.

mediocores:

2.1) i find the main paper pretty hard to read and would advice a bit of restructering i.p.
- abstract line 22ff are quite redundant
- intro line 132ff seem pretty random/ not needed/ more distractive
- repetitively bichromatic versions are mentioned but not required in the core eg 2.2.1, 2.2.2, 2.3 -> i would love to see that in a final/following discussion sections once. Similarly Min/Max-IP are pretty confusing as not required for the main result -> discussion afterwards
- you define in 2.3 MSD, but actually require LSD for the core proof. that is one part that actually should be written explicitly twice (or the other version) :)

2.2) the core result is 4. it, and its impact should be discussed further, in particular recall what sub-quadratic methods suffer from. The proof could use a rewrite. i.p.: 4.1. is a transformer from your definition (not just attention~...). i suffer a bit to understand the step 529: A_{Q,K,V}(X) IS NOT line 528, but it is upperbounded by it which is all you need (?) you miss the factors XV = in this construction #ones in v_i.. or did i miss something?

### Questions
- 259: finds
- 310: multi-layer
- 434 write the numbers explicitly, 'very large' is random here
- 534 left side v_i^*  (the star)
- line 529 as mentioned above

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Paper is well written and brings interesting results from complexity theory to the deep learning community. It describes theoretical  limitations of sub-quadratic attention architectures for similarity and related problems. Paper shows that MSD, LSD and their variants require quadratic time assuming SETH and therefore any subquadratic alternatives to transformers are not able to solve them due to computational constraints. Also the paper explicitly constructs one head / one layer transformer which is able to solve such a problem, therefore making clear an important difference between standard attention and subquadratic alternatives.

### Strengths
1. General results on limitations on sub-quadratic  architecture or heuristic for most similar, least similar and related problems. Proved that accuracy loss for any task relating to document similarity is unavoidable for any sub-quadratic approach.
2. Shown that one head / one layer transformer can solve those tasks.  This includes explicit transformer construction.
3. Bringing complexity results (Strong Exponential Time Hypothesis) to transformer architectures.

### Weaknesses
1. It is not exactly clear when the paper talks about approximate or exact results. The distinction between proving hardness for finding the absolute most similar pair versus finding a pair within some approximation factor is not consistently maintained, leading to potential confusion about the practical implications of the theoretical results.
2. It relies on the BOW (bag of words) model, which already introduces approximation in practical settings. This makes results (which are about exact solution) weaker. The bag-of-words model discards word order and syntactic information, which are crucial for capturing semantic similarity in many real-world scenarios. Therefore, the theoretical hardness results, while interesting, may not directly translate to practical limitations for more sophisticated document embeddings.
3. Considering that finding closest pairs in Euclidean or Manhattan distance both require quadratic time (assuming SETH) is well know, results for MSD, LSD are fairly incremental. The paper's core results on MSD and LSD largely mirror existing complexity results for distance-based problems. While the connection to transformer architectures is novel, the underlying hardness results are not fundamentally new, and the incremental nature of the contribution should be acknowledged.

### Questions
> We focus on document similarity tasks, where one is given
as input many documents and would like to find a pair which is (approximately)
the most similar.

Could you please elaborate, why 'approximately' mentioned here? Is it not SETH and derived conjectures about exact results only?

> In other words, in order to perform tasks that (implicitly or explicitly) involve document similarity, one may as well use Transformer and cannot avoid its quadratic running time.

Approximate similarity search involves tradeoff precision and run time. If we talk about the exact solution of the similarity search, it would be nice to make it explicit.

> bag-of-words embeddings
How important is usage of bag of words embedding?  Would it be possible to use embedding / technique which takes into account word ?

### Soundness
3

### Presentation
4

### Contribution
2
