# Math for AI: On the Generalization of Learning Mathematical Problem Solving

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 3, 6

## Abstract
There has been a growing interest in enhancing the mathematical problem-solving (MPS) capabilities of LLMs. While some researchers focus on developing specialized math models to advance AI for math, others study mathematical reasoning with a ''math for AI'' perspective, positing that integrating mathematical reasoning data could enable LLMs to perform complex reasoning more broadly. This hypothesis draws from neuroscience studies which show that solving mathematical problems aids in the development of general reasoning skills in humans. The concept of ''math for AI'' has gained particular relevance as the research community increasingly focuses on complex reasoning -- Given the scarcity of complex and lengthy chain-of-thought data, MPS emerges as a prime candidate for collecting or synthesizing substantial volumes of intricate thought processes, thus serving as a potential key resource for enhancing general complex reasoning. However, it remains unclear whether skills acquired through learning MPS can extend to other reasoning tasks or merely improve MPS-specific benchmark scores. 
In this paper, we present a comprehensive empirical analysis to address this question.
Specifically, we explore three prevalent methods for improving MPS: (1) continual pretraining on mathematical text; (2) instruction pretraining on large-scale QA pairs synthesized from raw text; and (3) instruction tuning on MPS datasets. 
Through controlled experiments and evaluations across seven distinct reasoning domains, 
while no approaches consistently generalize across all non-mathematical tasks, both continual pretraining and instruction pretraining outperform instruction tuning, with continual pretraining often yielding greater gains when effective.
These findings indicate that most readily available data sources do not support the ''math for AI'' objective in enhancing non-MPS tasks. Identifying which data sources best contribute to the acquisition of complex reasoning skills remains a crucial question for future research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper determines whether training on step-by-step mathematical explanations can improve a model’s general problem-solving ability. Specifically, the authors test three different training strategies: continual pretraining, instruction pretraining, and instruction tuning with different math problem-solving datasets. For all three methods, the authors consider a two-stage training approach, where they first train a model with a math dataset and then train with UltraChat. Additionally, for the third approach, the authors mix the math dataset with UltraChat and also benchmark the performance.  They find that although these training methods improve performance in mathematical reasoning, only continual pre-training with mathematical texts can enhance a model’s general problem-solving ability. The authors then go on to examine whether training on other non-mathematical problem-solving datasets could perhaps improve a model’s general reasoning ability but demonstrate that these too fall short.

### Strengths
I found the paper to have strong clarity and the authors have chosen an interesting problem of trying to examine which datasets and training approaches could improve an LLM’s general reasoning ability. From this, the authors did a thorough job of examining the effect of different 
training strategies with different datasets. They did an exhaustive job of benchmarking various mathematical and non-mathematical reasoning datasets with the post-trained LLMs.  Because of this, all of the claims are very well-supported. 

I also liked how the authors examined the effect of training on other step-by-step explanations of datasets and determined if that had any effect on improving the non-mathematical capability. This showed that this is truly a difficult problem to solve.

### Weaknesses
The major weakness in this paper is that they only attempt pretraining and finetuning-based approaches and that too with only two models. I am not sure if this is because the authors had limited computational resources, but if not, it would be interesting to examine the performance of LLMs with varying mathematical/reasoning capabilities and not just Mistral-7B and DeepSeek-Coder. 

I also think that the authors should try to examine methods beyond just continual pretraining and fine-tuning. For example, they should try reinforcement learning approaches as well which have demonstrated improved reasoning capabilities with models such as GPT-o1-preview. 

Finally, this paper is mostly focused on “correlations” as opposed to the “causations” as to why certain training approaches and datasets succeed or fail at improving a model’s generalizability when trained on mathematical problem-solving datasets. For this paper to have a greater impact, the authors should elaborate on the existing discussions as to why certain training methods and datasets do not improve an LLM’s general reasoning ability.

### Questions
Based on the limitations section, I have the following questions:

Are the findings from your paper model agnostic? If not, what kinds of models benefit from this sort of training and with sorts of datasets?  
What kinds of other training-based approaches could be done to improve the score? 
If you look at this paper in Figure 2: https://arxiv.org/pdf/2401.00812, the authors have a more fine-grained taxonomy as to the specific skills that training with code has helped LLMs with. Hence, I was wondering if there is any correlation to the specific skills (i.e. task decomposition/planning) that an LLM has after continual pre-training which is why the model shows an improvement in general reasoning tasks? You might have to manually inspect the LLM responses for this. 
Can you explain further as to why certain training methods with their corresponding datasets succeed or fail at improving an LLM’s general reasoning ability?

### Soundness
3

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
3

### Summary
This paper investigates the generalization of learning mathematical problem-solving for LLMs. It explores three training strategies: continual pretraining on mathematical text, instruction pretraining on diverse QA pairs, and instruction tuning on MPS datasets. Through experiments across seven reasoning domains, it finds that continual pretraining on raw mathematical text can improve performance on most non-MPS reasoning tasks, while other methods have limited generalization. It also conducts a pilot study on non-MPS SFT datasets with less promising results.

### Strengths
1. The experimental results suggest only continual pretraining on MPS data is useful to general reasoning tasks. The conclusion may be valuable to those we want to improve reasoning capability of LLMs.
2. The experiments are well designed.
3. The experiments are abundant.

### Weaknesses
1. This work lacks of novelty. It only conducts several experiments and comes up with a conclusion which is align with my assumption.
2. The result analysis is not deep enough. The readers may want to know why only continual pretraining works. Are there any cluse from th mechanical interpretability perspective, why some the instruction pretraining works while some are not, why all the instruction tuning fails.

### Questions
Need more deep analysis to see are there any insightful findings.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies whether improvements in LLMs' mathematical reasoning capabilities can generalize to broader reasoning domains. Specifically, it examines various training approaches (continual pre-training and instruction tuning) on math-related data and determine if enhanced mathematical performance transfers to tasks like symbolic reasoning, logical reasoning, and commonsense reasoning. This investigation addresses the "math for AI" hypothesis, which posits that training on mathematical reasoning could enhance LLMs' general reasoning capabilities.

The authors conduct controlled experiments comparing three training paradigms: (1) continual pre-training on mathematical text, (2) instruction pre-training on diverse QA pairs, and (3) instruction tuning on mathematical problem-solving datasets. They evaluate each approach's generalization to multiple non-mathematical reasoning domains. Their key finding suggests that only continual pre-training demonstrates meaningful generalization, showing improvements in 3 out of 5 non-mathematical domains.

### Strengths
The paper studies an interesting and an important question in the development of LLMs. Pushing LLMs’ capabilities on math datasets is indeed an increasingly popular research topic.  And this paper presents a timely study.

The experiments consider multiple training paradigms for improving math reasoning and evaluate the generalization performance on an array of datasets other than math.

The paper is well-written and easy to follow.

### Weaknesses
My major concerns include 1) the categorization of non-math datasets and the interpretation of results might be problematic 2) the conclusions are probably overstated

First, regarding the non-math dataset categorization, the paper classifies reasoning tasks into logical reasoning, STEM reasoning, commonsense reasoning, and symbolic reasoning. I think STEM reasoning should not be juxtaposed with the other categories. STEM reasoning interweaves mathematical reasoning, logical reasoning, and domain-specific STEM knowledge. It is not a good choice to treat as a distinct reasoning category.

More importantly, the STEM reasoning evaluation is based on GPQA and MMLU-STEM. MMLU-STEM is heavily intertwined with mathematical reasoning. MMLU-STEM contains a portion of problems requiring mathematical computation (like physics and finance problems which require solving some equations; Sprague et al., 2024). It is difficult to distinguish whether performance improvements indicate generalization or the improvements are still about mathematical abilities.

Furthermore, the paper's main claim that "continual pretraining generally improves non-math reasoning" (line 327) is drawn from improvements in 3 out of 5 domains. If we exclude STEM reasoning, this claim becomes questionable. Even considering all domains, showing improvement in 3 out of 5 areas probably does not suggest "significant" generalization, especially given the large performance degradation in commonsense and agent reasoning tasks.

Additionally, the paper could benefit from more in-depth analysis. While it presents performance numbers and draws broad conclusions, it does not provide more in-depth insights. For instance, If the paper claims major improvements on specific tasks, the paper could have some analysis which specific types of data points show improvement and provide potential explanations for these gains.

### Questions
See weakness

### Soundness
2

### Presentation
3

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
This paper investigates whether training on mathematical problem-solving (MPS) enhances LLMs' general reasoning capabilities. Through comprehensive empirical analysis of three training approaches (continual pretraining, instruction pretraining, and instruction tuning), the authors evaluate performance across seven reasoning domains. The study implements both two-stage and mix-data training strategies to assess how math-related training integrates with general model development. Their findings show that while continual pretraining on mathematical texts can improve broad reasoning capabilities, other approaches primarily enhance only MPS-specific performance, indicating that most current math datasets don't effectively support general reasoning enhancement. This work provides insights into the "math for AI" hypothesis and highlights the need for better data sources to develop general reasoning capabilities.

### Strengths
1. The research topic is novel and valuable. Humans can enhance their overall reasoning abilities by learning mathematics and practicing problem-solving. Inspired by this, the paper explores whether training AI models to improve their mathematical problem-solving skills could similarly enhance their broader general reasoning capabilities. By distinguishing between the "AI for math" and "math for AI" perspectives, this work provides a new evaluation perspective.
2. Given the increasing focus on the complex reasoning abilities of LLMs and the scarcity of high-quality reasoning datasets, constructing large-scale, high-quality mathematical reasoning datasets and training LLMs would require enormous resources. Therefore, researching "math for AI" to enhance AI's reasoning capabilities beyond mathematical problem-solving aligns with the goals of AI development and can improve data utilization efficiency.
3. The study presents a thorough experimental framework comparing three distinct training approaches. For continual pretraining, the researchers utilized RhO-Math and DeepSeekMath models, while instruction pretraining was conducted using the MammoTH2 model. Instruction tuning experiments employed Math-COT SFT and Math-POT SFT.  Through rigorous evaluation, the study yielded several significant findings.

### Weaknesses
1. The technical contributions seem to be limited. While the paper conducts extensive research across several models and datasets, it fails to establish a universal framework for evaluating AI's general reasoning capabilities in the context of "math for AI". This limitation reduces the study's potential impact on future assessments of AI's general reasoning abilities.
2. In the section "WHAT OTHER DATA SOURCES CONTRIBUTE TO REASONING," the paper does not provide effective methodologies or meaningful insights for constructing datasets that could enhance AI's general reasoning capabilities.
3. The classification of tasks relies solely on input-output format distinctions, without implementing deeper similarity detection or filtering mechanisms for the actual data content. This oversight could lead to data leakage between MPS and other tasks. The potential overlap between mathematical and general reasoning datasets might result in misleading conclusions about reasoning skill transfer.

### Questions
1.	In Table 1 of the main experimental results (3) Instruction tuning on MPS datasets, for the MPS results, why is the COT effect better than the POT, and why does the mixed method perform much better than the 2-stage method?
2.	Can you provide specific examples to demonstrate how mathematical training can improve or deteriorate different reasoning abilities, which can clarify the limitations of mathematical training and offer a qualitative analysis of the reasoning patterns developed through different training methods?
3.	What data do you think would really improve LLM's ability to reason over a wide range of tasks? How can this generalized reasoning capability be better assessed automatically?

### Soundness
3

### Presentation
3

### Contribution
3
