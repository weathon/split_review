# Permute-and-Flip: An optimally stable and watermarkable decoder for LLMs

- Decision: Accept
- Scores: 6, 8, 6, 6, 6

## Abstract
In this paper, we propose a new decoding method called Permute-and-Flip (PF) decoder. It enjoys stability properties similar to the standard sampling decoder, but is provably up to 2x better in its quality-stability tradeoff than sampling and never worse than any other decoder. We also design a cryptographic watermarking scheme analogous to Aaronson (2023)'s Gumbel watermark, but naturally tailored for PF decoder. The watermarking scheme does not change the distribution to sample, while allowing arbitrarily low false positive rate and high recall whenever the generated text has high entropy. Our experiments show that the PF decoder (and its watermarked counterpart) significantly outperform(s) naive sampling (and its Gumbel watermarked counterpart) in terms of perplexity, while retaining the same stability (and detectability), hence making it a promising new approach for LLM decoding. We provide the code in the supplementary materials.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors propose a new decoding method called the Permute-and-Flip (PF) decoder. This decoder maintains stability properties similar to standard sampling decoders while achieving up to 2x better performance in the quality-stability tradeoff than traditional sampling methods. A cryptographic watermarking technique from the specifically designed PF decoder has also been developed.
This work's core idea lies in applying PF sampling, initially developed in the context of differential privacy, to watermarking. They also argued that it is the first work to apply this method to LLM decoding and introduce the PF watermarking technique.

### Strengths
This paper introduces a new decoding method for large language models, called Permute-and-Flip (PF) decoding, along with a watermarking technique that allows precise control over false positive rates while maintaining high true positive rates. As a result, the approach balances detection accuracy and low perplexity, making it effective for generating high-quality text while preserving watermark detectability.

### Weaknesses
- While the PF watermark optimizes better, it reduces entropy in the distribution, potentially weakening the statistical signals that the watermarking scheme can leverage. This suggests that PF decoding may prioritize lower perplexity at the expense of detectability, raising questions about the balance between watermarking efficacy and text quality.
- PF decoding requires tuning the temperature T parameter to maximize detectability. Incorrect temperature settings could degrade performance, potentially limiting practical applications where robustness across diverse settings is essential.
- PF decoding involves a more complex computational process than softmax sampling, which can lead to higher computational costs, especially when handling large vocabulary sets. This complexity may restrict its applicability in real-time or resource-constrained environments.

### Questions
The paper claims that the proposed method allows for arbitrarily low false positive rates and high recall when the generated text has high entropy. However, it does not clarify the specific conditions or thresholds that define "high entropy" in the generated text nor the proportion of generated samples expected to meet this criterion. This is particularly confusing given the statement, "PF watermark is better at optimizing (recall Example 3.2 and Figure 1); thus, naturally, the resulting distribution has less entropy to be exploited by the watermarking scheme." This apparent contradiction raises questions about whether PF performance is generally suboptimal due to lower entropy. A precise explanation of these points would clarify the effectiveness and limitations of the PF watermark across different text generation conditions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
In this paper, authors propose Permute-and-Flip (PF) decoding for large language models (LLMs),
With reference to McKenna & Sheldon (2020)’s differentially private selection mechanism.
It enjoys the same perturbation-stability guarantees as softmax sampling and achieves substantially lower perplexity.
They also design PF watermark tailored for PF decoding that enables precise control over false positive rates while retaining high true positive rates, with reference to Aaronson (2023)’s Gumbel watermark.
Theorems and experiments indicate that PF decoding a promising new approach for practical applications of LLMs.

### Strengths
This paper successfully combines the results of previous studies such as McKenna & Sheldon (2020) and Aaronson (2023) in the context of LLMs research.
Theoretical guarantees are well organized and experimental performance verification is carried out sufficiently, and those make this study reliable.
The proposed method seems to have practical promise.

### Weaknesses
I found no serious weakness.

### Questions
I have no questions.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes sampling text from a language model using the Permute and Flip mechanism of McKenna and Sheldon—treating the token log probabilities as the "score" function to implement the mechanism—and proposes a method for watermarking text sampled from this mechanism.

### Strengths
The application of the Permute and Flip (PF) mechanism to sampling text from a language model is an interesting idea. The paper supports its main claims (about the effectiveness of the watermark) with both theoretical and empirical evidence.

### Weaknesses
Some parts of the overall problem formulation are not clear. For example, the stated goal is to maximize some utility function, in which case—unlike with differential privacy (i.e., the original context in which PF was proposed)—the optimal decoding strategy should be deterministic. The paper acknowledges as much but nonetheless argues in favor of using sampling via the following:

> That’s because there are other considerations besides text quality when selecting LLM decoders. For example,
computational efficiency and latency are hugely important, since each API call to the logits function is costly. The diversity of the generated text is also important, especially for creative tasks.

Several aspects of the above except are unclear. First, in what sense is greedy decoding more computationally expensive than sampling? Also, if diversity is important then why not formalize this as part of the problem statement (e.g., via the utility function)? Making these desiderata precise would help clarify the main problem statement and aid in comparing to prior work. For similar reasons, it's not clear what the motivation is for the stability property (Definition 2.1). The paper cites data poisoning and jailbreaking attacks as motivation, but the precise connection is not made explicit. The paper also mentions a connection between stability and diversity; however, if the only purpose of stability is to be a proxy for diversity, then why not just explicitly consider diversity? In general, being more explicit and rigorous about the problem formulation / desiderata would be helpful for clarity.

### Questions
> A more fair comparison, would be to increase the temperature for PF watermark appropriately so we compare detectability when the suboptimality is aligned. This is shown in Figure 2b. In fact we have added a second baseline that apply Gumbel watermark to the induced sampling distribution from PF-decoding (shown as the dotted line). The distribution induced by PF does not have a simple form, but in our special case, it was worked out in Example 3.2.

After increasing the temperature of the PF watermark so that its detectability is on par with the Gumbel watermark, is the utility of PF still better than that of Gumbel?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces the PF decoding method for LLMs, which is designed to improve text generation stability while lowering perplexity compared to traditional sampling methods. This method enhances quality-stability balance and integrates a cryptographic watermark for AI-generated text detection, using a pseudo-random technique that makes it secure and resilient to adversarial modifications. PF decoding achieves lower perplexity than softmax sampling while maintaining stability, and the PF watermark allows for high detection accuracy with precise control over false positives.

### Strengths
1. The proposed decoding method for LLMs is novel.
2. This paper provides theoretical proofs to support its statements.

### Weaknesses
1. Could authors specify the difference between the PF watermark and the Exponential Minimum watermark proposed in [1].

2. Diversity is an important property of LLM sampling. Are there any metrics or experiments to measure the diversity of different decoding methods?

3. PF watermark provides lower perplexity compared to Gumbel-Max watermark. Could authors present the robustness performance among PF watermark and other watermarking methods, like a token replacement, etc?

4. In Table 1, the authors specify the beam search can not watermark, but [2] uses beam search. Moreover, could authors explain the reason why beam search is not stable?

[1]. http://arxiv.org/abs/2307.15593
[2]. http://arxiv.org/abs/2301.10226

### Questions
please see above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The article introduces a novel decoder algorithm for LLMs. The proposed algorithm is based on the Permute-and-Flip (PF) method for differential privacy protection of data, which transforms the output of a dataset into independent sampling based on assigned probabilities to data elements. The paper also references an equivalent construction of PF, converting data sampling into random adjustments of the probability distribution of data elements, thereby outputting the element with the highest probability. This decoder algorithm can be used for embedding the output text, and the paper presents a watermark embedding algorithm based on the PF decoder. Compared to existing decoder algorithms, the paper demonstrates that the PF algorithm offers better stability.

### Strengths
1. A novel LLM decoder algorithm is proposed, and compared to existing algorithms, the PF decoder offers better randomness, which may provide improved output adaptability for certain application scenarios.

2. The paper proposes a method for embedding watermarks using the PF decoder. It converts candidate output tokens into different values using a pseudo-random function, thereby altering the output probabilities of the tokens to embed the watermark information.

### Weaknesses
1. The description of the scheme in the paper is not very straightforward. The PF decoder designed in the paper is not directly based on the original Permute-and-Flip method, but on a variant algorithm. Although it cites (Ding et al., 2021) to illustrate that the two methods are equivalent, this paper is still in a preprint status.

2. The paper does not sufficiently explain the characteristics of the PF decoder. In Theorem 3.1, the paper cites several quantitative calculations from (McKenna & Sheldon 2020) but does not explain their significance. Especially since the original paper was not intended for LLM decoders, the impact on the characteristics of the decoder in this context is unclear.

3. The experimental results show that PF does not demonstrate a significant advantage over existing algorithms. For instance, in text generation, its PPL is not superior to the greedy algorithm, and in watermark embedding detection, its TPR results are also not better than the comparison schemes.

### Questions
1. Some symbols in the paper are not fully defined. For example, what does  E_{y∼PF(u)}[u(y)]  mean?

2.In Theorem 3.1,  u^*  is the maximum value of  u(y)  outputs. However, in point 4,  u^* - u(y)  is used. How should one interpret a number being subtracted from a set? Perhaps this is related to the previous question?

### Soundness
3

### Presentation
2

### Contribution
3
