### Summary

This paper proposes SpecDec++, an enhanced version of speculative decoding that adaptively determines the candidate length on the fly. The method formulates the candidate length selection as a Markov Decision Process and trains an acceptance prediction head on top of the draft model. The method achieves speedup on several datasets compared to the baseline speculative decoding method.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The method of this paper is well-theorized and the empirical results are good to see.

- This paper trains an acceptance prediction head on top of the draft model to predict the conditional acceptance probability of the candidate tokens, which is a novel idea.

### Weaknesses

#### Some Related Works


#### comment

 - The training cost of this method seems too expensive. This method requires training an acceptance prediction head on top of the draft model, which requires a large training dataset and a lot of training time. This training cost is too high and makes the method less practical. It is recommended to provide a detailed training cost analysis of the acceptance prediction head, including the required dataset size, training time, and hardware resources, and compare it with other methods.

- The generalization ability of the acceptance prediction head is unclear. This paper trains the acceptance prediction head on one dataset and evaluates it on different datasets, and the results show that the method performs well. However, the generalization ability of the acceptance prediction head is unclear. It is recommended to evaluate the generalization of the acceptance prediction head across more diverse datasets and tasks to verify its robustness.

- The evaluation of this paper is not comprehensive enough. This paper only compares the proposed method with the baseline speculative decoding method. However, there are many other methods to improve the efficiency of large language models, such as quantification, distillation, and compression. The method of this paper can be combined with these methods to achieve greater acceleration. It is recommended to compare the proposed method with more methods to improve the efficiency of large language models and explore the combination of the proposed method with other methods.

### Suggestions

The paper introduces an interesting approach to adaptive candidate length selection in speculative decoding by formulating it as a Markov Decision Process (MDP) and training an acceptance prediction head. However, the practical applicability of the method is limited by the high training cost of the acceptance prediction head. To address this, the authors should provide a detailed breakdown of the training process, including the specific dataset size required, the training time on different hardware configurations, and the computational resources needed. A comparison with the training costs of alternative methods for improving decoding efficiency, such as knowledge distillation or model compression, would also be beneficial. Furthermore, the paper should explore techniques to reduce the training cost of the acceptance prediction head, such as using smaller training datasets, employing more efficient training algorithms, or leveraging transfer learning from other tasks. This would make the proposed method more accessible and practical for real-world applications.

To further strengthen the paper, a more thorough investigation of the generalization capabilities of the acceptance prediction head is necessary. While the paper demonstrates results on a few datasets, it is crucial to evaluate the model's performance across a wider range of tasks and data distributions. This should include datasets with varying characteristics, such as different domains, writing styles, and complexities. For example, the model could be trained on a general-purpose dataset and evaluated on specialized datasets like code, medical text, or legal documents. This would provide a more comprehensive understanding of the model's robustness and its ability to adapt to different scenarios. Additionally, the paper should analyze the performance of the acceptance prediction head under different levels of distribution shift between training and evaluation data, which would provide insights into the model's sensitivity to changes in the input data distribution.

Finally, the evaluation of the proposed method should be expanded to include comparisons with other state-of-the-art techniques for improving the efficiency of large language models. This should include methods such as quantization, pruning, and knowledge distillation, which are commonly used to reduce the computational cost of large language models. The paper should also explore the potential for combining the proposed method with these techniques to achieve even greater acceleration. For example, the acceptance prediction head could be used in conjunction with a quantized or pruned model to further reduce the inference time. A comprehensive evaluation of the proposed method in conjunction with other efficiency techniques would provide a more complete picture of its potential and limitations.

### Questions

- How does the acceptance prediction head perform on other models, such as Qwen2.5-7B or other models? Is the acceptance prediction head only applicable to Llama3 models?

- How does the acceptance prediction head perform on tasks other than text completion, such as question answering and code generation?

### Rating

6

### Confidence

3

**********
