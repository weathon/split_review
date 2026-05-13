# Language Fusion for Parameter-Efficient Cross-lingual Transfer

- Decision: Reject
- Scores: 3, 6, 5, 3

## Abstract
Limited availability of multilingual text corpora for training language models often leads to poor performance on downstream tasks due to undertrained representation spaces for languages other than English. This 'under-representation' has motivated recent cross-lingual transfer methods to leverage the English representation space by e.g. mixing English and 'non-English' tokens at input or extending model parameters to accommodate new languages, which in turn increases computational complexity. To address this, we introduce **F**usion for **La**nguage **Re**presentations (FLARE) in adapters, a method designed to improve both the representation quality and downstream performance for languages other than English. FLARE integrates source and target language representations within the bottlenecks of low-rank LoRA adapters using lightweight linear transformations. This maintains parameter efficiency as the method does not require additional parameters, while improving transfer performance, further narrowing the performance gap to English.
Furthermore, the proposed latent representation fusion does not increase the number of input tokens, this way maintaining computational efficiency. Moreover, FLARE provides flexibility to integrate various types of representations, e.g., we show that it is possible to fuse latent translations extracted from machine translation models. A series of experiments across representative cross-lingual natural language understanding tasks, including natural language inference, question-answering and sentiment analysis, demonstrate FLARE's effectiveness, reducing the average performance gap to English to 8.39% for XLM-R Large and 12.41% for Llama 3 across our benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces the method FLARE to improve cross-lingual performance in multilingual language models. FLARE utilizes adapters, specifically low-rank LoRA adapters, to fuse representations from source (typically English) and target languages without adding extra parameters or increasing computational complexity. The method reduces the performance gap between English and non-English languages by efficiently combining language-specific information within the adapter layers, demonstrating improvements across tasks such as sentiment analysis and question-answering.

### Strengths
- The method is parameter-efficient, as it achieves improved cross-lingual performance without additional parameters.
- The method maintains computational efficiency by fusing representations within adapters rather than extending input sequences.
- The method allows the integration of various representation types, such as latent translations from machine translation models.

### Weaknesses
 - FLARE’s performance is dependent on the quality of machine translations, potentially limiting its effectiveness in low-resource languages.
- The method has been tested primarily in bilingual scenarios, which may limit its generalizability to more complex multilingual contexts.

### Questions
-

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
3

### Summary
**Paper Summary**:
- The paper introduces an approach that fuses multilingual representations to improve their quality and the downstream performance of multilingual language models in a computationally efficient manner. The work integrates the fusion into low-rank adapters, and comprehensive experiments show that this approach can boost performance across multiple cross-lingual NLU tasks.

### Strengths
**Summary Of Strengths**:

- Parameter/computation efficiency: No additional parameters are needed to improve performance, as the fusion occurs within the adapter bottlenecks.
- Quality: The work shows positive experimental results that narrow the gaps between English and non-English language performances across multiple downstream tasks. Meanwhile, the comprehensive discussion and analysis in Section 5 brings insightful ideas to the community regarding this research direction.

### Weaknesses
 **Summary Of Weaknesses**:
- Limitations: As the authors note, this work focuses on bilingual transfer, so it is very difficult to draw conclusions about the effectiveness of this method in language identification-agnostic scenarios. The method's reliance on a clear source and target language pair limits its applicability in more realistic scenarios where the input language may not be known beforehand. This is a significant limitation, as many real-world applications require models to handle multiple languages without explicit language identification.
- Dependencies on data quality: Multilingual or, especially, low-resource data present significant challenges in LLM training. While this work seems promising, the impact of removing this dependency has not been fully addressed. The method's performance could be significantly impacted by noisy or low-quality training data, especially for low-resource languages where high-quality parallel data is scarce. The paper does not fully explore the robustness of the proposed fusion approach under such conditions.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present a method called Fusion for Language Representations (FLARE) to enhance cross-lingual transfer in multilingual language models. FLARE integrates source and target language representations within LoRA adapters, aiming to improve performance on downstream tasks for languages other than English. Experimental results across tasks such as natural language inference, question answering, and sentiment analysis demonstrate that FLARE effectively reduces the performance gap between English and other languages. The method shows consistent performance gains across various model architectures, including XLM-R, mT5, and Llama 3.

### Strengths
1. FLARE enhances cross-lingual transfer without increasing the model's parameter count or computational overhead. By integrating source (e.g., English) and target language representations within LoRA adapters, it maintains efficiency while improving performance.
2. The method demonstrates consistent improvements across various tasks—natural language inference, question answering, and sentiment analysis, highlighting its general applicability in cross-lingual settings.
3. FLARE is evaluated on multiple model architectures (XLM-R, mT5, Llama 3), showing its effectiveness across encoder-only, encoder-decoder, and decoder-only models.

### Weaknesses
1. The main contribution appears to be the integration of source and target language representations within LoRA adapters, which may be seen as an incremental extension of existing methods. The paper could benefit from a clearer articulation of how FLARE differentiates itself from prior work and what specific novel insights it brings to the field.

2. While FLARE shows consistent improvements, the performance gains over baselines are relatively modest. A more thorough analysis is needed to demonstrate the practical significance of these gains and to justify the method's effectiveness compared to the simplicity of the approach.

3. Section 3.2, which introduces the fusion functions, is somewhat hard to follow. It is unclear which of the three fusion functions (addition, multiplication, cross-attention) is primarily used in the experiments. Providing more detailed explanations and justifications for the choice of fusion functions would improve the clarity of the method.

### Questions
1. It seems that FLARE MT does not require the input in the source language during inference. Could the authors explain why this approach works effectively without the source input? Additionally, what would be the impact of feeding the source input into the MT encoder for this method?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces an adapter-based fusion technique to enhance the performance of multilingual language models on non-English languages. The proposed method improves cross-lingual transfer (XLT) with minimal additional computational cost and can leverage the hidden states of pre-trained translation models.

### Strengths
The approach demonstrates broad applicability across various models, as evidenced by experiments conducted on XLM-R, mT5, and Llama3. Additionally, the integration of adapters with cross-lingual transfer strategies makes the method cost-efficient.

### Weaknesses
Firstly, the modification to LoRA appears similar to existing methods [1, 2], and the observed improvements in XLT performance following adapter fine-tuning with representations from both source and target languages are unsurprising. According to the results presented in Table 1, the enhancements achieved by FLARE are marginal and constrained by the underlying translation model's performance, limiting its effectiveness for low-resource languages.

Secondly, the chosen baselines seem weak. For instance, X-Mixup consistently degrades the original model’s performance after fine-tuning. Moreover, the input-level fusion baseline sometimes outperforms FLARE on the NusaX dataset, and its performance on TyDiQA is not reported due to out-of-memory issues. Given that TyDiQA does not typically involve long-context scenarios, the omission of input-level fusion results for this task is problematic.

Furthermore, the manuscript requires significant improvements in clarity and presentation:

- Figure Illustrations: Figures 2 and 3 are confusing. For example, it is unclear why the target language is fed into the MT Encoder in figure 3. The proposed method essentially involves down-projecting and fusing representations from both source and target languages (whether from raw tokens or pre-trained MT encoder states) before up-projecting them to the decoder's next layer. However, the methodological descriptions are difficult to follow.

- Training Objective: The paper does not clearly specify the training objective used for updating the adapter module. It is unclear whether the module is fine-tuned using a classifier head for tasks like XNLI or if it employs a self-supervised objective such as masked language modeling, as used in XLM-R. Clarification of the training objective in Section 4.1 is necessary.

Overall, while the method shows potential, the marginal performance gains, weak baseline comparisons, and lack of clarity in methodology and presentation diminish the paper’s contribution.

### Questions
Can you give more intuition/explanation for why FLARE-MT does not work on Llama3 model (I see a drop in both XNLI and NusaX)?

Comparing FLARE-MT with FLARE, it seems that their improvement over different task/language is different. But it seems that for high-resource languages, directly using discrete token (FLARE) works the best. The paper mentioned that for language like Urdu, FLARE-MT gives more improvement. But at the same time, Llama3 + FLARE seems to work much better than FLARE-MT on these languages (see Table 6 ur column). Can you give some explanation for why FLARE-MT works or does not work in these scenarios?

### Soundness
2

### Presentation
2

### Contribution
2
