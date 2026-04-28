# MMCOMPOSITION: Revisiting the Compositionality of Pre-trained Vision-Language Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
The advent of large Vision-Language Models (VLMs) has significantly advanced multimodal understanding, 
enabling more sophisticated and accurate integration of visual and textual information across various tasks, including image and video captioning, visual question answering, and cross-modal retrieval. 
Despite VLMs' superior capabilities, researchers lack a comprehensive understanding of their compositionality -- the ability to understand and produce novel combinations of known visual and textual components. 
Prior benchmarks provide only a relatively rough compositionality evaluation from the perspectives of objects, relations, and attributes while neglecting deeper reasoning about object interactions, counting, and complex compositions. 
However, compositionality is a critical ability that facilitates coherent reasoning and understanding across modalities for VLMs. 
To address this limitation, we propose \textbf{\NAME}, a novel human-annotated benchmark for comprehensively and accurately evaluating VLMs' compositionality. 
Our proposed benchmark serves as a complement to these earlier works. With \NAME, we can quantify and explore the compositionality of the mainstream VLMs. 
Surprisingly, we find GPT-4o's compositionality inferior to the best open-source model, and we analyze the underlying reasons. 
Our experimental analysis reveals the limitations of VLMs in fine-grained compositional perception and reasoning, and points to areas for improvement in VLM design and training. Resources available at: 
 \href{https://hanghuacs.io/MMComposition/}{\textcolor{iclrblue}{\fontfamily{cmtt}\selectfont{hanghuacs.io/MMComposition}}}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MMComposition, a QA benchmark that evaluates the compositional capabilities of modern vision-language models. MMComposition encompasses a range of tasks, including perception, reasoning, and probing, with multiple subtasks presented in various QA formats: yes/no, multiple-choice, and indefinite-choice. The dataset is curated from numerous existing sources, with QA pairs annotated by humans. Covering 13 distinct vision-language compositionality tasks, this benchmark offers a comprehensive evaluation of both proprietary and open-source vision-language models. The paper also analyzes factors that may influence the compositional abilities of VLMs, such as the resolution of visual encoders, the scale of language decoders, and the volume of training data.

### Strengths
- This paper presents a comprehensive benchmark focused on compositionality, encompassing a wide range of skills from perception and reasoning to probing.

- This paper provides an extensive evaluation of recent models, including both open-source and API-based models, highlighting areas where they continue to fall short of human capabilities.

- The paper is well-written with clearly organized sections.

### Weaknesses
 - Although the benchmark includes diverse skill sets and QA formats, the specific aspects that pose challenges are not clearly defined. It is also unclear what distinguishes this benchmark from other general QA datasets designed to test modern VLMs for AGI, such as MMMU, MMStar, and tons of similar benchmarks. The paper does not provide comparisons in terms of general capabilities across QA datasets; instead, it focuses on embedding-based benchmarks for comparison, as shown in Table 1. Comparing the scale of evaluation samples, such as the number of images or questions across different benchmarks, would also be valuable.


- Related to the first weakness, one might question whether this benchmark is truly challenging. Some compositionality benchmarks or visual QA tasks could potentially be solved using only language models in an image-blind setting, due to language priors, such as coherence, grammar, and clues embedded across answer choices. As specific example, in second example in figure 3, can is often made of metal, such knowledge aids in answering correctly without relying on visual cues. It would be beneficial to examine the proportion of questions that can be solved solely using large language models. 


- Several essential details are missing regarding the benchmark construction. In the human annotation process, additional information is needed: Who annotated the dataset? How was confidence measured, and how were errors handled in finalizing the annotations? Additionally, it’s unclear how misaligned captions were manually added in the probing task (line 255). Furthermore, for reporting human performance, what was the process? It would be important to present individual human performance scores for each skill, rather than a single overall score.


- The empirical trends concerning the scale of the visual encoder, language decoder, and training data are perhaps not surprising. The paper does not analyze whether these trends are specific to the proposed benchmark or if they also appear in other general visual QA benchmarks. Meanwhile, an additional suggested analysis could explore how the design of the visual connector (e.g., fully connected layer or Q-Former style) and the method of visual token insertion (e.g., tokens input directly into the language model or through cross-attention connections) impact performance of the proposed benchmark. 


- There are some notable clarity issues, including typographical errors such as 'MuriBench' in line 237 and 'ARC' in line 241. Additionally, there are inconsistencies in publication years for certain cited papers, particularly recent NeurIPS papers like SugarCrepe, which collectively raise concerns about professionalism. 


- Could fine-tuning VLMs on specific datasets improve performance on MMComposition?

### Questions
- The reasoning behind the name 'MMComposition' is unclear.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new compositional reasoning benchmark that is constructed from existing benchmarks (data collection, lines 211-238) augmented with negative options retrieval by similarity, consensus filtering by several recent LMMs and further human filtering of the resulting visual QA. An extensive evaluation of recent models on the proposed benchmark is performed. Some additional ablations are attempted by grouping models trained on more data, larger LLM decoders, vis. encoder combinations etc. However, those only confirm known facts: larger data, larger decoders, or more encoders are beneficial. Some analysis of failures is provided, albeit only qualitative. Main interesting aspect seems to be a large gap reported between human performance and the models. However, no statistics of the human subjects are provided (eg how many humans were employed, how they were motivated, what was the disagreement between humans, age groups, etc.).

### Strengths
* new benchmarks are always good, human curation is appreciated
* large number of models evaluated

### Weaknesses
 * no new data is introduced, built from existing benchmarks
* no surprising conclusions
* no statistics for the human subjects
* error analysis is only qualitative
* dataset construction methodology involving humans could be more interesting - eg. humans could generate questions, red-team models to generate hard negatives etc.
* I disagree with Table 1, many benchmarks, including those listed have fine-grained questions, there are benchmarks (eg NVLRv2) involving multiple images, other benchmarks have human filtering, at least a partial subset, the only thing I indeed did not encounter before is "multiple right answers" (indefinite choice) - which could indeed be a contribution of the paper
* while benchmark contributions are appreciated, it seems this paper is somewhat below what I would expect from the level of contribution of an ICLR paper

### Questions
please see weaknesses

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
The paper "MMCOMPOSITION: Revisiting the Compositionality of Pre-Trained Vision-Language Models" presents MMCOMPOSITION, a new benchmark focused on testing VLMs' ability to handle complex compositional tasks like object interactions, counting, and scene reasoning. With 4,342 annotated questions across 13 categories, the benchmark highlights a clear performance gap between models and humans (67.95% vs. 90.31% accuracy). Results suggest that improving high-resolution encoders, scaling language decoders, and expanding training data are key to better compositional reasoning in VLMs. MMCOMPOSITION offers a practical tool for refining future VLMs to better understand complex compositions.

### Strengths
Strengths of MMCOMPOSITION:

1. Targeted Evaluation of Compositionality for VLMs: MMCOMPOSITION provides a focused benchmark to assess compositional reasoning in Vision-Language Models, an area where existing models often fall short. By going beyond basic attribute recognition, MMCOMPOSITION evaluates tasks like multi-image reasoning, object interactions, and counting, all of which are crucial for real-world, nuanced understanding.

2. Improvement upon Existing Compositional Datasets: This benchmark builds on and enhances data from existing compositional datasets, such as ARO, to create a more diverse and challenging evaluation framework. By curating tasks that move beyond traditional benchmarks, MMCOMPOSITION offers a comprehensive dataset for testing complex visual-language interactions.

3. In-Depth Model Comparison and Component Analysis: MMCOMPOSITION evaluates over 50 VLMs across different architectural components, allowing a detailed comparison. This thorough assessment reveals how factors like encoder resolution, decoder size, and training data diversity impact compositional reasoning. It offers practical insights that can guide future improvements in model design.

### Weaknesses
typos:
table 4 - Relolution 

1. In-context multimodal compositionality: Adding tests for in-context multimodal compositionality could strengthen the benchmark, as this capability is crucial for real-world applications. Evaluating models' ability to maintain compositional understanding across multi-modal inputs, rather than isolated tasks, could enhance the dataset's relevance.
2. Multi-hop compositional problems: The paper would benefit from including multi-hop reasoning tasks, where models must integrate multiple compositional steps to arrive at an answer. This kind of problem is essential for advanced compositionality and would make the benchmark more challenging and comprehensive.
3. Questionable novelty: The novelty of the paper could be improved if it incorporated points 1 and 2. Adding in-context multimodal compositionality and multi-hop compositional problems would make MMCOMPOSITION a more distinctive and valuable benchmark.

### Questions
see weaknesses

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
The paper proposes MMComposition - a human-annotated benchmark dataset for evaluation of the compositionality of large Vision-language models. 
The benchmark contains 4.3K questions in three main dimensions: perception, reasoning and probing which are divided into 13 categories. There are both questions that contain a single image and multiple images. Most questions have a single correct answer. There are 459 questions with indefinite-choice.
The benchmark demonstrates human performance (90.31%) and state-of-the VLMs (best performance of 67.95% among 54 evaluated VLMs). 
There is also analysis of impact of VLM architecture factor on the benchmark performance, e.g. visual encoder design, language decoder size, training data volume.

### Strengths
1) The dataset is human-annotated and covers a wide range of tasks in terms of compositional understanding
2) The paper evaluates 54 representative large VLMs including open-source and proprietary ones. The benchmark is challenging and demonstrates large performance gap between human and VLMs. 
3) The analysis on model component provides valuable insight on model design.

### Weaknesses
1) The paper categories the questions into 4 difficulty levels based on the performance of 6 open-source models. In Figure 8, it shows that 62.09% of questions in the category “superhard” lead to the average performance on all VLMs below the average level. It would be interesting to analyze what characteristics lead to the different difficulty levels of these questions? This can shed light on how to design difficult questions for the competent VLMs. 
2) In the evaluation benchmark, for questions that contain multiple images, the images are concatenated into a big collage and fed into the model. Some of the VLMs have multiple-image samples in the training data and can perform VQA with multiple input images. Does it impede the performance of these models to feed the collage into them?

### Questions
1) In line 254, “we select several captions from the dense captions in Visual Genome as the correct options and write the misaligned captions manually for the image”
What are the criteria for writing the misaligned captions? In terms of which characteristics do the misaligned captions differ from the original captions?

### Soundness
3

### Presentation
3

### Contribution
3
