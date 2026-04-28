# Faster Language Models with Better Multi-Token Prediction Using Tensor Decomposition

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
We propose a new model for multi-token prediction in transformers, aiming to enhance sampling efficiency without compromising accuracy. Motivated by recent work that predicts the probabilities of subsequent tokens using multiple heads, we connect this approach to rank-$1$ canonical tensor decomposition. By generalizing it to a rank-$r$ canonical probability decomposition, we develop an improved model that predicts multiple tokens simultaneously. This model can also be interpreted as a mixture of experts, allowing us to leverage successful techniques from that domain for efficient and robust training. Importantly, the overall overhead for training and sampling remains low. Our method demonstrates significant improvements in inference speed for both text and code generation tasks, proving particularly beneficial within the self-speculative decoding paradigm. It maintains its effectiveness across various model sizes and training epochs, highlighting its robustness and scalability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper borrows key idea from Gloecke et al. [1] to train multi-token predictors instead of single next word predictor. This work identifies a key flaw in [1] which is that the distributions for multiple $n$ future tokens are independent of each other thus ignoring the token  interdependency. This work interprets this as a rank-1 approximation to the full distribution tensor of $n$ next tokens and proposes to improve this to a higher rank estimate. This higher rank estimate is achieved by $r$ multiple heads defining $r$ different distributions and using their mixture for the $n$-future token prediction. Training and inference method for this is discussed followed by an observation that the multi-token predictor can be used in self-speculative sampling approach where the next word prediction is made faster by using proposal distribution that predicts multiple next tokens. The experiments are mainly performed on nano-GPT model architecture trained on TinyStories dataset and also finetuning the PyCodeGPT model.

### Strengths
-- The paper studies an interesting problem to speed updecoding by predicting multiple tokens in parallel at higher acceptance rates than typical speculative sampling approaches.

-- The proposed solution seems straightforward to implement.

-- The contribution to identifying issues with existing multi-token training approaches and proposing a higher rank alternative is novel.

### Weaknesses
 -- The evaluation leaves a lot to be desired. Experiments are done on small datasets and small models but more concerningly, little else is provided aside from loss curves of training runs and token acceptance rates for the scheduled sampling approach. As an example, performance of these models on various benchmarks to estimate the quality of these trained models would aid in better assessment of the approach. Specifically, perplexity scores on held-out datasets, or downstream task performance metrics would be more informative than just training loss. Also, it is unclear if this approach empirically scaled to larger datasets and models effectively in terms of speed and performance. The lack of information about the computational resources used for training and inference further limits the reproducibility and practical applicability of the work.

-- Comparison to other speculative sampling approaches with various draft models will give a better idea about the improvement on speed and resources with the proposed approach. The paper should include a comparison with other state-of-the-art speculative decoding methods, including those using different draft model architectures or training strategies. This comparison should not only focus on token acceptance rates but also on end-to-end generation speed, memory usage, and computational cost. Without such a comparison, it's difficult to assess the true value of the proposed method.

-- There is room for improvement in presentation. Figure 1 doesn't help with understanding the paper better and is confusing. The figure lacks clear labels and explanations of the axes and the different components. Algorithm 1 can also be described more clearly. Currently, it hinges on the reader's prior understanding of speculative decoding. The algorithm should be presented in a more self-contained manner, with clear definitions of all variables and operations. The paper would benefit from a more detailed explanation of the training process, including the specific optimization algorithms and hyperparameters used.

### Questions
Please address the issues above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
After reading the author response, I thank the authors for providing clarifications to Table 1 and Table 3 and answering some of my other questions. However, I still think it is important to compare to other baselines (e.g. EAGLE, Medusa as another reviewer points out) in addition to Gloeckle et al. 2024. Therefore I am keeping my score the same. 

----

The paper studies multi token prediction in transformer language models. Vanilla autoregressive degressing is expensive for long outputs since it only decodes one output at a time.

The authors are inspired by the work of Gloeckle et al. 2024. In Gloeckle et al. 2024, given a context x_{t:1} the next n tokens are predicted independently (with multiple heads). As the authors point out, this amounts to a rank-1 tensor approximation of the joint probability distribution.

In this work, the authors explore higher ranks (r > 1) using CP decomposition. They draw a connection to mixture-of-experts and propose a auxiliary load balancing strategy so all the weight is not on one expert (component). 

They then perform experiments validating their work.

### Strengths
-Tackles an interesting and important problem

-The method is written clearly. 

-I also find the connections to tensor decomposition interesting.

### Weaknesses
Some confusion on experimental results: I'm a bit confused as to how much of a speed up the author's approach gives over both the approach of Goeckle et al. 2024 (i.e. rank=1) and also vanilla non-autoregressive decoding for the same level of quality. 

For example in Table 1: I see that in Table 1 the  final column (time per token) is not much different across all the rows?

Moreover I don't quite understand Table 3.

Comparisons: I think the authors need additional baselines in addition to just ablations of their own approach from the related work. For example, as another reviewer suggested EAGLE and Medusa:
https://github.com/SafeAILab/EAGLE
https://arxiv.org/abs/2401.10774

Related work: The authors should also cite and discuss related work in non-autoregressive decoding (typically for neural machine translation) that has been developed for a while e.g. see below and citations therein. In particular it would be useful to discuss how the authors' approach compares and contrasts with these works.

https://arxiv.org/abs/1711.02281
https://arxiv.org/abs/2204.09269
https://arxiv.org/abs/2012.15833

### Questions
-How does the method combine with beam search?

-Does the speedup increase or decrease as a function of model size?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
One existing form of speculative decoding involves predicting k tokens at a time independently, which can be thought of as a rank-1 decomposition of the k-order joint probability tensor over those tokens. This paper instead proposes to predict the factors for a rank-r decomposition. They evaluate two instantiations of this idea: training a LM from scratch to predict this decomposition, and taking an existing LM and fine-tuning additional heads to predict this decomposition. Their experiments show that higher rank decompositions lead to higher acceptance rates in speculative decoding.

### Strengths
(1) The method is well-motivated and explained clearly. The connection to MoE, which motivates a load-balancing auxiliary loss, is also interesting.

(2) The paper seeks to improve inference speed in large models, which is an important problem.

### Weaknesses
While the method seems interesting and promising, the paper's experiments seem disorganized and insufficient to fully demonstrate the effectiveness of the method.

(1) The majority of the results are for a 56.3M parameter trained on TinyStories, which is a very limited evaluation setting, both because the dataset is synthetic and because the setting involves retraining. There are also some experiments on head-only tuning for PyCodeGPT in Table 3, but the results in that setting are not very strong --- increasing the rank does not actually seem to actually improve inference speed for many of the models. The paper would benefit from more thorough evaluation and stronger results (especially on non-synthetic datasets, and on speeding up existing models rather than requiring retraining: for example, the evaluations done in https://arxiv.org/pdf/2211.17192 (Table 3) would improve this paper).

(2) The majority of the experiments section seems to involve analysis rather than results: only tables 1 and 3 report inference times, which are the main results. I would suggest moving other plots (token acceptance rate, first token vs joint loss, etc.) to a separate analysis section.

(3) There are a substantial number of issues with the experiment design that would be beneficial to address: (a) In Figure 3, it seems like hyperparameters are being selected using the test set; I would suggest using a dev set instead. (b) To make comparisons fair, I would suggest training each rank for the same amount of wall-clock time, rather than number of steps, in case higher ranks require more time per forward pass. (c) The self-speculative setup makes the results hard to interpret because each rank uses a different target model. I would suggest that each method be speculative with respect to the same target model. (d) The paper would be clearer if the experiments were described concretely: for example, the paper states that "Our measurements were made with seq length varying from 1024
to 4096" (lines 408-409), but it's not clear which experiments use which sequence lengths.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on speculative decoding methods that incorporate additional prediction heads. The authors conceptualize current standard approaches as rank-1 canonical tensor decomposition and propose a generalized method that extends from rank-1 to rank-r canonical tensor decomposition to approximate the joint distribution of future tokens. To enhance model training, an auxiliary loss is introduced to address weight imbalances. Experimental results highlight several key findings:

1.	Increasing the ranks results in a decrease in joint loss.

2.	The first token appears to have no correlation with different ranks.

3.	The method is effective even when only the prediction heads are trained.

The proposed approach achieves notable speedups compared to autoregressive models and rank-1 baselines.

### Strengths
1.	This work identifies the limitations of recent multi-token prediction standards and proposes a more generalized approach.

2.	The experimental results demonstrate the method's effectiveness, and the ablation study underscores the importance of the introduced components.

### Weaknesses
1.	The work lacks comparison with existing state-of-the-art methods such as Medusa, Eagle, etc., which belong to the same research domain.

2.	In the code generation setting, the performance of averaging two accepted draft tokens is not promising.

3.	There are several typos in this version that need revision.

### Questions
1.	In line 113, the authors denote the input sequence as x_{t:1} and the corresponding embeddings as e_{t:1}. According to the description, the embeddings are the representations of the final transformer layer, while in Figure 1, the same value is denoted as z_t. Do z_t and e_t means the same representation, or e_t means the “input” embeddings? This notation is somewhat confusing.

2.	Are there any results on the acceptance rate for Llama 8B, not just inference time?

__Typos__:

1.	In line 116, a comma is missing before "the conditional probabilities ...".
2.	In line 150, "Note, that" should be revised to "Note that".

### Soundness
2

### Presentation
3

### Contribution
3
