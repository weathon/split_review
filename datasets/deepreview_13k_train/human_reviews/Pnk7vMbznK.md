# Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing

- Decision: Accept
- Scores: 3, 8, 6

## Abstract
High-quality instruction data is critical for aligning large language models (LLMs). Although some models, such as Llama-3-Instruct, have open weights, their alignment data remain private, which hinders the democratization of AI. 
High human labor costs and a limited, predefined scope for prompting prevent existing open-source data creation methods from scaling effectively, potentially limiting the diversity and quality of public alignment datasets.
Is it possible to synthesize high-quality instruction data at scale by extracting it directly from an aligned LLM?
We present a \textit{self-synthesis} method for generating large-scale alignment data named \dataname{}. 
Our key observation is that aligned LLMs like Llama-3-Instruct can generate a user query when we input only the pre-query templates up to the position reserved for user messages, thanks to their auto-regressive nature. 
We use this method to prompt Llama-3-Instruct and generate 4 million instructions along with their corresponding responses. We further introduce extensions of \dataname{} for filtering, generating multi-turn, preference optimization, domain-specific and multilingual datasets.
We perform a comprehensive analysis of the \dataname{}-generated data. To compare \dataname{}-generated data with other public instruction datasets (e.g., ShareGPT, WildChat, Evol-Instruct, UltraChat, OpenHermes, Tulu-V2-Mix, GenQA), we fine-tune Llama-3-8B-Base with each dataset and evaluate the performance of the fine-tuned models. Our results indicate that using \dataname{} for supervised fine-tuning (SFT) solely can surpass the performance of previous public datasets utilized for both SFT and preference optimization, such as direct preference optimization with UltraFeedback. We also show that in some tasks, models supervised fine-tuned with \dataname{} perform comparably to the official Llama-3-8B-Instruct, despite the latter being enhanced with 10 million data points through SFT and subsequent preference optimization. This advantage is evident on alignment benchmarks such as AlpacaEval, ArenaHard, and WildBench.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work proposes Magpie, which is a way to prompt aligned LLMs to generate alignment datasets. Unlike most previous studies in this area (LLM-generated alignment data), Magpie removes the need of a seed set of instructions and heavy prompt engineering efforts. Instead of prompting aligned LLMs with an meaningful instruction, Magpie directly puts the "pre-instruction" token, i.e. one of the formatting delimiter tokens, to LLMs and let the LLMs generate single-turn instructions "freely". With limited extra prompt engineering efforts and an extra reward model, the method can be extended to multi-turn, multi-lingual, multi-domain data, and DPO cases (preference data). The experimental results indicate that datasets generated through Magpie are of high quality, yielding superior performances on AlpacaEval2, ArenaHard, and WildBench, as well as comparable performances on general benchmarks like MMLU, GSM8K, etc.

### Strengths
- The proposed method is simple yet effective, according to the experimental results. In particular, the generated DPO data show a significant performance boost.

- The ablation study is comprehensive, considering different settings/datasets/baselines as well as different aspects like domain-specific capabilities and safety, though the result analysis lacks depth.

### Weaknesses
 - The presentation can be improved by putting more experimental results in the main context instead of the appendix. The proposed method is simple and easy to understand, similar to most prompt engineering related studies. The experimental results along with analysis and hypothesis test are the most important. For example, Section 3 is less important than Appendix F in terms of demonstrating the method's pros and cons.

- The experiments are well designed but lack deep analysis, which leaves many questions unanswered and makes it hard for other researchers to understand the method's best use cases and limitations. Please refer to Questions for details.

- For those most understanding results, e.g. surpassing GPT-4-Turbo(1106) on AlpacaEval 2, qualitative results are needed, i.e. random samples of actual generations for those benchmarks from all models in comparison. It is known that LLM-based judge could be biased and misleading.

- It would be better to add more alignment benchmarks like IFEval.

### Questions
1. It is not clear how the model used to generate data affects the final performance. The experimental results show that MAGPIE-Pro-300K-Raw has limited improvements over MAGPIE-Air-300K-Raw. This is counterintuitive and needs more insights.

2. Following up above, one possibility is that the base model is the same (llama-8b). From this point of view, the relationship between the model to be aligned and the model to generate data is crucial. More analysis is required.

3. We can also see that MAGPIE-Pro-300K-Filtered show much better performances when used on Llama than QWen. Of course, this could mean Llama base model is better, but could also be limitations of the proposed method. The proposed method essentially relies on the model itself to control the diversity of generated instructions, which is controlled by the pre-training data. If the model to be aligned was trained with the same pre-training data, we can intuitively expect better performances and less hallucination. If that is the case, it becomes kind of a chicken-egg thing, limiting the usefulness to the proposed method.

4. Why is a separate two-step process necessary? The aligned model should be able to generate instruction and response in one pass?

5. The DPO results are surprisingly good. How does the reward model's quality affect the final performances?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a new dataset for instruction fine-tuning and preference optimization called Magpie. The dataset is curated by prompting either LLama-3-70B-Instruct or LLama-3-8B-Instruct with the pre-query template or user tags and relying on the next token prediction ability of the model to elicit instructions. The instructions collected are then used to gather responses from LLMs. To generate instruction & responses that are multiturn or relevant to a certain task, the authors add relevant system prompts to steer the model ouptuts. Experiments across multiple baseline datasets, base models and comparison on multiple benchmark shows that effectiveness of Magpie dataset. The paper also has qualitative analysis highlighting various attributes of the dataset.

### Strengths
1. The paper introduces a simple & cost effective method of generating alignment data at scale, without relying on closed models or expensive human annotations.
2. Results on Alpaca Eval & Arena hard show significant improvements compared to other baseline datasets.
3. The paper presents an exhaustive quantative & qualitative experiments on question difficulty, safety, task categories, etc to highlight the attributes in Magpie.
4. The authors also experiments with various filtering configuration to improve the quality of final set of instructions.

### Weaknesses
1. The Magpie dataset is not conversational in nature. The MT variant of the dataset has at maximum 2 turns. In contrast, datasets like Ultrachat, Open Assistant and WildChat are multi-turn with maximum upto 7-8 turns. Also, the paper has no experiments or analysis on conversational benchmark and multi-turn nature of Magpie in comparison to existing datasets.
2. The paper has very limited improvements on OpenLLM leaderboard in Table 3 when compared to improvements in Table 2. Why is this the case, more dicussion around this is needed.
3. The paper does not have any analysis on contamination or information leakage in the dataset for the evaluation benchmarks used. Although the dataset is purely sythetic, and does not use any seed data the chances of leakage are less, but as there is no control over what the LLM generates, the chances that LLM results in generic instructions that end up being similar to evaluation datasets are high.
4. The method for generating questions is not controlled at all. The method relies only on the next token prediction, which might lead to simple instructions. The only way to steer the generation process is through system prompts, but it is hard to judge how effective is that, as the paper has no ablations on system prompts.
5. As the generation method is fully un-controlled, how does its ensures diverse instructions? T-SNE plot in figure 7 or the similarity analysis in Figure 3 using all-mpnet-base-v2 model is not enough to gauge the diversity.
6. The paper mentions that the method can be used to generate domain specific and multilingual datasets in the abstract. However, there are no evaluations on multilingual or domain specific data.

### Questions
Based on the Weaknesses, the questions are as follows:
1. How does the performance of Magpie look on multiturn benchamark? 
2. Does Magpie generation process even scale for longer turns?
3. Why there are limited improvements in Table 3 in comparison to massive improvements in Table 2?
4. As the data generation process is un-contolled, contamination analysis in Magpie datasets would be helpful.
5. How effective are system prompts for providing some control over the generation process? Is there any way to measure that? Are there any domain specific results?
6. How the generation process ensures diversity of instructions?

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
4

### Summary
MAGPIE is a scalable method for synthesizing high-quality instruction data from aligned large language models (LLMs) without requiring prompt engineering or seed questions. By leveraging the auto-regressive nature of models like Llama-3-Instruct, MAGPIE efficiently generates diverse instruction-response pairs through an automated two-step process, extendable to multi-turn, domain-specific, and multilingual datasets. Extensive analysis shows that models fine-tuned with MAGPIE-generated data outperform those using public datasets and can rival proprietary models fine-tuned on much larger datasets. MAGPIE’s versatility is further demonstrated through extensions for preference optimization and task-specific data generation, making it a significant contribution to scalable LLM alignment and democratized AI research.

### Strengths
- Good contribution to open source community as the dataset is quite large and diverse
- Interesting finding that aligned LLMs can be used to generate synthetic user instructions with just a system prompt
- Detailed insights on the generated SFT and Alignment pairs were presented
- The framework would be very useful for the open source community
- Authors also present a solution to overcome some limitations of the magpie dataset by developing a booster dataset

### Weaknesses
 - Good contribution to open source community as the dataset is quite large and diverse
- Interesting finding that aligned LLMs can be used to generate synthetic user instructions with just a system prompt
- Detailed insights on the generated SFT and Alignment pairs were presented
- The framework would be very useful for the open source community
- Authors also present a solution to overcome some limitations of the magpie dataset by developing a booster dataset

 - LLMs are typically trained (loss is computed) only on the assistant turns (during SFT, DPO, RLHF etc) and it is not clear how aligned models are able to produce user instructions. The paper does not provide enough insights to understand this. While this may not be directly in scope of the paper, it would help in increasing confidence in the presented approach.

### Questions
An important aspect of the work is the fact that aligned LLMs can generate user prompts with just a system prompt. 

For instance, the below system prompt would help generate user prompts for code related tasks.

"You are an AI assistant designed to provide helpful, step-by-step guidance on coding problems. The user will ask you a wide range of coding questions. Your purpose is to assist users in understanding coding concepts, working through code, and arriving at the correct solutions"

If an LLM can indeed produce a lot of diverse user prompts when sampled correctly, the novelty would seem limited. The work does go into depth on filtering etc. However fact remains that the LLM is able to generate most of the prompts. If this point can be addressed, the work would definitely be very convincing.

### Soundness
3

### Presentation
4

### Contribution
3
