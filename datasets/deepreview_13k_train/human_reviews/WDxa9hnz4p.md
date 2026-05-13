# Auto-Demo Prompting: Leveraging Generated Outputs as Demonstrations for Enhanced Batch Prompting

- Decision: Reject
- Scores: 3, 3, 1

## Abstract
Batch prompting is a common technique in large language models (LLMs) used to process multiple inputs simultaneously, aiming to improve computational efficiency. However, as batch sizes increase, performance degradation often occurs due to the model's difficulty in handling lengthy context inputs. Existing methods that attempt to mitigate these issues rely solely on batch data arrangement and majority voting rather than improving the design of the batch prompt itself. In this paper, we address these limitations by proposing ``Auto-Demo Prompting,'' a novel approach that leverages the question-output pairs from earlier questions within a batch as demonstrations for subsequent answer inference. We provide a formal theoretical analysis of how Auto-Demo Prompting functions within the autoregressive generation process of LLMs, illustrating how it utilizes prior outputs to optimize the model's internal representations. Our method effectively bridges the gap between batch prompting and few-shot prompting, enhancing performance with only a slight compromise in token usage. Experimental results across five NLP tasks demonstrate its effectiveness in mitigating performance degradation and occasionally outperforming single prompts. Furthermore, it opens new avenues for applying few-shot learning techniques, such as demonstration selection, within batch prompting, making it a robust solution for real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In batch prompting, many inputs are formatted consecutively in the prompt, and the model then produces responses for each input in single generation. This can improve computational efficiency by reducing the number of tokens processed (for instance, only needing one instruction for many samples). However, batch prompting tends to degrade prompting performance, while few-shot prompting---which uses the same in-context examples, but formatted differently---can improve it. Motivated by this observation, the paper proposes Auto-Demo prompting, which follows the format of batch prompting but instructs the model to output both the question and the answer, given the question. The intuition is that the model can then treat the consecutive (question, answer) pair as a traditional few-shot demonstration, while still attaining the parallelism of batch prompting. The paper also considers how to better select demonstrations, and finds that the method can outperform standard batch prompting techniques.

### Strengths
Quality: auto-demo prompt outperforms standard batch prompting on 7/10 tasks across batch sizes. 

Significance: improving inference-time efficiency in terms of prompting techniques is an important aspect of using LLMs on large amounts of data.

### Weaknesses
Quality:
- Limited evaluation: I could not find any baseline against few-shot prompting, which auto-demo prompting aims to "combine" with batch prompting. Moreover, there is no evaluation of efficiency/cost, even though I believe auto-demo prompting generates more tokens and thus is more expensive. Given this tradeoff and the lack of evaluation against few-shot prompting, it is unclear if we can conclude that auto-demo prompting provides a cost-performance tradeoff improvement over standard methods. Overall, the performance improvements appear to be minor, while incurring extra cost.
- Missing ablations: what is the role of the embedding space, and do other metrics for data selection also work?

Originality: my understanding is that models can process in-context demonstrations better when input output pairs are consecutive. Is there a deeper understanding of why few-shot prompting does better than batch prompting, despite having the same content? Is it simply because training data tends to have sequential (q, a) pairs? If so, the intuition of this paper is to align the prompt more with the data the LLM is trained on. This approach has limited novelty given that it directly combines two existing ideas, as well as standard demonstration selection techniques.

Clarity: Method 1 doesn't seem to generate $a_i$ conditioned on $q_i$. Also, Method 2 appears to generate $a_i$ preceded by $q_1 q_2$, when my understanding is that batch prompting has any $a_i$ preceded by $q_1 q_2 \dots q_n$.

### Questions
1. Can you discuss or show results on few-shot prompting 
2. Can you discuss or show results on efficiency of the method?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a method called auto-demo prompting, aiming to improve performance when batched processing is needed in in-context learning. The authors propose to ask the model to repeat each question in the batch following by answering each question, showing that this method can outperform previous batching methods that simply ask the model to provide the answers.

### Strengths
- The proposed method is interesting, showing that repeating the question in the batch can better help the model answer each question more accurately.

- The experiments are relatively comprehensive over 5 commonly used NLP datasets.

### Weaknesses
The writing is not very clear; there are several unnecessary details. For instance, in the intro:
- The definition of batch prompting is not clear in the intro Lines 43-48; Why does it help efficiency? The writing assumes that the reader is familiar with this.
- How does one decide which questions to batch?
- It is not clear where the model-generated answers as few-shot prompts come into play in Lines 100-102. - - The concept is not introduced in the intro before this.
- What does “proper design” mean on Line 105?
- It is not clear why having 0 to N-1 additional demos would help with long context (Lines 114-115)
- The contributions (Lines 123-141) say nothing about efficiency, despite this being an initial motivation for batch prompting
- It is also not clear why the reader needs any of the details in lines 213-219

How does this compare to methods like Hydragen (https://arxiv.org/abs/2402.05099), which do not increase the context length, but rather share the KV-cache on the shared prefix?

The Batch Data Selection with Retrieval approach is not novel – many approaches select similar examples via these embedding similarity scores

Results:
- The improvements from this method are unclear (0.2%, Lines 370-371)
- There is no comparison to few-shot learning with retrieval-based few-shot selection
- A motivation of batch prompting was efficiency – there is no evaluation of the efficiency improvements

### Questions
- Can the authors add standard deviations to Figure 3?

- Can the authors make the x-axis / batch-size range consistent across experiments?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper explores batch prompting, where the prompt groups similar questions to be able to optimize execution efficiency. The work examines how to shape the input context of the prompt to achieve improved quality in the batch prompting scenario.

### Strengths
The paper evaluates on multiple datasets
The idea that we can exploit the similarity across questions to reap efficiency improvements is interesting

### Weaknesses
The writing is not very clear; there are several unnecessary details. For instance, in the intro:
- The definition of batch prompting is not clear in the intro Lines 43-48; Why does it help efficiency? The writing assumes that the reader is familiar with this.
- How does one decide which questions to batch? 
- It is not clear where the model-generated answers as few-shot prompts come into play in Lines 100-102. - - The concept is not introduced in the intro before this. 
- What does “proper design” mean on Line 105?
- It is not clear why having 0 to N-1 additional demos would help with long context (Lines 114-115)
- The contributions (Lines 123-141) say nothing about efficiency, despite this being an initial motivation for batch prompting
- It is also not clear why the reader needs any of the details in lines 213-219

How does this compare to methods like Hydragen (https://arxiv.org/abs/2402.05099), which do not increase the context length, but rather share the KV-cache on the shared prefix? 

The Batch Data Selection with Retrieval approach is not novel – many approaches select similar examples via these embedding similarity scores

Results:
- The improvements from this method are unclear (0.2%, Lines 370-371)
- There is no comparison to few-shot learning with retrieval-based few-shot selection
- A motivation of batch prompting was efficiency – there is no evaluation of the efficiency improvements

### Questions
This work is not up to par for the conference and it is unlikely that author responses will change my opinion

### Soundness
1

### Presentation
1

### Contribution
1
