# DarkBench: Benchmarking Dark Patterns in Large Language Models

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
We introduce DarkBench, a comprehensive benchmark for detecting dark design patterns—manipulative techniques that influence user behavior—in interactions with large language models (LLMs). Our benchmark comprises 660 prompts across six categories: brand bias, user retention, sycophancy, anthropomorphism, harmful generation, and sneaking. We evaluate models from five leading companies (OpenAI, Anthropic, Meta, Mistral, Google) and find that some LLMs are explicitly designed to favor their developers' products and exhibit untruthful communication, among other manipulative behaviors. Companies developing LLMs should recognize and mitigate the impact of dark design patterns to promote more ethical Al.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors define six dimensions of 'dark design patterns' and develop the DarkBench benchmark to detect these patterns in LLMs. They test 14 LLMs, encompassing both proprietary and open models, to compare dark pattern prevalence across different systems.

### Strengths
- The paper tackles the crucial issue of dark patterns in LLMs. As far as I know, no prior research has defined and measured dark patterns in LLMs, making this a novel and much-needed contribution.

- Extensive comparison of 14 proprietary and open-source models on the DarkBench benchmark

### Weaknesses
 - The authors use LLMs to annotate dark patterns. However, LLMs’ own dark patterns may affect their ability to annotate dark patterns. For instance, if an LLM displays brand bias, it may evaluate responses from its own brand more favorably. A simple statistical test for potential biases in annotation could address this (e.g., comparing whether an LLM's scores for its own responses differ significantly from those it assigns to other LLM responses)

- The paper lacks detailed information on human annotations, particularly regarding the annotators' demographics or level of expertise. For instance, it would be helpful to clarify whether LimeSurvey annotators were laypeople or experts and whether they reflect a diverse demographic range (age, gender, etc.) similar to typical LLM users.

- There is no evidence of stability for the benchmark findings across variations in prompt designs. You could test for consistency by paraphrasing prompts in Table 1 and replicate the experiments.

- Overall, the paper lacks detail. The results section would benefit from including actual qualitative examples from the models.

- I do not understand 13p line 685. ``Despite a low Krippendorff’s Kappa, indicating poor inter-rater agreement, the summary statistics over models and dark patterns remain consistent.'' Please specify the exact Krippendorff’s Kappa score obtained and the threshold used for ``poor agreement''. Additionally, how do you justify that consistent summary statistics validate the use of these annotator models?

- I am concerned whether reducing dark pattern defined by the authors could unintentionally drop the performance in some popular use cases of LLMs. For instance, social scientists use LLMs to simulate human samples for scientific purposes, using LLMs to generate human-like samples when generating hypotheses or collecting human data is expensive (see Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023). Out of one, many: Using language models to simulate human samples. Political Analysis, 31(3), 337-351. or Törnberg, P., Valeeva, D., Uitermark, J., & Bail, C. (2023). Simulating social media using large language models to evaluate alternative news feed algorithms. arXiv preprint arXiv:2310.05984.). I'm concerned if reducing Anthropomorphization could affect the abilities of LLMs to accurately simulate human agents for scientific purposes.

### Questions
- I do not understand 13p line 685. ``Despite a low Krippendorff’s Kappa, indicating poor inter-rater agreement, the summary statistics over models and dark patterns remain consistent.'' Please specify the exact Krippendorff’s Kappa score obtained and the threshold used for ``poor agreement''. Additionally, how do you justify that consistent summary statistics validate the use of these annotator models?

- I am concerned whether reducing dark pattern defined by the authors could unintentionally drop the performance in some popular use cases of LLMs. For instance, social scientists use LLMs to simulate human samples for scientific purposes, using LLMs to generate human-like samples when generating hypotheses or collecting human data is expensive (see Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023). Out of one, many: Using language models to simulate human samples. Political Analysis, 31(3), 337-351. or Törnberg, P., Valeeva, D., Uitermark, J., & Bail, C. (2023). Simulating social media using large language models to evaluate alternative news feed algorithms. arXiv preprint arXiv:2310.05984.). I'm concerned if reducing Anthropomorphization could affect the abilities of LLMs to accurately simulate human agents for scientific purposes.

### Soundness
3

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
4

### Summary
Authors describe a benchmark for dark patterns: brand bias, user retention, anthropomorphization, sneaking, sycophancy and harmful generation. They created prompts designed to elicit the dark patterns. Then they used few-shot prompting to generate a total of 660 adversarial prompts. Using a mixture of human annotation and model annotation (Claude Sonnet, Gemini Pro, GPT-4o, and Llama3 70b) they tested 14 open and closed lmms. They found that 48% of the cases exhibited dark patterns, with the most common being user retention and sneaking. Dark patterns presence ranged from 30% to 61% across all models.

### Strengths
The paper is well-written and well-organized. The paper is a significant contribution as it presents a new benchmark for measuring dark patterns in LLMs. This is an important direction to help evaluate model safety.
In addition to LLM annotators, data were also reviewed by human annotators.

### Weaknesses
Unfortunately, the methods aren’t clear on the decision criteria, what makes a model’s performance count? Ought it be a simple proportion? Or something more akin to recall and precision might be more informative and valid for interpretation. Moreover, the authors did not report on group differences which would strengthen their conclusions. The lack of clarity on how models are classified as exhibiting a dark pattern, and the absence of statistical significance testing, further weakens the analysis. The paper also lacks a detailed discussion of inter-annotator agreement, which is crucial for validating the annotation process. The reported Krippendorff’s Kappa score is concerning, and the implications of this low agreement on the reliability of the results should be addressed more thoroughly.

### Questions
p. 5 243 “Our results can be found in Figure 4. We see that on average, dark pattern instances are detected in 48% of all cases”
-> What is the cutoff? How are models classified as exhibiting a dark pattern or not? Are the differences significant?

P.13 “In Figure 5, the annotations by annotation models other than Claude 3 Opus are displayed. The general trends of the annotations are similar. Despite a low Krippendorff’s Kappa, indicating poor inter-rater agreement, the summary statistics over models and dark patterns remain consistent” 
-> This should be part of the limitations and the results. What are the scores within/between models and humans?

### Soundness
2

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
The paper introduces DarkBench a set of prompts designed to elicit "dark patterns" in LLM responses. The authors describe how the benchmark was developed, how the benchmark is evaluated against a model, and presents benchmark results for a variety of open and proprietary models. 

Overall this is an interesting piece of work, the various patterns are relevant and the problem is well motivated. 

I would like to see more formality w.r.t your description of the data generation and evaluation processes i.e. 

1. It was unclear to me if humans reviewed all of the 600 DarkBench prompts for quality? You mentioned rephrasing occurred, why was this and what kind of rephrasing was necessary? 
2. When applying the benchmark to an LLM, what parameters were used? Did the LLM produce a set of responses via sampling, or did the LLM generate one response? Did the annotator models correlate with one another? How was the final yes/no answer generated? Was positional bias accounted for?
3. The results of the human reviews on the annotator model outcomes?

I would appreciate a discussion around system prompts. In the context of system prompts, used to adjust LLM behavior, how is the DarkBench to be interpreted? I could see it being a tool. 

Nice idea, good selection of patterns. I think the paper would be improved if the methodology was described in more detail as per the points above.

### Strengths
Nice idea 
The selection of patterns is relevant
Valuable asset (DarkBench dataset)

### Weaknesses
The description of the methodology is a little vague.
The paper would be stronger if the methodology was more detailed.

### Questions
1. It was unclear to me if humans reviewed all of the 600 DarkBench prompts for quality? You mentioned rephrasing occurred, why was this and what kind of rephrasing was necessary? 
2. When applying the benchmark to an LLM, what parameters were used? Did the LLM produce a set of responses via sampling, or did the LLM generate one response? Did the annotator models correlate with one another? How was the final yes/no answer generated with the annotator models? Was positional bias accounted for?
3. The results of the human reviews on the annotator model outcomes?

### Soundness
3

### Presentation
2

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
The authors develop DarkBench by manually conceptualizing six tendencies of LLMs that seem to align with the chatbot subscription-based business model (e.g., ChatGPT, Claude.ai), prompting an LLM with precise verbal descriptions of those tendencies to create adversarial prompts that would evoke dark patterns, and manually reviewing and modifying the LLM-generated prompts. Evaluation was done with LLMs prompted with human examples with samples of that LLM evaluation also done by humans for comparison. Results show that Claude performs best on this benchmark ("dark patterns" in 30-36% of responses, if I understand correctly), followed by the other models in a band of 48-61%. Some patterns (e.g., user retention) are much more frequent than others (e.g., sycophancy) in current LLMs.

### Strengths
- **S1.** I'm excited about this project's direction in evaluating LLM behavior based on design patterns found to be important in other interfaces (dark patterns, but also nudges, antipatterns, and so on). This is difficult, and I am sympathetic to work addressing it even if that work has many limitations.
- **S2.** I appreciate that some human review and validation was done for the LLM-generated benchmark and for the LLM-generated evaluations, and I think these general directions for datasets and benchmarks are promising in their scalability.
- **S3.** The figures are relatively clear and concise.

### Weaknesses
My primary concerns each refer to the benchmark development and evaluation seeming largely superficial, better suited to preliminary and exploratory formats, such as workshops or seminars, than a main conference publication. To be upfront and help the authors manage their time, I don't think W1 can realistically be addressed during review, and addressing only W2 and W3 would be insufficient for me to raise my score to acceptance.

**W1. Theoretical engagement.**

I'm skeptical that these six tendencies qualify as "dark patterns." Dark patterns are a specific idea regarding intentional design of user flow to trick the user into situations harmful to them and beneficial to the designer's institution (https://90percentofeverything.com/2010/07/08/dark-patterns-dirty-tricks-designers-use-to-make-people-do-stuff/index.html). It seems the authors are familiar with canonical examples, such as making it difficult to unsubscribe from a service, but I don't think the authors have successfully argued for any of their six tendencies being constitutive of, or even highly correlated with, this specific idea.

I would put the misalignments into three categories: (i) not being specific to dark patterns but just harmful generation more broadly ("harmful generation" and "sycophancy" are the main culprits), (ii) not necessarily being harmful, such as the model being "friendly" or "anthropomorphic," which can be in fact some of the main benefits of LLMs, such as for mental health (https://dl.acm.org/doi/full/10.1145/3485874), and (iii) being incidental, such as "brand bias" merely from preference tuning and system prompts that center the brand. I would not say Google has a dark pattern if the search engine highly ranks Google content.

I realize that it is impossible to have six metrics that uncontroversially fit into a subjective idea such as dark patterns, and it is nonetheless urgent that we build evaluations like this, but the current state of the paper is just too far off the mark.

**W2. LLM generation and validation.**

My concerns here may be due to the cursory explanation provided by the authors, but I'm missing a lot of necessary details about generation process and test validation. I would want to see, for example, the extent of mode collapse in the generations, comparisons across generations from different models, and ideally a more rigorous structure with subcategories within the six categories (a priori or through clustering). I think LLM-generated evaluations are promising, but as with any paradigm shift in scientific methodology (e.g., agent-based models, psychologists shifting from studying undergraduate students to online participants), the burden of validation will be high before it is more thoroughly vetted. It seems the authors are familiar with the explosion of literature on such methods, so there are many examples to draw from.

**W3. LLM evaluations.**

This is largely analogous to W2. I don't expect the authors to validate that LLM-as-a-judge aligns perfectly with human judgment, but only brief description such as "poor inter-rater agreement" is not sufficient to me that the LLM judges are performing well enough to trust this benchmark. It is also unclear to me how the different model judges (e.g., Claude versus Llama) were compared and aggregated, which is particularly concerning in a paper that (a) is focused on inevitably subjective distinctions between qualitative model output and (b) has a main empirical finding (or at least secondary) of differences between model brands/families. For example, it is well-known that Claude is heavily tuned to be "friendly" in various ways, such as modifying its behavior when nudged at all by the user. Some people like this. Some prefer ChatGPT as straightforward with less of that noise. But my point is that the benchmark may be merely picking up on tendencies like that, which would not only lack novelty as a finding but also be of little relevance to dark patterns.

**Minor concerns**

- The term "dark pattern" was not coined in the creation of darkpatterns.org but a talk Harry Brignull gave at UX Brighton in 2010, or technically shortly before that in this blog post (https://90percentofeverything.com/2010/07/08/dark-patterns-dirty-tricks-designers-use-to-make-people-do-stuff/index.html). It continues to be a focus of design research, which would be good to engage with in addition to popular media references to the concept.
- The presentation of the paper seems rushed, including numerous typos and some structural choices that may need correction or at least clarification (e.g., the ordering of models in Figure 4, which does not seem to be "by least to highest frequency of dark patterns" as stated).
- Where is the stated "Appendix 5"? Presumably this is related to the "Annotations on the dataset" section, but perhaps the authors meant to include more information in the appendix that would address some of my other concerns.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3
