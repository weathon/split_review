# E2LLM: Encoder Elongated Large Language Models for Long-Context Understanding and Reasoning

- Decision: Reject
- Scores: 6, 5, 6, 6, 5

## Abstract
In the realm of Large Language Models (LLMs), the ability to process long contexts is increasingly crucial for tasks such as multi-round dialogues, code generation, and document summarization. This paper addresses the challenges of enhancing the long-context performance, reducing computational complexity, and leveraging pretrained models—collectively termed the "impossible triangle." We introduce E2LLM (Encoder Elongated Large Language Models), a novel approach that effectively navigates this paradox. The method involves splitting long contexts into chunks, compressing each into embedding vectors via a pretrained text encoder, and utilizing an adapter to align these representations with a decoder-only LLM. Two training objectives, focusing on reconstruction of the encoder output and long-context instruction fine-tuning, are employed to facilitate the understanding of soft prompts by the LLM. Experimental results demonstrate that E2LLM achieves superior performance in long-context scenarios while balancing efficiency, performance, and compatibility with pretrained models. Our framework thus represents a significant advancement in the field, contributing to effective long-text modeling. \emph{Code will be available upon publication.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents E2LLM, an architecture that addresses long-context processing in LLMs through a chunk-based approach. 

At its core, E2LLM employs a pretrained text encoder to compress text chunks into embedding vectors, which are then aligned with a decoder-only LLM (LLaMA-2) through a two-layer MLP adapter. 

E2LLM also propose a two-stage training process: 1. an "understanding" task where the model reconstructs the original text from compressed representations, and 2. a "reasoning" task focused on answering queries using these compressed contexts. 

The authors position their work as solving the "impossible triangle"(I am not so sure about the reference here) of maintaining strong performance, computational efficiency, and compatibility with pretrained models.

I am concerned with unclear explanations of the core model architectures, not well collected benchmarks, and lack of in-depth analysis

### Strengths
1. Solving long-context language modeling is an important problem

2. Compression yields benefits in computation efficiency

3. In their selected benchmarks, their model yield good performance.

### Weaknesses
## Benchmark results are not tailored for the long context length argued in the paper. 

As far as I understand, most of benchmarks stated in this paper, their AVG length is not up-to-128k. And benchmarks are not on par with the recent advances, for example, RULER where there are way more challenging tasks mentioned in recent papers for example HELMET and long context controlled study

-  I would encourage authors to break down the task accuracy by length to show the real benefit of their method.

- Also adding some recent benchmarks, for example Ruler, and HELMET to have real long context evaluation thoroughly.

- I think the Needle task is not well presented. I understand that authors wanna focus on the accuracy, but the heat map might give us a clear image on where the model fails, and the trend per position more clearly w.r.t needle depth. Is it possible to have a similar analysis?


## Presentation can be improved.

- I am not so sure that I understand the compression process. The major compression is depending on the chunk size in this paper, but it is not well studies how this chunk size will influence the results, or how will influence the results, semantically for example. I would encourage authors break down the Negative LL per token position to demonstrate the effect of chunk size, particularly at boundaries. 

- Model architecture details are missing. Maybe this can be benefit from adding a clear model architecture figure and justifying the design choice. Figure 1 demonstrates the idea at very high level and paragraph descriptions are not very clear in 3.1. 


### Questions
Q1. What's the adapter is chosen and why? 

Q2. How the chunk size will affect results


See weakness for most of the comments and questions.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces E2LLM, a method for long-context language modeling. The main components consist of an encoder, an adapter, and a decoder-only LLM. It uses Llama 2 7B chat as the backbone LLM and GTE as the encoder. It’s evaluated on several long-context and QA tasks like QMSum, GovReport, Quality, NarrativeQA, and TriviaQA, and achieves competitive results. It’s also evaluated on the needle-in-a-haystack and LongBench.

### Strengths
- E2LLM is a novel method with significant inference benefits compared to previous works. It shows that encoder and decoder can be connected with an adapter in the middle. 
- The method shows strong empirical results on downstream tasks in the supervised training settings., and includes a number of tasks in the evaluation setting. 
- The paper also includes a number of ablation studies that reveal more insights regarding the method.

### Weaknesses
 - About the baseline methods, Appendix B states that Llama 2 7B is “the backbone for the other methods”, but E2LLM uses Llama 2 7B Chat as the decoder. It doesn’t seem fair to compare methods that use different backbone models. What would the performance of E2LLM be if Llama 2 7B were used as the backbone model instead? Or if the other methods use the chat model as the backbone?
- A key difference between previous methods and E2LLM is that they are typically studied in the pre-training/continual pre-training settings where they are first trained on a corpus like RedPajama (such as in the case of YaRN, LongLoRA, CEPE, and others), and then evaluated either zero-shot or with ICL on downstream tasks. It would be important to see how E2LLM would perform in such settings in addition to the supervised fine-tuning setting.

On the writing, there are some citation errors, for example: 
Line 033: Giorgi et al. → Giorgi et al., 2023. 
Line 053: Ding et al. → Ding et al., 2024.
Line 090: Kenton & Toutanova, 2019 → Devlin et al., 2019.
There are others throughout the paper.

### Questions
In addition to the questions listed in the Weakness section: 

- In Figure 4, why do the inference time and memory usage increase for StreamingLLM? It keeps a constant size of starting and recent KV caches, so it should stay constant past a certain length. 
- Why is E2LLM better than YaRN and LLoCO on NarrativeQA in Table 1 but not in Table 2? 
- In Sec 4.1, the datasets listed are QMSum, GovReport, HotpotQA, NarrativeQA, and TriviaQA, but the corresponding Table 4 lists Quality instead of HotpotQA for the statistics, and Table 1 shows Quality instead of HotpotQA.
- How important are the two training tasks in Sec 3.2? It's not clear how they are used during training and how they affect the performance and the training efficiency, as reconstructing the inputs from the encoder introduces additional costs.

### Soundness
2

### Presentation
2

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
In this paper, authors try to propose a framework to support LLM at long context side. They chunk the input text into different parts and try to compress then by an encoder and a LORA adaptor is used to improve the representation. They propose two training objectives to handle the understanding and reasoning at the same time. They conduct experiments on several benchmarks and show the effectiveness of their method.

### Strengths
1. The presentation is pretty clear to me and the T1, T2 and T3 categories make lot of sense and easy to follow. They summarize current methods in terms of them.
2. They do a comprehensive evaluation on their model to show the effectiveness.
3. The model aligns the encoder and decoder via a trainable adapter, minimizing the need for extensive retraining and making it easier to implement.

### Weaknesses
1. The encoder-decoder framework is reasonable but I am concerned that what if the LLM is a large scale one like llama 70B. will the train be feasible. Seems author just conductor experiments on small scales.
2. The chunk size is pretty heuristic and with different tasks, the performance varies with chunk size. Could we make it learnable as well?
3. Maybe another concern is the real time application, how do we plan for that given this framework.
4. With the encoder and adapter, how does the inference speed compared to the baseline?
5. Can we do the eval on RULER?

### Questions
Please refer to the above.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces E2LLM, designed to efficiently and effectively handle long-context understanding in LLMs. The method balances long-context performance, computational efficiency, and compatibility. E2LLM employs a soft prompt compression technique, segmenting long contexts into chunks, compressing them into embeddings using a pretrained text encoder, and aligning these embeddings with a decoder-only LLM through an adapter. The proposed training objectives of the model focus on reconstructing encoder outputs and fine-tuning for long-context instructions. Experiments demonstrate that E2LLM outperforms existing SoTA methods across multiple long-context benchmarks including summarization, QA, needle-in-a-haystack, and LongBench, while achieving low inference time and memory usage.

### Strengths
1. The paper is overall well-written and easy to follow.
2. The integration of an encoder to compress long contexts while preserving essential information is innovative and leverages existing pretrained architectures efficiently.
3. The extensive experiments show the proposed method's performance, efficiency, and robustness. The method could serve as a strong baseline for future works.

### Weaknesses
1. The authors would like to introduce E2LLM as a general framework that could work with any LLMs, which is intended to show the method's flexibility. However, when compared to similar methods like CEPE, both the encoder and the LoRA rank used are different. This both makes the "Trainable Parameters" in Table 1 incomparable and makes me doubt whether the improvement comes from the more powerful GTE-Large-en encoder or the proposed method. The lack of a controlled experiment where only the method is changed, while keeping the encoder and LoRA rank constant, makes it difficult to isolate the true source of the performance gains.
2. It is unsure how the authors trained E2LLM and the baselines on the tasks specified in Appendix C. How were the hyperparameters for each method decided? The absence of a clear explanation of the hyperparameter tuning process raises concerns about the reproducibility and fairness of the comparison. Specifically, it is unclear whether a consistent and principled approach was used to select hyperparameters for all methods, or if the hyperparameters were tuned to favor the proposed method.
3. The analysis of E2LLM's complexity has flaws. As per Figure 2, the input contains a span (prompt + query) that is directly put into the decoder. The complexity needs to separate the computation of the "context" part and the "prompt" part. The current analysis does not account for the computational overhead of processing the prompt, which could be significant, especially for long prompts.
4. The paper misses some related works. For example, for position embedding extension methods, there have been better methods [1] or improvements to YaRN [2]. For methods similar to CEPE, the concurrent work FocusLLM [3] has a very similar design to E2LLM.

### Questions
Other than the problems mentioned in the weaknesses section, below are some other questions:
1. In line 396, you mentioned "E2LLM addresses these challenges...", which includes the challenge that StreamingLLM requires training. However, E2LLM also requires training to align the encoder, adaptor, and decoder. Please explain this claim.
2. In line 404, you mentioned that YaRN faces the challenge that "attention mechanisms can become dispersed in exceedingly long contexts". However, YaRN proposes the dynamic scaling method for the attention scores to alleviate this problem.
3. In line 265, it would be easier to understand if "sequence length" could be replaced by "context window" for the input capacity of the model.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents E2LLM, a novel approach to tackle the challenge of processing long contexts in LLMs. The authors identify three key challenges: performance (T1), efficiency (T2), and compatibility (T3). E2LLM addresses these challenges by (1) splitting long contexts into chunks; (2) compressing each chunk into an embedding vector using a pre-trained text encoder; (3) utilizing an adapter to align the encoder’s output with the decoder’s input embedding space; (4) training two objectives: reconstructing the original text from the encoder’s output and fine-tuning the LLM on long-context instruction tasks.

### Strengths
1. E2LLM achieves a good balance between performance, efficiency, and compatibility;

2. The model is trained end-to-end, ensuring the alignment between the encoder and decoder and minimizing information loss;

3. Extensive experiments demonstrate that E2LLM outperforms several existing methods on long-context tasks such as document summarization, QA, Needle-in-a-Haystack, as well as LongBench;

4.  E2LLM achieves the lowest inference time and memory usage among compared methods.

### Weaknesses
1. The authors seem to overclaim that "E2LLM solves all the challenges of the impossible triangle" since the performance on long-context tasks of E2LLM still falls far behind "continual pertaining on longer texts + long-context SFT" paradigm [1, 2] (though there is no comparison between E2LLM and this approach in the paper), which is the mainstream and SoTA approach now and widely used in most advanced LLMs such as Llama3.1 and GLM4. This makes the real-world applicability of E2LLM doubtful. A comparison between E2LLM and "continual pretraining + SFT" approach should be presented to support the claim.

2. The figure of Needle-in-a-Haystack is deceptive since the color is all green (the score less than 5 should be marked in red). Though outperforms the baseline methods, E2LLM still struggles in recalling the needle with only 30% success rate， while current long-context LLMs can achieve nearly 100% performance. This low recall rate indicates a significant limitation in the model's ability to precisely retrieve information from long contexts, which is a critical aspect of long-context understanding.

### Questions
1. What is the maximum compression rate of E2LLM such that the context can be recovered losslessly?

2. Can E2LLM effectively harness the longer context windows? In other words, does the PPL/performance of E2LLM continue decreasing/increasing when the context window becomes longer?

### Soundness
3

### Presentation
3

### Contribution
2
