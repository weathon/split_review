# Federated Learning is Needed to Overcome Key Challenges Arising from the European Union AI Act

- Decision: Reject
- Scores: 6, 8, 5

## Abstract
The European Union AI Act (AI Act) introduces comprehensive requirements for AI systems regarding data governance, safety and security, and energy efficiency and sustainability, among others. High-risk AI applications, such as AI systems for medical data processing, face particularly stringent compliance requirements. We argue that _Federated Learning (FL) is needed to overcome key challenges arising from the AI Act_, especially with regard to data governance.
Through careful analysis of the AI Act from a technical perspective, we show that the distributed architecture of FL inherently addresses regulatory requirements around data privacy, consent-based processing, and computational resource allocation. We critically examine the current shortcomings of FL in the context of the AI Act and map out research priorities that are needed to on the path towards full regulatory compliance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper analyzes the regulatory challenges posed by the EU AI Act to high-risk AI applications, such as automotive semiconductor production, highlighting issues related to electricity constraints and data compliance. It proposes that Federated Learning (FL) enhances data accessibility, security, and energy transparency through localized learning and privacy techniques, such as differential privacy. The contribution lies in identifying FL’s compliance advantages and proposing research questions, such as data auditing and optimization. The position advocates FL as a critical solution for high-risk applications, calling for collaboration between the technical community and regulatory bodies to advance AI development.

### Strengths
Relevant Context: The paper effectively ties Federated Learning (FL) to the EU AI Act, addressing a timely regulatory challenge with practical implications for high-risk AI applications.
Practical Benefits: Highlights FL’s advantages in data privacy, accessibility, and energy efficiency, supported by examples like automotive semiconductor production.
Structured Argument: The paper organizes its position with clear sections (e.g., data governance, privacy, energy) and visual aids (e.g., Figure 3), enhancing readability.
Forward-Looking: Proposes research gaps (e.g., data lineage, energy transparency) and calls for collaboration between technical and regulatory communities, offering a roadmap for future work.
Experimental Insight: Provides initial energy efficiency comparisons (Figure 2) and algorithmic cost analysis (Table 1), grounding the argument in empirical data.

### Weaknesses
Limited Empirical Validation: The experiments rely on a single dataset (20 News Group) and lack diversity, reducing generalizability to high-risk domains.
Theoretical Gaps: Lacks detailed mathematical models or algorithms (e.g., privacy budget optimization), limiting the depth of technical support.
OCR and Formatting Issues: Repeated characters (e.g., “58”, “338”) and inconsistent references (e.g., [7] duplication) detract from professionalism.
Reproducibility Concerns: No access to full datasets or code is provided, contravening NeurIPS standards.
Incomplete Analysis: The paper does not fully address cross-device FL complexities or scalability challenges, leaving some research gaps underexplored.

### Questions
As above.

### Presentation
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper argues that Federated Learning (FL) is not just beneficial but necessary to meet the stringent requirements of the European Union AI Act, particularly in areas such as data governance, privacy, security, and energy efficiency. The authors systematically analyze how the distributed architecture of FL aligns with various regulatory dimensions of the AI Act. The paper positions FL as an ideal technical framework for legal compliance, emphasizing that:
1. FL keeps data on the client side, enabling better privacy control, data lineage, and bias mitigation.
2. FL can help distribute computational resources, mitigating the energy burden of centralized AI development.
3. Instead of solely focusing on FL's advantages, the authors also describe FL's limitations, especially in efficiency, secure computing costs, and support for unlearning.

### Strengths
1. The paper addresses a timely and critical challenge: the intersection of AI regulation and technology. This area is growing increasingly important as laws like the EU AI Act come into force.

2. As a researcher working on FL, I appreciate the authors' efforts in recognizing the AI Act and highlighting a legitimate and practical need for FL algorithms in the real world. This paper moves beyond the usual academic justification and shows that FL is not just a theoretical construct or a repeated call to action from researchers. It’s becoming a real-world necessity.

3. The analysis is systematic and well-structured, effectively mapping FL features to the requirements of the EU AI Act across different domains.

4. It’s also good to see that bias concerns are mentioned in Section 3.1. While FL addresses many issues of centralized learning, it can also introduce biases due to data imbalance across clients, which is a valid concern for future deployments.

5. The paper outlines a future research agenda, including federated quality monitoring and privacy-energy trade-offs, which are meaningful directions for continued exploration.

### Weaknesses
1. While it’s good to see the paper evaluate on an advanced language model, using a common and relatively simple dataset like 20 Newsgroups raises concerns about overfitting, especially given the model’s large number of parameters. A more complex or real-world dataset would strengthen the empirical claims.

2. The paper could benefit from a deeper discussion of privacy mechanisms, particularly differential privacy. In real-world FL deployments, there is a risk that client data could be reconstructed from shared gradients. Discussing this concern would make the paper more complete and grounded in practical privacy guarantees.

### Questions
I have no additional questions. See Weaknesses.

### Presentation
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This position paper addresses the regulatory challenges introduced by the European Union Artificial Intelligence Act (AI Act), especially for high-risk AI applications, and makes the case that Federated Learning (FL) is a necessary approach for achieving compliance in key areas. The authors provide a technical analysis of how FL’s distributed architecture aligns with regulatory requirements concerning data governance, privacy and security, energy efficiency, and sustainability. The paper details how FL allows data to remain local and can leverage distributed computational resources, which addresses data accessibility and energy requirements per the AI Act (Sections 3–5, Fig. 1). The paper also discusses the current limitations of FL, such as efficiency loss, technical complexity in secure aggregation, and difficulties in regulatory-mandated “right to be forgotten,” and presents directions for future research and development.

### Strengths
+ The paper focuses on the EU AI Act, which is arguably the most comprehensive and urgent regulatory development in AI globally. The analysis is well-timed and highly relevant, as technical and legal communities struggle to interpret and operationalize these new requirements.

+ The authors do a commendable job of translating the abstract obligations of the AI Act (regarding data governance, privacy, energy efficiency) into concrete technical challenges, then mapping them to specific FL properties ([Sections 3–5]). Figure 1 and Table 1 show the relations and roadmap effectively.

+ The paper is well-organized, moving logically from regulatory review to technical mapping, limitations, and open research questions.

### Weaknesses
- While the paper advocates for FL in the context of EU AI Act compliance and alludes to several techniques, such as cross-silo FL and secure aggregation. It falls short of providing a broad, systematic summary of mainstream FL algorithmic paradigms. There is little discussion or comparison of foundational approaches in FL, such as FedAvg (also its variants) versus personalization algorithms, strategies for handling non-IID data, communication efficiency methods, and model aggregation approaches.

- The position paper justifiably claims that FL reduces the risks associated with raw data transfer. However, it does not adequately address the reality that FL by itself is not robust to modern privacy attacks, such as membership inference or gradient inversion. In practice, attackers can often infer sensitive training data from shared model updates, even with only basic knowledge of the FL protocol. The paper briefly mentions that applying secure computing techniques, such as DP, MPC or HE can mitigate some of FL’s privacy risks. However, it does not provide a clear or comprehensive comparison of these approaches or how they combine with or differ from "vanilla" FL.

### Questions
- In which threat models are these techniques (MPC, DP, HE) necessary additions to FL, and when are they sufficient for meeting regulatory standards? How do trade-offs in efficiency, accuracy, and compliance differ when choosing FL+DP vs. FL+MPC, vs. pure FL?

- Can authors give a more formalized, comparative table or figure of technical approaches (FL, centralized, hybrid) versus specific AI Act provisions, indicating open issues and readiness status?

### Presentation
3
