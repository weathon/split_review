# Enhancing Zeroth-order Fine-tuning for Language Models with Low-rank Structures

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
Parameter-efficient fine-tuning (PEFT) significantly reduces memory costs when adapting large language models (LLMs) for downstream applications. However, traditional first-order (FO) fine-tuning algorithms incur substantial memory overhead due to the need to store activation values for back-propagation during gradient computation, particularly in long-context fine-tuning tasks. Zeroth-order (ZO) algorithms offer a promising alternative by approximating gradients using finite differences of function values, thus eliminating the need for activation storage. Nevertheless, existing ZO methods struggle to capture the low-rank gradient structure common in LLM fine-tuning, leading to suboptimal performance. This paper proposes a low-rank ZO gradient estimator and introduces a novel \underline{\textbf{lo}}w-rank \underline{\textbf{ZO}} algorithm (LOZO) that effectively captures this structure in LLMs. We provide convergence guarantees for LOZO by framing it as a subspace optimization method. Additionally, its low-rank nature enables LOZO to integrate with momentum techniques while incurring negligible extra memory costs. Extensive experiments across various model sizes and downstream tasks demonstrate that LOZO and its momentum-based variant outperform existing ZO methods and closely approach the performance of FO algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces low-rank zeroth-order optimization algorithms, called LOZO and LOZO-M, for memory-efficient fine-tuning of large language models (LLM). The authors claim that by utilizing a low-rank unbiased gradient estimator, LOZO and LOZO-M perform comparably to first-order (FO) methods while outperforming existing zeroth-order (ZO) approaches in term of memory and accuracy. The paper provides convergence guarantees and extensive experimental results to support these claims.

### Strengths
The paper proposes a novel algorithm to addresses a critical limitation of ZO methods which is the inability to capture low-rank gradient structures effectively. The application of momentum without substantial memory overhead is innovative. These features are valuable for fine-tuning LLMs in memory-constrained environments. LOZO and LOZO-M achieves comparable performance to traditional FO FFT methods and outperforms existing ZO methods shows that the proposed algorithms can be viable alternatives to widely used FO approaches. The rigorous convergence provides valuable insights into the understanding of LOZO.

### Weaknesses
The paper lacks direct memory comparisons with full fine-tuning (FFT) and FT-LoRA methods. This weakens the claim that LOZO and LOZO-M outperforms FO approaches in term of memory efficiency.

Furthermore, the paper primarily focuses on SuperGLUE benchmarks which is limited. Expanding experiments to more tasks would help demonstrate the generalizability of LOZO across different NLP tasks.

Next, one of the main claims of the paper is the ability of LOZO's to handle long-context tasks. However, focusing on SuperGLUE benchmarks only doesn't support this claim.

Finally, testing LOZO and LOZO-M on different types of models, especially, larger models would provide a stronger case for their scalability. Currently, the authors only test the proposed methods on one model family.

### Questions
1. Could you provide direct comparisons with FFT and FT-LORA in term of memory usage? This would strengthen your claim of LOZO's memory efficiency relative to FO methods.

2. How do LOZO and LOZO-M perform on tasks beyond SuperGLUE, especially ones tailoring to long-context? This would demonstrate their adaptability and robustness across various applications, and their ability to handle long-context.

3. How do LOZO and LOZO-M perform on different models, especially larger ones? This benchmark would further provide insights into their scalability.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a novel zeroth-order optimization method for fine-tuning. The proposed method consumes significantly less memory while maintaining (and sometime even improving) the quality when compared with other FT methods including MeZO (another zeroth order method), ICL and LoRA methods. The core contribution is the "lazy sampling strategy" where the perturbation matrix for gradient estimation is sampled over several training steps, rather than each iteration. This ensures that the model sufficiently explores low rank sub space, without abrupt changes in the parameters at each iteration step. Extensive Experimentation on large scale OPT models show the efficacy of the approach.

### Strengths
1) Well motivated approach, clearly outlines the shortcoming of other zeroth order approaches, like MeZO.
2) Proposed algorithm is well written, clear and the core concepts are presented well. The "lazy sampling strategy" is novel and interesting. 
3) The paper proposes momentum variant and provides convergence analysis by interpreting LOZO as subspace optimization method by employing ZO gradient estimator.
4) Extensive experiments on both medium scales and large scale LLMs are convincing in terms of quality gains and memory savings.

### Weaknesses
1) The experiments are performed on OPT based LLMs. It would be good to see what kind of memory savings and quality improvements the method gets on SoTA models like Llama.
2) Additionally, the LLM evaluations are not exhaustive and lack eval suites around critical benchmarks around reasoning, MATH, Instruction following etc. 
3) An Ablation study on hyper-parameter choices for N and r for critical evals maybe helpful.

### Questions
1) Line 268-269. Is there a justification for the chose hyper-parameter values of N and r? Are there ablation results for the same?
2) Figure 3 : Are there loss curves for other datasets at 13B and 30B scale to understand the scaling behavior?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript presents a approach to parameter-efficient fine-tuning (PEFT) of large language models (LLMs) using zeroth-order (ZO) optimization. The authors propose a low-rank ZO gradient estimator and introduce a new algorithm called LOZO, which captures the low-rank gradient structure common in LLM fine-tuning. The paper provides convergence guarantees for LOZO, frames it as a subspace optimization method, and demonstrates its effectiveness through extensive experiments across various model sizes and downstream tasks.

### Strengths
Strengths:

1. theoretical guarantees: The manuscript introduces a low-rank ZO gradient estimator and algorithm (LOZO) that addresses the memory inefficiency issue associated with traditional first-order fine-tuning methods for LLMs.

2. Clear Structure and Writing: The manuscript is well-organized, with a clear presentation of the problem, methodology, experiments, and results.

### Weaknesses
Weaknesses:

1. **Marginal improvements for memory**: While the manuscript emphasizes the superior memory efficiency of the LOZO algorithm over MeZO, the proposed advantage is not convincingly demonstrated. The potential improvements in memory usage could be predominantly attributed to MeZO's zeroth-order optimization approach, with LOZO offering only marginal enhancements. As illustrated in Table 1, the memory usage is reduced from a range of approximately 3 to 7.42 GB for MeZO to 2.84 GB for LOZO, which does not present a substantial difference to assert the claimed memory efficiency advantage of LOZO. The core issue is that the low-rank approximation, while theoretically sound, does not translate to a significant practical reduction in memory footprint compared to the base MeZO method, especially considering the overhead of maintaining the low-rank structure itself.

2. **Experiments insufficient**: Furthermore, the study's benchmark does not encompass key capabilities of LLMs, such as common sense reasoning (MMLU) and complex reasoning tasks (GSM8k). There is a concern that this proposed fine-tuning approach might not effectively enhance the LLM's high-level cognitive abilities. The absence of these benchmarks leaves a critical gap in evaluating the practical utility of the proposed method for real-world applications where these capabilities are paramount. The current evaluation is limited to tasks that may not fully capture the nuances of LLM reasoning and generalization.

### Questions
Questions:

1. How do the memory savings of LOZO when applied to larger models and datasets, such as OPT-13B or Llama-70B?

2. Have there been any experiments conducted to assess the impact of this fine-tuning method on the complex capabilities of LLMs, such as instruction following and reasoning?

3. Are there any experiemnts to demonstrate the improvements in  speed of training and convergence when comparing LOZO with current methods?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies the way to improve the performance of zeroth-order fine-tuning by doing perturbation in a low-rank space. The paper provide detailed theoretical proof for the convergence of the proposed algorithm and experimental results with similar setup as the previous ZO fine-tuning paper on model up to 30B.

### Strengths
The method proposed in this paper is interesting, which is inspired by the work on gradient low-rank structure. Also, the lazy sampling and LOZO-M methods are interesting to be considered. I quickly went through the proof for the convergence rate and it seems correct and reasonable, which provide solid support for the new subspace and lazy sampling method proposed in this paper.

### Weaknesses
Given the good theoretical foundation of this paper, my main concerns are about the parts of the experiment:
- I'm a bit confused about the total training steps for LoZO and other baselines like MeZO in the experiments. For example, in Figure 2, I'm not sure if the k represents epoch here as mentioned in the previous section, or similar to the MeZO paper, represents the number of shots. Also, I'm wondering what the total number of training steps here for LoZO and MeZO? Furthermore, it seems LOZO uses a different learning rate compared with MeZO, according to Table 4, which may make the comparison unfair. The use of different learning rates makes it difficult to isolate the impact of the proposed low-rank perturbation method from the effects of hyperparameter tuning. A more controlled experiment would involve using the same learning rate or providing a detailed analysis of how the learning rate impacts the performance of each method.

- Still, for Fig. 2, I'm wondering why the MeZO-LoRA is performing worse than MeZO, as fewer trainable parameters should improve the ZO convergence rate according to the eq. (18) in the draft. I have extra two concerns here. First, this is different from the observation in Table 18 of MeZO paper, where MEZO-LoRA is performing better in most cases Second, I think it's reasonable that MEZO-LoRA fails to help on model larger than maybe 1B, where there are a lot of trainable parameters even with LoRA. But for small-size models like Roberta, MeZO-LoRA is reasonable to perform better with only 0.8 M parameters needing to be optimized. I would appreciate if the author could further explain this. The discrepancy between the results presented here and those in the MeZO paper raises concerns about the reproducibility of the experiments and the robustness of the proposed method. It is crucial to understand the underlying reasons for these differences, as they may indicate potential limitations or sensitivities of the approach.

### Questions
My main questions are listed in the weakness section, here is a few of additional concerns:
- For Fig. 3, I have similar confusion about the total training steps. From my understanding, LOZO has an additional interval in each epoch. So LOZO has more training steps actually?
- I would appreciate it if the author could provide an evaluation loss vs. wall-time figure to demonstrate the effectiveness of the proposed method. Specifically, this would validate that the low-rank perturbation helps improve convergence speed with respect to training time, which is more critical than the number of training steps.
- The improvement in experiments is limited, considering the large variance of ZO method even between runs with different random seeds.
- How about LoZO-M perform on the large-scale model, just curious. I understand this is not the main purpose of your work and wondering if the momentum is becoming less important on large-scale models due to the large variance of ZO estimation.


Generally, I think this paper provides a solid method to improve the convergence of the ZO method. Further, clarifying experiments and including more discussion may benefit the reader of this paper.

### Soundness
3

### Presentation
4

### Contribution
3
