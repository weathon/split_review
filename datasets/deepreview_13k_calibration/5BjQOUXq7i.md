# RegMix: Data Mixture as Regression for Language Model Pre-training

- Decision: Accept
- Avg Score: 7.20
- Scores: 8, 8, 6, 6, 8

## Abstract
The data mixture for large language model pre-training significantly impacts performance, yet how to determine an effective mixture remains unclear. We propose \ourmethod to automatically identify a high-performing data mixture by formulating it as a regression task. \ourmethod involves training a set of small models with diverse data mixtures and fitting a regression model to predict their performance given their respective mixtures. With the fitted regression model, we simulate the top-ranked mixture and use it to train a large-scale model with orders of magnitude more compute. To empirically validate \ourmethod, we train 512 models with 1M parameters for 1B tokens of different mixtures to fit the regression model and find the optimal mixture. Using this mixture we train a 1B parameter model for 25B tokens (i.e. $1000 \times$ larger and $25 \times$ longer) which we find performs best among 64 candidate 1B parameter models with other mixtures. Further, our method demonstrates superior performance compared to human selection and achieves results that match or surpass DoReMi, while utilizing only 10\% of the compute budget. Our experiments also show that (1) Data mixtures significantly impact performance with single-task performance variations of up to 14.6\%; (2) Web corpora rather than data perceived as high-quality like Wikipedia have the strongest positive correlation with downstream performance; (3) Domains interact in complex ways often contradicting common sense, thus automatic approaches like \ourmethod are needed; (4) Data mixture effects transcend scaling laws, and our approach captures the complexity by considering all domains together.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The work introduces REGMIX, a method for optimizing data mixtures to enhance language model training efficiency. REGMIX treats data mixture selection as a regression task, using small proxy models to predict the performance of different mixtures and identify the best one, enabling larger models to be trained with significantly less compute. Key findings include:
- REGMIX’s mixtures perform as well as or better than those selected by human experts and prior methods like DoReMi, with only a fraction of the compute cost.
- Data mixture has a substantial impact on downstream performance, with single-task performance differences reaching up to 14.6%.
- General web corpora (such as CommonCrawl) outperform traditionally high-quality data like Wikipedia in driving downstream performance.
- Domain interactions are complex and often counterintuitive, highlighting the value of automated approaches like REGMIX.
- Data mixture effects go beyond scaling laws, with REGMIX capturing the complexity by jointly optimizing across all domains.

### Strengths
- The paper introduces a novel, regression-based approach for selecting data mixtures that reduces computational costs in language model training. The approach offers an efficient alternative to traditional dynamic or heuristic data allocation methods, making a valuable contribution to the field.

- The paper is technically robust and well-structured, with extensive validation across diverse data scenarios. It empirically supports the rank invariance hypothesis and uses clear, well-structured figures to illustrate the method and results, enhancing reader understanding. REGMIX’s ability to match or outperform other DoReMi and other methods with significantly less compute is a compelling outcome for LLM pre-training efficiency.

- The paper tackles a pertinent problem in LLM pre-training. Given the increasing size of training data and models, this approach could have a significant impact on the field, especially in reducing computational costs and environmental impact.

### Weaknesses
 - To maximize impact, the authors could highlight specific scenarios where the approach enables previously infeasible experiments due to resource constraints. Also, adding a broader discussion on trade-offs of the method (e.g., scenarios where the rank invariance assumption might not hold) would help readers assess its practical relevance and future applicability.

- The work could have used standardized computation metrics, such as FLOPs or GPU hours, to allow clearer comparison of the method efficiency gains relative to baselines.

### Questions
1) Can you further explain why the choice of multiplying the e token distribution by a value from 0.1 to 5.0? Is this a standard practice? Were other ranges tested, and if so, what were the results? 
     - Also, could you discuss the rationale behind this range and whether you conducted any sensitivity analyses to determine its impact on the results?

2) Given sufficient computation available, would segmenting domains further (into finer-grained topic-based segments) likely improve model performance or lead to more effective mixture predictions? Do you think that finer segmentation would affect the rank invariance assumption? I suggest the authors to discuss the potential impacts and challenges of a finer-grained domain segmentation in their future work section. This would help address the broader implications and limitations of their approach.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents RegMix, a new method for optimizing data mixtures in pre-training large language models (LLMs). Recognizing the importance of data composition, the authors frame mixture selection as a regression task. RegMix uses small proxy models trained on various data mixtures to build a predictive model that identifies the optimal mixture for larger models.

The authors conduct extensive experiments to validate the approach, showing that models trained with RegMix-selected data mixtures outperform those trained with mixtures chosen by other methods, including human selection and DoReMi, while utilizing only 10% of the compute budget.

The authors provide insights into the effects of data mixtures, offering empirical evidence that data mixtures can significantly impact performance, with single-task performance variations reaching up to 14.6%. They also emphasize the complex interactions that occur between different data domains.

### Strengths
1. RegMix introduces a fresh approach by framing data mixture selection as a regression problem rather than relying on complex optimizations or heuristics, making the process scalable and computationally efficient.

2. The paper’s experimental setup is robust, with 512 small proxy models across diverse data mixtures, creating a solid regression model for data selection.

3. The paper is well-organized, clearly explaining the methodology and experiments. It introduces the hypothesis of rank invariance in data mixtures, supported by visual aids, making the regression model’s role easy to understand.

### Weaknesses
The paper conducts a set of small-proxy models trained with small-scale tokens.

The paper only experiments with 1M models with 1B tokens. 
It is unclear how to decide the size of the proxy model parameter and training token.

### Questions
How do we decide the size for proxy model and training tokens.?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a method called REGMIX for automatically selecting an effective data mixture to optimize the pre-training of large language models. REGMIX formulates the data mixture selection as a regression task, training a set of small models with diverse data mixtures and fitting a regression model to predict their performance. The fitted regression model is then used to simulate and identify the top-performing data mixture, which is subsequently used to train a large-scale model. The empirical results demonstrate that REGMIX can improve downstream task performance and achieves results comparable to or surpassing the DoReMi method while using only 10% of the compute budget.

### Strengths
- The paper presents a novel method, REGMIX, which formulates the data mixture selection problem as a regression task. This is a creative approach that leverages small-scale proxy models to predict optimal data mixtures for large-scale models.
- The authors conducted extensive experiments, training 512 models with 1M parameters on 1B tokens to fit the regression model. They then validated this model by training a 1B parameter model on 25B tokens, showing superior performance compared to human selection and the DoReMi method.
- The method allows for parallel training of small proxy models, making it more scalable than previous approaches that require training a single model for a long time.
- The paper provides several interesting findings, such as the significant impact of data mixtures on performance, the strong positive correlation of web corpora with downstream performance, and the complex interactions between domains.

### Weaknesses
 - The key assumption of rank invariance of data mixtures across different model sizes and token counts is not thoroughly validated. This assumption might not hold in all cases, especially with significant changes in model scale and data distribution. Specifically, the paper does not explore the impact of varying the number of parameters in the proxy models on the optimal data mixture. It is possible that the optimal mixture identified using 1M parameter models might not be optimal for much larger models, such as 7B or 70B parameter models, which are more commonly used in practice. The paper also lacks a detailed analysis of how the rank invariance assumption holds up when the pre-training dataset is significantly scaled up, for example, from 25B tokens to 100B or even 1T tokens. This is a critical gap, as the optimal data mixture might change as the model sees more data and the data distribution shifts.
- The paper claims stability across different proxy model sizes, but the experiments are limited to models with up to 1B parameters. It remains unclear if the method would be equally effective for much larger models commonly used in practice (e.g., 7B or 70B parameters). If so, the additional computation cost could not be ignored. The paper does not provide a clear analysis of the computational cost associated with training the proxy models, especially when scaling to larger proxy models. The trade-off between performance gains and additional costs may not always hold when the model scales up. The paper should provide a more detailed analysis of the computational resources required by REGMIX, including the time and memory requirements for training the proxy models, and how these scale with the size of the proxy models and the number of data mixtures.
- The authors only trained 25B tokens using the obtained data mixtures. This raises the question of whether the data scale could be enlarged to 50 times or even 100 times. And can LLM sitll benefit from the obtained data mixture? It is not clear whether the data mixture optimized for 25B tokens would remain optimal when the pre-training dataset is significantly scaled up. The paper should provide an analysis of how the performance of the model changes when trained on much larger datasets, such as 100B or 1T tokens, using the optimized data mixture. The paper should also investigate whether the optimal data mixture changes as the model sees more data, and if so, how to adapt the data mixture during pre-training.
- Although the method is more efficient than some previous approaches, training 512 small models still requires substantial computational resources. This could be a limitation for teams with limited access to such resources. The paper does not provide a detailed analysis of the computational resources required by REGMIX compared to other methods, making it difficult to assess the practical feasibility of the method. The trade-off between performance gains and additional costs may not always hold when the model scales up.

### Questions
- Can the authors provide more theoretical or empirical evidence to support the rank invariance assumption? How does this assumption hold up with significant changes in model scale and data distribution?
- How does REGMIX perform with proxy models larger than 1B parameters? Can the authors provide any preliminary results or insights on this? Or could the obtained data mixtures guide us to train a better model using much more tokens, e.g., 100B?
- Can the authors provide a detailed comparison of the computational resources required by REGMIX and other methods? This would help in understanding the practical feasibility of the method.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper formulates data mixing problems as a regression task. The authors propose to search data mixtures on small models and fit regression models to predict the optimal data mixture, which is then transferred to larger-scale model training. The authors empirically show the rankings of different data mixtures hold consistent between small and large-scale training. And data mixture found to be optimal at small scales can lead to improved performance compared to human heuristics and previous methods at large scales.

### Strengths
1. The paper is well-written and easy to follow.
2. The author identifies a helpful assumption, namely ranking invariance regarding training scales, which helps reduce the cost of tuning data mixtures in this paper.
3. The proposed method is simple to implement and efficient, thus appealing to try in practice.
4. The paper contains extensive experiments to show optimizing data mixtures improves model performance.

### Weaknesses
1. The feasibility of treating the data mixing problem as a regression problem has been an idea unveiled by previous studies [1,2], as the authors also mentioned in the paper.
2. The methods experiment on as many as 512 training runs. It is unclear whether the regression step is still necessary with so many experimented mixtures. This makes the proposed method actually a grid search with a small-scale proxy.
3. The proposed method highly depends on the assumption of ranking invariance regarding scales. The author only provides limited empirical results on this assumption. However, such an assumption is questionable according to [3]. It would be better if the authors provide more discussion to explain the scope where this assumption holds.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a method that trains a simple regression model over data mixture ratios and the LLM loss on very small models, and then use the trained regressor to predict the best data mixture configuration for training larger scale models. The method is interesting and the experiments are relatively comprehensive. The paper considers two regression methods and verified the predicted mixture on a 1B model.

### Strengths
1. the proposed method is novel and has practical impact to LLM training
2. the authors evaluated the predicted mixture on 1B model and compared to a few prior methods based on the downstream performance of the model
3. the paper also has good analysis and insights about regarding optimizing data mixture ratio, the relationship between validation PPL loss and downstream task performance, and the issues regarding scaling laws for data mixture.

### Weaknesses
1. there are some details of the regression model that's not clearly explained. It is not clear to me how the authors fit the regression model, how many data points are used to fit the models. It would be nice to have a pseudocode or open-sourced script
2. the mixture weights for the baseline DoReMi is directly taken from the paper. However, it's not clear if the optimal weights learned using the DoReMi method would be different due to model and data processing differences. It's probably better to re-learn the weights using the small model in the current experiment setup.

### Questions
1. in table 2, why do you only list the MSE for 1M model but rank correlation for all model sizes? what's the MSE for the other two sizes? Why is rank correlation a better metric here?
2. on line 243, the author mentioned the rank invariance hypothesis. However, it's not super clear to me what exactly this means and how this hypothesis is verified by the experimental results. Could you provide a clear definition of the rank invariance hypothesis and explicitly state how the experimental results support or verify this hypothesis?
3. there are some related work on data selection that falls into the group-level data selection category: https://aclanthology.org/2020.acl-main.754/

### Soundness
3

### Presentation
3

### Contribution
3
