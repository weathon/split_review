# Sparse Watermarking in LLMs with Enhanced Text Quality

- Decision: Reject
- Avg Score: 3.00
- Scores: 5, 1, 3, 3

## Abstract
With the widespread adoption of Large Language Models (LLMs), concerns about potential misuse have emerged. To this end, watermarking has been adapted to LLM, enabling a simple and effective way to detect and monitor generated text. However, while the existing methods can differentiate between watermarked and unwatermarked text with high accuracy, they often face a trade-off between the quality of the generated text and the effectiveness of the watermarking process. In this work, we present a novel type of LLM watermark, *Sparse Watermark*, which aims to mitigate this trade-off by applying watermarks to a small subset of generated tokens distributed across the text. To demonstrate this type of watermark, we introduce **SpARK**, a **Sp**arse Waterm**ARK** method that achieves sparsity by anchoring watermarked tokens to words that have specific Part-of-Speech (POS) tags. Our experimental results demonstrate that the proposed watermarking scheme achieves high detectability while generating text that outperforms previous LLM watermarking methods in quality across various tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes SpARK, a new watermarking method for LLMs that aims to improve detectability and text quality. Unlike traditional methods that watermark every token, SpARK selectively watermarks tokens associated with specific POS tags, such as verbs. By embedding watermarks sparsely and only in specific token positions, SpARK enhances text coherence and robustness against adversarial attacks like synonym substitution and paraphrasing. Experimental results demonstrate that SpARK outperforms other watermarking methods regarding text quality retention and detection accuracy across various tasks and datasets.

### Strengths
1. By using POS tags to select tokens for watermarking, SpARK ensures that watermarking is applied selectively and minimally, reducing the model's interference with the natural language structure.

2. The methodology section is well-structured, with algorithms (e.g., POSWatermark, DetectWatermark) clearly defined. SpARK is tested against several existing watermarking techniques (e.g., Hard, LeftHash, SelfHash, and Unigram), allowing for a direct comparison of text quality, semantic similarity, and robustness.

### Weaknesses
1. While the method offers an interesting approach, it lacks significant novelty. Similar methods that alter synonyms based on POS tags already exist. This approach instead modifies logits to increase the number of "green" tokens. From a security standpoint, this method has notable weaknesses. In contrast to KGW-type watermarks—which embed watermarks in nearly every token, making it difficult for adversaries to distinguish green from red tokens—this method is more vulnerable. If adversaries know that POS tagging is used in the watermarking process, they could easily defeat it by randomly substituting verbs and nouns with synonyms. Additionally, because POS tagging patterns are relatively consistent across different texts, adversaries would not need to invest much effort to identify and remove the watermark.

2. Although the POS tagging approach is well-motivated, the experiments mainly focus on three tags (Verb, Noun, Determiner), with limited analysis on why these particular tags were chosen over others beyond their document frequency. A broader exploration of different tags and their effectiveness in watermarking would strengthen the study.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposed a sparse text watermarking algorithm via POS (part-of-speech) with the intention to improve the text quality that could be damaged by the KGW algorithm. To be specific, the watermarking algorithm would only be activated when the next token is of a certain group of POS tags. By leaving the generation process of other types of token unchanged, the text quality of generated output can be improved.

### Strengths
The idea is simple and easy to understand.

### Weaknesses
This paper obviously lacks baselines that are up-to-date to compare with, including but not restricted to SWEET [1], EWD[2]. Simply using the standard KGW[3] and Unigram[4] with different hash functions is far from sufficient in proving the effectiveness of the proposed method. BTW, both SWEET and EWD proposed to selectively perform watermark generation/detection according to token entropy, and have shown better text quality/detection accuracy in their work. To prove the proposed work is better than the listed two, more experiments on text quality, time complexity, detection accuracy and using low-entropy datasets should be conducted.

### Questions
As listed in Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present "SpARK," a sparse watermarking method for large language models (LLMs), claiming that it achieves high detectability with minimal impact on text quality by watermarking a subset of generated tokens linked to specific POS tags. While the concept is well-explored, the novelty of this approach is questionable.

### Strengths
1. Innovative Use of POS Tags: The paper introduces an innovative approach by associating watermarks with specific Part-of-Speech (POS) tags, allowing for selective, sparse embedding. This method cleverly leverages the natural structure of language, enhancing the watermark's subtlety and detectability.

2. High Detection Performance: The experiments demonstrate that SpARK achieves near-state-of-the-art detection performance (e.g., True Positive Rate and True Negative Rate close to 100%) across various datasets, while maintaining minimal text quality degradation.

### Weaknesses
1. Lack of Innovation: The core idea of applying watermarks to a sparse subset of generated tokens is not novel. Existing works have already explored similar sparse watermarking and selective token modification methods. The paper fails to demonstrate a significant deviation from or advancement beyond these existing solutions. Recent watermarking studies already emphasize limiting the impact on text quality while ensuring robustness, making SpARK's claims less compelling.

2. Questionable Benefit Claims: The authors argue that SpARK's sparse watermarking reduces the degradation of text quality compared to dense watermarking. However, numerous recent works on text watermarking already achieve minimal or no impact on text quality. These techniques do not require sparsity to maintain text integrity, suggesting that the claimed advantage of SpARK may not be as impactful as presented.

3. Evaluation Limitations: While the authors provide experimental results demonstrating the performance of SpARK, the evaluations do not sufficiently differentiate it from existing sparse watermarking techniques. The lack of comparative analysis with newer and more diverse watermarking approaches that similarly preserve text quality undermines the validity of the claimed improvements.

### Questions
1. What are the advantages of your method compared to distortion-free watermarking methods in LLMs?

2. The method proposed in the paper demonstrates a certain level of robustness against lexical substitution attacks. The paper notes that the method effectively maintains robustness when facing a 10% substitution rate, but as the substitution rate increases (e.g., 30% or 50%), the detection accuracy declines. My question is: Do you consider maintaining robustness against a 10% substitution rate as indicative of strong robustness? Additionally, is 10% sufficient for real-world application scenarios?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a watermarking technique called SpARK for Large Language Models (LLMs), which selectively embeds watermarks in a small subset of generated tokens. This approach aims to maintain high text quality while ensuring watermark detectability. Experimental results demonstrate that SpARK outperforms traditional watermarking methods in text quality across various tasks and effectively withstands common attacks, such as substitution and paraphrasing. By adding watermarks to tokens of specific part-of-speech tags and only detecting these specific tokens, this method preserves text quality without compromising detectability.

### Strengths
1. Although the idea may seem simple, it effectively maintains text quality by focusing watermarking on tokens with specific part-of-speech (POS) tags. This strategy helps mitigate robustness issues caused by token insertion or substitution in other positions.
2. Compared to traditional methods such as Hard Red-Green, Soft Red-Green, LeftHash, SelfHash, and Unigram, SpARK demonstrates a clear advantage in preserving text quality during watermarking.
3. The paper provides a thorough analysis of robustness against various attacks and considers resistance to watermark stealing, showcasing the method's effectiveness in real-world scenarios.

### Weaknesses
1. The main consideration of the paper is to preserve text quality; however, the baseline methods compared in the main experiments are traditional and do not primarily focus on preserving text quality.
- While there is a comparison with distortion-free methods in Appendix F, the only measure for text quality is perplexity (PPL), which is insufficient, and SpARK does not demonstrate an advantage over distortion-free methods.
- Additionally, other methods that could aid in preserving text quality, such as unbiased watermark[1], DiPMark[2], TS-Watermark[3], and SWEET[4], were not included in the experiments.

### Questions
See the Weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2
