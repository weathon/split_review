# Adaptive Rank Allocation: Speeding Up Modern Transformers with RaNA Adapters

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Large Language Models (LLMs) are computationally intensive, particularly during inference. Neuron-adaptive techniques, which selectively activate neurons in Multi-Layer Perceptron (MLP) layers, offer some speedups but suffer from limitations in modern Transformers. These include reliance on sparse activations, incompatibility with attention layers, and the use of costly neuron masking techniques. To address these issues, we propose the Adaptive Rank Allocation framework and introduce the Rank and Neuron Allocator (RaNA) adapter. RaNA adapters leverage rank adapters, which operate on linear layers by applying both low-rank matrix decompositions and adaptive masking to efficiently allocate compute without depending on activation sparsity. This enables RaNA to be generally applied to MLPs and linear components of attention modules, while eliminating the need for expensive maskers found in neuron-adaptive methods. Notably, when compared to neuron adapters, RaNA improves perplexity by up to 7 points and increases accuracy by up to 8 percentage-points when reducing FLOPs by $\sim$44\% in state-of-the-art Transformer architectures. These results position RaNA as a robust solution for improving inference efficiency in  modern Transformer architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Authors propose RaNA (Rank and Neuron Allocator), aiming to timprove the efficiency of LLMs by compressing linear layers. Authors propose the adaptive rank allocation, and decompose all linear layer into a product of low-rank matrices and an adaptive router.

### Strengths
1. The paper is clearly written.
2. The method is applicable to all linear layers. 
3. Error achieved by RaNA is far smaller than previous methods and SVD.

### Weaknesses
1. no wall-clock latency measurement. Measuring only FLOPs is not acceptable for a compression method on transformers.
2. The paper lacks baselines from the pruning literature (WANDA, SliceGPT). These are baselines that must be compared for this method since RaNA achieved compression by low rank and sparsity.
3. The proposed method takes individual layers into account while deciding sparsity. Some literature in LoRA (AdaLoRA) shows that different layers may need different ranks in the adaptation context. What is the gap between considering only one layer’s error and considering multiple layers’ errors while determining the rank to mask out?

### Questions
See weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel model compression framework that leverages adaptive rank allocation via rank and neuron allocation (RaNA) adapters. Specifically, weights in linear layers are decomposed into two low-rank matrices A and B, with a learnable router in between that selects which ranks to activate. RaNA also supports adaptive FLOP allocation across adapters. The paper evaluates RaNA on LLMs such as Llama2-7B and Gemma-2b, and compares its performance to other recent neuron adaptation methods such as CATS. The evaluation compares local (layer-wise) reconstruction errors for RaNa vs. baselines, FLOPs, and accuracy on downstream tasks.

### Strengths
* The paper is reasonably well-written and easy to follow.
* Model compression is a promising way of reducing LLM size and making it fit various deployment constraints such as target latency, parameter and memory-footprint. As such, this paper targets a relevant and important problem.

### Weaknesses
 * I’m not a big fan of using FLOPs as an optimization metric - it is well-known at this point that FLOP reductions may or may not correspond to reductions in inference latency or wall-clock time. This is likely also the reason why the main baseline method used in the paper (CATS) introduces a custom GPU kernel to realize runtime speedups. Have the authors done any study on how the proposed method improves the inference latency or throughput of the decomposed network? A theoretical discussion may also suffice given the limited time.
* I believe that RaNA needs to be compared to other related work on structured pruning to better understand its performance and specific scenarios where it does well. Examples might include Sheared Llama [1], ShortGPT [2] , SliceGPT [3], or Minitron [4].
* The size (< about 7B parameters) and age (Llama2 was released nearly 2 years ago at this point) of the models being used for evaluation is a weakness of the paper. While I understand that scaling up to larger models is not always feasible given limited resources, adding results on newer models (eg: Llama3.1 8b) would help compare with other recent pruning/compression efforts.

### Questions
* Please address the wall clock speedup comment in the weaknesses section.
* On the topic of inference speedups, RaNA replaces a single GEMM in linear layers with two GEMMs (please correct me if I’m wrong) - I’d really like to understand how this might affect real-world inference latency. 
* How well does RaNA perform on networks with sparse activation functions?

### Soundness
2

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
3

### Summary
The work proposes a new method for input-dependent compute allocation in transformer layers that is not dependent on activation sparsity and can be applied to any linear layer. The idea is to decompose $Wx$ as $A(r(x) \odot Bx)$ and find $A$, $B$ and $r$ such that the approximation error of $Wx$ is minimal. The derived 'RaNA'-adapters are  tested on MLP and QKV layers in a variety of Transformer models, demonstrating reduced approximation errors as well as improved performance on downstream tasks when compared to conventional neuron adapter baselines such as CATS (Lee+2024).

### Strengths
The key idea of this work to apply adaptive compute at the rank level of linear layers makes for a straightforward and generally applicable sparsification strategy that unlike other prior methods does not require specific architectural features or activation functions.

The formulation as an error minimization problem over the layer input distribution allows for a principled derivation of suitable decomposition and routing functions.  

The experimental results show improvements over existing neuron-adaptive methods.

### Weaknesses
While the experiments show that RaNA outperforms CATS in perplexity and accuracy, the setup offers little insight into where this improvement comes from. Table 1 compares RaNA with sparse MLP/QKV against CATS with sparse MLP only. Given that they are compared at an equal compression rate, I assume that the MLPs in the CATS model are more aggressively sparsified than the MLPs in RaNA. This makes it hard to conclude what causes the performance difference. Table 2 directly compares MLP-only sparsification but is for a different, smaller model Gemma-2b. It would be helpful to add RaNA with MLP-only sparsification for Llama2-7b to differentiate the influence of MLP vs. QKV sparsification. Furthermore, it would be useful to add an additional baseline like LLRA that like RaNA can sparsify MLP+QKV. To aid the comparison, could you also clarify the sparsification levels for each component (MLP, QKV) in both RaNA and baseline methods?

L509 offers different hypotheses for the causes of RaNA's performance (compression capacity, FLOP distribution, QKV applicability) but an ablation study to investigate the factors is missing. Adding results that can shed light on RaNA's performance could greatly strengthen the analysis, for instance, by comparing RaNA with and without QKV sparsification, or with different FLOP distribution strategies.

I suggest moving the proof for Proposition 1 into the main text and describing it as a concrete example to help the reader understand how the neuron-adaptive method is a special case of rank adaption. Specifically, I found it helpful to see that $B_{down}, A_{up}, r_{up} := I$ and $A_{down}, B_{up}$ adjustment are all it takes to get to the neuron-adapted version of the MLP.

### Questions
When describing the downstream and perplexity results in L480, you state that QKV is only RaNA-fied for Llama and Pythia, but not Gemma. Could you please explain why RaNA was not applied to QKV in Gemma?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a dynamic rank allocation method for improving the computational complexity of a transformer model.

The paper describes a related body of work on neural adaptors, and recognizes that those that rely on sparse activation functions (ReLU) are hardly suitable for transformers, the majority of which now use non-sparse activations functions (e.g. SwiGLU). Neural adaptors that do not rely on sparse activations are better suited to transformers but suffer from inefficiencies, primarily because of the need to densely evaluate the output of the gating layer. Besides, these methods leave the question of optimizing attention layers (QKV projection) unanswered.

The paper further sets context with adaptive rank allocation, which consists in decomposing a linear into two lower-rank layers parameterized by A and B matrices. Importantly, the rank is a function of the input x, and is determined by a learnable router r(x). The paper notes that adaptive rank allocation is a generalization of neural adaptors, which can be reformulated as adaptive rank allocation.
Linear layer rank adaptors can be simplified if the router is not input dependent, in which case the determination of an optimial decomposition into and B can be performed using the Eckart-Young theorem.
Further to this, a binary masker may be derived to output an input-dependent mask which, in expectation, leads to the target average rank. Specifically the binary masker requires calculating (Bx)^2. This operation is inexpensive when the output dimension is bigger than the input dimension and is thus suitable for QKV, up-projection and gate-projections.
The paper then tackles the case of down-projections: for these layers, a simple neural thresholding masker is used.

Experimental results are shown to empirically prove that a small number of A column vectors capture most of the information, making low-rank approximation efficient.
Further experimental results show superior accuracy and perplexity vs other methods at similar compression ratios.

### Strengths
The paper is very well written and is grounded with elaborate theory on the subject.
The topic of the paper is important for the field of transformers.
The method could be applied to a broad range of model architectures, including vision transformers.

### Weaknesses
The paper compares the method against a rather narrow range of baselines. It would be interesting to compare against pruning baselines, as these are related methods for optimizing the runtime performance of models.  Other baselines could include LLMPruner, SliceGPT, ShearedLLaMA, FlexTron, Minitron, etc.

The paper does not give much details on the practical implementation of the method. It would be useful to see more information on the training process. It would help readers to have an informative diagram to summarize the process. It would also be interesting to know how the method interfaces with DL frameworks (PyTorch, FlexAttention, etc.). An open-source implementation would be best.



### Questions
Can you provide a pseudo-code implementation of the method? 

How does the method compare against FlexTron (https://arxiv.org/pdf/2406.10260), Minitron (https://arxiv.org/pdf/2408.11796).

What is the relationship between the neural thresholding employed for down-projection layers and CATS?

Are the compression ratios mentioned in experimental results taking the contribution of the router FLOPs into account? Can you show a breakdown of total FLOPs between the main computation and the computation of the routers.

How is the FLOPs reduction achieved in practice? Are tensor sliced and how does this affect memory caching/coalescing? Which DL framework was used to implement the method? 

Does batched inference work and achieve the desired speed-ups if masks are inconsistent between samples?

Could you share end-to-end inference latency measurements and compare the achieved speed-up with the FLOPs reduction?

### Soundness
3

### Presentation
3

### Contribution
3
