# Measuring Vision-Language STEM Skills of Neural Models

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
We introduce a new challenge to test the STEM skills of neural models. The problems in the real world often require solutions, combining knowledge from STEM (science, technology, engineering, and math). Unlike existing datasets, our dataset requires the understanding of multimodal vision-language information of STEM. Our dataset features one of the largest and most comprehensive datasets for the challenge. It includes $448$ skills and $1,073,146$ questions spanning all STEM subjects. Compared to existing datasets that often focus on examining expert-level ability, our dataset includes fundamental skills and questions designed based on the K-12 curriculum. We also add state-of-the-art foundation models such as CLIP and GPT-3.5-Turbo to our benchmark. Results show that the recent model advances only help master a very limited number of lower grade-level skills ($2.5\%$ in the third grade) in our dataset. In fact, these models are still well below (averaging $54.7\%$) the performance of elementary students, not to mention near expert-level performance. To understand and increase the performance on our dataset, we teach the models on a training split of our dataset.
Even though we observe improved performance, the model performance remains relatively low compared to average elementary students. To solve STEM problems, we will need novel algorithmic innovations from the community.
\def\thefootnote{}\footnotetext{The dataset and leaderboard are available at \url{https://huggingface.co/datasets/stemdataset/STEM}.}
\def\thefootnote{\arabic{footnote}}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The paper proposes a new dataset, STEM, to test the STEM skills of neural models. Focusing on fundamental skills in the K-12 curriculum, STEM features a high coverage of skills in all four subjects, a large number of questions, and its multi-modal property. 

- The paper benchmarks a wide range of neural models, including baselines and SOTA models for both language models and vision-language models. Results show that neural models are still behind human performance.

- The paper breaks down its result analysis into different granularities, such as skills, subjects and grades, and identifies the shortcomings of models and challenges for future research.

### Strengths
1. The paper introduces a novel and challenging benchmark for multi-modal STEM skills. Compared to existing benchmarks, STEM covers all four subjects, contains more skills and questions, and strictly excludes single-modal questions. Therefore, it significantly contributes to the advancement of neural models' multi-modal skills.

2. The paper benchmarks a wide set of neural models, including the SOTA models such as ChatGPT and CLIP. The paper also analyzes the results at different granularities and in detail.

3. The paper presents illustrative figures and charts. For example, Figure 1(a) serves as a good demonstration of STEM questions that give the readers a good sense on what the dataset looks like; Figure 4 clearly shows the different mechanisms of CLIP model and ChatGPT model.

### Weaknesses
1. The paper does not present strong enough evidence for its claims. The human evaluation part is not clear enough. Therefore, I am not convinced that current neural models fall far behind the human performance on the STEM dataset. The paper uses a score of 90 from IXL as a benchmark for elementary student performance, but this seems to represent an 'expert' level of mastery rather than typical performance. The use of Ph.D. students for expert-level evaluation, while understandable, further complicates the comparison, as their performance might not be a relevant upper bound for elementary-level STEM questions. A more detailed breakdown of the human evaluation process, including the number of participants, their backgrounds, and the specific instructions given, would be beneficial.
2. When benchmarking on SOTA models, the paper does not use the newest language model, i.e., GPT-4. If GPT-4 is tested, we might see quite significantly different results. The absence of GPT-4 results is a notable gap, especially given its reported advancements in reasoning and multi-modal capabilities. This omission limits the paper's ability to assess the true state-of-the-art performance on the proposed STEM benchmark. The paper should acknowledge this limitation and discuss the potential impact of including GPT-4 in future work.
3. The paper touched the bad case analysis, but not deep enough. As part of its biggest contribution, it will be better to make a more thorough analysis on the examples and patterns where the models fail. While the paper provides some error analysis, it lacks a detailed qualitative analysis of specific failure modes. A more in-depth investigation into the types of questions that models struggle with, including specific examples and error patterns, would provide valuable insights into the limitations of current models and guide future research directions. This should include a more granular analysis of errors across different subjects and skills.

### Questions
1. The claims that the paper concluded seem inconsistent with the results it presented. In the abstract, the paper claims that "these models are still well below (averaging 54.7%) the performance of elementary students, not to mention near expert-level performance." My questions and concerns are:
  - How do we define "the performance of elementary students"? I see that the paper compares the model performance with a score of 90, which "according to IXL, is considered excellent for a mastered skill", but it does not make sense to take a score of excellence as "the performance of elementary students", because it is an "expert-level" human performance.
  - Where is the number 54.7% from?
  - Besides, it doesn't seem fair to use Ph.D. students' test scores for the human evaluation of these elementary school questions.
2. What is the reason of not experimenting on GPT-4? It would be beneficial to test it since its performance has largely increased compared to GPT-3.5

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper propose a new dataset, named STEM, consisting of science, technology, engineering and math subjects. The proposed STEM includes 448 skills and 107M+ questions, which is a large-scale multimodal dataset. Upon the new dataset, this paper analyzes some existing foundation models, e.g., CLIP and ChatGP. Experiments show that these models are still below the human although the model is finetuned. Code and dataset are available.

### Strengths
1. The new dataset STEM is valuable, which consists a large-scale skills and questions.
2. The analyses of some foundation models on STEM are detailed and interesting.

### Weaknesses
1. Despite the analyses of foundation models, e.g., CLIP and ChatGPT, there are still some new and better models missing, such as EVA-CLIP, Kosmos-2, BLIP-2 and etc. What are the results of these models?
2. Does the quality of the caption model influence the performance of zero-shot performance on vision-language models. How about changing the caption model to a more accurate one, e.g., BLIP-2, GPT4 (I understand that the API may be not available now)?
3. What is the performance on other datasets after finetuning on STEM, e.g., VQA (2015)? Which is better when comparing with the model before finetuning? It would be important to verify that STEM is important and finetuning on STEM can maintain or improve the generalization of the model.

### Questions
Please refer to the Weakness Section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new dataset to test the STEM skills of neural models. This dataset is one of the largest and most comprehensive datasets for the STEM challenge, especially on fundamental skills in the K-12 curriculum. They test state-of-the-art foundation models on this challenge, but found limited performance. Even when training these models on a training split, the performance is still not satisfactory, which indicates the difficulty of this challenge and needs novel algorithms.

### Strengths
${\bf Strengths:}$

[$\textbf{New Dataset for STEM}$] This work introduces one of the largest and most comprehensive datasets for the STEM challenge.

[$\textbf{Presentation Quality}$] The presentation is clear and easy to follow.

### Weaknesses
 ${\bf Weaknesses:}$ 

[$\textbf{Missing Comparison}$] This work only shows the results of foundation models on the proposed dataset. It would be nice to also see the performance of the same foundation models on other datasets, which helps understand the difficulty of different datasets. Specifically, a comparison with existing STEM datasets, even if they are not perfectly aligned, would provide crucial context for the novelty and difficulty of the proposed dataset. Without this, it's hard to gauge whether the poor performance is due to the inherent difficulty of the task or limitations of the models themselves. The lack of comparison makes it difficult to position this dataset relative to existing benchmarks.

[$\textbf{Missing Limitation and Potential Impact}$] It would be nice to show the limitations and potential impacts of the proposed dataset. A thorough discussion of potential biases in the dataset, or areas where it may not generalize well, is essential. Furthermore, exploring the potential applications of such a dataset, beyond just evaluating model performance, would strengthen the paper's contribution. This discussion should include both positive and negative impacts, such as potential misuse or unintended consequences.

[$\textbf{Confusions in Figure 9}$] In Figure 9, for RN50, RN101 and ViT-B/16, the performance decreases when the model size becomes larger. Could the authors explain this a bit more? This is counterintuitive to the general trend observed in model scaling. It would be important to understand whether this is a limitation of the dataset or an artifact of the experimental setup. Factors such as training data size, optimization strategies, or even the specific architecture of the models could contribute to this behavior, and should be explored to ensure the results are reliable.

[$\textbf{Unconvincing Human Study}$] In the human study, the inclusion of only seven university students may not be fully representative, potentially limiting the generalizability of the findings to the broader population and raising considerations about the robustness of the observed human performance. The study should have a more diverse group of participants, including those with varying levels of STEM background. The current study does not provide a strong baseline for human performance on the dataset.

### Questions
- Could the authors show many examples for better understanding the dataset?

- Could the authors provide some directions for improving the performance according to your expertise?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
