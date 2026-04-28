# Making Text Embedders Few-Shot Learners

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Large language models (LLMs) with decoder-only architectures demonstrate remarkable in-context learning (ICL) capabilities. This feature enables them to effectively handle both familiar and novel tasks by utilizing examples provided within their input context. Recognizing the potential of this capability, we propose leveraging the ICL feature in LLMs to enhance the process of text embedding generation.
To this end, we introduce a novel model \textbf{bge-en-icl}, which employs few-shot examples to produce high-quality text embeddings. Our approach integrates task-related examples directly into the query side, resulting in significant improvements across various tasks.
Additionally, we have investigated how to effectively utilize LLMs as embedding models, including various attention mechanisms, pooling methods, etc. Our findings suggest that retaining the original framework often yields the best results, underscoring that simplicity is best. Experimental results on the MTEB and AIR-Bench benchmarks demonstrate that our approach sets new state-of-the-art (SOTA) performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes to train instruction-conditional embedding models to take few-shot examples as inputs. Previous work trained embedding models to take instructions as input by contrastive-loss training on a collection of classification / question-answering datasets. This paper’s approach is similar and differs only in that in addition to the instruction during the training one adds several positive examples to the prompt. This additional conditioning leads to significant gains on AIR-Bench and MTEB benchmarks.

### Strengths
This is a very straight-forward paper, it is easy to read, it presents compelling, though not jaw-dropping results.

### Weaknesses
- It would be nice to see an experiment on how the number of few-shot examples impacts performance. 
- The discussion about overlap between training data and MTEB was a bit difficult to follow.

### Questions
The "more comprehensive" dataset that you train your model on still consists of public datasets, doesn't it? I find the way you chose to name these two different experimental settings a bit misleading.

### Soundness
3

### Presentation
3

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
This paper proposes to include in-context examples for better text embedding. They do so by finetuning for an epoch in a traditional contrastive learning/embedding-training setup but with in-context examples included in the training data.

### Strengths
- This method does appear to slightly improve the performance of text embedding models even at the 7B scale.
- Novelty: In-context learning has been shown to be effective for language models in many scenarios; as far as I'm aware, this is the first work to explore in-context learning at the 7B scale.
- The paper makes a number of other empirical contributions, analyzing factors such as bidirectional attention and pooling as well as details of whether instructions should be added to passages or queries or both.

### Weaknesses
 - In context examples have been shown to be most useful when a language model needs to learn a template or format for doing a task; in many cases, this is their *only* contribution (as opposed to actually teaching semantic information about the task at hand). This is not useful for embedding models because embedding models always have the same task format (outputting an embedding).
- A major weakness is that this obviously makes the embedding process slower, and it's not clear by quite how much or what the tradeoff is. The performance gains are quite marginal (71.2 -> 71.7 on MTEB) and practitioners would need to balance this with the 
- Similarly, it's not clear how much of the performance comes from increasing the number of tokens (and consequently FLOPs) that the model can use at test-time vs. actually incorporating new information into the model. A useful ablation would be training a model with the same number of tokens as a typical ICL example, but with a single token substituted for all ICL tokens (a-la the "let's think dot-by-dot" work). I would suspect that most of the performance comes simply from increased computation at test time.
- Little analysis is shown: beyond questions at the systems level, another clear demonstration of utility would come from comparing model performance to number of shots in context. If increasing the number of in-context examples also increases performance, that would provide a compelling case for practitioners.
- Finally, does this help more out-of-domain? One would expect in-context examples to be most useful (or perhaps even *only* useful) when the test task is most different from the training task. Is this true in your case?

### Questions
- Does performance get bewtter by using more examples in context?
- At test time, are few-shot examples selected per-example or per-dataset?
- Do you pool over instruction tokens?
- Do you pool over ICL tokens?

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
The paper proposes an LLM-based text embedding model that supports in-context learning. The training recipe is fairly simple and straightforward and yields impressive empirical results in comparable settings. The experiments also validate the modeling choices, and suggest that complex architectural changes are not required for performance gains.

### Strengths
- Simplicity and intuitiveness of the technique.
- Strong and extensive empirical results
- Thorough ablations
 
I especially liked the ablation from Section 4.4, which shows that the simple ICL setup outperforms other architectural choices. Such ablations are necessary for disentangling the performance gains due to data and architectural changes.

### Weaknesses
The submission is not following the ICLR template because line numbers are missing

My main concern regarding the paper is that some key implementation details are missing (See Questions). Given the extra page limit and verbose Section 3.1 and Figure 2, I think the authors could have done a better job in covering those details.   

Other than that, NV-Embed2 results can also be included in the revision. 

Other comments about writing:
- The right two subfigures in Figure 2 are not really required. I would suggest removing them altogether or moving the figures to the appendix. 
- The use of "full data" vs. "public data" feels like a misrepresentation of "full data," given that "full data" is also public. I suggest using different terms. 

Typos:
- Use \citet{}. Section 2, second paragraph, second line 
- Section 3.1 - "task_definition" -> Fix the opening quote.
- Section 4.4, third paragraph - "align" -> "aligned"
- Training Details: "conduct the process over a single epoch" - I have never seen such language for describing "trained for a single epoch".

### Questions
- How exactly are the query and passage representations obtained? The last line of Section 3.1 suggests that the two are obtained using <EOS> embeddings. Are there two <EOS> tokens?
- Why are passages/documents truncated to 256 tokens, given that Mistral has 32K tokens and there are only a maximum of 5 documents? Are the gains on Long Doc evals in line with other gains, given that nothing in the architecture/training should benefit long documents in particular?
- In Evaluation, it's said that "a consistent set" is used for ICL evals. What is a consistent set? Do you mean fixed? How many examples?
- In Section 4.4, are all the ablations models trained similarly to the baseline model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces in-context learning to enhance text representation. Since decoder-only LLMs show good performance when adapting into text embedding tasks, this paper proposes to inherit LLM's in-context capability to handle unseen tasks effectively.

Unlike previous task-specific prompt engineering, randomly sampling some examples as the demonstration during training enables embedding model to do in-context learning while maintaining the zero-shot capabilities. The paper shows performance improvement when adding task demonstration to encode text representation. This method does not require additional data or model modifications, keeping the original architecture to preserve ICL capabilities.

### Strengths
1. This paper proposes a simple and effective method to enhance text representation. Even though ICL is a common way to enhance model's performance in LLM area, applying it into the text representation is quite reasonable. The experiments are strong and show a great advantage to previous methods.

2. This paper makes a comprehensive ablation studies to justify the methods. First, by aligning the experiment setting, the paper shows that few-shot text embedding is better than zero-shot text embedding. Second, the experiment on model architecture comparison shows that keeping the model architecture is crucial for ICL capabilities.

### Weaknesses
Unlike zero-shot text representation, ICL is highly sensitive to the chosen demonstrations. There are countless related works discussing that the selection and order of task demonstration affects the final performance. However, in this paper, the demonstration is not discussed well. The paper only mentions "a consistent set of in-context examples is applied to each query".

### Questions
1. Following Weaknesses 1, I believe not all of the demonstration can provide a positive influence on text representation. Therefore, I'm curious if you make a demonstration search, or the examples is just randomly sampled, or you report the average score of many demonstrations. 

2. I notice that LoRA is activated in training stage. Is it due to the computation budget limitation or performance consideration? If it is only for efficient training, I'd like to know if you have make comparisons on different LoRA rank, and if it is possible to use full training to further improve models 'performance.

### Soundness
4

### Presentation
4

### Contribution
4
