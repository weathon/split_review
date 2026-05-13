# TrustSQL: Benchmarking Text-to-SQL Reliability with Penalty-Based Scoring

- Decision: Reject
- Scores: 5, 5, 5, 1

## Abstract
Text-to-SQL enables users to interact with databases using natural language, simplifying the retrieval and synthesis of information.
Despite the remarkable success of large language models (LLMs) in translating natural language questions into SQL queries, widespread deployment remains limited due to two primary challenges.
First, the effective use of text-to-SQL models depends on users' understanding of the model's capabilities—the scope of questions the model can correctly answer.
Second, the absence of abstention mechanisms can lead to incorrect SQL generation going unnoticed, thereby undermining trust in the model's output.
To enable wider deployment, it is crucial to address these challenges in model design and enhance model evaluation to build trust in the model's output.
To this end, we introduce \textit{TrustSQL}, a novel comprehensive benchmark designed to evaluate ~\textit{text-to-SQL reliability}—defined as a model's ability to correctly handle any type of input question by generating correct SQL queries for feasible questions and abstaining from generating infeasible ones (\textit{e.g.}, due to schema incompatibility or functionalities beyond SQL).
We evaluate existing methods using a novel penalty-based scoring metric with two modeling approaches: (1) pipeline-based methods combining SQL generators with infeasible question detectors and SQL error detectors for abstention; and (2) unified methods using a single model for the entire task.
Our experimental results reveal that achieving high scores under severe penalties requires significant effort and provide a new perspective on developing text-to-SQL models for safer deployment.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces TrustSQL, a benchmark designed to assess the reliability of text-to-SQL systems in handling both feasible and infeasible questions. To build the TrustSQL dataset, the authors re-annotated three existing datasets: ATIS, Advising, and EHRSQL. TrustSQL’s evaluation metric considers both question types, incorporating a novel metric, the Reliability Score. With this metric, correctly answering feasible questions and identifying infeasible questions yield a positive score of 1, while other responses result in a score of 0 or a negative penalty of -C.

The paper evaluates both classifier-based methods, which use a sub-model classifier to distinguish feasible and infeasible questions, and uncertainty-estimation-based methods, which rely on SQL generation uncertainty.

### Strengths
1. The paper introduces the TrustSQL dataset, aimed at evaluating text-to-SQL systems on both feasible and infeasible questions. The re-annotated datasets could serve as a valuable resource for the text-to-SQL community. 

2. The paper evaluates multiple text-to-SQL systems, including the SOTA fine-tuned text-to-SQL model (SQLCoder) and a general-purpose LLM (GPT-4), using both classifier-based and uncertainty-estimation approaches for detecting infeasible questions.

### Weaknesses
1. Re-annotation is a central component of the paper and should be included in the main content rather than the appendix, especially given that one page of space remains available. 

2. The authors find that many text-to-SQL models can produce responses that are potentially more harmful than helpful, but this observation depends on the choice of weight C in the penalty. The choices for C (set at 1, N/2, and N) seem arbitrary. The paper lacks a discussion on the rationale behind these values and whether any human studies informed this choice.

### Questions
1. Lines 200–201 mention that all questions were reviewed to ensure clarity, with adjustments made for SQL queries that were too similar. How was clarity ensured during annotation, and what metric was used to determine if a question was clear or if two SQL queries were overly similar?

2. Who are the annotators, and how are disagreements in annotation resolved?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces TrustSQL, a new benchmark designed to evaluate the reliability of text-to-SQL models. It addresses two significant gaps in existing benchmarks: the lack of infeasible questions that cannot be mapped to SQL queries and the absence of abstention mechanisms in current models. TrustSQL is constructed by re-annotating three datasets—ATIS, Advising, and EHRSQL—and incorporating infeasible questions to provide a comprehensive evaluation. The authors propose a novel metric called the Reliability Score (RS), which quantifies a model's helpfulness relative to its harmfulness, adjusted by a user-defined penalty. They evaluate text-to-SQL models integrated with various abstention mechanisms, such as classifiers and uncertainty estimation methods. The experiments reveal that most models fail to meet safety requirements under high penalty settings, underscoring the need for developing models that ensure a certain degree of reliability alongside SQL generation accuracy.

### Strengths
The paper makes a significant contribution by introducing TrustSQL, a benchmark that fills a critical gap in the evaluation of text-to-SQL models. By incorporating infeasible questions and proposing the Reliability Score (RS), the authors provide a fresh perspective on assessing model reliability, which is crucial for real-world deployment.
The authors conduct thorough experiments using both fine-tuning and in-context learning settings, integrating various abstention mechanisms. The meticulous re-annotation of existing datasets and the careful construction of infeasible questions enhance the quality and relevance of the benchmark. The paper's focus on reliability and safety has the potential to influence future research and practices in the field.

### Weaknesses
The paper evaluates several abstention mechanisms but could provide deeper insights into why certain methods perform better under specific conditions. A more thorough analysis of the trade-offs between coverage and risk for each mechanism would be beneficial.
The Reliability Score depends heavily on the user-defined penalty parameter. The paper does not offer sufficient guidance on how practitioners should choose this parameter in practice. A sensitivity analysis or guidelines would make the RS metric more practical.

### Questions
Can you provide practical advice or criteria for selecting the penalty parameter 'c' in the Reliability Score? 
How sensitive is the RS to different values of 'c'? 
Have you considered that frequent abstentions might affect user experience?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces TrustSQL, a benchmark aiming to evaluate the reliability of text-to-SQL models in handling both feasible and infeasible natural language questions. The authors identify limitations in existing benchmarks, specifically the lack of infeasible questions and abstention mechanisms in models, which can lead to incorrect or harmful responses. They propose the Reliability Score (RS) metric to quantify a model's helpfulness relative to its potential harmfulness, assigning positive scores for correct decisions and penalizing incorrect ones based on a user-defined penalty. The authors re-annotate three domain-specific datasets—ATIS, Advising, and EHRSQL—to include infeasible questions categorized into missing schema, ambiguous, and non-SQL types. Various text-to-SQL models integrated with abstention mechanisms are evaluated using this benchmark.

### Strengths
1. The introduction of TrustSQL fills a critical gap in the evaluation of text-to-SQL models by incorporating infeasible questions.
2. The Reliability Score metric provides a meaningful way to quantify the trade-off between a model's helpfulness and harmfulness.
3. The paper provides an evaluation of different abstention mechanisms and their effects on model reliability.

### Weaknesses
1. Insufficient Comparison with Existing Work: The paper lacks a thorough and clear comparison with existing works that address similar challenges in handling infeasible questions in text-to-SQL tasks. Prior studies, such as TriageSQL and more recent research on hallucination problems in LLMs, have explored methods for detecting and managing unanswerable or infeasible queries. The paper does not adequately position its contributions within the context of these existing approaches. Moreover, it does not provide empirical comparisons with previous benchmarks and methods dealing with infeasible questions.
2. Lack of Quality Analysis for the Proposed Dataset: The paper does not provide quality metrics or detailed analyses to demonstrate the high quality of the re-annotated datasets and the newly added infeasible questions. Quality metrics such as inter-annotator agreement, dataset statistics, or validation processes are essential to establish the reliability and usefulness of the proposed benchmark. The author could also consider adding a user study or real-world deployment to validate whether the proposed RS metric aligns with actual user satisfaction or trust in the models.
3. Limited Evaluation Scope and Generalizability Concerns: The evaluation is limited to three simple domain-specific datasets, which may restrict the generalizability to other domains or more complex schemas found in cross-domain datasets like Spider and BIRD.

### Questions
1. The proposed classification of infeasible questions into missing-schema, ambiguous, and non-SQL categories may not be exhaustive. Are there other types of infeasible or unanswerable questions that the classification does not cover, such as questions based on inaccurate premises, malformed queries, or those that require external knowledge beyond the database schema? How would these additional categories impact model performance and evaluation? It would be helpful if the authors could discuss the potential for other classes of infeasible questions and how their benchmark could accommodate them.
2. Regarding the penalty c, is the selection and sensitivity of the c value thoroughly explored? Why choose 1, 0.5N, and N? Could the authors elaborate on how it was determined? Are there recommended strategies or guidelines for practitioners to select appropriate values in different application contexts?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper introduces TrustSQL, a new benchmark for evaluating text-to-SQL model reliability. Current benchmarks overlook real-world scenarios with unanswerable questions, and existing models miss abstention mechanisms. TrustSQL addresses these issues by including both answerable and unanswerable questions, introducing a new scoring system rewarding correct answers and abstentions while penalizing errors. To faciliate evaluation, authors re-annotated three datasets and added infeasible questions to formalize a comprehensive benchmark. Experiments and related analysis reveal potential issues of current text-to-SQL systems when facing such safety requirements.

### Strengths
1) This paper proposes an important research problem of infeasible questions in the text-to-SQL domain.
2) Authors introduce a novel evaluation metric to assess model reliability regarding the potential harm of infeasible questions.
3) The work incorporates these features by re-annotating three existing datasets.
4) Experiments demonstrate the impact of abstention mechanisms and the Reliability Score in evaluating text-to-SQL model reliability.

### Weaknesses
### Unclear Dataset Construction:
1) The paper re-annotates three existing datasets (ATIS, Advising, and EHRSQL), which are limited. The generalizability of the findings across other domains or more diverse database schemas is uncertain. In contrast, benchmarks like SPIDER and BIRD include test sets with broader domain coverage (e.g., > 10 domains), making the generalizability of the dataset in this paper more limited in comparison.

2) The creation of "infeasible questions" appears to rely on manual annotation, potentially introducing bias or inconsistency. However, the authors do not provide **detailed guidelines** on the generation process for these infeasible questions. Appendix D only offers a high-level overview of data re-annotation without elaborating on **specific types** of infeasible questions or **how these types were defined and re-annotated**. Discussing measures taken to ensure consistency across annotators and mitigate potential biases in the manual annotation process would be more helpful. Additionally, while the authors criticize related work (e.g., EHR-SQL [2]) for using a **template-based** method to generate infeasible questions, their approach similarly employs **templates** (as suggested in Lines 1362–1363). This raises the question of how their method fundamentally differs from EHR-SQL. Furthermore, **no comparison** of data distributions between the authors’ dataset and related work, such as [1] and [2], is provided. Both of these works offer clear, detailed taxonomies of ambiguous with distributions or unanswerable (infeasible) question types, which is missed in this paper. The single table provided (Table 1) and Section 4.2 are quite insufficient; more detailed charts or a comprehensive taxonomy are necessary, especially since this is a central problem the paper aims to address. Also authors just state which papers that they follow to define for each category without discussing motivations of each, and it also seems the contribution of this work is incremental and limited.

3) When constructing benchmarks, it is essential to clearly describe the process of crowdsourcing. The paper should detail how many annotators were involved, what their expertise levels were, how the recruitment process worked, and what methods were used for data evaluation. Were expert panels involved? What were the criteria for evaluating the quality of annotations, and how was the workflow structured? Additionally, without information on compensations or incentives for crowdsourcing, it is difficult to evaluate the overall quality and reliability of the benchmark. These crucial details are missing, making it harder for readers to trust the quality and fairness of the dataset.

4) The paper does not adequately differentiate its contributions from similar works. Both [1] and [2] have already addressed infeasible questions (often referred to as ambiguous or unanswerable questions). The distinction in this work between their approach and previous works is only briefly mentioned, and a single sentence in the Related Work section does not sufficiently clarify the novelty or improvements conveyed by this work. For example, the statement "do not account for SQL generation errors" (Line 110) is vague without examples or tables. It is unclear why SQL generation errors are a critical focus. Do the authors envision text-to-SQL systems returning SQL queries with an explicit “unreliable” label to users? If so, why not fix the errors if they are detectable? Also as examples showing in Figure 1, "reliable" Text-to-SQL systems return an empty response by abstention. In this case, [1], an encoder-based classifier, can also achieve this by translating it from negative labels.

Similarly, the authors argue that template-based methods reduce diversity (as stated in Appendix D), but they also implement templates to structure data, followed by paraphrasing (as in [3]). The lack of a **diversity comparison** between their work and [2] weakens their claim that their methods result in more diverse infeasible question types.  The diversity the authors refer to in Appendix D seems to pertain to linguistic variation, not the diversity of categories of infeasible questions, which considered not quite important. Did this modification lead to some strong contributions of reliability of text-to-SQL systems?  Without experimental proof, it is hard to assert that template-based data generation inherently leads to less diversity. Furthermore, I also think the contribtion is quite limited if the diversity just refers to linguistic difference since [3] proposes much more formats of diversity including lingusitc modification and [1][2] already mention this problem. Also, following [3], please present and append your main types of templates

Given the availability of SPIDER and BIRD, which contain more domains and template-free data annotations, it remains unclear why the authors chose not to leverage these existing resources. These datasets naturally include ambiguous questions, as demonstrated in [4] and [5]. Why not explore them on such existing datasets, but spend more resources in re-annotation?

5) Question Familarity definition and detection is not clear and stable. As we know the same question may have multiple forms of gt SQLs. Clustering by GT SQLs from dataset may not be objective. For example, `highest score` can refer to SQLs with `max()` or `order by limit 1`, would your algorithm consider SQLs with such two keywords as infamiliar questions? This definition is questionable and not intuitive. The same with Question Difficulty in which authors mistakenly assume each question has the only one GT SQL. For example, they consider questions with no JOINs but no nesting in GT SQLs as `Medium`. How about its GT SQL is sub-queried such as `SELECT ... In (SELECT ...)`. It doesn't contain `JOIN` but nesting, what category should belong to? However, it could also be generated as a single `Join`, which should be considered as `Easy`. As pointed in Appendix A in BIRD, the only SQL difficutly cannot represent all difficulties of text-to-SQL tasks. The NL and environment with different complexity of DB schema and constrains should also be considered since it represent "text-to". In a short, I think the whole definitions in the second paragraph of Section 4.3 are not rigorous leading to unfair evaluation setting and distributions especially given authors didn't present a clear distribution and statitic analysis of their benchmark.

### RS Metric:
RS relies heavily on a user-defined penalty factor c. While this allows for flexibility, it also introduces subjectivity. Different penalty values could lead to significantly different conclusions about model reliability, and there's no clear guidance on how to choose an appropriate penalty for a given application. And no appropriate range of c has been discussed. And given this work was positioned as reflections of real-world text-to-SQLs. It would be better disccuss which ranges of c selected can represent which groups of people. For example, whether data analysis with strong SQL knowledge requires just small penalty since they can fix issues if just small alerts are allowed. If this user have high-privacy considerations or totally unaware of SQL knowledge, this penalty could be set to large? Did different range of c will lead to performance shift of LLM or strategy based on GPT-4o?  As a core contribution, the absence of detailed analysis about c's implications and practical application is a significant weakness.

Also, what does \Phi{} mean in Line 351-352, and N/2, this is hard to understand and i didn't find where the big \Phi was defined before. And why implement these three metrics here?

### Experiments:

1) The authors claim to include SQLCoder-2 as the state-of-the-art (SOTA) model. However, several crucial points about this are unclear. First, there are no links, references, or citations to provide more information about SQLCoder-2, and I couldn't locate it on established leaderboards such as SPIDER or BIRD. Additionally, the paper misses details on whether SQLCoder-2 is used as an encoder or decoder-based language model. It would be more appropriate to benchmark against well-recognized models like CodeS [6], which is a widely accepted SOTA model on the BIRD leaderboard. Testing a single model (SQLCoder-2) seems insufficient, and the paper would benefit from comparing performance with other popular large language models (LLMs) like CodeLlama, LLaMA 3/3.1, DeepCoder, and StarCoder. Furthermore, the decision to fine-tune models on the additional dataset TriageSQL, rather than using the training set of TrustSQL, requires more justification. Since this is a benchmark study, it raises concerns about whether other users would also need to fine-tune their models on TriageSQL before proceeding with TrustSQL. Lastly, the mention of "sub-model" is ambiguous—if this is referring to a mixture-of-experts (MoE) system, it should be explicitly stated. Otherwise, it is unclear why a single model's performance is not evaluated. This leaves questions regarding whether the authors are testing text-to-SQL systems as a whole or focusing purely on MoE systems.

2) Another point of concern is the separate implementation of CL methods for SQLCoder-2 and uncertainty estimation (UE)-based methods for T5. It would be more informative to apply both methods to the same model for a more direct comparison, as was done with GPT-4o. If there are specific reasons preventing SQLCoder-2 from being used with UE-based methods or preventing T5 from using CL-based methods, these limitations should be explicitly stated. This would help clarify the generalizability of these techniques. Additionally, the description of the CL-based method implementation is vague, making it difficult to understand how it differs from existing methods like DTE [1]. If CL-based methods are a core contribution of this work, the paper should include a comparison with prior methods and highlight the improvements made in this work.

3) The explanation of how uncertainty estimation (UE) is applied to GPT-4o is unclear. In Line 118, the authors state that the UE-based method can enhance LLM safety by qualifying model confidence, but the connection between this claim and the four dimensions defined in the Related Work section is not sufficiently explained. Moreover, the paper does not clarify how model confidence is represented for GPT-4o, given that it is a closed-source model. This is a crucial point that needs further elaboration to ensure the reproducibility and transparency of the method.

### Questions
1) Why did you choose to re-annotate existing datasets with just limited domains like ATIS and EHRSQL rather than leveraging larger benchmarks such as SPIDER and BIRD which contains ambiguous questions covering multiple domains already? What are trade-offs they considered in choosing these specific datasets over more diverse ones like SPIDER or BIRD? Could you explain the specific guidelines used for generating infeasible questions, and how your approach meaningfully improves upon template-based methods like EHR-SQL? Please provide concrete examples that demonstrate how your method yields more diverse or higher-quality data compared to existing techniques. 

2) Could you describe the **full annotation process** and **quality control** procedures used in your work? Specifically, how many annotators were involved, what were their expertise levels, how were they recruited, and what compensation was provided? Additionally, did you employ expert panels for review, and what specific measures were implemented to ensure the quality and consistency of annotations across the dataset?

3) How does your system address the complexity of SQL query equivalence in its classification scheme? For example, how are questions handled when they have multiple valid SQL representations (e.g., using `MAX` versus `ORDER BY LIMIT 1`), or when queries can be written both with and without nesting? Furthermore, why weren't factors such as natural language complexity or database schema constraints included in your difficulty assessment? See details in Weakness.

4) Could you provide a quantitative comparison of the diversity and distribution of questions in your dataset relative to existing datasets? This should include specifics on the types of templates, distribution across question categories, and empirical evidence demonstrating how your approach achieves greater diversity. How do these distributions align with the natural distribution of questions in real-world scenarios as authors claimed?

5) In terms of RS metric: What is the recommended range for the penalty factor `c`, and how should it be adjusted for different user groups, such as SQL experts or novices? What empirical evidence supports the choice of these ranges? Additionally, could you clarify the role and definition of large `\Phi{}` parameter and the rationale behind using `N/2` in your formula? How sensitive is model performance to changes in these parameter values? See details in Weakness.

6) What was the reason behind selecting SQLCoder-2 as the primary benchmark model? Can you provide details about its architecture (i.e., whether it is encoder- or decoder-based) and explain why other mainstream large language models (LLMs) were not included in the comparison? How does performance of SQLCoder-2 compare to other SOTA models such as CodeS on standard benchmarks?

7) One crucial point of concern is the separate implementation of CL methods for SQLCoder-2 and uncertainty estimation (UE)-based methods for T5. It would be more informative to apply both methods to the same model for a more direct comparison, as was done with GPT-4o. If there are specific reasons preventing SQLCoder-2 from being used with UE-based methods or preventing T5 from using CL-based methods, these limitations should be explicitly stated. This would help clarify the generalizability of these techniques. Additionally, the description of the CL-based method implementation is vague, making it difficult to understand how it differs from existing methods like DTE . If CL-based methods are a core contribution of this work, the paper should include a comparison with prior methods and highlight the improvements made in this work.

Please see other questions in Weakness for details.

### Soundness
1

### Presentation
1

### Contribution
1
