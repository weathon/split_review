# Mamba: Linear-Time Sequence Modeling with Selective State Spaces

- Decision: Reject
- Scores: 3, 6, 8, 8

## Abstract
\noindent
  Foundation models, now powering most of the exciting applications in deep learning, are almost universally based on the Transformer architecture and its core attention module. 
  Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers' computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language.  
  We identify that a key weakness of such models is their inability to perform content-based reasoning, and make several improvements.
  First, simply letting the SSM parameters be functions of the input addresses their weakness with discrete modalities, allowing the model to \emph{selectively} propagate or forget information along the sequence length dimension depending on the current token.
  Second, even though this change prevents the use of efficient convolutions, we design a hardware-aware parallel algorithm in recurrent mode.
  We integrate these selective SSMs into a simplified end-to-end neural network architecture without attention or even MLP blocks (\textbf{Mamba}).
  Mamba enjoys fast inference (5$\times$ higher throughput than Transformers) and linear scaling in sequence length, and its performance improves on real data up to million-length sequences.
  As a general sequence model backbone, Mamba achieves state-of-the-art performance across several modalities such as language, audio, and genomics. %
  On language modeling, our Mamba-3B model outperforms Transformers of the same size and matches Transformers twice its size, both in pretraining and downstream evaluation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes Mamba, which is a linear-time sequence model with selective state spaces. The authors propose to modify conventional state space models (SSMs) such that the modified models are input-dependent. The authors further propose engineering techniques for performance optimization. Experiments are conducted to demonstrate the effectiveness of the proposed method. In particular, several flavors of pre-trained models are provided.

### Strengths
* The proposed Mamba method includes a simple modification to the conventional SSM model: add additional models to make SSM models dependent on the inputs. SSMs are known for their computational difficulties, and the authors address this issue by several performance optimization techniques.

* The authors pre-train several variants of Mamba, ranging from 130M parameters to 1.4B parameters. These pre-trained models show performance improvements compared with the baselines in the paper.

### Weaknesses
Concerns about model design:

* The motivation of Mamba is to address the drawbacks of recurrent models while improving the efficiency of attention-based models. There are many works following the same direction: S4-diagonal [1], SGConv [2], MEGA [3], SPADE [4], and many efficient Transformer models (e.g., [5]). All of these models achieve near linear complexity, and the authors need to compare Mamba with these works in terms of both model performance and efficiency. Specifically, a direct comparison on a standard language modeling task like Wikitext-103 is crucial to establish the performance relative to these existing methods, rather than just focusing on pre-training metrics. The paper needs to demonstrate that Mamba offers a clear advantage over these alternatives in terms of both performance and computational efficiency.

* Many attention-based Transformer models show length generalization ability, i.e., models can be trained on a shorter sequence length and tested on a longer sequence length. Some examples include relative positional encoding (T5) and Alibi [6]. Because SSMs are in general sequential, does Mamba have this length generalization ability? This is a critical point that needs to be addressed with thorough experimentation, as the ability to generalize to longer sequences is a key advantage of many Transformer architectures.


Concerns about experiments:

* The authors need to compare with stronger baselines. The authors acknowledge that H3 was used as a motivation for the model architecture. However, they did not compare with H3 in the experiments. From Table 4 in [7], ppl of H3 is 8.8 (125M), 7.1 (355M), and 6.0 (1.3B) on the Pile dataset, which are considerably better than Mamba. The authors need to show comparisons with H3, especially since H3 is a direct predecessor in the SSM line of work. Furthermore, the comparison should be done with the same tokenizer to ensure a fair comparison.

* For the pre-trained models, the authors only show results on zero-shot inference. This setting is quite limited and the results cannot support the effectiveness of Mamba well. I suggest the authors run more long-sequence experiments such as document summarization, where the input sequence is naturally long (e.g., the average sequence length of the arXiv dataset is greater than 8k). Evaluating Mamba on tasks that require processing long sequences is crucial to validate its claimed benefits. The lack of fine-tuning experiments also limits the conclusions that can be drawn from the pre-training results.

* One of the main contributions that the authors claim is long sequence modeling. The authors should compare with more baselines on LRA (Long Range Arena), which is essentially the standard benchmark for long sequence understanding. This would provide a more direct and standardized way to assess the long-range modeling capabilities of Mamba against other models.

* Memory benchmarking is missing. Even though Section 4.5 is titled “speed and memory benchmark”, only speed comparisons are presented. Also, the authors should provide more detailed setups of Figure 8 left, e.g., model layers, model sizes, details of the convolution, etc. Could the authors provide some intuitions why FlashAttention is the slowest when the sequence length is very large (Figure 8 left)? A thorough memory analysis is crucial for a complete understanding of the model's efficiency, and the experimental setup for the speed comparison needs to be much more transparent.

### Questions
See above

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new class of selective state space models (SSMs) for sequence modeling that achieves Transformer-quality performance while scaling linearly in sequence length. The paper addresses the key problem in SSMs for selecting data by selecting particular inputs. The paper presents a hardware-aware algorithm that computes the model recurrently with a scan instead of convolution, avoiding materializing the expanded state to reduce memory usage. This results in faster computation than previous methods.

The paper simplifies prior deep sequence model architectures into a homogeneous architecture which is called as Mamba, incorporating the selective SSMs. Mamba enjoys fast inference, linear scaling, and improved performance on long sequences.

In the results the authors show that  Mamba achieves state of the art on synthetic tasks, audio/genomics modeling, and language modeling and outperforms Transformers of the same size on language modeling in both pretraining and downstream tasks.

The results suggest selective SSMs and the Mamba architecture could be a strong candidate for a general sequence model backbone for foundation models across modalities. The paper demonstrates the potential for linear-time models to match or exceed the performance of quadratic Transformers.

### Strengths
+ A key limitation of prior SSMs is the inability to efficiently select data in an input-dependent manner. The paper introduces a key mechanism by parameterizing the SSM parameters based on the input, allowing the model to filter out irrelevant information and remember relevant information indefinitely.
+ The results as compared to Pythia, and Transforms on many benchmarks are impressive.

### Weaknesses
 - The model still has a quadratic memory requirement during training like Transformers.

### Questions
1) Have you evaluated scaling behavior beyond 1.4B parameters? How does it compare to Transformers at 10B scales?

2) The input selection mechanism introduces additional hyper parameters. How sensitive are the results to hyperparameters like the projection rank?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper upgrades S4 by making the token mixing matrix data-dependent and introduces the Mamba structure. On the other hand, although the use of FFT is not possible, the authors provide a linear algorithm for computation, resulting in linear computational complexity. The effectiveness of the proposed method is validated on multiple datasets.

### Strengths
The paper is written in a clear and understandable manner, with a well-defined approach and simple yet effective improvement strategies.

### Weaknesses
The paper lacks references to some relevant works, such as [1], [2], [3], [4] which discusses some Linear Attention methods, and [5], which is also a LongConv method. However, these references are completely absent in the paper. I suggest that the authors consider adding these citations to provide a more comprehensive review of related work.

### Questions
1. Adding extrapolation experiments to the language model would be interesting.
2. The ablation analysis in Table 6 should be more comprehensive, with a total of $2^3$ possible combinations. I suggest that the authors include the remaining two combinations.
3. What's your setting of Scaling Law? Why is your ratio of token number and model size is the same as Chicilla's paper? I suppose the FLOPs of Transformers and SSMs would differ. Suppose the FLOPs of Transformers and SSMs would differ given the same amounts of total parameters, is this important to the final performance(accuracy)?
4. How did you parameterize the first convolutional layer in the Mamba-Block.
5. Providing more detailed implementation, such as offering core code, is very helpful.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors study the recent state-space models (SSM) family of efficient sequence architectures and address some of their challenges, related to the inability to perform content-based reasoning. The core contribution of the work is the addition of a selection method to the SSM architecture, which results in simple and scalable architecture, Mamba. Then they demonstrate the superiority of Mamba on standard language benchmarks, as well as DNA and audio modeling. The authors also contribute efficient implementation and benchmarking of Mamba on modern hardware.

### Strengths
S1: The paper addresses very efficiently and effectively pressing problems in sequential modeling. 

S2: The authors have identified simple toy tasks, such as selective copying and associative recall, that enable them to make design choices which state-of-the-art impact on real-world data.

S3: The connection to the role of gating mechanisms in RNNs is well-appreciated.

S4: The empirical part of the paper is very thorough, and the results are strong.

### Weaknesses
I do not identify any major weaknesses of the paper.

### Questions
I am curious if we could build a better understanding of the selection mechanism that you propose. In Theorem 1 you link that mechanism to gating in RNNs as a special case. Is it possible to understand better the generalization through some discussion / qualitative examples?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
