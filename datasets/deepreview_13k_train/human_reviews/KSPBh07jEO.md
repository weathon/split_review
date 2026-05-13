# Epistemic Integrity in Large Language Models

- Decision: Reject
- Scores: 3, 3, 3, 6

## Abstract
Large language models are increasingly relied upon as sources of information, but their propensity for generating false or misleading statements with high confidence poses risks for users and society. In this paper, we confront the critical problem of epistemic miscalibration — where a model's linguistic assertiveness fails to reflect its true internal certainty. We introduce a new human-labeled dataset and a novel method for measuring the linguistic assertiveness of Large Language Models (LLMs) which cuts error rates by over 50\% relative to previous benchmarks. Validated across multiple datasets, our method reveals a stark misalignment between how confidently models linguistically present information and their actual accuracy. Further human evaluations confirm the severity of this miscalibration. This evidence underscores the urgent risk of the overstated certainty LLMs hold which may mislead users on a massive scale. Our framework provides a crucial step forward in diagnosing this miscalibration, offering a path towards correcting it and more trustworthy AI across domains.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses an issue in the deployment of large language models (LLMs): epistemic miscalibration, where a model’s expressed confidence does not match its internal certainty, often resulting in overconfident yet potentially misleading statements. With some very simple methods for determining internal and expressed uncertainty, the paper shows that there is a misalignment.

### Strengths
The paper is looking to address an increasingly relevant issue, as LLMs are being used in fields where overconfidence or miscommunication can lead to real-world consequences (e.g., healthcare, misinformation mitigation).

The human survey component helps bridge the gap between computational model outputs and user perceptions, adding empirical support to the authors' claims about miscalibration risks.

### Weaknesses
The primary evaluation focuses on assertiveness in a limited context of misinformation detection.

There are a number of over-claims in the paper, especially at the end of the introduction and related work. There are several papers which have demonstrated the misalignment between internal and expressed uncertainty and even aligning the two, e.g. https://arxiv.org/pdf/2404.00474 and a few others. The authors should do a better literature review.
The research gaps presented in lines 91-102 are not substantiated.

The connection with human-centered approach is weak. So it is not clear what this paper's contribution is: is it demonstrating the misalignment between internal and expressed uncertainty, or aligning the two, or the human-centered aspect? It would be better if the paper focused on one of these in a deep manner.

### Questions
NA

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper tackles epistemic miscalibration in LLMs, which indicates the gap between the models' linguistic assertiveness and their internal certainty. To address this, the authors introduce a human-labeled dataset and a new metric for measuring linguistic assertiveness, reducing error rates by over 50% compared to previous methods. Human evaluations highlight a significant gap between models’ assertive language and actual accuracy.

### Strengths
The miscalibration issue in LLMs is an important and interesting topic

### Weaknesses
-  How to calculate internal certainty and linguistic assertiveness is not explained clearly in sec 3.2, this is the core part of the paper. Just referring to previous paper is not a good manner, as the paper should be self-contained.
- The authors claim that *they introduce a new human-labeled dataset*, while I didn't find how this dataset was constructed and its statistics.
- The authors claim that *they introduce a novel method for measuring the linguistic assertiveness*, while I didn't find how their method in sec 3.2 was different from previous ones, instead, it seems they were using previous methods.

### Questions
- The structure of this paper a bit confusing, e.g., in sec 3, dataset and models appear before the method is explained, sec 5 and sec 6 should be merged.
- Which result shows that the method cuts error rates by over 50% relative to previous benchmark mentioned in abstract? There's only results of MSE in the experiments.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces the concept of "epistemic calibration" in LLMs, addressing the misalignment between a model's internal certainty and its linguistic assertiveness in outputs. The authors develop a new framework to measure linguistic assertiveness and demonstrate significant miscalibration in current LLMs, showing that models often express high confidence in their outputs even when their internal certainty is low.

### Strengths
1. Clearly identifies and formalizes an important problem in LLM deployment.
2. Introduces a framework for understanding epistemic calibration through internal and external certainty.

### Weaknesses
1. The layout and writing of the paper are little bit hard to follow. (eg. 1. Line 41 directly references "Figures 1 and 5" which appear to be in the appendix without proper indication. 2. Inconsistent decimal point precision in tables (e.g., Table 1). 3. Full-page figure on Page 10 breaks the flow of the text. 4. mark "*" in Table 2). Moreover, There may be some issues with the template used, such as the author column being centered.
2. The choice of using only Llama-3.2-1B-Instruct fine-tuned with LoRA as representation is somewhat unusual with justification for this specific choice. This work would benefit from including results from other Llama variants (3B, 8B) to study potential scaling law effects on epistemic calibration. 
3. The paper relies on the method from [1] to measure internal certainty. However, it's important to note that there is no true ground truth for internal certainty - it can only be measured through indirect methods. There are numerous proposed approaches in the literature [2-5] for measuring internal certainty (e.g., logits, training probabilities). While the authors acknowledge the challenges of measuring internal certainty in Lines 186-191, they fail to provide adequate justification for why the method from [1] is superior to other available approaches. The lack of comparative analysis or explanation for their methodological choice weakens the paper's foundation for measuring internal certainty.
4. The "Empirical Evidence of Epistemic Miscalibration" (Main Contribution 2) merely confirms what is already a widely acknowledged phenomenon in the field, as detailed in [2, 6, 7]. In light of these concerns, a more comprehensive discussion of potential solutions is warranted. The authors should expand upon possible methodological approaches and practical strategies for addressing the identified epistemic calibration issues, which would strengthen the paper's contribution beyond problem identification.

[1] Combining Confidence Elicitation and Sample-based Methods for Uncertainty Quantification in Misinformation Mitigation

[2] CAN LLMS EXPRESS THEIR UNCERTAINTY? AN EMPIRICAL EVALUATION OF CONFIDENCE ELICITATION IN LLMS

[3] Confidence Under the Hood: An Investigation into the Confidence-Probability Alignment in Large Language Models

[4] Factual Confidence of LLMs: on Reliability and Robustness of Current Estimators

[5] A Survey of Confidence Estimation and Calibration in Large Language Models

[6] A Survey on the Honesty of Large Language Models

[7] Can Large Language Models Faithfully Express Their Intrinsic Uncertainty in Words?

### Questions
Refer to Weaknesses

### Soundness
2

### Presentation
2

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
This paper investigates the differences between internal and external certainty as measured in language models (LMs). The authors clearly differentiate these two conceptual types of certainty, each supported by a solid body of literature, and explore whether these measures are consistent, as one could hope. Their findings indicate a low correlation between the two, raising concerns about the reliability of certainty assessments derived from LMs.

The authors thoroughly survey relevant literature, carefully defining and explaining essential terms, which strengthens their argument about the inconsistency between internal and external certainty. Internal certainty, often measured by the probabilities a model assigns to an answer relative to alternatives, contrasts with external certainty, which is typically gauged by linguistic attributes of the generated answer. While internal certainty has received more research attention, external certainty is more intuitive and accessible for end-users, making the weak correlation between these measures particularly noteworthy.

The study uses a newly curated dataset to train models for estimating external certainty and applies an existing approach for internal certainty estimation. The primary results, based on their highest-performing model, underscore the weak correlation between the two metrics.

Overall, this paper tackles an important research question and presents intriguing findings. While I found no major flaws, there are several areas where further refinement could strengthen the work, outlined below.

Conclusive, Extensive Results for the Claims
------

The authors argue that internal and external certainty are distinct conceptual metrics, with the former being more complex to measure. However, they only test one internal certainty method, from Rivera et al., 2024. To support the broad claims made, additional methods for estimating internal certainty should be evaluated to rule out the possibility that this inconsistency arises from the limitations of a single method.

Writing
------

While the paper is generally well-organized, certain sections would benefit from a rewrite to enhance clarity and add detail.

The lack of a dedicated background/related work section is noticeable. The paper contains comprehensive background material, but it is interspersed across different sections, making it hard to delineate the authors’ contributions from previous work. Separating this content could enhance readability. For example, lines 73-102 in the introduction and lines 177-185 include related work content. The first paragraph of Section 2.2 also repeats related work. Consolidating this information in a single section could make room for additional details where they are currently lacking.

Other areas that could benefit from elaboration include the collected labels/data used to train the external certainty model. Providing a few sample data points would help readers understand the data domain better. Similarly, the setup for training the external certainty model lacks clarity. Details on how the dataset is split into training, validation, and test sets would be helpful.

Additionally, the dataset for this research is derived from news articles dating back at least seven years, based on a 2017 paper. Some information may now be factually outdated, potentially influencing the paper’s conclusions. This consideration warrants a brief discussion. Moreover, in line 296, the reference to Rivera et al. 2024 should specify which method was used for internal certainty measurement, as they employ multiple methods; detailing this would improve transparency.

Additional Writing Comments
-----
Note: these are not as important for the overall assessment, but the authors should consider them for their revision

- Line 270: Replace “coder” with “annotator,” a more standard term.
- Line 271: Specify whether the 800 data points were sampled from each source or in total.
- Line 273: Instead of “around 0.7,” provide the exact value.
- Line 303: Explicitly state which model performed best.
- Line 314: Indicate the exact gap in performance.
- Figure 2: Replace the legend with model names on the x-axis ticks for clarity.
- Table 1: Consider adding an average score.
- Section 6: This could be a subsection of Section 5.
- Line 442: Expanding the discussion of this result in the text would be beneficial.
- Line 446: The described correlation is moderate, not strong.
- Line 469: Add a citation for “silicon sampling,” as this term isn’t standard.
- Figure 4a: Ensure the tick values are clearly indicated on the top figure.

### Strengths
- The paper poses an intriguing question about the connection between internal and external certainty in language models.
- It provides interesting results, highlighting the need for further work on reliable certainty estimation.

### Weaknesses
- The experiments are limited,relying on a single certainty estimation method, leading to overstatements of the findings.
- The writing could benefit from added detail and examples to enhance clarity.

### Questions
1. Lines 47 and 51: What distinguishes the bullet points in these lines? They appear very similar to me.
2. Line 113: What specific “risk” is being referred to here? Do you believe it represents a substantial risk? Could you elaborate?
3. Internal Certainty Calculations: Internal certainty is derived using multiple generations or answers. Are multiple generations also considered in the calculation of external certainty, or only a single one? The exact calculation method for external certainty isn’t entirely clear.
4. Line 270: What qualifies the three annotators as experts? Experts in what? Is there any difference in agreement between experts and non experts?
5. How were the experts/non experts recruited? How much were they paid?
6. Figure 2: How is it possible for the MSE to exceed 1? Aren’t the values between 0-1?
7. Line 414: Where do these statements originate from?
8. The data used from Wang, 2017 is at least 7 years old. Did you consider some of the statements there to be factually incorrect anymore?

### Soundness
3

### Presentation
3

### Contribution
3
