# Adapting Large Language Models via Reading Comprehension

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
We explore how continued pre-training on domain-specific corpora influences large language models, revealing that training on the raw corpora endows the model with domain knowledge, but drastically hurts its prompting ability for question answering. Taken inspiration from human learning via reading comprehension--practice after reading improves the ability to answer questions based on the learned knowledge--we propose a simple method for transforming raw corpora into reading comprehension texts. Each raw text is enriched with a series of tasks related to its content. Our method, highly scalable and applicable to any pre-training corpora, consistently enhances performance across various tasks in three different domains: biomedicine, finance, and law. Notably, our 7B language model achieves competitive performance with domain-specific models of much larger scales, such as BloombergGPT-50B. Furthermore, we demonstrate that domain-specific reading comprehension texts can improve the model's performance even on general benchmarks, showing the potential to develop a general model across even more domains. Our model, code, and data are available at https://github.com/microsoft/LMOps.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces an approach for continuing the pretraining of Large Language Models (LLMs) on domain-specific corpora. Initially, the authors find that conventional domain-adaptive pretraining enhances knowledge probing while detrimentally affecting the model's prompting ability. Subsequently, they propose transforming domain-specific documents into a reading-comprehension style format. In this format, certain sentences are altered via mining patterns to pose NLP tasks such as summarization and commonsense reasoning, accompanied by their respective answers. The experiments, spanning the biomedical, finance, and law domains, demonstrate that the proposed approach yields marginal improvements in the performance of LLMs on domain-specific tasks.

### Strengths
- The proposed approach is straightforward yet effective in enhancing performance on domain-specific tasks, which has potential applicability to other models and domains.
- The experiments include three representative domains and six mining tasks, which may have sufficient coverage in terms of domains and tasks.
- The paper is well-written and easy to follow.

### Weaknesses
 - In Table 4, the performance improvements appear marginal to me (3% in biomedicine, 4.8% in finance, and 4.3% in law). I am uncertain whether the benefits gained from using the proposed approach justify the effort required to transform corpora into reading comprehension texts.
- The authors only use the LLaMA 7B model for verifying their proposed method. It remains unclear whether the approach is similarly effective for smaller and larger models.

### Questions
- Texts in corpora may possess their own document structure, and mining NLP tasks could potentially disrupt it, impacting readability and coherence. Have the authors manually verified whether their transformation is effective without compromising the integrity of the text?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on the investigating domain-adaptation pretraining method for LLMs, where they continued training on domain-specific corpora and found the approach hurts the LLMs' prompting ability. Thus, the author proposes to convert the corpora into reading comprehension texts to preserve the prompting performance. The experiments show the effectiveness of the method in three different domains (biomedicine, law, and finance).

### Strengths
- The proposed prompts are very effective, as showed with a significant zero-shot performance improvement across 3 domains, and the 7B model used in the experiment can outperform larger models (50B).
- The paper is well-written. The author puts a comprehensive details on the experiments and analysis.

### Weaknesses
 - Some ablation studies are essential to understand the effectiveness of the components (e.g., how the verbalizer affects the performance)
- The baselines are not comparable to the results reported by the authors. E.g., GPT-J 6B. It will be great to have the AdaptLLM result on top of the baselines wherever the models are publicly available.

### Questions
- How did you choose the set of strings for the verbalizer?
- Are there any analyses or findings on why the model performance improvement on domain "law" is the least? 
- Does the approach benefit another type of models? e.g., encoder-decoder model? or other decoder-only models?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to adapting LLMs via reading comprehension for QA. The authors conduct extensive experiments on various QA datasets. The results show the effectiveness of the proposed method. The paper is well written and the solution is clear.

### Strengths
1. The authors conduct extensive experiments on various QA datasets. The results show the effectiveness of the proposed method.
2.  The paper is well written and the solution is clear.

### Weaknesses
1. I download the Supplementary Material and find that there are many missing files, such as codes and the full data sets. 
2. The implemtation details are not clear, such as GPU and memory size and  the parameters.

### Questions
1. I download the Supplementary Material and find that there are many missing files, such as codes and the full data sets. 
2. The implemtation details are not clear, such as GPU and memory size and  the parameters.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper reveals that domain-specific pre-training greatly reduces LLMs'  prompting ability. The authors introduce a method to transform raw texts into comprehension tasks, aiming to enhance LLM's domain knowledge without sacrificing prompting skills. Experiment results show their 7B model is competitive with larger models.

### Strengths
1. Interesting observation: Pre-training on domain-specific datasets leads to a decline in LLM's prompting ability.
2. The proposed idea is straightforward, simple, and has the potential for broad applicability with clear motivation.
3. Experimental findings indicate that domain-specific reading comprehension texts enhance the model's performance.

### Weaknesses
1. The novelty seems somewhat constrained, especially regarding the idea of incorporating reading comprehension tasks during the pre-training phase, which appears similar to the following paper:
RECKONING: Reasoning through Dynamic Knowledge Encoding. 
2. The authors conducted experiments only on the 7B model. It's uncertain whether consistent results would be observed on larger-scale models, and it's unclear if the proposed method is effective on models after RLHF. (However, I think this weakness doesn't undermine the contribution.)

### Questions
I'm confused why pre-training on domain-specific knowledge leads to a decrease in LLM's prompting ability. Could you clarify?
Especially in the explanation, does the term 'input-output patterns' pertain to limited data patterns or is it referring to something else?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
