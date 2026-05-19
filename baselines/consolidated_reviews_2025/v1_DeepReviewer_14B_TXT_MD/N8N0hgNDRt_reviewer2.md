### Summary

The paper proposes a finetuned language model MetaMath that specializes in mathematical reasoning. The authors bootstrap mathematical questions by rewriting the question from multiple perspectives, which results in a new dataset called MetaMathQA. Then they finetune the LLaMA-2 models on MetaMathQA. Experimental results on two popular benchmarks (GSM8K and MATH) for mathematical reasoning demonstrate that MetaMath outperforms a suite of open-source LLMs by a significant margin.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The authors release the MetaMathQA dataset, the MetaMath models with different model sizes and the training code for public use.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should compare with more methods, such as distillation from GPT-4. The current comparison is limited to open-source models, and it's unclear how MetaMath would perform against state-of-the-art closed-source models. Specifically, the paper lacks a comparison with models distilled from GPT-4, which have shown strong performance in various reasoning tasks. This is a significant gap, as it leaves the reader unsure of the true performance ceiling of the proposed method.
2. The authors should conduct experiments on more datasets, such as MMLU. The evaluation is currently limited to GSM8K and MATH, which are primarily focused on mathematical reasoning. While these are important benchmarks, they do not fully capture the generalizability of the model to other types of reasoning tasks. The inclusion of datasets like MMLU, which covers a broader range of topics and reasoning skills, would provide a more comprehensive evaluation.

### Suggestions

The paper would benefit significantly from a more thorough comparison with state-of-the-art models, particularly those distilled from GPT-4. The current evaluation only compares against open-source models, which may not be the most competitive baselines. To address this, the authors should include a comparison with models that have been distilled from GPT-4, such as those available through the Hugging Face model hub. This would provide a clearer understanding of the performance of MetaMath relative to the current state-of-the-art in large language models. Furthermore, the authors should explore different distillation techniques, such as knowledge distillation and data distillation, to see if they can further improve the performance of MetaMath. This would not only provide a more comprehensive comparison but also potentially lead to further improvements in the model's performance.

In addition to expanding the comparison with state-of-the-art models, the authors should also broaden the scope of their evaluation by including more diverse datasets. While GSM8K and MATH are important benchmarks for mathematical reasoning, they do not fully capture the generalizability of the model to other types of reasoning tasks. The inclusion of datasets like MMLU, which covers a broader range of topics and reasoning skills, would provide a more comprehensive evaluation. Specifically, the authors should consider including subsets of MMLU that are relevant to mathematical and logical reasoning, such as the college algebra and calculus sections. This would help to determine if the improvements observed on GSM8K and MATH generalize to other types of reasoning tasks. Furthermore, the authors should consider evaluating the model on datasets that test different types of mathematical reasoning, such as proof verification or mathematical programming.

Finally, the authors should provide a more detailed analysis of the types of errors that MetaMath makes. While the overall performance is impressive, it is important to understand the limitations of the model. For example, are there specific types of mathematical problems that the model struggles with? Are there specific types of reasoning steps that the model has difficulty with? A detailed error analysis would help to identify areas where the model could be improved. This analysis should include examples of both successful and unsuccessful reasoning chains, highlighting the specific steps where the model succeeds or fails. This would provide valuable insights into the strengths and weaknesses of the model and guide future research.

### Questions

1. What is the performance of MetaMath on MMLU?
2. What is the performance of MetaMath compared with distillation from GPT-4?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
