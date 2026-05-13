# Characterizing Context Influence and Hallucination in Summarization

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Although Large Language Models (LLMs) have achieved remarkable performance in numerous downstream tasks, their ubiquity has raised two significant concerns. One is that LLMs can hallucinate by generating content that contradicts relevant contextual information; the other is that LLMs can inadvertently leak private information due to input regurgitation. Many prior works have extensively studied each concern independently, but none have investigated them simultaneously. Furthermore, auditing the influence of provided context during open-ended generation with a privacy emphasis is understudied. To this end, we comprehensively characterize the influence and hallucination of contextual information during summarization. We introduce a definition for context influence and Context-Influence Decoding (CID), and then we show that amplifying the context (by factoring out prior knowledge) and the context being out of distribution with respect to prior knowledge increases the context's influence on an LLM. Moreover, we show that context influence gives a lower bound of the private information leakage of CID. We corroborate our analytical findings with experimental evaluations that show improving the F1 ROGUE-L score on CNN-DM for LLaMA 3 by \textbf{10\%} over regular decoding also leads to \textbf{1.5x} more influence by the context. Moreover, we empirically evaluate how context influence and hallucination are affected by (1) model capacity, (2) context size, (3) the length of the current response, and (4) different token $n$-grams of the context.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the relationship between context influence and privacy leakage (e.g., PIIs) in LLMs. Specifically, context influence and context influence decoding (CID) were introduced and shown to give a lower bound of the private leakage of CID.

### Strengths
Strengths:
- The paper is very well written and easy to read.
- The topic is quite timely and interesting.
- The method is sound and summarization experiments (e.g., context influence, etc.) have been conducted on two datasets to show the effectiveness of the proposed method.
- Mathematical proofs and qualitative examples are provided to back up the proposed idea and results.

### Weaknesses
Weaknesses:
- My overall assessment of the paper is mostly positive, but I do have the following concern/question re the privacy part of the paper: 

Q. The main focus of the privacy part of the paper is on the fact that LLM can inadvertently regurgitate private information in the prompt. However there is no evaluation of the method whatsoever nor a relevant privacy metric in an adversarial learning setting (e.g., private attribute inference attacker [1])  that quantifies how well the proposed method is able to protect users from such attacks. In fact, except for the connection between the proposed method and DP mentioned in the appendix, I don’t see any other relevant information in the paper. I’d like to see some experiments and evals similar to [1] on different LLMs’ summary outputs (especially those from smaller ones) on both datasets.

[1] Privacy-Aware Recommendation with Private-Attribute Protection using Adversarial Learning, 2019.

### Questions
Please see the weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work studies the relationship between hallucination (generating content that contradicts context) and privacy risks from input regurgitation in LLMs. The authors propose a formal definition of "context influence" and introduce CID, demonstrating that amplifying context to reduce hallucination leads to increased context influence and potential privacy leakage. Through experiments using multiple models and datasets, they show that improving generation quality comes at the cost of significantly increased context influence, while also analyzing how factors like model capacity, context size, and response length affect this tradeoff between hallucination and privacy.

### Strengths
The problem of context leakage is very interesting, especially since RAG models are being more used in industry now. Theory statements seem correct.

### Weaknesses
## Sections 1 and 2

I'm familiar with hallucination/trustworthiness in LLMs, but not with the specific paper(s) this works draws ideas from. So it was particularly hard for me to follow the jargons used, I wasn't able to precisely infer the contributions from it. In particular, I suggest the authors change the presentation incorporating a figure with a running example of the problem. Some of the sentences are not very accurate, e.g. 

> With the knowledge obtained during pre-training Devlin et al. (2018); Radford et al. (2019), due to the exponential scaling of the transformer architecture Vaswani (2017) and pre-training data Chowdhery et al. (2023), LLMs display an In Context Learning (ICL) ability to further improve on various downstream tasks without additional training by supplementing prompts with relevant context

I don't think we understand the emergence of ICL that well ---in specific the citations don't claim that. We have a few promising hypotheses in other papers, but nothing that is as strong as the above claim. The authors can just say it's a well-documented emergent behavior in LLMs.

It's very hard to understand the problem setup and motivation in the first two pages. For instance, the words "context" and "hallucination" are consistently used without an appropriate definition. The paper is heavily based on Shi's contribution, which I was not familiar with. I read it and then understood section 2, but I think the authors need to rethink how they present it, making it more self-contained. An important comment to make about Eq 2 is that it biases the distribution by making the model more confident when the document posterior diverges from the prior. I think this comment can compress most of the text there.

## Section 3
>  we present a slightly more granular definition of P-CXMI

P-CXMI is only mentioned once in the paper, I still don't know what it is.
Def 3.1:
Documents were defined as vectors, not sets, do the authors mean that $D'$ is a substring of $D$?
What's $f_{Mem}$?

The author's main contribution is Eq 5. I'm not sure I see the novelty here other than simply down-weighing the context influence in the decoding.

> Since sampling from a probability distribution inherently induces privacy

This statement is wrong. In general privacy is saying a divergence between the distribution coming from one dataset to the distribution coming from an adjacent dataset is small. These are very different things, simply having a distribution isn't enough for privacy, e.g. dirac delta.

## Section 4

I had a hard time understanding the results. What's the main question the authors are trying to answer? It seems that the results just show how Eq 2, from Shi, is a good strategy to ground the model's faithfulness. What's the takeaway with respect to the authors method? It's not clear to me.  From the abstract I can tell you want to show that grounding the answer costs leaking context, but my comment for here is that this is not clearly highlighted in the section.

### Questions
I have a few questions in the weaknesses box, please refer to them. Here's some others:
- I don't think I understand the role of theorem 3.1. Can you explain to me its relevance? From the definition of pmi in Eq 2 it's straightforward to see that it enforces the context influence, since it was designed for it. Thus, as you increase the penalty, the more you'll concentrate.
- What is the takeaway of section 3.3 if you do not know $\lambda^*$? You can always tweak a model to achieve DP with some specified, unknown, parameter.
- Why do you focus on summarization? It seems that the focus is only because the experiments were run on summarization.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a definition of context influence and presents a decoding method for large language models (LLMs) named context influence decoding (CID). Previous work like [1] amplifies pointwise mutual information (PMI) to mitigate hallucination during decoding. PMI is measured by computing the difference between the probability with and without the context information. This paper argues that PMI could leak privacy since context may contain sensitive information. Specifically, privacy here is defined as the privacy of the prompt (or the context). In response, the authors characterize the context influence, simultaneously considering the privacy of the context.

[1] Shi, W., Han, X., Lewis, M., Tsvetkov, Y., Zettlemoyer, L., & Yih, S. W. T. (2023). Trusting your evidence: Hallucinate less with context-aware decoding. arXiv preprint arXiv:2305.14739.

### Strengths
The definition of P-CXMI in Definition 3.1 is an intuitive and useful extension to PMI (or previous P-CXMI), by subtracting a subset of the context and computing their difference. 

In Section 3.3, the authors bridge DP and context influence, which I think is novel. 

The experiments are adequate and show useful insights for decoding with context. For summarization, the privacy of the context and summarization quality are an important tradeoff.

### Weaknesses
Major suggestions. 

First, I am worried about the technical contribution of CID. In Equation 5, the authors claim that CID is indeed a linear combination of the prior and posterior logits, which is controlled by an additional temperature parameter. Compared to previous work [1], which proposes to reweight the logit by amplifying posterior $(1+\alpha)logit(y_t|c,x,y_{<t}) - \alpha logit(y_t|x,y_{<t})$, the only difference between this paper and [1] is to introduce a more general parameter $\lambda$, and a temperature parameter. In this way, the authors should consider CID as a simple extension of CAD. Also, from the experimental results, the faithfulness score is not comparable when $\lambda=0.5$, which somehow shows that averaging prior and posterior logits is not a common practice for decoding with context although a smaller $\lambda=0.5$ can lead to a better privacy score.

Second, although the authors define context influence by subtracting a subset of the context instead of subtracting the whole context, from Appendix C, the prompts used in this paper only consider removing the whole context. There seems an additional simplification in the experiment. I understand that removing a subset of a new article or a PubMedQA document is hard to define. However, even a simple experiment that considers this property can help the understanding of context influence. 

Minor suggestions. 

In Section 3.3, the authors discuss the relationship between CID and differential privacy (DP). I get the concept (e.g., $\epsilon$-DP and the relationship between context influence and DP) only after reading the appendix. I would recommend the authors move some of the definitions and discussion in Appendix B to the main article for a clear presentation. Also, if the authors could accept my first major suggestion, I would recommend that the authors discuss more about privacy in the method section, while keeping CID as an extension of the preliminary. 

A typo after Equation 1: (P-XCMI) should be (P-CXMI). 

[1] Shi, W., Han, X., Lewis, M., Tsvetkov, Y., Zettlemoyer, L., & Yih, S. W. T. (2023). Trusting your evidence: Hallucinate less with context-aware decoding. arXiv preprint arXiv:2305.14739.

### Questions
1. What are the major technical contributions of CID compared to previous work? 

2. The authors seem to only evaluate removing all context in the experiment. I would be interested in seeing how removing a subset of context affects the output. 

3. Relating context influence with DP is novel, however, is there a way to distinguish the information? In other words, how do the authors determine which part of the information is private and which part benefits the generation quality? 

I will raise my score if the authors could address my concerns. I extend my best wishes to the authors for this study.

### Soundness
3

### Presentation
3

### Contribution
3
