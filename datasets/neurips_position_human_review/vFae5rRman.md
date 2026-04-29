# Position: Benchmarking is Broken - Don't Let AI be Its Own Judge

- Decision: Accept
- Scores: 8, 4, 6

## Abstract
The meteoric rise of Artificial Intelligence (AI), with its rapidly expanding market capitalization, presents both transformative opportunities and critical challenges. Chief among these is the urgent need for a new, unified paradigm for trustworthy evaluation, as current benchmarks increasingly reveal critical vulnerabilities. Issues like data contamination and selective reporting by model developers fuel hype, while inadequate data quality control can lead to biased evaluations that, even if unintentionally, may favor specific approaches. As a flood of participants enters the AI space, this "Wild West" of assessment makes distinguishing genuine progress from exaggerated claims exceptionally difficult. Such ambiguity blurs scientific signals and erodes public confidence, much as unchecked claims would destabilize financial markets reliant on credible oversight from agencies like Moody's.

In high-stakes human examinations (e.g., SAT, GRE), substantial effort is devoted to ensuring fairness and credibility; why settle for less in evaluating AI, especially given its profound societal impact? This position paper argues that a laissez-faire approach is untenable. For true and sustainable AI advancement, we call for a paradigm shift to a unified, live, and quality-controlled benchmarking framework—robust by construction rather than reliant on courtesy or goodwill. Accordingly, we dissect the systemic flaws undermining today’s evaluation ecosystem and distill the essential requirements for next-generation assessments. 

To concretize this position, we introduce the idea of PeerBench, a community-governed, proctored evaluation blueprint that seeks to improve security and credibility through sealed execution, item banking with rolling renewal, and delayed transparency. PeerBench is presented as a complementary, certificate-grade layer alongside open benchmarks, not a replacement. We discuss trade-offs and limits and call for further research on mechanism design, governance, and reliability guarantees. Our goal is to lay the groundwork for evaluations that restore integrity and deliver genuinely trustworthy measures of AI progress.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This position paper argues that current AI benchmarking practices are fundamentally broken due to data contamination (test sets leaking into training data), selective reporting, systematic bias, fragmented metrics, and lack of quality control. These flaws make it virtually impossible to disentangle genuine progress from manufactured performance, undermining scientific credibility.

The paper advocates replacing current "open-book" self-reported leaderboards with standardized, proctored examinations similar to human examinations. Its solution centers on secret test sets, proctored execution, community governance, continuous renewal, cryptographic auditability, equitable access, and multi-metric reporting.

It presents PEERBENCH, a prototype platform implementing these principles through validators who create private test suites, reputation-based quality control, cryptographic verification, and rolling retirement of materials. The system aims to be contamination-resistant and governed by distributed stakeholders rather than centralized authorities.

The paper's contribution lies in its structural critique of existing evaluation practices and concrete roadmap for establishing trustworthy, sustainable AI assessment methods.

### Strengths
The paper presents a clear argument that current AI benchmarking practices are fundamentally broken and require systematic reform. The authors articulate their position with precision, advocating for a shift from "open-book" self-reported leaderboards to standardized, proctored examinations modeled after human tests.

The argument is well-supported with concrete evidence including specific contamination rates, documented cases of selective reporting, and systematic analysis of current failure modes. The authors provide theoretical reasoning about why contamination is inevitable with internet-scale training and practical examples of how benchmark gaming occurs.

The topic's NeurIPS relevance is high. Reliable evaluation underpins much machine learning research. The paper addresses an important problem of scientific credibility: benchmark scores may no longer reflect genuine capabilities. The PEERBENCH prototype demonstrates technical feasibility.

The authors thoughtfully address counterarguments in Section 5, showing awareness of legitimate concerns about their proposal while providing substantive responses.

### Weaknesses
The paper could benefit from empirical validation of PEERBENCH. The game-theoretic analysis of validator incentives needs deeper examination, as the reputation system could create new gaming opportunities. Cost-benefit analysis is superficial, lacking concrete estimates for infrastructure, human resources, and participation barriers that might exclude smaller research groups.

Alternative positions not adequately addressed include competition naturally eliminating unreliable benchmarks, regulatory standardization similar to clinical trials, industry self-regulation through research consortiums, and incremental reform focused on improving contamination detection. The paper also doesn't address whether some degree of benchmark gaming might have benefits, such as driving innovation, and it doesn't consider evaluations beyond exam-style ones, such as continuous real-world deployment metrics or collaborative/decentralized evaluation.

The subtitle does not accurately reflect the paper's position. Occasional capitalization/formatting inconsistencies appear unprofessional.

### Questions
How would PEERBENCH be economically sustainable? Who bears the costs? Would submission fees exclude smaller research groups or academic institutions with limited funding? This could influence its feasibility.

What evidence supports the claim that a complete paradigm shift is necessary instead of incremental reforms like better contamination detection, mandatory pre-registration of evaluation methods, or industry standards for benchmark retirement?

How would PEERBENCH prevent new forms of gaming, such as validator coalitions manipulating reputation scores, strategic timing of submissions, or validators reverse-engineering patterns from revealed test subsets? How would it manage the existing problem of sycophantic gaming?

Adoption requires mass coordination across competing organizations. Why is this feasible? What is your transition strategy?

For subjective tasks requiring human judgment, how would peer voting among validators avoid the biases you criticize in current LLM judging systems?

What would constitute failure conditions for PEERBENCH that would warrant returning to current approaches, and how would you detect such failures before they undermine scientific progress?

### Presentation
3

---

## Human Reviewer 2

### Rating
4

### Rating Number
4

### Confidence
3

### Summary
The paper critiques current AI benchmarking practices, highlighting critical limitations such as data contamination, lack of quality control, selective reporting, and fragmented evaluation standards. To address these issues, the authors propose PeerBench—a community-governed evaluation framework inspired by standardized human testing systems like the SAT or GRE. The proposed system incorporates features such as secret test sets, cryptographically verified execution environments, a reputation-based validator network, and continuous test renewal, aiming to create a contamination-resistant yet research-useful benchmarking ecosystem.

### Strengths
1. The paper addresses an urgent and widely recognized issue in the AI community - the growing unreliability of existing benchmarks as indicators of real-world model capability.
2. The authors provide compelling examples and analysis of systemic benchmarking failures, including training data leakage and selective reporting, which support the motivation for their proposal.
3. The concept of PeerBench introduces novel elements such as cryptographic verification and continuous test renewal, which could offer meaningful improvements in benchmark robustness and credibility.

### Weaknesses
1. Scalability is a major concern of the proposed approach. The system depends on sustained human participation for test development and validation.
2. The described framework appears more accessible to well-funded organizations, which may inadvertently reinforce existing disparities in the research ecosystem.
3. The proposal currently lacks empirical validation—there are no experiments or prototype implementations to assess feasibility or impact.

### Questions
1. It would be helpful for the authors to clarify their position on the concerns raised above, especially with regard to scalability and inclusiveness.
2. The paper reads more like a proposal for a new benchmark than a broader position paper. It would benefit from clearly distinguishing the overarching position from the specific PeerBench design, allowing space for alternative community-driven solutions to emerge.

### Presentation
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
The paper argues that current AI benchmarking practices are fundamentally flawed due to issues like data contamination, selective reporting, biased test construction, and lack of transparency. The paper calls for a shift toward robust, trustworthy, and auditable benchmarks to ensure that AI progress is accurately and fairly measured. To this end, the authors propose a new evaluation system, PEERBENCH, a prototype platform designed to implement this vision, using reputation-weighted validation, rolling test updates, and cryptographic auditability.

### Strengths
1. Clear: The paper clearly articulates a timely and pressing position: that current AI benchmarking practices are inadequate, prone to contamination, and increasingly untrustworthy.
2. Analytical: The authors support their position with a comprehensive critique of structural flaws in existing benchmarks, like  cherry-picking, selective reporting, lack of fairness, and data contamination.
3. Strong proposal: PEERBENCH is a strong prototype proposal that illustrates the feasibility of the vision, grounding the argument in practical design.
4. Counter-arguments: the paper engages with counterarguments and transparently acknowledges trade-offs, which strengthens its credibility.

### Weaknesses
1. While the paper presents a compelling case, it could more critically examine the limitations of using human standardized exams as the guiding metaphor for AI evaluation. 
2. While the paper briefly mentions infrastructure and participation challenges, the scalability, economic viability, and governance logistics of PEERBENCH deserve deeper exploration.
3. The paper could also benefit from engaging more substantively with alternative proposals. For example, consider hybrid models that combine open and closed testing, or community-driven, dynamic benchmark curation.

### Questions
1. How does PEERBENCH plan to manage the scalability and sustainability of continuous test generation and validator participation over time, especially as the number of models and evaluation streams continue to grow?
2. Human exams are known to suffer from biases and systemic inequities. Why is this paradigm considered a gold standard for AI evaluation, and how does PEERBENCH avoid inheriting those flaws?
3. Could you elaborate on the tradeoffs between transparency and secrecy in evaluation? How does the system ensure community trust if critical test sets are withheld until retirement?
4. How would PEERBENCH handle adversarial or low-quality validator participation at scale, and what are the fallback mechanisms if validator consensus becomes fragmented or manipulated?
5. Have you considered or experimented with hybrid benchmarking models that incorporate both real-time user feedback and proctored-style evaluations?

### Presentation
3
