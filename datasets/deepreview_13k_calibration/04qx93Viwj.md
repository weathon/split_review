# Holistically Evaluating the Environmental Impact of Creating Language Models

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
As the performance of artificial intelligence systems has dramatically increased, so too has the environmental impact of creating these systems. While many model developers release estimates of the power consumption and carbon emissions from the final training runs for their latest models, there is comparatively little transparency into the impact of model development, hardware manufacturing, and total water usage throughout. In this work, we estimate the real-world environmental impact of developing a series of language models, ranging from 20 million to 7 billion active parameters, trained on up to 5 trillion tokens each. When accounting for hardware manufacturing, model development, and our final training runs, we find that our series of models released $\textbf{270 metric tons}$ of carbon emissions, equivalent to powering about 53 homes in the United States for one year, and consumed $\textbf{1.137 million liters of water}$, equivalent to about 10 years of water usage by a person in the United States, even though our data center is extremely water-efficient. We measure and report the environmental impact of our model development; to the best of our knowledge we are the first to do so for LLMs, and we find that model development, the impact of which is generally not disclosed by most model developers, amounted to $\sim$$\textbf{80}$% of that of training. By looking at detailed time series data for power consumption, we also find that power usage throughout training is not consistent, fluctuating between $\sim$15% and $\sim$85% of our hardware's maximum power draw, with negative implications for grid-scale planning as demand continues to grow. We close with a discussion on the continued difficulty of estimating the environmental impact of AI systems, and key takeaways for model developers and the public at large.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper provides estimates and insights into power and water consumption during training and inference of Large Language Models (LLMs). Many of these estimates are based on real experiments in training these models of different parameter sizes. Some are rough estimates for cases where experiments were not possible, such as GPU manufacturing. The paper highlights that there are side activities such as data center cooling, development of the model etc. which are not accounted for in the literature reporting carbon emissions from model training.

### Strengths
1. The paper raises very important concerns about transparency in the area of energy and water consumption required for developing as well as using LLMs.
2. This paper includes aspects of this process which have not been reported before such as hyper-parameter tuning and manufacturing of GPUs.
3. The discussion around these calculations is useful for others to understand the environmental implications of doing AI research.

### Weaknesses
1. While some of the calculations are clear and seem reproducible as long as some of the manufacturer specific quantities are known, I am not 100% certain if all the steps can be followed by others. It would be useful if the authors can confirm whether someone can apply their methodology for similar experiments/calculations and if the paper contains all the details needed to do so. Specifically, the paper should clarify how the power consumption of individual components (e.g., GPUs, CPUs, memory) was measured and aggregated, and whether these measurements were taken at the component level or at the system level. Details on the specific tools or methods used for power measurement, such as the sampling rate and accuracy, are also needed to ensure reproducibility. Furthermore, the paper should include a detailed breakdown of the energy consumption for each stage of the training process, including data loading, forward and backward passes, and parameter updates, to allow for a more granular analysis.
2. It would be helpful if the `Development` part of Section 4.1 can provide more details of what it covers i.e. what kind of HPO, what was the search space, what scaling experiments etc. For example, the paper should specify the hyperparameter optimization algorithm used (e.g., random search, Bayesian optimization), the range of values explored for each hyperparameter, and the number of trials conducted. Additionally, the paper should detail the specific scaling experiments performed, including the number of parameters, the dataset size, and the hardware configurations used. This would allow readers to understand the computational cost associated with the development process and to compare it with other studies.

### Questions
I would think similar studies are done for other fields such as electric vehicles. Are there better regulations for reporting in those? What are some other parallels and what other gaps can we find in transparency compared to them?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper estimates the real-world environmental impact of training LLMs, including hardware manufacturing, model development, final training runs, and deployment. They vary model sizes, model architectures, and training time, providing a first view of the embodied CO2 production and water usage from AI systems at these scales. The entire study results in a production of 270t CO2 and a usage of 1.1M liters of water.

Additionally, it finds that model development accounts for 80% of the environmental impact, which is often not stated in related work. Additionally, they find that power draw has highs and lows due to checkpointing, creating a mixed load on the electrical grid, which may not easily be addressed, resulting in control challenges for power providers.

### Strengths
S1: This paper provides the first-ever comprehensive end-to-end view of the environmental impact of an LLM. It is highly valuable to have this data published, as we, as a research community, need to have a complete view of how current training and deployment practices affect CO2 production and water usage. The insights and data provided can be used as a building block to argue future performance improvements not only for $ cost reasons but also to quantify their environmental impact. 

S2: The authors take care to question current naive assumptions like a 100% power draw during training, making this paper stand out. While this is a low bar, research on environmental impact in LLM training has had its share of invalidated research due to these minor, overlooked details.

S3: The authors estimate the water usage during the development of an LLM, which I have not seen before in this line of research. This adds a new dimension to the environmental impact, providing a more complete picture of how current AI practices affect our environment.

### Weaknesses
W1: The result of model development being a large chunk of the environmental impact is not too surprising, but I agree that it is important to track and present in this paper. I am wondering about the representativeness of the data presented in this paper for model development and whether we will see a similar trend continue in the future. Given that this is a key contribution outlined in the abstract, I question whether the number of 80% will change significantly in future related work and if there are steps to take to present this more confidently. I am afraid that researchers in related fields take the final training costs and multiply them by 5x due to the results in this paper.

W2: The second point of discussion has a similar issue as W1. While I agree that oscillating power draw may be a problem for power providers, I hesitate to agree that this is an issue at large. GPU-memory checkpointing has been shown to be possible by Gemini (https://arxiv.org/pdf/2312.11805), which likely reduces this time to sub-seconds. I am not against keeping this insight in general, and that power draw may be an issue for future techniques, but I question the future-proofness of this discussion point. Also, this being a problem for power providers could be explained in more detail and what this implies for the environmental impact.

W3 (minor issues):
* The EU AI Act could be included in 5.1 as it also includes the environmental impact of AI systems (e.g. Art 95 https://artificialintelligenceact.eu/article/95/)
* Figure 1 takes a lot of space for the amount of information it provides. A double y-axis may not be the best visualization as it makes it harder to initially grasp the information. Maybe using two scatter plots would make the visualization more compact and easier to understand?

### Questions
I would like the authors to address W1 and W2, whether they agree or not, and if they do, how they plan to address them.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper discusses the impact of large language models on the environment by studying the costs associated with training and deploying them. It explores the hidden cost of training a model, particularly when it comes to hardware manufacturing and the pre-training steps of creating a model, along with the training and deploying costs. They run their experiments on a small set of models with parameter sizes ranging between 20 million and 7 billion parameters. The results show that models released 270 metric tons of carbon emissions and 1.137 million liters of water. Additionally, the author discusses the power fluctuation during training that is a result of model checkpointing.

### Strengths
The discussion of energy consumption and costs incurred by training and deploying LLMs is a rising and highly relevant topic.
This paper has the following strengths:

1. It is one of the first studies to report the environmental impact of model development, not just the final training runs, highlighting the significant but often overlooked costs associated with hyperparameter tuning and other development activities.
2. Cost evaluation encompasses power consumption, carbon emissions, and water usage and is not confined to a single aspect.
3. Reporting the costs and putting them into perspective with real-world equivalencies.

### Weaknesses
Even though the topic is highly interesting he are some limitations to the paper:
1. Lack of novelty: The issue of power consumption in LLMs has been widely studied, and this paper doesn't provide any additional ideas, metrics, or insights expect for the study development cost.
2. The findings are based on a specific set of small models, which may limit the generalizability of the results to other models and data centers with different configurations and efficiencies
3. The study does not include data from actual deployment and usage of the models, relying instead on simulated scenarios, which may not fully reflect the actual environmental costs. In fact, the paper has a limited set of inference simulations with very simplistic assumptions, which may not fully capture the real-world deployment scenarios and their environmental impacts. 
4. Some of the calculations rely on assumptions and estimates, particularly regarding the embodied emissions and water consumption of hardware manufacturing, which may not be entirely accurate.
5. Limited comparison across models: The authors seem to have taken the carbon consumption of llama and OLMo in Table 2 from previous works without replicating results, which meant no water usage comparison for training. For deployment, they only compare with Llama.
6. Given the small sizes of the models, the paper lacks an analysis of how their results scale to larger models.

### Questions
1. In table 2, why is OLMo reported twice is there a difference?
2. I am curious to know how much time it took to train your models. Given the hardware resources you had (up to 64 HGX servers with h100), why was your study limited to 7 billion parameter models?

### Soundness
3

### Presentation
3

### Contribution
3
