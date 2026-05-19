### Summary

The paper introduces a contrastive decoding approach to reducing hallucinations in LLMs. The proposed approach attempts to mitigate hallucinations by exploiting the difference in predictions from the LLM for masked and unmasked prompts. Specifically, the proposed contrastive decoding approach computes the difference between the logits of the LLM prediction for the unmasked prompt and a similar but corrupted (masked) prompt, to obtain a corrected distribution over the output tokens. The proposed approach is evaluated on a number of question-answering benchmarks, where the main improvements are observed for datasets with context.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The proposed approach is simple and intuitive, and does not require additional training or fine-tuning to mitigate hallucinations. 
2. The paper is well-written and easy to understand.
3. The proposed approach seems to be effective for context-rich QA datasets, demonstrating the potential of the proposed approach in mitigating hallucinations.

### Weaknesses

#### Some Related Works

[1] Contrastive Decoding
[2] Visual Contrastive Decoding: Mitigating Object Hallucinations in Large Vision-Language Models

#### comment

1. The proposed approach is similar to contrastive decoding [1, 2], where the core idea is to subtract the logits of an incorrect (corrupted) prediction from the correct prediction to obtain a corrected distribution over the output tokens. While the application of this idea to masking portions of the input text is novel, the paper does not adequately differentiate the proposed method from existing contrastive decoding techniques, nor does it provide a clear explanation of why masking was chosen as the method for corrupting the input text. The paper should explore and justify the choice of masking over other methods of corrupting the input, such as adding Gaussian noise or other types of perturbations.
2. The paper lacks crucial details on how the adaptive plausibility constraint (APC) is applied. The description of APC is vague, and it is unclear how the threshold $\beta$ is determined and how it affects the final results. The paper should provide a more detailed explanation of the implementation of APC, including the specific criteria used to determine plausible sequences and how this affects the decoding process.
3. The paper does not provide an ablation study on the effect of the hyperparameters $r_{mask}$, $\alpha$, and $\beta$. The lack of ablation studies makes it difficult to assess the robustness of the proposed approach and the sensitivity of the results to the choice of hyperparameters. The paper should include a comprehensive ablation study to demonstrate the impact of each hyperparameter on the performance of the proposed method.
4. The paper does not provide an evaluation of the proposed approach on recent LLMs, such as Llama 4 and Gemma. The evaluation should be extended to include more recent models to demonstrate the generalizability of the proposed approach across different architectures and model sizes.
5. The paper does not provide an evaluation of the proposed approach on tasks that do not involve question-answering. The evaluation should be extended to include other tasks, such as summarization or text generation, to demonstrate the generalizability of the proposed approach across different NLP tasks.

### Suggestions

The paper should provide a more thorough justification for the choice of masking as the method for corrupting the input text. While masking is a simple and intuitive approach, the paper should explore and compare it with other methods of corrupting the input, such as adding Gaussian noise, or other types of perturbations. A comparative analysis of different corruption methods would strengthen the paper's claims and provide a more comprehensive understanding of the proposed approach. The paper should also discuss the potential limitations of masking, such as the possibility of introducing bias or artifacts in the corrupted input, and how these limitations might affect the performance of the proposed method. Furthermore, the paper should provide a more detailed explanation of the adaptive plausibility constraint (APC), including the specific criteria used to determine plausible sequences and how this affects the decoding process. The current description of APC is too vague, and it is difficult to understand how it is implemented and how it contributes to the overall performance of the proposed method. The paper should also include a more detailed explanation of how the threshold $\beta$ is determined and how it affects the final results. A more detailed explanation of the APC would help to clarify the proposed method and make it easier to reproduce.

The paper should include a comprehensive ablation study to demonstrate the impact of each hyperparameter on the performance of the proposed method. The ablation study should systematically vary the values of $r_{mask}$, $\alpha$, and $\beta$, and evaluate the performance of the proposed method on a range of datasets. The results of the ablation study should be presented in a clear and concise manner, with appropriate visualizations to illustrate the impact of each hyperparameter. The paper should also discuss the optimal values for each hyperparameter and how these values might vary across different datasets and tasks. The paper should also extend the evaluation of the proposed approach to include more recent LLMs, such as Llama 4 and Gemma. This would demonstrate the generalizability of the proposed approach across different architectures and model sizes. The evaluation should also include a comparison of the proposed approach with other existing methods for mitigating hallucinations in LLMs. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed approach and its position relative to other state-of-the-art methods. The paper should also extend the evaluation of the proposed approach to include other NLP tasks, such as summarization or text generation. This would demonstrate the generalizability of the proposed approach across different NLP tasks and its potential for broader applications.

Finally, the paper should address the computational overhead of the proposed approach. The paper should provide a detailed analysis of the computational cost of the proposed method, including the time and memory requirements. The paper should also compare the computational cost of the proposed method with other existing methods for mitigating hallucinations in LLMs. This would provide a more comprehensive understanding of the practical implications of the proposed approach and its suitability for different applications. The paper should also discuss the potential limitations of the proposed approach, such as the possibility of introducing bias or artifacts in the corrected distribution over the output tokens, and how these limitations might affect the performance of the proposed method. A more thorough discussion of the limitations of the proposed approach would help to provide a more balanced and realistic assessment of its potential impact.

### Questions

1. How is the adaptive plausibility constraint applied? The details are lacking in the paper.
2. What is the effect of the hyperparameters $r_{mask}$, $\alpha$, and $\beta$?
3. How does the proposed approach perform on recent LLMs, such as Llama 4 and Gemma?
4. How does the proposed approach perform on tasks that do not involve question-answering?
5. What is the overhead of the proposed approach?

### Rating

3

### Confidence

4

**********
