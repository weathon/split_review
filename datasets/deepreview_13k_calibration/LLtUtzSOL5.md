# Assessing Episodic Memory in LLMs with Sequence Order Recall Tasks

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 3, 6, 8

## Abstract
Current LLM benchmarks focus on evaluating models' memory of facts and semantic relations, primarily assessing semantic aspects of long-term memory. However, in humans, long-term memory also includes episodic memory, which links memories to their contexts, such as the time and place they occurred. The ability to contextualize memories is crucial for many cognitive tasks and everyday functions. This form of memory has not been evaluated in LLMs with existing benchmarks. To address the gap in evaluating memory in LLMs, we introduce Sequence Order Recall Tasks (SORT), which we adapt from tasks used to study episodic memory in cognitive psychology. SORT requires LLMs to recall the correct order of text segments, and provides a general framework that is both easily extendable and does not require any additional annotations. We present an initial evaluation dataset, Book-SORT, comprising $36$k pairs of segments extracted from $9$ books recently added to the public domain. Based on a human experiment with $155$ participants, we show that humans can recall sequence order based on long-term memory of a book. We find that models can perform the task with high accuracy when relevant text is given in-context during the SORT evaluation. However, when presented with the book text only during training, LLMs' performance on SORT falls short. By making it possible to evaluate more aspects of memory, we believe that SORT will aid in the emerging development of memory-augmented models.co/datasets/memari/booksort}{https://huggingface.co/datasets/memari/booksort}}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a new dataset, called SORT, for assessing episodic memory in LLMs, centered around the task of recalling the correct order of two short book snippets. The authors report extensive evaluations of modern LLMs on the proposed dataset, studying both in-context and "parametric" memory (memory encoded in weights and acquired during training), as well as externally augmented memory options. They find that modern LLMs can use in-context memory quite well, but struggle when the relevant context is only presented during training.

### Strengths
The paper addresses a highly important topic of assessing memory capabilities in LLMs.

I appreciate the attention to statistical detail reporting, and the generally thorough reporting of the experiments.

The paper is well-written.

The inclusion of human baselines, especially with the clever involvement of Goodreads users, is a great addition to the paper.

### Weaknesses
 ** Significance and novelty **

I believe that the work, overall, is sufficiently novel. At the very least, it provides a unique and potentially useful dataset.
I'm however, very conflicted on the significance of this work.

First, the authors do not discuss whether the notion of Episodic memory in LLMs is valid at all. "Episodic memory" is not clearly defined in the paper, other than type of memory "which links memories to their contexts, such as the time and place they occurred".

If we take this definition, many general-knowledge questions can be seen as probing episodic memory. E.g. questions in the form of "what was the movie in which a <SCENE DESCRIPTION>?", and "Describe that scene in more detail", or "When was this movie created" which modern LLMs are well-equipped to answer.

Usually, in psychology, episodic memory is distinguished from declarative memory by being related to personal experiences as opposed to stated facts. This distinction is extremely moot in the case of LLMs. This seriously undermines the premise of the paper.

Moreover, the key psychological literature the authors cite actually refers to a specific subset of human episodic memory, namely temporal memory. This creates confusion. If accepted, the authors should consider changing "episodic" to "temporal" throughout the article. It's worth noting that preserving temporal order is not a necessary attribute of episodic memory. In fact, humans routinely mix up the order of their personally significant memories; a simple way to see that is to try to reliably order all of one's childhood memories.

Still, the problem is deeper than this mismatch in terms. With no clear distinction between "personal" and "stated" memories in LLMs, what is the importance of studying temporal memory in LLMs in the way that authors suggest? Why, and to what extent, do we equate personal experiences with the order in which a some information is presented in the data?

If this is a way to address the issue of correcting LLM memories - why isn't there a deeper discussion of alternative methods and of how exactly this dataset will benefit the effort. If this is about whether or not LLMs can remember the order of things presented in contiguous chunks in training data - we know very well that LLMs are very good at that, e.g. that common mathematical sequences can often be retrieved if included in the training data. If it's about in-context handling of long sequences - why isn't there a more thorough discussion of other datasets that look at long-context tasks?

** Quality of the experimental support **

When it comes to human evaluation, the experiment seems well-organized and adds a lot of value to the paper.

I am, however, very troubled by many fine-tuning results and experimental decisions. 

*Data ratio
The ratio of the new data to instruction data is very strange: the authors keep 3500 instruction following prompts "to avoid catastrophic forgetting", when there are only 116 independent book samples. It's very likely that in these conditions, the models simply do not have enough incentive to learn book-specific information. Additionally, the instruction fine-tuning stage behind Llama and Mixtral models is much more extensive than the 3500 instruction samples. Therefore, most likely, doing full fine-tuning on such a restricted sample severely hurts model performance across the board, making results hard to interpret. As I mention later in this review, it's not entirely clear why the authors even try to "preserve the models’ ability to understand and follow the task instructions" instead of simply fine-tuning a classification head for their specific task.

*Unusual training stage order:
Instruction fine-tuning and raw language modeling stages are mixed. I don't know how it affected results, but again, it makes interpretation harder. Instead, the authors could have chosen a much simpler two-step process: First, a language modeling fine-tuning stage on the books of interest (main condition) or on irrelevant books (control). Second, transfer learning fine-tuning with a classification head, treating SORT as a binary classification task. This would remove the need to keep a bunch of instruction-tuning samples and would clarify the results substantially. I understand that not all types of evaluations can be performed on these models, but that would more definitively answer whether LLMs can remember temporal information from their training set.

*Concerning training dynamics:
Another issue is that according to figure 16, the log probability of the correct answer is dropping with each new epoch. This is deeply concerning, and suggests that something is fundamentally wrong with the environmental set-up.

*Apparent failure to overfit:
It is well-known that LLMs are extremely good at verbatim memorization, and can overfit to memorize extreme amount of information. I am absolutely certain that the LLMs considered in the paper can be fine-tuned to memorize 9 books verbatim. The most likely reason that we didn't see improved performance is, then, either 1) inadequate training setup 2) inadequate methods of probing/information extraction (e.g. the model has the memory but its zero-shot skills are so degraded that it can't use this memory). Perhaps the authors are interested not only in whether a given "episodic" memory is implicitly present in LLM's parameters, but also whether it can it be used via zero-shot prompting? But that seems like a substantially different research question.

The last quality issue, not related to fine-tuning, is that the dataset is destined to become obsolete. I.e. as the public domain books in question enter the training sets of new LLMs, much of the dataset's value will be lost, and the reported results won't be comparable to an attempted replication on newer LLMs. I don't think this is a disqualifying consideration, but it does negatively affect the significance and potential impact of this work.

Overall, these issues largely invalidate the conclusions on whether parametric memory in transformer can be seen as a form of episodic memory.

A minor note: I believe it'd be beneficial to the paper to add an extra classification baseline where a model is finetuned to predict which segment comes earlier in a book, without any context. It's the same as "Baseline" in the paper, but with fine-tuning. The reason it's important is that it could be that zero-shot instructions are not enough to extract this information from the model. Of course, since there are only 9 books in the dataset, it'd be necessary to either do cross-validation (fine-tune on 8 books, evaluate on 1).


** Summary **

Overall, I highly resonate with the importance of creating new datasets to thoroughly evaluate LLM memory capacity. I deeply appreciate the inclusion of a human-subject study and a thorough approach to evaluation. That being said, unfortunately, I can't recommend the work for acceptance.

The main issue is the positioning of this work in the broader context. What exactly is the problem we are trying to address? Is this a useful benchmark that should use to test memory capabilities of new models, or is it more of an investigation into the nature of episodic memory in transformers? I feel that the paper attempts to tackle both questions at once, but, as a result, does not sufficiently address either. Another substantial problem is the experimental support: I find that many of the fine-tuning experiments are not sufficiently clearly constructed and executed.

My true overall score for this submission is 3.5, or 4. I think that even if published as is, it will provide some positive value to the community. That being said, unfortunately, in its present form, it is not strong enough for ICLR.

### Questions
I am sorry I could not provide a more positive evaluation. Clearly, a lot of work went into this paper, and it pains me to recommend a rejection. I deeply hope that the authors can slightly re-focus the paper, making it more focused on a specific problem or question. And if the question is the nature of LLM memory as compared to human memory, a much deeper discussion of characteristics and properties of different types of human memory would be necessary. It's also important to clearly decide on the distinction between having a memory and being able to access it. For example, some model might be able to recite Hamlet, but be unable to answer questions about it. Should we treat such a model as having the memory of Hamlet or not? In any case, the fine-tuning experiments need to be improved, as right now they are, in my view, the weakest part of the paper. Again, I am sorry I can't provide a more positive assessment at the moment. 

I hope the authors continue their work and I'd be happy to see a revised version of this paper published one day.

I will also, of course, read the other reviews and the rebuttal. I am not sure how likely it is, but I will be open to reevaluate my assessment if it turns out that I overlooked some important considerations.

Questions:

What is the criterion for having an episodic memory? If a model has it "implicitly" (see the Hamlet example above) -- does it count?

What was the reason behind trying to maintain instruction-answering capabilities of the LLMs instead of switching to a simple Supervised Fine-Tuning classification task to see if the information is internalized?

What is the main goal of the paper? Specifically, do the authors see it as more of an inquiry into the nature and characteristics of LLM memory, or is it primarily a benchmark to evaluate the newly released models' memory capacity?

Minor:
On line 162, the authors say that the segments are "preceded by X", which would mean providing the whole book. But this contradicts the actual experiments where only book samples are actually presented due to context length limitations.

** Extra sources **
If we treat this paper as primarily a useful benchmark for assessing trainsformers' memory capability, NarrativeQA (https://huggingface.co/datasets/deepmind/narrativeqa) and, even more so, NarrativeXL (https://arxiv.org/pdf/2305.13877), datasets propose a different approach to a similar problem of assessing long-term memory in transformers, and use a similar methodology. These and related works should probably be discussed to better define the role of the present contribution.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a new evaluation task called the Sequence Order Recall Task (SORT) to assess episodic memory in large language models (LLMs). SORT requires models to recall the correct order of two text segments extracted from longer sequences. The authors create a dataset named Book-SORT, consisting of 36,000 pairs of text segments from nine books recently added to the public domain. They also conduct a human evaluation with 155 participants who had recently read one of the books, demonstrating that humans can recall some segment orders based on long-term memory, especially when the segments are far apart. The paper evaluates various LLMs on SORT using different methods of memory insertion, such as in-context learning, fine-tuning, and retrieval-augmented generation. The main finding is that models perform relatively well when given relevant context but fail to recall the order when using only their parametric memory.

### Strengths
- **Valuable Human Evaluation**: The paper conducts a large-scale human evaluation involving 155 participants who recently read a book. This provides valuable data on human long-term memory performance in recalling the order of text segments.

- **Highlighting Limitations of Parametric Memory**: Although simple, the paper rightfully brings attention to the limitations of current LLMs' parametric memory in handling one of the episodic memory tasks (here segment order). This is important for raising awareness and fostering further research in this area.

### Weaknesses
 - **Little coverage of episodic memory** The correct order of text segments is one tiny aspect in a large spectrum of episodic memory capabilities: (i) places/spaces in which events occured, the (ii) intricate sorting of events and entities that are tracked along long periods of time. For example, we are able not only to sort the major events of our life, but also the major events that happened within the lifetime of a six-months long project, or the major events that happened in a movie, or a novel. We are able to sort, and recall the spatial and action details etc.


- **Reported events vs. "encountered" events** For humans, and LLMs in particular (for which language is also a *reporting tool* of episodic events), there are other aspects that matter: For example, what are the actual order of events as they happened in time (as reported by language), not only as they were told to the reader/LLM sequentially. Does it make sense to ask a model which book appeared first in its training set? but if so, based on which epoch? Are LLMs equipped to answer this type of questions? Wouldn't this task simply only test the positional encoding/embedding abilities of LLMs? because that's the only fundamental signal that allows them to know what comes before what.


- **Benchmark contamination** Although recently added to the public domain, the books are old and there are chances that they are part of the training data. I appreciate that the authors did the effort of verifying that the models failed to answer using only their parametric memory (e.g. Table1), but one cannot rule out that pre-training could have helped in the in-context task. 


- **No significant technical innovation in methodology**

### Questions
- Older versions of GPT4 used to know by heart some of the books on the gutenberg project ("the Murder of Roger Ackroyd" is present there). Did you ensure that the models did not know the book? (e.g. by asking questions?) 

- Why is the evaluation on GPT4-o missing from the second part? Would it be possible to include GPT-4 results or explain their omission?

- In which way your work is different from simply testing positional encoding capabilities of LLMs? Would it be possible to add analysis distinguishing positional encoding from true temporal understanding?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a new evaluation framework, Sequence Order Recall Tasks (SORT), designed to assess episodic memory in large language models (LLMs). Unlike traditional benchmarks that focus on semantic memory, SORT requires models to recall the order of text segments, assessing memory that links content to its context. The authors created Book-SORT, a dataset of 36,000 text segment pairs from nine public domain books, and conducted human experiments, showing that humans can remember sequence order from long-term memory with notable accuracy. Their findings indicate that while models perform well with in-context memory, they struggle with SORT when only trained on book content, highlighting current LLMs' limitations in true episodic memory.

### Strengths
1.  The paper offers a simple yet effective task, easily understandable and extensible to various settings. The general formulation of SORT enables adaptation to multiple domains and sequential data types, such as video or audio, enhancing clarity and future applicability.
2. The authors have open-sourced both the Book-SORT dataset and the code, ensuring reproducibility and enabling further research by the community.
3. The paper features multiple experiment setting, covering in-context memory, Retrieval-Augmented Generation (RAG), and fine-tuning methods.

### Weaknesses
1. Although the SORT task is positioned as an assessment of episodic memory, the simple task of sequence order recall does not fully capture the complexities of episodic memory as seen in humans. Episodic memory typically involves more than the temporal order of events; it also includes contextual elements such as the significance, location, or source of memories. As currently designed, SORT assesses temporal ordering without requiring models to associate segments with rich context or situational details.
2. The authors note in the related work that sequence order prediction tasks have been used in prior language models, such as BART, where sequence reordering is part of the training objective. SORT may therefore be too easy to offer a strong evaluation of advanced memory capabilities in LLMs.
3. While the paper includes a broad range of experimental settings (in-context memory, RAG, fine-tuning), it does not clearly identify which specific factors most significantly improve performance on the SORT task. Table 2 indicates that with in-context settings, models can achieve near-perfect accuracy (e.g., Mixtral-8x22b-inst reaches 0.95 accuracy). This high performance suggests that in-context memory alone might be sufficient for solving SORT.

### Questions
1. Given the results in Table 2, it appears that larger context windows may positively impact model accuracy on the SORT task. However, many of the models used in this study are limited to an 8k context window. Could the authors consider incorporating models designed for extended context lengths, such as LongLLaMA[1], to assess whether increasing the context window further improves SORT accuracy?
2. In the RAG setup, how sensitive are the SORT results to the choice of embedding model and vector dimensionality?
3. When using in-context learning for the SORT task, does the model exhibit a "Lost in the Middle" effect, where it struggles to differentiate the order of segments that appear in the middle of longer contexts?

[1] Tworkowski S, Staniszewski K, Pacek M, et al. Focused transformer: Contrastive training for context scaling[J]. Advances in Neural Information Processing Systems, 2024, 36.

[2] Liu N F, Lin K, Hewitt J, et al. Lost in the middle: How language models use long contexts[J]. Transactions of the Association for Computational Linguistics, 2024, 12: 157-173.

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
The paper proposes a new benchmark, SORT, for testing the episodic memory of and temporal order reasoning of LLMs, which is lacking in the current evaluation benchmarks. This test is inspired by cognitive sciences, and composed of pairs of randomly selected non-overlapping passages from fiction books, with a length of 20-50 words, which the model is provided with, along with contextual information in the form of an excerpt from the book, or without it. It is then asked to decide which of them precedes the other. Several setups are tested: Zero-shot prompting with and without context, with RAG, and finetuned on book data as a way to insert memory. The performance of the several models is compared to that of human baselines on this task (evaluated using 155 participants). 
The results show that without context models fail entirely in this task (with performance in the range of 50% - random chance). When given context, models succeed very well, but their performance degrades as the length of the excerpt increases. Finetuning on language modeling task with the book data does not improve the results much.
Due to these results, specifically degradation of performance with context length, authors surmise that the transformer’s context is more similar to working memory than episodic memory. Naive RAG can also not be considered episodic memory since it does not preserve order, and indeed performance is not high with this implementation. Order preserving RAG, with an oracle retriever, is successful.

### Strengths
* The authors builds a new task for assessing episodic memory which is a novel test for LLMs. This is done in a scalable way which can be used to generate more information if needed, and is furthermore carried out in a way that minimizes contamination.
* By using a no-context baseline, the authors show that the benchmark cannot be solved from temporal reasoning alone without knowing the context (~50% accuracy).
* Human evaluations are used to provide a human baseline on this task, which is very effective in understanding the limitations and successes of LLMs. 
* The authors compare the most common strategies used to adapt LLMs to specific tasks, and thus are able to compare and contrast them, which is also helpful when designing solutions based on LLMs that require this capability (specifically, pointing out that RAG naively does not perform well and that pretraining on book data does not help). 
* The authors compare several smaller and larger models (mostly open source) on this task which shows that performing well on this task is not just a matter of model size. 
* Authors perform prompt-optimization per model to reduce biases
Overall, many comparisons across different scenarios allow for a comprehensive understanding of LLM performance on this task.

### Weaknesses
 * It is very clear that the in-context scenario is relatively simple for LLMs. The paper thus hypothesizes that this is more similar to working memory. It would be interesting to compare to baseline human performance when shown the in-context SORT task, as a way of strengthening the claim. 
* Other than the fine tuning setup, the model cannot be said to have seen the entire book in any of the setups (this may be possible with long-context). This is markedly different from the human baseline, which also relies on long-term memory which makes comparison (and possibly relating the task to episodic memory) a bit more difficult.

### Questions
* Have you considered long-context models as a way of showing the model the entire book in context which may be more similar to the actual setup in humans?
* Why is GPT-4 present in the baseline tests but missing in RAG and In-context setups? It seems to have performed very well in the baseline.

### Soundness
3

### Presentation
3

### Contribution
3
