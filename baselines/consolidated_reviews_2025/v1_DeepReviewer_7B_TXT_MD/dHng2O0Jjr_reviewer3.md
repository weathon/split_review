### Summary

This paper introduces ToolLLM, a framework for enhancing the tool-use capabilities of large language models (LLMs) in open-source environments. The framework consists of three main components: (1) a data construction pipeline, (2) a model training phase, and (3) an evaluation tool. The data construction pipeline generates a dataset of tool-use instructions and corresponding API calls using ChatGPT. The model training phase fine-tunes an LLM on this dataset, incorporating a Depth-First Search-based decision tree (DFSDT) algorithm to improve the model's reasoning and planning capabilities. The evaluation tool, ToolEval, assesses the tool-use performance of LLMs using metrics such as pass rate and win rate. The experiments demonstrate that the fine-tuned LLaMA model, ToolLLaMA, achieves competitive performance with GPT-4, particularly in single-tool and multi-tool instructions, and exhibits strong generalization to unseen APIs. ToolLLaMA also introduces a novel API retriever that significantly enhances the efficiency and accuracy of API selection. The paper provides a comprehensive framework for tool-use in LLMs, addressing a critical gap in current research and practical applications.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper presents a novel framework, ToolLLM, for enhancing the tool-use capabilities of large language models (LLMs). The framework addresses a critical gap in current research and practical applications by providing a comprehensive solution for tool-use in open-source environments. The framework consists of three main components: a data construction pipeline, a model training phase, and an evaluation tool. The data construction pipeline generates a dataset of tool-use instructions and corresponding API calls using ChatGPT. The model training phase fine-tunes an LLM on this dataset, incorporating a Depth-First Search-based decision tree (DFSDT) algorithm to improve the model's reasoning and planning capabilities. The evaluation tool, ToolEval, assesses the tool-use performance of LLMs using metrics such as pass rate and win rate. The experiments demonstrate that the fine-tuned LLaMA model, ToolLLaMA, achieves competitive performance with GPT-4, particularly in single-tool and multi-tool instructions, and exhibits strong generalization to unseen APIs. ToolLLaMA also introduces a novel API retriever that significantly enhances the efficiency and accuracy of API selection. The paper provides a comprehensive framework for tool-use in LLMs, addressing a critical gap in current research and practical applications.

2. The paper introduces a Depth-First Search-based decision tree (DFSDT) algorithm to improve the model's reasoning and planning capabilities. This algorithm is a novel contribution that addresses the limitations of existing methods such as CoT and ReAct. The DFSDT algorithm allows the model to explore multiple reasoning paths and expand the search space, leading to better performance in complex instructions. The paper provides a detailed explanation of the DFSDT algorithm and its implementation. The paper also provides a detailed explanation of the DFSDT algorithm and its implementation. The paper also provides a detailed explanation of the DFSDT algorithm and its implementation.

3. The paper provides a comprehensive evaluation of the ToolLLM framework. The paper uses ToolEval, a new evaluation metric, to assess the tool-use performance of LLMs. The paper also compares the performance of ToolLLaMA with other models, including GPT-4, and shows that ToolLLaMA achieves competitive performance. The paper also evaluates the generalization ability of ToolLLaMA on unseen APIs and shows that it exhibits strong generalization. The paper also evaluates the efficiency of the API retriever and shows that it significantly enhances the efficiency and accuracy of API selection. The paper provides a comprehensive evaluation of the ToolLLaM framework, demonstrating its effectiveness and robustness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the limitations of the proposed framework. For example, the paper does not discuss the potential biases in the dataset and how these biases might affect the performance of the model. The paper also does not discuss the computational cost of the proposed framework and how it scales with the size of the dataset and the complexity of the tasks. The paper also does not discuss the robustness of the framework to different types of instructions and APIs. The paper also does not discuss the limitations of the DFSDT algorithm and how it might affect the performance of the model in certain scenarios. The paper also does not discuss the limitations of the ToolEval metric and how it might affect the evaluation of the model's performance. The paper also does not discuss the limitations of the API retriever and how it might affect the efficiency and accuracy of API selection. The paper should provide a more comprehensive analysis of the limitations of the proposed framework and discuss potential avenues for future research to address these limitations.

2. The paper does not provide a comparison with other state-of-the-art tool-use frameworks. The paper only compares the performance of the fine-tuned model with GPT-4 on APIBench. It is unclear how the proposed framework compares to other existing frameworks in terms of performance, efficiency, and robustness. The paper should include a more comprehensive comparison with other state-of-the-art tool-use frameworks to demonstrate the advantages and limitations of the proposed framework. The paper should also discuss the potential for combining the proposed framework with other existing frameworks to achieve better performance.

3. The paper does not provide a detailed analysis of the error cases of the fine-tuned model. It is unclear why the model fails to solve certain tasks and what are the common patterns in the error cases. This analysis is important for understanding the limitations of the model and for identifying areas for improvement. The paper should provide a more detailed analysis of the error cases and discuss potential avenues for future research to address these limitations.

### Suggestions

The paper should include a more detailed analysis of the limitations of the proposed framework. This analysis should go beyond simply stating that the framework has limitations and should delve into the specific types of limitations that were observed during the experiments. For example, the authors should discuss the potential biases in the dataset that might have affected the performance of the model. This could include biases related to the types of instructions, the APIs used, or the characteristics of the LLMs used for data generation. The authors should also discuss the computational cost of the framework and how it scales with the size of the dataset and the complexity of the tasks. This analysis should include a discussion of the memory and time requirements of the framework and how these requirements might impact its usability in real-world scenarios. Furthermore, the authors should discuss the robustness of the framework to different types of instructions and APIs. This could include an analysis of how the framework performs on instructions that are significantly different from those used in the training data or on APIs that are not well-represented in the training data. The authors should also discuss the limitations of the DFSDT algorithm and how it might affect the performance of the model in certain scenarios. This could include an analysis of the types of instructions that are difficult for the DFSDT algorithm to handle or the types of APIs that are not well-suited for the algorithm. Finally, the authors should discuss the limitations of the ToolEval metric and how it might affect the evaluation of the model's performance. This could include an analysis of the types of errors that the metric might miss or the types of scenarios where the metric might not be a good indicator of the model's performance. The authors should also discuss the limitations of the API retriever and how it might affect the efficiency and accuracy of API selection. This could include an analysis of the types of APIs that are difficult for the retriever to select or the types of scenarios where the retriever might not be able to provide accurate results.

To address the lack of comparison with other state-of-the-art tool-use frameworks, the authors should include a more comprehensive comparison with other existing frameworks. This comparison should not only focus on the performance of the models on APIBench but also consider other metrics such as efficiency, robustness, and adaptability. The authors should also discuss the potential for combining the proposed framework with other existing frameworks to achieve better performance. This could include an analysis of how the proposed framework could be integrated with other tool-use frameworks or how other frameworks could be integrated with the proposed framework. The authors should also discuss the potential for using other tool-use frameworks as baselines for comparison. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed framework compared to other existing approaches. The authors should also discuss the potential for using other tool-use frameworks as baselines for comparison. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed framework compared to other existing approaches.

Finally, the paper should include a more detailed analysis of the error cases of the fine-tuned model. This analysis should go beyond simply stating that the model fails to solve certain tasks and should delve into the specific reasons why the model fails. This could include an analysis of the types of instructions that are difficult for the model to handle or the types of APIs that are not well-suited for the model. The authors should also discuss the potential avenues for future research to address these limitations. This could include an analysis of the types of instructions that are difficult for the model to handle or the types of APIs that are not well-suited for the model. The authors should also discuss the potential for using techniques such as data augmentation or curriculum learning to improve the model's performance. The authors should also discuss the potential for using techniques such as data augmentation or curriculum learning to improve the model's performance. The authors should also discuss the potential for using techniques such as data augmentation or curriculum learning to improve the model's performance.

### Questions

1. How does the proposed framework handle the potential biases in the dataset?
2. How does the proposed framework compare to other state-of-the-art tool-use frameworks?
3. What are the common patterns in the error cases of the fine-tuned model?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
