# Setting $\varepsilon$ is not the Issue in Differential Privacy

- Decision: Accept
- Scores: 4, 6, 6

## Abstract
This position paper argues that setting the privacy budget in differential privacy should not be viewed as an important limitation of differential privacy compared to alternative methods for privacy-preserving machine learning. The so-called problem of interpreting the privacy budget is often presented as a major hindrance to the wider adoption of differential privacy in real-world deployments and is sometimes used to promote alternative mitigation techniques for data protection. We believe this misleads decision-makers into choosing unsafe methods. We argue that the difficulty in interpreting privacy budgets does not stem from the definition of differential privacy itself, but from the intrinsic difficulty of estimating privacy risks in context, a challenge that any rigorous method for privacy risk assessment face. Moreover, we claim that any sound method for estimating privacy risks should, given the current state of research, be expressible within the differential privacy framework or justify why it cannot.

## Human Reviews

## Human Reviewer 1

### Rating
4

### Rating Number
4

### Confidence
3

### Summary
The position paper argues that the perceived difficulty in setting the privacy budget (ε) in Differential Privacy (DP) is not a fundamental limitation of DP but a reflection of the inherent complexity of quantifying privacy risks. It challenges the notion that ε’s interpretability hinders DP’s adoption, asserting that this misconception drives decision-makers toward less robust privacy methods. The paper highlights DP’s strengths, such as post-processing robustness and composition properties, and critiques alternative privacy metrics (e.g., k-anonymity, l-diversity) for lacking these guarantees. It discusses DP’s interpretability through examples like randomized response and hypothesis testing, and warns against privacy-washing and overemphasis on small ε values. The paper proposes that DP should be the standard for privacy-preserving machine learning (ML), with alternative metrics translated into DP terms for comparability, and emphasizes that high ε values may indicate tasks inherently incompatible with strong privacy.

### Strengths
1) This paper directly challenges a widespread convention in DP research and deployment—fixating on ε as the central unit of privacy. Given the increased use of DP in public and commercial systems (e.g., US Census, Google, Apple), this critique is not only timely but crucial.

2) The authors don’t stop at critique—they propose an actionable alternative. Instead of publishing an abstract ε, they advocate privacy guarantees conditioned on realistic adversary capabilities, e.g., "an attacker with background data X has probability p of detecting participation."

3) The writing is clean, concise, and persuasive. Examples are used well to motivate concepts, such as privacy amplification by subsampling or the attack scenarios in facial recognition datasets.

4) The discussion references practical deployments (Google, US Census), connects with social science concerns (public trust, legal compliance), and is informed by research in both theory and usability of privacy. This broadens its relevance beyond technical DP researchers.

### Weaknesses
1) Not much visuals (not at all). Just reading pure text might be boring. Some intuitive illustrations could benefit for broader comunity.

2) The paper relies heavily on theoretical arguments and lacks empirical data or experiments to validate claims, particularly for DP’s practical performance in ML. The paper would be even more compelling with empirical illustrations—e.g., a worked example showing how threat-parameterized guarantees look in practice versus raw ε disclosure.

3) The authors assume that specifying threat models is a natural extension, but constructing and validating realistic threat models is nontrivial. The paper does not provide guidance or templates for doing so, which may limit immediate impact.

4) The authors advocate for stakeholder-centric privacy guarantees but do not engage deeply with how end-users or non-technical decision-makers interpret risk in the proposed format. How would a public institution decide if a given threat-parameterized guarantee is "good enough"?

### Questions
1) Could you include empirical results or case studies demonstrating DP’s performance in modern ML tasks (e.g., LLMs, image models) to strengthen claims about its practicality?

2) For tasks with inherently high ε (e.g., personalization tasks in Section 5.3), what specific strategies do you recommend to balance utility and privacy beyond acknowledging incompatibility?

3) How do you propose practically implementing the translation of alternative metrics (e.g., Renyi DP, Gaussian DP) into (ε, δ)-DP terms? Can you provide a concrete example?

4) Would you recommend any specific metrics or language for expressing privacy in threat-parameterized outputs?

5) How do you address subjectivity in choosing “realistic” adversary capabilities? Could this become a loophole that weakens practical privacy under the guise of transparency?

### Presentation
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This position paper argues that the common criticism of differential privacy (DP) regarding the difficulty of setting the privacy budget parameter $\epsilon$ should not be viewed as a fundamental limitation that hinders the adoption of privacy-preserving machine learning. The authors contend that the challenge of interpreting privacy budgets stems not from flaws in differential privacy itself, but from the inherent difficulty of quantifying privacy risks. The paper warns that overemphasizing the metric of $\epsilon$ can encourage overfitting to it instead of achieving a true privacy guarantee.

### Strengths
Differential privacy has been under development for nearly two decades and, despite its deployment in numerous real-world applications, remains a subject of ongoing controversy regarding its practical appropriateness. This work is highly relevant and can raise discussion at NeurIPS.

### Weaknesses
The authors argue that reported $\epsilon$ values can be misleading and advocate for quantifying privacy risk through auditing and empirical privacy attacks rather than relying solely on theoretical guarantees. However, this position appears to undermine one of differential privacy's fundamental advantages that has driven its adoption: the provable guarantees against *any* future attacks, including those not yet discovered. Currently, the DP research paradigm allows researchers to focus primarily on accuracy metrics while reporting $\epsilon$ as a sufficient privacy measure. If $\epsilon$ becomes "less meaningful" and practitioners must resort to empirical privacy attacks to evaluate actual privacy risks, this approach risks losing the very theoretical foundation that distinguishes DP from ad-hoc privacy methods. While the authors correctly identify problems with artificially small $\epsilon$ values achieved through questionable accounting, their solution may inadvertently weaken the theoretical rigor that makes DP attractive to the academic community in the first place.

### Questions
See above.

### Presentation
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This is a timely, well-argued, and important position paper that addresses a significant point of confusion and criticism in the differential privacy (DP) community and among practitioners. The authors effectively challenge a common narrative and provide a robust defense of the DP framework, particularly its use of the privacy budget ε. The paper is well-structured, supported by relevant literature, and makes a compelling case that will be valuable for researchers, reviewers, and practitioners.

### Strengths
1. The paper's core argument is persuasive and clearly articulated. It successfully reframes the "problem of ε" as a universal challenge in privacy risk assessment, not a unique flaw of DP.

    2. The paper covers a wide range of supporting points, from historical failures of anonymization and human cognitive biases in probability estimation to the technical strengths of DP (composition, post-processing) and current trends in research (auditing, gaming ε).

    3. The discussion on "gaming" the privacy budget (Section 4) is particularly insightful and addresses a critical issue in modern DP research. The critique of public pretraining and label DP is accurate and necessary. This section alone provides value by cautioning the community against counterproductive research directions.

  4. The authors acknowledge alternative views (Section 6) and clarify that their position is not against tighter privacy accounting (e.g., Rényi DP) but advocates for a standardized communication framework via (ε,δ)-DP.

### Weaknesses
1. While the paper excellently argues why setting ε isn't a unique problem, it could be strengthened by providing more concrete, practical guidance/examples on how to set it. 

    2. The connection between the Linda problem (conjunction fallacy) and the interpretability of ε is intriguing but slightly speculative. While it's an interesting hypothesis, it should be presented more cautiously as a potential area for future research rather than a firm point in DP's favor.

### Questions
if a concrete example of use cases would help the discussion?

### Presentation
3
