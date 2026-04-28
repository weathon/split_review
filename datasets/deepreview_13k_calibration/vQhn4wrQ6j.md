# Layer Swapping for Zero-Shot Cross-Lingual Transfer in Large Language Models

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
Model merging, such as model souping, is the practice of combining different models with the same architecture together without further training. In this work, we present a model merging methodology that addresses the difficulty of fine-tuning Large Language Models (LLMs) for target tasks in non-English languages, where task-specific data is often unavailable. We focus on mathematical reasoning and without in-language math data, facilitate cross-lingual transfer by composing language and math capabilities.
Starting from the same pretrained model, we fine-tune separate ``experts" on math instruction data in English and on generic instruction data in the target language. We then replace the top and bottom transformer layers of the math expert directly with layers from the language expert, which consequently enhances math performance in the target language. 
The resulting merged models outperform the individual experts and other merging methods on the math benchmark, MGSM, by 10\% across four major languages where math instruction data is scarce. In addition, this \ls is simple, inexpensive, and intuitive, as it is based on an interpretative analysis of the most important parameter changes during the fine-tuning of each expert. The ability to successfully re-compose LLMs for cross-lingual transfer in this manner opens up future possibilities to combine model expertise, create modular solutions, and transfer reasoning capabilities across languages \emph{all post hoc}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new approach to perform zero-shot cross-lingual transfer for solving tasks in a new language. The requirement is to have data for the task in a more resourced language (e.g. English) and non-task-specific data for other languages (4 languages in this paper). The idea is to fine-tune the model (Llama 3.1, 8B in the paper) separately to one new language and another copy to the task in English, then compose a new model of layers of these two models. A study is included of how much the models change during fine-tuning, which concludes that math tasks cause changes in the fine-tuned model closer to the middle layers, while tuning on a new language causes changes in the first and last layers. Based on that the composed model takes task-layers from the math-tuned model's middle, and language-layers from the language-tuned model's start and end. Transfer between the layers of two independently tuned models is done by "souping" intermediate layers, i.e. averaging the weights of layers of both models. Gains up to 10% are shown, in comparison to the expert models.

### Strengths
* Interesting idea and its evaluation on 1 model and 4 languages, with additional experiments
* Although the setup raises some questions (limited evaluation, why not freeze layers and avoid having to soup the transition layers, etc.), the expanded evaluation on Swahili and the limitations section address most of these
* excellent writing, justification and presentation

### Weaknesses
 * limited evaluation: only 1 model and one set of tasks (math)

### Questions
1. You write that combining layers works because models are fine-tuned for just a little bit: why not tune for longer?
2. What would the intuitive explanation be behind the findings of your preliminary analysis on which layers are changed by task-tuning and language-tuning, other examples of similar effects in related literature?
3. If you were to tune for longer, would that affect the results of the preliminary analysis and change more layers, or different layers?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a variant of model merging addressing the challenge of adapting LLMs for tasks in low-resource languages. The methodology involves *layer swapping* (parameters being swapped) between a task expert and a language expert, both following the same underlying architecture. The resulting re-composed LLM is said to outperform both the individual experts without the requirement of a task-specific fine-tuning in the low-resource language. The experiments involve evaluation of the proposed methodology on MGSM (a multilingual benchmark of grade-school math problems) on 4 resource-scarce languages: Japanese, Telugu, Swahili and Bengali.

### Strengths
1. The proposed methodology is highly practical in scenarios where one might have publicly available task-specific data in a high-resource language and generic instruction data in the low-resource language. The model parameter adjustments being fully post-hoc eliminate any additional computational overhead apart from the initial fine-tuning required to create task and language experts.

2. *layer swapping* with the best configuration consistently outperforms the individual SFT experts, the base LLM Llama 3.1 and the general model souping approach in three (Swahili, Telugu, Bengali) out of the four languages under this study.  

3. The paper is easy to follow. The authors also take the effort to acknowledge the possible limitations to the work, encouraging future exploration.

### Weaknesses
1. The methodology is evaluated only on Llama 3.1, using MGSM benchmark for 4 selective languages. In my opinion, evaluation of the method on a single model, single benchmark and limited languages makes the conclusion less generalizable. While the languages used in the study are diverse, incorporating more datasets and models (in terms of different architecture or pre-training) can strengthen the conclusion. Specifically, the lack of experiments with other model architectures, such as encoder-decoder models or models with different pre-training objectives, limits the scope of the findings. Furthermore, the MGSM benchmark, while useful, is limited to mathematical reasoning and might not reflect the performance of the proposed method on other tasks such as text summarization, question answering, or code generation. The selection of only four languages, despite their diversity, does not provide a comprehensive view of the method's effectiveness across a wider range of linguistic structures and complexities. A more robust evaluation would include a larger set of languages, covering different language families and resource levels, and a variety of tasks to assess the generalizability of the method.

2. The assumption of availability of generic instruction data for low-resource languages might not hold for all languages. Task-specific data and generic instruction data in a high-resource language is generally more accessible. An experiment where language expert is fine-tuned using translated instructions would increase the practicality of the work. The current approach assumes that high-quality, human-generated instruction data is readily available for low-resource languages, which is often not the case. In many low-resource scenarios, the available instruction data is either limited in quantity or quality, or it may be machine-translated, which can introduce noise and bias. An experiment that explores the use of machine-translated instruction data for fine-tuning the language expert would be more practical and relevant to real-world scenarios. This would also help in understanding the robustness of the proposed layer-swapping method under less-than-ideal data conditions.

### Questions
1. How does a re-composed model in one language affect model performance in typologically similar languages? In my opinion, an analysis of this kind would highly benefit the work. 

2. Would a 2-stage SFT work better than Joint SFT on language and task?

---

**[POST-REBUTTAL UPDATE]**

I have decided to increase the overall rating from **5** (marginally below the acceptance threshold) to **6** (marginally above the acceptance threshold).

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a novel layer-swapping methodology for zero-shot cross-lingual transfer in large language models (LLMs) aimed at improving task performance in non-English languages, particularly for mathematical reasoning. The approach tackles the lack of task-specific data in low-resource languages by fine-tuning two separate "experts" of the same base model: one trained on English mathematical data and another trained on general instruction data in the target language. The proposed method then selectively replaces the top and bottom transformer layers of the math expert with those from the language expert, buffered by transition zones between these regions. This configuration shows promising performance gains on the MGSM math benchmark across four languages—Swahili, Telugu, Bengali, and Japanese—without any additional in-language math data.

### Strengths
- The paper introduces an efficient, innovative layer-swapping method for zero-shot cross-lingual transfer in LLMs, addressing the lack of task-specific data in low-resource languages with simplicity and strong empirical results.

- This technique is particularly notable for its straightforward implementation, allowing effective merging of task and language expertise without complex adjustments, making it a practical alternative to standard methods like model souping. 

- Promising experimental gains on math reasoning benchmarks across multiple low resource languages validate the method's effectiveness, showing that layer swapping successfully enhances cross-lingual transfer without in-language task data.

### Weaknesses
 - The method is tested only on math reasoning, leaving it unclear if layer swapping generalizes to other tasks. Additional evaluations on tasks like question-answering or translation would strengthen the claims of broad applicability. Specifically, the paper lacks experiments on tasks that assess different aspects of language understanding and generation, such as tasks requiring complex reasoning beyond mathematical problems, or tasks that involve more nuanced linguistic skills. This narrow focus limits the ability to assess the true versatility of the proposed layer-swapping technique.
- While the paper mentions different layer-swapping configurations, it lacks in-depth analysis on which configurations work best and why. A more detailed study of these choices would help to better understand the method make it more robust. For example, provide ablation studies on the number of swapped layers or transition zone sizes, or to analyze how performance changes as these parameters are varied. The paper should explore the impact of varying the number of layers swapped from both the top and bottom of the model, as well as the size of the transition zones, to provide a more complete picture of the method's sensitivity to these parameters. Without this analysis, it is difficult to determine the optimal configuration for different tasks or model sizes.
- Comparisons to recent modular fine-tuning techniques, such as adapters or LoRA, are missing. Including these would clarify how layer swapping performs relative to other efficient, cross-lingual methods. The paper should include a comparative analysis with adapter-based methods, which are known for their efficiency in cross-lingual transfer, and low-rank adaptation (LoRA), which is effective for parameter-efficient fine-tuning. This comparison should include not only performance metrics but also computational costs and the number of trainable parameters, to provide a more comprehensive evaluation of the proposed method.

### Questions
1. Can the authors clarify if they have tried layer swapping on other tasks, such as translation, question-answering, or code generation? Evidence of generalizability beyond math would make the approach significantly stronger.
2. Layer swapping is positioned as an alternative to methods like model souping, but a comparison to more recent modular fine-tuning techniques, such as adapters (Pfeiffer et al., 2020) or LoRA (Hu et al., 2022), could help contextualize its relative strengths. Can the authors either conduct these comparisons (e.g. computational efficiency, performance) or discuss the anticipated performance differences? 
3. Given that this study uses a 8B (32-layer) LLM, how would the authors anticipate the method scaling to models with more layers or parameters? Could they provide guidance on applying layer swapping to larger models, especially in terms of choosing the number of layers to swap? Would the authors still anticipate the same performance gain with layer swapping on larger models? 
4. For Japanese, layer swapping results in lower average performance compared to the individual math experts. The authors mentioned that the Japanese experts were the weakest as performance across BELEBELE, FLORES, MBPP, and MMLU were minimal. Could the authors share the results on these benchmark (before and after SFT) to help better understand the case?

### Soundness
3

### Presentation
3

### Contribution
3
