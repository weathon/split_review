# INSTRUCTION-FOLLOWING LLMS FOR TIME SERIES PREDICTION: A TWO-STAGE MULTIMODAL APPROACH

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
We introduce Text-Informed Time Series Prediction (TITSP), an innovative multimodal framework that integrates textual knowledge with temporal dynamics using Large Language Models (LLMs). TITSP employs a two-stage process that bridges numerical data with rich contextual information for enhanced forecasting accuracy and interpretability.In the first stage, we present AutoPrompter, which captures temporal dependencies from time series data and aligns them with semantically meaningful text embeddings.In the second stage, these aligned embeddings are refined by incorporating task-specific textual instructions through LLM. We evaluate TITSP on several multimodal time series prediction tasks, demonstrating substantial improvements over state-of-the-art baselines. Quantitative results reveal significant gains in predictive performance, while qualitative analyses show that textual context enhances interpretability and actionable insights. Our findings indicate that integrating multimodal inputs not only improves prediction accuracy but also fosters more intuitive, user-centered forecasting

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The article describe a new model to incorporate textual information with a more traditional timeseries forecasting model. It does so by combining an embedding computed from the historical numerical data with an embedding computing from the textual information. The combined embedding is then used to generate the forecast.

The model is tested both on real-world data, where it shows competitive results, and on generated data, where it is shown to follow the instructions included in the textual information.

### Strengths
1. It is good that zero shot examples of descriptions which have not been provided in the training set have been tested with. Without those, the narrow set of possible descriptions could have made it impossible to check whether the result quality came from the model overfitting on these descriptions or not.
2. Training the model using generated data and computing how well the model follows the instructions is a relatively clean way to do a proof of concept of the idea, which is appropriate currently, as the field of using LLM and timeseries models together is still in its infancy.

### Weaknesses
1. There seems to be a mismatch between the described technique used to apply the modification (equation 3), and the examples shown (figure 3). According to the equation, the data in the forecast window should be a pure affine function, without any of the noise shown in figure 3.
2. While the model is tested against other multimodal text+timeseries models, it should also be tested against pure LLM approaches: just plugging the text and the history in a prompt for GPT 4 or LLama 3, and looking at the generated output. While such an approach won't scale to long series, recent work have shown it to be surprisingly decent at forecasting under textual instructions. See: LLM Processes by Requiema 2024 for a slightly more complex approach, but there may be more appropriate references for the more direct one.
3. Hyperparameters and training curiculum for the timeseries portion of the model are missing.

### Questions
1. For table 4, can you provide the same results, but for your model instead of only for TimeLLM? It would make it more obvious whether your model succeed on those tasks with incorrect textual information.
2. For real world dataset, was the textual information always constant (as shown in section B.3) for each dataset? This would allow a finetuned model to fully ignore it, since it could bake said information in its weights anyway.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents Text-Informed Time Series Prediction (TITSP), a multimodal framework that integrates textual context with time series data using Large Language Models (LLMs). The approach involves two stages: AutoPrompter, which aligns time series data with text embeddings, and a refinement stage that incorporates task-specific textual instructions to enhance prediction accuracy and interpretability. While TITSP proves particularly effective for context-rich forecasting tasks, by demonstrating improved performance under specific settings against some other methods.

### Strengths
- A novel two-stage framework for integrating temporal and textual data.
- A data generation workflow for instruction-based forecasting, compatible with LLMs.
- Comprehensive ablation studies and comparative evaluations demonstrating the effectiveness of TITSP.

### Weaknesses
 - **Technical Contributions are Incremental**  The proposed approach lacks significant technical innovation. Integrating LLMs with time series is an incremental step rather than a groundbreaking contribution. The use of cross-attention and VQ-VAE offers no substantial improvement beyond established techniques.
- **Poor Structure and Clarity**  The paper is poorly organized, with unclear explanations and an incoherent flow. The motivation and rationale for the proposed method are inadequately communicated, and critical components like AutoPrompter are explained in a convoluted manner, hindering comprehension.
- **Inadequate Experiments**  Experimental validation is weak, relying heavily on synthetic datasets that limit the assessment of practical applicability. Comparisons to related state-of-the-art methods are lacking, and statistical significance testing is absent, making it difficult to validate the performance claims.
- **Superficial Related Work**  The related work section lacks depth and fails to properly differentiate the contribution from prior research. Key works are missing or insufficiently discussed, weakening the justification for originality.
- **Numerous Typos and Lack of Polish**  Frequent typos (e.g. citation mistaches in line 54-55), poorly formatted figures(fig. 6), and poorly constructed tables suggest a lack of careful proofreading, which detracts from the overall quality and credibility of the paper.
- **Insufficient Practical Insights**  The claimed interpretability through textual integration lacks demonstration. There are no real-world examples showing how domain experts would benefit from these insights, making the practical value of TITSP unclear.

### Questions
- **How would the proposed model perform without access to textual inputs or under noisy conditions?** If textual instructions are incomplete, inconsistent, or contain noise, how would the model's performance be affected? This scenario is particularly relevant in high-stakes areas like finance, where decision-making often involves dealing with imperfect information. What measures have been taken to ensure robustness against these issues, which are common in real-world data?
- **How does the proposed framework address interpretability in practice?** The paper claims that incorporating textual instructions enhances interpretability, but there are no concrete demonstrations of how this contributes to meaningful insights for domain experts. Could you provide explicit examples or user studies that validate this claim? Without such evidence, how can the claim of improved interpretability be substantiated?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Text-Informed Time Series Prediction (TITSP), a novel two-stage framework that enhances time series forecasting by integrating domain-specific textual information. The paper demonstrates that TITSP significantly outperforms traditional and existing multimodal approaches, improving both predictive accuracy and interpretability.

### Strengths
1. The paper presents a novel approach to time series forecasting by integrating textual instructions, which is a creative extension of existing multimodal time series models. The introduction of a two-stage framework and the focus on instruction-based forecasting address a significant gap in the field.
2. The paper is well-written and logically organized. The figures and tables are clear and effectively support the text. The problem formulation and the description of the methodology are easy to follow.

### Weaknesses
1. Given the synthetic data generation process, how can the authors ensure that there is no data leakage between the text data and forecasting targets? Could the authors provide a detailed explanation of the data generation process to address this concern?
2. How practical is the proposed approach in real-world scenarios where textual instructions may not always be available or may be ambiguous? Could the authors discuss the potential limitations and challenges in deploying TITSP in practical applications?
3. Has the model been tested on any other multimodal time series analysis tasks beyond forecasting? If not, what are the potential challenges in applying TITSP to other tasks?

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a novel two-stage for multimodal forecasting through historical data and textual cues that are useful for LLM-based forecasters. The multimodal framework is evaluated on numerous multimodal forecasting tasks. The paper provides a setup to include expert opinions for a forecasting problem.

### Strengths
The strengths include the relevance of the problem of text-aided forecasting and the novelty of the prompting method. The methodology section is comprehensive and well-described, and the techniques and experiments have been explained in detail and are easy to follow. The figures convey the overall idea and highlight the improvements over the no-instruction setup.

### Weaknesses
The primary weaknesses of the paper are as follows:

1. **Incomplete Literature Coverage**: Section 2.2 does not fully address relevant multimodal forecasting models, omitting key references such as UniTime ([https://dl.acm.org/doi/10.1145/3589334.3645434](https://dl.acm.org/doi/10.1145/3589334.3645434)).

2. **Limited Comparative Analysis**: The results lack sufficient comparison with other multimodal forecasting models, reducing insight into how the proposed method performs relative to similar approaches.

3. **Insufficient Dataset Description**: Essential dataset details, including sample counts, history length, and forecasting horizon, are not provided. Additionally, the impact of the forecasting horizon on prediction quality remains underexplored.

4. **Simplistic Experimental Instructions**: The experimental instructions are overly simplistic, failing to reflect realistic scenarios. The limited set of training instructions may also suggest that simpler alternatives for instruction embedding could have been more effective.

5. **Circular  Evaluation**: The evaluation datasets have been tailored from existing datasets based on the training instructions intended for evaluation, which creates a circular reasoning issue that undermines the reliability of the evaluation setup.  A similar statement about the order compliance rate metric can also be made.

**Minor Issues:**

1. The paper inconsistently uses closing quotes (") instead of opening quotes (``) in multiple locations, including but not limited to lines 197, 203, and 213.

2. Textual citations, rather than parenthetical citations, would be more suitable for the references in lines 117 to 128, enhancing the readability and flow of the text.

3. Appropriate citations are not provided for the original dataset sources.

4. The authors claim to present a _novel framework_ for forecasting that leverages textual instructions and demonstrate its superior performance over existing frameworks in Table 2. However, the claimed novelty of this framework compared to existing methodologies remains unclear. I request the authors to further **elaborate on the framework's uniqueness as compared to the existing methods** and include the **parameter counts for both their model and the benchmarks** to confirm that the improvements are not merely due to higher computational resources.

5. Furthermore, despite the authors' appreciating the raised typographical issues, such issues have continued into the revised sections, with some of them listed below:
    1. Incorrect quotations- line 113
    2. Incorrect parenthetical citations- line 127
    3. Spelling errors- line 107 (_success_ - _sucess_)

### Questions
Questions:
1. The choice of order compliance rate as an evaluation metric is intriguing. This metric appears specifically tailored to the instructions outlined in the paper, which may limit its applicability to real-world scenarios. Could you clarify the advantages this metric offers over existing metrics for evaluating forecasting performance?

Suggestions:

- Benchmark results against a broader selection of existing multimodal forecasting models to enhance comparative insights.
- Include a detailed discussion of the dataset, covering aspects such as sample size, history length, and forecasting horizon.
- If feasible, incorporate more complex textual cues in the experiments to better reflect real-world forecasting challenges.

### Soundness
2

### Presentation
3

### Contribution
2
