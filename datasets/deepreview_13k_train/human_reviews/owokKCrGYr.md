# Quality-Diversity through AI Feedback

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
In many text-generation problems, users may prefer not only a single response, but a diverse range of high-quality outputs from which to choose. Quality-diversity (QD) search algorithms aim at such outcomes, by continually improving and diversifying a population of candidates. However, the applicability of QD to qualitative domains, like creative writing, has been limited by the difficulty of algorithmically specifying measures of quality and diversity. Interestingly, recent developments in language models (LMs) have enabled guiding search through \emph{AI feedback}, wherein LMs are prompted in natural language to evaluate qualitative aspects of text. Leveraging this development, we introduce Quality-Diversity through AI Feedback (QDAIF), wherein an evolutionary algorithm applies LMs to both generate variation and evaluate the quality and diversity of candidate text. When assessed on creative writing domains, QDAIF covers more of a specified search space with high-quality samples than do non-QD controls. Further, human evaluation of QDAIF-generated creative texts validates reasonable agreement between AI and human evaluation. Our results thus highlight the potential of AI feedback to guide open-ended search for creative and original solutions, providing a recipe that seemingly generalizes to many domains and modalities. In this way, QDAIF is a step towards AI systems that can independently search, diversify, evaluate, and improve, which are among the core skills underlying human society's capacity for innovation.\footnote[1]{Project Page: \url{https://qdaif.io/}}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces Quality-Diversity through AI Feedback (QDAIF), a novel method that leverages advances in foundation models to evaluate the quality and diversity of generated text in qualitative domains. QDAIF employs an evolutionary algorithm that uses language models to generate variation and evaluate the quality and diversity of candidate text. The results demonstrate that QDAIF covers more of a specified search space with high-quality samples compared to non-QD controls and aligns with human perception of quality and diversity.

### Strengths
1. QDAIF presents a novel approach to discover diverse and high-quality solutions in qualitative domains by leveraging AI feedback, which contributes to the development of AI systems.
2. The paper thoroughly discusses limitations and potential future work, offering some insights for further research in this area.

### Weaknesses
1. QDAIF still requires researchers to define the axes of diversity they are most interested in, which may limit its autonomy in creative search. This reliance on pre-defined axes could lead to a constrained exploration of the solution space, potentially missing out on novel and unexpected forms of diversity that might emerge from a more open-ended search process. The method's effectiveness is thus tied to the researcher's ability to anticipate relevant diversity dimensions, which is not always straightforward, especially in creative domains.
2. Could we have a detailed comparison with other AI feedback methods or discuss how QDAIF specifically addresses their limitations? The paper does not sufficiently contextualize QDAIF within the broader landscape of AI feedback techniques. A more thorough discussion is needed to understand how QDAIF builds upon or diverges from existing methods, and to clarify the specific advantages it offers over alternative approaches. Without this, it is difficult to assess the novelty and impact of QDAIF.
3. The generalizability of QDAIF to other domains and tasks beyond creative writing is not extensively discussed. The current evaluation is heavily focused on creative text generation, and it remains unclear how well the method would perform in other types of qualitative domains, such as music composition, visual art, or even more structured tasks like code generation. The lack of empirical evidence in these areas limits the scope of the paper's claims.

### Questions
1. Can you provide more insight into the scalability and computational efficiency of QDAIF in more complex and large-scale tasks?
2. How does the proposed QDAIF approach perform in other domains and tasks beyond creative writing?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the problem of generate a diverse range of high-quality outputs by using AI feedbacks, instead of traditional Quality-Diversity (QD) search algorithms. The authors propose a Quality-Diversity through AI feedback (QDAF) where an evolutionary algorithm applies LMs to both generate variation and evaluate the quality and diversity of candidate text. Experiments show that produced outputs have a reasonable agreement between AI and human evaluation.

The proposed approach QDAIF builds upon MAP-Elites [Mouret and Clune, 2015], which follows those steps: randomly select a solution, mutate it, evaluate the new solution in terms of quality and diversity. Finally, if the new solution is better, all previous cells are replaced. The improvement of QDAIF is significant and leverage the characteristics of LLMs. Instead of using a uniformly-separated grid, the authors split the grid by density. This makes a lot of sense because we output distributions generated by LLMs are skewed. The initialization and mutation are based on few-shot prompting. Finally, the quality and diversity evaluation is done via prompting the LLMs and observing whether the answer is "yes" or "no" and their log-probabilities.
Overall, the method is a composition of simply ideas that make it easy to follow.

The experiments consists of creative text generation in the domains of opinions and stories. The domain in the former is about eating plant-based diets, and for the latter a short story containing a spy and a politician. Diversity is based on the sentiment towards a topic in case o opinions and genre and ending for the stories. The authors evaluate using QD score [Pugh et al. 2016] and human evaluation. In terms of baseline, they seem to be simple variations of the framework. It would be needed to have baselines cited in prior work. The results are significantly better for QDAIF, but it is unclear whether this is due because the baselines are bad or whether the model is really better. I appreciate the other experiments that the authors have conducted on scaling up the models and trying other mutation methods.

Overall, the paper is well structured and written. The idea is simple but sounds effective. My only concern is the lack of more sophisticated baselines. I would ask the authors to evaluate their proposed approach on another task, such as control text generation (e.g., writing about specific topics and using a classifier to assess the topic being discussed)

POST-REBUTTAL: Thank you for your answers. I will keep my current rating.

### Strengths
- A combination of simple ideas that allow to generate diverse high-quality outputs
- Strong performance in the experiment section
- The paper is well written

### Weaknesses
 - The lack of strong baselines
- More datasets for the experiments would be appreciated

### Questions
Could you add more baselines and tasks?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a pipeline combining a quality-diversity search algorithm and LLM as feedback for quality and diversity, aiming to improve the quality-diversity in the creativity domain, such as creative writing. The authors also conduct human evaluations to evaluate the output of the pipeline.

### Strengths
Strength: 
* The paper addresses an interesting problem in the creativity domain, namely, generating solutions that are both diverse and of high quality. The integration of AI feedback and the existing QD algorithm seems to be novel and interesting

### Weaknesses
Weakness
* One key motivation of the paper using AI feedback seems to bypass the necessity to articulate a set of criteria. However, the prompt strategies still resort to specified diversity and quality criteria
* The evaluation result seems to be a bit confusing; for example, in Table 1, one of the methods is LMX, Fitness-only, then in section 4.3 when it explains the method, there is LMX Quality-only. Is that the same method as LMX, fitness-only
* It would be interesting to see ablation analysis to compare with the QD with and without AI feedback (not sure if LMX fitness-only or quality only serves the baseline) 
* QD metric is used throughout, which is the “sum of highest quality value found in each bin” - it seems to only focus on quality rather than diversity. For readers not familiar with QD metrics, some explanation/justification of why QD measures Quality and Diversity will be helpful

### Questions
Table 1:  there is a lack of explanation of the quality metrics. For example, what is the difference between human QD score and quality rating? Is quality rating from humans? 

* On page 5, section quantifying performance and diversity, it is unclear where the probability comes from in the sentence “ the solutions’ quality estimate is derived from the logarithm of the probability of the LM’s answer” …  Please clarify

* Figure 3 illustrates the differential performance of various methods on different generation tasks. Is there any qualitative difference in terms of the QD score difference of less than one point

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces an novel approach that integrates AI-generated (LMs) feedback into quality-diversity search algorithms, aiming to enhance the capability of AI systems in independent searching, evaluating, and innovation.

### Strengths
1. The authors have proposed a novel and effective quality-diversity algorithm that leverages the latest developments in AI feedback, demonstrating superior performance compared to existing alternatives.
2. The paper features a comprehensive set of experiments focused on creative writing, supported by a thorough analysis of the results, showcasing the practical applicability of the proposed method.

### Weaknesses
1. The presentation, particularly in the experimental section, could benefit from clarification and better organization to enhance readability and comprehension.  
2. The paper occasionally employs exaggerated language and makes promising claims that seem to lack sufficient empirical backing. For example, the paper states “providing a recipe that seemingly generalizes to many domains and modalities” and “it is often easier for a model to evaluate the quality of a generation than to generate the same high-quality text.” These claims would be more convincing if supported by concrete evidence or reference or discussion.

### Questions
A separate conclusion section, summarizing the key findings and contributions, would be advantageous for providing clear takeaways for the readers.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
