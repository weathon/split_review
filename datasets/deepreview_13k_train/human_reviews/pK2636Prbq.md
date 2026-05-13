# Preference fine-tuning for factuality in chest X-ray interpretation models without human feedback

- Decision: Reject
- Scores: 6, 3, 5, 3

## Abstract
Radiologists play a crucial role by translating medical images into medical reports. However, the field faces staffing shortages and increasing workloads. While automated approaches using vision-language models (VLMs) show promise as assistants, they require exceptionally high accuracy. Most current VLMs in radiology rely solely on supervised fine-tuning (SFT). Meanwhile, in the general domain, additional preference fine-tuning has become standard practice. The challenge in radiology lies in the prohibitive cost of obtaining radiologist feedback. We propose a scalable automated preference alignment technique for VLMs in radiology, focusing on chest X-ray (CXR) report generation. Our method leverages publicly available datasets with an LLM-as-a-Judge mechanism, eliminating the need for additional expert radiologist feedback. We evaluate and benchmark five direct alignment algorithms (DAAs). Our results show up to a 57.4\% improvement in average GREEN scores, a LLM-based metric for evaluating CXR reports, and a 9.2\% increase in an average across six metrics (domain specific and general), compared to the SFT baseline. We study reward overoptimization via length exploitation, with reports lengthening by up to 3.2x. To assess a potential alignment tax, we benchmark on six additional diverse tasks, finding no significant degradations. A reader study involving four board-certified radiologists indicates win rates of up to 0.62 over the SFT baseline, while significantly penalizing verbosity. Our analysis provides actionable insights for the development of VLMs in high-stakes fields like radiology.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a scalable, automated preference alignment technique for chest X-ray (CXR) report generation using publicly available datasets and an LLM-as-a-Judge mechanism. The authors evaluate and benchmark five direct alignment algorithms (DAAs) and show that their approach achieves an overall improvement over the SFT baseline. Additionally, they analyze the alignment tax and clinical implications of the proposed methods.

### Strengths
1. The article is well-motivated and clearly written, making it easy to follow.
2. The authors systematically examine how DAAs can enhance factual accuracy from three perspectives, considering both improvements and potential degradations introduced by DAAs.

### Weaknesses
1. The method for collecting preference data is relatively simplistic. An ablation study on the impact of different metrics used as the Judge for preference data generation would be valuable. Specifically, the current approach relies on a single metric (GREEN) without exploring alternatives, which could lead to biased preference data. The lack of diversity in the preference signal might limit the generalizability of the findings.
2. The use of LLMs for preference data collection without human feedback has been explored in prior work, such as RLAIF[1]. A comparison or discussion between the proposed method and RLAIF would strengthen this study. The current discussion does not adequately address the differences in methodology and potential advantages or disadvantages of each approach, particularly in the context of chest X-ray report generation.
3. As the authors acknowledge, this work focuses on a single model, raising concerns about whether the experimental results adequately support the study's conclusions. The lack of evaluation on other vision-language models (VLMs) limits the generalizability of the proposed approach and raises questions about the robustness of the findings across different architectures and pre-training strategies.

### Questions
Overall, this paper is strong, though it may not fully meet the ICLR criteria. I would consider raising my score if the authors:

1. Compare the impact of metrics beyond GREEN in collecting preference data.
2. Provide a comparative analysis between their method and RLAIF for preference data collection.
3. Conduct additional experiments, such as evaluating their method on other vision-language models (VLMs) like LLM-CXR[1].

[1] Suhyeon Lee, et al. "LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation." In *The Twelfth International Conference on Learning Representations*, 2024.

### Soundness
2

### Presentation
3

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
The paper introduces a scalable preference alignment technique using an automated “LLM-as-a-Judge” mechanism, reducing the cost and complexity of obtaining preference data without requiring expert radiologist feedback.

### Strengths
1.The paper is well-structured overall, with clear and thoughtfully designed figures that effectively illustrate the concepts and results

2.The paper introduces a scalable preference alignment technique using an automated “LLM-as-a-Judge” mechanism, reducing the cost and complexity of obtaining preference data without requiring expert radiologist feedback.

3.The approach leverages Direct Alignment Algorithms (DAAs), showing significant improvements in multiple metrics over SFT baselines, which enhances the accuracy and clinical relevance of the outputs.

4.The model demonstrates consistent performance across various tasks, avoiding the “alignment tax” phenomenon, which further enhances its applicability in high-stakes medical domains.

### Weaknesses
Q1. Please discuss specific theoretical limitations of DAAs that may affect applicability to other medical domains or high-stakes fields beyond medicine. 

Q2.  Specific experiments to test robustness to biased/noisy data are necessary, such as evaluating performance across different age groups or testing with artificially injected label noise.

Q3. How to detect and mitigate potential bias accumulation in the LLM-as-judge approach.

Q4. Please justify the choice of baseline and comparison methods, and suggest 1-2 specific additional relevant baselines you should consider including, explaining why they would be particularly relevant comparisons for this work.

Q5. How does this approach scale in terms of cost and efficiency over time and with larger datasets?

Q6. Please discuss how the proposed approach specifically compares to or differs from Token-level Direct Preference Optimization (TDPO) https://doi.org/10.48550/arXiv.2404.11999, and whether incorporating ideas from TDPO could potentially improve their method.

### Questions
Q1. Please discuss specific theoretical limitations of DAAs that may affect applicability to other medical domains or high-stakes fields beyond medicine. 

Q2.  Specific experiments to test robustness to biased/noisy data are necessary, such as evaluating performance across different age groups or testing with artificially injected label noise.

Q3. How to detect and mitigate potential bias accumulation in the LLM-as-judge approach.

Q4. Please justify the choice of baseline and comparison methods, and suggest 1-2 specific additional relevant baselines you should consider including, explaining why they would be particularly relevant comparisons for this work.

Q5. How does this approach scale in terms of cost and efficiency over time and with larger datasets?

Q6. Please discuss how the proposed approach specifically compares to or differs from Token-level Direct Preference Optimization (TDPO) https://doi.org/10.48550/arXiv.2404.11999, and whether incorporating ideas from TDPO could potentially improve their method.

### Soundness
2

### Presentation
2

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
This paper develops a framework for fine-tuning VLMs without requiring clinician annotation. Using various DAA algorithms, the authors claim to have achieved good performance based on automated scoring metrics. I appreciate their comprehensive study in exploring how different DDA algorithms contribute to model performance, as well as their findings that some RL frameworks exploit the automatic grading system by systematically increasing response length. Overall, the authors have done an excellent job explaining their methodology and results, which provide valuable insights for future research. However, I have questions and concerns about whether this framework genuinely enhances the capacity of VLM models.

### Strengths
*Innovative Framework*: The framework allows fine-tuning VLMs without clinician annotation, addressing a key barrier in medical AI by reducing dependency on expert-labeled data.

*Comprehensive Algorithm Comparison*: The study thoroughly evaluates different DAA algorithms, providing insights into how each algorithm uniquely enhances model performance.

*Detailed Methodology and Evaluation*: The paper offers a clear, thorough explanation of its methods and results, making it a valuable resource for future research in VLM fine-tuning and performance evaluation.

### Weaknesses
1. One major issue is that you used the GREEN score as the judge for your reward model, which introduces bias and makes the comparison less fair. When I evaluate performance without considering the GREEN score, the improvement across other tasks appears somewhat marginal. Additionally, there is evident over-optimization or reward hacking occurring by simply extending response length. I am not convinced this result is sufficiently robust to demonstrate the effectiveness of this method.

2. My primary concern, which raises doubts about this paper, is that DPO and IPO—the two methods with the highest performance in Table 3—are rated the lowest in expert evaluation. It seems insufficient to attribute this discrepancy to verbosity alone negatively impacting human evaluation. There appears to be a more fundamental issue in these responses, leading clinicians to favor responses generated by SFT. For example, the model produces extensive text, some of which is counterfactual. If this is the case, it contradicts the paper’s objective of improving model factuality through RL.

3. Reproducibility. It would be beneficial to make the code public to enhance reproducibility. At a minimum, a clear summary of the DDA algorithms would assist future researchers.

### Questions
1. I don't think general metrics like BERTScore, BLEU-4, and ROUGE-L are particularly helpful here, as they do not assess the factual quality of the response. Consider including these in the supplementary figures.

2. I would like to see more examples to understand why clinicians favor the SFT model. I suspect verbosity is a significant issue, negatively impacting response reliability.

3. A straightforward way to mitigate verbosity issues could be to add a rule-based reward term to DPO, IPO, etc., to see if it improves performance in human ratings. If expert ratings are difficult to get, alternatively, using this method to generally reducing verbosity without affecting evaluation scores could also strengthen the findings. This would be a convincing result that could change my assessment of the paper. 

4. You might also want to cite this paper, the first to perform RLHF fine-tuning in VLM models: Sun, Z., Shen, S., Cao, S., Liu, H., Li, C., Shen, Y., ... & Darrell, T. (2023). Aligning large multimodal models with factually augmented RLHF. arXiv preprint arXiv:2309.14525.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This is an empirical analysis paper based on the CheXagent VLM model, which compares the performance of different alignment methods in preference fine-tuning for medical report generation, including DPO, KTO, SimPO, IPO and OROP.

### Strengths
The article explores the preference fine-tuning pipeline and significantly enhances the GREEN performance through alignment optimization for the VLM based on the GREEN metric, compared to the baseline SFT.

### Weaknesses
1. This is an experimental analysis article, but the generalizability of the experimental conclusions is insufficient, as it only evaluates one medical VLM model, leaving unclear whether the conclusions apply to other models as well.
2. In preference fine-tuning, the quality of the generated candidates seems critical; however, the overall performance of report generation is not good enough, with metrics like precision and recall generally below 0.5. The SFT baseline struggles to produce high-quality candidates, making it difficult to ensure the chosen candidates are reliable, which raises doubts about the alignment's ability to optimize the model in the desired direction.
3. There is a lack of clinical efficacy (CE) metrics that are often used and are very important in report generation. Although preference fine-tuning optimized for the GREEN metric performs much better than the baseline, the GREEN metric itself is not necessarily what is clinically relevant. Clinicians are more concerned about whether a specific disease in the image has been detected, so a comparison of CE metrics for dozens of diseases in MIMIC-CXR is needed, including precision, recall, and F1-score.
4. This paper is vague in the description of some results or conclusions, lacking in-depth analysis. For example, in the experimental results in Table 5, what are the reasons for the error increase in alignment methods in (e) and (f) compared to the SFT baseline? Additionally, the authors state that "verbosity will limit the clinical utility of generated reports," yet, according to the results, SimPO has the smallest verbosity bias but performs the worst among the alignment methods. What is the relationship between verbosity bias and the quality of the generated reports? This is not clearly explained.
5. The alignment methods lead to performance drops in additional diverse tasks, albeit not significantly. This raises questions about the practicality and reliability of performing alignment on medical VLMs. While alignment improves report generation performance, indicating better model understanding of images, why does it not exhibit advantages in other image understanding tasks? What exactly does alignment change in the model? Is it merely a shift to a radiologist-friendly expression? This is not the focus in the clinical setting, and what we care about more is the model’s general ability to understand images.

### Questions
Please refer to Sec. weakness for details.

### Soundness
2

### Presentation
3

### Contribution
2
