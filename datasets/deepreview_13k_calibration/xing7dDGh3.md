# Vector-ICL: In-context Learning with Continuous Vector Representations

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Large language models (LLMs) have shown remarkable in-context learning (ICL) capabilities on textual data. 
We explore whether these capabilities can be extended to continuous vectors from diverse domains, obtained from black-box pretrained encoders. 
By aligning input data with an LLM's embedding space through lightweight projectors, we observe that LLMs can effectively process and learn from these projected vectors, which we term Vector-ICL. 
In particular, we find that pretraining projectors with general language modeling objectives enables Vector-ICL, while task-specific finetuning further enhances performance.
In our experiments across various tasks and modalities, including text reconstruction, numerical function regression, text classification, summarization, molecule captioning, time-series classification, graph classification, and fMRI decoding, Vector-ICL often surpasses both few-shot ICL and domain-specific model or tuning. 
We further conduct analyses and case studies, indicating the potential of LLMs to process vector representations beyond traditional token-based paradigms.}\renewcommand\thefootnote{\arabic{footnote}}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies the feasibility of vector-ICL, that extends the in-context learning capabilities of LLMs to continuous vectors. Authors use light-weight projectors to align embedding space of input text embedding with LLM. To train the projectors, they use general language modeling objective followed by task-specific objectives. Authors experimented with multiple tasks and modalities, e.g., text classification, summarization, time-series classification, fMRI decoding, etc.

### Strengths
- The concept of using vectors for in-context learning is a new exploration, and the proposed methods for vector-ICL and evaluations show  promising results.

- Using light-weight trainable projectors with simple pre-training on general task is also not very expensive and can be integrated as a part of general LLM pre-training. 

- Experiments cover a wide range of tasks and modalities.

### Weaknesses
 - Method lacks depth. Specifically, replacing any length text for any complexity task with a single embedding may not be sufficient. Including an ablation where text is replaced with a series of vectors (one vector per sentence/ chunk) would be helpful.

- Currently, the method requires task-specific fine-tuning to outperform token-ICL. I think authors should explore RLHF/ instruction finetuning datasets/ objectives to avoid task-specific finetuning.

### Questions
- How do you see vector-ICL applied in practical scenarios, considering decreasing inference cost and increasing context length of LLMs?  Given your experiments show that without task-specific fine-tuning, vector-ICL consistently outperforms tokens-based ICL?

- Did you explore instruction tuning after pre-training? Authors should discuss the tradeoffs between task-specific finetuning and more general approaches like instruction tuning/ human preference training.

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
*Update after rebuttal*

After discussions with the authors my main concern was resolved. It appears that soft prompting with few-shot is a good baseline to demonstrate the power of Vector-ICL. I raised my score accordingly.

----------

The paper proposes a new method for in-context learning. By encoding examples into single vector representations via a separate, frozen encoder, and training a simple projection on top of the vector, LLMs are trained to perform ICL from continuous vector representations alone (Vector-ICL). The projection is trained a) via pretraining on unlabeled data and can optionally be b) finetuned on a labeled corpus.
The method is evaluated on a range of tasks, including text only tasks like text classification and summarization, as well as multi-modal tasks that utilize encoders for brain scans, graph data, or time-series.

### Strengths
* The proposed approach is simple to understand and implement.
* The method is evaluated on a wide range of tasks and datasets, including multiple modalities.
* Parts of the results suggests that the models perform better with more shots.
* The paper is relevant to the ICLR audience.

### Weaknesses
 * The paper claims that with finetuning the vector-ICL method outperforms standard ICL. However, The method's baseline is standard-ICL without any finetuning, i.e. the method compares a supervised method (albeit with a weak adapter projection P) with an unsupervised one. A baseline that is obviously missing is when finetuning the base model with standard ICL, perhaps using an adapter that is equally weak. For text classification and summarization, the soft prompting baseline may be adequate, but the reason for its inclusion is never discussed.
* The method is not well-motivated. In lines 34-38 it states that many data modalities cannot be well represented in natural language, making continuous vector representations necessary for in-context learning. While this is true, many of the experiments on non-textual either don't benefit from multiple shots or need to be trained on downstream data to work (e.g. time-series classification and graph classification in Figure 3, bottom). What's the value of Vector-ICL here? If you need to finetune a model to perform a task, can it still be called in-context learning?
* The paper structure could be better. The information pertaining to a particular task is scattered all over the paper, such that I found myself scrolling back and forth a lot. For example, I did not find Figure 3 particularly helpful because the information necessary to understand it fully is located far away from it (e.g. what the horizontal bar represents). I think it would be better to focus on fewer tasks in the main body of the paper, but explain these really well. The remainder could go into the appendix.

### Questions
* Figure 4a: Why does the correlation vary so much between datasets and models of similar size?
* Figure 4b: What do the axes represent?
* lines 477-479: Can you expand on the block patterns and how they are explained?
* How does the finetuning work precisely? Do you finetune with multiple shots already? If so, how many?

### Soundness
3

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
The paper is about projecting input data into an LLM embedding space, such that the LLM can perform in-context learning on the projections. The paper claims that this approach can improve the performance of the LLM on downstream tasks and opens up new application domains with Graphs, fMRI, and Time Series.

### Strengths
To the best of my knowledge, the proposed method is original (although some connections with soft prompt tuning should be discussed).
The paper is for the most part clear and the approach is interesting in the sense that it shows that LLMs can operate in-context on projected vectors. The results seem promising, as the learned projectors allow LLMs to tackle new tasks (graphs, fMRI etc) that are (assumed to be) not possible to tackle without projectors. The experimental part covers a wide range of tasks with different input types (8 tasks, with only 3 being classic text tasks and the proposed method beats its baselines in most cases. Clarity is generally good with some exceptions (see questions).

### Weaknesses
1. A weakness is that the projectors require pre-training with a language modeling objective and task-specific fine-tuning. It feels this defeats the purpose of in-context learning (i.e. not needing any training data to tackle a new task) to some extent. Authors can reflect if a change of the proposed methods name would be needed here.
2. Although the paper uses soft prompt tuning as a baseline, the relationship of the proposed approach with soft prompt tuning (Li and Liang, 2021; and follow-up work) is not explicitly discussed, i.e. as both methods learn some artificial token representations that are placed into the prompt.
3. The paper assumes that regular ICL is not applicable to Graphs, fMRI, and Time Series. While arguably not a natural fit, this assumption should be supported by some experiments, e.g. just using the numerical PCA vectors as text, or some flattened representation of the graph edges. As people have even thrown the parameters of another LM at an LM -- just in text format, I could imagine that even those non-text data types could be successfully encoded as text in a more straightforward manner without the need for training artificial tokens.
4. The experiments on time-series, graph classification and two fMRI tasks do not have a baseline, but only compare the pretrained-only projectors with fine-tuned projectors. It would be interesting to see how the proposed approach compares to some standard baseline of the respective domain, i.e. graph neural networks for graphs.

Minor point: In terms of presentation, the results description could directly link to the results, even if repetitive, e.g., Fig 3.

### Questions
q1: How does the proposed approach differ from soft prompt tuning (Li and Liang, 2021)?

q2: In 3.3 it is mentioned that the LLM would be trained with ``conditional generation loss''. However, in Figure 2b that is referred to, the LLM is supposed to be frozen. Could you clarify this point and explain the training process in more detail, including which components are frozen and which are updated during a) pre-training and b) fine-tuning?

q3: For Time Series (l 346), it is mentioned that you use the output of the last time step from Chronos-base. Doesn't this mean that the model is not able to use the full context of the time series but just the final state? What are the trade-offs between using the full context of the time series and just the final state?

### Soundness
3

### Presentation
2

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
The paper explores using embeddings for examples in in-context learning (ICL), which may be more suited in non-textual tasks. The paper proposes a light-weight pretraining and finetuning scheme to obtain the encoder. The paper shows improvements over textual ICL on various non-textual tasks.

### Strengths
The paper identifies an interesting research problem and presents a well thought-out exploration. The idea of using embeddings for conditional generation has been explored n various indirect forms (e.g., [1]), but the paper's focus on ICL seems to be a useful contribution.

[1] Text Embeddings Reveal (Almost) As Much As Text (Morris et al., 2023)

### Weaknesses
1. The proposed framework is back to encoder-decoder. In this context, previous works like Flan-T5 have thoroughly explored the model's ICL capabilities [2]. While the paper differs since it focuses on a single embedding  and non-textual tasks, it's a bit odd to omit this context.

2. Intuitively vector-ICL should not work as well as textual ICL for a lot of tasks. Clearly if the task requires a lot of symbolic data ICL is strictly more powerful than the proposed approach. But the paper seems to mostly show positive results. It'd be good to do some exploration of the cases vector-ICL is worse than textual ICL and by how much.

### Questions
N/A

### Soundness
4

### Presentation
4

### Contribution
3
