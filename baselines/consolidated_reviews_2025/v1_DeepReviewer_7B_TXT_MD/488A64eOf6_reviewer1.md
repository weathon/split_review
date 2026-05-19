### Summary

This paper proposes a decoding method that optimizes the decoding distribution to align with human texts across various aspects. The resulting decoding distribution enjoys an analytical solution that scales the input LM distribution via a sequence-level energy function defined by constraints of chosen metrics. The authors also introduce a contrastive sampling technique to efficiently sample from the decoding distribution. Experiments on various domains and model scales demonstrate the superiority of the proposed method in terms of automatic evaluation, perplexity, and human evaluation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

* The paper is well-written and easy to follow.
* The proposed method is novel and well-motivated.
* The proposed method is theoretically grounded and has an analytical solution.
* The proposed method is efficient and scalable.
* The experiments are comprehensive and demonstrate the superiority of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 * The proposed method relies on the availability of human-annotated data, which may not be feasible in many real-world scenarios. The need for a development set with human annotations to tune the energy function introduces a dependency on labeled data that might not be readily available or representative of the target domain. This reliance could limit the applicability of the method in situations where such data is scarce or expensive to obtain.
* The proposed method is computationally expensive, especially for large models and long sequences. The contrastive sampling technique, while efficient, still involves sampling multiple candidate continuations and reweighting them, which can be computationally intensive. The paper does not provide a detailed analysis of the computational cost as a function of model size and sequence length, making it difficult to assess the scalability of the method.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations imposed by the need for human-annotated data. While the authors mention that the development set can be sampled from the pretraining corpus, they should elaborate on the potential biases that might be introduced by this approach. For example, if the development set is sampled from a specific subset of the pretraining data, the resulting energy function might be biased towards that subset, limiting the generalizability of the method. Furthermore, the authors should explore alternative approaches to reduce the reliance on human-annotated data, such as using weakly supervised learning techniques or self-training methods. This would make the method more practical and applicable in real-world scenarios where labeled data is scarce.

To address the computational concerns, the authors should provide a more detailed analysis of the computational cost of the proposed method. This analysis should include the time complexity of the contrastive sampling technique as a function of model size and sequence length. It would also be beneficial to compare the computational cost of the proposed method with other decoding methods, such as beam search and nucleus sampling. Furthermore, the authors should explore techniques to reduce the computational cost of the method, such as using more efficient sampling algorithms or approximating the energy function. This would make the method more practical for large-scale applications. The authors should also provide a more detailed breakdown of the time spent on different parts of the algorithm, such as sampling, reweighting, and decoding, to identify potential bottlenecks.

Finally, the authors should clarify the specific metrics used in the experiments and provide a more detailed explanation of how these metrics are calculated. This would make the results more transparent and reproducible. The authors should also discuss the limitations of the chosen metrics and how they might affect the evaluation of the proposed method. For example, they should discuss whether the chosen metrics are sufficient to capture all aspects of human preference and whether there are other metrics that could be used to evaluate the method. A more thorough discussion of the evaluation metrics would strengthen the paper and make the results more convincing.

### Questions

* The proposed method relies on the availability of human-annotated data, which may not be feasible in many real-world scenarios. Can the authors elaborate on how to obtain human-annotated data for the development set?
* The proposed method is computationally expensive, especially for large models and long sequences. Can the authors provide more details on the computational cost of the proposed method?
* The authors should clarify the specific metrics used in the experiments and provide a more detailed explanation of how these metrics are calculated.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
