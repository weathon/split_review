# ER2Score: An Explainable and Customizable Metric for Assessing Radiology Reports with LLM-based Rewards

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 3, 6

## Abstract
In recent years, the automated generation of radiology reports (R2Gen) has seen considerable growth, introducing new challenges in evaluation due to its complex nature. Traditional metrics often fail to provide accurate evaluations due to their reliance on rigid word-matching techniques or their exclusive focus on pathological entities, leading to inconsistencies with human assessments. To bridge this gap, we introduce ER2Score, an automatic evaluation metric designed specifically for R2Gen that harnesses the capabilities of Large Language Models (LLMs). Our metric leverages a reward model and a tailored design for training data, allowing customization of evaluation criteria based on user-defined needs. It not only scores reports according to user-specified criteria but also provides detailed sub-scores, enhancing interpretability and allowing users to adjust the criteria between clinical and linguistic aspects of reports. Leveraging GPT-4, we generate extensive evaluation data for training based on two different scoring systems, respectively, including reports of varying quality alongside corresponding scores. These GPT-generated reports are then paired as accepted and rejected samples to train an LLM towards a reward model, which assigns higher rewards to the report with high quality. Our proposed loss function enables this model to simultaneously output multiple individual rewards corresponding to the number of evaluation criteria, with their summation as our final ER2Score. Our experiments demonstrate ER2Score's heightened correlation with human judgments and superior performance in model selection compared to traditional metrics. Notably, our model's capability to provide not only a single overall score but also scores for individual evaluation items enhances the interpretability of the assessment results. We also showcase the flexible training of our model to varying evaluation systems. We will release the code on GitHub.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This study proposes ER2Score, an evaluation framework for automated radiology report generation, grounded in the RadCliQ and MRScore scoring systems. To address the limitations of traditional metrics, ER2Score leverages pairs of “accepted” and “rejected” reports with corresponding scores obtained from GPT-4. These pairs are then used to train a Llama3 model, allowing it to assign quality scores to individual reports during inference. ER2Score demonstrates the potential to capture the semantic content and clinical significance of radiology reports, achieving a high correlation score with human evaluations. The authors suggest that this method offers a more fine-grained assessment compared to existing evaluation approaches. 

However, while ER2Score builds on RadCliQ and MRScore, the improvements remain incremental, potentially limiting its overall contribution.

### Strengths
1. Development of a Model with Strong Human Alignment: ER2Score demonstrates high alignment with human evaluations by employing GPT-4 to generate high- and low-quality report samples for a large set of ground truth reports, with GPT-4 assigning scores based on the RadCliQ and MRScore evaluation criteria. These scored pairs are then used as input for training Llama3, introducing a structured approach to calculating both total and individual scores, resulting in a model that closely aligns with human assessments.

2. Rad-100 Dataset for Comprehensive Evaluation: The Rad-100 dataset, comprising 100 reports scored by an experienced radiologist following the MRScore framework, was created to provide additional validation of ER2Score’s effectiveness.

### Weaknesses
1. This study builds on RadCliQ and MRScore, yet the improvements are minimal, with only slight modifications to the loss function, making it difficult to view ER2Score as a truly fine-grained evaluation metric. Additionally, the customization feature highlighted as a key contribution lacks sufficient experimental support, with limited results in Table 2 that do not fully demonstrate its claimed flexibility.

2. The study would benefit from evaluating state-of-the-art models using ER2Score, providing further evidence of its practical advantages beyond metric-to-metric comparisons.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces ER2Score to automated radiology report generation evaluation. 
ER2Score utilizes a reward model based on GPT-4, for more nuanced and human-aligned evaluations, and provides sub-scores across various criteria. The authors also train a reward model using ER2score.

### Strengths
- ER2Score provides detailed sub-scores for specific report components, making it easier to identify deficiencies in generated reports.
- The metric is highly agreeable with human evaluation standards

### Weaknesses
 - Testing is restricted to a narrow set of benchmarks on a total of 200 + 100 reports, which is quite small and introduces concerns of overfitting.
- ER2Score bases its scoring criteria on established scoring systems like RadCliQ and MRScore, which are limited in scope and may not fully encompass the complexity of radiological reporting. The model lacks flexibility to adapt to other or emergent scoring needs without significant retraining.
- ER2Score's accuracy varies across sub-criteria, performing well on some (e.g., omission of findings) but poorly on others (e.g., location or position accuracy). More in-depth analysis would be interesting to see why this is the case.
- Margin-based scoring criteria for distinguishing between accepted and rejected reports is interesting, but lacks an in-depth analysis of the impact of margin size on model sensitivity. Margin thresholds should be rigorously analyzed for borderline cases.

### Questions
See weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the limitations of traditional metrics for evaluating automated RRG and introduces ER2Score, a metric based on LLMs. ER2Score attempts to improve evaluation accuracy by using a reward model that can be tailored to user-defined criteria and provides detailed sub-scores for enhanced interpretability.

### Strengths
Many experiments and ablation studies. Nicely presented paper with clear figures and methodology. I commend the authors for doing many experiments and evaluation studies to validate their metric.

### Weaknesses
It seems like the candidate metrics selected for comparison are not the most recent ones or relevant ones, especially given ER2Score's LLM-based nature. It is expected for ER2Score to outperform the traditional lexical/semantic/factuality metrics; however, I cannot judge on its performance without comparisons to other more recent LLM-based metrics for RRG.

I recommend the authors do experiments with GREEN (https://arxiv.org/html/2405.03595v1), FineRadScore (https://arxiv.org/html/2405.20613v2), and G-Rad (https://arxiv.org/html/2403.08002v2), as these are more relevant. They also use similar ReXVal dataset and error counts, as well as correlation evaluation with Kendall's Tau.

### Questions
Recommend authors do further comparison and validation studies with the suggested metrics to fully demonstrate/prove that ER2Score is superior.

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
This paper introduces ER2Score, a novel metric for evaluating automated radiology report generation. ER2Score leverages LLMs, specifically GPT-4 and Llama 3, to address the limitations of existing metrics that rely on n-gram overlap or predefined clinical entities. 

GPT-4 generates training data by scoring synthetically generated reports against reference reports based on predefined customizable criteria (RadCliQ and MRScore). Llama 3 is then LoRA fine-tuned as a reward model to predict sub-scores for each criterion, which are summed to produce the final ER2Score. The authors claimed ER2Score's improved correlation with human judgments and superior model selection capabilities compared to traditional metrics on two datasets.

### Strengths
The generation of sub-scores for individual evaluation criteria offers valuable insights into report quality, potentially better interpretability, and potentially enabling targeted improvements.

The ability to train the metric with different scoring systems (RadCliQ and MRScore) demonstrates flexibility and adaptability to diverse evaluation needs.

### Weaknesses
The relatively small size of the evaluation datasets (ReXVal and Rad-100) raises concerns about the generalizability of the results. Larger-scale evaluations are needed to validate the robustness of ER2Score.

Relying on GPT-4 generating training data, certain combinations of sub-scores might be rare, leading to data sparsity issues. This can hinder the model's ability to learn effectively and generalize to unseen examples, affecting convergence. Also, introduce a performance cap. 

The supplementary material provides example prompts, but more details on the prompt engineering process and its impact on GPT-4's scoring would be beneficial. How sensitive is the performance to prompt variations?

Lacking inter-human agreement.

### Questions
How sensitive is ER2Score to the quality of the ground truth reports used for training and evaluation?

What are the computational costs associated with training and using ER2Score? How does it compare to other metrics?

What are the limitations of using reward modeling for this task? Is the reward guaranteed to converge due to the multi-dimensionality of the grading criteria? 

Other: 

line 77, citation (Meta, 2024) missing space afterward.

line 142, 143 "Kendall's tau of 0.735" - needs to be consistent capitalization: "Kendall's Tau."

Really inconsistent capitalization on Dataset: for example, line 288 "ReXVal Dataset" but "MIMIC dataset" on following lines.

Various instances: Inconsistent capitalization of "RadCliQ" and "MRScore."

And many awkward phrasings. Careful proofreading and editing are required going further.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a method for training language models to evaluate generated radiology reports across a variety of metrics. The authors create a dataset of generated radiology reports of varying quality and train a reward model to assign scores to radiology reports using this “ground-truth” data, producing fine-grained evaluations across a range of relevant sub-categories. The authors find that their approach produces results that align better with radiologists than other common approaches. As new approaches to automated radiology report generation are developed, this approach could be an effective method of generating quick feedback on the effectiveness of these approaches.

### Strengths
The approach is well motivated taking an approach to evaluation that can score reports across a range of clinically valid dimensions. The described loss function seems mathematically sound with different terms well justified and the usage of human evaluation when scoring the method is important in validating the approach beyond automated metrics.

### Weaknesses
Despite the method outperforming other approaches, the final performance of ER2Score still seems fairly low. The manuscript needs more justification in light of this low performance to justify why this method will still be useful. It would also be useful to study the ReXVal criteria where performance was particularly low in more detail, to understand why agreement with radiologists might have been poor.

Additionally, there were areas where the approach was unclear and requires more clarification. Please see the questions.

### Questions
* The sample-size of 50 used to validate/spot-check the model generated radiology reports is fairly low. Did the authors perform any kind of power analysis to verify that this is a sufficiently large sample to validate their automated report generation process?
* I’m not sure I fully understand the pairing rule. From figure 2 it appears that each report in a predicted report pair was also paired with the ground-truth report? Is this the case or did a pair simply consist of 2 predicted reports? If the former then what was the reason for also providing the ground-truth report?
* For the Rad-100 dataset was there a 1-to-1 correspondence between a report in the dataset and ground-truth MIMIC report it was based on? Or are there several reports based on a single report?
* In Table 1 what does Total mean? These values seem very different to the individual criteria score
* How are our NLG metrics computed for table 2? Are these based on BLEU/ROUGE between the generated report and a ground-truth report?

### Soundness
3

### Presentation
2

### Contribution
2
