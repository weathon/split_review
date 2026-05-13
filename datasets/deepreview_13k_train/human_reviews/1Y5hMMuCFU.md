# Unleashing Reasoning Capability of LLMs via Scalable Question Synthesis from Scratch

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
The availability of high-quality data is one of the most important factors in improving the reasoning capability of LLMs. 
Existing works have demonstrated the effectiveness of creating more instruction data from seed questions or knowledge bases.
Recent research indicates that continually scaling up data synthesis from strong models (e.g., GPT-4) can further elicit reasoning performance.
Though promising, the open-sourced community still lacks high-quality data at scale and scalable data synthesis methods with affordable costs.
To address this, we introduce ScaleQuest, a scalable and novel data synthesis method that utilizes ``small-size'' (e.g., 7B) open-source models to generate questions from scratch without the need for seed data with complex augmentation constraints.
With the efficient ScaleQuest, we automatically constructed a mathematical reasoning dataset consisting of 1 million problem-solution pairs, which are more effective than existing open-sourced datasets.
It can universally increase the performance of mainstream open-source models (i.e., Mistral, Llama3, DeepSeekMath, and Qwen2-Math) by achieving 29.2\% to 46.4\% gains on MATH.
Notably, simply fine-tuning the Qwen2-Math-7B-Base model with our dataset can even surpass Qwen2-Math-7B-Instruct, a strong and well-aligned model on closed-source data, and proprietary models such as GPT-4-Turbo and Claude-3.5 Sonnet.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a novel framework for generating high-quality reasoning datasets using smaller open-source models. The primary focus is on addressing the challenges of synthesizing high-quality data at scale with affordable costs. 

Key contributions of the paper include:

- The authors present a scalable data synthesis method that enables the generation of 1 million question-answer pairs without relying on extensive seed data or complex augmentation techniques.

- The framework incorporates a two-stage process consisting of Question Fine-Tuning (QFT) and Question Preference Optimization (QPO), which enhances the question generation capabilities of the models.

- The paper demonstrates that models fine-tuned with the ScaleQuest dataset achieve significant performance gains compared to baseline models.

### Strengths
- This article focuses on synthesizing mathematical problems using open-source large language models, which is an important topic. The fine-tuning and filtering techniques proposed by the authors demonstrate some effectiveness.
- The article presents a thorough and detailed set of experiments.

### Weaknesses
 - The proposed Question Preference Optimization (QPO) appears to be less effective; as shown in Figure 5, the difference between QPO and QFT is minimal, raising questions about the validity of QPO.

- This paper attempts to extract training data from models, similar to the approach of MAGPIE. Therefore, the authors should conduct a more fair and detailed comparison between Question Fine-Tuning (QFT) and direct prompting methods. In Figure 5, the authors generated 1 million question-response pairs using MAGPIE with Qwen2-Math-7B-Instruct as the "raw data" setting. However, the other settings filtered 2 million( from DeepSeekMath-QGen and Qwen2-Math-QGen) questions down to 1 million and applied a reward model to filter the responses. Consequently, it is difficult to determine whether QFT is more effective than the MAGPIE method or if the filtration of questions and responses is more effective.

- The ablation experiments are insufficient. The authors conducted experiments only on Llama3-8B, rather than comparing all four base models as presented in the main table. 

- The authors suggest that the data generation method proposed in this paper can produce diverse and high-quality questions at a lower cost. However, with advancements in open-source models, previous sample-driven and knowledge-driven question synthesis models can also be replaced with open-source models. Moreover, Qwen2-Math, as a response synthesizer, demonstrates superior mathematical capabilities compared to earlier versions of GPT-4. Therefore, it is difficult to assert that the data synthesis approach presented in this paper is superior to other methods in cost.

### Questions
- The authors should compare different base models in Figure 5 and Table 2.

- The experimental setup in the experimental module should be clearly presented; for instance, in Table 2, did the responses corresponding to questions from other datasets involve generating five responses and filtering down to one based on the reward model, or was only one response generated?

- The authors might discuss the effects of optimizing different question data volumes during QPO. Additionally, since the authors note that optimizing for both solvability and difficulty simultaneously in QPO is challenging, are there corresponding experimental results to support this?

- The author should probably compare the generated questions with the questions in the test set (n-grams or other methods) to prevent potential data leakage.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a scalable data synthesis method, ScaleQuest, for math reasoning. The augmented math datasets can enhance the model performance of mainstream open-source models such as Mistral, Llama3, DeepSeekMath, and Qwen2-Math. After finetuning the proposed dataset, the small open-source models can even outperform closed-source models such as GPT-4-Turno and Claude-3.5 Sonnet

### Strengths
1. This paper provides a cost-effective data synthesis method for math reasoning problems.   
2. The synthetic dataset can boost the performance of multiple open-source models in both in-domain and out-of-domain evaluation.

### Weaknesses
1. The main weakness of this paper is, that the proposed data synthesis pipeline is too complex and may be domain-specific. It includes the training in question fine-tuning, question preference optimization, the inference for solvability and difficulty check, reward scoring, etc. Although the API and training cost is not as expensive as GPT-4, this method is more time-consuming and requires extra effort to adapt to other domains. Specifically, the question fine-tuning stage requires training a new model for each domain, which adds significant overhead. The question preference optimization also relies on a model trained on math data, and its effectiveness in other domains is questionable. The multiple stages of filtering and scoring further complicate the process, making it difficult to isolate the impact of each component.
2. The proposed data synthesis method is only evaluated in the math domain. It is unsure whether this method can be easily adapted to other domains such as code or logical reasoning. Specifically, can the question finetuning and question preference optimization trained on the math domain be directly used for other domains, or the extra finetuning for each domain and each stage is needed? The paper does not provide sufficient evidence to support the generalizability of the proposed method. The reliance on domain-specific models for question generation and reward filtering raises concerns about the portability of the approach.
3. The experimental results are not easy to interpret:
(i) For the baselines with different synthetic datasets, are they finetuned on the same scale of training examples? It is unclear whether the performance gains are due to the proposed method or simply due to larger training datasets. A controlled experiment with the same number of training examples is needed to validate the effectiveness of the proposed method.
(ii) What does the Percentage and Accuracy in Figure 5 mean? Where is the legend of the left plot of Figure 5? The lack of clear definitions for these metrics makes it difficult to understand the results. The figure also lacks a legend, which further hinders the interpretation of the results.
(iii) What does the question quality in Table 2 refer to? The term 'question quality' is vague and needs to be defined more precisely. It is unclear what specific criteria are used to evaluate the quality of the questions.
4. There are many components in the data synthesis pipeline, but the impact of each component is not clear. For example, what if removing the question preference optimization and directly using the solvability filtering and difficulty sampling? This is different from the ablation study, which compares the performance w/ and w/o reward filtering while keeping all other components the same. The ablation study should systematically evaluate the impact of each component, including question fine-tuning, question preference optimization, solvability filtering, and difficulty sampling, to understand their individual contributions.

### Questions
There are plenty of LLMs used in the data synthesis pipeline: DeepSeekMath- 7B-RL , Qwen2-Math-7B-Instruct, GPT-4o-mini, GPT-4o, DeepseekMath-7B-Base, InternLM2-7B-Reward. Can you provide a Table for all the settings? Is there any specific reason to select different LLMs for different stages?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents ScaleQuest, a scalable and cost-effective data synthesis framework designed to enhance the mathematical problem-solving capabilities of large language models (LLMs). Motivated by the need for high-quality, large-scale data, the authors propose a two-stage synthesis process. Specifically, ScaleQuest employs Question Fine-Tuning (QFT) to activate question-generation (QG) capabilities in small base models and Question Preference Optimization (QPO) to improve question solvability and difficulty. This is followed by filtering for language clarity, difficulty, and solvability, as well as reward-based response selection to ensure high-quality outputs. Experiments demonstrate that models fine-tuned with the ScaleQuest dataset outperform several baselines on benchmarks, achieving substantial improvements in accuracy across in-domain and out-of-domain mathematical reasoning tasks.

### Strengths
1. ScaleQuest targets data synthesis for instruction tuning, focusing on affordable low-cost methods. This approach demonstrates significant cost savings (Section 3.4), making large-scale data creation more accessible for open-source communities.

2. The study includes thorough experimentation with multiple baselines, assessing both question and response quality across a total of four mathematical problem-solving benchmarks, thereby increasing the credibility of ScaleQuest.

3. The paper is well-structured and quite easy to follow, with sufficient implementation details to enhance reproducibility.

### Weaknesses
1. As claimed by the authors in Lines 17-20 and 76-80, the main contribution of the paper is the scalable synthesis method, ScaleQuest. However, the method heavily depends on domain-specific fine-tuning and specialized models, which raises questions about its generalizability and applicability to domains beyond mathematical reasoning. For instance, the authors use Question Fine-Tuning (QFT) and Question Preference Optimization (QPO) to optimize the question generation process within the target domain of mathematical reasoning. Furthermore, the method involves components like solvability filtering, difficulty sampling, and reward filtering, each relying on different models and a specialized fine-tuned difficulty scorer, which appear tailored to mathematical data construction. This reliance on fine-tuned, domain-specific models, while effective in the tested domain, makes it challenging to adapt ScaleQuest to broader applications, potentially limiting its utility as a general-purpose data synthesis method.

2. Additionally, the paper appears to make some overclaims regarding its scope and efficiency. While the title suggests an enhancement of "reasoning capability," the paper narrowly addresses mathematical reasoning tasks, with little consideration given to other reasoning types, such as causal, commonsense, or logical reasoning. The claim of using “small-size” models (Lines 18-19) is also somewhat misleading. Specifically, the QPO stage (Lines 199-202) requires a larger model, GPT-4o-mini, to achieve better preference-based filtering, suggesting that smaller models alone may not fully support the quality goals of ScaleQuest. The ablation results (Figure 5) further highlight the critical role of QPO, reinforcing the notion that the trade-off between model size and final data quality is not fully acknowledged, which impacts the efficiency claims of the method.

3. Lastly, despite the authors’ assertions that ScaleQuest-generated data significantly enhances performance across various benchmarks, the observed improvements are marginal. For instance, Table 1 shows only a slight average increase from 62.7 to 62.9 when comparing Qwen2-Math-7B-ScaleQuest to its baseline Qwen2-Math-7B-Instruct, even with a decrease in performance on the CollegeMath benchmark. These limited gains suggest that the effectiveness of ScaleQuest’s synthesized data may not justify its complexity. Consequently, these modest gains raise concerns about the practical value and impact of the ScaleQuest approach.

### Questions
1. How did the authors select the base difficulty filtering model for fine-tuning (Lines 222-239) and the reward filtering model (Lines 251-252)? Considering that filtering significantly impacts final data quality (Figure 5), further discussion of criteria for model selection, along with any experimental comparisons, would enhance clarity on whether these models represent optimal choices.

2. In Table 1, the term “Synthesis Model” in the header needs clarification. Does it refer to the model used for both question and response generation, or only response generation? This ambiguity is notable, especially as fine-tuned models such as Deepseek-QGen and Qwen2-Math-QGen are absent from the table. 

3. The left bar chart in Figure 5 has a confusing y-axis. Does the percentage indicate solvable/non-solvable or easy/difficult ratios? If it reflects these ratios, how does this relate to the five difficulty levels introduced in Lines 377-406? Detailing this connection would make the difficulty and solvability metrics clearer.

4. Lastly, while evaluating synthesized data via difficulty distribution and solvability is helpful, a rigorous human evaluation on a random subset would better demonstrate ScaleQuest’s quality. Including human assessments of clarity, coherence, and real-world relevance could provide a nuanced verification of the synthesized data's effectiveness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a synthetic training data generation method for mathematical LLMs. Based on two small models at a 7B scale, the authors achieve state-of-the-art performance than other models trained with the data from larger LMs. The proposed method including question supervised fine-tuning, question preference tuning and reward-score-based selection.

### Strengths
As for the method, ScaleQuest generates questions independently from scratch, removing dependency on existing question datasets, which enhances question diversity and supports scalability. Also, the paper integrates comprehensive filtering techniques, including language, solvability, and difficulty sampling, which could be a good reference for future efforts in data filtering.

The presentation is very clear, the workflow of the method is easy to follow. All the details such as prompts are all clearly given. The authors said they will release the data and code, which will be a useful resource to the community.

### Weaknesses
The main experiments in Table 1 are somehow not very fair. Some of the baseline methods contain less data than the used dataset in the paper. 

In Table 1, it seems that Qwen2-Math-7B-ScaleQuest achieves similar performance with Qwen2-Math-7B-Instruct, I am wondering if their performance is similar on OOD test sets like GSM-hard (https://huggingface.co/datasets/reasoning-machines/gsm-hard) and MathChat (https://github.com/Zhenwen-NLP/MathChat). I would like to see if Qwen2-Math-7B-ScaleQuest is over-fitting on GSM and MATH style questions.

For the efficiency result, it seems that the cost is similar to (even slightly higher) GPT-4o mini if we put that in the table. I am wondering why the authors choose models like Qwen2-Math-7B instead of GPT-4o mini for solvability & difficulty check, etc.

### Questions
Typo: Filering -> Filtering in line 215

In Figure 5, it seems that QPO is less effective. Does the author try the combination of QFT and reward filtering only?

I am curious about the effectiveness of Solvability Filtering and Difficulty sampling. For Solvability Filtering, it seems that the final dataset still does not have perfect quality but produces a good performance. So I am curious about the influence of the quality. For difficulty sampling, I am not sure why we need to fit certain difficult distributions.

### Soundness
3

### Presentation
3

### Contribution
2
