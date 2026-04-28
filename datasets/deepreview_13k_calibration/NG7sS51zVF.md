# Efficient Streaming Language Models with Attention Sinks

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
Deploying Large Language Models (LLMs) in streaming applications such as multi-round dialogue, where long interactions are expected, is urgently needed but poses two major challenges.
Firstly, during the decoding stage, caching previous tokens' Key and Value states (KV) consumes extensive memory.
Secondly, popular LLMs cannot generalize to longer texts than the training sequence length.
Window attention, where only the most recent KVs are cached, is a natural approach --- but we show that it fails when the text length surpasses the cache size.
We observe an interesting phenomenon, namely \emph{attention sink}, that keeping the KV of initial tokens will largely recover the performance of window attention. In this paper, we first demonstrate that the emergence of \emph{attention sink} is due to the strong attention scores towards initial tokens as a ``sink'' even if they are not semantically important.
Based on the above analysis, we introduce \method, an efficient framework that enables LLMs trained with a \textit{finite length} attention window to generalize to \textit{infinite sequence length} without any fine-tuning.
We show that \method can enable Llama-2, MPT, Falcon, and Pythia to perform stable and efficient language modeling with up to 4 million tokens and more.
In addition, we discover that adding a placeholder token as a dedicated attention sink during pre-training can further improve streaming deployment. In streaming settings, \method outperforms the sliding window recomputation baseline by up to 22.2$\times$ speedup.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes the addition of a placeholder token, called a token sink, to language models.This is motivated by the observation that significant attention mass is placed at the initial token positions in a sequence and performance deteriotes whenever tokens in this position are dropped/evicted. The authors carry out extensive experiments to validate this claim and make a convincing argument for the placement of a special token in the initial position, whose purpose is to help regulate and channel the attention mass across layers. This leads to stable language model performance at million-scale sequence lengths.

### Strengths
The paper is well written, the problem is well motivated with many experiments used to help make a convincing claim.

All code and datasets are made available, allowing for easy reproducibility and validation of claims made in this work.

### Weaknesses
The claims on long horizon performance need additional clarity and evaluation. I am not sure how practically useful this approach is for long-horizon language modelling.. For example, at million-scale sequence lengths, when intermediate tokens are evicted, how does performance translate relative to the evicted tokens? Doesnt it mean, the model is only practically useful for information covered at the beginning of the sequence and at the end?

There is a missing section on the broader societal impacts of this work.

### Questions
It is interesting to see how concentrated attention gets on the initial tokens as you go deeper into the model, could it be said that these tokens are carrying out some form of global memory/attention operation?

How does this work relate to [Vision Transformers Need Register](https://arxiv.org/abs/2309.16588v1).. This statement from this work reminds me of the registers paper; "As a result,
initial tokens are more easily trained to serve as attention sinks, capturing unnecessary attention"

Looking at the StreamEval benchmark, it would also be good to have an idea of how performance decays with length. How does it perform when you ask it a question related to line 1k, after it has seen 10/100k lines. This gives a better idea of long-context/sequence performance profile than consistently quering only 20 lines prior. I would be willing to improve my score if i had better insight of how this method performed on such a benchmark over (extremely) long horizons. How it performs relative to the evicted tokens.


Update: Authors addressed all my questions.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on the challenge of efficiently scaling and generalizing beyond the training sequence length for large language models. Specifically, they propose to cache and attend to the initial tokens of the sequence in addition to the most recent tokens used in window attention. The main motivation behind this proposal is the "attention sink" phenomenon that is caused by the strong attention scores toward initial tokens that are accumulated as the sequence increases. Since this method introduces this simple change of attending to the initial tokens, it can be applied to any LLM; they also show it is possible to train the model with a single token as attention sink for further efficiency. Experiments on a models of vaying model size show that it allows them to generalize far beyond their context window and it is much faster than sliding window with recomputation.

### Strengths
- Several methods have been introduced in the past for generalizing to longer context lengths but most of them require training the model from scratch or through continued training. The observation that this paper is making about the attention sink phenomenon is fascinating and inspires a simple solution that requires no additional training that prior work has overlooked. 
- The paper is positioned well wrt. prior length generalization work and shows how different relative positional embedding methods such as RoPE anD Alibi can be combined with attention sinks. The fact that it can be combined with any of these methods with minimal effort makes it potentially very impactful; virtually any transformer model can be modified to handle large context sizes in this way. 
 - The exposition is clear and experimental part well executed. The empirical analysis based on actual attention logits and the theoretical explanation of why it happens is convincing and intuitive. 
- Evaluation covers models of different sizes and different metrics (perplexity and downstream performance) and shows that proposed attention is effective across all sequence lengths.

### Weaknesses
 - The proposed attention is reminiscent of methods that introduce sparse attention patterns such as Sparse Transformer but there is no in-depth discussion that draws a connection.
- Even though attention sinks maintains the perplexity levels in check for extremely large sequence lengths, the paper does not study in detail on how good utilization of the context the model is doing.

### Questions
- Have you considered evaluating on a benchmark for long-range tasks such as LongBenh, MuLD or Long-range arena? It would help quantify limitations of the proposed attention in terms of context utilization.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper demonstrates that the first few token(s), called attention sink, take most of the attention scores in large language models and propose StreamingLLM by keeping them in the KV cache. StreamingLLM achieves significant speedup compared to the baseline of sliding window attention with recomputation while having reasonable language modeling perplexity and zero-shot accuracy on several NLP benchmarks. Additionally, the authors pre-trained a small language model with a single learnable sink token so that StreamingLLM can only use one token for attention sink.

### Strengths
Improving the efficiency of language modeling with long text input is a practically important and very timely topic. The paper is well motivated and structured in that it first introduces problems, suggests an easy and effective solution, and validates it with experiments and required ablation studies.

### Weaknesses
StreamingLLM is compared with only very basic baselines (i.e., (a) dense attention, (b) window attention, and (c) sliding window with re-computation) without alternative ways to use LLMs with longer inputs. The authors argue StreamingLLM’s 22.2x speedup compared to (c), but it looks too extreme because there could be a sweet spot that could achieve reasonable ppl and inference speed by sliding window with appropriate strides (less frequent re-computation instead of every step). 

The paper argues that StreamingLLM can handle infinite sequence length, but again the abovementioned basic baselines on PG-19 are used to show this. Experiments on benchmark datasets that truly require long context modeling are necessary. Also, providing numbers of SoTA models on PG-19 could be helpful in understanding how absolutely StreamingLLM performs well, though accuracy might not be the main interest of this paper. Particularly, using a small size cache (not beyond the training sequence length) makes it suspicious whether StreamingLLM is capturing long context information well. I guess it will have difficulty utilizing information from tokens that do not belong to the cache at the prediction step, and this can be easily checked with synthetic datasets (e.g., Little Retrieval Test).

There have been several previous works that observe position bias on attention patterns in transformers. Also, there are existing architectures, including LongFormer, BigBird, and ETC, that have global tokens for attention, though most of them are encoder-based language models. It is worth having a discussion on them.

### Questions
Could you elaborate more on why (1) window attention blows up and (2) attention sink exists?
I think current explanations are mostly empirical and not theoretically grounded. Specifically, I agree that attention scores could be skewed toward earlier tokens due to the autoregressive nature of language models. However, why very few (less than 4) tokens are enough to cover most attention scores?

Visualization on a short sequence (length 16) in Figure 2 might not be enough. Does the same phenomenon occur for longer sequences, which is our main interest? I guess some important tokens with high attention scores might be shown up for each text (of course, it will not be shown if you average per position over different texts). Do you have any quantitative values on how much attention sink occupies the attention scores (especially for longer inputs)?

In Figure 3, MPT has different patterns from other LLMs. Is it because MPT uses ALiBi and others use RoPE? Any explanation?

Regarding pre-training with a sink token, I think reducing 4 -> 1 is not important considering the large size of the cache. Am I missing? It could be marginal but why is a model with a sink token consistently better than the vanilla one? An LM with 160M parameters is used, and I understand this is because of the academic budget. I am just wondering if the same conclusion can be guaranteed for larger LMs. 

In Figure 10,  why do two options have different memory usage for 4096 cache size?

This paper uses the attention sink for efficient streaming of LLMs. However, my one aspect is having attention sink is a kind of artifact of autoregressive LLMs not fully utilizing its representation power. Can we make/train LLMs not to have the attention sink for better performance?

There is almost similar concurrent work: LM-Infinite (https://arxiv.org/abs/2308.16137). It is not required, but how do you compare your work with this?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces StreamingLLM, a framework that enables large language models (LLMs) to handle infinite sequence lengths without fine-tuning. The paper makes the following contributions:

- It observes the attention sink phenomenon, which means that LLMs tend to allocate a lot of attention to the initial tokens, regardless of their semantic importance.
- It proposes the StreamingLLM framework, which leverages the attention sink phenomenon to retain only the most recent tokens and a few attention sinks, discarding intermediate tokens. This allows LLMs to generate coherent text from recent tokens without a cache reset.
- It suggests adding a placeholder token as a dedicated attention sink during pre-training, which can further improve the streaming performance of LLMs.
- It demonstrates that StreamingLLM can enable models like Llama-2, MPT, Falcon, and Pythia to perform efficient language modeling with up to 4 million tokens.

### Strengths
- This paper studies an important topic/setting on the long context of large language models, how to enhance LLMs to handle long/infinite sequence without fine-tuning.
- Attention sink phenomenon is remarkably interesting. It was found that retaining the KV of initial tokens can significantly improve the performance of window attention. 
- This paper poses comprehensive experimental investigations on different large language models, and it also shows that StreamingLLM outperforms other baselines by up to 22.2× speedup in streaming settings.
- The paper is well written, clear to follow.

### Weaknesses
See Questions Section

### Questions
- The authors focus on LLMs that are autoregressive, meaning that they generate text one token at a time, conditioned on the previous tokens. Dose the attention sink phenomenon exist in other types of models, such as bidirectional models (e.g., BERT) or non-transformers models?
- Can attention sink be applied to the pre-training stage, retaining more placeholders from scratch to further improve the performance?
- Does this phenomenon also exist in larger models like Falcon-40B, LLaMa2-70B?
- Does the Group Query Attention structure have any impact?
- If you combine proposed Attention Sink with Sliding Window w re-computation, I wonder whether it performs better than re-computation.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
