# MoTE: Mixture of Task Experts for Embedding Models

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 3, 5

## Abstract
Dense embeddings are essential for Retrieval-Augmented Generation (RAG), search, classification, and clustering systems. Recent methods improve dense embeddings by enriching them with instructions that incorporate downstream task information, enabling a single model to generate task-specific embedding spaces. However, we empirically show that requiring all tasks to share the same model parameters imposes significant representational limitations. To address these challenges, we introduce Mixture of Task Experts (MoTE), a novel transformer block designed for embedding architectures. MoTE employs dedicated parameter sets tailored to the unique requirements of each task and is paired with a task-aware training framework to improve representation quality. Experiments on 56 datasets spanning $7$ tasks demonstrate that MoTE outperforms instruction-conditioned models, achieving, on average, $1.62$ higher NDCG@10 on retrieval datasets, $1.54$ higher MAP on re-ranking datasets, and a $0.65$ improvement in overall performance. Notably, these gains are achieved without altering inference-time information, training data, inference speed, or number of active parameters.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a novel approach for embedding models called Mixture of Task Experts (MoTE) that incorporates task-specific MLP blocks within the transformer architecture. During training, different tasks are directed to task-specific blocks, allow the model to generate different embeddings for the same query based on the task context.
This adds new parameters (the task-specific blocks) corresponding to the number of tasks during training. To reduce the parameter count, they apply WAVE (Weight Average of Vector Experts) where they average the weights of the task specific blocks.

### Strengths
The embeddings of two different queries may need to be close or far apart depending on the task. Their approach to generating task-specific embeddings enables the optimization of distinct parameters for each task, promoting better task specialization.

### Weaknesses
1. Adding a new ML block after every other transformer layer will add significant memory requirement. It would be beneficial to explore optimization strategies to reduce this, such as adding ML blocks only in the topmost layers. Furthermore, the current approach does not consider the potential for parameter redundancy across different task-specific blocks. It is possible that many tasks might benefit from similar, or even identical, transformations, leading to inefficient use of parameters. A more nuanced approach to sharing or adapting parameters across tasks could lead to a more memory-efficient model without sacrificing performance.
2. The authors show that using the WAVE approach to reduce the gpu requirement retains 98.2% average performance. However, the more important metric is how much of the improvement is retained. Table 6 indicates that WAVE does not provide significant performance improvement. The focus on average performance retention obscures the fact that the absolute performance gains achieved by the full MoTE model are not well preserved by the WAVE approximation. It is crucial to analyze the performance of individual tasks to understand where the performance drops are most significant.
3. There should be an analysis of GPU memory increment as the number of tasks during training increases. The paper lacks a clear analysis of how the memory footprint scales with the number of tasks. This is a critical practical concern, as the number of tasks can vary significantly in real-world applications. Without a detailed analysis, it is difficult to assess the feasibility of this approach for large-scale applications.
4. From Table 3, task-aware training does not seem to improvement performance for most tasks. The reported improvements are marginal for many tasks, raising questions about the practical utility of the proposed approach. A more detailed analysis of the tasks where the approach fails to provide improvement is needed to understand its limitations.

Minor:
1. There are duplicate lines in Section 3.3.
2. Page 5 line 216: texty-type should be text-type

### Questions
N/A

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
4

### Summary
This paper presents a novel approach for task-specific fine-tuning of embedding models in a mixture-of-experts framework, termed Mixture of Task Experts (MoTE). The MoTE model generates task-conditioned embeddings through dedicated parameter sets for each task, allowing for specialized representations tailored to specific downstream requirements. To address the increased memory demands associated with this approach, the authors introduce Weight Average of Vector Experts (WAVE), which mitigates the computational overhead of MoTE by efficiently managing memory without sacrificing performance. This dual approach overcomes the limitations of single-expert models applied across diverse tasks.

To evaluate its effectiveness, the proposed method was tested on seven in-scope and out-of-scope tasks across 56 datasets, demonstrating notable performance gains due to the MoTE architecture.

### Strengths
- This work presents innovative methods for generating task-aware embeddings, building on and extending previous research.
- It introduces a novel approach that leverages task-specific hyperparameters to create specialized embeddings while effectively managing the memory consumption challenges of task-conditioned models.
- The method demonstrates practical applicability by addressing the limitations of using a single expert across multiple downstream tasks, showing promise for real-world implementations.
- The paper is clearly written, with well-chosen examples and motivating illustrations that enhance comprehension.
- It includes a robust experimental setup, testing across seven tasks (both in-scope and out-of-scope) with a total of 56 datasets.
- A thorough ablation study and in-depth analysis strengthen the insights derived from the experimental results.

### Weaknesses
 - This work represents an incremental advancement in mixture-of-expert models, focusing on generating task-aware embeddings for downstream tasks and addressing limitations of prior approaches.
- The approach shows only marginal gains for out-of-scope tasks, such as in pair similarity. For task-aware applications like Classification, Clustering, and Retrieval, in general, they share semantic or latent spaces across them. However, the applicability of the proposed method does not generalize effectively to out-of-scope tasks and domain?
For example, in Table 2, the proposed approach yields only slight improvements on semantic textual similarity (STS) tasks, highlighting limited performance gains in out-of-scope settings.

### Questions
NA

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper tries to introduce the MOE architecture into the general embedding models and provide different hyperparameters for each task expert to improve performance. Meanwhile, the Weight Average of Vector Experts is obtained by merging the trained experts, which reduces the overall number of parameters and keeps the performance almost equal to that before merging.

### Strengths
1. The improvements presented in this paper are straightforward, with expected gains from the MOE architecture and Weight Averaging.
2. The ablation experiments are sufficient, covering performance variations across different settings.
3. The final model maintains the backbone parameter count, ensuring a fair comparison.

### Weaknesses
1. The work lacks innovation. It primarily enhances model performance by applying two established strategies (MOE and Weight Averaging) to generic representations without offering new insights. The application of MOE, while novel in the context of embedding models, does not fundamentally alter the underlying representation learning process. The paper fails to demonstrate a novel mechanism or theoretical insight derived from this combination. The gains, while present, are largely expected from the application of these techniques, rather than from a novel interaction or discovery.
2. The paper centres on technical implementation but (1) does not commit to open-sourcing the code and (2) provides a very brief methodology, omitting details such as the implementation of the Task-Aware Training Strategy. The lack of code availability hinders reproducibility and further investigation by the community. The methodology section lacks crucial details, such as the specific loss functions used for each expert, the precise nature of the task-aware training, and the exact architecture of the MOE layer, making it difficult to assess the novelty and impact of the proposed approach. The description of the training process is also too high-level, lacking specifics on the optimization algorithm, learning rate schedules, and other crucial hyperparameters.
3. The paper appears incomplete, falling short of the 10-page limit and lacking a thorough methodology section. Grammar and citation issues also affect readability. The brevity of the paper, especially the methodology, makes it difficult to fully understand the proposed approach. The lack of detail makes it hard to assess the validity and generalizability of the results. The grammatical errors and citation inconsistencies detract from the overall clarity and professionalism of the paper.
4. Weight Averaging is a model merging method, yet no background on model merging is provided, making the work hard to follow for readers unfamiliar with this area. The paper assumes that the reader is familiar with weight averaging techniques, which is not always the case. A lack of background on model merging makes it difficult to understand the motivation and the specific implementation of the weight averaging process in this context. The paper should provide a more thorough explanation of the theoretical underpinnings and the practical implications of this technique.

### Questions
1. The performance difference between "TEM-Inst." and MoTE is minimal (less than 1% in Tables 1 and 2). However, as "TEM-Inst." results don’t appear to be from a public source and the hyperparameter search process isn’t clearly detailed, could you clarify the hyperparameter tuning efforts made to ensure a fair comparison?

2. The statement that “existing methods, ..., limits the degree of task-specialization of the final vector representation” is unclear. In Tables 1 and 2, "TEM-Inst." clearly outperforms STEM, suggesting that multi-task joint learning generally enhances performance across tasks. Thus, setting aside the results in MTEB:

(1) What evidence shows that the trained representation space is task-specialized?

(2) To what extent does the representation space differ between tasks?

(3) Why can’t instructions alone resolve this issue?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel architecture, MoTE, which allocates a dedicated set of parameters for each task to enhance dense text embeddings. MoTE offers a robust approach to improving dense text embeddings by employing a mixture of experts. This architecture, combined with a dynamic training strategy and WAVE, achieves better task specialization without intensively increasing latency or memory overhead. Experiments were conducted on the MTEB benchmark to compare MoTE with previous instruction-based embedding model training approaches and analyze the contributions of its techniques.

### Strengths
1. This paper explores the novel Mixture of Task Experts architecture for embedding models, which has the potential to effectively address the challenges posed by various retrieval tasks with differing intents.
2. It conducts numerous analytical experiments and investigates the impact of training configurations, yielding insights that may aid further research on MoTE.

### Weaknesses
1. The experiments on MTEB do not compare MoTE against mainstream retrieval models, such as E5 and BGE, nor does it provide comparisons by using training data of mainstream retrieval models, which weakens the reliability of the experimental results. The absence of these comparisons makes it difficult to assess the true performance gains of MoTE in relation to established state-of-the-art models. The paper should have included experiments using the same training data as E5 and BGE, or at least a subset, to provide a more direct and fair comparison. Without this, it's unclear whether the improvements are due to the architecture itself or simply the training data used.
2. Many analytical experiments only present results without in-depth analysis, such as in sections 4.5 and 4.6. For example, the paper presents the results of ablation studies but does not delve into the reasons behind the observed trends. A more detailed analysis should include discussions on why certain configurations perform better than others, and what the implications are for the model's learning process. The lack of such analysis limits the insights that can be drawn from these experiments.
3. The writing is relatively poor. For example, the two paragraphs in section 3.3 appear to be repetitive. The paper lacks clarity and conciseness in several sections, making it difficult to follow the authors' line of reasoning. This is particularly evident in section 3.3, where the repetition of ideas makes the text cumbersome and less impactful. The paper would benefit from a thorough revision to improve the flow and readability.

### Questions
1. Is the WAVE method introduced in section 4.7 too simplistic, merely averaging the expert layers post-training but can maintain the performance?
2. As many current MoE architectures are based on LLMs, could this approach be more suitable for retrieval models grounded on LLMs?

### Soundness
2

### Presentation
2

### Contribution
3
