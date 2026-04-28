# MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
Multimodal Language Language Models (MLLMs) demonstrate the emerging abilities of "world models"---interpreting and reasoning about complex real-world dynamics. 
To assess these abilities, we posit videos are the ideal medium, as they encapsulate rich representations of real-world dynamics and causalities.
To this end, we introduce \benchmarkname, a new benchmark for multi-discipline, multi-faceted multimodal video understanding.
\benchmarkname distinguishes itself from previous video understanding benchmarks with two unique advantages: (1) \textbf{multi-discipline}, covering various disciplines that often require domain expertise for comprehensive understanding; (2) \textbf{multi-faceted reasoning}, including explanation, counterfactual thinking, future prediction, etc.
\benchmarkname consists of a human-annotated dataset to evaluate MLLMs with questions about the whole videos and a synthetic dataset to analyze MLLMs within a single modality of perception. 
Together, \benchmarkname encompasses 1,910 videos across seven broad disciplines and 69 subdisciplines, complete with 6,627 question-answer pairs and associated captions. 
The evaluation includes 2 proprietary and 10 open-source MLLMs, which struggle on \benchmarkname (e.g., GPT-4V performs the best with only 52.3\% accuracy), showing large room for improvement. Further ablation studies reveal other interesting findings such as models' different skill sets from humans. We hope \benchmarkname can serve as an essential step towards world model evaluation in videos.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MMWorld, a new benchmark for evaluating multimodal large language models' (MLLMs) ability to understand and reason about video content across multiple disciplines. The benchmark consists of 1,910 videos spanning 7 broad disciplines and 69 subdisciplines, with 6,627 question-answer pairs. The key innovation is its focus on multi-faceted reasoning (explanation, counterfactual thinking, future prediction, domain expertise) and multi-discipline coverage. The authors evaluate 15 MLLMs (both proprietary and open-source) on this benchmark and provide detailed analysis of model performance and error patterns.

### Strengths
1: The benchmark makes a novel contribution by filling an important gap in evaluating MLLMs' world modeling capabilities through video understanding across diverse disciplines.

2: The evaluation framework is comprehensive, covering seven broad disciplines and 69 subdisciplines while testing multiple reasoning types including explanation and counterfactual thinking.

3: The methodology demonstrates rigorous attention to detail, with well-documented data collection processes and multiple evaluation strategies.

4: The research provides valuable insights by identifying significant performance gaps in current MLLMs and revealing interesting differences between human and MLLM capabilities through detailed error analysis.

### Weaknesses
1. The dataset, while diverse, remains relatively similar compared to other modern benchmarks. Please include the recent works and discuss the difference between MMWorld and recent works, such as VideoMME, MMBench-Video.

2. The evaluation methodology shows potential bias through its heavy reliance on GPT-4V as a judge and in synthetic dataset generation.

3. The temporal reasoning aspect, though claimed as a key feature, could be more thoroughly explored and evaluated in the benchmark.

4. How to get the final results with the three subsets (Main Subset, Synthetic I, Synthetic II) in Table 3?

5. As the evaluated models cannot handle the audio modality, is the model's performance on the audio-related questions underestimated?

6. As the current VLMs are not the world model and the current questions in this benchmark are also limited to basic QA, limiting complex reasoning tasks. I think the author may reconsider the name of the benchmark to avoid over-claiming.

7. More in-depth analysis of the errors from the perspective of current VLM's architecture, training data, or training techniques would improve the work.

### Questions
As comments in Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a comprehensive benchmark for MLLMs, covering 7 major disciplines, 69 subdisciplines, and multi-faceted reasoning tasks. The authors conducted experiments on 15 models (including both open-source and closed-source models) and analyzed the results.

### Strengths
* This benchmark encompasses 7 major disciplines and 69 subdisciplines, offering comprehensive coverage and highlighting its advantages over existing benchmarks.
* The authors introduced a new dataset, ensuring its quality through human annotation.
* The experiments are conducted on a large scale, covering mainstream MLLMs and providing analysis across different difficulty levels.

### Weaknesses
 * Although the authors conduct an error analysis with six different categories, the error sample size is relatively small.
* The analysis of experimental results across different models lacks depth. For example, what specific differences exist between model and human reasoning? It would be helpful to compare with human performance, as in business discipline, the model achieves 90% accuracy, showing a strong understanding ability. It is not surprising that MLLMs perform better than average humans. It would be meaningful to see whether the model has reached a level close to or beyond human expert performance, especially in business discipline.

### Questions
1. Based on the results in Table 3, it appears that MLLMs perform significantly better in the Business discipline compared to other disciplines. Does this imply that the QA pairs in the Business discipline are relatively simpler, or does it indicate that MLLMs are stronger in the Business discipline than in other disciplines?
2. The authors emphasize that they have introduced a new dataset. I did not see an anonymous dataset link in the paper. Where can I find it?
3. Typos:
 • “an characteristic” in Figure 1.
 • “%%” at line 215.

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
4

### Summary
This work proposes a novel benchmark to evaluate commonsense knowledge and reasoning capabilities of the existing multimodal LLMs that are capable of processing videos or sequences of images. The proposed benchmark is classified as *multi-discipline* since it includes videos from a diverse set of subjects, and it is also classified as *multi-faceted* because it also includes different types of tasks where some tasks are focusing on commonsense reasoning abilities. The authors also collected a synthethic dataset to evaluate either auditory or vision processing capabilities of these models. The experiments reveal that (i) most of the existing models fail to excel in the proposed benchmark, (ii) even the proprietary models lack deficiency in embodied tasks, (iii) and they fail to process auditory information sufficiently.

### Strengths
I think the most valuable aspect of this paper, the proposed dataset contains videos from a diverse set of subjects, and questions have a variety focusing on commonsense knowledge and reasoning. This unique combination could position the benchmark as an important resource for the near future, as recent models fails to thrive in this video question answering benchmark.

### Weaknesses
- Presentation could be improved (see the questions field).
- The paper actually has a main contribution, which is human annotated dataset. There are also two synthetic datasets to evaluate the performance of individual modality processing performances of the models that are capable of processing both vision and audio. This aspect complicates this work a little bit, where I think it would better to have a separate work which carefully examines how well the models process each modality.
- The related work could be improved there are a lot of recent related work which are missing (e.g. [TempCompass](https://arxiv.org/abs/2403.00476), [VILMA](https://openreview.net/forum?id=liuqDwmbQJ), [VITATECS](https://arxiv.org/abs/2311.17404v1), also older but related since nearly half of the questions focus on explainability [Next-QA](https://arxiv.org/abs/2105.08276))
- The imbalanced nature of the subtasks: 48% of the questions belong to the explanation category/task. Also, the main task figure gives the impression of that these tasks could be fluid. For instance, the *explanation* example also requires *spatiotemporal reasoning*, and *future prediction* requires also some *domain-expertise*. Maybe, rather than assigning just single category, they could have multiple categories.

### Questions
- The hexagon figure (Fig.4) is really difficult to interpret: I think this kind of figures makes sense if one compares 3 models at most. The score normalization makes things even worse: So we cannot see how well the best model performs in this way. I would definitely remove it from the paper, and put the Table 8 into the main text. Also note that the figure is embedded as "PNG/JPEG" instead of "PDF" (but removing it from the paper would make things much more better).
- Fig. 6 is also hard to interpret. I would rather group some selected models instead of error categories, so one can observe which model produces what kind of errors more or less.
- Is there any example for auditory questions in the appendix? Can you please point? Can we see some synthethic questions/answer pairs generated using vision and audio side-by-side?
- How much diverse is the language, i.e. questions and answers?
- One suggestion: Please embed all figures as PDFs.
- It would be good to see many more examples in the appendix in a more compact format by avoiding large text with conversation bubbles.

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
4

### Summary
This paper introduces MMWorld, a new benchmark designed for multi-disciplinary, multi-faceted multimodal video understanding. MMWorld comprises 1,910 videos spanning seven broad disciplines and 69 sub-disciplines, along with 6,627 question-answer pairs and corresponding captions.

### Strengths
- MMWorld is the first video benchmark to cover videos beyond the general visual domain.
- The paper includes several analyses to assess the strengths and limitations of current video large language models (LLMs).

### Weaknesses
 - Regarding multi-faceted abilities, almost all are already evaluated in previous datasets, such as CVRR and Tempcompass. This raises the question of the necessity for another benchmark to assess these capabilities, especially as the data in MMWorld also comes from YouTube, which may reduce its novelty and significance.

- For multi-discipline evaluation, the use of GPT-4V to generate questions raises concerns about ensuring expertise-level quality, as seen in MMMU, which uses college exam questions to maintain a rigorous standard. If the generated questions don’t meet this level, it blurs the distinction between domain-specific and general-domain questions. If no substantial difference exists, a model that performs well in general-domain benchmarks (e.g., CVRR or Tempcompass) may also perform well in MMWorld, potentially limiting the unique insights this new dataset could offer.

### Questions
- Regarding multi-discipline evaluation, if a model underperforms in specific domains, is it due to a lack of general domain knowledge, specific domain ability, or both? Designing experiments to analyze this would be valuable. For instance, comparative testing with models pre-trained on general knowledge versus those fine-tuned with domain-specific datasets could help isolate the impact of each knowledge type on performance.

### Soundness
3

### Presentation
3

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
The paper introduces MMWorld, a new benchmark designed to evaluate multimodal large language models (MLLMs) across multiple disciplines in their understanding of real-world dynamics. MMWorld includes three datasets: a manually annotated dataset for multimodal reasoning and two automatically generated datasets focused on audio and visual understanding, respectively. Comprehensive baseline results and analyses demonstrate the challenges presented by MMWorld, with a detailed examination of primary errors and valuable insights.

### Strengths
1.To my best knowledge, MMWorld is the first video understanding dataset that contains diverse question types necessitating knowledge from multiple disciplines.

2.The baselines and analyses are comprehensive, covering 15 advanced MLLMs.

### Weaknesses
1.	According to the results in Table 3, GPT-4o already achieves high performance (80%~90%) on some disciplines, significantly surpassing other competitors. However, the QAs are generated and the model predictions are evaluated by GPT-4 families. This raises a concern that the dataset is likely biased to the knowledge of specific models (GPT-4). It would be better to show how the human annotators are instructed to amend the generated QAs.

2.	The paper seems forget to discuss and compare with two related benchmarks: NExT-QA and Causal-VidQA. The two benchmarks also emphasize explanation, temporal dynamics, counterfactual and future predictions, respectively.

### Questions
For the first weakness. I hope the authors can provide the followings:

1. The instructions given to human annotators for reviewing and modifying generated QAs.
2. The criteria used for accepting or rejecting generated QAs.
3. Any measures taken to ensure diversity of knowledge sources beyond GPT-4.
4. The percentage of questions that were significantly modified or entirely rewritten by human annotators.

For the second weakness. I suggest that the authors include a comparison that explicitly compares MMWorld to NExT-QA and Causal-VidQA, especially on the types of reasoning tasks.

Finally, I find that the average scores (the right most column) in Table 3 are much below than the average of the 7 disciplines. Any explanations on how to obtain the average scores?

### Soundness
3

### Presentation
2

### Contribution
3
