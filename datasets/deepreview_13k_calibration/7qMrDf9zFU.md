# Priority on High-Quality: Instruction Data Selection for Optimized Instruction Tuning

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
Large Language Models (LLMs) have demonstrated a remarkable understanding of language nuances through instruction tuning, enabling them to effectively tackle various natural language processing tasks. Previous research on instruction tuning mainly focused on the quantity of instruction data. Recent studies indicate that the quality of instruction data is more significant than the quantity of data. Even selecting a small amount of high-quality data can achieve optimal fine-tuning effects. However, existing selection methods have severe limitations in defining the quality of each instruction data and considering the balance between data quality and data diversity. To address these challenges, we propose a strategy that utilizes noise injection to identify the quality of instruction data. We also implement the strategy of combining inter-class diversity and intra-class diversity to improve model performance. Experimental results demonstrate that our method significantly outperforms the model trained on the full dataset when utilizing only 12% of the entire dataset. Our study provides a new perspective on noise injection in the field of instruction tuning, and also illustrates that a high-quality instruction dataset should possess both quality and diversity. Additionally, we have published our selected high-quality instruction data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose a data selection approach using noise injection to assess instruction quality by introducing controlled noise into the input data and measuring the consistency of the model's output distribution. This method identifies high-quality data that aligns with the model’s pre-trained knowledge, allowing for more efficient fine-tuning. Additionally, to prevent over-representation of certain data types, the authors implement inter-class and intra-class diversity strategies using clustering and cosine similarity to ensure a balanced dataset. Their approach demonstrates superior model performance using only 12% of the original dataset, reducing training costs while enhancing model efficiency. As part of their contributions, the authors also publish a high-quality instruction dataset curated through their method, offering a valuable resource for further research in instruction tuning.

### Strengths
- The approach of assessing data quality via noise injection is innovative, presenting a fresh perspective on defining quality in instruction tuning without relying on external scoring models. This originality extends to combining noise-based quality assessment with diversity strategies, addressing a critical gap in current methods that either prioritize quality or diversity but rarely balance both effectively.
- the use of inter-class and intra-class diversity strategies showcases a nuanced understanding of dataset composition and further enhances the quality of the work.
- The explanation of noise injection and consistency measures is detailed and accessible, allowing readers to understand the novel concepts and replicate the approach.

### Weaknesses
 - The paper’s experimental results could be improved with additional baseline comparisons. While the authors compare their method to full-data training, adding comparisons to recent quality and diversity-oriented methods would allow readers to better gauge the benefits and trade-offs of this approach in a broader context.
- The paper solely relies on output distribution consistency following noise injection to define quality, which may overlook other nuanced aspects of instruction quality, such as contextual relevance, instruction clarity, or alignment with specific model objectives. 
- Although the paper introduces inter-class and intra-class diversity strategies, it only uses k-means clustering and cosine similarity to ensure diversity. This limited approach might lead to clusters that fail to represent complex hierarchical or nuanced differences within data types.

### Questions
- The paper’s noise injection approach is innovative, but it lacks an in-depth exploration of the noise parameters. Could you provide more details on how the noise injection parameters, such as the scaling factor β, were selected? Did you experiment with different values, and if so, how did these affect the results?

- The selected high-quality data are determined based on consistency following noise injection, but it would be helpful to understand what specific characteristics these data share. Could you analyze or describe typical examples of the high-consistency data and explain why these instructions align well with model knowledge?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel approach for selecting high-quality instructional data for tuning LLMs. Unlike previous research, which primarily emphasizes the volume of instructional data, this work addresses limitations in defining and balancing the quality and diversity of the data. The authors propose a method that uses noise injection to identify high-quality instructional data, analyzing the pre-trained model’s response to perturbed inputs to measure the consistency of probability distributions. This approach enables a model-centric quality assessment without relying on external scoring models. Additionally, the framework integrates both inter-class and intra-class diversity to ensure comprehensive task coverage and reduce data redundancy. Experimental results demonstrate that the proposed method achieves strong performance on unfiltered datasets across various standard benchmarks.

### Strengths
- This paper is well-written in general and well-motivated.
- The research direction of studying how to select datasets for LLM supervised fine-tuning is of practical importance.
- The proposed data selection pipeline is easy to follow and intuive.
- The experimental results of the proposed data selection pipeline seem to be very promising.

### Weaknesses
 - The paper lacks fundamental explanation and justification for the assumption that low KL divergence after noise perturbation indicates high data quality. It is unclear whether this is purely heuristic or based on a specific hypothesis or experimental observation. Specifically, the paper does not explore the relationship between the magnitude of KL divergence and the actual quality of instruction data, nor does it provide any theoretical analysis to support this assumption. A more rigorous analysis, perhaps involving controlled experiments with varying degrees of noise and corresponding changes in KL divergence, would be beneficial.
- The proposed method seems computationally intensive. For instance, all the perturbed data must pass through the LLM to obtain predictions and calculate KL divergence. The paper does not provide a detailed analysis of the computational cost, such as the time complexity or the required hardware resources. This lack of analysis makes it difficult to assess the practicality of the proposed method, especially for large datasets and models. Furthermore, the paper does not discuss potential optimization strategies to reduce the computational burden.
- There is no comparison between the proposed data selection pipeline and similar methods, e.g., [1]. The paper should include a comparison with existing data selection techniques, particularly those that also focus on selecting high-quality instructional data. This comparison should not only focus on performance but also on computational efficiency and resource requirements. Without such a comparison, it is difficult to assess the novelty and advantages of the proposed method.
- It is unclear whether the dataset selected using one LLM (preferably at a smaller scale, e.g., 7B) can be broadly applied to fine-tune various LLMs. The paper does not provide sufficient evidence to support the generalizability of the selected data across different model architectures and sizes. It is possible that the data selected by a smaller model may not be optimal for a larger model, or vice versa. Further experiments are needed to validate this aspect.

### Questions
- Why is low KL divergence among LLM outputs before and after noise perturbation an indicator of high data quality? Is there any fundamental reason behind it?
- Are there potential methods to accelerate the speed of data selection in the proposed approach?
- Could one use, say, Llama3 7B to select data and then use it for fine-tuning Llama3 405B?
- How does the proposed method compare to the approach presented in https://arxiv.org/abs/2405.00705?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method that utilizes noise injection to identify the quality of instruction data. They also implement the strategy of combining inter-class diversity and intra-class diversity to select instruction data accompanied by the quality identification method. Experimental results demonstrate that the method outperforms some previous methods and outperforms the model trained on the full dataset when utilizing a small percentage of the entire dataset.

### Strengths
1. It is reasonable to use noise inject to judge the quality of instruction data. The authors have explained their insight in the paper, and it is also effective in experiments.
2. The writing is clear and easy to understand.
3. The ablation experiment well demonstrated the roles of consistency and diversity in the method.

### Weaknesses
1. Only one data set is used for the experiment. Using multiple data can illustrate the generality of the method. For example, Mods[1] also uses a larger mixture instruction datasets which is composed of instruction data from several different datasets. 
2. I noticed that the methods cited and compared in this paper are up to 2023, but there are still new methods that have not been compared in related works or experiments, e.g. [2][3].

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a data selection method which could define the quality of each instruction data and considering the balance between
data quality and data diversity. Experiments demonstrate that the proposed method maintain the performance of the whole dataset, and even outperforms the model trained on the full dataset.

### Strengths
1. Novel approach: The proposed method of using noise injection to identify the quality of instruction data is innovative and provides a new perspective in the field of instruction tuning.
2. Performance improvement: Experimental results show that the method significantly outperforms the model trained on the full dataset when using only 12% of the entire dataset, reducing training costs while improving model performance.
3. Consideration of quality and diversity: The study effectively combines data quality and diversity, addressing the limitations of existing methods that often focus on one aspect over the other.

### Weaknesses
1. This paper is not well-motivated.

> From this insight, we formulate a hypothesis: instructions that align with the knowledge absorbed during pre-training are more easily learned and integrated by the model through subsequent fine-tuning. We term these effective guiding instructions as "high-quality instructions. (at line 83)

There is no related publications or experiments (not mentioned in this paper) to support this opinion, but the method of this paper is motivated by such a non-verified 'idea'.

2. Lack of in-depth exploration of noise: The study did not conduct an exhaustive gradient experiment to determine the optimal level of noise intensity, leaving room for further investigation into the relationship between noise and data quality.
3. While the method shows promising results, the process of noise injection and how it exactly relates to data quality may lack interpretability. This could make it difficult for practitioners to understand and trust the method fully.
4. The method relies on the pre-trained model's behavior and certain assumptions such as the smoothness and clustering assumptions. If these assumptions do not hold true for certain datasets or models, the effectiveness of the method may be compromised.

### Questions
see the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2
