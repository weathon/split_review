# SMRS: advocating a unified reporting standard for surrogate models in the artificial intelligence era.

- Decision: Accept
- Scores: 7, 7, 2

## Abstract
Surrogate models are widely used to approximate complex systems across science and engineering to reduce computational costs. Despite their widespread adoption, the field lacks standardisation across key stages of the modelling pipeline, including data sampling, model selection, evaluation, and downstream analysis. This fragmentation limits reproducibility and cross-domain utility – a challenge
further exacerbated by the rapid proliferation of AI-driven surrogate models. We argue for the urgent need to establish a structured reporting standard, the Surrogate Model Reporting Standard (SMRS), that systematically captures essential design and evaluation choices while remaining agnostic to implementation specifics. By promoting a standardised yet flexible framework, we aim to improve the reliability
of surrogate modelling, foster interdisciplinary knowledge transfer, and, as a result, accelerate scientific progress in the AI era.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
3

### Summary
This paper proposes the Surrogate Model Reporting Specification (SMRS), a unified and modular reporting standard designed to improve transparency, reproducibility, and cross-domain collaboration in surrogate modeling. Surrogate models, which approximate expensive simulations or physical processes, are increasingly used across scientific and engineering domains but suffer from inconsistent documentation of key decisions such as data sampling, model choice, uncertainty handling, and evaluation. SMRS outlines a structured schema covering these aspects and demonstrates its utility through case studies. While the framework is tailored to surrogate modeling’s unique needs—such as replacing known simulators rather than modeling observational data—it is designed to be model-agnostic and flexible to accommodate diverse methodologies. The authors argue that adopting SMRS can reduce fragmentation in the field, foster methodological rigor, and accelerate scientific progress.

### Strengths
The paper offers a timely discussion about the lack of standardization in surrogate modeling and proposes a possible solution through the Surrogate Model Reporting Specification (SMRS). The proposed framework is a reasonable starting point for improving reporting consistency. The inclusion of multiple case studies, drawn from a review of 17 papers, helps to illustrate the practical challenges and potential use of the SMRS. Overall, the paper raises a relevant issue and contributes to ongoing conversations around reproducibility and documentation in this area.

### Weaknesses
While the paper provides a thorough and structured discussion of what should be reported in surrogate modeling, the practical necessity and expected impact of this level of documentation could be made clearer. The authors propose SMRS as a solution, but the paper would benefit from a deeper discussion of why such detailed reporting is essential — especially in cases where code and data are already open-sourced. It remains somewhat unclear how SMRS would materially improve reproducibility, reuse, or model assessment beyond existing practices. A stronger justification of its added value, perhaps with concrete examples or user perspectives, would strengthen the case.

### Questions
While the paper proposes a detailed reporting framework for surrogate modeling, I’m unclear on what specific benefits this would offer beyond open-sourcing code and data. Could the authors clarify how SMRS adds value in scenarios where full implementation code is already shared? In particular, how does structured reporting improve reproducibility or model reuse in ways that well-documented repositories or notebooks might not?

### Presentation
3

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The paper advocates for a unified reporting standard, SMRS, for surrogate models across domains. It argues that fragmentation in current practice hampers reproducibility, comparability, and cross-domain knowledge transfer, and proposes a modular, model-agnostic schema covering data collection (including sampling design, fidelity), model class specification, learning methods, evaluation (diagnostic and task-based), and benchmarks. The authors discuss alternative viewpoints (e.g., risks of over-standardization, domain specificity) and address them. The case studies illustrate how the framework might be applied to existing and future literature.

### Strengths
* The paper makes a persuasive case that a unified reporting schema could significantly improve reproducibility, transparency, and cross-domain reuse of surrogate models. The argument for cross-domain knowledge transfer was convincing to me even though I was initially skeptical due to highly domain-specific practices.
* Data discussion was thorough, well structured by splitting into observational and simulated data. Appreciate the discussion of data selection, fidelity levels, active learning, etc. which will become more important as the field progresses, as well as the emphasis on data sampling which is often not reported or justified in papers. 
* The deterministic vs probabilistic discussion, learning methods, sections are well reasoned and show an awareness of both classical and modern AI-based approaches.
* Alternative views section addressed genuine concerns.
* The call for benchmarks is important and well argued, with a reasonable scope that could realistically be adopted incrementally.
*  The case studies were helpful in showing the schema’s immediate use.

### Weaknesses
* While the paper discusses fidelity levels, it does not directly address surrogates trained from multiple heterogeneous simulation datasets (e.g., ClimateSet [1]). This might be a valuable scenario SMRS to address.
* Some applications mentioned (e.g., drug development) do not map cleanly to the fidelity concept, and the paper does not fully explain how SMRS should be adapted in such cases. This gap could make adoption harder in certain fields. Including some of these in the case studies would be helpful.
* The evaluation section could give more emphasis to defining good diagnostic and especially task-based evaluation protocols. Examples include metrics for extremes or quantiles, assessing scaling relative to naive baselines, and measuring the spread of predictive distributions for generative models. These could be explicitly encouraged in the schema rather than implied (an "X" mark for missing evaluation which goes beyond basic MSE, etc.).
*

### Questions
1. How would SMRS handle a surrogate trained on multiple simulation sources with differing definitions of fidelity?
2. Can the authors clarify how richer task-based evaluation metrics could be systematically incorporated into the schema to encourage their use?
3. For domains without a clear fidelity hierarchy (e.g. drug development), how should that part of the schema be adapted or marked as “not applicable”?
4. From the case studies, it seems the framework is especially useful when an outsider is able to evaluate the work and note deficiencies. An author self-reporting might write things more generously. Is there a way to address this? Further, how should the framework be used and by whom (in a new paper itself, as part of their documentation, in a survey work or benchmark work, etc.)? Some more discussion on the author's vision for implementation and use would be helpful.

### Presentation
4

---

## Human Reviewer 3

### Rating
2

### Rating Number
2

### Confidence
5

### Summary
The paper argues for a position to use rigorous reporting schema when publishing new surrogate models.

### Strengths
1. The paper clearly argues in favor of using rigorous reporting schema when proposing new surrogate models.
2. The authors provide 3 case studies to support their arguments.

### Weaknesses
1. The argument of the paper is trivial. Any paper of any research field should use a rigorous reporting schema describing its computational gains and losses, data collection, model class, learning and evaluation methods.
2. The case studies are very limited and at times are wrongly cited: for example, the paper in case study in Section B uses the learning rate of 1e-3 and not 1e-4. The same optimizer is called Adam in Section B and ADAM in Section C indicating that the authors potentially simply copy-pasted arbitrary details from 3 papers, which they call case studies.

### Questions
1. I would be interested to understand, which information would authors like to convey with this paper apart from a trivial statement that any paper of any research field should use rigorous reporting schema?

### Presentation
2
