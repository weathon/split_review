# COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
FP8 training has emerged as a promising method for improving training efficiency. Existing frameworks accelerate training by applying FP8 computation to linear layers while leaving optimizer states and activations in higher precision, which fails to fully optimize memory usage. This paper introduces COAT (\textbf{C}ompressing \textbf{O}ptimizer States and \textbf{A}ctivations for FP8 \textbf{T}raining), a novel FP8 training framework designed to significantly reduce memory footprint when training large models. COAT addresses current limitations through two key innovations: (1) \textbf{Dynamic Range Expansion}, which aligns optimizer state distributions more closely with the FP8 representation range, thereby reducing quantization error, and (2) \textbf{Mixed-Granularity Activation Quantization}, which optimizes activation memory using a combination of per-tensor and per-group quantization strategies. Experiments demonstrate that COAT effectively reduces end-to-end training memory footprint by 1.54× compared to BF16 while achieving nearly lossless performance across various tasks, such as Large Language Model pretraining and fine-tuning and Vision Language Model training. COAT also achieves a 1.43× end-to-end training speedup compared to BF16, performing on par with or surpassing TransformerEngine's speedup. COAT enables efficient full-parameter training of large models on fewer GPUs, and facilitates doubling the batch size in distributed training settings, providing a practical solution for scaling large-scale model training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a novel fp8 training framework named COAT that improves throughput and memory footprint of (end-to-end) large-scale training respectively by 1.54x and 1.43x. In detail, COAT is built upon two key techniques of (1) dynamic range expansion that allows for abetter utilization of fp8 format’s representation range, and (2) mixed-granularity activation quantization that reduces the memory footprint for activations. The authors demonstrate that COAT achieves superior memory/compute efficiency while preserving the bf16 performance on three tasks of LLM pretraining, fine-tuning, and VLM training.

### Strengths
1. Given that H100 is a fairly new hardware, fp8 training has not been explored extensively in previous literature. At the same time, the potential memory/compute efficiency gain from fp8 training can be significant, so I believe this paper addresses an important problem and makes a progress in this topic.
2. Dynamic range expansion is well-motivated by the analysis from Figure 2.
3. I believe ~1.5x improvements in memory/compute efficiency is significant.

### Weaknesses
1. Even if the performance gap looks not too significant, COAT still underperforms bf16 training on most tasks. At the same time, the ablation study only focuses on memory/compute efficiency, but not the final model performance. Providing insights on how each component influences the model performance and insights on the source of the performance degradation can be useful.
2. It is unclear to me how/whether the dynamic range is synchronized across GPUs in the distributed training setting.

### Questions
See above.

### Soundness
3

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
This work proposes a quantization improvement for transformers that mainly targets the optimizer’s states and activations. The authors propose a FP8 per-group quantization of the optimizer’s states along with a “dynamic range expansion” that utilizes the quantized space more effectively. The FP8 per-group quantization is also applied on the activations with "mixed-granularity", i.e., different layers quantize their inputs differently (e.g., layernorm vs. linear). These improvements can save up to 1.5x memory over TransformerEngine and is slightly faster as well without sacrificing performance vs. FP16 quantization.

### Strengths
- The experiments demonstrate significant space improvements in practice and slight speed up.
- Figures illustrates methodology and motivation clearly.
- The authors motivate the quantization method by looking at the low-bit values as a range of representable values, and show that optimizer states are sparse in this representation and do not span the range nicely. A transformation $f(x)=x^k$ can be applied before quantization and inverted after dequantization easily, allowing for the quanitized values to span the range of representable values more uniformly.
- Table 2 shows the actual improvements in memory clearly.
- The mixed-granularity approach is simple yet effective in practice.

### Weaknesses
The scientific contribution of this work is limited. Despite the practical improvements, it might be of little interest to the community of “learning representations”, but perhaps of great interest to LLM practitioners, which is certainly a significant part of the AI community. Thus, I will not wholly judge the paper by its scientific merit and shall take a pragmatic approach in my rating here, but the point regarding the contribution still stands.

The authors could have, for example, expanded on Sec 4.1. They could have studied or tried other inveritble transformations that spread out the values nicely across the representable values. Would direct training in this transformed low-bit regime work? Perhaps the author can study whether polynomial activations can have the same benefits, for example. This would make the paper more interesting.

Another thing is that the idea behind the dynamic range is quite straightfoward to conceive, so I believe a more careful literature review can reveal very similar techniques. For example, a quick search reveals [1], which studies a similar problem.

Finally, the engineering improvements to transformer quantization are indeed non-trivial but can be found by extensive experimentations and ablation studies, which might not be possible for those who cannot afford to run such extensive experiments. Thus, I believe more effort should go into justifying the engineering choices found by the authors, which would be greatly appreciated and would motivate similar practices in the future. For example, a more fine-grained ablation studiy or theoretical analysis of the mixed-grained quantization can be great. This should also inform future readers on whether this particular quantization method is the best one for some particular setting.

### Questions
None.

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
3

### Summary
This paper introduces COAT, a scheme for efficient low-precision training of large models. It is based on compressing optimizer states and model activation through two mechanisms: _(i) Dynamical Range Expansion_ for fully exploiting the representation range of the FP8 format for the optimizer states) and _(ii) Mixed-Granularity Activation Quantization_, which uses a combination of per-tensor and per-group quantization strategies to compress model's activations.

Extensive experiments are conducted on LLMs (OLMo-1/7B, LLaMa 2/7B) and VLMs (VILA1.5-7B), showing solid and consistent improvements in (i) memory efficiency and (ii) training speed, at nearly lossless performance.

### Strengths
In my opinion, this paper has the following main strenghts:
- **Clear presentation:** the paper is very clearly written, both the introduction and the related work sections introduce the necessary notions the proposed approach is built on and improves upon. All the figures/tables are of good quality and are well displayed in a printed version of the manuscript.
- **Practical significance:** as highlighted by the authors, efficient training of large models is a timely problem, the ideas presented in this work are relatively simple but proven effective in realistic scenarios. Overall, I believe that the proposed approach has the potential to be integrated in classical schemes for large-scale training.

### Weaknesses
The main points of discussion of this submission are in my opinion related to:
- **Novelty/Fit for ICLR:** the proposed techniques are not strictly novel in terms of research. Indeed, while the approach itself is technically new (e.g. at the best of my knowledge has not been proposed in previous works) it uses a combination of state-of-art techniques, with a strong engineering focus on how to integrate them in the most effective way. For example, the proposed _Dynamic Range Expansion_ is a simple expansion of the domain values of the optimizer states to the range of the used representation, and the _Mixed-Granularity Activation Quantization_ uses VS-Quant and Per-Block Quant for non-linear layers and per-tensor quantization for linear layers, which are not themselves new techniques.
- **Missing implementation details:** given that the work is purely experimental and that reproducing the results strongly relies on efficient implementation, one would expect more implementation details. The provided details are sufficient for an high-level understanding of the proposed approach but still require significant effort to reproduce the results. Ideally, one would like to have a working code attached to the submission, such that reviewers can try it. Indeed, at the current state, it is not possible for a reviewer to reproduce the results.

In essence, I believe that this paper has mainly (good) incremental engineering contributions, while I have some concerns about its contributions in term of research ideas. Overall, I do question if it is a good fit for ICLR, rather than the validity of the approach or its practical usefulness.
I provisionally give a "Borderline accept" and wait for the next phase to discuss with other reviewers.

### Questions
- Can you discuss better the approaches related to Activation Quantization? From lines 128-132 is not clear what are the improvements and the novelty of the proposed approach with respect to previous works.
- Can you provide a deeper explanation of what are the main differences between the proposed Group Scaling and the TransformerEngine's Delayed Scaling? In the text it is mentioned that it causes instabilities, but it is not clear what they are and why they arise.

Small issues:
- There is a missing ref. in line 372: "performance in [] 4".
- Table 6 is a little bit confusing in reporting the memory saving and the speedup, e.g. it is not immediately clear that the first "Ratio" column refers to runtime and the second to memory usage. I suggest to make it clearer, for example by adding a vertical line after the first "Ratio" column.

### Soundness
3

### Presentation
3

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
This work presents COAT, a new framework for FP8 training. There are two key designs. The first is a dynamic range expansion that tries to align the value range of optimizer states to that of FP8 representation, which improves the utilization of the FP8 value range and reduces quantization errors. The second is a mixed-granularity activation quantization, which combines (less nuanced) per-tensor quantization to linear layers and (more nuanced) per-group quantization to non-linear layers. Experimental results show that COAT achieves nearly the same convergence as BF16 training, yet is more time and memory efficient.

### Strengths
The paper is clearly written, well elaborating the problems of FP8 training as well as the proposed techniques to address the problems. Experiments on LLM pre-training, LLM fine-tuning, and VLM SFT demonstrate the sound convergence of COAT. And positive results present the improvement in terms of memory reduction and training speedup.

### Weaknesses
- The novelty of this work needs a justification. 
- The ablation studies do not break down the improvement of each component.
- All discussions about FP8-LM are textual, lacking empirical comparisons in Section 6 and formal analysis in Table 2.

### Questions
(Q1) Dynamically scaling the value been has been proposed for long. For instance, almost all integer quantization approaches will scale the values with the max value or the norm of tensors. I suggest the authors discuss the novelty of their work, such as why exponential expand function is chosen.

(Q2) Per-group quantization can be done by first slicing the original tensor and then performing a per-slice quantization, which is implementation-specific. For me, a more important problem is how to determine the group size automatically. Currently there are no related discussions. And it is unclear how group sizes are determined in the experiments (e.g., based on hyper-parameter tuning or adaptive selection). If it is manually tuned, a sensitivity experiment would be nice to have.

Besides, in lines 83-85, the authors said that “per-tensor quantization for matrix multiplications is more efficient and better suited for TensorCores, while fine-grained quantization helps maintain accuracy.” I was expecting an empirical assessment on this, but failed to see any. Intuitively, fine-grained per-group quantization should always achieve lower quantization errors, then we should always prefer it to the per-tensor one if the efficiency gap is not significant. 

(Q3) The convergence experiments are incredible. However, it would be better to break down the improvement of each design in your work. In addition, breaking down the speedup and memory reduction for different modules in the model can help readers better understand the effectiveness. 

(Q4) FP8-LM, one of the most relevant works, is only briefly discussed, while not included in the analysis and experiments in the main body. 

(Q5) In lines 333-334, the authors said that the max reduction on each $1 \times G$ “can be seamlessly fused with the previous operation, adding minimal overhead”. Can you provide more details about how this is achieved?

(Q6) Minor comments:
- Line 192: “can not” should be “cannot”.
- Footnote 2: “RoPE and FlashAttention is …” should be plural.
- In Table 2 and Appendix, it might be more appropriate to set 1U to be FP8, rather than BF16.

### Soundness
3

### Presentation
3

### Contribution
3
