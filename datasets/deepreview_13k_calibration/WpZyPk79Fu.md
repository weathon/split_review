# AnyPrefer: An Automatic Framework for Preference Data Synthesis

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
High-quality preference data is essential for aligning foundation models with human values through preference learning. However, manual annotation of such data is often time-consuming and costly. Recent methods adopt a self-rewarding approach, where the target model generates and annotates its own preference data, but this can lead to inaccuracies due to the reward model sharing weights with the target model, amplifying inherent biases. To address these issues, we propose Anyprefer, a framework designed to synthesize high-quality preference data for the target model. Anyprefer frames the data synthesis process as a cooperative two-player Markov Game, where the target model and a judge model collaborate. Here, a series of external tools are introduced to assist the judge model in accurately rewarding the target model’s responses, mitigating biases in the process. We also introduce a feedback mechanism to optimize prompts for both models, enhancing collaboration and improving data quality. The synthesized data is compiled into a new preference dataset, Anyprefer-V1, consisting of 58K high-quality preference pairs. Extensive experiments show that Anyprefer significantly improves model alignment across four applications, covering 21 datasets, achieving average improvements of 18.55 in five natural language generation datasets, 3.66 in nine vision-language understanding datasets, 30.05 in three medical image analysis datasets, and 14.50 in four visuo-motor control tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a framework that automates the synthesis of high-quality preference data. It employs a target model and a judge model, and leverages external tools and a feedback mechanism to enhance data quality. The framework generates a diverse dataset, Anyprefer-V1, which contains 58,000 preference pairs, and improves model performance across applications in natural language generation, vision-language understanding, medical image analysis, and visuo-motor control.

### Strengths
1. Extensive experiments on four downstream tasks demonstrate that the framework can generalize across various domains and tasks.
2. Besides proposing a framework, the authors also provide their generated synthetic dataset, which would help future works.
3. Their experimental results are promising in all the four downstream tasks.

### Weaknesses
1. The overall idea of tool-enhanced critiquing and self-correction is similar to the paper [1]. The authors should have some discussions here.
2. Equation 2 of prompt optimization is misleading. I believe there should not be any gradient descent for the prompt optimization part.
3. In line 196 in Section2.3, the authors should explain how is "high-quality" defined and what kind of reward R(y+,y-) would indicate high-quality reward.
4. The authors only consider self-rewarding as the baseline. It's better to explore and include more baselines, such as [2].

### Questions
1. The authors indicate the the self-rewarding method uses the model itself to reward the responses, which would amplify inherent biases. In this paper, the authors use three different models (target model, judge model, and reward model) for this process. However, there can also be inherent biases in any of those three models, why won't this method amplify the inaccuracies and compromise data quality?

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
In this paper, the authors consider the problem of how to generate a preference data dataset synthetically, as current methods for generating high-quality preference-data currently require significant data annotation. As a solution, the authors propose Anyprefer a framework that frames the preference dataset production as a two-player game between the target and judge models, with a third method acting as a reward proxy for what the performance increase would be if the target (base) model was optimized through preference learning. Anyprefer functions by the target model producing a set of candidate responses to some prompt p_t, which are then ranked by a judge model that additionally gets inputs from expert tools that correspond to the kind of dataset that is being optimized for (vision, medical, natural language generation, or control in their case). They then use a reward model that determines if the preference pair, constructed from the best and worst of the ranking, was sufficiently good to be included. The authors then demonstrate the benefits of such generated pairs on a set of downstream tasks in comparison to the original target models, and both a self-rewarding scheme versus their proposed method that are both used to generate pairs and which are subsequently  used for fine-tuning.

### Strengths
1. The authors consider quite a broad set of target models and target domains to demonstrate their method on, showing that it's efficacious in different data scenarios and regimes. 

2. Anyprefer cleverly integrates other tools outside of the target and judge model, and because of the nature of the judge model being an incredibly powerful VLM like GPT-4o, this strategy seems like an extendable and scalable as more specialized tools become available.

3. The improvements on downstream target models, in comparison to baselines, is clear. This technique effectively is able to take advantage of GPT-4o to improve the capabilities of weaker models.

### Weaknesses
1. It is unclear in the paper what the authors gain in perspective or methodology from framing their generation as a "two-player game". Given that this technical detail was referenced several times, I was expecting that it would be involved in some sort of modeling decision or theoretical result. Another point that I believe is important to explain well, and lacked clarity, was how one can update the policy of the target model p_t, by optimizing the input prompt p_t. This mixes together a few notions from language modeling and RL that I believe should be explained better.

2. The authors should include their benchmarking on IMG/MED datasets with the synthetic dataset VLFeedback in the main text. If I understand correctly, it similarly does not require human effort, is larger than Anyprefer-V1, and could be compared against to demonstrate the claim made by Figure 6 that the diversity of Anyprefer is its strength over existing techniques. Additionally, I was not convinced by the t-SNE plots that Anyprefer seemed to cover all datasets, it is just in the distribution diagram spread that they appear either more sparse (Anyprefer) or more dense (VLFeedback). A quantitative analysis here consistent with what is done in the literature seems necessary.

3. The authors claim in Lines 70 and 95 that the methods used as 'tools' for providing auxiliary information to the judge models are 'selected based on the input prompt' or 'Anyprefer strategically selects tools'. From what I understand in section 3.1, either the tools are selected manually corresponding to the task or it is not explained how 'Anyprefer' selects tools. This makes me believe that how the tools are chosen is ambiguous.

### Questions
1. In line 47, its said that "…this approach may fail to capture the inherence preferences of the target model being fine-tuned, rendering the data-generation less useful". I found this phrasing quite confusing, as if your target model is imperfect, why would it matter that you aren't aligned with it. From my perspective the whole benefit of the proposed system is effectively a distillation of GPT-4o preferences into the target model.

2. It would've been interesting to see ablations regardless the dataset generation process. For example, if the Judge model produces quality rankings, then doesn't it seem suboptimal to use only the best and worst generation? Couldn't one use many different pairs (preserving ranking order for + or -) from the ranking? Also it seems that 5 was chosen as the number of generations, but it's unclear the role that this plays in the final quality.

3. Once the preference datasets are generated using any of the proposed techniques, what was the process for actually improving the target models? We are given the results but without any experimental setup for that tuning. I'm leaning on making this a weakness, as I think it's important to be included, but it could be that this should be a common knowledge process.

4. Why is it the case that both the prompt of the target model AND of the judge model need to be optimized in this process? Is it not sufficient to optimize the prompt of the target model through the preferences of the judge? It would be interesting to see that this is insufficient.

5. Where does so much improvement come from in the medical VQA task? It seems like 31.05% is a massive gain.

6. In section 3.5, how were these samples manually selected? 

7. Was there an analysis done on how including different numbers of tools was helpful for different datasets, or which tools mattered the most?

### Soundness
3

### Presentation
1

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
This paper proposed Anyprefer, an automatic method to synthesize high-quality preference data to improve model alignment with human values. The preference data generation is set as a cooperative two-player Markov game between a target model and a judge model. Using external tools and feedback, the proposed Anyprefer claim to show substantial performance improvement across four applications: natural language generation, vision-language understanding, medical image analysis, and visuo-motor control.

### Strengths
-  This paper solves an important problem in synthetic data generation for model alignment. The proposed framework can automates preference data synthesis, which can reduce the reliance on human annotations.
- The proposed model uses external tools in the reward phase, which may be able to make the data more diverse, reduce bias, and improve data quality in preference synthesis.
- The paper conducted extensive experiments and ablation studies across multiple applications.

### Weaknesses
 - The setting, a two-player cooperative Markov Game for preference data synthesis, is only vaguely justified. The paper could be better if adding some explanations about  how this approach explicitly improves alignment over simpler, existing methods. Specifically, the paper lacks a clear explanation of why a cooperative game is necessary for preference data generation, rather than a simpler approach where a single model generates data and a separate model evaluates it. The current justification relies on intuition rather than a rigorous analysis of the benefits of this specific game-theoretic framework.
- External tools are incorporated to reduce bias. It would be good to add additional analysis or metrics to show that these tools effectively mitigate model bias or improve reliability beyond existing methods. The paper does not provide sufficient evidence that these tools effectively reduce bias. It would be beneficial to include metrics that directly measure bias, such as demographic parity or equal opportunity, to demonstrate the effectiveness of the external tools in mitigating bias. Without such metrics, the claim that these tools reduce bias remains unsubstantiated.
- The proposed model’s effectiveness is evaluated on a narrow set of datasets within each application domain, which may not be able to show its overall generalizability. It would be good to perform on datasets or domains outside the four tested applications as well. The current evaluation is limited to a few datasets within each of the four domains. This raises concerns about the generalizability of the proposed method to other datasets or domains. For example, in natural language generation, the model is evaluated on GSM8K, ARC-Easy, ARC-Challenge, and Alpaca Eval 2.0, but not on other common benchmarks such as summarization or dialogue datasets. Similarly, in the other domains, the evaluations are limited to a small number of datasets, which makes it difficult to assess the overall applicability of the approach.
- While the  feedback mechanisms are described,  the impact of these mechanisms on the process is not clearly analyzed. It would be good to add ablation study to study their specific contribution. The paper describes the feedback mechanisms but does not provide a detailed analysis of their impact on the overall performance. It is unclear how much each component of the feedback mechanism contributes to the final results. An ablation study that systematically removes or modifies different components of the feedback mechanism would be necessary to understand their specific contributions.

### Questions
Please see the comments above.

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
4

### Summary
The paper proposes Anyprefer, a novel framework for generating preference data for aligning AI models. Anyprefer accomplishes the preference data generation process as a cooperative two-player Markov Game between a target model and a judge model. The judge model uses external tools to get rewards and rank the responses generated by the target model. Additionally, a feedback mechanism is adopted to learn the prompts for both models. Experimental results show the effectiveness of Anyprefer comparison to existing baselines such as an untrained model and self-rewarding. The author also conducts a series of analyses to investigate different components of Anyprefer.

### Strengths
1. The paper is well-written.
2. The experiments are good and provide positive results on AnyPrefer.
3. The author claims to release a preference dataset that may help the community.
4. The framework is novel with the feedback learning mechanism and tool argumentation.

### Weaknesses
1. The author may provide at least a short explanation on how you update the prompt for GPT-4o (a black box model) with policy gradient? I suspect that not all audients are not famaliar with TextGrad. It is better to provide more experimental details in the appendix on how TextGrad is accomplished in different datasets.
2. The method requires an additional reward model for refining the prompt, what's the expected performance if directly using the additional reward model as the judge model? 
3. The proposed method is called AnyPreference and the author conducts experiments on various scenarios that need preference data. The comparison and insights on evaluations of different scenarios can be discussed. 
4. The author can consider more references regarding reward modeling, tool argumentation, and preference data construction, including but not limited to:
   Li L, Chai Y, Wang S, et al. Tool-augmented reward modeling[J]. arXiv preprint arXiv:2310.01045, 2023.
   Ye Z, Li X, Li Q, et al. Beyond Scalar Reward Model: Learning Generative Judge from Preference Data[J]. arXiv preprint arXiv:2410.03742, 2024.
   Mohammad Gheshlaghi Azar, Zhaohan Daniel Guo, Bilal Piot, Remi Munos, Mark Rowland,
   Michal Valko, and Daniele Calandriello. A general theoretical paradigm to understand learning from human preferences. In International Conference on Artificial Intelligence and Statistics,
   pp. 4447–4455. PMLR, 2024.
   Junlong Li, Shichao Sun, Weizhe Yuan, Run-Ze Fan, Hai Zhao, and Pengfei Liu. Generative judge for evaluating alignment. arXiv preprint arXiv:2310.05470, 2023
  Wu T, Yuan W, Golovneva O, et al. Meta-rewarding language models: Self-improving alignment with llm-as-a-meta-judge[J]. arXiv preprint arXiv:2407.19594, 2024.
5. The method can be compared with more strong baselines in addition to an untrained model and self-rewarding, such as meta-rewarding.

### Questions
1. The method requires an additional reward model for refining the prompt, what's the expected performance if directly using the additional reward model as the judge model? 
2. Are there any insights on the adoption of AnyPrefer in different scenarios?
3. If I understand correctly, the novelty of AnyPrefer lies in tool usage and prompt tunning from reward, these contribution looks more engineering-oriented. Is there any connection between the design of these two modules?

### Soundness
3

### Presentation
4

### Contribution
3
