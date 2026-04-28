# LLaCA: Multimodal Large Language Continual Assistant

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Instruction tuning guides the Multimodal Large Language Models (MLLMs) in aligning different modalities by designing text instructions, which seems to be an essential technique to enhance the capabilities and controllability of foundation models. In this framework, Multimodal Continual Instruction Tuning (MCIT) is adopted to continually instruct MLLMs to follow human intent in sequential datasets. We observe existing gradient update would heavily destroy the tuning performance on previous datasets and the zero-shot ability during continual instruction tuning. Exponential Moving Average (EMA) update policy owns the ability to trace previous parameters, which can aid in decreasing forgetting. However, its stable balance weight cannot deal with the ever-changing datasets, leading to the out-of-balance between plasticity and stability of MLLMs. In this paper, we propose a method called Multimodal \textbf{\underline{L}}arge \textbf{\underline{La}}nguage \textbf{C}ontinual \textbf{\underline{A}}ssistant (LLaCA) to address the challenge. Starting from the trade-off prerequisite and EMA update, we propose the plasticity and stability ideal condition. Based on Taylor expansion in the loss function, we find the optimal balance weight is basically according to the gradient information and previous parameters. We automatically determine the balance weight and significantly improve the performance. Through comprehensive experiments on LLaVA-1.5 in a continual visual-question-answering benchmark, compared with baseline, our approach not only highly improves anti-forgetting ability (with reducing forgetting from 22.67 to 2.68), but also significantly promotes continual tuning performance (with increasing average accuracy from 41.31 to 61.89). Our code will be published soon.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the challenge of catastrophic forgetting in MCIT. While existing methods like EMA help keep prior knowledge, their fixed weights cannot adapt to evolving datasets. To address this, the authors introduce a novel framework, LLaCA. By deriving an optimal balance weight through Taylor expansion and the Lagrange multiplier method, LLaCA dynamically adjusts EMA weights, reducing memory and computation costs. Experimental results demonstrate that LLaCA achieves significant enhancements compared to baseline methods, highlighting its effectiveness in continual instruction tuning.

### Strengths
1. The paper is generally well-written and structured, followed by the motivation and explanation.
2. The model can be easily applied across a wide range of fine-tuning methods.
3. The model achieves good results compared to baseline methods, with only a modest increase in training time.

### Weaknesses
 1. In the second equation of Eq(3), $\theta_{t}^*$ represents the parameters after training on the first $t-1$ datasets, and 
$\theta_{t}^*$ represents the parameters after training on t datasets. When tuning on a new dataset, parameter updates are necessary; however, preserving performance on previous datasets does not require keeping parameters unchanged. I think it's better to maintain consistent loss values rather than preserving the parameters themselves.
2. The paper introduces the L1-Norm to approximate $\beta_t$. However, in line 291, the authors state that the L1-norm demonstrates exceptional performance without providing an explanation or presenting empirical results to support this claim.
3. While the paper states that it addresses continual learning in MLLMs, the proposed method does not leverage any modality-specific capabilities, such as distinct features for the feature encoder and the LLM. There's a question of whether $\beta_t$ should be calculated to balance across different modalities.
4. This method is applicable to LLMs without any modifications, and catastrophic forgetting in LLMs has been a well-studied area. The problem is not novel. Recent methods like [1] and [2] also address reducing catastrophic forgetting.
5. The paper does not compare its approach with SOTA methods for mitigating catastrophic forgetting in MLLMs, such as [3]. Most of the baselines used are designed for LLMs.

### Questions
1. The paper presents a method for dynamically updating the EMA weight. However, it only compares results using a stable weight of 0.99 to show the method's effectiveness. I suggest adding additional results, such as those using other static weights or weight decay, to provide a more comprehensive evaluation.
2. The writing could be polished for clarity. For example, some detailed explanations could be moved out of the main text into the Appendix, such as the content on line 166 and Equation (4). Additionally, Section 4.4 is somewhat redundant and could be streamlined.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Instruction tuning is currently a very hot topic, as it guides the Multimodal Large Language Models (MLLMs) in aligning different modalities by designing text instructions. In this framework, Multimodal Continual Instruction Tuning (MCIT) is adopted to continually instruct MLLMs to follow human intent in sequential datasets.

### Strengths
1.	Authors introduce a novel framework LLaCA for Multimodal Continual Instruction Tuning (MCIT) based on Exponential Moving Average (EMA) update policy.
2.	LLaCA overcomes the disadvantage of previous MCIT methods that require a great amount of trainable parameters, achieving parameter-efficiency during training.
3.	LLaCA exhibits good performance on various QA datasets and lowest forgetting score with both two different instruction types.

### Weaknesses
1.	While LLaCA outperforms several baselines, LLaCA is only evaluated on QA tasks (ScienceQA, TextVQA, GQA, VizWiz, VQAv2, OCRVQA), covering perception, recognition, OCR, and visual reasoning capabilities of MLLMs. More tasks such as Visual Entailment (VE) and classic classification (CIFAR100, MNIST) could be considered as a part of performance evaluation to further validate the effectiveness of LLaCA.

2.	LLaCA performs well with LoRA, which is remarkable. However, the performance of LLaCA with different PEFT methods such as Prompt-tuning [ref1] and Adapter could also be explored and included. The inherent differences between the different PEFT methods need to be highlighted and further discussed.

3.	All experiments conducted in the paper are on a single LLaVA-1.5 architecture. Suggestion: more backbone models, including Mini-GPT4 [ref2], OpenFlamingo [ref3] could be employed for more comprehensive studies of LLaCA.

4.	Discussion on Optimization Analysis such as Attention Activation Pattern Analysis [ref4] and Loss Landscape [ref5] could be beneficial for investigating why LLaCA holds superior performance compared to the other baselines.

### Questions
Please see the Weaknesses.

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
5

### Summary
The paper proposes the Multimodal Large Language Continual Assistant (LLaCA), a method designed to improve the continual instruction tuning of MLLMs. LLaCA focuses on mitigating catastrophic forgetting when fine-tuning MLLMs with new instructions. The method employs a dynamic EMA strategy to balance retaining old knowledge while learning new information. Experimental results show that the approach improves both anti-forgetting and continual tuning performance compared to baseline methods.

### Strengths
1. The paper provides detailed mathematical formulations and theoretical derivations.
2. The method demonstrates strong performance compared to the baselines, showing significant improvements in reducing catastrophic forgetting and enhancing continual learning.
3. Compared to basic LoRA fine-tuning, LLaCA adds slight extra computational cost, highlighting its efficiency.

### Weaknesses
1. LLaCA appears to be more aligned with general Continual Learning (CL) methods and lacks specific adaptations for Multimodal Continual Instruction Tuning (MCIT), such as addressing the interaction between multiple modalities and managing diverse instruction types across sequential tasks. The paper primarily focuses on the EMA update strategy and dynamically computed $\beta$, but it does not sufficiently address the unique challenges of MCIT. Furthermore, the specific advantages of applying LLaCA in the MCIT context, such as how it enhances multimodal learning, need to be clarified.

2. The experimental setup generally follows the CoIN [1] benchmark but omits the Referring Expression Comprehension (RefCoCo) and Image Classification (ImageNet) datasets without explanation, focusing solely on the Image Question Answering task. For multimodal large language models (MLLMs), these tasks do not differ fundamentally in format from Image Question Answering. Their exclusion raises concerns about the model's performance on these tasks. Including them would provide a more complete evaluation.

### Questions
1. As mentioned in Weakness 2, this paper omits 2 tasks from CoIN, so directly copying the full fine-tuning results from CoIN is incorrect. The authors should reproduce the experiment themselves.
2. In Section 5.1, the authors mention that having "ten kinds of instruction templates" (Instruction Type 2) is more challenging. However, in continual learning, different instructions can serve as implicit task identifiers, helping MLLMs find relevant knowledge for specific tasks.
3. The subsection "Multimodal Continual Instruction Tuning Definition" in Section 2 appears to focus more on problem formulation than related work. Moving it to a more suitable section could improve the paper's overall clarity.
4. The "checkpoints" mentioned in Figure 3 and Algorithm 1 are unclear. If checkpoints are being saved, there should be corresponding loading operations. Could the authors clarify this process?
5. The framework caption in Figure 3 could benefit from more detailed explanations of each module and process to improve clarity and help readers better understand the methodology.
6. There are inconsistencies in the implementation details: Appendix A.8 mentions experiments on 8 NVIDIA A100 GPUs, while Table 3 reports training on 8 A6000 GPUs. Could the authors clarify this discrepancy?
7. The term "baseline" is used throughout the paper, but it is unclear whether it consistently refers to LoRA fine-tuning or other methods. Could the authors clarify what "baseline" refers to, particularly in the tables? It would also be helpful to compare the method with stronger baselines like PGP instead of just LoRA (e.g., Table 4).
8. The paper provides detailed results for seen tasks (Appendix A.5), but results for unseen tasks are missing, despite the discussion of zero-shot performance in Section 5.3. Including these results would clarify how training on certain tasks affects zero-shot performance and explain the improvements over the baseline and original LLaVA-v1.5.
9. The paper cites many arXiv preprints, some of which have formal publications. It would be better to reference the peer-reviewed versions where available.
10. The numbering of multi-line equations representing the same derivation in the appendix is inconsistent (e.g., Eqs. (20)-(21) and (23)-(25)). Using a single equation number for each derivation would be clearer.
    
    **[Reference]**
    
    [1] Chen C, Zhu J, Luo X, et al. CoIN: A Benchmark of Continual Instruction Tuning for Multimodal Large Language Model. arXiv preprint arXiv:2403.08350, 2024.

### Soundness
3

### Presentation
3

### Contribution
3
