# CS-Bench: A Comprehensive Benchmark for Large Language Models towards Computer Science Mastery

- Decision: Accept
- Scores: 8, 5, 6, 8

## Abstract
Computer Science (CS) stands as a testament to the intricacies of human intelligence, profoundly advancing the development of artificial intelligence and modern society. However, the current community of large language models (LLMs) overly focuses on benchmarks for analyzing specific foundational skills (e.g. mathematics and code generation), neglecting an all-round evaluation of the computer science field. To bridge this gap, we introduce CS-Bench, the first bilingual (Chinese-English) benchmark dedicated to evaluating the performance of LLMs in computer science. CS-Bench comprises approximately 5K meticulously curated test samples, covering 26 subfields across 4 key areas of computer science, encompassing various task forms and divisions of knowledge and reasoning. Utilizing CS-Bench, we conduct a comprehensive evaluation of over 30 mainstream LLMs, revealing the relationship between CS performance and model scales. We also quantitatively analyze the reasons for failures in existing LLMs and highlight directions for improvements, including knowledge supplementation and CS-specific reasoning. Further cross-capability experiments show a high correlation between LLMs' capabilities in computer science and their abilities in mathematics and coding. Moreover, expert LLMs specialized in mathematics and coding also demonstrate strong performances in several CS subfields. Looking ahead, we envision CS-Bench serving as a cornerstone for LLM applications in the CS field and paving new avenues in assessing LLMs' diverse reasoning capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Develops CS Bench, a benchmark dataset of CS expertise that tests the ability of LLMs in computer science, as well as the relationship between CS math and code programming ability.  The benchmark measures 4 languages and 26 sufields with 9676 samples. To test this they evaluated using 30 LLMs.

The datasets were constructed using professional exams and practice tests widely available on the internet; extraction from blog articles of questions and answers; teaching materials and exams from the authors institutions.  For scoring, the authors use autoraters (GPT4) for genration tasks and  for comprehension tasks use questions where they can score with a regex

### Strengths
The strength of the paper is the dataset . This type of dataset is extremely valuable and I especially appreciate the sourcing of exam questions from universities and the knowledge transfer from blogs across specialized fields with such a large corpus of questions.  The final version of the paper should explain exactly where the questions came from, including giving the class and level at the university so that the difficult level is clear. 

I'd also call out the thoroughness of the analysis. The different correlations noted, eg math and CS ability and so forth, are interesting as is the relationship between performance and tokens across scales. None of these are unexpected but they are nice things to see.

### Weaknesses
The first sentence "Computer Science (CS) stands as a testament to the intricacies of human intelligence, profoundly advancing the development of artificial intelligence and modern society"  is a bit much and some of the corresponding language needs to be toned down. Could we please not philosphize about the importance of specific fields (especially those were we are practitioners) and instead focus on the task that the paper accomplishes -- building a novel eval set and using it.

Other than this, the generative questions that require autorating to score are less convincing than the regex. The authors are right to emphasize that people should focus on this dataset if they can, but it does make me wonder whether the generative questions could be downgraded even further.

### Questions
What does your dataset not include for testing compettency in CS?
What level does this test? The level is notably absent from the paper -- but staging this relative to expertise (high school, undergrad, grad, etc) is extremely useful. 
What is the breakdown of problems in the benchmark to expertise?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a benchmark of 10k test samples that pertain to Computer Science specific knowledge.

### Strengths
1. Commendable that 70% of the benchmark is from private source not already on the intrernet.

2. The paper has a somewhat thorough review of several LLMs on where they stand in the benchmark.

### Weaknesses
1. It is not clear what the benchmark aims to achieve or improve. LLMs are already good at MCQ, open-ended, FITB and T/F questions. There is no coding in the benchmark. The authors need to discuss more clearly why this is pivotal and important to the field.

2. Scoring on the benchmark appears to be ad-hoc with regular expression matching, instead of measuring with existing techniques.

3. The benchmark lacks a fingerprint to prevent training. THis would be required to protect the integrity of the benchmark.

4. The paper indicates that this may help evaluate or improve reasoning though it is unclear how?

### Questions
Q1. What would the key contributions of the benchmark be to the field at large, as it stands today?

Q2. Can the authors evaluate the value of the data through one of several Value-of-Data approaches including perplexity of training on the benchmark, FT-ing on the benchmark or other approaches?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces CS-Bench, a comprehensive, multilingual benchmark designed to evaluate the computer science knowledge and reasoning abilities of Large Language Models (LLMs). Comprising approximately 10,000 meticulously curated samples across 26 subfields within four key CS areas (Data Structures and Algorithms, Computer Organization, Computer Networks, and Operating Systems), CS-Bench supports evaluation in English, Chinese, French, and German, and includes diverse task formats such as multiple-choice, assertion, fill-in-the-blank, and open-ended questions. The authors conduct an extensive evaluation of over 30 mainstream LLMs on CS-Bench, analyzing their performance relative to model scale and investigating the reasons for model failures. They further explore the relationship between LLM capabilities in computer science, mathematics, and coding, observing strong correlations and evaluating the performance of specialized expert LLMs on the benchmark. The findings suggest a logarithmic growth relationship between model scale and CS performance, highlight the challenge of CS-specific reasoning for LLMs, and reveal the potential for expert LLMs to improve performance in certain CS subfields. CS-Bench aims to serve as a valuable resource for assessing and improving the diverse reasoning capabilities of LLMs in the context of computer science.

### Strengths
Focus on Reasoning: The inclusion of both knowledge-based and reasoning-based questions is a good step towards a more comprehensive evaluation of LLMs' understanding of CS concepts.

Extensive Evaluation: Testing numerous LLMs, both open-source and closed-source, across various scales provides a good overview of current capabilities and highlights areas where models struggle. The scale-score analysis is also a useful contribution.

Comprehensive Benchmark: The breadth of CS topics covered, along with the multilingual aspect and diverse task formats (multiple-choice, assertion, fill-in-the-blank, open-ended), makes this a valuable contribution. Creating such a benchmark is a substantial undertaking.

Error Analysis: The analysis of error types provides some insights into the reasons for model failures and points towards potential directions for improvement.

### Weaknesses
Writing and Presentation Could Be Improved: The writing is occasionally dense and could be more concise and clear. Some figures, especially the radar charts, are difficult to interpret and don't effectively communicate the key findings. A more visual and intuitive presentation of the results would enhance readability and impact.

Limited Insight into Cross-Capability Relationships: While the paper shows correlations between CS, math, and coding abilities, it doesn't delve deeply into why these correlations exist. More in-depth analysis is needed to understand the underlying factors driving these relationships. Do specific architectural choices or training data characteristics explain the observed correlations? The analysis of expert LLMs is a step in the right direction, but it lacks depth. How do the internal representations of CS concepts differ between general and expert LLMs?

Lack of Actionable Insights for Improvement: The error analysis, while pointing towards knowledge gaps and reasoning challenges, doesn't offer concrete suggestions for how to address these limitations. Beyond general recommendations like "knowledge supplementation" and "CS-specific reasoning," what specific techniques or strategies could be employed to improve LLM performance on CS tasks? Exploring methods like curriculum learning, incorporating external knowledge sources, or fine-tuning on specific CS datasets could provide more actionable insights.

Limited Discussion of Benchmark Biases: All benchmarks have biases. What are the potential biases in CS-Bench, and how might these biases influence the results? For example, the reliance on university-level content might not fully reflect the diversity of CS tasks in real-world applications. Addressing this limitation by including tasks from different levels of expertise or from specific industry applications would strengthen the benchmark's generalizability.

### Questions
Reducing Reliance on GPT-4 for Evaluation: The dependence on GPT-4 for scoring generative tasks raises validity and reproducibility concerns. While you explored alternative scoring models and human evaluation, these were limited. Could you elaborate on the feasibility of using alternative automatic metrics like BLEU, ROUGE, or METEOR, perhaps in conjunction with domain-specific constraints or regular expressions? Could a smaller, more accessible model be fine-tuned specifically for evaluating CS-related generative tasks? This would improve reproducibility and lower the barrier for other researchers to use CS-Bench. Also, provide more details on the human evaluation: the number of annotators, their expertise level, and the specific guidelines they followed. Calculating inter-annotator agreement (e.g., using Cohen's kappa) would strengthen the validation of both human and GPT-4 scoring.

Deepening the Analysis of Cross-Capability Relationships: The observed correlations between CS, math, and coding performance are interesting, but the analysis lacks depth. Could you investigate why these correlations exist? Are certain model architectures better suited for integrating these skills? Does the training data composition play a significant role? Analyzing the internal representations of CS concepts in general vs. expert LLMs could provide valuable insights. Consider using techniques like probing tasks or representational similarity analysis to understand how different models learn and represent CS knowledge. This would move beyond simple correlations to provide a more mechanistic understanding of cross-capability transfer.

Generating Actionable Insights for Improvement: The error analysis identifies knowledge gaps and reasoning challenges, but it doesn't offer concrete solutions. How can we leverage these insights to improve LLM performance on CS tasks? Could you explore targeted fine-tuning on CS-specific datasets, curriculum learning strategies, or methods for incorporating external knowledge sources (e.g., knowledge graphs, symbolic reasoning systems)? Providing concrete examples of how these techniques could be applied would significantly enhance the paper's practical value.

Addressing Benchmark Biases: What are the potential biases introduced by the composition of CS-Bench (e.g., university-level focus, source selection)? How might these biases affect the evaluation of different LLMs? Consider expanding the benchmark to include tasks from different levels of expertise (e.g., introductory CS, advanced topics, real-world applications) and diversifying the sources to mitigate potential biases. Discuss the limitations of CS-Bench in representing the full spectrum of CS knowledge and skills. A critical self-reflection on the benchmark's limitations would strengthen the paper.

Improving Visualization and Clarity: Some figures, particularly the radar charts, are difficult to interpret. Consider using alternative visualizations (e.g., bar charts, scatter plots) that more clearly communicate the key findings. Streamline the writing to improve conciseness and clarity. Focus on conveying the key messages effectively and avoid unnecessary jargon. Ensure that the figures are clearly labeled and explained in the captions. A more polished presentation would enhance the paper's impact and accessibility.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces CS-Bench, the most comprehensive and detailed benchmark for testing computer science knowledge and reasoning that exists to date. It contains over 10,000 items over 26 subfields of computer science, uses 4 different response types (multi choice, assertion, fill-in-the-blank, and open-ended responding), and is presented in 4 languages (English, Chinese, German, French). The authors study over 30 LLMs, including both open- and closed-source models. They provide extensive analysis of performance across the benchmark and its subdomains, and conduct post-hoc studies of how performance scales with model size and the kinds of errors that LLMs make on CS-Bench.

### Strengths
In the already saturated LLM benchmark market, this paper has a number of stand-out strengths. First, it is highly comprehensive. Unlike other benchmarks which seek generality at the cost of precision and depth, CS-Bench focuses on a single domain and contains thousands of in-depth testing items from it. This is an improvement on existing computer science benchmarks like MMLU. Second, it is multilingual. This facilitates, among other things, the generalisability of deeper CS knowledge and reasoning skills when changing the surface level features of the language the system is operating in. This will also allow users to measure the degree of contamination, since (ex hypothesi) a considerable amount of LLM training data will be from English-language sources. Third, the authors include multiple response types, ranging from multiple choice to open ended responding. This facilitates researchers using CS-Bench to probe CS knowledge and reasoning skills with more nuance. Fourth, the results on logarithmic scaling laws is intriguing. Finally, the extensive error analysis is commendable and often not seen in benchmark papers such as this. It demonstrates again that CS Bench can be used to produce a much richer picture of the knowledge and reasoning skills of LLMs in this domain than can be gleaned by simply aggregating task performance.

### Weaknesses
There are a few weaknesses with this paper. First, CS-Bench is static and openly available online. This means that it is possible that LLM developers can train directly on the benchmark, leading to contamination. While we as a community hope that developers wouldn't be so mal-intentioned, it is an increasingly common phenomenon. Dynamic benchmarks (e.g., DynaBench) in which testing items are produced on the fly are able to sidestep such problems.

Second, true tests of computer science skills, particularly for software engineering and development, come from situating models in a coding environment, with access to a terminal. The authors might consider comparing their approach to this more embodied approach to evaluation.

Finally, I am sceptical of the use of GPT-4 for translating the benchmark from Chinese to other languages. While this is certainly scalable, I fear that the translations will be poor, particularly for the most complex questions. The authors' note that some manual checking was done, but I would like to see a more robust measure of translation quality, perhaps through asking a sample of independent native speakers of English, French, and German to check a random sample of questions and answers for soundness.

### Questions
1. What do the authors suggest to avoid the issue of contamination? 
2. Have the authors considered using answer ordering permutation, number switching, orquestion negations to reduce the risk of contamination? By number switching, I mean dynamically changing the numbers in questions so that the answers are different but the fundamental relationships continue to hold. By question negations, I mean asking the opposite question by including a negative particle, such that the question has a different answer.
3. What is the utility of CS-Bench when compared to approaches in which LLMs are situated in an environment with access to a terminal and tasked to solve problems?
4. Can the authors provide further evidence that the interlingual translations using GPT-4 are sound and accurate?

### Soundness
4

### Presentation
3

### Contribution
3
