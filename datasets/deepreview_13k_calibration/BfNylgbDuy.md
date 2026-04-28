# Preference-Enhanced Instruction Tuning for Machine Translation

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
Although Large Language Models (LLMs) like GPT-4 perform excellently in machine translation, their high costs and scalability make them unavailable in many scenarios. Recently, there has been increased effort to build smaller LLMs that can achieve comparable performance. However, while typical instruction tuning methods tend to directly mimic reference translations, leading to less meaningful results, recent preference optimization methods have shown improvements. Despite this, they still fail to effectively utilize crucial preference information during inference.  In this paper, we introduce Preference-Enhanced Instruction Tuning (PEIT), a novel method that explicitly incorporates preferences into both the instruction fine-tuning and the inference phase. Our extensive experiments show that PEIT not only improves translation quality but also significantly outperforms state-of-the-art preference optimization methods and instruction tuning baselines on multiple language benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes preference-enhanced instruction tuning (PEIT) for machine translation which consists of three parts:
  1. a typical generation loss function that considers in-context demonstrations during training;
  2. a DPO like loss function to consider a win-loss pair of outputs;
  3. a hidden representation-level loss that aligns a model's preference representation of the in-context example.

The paper compares the proposed method with quite a few baselines and some ablation cases by removing some part of the overall loss. Evaluated on a few languages in FLORES, the proposed method performs well especially when evaluated by the neural metric xCOMET.

### Strengths
1. The idea of making in-context preference information during fine-tuning and inference is intuitive for the approached task, machine translation, where sometimes there is no single gold translation and user-defined preference and consistency should be taken into consideration.
2. The paper experimented with a good number of baselines which are strong in the current research landscape. Overall, the results show that the PEIT method with all three losses incorporated performs pretty well.

### Weaknesses
1. I think the paper should make it clear about this paper's contribution. The proof in Sec 2.2 is the same as in (Dai et al., 2023) which is cited in the paragraph. I am not sure about the novelty of using in-context representations (even just for MT) and applying $\mathcal{L}_{ICFT}$ as these are neither defined nor cited. Please also see Question 1. Perhaps some clarifications are needed? 
2. Being able to leverage the preference information in the context/demonstration (both at training and inference) is definitely a selling point. However, I think this is not proven through the experiment design because "preference" is not equivalent to translation quality. I feel that more ablation studies are needed in addition to Sec 4.1.
    - For example, it would be nice to see inference with the same test input but using in-context examples with a different preference distribution and understand how that qualitatively affects the output translation. In addition to general-domain or news translation test sets, one simple and reasonable setup could be terminology translation.

### Questions
1. Line 190 to line 207: this part looks a bit disconnected.
    - Iines 190-196, how are those $h^{i}_{C}$ context terms obtained? What exactly is the similarity function $sim()$?
    - Also given that these are fed as context in a prompt, I am unsure how these can be disentangled.
    - Near line 201, $\mathcal{L}_{ICFT}$ is not defined.

2. What does "incomplete ablation" mean in "Compared with incomplete ablation" under Sec 3.4 Line 312?

3. Citations and software version:
    - related work on preference learning for MT [1].
    - for the xCOMET [2] and "KIWI" metrics, it would be better to provide the correct citation and perhaps footnote the exact model version.

[1] Zhu et al., 2024, https://arxiv.org/abs/2404.11288

[2] Guerreiro et al., 2023, https://arxiv.org/abs/2310.10482

### Soundness
3

### Presentation
2

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
During the inference process, the preference intentions in the prompt may not align with the training data of the model, which will affect the overall effectiveness of the model. To address this issue, this paper introduces Preference-Enhanced Instruction Tuning, a method that integrates preferences into both the fine-tuning and inference stages. This approach improves translation quality and outperforms existing preference optimization methods on multilingual benchmarks.

### Strengths
1. The experimental results presented in the paper demonstrate that PEIT achieves better translation quality and alignment preformence.  
2. The paper theoretically establishes the effectiveness of ICL in addressing the identification of preference intentions.

### Weaknesses
 1. The proof of ICL's effectiveness presented in the paper mainly derives from Dai et al. (2023), which raises concerns about the novelty of your paper.
2. The term $L_{ICFT}$ on page 4 lacks clear definition or explanation, which may hinder understanding of the proposed method.
3. The definition of the concept of "preference intention" in the article is vague, affecting the clarity of the paper's arguments. Furthermore, the article does not provide detailed information on how to determine the preference intentions of samples in the dataset.
4. The experiments appear to be conducted within a single domain or distribution, indicating that the similarity of preferences between the training and testing datasets is consistent. This seems insufficient to validate the scenario mentioned in the introduction, where the preferences in the inference prompts do not align with the training data.
5. There is a writing error: in the seventh line of the first paragraph of the introduction, a citation is incorrectly marked as “?”.

### Questions
1. How does the paper categorize samples in the dataset into subsets that contain different preference intentions?  
2. During the inference process, is the retrieval corpus still derived from the training set? If so, how does this method's performance get affected when the preference intentions in the prompt are not sufficiently similar to those in the training data?  
3. In the inference process, what is the specific $k$ value of top-$k$? Does the value of $k$ impact performance? Additionally, more comprehensive details on other experimental settings, such as learning rate, are needed.  
4. In the section 4.1 titled “Different preferences representations of context,” could you provide a more detailed description of the experimental setup? Did you select similar samples at different levels of contextual similarity for each of the 100 sample points?

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
This paper proposes PEIT, which improves the quality of machine translation by incorporating preference learning into instruction tuning and inference. The authors suggest that PEIT can do better than existing tuning methods such as Contrastive Preference Optimization (CPO). PEIT demonstrates improved BLEU and XCOMET scores.

### Strengths
1. Theoretically demonstrated the proposed method can help the paradox of fitting, allowing a single model to achieve the same loss lower bound as a multi-model setup.
2. The experimental results demonstrated superior performance than other competitors, such as CPO, DPO, etc.

### Weaknesses
1. Lacks lots of the details, which makes the results not convincing enough. For example:
  - training details of other baselines, such as line 268, by "we have made a specific design for the DPO training process ...", the details are not clear to readers.
  - training details and performance of the retriever, I believe this would greatly impact the final translation performance. Specifically, the paper lacks details on how the retriever is trained, including the training data construction, training steps, batch size, and any constraints during the LLM training process. It is also unclear how the embedding similarity is calculated (e.g., average across all words, average pooling, or max pooling). The absence of these details makes it difficult to reproduce the results. Furthermore, the performance of the retriever itself is not evaluated, which is crucial to understand its impact on the overall translation performance.
2. Performance.
Actually, I tried to calculate the average BLEU and XCOMET score across languages, for example Table 1. There's no significant differences of BLEU and xCOMET score between methods. This might not be considered significant. [1]
3. Lack of baselines such as [2]
4. I would appreciate if various sized models/ training data could be involved.

### Questions
Please see the weaknesses.
1. The details
2. Why the performance gain is not consistent across languages.

### Soundness
2

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
In this study, the authors present Preference-Enhanced Instruction Tuning (PEIT), a novel approach that explicitly integrates preferences into both the instruction fine-tuning and inference phases. Experimental results highlight the effectiveness of PEIT.

### Strengths
1. The empirical results clearly demonstrate the effectiveness of the proposed PEIT.

### Weaknesses
1. This paper is not well-written and is hard to follow. For instance, some concepts are not well-defined at their first use. $D$ is mentioned for the first time at line 126 but is defined at line 173, where $k$, referring to the number of distributions, is not explicitly defined in this paper, unless I missed it. Furthermore, in my opinion, sections 2.1 and 2.2 are unnecessary and disconnected from other parts of this work. They do not help in understanding the idea of this work.

2. This paper is not self-contained. In the abstract, the authors mention that PEIT explicitly incorporates preferences into both the fine-tuning and inference phases. However, the authors did not explain how PEIT is used in the inference stage.

3. This paper presents minimal novelty. If I understand this work correctly, there are three components in the training objective. $L_{ICL}$ is the standard training loss used for supervised fine-tuning, $L_{prefer}$ is the same as the CPO loss, and $L_{context}$ is highly similar to the contrastive loss as presented in SimCSE[1] and SimCLR[2]. The use of these components in a combined loss function, while potentially effective, does not represent a significant conceptual leap.

4. There are some presentation issues. Table 3, Figure 2, Figure 3, and Table 4 are not referred to in the text, which makes the paper hard to follow.

### Questions
1. What are $C^{+}$ and $C^{-}$? As shown in the equation at line 183, both $y_w$ and $y_l$ are conditioned on the same context $C_i$.
2. What is the similarity in $L_{context}$?
3. What is $L_{ICFT}$ at line 202?

### Soundness
2

### Presentation
1

### Contribution
1
