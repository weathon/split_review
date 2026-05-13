# Instruction-tuned LLMs with World Knowledge are More Aligned to the Human Brain

- Decision: Reject
- Scores: 3, 6, 3, 5

## Abstract
Instruction-tuning is a widely adopted method of finetuning that enables large language models (LLMs) to generate output that more closely resembles human responses to natural language queries, in many cases leading to human-level performance on diverse testbeds. However, it remains unclear whether instruction-tuning truly makes LLMs more similar to how humans process language. We investigate the effect of instruction-tuning on LLM-human similarity in two ways: (1) brain alignment, the similarity of LLM internal representations to neural activity in the human language system, and (2) behavioral alignment, the similarity of LLM and human behavior on a reading task. We assess 25 vanilla and instruction-tuned LLMs across three datasets involving humans reading naturalistic stories and sentences, and discover that instruction-tuning generally enhances brain alignment by an average of 6%, but does not have a similar effect on behavioral alignment. To identify the factors underlying LLM-brain alignment, we compute the correlation between the brain alignment of LLMs and various model properties, such as model size, performance ability on problem-solving benchmarks, and ability on benchmarks requiring world knowledge spanning various domains. Notably, we find a strong positive correlation between brain alignment and model size (r = 0.95), as well as performance on tasks requiring world knowledge (r = 0.81). Our results suggest that making world knowledge in LLMs more accessible via instruction-tuning also yields neural representations more similar to those of the human language system.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the correlation between instruction-tuned LLMs and human similarity in the field of neuroscience by examining brain alignment and behavioral alignment. The authors evaluate 25 LLMs on a reading task to identify the effects of instruction tuning LLMs in terms of human language processing. Instruction turned LLMs have higher brain scores than vanilla LLMs, and further analyzed the properties of LLMs that contribute high alignment and found out that the model size and world knowledge are correlated to brain alignments. For the behavioral alignment, there was no correlation between per-word LLM perplexity and per-word human reading times.

### Strengths
This paper explains why instruction-tuned LLMs perform better than vanilla LLMs from a neuroscience perspective by measuring brain scores.

### Weaknesses
 - This paper appears to be a replication of [1,2], specifically focusing on instruction-tuned models. It lacks novelty and originality.
    - Increasing the model size and integrating world knowledge (using a larger training dataset) are not surprising new discoveries for improving language modeling.
    - Additionally, this paper measures the correlation between world knowledge tasks and brain alignment.
    - This paper should demonstrate the effects of contributing factors separately (world knowledge and model size). The plots seem to be dependent on model size.
- The current version of the paper requires further improvement.
    - It lacks details for readers without a background in neuroscience.
        - How is the brain score computed for each model? Does it compute the hidden state of every layer?
    - In Section 4.1, the last paragraph seems to be located too early, making it difficult to understand before explaining the dataset.
    - In Figure 3A, shouldn't the language stimuli be labeled as Futrell2018?
    - Figure 3B appears to be an empty plot.

### Questions
- How is the 'No Instruction' model trained in Figure 1D? The Alpaca instruction dataset is formed with both non-empty input fields (instruction, input, output) and empty input fields (instruction, output). Did you only use non-empty input fields and remove the instruction in those cases?
- What aspect do you believe instruction tuning contributes to the correlation between world knowledge and brain alignment?
- In Figure 2, it appears that there are different correlations for each dataset (Pereira2018, Blank2014, and Wehbe2014). Why is Blank2014's correlation so much lower compared to the other two?
- How is word perplexity measured? Could you provide an example of input and the corresponding NWP loss?
    - Since Flan-T5 models are encoder-decoder models, I'm not sure how they are measured differently from decoder-only models. Were the same inputs passed into both the encoder and the decoder?
    - Did the vanilla LLMs also show no correlation?
- Why is there a performance drop when Flan-T5 is fine-tuned on instruction tuning datasets (Alpaca, GPT4ALL, ShareGPT) as seen in Table 5 (Flan-T5-XL results)?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the effect of instruction-tuning in the alignment between LLMs’ representations and human language processing. The authors use two types of human data: brain activity patterns (brain alignment) and reading times (behavioral alignment). The brain alignment is defined as the extent to which a linear regression model predicts brain activity patterns using the LLMs’ representations. The behavioral alignment is defined as a correlation between LLM perplexity and human reading time for each word. Through the experiments across 25 vanilla and finetuned models from the T5 and LLaMA families, the authors conclude that instruction tuning improves brain alignment, (2) the performance on the world knowledge-related tasks and model size are correlated with brain alignment, and (3) instruction-tuning and other examined factors are not correlated with behavioral alignment.

### Strengths
- Using 25 models and two benchmarking datasets covering various task categories, the authors perform detailed analysis between LLM representations and human brain and behavioral data.
- The discussion includes implications both for NLP and neurosciences along with the literature review, which can encourage interdisciplinary research across both fields.
- The paper is well-written and easy to follow.

### Weaknesses
 - The authors use models from just two families, T5 and LLaMA. Looking at Figure 2, it seems that LLaMA models do not show a significant correlation between brain alignment and MMLU score, BBH world knowledge, and model size. The results would be more convincing if the authors could use a few more families such as GPT.
- Concerning the tasks related to world knowledge, it appears that these tasks may simply exhibit greater linguistic diversity compared to the other tasks examined. The concept of world knowledge seems somewhat ambiguous, and any clarification could be insightful. For instance, would similar results be observed if more language understanding tasks were added? I was unable to determine how the BBH tasks are categorized into "language understanding" and "world knowledge."

### Questions
- How did the authors determine the category classification for the BBH tasks?
- Is it possible to provide a more detailed analysis regarding world knowledge? Any discussion and additional analysis would be appreciated.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper explores the impact of instruction-tuning on large language models (LLMs) to determine their alignment with the human brain in terms of brain and behavioral alignment. Experimental results from two renowned LLM families indicate that instruction-tuning improves brain alignment by 6.2%, with world knowledge and model size being the primary contributors. However, instruction-tuning does not have a similar effect on behavioral alignment. The authors emphasize the importance of integrating world knowledge in future LLM developments.

### Strengths
This paper focuses on the instruction tuning of LLMs, exploring the neuroscience behind language models. This unique perspective advances the understanding of LLMs in the context of human cognition.

The experiment design is intuitive and relatively easy to follow. The experiments are extensive, including 3 datasets for brain and behavioral alignment, respectively.

### Weaknesses
Lack of comparative analysis with other tuning techniques such as reinforcement learning from human feedback (RLHF).

The investigation of behavioral alignment is limited. A more comprehensive exploration could offer insights into the discrepancy between brain and behavioral alignments and its implications for LLM development and application.

Other alignment measure methods may be considered to increase the reliability of the results, such as:

Jiaang, Li, et al. "Structural Similarities Between Language Models and Neural Response Measurements." arXiv preprint arXiv:2306.01930 (2023).

Liu, Xu, et al. "Coupling Artificial Neurons in BERT and Biological Neurons in the Human Brain." arXiv preprint arXiv:2303.14871 (2023).



### Questions
What is the computational cost of this study? 33B model is quite large, are there any quantization techniques used like LoRA?

May need proofreading: Table 3 and Table 4 in the Appendix have the same caption.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a study about the relation between LLMs and humans. The motivation is that the instruction-tuned LLMs carry out human instructions better (seems closer to humans). Analysis on both brain activities  shows a closer alignment from LLMs after instruction tuning. The authors also found that the world knowledge and model size are strongly correlated with brain alignment.

### Strengths
1. The authors examined two famous and commonly used families of instruction tuned models and find a consistent phenomenon. They also observed the gradual increase in brain score during instruction tuning.

2. The authors studied the models’ fit to both human neural and behavioral data.

### Weaknesses
1. It remains unclear in the whole passage that which “internal representations” from LLMs are used, which makes it difficult to reproduce the results.

2. The “world knowledge” part in the BBH dataset is different from the knowledge required in MMLU. The formal consists subsets such as Sports Understanding, Movie Recommendation, and Causal Judgement; While the latter is mainly about disciplinary knowledge such as Anatomy and College Physics. This makes the key term, “world knowledge”, much ambiguous. What knowledge are considered “world knowledge”? Are there any difference between factual, general and disciplinary knowledge?

3. The authors tried to study the effect of world knowledge and model size separately in Section 4.2. However, the two factors are deeply intertwined, given that larger LLMs tend to outperform smaller ones in knowledge-related question answering. The results in Figure 2 also show that model size has even stronger and more significant effect on the brain score. As a result, it cannot be concluded that “world knowledge” is a key contributor to the increase in brain score. Instead, it can be just another indirect effect of the larger model size.

4. The authors use the performance on MMLU and BBH to represent the models’ capability of “world knowledge”. However, performance on these benchmarks is affected not only by the quantity of knowledge that the models possess, but also by their ability to follow instructions. Thus, a higher performance on MMLU and BBH doesn’t necessarily mean that the model has more world knowledge, and the correlation between benchmark scores and brain scores does not necessarily show a link between world knowledge and the fit to human neural data.

5. The authors use the correlation between model per-token perplexity and human reading time to represent the behavioral fit. However, they pointed out in Section 6.2 that this approach is controversial when applied to large Transformer-based models. Thus, the choice of this approach is confusing. Why not use other ways to test the behavioral fit?

6. It is counter-intuitive that factual, domain knowledge can contribute the higher human fit in general reading. In fact, many questions in MMLU are difficult even for most people (e.g., Anatomy, Astronomy, College Physics, ...), and are not going to be retrieved during story reading. It is confusing why the authors choose MMLU as an aspect of the “world knowledge”, and how this can guide Neuroscience research in human language understanding.

7. The three fMRI datasets are in different settings, i.e., reading sentence by sentence, listening the whole passage, and reading word by word, which could bring different activation patterns in the human brain. However, the authors did not discuss the difference between them.

### Questions
See the weaknesses part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
