# DuaRot: Dual Rotation for Advanced Outlier Mitigation in Rotated LLMs

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 5, 3

## Abstract
By employing rotation, outliers in activations can be effectively mitigated without altering the output, thereby facilitating the quantization of large language models (LLMs). However, existing rotation-based methods only consider global activation distributions, leaving the finer-grained distributions underexplored. Additionally, these methods predominantly rely on the Walsh–Hadamard transform (WHT) to accelerate online rotation operations, while not fully considering performance between matrix multiplication~(Matmul) and WHT in actual runtime. These limitations hinder the rotation's ability to effectively reduce quantization errors and decrease inference speed. Therefore, improvements are needed in their performance regarding both accuracy and speed. In this paper, we propose a dual rotation method for rotation matrices, dubbed DuaRot, based on reparameterization. During training, DuaRot sequentially refines global and local features to achieve effective outlier mitigation. During inference, global and local rotations can be merged, which maintains rotational invariance without introducing additional computational overhead. Meanwhile, we propose a hardware-aware matrix configuration strategy, which determines whether the online Hadamard matrix should be expanded into a trainable parameter space by taking the runtime of the WHT and Matmul into account. This approach further enhances the reduction of quantization errors in online rotation operations without compromising inference speed. Extensive experiments demonstrate that DuaRot outperforms existing methods across various models and quantization configurations. For instance, when applied to LLaMA3-8B, DuaRot achieves WikiText-2 perplexities of 7.49 and 7.41 under W4A4KV4 and W4A4KV16 configurations with Round-to-Nearest (RTN), improving by 0.51 and 0.41 over the state-of-the-art, respectively. The code will be publicly available soon.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a rotation-based method to alleviate issues with LLM quantization. The proposed method utilizes two strategies to enhance adaptability and achieves excellent performance even without GPTQ under the INT4 setting.

### Strengths
1. The paper is well-structured and developed, making it easy for readers to follow.
2. The motivation for the proposed method is convincing.
3. The method is supported by numerous experiments, which verify its effectiveness from several perspectives.

### Weaknesses
1. Some terms mentioned in the paper may be misleading. The phrase "hardware-aware configuration" suggests that the method can automatically adapt to specific hardware. However, it may be more accurately described as a hyperparameter selection strategy guided by hardware considerations, rather than a truly adaptive mechanism. Additionally, there is results presented for only one type of hardware in the paper, which further limits the generalizability of this claim.
2. There is a lack of comparison between DuaRot and other baselines in **real runtime** for both training and inference matrices. Specifically, the paper lacks a detailed breakdown of the computational overhead introduced by the rotation operations, making it difficult to assess the practical benefits of the method. Since the authors emphasize this point multiple times in the paper, it would be beneficial for them to provide more experimental results in this area, including a comparison of wall-clock time for both training and inference.
3. The model size used in the paper is somewhat too small, which limits the persuasiveness of the method's effectiveness. The experiments are primarily conducted on 7B and 13B models, which may not fully reflect the challenges and performance characteristics of larger models, such as those with 70B parameters or more. This raises concerns about the scalability of the proposed method.
4. The ablation study is incomplete from my perspective. I believe it would be beneficial to verify the effectiveness of both global and local rotation matrices independently, as well as in combination, to fully understand their individual contributions and interactions. Furthermore, the impact of varying the size of the local rotation matrices should be explored more thoroughly.

### Questions
1. As mentioned in the Introduction section, the lack of previous work indicates that "both QuaRot and SpinQuant slow down inference speed for the decoding stage." How does DuaRot address this issue? Is there any difference between DuaRot and the mentioned methods in this regard?
2. As noted in Weakness 1, I believe it would be beneficial if you conducted experiments on additional hardware, at least including the 3090 (or 4090). Otherwise, you may want to reconsider the naming of the strategy you used.
3. What do you mean by "w/o DuaRot" in Table 3 and Figure 5? Does it imply that the method degrades to SpinQuant or something else?
4. Could you specify the modules with the online matrix $R^{d\times d}$ where $d \ge 512$ in the LLaMA/Mistral models? If there is a scenario where the online matrix is entirely Hadamard due to the hardware-aware matrix configuration strategy, will this negatively affect performance?
5. It seems peculiar that in Figure 5, when the size of $R_L = 128$, the method shows similar performance with and without DuaRot. Could you please provide a simple explanation for this? Additionally, what do you mean by "instability during training"? Is there any situation where training cannot be completed due to this instability?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces DuaRot, a method that trains global and local rotational matrices independently to effectively mitigate activation outliers.

### Strengths
- The motivation for proposing a hardware-aware matrix configuration strategy is strong and well-supported.
- The paper is clearly written and easy to follow.

### Weaknesses
 - The paper does not provide measurements for speed and memory usage, which I believe are critical evaluations and should be included.
- The experiments are limited to small-scale language models, leaving the method’s effectiveness on larger models unexplored.
- It would be helpful to provide a more direct visualization of the reduction in activation outliers to better illustrate DuaRot’s effectiveness.

### Questions
See Weakness

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
5

### Summary
This paper follows the rotation-based method QuaRot and proposes a method to learn dual rotation matrices for achieving smoother activation distributions.

### Strengths
1. The hardware-aware matrix configuration strategy is well-motivated.
2. The illustration of rotational invariance is clear and enhances understanding.

### Weaknesses
1. Although the authors mention that SpinQuant and QuaRot rely on GPTQ and aim to achieve smoother activation distributions, DuQuant [1] accomplishes this goal through two orthogonal transformations. There is a lack of discussion and experimental comparison with DuQuant, which directly addresses this motivation. Specifically, DuQuant employs a dual transformation approach, which, unlike the single rotation in DuaRot, involves two distinct orthogonal transformations to achieve a smoother activation landscape. The absence of a comparative analysis, especially given DuQuant's reported effectiveness in this area, is a significant oversight.
2. All evaluations are conducted on small-scale language models, leaving the effectiveness of DuaRot on larger models unexplored. The lack of evaluation on models such as LLaMA3-70B is a notable gap, especially considering the unique challenges and outlier distributions that have been observed in these larger models [2]. This limits the generalizability of the findings.
3. There is no measurement of speedup. Given that the authors claim improved efficiency through their matrix configuration strategy, this evalution should be included. The absence of concrete speedup metrics, especially when compared to baseline methods like QuaRot, makes it difficult to validate the efficiency claims. A detailed analysis of inference time with and without DuaRot is crucial.
4. The optimization-based approach used to enhance existing baselines is not novel. The use of Cayley optimization, while effective, does not represent a significant methodological advancement, as it has been previously employed in similar contexts.

### Questions
1. Could you discuss and compare DuaRot with DuQuant, which achieves competitive results and a smoother activation landscape without relying on GPTQ?
2. Including figures to illustrate the activation changes might strengthen the argument for DuaRot's effectiveness.
3. Please provide additional evaluation results on the LLaMA3-70B model.
4. Could you include evaluations of memory usage and inference speedup for DuaRot?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper enhances SpinQuant using two techniques. First, it introduces learnable local rotation, which can be integrated with the original global rotation after training. Additionally, the paper notes that sometimes online Hadamard rotation is slower than same-dimension matrix manipulation. To address this, the paper suggests converting the slower online Hadamard rotation into trainable parameters for more accurate quantization.

### Strengths
1. The writing is clear and easy to follow.
2. The paper provides comprehensive experiments and a detailed discussion of related works.

### Weaknesses
1. What is the source of the QuaRot and SpinQuant results? Were these results reproduced by the authors? It would be beneficial to report the source of the comparison methods.
2. This method builds on SpinQuant with two new techniques. However, Table 2 shows that the accuracy improvement over SpinQuant is negligible in most cases. While Table 1 shows more significant improvement, it may result from overfitting to the WikiText2 dataset due to more trainable parameters. It would be more reliable to test WikiText2 perplexity on other datasets, such as C4.
3. The online Hadamard rotation matrix is shared across all blocks, while the hardware-aware strategy introduces additional parameters. The paper should discuss the additional parameter overhead.
4. The introduction mentions that "both QuaRot and SpinQuant slow down inference speed during the decoding stage." Does this paper address speeding up the inference during the decoding stage?

### Questions
Please refer weakness for details.

### Soundness
2

### Presentation
2

### Contribution
2
