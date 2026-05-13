# A Watermark for Order-Agnostic Language Models

- Decision: Accept
- Scores: 5, 6, 6, 5

## Abstract
Statistical watermarking techniques are well-established for sequentially decoded language models (LMs). However, these techniques cannot be directly applied to order-agnostic LMs, as the tokens in order-agnostic LMs are not generated sequentially. In this work, we introduce \methodname, a pattern-based watermarking framework specifically designed for order-agnostic LMs. We develop a Markov-chain-based watermark generator that produces watermark key sequences with high-frequency key patterns. Correspondingly, we propose a statistical pattern-based detection algorithm that recovers the key sequence during detection and conducts statistical tests based on the count of high-frequency patterns. Our extensive evaluations on order-agnostic LMs, such as ProteinMPNN and CMLM, demonstrate \methodname's enhanced detection efficiency, generation quality, and robustness, positioning it as a superior watermarking technique for order-agnostic LMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents a watermarking method tailored for order-agnostic language models (LMs), which generate content in a non-sequential manner. The approach utilizes a Markov-chain-based key sequence to embed identifiable patterns within the generated content, enabling effective watermarking. Additionally, a statistical, pattern-based detection algorithm is employed for watermark verification. The authors also introduce a dynamic programming algorithm that optimizes the detection process by reducing its time complexity, enhancing the method's practical efficiency.

### Strengths
1. The paper effectively addresses the challenge of watermarking order-agnostic language models (LMs) by introducing a Markov-chain-based key sequence approach that overcomes the limitations inherent in traditional sequential watermarking methods.
2. The inclusion of a dynamic programming algorithm to optimize the detection process by significantly reduces the time complexity, thereby improving the practical feasibility of the proposed approach.
3. The proposed method enhanced detection accuracy and robustness, as well as the LMs output quality, in comparison to baseline methods.

### Weaknesses
1. The reliance on an alternating key sequence pattern introduces a potential vulnerability, as it may be more easily detected and disrupted by adversaries. Should the specific pattern structure (e.g., alternating keys) be identified, adversaries could develop targeted strategies to either erase or replicate the watermark. Incorporating more complex or adaptive key sequence strategies could enhance the method's robustness against such targeted disruptions.
2. The paper lacks a thorough discussion on why the proposed method, which utilizes alternating vocabulary splitting based on key sequences, outperforms global vocabulary splitting (e.g., the Unigram method) for watermarking order-agnostic LMs. Given that Unigram serves as a strong baseline, a detailed comparative analysis is needed to explain why the proposed approach achieves superior detection accuracy, robustness, and output quality despite both methods being context-independent.

### Questions
1. The authors should provide a detailed justification for why using an alternated vocabulary splitting strategy (the proposed method) offers advantages over a global vocabulary splitting approach (e.g., Unigram) in terms of output quality and watermark robustness in order-agnostic LMs, given that both methods are context-independent?
2. In Table 4, what does the term "attack strength ε" represent in the context of the ChatGPT paraphrasing attack? Additionally, how is this attack strength controlled or quantified during the experiments?
3. Could the authors clarify the mathematical meaning of \( e^\delta \) in Equation (1)? 
4. The method is described as Markov-chain-based due to its key sequence generation process; however, the paper’s use of an alternating key sequence (e.g., a fixed pattern like \( k_1, k_2, k_1, k_2 \)) does not appear to leverage the stochastic properties of Markov chains. This seems potentially misleading, as the approach is more akin to an alternated 0/1 key sequence than a Markov-chain-based generation. 
5. The proposed method employs fixed vocabulary splitting, which resembles the Unigram approach and may be easier to detect. What justification do the authors provide for the detectability and resilience of the proposed watermark against adversarial attempts to identify or remove it?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a watermarking scheme for order-agnostic language models based on the proposed pattern-mark and hypothesis test. The method generates key sequences through a Markov-chain-based key generator, improves the probability of sampling from the sub-vocabulary corresponding to each key, and detects key sequences of specific patterns to calculate the false positive rate using hypothesis test. Compared with other watermarking methods, the method proposed in this paper shows superiority in protein generation and machine translation.

### Strengths
1.	This paper is well-organized and well-written.
2.	The discussion part of the paper provides a good explanation of the motivation for the method.

### Weaknesses
1.	The paper does not detail how the vocabulary set is divided. Splitting the vocabulary will inevitably affect the original probability distribution, resulting in a decrease in output quality. In addition, improper vocabulary segmentation may lead to grammatical errors in the generated sentences, such as incorrectly connecting the verb after the preposition. Is the part of speech considered when dividing the vocabulary?
2.	The probability outputs of language models often exhibit high probabilities for certain tokens while other tokens have much smaller probabilities, sometimes approaching zero. Although the factor used in Equation (1) aims to increase the probabilities of tokens in the sub-vocabulary, this amplification factor does not seem sufficient to bridge the gap between low-probability and high-probability tokens. In other words, if the vocabulary segmentation is not reasonable, it may not effectively enhance the sampling probability for specific sub-vocabularies. Particularly, when there are many sub-vocabularies, they may consist entirely of low-probability tokens. Was the original probability output considered when segmenting the vocabulary?
3.	The paper does not provide detailed explanations on how to obtain the set of target patterns. The target patterns should accurately reflect the characteristics of the specific key sequence.
4.	The comparative experiments in the experimental part of the paper are insufficient. This paper only compares the methods of two papers.

### Questions
NA

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
3

### Summary
This paper proposes PATTERN-MARK, a watermarking method to label the output of order-agnostic language models (LMs). The authors developed a Markov-chain-based watermark generator to produce watermark key sequences, then assigned the keys one by one to the generated tokens to adjust their sampling probabilities. During detection, they first recover the key sequence from the suspected text and verify the watermark through hypothesis testing.

### Strengths
+） This paper is well-written and presents its ideas clearly.

+）This paper focuses on watermarking order-agnostic LMs, which, to the best of my knowledge, has not been considered in the existing literature.

+) This paper proposes an effective strategy to watermark order-agnostic LMs by embedding watermarks within the relationships between adjacent words.

### Weaknesses
-）I think the protein generation task is not suitable for experiments, as it may not be able to identify important unknown protein architectures.

### Questions
For the translation task, how can we identify whether a given text is generated by order-agnostic LMs or sequential LMs? This is critical for accurate detection.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a method for generating and detecting watermarks in ordered-agnostic language models (LMs). At a high level, the method is an extension of the red-green list approach in which the vocabulary is divided into two sets: the "green" list and the "red" list. The detector counts the number of tokens in the green list as a statistic for detection. The current method takes a more sophisticated approach to generating patterns in the key sequence by utilizing a Markov model during the text generation process. Detection is based on the number of patterns that appear in the key sequence, which are reconstructed from the text and the vocabulary partitions. The authors demonstrate that this method is more effective in terms of detectability and text quality than other existing watermarking schemes.

### Strengths
The paper presents a thorough investigation of watermarking for order-agnostic language models, a topic that appears to be less explored in the existing literature. The proposed method introduces several new ideas, including using Markov models to generate more complex patterns, setting it apart from previous approaches. The new approach shows promising performance when compared to existing methods. Additionally, the authors have explored the impact of various parameters on the method's effectiveness.

### Weaknesses
The assertion that "this is the first work to explore watermarking for order-agnostic language models" is somewhat exaggerated. The same problem can be addressed using existing methods, even though they may not be specifically tailored for order-agnostic settings (e.g., Zhao et al., 2023). 

Additionally, the proposed method is more computationally intensive compared to the red-green list approach. Furthermore, the Markov structure seems to introduce another factor (in addition to $\delta$), which could cause the distribution of the watermarked language model to differ from that of the original model.

### Questions
1. My main question is why the Markov model is suitable for order-agnostic language models (LMs). Order-agnostic LMs do not generate tokens from left to right, while Markov models create sequences in a left-to-right manner. This presents a discrepancy between the order-agnostic nature of the LMs and the order-dependent nature of Markov models. It is unclear why Markov models would be particularly appropriate for order-agnostic LMs. Additionally, the discussions in Section 3.2, central to the proposed procedure, are vague and require more careful explanations. 

2. The discussion regarding why distortion-free watermarking schemes cannot be adapted to order-agnostic LMs is misleading. For instance, on page 3, line 196, it states, “A distortion-free watermark requires independent probabilities…” The term “independent probabilities” is unclear in this context. Distortion-free refers to $P_W(x_n|\mathbf{x}_n^{oa},k_n) = P_M(x_n|\mathbf{x}_n^{oa},k_n)$. Additionally, the assertion that “The distortion-free property also requires non-repeating watermark keys during generation” lacks clarity. The authors should be cautious with such an impossibility claim, as it requires a proper justification.

3. The Markov structure seems to introduce another factor (in addition to $\delta$), which could cause the distribution of the watermarked language model to differ from that of the original model. I wonder if there is any way to quantify the distortion caused by the Markov model.

4. A potential drawback of the current approach is its time complexity. Could the authors report the computational time compared to other methods?

### Soundness
2

### Presentation
3

### Contribution
2
