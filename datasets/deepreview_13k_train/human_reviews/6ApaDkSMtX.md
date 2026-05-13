# Encoder-only Next Token Prediction

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
\rebuttal{Next-token prediction is conventionally done using decoder-only Transformers with causal attention, as this approach allows for efficient reuse of keys and values. What if we were not compute-limited, should we still use decoder-only Transformers? In this work, we introduce \textbf{E}ncoder-only \textbf{N}ext \textbf{T}oken \textbf{P}rediction (ENTP). We use small scale experiments to explore the differences between ENTP and decoders, highlighting potential advantages of ENTP in setting with unbounded compute. We introduce the $\operatorname{Count3}$ task and show, both theoretically and experimentally, that while ENTP can perform this task easily, a decoder-only Transformer cannot. Finally, we empirically demonstrate ENTP’s superior performance across various synthetic tasks, such as length generalization and in-context learning.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper analyzes the Encoder-only Next Token Prediction (ENTP), which challenges the prevailing use of decoder-only Transformers with causal attention in next-token prediction tasks. This paper tries to theoretically prove that encoder-only architectures can achieve comparable performance with decoder-only, and construct some tasks like triplet-counting to show that on some task, decoder-only will fails.

### Strengths
1. The paper is in general well-writing and easy to follow. The figures are good (like Figure 3 and 8) for understanding.
2. Construct an interesting task Triplet-Counting to compare decoder-only and encoder only architecture. 
3. Do both theoretical analysis and small-scale empirical study to do some analysis of ENTP

### Weaknesses
In general I still have some concerns as illustrated in weakness and questions. I will increase my score if these problem are solved

1. In 237-239, I think the claim is little weird because it's well-known decoder-only architecture also use KV cache to save memory, and the claim in 240-242 may not hold. 
2. Besides, I think the claim of Space complexity comparison in line 245-246 is not that reasonable if you also consider time complexity. In algorithm 3 you use a O(n^2) loop for calculating attention score for using O(n) than O(n^2) space. And this can not happen if you want to store the previous keys and values for accelerating as said in Time Complexity Comparison part
3. In section 5.1, my advice is that you may add some summarization about the intuition about why encoder can solve the Triplet-Counting function better but Decoder-only architecture can not. And a related question is illustrated in Questions-2
4. The scale of "large" encoder is still small (from Appendix C.4), and the main issue of encoder-only architecture will face efficiency issue when scaling the architectures. The lack of larger scale experiment may let people wonder if it's suitable for large scale experiments.
5. The improvement on validation loss/perplexity is not that significant, and a better way may be to evaluate on some downstream tasks.

### Questions
1. What's the result of decoder-only model with non-causal attention (you mentioned in 103-104) on the Triplet Counting task? Will they also fail?
2. I just feel confused about Remark1, Lemma1 and Lemma2. If Remark1 and Lemma2 holds, why we can not construct an decoder-only Transformer from the L=O(1) encoder-only Transformer and thus improve the result in Lemma1?
3. Have you do some experiments using Bert which is encoder-only architecture? If Bert can learn the Triplet Counting task? It's maybe an helpful experiment I think

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
This paper introduces Encoder-Only Next Token Prediction (ENTP), which challenges the traditional reliance on decoder-only transformers with causal attention for next-token prediction tasks. The authors argue that encoder-only models can perform next-token prediction without the need for causal masking and propose ENTP as an alternative to decoder-only transformers. ENTP has advantages in expressive power, allowing it to handle tasks like the Triplet-Counting task, which the paper theoretically and experimentally shows that decoder-only transformers struggle with. Through empirical results, the paper demonstrates that ENTP outperforms traditional decoder-only models in generalization tasks, including length generalization and in-context learning.

### Strengths
The main strength of the paper lies in questioning the conventional wisdom of the current literature that predominantly focuses on Transformer decoders for language modeling and generative tasks. The paper provides relevant theoretical and experimental justification to demonstrate that decoders are unsuitable for all ranges of tasks. The proposed method of ENTP shows superior length generalization and lower sample complexity, enabling it to perform well with fewer examples. The theoretical and experimental results provided in the paper will help the research community to gain a broader understanding of this subject.

### Weaknesses
The major weakness of the paper is overstretching of few claims without sufficient analytical justification. For instances -- 

1. "In principle, there is no inherent reason that language models should be limited by this restriction." 
2. "Triplet-Counting sequences have very small Kolmogorov complexity"
3. "Remark 1 conclude that encoders have strictly larger expressive power than decoders"
4. "Transformer encoder or decoder work with uncountable vocabulary"

See my questions below for more clarification.

More limitations --

5. The time and space complexity of the triplet counting algorithm in conjecture 1 raises its relevance. I am not sure if a task that requires atleast n^2 time complexity is at all practically relevant to explore or not.
6. The zero accuracy of Llama-7b and GPT-4o, even after fine-tuning, is alarming and needs a more convincing explanation. The authors should investigate if this failure is due to model architecture limitations, training procedures, or task-specific challenges.


### Questions
1. "In principle, there is no inherent reason that language models should be limited by this restriction."  - what evidence do you have to support this claim?
2. "Triplet-Counting sequences have very small Kolmogorov complexity" - can we elaborate how algorithm 1 concludes this fact? How do you quantiy "very small"? What is the typical range of Kolmogorv complexity?
3. "Remark 1 conclude that encoders have strictly larger expressive power than decoders" - how do you connect remark 1 with this conjecture?
4. "Transformer encoder or decoder work with uncountable vocabulary" - How does uncountable vocabulary work? 

More questions --

5. How does ENTP scale with longer sequences?
6. How adaptable is ENTP across diverse natural language processing tasks beyond token prediction, such as classification or sequence alignment?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tries to do a comparison between encoder only models (where there is kind of bidirectional attention) vs decoder only model. They try to pitch that under infinite compute, encoder only models perform as good or better than decoder only model. However, I don’t think that it makes sense to compare training approaches, assuming unlimited compute (I mean an MLP can represent anything by that logic). Most of the space and time complexity analysis in this work is trivial. The main section of the paper has a lot of unnecessary details.

### Strengths
- Some nice toy tasks were formulated to compare encoder and decoder models.

### Weaknesses
 - I dont understand the time complexity comparison argument in L241. Why does an encoder requiring \omega(n^2) operations cannot be efficiently expressed by decoder? Shouldn’t it be reverse, that encoder is worse here.
- I don’t agree with the basic premise which the paper is trying to prove i.e. the first line of conclusion (L522). The paper is trying to show that under infinite compute, encoder only model outperforms the decoder only model. I am not sure why authors feel the need to prove this, but it is intuitive and pretty obvious that encoder only model will outperform uni-direction decoder only models. Bi-direction attention decoder only models are not used in practice precisely because they are expensive to train due to more operations and expensive at inference as well.
- Authors tried to show encoder models outperform decoder models, on some toy tasks and even their real tasks are quite easy and trivial (addition, regression, etc.)
- Authors try to talk about experiments on openwebtext, with minimal details. Again, the compute is not fixed for this pretraining experiment (encoder model gets more compute or the data is simply repeated for decoder model to match the compute, which is NOT a realistic setting). I as a reviewer have to guess what the experiment would have been here, as no details were provided.

### Questions
I would be willing to increase my score for this paper if the authors can show that I misunderstood a major part of this work or the takeaways. Please see the weakness section for the questions.


----POST AUTHOR RESPONSE
I have updated the score post author response, as it clarified multiple key sections of the paper.

### Soundness
3

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper challenges the widely accepted view of next-word prediction using the transformer decoder and instead proposes next-word prediction via the encoder, supported by strong motivation and intuition. The paper also provides theoretical results comparing the expressivity of encoder-only and decoder-only architectures, and highlights the benefits empirically in several experiments.

### Strengths
-  The paper is well-organized and well-written, with clear motivation, theoretical results, and empirical validation.
- The motivation for using the encoder to predict the next word is compelling, especially in scenarios where computing resources and efficiency are not primary concerns. This opens up a challenge and an opportunity for the community to develop a more efficient encoder-only architecture for next-word prediction.
- The theoretical result on the difference in expressivity between encoder-only architecture and decode-only architecture is promising.
- The paper demonstrates the benefits of an encoder-only architecture across various experimental setups, yielding promising results.

### Weaknesses
 -  **The main weakness** is that encoder-only architecture requires O(n^3) time to generate the sequence during inference and needs to calculate the attention matrix n time during training. In contrast, decoder-only architecture only requires O(n^2) time during inference and can calculate the attention matrix once during training. This makes the proposed method **impractical** for real-world language modelling applications due to the high complexity, which is not addressed in the paper.

- As a result of the previous weakness, the experiment on laugnage modelling only consider small architectures, due to the complexity. Additionally, the improvements over decoder-only architectures, as seen in Table 3, are quite minimal given the potentially much longer training and inference times (which is not reported).

- Theoretical results of lemma 1 and lemma 2 rely on the conjecture 1, which might not hold. why "This conjecture seems plausible given that both Algorithm 1 and Algorithm 2"?

- The experimental set-up, e.g., learning rate, epoch, for the openwebtext experiment seems not provided.
- (minor) Causal function in line 175 is not defined.
- (minor) It would be clearer if the author could illustrate Figure 1 in two-layer cases with ellipsis instead of one-layer cases with ellipsis.

### Questions
- Why any causal function that can be expressed by an encoder requiring ω(n) time cannot be efficiently expressed by a decoder?
- lines 164-175 is a bit confusing, does $T_\epsilon = \epsilon$ hold? what is the meaning of ``we can view $T_\epsilon$ as an explicit and necessary way to introduce causality to the encoder $\epsilon$ since there is nothing
implicit to the encoder that forces causality. ''?
- Why consider/construct such triplet-counting tasks, at first glance it is a bit complicated.
- Why decoder architecture perform better than encoder architecture in table 2?
- What is RASP in line 363?

### Soundness
4

### Presentation
4

### Contribution
2
