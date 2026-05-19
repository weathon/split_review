### Summary

The paper introduces SpecDec++, an enhanced version of speculative decoding that adaptively determines the candidate length on the fly. The authors formulate the choice of candidate length as a Markov Decision Process and theoretically show that the optimal policy takes the form of a threshold policy. They implement SpecDec++ and apply it to the llama-2-chat 7B & 70B model pair. Their adaptive method achieves a 2.04x speedup on the Alpaca dataset, an additional 7.2% improvement over the baseline speculative decoding. On the GSM8K and HumanEval datasets, their method achieves a 2.26x and 2.23x speedup, respectively.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The authors formulate the choice of candidate length as a Markov Decision Process and theoretically show that the optimal policy takes the form of a threshold policy. This provides a theoretical foundation for their method.
2. The authors implement SpecDec++ and apply it to the llama-2-chat 7B & 70B model pair. Their adaptive method achieves a 2.04x speedup on the Alpaca dataset, an additional 7.2% improvement over the baseline speculative decoding. On the GSM8K and HumanEval datasets, their method achieves a 2.26x and 2.23x speedup, respectively.
3. The authors train an acceptance prediction head on top of the draft model to predict the conditional acceptance probability of the candidate tokens. This allows them to stop the current speculation when the predicted probability that at least one token gets rejected exceeds a threshold.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only evaluate their method on three datasets: Alpaca, HumanEval, and GSM8K. It is unclear how well their method would generalize to other datasets and tasks. Specifically, the datasets used are primarily focused on text generation and mathematical reasoning. The paper lacks evaluation on tasks that require different types of reasoning, such as commonsense reasoning or tasks involving more complex multi-turn interactions. This limited scope makes it difficult to assess the robustness of the proposed method across a broader range of language model applications.
2. The authors only use llama-2-chat models in their experiments. It is unclear how well their method would generalize to other model architectures and sizes. The experiments are limited to a single model family, and it is not clear if the observed speedups would hold for other model architectures, such as those based on different transformer variants or models trained with different objectives. Furthermore, the paper does not explore the impact of model size on the effectiveness of SpecDec++, which is a crucial factor in practical applications.
3. The authors mention that there will be distribution shifts between the training and inference process, which may cause certain biases in the prediction head. However, they do not provide any empirical results to quantify the impact of these distribution shifts on their method's performance. The paper lacks a detailed analysis of how the acceptance prediction head performs under different degrees of distribution shift. It is important to understand the sensitivity of the method to such shifts, as real-world applications often involve significant changes in the input distribution.

### Suggestions

To address the limited evaluation scope, the authors should include a more diverse set of benchmarks that cover a wider range of tasks and reasoning types. This should include datasets that evaluate commonsense reasoning, natural language understanding, and tasks that involve multi-turn interactions. For example, incorporating datasets like Winograd Schema Challenge for coreference resolution, or tasks from the GLUE benchmark, would provide a more comprehensive evaluation of the method's generalization capabilities. Furthermore, the authors should consider evaluating their method on tasks that require different types of reasoning, such as logical reasoning or abductive reasoning, to assess its robustness across various cognitive tasks. This would provide a more complete picture of the method's strengths and weaknesses and its applicability to different real-world scenarios.

To address the lack of model diversity, the authors should conduct experiments using different model architectures and sizes. This should include models from different families, such as models based on different transformer variants, or models trained with different objectives. For example, evaluating SpecDec++ on models like the Falcon or Mistral models would provide insights into its generalization across different model families. Additionally, the authors should explore the impact of model size on the effectiveness of SpecDec++. This could involve evaluating the method on models of varying sizes within the same family, or on models with different architectural configurations. This would help to determine the optimal model size for SpecDec++ and its scalability to larger models. Such experiments would also help to identify any architectural biases that might affect the performance of the method.

Finally, to address the issue of distribution shifts, the authors should conduct a more detailed analysis of the impact of these shifts on the acceptance prediction head. This should include experiments where the training and inference data are drawn from different distributions, and the performance of the prediction head is evaluated under these conditions. For example, the authors could train the prediction head on one dataset and evaluate it on another dataset with a different distribution. This would help to quantify the sensitivity of the method to distribution shifts and identify potential biases in the prediction head. Furthermore, the authors should explore techniques to mitigate the impact of distribution shifts, such as domain adaptation or adversarial training. This would help to improve the robustness of the method in real-world applications where distribution shifts are common.

### Questions

1. How does SpecDec++ perform on other model architectures and sizes?
2. How does SpecDec++ perform on other datasets and tasks?
3. How does SpecDec++ perform under different degrees of distribution shifts between the training and inference process?
4. What is the computational overhead of training and using the acceptance prediction head?

### Rating

6

### Confidence

3

**********
