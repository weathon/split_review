### Summary

This paper proposes a tool-use framework for large language models (LLMs) that consists of three main components: a data construction pipeline, a model training phase, and an evaluation tool. The data construction pipeline generates a dataset of tool-use instructions and corresponding API calls using ChatGPT. The model training phase fine-tunes an LLM on this dataset, incorporating a Depth-First Search-based decision tree (DFSDT) algorithm to improve the model's reasoning and planning capabilities. The evaluation tool, ToolEval, assesses the tool-use performance of LLMs using metrics such as pass rate and win rate. The experiments demonstrate that the fine-tuned LLaMA model, ToolLLaMA, achieves competitive performance with GPT-4, particularly in single-tool and multi-tool instructions, and exhibits strong generalization to unseen APIs. ToolLLaMA also introduces a novel API retriever that significantly enhances the efficiency and accuracy of API selection.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper introduces a comprehensive framework for enhancing tool-use capabilities in large language models (LLMs). The framework addresses a critical gap in current research and practical applications by providing a systematic approach to improving LLMs' ability to interact with external tools and APIs.

2. The proposed framework consists of three key components: a data construction pipeline, a model training phase, and an evaluation tool. The data construction pipeline leverages ChatGPT to generate a diverse set of tool-use instructions and corresponding API calls, which is a novel approach to creating a large-scale dataset for tool-use tasks. The model training phase fine-tunes an LLM on this dataset, incorporating a Depth-First Search-based decision tree (DFSDT) algorithm to improve the model's reasoning and planning capabilities. The evaluation tool, ToolEval, provides a robust and automated way to assess the tool-use performance of LLMs, reducing the need for manual annotation. These components work together to create a comprehensive and effective framework for enhancing tool-use capabilities in LLMs.

3. The paper presents a novel Depth-First Search-based decision tree (DFSDT) algorithm to improve the reasoning and planning capabilities of LLMs. This algorithm allows the model to explore multiple reasoning paths and expand the search space, leading to better performance in complex instructions. The use of DFSDT is a significant contribution to the field, as it addresses the limitations of existing methods such as Chain-of-Thought (CoT) and ReAct, which often struggle with complex instructions.

4. The paper demonstrates the effectiveness of the proposed framework through extensive experiments. The fine-tuned LLaMA model, ToolLLaMA, achieves competitive performance with GPT-4, particularly in single-tool and multi-tool instructions. The model also exhibits strong generalization to unseen APIs, indicating its robustness and adaptability. The introduction of a novel API retriever that significantly enhances the efficiency and accuracy of API selection further demonstrates the practical value of the framework. These results provide strong evidence for the effectiveness of the proposed approach and its potential for real-world applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost associated with the proposed framework. While the paper mentions the use of a Depth-First Search-based decision tree (DFSDT) algorithm, it does not discuss the computational resources required for training and inference, which is an important factor for practical applications. Specifically, the paper lacks details on the memory footprint of the model, the time required for training the model, and the inference time for different numbers of tools. This information is crucial for understanding the feasibility of deploying the framework in resource-constrained environments.

2. The paper does not provide a detailed comparison of the proposed framework with other existing tool-use frameworks. While the paper mentions that the proposed framework achieves competitive performance with GPT-4, it does not provide a comprehensive comparison with other state-of-the-art tool-use frameworks. This makes it difficult to assess the relative strengths and weaknesses of the proposed approach. For example, the paper does not compare the performance of the proposed framework with other methods that use different approaches for tool selection and invocation. A more detailed comparison would help to better understand the advantages and limitations of the proposed framework.

3. The paper does not provide a detailed analysis of the limitations of the proposed framework. While the paper demonstrates the effectiveness of the proposed framework on a set of benchmark tasks, it does not discuss the potential limitations of the approach. For example, the paper does not discuss the limitations of the DFSDT algorithm, such as its potential for overfitting or its sensitivity to the choice of hyperparameters. A more detailed analysis of the limitations of the proposed framework would help to identify areas for future research and improvement.

### Suggestions

The paper would benefit from a more thorough analysis of the computational cost associated with the proposed framework. The authors should provide a detailed breakdown of the computational resources required for training and inference, including the memory footprint of the model, the time required for training, and the inference time for different numbers of tools. This analysis should also include a discussion of the scalability of the framework, including how the computational cost scales with the size of the dataset and the complexity of the instructions. Furthermore, the authors should provide a comparison of the computational cost of the proposed framework with other existing tool-use frameworks. This would help to better understand the trade-offs between performance and computational cost. For example, the authors could compare the training time and inference time of the proposed framework with other methods that use different approaches for tool selection and invocation. This would provide a more complete picture of the practical feasibility of the proposed framework.

To better assess the relative strengths and weaknesses of the proposed framework, the authors should provide a more detailed comparison with other state-of-the-art tool-use frameworks. This comparison should include a discussion of the performance of the proposed framework on a variety of benchmark tasks, as well as a comparison of the performance of the proposed framework with other methods that use different approaches for tool selection and invocation. The authors should also discuss the limitations of the proposed framework, such as the potential for overfitting or the sensitivity to the choice of hyperparameters. A more detailed analysis of the limitations of the proposed framework would help to identify areas for future research and improvement. For example, the authors could discuss the limitations of the DFSDT algorithm, such as its potential for overfitting or its sensitivity to the choice of hyperparameters. This would help to better understand the limitations of the proposed approach and identify areas for future research.

Finally, the authors should provide a more detailed analysis of the error cases of the fine-tuned model. This analysis should go beyond simply stating that the model fails to solve certain tasks and should delve into the specific reasons why the model fails. This could include an analysis of the types of instructions that are difficult for the model to handle or the types of APIs that are not well-suited for the model. The authors should also discuss the potential avenues for future research to address these limitations. For example, the authors could discuss the potential for using techniques such as data augmentation or curriculum learning to improve the model's performance. This would help to better understand the limitations of the proposed approach and identify areas for future research.

### Questions

1. What are the computational costs associated with the proposed framework? How does the computational cost scale with the size of the dataset and the complexity of the instructions?

2. How does the proposed framework compare with other existing tool-use frameworks in terms of performance, efficiency, and robustness? What are the specific advantages and disadvantages of the proposed approach compared to other methods?

3. What are the limitations of the proposed framework? Are there any specific types of instructions or APIs that are difficult for the model to handle? What are the potential avenues for future research to address these limitations?

### Rating

8: accept, good paper

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
