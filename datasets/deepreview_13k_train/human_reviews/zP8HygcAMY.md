# Can LLMs Evaluate Complex Attribution in QA? Automatic Benchmarking Using Knowledge Graphs

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
The attribution of question answering (QA), which is to get evidences for supporting the generated answer, has attracted wide research attention. The current methods for automatically evaluating the attribution, typically relying on Large Language Models (LLMs), are still inadequate, particularly in recognizing subtle differences between attributions, and in measuring complex attribution reasoning. Existing benchmarks, which are primarily based on manual annotations, suffer from limited evaluation settings with incomplete and coarse attribution categories and reasoning scenarios, hindering the evaluation and advancement of attribution evaluators. To address this gap, we introduce Complex Attributed Question Answering (CAQA), a large-scale benchmark automatically generated using Knowledge Graphs (KGs), containing more comprehensive attribution categories and complex attribution reasoning scenarios. Our experiments with two specifically developed evaluators and nine LLM evaluators reveal that they struggle in identifying negative attribution categories and handling complex attribution reasoning in both zero-shot and few-shot settings, but mostly perform relatively well in the fine-tuning setting. Moreover, all evaluators perform inadequately in fine-grained attribution identification scenarios. The experiments also demonstrate that CAQA is consistent with human annotations, and is promising for selecting and developing more effective attribution evaluators in QA.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents CAQA (Complex Attributed Question Answering), a large-scale automatically generated benchmark designed to assess the attribution capabilities of QA systems, particularly Large Language Models (LLMs). CAQA leverages Knowledge Graphs (KGs) to create comprehensive attribution categories and to handle complex reasoning scenarios. The benchmark distinguishes between supportive, partially supportive, contradictory, and irrelevant evidence types and introduces reasoning complexity through different forms of evidence combination (e.g., union, intersection, concatenation).

### Strengths
- CAQA uses KGs to generate complex QA benchmarks automatically, enabling scalability and minimizing manual annotation effort.
- Different reasoning complexities are considered, highlighting LLMs' capabilities in handling logical relationships between facts.
- The benchmark includes fine-grained attribution categories.

### Weaknesses
 - The task setting seems very similar to NLI to me, more discussions are needed.
- Lack of a few details about the human annotation process.
- The distribution of the complexity is biased.

### Questions
- How do you verify the quality of converted natural language style questions?
- What is the inter-agreement score of human annotations?

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
4

### Summary
This paper introduces Complex Attributed Question Answering (CAQA), a large-scale benchmark designed to evaluate complex attributions in question answering (QA). CAQA is automatically generated using knowledge graphs (KGs), includes a broader range of attribution categories along with intricate attribution reasoning scenarios, and is also aligned with human annotations. Experiments with two specifically developed evaluators and nine large language model (LLM) evaluators reveal that these models struggle to identify negative attribution categories and handle complex attribution reasoning in both zero-shot and few-shot settings but mostly perform relatively well in the fine-tuning setting.

### Strengths
1. This paper introduces CAQA, a large-scale benchmark for evaluating complex attributions in QA.
2. The CAQA dataset contains various new definitions (e.g., fine-grained attribute categories and attribution complexities), and the data construction process is automatic, considerate, and comprehensive.
3. This paper contains comprehensive experiments. In addition to model performance on CAQA, it also includes fine-grained analysis, human consistency, and out-of-distribution data.

### Weaknesses
1. This paper only considers GPT-3.5 and GPT-4 as closed-source LLMs, and some open-source LLMs used may be outdated (e.g., Mistral-7B has revolutionized various versions). Adding more diverse and latest models in experiments would have greater contributions and help to discover which LLMs perform best on this challenging task.
2. There is a lack of comparisons with human performance on (a subset) of the dataset, which would better illustrate the performance gap and the challenge of the dataset.
3. While the contribution of the paper centers on a new challenging benchmark, it would be much helpful if the authors can provide an error analysis, which will direct newcomers in future research.

### Questions
See "Weaknesses".

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces the dataset Complex Attributed Question Answering (CAQA), containing answers to questions with associated source attributions, where the attributions may or may not support the answer. The non-support attributions are divided into 3 labeled categories: Partially supported, Contradictory Irrelevant.

They evaluate how well different LLMs can classify Q+A+source into these 4 categories, finding that in many cases they struggle to do well, especially on distinguishing the non-supportive categories.

The CAQA dataset is constructed from existing KGQA datasets (GrailQA and WebQuestionsSP), making use of the associated knowledge graph to produce different types of non-supportive evidence (and using GPT-3.5 to turn KG triples into natural language sentences). The resulting dataset is quite big (137k train, 24k test), allowing for fine-tuning experiments as well. The fine-tuned models do very well in distribution, and they also do limited out-of-distribution evaluation on a subset of ALCE further annotated with these non-supportive categories, showing promising results there as well.

### Strengths
The dataset is relevant for the important topic of answers with attributions from LLMs. Being able to carefully validate whether an answer actually follows from the sources is an important skill, and this dataset aims at helping with this.

The paper is well written, clearly describing the approach.

The use of the KG to create various incorrect attributions, together with using LLM to rewrite at text, seems quite effective.

The paper provides access to the full dataset for exploration which is truly helpful in assessing it.

The methods are tested on a more realistic, OOD, dataset.

### Weaknesses
While breaking down the non-supportive cases into three subcategories can be helpful for understanding limitations, the boundary between them can be quite unclear. Also the prompt for the non-GPT models doesn't go into great detail (beyond some examples) on what each category means. For instance, the "contradictory" evidence is often for actual true facts, so they're not actually contradiction, it's just the "wrong" evidence.

E.g., the answer "The person who founded the United States Coast Guard also founded the United States Department of the Treasury." is presented as being contradicted by the source "Alexander Hamilton is the founder of the United States Coast Guard and the Montgomery County Sheriff's Office, which is a government agency.", but this isn't really a contradiction, it's more like missing evidence. A true contradiction should lead you to think the answer is actually false, if you trust the source.

The "Partial support" category also can be quite subjective, as in the case of "The 2011 Estoril Open tournament event competition is the Men's Singles." being partially supported by "The 2011 Estoril Open had a men's singles competition."  (what's missing is apparently that "2011 Estoril Open" was "tournament event competition", but that's pretty much implied by the fact that they had a men's single compeition).

Because of this, it might also be useful to report the most important "supported" vs "not supported" scores.

Another concern is the simplicity of the dataset, with simple QA assertions attributed by short source sentences. How does good performance on CAQA transfer to more realistic settings. And can it be used to train better source attribution models as well? There is some exploration of this with the OOD ALCE dataset, but the effect (e.g., between Vicuna-13B and Vicuna-13B-finetuned) isn't as impactful as one might have hoped.

### Questions
Some discussion on the ambiguity (and actual errors) in the labeled categories would be useful (e.g., human annotator agreements on a sample). 

Also would be good to discuss the lack of context consideration which is usually very important in real usage (e.g., the example in the paper "Who plays Fruma Sarah in Fiddler on the Roof" depends on which version of Fiddler on the Roof is being referenced).

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
This manuscript aims to bridge the gap in attribution evaluators' use of knowledge graphs by providing detailed categories. This study's experiment offers multiple configurations in zero-shot, few-shot, and fine-tuned contexts, demonstrating that the fine-tuning process can significantly improve performance. This benchmark aims to address the shortcomings of existing attribution evaluators, which face challenges with intricate attribution categories and sophisticated reasoning processes.

### Strengths
The use of KGs for automatic construction of the benchmark is novel, making the process scalable and adaptable.
The research tests various models and demonstrates the needs of fine-tuning for achieving robust performance.
The benchmark shows high consistency with human evaluations, supporting its credibility as an effective tool for future developments in QA systems.
The choice to test multiple LLMs, including state-of-the-art models like GPT-4 and LLaMA variants, provides a robust analysis of performance across different model scales and settings.
The inclusion of a wide range of attribution types and complexity levels sets a high standard for evaluating QA systems.

### Weaknesses
 The benchmark is tailored for KG-based QA tasks, which may not reflect the challenges present in more diverse, open-domain QA systems. 
The reliance on GPT models for generating natural language representations from KGs may introduce subtle biases.
The rationale behind choosing specific complexity types (e.g., concatenation, intersection) could be expanded with examples illustrating real-world implications of these complexities in QA.

### Questions
1. How might CAQA be adapted to handle dynamic or temporal data in QA tasks?
2, What specific types of biases were identified or considered when using LLM-generated prompts?
3. Are there plans to include more diverse logical operations, such as negation, in future iterations of CAQA?
4. Could the inclusion of human-in-the-loop evaluations further enhance the quality of the generated benchmark data?
5, Extend the benchmark's applicability by including examples from various knowledge domains (e.g., medical, legal) to test the robustness of attributions in specialized contexts.
6. The reliance on GPT models for generating natural language representations from KGs may introduce subtle biases. Addressing how these biases are minimized or discussing potential implications would strengthen the manuscript.
7. Discussing how CAQA could be adapted for such tasks would add value especially how to address the challenges in more diverse, such as open-domain QA systems. .

### Soundness
3

### Presentation
3

### Contribution
3
