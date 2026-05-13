# Lawma: The Power of Specialization for Legal Tasks

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Annotation and classification of legal text are central components of empirical legal research. Traditionally, these tasks are often delegated to trained research assistants. Motivated by the advances in language modeling, empirical legal scholars are increasingly turning to prompting commercial models, hoping that it will alleviate the significant cost of human annotation. Despite growing use, our understanding of how to best utilize large language models for legal tasks remains limited.
We conduct a comprehensive study of 260 legal text classification tasks, nearly all new to the machine learning community. Starting from GPT-4 as a baseline, we show that it has non-trivial but highly varied zero-shot accuracy, often exhibiting performance that may be insufficient for legal work. We then demonstrate that a lightly fine-tuned Llama 3 model vastly outperforms GPT-4 on almost all tasks, typically by double-digit percentage points. We find that larger models respond better to fine-tuning than smaller models. A few tens to hundreds of examples suffice to achieve high classification accuracy. Notably, we can fine-tune a single model on all 260 tasks simultaneously at a small loss in accuracy relative to having a separate model for each task. 
Our work points to a viable alternative to the predominant practice of prompting commercial models. For concrete legal tasks with some available labeled data, researchers are better off using a fine-tuned open-source model.$^\ddag$

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper produces a novel dataset, CaselawQA, of broad-ranging text classification tasks, based on the annotations of two US Supreme Court and Court of Appeals datasets (for a wide range of issues, everything from whether the defense attorney was a legal aid or public defender to whether a previous precedent was being overturned) and then investigates the success of current LLMs on these tasks. They find that prompting typical LLMs produces very poor results, often below a most frequent answer baseline, prompting GPT-4 or Llama 3 70B produces moderately good results, but that much better results can be produced by using a Llama 3 8B model fine-tuned for the various tasks at issue here. The result is not only a useful new benchmark but a strong result showing that in various distant-from-the-web domains, a fine-tuned small LLM can perform much better than a state-of-the-art huge LLM.

### Strengths
The strengths include:
- Carefully and thoroughly done experimentation. Even when I disagreed with the choices they made for how to measure things in the main paper, the way I would have done things is usually available in the lengthy appendices. The paper reads as comprehensive, not rushed.
- A valuable new benchmark dataset, with nearly all new tasks rather than just collating existing tasks.
- The tasks of the dataset are derived from a pre-existing database by programmatic means. This is a strength since they are annotations that have been built up by lawyers and political scientists and so have ecological validity, but a weakness in that they were in a sense pre-existing rather than this being a major contribution of new labeling.
- The paper is clearly and well written.

### Weaknesses
 - The tasks of the dataset are derived from a pre-existing database by programmatic means. This is a strength since they are annotations that have been built up by lawyers and political scientists and so have ecological validity, but a weakness in that they were in a sense pre-existing rather than this being a major contribution of new labeling.
- The paper is not very original: There is no new machine learning, there are several pre-existing benchmark legal datasets to which this adds another one, and not with a new type of task (all of them have many text classification tasks), and the central result that fine-tuning can outperform prompting has appeared in many places (as well as sometimes the opposite; it depends on various factors including model and data scale and the distance of the tasks from what appears in the pre-training and post-training data). E.g., https://www.semanticscholar.org/paper/Prompt-Engineering-or-Fine-Tuning-A-Case-Study-on-Trad-Chehab/505e4a7bedadab7f6de006c3c1e1144e272f4695, https://arxiv.org/abs/2408.01346, https://arxiv.org/abs/2402.17193, https://reglab.github.io/racialcovenants/ vs. the opposite in https://arxiv.org/abs/2309.01715 .


### Questions
[none of these are important fundamental questions wrt the paper]

line 129: Would not it actually be useful to show performance on LegalBench? It would be a useful test of transfer, beyond section xx, and give people a better indication of how useful Lawma would be in general for legal tasks with/without doing further fine-tuning?

line 246: I think this form of data sampling is questionable. It seems particularly questionable for binary tasks, since it ends up making the two classes balanced, which is the easiest case. Historically, it has usually been argued that text classification should be done as an unbalanced task, because that is the setting that has ecological validity, and the falsely high numbers that accuracy then gives can be dealt with by not using accuracy but macro F1 for evaluation. Of course, I saw that you have all the other settings in the appendix, so I'm not unhappy, just questioning the choice of setting for the main paper. 

line 290: Similarly, here, using micro-averaging not macro-averaging seems questionable, but you provide the opposite in the appendix.

line 411: While this graph is useful, the single axis for FLOPs is really unsystematically mixing scaling training data size and model size in a way that I think can cause as much fog as light. This isn't like a chart of Chinchilla-optimally scaled models for which we are comparing performance for different amounts of compute. Rather, if I have everything right (the paper doesn't give the details), the 6 Pythia models on the left are all trained on the same amount of data but are progressively larger models. You might conclude that models larger 410M make little difference for the benchmark here. Conversely, the 3 models 2nd, 3rd, and 4th from the right (Pythia 6.9B, Llama 2 7B, and Llama 3 8B) are all approximately the same size but differ by scaling the training the scaling data (and by instruction post-training of Llama 3 70B and Llama 3 perhaps just being better done than Llama 2). These results indicate that more pre-training data still really helps (well, at least very clearly on the Supreme Court tasks). The rightmost 2 data points return to a comparison of model size (it doesn't help much at large sizes). This suggests that around line 426 that suggesting more, better pre-training data is probably also a good source for improvements. Though I think all the big LLM companies are increasingly aware of this.

Figure 8: Given that most of the curves are still point up steeply, it would be lovely to also see results for 2500 train examples. But I realize you've already expended a lot of H100 hours on this paper. On the other hand, it seems like the graphs would be closer to a logarithmic scale and the steep curve between the first two points would be avoided if you also included points for 25 main examples, and that would cost much less to add.


Typos:

111 interests > interest;
317 were > where;
340 unfeasible > infeasible;
343 compared > compared to;
Lots of things need capitalization in the references, e.g. on line 546.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce a dataset of 260 legal text classification tasks, by extracting case text and labels from US Supreme Court and Court of Appeals. They evaluate different approaches such as prompt engineering, few-shot learning, and fine-tuning. It is not clear how much engagement the authors had with true legal experts in the creation of this dataset.

### Strengths
- Legal text processing has economic value but is difficult for most state of the art LLMs.
- The authors assemble a large dataset of real-world legal documents (via querying 3rd party services), annotated with diverse question-answering tasks.
- They show the effectiveness of fine-tuning on this dataset, over few-shot learning. They report performance of various tuning configurations.

### Weaknesses
 - There is little exploration of the relative difficulty of the different types of tasks they introduce—it would be useful to know more about which tasks that GPT-4 outperformed on, and where fine-tuning had minimal vs. substantial gains. Specifically, a more granular analysis of task difficulty, perhaps using metrics like inter-annotator agreement on a subset of the data, would be beneficial. This would help contextualize the performance of the proposed models.
- The paper is awkwardly organized, such as “limitations” abruptly inserted before the main contributions are outlined.
- “The costs and error of existing methods is the single most important bottleneck in the empirical legal studies pipeline.” (39-40) is vague and needs a citation.
- Despite the significant contribution of the dataset and language modeling performance, there is little methodological novelty to their approach. This begs the question of why ICLR is the appropriate venue for this work.

### Questions
- What process did you use to determine the relative difficulty of these tasks and whether they are comprehensive wrt the legal activities of humans? For instance the paper would benefit significantly from a legal expert's classification of the tasks by difficulty, followed by an analysis of Lawma according to those tasks
- What does "mixed answer" mean in Appendix G?
- Will you release the model weights and code?
- Is there any transferability across tasks—i.e., if you train a model on a subset of the task, how does it perform on the held-out tasks? Do you anticipate that in the future all subtasks of legal reasoning need to be spelled out, or is there a critical mass of legal subtasks that accrue towards "legal AGI" ?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new dataset of 260 classification tasks, derived from the USDB and USCAD resources. These tasks each require fairly long contexts, and can have a large number of classes (e.g. multi-label classification). They combine these tasks into an evaluation benchmark and show results for a variety of legal and otherwise SoTA models.  They find that most models struggle, although performance follows a monotonically increasing pattern based on pre-training compute.

They then propose to fine-tune the model on these law tasks, and show that fine-tuning them (which they call Lawma) results is significantly improved performance, across a wide range of tasks.

### Strengths
- The data proposed seems very useful and covers a broad range
- The analysis evaluates a wide range of models and situations
- The fine-tuning experiments show large gains can be had with domain-specific specialization.
- The appendix has a lot of good information about where the data came from and their inter annotator agreements

### Weaknesses
 - It is somewhat unclear how the authors created these tasks, in terms of how the questions were designed. E.g. who wrote the explanation for each of the legal variables provided by USCAD? How are the authors sure that these are accurate representations of the classification?
- [Minor] some of these tasks are pretty niceh/easy ("What state is associated with the respondent") but again this comes from using the variables in some schema.

### Questions
From Weakness 1: How did you make the prompts for the questions? 
Q2: What license does this fall under and will it be publicly released?

### Soundness
4

### Presentation
4

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
The paper explores the use of specialized language models for legal text classification, introducing CaselawQA, a dataset with 260 legal classification tasks based on U.S. Supreme Court and Court of Appeals cases. The authors evaluate various models, including GPT-4 and a fine-tuned LLaMA model (Lawma), to test whether specialization improves performance. They find that Lawma, trained specifically on CaselawQA, outperforms GPT-4 in accuracy by up to 20 percentage points. This performance boost highlights that fine-tuned, domain-specific models can handle nuanced legal tasks more effectively than general-purpose models. Additionally, the authors demonstrate that Lawma achieves high accuracy with limited labeled data, making it a feasible and cost-effective option for empirical legal research.

### Strengths
- **Clarity and Quality of Writing:** The paper is well-written, with clear explanations of the methodology and findings.
- **Dataset Contribution (CaselawQA):** CaselawQA is a valuable addition to the legal NLP field, featuring a comprehensive set of 260 legal classification tasks that reveal the limitations of general-purpose models in handling specialized legal contexts. Its diverse structure makes CaselawQA a beneficial resource for benchmarking capabilities of LLMs and advancing specialized model development.
- **Empirical Validation of Fine-tuning:** The study demonstrates the advantages of fine-tuning open-source models for legal tasks, with Lawma, a fine-tuned Llama model, consistently outperforming larger general-purpose LLMs like GPT-4 across various legal tasks. This empirical evidence supports the claim that domain-specific fine-tuning can yield more effective models for niche tasks, particularly within the legal domain.
- **Sample Efficiency Insights:** By analyzing performance across different sample sizes, the study provides valuable insights into the sample efficiency of fine-tuning, showing that Lawma can achieve high accuracy with limited labeled data. This practical approach underscores the feasibility of creating specialized models even with restricted datasets, a crucial benefit for resource-limited legal research settings.

### Weaknesses
 - **Limited Novelty in Contribution:** Although the paper effectively demonstrates the value of task-specific fine-tuning, the concept itself is not novel. Prior work has already shown that fine-tuned, specialized models outperform general-purpose LLMs [1, 2, 3]. This paper reinforces existing ideas rather than offering new methodologies or innovations in model specialization.

- **Overlooked Generalizability:** By evaluating Lawma exclusively on CaselawQA, a U.S.-specific dataset, the study limits insights into its effectiveness across other legal systems and domains [4, 5]. Without comparisons on datasets from different jurisdictions or areas of law, it’s challenging to assess the model’s broader applicability. Expanding evaluations to diverse legal datasets could strengthen the paper’s general claims about the effectiveness of fine-tuning for legal NLP tasks.

- **Narrow Focus on Text Classification:** The paper’s focus is restricted to text classification tasks, a valuable but limited subset of legal NLP. Broader experimentation on tasks such as legal text summarization for real-world low-resource data and hardware scenarios [6] could enhance the impact and relevance of the Lawma contribution for the legal community.

- **English-only Focus:** The experiments are conducted solely in English, overlooking the need for legal NLP solutions in low-resource languages and multilingual contexts [7, 8]. Legal research frequently requires cross-linguistic and multilingual analysis, and models that generalize across languages would have broader utility.

**Minor Presentation Weaknesses:**
- Typographical errors (e.g., "we conclude **that that** the performance") need correction.
- Figure 1 lacks clarity and could benefit from improved labeling or explanation to make differences in model performance more interpretable.
- The Limitations section would be more effective if positioned after the Conclusion, rather than within the Introduction, to ensure that findings are fully contextualized before limitations are addressed.

### Questions
- **Generalization to Other Jurisdictions:** Can the authors provide insights or preliminary findings on how well the Lawma models might transfer to legal data from jurisdictions outside the U.S. or to other branches and tasks of law?
- **Impact of Fine-tuning on Error Patterns:** What are some examples of typical errors Lawma makes, especially on complex tasks? Understanding these errors could help refine the approach and better inform future model improvements.
- **Exploration of Advanced Prompting Techniques:** The paper mentions that few-shot prompting did not improve GPT-4’s performance significantly. Were other advanced prompting methods, such as chain-of-thought or other reasoning prompts, considered? This could be relevant, as legal tasks often benefit from reasoning-style responses.

### Soundness
3

### Presentation
3

### Contribution
2
