# Evaluating Privacy Risks of Parameter-Efficient Fine-Tuning

- Decision: Reject
- Avg Score: 5.80
- Scores: 5, 8, 6, 5, 5

## Abstract
Parameter-efficient fine-tuning (PEFT) is a new paradigm for fine-tuning language models at scale. Unlike standard fine-tuning,
PEFT adjusts only a small number of parameters, making it more computationally accessible and enabling practitioners to develop personalized services by fine-tuning models on user data. Because the models are trained on user data, this emerging paradigm may attract adversaries who want to extract sensitive information from fine-tuning data. However, their privacy implications have not been well-understood in the literature.

In this paper, we study the impact of this new fine-tuning paradigm on privacy. We use an off-the-shelf data extraction attack as a vehicle to evaluate the privacy risk on two pre-trained language models fine-tuned on 2 datasets, repeated 5 times with different random seeds, resulting in a total of 100 variations. Our main findings are: (1) for practitioners employing PEFT to construct personalized models, the fine-tuned models have lower privacy risks while maintaining reasonable utility; (2) for developers designing new PEFT algorithms,
while safer than standard fine-tuning, certain design choices in the algorithms increase memorization in an unexpected way; and (3) for researchers auditing the privacy of fine-tuned models, employing weak differential privacy is sufficient to mitigate existing data extraction risks without significantly compromising model utility. We hope our work encourages the safe adoption and development of PEFT algorithms in practice, as well as future work on advancing stronger privacy auditing mechanisms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper examines privacy risks of models fine-tuned using various types of parameter-efficient fine-tuning. The risk assessment is performed by quantifying memorization of fine-tuning datasets through the Exposure metric. The authors conduct experiments on GPT-2 and GPT-2 XL using two datasets and four types of fine-tuning methods. Additionally, they investigate the impact of differential privacy on Exposure during parameter-efficient fine-tuning.

### Strengths
1. The paper addresses a timely research question about privacy vulnerabilities when using PEFT, which is particularly relevant given the widespread adoption of PEFT techniques in deploying LLMs across various domains.

2. The authors conducted extensive experiments and ablation studies to evaluate privacy leakage across various setups.

3. The findings demonstrating that PEFT methods offer significantly better privacy guarantees compared to full-parameter fine-tuning provide valuable insights for the broader ML community.

### Weaknesses
1. While this work is primarily experimental, the presentation quality of the experimental results requires improvement:

  * In Figures 1, 4, 5 (and similar figures in the Appendix), the axis scaling choices result in most data points being clustered in one corner, making it difficult to interpret the results accurately. This is particularly problematic in Figures 4 and 5, where high Perplexity values for a single point obscure the differences between other points. A recommended solution would be to revise the plotting approach (for instance, using log-scale (essentially, Cross-Entropy Loss) instead of raw Perplexity).

  * All figures in the main paper contain multiple plots, but their differences are only explained in the captions. This significantly impairs figure readability, as understanding the distinctions between plots requires repeatedly referring to the full description. One potential improvement would be to place key distinguishing features (such as $\varepsilon$ values in Figure 4) as titles above the corresponding plots.

  * The paper's analysis of DP privacy-utility trade-off would be more compelling if presented as plots with multiple points per method (such as Perplexity versus Exposure with points corresponding to different $\varepsilon$ values) rather than the current approach (Figure 4) of separate plots one by one with single point per method. (and with different scales and $\varepsilon$ values, which also makes direct comparisons challenging)

The main paper also contains strange results that were not commented on by the authors (see Questions).

2. In lines 246-247, the authors state that 'We observe a slight increase in perplexity (0.01-0.15), but the increase is too small to result in a significant increase in the exposure.' (Presumably, there's a typo and it should read 'decrease in exposure'.) This statement isn't entirely self-evident, given that the perplexity losses are quite substantial (~13%). To validate that such performance losses don't affect exposure, it would be valuable to measure exposure values for an undertrained baseline at perplexity levels matching those of the PEFT methods (e.g. for GPT-2 on MIMIC-III, at perplexity points of 1.30, 1.24, etc.).

3. In Definition 3.1, the authors introduce an adaptation of the term Memorization. The motivation for this decision is unclear since all experimental measurements use the Exposure metric, which, unlike Memorization, is adopted from [1] without modifications. The paper would benefit from a clearer explanation of why this adapted definition was included.

4. While the methods described in lines 126-131 don't provide formal guarantees, it would be beneficial to understand how their combination with PEFT affects privacy.

5. Additionally, the paper would benefit from explicit examples of dataset records after secret insertion (for example, in Appendix section).

### Questions
1. How do the authors explain that in Figure 3, Exposure with differential privacy is worse than without it?

2. In Figure 3, why is the Exposure metric notably worse (higher) when using 1 insertion versus 500 insertions?

3. Given the high Exposure values with 500 insertions shown in Figure 2, was Table 1 constructed using 1 insertion? If so, this should be explicitly stated. Furthermore, it would be valuable to show the relationship between Exposure and intermediate insertion values (between 1 and 500).

4. In Figure 5, the dependencies on hyperparameters are not consistently monotonic (for example, $r=32$ is unexpectedly low in the top left, $r=16$ is low in the bottom left, and $pt=16$ between 32 and 64 in the bottom middle). Do the authors have any hypotheses explaining these inconsistencies?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper systematically studies how different parameter-efficient fine-tuning methods can memorize secrets. It uses a standard definition of "exposure" and evaluates how exposure is affected by PEFTs. Additionally, the paper studies how differential privacy can be applied to limit exposure for a limited utility loss.

The key contribution of this paper is its thorough evaluation, which uses two types of models (GPT2 and GPT2-XL) and 4 widespread PEFT techniques. The experiments carefully evaluate the impact of various PEFT configurations (algorithm, number of fine-tuning parameters, position of the secret) on memorization.

Some findings of the paper are surprising -- for instance, increasing the number of tunable parameters does not necessarily lead to an increase of memorization, in the context of PEFTs. The authors intend the paper to be a guide to privacy-preserving PEFTs ; I find that the paper satisfies this purpose.

### Strengths
Main strengths:
- The key contribution of this paper is its thorough evaluation of the PEFT landscape in terms of memorization. Experiments are extremely detailed, and provide extremely valuable datapoints for practitioners and future research.
- I really appreciated the focused and methodical approach of the paper. It made the space of PEFTs digestible (I am not an expert in PEFTs so I learned a lot). The evaluation questions are clearly-formulated and well-motivated.
- The paper does a great job breaking down a general question ("what are the privacy risks of PEFTs") into modular components that can be studied in a structured manner. Exposure, perplexity, and differential privacy budget are nicely orthogonal metrics. PEFT algorithm, number of tunable parameters, secret duplication and position are also great variables.

Other strengths:
- I appreciated the comparison of DP libraries in appendix. I didn't know about FastDP, so sharing this type of details is useful for other researchers.

### Weaknesses
Main weakness:
- I am concerned about the generalizability of the results to other types of secrets. The paper does a great job at varying the PEFT algorithms and parameters, but somehow the way secrets are chosen seems quite arbitrary. 
- The authors hint at the fact that the type of secret can be an important variable ("We attribute this difference to the secrets we choose"). Thus, I find it surprising that this variable is not studied with the same depth as other variables. For instance, the author's hypothesis that the difference in exposure between Enron and MIMIC is due to secret types could be evaluated by also using an email address in MIMIC (and a name in Enron). 
- I also wonder about other types of secrets, such as less common names, longer secrets, or numbers such as an SSN.


Other weaknesses:
- The fine-tuning datasets seem pretty small, with about 14k records (by the way, why is Enron 13,399 instead of exactly 13,431 records if the goal is to match the size of MIMIC?). I would be curious about the impact of dataset size on memorization, for instance on the Enron dataset with 600,000 records. But this might just have the inverse effect of secret duplication, so I understand if this variable is less important in the evaluation. 
- Fig 4. "Setting ε below 10.0 completely breaks the models fine-tuned with prompt tuning and prefix tuning." Indeed, epsilon = 0.1 is probably too strong, so this might not be the most interesting value to pick. But what about epsilon=1? The scales of axes in Fig 4 are very different too. 
- Fig 5: the privacy-utility tradeoff is pretty well understood, so I would personally be more interested in graphs showing epsilon vs memorization (and this paper is about memorization anyway). Fig 12 does that in appendix, but only for GPT2 XL, with just two datapoints. How about GPT2 for more values of epsilon?

Minor comments:
- I was looking for the equivalent of Fig 2 for prompt tuning, and finally found it in Fig 13. It could be helpful to include pointers to the appendix in the body of the paper.
- Table 1 is packed with useful information but a bit hard to digest, maybe put some numbers in bold?
- Why the quotation marks in: MEMORIZATION OF MODELS FINE-TUNED WITH “PRIVACY”
- typo" "Our definition above is strict: memorization is only confirmes"
- typo: "This construction fllows the same methodology as"
- typo: "insert the same secert at 5 different positions"

### Questions
* You formulate an interesting hypothesis about LoRA, saying that "the reduced rank in the latent representation space acts as an information bottleneck, making it difficult for the model to memorize outliers, such as the secret, which the model first encounters during fine-tuning (as we ensure the secret is not present in the pre-training corpus)." Have you evaluated this hypothesis by comparing how easily secrets can be memorized depending on how close they are compared to the pre-training dataset? For instance, what if a name is already present in the pre-training dataset, but the secret is about extracting the name in a particular context?
- What is the value of delta for the DP training? I assume you are not doing pure DP, but I couldn't find delta. Also, what is the unit of privacy for the DP training, is it token-level or record level?

### Soundness
4

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
4

### Summary
This paper examines privacy risks in Parameter-Efficient Fine-Tuning (PEFT) for language models, which adjusts only a subset of parameters for computational efficiency. Through data extraction attacks on models fine-tuned with PEFT on sensitive datasets, the authors show that PEFT generally reduces privacy risks compared to traditional fine-tuning. They identify factors in PEFT design that affect privacy and demonstrate that integrating differential privacy (DP) can further mitigate risks while preserving model utility. This study highlights privacy-utility trade-offs in PEFT, providing valuable guidance for privacy-aware model fine-tuning.

### Strengths
1.  The paper explores the largely uncharted territory of privacy implications in PEFT (Parameter-Efficient Fine-Tuning) models, a critical consideration as these models gain prominence in user-specific applications. By employing data extraction attacks to assess privacy risks across different PEFT configurations, it provides a sophisticated and nuanced approach for privacy auditing. The integration of Differential Privacy (DP) within PEFT algorithms showcases potential advancements over conventional fine-tuning, particularly for applications that require both enhanced privacy and computational efficiency.

2. The paper employs clear and effective metrics, such as exposure and perplexity, to evaluate the trade-offs between privacy and utility. The comprehensive assessment across various fine-tuning methods (e.g., LoRA, prompt-tuning) highlights the distinct privacy impacts of different PEFT strategies, providing robust insights into their relative effectiveness.

3. The paper features precise definitions of key terms, well-grounded in existing literature and adapted to the privacy-focused nature of this study. Its logical structure—from the background and methodology to the findings and discussion—enhances accessibility and readability for the audience.

4. This work offers vital guidance for designing PEFT models that balance privacy with utility, a crucial factor for privacy-conscious AI applications. Its practical recommendations underscore the privacy-preserving benefits of PEFT, making it a valuable resource for industries seeking to develop and scale user-centric, privacy-aware AI solutions.

### Weaknesses
 1. Limited Scope of Privacy Attacks

A notable limitation of the paper is its reliance on a single type of data extraction attack as the primary method for evaluating privacy risks. Given the title, “Evaluating Privacy Risks of Parameter-Efficient Fine-Tuning,” this scope may be overly ambitious. The study would benefit from incorporating additional types of privacy attacks, such as membership inference or model inversion attacks, which are commonly used to assess vulnerabilities in language models. These additional analyses could provide a more comprehensive understanding of potential weaknesses in PEFT algorithms, especially in scenarios involving adversaries with varying degrees of access or prior knowledge. For example, membership inference attacks could reveal if an adversary can determine whether a specific data point was used in the fine-tuning process, while model inversion attacks could attempt to reconstruct sensitive training data from the model parameters themselves. Including these evaluations would enhance the credibility of the paper’s claims regarding the privacy resilience of PEFT models.
To present a more balanced view of privacy risks, the authors could either broaden the analysis to include multiple attack methods or adjust the paper’s scope to focus specifically on data extraction risks.

2. Over-Reliance on Perplexity as a Utility Metric

The study’s primary use of perplexity as a utility metric, while relevant, may not capture the full spectrum of performance considerations. Perplexity is effective for general language model evaluation but may not align directly with task-specific outcomes, particularly for models fine-tuned for specialized applications. For instance, a model might achieve a low perplexity score but perform poorly on a downstream task like question answering or sentiment analysis, where accuracy or F1 scores are more relevant. Evaluating additional utility metrics, such as task-specific accuracy or F1 scores for downstream tasks, would provide a more nuanced understanding of the impact of PEFT on utility.
To improve this, the author could expand the analysis to include a broader range of performance metrics, especially those relevant to specific tasks, offering a more comprehensive view of model utility and its trade-offs with privacy. This approach would be particularly beneficial for fine-tuning applications involving domain-specific tasks (e.g., question answering or sentiment analysis).

3. Language and Presentation Issues

Spelling Error: In Section 4.4, line 381, “measyured” should be corrected to “measured.”
Reference Issues: In Sections 4.2 and 4.3, there are references to Table 1, but the text mistakenly cites it as Table 3. These inconsistencies could lead to reader confusion.

4. Lack of Supporting Data

The analysis in Section 4.4, particularly the part discussing prompt-tuning, lacks direct data support or a clear reference to supplementary material in the appendix. This absence of detailed data makes it difficult for readers to validate the findings or understand the depth of the analysis. Suggested Improvement: Include specific data points within the main text or ensure they are readily accessible in the appendix for more transparent and verifiable results.

### Questions
Q1. In line 376, the presentation states: “The left figure shows results from models trained with differential privacy (DP), while the right figure presents results with DP at ϵ=10.0.” This is somewhat confusing as both figures are described as using DP. Could you clarify if the left figure represents models trained without DP? If both are indeed trained with DP, specifying the difference more explicitly would improve clarity.

Q2. The paper primarily uses perplexity as the utility metric, but perplexity may not reflect performance on specific downstream tasks. Would it be possible to include additional metrics, such as task-specific accuracy or F1 scores, to provide a broader view of PEFT’s utility? Alternatively, could the authors clarify if perplexity alone is considered a sufficient and representative utility measure across general scenarios?

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
The paper leverages data extraction attack to evaluate the privacy risk of PEFT fine-tuned language models. The data extraction attack utilized assume that the adversary knows the context associated with a secret and has a list of secret candidates to compare, and the goal is to reconstruct the remaining specific tokens. The PEFT algorithms considered are adapters, prefix-tuning, prompt-tuning and LoRA.

The authors made some insightful findings, such as how the position of the secret affects the privacy leakage of different PEFT methods. Importantly, their findings can be useful to different stakeholders including practitioners, developers and researchers.

### Strengths
I particularly appreciate some findings of the experiments e.g. the position of the secret in a sentence, it gives a unique perspective into the memorization of PEFT. The authors did a fine job in addressing different stakeholders, which I believe is very timely and important in this fast-paced LLM development.

In addition, understanding the vulnerabilities of model fine-tuned using PEFT algorithm is important considering the ease of downloading models, fine-tuning the model and then possibly releasing or offering the fine-tuned model as a service. Hence, this study can be used as a basis for quantifying leakage and further develop strategies to protect data privacy from fine-tuned language models.

### Weaknesses
The claims of the authors are overly exaggerated in saying that the risk evaluation is wrt "100 language model". When in reality, they only considered 2 language models. Repeating an experiment 5 times does not constitute a completely new language model. While these variations lead to differences in the final trained models, the overall performance and behavior of the models are often similar.

While in line 184, the authors elaborated on how they constructed 5 distinct fine-tuning datasets from a single dataset, which would in turn lead to supposedly 5 "different" language models, I am still not convinced. Importantly, the authors used 4 algorithms / methods (Adapter, prefix-tuning, prompt-tuning and LoRA) and not 5. Or does the baseline (standard fine-tuning) also count as a PEFT method?

Some findings of the paper are rather obvious and in line with the findings of [a] where they showed that closed LLM are better at privacy preserving than open LLMs.

The paper would be stronger with more experiments on other language models rather than the two considered models.

Definition 3.1 is different from that of Carlini 2021, but your quantification metric (exposure) is the same as Carlini 2019. What is the interplay here? I mean, why is there really a need for adaptation of the definition?

From the analysis, lower model perplexity is better. It means that the model performs better. In contrast, lower exposure means low attack success. Then shouldn't this statement read increase perplexity does not lead to decrease exposure? Since what you are trying to say is that PEFT methods performs slightly worse (increased perplexity) but their memorization is still very low (decreased exposure) compared to baseline.
"We observe a slight increase in perplexity (0.01—0.15), but the increase is too small to result in a significant increase in the exposure."

Is there a reason to only show the differential privacy experiments on prefix tuning, as in Figure 3? 
Could the author please run the experiments on other PEFT methods (prompt tuning, LoRA and adapters)? This would have made the paper stronger in that understanding the effect of the secret position in the DP paradigm will further support the author's claims.
"Moreover, it is essential to understand how the formal defense against privacy attacks—differential privacy—mitigate this risk while maintaining model utility."

Could the authors provide justifications for the selections of hyperparameters in line 409-410? Were they chosen via some optimization process or based on prior works?
"In evaluation, we set the adapter rank to 32, the number of prompt and prefix tokens to 32 and 16, respectively, and the LoRA rank to 8."


Minor:

line 163--> confirms not confirmes

line 184--> follows not fllows

line 242--> find not fine

In the caption of Figure 5, it should be *datasets* and not models. "MIMIC-III models are located on top and Enron *models* below"

### Questions
I have the following questions. I am willing to adjust my scores if the authors can provide reasonable justifications.

1. Rather than claim that the evaluation is over "100 language models", could you modify the claim to only specifying the number of base models? You can further clarify that you have 100 variations of those models under different fine-tuning conditions (although it should be 80 excluding the full fine-tuning).

2. Could the authors perform additional experiments using models like Pythia (any of the models) [c], Gemma [d] or LLama3 [e] since these models are used in practice and understanding how they memorize would allow for better understanding and effective auditing?

3. The text: "We demonstrate that, even with a sufficiently small $\epsilon$, data extraction can be completely rendered ineffective across all PEFT algorithms, while preserving model utility."
A smaller $\epsilon$ would mean stronger privacy (higher noise) which implies less leakage, hence, the reason why data extraction is ineffective. This is very obvious, or do the authors mean the opposite? Meaning, even with a large $\epsilon$ (low privacy regime), the extraction attack is ineffective?

4. Definition 3.1 is different from that of Carlini 2021, but your quantification metric (exposure) is the same as Carlini 2019. What is the interplay here? I mean, why is there really a need for adaptation of the definition?

5. From the analysis, lower model perplexity is better. It means that the model performs better. In contrast, lower exposure means low attack success. Then shouldn't this statement read increase perplexity does not lead to decrease exposure? Since what you are trying to say is that PEFT methods performs slightly worse (increased perplexity) but their memorization is still very low (decreased exposure) compared to baseline.
"We observe a slight increase in perplexity (0.01—0.15), but the increase is too small to result in a significant increase in the exposure."

6. Is there a reason to only show the differential privacy experiments on prefix tuning, as in Figure 3? 
Could the author please run the experiments on other PEFT methods (prompt tuning, LoRA and adapters)? This would have made the paper stronger in that understanding the effect of the secret position in the DP paradigm will further support the author's claims.
"Moreover, it is essential to understand how the formal defense against privacy attacks—differential privacy—mitigate this risk while maintaining model utility."

7. Could the authors provide justifications for the selections of hyperparameters in line 409-410? Were they chosen via some optimization process or based on prior works?
"In evaluation, we set the adapter rank to 32, the number of prompt and prefix tokens to 32 and 16, respectively, and the LoRA rank to 8."

8. I would also like to point the authors to a concurrent work [b]. Although the focus of their work is on full fine-tuning and their method of auditing is MI attacks, it is important for the authors to be aware of this work.



Minor:

line 163--> confirms not confirmes

line 184--> follows not fllows

line 242--> find not fine

In the caption of Figure 5, it should be *datasets* and not models. "MIMIC-III models are located on top and Enron *models* below"

[b] "Privacy auditing of language models" https://openreview.net/forum?id=60Vd7QOXlM

[c] Pythia: A suite for analyzing large language models across training and scaling. https://arxiv.org/abs/2304.01373

[d] Gemma: Open models based on gemini research and technology. https://arxiv.org/abs/2403.08295

[e] llama 3 herd of models. https://arxiv.org/abs/2407.21783

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores performance leakage in large language models during PEFT (Parameter-Efficient Fine-Tuning) training, addressing a crucial issue in model privacy. The authors introduce two definitions for assessing privacy leakage and conduct experiments across various datasets, models, and scenarios. The findings contribute valuable insights into understanding privacy risks associated with PEFT training.

### Strengths
The privacy risks associated with PEFT training remain under-explored, and this paper presents experimental studies to help address this gap. 

The experiments cover various scenarios, including different PEFT algorithms, datasets, and models. The results are insightful and offer valuable guidance for researchers and practitioners in this field.

### Weaknesses
The models used in this paper are relatively small, so it’s uncertain if the findings would generalize to larger models like the LLaMA series, which are widely used in various applications. Additionally, the larger scale of PEFT parameters in such models could potentially impact the conclusions.

The experimental scenarios primarily focus on a "secret guess" task, which may not provide sufficient basis for a comprehensive assessment of privacy leakage. Expanding the experiments to include other scenarios, such as information retrieval tasks, could offer insights into whether PEFT indeed exposes sensitive information.

Furthermore, the definitions lack sufficient theoretical analysis on the extent of privacy risk. More in-depth theoretical explanations and analyses would enhance the robustness of the findings.

### Questions
What if extending to large-scale models alters the findings?
If we train the model on larger-scale data, could this help reduce privacy risk? Do we have a relationship between the privacy risk vs number of trained data?

### Soundness
3

### Presentation
3

### Contribution
2
