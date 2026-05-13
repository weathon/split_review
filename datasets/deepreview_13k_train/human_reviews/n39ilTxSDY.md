# Ditto: Quantization-Aware Secure Inference of Transformers upon MPC

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
Due to the rising privacy concerns on sensitive client data and trained models like Transformers, secure multi-party computation (MPC) techniques are employed to enable secure inference despite attendant overhead. Existing works attempt to reduce the overhead using more MPC-friendly non-linear function approximations. However, the integration of quantization widely used in plaintext inference into the MPC domain remains unclear. 
To bridge this gap, we propose the framework named \name to enable more efficient quantization-aware secure Transformer inference.
Concretely, we first incorporate an MPC-friendly quantization into Transformer inference and employ a quantization-aware distillation procedure to maintain the model utility. Then, we propose novel MPC primitives to support the type conversions that are essential in quantization and implement the quantization-aware MPC execution of secure quantized inference.
This approach significantly decreases both computation and communication overhead, leading to improvements in overall efficiency.
We conduct extensive experiments on Bert and GPT2 models to evaluate the performance of \name. The results demonstrate that \name is about $3.14\sim 4.40\times$ faster than MPCFormer (ICLR 2023) and $1.44\sim 2.35\times$ faster than the state-of-the-art work PUMA with negligible utility degradation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a framework for quantization-aware secure Transformer inference.

### Strengths
+ MPC-friendly Quantization-Aware Distillation.
+ MPC primitives for scale down and scale up.
+ Comparison with SOTA.

### Weaknesses
 - Distillation is widely used in MPC-based secure inference works.
- It seems limited contributions of MPC protocols.

### Questions
1. Does the  Downcast protocol have a probabilistic error? What is the difference compared with the truncation of SecureML?
2. In Upcast, what distribution is $r$ sampled from? How to ensure the input is positive?
3. Could you provide the theoretical or experimental advantages of the proposed Downcast and Upcast protocols compared with SOTA?

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes MPC primitives to support quantization-aware private inference. Moreover, the authors propose a MPC-friendly quantization-aware distillation to retrain the model utility.

### Strengths
1. This paper targets an important problem in private inference.

2. The proposed type conversion protocols are creative solutions to a key challenge in quantization-aware secure inference.

3. Extensive evaluations analyzing efficiency, utility, scalability, and communication costs and latency on factors like sequence length and batch size.

### Weaknesses
1. Lack of comparison to the latest related work.

### Questions
How would the proposed DITTO be compared with Iron [1]?

[1] Hao, Meng, et al. "Iron: Private inference on transformers." Advances in Neural Information Processing Systems 35 (2022): 15718-15731.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Author introduce Ditto -- a framework designed to enhance the efficiency of secure inference in Transformer models using multi-party computation (MPC). It incorporates MPC-friendly quantization and a quantization-aware distillation procedure to both reduce computational overhead and maintain model utility. Empirical tests on Bert and GPT2 models show that Ditto significantly outperforms existing solutions, being 3.14 to 4.40 times faster than MPCFormer and 1.44 to 2.35 times faster than PUMA, with negligible loss in utility.

### Strengths
* The authors present a solution that addresses multiple bottlenecks in secure multi-party computation (MPC) for Transformer models. For example, challenges like handling non-linear functions and dynamic quantization in an MPC context. They also offer a solution such as modified dyadic quantization and static dyadic quantization for these issues. 

* The paper highlights and addresses the often-overlooked disconnect between the expertise in machine learning and multi-party computation. For example, it effectively integrates best practices from MPC-friendly quantization and type-conversion primitives, thereby enhancing end-to-end secure inference efficiency.

* The authors show empirical evidence that their contributions are valid. They compared Ditto against existing state-of-the-art frameworks like MPCFormer and PUMA, the authors make a compelling case for the performance advantages of their approach.

### Weaknesses
 * The paper acknowledges that both Ditto and MPCFormer exhibit noticeable utility drops in Bert tasks when employing ReLU approximation for Softmax. They offer Quad approximation for GeLU to maintain a balance between utility and efficiency, but this limitation may constrain the applicability of the framework for tasks where such approximations are not tolerable. Specifically, the reliance on a quadratic approximation for GeLU, while efficient in MPC, introduces an approximation error that can be significant for certain tasks. The authors should provide a more detailed analysis of the cases where this approximation is most detrimental and explore alternative approximation strategies that may offer better accuracy.

* The paper in general is hard to read and require additional proof-reading. I would recommend making the paper to be easier to read by highlighting important concepts, introducing figures that support main results, and describing contributions and future work. For example, a clearer explanation of the type conversion primitives and their impact on communication overhead would be beneficial. The current presentation makes it difficult to grasp the technical novelty and practical implications of the proposed approach. The paper would also benefit from a more detailed discussion of the limitations and potential failure modes of the proposed quantization-aware distillation procedure.

### Questions
What are the primary limitations of using more aggressive quantization methods, as mentioned in the future work section, in the context of secure inference? Would it significantly affect model utility, or are there other challenges like security vulnerabilities that need to be addressed?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
