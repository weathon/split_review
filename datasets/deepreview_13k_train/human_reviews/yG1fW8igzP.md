# Data-Augmented Phrase-Level Alignment for Mitigating Object Hallucination

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Despite their significant advancements, Multimodal Large Language Models (MLLMs) often generate factually inaccurate information, referred to as hallucination. In this work, we address object hallucinations in MLLMs, where information is generated about an object not present in the input image.  We introduce Data-augmented Phrase-level Alignment (\method), a novel loss which can be applied to instruction-tuned off-the-shelf MLLMs to mitigate hallucinations, while preserving their general vision-language capabilities. To fine-tune MLLMs with \method, we first generate a set of `hallucinated' and `correct' response pairs through generative data augmentation by selectively altering the ground-truth information of the correct responses at a phrase level. 
The \method loss is then used to train MLLMs to reduce the likelihood of hallucinated phrases compared to the correct ones.
Our thorough evaluation on various benchmarks confirms the effectiveness of \method in mitigating hallucination while retaining the out-of-the-box performance of the MLLMs on general tasks. 
For instance, MLLMs finetuned with \method, which we refer to as Hallucination Attenuated Language and Vision Assistant (\halva), improve F1 by up to $13.4\%$ on hallucination visual question-answering and reduce the hallucination rate by up to $4.2\%$ on image description tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes Data-augmented Phrase-level Alignment (DPA), a novel loss function designed to reduce object hallucinations in multimodal large language models (MLLMs) while preserving their general vision-language capabilities. By generating pairs of hallucinated and correct responses through data augmentation, DPA trains MLLMs to distinguish hallucinated phrases from correct ones. Experimental results show that MLLMs fine-tuned with DPA achieve significant improvements, reducing hallucination rates and enhancing performance on visual question-answering and image description tasks.

### Strengths
* The DPA loss function is an innovative approach that mitigates object hallucinations by targeting phrase-level distinctions, offering a focused solution for multimodal hallucination issues.

* The data augmentation method is straightforward yet effective, generating hallucinated-correct response pairs that enable the model to learn nuanced differences with minimal complexity.

* DPA demonstrates significant performance gains

### Weaknesses
The core idea of the paper is to generate correct-hallucinated data pairs through data augmentation. However, I have three questions about this process.
1. In hallucination-related datasets, object hallucination does not frequently occur, raising questions about the validity of replacing every possible object and attribute with hallucinations. Since models seldom generate such hallucinations, this augmentation strategy might introduce excessive "non-realistic" hallucination cases, leading to a mismatch between training and real-world distributions, potentially impacting the model's generalization.
2. The method’s effectiveness may be limited by the diversity of data augmentation. Since hallucinated data generation relies on a finite set of replacements, it may not fully cover the types of hallucinations that could appear in practical applications, limiting the model’s ability to handle unseen hallucinations.
3. The data augmentation strategy itself lacks independent experimental evaluation. The experiments mainly focus on improvements in model performance across different benchmarks, without assessing the augmentation strategy’s generalization effect and impact on model training stability across tasks.

### Questions
Please see the weakness part.

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
5

### Summary
This paper presents a Data-Augmented Phrase-Level Alignment (DPA) approach aimed at reducing object hallucinations in Multimodal Large Language Models (MLLMs). The method centers on generating paired “correct” and “hallucinated” responses using data augmentation, which are then used to train a phrase-level alignment loss that reduces the probability of hallucinated tokens. The authors strive to maintain the model’s overall vision-language capabilities while minimizing hallucinations. Experimental results across multiple benchmarks indicate that DPA effectively mitigates hallucinations and may even improve detailed object coverage in generated descriptions.

### Strengths
1. This paper proposes an effective alignment method that successfully mitigates object hallucinations, showing improved scores across hallucination benchmarks in both discriminative and generative tasks.
2. DPA reduces object hallucinations without impacting the overall performance on VQA tasks, achieving comparable or even higher scores on VQA benchmarks.
3. The paper provides a variety of quantitative results across multiple benchmarks, including both generative and discriminative tasks. This breadth of evaluation provides some evidence of the DPA’s effectiveness in certain contexts.

### Weaknesses
1. The DPA approach offers limited novelty beyond existing finetuning and data augmentation techniques. While phrase-level alignment is applied in a new way here, it basicly builds on existing concepts and does not significantly advance the field of hallucination mitigation research.
2. Although the results include some competitive baselines, such as HA-DPO and EOS, several relevant and recent methods are omitted. A more comprehensive comparison would strengthen the evaluation. Additionally, some detailed results for LLaVA-13B and VILA are missing, and the selection of methods across different benchmarks lacks consistency.
3. While the paper asserts that DPA preserves general vision-language capabilities, the supporting evidence is limited. A broader evaluation across diverse benchmarks would help determine whether this approach impacts overall performance.
4. The authors highlight the limitations of existing methods, noting they “require massive training data.” However, the proposed DPA also introduces additional training requirements, which suggests a tradeoff between efficiency and effectiveness.

### Questions
1. How does DPA perform on other types of hallucinations beyond object hallucination, such as attribute or location hallucinations?
2. The reported results for some baseline methods, such as VCD, differ from those in the original papers. Did you directly test VCD, or were the results extracted from their papers? If the latter, the comparison may not be entirely fair, as it mixes experimental results with reported findings from other sources.
3. This paper augments the training data with hallucinated responses by substituting terms in both open-set and closed-set cases. However, simple substitution could potentially impact fluency and grammatical accuracy. Could this approach compromise data quality and, in turn, affect model performance?

### Soundness
2

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
This paper introduces a novel method called Data-augmented Phrase-level Alignment (DPA) to mitigate object hallucinations in multimodal large language models (MLLMs) for vision-language tasks. DPA generates pairs of “hallucinated” and “correct” responses to fine-tune the model, reducing the generation of hallucinated phrases. A KL divergence regularization term is added to retain the model’s general capabilities. Experimental results demonstrate that models trained with DPA exhibit significant improvements in hallucination mitigation and maintain strong performance on general tasks across multiple benchmarks.

### Strengths
1. The writing of this paper is excellent and very detailed. The experiments are comprehensive, covering most of the popular benchmarks.

2. I really like this paper. Many works that use DPO-like methods to reduce hallucinations experience a decrease in VQA capabilities. The authors identified this issue and proposed a specialized loss to maintain the model’s performance while penalizing hallucinated phrases. Additionally, the authors validated their method separately on non-hallucination benchmarks, such as VQA-v2 and TextVQA, demonstrating its effectiveness. I believe this work makes a significant contribution to reducing hallucinations in MLLMs.

### Weaknesses
1. DPA relies on the quality of the generated “hallucinated-correct” response pairs. If these generated data lack accuracy or diversity, it may affect the model’s training effectiveness and generalization capability.
2. Although the experimental results demonstrate the effectiveness of DPA, the paper lacks a fine-grained analysis of hallucination types (such as objects, attributes, actions). Such analysis could provide a deeper understanding of the method’s performance across different types of hallucinations.

### Questions
1. VILA is also based on LLaVA-1.5 SFT. Is DPA equally effective on other architectures, such as Qwen?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose data-augmented phrase-level alignment to mitigate object hallucination in MLLMs. The method mainly involves the generation of negative hallucinated responses and phrase-level fine-tuning. The hallucination issue of models fine-tuned with the proposed method is alleviated and the general performance is maintained.

### Strengths
1. It is critical to study the issue of hallucination in MLLMs as well as the trade-off phenomenon in the mitigation of hallucination.
2. The proposed method is simple yet effective.
3. Extensive experiments verify the effectiveness of the method.

### Weaknesses
1. The motivation to mitigate hallucination at phrase level is not clearly addressed. There is no illustration on why the phrase-level loss can retain the original performance on general multimodal tasks. It seems straightforward that the constraint on the KL divergence can prevent the fine-tuned model from diverging too far. If it is the only reason, the contribution of the method is greatly weakened.

2. The explanation of Figure 2 is likely to be overclaimed. On line 260, it says "_EOS achieves a slightly lower hallucination rate_", but the figure shows that the hallucination rate of EOS is around 5.0 and that of HALVA is around 6.5. This difference is noticeable enough to me as the gap of this metric between HALVA and LLaVA-1.5 is similar. Meanwhile, Figure A right demonstrates that HALVA has a much higher F1 score on AMBER, which is natural because neither EOS nor HA-DPO is trained with Yes/No questions.

3. The presentation of results in experiments is inconsistent. The model lists are different in different tables. For instance, EOS-13B is only shown in Table 1, which makes the verification of the effectiveness less convincing.

4. There are other work mitigating hallucinaton with sub-sequence level training [1]. It is recommended to discuss the difference.

### Questions
Minors:
1. The construction of dataset is not introduced with details. Details in appendix should be at least provided via cross-reference.
2. Figure 5 right is not illustrated in the main text. I find it not easy to understand the information it's trying to convey.

### Soundness
3

### Presentation
2

### Contribution
2
