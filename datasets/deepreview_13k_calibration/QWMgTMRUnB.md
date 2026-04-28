# Self-Alignment Optimization for Language Models

- Decision: Reject
- Avg Score: 3.60
- Scores: 3, 3, 6, 3, 3

## Abstract
Traditional reinforcement learning from human feedback (RLHF) relies heavily on costly and time-consuming human-annotated datasets. Even Reinforcement Learning from AI Feedback (RLAIF), which trains a reward model using AI-generated preference data before refining the language model through reinforcement learning, remains expensive. These methods often necessitate either specialized reward model designs or larger models (e.g., GPT-4) for external labeling. In this paper, we introduce a dataset-free and annotation-free framework called Self-Alignment Optimization (SAO), which addresses the aforementioned issue by aligning the model with its own prompts and feedback as preferences. SAO begins with a chat-based model that engages in persona role-play to generate diverse prompts and responses, which are then self-evaluated and used for preference optimization.
Extensive experiments with two strong LLMs on several benchmarks demonstrate the effectiveness of SAO. Specifically, on AlpacaEval 2.0, Gemma-2-9B-it-SAO achieves a Length-Controlled Win Rate (LC)  of 69.2\% and win rate (WR) of 66.0\%, surpassing the baseline model by 18.1\% and 27.9\%. Llama-3-Instruct-8B-SAO reaches 33.3\% LC and 39.0\%  WR, with performance improvements of 10.4\% and 16.4\%, respectively. On the MT-Bench benchmark, Gemma-2-9B-it-SAO and Llama-3-8B-Instruct-SAO score 7.41 and 6.76, compared to their pre-SAO scores of 7.09 and 6.70. The Arena-Hard benchmark shows even greater gains from SAO, with Gemma-2-9B-it's WR increasing from 52.6\% to 70.1\% and Llama-3-Instruct-8B's WR rising from 40.3\% to 56.4\%. In addition, our further experiments demonstrate that models fine-tuned with SAO exhibit similar or even superior performance on downstream NLP tasks compared to baseline models, rather than those trained with external labeled datasets, which enhance alignment ability but may compromise some general capabilities. We anticipate that this work will provide new insights for future research on self-improvement in LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes Self-Alignment Optimization (SAO), a framework for enhancing language model alignment without external datasets or human-labeled feedback. Traditional alignment methods, like Reinforcement Learning from Human Feedback (RLHF) and Reinforcement Learning from AI Feedback (RLAIF), are resource-intensive due to the need for specialized reward models or substantial external data. SAO addresses these limitations by enabling models to align autonomously: a model generates prompts based on various personas, produces responses, and then ranks these responses through self-assessment. The framework relies on this self-generated dataset and uses preference optimization (SimPO) to refine model alignment, reducing the need for human input or costly external tools.

Empirical results show that SAO achieves improvements in model performance across several benchmarks. For instance, on AlpacaEval 2.0, SAO-tuned models exhibit significant gains in Length-Controlled Win Rate (LC) and Win Rate (WR) over baseline models, with similar enhancements observed on the MT-Bench and Arena-Hard benchmarks. Additionally, SAO-tuned models maintain or slightly improve downstream NLP performance metrics as measured by the Open LLM Leaderboard, suggesting that SAO can enhance alignment without compromising general task capabilities. Further analysis in the paper explores factors that influence SAO's effectiveness, including synthetic dataset size, persona role diversity, and optimization methods, underscoring the potential of SAO as an efficient and scalable alternative to traditional alignment approaches.

### Strengths
1. The SAO framework operates without the need for external, human-annotated data, eliminating costly annotation requirements while maintaining alignment effectiveness.
2. Empirical results show that models fine-tuned with SAO achieve substantial improvements over their vanilla base models, particularly in alignment-specific metrics like Length-Controlled Win Rate (LC) and Win Rate (WR) across multiple benchmarks.
3. The paper provides comprehensive empirical results, evaluating SAO across a range of benchmarks and scenarios, including AlpacaEval 2.0, MT-Bench, and Arena-Hard, which thoroughly demonstrate the robustness and scalability of the proposed method.

### Weaknesses
1. Most of SAO’s components—such as persona-based prompt generation, self-generation/self-judgment, and preference optimization using SimPO—are adapted from prior work, potentially limiting the novelty of the technical approach. To strengthen the contributions, the paper needs to explore innovative adaptations or improvements to these existing methods that demonstrate clear enhancements in model performance or alignment capabilities. Specifically, the paper lacks a detailed analysis of how the combination of these known components leads to emergent behavior or synergistic effects that are not present when these components are used in isolation or in different configurations. The current analysis does not sufficiently justify the specific choice of these components over other possible alternatives.

2. While SAO achieves improvements over vanilla models, its enhancements compared to more meaningful direct counterparts (e.g., Gemma-2-9B-it-SAO vs. Gemma-2-9B-it-SimPO) are relatively minor. Given that SimPO relies on external datasets, this limited improvement suggests that self-generated preference data may currently be less effective. The study needs a deeper examination of self-generated data’s limitations and a discussion of methods to enhance its quality, which may reveal additional advantages over using external data. The paper should investigate the characteristics of the self-generated data, such as its diversity, quality, and potential biases, and how these factors impact the final model performance. A comparison of the data distributions between self-generated and external datasets would also be beneficial.

3. Although the paper promotes SAO’s dataset-free and annotation-free aspects, the practical impact of this approach is not fully substantiated. Alignment research aims for impactful, real-world outcomes, and it would be helpful if the authors clarified specific advantages or applications where being dataset-free provides measurable benefits (e.g., scenarios with limited access to annotation resources or environments needing continual self-adaptation). For example, people probably don't need a full dataset/annotation-free pipeline, but just a single significant improvement in the RLHF pipeline, like the SimPO technique. Further analysis of the unique applications and limitations of a dataset-free strategy could better ground this approach in practical relevance. The paper should also discuss the potential trade-offs between the dataset-free approach and the performance that can be achieved with high-quality, human-annotated data.

### Questions
1. Suggestion on the writing: reduce the length of section 3, which is commonsense knowledge in the field now
2. Questions about the efficiency: the proposed techniques still require the significant cost of training/fine-tuning, how this paper should be positioned in the current trend of much cheaper alignment techniques, like using prompting, representation editing, or reward-guided test-time decoding to improve the alignment performance

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
* The paper proposes Self-Alignment Optimization (SAO), a framework for fine-tuning language models without external labeled datasets by leveraging self-generated prompts and responses through persona role-play.
* The study evaluates SAO on two main models: Gemma-2-9B-it and Llama-3-Instruct-8B, testing them on multiple benchmarks including AlpacaEval 2.0, MT-Bench, and Arena-Hard.
* Key findings suggest performance improvements on subjective benchmarks (e.g., Gemma-2-9B-it-SAO achieves 69.2% LC and 66.0% WR on AlpacaEval 2.0) while maintaining performance on objective downstream tasks.

### Strengths
* The approach demonstrates meaningful performance gains without requiring external labeled datasets, which could make fine-tuning more accessible and cost-effective for smaller organizations.
* The paper provides nice ablation studies and analyses, particularly in Figure 3, exploring various aspects like dataset size impact, optimization algorithms, persona role-play influence, and self-judgment capabilities.
* The experimental evaluation is systematic, covering both subjective and objective benchmarks, with clear performance metrics and comparisons against baseline models.

### Weaknesses
 * The paper's technical novelty is limited, as similar self-improvement approaches have been explored in previous works like Self-Rewarding LMs. The core concept appears to be a variation of existing methods rather than a new approach.
  * The claimed benefits of being "dataset-free and annotation-free" are not novel in the field
  * The paper lacks comparison and discussion with relevant prior work on self-alignment, for example SALMON, OAIF, and SAMI.
* There are several methodological concerns:
  * The use of GPT-4o-mini as a judge model for evaluating Arena-Hard and MT-Bench seems questionable given its relative weakness compared to state-of-the-art models
  * The reported improvements on the Open LLM Leaderboard are minimal to non-existent

### Questions
* Given that dataset-free or annotation-free alignment approaches are already established in the field, could the authors clearly articulate in one sentence what they consider to be the primary novel contribution of this work?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents Self-Alignment Optimization (SAO), a framework that bypasses the need for expensive human-annotated datasets or AI-labeled preference data in aligning LLMs. Instead of relying on annotated data or costly labeling with larger models, SAO aims to replace with a self-supervised alignment process. In SAO, a chat-based model generates its own prompts and feedback through persona-based role-play, evaluates its responses, and refines itself based on these self-assigned preferences. Experiments show that models trained with SAO outperform baseline models on various benchmarks (e.g., AlpacaEval 2.0, MT-Bench, Arena-Hard) in alignment tasks.

### Strengths
- The proposed Self-Alignment Optimization (SAO) framework removes the need for expensive human annotations or AI-labeled preference data. By doing so, SAO makes model alignment significantly more affordable and accessible, lowering the barrier for effective model refinement.
- SAO leverages persona role-play to generate a wide variety of prompts, which enriches the diversity of inputs and responses the model can handle. This method shows effective results in generating robust, varied prompts, as demonstrated by the paper's experiments.
- SAO’s effectiveness is shown across different language models and multiple benchmarks (e.g., AlpacaEval 2.0, MT-Bench, Arena-Hard). The framework consistently improves performance across diverse tasks and evaluation settings, indicating its general applicability and robust alignment capabilities.

### Weaknesses
 - **Dependence on Initial Model Performance for Self-Alignment:** The SAO framework appears to rely on a certain level of initial model performance for effective self-alignment, as the model must be able to understand and follow instructions to generate meaningful responses. However, the paper only demonstrates SAO’s efficacy with relatively well-performing LLMs. It remains unclear how SAO would perform with smaller LLMs, such as those with 1B or 3B parameters, which might struggle with instruction following and generating coherent responses. Further investigation is needed to evaluate SAO’s effectiveness on these smaller-scale models.
- **Challenges with Output Consistency in Self-Supervision:** In some cases, models may fail to produce outputs in the desired format, which could lead to instability or even failure in the training process. This issue poses a risk to the reliability of the self-alignment process. How do authors address instances where the model’s output deviates from the required format during training—whether through corrective measures, filtering techniques, or additional constraints to ensure format consistency.
- To assess the effectiveness of persona-style prompt generation, how does the model's performance compare when using existing prompts instead of persona-based prompts, while keeping all other components of the method unchanged?

### Questions
Is there a specific reason for using different prompts for MT-Bench and AlpacaEval?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a way of self-improving without any data annotation, specifically, they randomly sample some personas from Persona-Hub (Chan et al. 2024), and ask base LLMs to produce prompts, then, generate two responses for each prompt, followed by prompting LLMs again for pair-wise ranking. With those data, they can run SimPO to update base LLMs. Experiments show significant improvements on AlpacaEval 2.0 and Arena-Hard Benchmarks, however, there is no difference in many downstream NLP tasks (e.g. GSM8K, MMLU etc.)

### Strengths
1.	The improvements on AlpacaEval 2.0 and Arena-Hard Benchmarks over base models are surprising.

### Weaknesses
1. Many researchers are working on self-improving with external supervision and guidance to achieve some improvements over base policy models. And I believe all those studies have already confirmed that LLMs itself cannot be self-improved without using external supervision. 
2.	The idea of this paper is very simple, the improvements on AlpacaEval 2.0 and Arena-Hard are very surprising, further investigation and analysis must be done on those results. 
3.	The novelty of this paper is very limited.

### Questions
The experimental results must be well-examined: a) why the improvements on AlpacaEval 2.0 are so high, but there is no improvement in average score on downstream NLP tasks; b) Why experiments in Table 2 are in few-shot settings? Those models are all instruct models, please test in zero-shot setting; c) Larger LLMs, at least 70B, are required to support the claims of this paper.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Paper proposes Self-Alignmenet Optimization(SAO) claiming it is a data-free, annotation-free framework to perform preference alignment. 
The paper shows that without using an external prompt space, and an external reward model, LLM can learn from an on-policy sampled dataset annotated by using itself as a judge. The paper demonstrates improvements on 3 trusted alignment Benchmarks, AlpacaEval, MT-Bench, and ArenaHard over the starting model, and for gemma model in particular, it shows comparable performance as models aligned using SoTA trained reward models on AlpacaEval. Meanwhile, experiments on academic Benchmarks show no noticeable regression overall from the starting model.

### Strengths
* Novel method of self-generating prompt using persona library as seed. 

* Extension of RLAIF work that uses itself as the judge model to perform self-improvement. This is highly efficient and resource-friendly, without needing to collect external feedback or using external reward models. 

* It designed a comprehensive alignment experiment, and ablated on size of alignment dataset, and importance of having diversity in prompt space, and optimization algorithm. 

* it shows impressive result, especially for Gemma-2 model.

### Weaknesses
 * "data-free, annotation-free framework " is in accurate. For example, it uses Persona Library as seed, and it uses self-judge to annotate data. Better claim to be free of external annotator and generate prompt space from seed. 

* Lack of novelty in the method. It is overall an extension of existing RLAIF literature, using self-judge plus on-policy sampling dataset. The main difference is that it proposes to self-generate the prompt space using Persona library as seed. 

* If one major point of novelty in the paper is Persona based prompt space generation, then, experiment will be needed to compare it against existing open-source prompt space, such as UltraFeedback or HelpSteer. I encourage authors to include such baselines to your main experiment tables. 

* If the Self-judge portion is the major novelty of the paper, then, experiment should be performed to compare self-judge vs external trained reward or other LLM-as-a-judge reward. An experiment table demonstrating the LLM-as-a-judge's reward accuracy would be helpful to understand the contribution here. 

* Evaluation could be improved to be more consistent and clear by comparing AlpacaEval, ArenaHard, and MT-Bench of baseline models + your method all in Table-1, similar to the presentation in SimPO paper. I would like to see how much improvement proposed method brings on all three Benchmarks compared to other methods. Placing heavy emphasis on AlpacaEval2.0 risk over-fitting to one Benchmark.

### Questions
* Why is there  such a big difference between SAO's effectiveness on Llama-3 and on Gemma-2? Is it possible that difference arises from that Gemma-2 is a much better reward model when being prompted to pick responses? 

An experiment comparing the LLM-as-a-judge accuracy between Llama-3 and Gemma-2 model may be helpful to answer the question.

### Soundness
2

### Presentation
3

### Contribution
2
