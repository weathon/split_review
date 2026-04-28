# One-for-All Few-Shot Anomaly Detection via Instance-Induced Prompt Learning

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 8, 6, 6

## Abstract
Anomaly detection methods under the 'one-for-all' paradigm aim to develop a unified model capable of detecting anomalies across multiple classes. However, these approaches typically require a large number of normal samples for model training, which may not always be feasible in practice. Few-shot anomaly detection methods can address scenarios with limited data but often require a tailored model for each class, struggling within the 'one-for-one' paradigm. In this paper, we first proposed the one-for-all few-shot anomaly detection method with the assistance of vision-language model. Different from previous CLIP-based methods learning fix prompts for each class, our method learn a class-shared prompt generator to adaptively generate suitable prompt for each instance. The prompt generator is trained by aligning the prompts with the visual space and utilizing guidance from general textual descriptions of normality and abnormality. Furthermore, we address the mismatch problem of the memory bank within one-for-all paradigm. Extensive experimental results on MVTec and VisA demonstrate the superiority of our method in few-shot anomaly detection task under the one-for-all paradigm.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a novel anomaly detection challenge: multi-class few-shot anomaly detection (AD). The authors examine the current few-shot AD methods using image-text models, such as WinCLIP and PromptAD, and identify the key limitations when applied to multi-class few-shot AD tasks. In response, they propose an instance-specific prompt generator that enhances the prompt's capacity to identify both anomalous and normal regions while mitigating issues that arise from shared prompts. Additionally, the paper introduces a multi-model prompt training strategy to strengthen model training and modifies the memory bank approach for multi-class tasks by proposing a class-aware memory bank.

### Strengths
1.The authors have innovatively proposed a new detection task that meets the practical industrial needs. They tested numerous outstanding anomaly detection algorithms on this task.
2.The proposed anomaly detection algorithm performs well in multi-class anomaly detection within few-shot scenarios. This method incorporates the capabilities of several currently popular large models. The proposed prompt learning strategy is innovative.

### Weaknesses
1. The paper contains several issues that affect its clarity and focus. The introduction covers too broad a range of topics and fails to highlight the core theme of the article. Additionally, Figure 1 does not fully and clearly illustrate the methodology of this paper, especially the Guidance of Prompt Learning section. It also fails to adequately represent the complex visual guidance process described in Section 3.2.1. Furthermore, there is a grammatical error with the second 'S's in line 203 of the paper.
2. The method contains too many modules, and the ablation experiments are insufficient to demonstrate whether the certain modules  contribute to the final experimental results, especially in the Prompt Generator Ablation part. The existing ablation experiments do not clearly show whether the projection network and cross-attention are truly useful. The method uses too many loss functions, and the analysis in the ablation experiments is not accurate enough. For example, the role of Synthetize Visual Features is not clearly stated.
3. AnomalyClip and InCTRL are representative works in the same field but this paper does not compare their performance in the experiments section.

### Questions
Please kindly refer to the weakness.

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
3

### Summary
This study proposes an instance-specific prompt generator and a category-aware memory bank aligned with a new one-for-all paradigm in few-shot anomaly detection.

### Strengths
This study proposes a novel prompt generation method, utilizing a class-aware memory bank to store visual features by class and extract normal and abnormal features tailored to each instance. As a result, it achieved the highest performance in the new one-for-all task.

### Weaknesses
 - In the overall performance comparison table supporting the proposed methodology, the performance of "one-for-all" and "one-for-one" is identical, yet no interpretation is provided for this outcome.
- In Figure 1, the representation of P is omitted.
- The meaning of the output values of the newly applied Q-Former in this study is not explained. Specifically, it is unclear how the Q-Former's output tokens are processed and what information they encode before being used to construct prompts.
- In Equation 12, there is an undefined loss term. The loss terms \(\tilde{\mathcal{L}}^n_f\) and \(\tilde{\mathcal{L}}^a_f\) are not defined, making it difficult to understand the complete loss function and its implications.
- In Table 4, it is essential to confirm whether variables outside the experimental modules were well controlled. Given that the highest performance was achieved by adding the M1 and M2 modules, it seems possible that other modules were incorporated at intermediate stages, potentially confounding the ablation study.
- Table 5 lacks definitions and contains errors in the loss expressions, making comparison and evaluation challenging. Specifically, the loss terms are not clearly defined, and there appears to be a typo in the loss expression.
- In Table 6, the AUROC performance for VisA at the image level differs, indicating a need to verify whether the experiments were conducted accurately.

### Questions
1. Given that both normal and anomalous object tokens 𝑂 are output from the same MLP, please clarify whether they utilize the same learnable token. Additionally, if the same token is used, it would be helpful to explain how the MLP architecture enables the generation of distinct normal and anomalous tokens.
2. To validate the claim that Gaussian noise is not required, consider including an experiment comparing the proposed method to a version that incorporates Gaussian noise. Such a comparison could illustrate the impact of Gaussian noise on performance and provide evidence for this design choice.
3. In Table 4, the shift from OVB to CAMV in the Memory Bank module when adding M2 could explain some performance improvements. To better understand each module's role, an additional ablation study that isolates the effects of the Prompt Generator and the Class-aware Memory Bank would clarify their individual contributions to performance in the one-for-all task.
4. The identical performance results in Tables 1 and 2 between the class-wise training in the one-for-one setting and the one-for-all setting are intriguing. A more detailed explanation of how the method differs across these settings, as well as a discussion on why the performance remains the same, would provide valuable insights into the implications for the method's contributions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel anomaly detection methodology for industrial applications in a one-for-all categories paradigm. It uses prompt tuning and contrastive learning to pull training images and normal prompts closer together and multi-level fusion to create pseudo-anomalies which are pulled together with the anomaly prompts.

### Strengths
The methodology appears to be sound and introduces several steps.

The experimentation is comprehensive and the results show consistent improvement over baselines.

The paper is mostly well written and clear.

### Weaknesses
Please see questions

### Questions
1. On line 218, how are the selected subset of F for prompt learning chosen? 

2. It is not clear to me why building the category-aware memory bank using image patch tokens as well as category tokens is necessarily better than the memory banks used in previous methods. Is it the case that query samples from one category were often being matched to memory bank items from other categories? This seems unlikely. 

3. How does the additional training and prompt tuning affect computation complexity / runtime compared with the base methods?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors propose a novel "One-for-All Few-Shot" anomaly detection method, aimed at addressing the challenge of few-shot anomaly detection. Compared to traditional "One-for-One" approaches, the authors design a class-shared prompt generator that utilizes vision-language models (VLMs) to generate instance-specific prompts, improving the model's adaptability in few-shot scenarios. The method is trained to capture normality and abnormality in both visual and textual modality and introduces a category-aware memory bank to resolve the memory mismatch issue within the "One-for-All" paradigm.

### Strengths
1. This paper designs a novel task.
2. The proposed method is innovative and practical.
3. The experimental results show that the proposed method has achieved excellent performance on the two datasets.

### Weaknesses
This paper has some drawbacks and the authors can consider improving the paper's quality from the following perspectives:

1. **Grammar Mistakes and Spelling Errors**, such as:

(1) In the Abstract, it has "...fix prompts for each class, our method **learn** a class-shared prompt generator...". Here, "learn" should be in the third person singular form and changed to "...fix prompts for each class, our method **learns** a class-shared prompt generator...".

(2) In line 236, it has "we propose to encourage the alignment between a group of patches **an** the embedding of one prompt token". It seems that "an" should be replaced with "and" to ensure the correctness of the sentence.

2. **Confused Content**, such as:

In the abstract, the expression that 'We address the **mismatch problem** of the memory bank within one-for-all paradigm' is relatively ambiguous, and the specific definition of 'mismatch problem' is not clearly explained in **Sec.3 Methods**. The authors may provide more explanations about this term.

3. **Differences from others**:

Although the comparisons with PromptAD and other methods have been mentioned, there is a lack of detailed comprehensive analysis. More comparative content can be added to illustrate the specific advantages of the proposed method. For example, the author can add an independent section in the Appendix to illustrate WinCLIP/PromptAD has limitations in some specific scenarios, and how the proposed method outperforms them under these scenarios.

### Questions
1. **More Experimental Details**:

The impact of semantic-level alignment loss has not been extensively discussed in **Table 5**. The authors may add more experimental results to demonstrate the effectiveness of this specific loss.

2. **More Quantitative Analysis**:

The performance impact of adopting Q-Former and instance-specific prompt generator is still unexplored. For example, an extra experiment or performance analysis can be added to demonstrate the specific contribution of Q-Former to the method. My concern is that the original ViT and Q-Former are unaligned and frozen during the training, without pre-training, e.g. representation learning stage in BLIP2, they may not own the ability to align the text feature with the visual feature. Additionally, due to the CLIP having been pre-trained to align the two modality features, why the authors did not use it? In other words, the advantages of the proposed architecture are not obvious in the paper when compared with other frameworks.

3. **More theoretical analysis**:

Although the experimental results demonstrate the effectiveness of the method, the theoretical analysis is somewhat insufficient. For example, in the Prompt Generator Ablation and Loss Ablation, the authors can add one sentence to analyze and generalize why the proposed module is effective.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents a new anomaly detection problem: multi-class few-shot anomaly detection (AD). The authors analyze current image-text model based few-shot anomaly detection methods such as WinCLIP, PromptAD et al. have problems in multi-class few-shot AD tasks and propose an instance-specific prompt generator, which not only improves the ability of prompt to capture abnormal regions and normal regions, but also prevents the problems caused by prompt sharing. 
In addition, this paper proposes a multi-model prompt training strategy for model training, and improves the memory bank strategy for multi-category tasks to propose a class-aware memory bank.

### Strengths
1. This paper discusses a new and practical task.
2. The method has some novelty.
3. The experimental results show that the performance of this paper is very superior.

### Weaknesses
There are some problems in the organization of the paper, 1) the introduction is too redundant and not concise enough, and it is difficult to get the core views of the authors. 2) Some details of the method section are not clear enough and some parts are not reflected in Figure 1

### Questions
major
1. I would like the authors to briefly introduce the core insights of the paper.
2. There are many modules in the method part, and more ablation experiments are needed to demonstrate the contribution of each module, especially the instance-specific prompt generator module, in which the Projection Network and Cross Attention need to be ablated. In addition, the two losses of Synthetic Visual Guidance for Anomalous Prompt also require separate ablation experiments.
minor
3. 236 “group of patches an the embedding” “an” seems to be a misspelling
4. Table 5, I couldn't find “L_c”, if the author meant “L_s”.

### Soundness
3

### Presentation
2

### Contribution
3
