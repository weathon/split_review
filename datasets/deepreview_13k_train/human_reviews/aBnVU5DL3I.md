# SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Evaluating the response quality of large language models (LLMs) for open-ended questions poses a significant challenge, especially given the subjectivity and multi-dimensionality of "quality" in natural language generation. Existing LLM evaluators often neglect that different scenarios require distinct evaluation criteria. In this work, we propose **SaMer**, a scenario-aware multi-dimensional evaluator designed to provide both overall and fine-grained assessments of LLM-generated responses. Unlike fixed-dimension evaluation approaches, SaMer adapts to different scenarios by automatically identifying and prioritizing relevant evaluation dimensions tailored to the given query. To achieve this, we construct a large-scale fine-grained preference dataset spanning multiple real-world scenarios, each with distinct evaluation dimensions. We then leverage a text embedding model combined with three specialized heads to predict the appropriate evaluation dimensions and corresponding scores, as well as the respective weights that contribute to the overall score. The resulting model offers fine-grained and interpretable evaluations and shows robust adaptability across diverse scenarios. Extensive experiments on eight single rating and pairwise comparison datasets demonstrate that SaMer outperforms existing baselines in a variety of evaluation tasks, showcasing its robustness, versatility, and generalizability.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces SaMer, a novel scenario-aware multi-dimensional evaluator designed to assess the quality of Large Language Model (LLM) responses to open-ended questions. The work addresses a significant challenge in LLM evaluation: the complex, multifaceted nature of response quality assessment, which varies significantly across different types of queries and use cases. While traditional LLM evaluators typically provide only overall scores or rankings, with some offering limited multidimensional evaluations across fixed dimensions like harmlessness, honesty, and helpfulness, different scenarios require different evaluation criteria. The key innovation of SaMer lies in its ability to provide both overall and fine-grained assessments of LLM-generated responses, with a flexible framework that adaptively identifies and prioritizes relevant evaluation dimensions based on the query type. This approach contrasts with existing methods that rely on predetermined evaluation dimensions. To support this framework, the authors developed a large-scale fine-grained preference dataset encompassing 42 evaluation dimensions across 36 scenarios, with scenarios categorized into five main types based on Maslow's hierarchy. Three graduate students created dimension definitions, and the final dataset contains 135,402 total data points, with 2,000-5,000 samples per scenario.
The dataset construction started with the collection of preference data (win/lose/tie labels) from multiple sources, including custom datasets built using LLM-generated annotations. Scenario annotation utilized a custom-trained LLaMA-3-8B classifier on [Li et al., 2023] data, enriched with GPT4-o-mini annotations for target scenarios without previously existing annotations. The sampling process initially gathered 6,000+ instances per scenario, followed by GPT-4o-mini verification of scenario labels and final balancing to 2,000-5,000 samples per scenario. Fine-grained preference annotation was performed using GPT-4o.
The model architecture consists of a frozen pre-trained LLaMA-3-8B (pre-trained for rewarding using [Wang et al., 2024]) as the text encoder, with its original output projection layer removed. On top of this encoder, the model employs three specialized MLP heads: a quality dimension prediction layer performing multi-label classification using ZLPR loss, a pairwise preference learning layer using margin ranking loss, and a weighting layer for overall scoring also utilizing margin ranking loss. The training process combines these losses (L_{zlpr}, L_{dim}, and L_{o}) through weight hyperparameters lambda.
The evaluation of SaMer was conducted across 9 benchmarks spanning 3 families. For single rating benchmarks, the assessment used Pearson, Spearman, and Kendall-Tau correlations, while preference selection tasks were evaluated using accuracy metrics for pairwise and fine-grained comparisons. The results demonstrate SaMer's superior performance compared to existing baselines, showing strong adaptability across diverse scenarios while providing interpretable, fine-grained evaluations.

### Strengths
- The paper is clear and well-structured, effectively communicating complex ideas through a logical flow and professional presentation.
- The fine-grained preference dataset represents a valuable contribution to the field.
- The model is efficient and practical, making it accessible for deployment and fine-tuning.
- The evaluation is thorough and comprehensive, benchmarking against both proprietary models and open-source alternatives.

### Weaknesses
 - From a methodological standpoint, the paper's novelty is limited. While it combines multiple components to create a comprehensive evaluation system, the individual techniques used are standard approaches in the field, and many data resources are derived. The main innovation lies in the application rather than the methodology itself.
- The hyperparameter analysis lacks depth and transparency. For example, the authors fix lambda values to combine the different losses without exploring or discussing their impact on model performance. Similarly, other hyperparameters are presented with single values, offering no insights into their selection process or their effects on the model's behavior. This absence of ablation studies or sensitivity analyses makes it difficult to understand the robustness of the approach.
- The use of GPT-4o-based models on this scale for intensive annotation and filtering is resource-intensive and appreciable. However, this heavy reliance can introduce potential biases and raises questions about the overall training dataset quality. Specifically, the potential for annotation bias due to insufficient understanding of the evaluation dimensions by GPT-4o, and the possibility of the model overlooking key dimensions when synthesizing overall preferences, are significant concerns. The paper lacks a thorough discussion on how these biases were addressed during the annotation process.
- There is no discussion of verification steps or quality control through human analysis to ensure the artificial annotations' reliability. This is particularly important given the subjective nature of many evaluation dimensions.
- The supplementary materials lack data samples, making it impossible for reviewers to assess the quality and characteristics of the dataset.
- The metrics section (5.2) requires a more detailed explanation.
- The paper does not clearly provide information about code availability, model checkpoint distribution, or dataset licensing.

### Questions
Please specify the version of the employed proprietary models to ensure reproducibility.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an evaluation model (SaMer) that assess the quality of responses based a 42 pre-selected dimensions and gives an overall evaluation by weighting scores on different dimensions. The experimental results show that the proposed model achieves the best efficacy on single rating datasets and the fine-grained comparion data curated by the authors, and it also achieves a comparable performance with ArmoRM on pairwise comparison datasets.

### Strengths
- Compared to past evaluators that assessed overall quality, the fine-grained evaluation method proposed in this paper provides more fine-grained evaluation results. The weights across different dimensions offer a certain level of interpretability.

- Since this model can implicitly determine the required dimensions based solely on the query without task information, this evaluator is task-agnostic and possesses a certain degree of generality.

### Weaknesses
 - The evaluator's ability to understand different dimensions is questionable. Firstly, the 42 dimensions are fixed, and the model did not even encounter these dimension definitions during training (nor did the paper provide their specific definitions). Secondly, the experimental results do not demonstrate whether the evaluator can accurately determine which dimensions are needed when encountering out-of-domain data. Compared to similar work like X-Eval [1], which allows users to input personalized dimension definitions, it is hard to say that this model has a clear advantage.

- The paper employs three loss functions but lacks ablation studies to investigate the impact of choosing $\lambda_1$ and $\lambda_2$ on model performance, making it difficult for readers to understand the individual contributions of these designs.

### Questions
- Typos: The term "Demension" in Figure 3 should be corrected to "Dimension."

- How is the dimension-level accuracy in Table 5 calculated?

- The data used to train fine-grained preferences is primarily annotated by GPT-4o; however, GPT-4o has issues with confusing different dimensions [2]. How can you ensure that the data generated by GPT-4o is of high quality?

- Could you please provide more information on how you verify the quality of MD-Eval test set (used in Table 5) through human evaluation?

[2] Are LLM-based Evaluators Confusing NLG Quality Criteria? (Hu et al., ACL 2024)

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
4

### Summary
This paper presents SaMer, a new framework to evaluate LLM responses with more flexibility. Instead of using static criteria for evaluating open-ended generation, SaMer adapts its approach based on the context, whether it's looking at a creative response, answering a factual question, or offering advice. To achieve this, the authors created a large-scale dataset covering a variety of real-life scenarios so SaMer could learn to recognize what matters most in different situations. The framework is set up with three parts: one to pick relevant criteria, one to score based on those criteria, and one to weigh them for an overall score. 

Experiments indicate that SaMer performs competitively, achieving improvements over baseline models across single rating, pairwise comparison, and fine-grained dimension-specific benchmarks. It also sheds light on which factors are key in different scenarios. Overall, SaMer brings a more adaptable, context-sensitive way to evaluate LLM responses, making it better suited to assess responses based on what's actually needed in each situation.

### Strengths
1. The motivation for a more fine-grained, multi-dimensional evaluation of LLM responses is reasonable and relatively under-explored, as current evaluations usually rely on a single overall score.
2. The authors have built a large-scale preference dataset from existing corpora, covering diverse scenarios and annotating each with corresponding evaluation dimensions.
3. Experimentally, the model shows performance improvements over baselines across several settings.

### Weaknesses
 **Major Issues:**

1.  **The choice of evaluation dimensions for each scenario is unclear**: The authors mention that three graduate students annotated the evaluation dimensions for each scenario. However, this task seems highly subjective and challenging. From Table A2, many dimensions appear vague or redundant. For instance, why doesn’t "data analysis" include "Accuracy"? Why is "Logic" missing for "reading comprehension"? “Recommendation” seems subjective, so why does it include "Objectivity"? "Accuracy" and "Admit Uncertainty" also seem somewhat contradictory, yet both are included in five scenarios. "Being Friendly" and "Audience Friendly" seem overlapping. Overall, the annotations lack clarity and intuitiveness. The authors could improve this by defining these dimensions and including the guidelines used for annotation in the paper. Additionally, reporting inter-annotator agreement with discussion would be helpful.

2.  **The predicted evaluation dimensions are still pre-defined**: Although SaMer claims to flexibly predict relevant evaluation dimensions per scenario, it actually selects from a set of 42 dimensions defined in previous studies. This limits SaMer's ability to generalize to broader, unforeseen scenarios.

3.  **No evaluation of selected evaluation dimensions**: The experiments in this paper focus on overall response preference or specific fixed dimensions. However, one of SaMer's primary contributions is automating the prediction of relevant dimensions for each scenario, yet there is no experiment supporting SaMer’s effectiveness in this. A potential experiment could involve having LLMs generate reasonable evaluation dimensions for given scenarios as a baseline, then comparing those results with SaMer's using human judgment as a metric.

4.  **Missing related work**: Multi-dimensional and explainable evaluations for text generation are not new ideas, and it would be helpful for the authors to include comparisons and discussions with prior works such as [1-3].

**Minor Issues:**

1.  **Potential unfair comparisons**: The training of SaMer heavily relies on GPT-4o for preference annotation, while some baselines may not have used this newer and potentially stronger teacher model, which could lead to unfair comparisons.
2.  **Lack of efficiency discussion**: Since SaMer first predicts evaluation dimensions before aggregating them into an overall score, discussing runtime and efficiency comparisons would help the community better understand the practical efficiency of this framework.

### Questions
In Table 2, SaMer's Pearson correlation on the Vicuna Bench is comparable to GPT-4o, but its Spearman and Kendall correlations are significantly higher. Given that GPT-4o performed all preference annotations, why does SaMer outperform GPT-4o on these metrics, and are there any insights into why these correlations differ so much from the Pearson correlation?

### Soundness
2

### Presentation
3

### Contribution
3
