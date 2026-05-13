# More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
The trustworthiness of Large Language Models (LLMs) refers to the extent to which their outputs are reliable, safe, and ethically aligned, and it has become a crucial consideration alongside their cognitive performance. In practice, Reinforcement Learning From Human Feedback (RLHF) has been widely used to align LLMs with labeled human preferences, but its assumed effect on model trustworthiness hasn't been rigorously evaluated. To bridge this knowledge gap, this study investigates how models aligned with general-purpose preference data perform across five trustworthiness verticals: toxicity, stereotypical bias, machine ethics, truthfulness, and privacy. Our results demonstrate that RLHF on human preferences doesn't automatically guarantee trustworthiness, and reverse effects are often observed. Furthermore, we propose to adapt efficient influence function based data attribution methods to the RLHF setting to better understand the influence of fine-tuning data on individual trustworthiness benchmarks, and show its feasibility by providing our estimated attribution scores. Together, our results underscore the need for more nuanced approaches for model alignment from both the data and framework perspectives, and we hope this research will guide the community towards developing language models that are increasingly capable without sacrificing trustworthiness.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper evaluates how Reinforcement Learning from Human Feedback (RLHF) impacts Large Language Model (LLM) trustworthiness. It assesses five dimensions: toxicity, bias, machine ethics, truthfulness, and privacy. Results show mixed outcomes: while RLHF improves machine ethics, it often increases bias and privacy leakage and reduces truthfulness, with minimal impact on toxicity. The paper also introduces a novel data attribution method in the RLHF setting to analyze RLHF's effect on these dimensions, highlighting the need for more targeted alignment strategies.

### Strengths
- The paper provides a detailed analysis of RLHF methods across multiple trustworthiness dimensions, offering nuanced insights into alignment challenges.
- By comparing SFT, PPO, and DPO, the paper highlights strengths and weaknesses of each method on its effect on trustworthiness, helping guide future model alignment choices.
- The paper evaluates trustworthiness through several dimensions—such as bias, truthfulness, toxicity, ethics, and privacy—rather than limiting its analysis to one aspect. This multi-faceted approach strengthens the research by showing how alignment impacts different areas, which are crucial for real-world applications where trustworthiness encompasses various dimensions.
- The proposed data attribution method is useful for observing which data points most significantly affect certain trustworthiness dimensions, such as reducing toxicity. By attributing changes in model behavior to specific data inputs, this method provides insights into how particular data segments influence alignment outcomes.
- The paper is well-written and easy to follow.

### Weaknesses
 - In this paper, toxicity is evaluated using the Perspective API. However, several existing papers (see https://aclanthology.org/2023.emnlp-main.472.pdf and https://arxiv.org/pdf/2312.12651) have raised concerns that such black-box APIs may introduce inaccuracies or biases in toxicity assessments. This may affect the reproducibility of this research on this dimension.
- What are the potential trade-offs between the 5 dimensions in trustworthiness? In real-world applications, improving one dimension (e.g., reducing bias) might compromise another (e.g., truthfulness). Would appreciate some insights here.

### Questions
See above weaknesses.

### Soundness
4

### Presentation
4

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
**Summary**:
This paper investigates the overall impact of RLHF training on the moral values exhibited by LLMs. The analysis is carried out by fine-tuning base models (up to 8B in size) in general-purpose preference alignment data and then contrasting the performance before and after RLHF across 5 trustworthiness tenets: toxicity, social bias, ethics, truthfulness, and privacy. The obtained results suggest that although RLHF improves ethics measurements by 16.5-18.5% points on average, it significantly worsens performance in other verticals: social bias, truthfulness and privacy leakage worsen on average by 150%, 25% and 12%, respectively. 

**Main contributions**:
The main contribution is the idea that RLHF models trained on general-purpose preference data may not align with other trustworthiness values that we care about. The application of data influence functions is also novel and interesting.

**Methodology**:
- The authors start with the Anthropic Harmlessness and Helpfulness (HH-RLHF) preference alignment dataset, from which they fine-tune the base model (SFT), the reward model (RM), as well as two RLHF-based models (one trained with DPO loss and the other with PPO loss).
- Adopting the evaluation testbed proposed in [Wang et al 2024](https://arxiv.org/pdf/2306.11698), the authors report metrics for the four different variants of the models (base, SFT, DPO, PPO) and across model sizes (1.4B up to 8B) across 5 trustworthy tenets contrasting the impact of fine-tuned models with base models. 
- Finally, the authors use data influence functions to determine the impact of individual data points in the HH-RLHF dataset for each of the trustworthiness dimensions.

**Interpretation of Results**:
- The results reported across 5 different trustworthiness benchmarks show that fine-tuning LMs in general-purpose preference data (RLHF-HH) leads to worse model behavior in 4  benchmarks when compared to not fine-tuning in RLHF-HH. Across four models, RLHF leads to average improvements of up to 18.5% in recognizing morally wrong scenarios (Figure 3 left). For all other benchmarks, the metric values decrease on average across models by at least 12% points (in Figure 4 left) up to 30% (Figure 3 right). 
- In lines 228-229, the authors claim that “toxicity first increases notably after SFT“ which suggests that there is a large improvement in toxicity. However, there is no statistical test supporting this claim and the error bars are overlapping for two larger models (Figure 2 left), suggesting non-significant differences resulting from the SFT procedure.
- In Section 4.2 the authors claim that “both PPO and DPO significantly increase the stereotypical bias scores [...] and the SFT step is most responsible for this increase.”. However, the carried evaluation consists (to the best of my knowledge) of prompting models whether they agree with a stereotypical sentence concerning a marginalized group but not whether the model agree with the same stereotypical sentence concerning a different group. In other words, **the reported results do not disentangle the models’ propensity to agree with claims (as suggested in lines 260-263 and by prior work (Sharma et al 2023)) from the models’ stereotypical bias**. 
- In Section 5, the authors mention that “Table 5 clearly demonstrates that the language model becomes increasingly deterministic through RLHF, which may provide some insights on why PPO and DPO fail to decrease toxicity [...]”. However, the maximum log likelihood difference between base model and SFT is only 0.78, raising questions about whether this difference is due to noise or if it’s a systematic behavior. Moreover, the generations for the original toxicity experiment were obtained using temperature=0.5, which modifies the actual distribution of the SFT model, potentially leading to narrower distributions. It is important that the authors clarify which temperature was used to carry the experiments in Appendix F.


### Writing
The paper could improve its clarity by adding relevant citations, better positioning their work with respect to previous work, and being clear about the hyperparameters used during the evaluations. Consider the following suggestions: 
- Relevant citations: overall the authors would benefit from adding more relevant citations to back their arguments and strengthen the motivation.
- In the Related Work, subsection “Reinforcement Learning Human Feedback section”, the authors could add citations to the RLHF-HH dataset, but also to other preference datasets (e.g., Cui et al, 2023, Ethayarajh et al 2022). It could also be useful to motivate why the authors settled on the RLHF-HH dataset as opposed to other datasets.
- Lines 260-263 could cite work reporting sycophancy and language model (Sharma et al 2023).

**Clarity**:
- Line 132: “D_demo” → “D” (to be consistent with Equation 1)?
- Equation 1: consider specifying what y_w right after Equation 1 or at the beginning of the section.
- The authors should try to clarify the differences between their experimental design and that of Havrilla et al (2023) and Wang et al (2024). For instance, the analyses carried in Section are very similar to the ones reported in Wang et al (2024), in particular, the evaluation in Section 4.2 appears to be the same but no citation is provided. It could also be nice to motivate the selection of GPT-J-6B based on Havrilla et al (2023) in case the authors didn’t perform any additional experiment using reward models.
 - The authors use different hyperparameters depending on the evaluated criteria. While these parameters are specified in the Appendix C, the only hyperparameters mentioned in the main paper are those for the toxicity evaluation (without referring to the Appendix C or differences in the hyperparameters). The authors should consider being more explicit within each section, motivating the reasons behind selecting different hyperparameters. This is relevant as different hyperparameters have different implications (e.g., lower temperature values have been shown to be associated with higher toxicity)
- Could be useful to add examples for each of the evaluation datasets. Specifically, for the Steoreotypical Bias (in Section 4.2), it would be useful to get a sense of what are the demographic groups, their cardinality, and also the types of stereotypes explored.
- Could be useful if the authors provided a notion of what a meaningful influence score is.
- Figure 5 caption could be more informative, providing more insights on the performed analyses.

Typos:
- Line 398: “8 with 9” → “Equation 8 with Equation 9”
- Line 407: “in 9” → “in Equation 9”

### References

- Touvron et al (2023): Llama 2: Open Foundation and Fine-Tuned Chat Models (https://arxiv.org/abs/2307.09288)
- OpenAI Team (2023): GPT-4 Tech Report (https://arxiv.org/pdf/2303.08774)
- Cui et al (2023) UltraFeedback: Boosting Language Models with Scaled AI Feedback (https://arxiv.org/abs/2310.01377)
- Ganguli et al (2022): Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned (https://arxiv.org/abs/2209.07858)
- Ethayarajh et al (2022): Understanding Dataset Difficulty with V-Usable Information (ICML 2022). (https://proceedings.mlr.press/v162/ethayarajh22a.html)
- Askell et al (2021): A General Language Assistant as a Laboratory for Alignment (https://arxiv.org/abs/2112.00861)
- Glaese et al (2022): Improving alignment of dialogue agents via targeted human judgements
- Tirumala et al (2023): D4: Improving LLM Pretraining via Document De-Duplication and Diversification (https://arxiv.org/abs/2308.12284)
- Sharma et al (2023): Towards Understanding Sycophancy in Language Models (https://arxiv.org/abs/2310.13548)

### Strengths
- Important research question regarding whose preferences concerning what behaviors models are implicitly learned through RLHF.
- The finding that privacy leakage increases with RLHF and is due to the DPO/PPO algorithms (as opposed to SFT) is interesting.
- The use of data influence functions to traceback the impact of RLHF training data to different aspects of trustworthiness is novel and interesting and could prove beneficial to inform the creation of higher quality and better-aligned preference datasets.

### Weaknesses
 - Unclear contribution with respect to previous work: Wang et al (2024), GPT-4, and Llama 2 paper tech reports also carry analyses assessing the impact of RLHF in bias, toxicity, and truthfulness. The authors should make their contribution clearer and compare with previous work.
- The evaluation is carried out in Pythia and Llama models as opposed to more recent and prominent models like OLMo and Llama 3 models. Given the considerable differences between the models (e.g., data deduplication and diversity (Tirumala et al 2023)) it is unclear how the results will generalize to these newer and carefully trained base models.  
- The reported analysis using influence functions provides no insights into the observed patterns in RLHF or the optimal composition of the RLHF training data. It could be beneficial to add a section with further analysis and/or a discussion section about how the authors see this analysis being useful in the long-term to fix the mis-alignment problem.
- In lines 228-229, the authors claim that “toxicity first increases notably after SFT“ which suggests that there is a large improvement in toxicity. However, there is no statistical test supporting this claim and the error bars are overlapping for two larger models (Figure 2 left), suggesting non-significant differences resulting from the SFT procedure.
- In Section 4.2 the authors claim that “both PPO and DPO significantly increase the stereotypical bias scores [...] and the SFT step is most responsible for this increase.”. However, the carried evaluation consists (to the best of my knowledge) of prompting models whether they agree with a stereotypical sentence concerning a marginalized group but not whether the model agree with the same stereotypical sentence concerning a different group. In other words, **the reported results do not disentangle the models’ propensity to agree with claims (as suggested in lines 260-263 and by prior work (Sharma et al 2023)) from the models’ stereotypical bias**.
- In Section 5, the authors mention that “Table 5 clearly demonstrates that the language model becomes increasingly deterministic through RLHF, which may provide some insights on why PPO and DPO fail to decrease toxicity [...]”. However, the maximum log likelihood difference between base model and SFT is only 0.78, raising questions about whether this difference is due to noise or if it’s a systematic behavior. Moreover, the generations for the original toxicity experiment were obtained using temperature=0.5, which modifies the actual distribution of the SFT model, potentially leading to narrower distributions. It is important that the authors clarify which temperature was used to carry the experiments in Appendix F.

### Questions
1. One of the main claims in the paper is “[RLHF]’s assumed effect on model trustworthiness hasn’t been rigorously evaluated” (for instance lines 15-16 and 42-43). However, the evaluation of  RLHF impact in ethical aspects (e.g., truthfulness, bias, toxicity, ethics) has been reported previously (Askell et al 2021, Glaese et al 2022, OpenAI Team 2024, Touvron et al 2023). Can you provide a more detailed comparison of your methodology and findings with the previous works, highlighting specific differences or extensions to their approach? 
2. In lines 202-203, the authors mention “since our language models are large enough, we use zero-shot generated outputs for all benchmarks”. However, a limitation of base models is that they struggle to adapt to the output format. Specifically they may struggle to adhere to the multiple-choice question format of the TruthfulQA (Section 4.4) or to produce yes/no/unknown for the stereotypical bias experiment (Section 4.2). How do you ensure that the output of the language model is consistent with the multiple choice question answering format? Do you perform any test to assess the capability of LLMs to handle 0-shot QA? You could include a specific analysis of the models' ability to adhere to the required output formats in zero-shot settings, perhaps by reporting the percentage of responses that correctly follow the format for each task.
3. The toxicity evaluation reported in line 222 differs from the original evaluation procedure (5 independent generations and temperature=0.5 vs 25 generations and temperature=1). The lower number of generations may substantially affect the results and the lower temperature modifies the model’s distribution, potentially, skewing results. Could you please motivate the selection of these parameters for your analysis? Moreover, you could provide a sensitivity analysis showing how your results change with different numbers of generations and temperature settings. This would help clarify the robustness of your findings.
4. Some experiments like the stereotypical bias (Section 4.2) are carried out by eliciting whether the model agrees or not with a specific stereotypical topic. How can we guarantee that the observed bias amplification is not an artifact of the evaluation (e.g., models being more likely to output yes vs no, or their sycophantic tendency (Sharma et al 2023))? 
5. In Section 4.3, the authors mention that they aim to measure a model's ability to detect morally wrong actions by prompting models whether each example is against human morality. This presupposes that the correct answer (true positive) is to answer yes and that a wrong answer is to answer “no” (false negative). However, the authors call their metric FPR, which does not match with this intuition. Can you provide a clear definition of a true positive, true negative, false positive, and false negative are in this context and explain why FPR is the most appropriate metric for your analysis?
6. What exactly is the prompt being used to prompt base models? If you’re using different prompts, are models sensitive to the prompts, i.e., do you observe considerably different behaviors depending on the prompt used? 
7. The privacy evaluation is unintuitive (to me). I am not surprised that fine-tuning LLMs with general purpose preference data would lead to improvements in such a task. In particular, (1) there is no explicit fine-tuning stage that could boost models’ ability to understand the instructions, (2) most conversation scenarios that I can think of the information shared by the user is already known by it. Would you mind commenting on the motivation and practicality of the proposed evaluation?
8. In lines 365-366, the authors mention that “the most intuitive answer is that the HH dataset used for RLHF is out-of-domain for the evaluation tasks” but provide no support for this hypothesis. Have you considered reporting the perplexity of the evaluation datasets  and comparing it to the perplexity achieved in the training dataset or the Ethics benchmark?

### Soundness
3

### Presentation
4

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
The authors systematically assess how two RLHF variants, PPO and DPO, influence these trustworthiness dimensions using general-purpose preference data. What’s more, this paper introduces a data attribution method to analyze the influence of individual fine-tuning data points on trustworthiness, suggesting the need for more nuanced RLHF approaches.

### Strengths
1. This study offers a systematic assessment of RLHF on multiple trustworthiness aspects;
2. The introduction of an influence-function-based data attribution method tailored to RLHF offers insights into individual data points’ impacts, aiding future data selection for alignment;
3. The work highlights the limitations of using general-purpose datasets for trustworthiness, emphasizing the importance of targeted data in achieving specific alignment goals.

### Weaknesses
1. The experiments are limited to models up to 7B parameters, which may limit the generalizability of findings to larger;
2. The study relies solely on the Anthropic HH dataset, and results might vary with different datasets;

### Questions
1. How might these findings change with LLMs that exceed 7B parameters?
2. Would a more specialized preference dataset yield different outcomes for bias or other dimensions compared to the general-purpose Anthropic HH dataset?
3. What guidance do the paper’s evaluation results offer for balancing helpfulness and trustworthiness in the future?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work investigates the impact of RLHF on the trustworthiness of LLMs. evaluating key dimensions such as toxicity, stereotypical bias, machine ethics, truthfulness, and privacy. Findings indicate that RLHF does not consistently enhance trustworthiness and may even degrade it in some areas.

Further analysis with targeted datasets and a discussion of potential solutions would strengthen its impact. However, this contribution is significant and could be accepted for the conference.

### Strengths
- **Well-structured:** The paper is organized clearly and uses precise language. It offers the first systematic evaluation of RLHF’s impact on specific aspects of trustworthiness.
- **Thorough Evaluation:** Multiple trustworthiness dimensions of RLHF’s effects are thoroughly examined.
- **Innovative Methodology:** The application of influence-function-based data attribution methods to RLHF provides valuable insights into how training data influences model behavior.
- **Empirical Rigor:** The results are detailed, with comprehensive benchmarks and rigorous experimental designs, involving multiple models and controlled benchmarks, allowing for broader generalization.

### Weaknesses
 - **Mitigation Strategies Lacking:** Although RLHF exacerbates bias and privacy issues, potential solutions are not explored in depth. There is limited discussion on why these misalignments occur and how they could be systematically addressed. Specifically, the paper does not delve into the nuances of how different RLHF reward functions might contribute to these issues, nor does it explore methods for regularizing the RLHF process to prevent such degradation. The analysis would benefit from a discussion of techniques like adversarial training or constrained optimization within the RLHF framework.
- **Dataset Limitations:** The reliance on the Anthropic HH dataset for RLHF may limit the generalizability of findings across different applications and LLM architectures. The general-purpose nature of this dataset appears somewhat misaligned with the targeted trustworthiness benchmarks, potentially skewing the results. The paper does not explore the impact of using datasets specifically curated for each trustworthiness dimension (e.g., datasets focused on ethical reasoning, truthfulness, or privacy). This lack of targeted data could explain why RLHF appears to degrade performance in certain areas.
- **Model Scale Constraints:** The analysis is limited to models of up to Pythia-6.9B and Llama-7B, which may not reflect performance in larger, frequently used LLMs. It is unclear whether the observed trends would hold for models with significantly more parameters, as larger models often exhibit emergent behaviors that are not present in smaller ones. The paper should acknowledge this limitation and discuss the potential for different outcomes at larger scales.
- **Figure Clarity:** Certain figures, such as Figures 5 and 11, are not optimally clear. Text and data appear crowded, reducing readability. The use of smaller font sizes and overlapping data points makes it difficult to discern the trends and comparisons being presented. The figures need to be redesigned for better visual clarity.
- **Dense Methodology Sections:** Sections such as 3 and 5 contain dense explanations that could benefit from clearer, more accessible language. The descriptions of the influence-function-based data attribution methods and the RLHF process are particularly challenging to follow, lacking intuitive explanations and concrete examples.

### Questions
- Can additional fine-tuning methods be combined with RLHF to mitigate observed trustworthiness degradation?
- Would using smaller, targeted RLHF datasets for each trustworthiness aspect outperform a single general-purpose dataset? Additionally, how would the combination of general-purpose and aspect-specific datasets impact trustworthiness?
- How does dataset size influence the observed trends in trustworthiness metrics? Specifically, would varying dataset sizes in RLHF lead to different levels of model trustworthiness?

### Soundness
3

### Presentation
4

### Contribution
3
