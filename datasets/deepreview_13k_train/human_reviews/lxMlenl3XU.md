# An Empirical Study on Reconstructing Scientific History to Forecast Future Trends

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
The advancement of scientific knowledge relies on synthesizing prior research to forecast future developments, a task that has become increasingly intricate. The emergence of large language models (LLMs) offers a transformative opportunity to automate and streamline this process, enabling faster and more accurate academic discovery. However, recent attempts either limit to producing surveys or focus overly on downstream tasks. To this end, we introduce a novel task that bridges two key challenges: the comprehensive synopsis of past research and the accurate prediction of emerging trends, dubbed $\textit{Dual Temporal Research Analysis}$. This dual approach requires not only an understanding of historical knowledge but also the ability to predict future developments based on detected patterns. To evaluate, we present an evaluation benchmark encompassing 20 research topics and 210 key AI papers, based on the completeness of historical coverage and predictive reliability. We further draw inspirations from dual-system theory and propose a framework $\textit{HorizonAI}$ which utilizes a specialized temporal knowledge graph for papers, to capture and organize past research patterns (System 1), while leveraging LLMs for deeper analytical reasoning (System 2) to enhance both summarization and prediction. Our framework demonstrates a robust capacity to accurately summarize historical research trends and predict future developments, achieving significant improvements in both areas. For summarizing historical research, we achieve a 18.99% increase over AutoSurvey; for predicting future developments, we achieve a 10.37% increase over GPT-4o.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes Dual Temporal Research Analysis (DTRA), a task that combines the synthesis of historical research with the prediction of future trends. The authors highlight the limitations of existing methods that tend to focus solely on retrospective reviews or isolated future forecasting, which fails to provide a holistic understanding of scientific trajectories. To address this, they introduce HorizonAI, a framework inspired by Dual-System Theory. In HorizonAI, "System 1" uses PaperTKG, a temporal knowledge graph, to organize historical research efficiently, while "System 2" employs large language models (LLMs) for in-depth reasoning and analysis. This dual approach allows HorizonAI to create both historical narratives and predictive insights, bridging the gap between past knowledge and future possibilities.

The paper emphasizes the novelty of DTRA in its ability to capture and validate research trajectories over time, especially within fast-evolving domains like AI. To evaluate the framework, the authors introduce ResBench, a benchmark designed to assess HorizonAI's performance in two main areas: historical completeness and predictive reliability. ResBench includes a set of topics, covering 20 research areas and 210 key AI papers. HorizonAI reportedly outperforms baseline models, including AutoSurvey and GPT-4o.
The HorizonAI framework's methodology involves constructing PaperTKG to dynamically store historical research data and relationships through a structured graph. This graph construction is guided by a systematic process of data retrieval, entity extraction, and augmentation to form a coherent research timeline. For prediction, the authors use LLMs with chain-of-thought reasoning, allowing the model to detect research patterns and hypothesize future directions based on established trajectories. This combination of structured historical data with LLM reasoning enables HorizonAI to improve both in capturing research milestones and in generating contextually relevant forecasts.

However, this paper has many limitations, including a restricted focus on AI topics and a dependence on HTML sources from arXiv, which could limit HorizonAI’s generalizability across other scientific fields. Additionally, while the predictive accuracy is evaluated using LLM scoring, the absence of expert evaluations means that some aspects of practical feasibility and relevance may not be fully captured. The evaluation dataset is also too small.

### Strengths
1) By integrating historical synthesis with future predictions, this paper addresses an important need in scientific forecasting, especially in fields where understanding past trends is key to predicting future developments.
2) The use of structured data organization and LLM reasoning enhances both the accuracy of historical narratives and the relevance of future predictions.
3) The introduction of benchmark data ResBench allows for rigorous and public evaluation.

### Weaknesses
1) Focusing only on AI topics restricts the applicability to other scientific fields. The current implementation, which relies on specific data structures and entity recognition models trained on AI literature, may not generalize effectively to domains with different terminologies and research patterns, such as biology or chemistry. The lack of demonstrated adaptability raises concerns about the true domain-agnostic nature of the proposed framework.
2) Predictions lack expert review, relying solely on LLM scoring, which may reduce result reliability. The evaluation process, which uses LLM-generated JSON outputs compared against target subtitles, is insufficient to capture the nuances of scientific forecasting. The absence of expert validation means that the practical relevance and feasibility of the predicted research directions are not adequately assessed, potentially leading to inflated performance metrics.
3) Dependence on HTML-based arXiv sources limits data diversity, reducing historical coverage robustness. The reliance on a single source, particularly one that primarily hosts pre-prints, introduces a bias towards more recent and potentially less rigorously peer-reviewed work. This could lead to an incomplete and skewed representation of the historical research landscape, especially in fields where archival publications and conference proceedings are crucial.

### Questions
1) Since the problem of synthesizing and forecasting scientific literature is not new, how does HorizonAI improve upon or differ from established pre-LLM methods?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes HorizonAI, a future research trend forecasting framework inspired by the dual-system theory. In HorizonAI, the Paper2Graph algorithm, which mimics System 1, transforms existing research into temporal knowledge graphs. After that, LLM is leveraged as System 2 for both summarization and prediction through grounded analytical reasoning. The authors collected papers from the arXiv repository, covering 9 distinct topics, and designed a tasked named Dual Temporal Research Analysis. Experimental results on the newly introduced dataset demonstrate that HorizonAI is able to outperform some existing benchmark models, such as AutoSurvey on  summarizing historical research and GPT-4o on predicting future developments, respectively.

### Strengths
- Forecasting future trends in research with the help of LLM is an important topic with many potential downstream applications and high impacts.

- The use of a dual-system theory inspired workflow is theoretically sound and works well empirically.

### Weaknesses
 - The paper is missing a few references [1-4]. These papers are highly relevant to the current paper, and should be cited and discussed about how they relate to and different from the current paper.

- HorizonAI is only compared against AutoSurvey and GPT-4o. The authors should also compare HorizonAI against other existing models such as the ones in [1-4].

- The paper lacks sufficient ablation study. For example, how much performance degradation would there be if HorizonAI does not employ a dual-system theory inspired workflow?

### Questions
Why are the 9 distinct topics used in data collection all related to LLM? How is the generalizability of HorizonAI beyond the domain of LLM-related research?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces Dual Temporal Research Analysis (DTRA), a task that unifies historical research analysis with future trend forecasting to enhance scientific discovery. The proposed framework (HorizonAI) draws from Dual-System Theory, using a cognitive-inspired model where System 1 organizes research data into a Temporal Knowledge Graph (PaperTKG) to capture historical research patterns, and System 2 employs LLMs for analytical reasoning, facilitating comprehensive historical summarization and accurate trend prediction. The study’s contributions include the DTRA task, the HorizonAI framework, and a new ResBench benchmark to evaluate performance based on historical completeness and predictive accuracy, with experiments across 20 topics and 210 AI papers demonstrating improved capacity of HorizonAI over existing methods for summarizing historical trends and forecasting future developments.

### Strengths
S1: The paper introduces a novel task (DTRA) that uniquely combines historical research analysis with forecasting future trends.
  
S2: The paper presents a dual-system cognitive-inspired methodology with comprehensive experiments and the robust ResBench benchmark to validate historical completeness and predictive reliability.
  
S3: The paper offers an interesting approach for automating research synthesis and trend prediction.

### Weaknesses
W1. The contribution of this paper appears limited. The authors claim that "most existing approaches either concentrate on retrospective literature reviews (Wang et al., 2024; Agarwal et al., 2024) or focus solely on generating novel research ideas (Si et al., 2024; Baek et al., 2024). These narrow approaches neglect the essential integration of synthesizing past research with projecting future developments, a combination that is increasingly crucial for scientific discovery. To address this gap, we propose a novel task that unifies the analysis of past research with the forecasting of future trends." In my opinion, the contribution of this paper is not a combination of (Wang et al., 2024; Agarwal et al., 2024) and (Si et al., 2024; Back et al., 2024). The contribution of (Wang et al., 2024) is devising a model to write survey paper with the help of LLM, while (Agarwal et al., 2024) proposes a web system to enhance the paper searching results thereby reducing the time and effort for literature review. However, this paper just uses a knowledge graph to summarize historical papers, the contribution of which is less significant and distinct from these two works. Its main contribution is inferring future research trends through the summary of historical topics, inspired by human cognitive processes.

W2. The significance of this paper is not clearly articulated. While the authors highlight the importance of synthesizing past insights to drive future advancements, they fail to clearly convey the benefits of predicting future research. For example, what real-world benefits could this model offer? What specific real-world problems does it aim to address?

W3. The reliability of the evaluation metric is unverified. The paper introduces a score for assessing predictive reliability from perspectives such as semantic similarity, innovation and feasibility, temporal consistency, and contextual consistency. However, these calculations rely solely on LLMs without human verification, making the use of a model-generated score as an evaluation metric seem unreliable, given that the model itself is not explainable.

W4. The metrics used to compare the performance of HorizonAI and AutoSurvey are not detailed. Specifically, how are "citation overlap" and "key citation overlap" calculated and defined?

W5. The experiments presented in the paper are insufficient. A similar work mentioned, Si et al. (2024), is not compared in the experimental section. 

W6. Experimental details are lacking. For instance, an LLM is used as the baseline in Table 3, yet specific details about the LLM are missing and should be provided. Additionally, given the wide variety of LLMs released, comparing these with HorizonAI would further substantiate the findings.

### Questions
Q1. What is the novel contribution of this paper as compared to that of Wang et al. (2024) and Si et al. (2024)?
Q2. Why is this paper significant from the perspective of real-world needs?
Q3. Can you introduce each evaluation metric used in the experiments clearly?
Q4. Is it possible to compare HorizonAI with Si et al. (2024) experimentally?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces "HorizonAI," a framework combining historical research summarization with predictive trend analysis through a method termed Dual Temporal Research Analysis (DTRA). This approach bridges a gap in current methodologies that typically focus only on past reviews or future predictions. HorizonAI uses temporal knowledge graphs to capture historical research data, while LLMs with Chain-of-Thought reasoning drive future predictions. The framework is evaluated on a new benchmark, ResBench.

### Strengths
The approach of employing temporal knowledge graphs to track the evolution of literature is reasonable.

The paper is easy to follow.

### Weaknesses
- **Dataset Limitations (ResBench)**: The dataset is limited in size and scope, consisting of only nine data points. Each data point includes a source paper, a survey, and related target papers, all centered on LLMs from 2024. Given this scale and topic restriction, the dataset feels more like a case study than a broad benchmark. I raise concerns about its effectiveness in assessing the framework. The lack of diversity in topics and the small number of instances per topic severely limit the generalizability of the results. A more robust benchmark would include a wider range of research areas and a larger number of instances per area to properly evaluate the framework's performance across different contexts.
- **Lack of Baselines for Historical Completeness**: The evaluation of historical retrieval includes only one baseline (AutoSurvey). This is a retrieval problem. Authors should include additional baselines to establish more comprehensive comparisons, or justify that AutoSurvey is a baseline strong enough so that they do not need to include other baselines. The absence of comparisons to other retrieval methods, such as those based on TF-IDF or graph-based approaches, makes it difficult to assess the relative performance of the proposed method. A more thorough evaluation would include a range of baselines to demonstrate the method's superiority.

- **Issues with Future Prediction Task (Section 4.2)**: 1. **Evaluation**: The evaluation framework in Section 3.2.2 appears handcrafted, with no clear rationale for certain design choices. The explanations for the scoring ranges lack clarity, and the weighting criteria for each score component are not discussed. The lack of a clear methodology for determining the weights in the evaluation equation raises concerns about the validity of the evaluation results. 2. **Baseline**: The baseline model is not clearly introduced in the main text. The absence of a clear description of the baseline model makes it difficult to understand how the proposed method compares to existing approaches. 3. **Argument for LLM-based Predictions**: The authors suggest that “LLMs can generate more reliable research ideas than those without historical context.” While plausible, this argument feels trivial without further validation or exploration. The claim that LLMs can generate more reliable research ideas requires more empirical support and a more detailed analysis of the underlying mechanisms. The paper does not provide sufficient evidence to support this claim.
- **Disconnect Between Tasks**: The tasks of historical summarization and future prediction appear only loosely related. While conceptually connected, in the paper they are treated as distinct retrieval and generation tasks. For example, how the historical retrieval task might enhance predictive accuracy remains unexplored, leaving important questions about task synergy unanswered. The paper does not provide a clear explanation of how the historical summarization task directly contributes to the future prediction task. The lack of a clear connection between these tasks raises questions about the overall coherence of the proposed framework.

### Questions
Line 272-273, authors mention that “The LLM evaluation consists of three main areas: historical completeness, predictive reliability, and text readability”. However, “text readability” is not included throughout the paper.

### Soundness
2

### Presentation
3

### Contribution
2
