# LiveXiv - A Multi-Modal live benchmark based on Arxiv papers content

- Decision: Accept
- Scores: 5, 6, 6, 5

## Abstract
The large-scale training of multi-modal models on data scraped from the web has shown outstanding utility in infusing these models with the required world knowledge to perform effectively on multiple downstream tasks. 
However, one downside of scraping data from the web can be the potential sacrifice of the benchmarks on which the abilities of these models are often evaluated. 
To safeguard against test data contamination and to \textit{truly} test the abilities of these foundation models we propose \method: A scalable evolving \underline{{live}} benchmark based on scientific Ar\underline{{Xiv}} papers. 
\method accesses domain-specific manuscripts at any given timestamp and proposes to automatically generate
visual question-answer pairs (VQA). This is done without any human-in-the-loop, using the multi-modal content in the manuscripts, like graphs, charts, and tables.
Moreover, we introduce an efficient evaluation approach that estimates the performance of all models on the evolving benchmark using evaluations of only a subset of models. This significantly reduces the overall evaluation cost.
We benchmark multiple open and proprietary Large Multi-modal Models (LMMs) on the first version of our benchmark, showing its challenging nature and exposing the models' true abilities, avoiding contamination. 
Lastly, in our commitment to high quality, we have collected and evaluated a manually verified subset. By comparing its overall results to our automatic annotations, we have found that the performance variance is indeed minimal ($<2.5\%$).
Our dataset is available online on \href{https://huggingface.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces LiveXiv, an automated multi-modal live benchmark system that generates Visual Question-Answering (VQA) pairs from ArXiv papers. The work is motivated by the critical issue of test set contamination in current LMM evaluations, as models increasingly train on web-scraped data that may include benchmark test sets. The authors propose an evolving benchmark using newly published scientific papers. Besides, they introduce an efficient evaluation method to make continuous assessment practical. Multiple open and proprietary LMMs are benchmarked.

### Strengths
1. The motivation is clear and good: this work addresses the critical issue of test set contamination in current LLM evaluations, as models increasingly train on web-scraped data that may include benchmark test sets.

2. This paper proposes a scalable live benchmark without any human involvement, automatically drawing data from online scientific manuscripts, generating multiple VQA pairs, and filtering these questions to reduce errors.

3. An efficient evaluation methodology is introduced, offering significant computational savings.

### Weaknesses
1. The paper heavily relies on one LLM, i.e., Claude for question filtering. While filtering aims to reduce errors, potential biases may arise from Claude being the only model used for answer verification. This can introduce an inherent bias in the benchmark, potentially skewing results to favor Claude's architecture and underlying methodologies. The superior performance of Claude-Sonnet shown in Table 1 may be partially attributed to the fact that Claude-Sonnet itself verified these questions, potentially making them more aligned with its capabilities. The authors might address this by including additional, distinct filtering mechanisms to mitigate model-dependent biases.

2. The paper suggests that only certain types of scientific data (e.g., block diagrams, qualitative visuals, charts) are categorized for question generation. While this is effective for consistency, it risks oversimplifying the diversity of visual data in scientific publications. Expanding the types of visuals and including more complex multi-modal question types (e.g., cross-referencing multiple figures) would make the benchmark more challenging and comprehensive.

3.The benchmark is restricted to multiple-choice format questions, which limits the evaluation of models' true generative and reasoning capabilities. Including free-form answering would provide a more comprehensive assessment of model understanding and better reflect real-world applications.

4. The benchmark evaluation would benefit from more comprehensive quantitative comparisons with established datasets like DocVQA and ChartQA. Such comparisons would better demonstrate LiveXiv's advantages over static benchmarks and more clearly illustrate how it addresses test contamination issues and aligns with human preferences.

### Questions
1. How does the system ensure diversity in question types and difficulty levels?

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
This paper propose a new live multimodal benchmark on scientific ArXiv papers. The authors also designed an efficient evaluation approach to rank the models. The authors verified their evaluation metric to be aligned with human evaluation with a small variance (<2.5%).

The main contributions are:
(1) A pipeline to generate and filter scientific paper VQA and TQA data using a document parsing pipeline (preprocessing), gpt-4o (generation), and Claude (filtering).
(2) An evaluation pipeline that, when evaluating a new model on the latest data, the pipeline re-evaluate old models on a subset of the latest data with a few old models for performance comparison.

### Strengths
1. The author propose to have a live benchmark is a promising direction to mitigate the impact of data contamination on holistic evaluation. It is challenging to maintain a live and scalable benchmark, and the author proposed several methods to resolve the challenges: a question-answer generation pipeline grounded on a structured pdf processor and powerful proprietary VLMs for generation and filtering, and an efficient evaluation algorithm to make model comparison affordable.
2. The proposed methods at both data curation stage and the evaluation stage have been shown to be effective in previous works on language-only datasets. The authors extend the thoughts to the multimodal domain and show these methods are still effective.
3. The human study shows the automatic data filtering pipeline is effective in removing annotation errors during data curation.

### Weaknesses
1. All questions are generated by gpt-4o, which may introduce issues such as the lack of diversity in questions. The reliance on a single model for question generation could lead to a narrow range of question types and biases inherent in that model's training data, potentially skewing the benchmark towards specific capabilities while neglecting others. This could result in an incomplete evaluation of a model's true multimodal understanding.
2. The authors only did human study for the question-answer filtering, while they did not verify if the final ranking of models is aligned with human perception and other established benchmarks. Without validation against human judgment of overall model ranking, it's unclear if the automatic evaluation metric accurately reflects real-world performance. Furthermore, comparison with existing benchmarks is needed to contextualize the difficulty and scope of the proposed benchmark.
3. As the author mentioned, the data curation replies on proprietary models, which makes the benchmark prone to bias and low reproducibility. The use of closed-source models for data generation and filtering introduces a black-box element, making it difficult to understand and mitigate potential biases. This lack of transparency also hinders reproducibility, as the exact behavior of these models may not be consistent or accessible to other researchers.
4. The question type is limited to multi-choice answering, while it could be more interesting if the authors could extend it to a broader categories of tasks such as long-form generation. The restriction to multiple-choice questions limits the evaluation to a narrow aspect of multimodal understanding. More complex tasks, such as open-ended question answering or descriptive image generation, could provide a more comprehensive assessment of model capabilities.
5. The novelty of the method: the authors should clarify their novelty by comparing with existing works that ask a powerful model to generate evaluation benchmark. For example, [1] also parses papers and ask an LLM to generate question for long-form paper question-answering. These works could be extended to VLM domains by swapping out the LLM to VLM and keeping add live new data to the benchmark in a straightforward way.

### Questions
1. How do the authors make sure the diversity of the VQA is also scalable? For example, if gpt-4o keeps generating many questions like "what is the number in the third row and second column of the table?", which will only evaluate a fixed OCR capability regardless of which timestamp the question is generated from.
2. Why the GPT-4o performs very badly in Table 1 while it is the model to generate the questions and answers?
3. How does the domain impact the evaluation scores? Could the authors show how models perform on different categories (as shown in Table 3) in different domains and see the correlation?
4. Despite I like the benchmark, could the authors clarify their innovation in method design beyond (1) taking an efficient evaluation strategy from nlp domain and apply it to vlm domain; (2) synthetic evaluation data generation using one proprietary api for generation and another for filtering which has been applied in nlp broadly even using the same apis? The pdf parsing is also a basic step in previous works  on paper QA. Could the author provide a clear statement of their key technical innovations and how they differ from or improve upon existing approaches and include a discussion of how combining these existing techniques in a novel way for this specific application represents an innovation?

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
This paper introduces an evolving benchmark derived from arXiv papers, utilizing LLMs to automatically identify and generate visual-based question-answer pairs from the multi-modal content within manuscripts. To manage the growing dataset efficiently, an evaluation method is proposed that avoids the need to assess every method as the dataset expands.

### Strengths
1. A large-scaled dataset that could be very useful for people in the VQA domain. 
2. I like the idea of 'evaluating the dataset in a dynamic way'. As most of the datasets get contaminated as training data increases by time. 
3. A rather comprehensive evaluation of the dataset, covering most state-of-the-art LMMs.

### Weaknesses
1. A limitation of this work is that it relies on OCR to extract only tables and figures, using only their captions as input to create the dataset. This approach ignores the broader context of the paper, which may contain valuable information. For instance, many tables have generic captions like "Main experimental result of our proposed method," which may lead GPT-4 to generate only simple structure-related questions, such as "Which column has a value of **," rather than more insightful content-based questions.

2. As the dataset is entirely LLM generated, it's necessary to perform some human evaluation to avoid hallucinations and errors. Even though it's not feasible to perform such evaluation on the entire dataset, at least a small portion could be sampled and more detailed manual check could be performed beyond the simple one briefly described in Line 255.

3. I'm not sure about the efficiency and robustness of the evaluation model, even though I appreciate the idea, given the diverse styles and topics of newly added arXiv papers. Previous LMMs may become outdated, exhibit biases, and struggle to handle shifts in data distribution effectively.

### Questions
In Line 235, which LLM do you use here?
How do you select the test set in Table 1?
Line 458, which 5 models are selected by the algorithm exactly?

### Soundness
3

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
3

### Summary
The study presents LiveXiv, a multi-modal live VQA benchmark designed to evaluate the capabilities of LMMs on scientific content from ArXiv papers. The benchmark addresses the issue of test data contamination by continuously evolving and utilizing the latest data, thereby providing an up-to-date assessment of model performance. LiveXiv automatically VQA pairs from figures, charts, and tables in scientific manuscripts without human intervention, leveraging advanced LMMs like GPT-4o and Claude. The study also introduces an efficient evaluation approach that estimates the performance of all models on the evolving benchmark by evaluating only a subset, thereby reducing evaluation costs.

### Strengths
1) It is a innovative approach to creating a live, contamination-free benchmark that is both scalable and efficient. 
2) The use of advanced LMMs for automatic generation and filtering of VQA pairs is commendable, as is the development of an efficient evaluation method inspired by Item Response Theory, which reduces computational overhead. 
3) he benchmark's design allows for the expansion into new domains, potentially increasing its relevance and applicability.

### Weaknesses
1) The scope of work presented may not be substantial enough for a benchmark paper, as the number of samples and the diversity of domains covered could be expanded. 
2) While the idea of a contamination-free benchmark is valuable, the study's focus on Knowledge-VQA tasks narrows its applicability and relevance. Data contamination is a broader issue that extends beyond Knowledge-VQA tasks. 
3) The reliance on proprietary LMMs for the benchmark's operation introduces potential variability and a lack of control over the evaluation process
4) The efficient evaluation method shows promise, its effectiveness and reliability over time and across different versions of the benchmark need further validation.

### Questions
Please address my concerns above.

### Soundness
2

### Presentation
2

### Contribution
2
