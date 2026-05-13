# MiniPLM: Knowledge Distillation for Pre-training Language Models

- Decision: Accept
- Scores: 6, 8, 6, 6, 6

## Abstract
Knowledge distillation (KD) is widely used to train small, high-performing student language models (LMs) using large teacher LMs. 
While effective in fine-tuning, KD during pre-training faces challenges in efficiency, flexibility, and effectiveness. 
Existing methods either incur high computational costs due to online teacher inference, require tokenization matching between teacher and student LMs, or risk losing the difficulty and diversity of the teacher-generated training data.
To address these issues, we propose \textbf{$\name$}, a KD framework for pre-training LMs by refining the training data distribution with the teacher's knowledge.
For efficiency, $\name$ performs offline teacher LM inference, allowing KD for multiple student LMs without adding training-time costs.
For flexibility, $\name$ operates solely on the training corpus, enabling KD across model families.
For effectiveness, $\name$ leverages the differences between large and small LMs to enhance the difficulty and diversity of the training data, helping student LMs acquire versatile and sophisticated knowledge.
Extensive experiments demonstrate that $\name$ boosts the student LMs' performance on 9 widely used downstream tasks, improves the language modeling capabilities, and reduces pre-training computation. 
The benefit of $\name$ extends to large pre-training scales, evidenced by the extrapolation of the scaling curves.
Further analysis reveals that $\name$ supports KD across model families and enhances the utilization of pre-training data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies the field of language model pre-training by proposing an efficient KD framework. MINIPLM’s use of offline inference and Difference Sampling stands out as a method that balances computational efficiency and model performance improvement. The findings are well-supported by robust experiments, although the explanations and practical considerations could be more user-friendly and extensive.

### Strengths
The introduction of MINIPLM, which uses offline teacher inference and a unique Difference Sampling method, provides an innovative solution to enhance KD during pre-training. This method effectively balances computational costs and improves student language model performance.

The paper presents extensive experimental results across a variety of downstream tasks and model sizes (200M, 500M, 1.2B parameters), demonstrating the effectiveness of MINIPLM. Comparisons with various baselines show substantial improvements.

The results on computation reduction and performance scalability (e.g., 2.2x computation reduction) validate the practicality of MINIPLM for large-scale pre-training.

### Weaknesses
The explanation of Difference Sampling and its theoretical justification could be simplified or supplemented with more intuitive examples for clarity.

The requirement for teacher LM’s probabilities on pre-training corpus data may pose challenges for closed-source models or environments with limited computational resources. This could be highlighted more explicitly as a practical limitation.

The paper would benefit from a more detailed discussion on the transferability and generalizability of MINIPLM across different language models and types of downstream tasks, beyond the ones tested.

While a brief limitations section is included, expanding on potential drawbacks, such as cases where MINIPLM may underperform compared to online KD or specific model configurations where it might not be ideal, would strengthen the discussion.

### Questions
The explanation of Difference Sampling and its theoretical justification could be simplified or supplemented with more intuitive examples for clarity.

The paper should discuss in detail the limitations of the proposed method.

The transferability and generalizability of MINIPLM across different language models and types of downstream tasks should be discussed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces an approach to knowledge distillation (KD) for pretraining LLMs. The proposed method, MINILLM, reformulates the objective of KD with reverse KL divergence as a reward maximization problem, enhancing the student model's focus on the teacher model's primary knowledge modes through difference sampling. Evaluations further show the efficiency and effectiveness of this approach.

### Strengths
- This paper provides decent theoretical foundations 
- The contribution and experiments designed for this paper is very clear. 
- Evaluations demonstrate improved performance and data efficiency gained from the method. 
- The contribution of this paper is important to scenarios when data is insufficient.

### Weaknesses
Overall, I don't have many criticism toward this paper. 
- There is not enough emphasis on how much of this approach would require computational resources to perform distillation. A discussion on resource consumption, such as training time or memory usage, would help assess its practicality for real-world deployment.
- The complexity of the training process may impose challenges in reproducibility and implementation.

### Questions
Please refer to weakness.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
MiniPLM introduces a novel approach to knowledge distillation (KD) for pre-training smaller language models that addresses key challenges in efficiency, flexibility, and effectiveness. The core innovation is "Difference Sampling" - a method that intelligently refines the pre-training data distribution by comparing probabilities between a large teacher model and a small reference model. This enables efficient offline KD by selecting training instances where the teacher model shows strong confidence but the reference model struggles, indicating valuable knowledge that smaller models need to learn. Notably, MiniPLM achieves 2.2x computational savings while maintaining performance comparable to traditional KD approaches.

### Strengths
- This paper Introduces "Difference Sampling" as a novel offline KD method that fundamentally changes how knowledge is transferred.
- This paper re-computes teacher model probabilities just once, requiring only 200MB storage for 50B tokens vs 30PB for traditional methods.
- This paper shows clear computational efficiency gains (2.2x reduction for equivalent performance).
- This paper provides solid theoretical justification through Proposition 2.1 and detailed analysis of the sampling approach

### Weaknesses
 - First, the absence of teacher model (1.8B) performance metrics in Table 1 makes it difficult to gauge the effectiveness of knowledge transfer - readers cannot assess how much of the teacher's capabilities are preserved in the student models. Specifically, without the teacher's performance, it's impossible to determine if the student model is truly learning from the teacher or simply achieving a baseline level of performance.
- The paper's experimental scope is rather constrained. By focusing primarily on a 1.8B teacher model, it misses the opportunity to demonstrate effectiveness with larger, more modern models. The experiments would be more convincing if they demonstrated success with larger model gaps, such as distilling from Llama 3.1 8B to 1B on Table 1 setting. This is crucial to show the method's scalability and applicability to current large language model research.
-  While the paper introduces "Difference Sampling" as a key innovation, it doesn't thoroughly demonstrate its effectiveness through controlled experiments. The comparison with SeqKD might be not enough because SeqKD's lower performance might be attributed to the authors' implementation choice of using only 768 tokens for approximation. It is unclear if the performance difference is due to the sampling strategy itself or other implementation details. A more rigorous ablation study is needed to isolate the impact of the sampling strategy.
- Furthermore, the omission of comparisons with recent work in small language models, particularly MobileLLM and its associated baselines in the 200M/500M parameter range, leaves an important gap in understanding how MiniPLM compares to state-of-the-art approaches in efficient model training.

[MobileLLM] MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Cases

### Questions
- While the cross-model family experiments with Llama 3.1 and Mamba are interesting, they lack details about model configurations, training data, and experimental setup. Could the authors provide them?

### Soundness
3

### Presentation
3

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
This paper introduces MINIPLM, a knowledge distillation framework for pre-training language models. The key innovation is Difference Sampling, which refines the training data distribution by comparing a large teacher model with a small reference model. The framework: (1) performs offline teacher inference to avoid online KD computation overhead, (2) maintains data difficulty through reference model comparison, and (3) enables cross-family model distillation. Experiments on models from 200M to 1.2B parameters demonstrate improvements in downstream performance, language modeling capability, and computational efficiency.

### Strengths
- Well-motivated solution approach
- Elegant Difference Sampling design
- Efficient offline computation strategy
- Comprehensive experiments across model scales

### Weaknesses
 - Limited analysis of finite-sample scenarios
- Teacher model size limited to 1.8B
- Limited cross-family experiments
- Limited exploration of alternative sampling strategies
- Reference model selection criteria not fully justified

### Questions
- Can you provide theoretical justification for using log(p(x)/p_ref(x)) as the sampling metric?
- How does the method's effectiveness scale with model size differences?
- How would the method perform with larger teacher models (>10B)?
- What modifications are needed for very large scale deployment?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a method to train a small PLM using knowledge distillation from large PLM and in an offline manner instead of the existing online methods. The methods first trains a small LM from scratch on small subset of the training corpus and then a large PLM is used to perform difference sampling that samples from the large corpus the difficult samples reducing the chances of learning the patterns only from the easy portion of the dataset.

### Strengths
1. The paper uses knowledge distillation to obtain a better subset of samples for training a small PLM which is different from existing methods.

2. The paper is well written and easy to follow.

3. The paper has good experimental results as compared to the existing methods.

4. The problem taken up is an important problem in pre-training the language models.

### Weaknesses
1. The paper proposes to choose a subset of training dataset that can provide better performance of the small model using knowledge distillation but the title of the paper is ``Knowledge distillation for pre-training language models", here knowledge distillation is not being used for pretraining instead it is being used for a better subset selection from a huge corpus of data that can in turn have better pre-training of the PLMs, this makes it quite misleading.

2. In line 238 paper says that when the log term is less than zero, those instances are harmful, however, this is not true as explained in papers such as [1] where an easy sample can be predicted correctly by a smaller model while it can get wrong on a larger model due to extraction of overly distracted features. This phenomenon is termed as `overthinking' of PLMs.

3. I am not very clear how $p_{ref}$ can mimic the behavior of $q_{\theta}$, even these models can have certain differences and how MINIplm performs better than MINIllm even when MINIllm directly uses the $q_{\theta}$ distribution?

4. The method is computationally very heavy as we need three LLM model: one large model from which distillation is being performed, a smaller version trained from scratch and then training the distilled model using the existing two, which makes it complex.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
