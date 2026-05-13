# OBI-Bench: Can LMMs Aid in Study of Ancient Script on Oracle Bones?

- Decision: Accept
- Scores: 8, 6, 6, 5

## Abstract
We introduce {\bf OBI-Bench}, a holistic benchmark crafted to systematically evaluate large multi-modal models (LMMs) on whole-process oracle bone inscriptions (OBI) processing tasks demanding expert-level domain knowledge and deliberate cognition.
OBI-Bench includes 5,523 meticulously collected diverse-sourced images, covering five key domain problems: recognition, rejoining, classification, retrieval, and deciphering. These images span centuries of archaeological findings and years of research by front-line scholars, comprising multi-stage font appearances from excavation to synthesis, such as original oracle bone, inked rubbings, oracle bone fragments, cropped single character, and handprinted character. 
Unlike existing benchmarks, OBI-Bench focuses on advanced visual perception and reasoning with OBI-specific knowledge, challenging LMMs to perform tasks akin to those faced by experts.
The evaluation of 6 proprietary LMMs as well as 17 open-source LMMs highlights the substantial challenges and demands posed by OBI-Bench. Even the latest versions of GPT-4o, Gemini 1.5 Pro, and Qwen-VL-Max are still far from public-level humans in some fine-grained perception tasks. However, they perform at a level comparable to untrained humans in deciphering task, indicating remarkable capabilities in offering new interpretative perspectives and generating creative guesses.
We hope OBI-Bench can facilitate the community to develop domain-specific multi-modal foundation models towards ancient language research and delve deeper to discover and enhance these untapped potentials of LMMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces OBI-Bench, a comprehensive benchmark for evaluating large multi-modal models (LMMs) on oracle bone inscription (OBI) processing tasks. The work aims to assess whether modern AI models can assist in studying and interpreting these important historical artifacts, by repositioning the LLMs as subject experts for the tasks.  The evaluation targets critical domain challenges in: recognition, rejoining, classification, retrieval, and deciphering.

The paper highlights the use-cases of the current LMMs, and also throws caution towards the issues.

### Strengths
1. Novel (and important) Application Domain - Important systematic evaluation of LMMs for ancient script analysis, addressing a significant real-world problem in historical research with potential to accelerate archaeological research and cultural heritage preservation.
    
2. Comprehensive fine-grained benchmark - covering tasks like recognition, rejoining, classification, retrieval, and deciphering
    
3. Specific data curation for each task helps to answer queries specific to each of them.
    
4. Extensive Evaluation with 23 state-of-the-art LMMs (6 proprietary, 17 open-source)

### Weaknesses
1. The overall technical importance of the benchmark might be limited - the evaluation is very sensitive to the query-answer form (spectrum of questions), even a little change or adding some context can influence the outcomes drastically. Although the work is quite extensive, a decent foray into how prompt engineering can impact the performance could have been a nice addition to the work. Eg: Take the example of Deciphering task, use the best open-source and proprietary models (as already done in evaluation for this task) and test this for prompt engineering.
    
2. How many images are original and how many are pseudo-oracle bone characters?  What are the differences in evaluation between both these types of bone-fragments? - these are unclear and not mentioned in the main article.
    
3. Section 3.1 (scenario 2): What about the situation when the query does not include the word ‘OBI‘ (reflection of first point above)?
    
4. An interesting trend is visible in Fig. 3, can there be another experiment to check if this trend is correlated with the parameter sizes? Eg: Fix a type of LMM, and then observe the effect of increasing parameters?
    
5. Tab. 5 - Recall@10 is roughly 10x Recall@1 which is understandable. More meaningful will be to have Recall@3 and/or Recall@5 - often (like in Google search results) users aren’t interested in top-10 recalls, rather how good is the top-3/top-5.
    
6. Some discussion on the impact of model architectures (of course only possible with open-source models), and computational requirements can improve the overall comprehensiveness of the work.

### Questions
1. What’s the main takeaway of the OBI-Benchmark? Having presented the empirical studies in the paper, it is clear that LMMs are sensitive to local/input information (borders, fragments, low-resolution, noisy fragments), perform better when the data is clean with better resolution, and are short on domain specific knowledge. In most of these tasks, better data will improve the performance but that is the nature of the OBI data…it is quite difficult to get a higher quality. So, as a researcher what shall I do? -- A discussion or propositions in this direction could be useful to add in the paper.  
    
2. Non-generative AI models have recently become more interpretable and explainable [1]. So, given the niche domain of the data handled in OBI-Bench, wouldn’t it be more useful if such traditional ‘deep learning‘ methods are used if there is better data available, as compared to using LMMs which (as pointed above and in the article) are not at par and also are still a bigger black-box model?
    
3. Stress-testing the LMMs by increasing no. of categories clearly shows the real limitations of the LMMs. Given this finding (Fig. 3), do the authors think scaling is an issue? - that the performance will improve if the models were bigger with larger context windows?
    
4. There is a “Human“ performance metric mentioned in Table.2, is it possible to have such reference metrics for consequent tables as well? This should help understand the performance gap of the LMMs vs. Humans.

[1] Minh, D., Wang, H.X., Li, Y.F. et al. Explainable artificial intelligence: a comprehensive review. Artif Intell Rev 55, 3503–3568 (2022). https://doi.org/10.1007/s10462-021-10088-y

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
3

### Summary
This paper introduces OBI-Bench, a benchmark designed for evaluating multiple capabilities in the field of oracle bone script research. OBI-Bench encompasses five domains: recognition, rejoining, classification, retrieval, and deciphering. It involves four types of questions and includes a total of 5,523 questions, ultimately demonstrating these capabilities through extensive experiments.

### Strengths
1. This paper covers five specific areas of oracle bone script exploration, providing a comprehensive summary of prior work in the field.
2. The evaluation dimensions of this paper are diverse, it attempts to explore more fine-grained capabilities through the design of questions such as "How" and "Where" questions. Although the design of these two types of questions may not be critical, this approach seems to offer a potential framework for exploring process supervision mechanisms for models in the field of oracle bone script research.

### Weaknesses
1. There are some long-tail issues in the data volume of each task, particularly with an excessive amount for Recognition and insufficient data for Deciphering.
2. Despite the diversity of tasks, would it be possible to provide an overall score to evaluate the comprehensive ability of LMMs? This score should not be a simple average but should also take into account that LMMs are still in the early stages in the field of oracle bone scripts. Consideration should be given to the lower scores that may result from the model not being trained in certain areas. It would be beneficial to design a dynamic evaluation score to provide a more comprehensive guide for LMMs.

### Questions
Please refer to the weaknesses section.

### Soundness
3

### Presentation
3

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
This paper focuses on an interesting research filed, Oracle Bone Script. Considering the understanding of Oracle Bone Script requires aligning its images with actual meanings, it indeed serves as a good evaluation of LLM's capabilities in vision-image alignment. The dataset consists of most of the currently available public datasets, covering five different tasks, namely recognition, rejointing, classification, retrieval, and deciphering. A detailed baseline is yielded among most proprietary and open-source LMMs.

### Strengths
1. The five domain problem is spanning from excavation to synthesis and coarse-grained to fine-grained which is novelty to the evaluation of a LMM.
2. The baseline consists of most proprietary and open-source LMMs and the results are consist to other LMM benchmarks.

### Weaknesses
1. Some domain problem setting, namely rejoining and deciphering, is not convincing. The rejoining task, focusing primarily on high-frequency image textures, may not effectively evaluate an LMM's understanding of Oracle Bone Script (OBS) semantics. The deciphering task, relying on BERTScore, might be biased due to its sensitivity to surface-level textual similarities rather than deeper semantic understanding.
2. Lack of the results of fine-tuned open-source LLMs which is quiet important to a domain specific benchmark. The absence of fine-tuned models limits the benchmark's ability to assess the potential of domain-specific adaptation, which is crucial for practical applications in OBS analysis.
3. Among the analysis of each domain problem or each scenario, the essential reason why open LMM perform like that is lacking which is important to the community beyond a specific benchmark. The analysis lacks a detailed investigation into the underlying causes of open-source LMMs' performance, such as limitations in parameter size, training data, or architectural biases, which are critical for guiding future research.

### Questions
1. I am agree the rejoining problem is important to the recovery of paper money, calligraphy, and painting files. Does the rejoining problem is necessary in exploring the capability of understanding the OB of a LMM? I believe the rejoining problem only focus on the high-frequency image textures，but not the real meaning of a pattern. If so，a yes-or-not or how problem is rather superficial to evaluate this domain problem.

2. For the evaluating the performance of deciphering, a BERTScore might be bias. A detailed instruction prompt to identify the output patten of a LMM should be better.

3. It seems "yes-or-no" query and "how" query are alternative (according to the results and common sense). It is better to show these two queries are irrelevance.

4. Line 471. What does "with different frequency levels F" mean?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces OBI-Bench, a benchmark designed to evaluate the capabilities of Large Multi-Modal Models (LMMs) in processing oracle bone inscriptions (OBI), an ancient form of Chinese writing. The benchmark includes 5,523 images sourced from diverse origins, covering five key tasks: recognition, rejoining, classification, retrieval, and deciphering. These tasks demand expert-level domain knowledge and cognitive abilities.

### Strengths
The paper presents OBI-Bench, a novel benchmark that systematically evaluates Large Multi-Modal Models on tasks related to oracle bone inscriptions, addressing an unexplored and complex domain in LMM research. This benchmark encompasses five critical tasks: recognition, rejoining, classification, retrieval, and deciphering, going beyond standard evaluations to include recovery and interpretation tasks；Designed to test LMMs with expert-level challenges, OBI-Bench requires deep domain knowledge and cognitive skills. This innovative approach pushes the boundaries of LMM capabilities, contrasting with typical benchmarks that focus on general performance； The benchmark is backed by a diverse dataset of over 5,500 images from archaeological findings, significant for training and evaluating LMMs in real-world applications. Additionally, the paper includes a comprehensive evaluation of both proprietary and open-source LMMs, providing valuable insights into their performance and limitations in deciphering ancient scripts, thus highlighting the potential for advancing research in historical linguistics and cultural heritage.

### Weaknesses
The paper introduces a dataset of 5,523 images, but its diversity and scale could be enhanced by incorporating more images from various sources and time periods. This expansion would improve the robustness of the benchmark and better reflect the complexities of OBI variations; The paper evaluates LMMs at a single point in time. A longitudinal study tracking the performance of LMMs over successive versions could provide valuable insights into the progress and potential of these models; The paper discusses the performance of LMMs on various tasks but does not delve into the interpretability of these models. Providing insights into how LMMs make decisions, especially on deciphering tasks, could be insightful for both the AI community and OBI scholars.

### Questions
Would the authors consider conducting a longitudinal study to track the performance of LMMs over time as the models evolve, to measure the progress and potential of these models in the OBI domain? How will the authors address the issue of cultural bias in LMMs, and will they investigate how different cultural backgrounds of the model's training data and developers might influence performance on OBI tasks?

### Soundness
2

### Presentation
3

### Contribution
3
