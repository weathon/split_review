### Summary

The paper introduces a novel method called Probability Distribution Estimation (PDE) to address the challenge of machine-generated text detection, especially in the context of proprietary large language models (LLMs). The method estimates full probability distributions from partial observations, enabling the application of white-box detection methods to proprietary models. The authors demonstrate that PDE can extend the capabilities of existing detection methods and achieve high accuracy in detecting machine-generated text.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper presents a creative solution to a significant problem in the field of machine-generated text detection. The authors propose a method that bridges the gap between white-box and black-box detection methods, allowing for the use of advanced proprietary LLMs in scenarios where full model access is not available. The research is of high quality, with thorough experiments and robust validation. The results are compelling and have important implications for the development of trustworthy AI systems. The paper is well-written and clearly structured, making it easy to follow the methodology and results. The significance of the work is evident, as it addresses a pressing issue in the age of increasingly sophisticated LLMs.

### Weaknesses

#### Some Related Works


#### comment

The paper could benefit from a more detailed discussion of the limitations of the PDE method. While the authors mention some constraints, a deeper analysis of potential failure cases and the sensitivity of the method to various parameters would be valuable. Specifically, the paper lacks a thorough investigation into how the choice of K, the number of top probabilities used for estimation, impacts the accuracy and robustness of the method. Different values of K might lead to significantly different estimation quality, and this sensitivity should be explored with respect to different models and datasets. Additionally, the paper could explore the potential for adversarial attacks on the PDE method and how these might be mitigated. It would be beneficial to see an analysis of how small perturbations in the input text or in the estimated probability distribution could affect the detection performance. Furthermore, the computational cost associated with the PDE method, especially when applied to large-scale models, should be discussed in more detail. The paper should provide a more granular breakdown of the time and resources required for each step of the method, including the API calls, local processing, and any overhead.

### Suggestions

To enhance the paper, the authors should conduct a more rigorous analysis of the PDE method's sensitivity to the parameter K, the number of top probabilities used for estimation. This analysis should include experiments across a range of K values, and should evaluate the impact on detection accuracy for different models and datasets. The authors should also investigate the trade-offs between computational cost and detection performance as K varies. For instance, a smaller K might lead to faster computation but potentially lower accuracy, while a larger K might improve accuracy but increase computational overhead. This analysis should be presented with clear visualizations, such as plots of detection accuracy versus K, and should include a discussion of the optimal K values for different scenarios. Furthermore, the authors should explore the potential for adversarial attacks on the PDE method. This could involve examining how small perturbations in the input text or in the estimated probability distribution affect the detection performance. The authors could investigate different types of adversarial attacks, such as adding noise to the input text or manipulating the estimated probabilities, and should discuss potential mitigation strategies. This analysis would provide a more complete understanding of the method's robustness and its limitations in real-world scenarios. Finally, the authors should provide a more detailed breakdown of the computational cost associated with the PDE method. This should include a granular analysis of the time and resources required for each step of the method, such as the API calls to the proprietary models, the local processing of the estimated distributions, and any overhead. The authors should also compare the computational cost of the PDE method with other detection methods, and should discuss the scalability of the method to large-scale datasets and models. This analysis should be presented with clear metrics, such as the average time per text sample and the memory usage, and should include a discussion of the practical implications of the computational cost.

### Questions

1、The paper mentions that the PDE method is the first to investigate white-box detection methods on proprietary models. Can the authors provide more details on the specific challenges they faced in this investigation and how they overcame them? 
2、The authors claim that the latest LLMs can effectively detect their own outputs. Has there been any observation of potential biases in this self-detection process? For example, are there certain types of text that are more likely to be misclassified? 
3、The paper discusses the use of different distributions for estimation, such as Geometric and MLP distributions. Can the authors provide more details on how they chose these distributions and whether other distributions were considered? 
4、The authors mention that the PDE method can be applied to various white-box detection methods. Can they provide more details on the specific requirements for applying the method to different detection techniques? 
5、The paper presents a comparison of the PDE method with other detection methods in terms of accuracy, speed, and cost. Can the authors provide more details on the specific experimental setup used for this comparison, including the datasets, models, and evaluation metrics?

### Rating

6

### Confidence

3

**********
