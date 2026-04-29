# Position: Bridge the Gaps between Machine Unlearning and AI Regulation

- Decision: Accept (Oral)
- Scores: 4, 5, 8

## Abstract
The "right to be forgotten" and the data privacy laws that encode it have motivated machine unlearning since its earliest days. Now, some argue that an inbound wave of artificial intelligence regulations — like the European Union's Artificial Intelligence Act (AIA) — may offer important new use cases for machine unlearning. However, this position paper argues, this opportunity will only be realized if researchers proactively bridge the (sometimes sizable) gaps between machine unlearning's state of the art and its potential applications to AI regulation. To demonstrate this point, we use the AIA as our primary case study. Specifically, we deliver a "state of the union" as regards machine unlearning's current potential (or, in many cases, lack thereof) for aiding compliance with the AIA. This starts with a precise cataloging of the potential applications of machine unlearning to AIA compliance. For each, we flag the technical gaps that exist between the potential application and the state of the art of machine unlearning. Finally, we end with a call to action: for machine learning researchers to solve the open technical questions that could unlock machine unlearning's potential to assist compliance with the AIA — and other AI regulation like it.

## Human Reviews

## Human Reviewer 1

### Rating
4

### Rating Number
4

### Confidence
4

### Summary
This position paper argues that machine unlearning (MU) could assist compliance with AI regulations like the EU's Artificial Intelligence Act (AIA), but only if researchers bridge significant technical gaps between current capabilities and regulatory requirements. The authors catalog six potential AIA compliance applications for MU: improving accuracy, mitigating bias, defending against confidentiality attacks, addressing data poisoning, managing generative AI risks, and supporting copyright compliance. For each use case, they identify substantial limitations in current MU techniques, including difficulties identifying problematic data, lack of formal guarantees, and trade-offs between utility and forgetting quality. The paper concludes with a call for the AI research community to address these technical challenges to realize MU's regulatory potential

### Strengths
The paper provides the most comprehensive analysis to date of machine unlearning's potential regulatory applications. The systematic mapping of AIA requirements to technical capabilities is valuable for both researchers and policymakers. The honest assessment of current limitations and clear identification of research gaps could effectively guide future work. The technical analysis is rigorous while remaining accessible to non-experts

### Weaknesses
The analysis may overstate MU's potential benefits while understating the challenges of defining and measuring successful "unlearning" in regulatory contexts. Limited discussion of how regulatory compliance would be verified or audited in practice. Some use cases (particularly copyright) may be better addressed through alternative approaches that receive insufficient consideration. The paper doesn't adequately address whether current MU limitations reflect fundamental theoretical constraints versus engineering challenges. Also and foremost: the EU AI Act is a product safety regulation under the EU New Legislative Framework. It is thus 'techniques-agnostic' by default and this study might be more relevant for other regulations such as the EU GDPR, Data governance act, Data act etc

### Questions
How would regulators verify or audit successful machine unlearning in practice, given the current limitations in evaluation metrics? What evidence suggests that the identified technical gaps are solvable rather than fundamental limitations of the unlearning approach? How might the regulatory landscape's rapid evolution affect the relevance of these specific technical research priorities? Could you elaborate on the trade-offs between investing in MU research versus alternative approaches like differential privacy or architectural solutions?

### Presentation
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper examines the gap between the EU's AI Act (AIA) requirements and current machine unlearning capabilities. The authors explore potential applications of machine unlearning for AIA compliance across several domains: improving model accuracy, mitigating bias, defending against confidentiality attacks and data poisoning, addressing generative AI risks, and resolving copyright issues. The paper provides a comprehensive summary of existing machine unlearning approaches' key limitations and identifies critical open problems that require further research.

### Strengths
- The paper addresses a timely and important intersection between machine unlearning research and EU AI regulation, identifying critical technical gaps that must be bridged for practical compliance.
- The authors provide an effective literature review that clearly synthesizes existing machine unlearning approaches and systematically identifies their key deficiencies and limitations.
- The paper is well-written, clearly structured, and accessible to readers across different technical backgrounds.

### Weaknesses
(1) The paper's title references "AI regulation" broadly, but the analysis focuses exclusively on the EU's AI Act. While this represents a minor overclaim in scope, it could be easily addressed by adjusting the title to reflect the specific focus on EU regulation. A comprehensive analysis of the AIA alone remains valuable and substantive.

(2) The authors propose six distinct applications of machine unlearning for regulatory compliance, which provides a useful organizational framework. However, several of these applications exhibit significant conceptual and technical overlap that warrants deeper analysis. For instance, mitigating bias, controlling generative outputs, and addressing copyright issues all fundamentally relate to neural network memorization and may face similar algorithmic challenges. The paper would benefit from explicitly acknowledging these interconnections and discussing how they affect the design and evaluation of machine unlearning approaches. Additionally, since many existing machine unlearning algorithms claim to address multiple problems simultaneously, a more detailed algorithmic analysis examining which specific techniques are most suitable for each application domain would strengthen the contribution.

### Questions
Following the previous section:

(3) The paper falls a bit short of fully exploring the critical interaction between policy requirements and technical capabilities within the EU regulatory framework. Rather than offering a unique perspective on how machine unlearning should evolve to align with AI governance needs, the work reads primarily as a literature survey cataloging existing technical limitations. The paper would be significantly strengthened by providing concrete insights into how machine unlearning can be positioned as an effective regulatory compliance tool, including specific recommendations for bridging the gap between current technical capabilities and policy requirements. I encourage the authors to articulate a clearer vision for the co-evolution of machine unlearning research and AI regulation, addressing both the technical research priorities and the policy considerations necessary to make machine unlearning a viable compliance mechanism.

Question:
- When bias is exhibited in model behavior, are there any existing techniques that can attribute this to specific training data and then perform machine unlearning accordingly?

### Presentation
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This position paper examines the gap between the current state of machine unlearning and its potential role in helping organizations comply with emerging AI regulations, using the EU’s Artificial Intelligence Act (AIA) as a case study. It catalogs possible applications of machine unlearning to AIA compliance, identifies technical shortcomings, and calls for research to address these gaps.

### Strengths
the paper is very well written.
it show case the bullet points  in GDPR and the relation with machine unlearning. the paper properly discusses intersection between the provided regulations and machine unlearning. 

for each point, it first discusses how that rule is interpreted, or employed. then it shows the relation with unlearning and it then discusses the potential and downside of machine unleanring methods for that particular topic. 


the paper is also very well positioned on the existing literature, regulations.

### Weaknesses
line 79> Hyperparameters .... > Please add reference for this statement. 

line 112> Here risks ... > This statement can broadly cover many topics. It would be better specify the objective related to regulation for unlearning

### Questions
1- It would be interesting if the authors a direction for the research direction of the appointed topics for example in section "MU for AIA compliance: a catalog > Accuracy" authors very well described the what AIA expects by  "Accuracy: Improve accuracy per EU [35, Arts. 9, 15];", they also discussed the SOTA unlearning methods for that topic, and the advantages and disadvantages of those method. I think, the only missing point, is the proposed future direction for the unlearning research society to address the discussed concerns.

### Presentation
4
