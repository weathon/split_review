# Optimize Weight Rounding via Signed Gradient Descent for the Quantization of LLMs

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Large Language Models (LLMs) have demonstrated exceptional proficiency in language-related tasks, but their deployment poses significant challenges due to substantial memory and storage requirements. Weight-only quantization has emerged as a promising solution, significantly reducing memory and storage needs without sacrificing too much performance.
In this study, we introduce SignRound, a method that leverages signed gradient descent (SignSGD) to optimize rounding values and weight clipping in just 200 steps. SignRound integrates the advantages of Quantization-Aware Training (QAT) and Post-Training Quantization (PTQ), delivering exceptional results across 2 to 4 bits while minimizing tuning costs and avoiding additional inference overhead. For example, SignRound achieved absolute average accuracy improvements ranging from 6.91\% to 33.22\% at 2 bits, as measured by the average zero-shot accuracy across 11 tasks. It also demonstrates strong generalization in recent models, achieving near-lossless 4-bit quantization in most scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
* The paper proposes to optimize the layer-wise rounding problem that occurs for LLM PTQ using signed gradient descent.
* The method is evaluated across various models and tasks.

### Strengths
* The paper is easy to follow.
* The paper conducts a large number of experiments across various models, tasks and quantization setting. Further, it also consider state-of-the-art LLMs like Llama2 in addition to older ones like OPT and BLOOM.
* SignRound appears to bring some performance improvements relative to GPTQ, in particular on smaller models and for zero-shot tasks.
* I also like that the paper includes also handful of unfavorable results to provide a more complete.

### Weaknesses
 * The paper essentially seems to apply signed gradient descent (which is not new) to the standard layer-/block-wise rounding problem considered by various LLM PTQ papers. Hence, the overall novelty is low.
* GPTQ Activation-reordering can also be performed without any impact on inference performance (see the official GPTQ repo, option `--static-groups`). Further, if there is no grouping, reordering has no impact on inference. LLaMa1-7B and OPT-66B are known to be GPTQ outliers, for which reordering should be enabled to conduct a fair comparison.
* The paper argues that signed gradient descent is preferable over standard straight-through QAT (applied to the layer-wise quantization problem, like ZeroQuant) for this application, but does not provide any ablation studies supporting that point. Furthermore, the justification provided for using signed gradient descent over other optimizers like AdamW is not sufficiently compelling. The argument that the search space is bounded and that the optimal value is a region rather than a single point does not inherently favor signed gradient descent. Other optimizers can also effectively navigate such a space, and the claim that signed gradient descent is more lightweight is not substantiated with concrete evidence of resource savings. The fact that AdamW is only 20-30% slower and requires slightly more memory, given the relatively short overall runtime, does not make this a decisive factor.
* Based on Table 5, it appears that for the largest and most interesting models for compression applications, SignRound seems to perform very similar to GPTQ and in some cases even worse. Further, in Tables 9 & 10, GPTQ/GPTQ-R wins in 13/16 cases, further confirming the initial concerns.
* The code is not available in the Supplementary material.

### Questions
* Is GPTQ using the same amount of samples as SignRound in your comparisons?
* Do you have any explanation for the surprisingly poor perplexity performance on Llama" models in Table 3? Related to that, how comes that those models still exhibit comparable or better ZeroShot performance.
* The runtime comparisons in Table 12 stop at 13B size, how long does your method take for the largest models?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work develops a signed gradient decent for the quantization of large language model weights. It compares against other approaches that are more complicated algorithmically and achieve slightly better results.

Recommendation: This is a solid contribution that I would rather see accepted than rejected.

### Strengths
- simple approach will make it easier to develop more complicated methods. This is a large advantage over GPTQ which is a good foundation for future methods.
- evaluation is quite extensive, leaving little doubt that the method works well
- shows that the Hessian approach from GPTQ does not add too much unique value, but mostly reduces the samples needed for good performance. This is a very valuable insight that will quite future quantization work.

### Weaknesses
 - while the simplicity is an advantage of this method, it can also be seen as a disadvantage. However, I would like to highlight for the AC and reviewers that the main goal of the paper is to simplify a complicated algorithm (GPTQ), and the authors succeed
- not competitive with other more extensive methods. However, other methods cannot be used as a base optimization method for finding quantization. As such, this approach is more useful for future work
- why is there such high C4 perplexity for transformer block quantization for W3G128? Do the numbers indicate some form of instability during sign SGD?
- Why is the runtime so slow? Are you building on the GPTQ codebase?

### Questions
Comments:
 - before equation 6, the equation is missing an "s"

Questions:
- why is there such high C4 perplexity for transformer block quantization for W3G128? Do the numbers indicate some form of instability during sign SGD?
- Why is the runtime so slow? Are you building on the GPTQ codebase?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
For better weight-only LLM quantization, this work proposes to optimize the rounding of weights with the block-wise reconstruction error as the objective. Following previous smart rounding work such as AdaRound, it optimizes continuous variables that will be added onto the scaled weights before rounding. This work also emphasizes the need to use "signed gradient descent" in the rounding variable optimization, which only exploits the gradient direction instead of the magnitude. This work conducted experiments on quantizing LLaMA v1, v2, BLOOM, and OPT models to W3 and W4 with different group sizes.

### Strengths
* Motivation: How to make weight-only LLM quantization work for fewer bits is worth studying, especially for edge scenarios with very limited memory.
* Reasonable pathway: Applying smart-rounding PTQ methods is a reasonable pathway.
* The experiments are conducted with different model families.
* The paper is easy to understand.

### Weaknesses
 * Unclear logic of applying signed gradient descent: The paper said "prefer the signed gradient descent method to tackle the issue of sub-optimal rounding" without intuitive logic description, theoretical justification, or experimental verification of this technique. The paper lacks a clear explanation of why signed gradient descent is superior to other optimization methods for this specific rounding problem. It's not clear why the magnitude of the gradient is not important in this context, and the paper does not provide any analysis of the loss landscape that would justify this choice. The claim that signed gradient descent is better suited for the constrained rounding space is not sufficiently supported by evidence or theoretical arguments. Furthermore, the paper does not explore alternative optimization strategies, such as adaptive methods, in sufficient detail to justify the exclusive use of signed gradient descent.
* Marginal improvements: The method shows improvements on relatively smaller models, but on larger models (>7B), it achieves marginal improvements over GPTQ or RTN. The improvements over existing methods like GPTQ and RTN are not consistently significant, especially for larger models. The paper needs to provide a more in-depth analysis of why the proposed method's performance plateaus on larger models. It's not clear if the method's limitations are due to the optimization strategy, the rounding approach itself, or the model architecture. The lack of substantial improvement on larger models raises questions about the practical applicability of the method in real-world scenarios where large models are often preferred.

### Questions
See the weakness part

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces SignRound, a lightweight and effective approach for optimizing weight rounding in Large Language Models (LLMs) with 3 and 4-bit weight-only quantization. SignRound leverages signed gradient descent and achieves remarkable results in just 400 steps, competing favourably with recent methods. Experiments on several datasets demonstrate the effectiveness of the proposed method.

### Strengths
The paper is well written and easy to follow. SignRound achieves significant results within only 400 steps, showcasing its efficiency.

### Weaknesses
The paper's novelty is somewhat circumscribed, given its central focus on learning weight rounding—a concept previously introduced by AdaRound (Nagel et al., 2020). While SignRound's utilization of the signed gradient to refine the rounding function distinguishes it, the motivation behind prioritizing only the gradient direction (ignoring gradient magnitudes) remains ambiguous. 

The authors appear to have not fully accounted for certain pivotal baselines in their study. Specifically, AdaRound (Nagel et al., 2020) and FlexRound (Lee et al., 2023) stand out as established methods that delve into the realm of learning weight rounding. It would enhance the paper's comprehensiveness and comparative analysis if these methodologies were discussed and compared with SignRound.

The performance comparisons between GPTQ and the proposed method are unfair since act-order was not enabled. This omission potentially skews the results, leading to instances where GPTQ underperforms compared to rounding-to-nearest (RTN) in some cases (W4 in Table 1).

GPTQ, by utilizing second-order information, offers an efficient solution to the weight quantization problem. It would benefit for the authors to provide a clearer distinction of the advantages offered by the proposed method, especially when there are instances where it lags behind GPTQ, as evidenced in Tables 3, 4, and 5. Additionally, omitting a comparative analysis on training time introduces ambiguity, making it challenging to ascertain the relative efficiency of the two methods.

Referring to Table 4, it is noteworthy that the proposed method underperforms compared to RTN for both W4G128 LLaMA-7B and W3G128 LLaMA-7B configurations. A more in-depth exploration or justification for this discrepancy would enhance the paper's clarity. 

The comparisons presented in Table 8 between AWQ and the proposed method appear unfair due to disparities in the calibration datasets. For a comprehensive assessment of the proposed method's efficacy, it would be better for the authors to provide fair comparisons.

The novelty of the proposed method remains unclear. A comprehensive performance comparison against AdaRound and FlexRound is necessary to demonstrate the advantages of the proposed method. Furthermore, the comparison with GPTQ is not entirely fair, as GPTQ uses a smaller calibration dataset (128 samples) than the proposed method (512 samples). Finally, the inferior results of the proposed method compared to RTN in certain configurations is a significant concern that requires further investigation.

### Questions
1.	The paper's novelty is somewhat circumscribed, given its central focus on learning weight rounding—a concept previously introduced by AdaRound (Nagel et al., 2020). While SignRound's utilization of the signed gradient to refine the rounding function distinguishes it, the motivation behind prioritizing only the gradient direction (ignoring gradient magnitudes) remains ambiguous. 

2.	The authors appear to have not fully accounted for certain pivotal baselines in their study. Specifically, AdaRound (Nagel et al., 2020) and FlexRound (Lee et al., 2023) stand out as established methods that delve into the realm of learning weight rounding. It would enhance the paper's comprehensiveness and comparative analysis if these methodologies were discussed and compared with SignRound.

3.	The performance comparisons between GPTQ and the proposed method are unfair since act-order was not enabled. This omission potentially skews the results, leading to instances where GPTQ underperforms compared to rounding-to-nearest (RTN) in some cases (W4 in Table 1).

4.	GPTQ, by utilizing second-order information, offers an efficient solution to the weight quantization problem. It would benefit for the authors to provide a clearer distinction of the advantages offered by the proposed method, especially when there are instances where it lags behind GPTQ, as evidenced in Tables 3, 4, and 5. Additionally, omitting a comparative analysis on training time introduces ambiguity, making it challenging to ascertain the relative efficiency of the two methods.

5.	Referring to Table 4, it is noteworthy that the proposed method underperforms compared to RTN for both W4G128 LLaMA-7B and W3G128 LLaMA-7B configurations. A more in-depth exploration or justification for this discrepancy would enhance the paper's clarity. 

6.	The comparisons presented in Table 8 between AWQ and the proposed method appear unfair due to disparities in the calibration datasets. For a comprehensive assessment of the proposed method's efficacy, it would be better for the authors to provide fair comparisons.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
