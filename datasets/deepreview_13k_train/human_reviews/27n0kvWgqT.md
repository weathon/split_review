# Parameter-Efficient Fine-Tuning of State Space Models

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Deep State Space Models (SSMs), such as Mamba~\citep{gu2023mamba}, have emerged as powerful tools for language modeling, offering high performance with efficient inference and linear scaling in sequence length. 
However, the application of parameter-efficient fine-tuning (PEFT) methods to SSM-based models remains largely unexplored. 
This paper aims to systematically study two key questions: (i) How do existing PEFT methods perform on SSM-based models? (ii) Which modules are most effective for fine-tuning?
We conduct an empirical benchmark of four basic PEFT methods on SSM-based models.
Our findings reveal that prompt-based methods (e.g., prefix-tuning) are no longer effective, an empirical result further supported by theoretical analysis. 
In contrast, LoRA remains effective for SSM-based models. 
We further investigate the optimal application of LoRA within these models, demonstrating both theoretically and experimentally that applying LoRA to linear projection matrices without modifying SSM modules yields the best results, as LoRA is not effective at tuning SSM modules. 
To further improve performance, we introduce LoRA with Selective Dimension tuning (SDLoRA), which selectively updates certain channels and states on SSM modules while applying LoRA to linear projection matrices. 
Extensive experimental results show that this approach outperforms standard LoRA.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents the first study on the performance of PEFT methods applied to SSM-based models. Specifically, prompt-based and parameter-based methods are involved. With theoretical analysis and extensive experiments, LoRA tends to achieve better performance. To further improve the performance, this paper introduces SDLoRA, which selectively updates certain channels and states on SSM modules while applying LoRA to linear projection matrices.

### Strengths
1.	Reasonable theoretical analysis and comprehensive experiments.
2.	The introduced SDLoRA is novel and effective.
3.	Through extensive experiments, the findings in this paper is useful and inspired.

### Weaknesses
1.	The speed of SDLoRA is nor reported.
2.	Experimental results on larger datasets are needed.

### Questions
1.	During the process of selective dimension tuning, the authors select the target channels and states based on magnitude, any other metrics have been tried?
2.	Will SDLoRA's training speed be slower compared to vanilla LoRA? How much slower will it be?
3.	What is the accuracy of SDLoRA on a larger data set, such as ImageNet?
4.	Some other advanced parameter-efficient tuning method like DoRA [1] can be adapted to Mamba? or the proposed SDLoRA can be adapted to Jamba?

[1] DoRA: Weight-Decomposed Low-Rank Adaptation

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
The paper explores parameter-efficient fine-tuning (PEFT) methods for deep State Space Models (SSMs), especially in the context of language modeling tasks. It investigates the effectiveness of various PEFT methods, such as prompt-based prefix-tuning and Low-Rank Adaptation (LoRA), applied to SSM architectures like Mamba. A new variant called SDLoRA (Selective Dimension LoRA) is proposed in this paper to selectively update channels and states in the SSM modules, aiming to enhance the fine-tuning performance while reducing parameters. The results indicate that SDLoRA outperforms conventional LoRA when fine-tuning SSM-based models.

### Strengths
(1) Efficiency and Scalability: By focusing on selective parameter updates, the SDLoRA method enhances computational efficiency, which is crucial for large-scale models. Experimental results show that SDLoRA consistently outperforms traditional LoRA across several benchmarks, proving its efficacy in SSM architectures.
(2) Adaptability: The proposed SDLoRA method demonstrates adaptability across multiple tasks, including NLP tasks and vision tasks

### Weaknesses
(1) Limited Applicability Beyond SSMs: The focus on SSMs means SDLoRA may not generalize well to non-SSM architectures or hybrid models such as Transformer models or Transformer-SSM combinations. Its broader applicability to other architectures remains untested.
(2) Parameter Selection: The dimension selection process in SDLoRA relies on parameter magnitudes, which may not be optimal and could benefit from a more sophisticated selection algorithm. And what if the magnitude of each channel changes during the fine-tuning stage?

### Questions
See the weaknesses

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
3

### Summary
The paper aims to explore the application of LoRA to SSMs. It explores different adapter types as well as different ways of how to apply them to the SSM block. The paper additionally includes theoretical results to justify their choices.

### Strengths
The paper is looking at something which definitely needs to be studied, as it is not a foregone conclusion that adapters, prompt tuning, etc... will have the same benefits for SSMs as they do for transformers. A detailed study understanding the different tradeoffs brought on by the SSM architecture should be explored.

The paper has a good mix of theoretical and empirical analysis.

### Weaknesses
The paper, to me, does not have enough substance. It needs either more detailed theoretical results, which result in some innovation or needs more empirical results which help the community understand how different adapters perform with transformers vs SSMs.

Here are some specifics:
1. Mamba2 is not included in any of the results, the paper should be updated to look at this architecture as well
2. The theoretical analysis is largely only for the S4 block, its not clear to me the conclusions would extend to S6, and aren't convincing to me for that reason.
3. The empirical results are lacking. The SDLoRA module is slightly different application of the standard LoRA block, essentially targeting different layers within the block instead of new a design. Also only two adapters are compared within this work. To have a true empirical study of this, many more experiments need to be conducted, even in the presence of theoretical results.

I think the paper might be more interesting if it were to do something like the following:
- Compare many adapters in a standardized for Transformers, Mamba1, and Mamba2
- Isolate differences in which adapters perform well for each class of model
- See if these insights give rise to a new adapter design specifically for this model class
- Draw theoretical results to try to explain why certain adapters perform differently than in Transformers

The current structure doesn't feel as though it is contributing much

### Questions
Have you looked at all into Hybrid Architectures?

### Soundness
2

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
This paper presents a systematic study on the application of parameter-efficient fine-tuning (PEFT) methods to Deep State Space Models (SSMs). The paper reveals that prompt-based methods are less effective for SSMs, while LoRA remains effective. The authors further propose SDLoRA, which selectively updates certain channels and states on SSM modules while applying LoRA to linear projection matrices, demonstrating improved performance over standard LoRA.

### Strengths
The paper systematically analyzes how existing PEFT methods perform on SSM-based models and which modules are most effective for fine-tuning, revealing that prompt-based methods like prefix-tuning are no longer effective. Additionally, it shows that applying LoRA to linear projection matrices without modifying SSM modules yields the best results. The paper further introduces SDLoRA, a novel approach to parameter-efficient fine-tuning (PEFT) for SSMs. This method's innovativeness lies in its selective dimension updating strategy within SSM modules. The document also references various datasets used for evaluating the proposed methods, and the clarity of the paper is generally good.

### Weaknesses
1. While the paper presents a novel approach for parameter-efficient fine-tuning SSMs, the innovation seems to be more incremental than groundbreaking. Specifically, the selective dimension updating strategy, while effective, appears to be a relatively minor modification to the existing LoRA framework. The core idea of applying low-rank adaptation to SSMs is not entirely new, and the proposed method primarily focuses on optimizing the selection of dimensions for updating. A more detailed comparison with other potential optimization strategies for dimension selection would strengthen the claim of novelty.

2. The paper lacks a detailed analysis of the computational overhead from the selective dimension tuning process. This is crucial to understanding the trade-offs between parameter reduction and computational efficiency in SDLoRA. While the paper mentions that SDLoRA selectively updates certain channels and states, it does not provide a quantitative analysis of the computational cost involved in identifying these channels and states during the fine-tuning process. For instance, how does the overhead of dimension selection scale with model size and dataset complexity? What is the proportion of time spent on dimension selection versus actual parameter updates? These details are critical for assessing the practicality of SDLoRA.

3. The paper would benefit from a more detailed analysis of SDLORA with hybrid models that combine SSMs and Transformers, as these models are becoming increasingly popular and have shown promise in various domains. The current evaluation focuses primarily on pure SSM architectures. However, given the growing interest in hybrid models like Jamba, it is important to understand how SDLoRA performs in such architectures. For example, how does SDLoRA interact with the attention mechanism in Transformers? Does it offer similar benefits when applied to the SSM components within a hybrid model? A more comprehensive evaluation on hybrid models would significantly enhance the paper's impact.

### Questions
1. Could the authors comment on how SDLoRA benefit to hybrid models that combine SSMs and Transformers? 
2. On Mamba-130M, the authors use GLUE and DART benchmarks, while on Mamba-1.4B, they use SAMSum and Spider benchmarks. Could the authors elaborate on the considerations behind this benchmark selection strategy?
3. In Table 4, SDLoRA outperforms Full Fine-Tuning. Was this outcome expected, and if so, could the authors provide insights into why this might be the case? Additionally, have the authors considered conducting experiments on more challenging visual tasks, such as Imagenet-1k, to further validate the effectiveness of SDLoRA?

### Soundness
3

### Presentation
3

### Contribution
3
