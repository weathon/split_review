# Instruct-SkillMix: A Powerful Pipeline for LLM Instruction Tuning

- Decision: Accept
- Scores: 3, 5, 6

## Abstract
We introduce \instructSM{}, an automated approach for creating diverse, high quality SFT data for instruction-following. The pipeline involves two stages, each leveraging an existing powerful LLM: (1) {\em Skill extraction}: uses the LLM to extract core ``skills'' for instruction-following by directly prompting the model. This is inspired by ``LLM metacognition'' of \cite{didolkar2024metacognitive}; (2) {\em Data generation:} uses the powerful LLM to generate (instruction, response) data that exhibit a randomly chosen pair of these skills. Here, the use of random skill combinations promotes diversity and difficulty. The estimated cost of creating the dataset is under \$600.

Vanilla SFT (i.e., no PPO, DPO, or RL methods) on data generated from \instructSM{} leads to strong gains on instruction following benchmarks such as AlpacaEval 2.0, MT-Bench, and WildBench. With just $4$K examples, \llamaiii{8} achieves 42.76\% length-controlled win rate on AlpacaEval 2.0, a level similar to  frontier models  like Claude 3 Opus and LLaMA-3.1-405B-Instruct. 

Ablation studies also suggest plausible reasons for why creating open instruction-tuning datasets via naive crowd-sourcing has proved difficult. In our dataset, adding $20\%$ low quality answers (``shirkers'') causes a noticeable degradation in performance.

The \instructSM{}
pipeline seems flexible and adaptable to other settings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces INSTRUCT-SKILLMIX, a pipeline for creating instruction-tuning datasets using large language models. The method involves two stages: (1) extracting instruction-following skills using an LLM's metacognitive abilities, and (2) generating synthetic (instruction, response) pairs using random combinations of these skills. Using just 4K examples, the authors demonstrate that base models fine-tuned on this data achieve competitive performance on instruction-following benchmarks compared to much larger models.

### Strengths
The paper presents a novel approach to synthetic data generation that achieves strong results with only 4K examples, suggesting an efficient path forward for instruction tuning. The empirical validation is well-designed, testing across multiple benchmarks and models while including careful ablation studies that isolate the effects of different components. 

The method is cost-effective, requiring only about $600 compared to traditional human annotation approaches. 

The authors provide some analysis of how low-quality data affects model performance, offering practical insights for dataset creation. 

The paper also test both their preferred method and a seed-dataset dependent variant, providing comparative insights.

### Weaknesses
The paper's most significant limitation is the performance plateau at 4K examples, with no clear explanation or analysis of learning curves as dataset size increases. This is compounded by limited investigation of whether different architectures or model sizes might hit different ceilings. 

The evaluation methodology relies heavily on AlpacaEval 2.0 and lacks assessment of long-form generation and multi-turn conversations. The use of both teacher and grader models from the same model family (GPT-4) raises concerns about potential systematic biases. 

Also, the methodology lacks a principled approach for determining the optimal number of skills or combinations, and provides no systematic quality metrics for the generated data. 

The paper provides limited investigation of how different teacher models might affect results. Lack of this raises questions about the method's generalizability. 

The relationship between skills and model performance remains inadequately explored, with no clear metrics for assessing skill quality or coverage.

### Questions
Have you investigated whether different model architectures or sizes hit the 4K example ceiling at different points?

Could you explain the choice of k=2 for skill combinations? Have you explored other values?

How would the method perform with different teacher models (e.g., Claude, PaLM)?

Would it be possible that combining synthetic data with human annotations potentially break through the 4K example ceiling?

Could you elaborate on potential approaches for quality control in the data generation process?

Could you provide analysis of model performance on longer-form tasks and multi-turn conversations?

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
The authors propose a new instruction tuning data generation pipeline, INSTRUCT-SkillsMIX. They prompt a strong LLM to identify some key instruction following skills. They then use these skills to produce useful instruction following data. They show strong results on instruction following benchmarks where an LLM is used as a judge.

### Strengths
- This paper shows very strong performance on benchmarks where LLMs are used as a judge.
- The InstructSkillMix framework is novel and interesting. Moreover, it does not require any seed data, which is beneficial.

### Weaknesses
- The baseline methods are not fair: the main comparison is to Alpaca 52K, which is really old and known to be a low quality dataset. I think the authors should try comparing their dataset to stronger datasets such as ShareGPT with the responses regenerated by GPT4-Turbo.
- In my opinion, section 1.1 is somewhat misleading. The authors (in line 70-75) say it is a mystery why public instruction tuning does not match the performance of proprietary instruct models. However, these proprietary models are trained in a variety of stages, and with distillation and RL techniques. It is not expected that instruction tuning alone can match the performance of proprietary models.
- Table 4 suggests that the main reason for the good performance of InstructSkillMix is that a stronger model is used for distillation compared to previous IFT datasets. With the same judge, Alpaca-1K longest performs similarly to InstructSkill Mix (although Alpaca 1K longest is a weak dataset in my opinion: instructions are created using text-davinci-003). Alpaca-1K longest does perform worse on the length-controlled benchmark, but this is not a fair comparison since Alpaca-1K longest is specifically biased to encourage longer responses. 
- The authors claim that InstructSkillMix is a more performant data generation method than UltraChat and Vicuna (line 511). Although InstructSkillMix seems to be a strong method, my guess is that the primary reason that InstructSkillMix outperforms UltraChat and Vicuna is due to a stronger teacher model. If the authors want to make this claim, I think they should regenerate responses from UltraChat and ShareGPT using the same teacher model InstructSkillMix uses.
- In my opinion relying only on AlpacaEval 2.0 and MTBench is a bit limited. It would be beneficial for the authors to evaluate their models on other tasks, including mathematical reasoning (MATH, GSM8K), instruction following (IFEval), and knowledge benchmarks (MMLU).

### Questions
- Can you compare performance to ShareGPT with the responses regenerate with GPT4-Turbo?
- Can the authors discuss weakness 3?

### Soundness
3

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
4

### Summary
This paper focuses on constructing high-quality data for enhancing base LLMs’ instruction following capability. To achieve this goal, the authors propose a novel pipeline, called Instruct-SkillMix, which naturally combines diversity and difficulty in the data generation process. SFT with the resulting SFT dataset leads to very impressive performance gains on several established benchmarks. In particular, the data generation is fully automatic and the size of dataset can scale up easily.

### Strengths
- It finds that directly prompting a strong LLM to identify crucial skills achieves better performance than extracting skills from existing IFT datasets.
- The performance of using merely thousands of Instruct-SkillMix data is impressive.
- The data generation pipeline is fully automated and has nearly no human intervention.
- It conducts detailed ablation studies and shows the contributions of different components.
- It reveals that even a small amount of low-quality data greatly harms the instruction following performance.

### Weaknesses
- The type of queries and topics could be relevant to coverage of data. I think it might be worth to do ablation study on the query and topic types.

### Questions
Kindly refer to the weaknesses.

### Soundness
4

### Presentation
3

### Contribution
4
