# Chunk, Align, Select: A Simple Long-sequence Processing Method for Transformers

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 3, 8, 6

## Abstract
Although dominant in natural language processing, transformer-based models still struggle with long-sequence processing, due to the computational costs of their self-attention operations, which increase exponentially as the length of the input sequence grows. To address this challenge, we propose a \textbf{Sim}ple framework to enhance the long-content processing of off-the-shelf pre-trained transformers via three steps: \textbf{C}hunk, \textbf{A}lign, and \textbf{S}elect (SimCAS). More specifically, we first divide each long-sequence input into a batch of chunks, then align the inter-chunk information during the encoding steps, and finally, select the most representative hidden states from the encoder for the decoding process. 
With our SimCAS, the computation and memory costs can be reduced to linear complexity. In experiments, we demonstrate the effectiveness of the proposed method on various real-world long-text summarization and reading comprehension tasks, in which SimCAS significantly outperforms prior long-sequence processing baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper induces attention sparsity by selecting the positions of Key and Value in \textbf{cross-attention}.  The proposed method first chunks a sequence into blocks, then aligns the bos and eos of each block by using the average of them in every block of the next layer, in the last, it filters the positions of each block according to language modeling likelihood. This paper experiments on many summarization datasets and improves the baseline model Bart by a large margin. The main improvement comes from chunking and selecting.

### Strengths
1. This paper shows that sparsification in cross-attention has a surprising potential for performance improvement, the proposed method improves about 20% over baselines.

### Weaknesses
1. The proposed method depends on cross-attention, and we could not introduce it to the encoder-only or decoder-only Transformer model.   If it can outperform existing LLMs, this would not be a weakness.

2. Experiments on other tasks are limited. This paper mainly experiments on summarization tasks, but does not experiment on CNN/DM or Xsum, which are the most compared data. For other tasks, this paper only does Narrative QA.  More experiments on document translation or classification would be an advantage.

### Questions
1. Do the baselines sparse self-attention?

2. There is a typo in Figure 3, the blue line should be selected length.

3. Table 4 should add a row of pure baseline, i.e., w/o neither. It is a surprise that we need both chunk and select, or we will lose the baseline.

4. I would like to see a comparison regarding latency.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an approach concentrated on the refinement of long-sequence modeling. The proposed method divides a sequence into a series of chunks. This technique meticulously aligns the inter-chunk information during the encoding phases, and subsequently, the most pivotal hidden states are discerningly selected from the encoder to facilitate the decoding process. Experiment results show that in long-text abstractive summarization and reading comprehension tasks, the proposed method outperforms strong baselines of long-sequence processing.

### Strengths
1. The authors propose a simple framework that can directly be used on existing PLMs for processing long sequences.
2. The authors propose a RL method to facilitate the transformer to concentrate more effectively on the crucial encoded hidden states.
3. Experiments show better results over strong baselines.

### Weaknesses
1. Missing related work. Long sequence Transformer is a hot topic, including two main directions: efficient computation or length extrapolation (train-short-test-long). In the realms of long-sequence Transformers, there appears to be a noticeable omission in the exploration of length extrapolation. Here are two related studies:
   1) A Length-Extrapolatable Transformer
   2) Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation
2. The proposed RL objectives lack solid motivation. It is well-known that RL objectives are hard to implement due to the variance of reward scores. There lacks necessary evidence to show how these RL objectives work and whether these RL objectives are necessary (compared to traditional MLE loss). Specifically, the paper does not provide a clear justification for why a reinforcement learning approach is needed over simpler methods for selecting important hidden states. The reward function design seems arbitrary, and there is no analysis of how sensitive the model is to different reward formulations. Furthermore, the paper does not discuss the potential instability issues that can arise from using RL in this context, nor does it provide ablation studies to demonstrate the necessity of each component in the RL objective.
3. The authors only conduct experiments on BART models.  It remains unclear whether the proposed method still works on more recent models, like LLAMA.

### Questions
1. How about the PPL scores on long text modeling? It is a widely-used metric to evaluate the performance of  long-text language modeling.
2. A minor stylistic observation pertains to the line spacing within the background section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduced a Simple learning framework with three typical operations: Chunk, Align, and Select to enable pre-trained encoder-decoder language models to process long-context. The chunking process is a variant of batchfying. The aligning process is the forwarding via BART or other LM encoders. The proposed selector network as well as the RL-based training is novel and interesting. The experiments are very solid, which covers almost all long-context datasets as far as I know.

### Strengths
1. The experiments are comprehensive and the results are robust and strong. The evaluation tasks and datasets coverage is excellent.  I appreciate that the authors conduct experiments on NarrativeQA to demonstrate the method's effectiveness and the NarrativeQA is recognized as the hardest benchmark for long-context transformer.

2. The method is intuitive and easy to understand. Even if the chunking and selection/retrieval is not that novel, the introduced PPO-based training for selector network is interesting and brings some insights.

### Weaknesses
1. The computational timecost brought by retrieval or selection based methods are always a significant issue. I did not find such discussions in main context and appendix about the latency part. The author should discuss and measure it to show the tradeoff between performance gain and latency increase.

2. As the selector FFN is randomly initialized but the backbone is pre-trained well, I think in the first 10k training iterations, the training might be unstable if following the alternative updates on a well-trained model and a newly-initialized model. The author provides limited details about this.

3. The ablation study on the chunk length might be interesting and important. A smaller chunk length brings better granularity and a larger chunk length accelerates the inference. Is the selected 512 length the best length for chunks?

### Questions
1. For footnote 1 of Page 3, how you deal with cases that a sentence is longer than a chunk as sometimes the sentence segmentation tool does not work well to split the sentence to desired length?

2. The selector is a small-size 8M FFN. Did you consider to scale up the parameters and also change the FFN to a RoBERTa model with binary classification head? This might be better for the action decision. 

3. If I understands the paper well, the selector is not pre-trained and is only randomly initialized FFN. Then you fine-tune the BART and selector together on specific task. Did you try to freeze BART and pre-trained the FFN selector on the same pre-training corpus of BART? Personally, I think if your selector FFN is only 8M parameters, the pre-training might not be helpful. But if the selector size is scaled up, this might be good to the model.

4. Some missing related works: TRIME (Zhong et. al., 2023) and LongMem (Wang et. al., 2023) are related to this method in terms of chunking and memorizing; Landmark Attention (Mohtashami and Jaggi, 2023) is related to this method in terms of S and E tokens.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper develops a way to use pre-trained transformers efficiently on long sequences without the need for further pre-training due to architectural changes.

The method first creates non-overlapping chunks to apply Transformer attention locally only (within chunks). After each layer, it does an elementary form of inter-chunk interaction by updating each bos and eos special tokens (indicating chunk boundaries within each chunk) with the average of newly produced eos and bos tokens (after the earlier local chunk processing layer) respectively. 

The method uses reinforcement learning for token selection for decoding with rewards created to penalize selecting too many tokens and other rewards based on language modeling probabilities. PPO is used in an actor-critic framework.

### Strengths
1. While the literature is saturated with efficient transformers for handling long sequences, this work can be applied to pre-trained models like BART directly without additional pre-training. 

2. The performance is quite decent compared to baselines.

### Weaknesses
The method could be counted as a form of dynamic pruning technology. There are already several works in that area. For example, transkimmer [1] already has dynamic token pruning. And there are other works in similar directions [2]. The usability of RL for token pruning is not a particularly surprising method, and chunking + local attention is a very standard policy for efficiency gain. More research can be done in contextualizing the work in the literature review by exploring other related works to [1,2] in the citation network. That said, The inter-chunk communication through average is interesting (although quite simple and could be seen as a hack)  and the overall synthesis seems to work well.

### Questions
1. Is the chunking method only applied to the encoder? Would there be any problem in applying it to the decoder and decoder-only models (standard LLMs) after appropriate changes (such as causality constraint in averaging for chunk alignment)? 

2. Is there a graph for per-iteration speed-up comparisons with baseline?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
