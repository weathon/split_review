# CodePMP: Scalable Preference Model Pretraining for Large Language Model Reasoning

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
Large language models (LLMs) have made significant progress in natural language understanding and generation, driven by scalable pretraining and advanced finetuning. However, enhancing reasoning abilities in LLMs, particularly via reinforcement learning from human feedback (RLHF), remains challenging due to the scarcity of high-quality preference data, which is labor-intensive to annotate and crucial for reward model (RM) finetuning. To alleviate this issue, we introduce CodePMP, a scalable preference model pretraining (PMP) pipeline that utilizes a large corpus of synthesized code-preference pairs from publicly available high-quality source code. CodePMP improves RM finetuning efficiency by pretraining preference models on large-scale synthesized code-preference pairs. We evaluate CodePMP on mathematical reasoning tasks (GSM8K, MATH) and logical reasoning tasks (ReClor, LogiQA2.0), consistently showing significant improvements in reasoning performance of LLMs and highlighting the importance of scalable preference model pretraining for efficient reward modeling.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents CodePMP, a novel and scalable preference model pretraining (PMP) pipeline aimed at enhancing the reasoning capabilities of Large Language Models (LLMs). 

CodePMP builds its dataset in two stages: 1) generating instructions from GitHub files using a CodeLLM, and 2) generating two responses for each instruction from a strong CodeLLM and a weak CodeLLM, which are the preferred and rejected response pairs. 28 million such response pairs are constructed.

After pre-training an LLM on these 28 million pairs, CodePMP improves RM finetuning efficiency. The resulting reward model built upon CodePMP can then be leveraged to improve performance on reasoning tasks, including solving mathematical and logical problems.

### Strengths
- The proposed method is highly scalable, allowing it to create 28 million preferred and rejected response pairs.

- The reward model can improve two different reasoning tasks (math reasoning and logic reasoning).

### Weaknesses
 - CodePMP creates preference pairs for coding tasks, but coding tasks are not evaluated in experiments. 

- The CodePMP data is constructed by deepseek-coder-instruct. It would be interesting to see whether CodePMP can further improve deepseek-coder-instruct on coding tasks.

- The reward model is initialized using Qwen2 models (Qwen2-1.5B and Qwen2-7B), which are more capable in math reasoning than the math generator MetaMath-Mistral-7B in Section 4.1.3. A more meaningful setting would be to examine whether the Qwen2 based reward model can further improve the performance of Qwen2 or Qwen2-Math on math reasoning tasks.

- Majority voting should be included as a baseline in Figure 3.

- Further analysis is needed to understand why the coding-based CodePMP contributes to improvements in math and logical reasoning.

### Questions
- Is Majority voting@K comparable with reranking top K with a RM in Figure 3?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents codepmp, a scalable pretraining method designed to improve the reward model by leveraging synthesized code-preference pairs. CodePMP collects a vast repository of publicly available source code from GitHub and leverages a strong and a weak model to generate synthetic preference pairs to pretrain a reward model. Utilizing this pretrained reward model, LLM's ability to solve reasoning tasks is largely improved by best of N sampling.

### Strengths
1. This work proposes an interesting idea of preference pre-training.
2. This method is automated, reducing the dependency on manually annotated preference data.
3. With best-of-N strategy, CodePMP could improve LLM's reasoning performance.

### Weaknesses
1. Unfortunately, the effectiveness of the RM was not fully verified, e.g. by using the RM for RFT or PPO training. The reliance on Best-of-N sampling, while informative, does not fully validate the reward model's utility in a reinforcement learning setting. Specifically, it's unclear how well this reward model would perform when used to guide policy optimization through methods like Proximal Policy Optimization (PPO) or Reward Fine-Tuning (RFT). The paper lacks experiments that directly demonstrate the RM's ability to shape policy behavior, which is a crucial aspect of reward model evaluation.
2. It remains unclear whether and how code training could help reasoning tasks in natural language. It would be great if the authors could have explored more on relationship between coding and reasoning tasks for model training. The paper does not provide a strong theoretical or empirical justification for why pre-training on code preferences would improve performance on mathematical and logical reasoning tasks. While code embodies a form of logic, the connection to natural language reasoning is not explicitly established. A more detailed analysis of the underlying mechanisms by which code-based pre-training transfers to natural language reasoning would be beneficial.
3. No mention of whether the dataset will be open sourced.
4. The models used in data construction are limited. It would be helpful to verify the generalization with more number of generators, at least the ones used to construct the training data. The paper's reliance on a limited set of generators for creating the synthetic preference pairs raises concerns about the robustness and generalizability of the method. It would be important to evaluate the performance of the approach using a more diverse set of generators, including those with varying architectures and training data, to ensure that the observed improvements are not specific to the chosen models.
5. Evalution tasks are limited. Regular coding benchmarks like humaneval and mbpp should be relevant.

### Questions
1. Figure 4 and 5 are too small to watch.
2. Why CodePMP can help reward modeling in mathematical tasks? Please give more analysis in the paper.
3. Reference formatting issues, such as line 429.
4. Would you consider using a larger reward model to verify the scalability?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work introduce CodePMP, a pipeline that create synthesize code-preference pairs in order to have more high quality preference data. The authors show that a better reward model can be obtained with these preference pair data. And it also shows the improvements in several reasoning tasks (GSM8K, MATH, ReClor, LogiQA2.0) with these synthesize code-preference pairs data.

### Strengths
1. A pipeline that create synthesize code-preference pairs is introduce in this work. It can help to solve the scarcity of high-quality preference data if it is working well.

2. Large improvements are achieved on several reasoning tasks (GSM8K, MATH, ReClor, LogiQA2.0) with these synthesize code-preference pairs data.

3. Some details of CodePMP are shown. These can be helpful to the community.

### Weaknesses
1. The experiments details are missing or confused. It is better to clarify in the next version. Please check the following Questions section for more details. 

2. In the experiments, only two Qwen2 models are used for the evaluation. Other model family results can be used for the verification of the methods.

3. In the Data Construction, a description summarizer is used to generate prompts that describe the code. There is no any detail on this part. And what is quality of constructed data pair? There is no any related analysis in this work. It is not a human-annotated dataset. So it is important to show the data quality.  

4. In Section 4.2.2, how the different number of N candidate responses are generated? Is Qwen2 model used to sample these candidate response? There is no details about this.

5. In Figure 4, the author claims that: RM with Code PMP initialization consistently outperform. However, it seems not right. Figure 4 (g) shown a counter part case. RM with Code PMP initialization is consistently  worse than RM without Code PMP initialization. Please check in detail.

### Questions
1. In the Data Construction, a description summarizer is used to generate prompts that describe the code. There is no any detail on this part. And what is quality of constructed data pair? There is no any related analysis in this work. It is not a human-annotated dataset. So it is important to show the data quality.  

2. In Section 4.2.2, how the different number of N candidate responses are generated? Is Qwen2 model used to sample these candidate response? There is no details about this.

3. In Figure 4, the author claims that: RM with Code PMP initialization consistently outperform. However, it seems not right. Figure 4 (g) shown a counter part case. RM with Code PMP initialization is consistently  worse than RM without Code PMP initialization. Please check in detail.

4. As shown in Figure 5, increasing the number of code-preference pairs consistently improve accuracy. Look like there is still some improvement space. Do you think more preference data can be obtained without too much work?

Other questions: is the PMP data planed to be released? how many code-preference pairs? (only file number and token number are shown, e.g, Python files, with 20 million files and 13.1 billion tokens,)

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
3

### Summary
This paper presents CodePMP, a novel pipeline for preference model pretraining aimed at enhancing the reasoning capabilities of large language models (LLMs). The primary challenge addressed is the scarcity of high-quality preference data, which is crucial for reinforcement learning from human feedback (RLHF) but costly to annotate. The authors propose a solution by leveraging code-preference pairs synthesized from publicly available high-quality source code, such as from GitHub, to improve reward model finetuning.

The CodePMP pipeline generates millions of code-preference pairs by using two different code models (a stronger model and a weaker model) to create a “chosen” and “rejected” code response for a given code prompt. These pairs are then used to pretrain the preference models, leading to better sample efficiency and improved reasoning performance in downstream tasks like mathematical reasoning (GSM8K, MATH) and logical reasoning (ReClor, LogiQA2.0).

### Strengths
**1. Efficiency in Reward Model Fine-Tuning**


CodePMP significantly enhances the sample efficiency of reward model (RM) fine-tuning, as the experiments indicate that fewer samples are required to achieve high accuracy. The paper shows that RMs initialized with CodePMP outperform directly fine-tuned models, even with smaller amounts of data. This efficiency makes the method appealing for real-world applications where data collection can be expensive or time-consuming.

**2. Scalable Data Generation**


One of the major strengths of CodePMP is its ability to generate large-scale preference data using code-preference pairs. By synthesizing data from publicly available source code on platforms like GitHub, the authors address the scarcity of high-quality preference data. This reduces the reliance on costly human annotation, making the pretraining process significantly more scalable and potentially more cost-effective than traditional methods relying solely on human feedback.

**3. Leveraging Code for Reasoning Tasks**

The paper introduces an innovative use of GitHub-sourced code to enhance reasoning in LLMs. By leveraging the logical structure of code, the authors create code-preference pairs, where stronger models generate "accepted" responses and weaker models generate "rejected" ones. This approach capitalizes on the abundance of publicly available code on GitHub, using it to simulate reasoning tasks. The structured nature of code makes it an ideal dataset for pretraining models to improve problem-solving and logical reasoning capabilities, aligning with recent research showing that training on code boosts reasoning performance in LLMs.

### Weaknesses
 **1. Lack of Examples** 

The paper lacks clear and detailed examples that illustrate how CodePMP actually solves reasoning tasks using code-preference pairs. While the overall methodology is explained, it's hard for the reader to grasp how reasoning is specifically improved through the use of code data. The absence of step-by-step examples of how the code-preference pairs are used to train the reward model leaves an important gap. For instance, showing a few real examples of code, its corresponding “chosen” and “rejected” responses, and how these responses contribute to solving a reasoning task would be highly valuable. The appendix, while providing some additional technical details, does not adequately fill this gap. 


**2. Limited Baselines**

The paper’s comparison to **alternative methods** is quite limited. It focuses primarily on showing the improvements over direct RM fine-tuning without pretraining, but fails to benchmark CodePMP against other advanced reasoning techniques such as:

Chain-of-Thought (CoT) prompting, which has been shown to significantly improve reasoning performance by breaking down tasks into intermediate steps.
Search-based methods like Monte Carlo Tree Search (MCTS), which have been effective in enhancing reasoning capabilities in language models through external computation and verification steps.
A reader would expect a thorough comparison of CodePMP against these methods, especially since these are widely used in the current state-of-the-art LLM systems. Additionally, the paper should clarify:

How does CodePMP stack up against CoT and search-based approaches in the same experimental setup?
What are the strengths and weaknesses of CodePMP relative to these techniques?

**3. Challenges in Maintaining Data Quality with Evolving LLM Capabilities**

A key limitation of the CodePMP methodology is its reliance on two distinct models—one to generate "accepted" (high-quality) responses and another to produce "rejected" (low-quality) responses. While this setup works for synthesizing large quantities of training data, there is a valid concern that as LLMs improve, the gap between the two models could narrow, leading to mismatches in the data quality. For example, there is a risk of **data distribution drift:** As the strong model improves, the generated "accepted" responses may no longer reflect the kind of reasoning tasks the preference model was initially trained on, leading to a mismatch between the training data and the actual data seen in practice. The system might overfit to synthetic training data that does not generalize well to the actual tasks faced by stronger LLMs.

### Questions
Given that CodePMP relies heavily on code data, how well do you expect it to generalize to reasoning tasks that do not have a structured, logical basis like code (e.g., common-sense reasoning, social interactions, or natural language inference)? Have you explored tasks beyond mathematical and logical reasoning?

### Soundness
2

### Presentation
3

### Contribution
3
