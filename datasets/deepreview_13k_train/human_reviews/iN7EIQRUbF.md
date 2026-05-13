# Advancing Few-shot Continual Learning via Selective Knowledge Transfer

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Continual learning with large language models (LLMs) is a promising and challenging research that greatly impacts many applications. Existing solutions treat previous tasks equally, making them vulnerable to task interference, lacking scalability with a large number of tasks, and oblivious to the intrinsic relationships among tasks. This work presents selective knowledge transfer (SKT), a novel
and principled framework for continual learning with LLMs. SKT aims to maximize positive knowledge transfer while systematically minimizing the effects of irrelevant information from dissimilar tasks. To this end, SKT first assesses the degree of interference between the current and previous tasks and then selectively aggregates the tasks that maximize knowledge transfer for continual
training. In addition, we integrate SKT into the current state-of-the-art continual language learning algorithm, Progressive Prompts, to introduce Log-evidence Progressive Prompts (LePP), which facilitate knowledge transfer between tasks. Comprehensive evaluations on challenging few-shot continual learning benchmarks demonstrate that LePP can surpass existing baselines for continual learning with LLMs with minimal overhead. Our extensive ablation studies reveal that SKT can discover useful task correlations without any prior knowledge, many of which align with human evaluations. Code will be published upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on few-shot continual learning for large language models and introduces the Selective Knowledge Transfer (SKT) framework. The framework leverages transferability measures to autonomously identify relevant past memories for current tasks, enhancing knowledge transfer and improving system performance. The paper integrates SKT into existing prompt-based continual learning algorithm, Progressive Prompts, which learns a prompt for each new task. The paper empirically shows the effectiveness of SKT for BERT and T5 models on various NLP benchmarks. Additionally, SKT is shown to work with various data modalities, including images.

### Strengths
1. The proposed approach is straightforward and computationally efficient.
2. The Selective Knowledge Transfer framework effectively facilitates knowledge transfer between tasks.
3. The performance of LePP surpasses baseline methods on several continual learning benchmarks.

### Weaknesses
1. The writing of this paper could be improved. There are a few writing errors, e.g. line 65 and 168-169, and some areas that are confusing, e.g. the baseline and corresponding reference in line 262 and 294.
2. The paper assumes that task-ids are available during inference, allowing the framework to use a specific prompt for each task. However, obtaining these identifiers in real-world scenarios may be challenging.
3. It would be beneficial to include comparisons with more recent approaches, such as SAPT: A Shared Attention Framework for Parameter-Efficient Continual Learning of Large Language Models (ACL 2024) and Mitigate Negative Transfer with Similarity Heuristic Lifelong Prompt Tuning (ACL 2024).
4. The experimental results do not clearly demonstrate the effectiveness of positive knowledge transfer. The results only provide average performance of the models. It is important to compare continual learning methods from different perspectives to demonstrate positive knowledge transfer in a more direct way.
5. While the authors claim that the proposed framework can be applied to any Parameter-Efficient Tuning method, only results for Prompt Tuning are provided.
6. The proposed method is evaluated only on classification task, while its effectiveness on other generation tasks remains unclear.

### Questions
1. The largest language model used in the experiments is T5-large(770M), which may not be sufficient to demonstrate scalability with the size of language models. Have the authors experimented with larger language models, e.g. Llama3-8B?
2. Could the authors explain how the proposed framework can be applied to other PEFT methods?
3. How does the method work if task-ids are not available during inference?

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
4

### Summary
This paper proposed selective knowledge transfer, a continual learning framework for LLMs utilizing transferability measures. It can be integrated into the prompt-based continual learning frameworks, leveraging related past knowledge to improve system performance.

### Strengths
It is a good point to consider knowledge transfer in continual learning, and combining it with prompt tuning is reasonable and effective.

### Weaknesses
1. The proposed method LePP heavily relies on previous work LogME and Progressive Promt. It is applying the LogME to Progressive Promt within the already established research question. As the research question is established with benchmarks, and the method is an A+B, this work only provides a limited technical contribution.
2. The author claims selective knowledge transfer is a novel and principled framework for continual learning with **LLMs**. However, the current knowledge transferability calculation requires the model to have the ability to encode features. As discussed by the authors in the limitation, LePP cannot be directly applied to decoder-only models which are the majority of "LLMs". As a reference, T5 is not claimed as "LLM" in Progressive Promt. This is an overclaiming. The influence of this work is limited by the supported task type and model type.
3. The writing could be further improved. Will list the writing problems in the questions section.

### Questions
1. Line 15~16, two points to improve with "This work presents selective knowledge transfer (SKT), a novel and **principled** framework towards continual learning with **LLMs**." First, I would suggest the authors carefully reconsider using "principled" as a self-comment. It is always better to provide a good presentation to let readers feel the method is principled, not commented by the authors themselves. Second, "LLMs" is somehow overclaimed as T5 is not always considered a LLM.
2. Line 32, "Modern language models must efficiently adapt to dynamic environments", "must"--> "are expected to" / "are required to"/ "need to", whatever appropriate word instead of must. 
 Another problem with this sentence is that decoder-only modern LLMs can adapt to dynamic environments with in-context learning.
3. Line 36~39, "However, two main obstacles ...  catastrophic forgetting (CF),... and forward transfer (FT), ..." The word "obstacles" needs consideration. Should forward transfer be considered an obstacle or a research question/methodology?
4. Table 1 caption is too short and void. Should put more information into the caption to make the table self-contained. The author can refer to the Progressive Prompt paper.
5. Line 504, the authors claim their proposed framework is computational-efficient, "Our proposed framework are computational-efficient...".  "are"-->"is", and although theoretically, this may be true, the authors should provide perceptible results to demonstrate how 
computational-efficient their framework is.

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
4

### Summary
This paper explores few-shot continual learning with large language models and proposes a new strategy called selective knowledge transfer, which aims to identify and leverage relevant information from past knowledge to enhance performance. Additionally, it introduces Log-evidence Progressive Prompts (LePP), a two-stage continual learning algorithm that incrementally learns a soft prompt . It selects the top K trained prompts based on their transferability scores derived from encoder features.

### Strengths
1. Complete and clear algorithmic flow
2. This method is lightweight and efficient, , incurring minimal additional costs.
3. The experiments yield exceptional results.

### Weaknesses
1. All experiments are limited to classification with small datasets, which may restrict the paper's generalizability and contributions to other applications.

2. "However, more accurate measures have higher accuracies. " This sentence is a bit unclear. 

3. Also, why was LogME chosen when ETran demonstrates better performance?

4. One of the key proposals of this paper is the introduction of transferability measures into continual learning; however, it lacks sufficient evidence and experiments to support its advancements and to clearly differentiate these measures from standard similarity metrics, such as cosine similarity. At present, it is difficult to see its superiority and necessity.

### Questions
1. A slight suggestion:  there are too many abbreviations in this paper. While some contribute to conciseness, others may cause confusion.
2. "Learning from the least transferable tasks slightly improved overall performance..." This conclusion is unclear and appears contradictory. The explanation is not fully convincing, as 'unrelated tasks' are not necessarily equivalent to 'harder tasks.'

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
4

### Summary
This paper introduces Selective Knowledge Transfer (SKT) for few-shot continual learning with large language models (LLMs), aiming to enhance positive forward transfer when learning new tasks. The proposed framework is computationally efficient and can automatically identify both similar and dissimilar tasks, ensuring scalability as the task stream grows. The authors also present Log-evidence Progressive Prompts (LePP), an improved version of Progressive Prompts. In this approach, prompts from previous tasks are selected based on transferability scores, and their weighted sum is used as additional input for the LLMs. Extensive experiments demonstrate that the proposed framework significantly improves upon state-of-the-art methods for continual learning across both natural language processing and computer vision tasks.

### Strengths
* The proposed method is simple and effective.

* Experiments are extensive.

### Weaknesses
 * The proposed method has limited novelty since it is a simple variant of the Progressive Prompts, proposed in [1] with prompt selection. Specifically, the proposed method replaces the prompt concatenation with prompt weighted average. Furthermore, weighted knowledge transfer has been widely studied in various fields. For example, in domain adaptation [3], continual learning [4], although the methods are slightly different, the principle is about the same.


* The proposed transferability scores is also proposed in [2], thus the metirc is not new in this paper. Also, the authors state that the previous task data is not available when learning new task, so they use the previous prompt parameters applied on new task to calculate the transferability metric. There is no analysis whether this way of calculation is suitable or not. 

* Lack of deeper analysis on how the proposed approach with prompt selection improves the continual learning performance.  For example, select which part of prompt knowledge is helpful for learning new task.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2
