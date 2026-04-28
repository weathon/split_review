# Mosaic-IT: Free Compositional Data Augmentation Improves Instruction Tuning

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Finetuning large language models with a variety of instruction-response pairs has enhanced their capability to understand and follow instructions. Current instruction tuning primarily relies on teacher models or human intervention to generate and refine the instructions and responses for training, which are costly, non-sustainable, and may lack diversity. In this paper, we introduce Mosaic Instruction Tuning (Mosaic-IT), a human/model-free compositional data augmentation method that can efficiently create rich and diverse augmentations from existing instruction tuning data to enhance the LLMs. Mosaic-IT randomly concatenates multiple instruction data into one and trains the model to produce the corresponding responses with predefined higher-level meta-instructions to strengthen its multi-step instruction-following and format-following skills. Our extensive evaluations demonstrate a superior performance and training efficiency of Mosaic-IT, which achieves consistent performance improvements over various benchmarks and a $80\%$ reduction in training costs compared with original instruction tuning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper argues that acquiring instruction-tuning data from a teacher model or humans is resource-intensive. In addition, it suggests that the complexity of single instruction can be limited for many instances which limits the instruction-following capabilities. To address this, the authors propose Mosaic-IT, a data augmentation strategy where the model is trained to follow multiple instructions via a meta instruction. Specifically, the paper considers multiple mosaic strategies including primary, maskout, permute, and format. Finally, the paper shows good improvements across models, instruction-tuning datasets and evaluation methods.

### Strengths
- The paper proposes an interesting way to stack multiple instructions to teach more complex instruction-following capabilities to them. It is encouraging that the authors consider many ways in which the instruction-response data can be stacked.
- The paper performs a diverse set of experiments across many base language models, instruction-tuning datasets, and evaluation methods. 
- The paper performs several ablation studies to understand the usefulness of different experimental components.  The paper further analyzes the usefulness of the method using the smoothness of the learning dynamics.

### Weaknesses
 - Motivation: how much of instruction tuning data acquisition is a bottleneck? There are several papers that show that a small number of instruction tuning data is enough to enable strong instruction-following capabilities. With the rise of powerful small language models (e.g., 4o-mini, Gemini-Flash, Haiku), getting a lot of instruction tuning data is not a bottleneck in terms of resources. In addition, I do not understand the connection between instruction tuning and Dense and Aligned Captions paper from the VL literature. The authors should rethink the motivation in the introduction. It is unclear whether this strategy scales with data i.e., having more Mosaic-IT data beneficial or not. 
- The absolute performance on Alpaca2-LC seems too low. According to the original leaderboard [1], the AlpacaEval LC performance of Alpaca 7B (w/ LLama-1) is 5.9%, and Vicuna is 6.3%. However, the paper indicates that the baseline performance with much stronger base models (Mistral and LLaMA-3-8B) and datasets (Alpaca-GPT4, Wizard-70K, Vicuna, Magpie) is quite low. This makes me wonder if the models have been instruction tuned properly or not.
- Table 2 suggests that baseline methods have better 2-round MT-Bench scores than Mosaic-IT. Shouldn’t the second round MT-Bench scores improve with Mosaic-IT augmentation? Mosaic-IT shares similarity with multi-turn chats in the sense that both require answering multiple instructions in the given context.

### Questions
Mentioned in the weakness

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
5

### Summary
This paper studies instruction-tuning methods in LLMs by augmenting training data with three different templates, Format, Permute, and Maskout strategies. These techniques may reduce the over-fitting or memorization. The proposed method, Mosaic-IT, achieves consistent performance improvements over various benchmarks.

### Strengths
- [S1] The experimental results seems to be solid by demonstrating consistent improvement against a no-augmentation baseline.

### Weaknesses
 - [W1] The techniques to prevent over-fitting and memorization by preparing various formatted templates and order randomization has been well studied and widely known approach; such as pioneering work of Instruction Tuning (Wei et al., 2021, Flan-T5 paper). From that time, the input/output pairs for instruction tuning are not always fixed and dynamically randomized. Considering these literatures, I think this paper is a kind of re-invention of those techniques, and the technical novelty and contribution seems to be limited.
- [W2] Figure 3 is unclear to me. Could you clarify what is a “mixture count”? While “Fix” strategy is adopted, the number of “mixture count” seems to be distributed among 1-10 (not fixed?). Why do you use Uniform as a default despite its not the best performance?
- [W3] In Figure 4, we can see that Mosaic-iT accelerates its training, but the performance at the convergence seems to be the same or even worse than the baselines, which is contradictory to your main results that improves the performance against baselines. Could you clarify the relationship between the convergence performance and the logic of performance improvement.
- [W4] In Table 4 (a) (ablation of Mosaic-IT), you tried Format, Permute, Maskout, and Permute/Maskedout. Why didn’t you try all the combinations?
Also, your best performance came from Maskout, but the adopted variant for Table 1 seems Permute/Maskedout. Why didn’t you use Maskout only?

### Questions
See the weakness above.

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
5

### Summary
This paper introduces a data augmentation method, Mosaic-IT, for instruction-tuning large language models (LLMs) without human or model dependency. Unlike traditional approaches that rely on human intervention or teacher models to generate instruction-response pairs, the proposed method works by combining existing instructions into composite multi-instruction samples. They propose four ways to do the composition - primary, format, permute and maskout. By doing so, the paper shows that LLMs trained with this method develop a higher level of instruction-following capacity and format adherence. The proposed method, which reduces training time by approximately 80%, holds promise as a scalable solution for instruction tuning without extensive resource requirements.

### Strengths
1. The paper is well-structured, progressing logically from the motivation behind Mosaic-IT to the methodology, followed by experiments and results. Each section builds on the last, making the paper easy to follow and understand.
2. The figures do a great job of clearly summarizing the idea. 
3. The experiments are comprehensive for the scope the paper setup - they have explored different datasets and model families and explored different sampling procedures for the composition

### Weaknesses
1. The paper lacks a theoretical basis for why random concatenation should improve instruction-following abilities; structured or semantically grouped concatenations could offer further insights. Specifically, the paper does not explore the potential for interference or synergistic effects between instructions when concatenated randomly. A more detailed analysis of how different types of instruction combinations affect the model's learning process would be beneficial. For instance, concatenating instructions with similar underlying tasks might lead to better generalization than combining unrelated instructions. The current approach treats all instructions as equally compatible for concatenation, which may not be the case in practice.
2. Randomly concatenated instructions may introduce noise, potentially impacting training stability. An analysis of this effect on model perplexity would strengthen the work. The paper should investigate whether the random concatenation leads to a higher variance in training loss or if it causes the model to overfit to the concatenated structure. Furthermore, it would be useful to examine the impact of different concatenation lengths on training stability and final performance. The current analysis lacks a quantitative assessment of the noise introduced by the random concatenation process.

### Questions
Please refer to the weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes Mosaic-IT, a data augmentation method for the instruction following. It proposes Primary and advanced mosaic strategies. It also includes format, permute, and mark out.

### Strengths
The paper deploys the method into several evaluation benchmarks and different model structures. It also includes several analyses to study the method's aspects.

### Weaknesses
1.	The core problem of the proposed method is the lack of a detailed explanation of the core reasons for the proposed method. It does not provide justifiable and experimental explanations for the effectiveness of the proposed method. The primary motivation of the proposed method should be further cleared here. 
2.	From the experiments, it seems that the proposed method does not improve the multi-turn data for MT-Bench. Would there be any explanations for this?
3.	Many instruction-following methods and literatures focus on data augmentation. There are no comparisons with those baselines. In addition, how would mask methods be different from the other dropout, etc. methods?

### Questions
1. Would there be any justifiable and experimental explanations for demonstrating the method's effectiveness?

2. Would it be possible to show more experiments on multi-turn benchmarks?

3. For the comparison baselines, would it be possible to add more baselines related to data augmentation for instruction turning?

### Soundness
2

### Presentation
2

### Contribution
2
