# AttnInput: Revolutionizing Pinyin Input with Context-Aware RWKV Language Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
The Pinyin Input Method Engine (IME) is widely used for inputting Chinese characters, but effectively integrating it with powerful large language models (LLMs) remains a challenge due to issues such as semantic discontinuity and inefficient training. This paper presents AttnInput, a novel approach that leverages the strengths of the RWKV language model, specifically its linear computational complexity and "infinite" context length, to enhance Pinyin IME. Our method integrates Pinyin information directly into the internal state of RWKV through a lightweight side network, effectively addressing the semantic discontinuity issue faced by previous LLM-based IMEs. Furthermore, AttnInput utilizes a pre-training strategy, significantly reducing training data and computational costs compared to previous methods. Experimental results demonstrate that AttnInput achieves state-of-the-art performance on abbreviated Pinyin input, especially as the Pinyin sequence length increases. This efficient design allows us to scale up to larger models and incorporate longer contexts, further improving accuracy and user experience.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a novel approach to improving the Pinyin Input Method Engine (IME) by leveraging the RWKV language model. AttnInput addresses the integration of Pinyin with large language models, aiming to overcome challenges like semantic discontinuity and inefficient training. The model uses a lightweight side network to enhance the RWKV model's state representations with Pinyin information, improving efficiency in both training and inference. AttnInput claims state-of-the-art performance in abbreviated Pinyin input by utilizing RWKV's linear computational complexity and infinite context length. The proposed method also reduces computational requirements compared to prior approaches like PinyinGPT-Concat. The experimental results showcase significant performance improvements, particularly with longer Pinyin sequences, while maintaining practical latency for real-world applications.

### Strengths
The paper proposes an innovative integration of a lightweight side network with the RWKV model to enhance Pinyin IMEs, utilizing RWKV's infinite context length and efficient linear computational complexity, which is novel in the context of Pinyin input. The model achieves state-of-the-art results in experiments, especially with long Pinyin sequences, demonstrating the value of integrating the Pinyin information directly into the language model state. The structure of the paper is well-organized, with detailed explanations of the model components such as RWKV6, AttnInput, ladder side-tuning, and efficient training mechanisms. The experiments are thoroughly explained, with useful visual aids like figures and tables to support the analysis. AttnInput presents a meaningful advancement in the use of large language models for Pinyin IMEs, with potential real-world applications. The reduction in computational resources and training data compared to previous methods, without compromising performance, is a substantial contribution to the field.

### Weaknesses
The experimental evaluation is primarily limited to synthetic data generated from SkyPile-150B, which may not fully reflect performance on real-world user-generated text. The model's robustness to varied and noisy input, which is common in real-world scenarios, remains unclear. Specifically, the synthetic data may not capture the nuances of user typing errors, colloquial language, and the diverse range of Pinyin input patterns that would be present in actual usage. The ablation study only tests the model without Pinyin sequences but does not explore other architectural variations, such as different side network configurations or the impact of varying the number of layers or hidden units within the side network, limiting the insights into each component's importance. Furthermore, the paper primarily compares AttnInput with the vanilla RWKV6 and PinyinGPT-Concat, lacking direct comparisons with other state-of-the-art methods like LSTM-based or Transformer-based IMEs. A more comprehensive comparison would include models such as those using attention mechanisms or other sequence-to-sequence architectures, which are commonly used in this domain, to provide a broader context for the contribution.

### Questions
Can the authors provide more detailed evaluations on real-world datasets, including user-generated Pinyin input, to validate the model's robustness to noisy and diverse input?

How does the performance of AttnInput compare when trained with fewer training steps or using smaller datasets? Does the model generalize well with reduced training resources?

Could the authors expand on the computational cost of integrating ladder side-tuning compared to other parameter-efficient fine-tuning techniques? How does this approach balance trade-offs between performance and efficiency?

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
Authors present a novel form of pinyin to Hanzi character conversion model using a RWKV model as the backbone.

### Strengths
Language technology support for pinyin is a critical field for investigation but remains niche in NLP community. Conventional wisdom would be to conduct SFT with an LLM, whereas the authors have shown that superior results can be achieved with specialized architectures. This is a suitably novel approach. Further, the use of RWKV instead of a conventional LLM is a necessary consideration of alternative technologies that goes understudied in current environment.

### Weaknesses
Several motivations of the paper are no substantiated and would benefit from citation of other works to defend. For instance, authors claim:

"However, inserting pinyin sequences disrupts the semantic flow between the prompt and target text,
poses challenges for effectively leveraging pretrained large language models, as their training objective primarily focuses on predicting the next token."

But lacks substantiation. Especially with current developments in long-context language modeling, there's no reason to suspect an attention based framework to maintain different semantic contexts despite the break in flow.

While investigation of other LLM frameworks is sorely needed in the research community, transformer-decoders are effectively the default when it comes to LLMs. Choice of RWKV in their stead would benefit from clear motivation and comparison against methods.

Use of Top-N for accuracy is an infrequent metric. Taken in combination with the lack of a numbers table and the heavy overlap between models in the Top-1 counts, the performance of the model appears questionable. This issue can be alleviated with a numeric table.

### Questions
Could you provide an appendix section on Pinyin? For non-native writers, it's difficult to follow the convention and how it overlaps with Hanzi system.

What was the motivation for using RWKV as opposed to transformer based methods and current SOTA LLM systems?

Could you substantiate the concern for semantic discontinuity in the concatenation approach?

Please provide clear accuracy numbers in support, or in lieu, of the graphs. It is difficult to evaluate if results are significant without.

### Soundness
2

### Presentation
3

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
This paper presents a modification of RWKV architecture to support pinyin input, by integrating the pinyin information in the internal state of RWKV through a lightweight network. The proposed method has minimal computational overhead, and shows better performance than other baselines especially for longer pinyin lengths.

### Strengths
- The paper addresses an important problem of adding support for pinyin method input in language models.
- The proposed method seems to perform better than other baselines, particularly on longer context lengths with P@10 and P@15 eval.
- The writing is clear overall. A few improvements (highlighted below) would further improve the clarity of the paper.

### Weaknesses
 - The vanilla RWKV seems to perform better than the proposed AttnInput for the P@1 setting (up to 9 pinyin length) and the P@5 setting (up to 6 pinyin length). 
- AttnInput is evaluated on one dataset. It should be evaluated on additional pinyin input datasets to establish the generalizability of the proposed approach.
- A comparison of the performance of AttnInput with the regular GPT baseline would be useful (similar to how it is done in the PinyinGPT paper [1]).
- Were multiple runs done (with different seeds) for the main results presented in Figure 3? If so, the error bars should be included as well.
- Minor issues:
    - Line 49: achieving -> achieve
    - Line 95 - 97: v, k and r should be defined.
    - Line 276, 286, 296: Traget -> Target
    - Line 53: , poses challenges -> and poses challenges
    - Line 80-83: This paragraph should be moved to a more relevant position.

### Questions
- While Figure 3 helps in comparing the performance trend, can the accuracy numbers be presented in a Table form as well? It would assist in quantitatively understanding the differences in performance.
- What are the potential reasons for the better performance of vanilla RWKV over the proposed approach in the P@1 setting (up to 9 pinyin length) and P@5 setting (up to 6 pinyin length)? How will this affect the practical usage of the proposed model for pinyin input?

### Soundness
3

### Presentation
2

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
This paper introduces AttnInput, a novel approach integrating Pinyin information with RWKV-6. The method combines contextual and Pinyin information with a side network, enabling more efficient training than traditional techniques. Experimental results demonstrate that AttnInput achieves state-of-the-art performance on abbreviated Pinyin input.

### Strengths
1. The paper introduces a method that employs RWKV-6 for Pinyin IMEs. RWKV, an RNN-based model, is particularly well-suited for this task.
2. The design of the side model efficiently integrates Pinyin information into the backbone model, and ladder side-tuning enables efficient training.
3. The proposed method achieves state-of-the-art performance in this task.

### Weaknesses
1. The authors demonstrate that their method is both efficient and effective for training. However, they do not provide experiments to substantiate its superiority over other Pinyin integration methods.
2. The comparison of your model with other approaches is not fair due to the inherent strengths of RWKV-6. A more appropriate comparison would involve other methods that integrate contextual and Pinyin information under the same conditions, such as comparable models.
3. The paper's presentation is unclear and lacks structure. The authors do not clearly explain the design of AttnInput, particularly the side network, nor do they describe how vanilla RWKV-6 is employed. Furthermore, the Introduction section is too brief and fails to provide an overview of the method.
4. The tables could be improved aesthetically: Table 1 exceeds the linewidth, and Table 2 would benefit from being presented in a three-line table format.

### Questions
1. As discussed in Weaknesses 1 and 2, what are the experimental results of other integration methods with RWKV-6?
2. The P@1 performance of the method is not better than the vanilla RWKV-6. Does this imply that incorporating Pinyin information merely imposes a constraint on the decoding process?
3. The authors claim that RWKV-6 was chosen for its infinite context window. However, RNN-based models also suffer performance degradation beyond their context window. Could the authors provide details on the length extrapolation capacity (i.e., performance beyond the context window) of their methods?

### Soundness
2

### Presentation
1

### Contribution
2
