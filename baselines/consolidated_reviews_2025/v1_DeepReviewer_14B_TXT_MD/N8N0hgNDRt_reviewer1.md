### Summary

This paper proposes a new finetuned language model called MetaMath, which specializes in mathematical reasoning. MetaMath starts with bootstrapping mathematical questions by rewriting the question from multiple perspectives, resulting in a new dataset called MetaMathQA. Then, the LLaMA-2 models are finetuned on MetaMathQA. MetaMath outperforms a suite of open-source LLMs on two popular benchmarks (GSM8K and MATH) for mathematical reasoning.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. MetaMath is finetuned from state-of-the-art open-source LLMs (e.g., LLaMA-2), showing excellent elementary mathematical problem-solving capability. 
2. The MetaMathQA dataset is constructed in a novel way, rewriting questions with both forward and backward reasoning paths and also leveraging LLMs to rephrase the question text.
3. MetaMath outperforms existing open-source LLMs by a large margin on two standard mathematical reasoning benchmarks: GSM8K and MATH.

### Weaknesses

#### Some Related Works


#### comment

1. The paper only reports results on GSM8K and MATH, which may not be sufficient to evaluate the overall performance of MetaMath on mathematical reasoning. More benchmarks should be used to demonstrate the effectiveness of MetaMath, such as MMLU (especially college-level subjects like college algebra), GSM-Hard, and others. The lack of evaluation on diverse mathematical datasets limits the generalizability claims of the proposed method. Specifically, the paper should include benchmarks that test different aspects of mathematical reasoning, such as algebra, geometry, and calculus, to provide a more comprehensive evaluation.
2. The effectiveness of MetaMathQA is not well studied. Although the paper conducts experiments on the effect of augmentations, it is unknown whether the improvement of MetaMath over LLaMA-2 is solely due to the increased data amount. The paper should include a control experiment where LLaMA-2 is trained on an equivalent amount of randomly sampled data from MetaMathQA to isolate the effect of the data augmentation strategy. Furthermore, the paper should analyze the quality of the generated questions in MetaMathQA, for example, by evaluating the difficulty and diversity of the generated questions compared to the original questions.
3. The paper does not discuss the potential limitations or broader impacts of MetaMath, such as the potential for misuse or the ethical implications of using such a model. The paper should include a discussion of the potential risks associated with the model, such as the generation of incorrect or misleading solutions, and the potential for the model to be used for unethical purposes. The paper should also discuss the limitations of the model, such as its inability to solve certain types of mathematical problems.
4. The paper does not compare MetaMath with other closed-source models like GPT-4, which may be a concern for the readers to evaluate the performance of MetaMath. While comparing with closed-source models is difficult, the paper should at least provide a discussion of the expected performance of MetaMath relative to these models, based on the available benchmarks and the model's architecture. This would help the readers to understand the relative strengths and weaknesses of MetaMath.
5. The paper does not provide any qualitative analysis of the model's predictions, such as examples of the model's successes and failures. The paper should include a detailed analysis of the model's predictions, including examples of both correct and incorrect solutions, and an analysis of the types of errors that the model makes. This would provide valuable insights into the model's strengths and weaknesses, and would help to identify areas for future improvement.

### Suggestions

The paper should significantly expand its evaluation to include a wider range of mathematical benchmarks, beyond just GSM8K and MATH. Specifically, the authors should consider including benchmarks that cover different areas of mathematics, such as algebra, geometry, and calculus, to provide a more comprehensive assessment of the model's capabilities. For example, the MMLU benchmark, particularly the college-level subjects, would be a valuable addition to the evaluation. Furthermore, the authors should also consider including more challenging benchmarks like GSM-Hard, which contains more complex problems that require deeper reasoning. This would help to demonstrate the model's ability to handle more difficult mathematical problems. The evaluation should also include an analysis of the model's performance on different types of problems, such as word problems, equation solving, and proof problems, to provide a more detailed understanding of the model's strengths and weaknesses. This expanded evaluation would provide a more robust assessment of the model's generalizability and its ability to handle diverse mathematical reasoning tasks.

To better understand the effectiveness of the MetaMathQA dataset, the authors should conduct more rigorous ablation studies. Specifically, they should train LLaMA-2 on an equivalent amount of randomly sampled data from MetaMathQA, as well as on the original training data, to isolate the effect of the data augmentation strategy. This would help to determine whether the improvement of MetaMath over LLaMA-2 is solely due to the increased data amount or the specific augmentation techniques used. Furthermore, the authors should analyze the quality of the generated questions in MetaMathQA, for example, by evaluating the difficulty and diversity of the generated questions compared to the original questions. This could be done by using metrics such as the average number of reasoning steps required to solve the problem, or by using a diversity metric to measure the range of different question types. The authors should also provide a qualitative analysis of the generated questions, by examining examples of the generated questions and comparing them to the original questions. This would provide a more detailed understanding of the quality of the generated questions and the effectiveness of the data augmentation strategy.

Finally, the paper should include a more detailed discussion of the limitations and potential broader impacts of MetaMath. The authors should discuss the potential risks associated with the model, such as the generation of incorrect or misleading solutions, and the potential for the model to be used for unethical purposes. For example, the paper should discuss the potential for the model to be used to generate incorrect solutions to mathematical problems, which could lead to incorrect conclusions or decisions. The authors should also discuss the limitations of the model, such as its inability to solve certain types of mathematical problems. Furthermore, the paper should include a qualitative analysis of the model's predictions, such as examples of the model's successes and failures. This would provide valuable insights into the model's strengths and weaknesses, and would help to identify areas for future improvement. The authors should also discuss the potential for misuse of the model, such as using it to automate the solution of mathematical problems without understanding the underlying concepts. This discussion would help to ensure that the model is used responsibly and ethically.

### Questions

Please see the Weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
