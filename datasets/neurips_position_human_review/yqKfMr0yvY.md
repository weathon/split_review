# Neither Valid nor Reliable? Investigating the Use of LLMs as Judges

- Decision: Accept
- Scores: 8, 9, 6

## Abstract
Evaluating natural language generation (NLG) systems remains a core challenge of natural language processing (NLP), further complicated by the rise of large language models (LLMs) that aim to be general-purpose. Recently, large language models as judges (LLJs) have emerged as a promising alternative to traditional metrics, but their validity remains underexplored. This position paper argues that the current enthusiasm around LLJs may be premature, as their adoption has outpaced rigorous scrutiny of their reliability and validity as evaluators. Drawing on measurement theory from the social sciences, we identify and critically assess four core assumptions underlying the use of LLJs: their ability to act as proxies for human judgment, their capabilities as evaluators, their scalability, and their cost-effectiveness. We examine how each of these assumptions may be challenged by the inherent limitations of LLMs, LLJs, or current practices in NLG evaluation. To ground our analysis, we explore three applications of LLJs: text summarization, data annotation, and safety alignment. Finally, we highlight the need for more responsible evaluation practices in LLJs evaluation, to ensure that their growing role in the field supports, rather than undermines, progress in NLG.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This position paper argues that the widespread adoption of LLJs for NLG evaluation has been premature, outpacing rigorous validation of their reliability and validity. Drawing on measurement theory from social sciences, the authors critically examine four core assumptions: LLMs as proxies for human judgment, their capabilities as evaluators, their scalability, and cost-effectiveness. Through analysis of three applications, namely text summarization, data annotation, and safety alignment, they demonstrate systematic flaws in current LLJ practices and call for more responsible evaluation standards before further deployment.

### Strengths
- Principled theoretical framework using measurement theory provides rigorous foundation for critique
- Comprehensive coverage of LLJ applications across the ML pipeline
- Well documented analysis of inconsistencies in current practices with concrete examples
- Strong literature review
- Clear articulation of the stakes, evaluation practices shape research directions and funding

### Weaknesses
- Environmental impact discussion feels somewhat tangential to main arguments
- Some sections could be more concise.

### Questions
- Given the documented problems with both human evaluation practices and LLJs, what specific standards or methodologies would you recommend for responsible LLJ validation?
- How do you envision the field transitioning from current practices, taking into consideration the cost benefits in terms of time and money?

### Presentation
3

---

## Human Reviewer 2

### Rating
9

### Rating Number
9

### Confidence
4

### Summary
The paper argues that the LLM as judges for evaluating natural language generation requires more rigorous evaluation practices, suggesting that we haven't evaluated models on reliability and validity aspects. The authors draw from the social science measurement theory which provides a framework for thinking about evaluation, including validity and reliability aspects. The authors bring into question that common narratives that favor use of LLM-as-judges for evaluations, highlighting how some of these narratives are rooted in assumptions that fail or not fully realized in practice. These include, a) LLMs as a proxy for human judgment b) LLMs as capable evaluators c) LLMs as scalable evaluators and d) LLMs as cost-effective evaluators. The authors discuss the limitations in each of these areas.

### Strengths
1. The paper is well motivated and grounded in the framework of social science measurement theory, which provides a great way to think about evaluations.
2. The authors have clearly articulated their position and provide an in-depth discussion of different reasons for using LLM-as-judge for NLG evaluations and provided evidence on how these reasons are not fully realized or have some limitations. The authors have also provided excerpts from the prior work describing how people have framed LLM-as-judge evaluations in their own work.

### Weaknesses
1. The authors argue that we need to "put work into putting in place proper mechanisms for transparent, valid and reliable evaluation." However, the discussion could benefit from adding more on how do authors envision NLG evaluations to be conducted in the future? What sort of roadmap we would want to follow in order to take steps towards conducting more rigorous evaluations? Are there avenues that should be prioritized first? Some of the suggestions might require institutional changes, what challenges do authors envision there?

### Questions
1. Many of the interdisciplinary/applied computational work often spends a lot of time thinking about evaluations, do authors think we have anything to learn from them?

### Presentation
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper analyzes the growing use of Large Language Models as Judges (LLJs) for evaluating NLG systems. The authors argue that adoption has outpaced scientific validation of their reliability and validity. Based on measurement theory, the paper examines four assumptions: (1) a proxy for human judgment, (2) evaluator capability, (3) scalability, and (4) cost-effectiveness. The authors identify key limitations: inconsistent human benchmarks, deviation from instructions, vulnerability to biases such as position and self-enhancement, and data contamination. The authors argue that future progress depends on developing standardized evaluation practices that go beyond simple bias mitigation.

### Strengths
- The paper is well-written and timely. Since LLJs are increasingly used not only for evaluation but also in training, a position paper that critically reflects on this trend is both necessary and important.

- It offers a sharp critique, pointing out the limitations of relying solely on correlation with human judgments as a validation criterion. The discussion of vague definitions and inconsistent evaluation scales is also convincing, as these issues can directly cause unreliable scores. 

- The paper's discussion on explainability is important. It correctly identifies a critical gap in the literature: while many studies tout the ability of LLJs to provide rationales, the faithfulness of these explanations is rarely scrutinized. The authors rightly call for a more rigorous evaluation of these generated explanations beyond their 'face validity'.

### Weaknesses
- The paper does not clearly distinguish between pairwise evaluation and independent scoring. For instance, position bias is mainly an issue in pairwise setups, whereas SummEval illustrates problems tied to inconsistent definitions in independent scoring. Explicitly separating these settings would make the argument stronger.

- The authors suggest that annotator disagreement may be seen as “valuable diversity.” While this can be true in subjective tasks, the claim should be made more carefully, since such disagreement may also stem from ambiguous criteria or poor task/aspect design. In this context, exploring agreement across a diverse panel of LLJs could be a useful complementary direction.

### Questions
This paper already provides sufficient discussion; I have no further questions.

### Presentation
3
