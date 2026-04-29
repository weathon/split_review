# Comparison requires valid measurement: Rethinking attack success rate comparisons in AI red teaming

- Decision: Accept
- Scores: 9, 6, 5, 5

## Abstract
We argue that conclusions drawn about  relative system safety or attack method efficacy via AI red teaming are often not supported by evidence provided by attack success rate (ASR) comparisons. We show, through conceptual,  theoretical, and empirical contributions, that many conclusions are founded on apples-to-oranges comparisons or low-validity measurements.  Our arguments are grounded in asking a simple question: When can attack success rates be meaningfully compared? To answer this question, we draw on ideas from social science measurement theory and inferential statistics, which, taken together, provide a conceptual grounding for understanding when numerical values obtained through the quantification of system attributes can be meaningfully compared.  Through this lens,  we articulate conditions under which ASRs can and cannot be meaningfully compared.  Using jailbreaking as a running example, we provide examples and extensive discussion of apples-to-oranges ASR comparisons and measurement validity challenges.

## Human Reviews

## Human Reviewer 1

### Rating
9

### Rating Number
9

### Confidence
4

### Summary
This position paper maintains that the conclusions involving AI system safety deriving from the comparisons of Attack Success Rate (ASR) are often fundamentally flawed. It identifies a conceptual incoherence where the comparability of the ASRs used is di erent in the underlying quantities (estimands) being evaluated.

This paper concerns itself mostly in providing a formal measurement framework of the ASRs that is di erentiated from the social sciences, which aids in conceptualizing safety. This framework also separates high-level safety estimands (theoretical success probability) from the ASR used. 

ASR comparisons to be more meaningful, the paper emphasizes the need for researchers to explicitly describe their estimands. It states that ASR measurement relies on providing precise criteria for ASR which in turn leads to poorly-defined measurement.

### Strengths
This paper is an exemplarity of clarity, logic, and persuasion in its argumentation. It constructs a new and useful measurement framework taken from social science to identify deep-seated issues in the AI red teaming evaluation paradigm. The argument is cohesive and meticulously crafted, blending robust conceptual reasoning, insightful case studies of pivotal published work, and targeted empirical evidence that vividly illustrates the core claims. Why this topic is critical and timely for the NeurIPS community is that it concerns the validity of the measurements that were used to justify the AI safety claims. The paper is not a mere critique; it is proactive by offering constructs aimed at helping researchers by providing them the theories and actionable guidance needed to perform more meaningful evaluations.

### Weaknesses
The debate around 'AI red teaming' tends to use the term too broadly. This term should be scoped to the focus on automated and quantitative jailbreaking assessments. While the paper’s theoretical framework is coherent, it must confront the practical challenge of defining ‘the oracle’ for complex, contested biases or manipulations, which is essential to its proposed process. The primary alternative position addressed is the status quo of ad-hoc evaluation. The paper could further construct its argument to consider other evaluation philosophies, those which aim to derive a diverse portfolio of exploitable weaknesses as opposed to a single, easily comparable ASR or those which privilege qualitative ‘existence proofs’ as the primary goal of red teaming.

### Questions
Your framework provides strong justification for comparing conceptually coherent estimands. In cases of more qualitative, exploratory forms of red teaming where a single ASR does not serve as a serting a diverse portfolio of "unknown unknown" vulnerabilities, how would you apply it? Is it possible that a system’s safety can be better described as a vector of coherent ASRs for different threat models than a single score?  

The oracle success criterion s remains a powerful theoretical construct. In the case of subtle biases or more complex, contested harms like manipulation, what practical steps or best practices can be taken to develop a defensible systematization of s in the absence of a true oracle, and do so, even if imperfectly?

### Presentation
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper critiques the common practice of comparing "Attack Success Rates" (ASRs) in AI red teaming, arguing that such comparisons are often flawed and don't provide meaningful insights into a system's safety. The authors propose that for ASR comparisons to be valid, they must satisfy two conditions: conceptual coherence, meaning the attacks and outcomes being measured are truly comparable, and measurement validity, ensuring the ASR accurately reflects the intended concept. The paper details how current red teaming efforts often violate these conditions through poor quality prompts, unreliable judges, and misleading "apples-to-oranges" aggregations, leading to misleading conclusions about AI safety. It uses recent "jailbreak" studies to illustrate these failures and recommends stricter definitions, more valid threat models, and better evaluation methods to improve the rigor of AI safety testing.

### Strengths
The paper presents a strict, formal framework for determining when Attack Success Rates can be reliably compared. It offers both the theoretical foundation and real-world examples to show the common mistakes in current research. The examples are specific, well-explained, and directly relevant to the topic. The paper's recommendations, if adopted, have the potential to significantly improve the accuracy of metrics used in AI red teaming.

### Weaknesses
The paper is overly long and repetitive, relying heavily on examples of failures without acknowledging when Attack Success Rate comparisons might be useful. It also fails to address practical counterarguments, making its theoretical framework seem too complex for the issues it's discussing.

### Questions
How do the authors propose we retroactively correct for issues like conceptual incoherence or judge bias in those already-published results?

### Presentation
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper argues that ASR (attack success rates) are compared for AI red teaming, researchers need to be more careful thinking about what they are measuring and that this is constant across comparisons, and that this measurement reflects what you care about. The paper proposes precise guidelines to avoid potential problems when comparing ASRs.

### Strengths
- takes a concrete example where a paper does not make valid comparisons 

- underlying position is surely true, you should keep estimand constant when making comparisons! 

- gives clear guidelines for researchers

### Weaknesses
- estimand bit is overly formal for a fairly basic point should be majorly streamlined to make the intuitive point 
- Only a single example presented on when researchers are not holding the estimand constant, hard for me to tell how common this problem is.

### Questions
1. Is there any evidence this is a widespread problem beyond the single example you go over? If you could do some sort of systematic review of ASR's being problematically compared that would update my score. 
2. Doesn't this problem hold for all ML comparisons (e.g. benchmarking?)

### Presentation
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This article points out that many current red team evaluation comparisons based on attack success rate (ASR) often draw untenable conclusions due to inconsistent comparison objects (apples to oranges) or insufficient measurement validity. Drawing on social science measurement theory and inferential statistics, the author proposes two conditions that guarantee comparability:

1. Conceptual coherence—the "estimands" being compared must be consistent. 2. Measurement validity—ASR, as a measurement, should truly reflect the claimed "system security/attack effectiveness." Focusing on jailbreak evaluations, the article systematically deconstructs how different aggregation methods (e.g., one-shot vs. Top-1/Best-of-K/Any-from-T) alter the "quantity being measured," rendering direct comparisons impossible across studies or methods. Using the example of GE vs. GCG, the article illustrates that comparing "Top-1" (392 times) with "one-shot" (1 time) is inherently incomparable. The authors also demonstrate that errors in the judgement (LLM-as-judge) can cause model rankings to reverse, demonstrating that simply using a unified judgement is not sufficient to ensure valid comparisons.

### Strengths
The problem definition is clear and universal: It elevates "ASR comparison" to the level of "estimand comparison" and, using a medical trial analogy, clearly distinguishes between three types of conclusions: descriptive, inferential, and evaluative. The logic is self-consistent and easily transferable to other evaluation scenarios. The methodological foundation is solid: It incorporates the social science measurement theory framework (concepts - systematized concepts - measurement tools - observables) and the "probabilistic threat model," elevating red team evaluation from an empirical practice to a reasoned measurement process. The impact of "aggregation method → ​​measured object" is revealed in depth: the "ontological changes" of indicators such as one-shot, Best-of-K, Top-1/Any-from-T are systematically sorted out, and the inevitability of "increase in option set size → monotonically increase in ASR" is clarified, avoiding the mistaken interpretation of sampling strategy differences as method advantages and disadvantages. The empirical criticism is convincing: using the comparative example of GE vs. GCG, it accurately points out the incomparability of "Top-1 (392) vs. one-shot (1)";

### Weaknesses
Narrow scope: Almost all analysis focuses on jailbreaking/ASR and prompt-based interactions; attacks requiring weighted access or fine-tuning of interfaces are simply acknowledged as "not covered." This limits the generalizability of the conclusions to other red teaming strategies.

Narrow empirical scope and single subject: Reproduction experiments primarily focus on LLAMA 2 (7B/13B), a fixed set of 100 MaliciousInstruct prompts, and 49 decoding configurations, resulting in insufficient sample and model diversity.

The experimental setup may deviate from common deployments: To demonstrate that multiple Top-1 sampling can improve ASR, the authors employed high-entropy decoding and high temperatures (even up to 1.5 and 2.0). While this demonstrates statistical effects, its generalizability to conventional conservative decoding is questionable.

### Questions
Same as the weakness.

### Presentation
3
