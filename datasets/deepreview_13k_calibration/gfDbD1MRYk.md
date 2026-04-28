# Semi-autoregressive Decoding for Efficient LLM Inference

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
Inference in large language models (LLMs) is often slow due to their autoregressive nature. 
In this work, we formulate a semi-autoregressive decoding paradigm for LLMs that delegates part of the expensive computation from the original large model to a smaller, more efficient autoregressive model. The core of our design lies in the separate modeling of token dependencies, where the large model handles long-term dependencies on distant tokens, while the smaller model addresses short-term dependencies on recent tokens. When employed as a draft model in speculative decoding, our method allows for substantial reuse of computation in the LLM without missing any token dependencies, thereby striking a good balance between draft quality and drafting speed. Experiments on text summarization, medical QA, code generation, and mathematical reasoning tasks demonstrates the efficacy of our method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper formulates a semi-autoregressive decoding paradigm for LLMs that delegates part of the expensive computation from the original large model to a smaller, more efficient autoregressive model, which allows for substantial reuse of computation in the LLM without missing any token dependencies, thereby striking a good balance between draft quality and drafting speed. Experiments on text summarization, medical QA, code generation, and mathematical reasoning tasks demonstrates the efficacy of our method.

### Strengths
- The research direction of this paper, i.e., efficient LLM inference, is meaningful for the development of large language models. 
- This paper is well writen and easy for understanding. 
- This paper compare several draft methods and combine the advantages of the two previous models, leading to better performance.

### Weaknesses
 - The main contribution of this article is not clear, which is more likely to be a technical report, thus, I worry about the noverty of this paper.
- Lacking the comparison between current sota speculative decoding methods in main tables.

### Questions
see weaknesses.

### Soundness
2

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
The paper presents a semi-autoregressive decoding approach aimed at enhancing the inference efficiency of large language models (LLMs). It offloads some computational burden from the original LLM to a smaller, more efficient autoregressive model. This approach separately handles long-term dependencies using the large model and short-term dependencies with the smaller model, striking a balance between draft quality and drafting speed. Experiments across text summarization, medical QA, code generation, and mathematical reasoning tasks demonstrate the efficacy of the proposed method in terms of acceleration, memory cost, and training convenience. The study contributes to the field by offering a practical solution for efficient LLM inference, which is crucial for real-world deployment of these models.

### Strengths
1. The paper introduces a semi-autoregressive decoding paradigm that attempts to optimize the balance between draft quality and inference speed in LLMs.
2. The proposed method demonstrates potential in accelerating inference across various text generation tasks.

### Weaknesses
1. The approach of integrating a small autoregressive model is not novel and has been previously explored in Cheng et al. (https://arxiv.org/abs/2403.09919) The paper does not sufficiently differentiate its method from existing works and misses comparison in experiments, which is a significant oversight. 

2. The study's scope is confined to models no larger than 13 billion parameters. There is an absence of discussion and experimentation regarding how the proposed method scales and performs as model size increases. This is a critical gap, as the acceleration benefits and computational efficiency are likely to vary with larger models.

3. While the paper initiates a meaningful discussion on the types of tasks that could benefit from the proposed method, it does not delve deeply enough into this analysis. A more comprehensive investigation into which task types experience significant acceleration and the underlying reasons would have strengthened the study's conclusions and practical implications.

### Questions
1. The study is limited to models no larger than 13 billion parameters. Could you discuss how you anticipate your method would perform as model size increases, especially given the trend towards larger LLMs? Are there any scalability concerns or potential modifications to the approach that you foresee as necessary for larger models?

2. The paper includes a discussion on the types (Sec. 6.2. structured vs. unstructured data) of tasks that benefit from your proposed method but does not delve deeply into this analysis. Could you provide a more in-depth exploration of which task types are most likely to see significant acceleration with your method, and what factors contribute to these differences? This could include a discussion on the nature of the tasks, the complexity of the inputs,  the models' original ability on the tasks, and how these factors interact with the decoding process.

3. Table 2 shows that the skip method achieves a lower token acceptance rate compared to the proposed model, which contradicts intuition. Typically, one would expect the performance of the skip method to be closer to that of the original model. The manuscript does not provide a clear explanation or empirical evidence to support this claim, which undermines the credibility of the findings.

### Soundness
2

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
3

### Summary
This paper proposes a semi-autoregressive decoding method aimed at accelerating LLM inference. Compared with two existing approach: 1) block autoregressive model and 2) pruned autoregressive model, this work introduces a new framework that combines the advantages of both: the improved latency of the block autoregressive model and the high acceptance rate of pruned autoregressive models. Specifically, in the proposed framework, preceding tokens are encoded using the large target model, while draft tokens are encoded with a smaller model, such as a one-layer transformer or RNN. To train the smaller model, the authors experiment with two training strategies: separate training and joint training with Q-LoRA. The experiments demonstrate that the proposed semi-autoregressive decoding approach achieves promising results in both acceptance rate and inference latency.

### Strengths
1.	This work unifies and analyzes existing speculative decoding methods, proposing a semi-autoregressive framework that effectively balances acceptance rate and low latency.
2.	The paper is well-organized and clearly written.

### Weaknesses
1.	The novelty of this paper is limited.

2.	This paper lacks direct comparisons with previous works under the same settings. For example, in the GSM8K code generation dataset, Eagle achieves a 3.x speedup, while this paper achieves only 2.6. More discussion on this is needed.

### Questions
1. Have you compared your methods with Medusa or Eagle under the same settings? It appears that all the results listed are from your experiments.

2. The use of distance token representations in the tiny model is unclear. In the Appendix, the MLP in the MLP head takes the concatenation of h_p and h_q as input. However, h_q maybe the size of SH, where S in the distance token number. Did you use the last token representation or some other methods? Did I miss some details?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a method for efficient inference in LLMs, based around speculative decoding where a cheap drafter model/algorithm is used to generate a sequence of outputs that are then validated in a larger model. This paper specifically contributes a cheap mechanism (based on semi-autoregressive generation) for generating fast but high quality draft sequences, and show that this can improve overall runtime versus several baseline methods.

### Strengths
This paper is very well written, and easy to follow. I had no trouble understanding the motivation, algorithm, or experimental evaluation, and the design decisions underlying the technique were convincingly argued. The exploration of simple architectures for the drafter is interesting, and includes some very light models with few parameters.

### Weaknesses
I have three issues: novelty, need for joint training, and quality of experimental setup.

1. On novelty, a key paper is not cited: 
Tandem Transformers for Inference Efficient LLMs; Aishwarya P S, et al 2024 https://arxiv.org/abs/2402.08644
This work performs block-generation from the drafter model with lagged cross-attention into the larger model, and includes experimentation with SPEED. The way in which the models are combined may be different, but the idea appears to be the same. At the very least your approaches should be compared analytically, or - better - empirically.

2. It is not clear why there is a need to finetune the original LLM. The fact this is shown to help in the experiments suggests to me that the data signal in the loss function (8) is quite different from the original LLM's output. That is, there's a problem of domain shift such that when the drafted is tuned with lambda=1 there ends up being a disconnect between that and the original LLM. An easier way to fixing this than tuning the LLM is to reframe the loss as a distillation objective, such that you train the drafter against the outputs of a frozen teacher. This is much cleaner than fine-tuning the original LLM to several different domains.

3. Experiments use a block size of 3-4 draft tokens. Compared to prior work on speed, e.g., the Tandem paper above,  Elhoushi et al, 2024, Medusa (last two of these cited in the submission), experiment with much bigger blocks, e.g., 20+ tokens. Maybe there are benefits to be had from using a small block (and a simpler model), however this disconnect is jarring, leading me to distrust the results in the paper. Line 406 says looking further ahead doesn't help, but perhaps this is because the drafter has been oversimplified.

Another jarring issue is the choice of datasets and models, namely that there is no overlap I can see with the prior work. I suggest adding datasets to facilitate easier comparison. Why did the model change between most evaluation tasks (Table 1)? Sticking to one model for the primary results would remove one confound, then report an ablation of the method across models separately.

### Questions
282: It's not clear how the original model vectors and drafter model vectors are used together. From the graphic is seems they are concatenated and then treated the same (weighted with a LORA matrix). I'd also appreciate more motivation for the asymmetry in LORA size.

Figure 4: it wasn't clear what the x-scale was on the zoomed box in 4a.

### Soundness
2

### Presentation
4

### Contribution
2
