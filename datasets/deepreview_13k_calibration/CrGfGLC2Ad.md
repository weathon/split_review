# Discovering Factor Level Preferences to Improve Human-Model Alignment

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
Despite advancements in Large Language Model (LLM) alignment, understanding the reasons behind LLM preferences remains crucial for bridging the gap between desired and actual behavior.
LLMs often exhibit biases or tendencies that diverge from human preferences, such as favoring certain writing styles or producing overly verbose outputs. 
However, current methods for evaluating preference alignment often lack explainability, relying on coarse-grained comparisons.
To address this, we introduce PROFILE (PRObing Factors of InfLuence for Explainability), a novel framework that uncovers and quantifies the influence of specific factors driving preferences. 
PROFILE's factor level analysis explains the ``why'' behind human-model alignment and misalignment, offering insights into the direction of model improvement.
We apply PROFILE to analyze human and LLM preferences across three tasks: summarization, helpful response generation, and document-based question-answering. 
Our factor level analysis reveals a substantial discrepancy between human and LLM preferences in generation tasks, whereas LLMs show strong alignment with human preferences in evaluation tasks.
We demonstrate how leveraging factor level insights, including addressing misaligned factors or exploiting the generation-evaluation gap, can improve alignment with human preferences.
This work underscores the importance of explainable preference analysis and highlights PROFILE's potential to provide valuable training signals, driving further improvements in human-LLM alignment.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the preference discrepancy between human judgment and model judgment. Specifically, it investigates three RQs using a unified framework, PROFILE, to understand and enhance preference alignment at a fine-grained level (length, hallucination, etc). The authors conduct experiments on three datasets across two settings, and the results suggest misalignment in the generation setting. Their analysis highlights the potential of the proposed model to further improve alignment.

### Strengths
The idea of `enhancing' alignment by better understanding the preference discrepancy between human and model judgment through more fine-grained factors is both interesting and important.


Their findings and insights could be valuable for researchers interested in human alignment, LLMs, and explainable AI.


I liked the overall organization of the paper, which consistent with the state of the field.

### Weaknesses
The paper would benefit from more precise notation to improve clarity. I found the notation to be inconsistent and, at times, confusing, which impacts readability. For example:

- L134-135: The notation of score level s and Score(r) is confusing. If Score(r) already equals s, what is the purpose of having the model assign a score again?

The writing quality could also be improved. The core value of this paper lies in the exploration of the preference discrepancy between human and model judgment, yet the novelty and key ideas are not clearly articulated. Some concepts and terms are introduced without sufficient explanation, leading to confusion. For example:

- L40-41: “considering their alignment not only as generators but also as evaluators becomes crucial”

A better discussion and analysis are needed. Some findings and conclusions lack depth and specificity. For example:

- L471: "… engage in reward hacking by generating overly lengthy outputs…"  it is unclear how these conclusions were reached. The proposed method does not appear to involve RLHF/DPO training (correct me if I’m wrong).

The so-called "generalizability" conclusion seems to be derived solely from the summarization experiment, which may not provide sufficient support.”

### Questions
What factors should we consider regarding preference discrepancies in other tasks, such as math and coding?

Aside from reward models, how do you think RLHF/DPO contributes to alignment?

### Soundness
2

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
4

### Summary
This paper introduces a framework called PROFILE, designed for fine-grained factor analysis of LLM alignment. PROFILE reveals the discrepancies between human and AI preferences, pinpointing specific areas of divergence. By quantifying the influence of various factors, this framework provides new insights into the interpretability and improvement of models.

### Strengths
- **Comprehensive Analysis from a Unique Perspective**: The paper conducts a detailed analysis of the underlying factors affecting human and AI preferences, providing a comprehensive view into the mechanisms of preference alignment.
- **Interpretability**: By performing factor-level preference analysis, PROFILE helps identify specific reasons for human-model preference divergence, offering clear directions for model optimization.

### Weaknesses
 - **Unclear Justification for Multi-level Factor Classification**: While the paper proposes a three-level factor classification system, it does not sufficiently explain the basis for each factor level, the scientific soundness of the classification, or its handling of task complexity. This raises concerns about whether the framework can accurately reflect human-model preference differences. Specifically, the criteria for distinguishing between levels, and the rationale for the number of levels is not well-defined, making it difficult to assess the framework's validity. The lack of a clear, theoretically grounded approach to factor classification undermines the interpretability of the results.
- **Potential Issues in the Analytical Approach**: The study uses GPT-4o for factor quantification while examining human-AI preference alignment, which may introduce new biases, potentially affecting the objectivity of the analysis. The reliance on a single model for factor quantification, without exploring alternative methods or validating against human judgments across a diverse set of cases, raises concerns about the robustness of the findings. The potential for systematic biases in GPT-4o's factor assessments could skew the results and limit the generalizability of the conclusions.
- **Limitations in Experimental Design**: The paper validates the PROFILE framework on a limited set of public datasets, which restricts its demonstration of applicability to other tasks. Moreover, it lacks sufficient ablation studies to analyze the contribution of each factor, making it difficult to understand their impact across tasks. The limited dataset scope does not adequately demonstrate the framework's applicability to diverse tasks and contexts. The absence of ablation studies makes it challenging to isolate the influence of individual factors on overall preference alignment, hindering a deeper understanding of the framework's mechanisms.
- **Weak Correspondence between Results and Conclusions**: Although the experiments showcase preference alignment in some tasks, they lack clear methodological and empirical support for guiding improvements in human-AI alignment. The paper does not clarify how PROFILE contributes to enhancing model performance or its impact on generation quality in practical applications. The connection between the observed preference alignment and practical improvements in model behavior is not clearly established. The paper fails to demonstrate how the insights gained from PROFILE can be translated into concrete strategies for enhancing model performance or generation quality.
- **Over-reliance on Quantitative Metrics in Analysis**: The paper's analysis mostly depends on correlation and quantitative scores, lacking qualitative insights into why the model exhibits inconsistencies with human preferences for certain factors. This approach results in a somewhat superficial view that fails to reveal the deeper reasons behind the observed divergences. The exclusive reliance on quantitative metrics limits the depth of analysis, neglecting the nuanced, qualitative aspects of human preferences. The lack of qualitative analysis prevents a thorough understanding of the underlying reasons for the observed discrepancies between human and model preferences.

### Questions
1. I am curious about the correlations between different factors. Could you provide an analysis on this?

### Soundness
2

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
4

### Summary
This paper introduces PROFILE, a framework designed to uncover and quantify the specific factors influencing both human and LLM preferences in language generation tasks. It addresses the problem of misalignment between LLM outputs and human preferences by providing a granular, factor-level analysis rather than relying on coarse-grained comparisons. The main contributions include the development of PROFILE, its application across three tasks (TLDR summarization, helpful response generation, and WebGPT document-based QA), and demonstrating how factor-level insights can improve human-LLM alignment

### Strengths
● The paper presents an explainable framework that enhances understanding of human-model preference alignment at a granular level.
● It addresses a significant gap in current methods by focusing on specific factors influencing preferences, which can guide improvements in LLM training.
● Demonstrating that leveraging factor-level insights can improve alignment has practical implications for developing more human-aligned LLMs.

### Weaknesses
● The paper might not thoroughly compare with existing methods, leaving questions about its relative advantages.
● The paper may lack sufficient empirical validation due to limited experiments or datasets, potentially affecting the generalizability of its conclusions. 
● There might be concerns about the scalability of the proposed framework without fine-grained human annotations, impacting its practicality.

● The boundary between Receptiveness / Intent Align / Helpfulness is vague and not independent of each other.

### Questions
1. How does your approach compare quantitatively and qualitatively with existing methods in preference alignment? Such as all kinds of llm-as-a-judge methods / G-Eval / ... etc

2. Can you provide more details on how the framework performs when applied to tasks beyond the three studied, and are there limitations to its generalizability? Such as creative writing, role-playing, and coding.

3.  The boundary between Receptiveness / Intent Align / Helpfulness is vague and not independent of each other.

### Soundness
3

### Presentation
3

### Contribution
3
