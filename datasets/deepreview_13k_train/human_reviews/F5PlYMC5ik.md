# LOIRE: LifelOng learning on Incremental data via pre-trained language model gRowth Efficiently

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Large-scale pre-trained language models (PLMs) require significant computational resources to train from scratch on large volumes of data. But in the real world, emerging data from diverse sources may not be initially available for pre-training. Recent studies on lifelong learning have tried to solve this problem by exploring the use of model growth techniques to effectively incorporate new knowledge without the need for complete re-training. However, model growth approaches utilized have issues with growth operators that do not ensure strict function preservation or growth schedules that only include a few growth dimensions, reducing lifelong learning's effect. Furthermore, existing approaches often assume that emerging data has the same distribution as pre-training data, causing catastrophic forgetting of previously acquired knowledge. To address the aforementioned issues, we introduce LOIRE, a framework for lifelong learning that enables PLMs to effectively grow their capacity using incremental data. LOIRE employs growth operators for all feasible dimensions and a growth schedule to generate the optimal expansion sequence in the field of lifelong learning. Specifically, we present a novel plug-in layer growth operator with residual connections that skip the newly added layer during initial training while ensuring function preservation. We additionally propose an iterative distillation strategy for LOIRE that allows an intermediate model in the growth stages to switch between being a student and a teacher, reducing catastrophic forgetting during growth. Experiments show that LOIRE can reduce computational expenses by an average of 29.22\% while retaining equivalent or better downstream performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces LOIRE, a lifelong learning framework for pre-trained language models that enables efficient adaptation to incremental data without full retraining. LOIRE tackles catastrophic forgetting and model growth challenges using a plug-in layer growth operator with residual connections for function preservation, a multi-dimensional growth schedule for optimal model expansion, and an iterative distillation strategy to retain prior knowledge. Tested on multiple benchmarks, LOIRE shows strong performance in reducing computational costs and maintaining task accuracy across evolving domains.

### Strengths
- Rigorous Experimental Validation: The paper describes extensive experiments conducted across various domains using multiple datasets. It also includes ablation studies that examine the effects of growth operators and schedules.
- Comprehensive Methodology: LOIRE uses a multi-dimensional growth schedule (covering dimensions like hidden size, FFN, MHA, and layers) combined with iterative distillation. This methodology is applied to manage catastrophic forgetting and model adaptation across evolving data.

### Weaknesses
 - Limited Scalability Testing: The experiments are limited to relatively small models (up to 114M parameters), which may not fully demonstrate LOIRE’s scalability to larger PLMs, commonly used in industry. Further exploration with larger models could strengthen confidence in its applicability for high-parameter models.
- Although LOIRE’s function preservation claims are theoretically sound, empirical validation shows minor deviations. Further exploration into these deviations might strengthen the reliability of the proposed growth operators, especially in dynamic adaptation scenarios.

### Questions
- Have you experimented with different initialization methods for the extended parts of the model, such as the Hidden Dimension, FFN, or MHA, beyond the current method you’re using? If so, what impact did these alternatives have on model performance, function preservation, and adaptation to new data?
- Did you calculate perplexity (PPL) separately for each previous domain as the model grows, rather than averaging across them? Measuring PPL individually for each domain could provide clearer insights into any knowledge degradation specific to earlier domains.
- Did you measure LOIRE’s efficiency—such as FLOPs, training time, or memory usage—compared specifically to continual learning baselines like ELLE? Since efficiency is a key claim, it would be helpful to understand how LOIRE performs against ELLE and other lifelong learning frameworks on these metrics.

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
1

### Summary
This paper introduces LOIRE, a new framework, introduces comprehensive growth operators and a strategic schedule to expand PLMs effectively while preserving function. It also uses iterative distillation, allowing the model to alternate between teacher and student roles to reduce forgetting. LOIRE demonstrates a 29.22% reduction in computational costs with maintained or improved performance.

### Strengths
The proposed method seems novel and sound, and the extensive experiments and ablation studies demonstrate the efficacy of the method from multiple dimensions.

### Weaknesses
I don't see any major weakness of this paper, but that may be due to my minimal knowledge of this topic.

### Questions
NA

### Soundness
3

### Presentation
3

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
This paper proposes a framework called LOIRE to address the challenges of lifelong learning for pretrained language models (PLMs). The motivation comes from the need to improve the adaptability of PLMs to new, emerging data without requiring complete retraining. In real-world applications, data often evolves over time, with new domains and tasks emerge that were not part of the original pretraining data.  PLMs generally struggle with this scenario because they are typically trained once on a large dataset and then fine-tuned for specific tasks and this leads to two major problems: 1) Catastrophic Forgetting where the models are fine-tuned on new data, they tend to forget previously learned information and 2) Computational Inefficiency where retraining LLMs from scratch every time when new data emerges is computationally expensive and impractical. LOIRE addresses these challenges in lifelong learning by introducing growth operators, schedules, and distillation strategies.

### Strengths
LOIRE proposes several approaches to overcome the limitations given in the summary. These approaches are the strength of this work IMHO. 

First one is layer growth operator that replicates selected layers and inserts them between existing layers with residual connections. The residual connections allow the newly added layers to be skipped during initial training, ensuring that the model's function is preserved. By ensuring that new layers do not interfere with the model's initial behavior, LOIRE enables smoother transitions when expanding model capacity. This is particularly important in lifelong learning scenarios where models must adapt to new data without forgetting previously acquired knowledge.

Second one is multi-dimensional growth operators that expands model capacity across multiple dimensions, such as hidden states, feed-forward networks, multi-head attention, and layers. By considering multiple dimensions, LOIRE can better adapt its expansion strategy to the specific needs of different tasks or datasets.

The main proposal is the growth schedule that determines when and where to expand the model structure across multiple stages. The schedule is designed to optimize the sequence of growth operations, ensuring that the model grows efficiently while minimizing computational costs. The results shows the significant computational savings -- an average reduction of 29.22% in expenses while maintaining or improving task performance compared to baseline methods.

And finally the iterative distillation warmup to mitigate catastrophic forgetting during model growth where intermediate models generated during growth stages switch between being students and teachers. The iterative distillation warmup strategy helps retain knowledge from previous stages while adapting to new data, ensuring that the model remains effective across both old and new tasks. This technique enhances LOIRE's ability to handle incremental data without sacrificing performance on previously learned tasks.

### Weaknesses
 - Although these approaches are individually strong, all these process is pretty complex and i have doubts how practical is the proposed method overall in real world applications. Implementing multi-dimensional growth operators and optimizing growth schedules requires careful tuning and may be challenging for practitioners who are not familiar with these techniques. The added complexity could limit the accessibility of LOIRE for users who need simpler or more straightforward solutions for lifelong learning. It would greatly help if the authors can address these concerns. 

- My main concern is the scalability of the proposed method. While LOIRE improves computational efficiency by reducing expenses by an average of 29.22%, scaling up this approach to very large models or datasets might still pose challenges. Lifelong learning frameworks need to be scalable to handle ever-growing datasets and increasingly large models. LOIRE's reliance on iterative distillation and multi-stage growth could still become computationally expensive as models grow larger. Further research may be needed to ensure that LOIRE can scale effectively without resulting in excessive costs. If the authors can provide computational complexity analyses for larger models, or conduct experiments with models of varying sizes to show how performance and efficiency scale, that would help to address this concern.

- I also have concerns about the increasing model parameters. Table-1 shows that model parameters increases significantly for each task --> M1:27.59M, M2:62.25M, M3: 71.69M, M4: 71:69M, M5: 104.78M. In reality we may observe hundreds or thousands of new tasks and if we want our model to perform well on all these how big the model will end up? That seems like a bottleneck for scalability of the approach. Can you explain what is the behaviour of parameter growth?

### Questions
As I mentioned in weaknesses, I have concerns about the scalability of the approach. Can you please explain how scalable the proposed method? 

How well LOIRE handles significant shifts in data distribution? -- In real-world applications, new data often comes from domains that are very different from what was seen during pretraining or earlier stages of fine-tuning. It is unclear how well LOIRE would perform in such scenarios where there are drastic shifts in data distribution.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a method for lifelong learning of foundation models that relies on a growth strategy to allow updating of multiple dimensions of a Transformer architecture (multi-head attention, FFN, layer and hidden dimensions). Growth operators are proposed for each of these dimensions. A growth schedule, which is controlled by a hyper-parameter, is also proposed based on previous findings that "growing the layers and heads in later stages and having a larger hidden dimension in earlier stages can lead to better model performance". Experiments are run over 5 benchmark datasets, on both GPT and BERT-like architectures with increasing number of parameters. Experimental results include analyses on computation cost.

### Strengths
Originality: The paper is original in the sense that it proposes a new growth strategy for foundation models which consists of growing multiple dimensions of these Transformer-based models. It presents 

Quality: The quality of the paper is good. There is explanation of existing concepts of new concepts, using tools such as text, diagrams and equations. There are no major points where quality needs to be 

Clarity: The paper is written clearly, the concepts are presented in a reasonable flow. Experiments are also mostly clear.

Significance: There seems to be some significance of the paper from the experimental results presented against other architectures such as GPT.

### Weaknesses
 - Significance of experiments: According to Table 1, each of the M_x steps is related to applying one of the growth operators proposed in the paper. However, the common setting in lifelong learning is grouping data(sets) into "tasks", which are learned sequentially. How is this lifelong learning idea applied in this paper?

- Significance of experiments: Similar to the previous point, in lifelong/continual learning typically measuring "forgetting" gives useful information about the "interference" experienced by the system because of learning sequentially. I do not see this reflected in this lifelong learning paper at all. 

- Significance of experiments: There is no further justification as to why the particular growth schedule presented in Table 1 was selected. Are there other possible schedules? What would the results be under these schedules?

### Questions
- It was not entirely clear to me why there are GPT-like baselines but not BERT-like baselines to be compared against the proposed method (specifically in Table 1). Please clarify.

- In the experiments, it was not entirely clear to me how are datasets divided into n number of tasks. From Table 1, it seems that each "x" is a growth operator, so how is this related with grouping datasets into tasks? Or are all datasets used all-together from the beginning?

- Did you test all possible schedules beyond the growth schedule presented in Table 1? What are the results like?

### Soundness
3

### Presentation
3

### Contribution
3
