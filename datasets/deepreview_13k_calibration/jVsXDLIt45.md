# Nugget 2D: Dynamic Contextual Compression for Scaling Decoder-only Language Models

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Standard Transformer-based language models (LMs) scale poorly to long contexts. We propose a solution based on dynamic contextual compression, which extends the Nugget approach of Qin & Van Durme (2023) from BERT-like frameworks to decoder-only LMs. Our method models history as compressed “nuggets” which are trained to allow for reconstruction, and it can be initialized with off-the-shelf models such as LLaMA. We demonstrate through experiments in language modeling, question answering, and summarization that Nugget2D retains capabilities in these tasks, while drastically reducing the overhead during decoding in terms of time and space. For example, in the experiments of autoencoding, Nugget2D can shrink context at a 20x compression ratio with a BLEU score of 98% for reconstruction, achieving nearly lossless encoding.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
# Response to the authors rebuttal

Thanks for your response.

My biggest concern to this paper is that its main claim on scaling LLM to handle long contexts is not sufficiently supported by its experiments. The authors conducted their experiments on NLP tasks with less than 1k tokens, including WikiText (640+64), SQuAD (231) and CNN/DailyMain (878). In the response, the authors also provides an experimental result, i.e. "the maximum context length for encoding is ~1200 tokens", and admit a fact, i.e. "it is still tough to conduct experiments with contexts longer than 2000". Although the authors say that limited computational resources, i.e. 32G V100, prevents Nugget2D from scaling to longer context, it is still doubtful if Nugget2D could process context with 10k or even more tokens on an advanced 80G GPU, given the theoretic memory complexity of 
$O(m^2+n^2+mn)$. The complexity in autoregressive transformer seems a techniqucal error given an n-lengthed input, by ingoring the compressing process in Nugget2D.

In conclusion, I think this paper (Nugget2D with maximum 1200 tokens) does not contribute to long-context sequence modeling community, with observation on rapid progress in this field, such as RMT (1M tokens, 2023/4), AutoCompressors (30k tokens, 2023/5) and ChatGPT (4k->32k tokens, 2022/11-2023/6).

References:

Scaling Transformer to 1M tokens and beyond with RMT. Bulatov et.al. 2023/4

Adapting Language Models to Compress Contexts. Chevalier et.al. 2023/5

GPT4 Models: https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo


# below is the original review

The authors propose NUGGET2D, a NUGGET extension, to solve long context modeling problem for existing LLMs. 
The main idea of NUGGET2D is to dissect the contextual tokens into local and global parts.
The local tokens are fully kept for attention and the global tokens are progressively filtered out by a threshold score.
The proposed method is tested on three tasks, i.e. language modeling on WikiText and Pile, question answering on SQuAD and summarization on CNN/Daily Mail.

### Strengths
1. The idea is well-motivated that only part of contextual token representations are informative.
2. The redicual connection modification to ensure differentiability is novel.
3. The empirical results look good.

### Weaknesses
1. The experiments are not sufficient to support the main contribution of scaling autoregressive LLMs to long contexts, comparing with recent long-context LLM studies (e.g. RMT, LongLLAMA). The experiments are conducted on tasks with relatively short context lengths: WikiText (640+64 tokens), SQuAD (231 tokens), and CNN/DailyMail (878 tokens). These context lengths are significantly shorter than what is considered 'long context' in recent literature, which often targets tens of thousands to millions of tokens. The claim that NUGGET2D can handle long contexts is not adequately validated by the provided empirical evidence. The experiments do not explore the performance of NUGGET2D on tasks that truly require long-range dependencies.
2. The idea is quite simple by splitting context tokens into local and global tokens, where the distinguishable part is compressing global tokens with a layer-wise NUGGET. While the authors introduce a residual connection modification to ensure differentiability, the core concept of selectively compressing global tokens based on a threshold score is not fundamentally novel. The method essentially performs a form of token pruning, which has been explored in various forms in prior work. The novelty of the approach is incremental rather than transformative, and the method's effectiveness in handling long contexts remains unproven.


### Questions
1. The baseline is relatively limited. It would be good to see other long-context LLMs (e.g. LongLLAMA[1]) as baselines.
2. I wonder how the memory grows as the context length increases against other context scaling methods. It seems the memory complexity in training stage is $O(n^2 * r)$. What is the limit of the context length of your model?
3. The context length of downstream tasks is really short. Do you ever try other dataset for long-context downstream task evaluation, such as Multi-News[2], Narrative QA[3] and CUAD[4].
4. What does "100k tokens" on $5.2 stand for? Does it mean context length? How is the random selection process performed?


[1] Focused Transformer: Contrastive Training for Context Scaling. Tworkowski1 et. al. 2023

[2] Multinews: A large-scale multi-document summarization dataset and abstractive hierarchical model. Fabbri et.al. 2019

[3] The narrativeqa reading comprehension challenge. Kocisky et al. 2017

[4] CUAD: An expert-annotated nlp dataset for legal contract review. Hendrycks et al., 2021b

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Qin and Van Durme (2023) proposes NUGGET for encoder-decoder transformer models where the input context to the encoder is "compressed" and represented by selected tokens to be conditioned on during decoding. This paper proposes NUGGET2D that extends the idea to decoder-only transformers. The "nuggets" are not just the last layer representations from the encoders, but representations of selected tokens in a context on every layer to be conditioned on in decoding the answer. Promising results are shown on autoencoding, language modeling, summarization, and question answering.

### Strengths
- The method is a novel and useful technique to process long contexts.
- The experiments on multiple important tasks show promising results.

### Weaknesses
### weaknesses:
 - Typo: Before Eq (8) I think you mean "\textit{recent} tokens $w_{\tau+1:t}$" -- $t$ instead of $i$.
- The presentation can be improved and multiple questions need to be clarified. Please see Questions. -- Willing to increase the score once the questions are clarified.

- The definition of the NUGGET2D function in Sec. 2.2 is unclear. Specifically, the role of $\phi$ and its relation to the function's output needs further elaboration. The notation is inconsistent, as "NUGGET2D" is used as both a function and a method name.

- The relationship between $\mathbf{x}_i^l$ and $\phi$ in equations (2), (3), and (4) is not explicitly stated. It is unclear whether these hidden states are computed using $\phi$ exclusively or if $\theta$ also plays a role.

- The training methodology for the Scorer, as described in [1], is not adequately explained in Section 2.1. A more detailed description of the Scorer's training process, including the residual connection, is necessary for a complete understanding of the proposed method.

- The rationale behind removing $s_j$ from Eq. (5) after the Scorer converges is not well-justified. The potential impact of this removal on the model's activations and overall performance needs further investigation and clarification.

- The process of selecting $\tau$ in Section 2.5 is not clearly defined. A more precise explanation of how $\tau$ is determined and its significance in the context of long sequences is needed.

- The paper lacks a detailed analysis of the space overhead introduced by the additional model parameters, particularly since $\phi$ and $\theta$ are not tied. A quantitative assessment of the memory footprint would be beneficial.

- The potential for information loss due to the nugget selection being based solely on $\phi$ and not $\theta$ is a concern. It is possible that tokens with significant contextualized representations according to $\theta$ might be overlooked.

- The first paragraph on page 5 is confusing and contains inconsistencies. The reference to $\theta$ in equation (11) is incorrect, and the concept of "re-assignment" needs to be clarified using more precise notation and explanation.

- The model's handling of long contexts, specifically whether it only processes $w_r + w_d$ tokens and ignores the beginning tokens, raises concerns about potential information loss. The suggestion of incorporating "gist" tokens to summarize the beginning tokens, as seen in other long-context processing papers, should be addressed.

### Questions
- Please define the NUGGET2D function in Sec. 2.2 NUGGET2D, including what is $\phi$, instead of letting readers figure out themselves. Later you use "NUGGET2D" as a function, but in Sec. 2.2 you only use it as a method name.
- Perhaps you could consistently use $\mathbf{z}$ to denote hidden states from $\phi$. In Eq. (2) (3) (4), are $\mathbf{x}_i^l$ computed using $\phi$ but not $\theta$? 
- How does Qin and Van Durme (2023) train the Scorer? You should also add the explanation to 2.1 Background.
- You mention in footnote 4 that Scorer quickly converges, and then $s_j$ can be removed from Eq. (5). How do you decide when to remove it? Do you first train all trainable parameters (based on the task) with $s_j$, and then just continue to still train all trainable parameters without $s_j$? Removing $s_j$ will cause all activations to change suddenly; not sure if it's a problem.
- In Sec. 2.5, can you clarify how you pick $\tau$?
- Can you provide analysis about how much space are used by the extra model parameters when you introduce NUGGET2D?  I notice that $\phi$ and $\theta$ are not tied.
- The nugget tokens are picked based on $\phi$ but not $\theta$. Is it possible that some tokens' contextualized representations according to $\theta$ has much information but is not selected based on $\phi$?
- First paragraph on page 5 is confusing, e.g., you said $\theta$ in eq (11) but there's no $\theta$ in eq (11). Please clarify what re-assignment means with more understandable notations.
- Is it true that the model only processes $w_r+w_d$ tokens and ignore the beginning tokens if the context is long? Would it be helpful if, like in many long-context processing papers, you still have some "gist" tokens to summarize the beginning tokens?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper extends the Nugget approach [Qin, Durme, '23] from encoder-decoder architectures to decoder only architectures and explores its applications to compression of context in auto-encoding, auto-regressive decoding and downstream tasks like QA and summarization.
In all applications, the context to be compressed is encoded by a Nugget2D encoder, which seems to be a vanilla transformer encoder (initialized by some Llama variant LLM). The encodings are passed through a scorer and embeddings from the top-k scores are selected (similar to the original Nugget paper). Finally a separate LM (again initialized using some Llama variant LLM) operates on the actual task, encodes prompt/question and decodes the answer. This LM is trained to attend to only the selected nugget encodings. To easily propagate gradients to the scorer, during this attention mechanism between LM and nugget encoder, the scores are added to the attention logits (similar to the original nugget paper). The LM, nugget encoder and scorer are finetuned using PEFT.
The paper demonstrates that on the task of auto-encoding, Nugget2D outperforms ICAE, which allocates fixed size memory for compression, on the auto-regressive LM task, Nugget2D outperforms "Compressive" baseline, which pools the embeddings of context divided into constant sized chunks. On the QA task, their model retains 90% of the performance of an uncompressed baseline at 5x compression. Interestingly on the summarization task, their model outperforms baseline without an compression.

### Strengths
Main strength of the paper is to show that the original Nugget approach can be scaled and adapted to be used by LLMs. The technique is also adapted to various use cases: auto-regressive LM, auto-encoding and downstream tasks. They show strong results compared to baseline approaches considered in the paper.

### Weaknesses
The weaknesses of the paper are as follows:
1. The novelty of the key idea. Extending nugget to nugget2D seems to be a straightforward extension by changing the residual connections.
2. Some experimental results/comparisons are not clear.
    a) The results of the section 4.2 are not provided in a table, but depicted in a figure: figure 4. I found Figure 4 to be hard to    interpret and not clear at all. What do the bars represent there, ICAE bar is missing for x axis values 100, 200, 300?
    b) For results in 5.2, are the number of trainable parameters for Compressive and nugget 2D comparable? nugget2d employs an encoder and an LM, whose parameters are fine-tuned separately. How does this compare to compressive?
3. Some missing details about the method and training:
    a) Is "informed nugget encoding" used in the original nugget work still applied in this work?
    b) In section 2.5, Choice of k, its mentioned that the scorer is not trained on the autoregressive text continuation task, but taken from     the autoencoding experiments, why is that?

### Questions
1. In Fig 2, the attention pattern of the LM is shown, what is the attention pattern within Nugget2D?
2. In equation 4, do (i, j) represent all possible indices, or are some indices restricted to a subset chosen by the scorer?
3. Is "informed nugget encoding" used in the original nugget work still applied in this work?
4. In section 2.5, Choice of k, its mentioned that the scorer is not trained on the autoregressive text continuation task, but taken from     the autoencoding experiments, why is that?
5. For results in 5.2, are the number of trainable parameters for Compressive and nugget 2D comparable? nugget2d employs an encoder and an LM, whose parameters are fine-tuned separately. How does this compare to compressive?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
