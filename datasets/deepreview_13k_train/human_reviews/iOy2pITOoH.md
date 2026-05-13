# Spark Transformer: How Many FLOPs is a Token Worth?

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
This work introduces Spark Transformer, an architectural variant of the Transformer model that drastically reduces the FLOPs count while maintaining comparable quality and an identical parameter count. This reduction is achieved by introducing sparse activations in both the feedforward network (FFN) and the Attention mechanism. In the FFN, this sparsity engages only a subset of parameters for each input. In the Attention mechanism, it limits the number of tokens that each token attends to.  We achieve this sparsity through statistical top-$k$, a lightweight approximate algorithm that is well-suited for accelerator hardware and minimizes training slowdown. Furthermore, Spark Transformer incorporates dedicated predictors to identify the activated entries. These predictors are formed by allocating a portion of the model's parameters and are trained jointly with the rest of the model. This approach distinguishes Spark Transformer from existing methods that introduce sparsity and predictors post-training, which often leads to increased training costs, additional model parameters, and complex modifications to the model architecture. Our Spark Transformer, pretrained using the Gemma 2 recipe, achieves competitive performance on standard benchmarks while exhibiting significant sparsity. Specifically, it utilizes only 8% nonzeros in the FFN activation and attends to a maximum of 256 tokens. This results in a 3.1$\times$ reduction in FLOPs, yielding a 1.70$\times$ speedup for prefill and a 1.79$\times$ speedup for decoding on a 16-core CPU VM.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
From the trials to replacing non-sparsified activations (e.g., SiLU) to sparsified activations (e.g., ReLU), sparsity-based LLM inference acceleration is widely studied due to its effectiveness in reducing the computational cost. It generally adopts non-ReLU activation and sparsity predictors for acceleration. This paper, Spark Transformer, aims for the same target (i.e., exploiting sparsity) but introduces a sparsity-exploiting drop-in replacement structure for the transformer while providing an end-to-end exploitation of sparsity in LLM. From this replacement, Spark Transformer can reduce the post-processing overhead (to train sparsity predictors additionally) compared to existing non-ReLU approaches. For this alternative solution, Spark Transformer proposes statistical Top-K and Spark Attention, which utilizes statistical Top-K. When trained from scratch using Spark Transformer (based on Gemma), it achieves around 1.7-1.8x speedup compared to the original Gemma (not compared to a previous sparsity-based LLM inference acceleration) through this sparsity-exploiting structure.

### Strengths
1. Important Domain: This paper tackles a timely domain, sparsity-based LLM inference.

2. New Approach: This paper proposes a new structure for sparsity-based LLM inference. While previous works mainly focus on better estimating sparsity through predictors, this paper introduces a drop-in replacement structure for transformers. Also, it exploits the attention sparsity for both FFN and attention.

3. Profound Descriptions: This paper provides profound descriptions of its methods with proofs.

### Weaknesses
1) Limited novelty: While statistical Top-K could seem to be a fresh approach in the sparsity-based LLM inference, the Top-K methods, especially statistical Top-K [1], were already extensively researched areas in the gradient/activation compression [1,2,3]. As previous statistical Top-K gradient compression [1] introduced a profound statistical Top-K selection (through threshold estimation) for various statistical distributions, the paper should show the main differences and emphasize the novelty. ([2] introduced Gaussian-based threshold estimation, and [1] significantly extended it with various distributions.) Also, [6] seems to propose a similar approach for the partial weights to predict the approximate scores of tokens.

2) Practicality: 1. Does this method provide inference time speedup compared to existing sparsity-based LLM inference? (e.g., DejaVu [4,5,6]). The main speedup is compared to the original Gemma only in the evaluation section. 2. Is single-stage training more practical than preprocessing existing sparsity-based LLMs? The introduction mentions this as one of the paper's strong points, so it should be tested quantitatively or with experiments. 3. As far as the reviewer understands, Spark Transformer requires a pretraining from scratch. Is this choice preferable to the predictor overhead of existing sparsity-based LLM inference acceleration?

3) Insufficient evaluations: This paper provides an in-depth analysis of the methods in the main body, but the evaluations are somewhat limited. Accuracy analysis is limited, and speedup comparison is conducted only with the original model (not sparsity-based LLM inference acceleration baselines). Also, there are many top-K methods to address the top-K selection overhead (e.g., quasi-sort with O(logN) complexity [7]), so statistical Top-K should be compared with those works excluding JAX top-K implementation.

### Questions
I enjoyed reading this paper, which tackles the timely topic of sparsity-based LLM inference acceleration. The main worrisome aspects of this paper are two-fold: novelty and practicality. The following are my questions related to them.

(Novelty)

Q1: What is the main difference between this paper and the existing statistical Top-K methods ([1,2])? I think [1,2,3] should be considered as related works in the paper. Additionally, please compare Spark Transformer with [6], which proposes a similar approach for the partial weights to predict the approximate scores of tokens.

(Practicality)

Q2: How much speedup (e.g., tokens per second) does Spark Transformer provide compared to the existing sparsity-based LLM inference acceleration (e.g., DejaVu [4], ProSparse, LLaMa ReGLU)?

Q3: What is the actual benefit (e.g., in terms of training time) of reducing preprocessing overhead through Spark Transformer?

Q4: Please compare Spark Gemma-2 with other accuracies. While the current evaluation compares Spark Gemma-2 with MMLU, GSM8K, AGIEval, BBH, Windogrande, and HellaSwag, as Spark Transformer may affect accuracy, wider comparison should be conducted. [5] provides a simple and easily accessible API for evaluating accuracies, so it would not be that difficult to compare.

Q5: Most of the previous works tried to avoid pretraining costs, but the reviewer wonder why this work chooses to train the model from scratch, which takes a huge overhead to prove the real effect of this work. 

[5] lm-evaluation-harness: https://github.com/EleutherAI/lm-evaluation-harness

(Other Points)

Q6. This paper only shows the experiments on the CPU, not any kind of GPUs or TPUs. Does Spark Transformer show similar speedup on GPUs or TPUs?

Q7. The reviewer guesses there is a typo on page 6, line 315. Eq.(13) should be changed to Eq.(14).

Here are some of the suggestions to make the paper more valuable. 
- Novelty: Emphasizing the main difference between Sparse Top-K’s statistic al Top-K and the previous Top-K approaches would make the paper more novel. Providing the difficulty of synergizing the Top-K to the transformer-based structure would be a good option.

- Practicality: Providing more extensive evaluations to show the speedup and stable accuracy of Spark Transformer in various settings would significantly enhance its practicality. Also, please show that the pretraining of Spark Transformer is more efficient than the existing sparsity-based LLM inference acceleration.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a statistical top k algorithm and a low rank predictor as a sparsity regularizer during pretraning, which maintains similar model quality benchmark as the dense counterpart (aka GEMM 2) and achieves improved (e..g, ~2X) inference speed up on CPU (or SIMD machines).

### Strengths
1. The proposed statistical top K method is intuitive and algorithm/hardware efficient
2. Both of the Sparisity regularizers (Statistical top K and low rank predictor) are applied during pretraining, thus saving post-training adapters and potentially contributes to close to SOTA model quality
3. analytical modeling is clear and shows it is an error-bound system
4. Due to the activation sparsity, it reduces the flops-heavy ops during inference on SIMD machines as table look-up instead of dense GEMMs thus demonstrates significat speed up on commercially more available CPUs

### Weaknesses
The table look up is efficient in SIMD machines but not friendly to accerlerators with Tensor cores or systolic arrays like GPU/TPUs. Though CPUs are much more commercially available than high end GPUs, it is unclear if the tokens/watt or tokens/second/watt of CPUs can beat GPUs during batched (instead of batch size 1) inference, even with sparsity

It is unclear to me how important it is have the two regularizers in pre-train or post-train (e..g, how does it contribute to final model quality), if it is still effective with just post-training/fine-tune, then it is more applicable to wider range of models

why is the score of HumanEval of GEMMA  2 much lower than published ones in table 2?

Is the model trained with Tensor Parallel? If not, how does the statistical top K performs when the activation is sharded? Would it incur extra CCL overhead or skewed top-K distribution (over devices) that further slows down the training?

### Questions
1. It is unclear to me how important it is have the two regularizers in pre-train or post-train (e..g, how does it contribute to final model quality), if it is still effective with just post-training/fine-tune, then it is more applicable to wider range of models

2. why is the score of HumanEval of GEMMA  2 much lower than published ones in table 2?

3. Is the model trained with Tensor Parallel? If not, how does the statistical top K performs when the activation is sharded? Would it incur extra CCL overhead or skewed top-K distribution (over devices) that further slows down the training?

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
Sparse transformer is an approach to select statistical top k entries from the input with two goals 

1. To reduce computation of entries not in top k 
2. To achieve the same in an efficient manner  (complexity - 2d vs O(dlogd))
3. To get speedup/Lower FLOP for efficient inference (on CPU only)

The above goals are quantified by showcasing the results where by using 8% non-zeros in the FFN activation and attending to a maximum of 256 tokens, the model achieves 3.1× reduction in FLOPS resulting in 1.70× speedup for preﬁll and a 1.79× speedup for decoding on a 16-core CPU VM. No speedup is shown on other devices like GPU, accelerators because inference needs special kernel which is available in Gemm-2 implementation.

### Strengths
- Solving an important problem of transformers (increasing speed by reducing the number of FLOPS)
- Mathematical explanation of statistical top k entry is solid and clear to readers. Both Spark FNN and Spark Attention approach makes sense and expected to reduce FLOPs (with certain impact on accuracy)
- Showing the FLOP reduction using a custom matrix multiplication (sparse vector matrix multiplication) which gives further boost to theoretical explanation of FLOP reduction.

Overall a good paper proposing a new method of exploiting fine-grain sparsity in transformer.

### Weaknesses
 - Although the method is convincing and shows speedup on CPU using special implementation of GEMM (sparse GEMM), the Author(s) need to show approaches which can convince readers that this method can potentially be useful for mainstream hardware like GPUs, custom accelerators. [Semi-structured sparsity]((https://arxiv.org/abs/2309.06626/) and [Deep Adaptive Inference Networks](https://arxiv.org/abs/2004.03915) methods also proposed similar approach for CNN but has similar limitation of speedup being shown only for CPUs.
- L324 : The comparison with state of the art methods like ProSparse can be done using same model so that we can see a fair comparison. The table suggests that for first four benchmark, ProSparse and LLaMMA ReGLU perform better (lower FLOP/token)
- Comparison with token pruning methods and impact on inference of end to end model with Sparse transformer will strengthen this paper.

My rating is based on the fact that this method may not be able to scale to other hardware and speedup on CPU alone is not significant. Even if it works for other Edge hardware, it might be a good contribution.

### Questions
- L065: $0.5*d_{model} * d_{ff} + 1.5 * d_{model} * k_{ff}$ , Authors are encourage to explain the origin of factors 0.5 and 1.5. 
- Authors are also requested to provide a comparison with other token pruning methods to compare speedup with state of the art methods ? it will be helpful to amplify the contribution of this paper. 
- What is the future plan to make this method work on other hardware like GPU/Accelerators ? Making this method work for other hardware will increase the usefulness of this approach.

### Soundness
3

### Presentation
3

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
This paper employs an approximate statistical top-k algorithm, using the Gaussian quantile function to estimate the top-k threshold by calculating the mean and standard deviation of the activation maps. The statistical top-k algorithm is applied in sparse attention and integrated into the Gemma-2 model. Experiments were conducted, and the results demonstrate a speed-up compared to the original model.

### Strengths
This paper uses an approximate statistical top-k algorithm, leveraging the Gaussian quantile function to estimate the top-k threshold by calculating the mean and standard deviation of the activation maps. This approach requires only the computation of the mean and standard deviation to efficiently complete the selection, eliminating the time-consuming top-k selection process. Therefore, it is reasonable at least from the perspective of improving computational speed.

### Weaknesses
1. Only a theoretical estimation of the error for the approximate statistical top-k algorithm was provided, without experimental validation.  
2. There was no analysis or testing of the gap between the approximate statistical top-k algorithm and the actual top-k selection.  
3. The study lacks comparisons with a sufficient number of state-of-the-art sparse attention works.  
4. Experiments were conducted only on CPUs, with no results provided for mainstream platforms such as GPUs.
5. There were no performance impact studies or experiments on applying the approximate algorithm.

### Questions
1. What is the actual distribution of the scores? How does it deviate from the Gaussian distribution?
2. What is the overlap between the selection results of the approximate statistical top-k and the actual top-k selection? How large is the error? What impact does it have on performance?

### Soundness
2

### Presentation
3

### Contribution
2
