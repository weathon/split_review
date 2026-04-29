# A Sustainable AI Economy Needs Data Deals That Work for Generators

- Decision: Accept
- Scores: 7, 7, 4

## Abstract
We argue that the machine learning value chain is structurally unsustainable due to an economic data processing inequality: each state in the data cycle from inputs to model weights to synthetic outputs refines technical signal but strips economic equity from data generators. We show, by analyzing seventy-three public data deals, that the majority of value accrues to aggregators, with documented creator royalties rounding to zero and widespread opacity of deal terms. This is not just an economic welfare concern: as data and its derivatives become economic assets, the feedback loop that sustains current learning algorithms is at risk. We identify three structural faults - missing provenance, asymmetric bargaining power, and non-dynamic pricing - as the operational machinery of this inequality. In our analysis, we trace these problems along the machine learning value chain and propose an Equitable Data-Value Exchange (EDVEX) Framework to enable a minimal market that benefits all participants. Finally, we outline research directions where our community can make concrete contributions to data deals and contextualize our position with related and orthogonal viewpoints.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This position paper argues that the current machine learning value chain is structurally unsustainable due to "economic data processing inequality" that systematically transfers value away from data generators to aggregators and model monetizers. Through analysis of 51 publicly disclosed data deals totaling an estimated $1.75 billion, the authors demonstrate that creator royalties effectively round to zero while aggregators capture the vast majority of value. They identify three interconnected structural faults: invisible provenance (loss of data lineage and licensing information), asymmetric bargaining power (individual creators vs. large aggregators), and inefficient price discovery (static lump-sum payments that ignore dynamic data value). To address these issues, they propose an Equitable Data-Value Exchange (EDVEX) Framework featuring task-data matching, auditable lineage tracking, and utility-driven valuation mechanisms. The framework aims to create dynamic data unions that enhance creators' bargaining power while providing better data discovery for model developers.

### Strengths
The paper excels in combining rigorous empirical analysis with comprehensive theoretical framework development. The analysis of 51 real data deals provides concrete evidence for abstract economic arguments, while specific examples like Reddit's licensing arrangements make the inequality tangible and compelling. The identification of three interconnected structural faults creates a coherent diagnosis that explains why current approaches systematically disadvantage data generators. The proposed EDVEX framework demonstrates sophisticated thinking about market design, incorporating insights from economics, computer science, and organizational theory. The technical primitives (task-data matching, lineage tracking, utility-driven valuation) are well-motivated and address specific market failures identified in the analysis. The paper successfully bridges multiple disciplines, making contributions to our understanding of both technical ML systems and their economic foundations.

### Weaknesses
While the paper provides a compelling diagnosis and comprehensive framework, several limitations affect its practical impact. The analysis necessarily relies on publicly disclosed deals, which may not be representative of the broader (largely private) data marketplace, potentially biasing conclusions about industry practices. The EDVEX framework, while conceptually sound, remains quite abstract with limited discussion of implementation challenges, transition costs, or adoption incentives for existing market participants. Some proposed technical solutions, particularly Shapley value-based revenue sharing, face known scalability and computational challenges that receive insufficient attention. The paper also underestimates potential resistance from current market incumbents who benefit from existing asymmetries, and provides limited analysis of how to overcome these barriers. Additionally, while the framework addresses multiple technical challenges through "open problems," the complexity of coordinating solutions across all components simultaneously may make implementation more difficult than presented.

### Questions
1. The paper mentions Shapley values for revenue sharing but doesn't address computational complexity. How would EDVEX handle scenarios with millions of data contributors and complex data lineages?
2. Given the entrenched interests of current market incumbents, what specific strategies would you recommend for transitioning from current practices to EDVEX? How might early adoption be incentivized?
3. How would EDVEX prevent the formation of new oligopolies or market concentration among platform providers who operate the framework infrastructure?

### Presentation
3

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
2

### Summary
The authors highlight biases in the current machine learning ecosystem: while data aggregators, transforms, and model monetizers are compensated for their work that builds on top of data generators, data generators themselves are poorly compensated (if compensated at at all). A long term future for machine learning requires fixing this inequity to ensure that data generator continue to be incentivized for long term data generation. The authors highlight that the current faults lie with missing provenance, asymmetric bargaining power, and non-dynamic pricing. The authors propose an Equitable Data-Value Exchange Framework to correct these issues and highlight open questions in this space.

### Strengths
- The authors clearly articulate the issues with the current machine learning pipeline. As someone who does not necessarily work in these areas, the discussion was incredibly eye opening and thoroughly informative. I truly enjoyed reading this piece
- The authors successfully acknowledge opposing viewpoints without dismissing them outrightly
- I have not seen an actual analysis of public data in a position paper, and I think it was really smart of the authors to tie in public data sources in this argument

### Weaknesses
- Sometimes the authors make strong claims that are not necessarily justified. For example, on page 5, the authors claim that, "For fair data deals, it is necessary to understand when, where, and how data is used in the AI pipeline." It's not clear to me why this tracking is necessary or how fairness can be imposed (or to what notion of fairness). 
- It's not clear to me whether EDVEX is a new framework or one that already exists in the literature. *If EDVEX is completely brand new, the position track is not suitable for this paper as it should undergo a thorough peer review with more evidence of its possible success.* 
- There are a lot of open directions and problems and little discussion on the possible downsides that could arise from this. While the authors do acknowledge that malicious actors could "game" the data valuation system (page 7), it still feels like there should be a stronger discussion on possible pitfalls

### Questions
- Is EDVEX a new framework?
- There are a lot of open questions. What should be prioritized?
- The authors mention that there is a challenge with tracking provenance and dealing with data privacy regulation. How do the authors suppose someone could manage these?

### Presentation
4

---

## Human Reviewer 3

### Rating
4

### Rating Number
4

### Confidence
2

### Summary
The paper argues that the current machine learning (ML) value chain is economically unsustainable due to an "economic data processing inequality" that strips value from data generators while enriching aggregators and model monetizers. By analyzing 51 public data deals, the authors identify three structural flaws that systematically disadvantage data originators. They propose the Equitable Data-Value Exchange (EDVEX) framework to create fairer, more transparent data markets that align incentives and improve long-term sustainability for all participants.

### Strengths
The authors present a clear conceptual framework (EDVEX) grounded in empirical evidence from 51 publicly disclosed data deals. Their analysis articulates structural economic problems in the ML data economy with clarity, combining economic theory with practical examples. The integration of technical, economic, and policy considerations makes the proposal relevant across multiple disciplines. Visual diagrams and well-structured sections enhance accessibility and engagement for both technical and non-technical readers.

### Weaknesses
The empirical dataset is limited to publicly disclosed deals, potentially omitting the most impactful or representative transactions. The framework, while conceptually robust, is still theoretical and lacks a concrete implementation or pilot study to validate feasibility. Some recommendations, such as global provenance standards, face substantial political, legal, and logistical barriers that are underexplored. The scope is broad, which can dilute the depth of analysis on critical technical aspects like utility-driven pricing algorithms.

### Questions
1. How might EDVEX be adapted for sensitive data domains (e.g., healthcare, defense) where provenance tracking and open pricing could be restricted by law?
2. What governance or incentive structures could prevent powerful aggregators from capturing and dominating an EDVEX-like marketplace?
3. Could synthetic data generation alter the economic balance the authors describe, and how would EDVEX handle valuation of synthetic contributions?
4. What metrics or experiments could be used to validate whether EDVEX truly improves bargaining symmetry and economic equity in practice?

### Presentation
3
