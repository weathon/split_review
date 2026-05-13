# Mechanistic Behavior Editing of Language Models

- Decision: Reject
- Scores: 5, 6, 3, 6

## Abstract
Large Language Models trained on web-scale text acquire language generation abilities that can solve a wide range of tasks, particularly when task knowledge is refined into the generative prior using in-context examples. However, spurious features learned from noisy data hinder their generalizability. Supervised finetuning can introduce task specificity, but introduce data inefficiency. Prior studies indicate that (i) noisy neural circuitries coexist with generalizable ones within LLMs, and (ii) finetuning typically enhances (or suppresses) existing abilities without introducing newer ones. Building upon these, we propose \shortname, a novel method for task adaptation. \shortname intervenes in the neural circuitries using learnable rotation matrices that are optimized using Bayesian Optimization, on labelled samples in the order of standard few-shot prompting examples. Experiments on multiple classification and generation tasks using LLMs of varying sizes reveal the efficacy of \shortname, improving upon both zero- as well as few-shot performance, with average improvements (across models and tasks) of 23.81\% and 11.15\%, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper investigates the challenge of adapting pre-trained Large Language Models (LLMs) to downstream tasks, building on the established understanding that LLMs possess both generalizable and spurious neural circuits, and that fine-tuning often suppresses existing circuits rather than introducing new ones. The core research question posed is: is it possible to directly edit the model behavior via mechanistic interventions in a generalizable manner? To address this, the authors propose TaRot (Task-aware Rotation of token association), a novel method presented as an alternative to instruction tuning, aiming to bypass the need for extensive prompt engineering or computationally expensive full finetuning. TaRot achieves this by applying learned rotation matrices to the output of attention heads in the early layers of the LLM, where pretrained knowledge is believed to reside. These rotations are optimized using Bayesian optimization with a small number of labeled examples. The authors demonstrate that TaRot improves performance on a variety of classification and generation tasks on different LLMs.

### Strengths
Steering pretrained LLMs with lightweight and interpretable intervention is of massive importance.

### Weaknesses
The central claim of TaRot being a "tuning-free" method achieving effects comparable to finetuning requires further scrutiny.  While TaRot avoids modifying the original LLM weights directly, it introduces and optimizes a set of parameters (rotation matrices) for each task.  This approach parallels other parameter-efficient adaptation methods like adapter-based techniques, which also modify model behavior without full finetuning, albeit in a gradient-based manner.  Thus, the distinction of TaRot as truly "tuning-free" is questionable.

Furthermore, the use of the term "mechanistic intervention" feels somewhat weak in this context. Previous mechanistic intervention approaches typically target specific tasks or capabilities within the model, offering valuable insights and interpretability.  In contrast, TaRot’s aim for general applicability across tasks comes at the cost of reduced interpretability, as it does not focus on isolating or explaining specific neural mechanisms.  A direct comparison with gradient-based methods, in terms of both performance and computational cost, is also lacking.  It's unclear whether TaRot's Bayesian optimization of rotation parameters offers a significant advantage over the efficiency of gradient-based updates in techniques like adapters.

Finally, the paper's emphasis on the "gradient-free" nature of TaRot oversimplifies the optimization process. While the original LLM weights remain fixed, the Bayesian optimization of rotation matrices still involves an iterative search procedure guided by performance feedback.  This indirect use of gradients, through the evaluation of the objective function, means TaRot is not strictly gradient-free. A more nuanced discussion of the computational costs and trade-offs compared to fully gradient-based methods would strengthen the paper.

To summarize, previous "mechanistic invervention" approaches usually have good interpretability since they target specific tasks or capabilities. TaRot is supposed to be general so it does not add much interpretability compared to other methods and it is unknown if it performs better than other gradient-based approaches.

### Questions
N/A

### Soundness
3

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
This paper introduces TaRot, a novel method for task adaptation in Large Language Models (LLMs). TaRot intervenes in the neural circuitries using learnable rotation matrices optimized with Bayesian Optimization on few labeled samples. The method aims to improve the generalizability of LLMs by minimizing the effects of undesired memorizations from noisy data. Experiments on various classification and generation tasks demonstrate TaRot's efficacy in enhancing both zero-shot and few-shot performance across different LLMs. The paper also analyzes the changes in neural representation introduced by TaRot, providing insights into its mechanism of action.

### Strengths
1. TaRot offers a new perspective on task adaptation by directly editing model behavior through mechanistic interventions, which is a significant departure from traditional SFT.
2. The method is highly data-efficient and designed to work with LLMs of varying sizes, demonstrating its scalability and versatility.
3. The paper provides extensive experimental results, showing consistent improvements in performance across multiple tasks and models.

### Weaknesses
1. While the method is innovative, the complexity of understanding and implementing rotation matrices in neural circuits might be a barrier for some researchers and practitioners.
2. TaRot's effectiveness is dependent on the quality of pretraining, which means it may not perform well if the base model has significant limitations. This also limits its applicability in scenarios where models need to be fine-tuned for new domains.
3. The paper could benefit from a more detailed comparison with SFT and other model-editing methods such as [1] and [2]. The current results do not clearly show the superiority of TaRot over SFT, especially considering the additional complexity introduced by the rotation matrices. The improvements are not consistent across tasks, and in some cases, SFT appears to perform better.

### Questions
1. Will you open-source the code? With the code, can we easily obtain the optimized model by only providing the original model and data, like SFT?
2. How does TaRot ensure that the rotation matrices do not disrupt other valuable associations?
3. Could you demonstrate how TaRot performs with models of varying pretraining quality, or to clarify the limitations of TaRot in domain adaptation scenarios?
4. How does the selection of 6-20 training samples used for training affect the effectiveness?
5. Regarding data selection.
- What are the criteria that the authors used to select the current datasets? 
- Are there any specific tasks or types of data where TaRot has been observed to underperform? 
- How does the choice of downstream tasks affect the effectiveness of TaRot in comparison to SFT?
6. The current results seem to only demonstrate the effectiveness of TaRot as an alternative to SFT, so why not compare the results with SFT or few-shot SFT?
7. I believe that  additional experimental results on larger models are needed; otherwise, even SFT won't incur much cost and may be easier to use.
8. Are there any application points for TaRot in instruction-tuning?

Typos: line 083 'pertraining'

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents TaRot, a method of task adaption for large language models (LLMs). TaRot applies rotation matrices to attention head outputs, aiming to align token associations for desired outcomes in zero- and few-shot settings.

### Strengths
1. This work proposes a new mechanistic intervention method for model adaptation without extensive fine-tuning, highlighting its potential significance.

2. The methodology is well-designed, combining mathematical rigor with empirical validation across diverse tasks.

3. This work demonstrates improvement across multiple LLMs on classification and generation tasks.

4. The paper clearly articulates the TaRot concept and its implications, offering comprehensive descriptions of experiments and results.

### Weaknesses
1. There is a lack of comprehensive comparison among different editing methods proposed in prior works. Relying on a single method based on singular values may not provide sufficient insight.

2. Current LLMs often exceed 8 billion parameters such as Llama 3 70B, yet this work does not include experiments on models larger than 8B.

3. The proposed method does not outperform the baseline on the primary metric shown in Table 3.

4. The impact of rotation editing on other previously learned knowledge in LLMs is not evaluated.

### Questions
1. What does M represent in Equation 9?

2. Since the rotation matrices apply to any input vectors, how can we ensure that they do not negatively affect performance on tasks that were neither trained nor tested?

3. The relevance of Figure 3 to the claims of this work is unclear. The proposed method and the baseline appear to follow very similar distributions. Could the authors provide further clarification?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes TaRot, a method for editing language models. It uses learnable rotation matrices with Bayesian optimization on few shot examples. TaRot is data efficient and demonstrate improvements upon traditional zero-shot and few-shot learning on several classification and generation tasks.

### Strengths
- TaRot is an innovative method that is theoretically grounded. 
- Strong empirical results demonstrating the benefit of the proposed approach.
- The paper is well written.

### Weaknesses
Strong results are observed on simple classification tasks but on generation (positive reviews, detoxification) tasks the results are mixed.

### Questions
It would be great to have more analysis/experiments on how the number of available labeled examples and base model size change the behavior of the proposed methods.

### Soundness
3

### Presentation
3

### Contribution
3
