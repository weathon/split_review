# Understanding Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Structured State Space Models (SSMs) have emerged as alternatives to transformers, addressing the challenges of processing long sequences.
While SSMs are often regarded as effective in capturing long-term dependencies, we theoretically demonstrate that they suffer from a strong recency bias.
Our empirical findings reveal that this bias impairs the models' ability to recall distant information and introduces robustness issues.
We conducted scaling experiments and discovered that deeper structures in SSMs facilitate the learning of long contexts.
However, our theoretical analysis reveal that as SSMs increase in depth, they exhibit a tendency toward over-smoothing, resulting in token representations becoming increasingly indistinguishable.
This over-smoothing phenomenon ultimately constrains the scalability of SSMs to achieve improved performance.
Collectively, these findings highlight important limitations of SSMs and underscore the need for further research to address these challenges in long-range sequence modeling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents 2 limitations of current SSM. The first points out to the fact that SSMs suffer from a strong recency bias. This in turn limits the SSMs ability to recall distant information and introduces robustness issues. Secondly, it is revealed that as SSMs increase in depth, they exhibit a tendency toward over-smoothing, resulting in token representations becoming increasingly indistinguishable

### Strengths
1. The paper presents important findings, which open up future directions to resolve the issue.
2. The section on adversarial attacks is praiseworthy, as it utilizes one of the findings to describe something very practical.
3. Both findings are substantiated with some theoretical understanding.

### Weaknesses
1. While, empirical results are satisfactory for the recency of SSMs, I don't feel these are extensive for the claim of over-smoothing in SSMs.
2. How do initialization scheme of SSMs interfere with these findings. Can there be some discussion around these?

### Questions
Please see above

### Soundness
2

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
5

### Summary
This paper lists inspects and provides a theoretical investigation of some of the pitfalls of SSMs. Such pitfalls are caused by a "recency bias," which alters the "token importance," making it flow exponentially down to zero. This fact presents an issue for robustness, as well as for needle-in-a-haystack problems.

### Strengths
What I really like about this paper is that it is easy to understand, it is well written and interesting. The contributions are, in my opinion

1) giving practical examples of failure cases of SSMs.

2) showing high-quality and clear plots that can be used for future research or for reference.

This paper indeed seems a bit like a "first step". I like it, though: definitely SSMs have such problems (as intuitively the case and also as pointed out in recent literature) -- yet is **very good to have a reference** - will be interesting for future research!

### Weaknesses
I think the following are weaknesses in the current status:

1) The derivation of "exponential memory" results are not novel nor surprising: it is very well known that SSMs have exponential memory (e.g., https://openreview.net/forum?id=i0OmcF14Kf). It is also known that they might struggle with long memory (https://arxiv.org/abs/2402.01032) and to retrieve past information (https://arxiv.org/abs/2312.04927) -- yet scale helps (https://arxiv.org/pdf/2406.07887).

2) Note that exponential memory per see does not imply loss in perplexity and length generalization; this was shown in recent papers such as https://arxiv.org/pdf/2410.11135v1 (or the xLSTM paper https://arxiv.org/abs/2405.04517). Note also that Alibi positional embedding induce a similar exponential decay.

3) The CIFAR robustness example I find a bit weak because here you are implicitly constructing a 1D model for 2D data: in 1D data, recency bias is actually helpful! In 2D there is no notion of recency. I think the example is interesting for improving or researching Visual state-space models such as VMamba. Please frame this a bit more carefully.

3) The paper does not provide hints into solving the stated problems.

### Questions
What do you this should the path ahead be for improving SSM models?

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper identifies two issues in State Space Models: the recency bias in long-context modeling and the over-smoothing effect that arises as the model scales. The authors provide a theoretical framework to analyze these challenges and substantiate their findings with empirical evidence.

### Strengths
The paper is well-written and easy to follow.

Experiments are extensive and effectively support the theoretical results.

### Weaknesses
While the authors have comprehensively identified and examined these two issues, they did not provide any discussion on possible methods for mitigation. Including a brief exploration of potential strategies could further enrich the paper's contributions.

The problem of recency in SSMs appears somewhat similar to the vanishing gradient problem in RNNs mentioned in, e.g., [1]. Could the authors provide a discussion comparing these two phenomena and highlight the novelty of this work?

The experimental details for Section 4.1 are currently lacking, which makes it challenging to assess the validity of the results fully. Additionally, if I understand correctly, the over-smoothing problem is characterized by a performance degradation when additional layers are stacked beyond a certain threshold (as observed with GNNs, see [2]). However, this effect does not appear to manifest in the experiments presented in Section 4.1. Could the authors clarify whether this phenomenon is inherently absent in SSMs or if it might be a limitation of the current experimental setup?



Minor comments: 
- Typo in Eq. 4: The indices $i$ and $j$ are likely meant to be $s$ and $t$.
- Typos in Eq. 18 and Eq. 19: the inequality signs are likely to be $ \geq $ and $ \leq $, respectively.

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates why the neural networks based on state space models (SSMs) are inferior to Transformers for sequence data with long-range dependencies. First, the authors theoretically and experimentally demonstrate that the SSM output’s dependency on input diminishes exponentially with the distance from the output position. They call this phenomenon recency bias. They also reveal through experiments that SSMs are vulnerable to attacks targeting the trailing part of the sequence due to recency bias. Furthermore, they explore the effects of increasing the layers of SSMs and find that while this reduces recency bias, it causes over-smoothing.

### Strengths
1. The limitations of SSMs’ capabilities are theoretically examined from multiple perspectives, including recency bias, robustness to attack, and over-smoothing.
2. Since multiple experiments closely linked to the theory are conducted, the paper’s claims are easy to understand.

### Weaknesses
1. One of the contributions of the paper is that the authors demonstrate the exponential decay of the input-dependency on the SSMs’ output. However, similar findings have already been established in studies such as [Wang & Xue, 2023] (Theorem 3.13).

    [Wang & Xue, 2023] State-space models with layer-wise nonlinearity are universal approximators with exponential decaying memory. In NeurIPS 2023.
    
2. The experiments on recency bias, such as those in Figure 2, are limited to a few pre-trained models. As with the experiments in Figure 4, it would be preferable to observe the change in performance across the number of parameter counts. In particular, it should be checked whether recency bias can be reduced when the dimensions of the hidden state and the number of heads are moderately increased.
3. Line 463 suggests a trade-off between A_max (related to recency bias) and A_min (related to over-smoothing). However, it is not trivial whether this is actually a challenge when training SSMs since $A_{\max}\approx 1$ and $A_{\min}\approx 0$ can hold at the same time. To clarify this point, additional experiments would be beneficial, such as observing the dynamics of A_min and A_max during training.

### Questions
1. In the experiment in Figure 1, the context length is around 1000, whereas in Figure 2, it exceeds 10,000. In the latter case, would there be any difference between SSMs and Transformers with a context length around 1000?
2. Are there any experimental/theoretical results showing that over-smoothing does not occur in Transformers? Figures 4 and 5 contain experimental results demonstrating over-smoothing in Mamba; is it possible to conduct similar verification for Transformers?

### Soundness
3

### Presentation
3

### Contribution
3
