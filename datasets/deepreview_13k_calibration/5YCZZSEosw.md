# Let Large Language Models Find the Data to Train Themselves

- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 3, 6, 6, 3

## Abstract
The current iterative development process for large language models (LLMs) is heavily data-centric, relying on human researchers and engineers to manually analyze model performance and determine what data to acquire for further training. However, this human-supervised approach is costly and may fail to identify optimal training signals. Its scalability is further limited as models become increasingly capable and may eventually exceed human intelligence. To address these issues, we propose an automated framework that enables models to autonomously discover and strategically acquire the most valuable training data to enhance their performance. It establishes a self-improving framework where models can invoke APIs to crawl and/or generate tailored datasets from various resources and environments, and retrain themselves. The data selection decisions are shaped by reinforcement feedback signals that reward performance gains while penalizing computational overhead. This formulation incentivizes models to develop self-knowledge about their strengths and areas for improvement in order to efficiently select training data. Empirical results demonstrate that LLMs operating within our framework are able to autonomously and strategically acquire valuable training data to enhance their performance across a variety of skills in 1,000 diverse in-house test tasks and three public benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
Currently, LLM developers manually analyze model errors and engineer training datasets (be it through human labels, or synthetically) to enhance model performance across pre-training, instruction tuning, and preference learning stages. This approach is costly, error-prone, heavily reliant on developer expertise, and lacks scalability. To address these limitations, this paper introduces the **Active Data Search (ADS)** framework, where an LLM assesses its own strengths and weaknesses for a given task and autonomously collects relevant training data to improve itself.

At the core of ADS is an LLM-driven optimizer that, when given a target task (grounded by a few guiding questions), evaluates the capabilities of the primary LLM (referred to as the policy LLM) for the task and dynamically calls different data retrieval and generation APIs to collect relevant data for improvement. This data can then be used to fine-tune the policy LLM for the target task or enhance it via in-context prompt augmentation (as implemented in this paper). Since LLMs typically are not designed for this autonomous data collection task, ADS first trains this optimizer offline with reinforcement learning to balance the reward and cost associated with obtaining new data.

The paper employs three simple data collection APIs: (a) information retrieval from Wikipedia, (b) demonstration generation powered by an LLM, and (c) question-answering using an LLM. Trained on the MagPie dataset, the optimizer effectively learns to use these APIs to acquire relevant data, leading to improved performance on an internal test set and on 3 additional public benchmarks (AlpacaEval, MT-Bench, and Arena-Hard) across two different LLMs, at times matching the performance of larger LLMs.

### Strengths
1. The paper tackles the important challenge of gathering optimal data to enhance LLM performance for a given task.
2. The proposed framing, where LLMs become self-aware of their strengths and weaknesses to identify optimal data for self-improvement, is compelling. This framing has significant implications, not only for advancing the next generation of state-of-the-art LLMs but also for democratizing AI by empowering non-experts to tailor LLMs to their specific needs.
3. The proposed ADS method of framing diverse data collection techniques as API/Tool calls and training an optimizer using DPO to dynamically select the most effective data collection API calls for a given task, is innovative and powerful.
4. The paper’s related work section is well-structured, effectively positioning the authors' contributions within the context of prior research.
5. Experimental evaluations demonstrate substantial improvements over the baseline Qwen-2-7b-instruct model across several public benchmarks.

### Weaknesses
The core weaknesses of this paper can be organized along the following broad themes:

---
### Insufficient Experimental Validation
---
The paper lacks comparisons with key baselines and prior work, making it challenging to fully assess the contributions of this approach. Specifically:

1. **Dynamic API Selection Validation**: While the individual data collection APIs—Information Retrieval, Demonstration Generation, and Question Generation—are well-studied in prior work as Retrieval-Augmented Generation and its variants [1], Self-Instruct [2], and behavior cloning/distillation from teacher LLMs respectively, this work’s primary novelty lies in an optimizer that dynamically selects among these APIs. However, the paper does not compare this dynamic selection against these established methods, leaving unclear whether it is indeed critical for improved performance. To clarify, a comparison is recommended in the following settings:

    - *Inference-only Comparison*: Evaluate ADS against comparable-sized synthetic datasets generated by prior methods, as well as a larger dataset from these methods, given that they do not require additional compute for optimizer training.
    - *Optimizer Training with Single APIs*: Train ADS-style optimizers with individual APIs (e.g., Information Retrieval only) on the MagPie dataset, to assess the relative impact of each API within ADS.

&nbsp;

2. **MagPie Fine-Tuned Baseline**: Unlike ADS, which is trained on the MagPie dataset, baseline LLMs are not. Since fine-tuning on MagPie has been shown to enhance performance on target benchmarks, this gives ADS an advantage over baseline models. A more balanced comparison would involve fine-tuning baseline LLMs on MagPie to assess if ADS's optimizer training and synthetic data generation offer distinct advantages over straightforward fine-tuning.

&nbsp;

---
### Scalability Concerns & Scaling Experiments
---
3. **Generated Dataset Size and Limitations**: The paper studies the proposed method in an in-context policy improvement setting, where synthetic data is added directly to the prompt. This restrictive setting limits the amount of synthetic data that can be utilized, as it must fit within the model's maximum sequence length. Discussion on scenarios where generated data exceeds this length and experiments studying the impact of synthetic data scaling on the method’s effectiveness would strengthen the paper. Specifically, the paper should explore how the method performs when the generated synthetic data exceeds the context window, and whether techniques like iterative prompting or summarization can be used to address this limitation.

4. **Input Task-Specific Dataset Size**: The method currently relies on only five labeled instances from the target task to generate synthetic data, whereas real-world applications may allow access to more extensive task-specific data. Including a discussion on method scalability to larger datasets (e.g., prompt with all task data at once or using sampling and multi-prompting) and experiments exploring the impact of task-specific data scaling would be beneficial. The paper should investigate how performance varies with the number of input examples, and whether there is a point of diminishing returns.

5. **Method Extension and Efficacy for Fine-Tuning**: Since the method is limited to in-context policy improvements, its effectiveness in policy fine-tuning contexts remains untested. Additionally, the feasibility of using the current optimizer training algorithm for fine-tuning is uncertain, as retraining policies to obtain reward for each data generation step could be prohibitively costly. Discussion of this limitation and experiments in fine-tuning scenarios could further clarify the method's general applicability. The paper should discuss the computational cost of fine-tuning the policy model with the generated data and whether the optimizer can be adapted for this setting.

&nbsp;

---
### Method Robustness Concerns
---
6. **Optimizer Generality**: It is unclear if the optimizer learns generalizable insights into model strengths and weaknesses or if its effectiveness is limited to specific tasks. Current training and testing datasets are closely related (e.g., MagPie -> AlpacaEval, etc.). Testing on unrelated benchmarks, like Big-Bench-Hard, GSM8k, or MMLU, would offer insights into the optimizer’s generality. The paper should include experiments on more diverse and challenging benchmarks to assess the optimizer's robustness.
7. **Dependence on MagPie Dataset**: The extent to which the optimizer’s performance depends on the choice of MagPie as the training dataset is unclear. Evaluating its performance when trained on different datasets would provide evidence of ADS's broader applicability. The paper should explore the sensitivity of the optimizer to the training dataset by training it on datasets with varying characteristics.
8. **Reliance on Task Clustering**: ADS clusters similar instances into tasks to generate synthetic data during both training and testing. This clustering may not always be feasible and could require manual intervention. Without this careful clustering, retrieving the relevant synthetic data for a test instance could become a challenge, raising questions about the method's performance if instances are grouped differently, such as randomly, during data generation. The paper should investigate how the quality of task clustering affects the performance of the method and whether the method is robust to different clustering strategies.

&nbsp;

---
### Limited analysis
---
Several important areas lack critical analysis in the paper:

9. **Generated Synthetic Data**: The paper does not analyze the characteristics or quality of the synthetic data generated. A manual review of the generated data could provide valuable insights into its role in improved performance. The paper should include an analysis of the diversity, quality, and relevance of the generated synthetic data, potentially using metrics like perplexity or human evaluation.

10. **API Call Patterns**: There is no examination of the API calls made by the optimizer at test time. Analyzing the frequency and distribution of these calls could clarify the optimizer's behavior and the relative importance of each data source (API). The paper should include an analysis of the API call patterns, showing which APIs are used more frequently for different tasks and how this relates to performance.

11. **Weakness Reflection Rationales**: Although the paper claims that the optimizer uses LLM-driven reflections to assess model strengths and weaknesses, it lacks a qualitative or manual analysis of these reflections. This omission makes it challenging to gauge the accuracy and depth of these self-assessments. The paper should include a qualitative analysis of the rationales generated by the optimizer, evaluating their accuracy and relevance to the task at hand.

&nbsp;

References:

[1] Yu, Wenhao, et al. "Generate rather than retrieve: Large language models are strong context generators." arXiv preprint arXiv:2209.10063 (2022).

[2] Wang, Yizhong et al. “Self-Instruct: Aligning Language Models with Self-Generated Instructions.” Annual Meeting of the Association for Computational Linguistics (2022).

### Questions
Please refer to the *Weakness* section above for recommendations on experiments and analyses that could further strengthen the paper.

Additional questions and suggestions **that do not impact the score**:

1. How are preference pairs constructed from sampled API trajectories for rejection sampling and DPO? Is a single preference pair created from the highest and lowest reward trajectories?
2. Is the cost of API calls considered only when selecting an efficient trajectory from a trajectory tier (group) or do you also add a cost term to the overall reward?
3. Are all prompts (individual APIs, optimizer, evaluation prompts) zero-shot? If not, how many demonstrations are provided for each?
4. Consider expanding the discussion on other data collection techniques (APIs) that could be integrated into the framework.
5. The "internal test-set" is not described in the paper. Without additional details about this internal test set, it is difficult to assess the quality of the improvements. Is it just the test partition of the MagPie dataset?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces the Active Data Search (ADS) framework, which enables large language models (LLMs) to autonomously identify and acquire training data to improve their own performance with minimal human intervention. The authors propose an optimizer model that generates API calls for data collection from various external sources, such as web search engines, AI assistants, and annotation services. This framework leverages reinforcement learning to refine the optimizer, balancing task performance enhancement with computational cost. Experimental results, using models like Qwen-2-7B-Instruct and Gemma-2-9B-Instruct, show substantial performance gains in in-house tasks and public benchmarks, demonstrating ADS’s effectiveness in enabling smaller models to achieve results comparable to larger ones.

### Strengths
The paper presents the ADS framework, which automates the identification and acquisition of training data, enhancing the self-improvement capabilities of LLMs. This direction holds promise for reducing reliance on human intervention, making model development more efficient and scalable.

### Weaknesses
While the paper offers an innovative approach, it has several areas that could be strengthened. The lack of comparison with diverse baselines limits the assessment of the ADS framework's true efficacy. Specifically, comparisons with 
(a) LLMs using basic RAG for retrieval,
(b) untrained LLMs collecting data for policy model inference, 
(c) training the optimizer model with simple rule-based or manually collected data,
(d) other naive automated data collection techniques would provide deeper insights into the relative advantages of ADS. 
Including these baselines would enhance the evaluation's comprehensiveness and validate the framework's practical significance against existing methods.

### Questions
1. Relationship with RAG: The paper lacks a thorough discussion on how the proposed ADS framework relates to or differs from Retrieval-Augmented Generation (RAG). Given that both approaches involve external data retrieval, it would be beneficial to address whether ADS extends, overlaps, or diverges from RAG in terms of methodology, application, or objectives. This comparison would help position the contribution within the broader context of retrieval-based techniques and clarify its novelty.

2. Inconsistent Use of Llama in Experiments: The absence of Llama-based experiments in Figure 2, despite its inclusion as a comparison point in Table 2, raises questions about consistency. It would be helpful for the authors to explain why Llama models were not tested under the same conditions as other models, or why their results were only included in specific sections. This would ensure a clearer understanding of the comparative analysis and model choice rationale.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces an automated framework called ACTIVE DATA SEARCH (ADS), designed to enable large language models (LLMs) to autonomously discover and acquire valuable training data for self-improvement without the need for human supervision.
The authors propose using reinforcement feedback signals to guide the models in selecting optimal data, rewarding performance gains while penalizing computational overhead.
The framework is validated through extensive experiments on 1,000 diverse in-house test tasks and three public benchmarks, demonstrating significant performance improvements.

### Strengths
(1) The ADS framework is innovative as it leverages LLMs to autonomously enhance their training data, reducing the need for costly human intervention and addressing scalability issues. The use of reinforcement feedback signals to balance performance improvement and computational efficiency is a practical and smart approach.
(2) Empirical results are robust, including 1,000 in-house test tasks and three public benchmarks, showing clear performance gains and generalization capabilities. The inclusion of detailed implementation protocols, such as API designs for data acquisition, is valuable for reproducibility.
(3) The paper presents a method for iterative refinement, demonstrating consistent performance improvements with the optimizer refinement through reinforcement learning.

### Weaknesses
 (1) The paper would benefit from more comprehensive ablation studies. Specifically, it would be insightful to understand the individual contributions of each proposed API and the iterative refinement process. For example, what is the impact of excluding one of the APIs, or how does the system perform without the iterative refinement? It is unclear how much each API contributes to the overall performance, and whether some APIs are more critical than others. A detailed analysis of the performance with different API combinations is needed to justify the design choices.
(2) The paper does not sufficiently discuss the potential limitations and failure cases of the ADS framework. Identifying scenarios where the framework might not perform well or discussing any observed limitations during the experiments would provide a more balanced view. For instance, are there specific types of tasks or data distributions where the framework struggles to improve performance? What are the computational bottlenecks or resource constraints that could limit the applicability of the method?
(3) Comparisons with more diverse sets of baselines, especially in terms of data acquisition strategies, would strengthen the validation of the effectiveness of the proposed framework. The current baselines do not fully explore the space of alternative data acquisition techniques, making it difficult to assess the relative advantages of the proposed approach. For example, how does the performance compare to methods that use active learning or curriculum learning for data selection?
(4) The exposition around reinforcement learning strategies could be expanded to aid comprehension, especially for readers less familiar with advanced reinforcement learning techniques. The paper lacks a detailed explanation of the reward function, the policy optimization algorithm, and the specific hyperparameters used in the reinforcement learning process. This makes it difficult to understand the nuances of the reinforcement learning component and to reproduce the results.

### Questions
(1) Could you perform additional ablation studies to analyze the impact of each data acquisition API within the framework? Understanding the individual contributions of each API would highlight their importance and the overall robustness of the ADS framework.
(2) Were there any particular scenarios or tasks where the ADS framework did not perform as expected? If so, what were these failure cases, and how were they addressed or mitigated in the study?
(3) Could you provide further comparisons with alternative data acquisition methods beyond the ones mentioned in the paper?
(4) How sensitive is the ADS framework to different policy model architectures and sizes?

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
The paper presents a self-improvement framework for LLMs that leverages external environments for data acquisition.

During training of the optimizer model, given a set of tasks and instructions for each task, the optimizer model learns (through RL) to generate optimized API call trajectories to acquire relevant external data, by measuring how the acquired data help improve performance of the policy model through finetuning or in-context learning on the data. The RL also takes cost control into account.

During test time, the optimizer model generates data acquisition calls for tasks and instructions unseen during training and the data acquired is used to improve the policy model for these tasks.

The experiments show that data acquisition significantly improves the policy model's performance on various tasks, including Alpaca Eval, Arena Hard, and MT bench, when relevant tasks and instructions are provided for training the optimizer model and with in-context learning of the policy model on the acquired data.

### Strengths
Originality: Self-improving LLMs via data acquisition is a novel direction, to the best of my knowledge.
Quality: The paper shows promising quality gains against the baselines.
Clarity: The framework and the complex process of training the optimizer model are clearly explained.
Significance: Self-improvement of LLMs is clearly an important direction. Acquiring data from an external environment will be critical.

### Weaknesses
Significance: The quality gains against a stronger baseline strategy that "utilizes the Question Answering API for each  observed instruction in the target task" are relatively minor.

Generalization: It's not clear how well the optimizer model generalizes across tasks. The experiments are set up so that the training tasks and instructions appear to be similar to those used during test time. The paper would be strong if it could demonstrate generalization across more distinct tasks.

### Questions
What are the important characteristics of the optimized trajectories that allow them to outperform the baseline trajectories? 

What roles do "information retrieval", "demonstration generation", and "question answering" each play? What if we remove one of the APIs? How does their respective quality affect the final results?

The comparison against the "Question Answering for all instructions" strategy is only conducted for the in-house test set. Does it hold across benchmarks? 

In Algorithm 1, "Split task instructions Q into observed set Qo and held-out set Qh" is in the iteration loop (t), does it mean that the split is different across iterations?

In section 4.3 "we employ the Self-Instruct approach to generate three new instructions for each task and use them as the observed instructions for that task". How much overlap is there between the generated instructions vs. the original ones?

In section 6.2, "In comparison to the approach that focuses solely on maximizing performance without considering costs, our method not only achieves a lower cost as expected but also demonstrates an improved win rate". It's not clear why cost control also improves quality. Is this due to randomness or some other factor?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents the active data search (ADS) framework, allowing large language models to autonomously acquire training data without human supervision. ADS learns an "optimizer" via reinforcement learning to enable active data acquisition while minimizing costs. Experiments demonstrate that ADS leads to performance gains compared with the original model.

### Strengths
The method is well-motivated. Letting LLMs actively identify training data for themselves can potentially improve data efficiency and reduce human efforts in model training.

### Weaknesses
- **The true implementation of ADS is different from its description.** In Sec. 3.2, the authors claim that "_we **train** the original $\mathcal M^p$ on the tailored training dataset to update its knowledge and capacities_". This claim is very misleading because according to Appendix C, the so-called "training" is simply adding the collected data to the prompt. The authors refer to this as "in-context learning" (ICL). However, in [1], ICL is introduced as an _inference_ approach in contrast to _training_. Thus, I believe the main selling point in the title, "finding the data to _train_ the models", is a $\text{\color{red}significant overclaim}$, which can be very misleading to the community.

- **The paper does not compare ADS with any relevant baselines.** The authors include a few relevant papers in Sec. 2, e.g., [2,3]. The authors should compare the cost and quality of ADS with baselines to demonstrate its effectiveness. 
- **I'm concerned about the efficiency of the method.** Algorithm 1 requires $\mathcal O(N|\mathcal A||\mathcal T|)$ evaluations of the policy model. No where in the paper do the author report the computation cost of the method. It's also not clear whether the method can scale up to more types of API calls and larger models in a truly practical scenario.
- Minor issues:
  - Line 50: This sentence is hard to read and grammatically  incorrect. Please consider the modification proposed by LLM: "We achieve the above automatic process through development of an optimizer that generates these APIs sequentially based on the target task to solve."
  - Line 58: `\citet` $\to$ `\citep`
  - Line 138: LLM-as-a judgment  $\to$ LLM-as-a judge

### Questions
Please refer to the **weakness** part.

### Soundness
1

### Presentation
2

### Contribution
2
