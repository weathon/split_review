# A Statistical Framework for Ranking LLM-based Chatbots

- Decision: Accept
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Large language models (LLMs) have transformed natural language processing, with frameworks like Chatbot Arena providing pioneering platforms for evaluating these models. By facilitating millions of pairwise comparisons based on human judgments, Chatbot Arena has become a cornerstone in LLM evaluation, offering rich datasets for ranking models in open-ended conversational tasks. Building upon this foundation, we propose a statistical framework that incorporates key advancements to address specific challenges in pairwise comparison analysis. First, we introduce a factored tie model that enhances the ability to handle ties—an integral aspect of human-judged comparisons—significantly improving the model’s fit to observed data. Second, we extend the framework to model covariance between competitors, enabling deeper insights into performance relationships and facilitating intuitive groupings into performance tiers. Third, we resolve optimization challenges arising from parameter invariances by introducing novel constraints, ensuring stable and interpretable parameter estimation. Through rigorous evaluation and extensive experimentation, our framework demonstrates substantial improvements over existing methods in modeling pairwise comparison data. To support reproducibility and practical adoption, we release leaderbot, an open-source Python package implementing our models and analyses.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a statistical framework for ranking LLM-based chatbots. It addresses the limitations of existing methods like the Elo rating system by incorporating ties and covariance structures. The proposed apply well-established statistical models to properly account for ties within an axiomatic framework and introducing factor analysis. Experiments on the Chatbot Arena dataset show improved accuracy and insights into chatbot rankings and relationships.

### Strengths
1. The proposed method can account for ties in an axiomatic framework. This improves not only tie prediction but also enhances win-loss inference.
2. The mathematical analysis is comprehensive and thorough.
3. This work has an open source python package which is easy to use.

### Weaknesses
1. For model ranking, it has no "ground truth". Therefore, it is hard to convince others under this method, the ranking is more accurate.
2. The evaluation is highly dependent on the Chatbot Arena dataset which makes this work a slight improvement on chatbot arena. Therefore, the impact of this work is limited.
3. As for chatbot arena, a simple enough ranking rule is more important if the users are common users. This work will make the rule too complicated for them to understand and then reduce the impact of chatbot arena.

### Questions
1. Is this method only useful to chatbot arena or it is useful to all Elo ratings?
2. We need another figure to see the ranking difference of original chatbot arena and this methods. Also the figure 1 showing the result of PCA analysis is confusing.

### Soundness
3

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose an improved statistical model for ranking large language models (LLMs) on the Chatbot Arena dataset to enhance the traditional Elo rating system. Paper points out that the Elo system has limitations in handling ties and capturing relationships between models. To address these issues, paper introduces the Rao & Kupper and Davidson models, as well as a novel factor model to better capture the complexity of ties between different models, thereby improving prediction performance. Finally, they provide a Python package, “Leaderbot,” to reproduce the statistical model and support further experiments.

### Strengths
1. The authors identify symmetry issues in the likelihood function of traditional models, which could lead to instability in parameter estimation. To address this, they propose symmetry constraints that ensure stable parameter estimation, thereby enhancing the model’s optimization performance and interpretability;
2. They effectively address the issue of ties, which is a limitation of the existing Elo system, and make optimizations to handle this;
3. They provide a Python package that allows for the reproduction of the paper's results and supports further research.

### Weaknesses
1. The authors use multiple models to rank models, showing that high-ranking models exhibit greater consistency than lower-ranking ones. However, they do not provide further analysis, such as examining the specific characteristics of models that initially show ranking inconsistencies. For instance, do these inconsistencies correlate with model size, training data diversity, or architectural differences? A deeper investigation into *why* certain models exhibit inconsistent rankings would strengthen the analysis.
2. The authors’ work focuses on optimizing the ranking model but lacks subsequent analysis. Additional insights, such as a more in-depth examination of correlations between LLMs or an analysis of the differences between Leaderbot rankings and Chatbot Arena Elo rankings in relation to model characteristics, would enhance this work. The current analysis could be expanded to explore how these ranking differences manifest in practical applications or downstream tasks. For example, do models that are ranked differently by the two systems exhibit different performance in specific use cases?


### Questions
1. In the treatment of pairs and unique pairs, have the authors considered introducing semantic clustering to their model, as opposed to solely using statistical techniques? Additionally, could they clarify the reasoning behind not exploring semantic relationships within pairs?
2. Have the authors considered methods other than PCA to further analyze the correlations between models in the results? The current approach does not sufficiently reveal the underlying correlations between LLMs in an intuitive way.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses a novel problem in the evaluation of large language model (LLM)-based chatbots by proposing an advanced statistical framework that builds on existing methods used in the Chatbot Arena setting. The framework integrates well-established models, such as Rao-Kupper and Davidson, to account for ties in a rigorous axiomatic framework, and introduces Thurstonian representations to model covariance structures between competitors. These additions allow for more nuanced insights into chatbot rankings and performance consistency. A Python package, leaderbot, is also provided for reproducibility and ease of experimentation.

### Strengths
1. **Pioneering Approach**: This paper tackles a novel and important problem in LLM evaluation, presenting a unique perspective on using advanced statistical models to refine the ranking process in chatbot comparisons. Its approach to systematically modeling ties and latent structures sets a new precedent for evaluating LLM-based chatbots and offers fresh insights that go beyond traditional ranking methods.
2. **Innovative Use of Thurstonian Representations**: By integrating Thurstonian models and introducing covariance structures, the paper offers a groundbreaking method for capturing relationships among LLMs. This enables a deeper analysis of model consistency and performance that extends beyond simple rankings, marking a notable advancement in chatbot evaluation techniques.

### Weaknesses
1. While the paper introduces an alternative framework, it does not clearly discuss why Arena’s Elo-based approach is insufficient beyond the issue of ties. Additional insight into Arena’s limitations in capturing competitive dynamics or certain statistical shortcomings would strengthen the argument for this new model.
2. The authors mention consistency in high-ranking models and variability in lower-ranking models, but do not explore further distinctions within these groups. For example, identifying specific characteristics (e.g., model size) associated with high consistency could provide more actionable insights.

### Questions
1. The paper mentions that high-ranking models show greater consistency than lower-ranked ones. Could you expand on this observation? For example, are high-ranking models generally larger or more sophisticated in architecture? And at what ranking position does this shift in consistency typically occur?
2. How is the effectiveness of handling ties quantified across different statistical models? Is there an analysis of which models are more favorable to certain LLMs, and if so, what might explain these differences?

If these questions can be addressed, the paper could potentially be rated one point higher.

### Soundness
4

### Presentation
2

### Contribution
3
