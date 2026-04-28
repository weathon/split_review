# Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Recent alignment algorithms such as direct preference optimization (DPO) have been developed to improve the safety of large language models (LLMs) by training these models to match human behaviors exemplified by preference data. 
However, these methods are 
both computationally intensive and
lacking in controllability and transparency, 
inhibiting their widespread use.
Furthermore, these tuning-based methods require large-scale preference data for training and 
are susceptible to noisy preference data.
In this paper, we introduce a tuning-free alignment alternative, \method (\underline{Pro}jection \underline{F}ilter for \underline{S}ubspaces), and demonstrate its effectiveness under the use case of toxicity reduction. 
Grounded on theory from factor analysis, 
\method is a sample-efficient model editing approach that
identifies a toxic subspace in the model parameter space and reduces model toxicity by projecting away the detected subspace. 
The toxic subspace is identified by extracting preference data embeddings from the language model, and removing non-toxic information from these embeddings.
We show that \method is more sample-efficient than DPO, further showcasing greater robustness to noisy data. 
Finally, we attempt to connect tuning based alignment with editing, by establishing both theoretical and empirical connections between \method and DPO, showing that \method can be interpreted as a denoised version of a single DPO step.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a novel flow matching method. This method can be applied to high dimensional data measured at non-equidistant time points without reducing dimensionality, so that the dynamics of the data are not oversimplified. The method is validated on several datasets and showed the improvement compared to existing methods.

### Strengths
This paper relied on the key observation/assumption that embedding vector $\approx$ high-frequency vector + toxic vector + context-dependent vector, and then used linear algebra tools including SVD to separate toxic vectors. I think an algorithm to separate toxic vectors based on the factorization of the embedding vector is original and nicely designed. Although, my research is not in LLM, so I cannot correctly evaluate originality or significance. I think the paper is in good quality and clearly written.

### Weaknesses
As far as I understand, the weakness also comes from the key assumption that embedding vector $\approx$ high-frequency vector + toxic vector + context-dependent vector.

If toxic vector and other vectors are not linearly separable but have interaction terms, then we cannot really separate out toxic vectors by the projection matrix as Step 3 suggested. Could we guarantee that this interaction between the toxic and other features do not happen? Or can we verify that the interaction terms do not exist in the dataset? Designing a new algorithm considering the interaction terms would be beyond the scope of this paper, but this kind of discussion would be helpful to readers.

### Questions
As far as I understand, the algorithm is handling in fact a more flexible model than what is described in Equation (4). Currently in Equation (4), stopword parts of all data points are either one of two vectors, $a^{+}\mu$ for toxic data and $a^{-}\mu$ for non-toxic data. In Eqation (1) in Step 1, the linear space spanned by $\mu$ is removed from each data. Hence in Equation (4), it is not required that $x_{i}^{+}=a^{+}\mu$, i.e., stopword parts are all the same, but we can relax so that $x_{i}^{+}=a_{i}^{+}\mu$, we can let stopword parts be different but just on the linear space spanned by $\mu$. Also, we can relax so that $x_{i}^{-}=a_{i}^{-}\mu$. Is my understanding right, or is there some reason that stopword parts of all toxic data should be identical?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
First, as wrote to the AC ( or at least I tried) I am not competent for reweing this manuscript and I hope that more qualifiedd reviewers will comment on the paper.

Nonetheless, I have read the paper, and I am trying to give useful feedback.

The paper introduces a novel alignment alternative called Project Filter for Subspaces (ProFS), which relies on running SVD on the model parameter space. The method tries to disentangle the so-called "toxic subspace." Overall, the paper is somewhat empirical yet tries to connect its approach with some theoretical work. From its experiment, the approach seems to work reasonably well.

I appreciate the presentation

For example, I can't tell if the equation
embedding  ≈ high-frequency vector + toxic vector + context-dependent vector
makes sense or it is wishful thinking. It seems that previous literature goes in this direction, but I myself am quite unsure about that.

### Strengths
The paper read well and is easy to follow. I was able to follow it. The mathematical details for the use of SVD seem correct. From an outsider's perspective, the idea seems sensible.

The general idea is to look at the difference of the embedding matrix between label toxic and non toxic content, hence giving an idea of   what seems to differ between the two embeddings. The gist is to project the toxic embedding torward an not toxic embedding while keeping the non toxic embedding untouched.

The benchmarks seems quite extensive across multiple different model, and the robustness to misslabelling sounds like an interesting but my understanding is that is quite because this procedure keep the "distance" between the toxic vs non toxic embedding constant.

### Weaknesses
The problem that I have with this paper (and perhaps with this literature) is that the framework proposed matches really closely the literature, and so from a theoretical perspective, it sounds a bit like the authors assume some framework is designed for SVD to work and then suggest the using SVD in this context. While this is more of a theoretical criticism,    from a benchmark perspective, this approach seems to work decently. So perhaps I am a bit harsh.

Specifically, the paper's reliance on the linear representation hypothesis, while empirically supported in some contexts, feels somewhat like a post-hoc justification for applying SVD. The assumption that a 'toxic subspace' can be neatly disentangled via SVD, without a more rigorous theoretical grounding, is a concern. The method seems to leverage the properties of SVD to find a low-rank approximation of the difference between toxic and non-toxic embeddings, but it's not entirely clear why this specific approach is the most appropriate, beyond its computational convenience. The lack of a deeper theoretical analysis of why SVD should be effective in this particular scenario is a weakness.

### Questions
Have you considered using other approaches like sparse SVD or Non-negative matrix factorization?
 Could you comment on the effect on the size of $T_l^0$ and its effect on reducing toxicity? 
I suspect that you need a decent amount of data. Have you tried testing a version with few rows (say just 100), and what is the recommended corpus size one should use?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors propose to align large language models by projecting out subspaces from late-layer MLPs in the LLM. This is then shown to be connected to DPO in one layer. Good performance is seen across a range of models for toxicity, and some initial results are obtained for broader-spectrum alignment.

### Strengths
This approach successfully matches or even outperforms DPO, with a fraction of the training cost. If it fully generalizes to broad-spectrum alignment goals, this could be a powerful approach for cheaply aligning open source models. 

The presentation is thorough and well-written, and the authors have provided extensive numerical experiments despite having limited GPU hardware.

### Weaknesses
While the experimental results are quite extensive and thorough, only DPO is compared against (and only with the default hyperparameters). See "Questions" below for a possible suggestion to expand comparisons by referring to benchmark experiments in the literature.

Experimental results could be made more readable by more prominently defining metrics, and indicating whether higher or lower is better.

Minor style point: Throughout, "inter alia" is used, but I believe "etc." is probably the more preferred Latin phrase here.

### Questions
As far as I can tell, the proposed method is only compared against DPO, while other methods like KTO, IPO, and AOT exist and can outperform. I understand more evaluations may be prohibitively expensive, but perhaps it would be worth it to find benchmark experimental results for some of these alternatives in the broader literature? ProFS could then be run on the same benchmark to get directly comparable results.

Clearly the linear projection method is powerful - if it does have a weakness, I imagine that it might be that it would be too heavy-handed/brittle in some sense if the subspaces end up being primarily about specific words. Are ProFS-aligned models still able to, for instance, have non-toxic discussions about words included in the toxic subspace? Or are they robust to being prompted to give toxic opinions using professional, nontoxic language? Furthermore, it is often desirable that models refuse to reply to harmful instructions (rather than reply in a nontoxic way). How well would the subspace approach work in aligning a model to refuse to reply?

### Soundness
4

### Presentation
4

### Contribution
4
