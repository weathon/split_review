# Position: Towards Bidirectional Human-AI Alignment

- Decision: Accept
- Scores: 10, 8, 6

## Abstract
Recent advances in general-purpose AI underscore the urgent need to align AI systems with human goals and values. Yet, the lack of a clear, shared understanding of what constitutes "alignment" limits meaningful progress and cross-disciplinary collaboration. In this position paper, we argue that the research community should explicitly define and critically reflect on "alignment" to account for the bidirectional and dynamic relationship between humans and AI. Through a systematic review of over 400 papers spanning HCI, NLP, ML, and more, we examine how alignment is currently defined and operationalized. Building on this analysis, we introduce the Bidirectional Human-AI Alignment framework, which not only incorporates traditional efforts to align AI with human values but also introduces the critical, underexplored dimension of aligning humans with AI – supporting cognitive, behavioral, and societal adaptation to rapidly advancing AI technologies. Our findings reveal significant gaps in current literature, especially in long-term interaction design, human value modeling, and mutual understanding. We conclude with three central challenges and actionable recommendations to guide future research toward more nuanced, reciprocal, and human-AI alignment approaches.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This position paper conducts a systematic literature review of 411 papers in the AI alignment literature. It then introduces the "Bidirectional Human-AI Alignment Framework," which consists of 1) aligning AI values to human values and 2) aligning humans to AI (i.e., enabling humans to adapt to rapid AI development and the associated social, political, economic changes). Through qualitative coding of the papers included in the systematic review, the paper then identifies gaps in the alignment literature such as human-in-the-loop evaluation, fostering AI literacy, human-AI collaborative dynamics, and ethical auditing. 

The paper then outlines three important directions for future research: 
- Specification Game: how can human values be fully specified and then integrated into AI systems? How can human values be elicited from dynamic interfaces beyond instructions, rankings, and ratings?
- Dynamic Co-evolution of Alignment: how can AI systems keep up with/update to reflect evolving human values? How do AI systems themselves influence human values? How can humans adapt to rapidly advancing AI capabilities?
- Safeguarding Co-adaptation: how can values in AI systems be made interpretable, and how can we intervene on those values?

### Strengths
- [Major] Support: this position paper is based on a systematic literature review of over 400 papers. Reviewed papers are individually tagged/categorized in order to determine which areas of alignment research are most/least covered, which is useful quantitative evidence for the position. The tags/categories also appear comprehensive. 
- [Major] Significance & context: the paper sufficiently demonstrates the importance of bidirectional alignment, and the three directions for future research are well-justified, cited, & explained. I appreciated how specific some of the research ideas were, which made the paper very actionable and also useful given the number of citations to prior work (e.g., the discussion in lines 316-30)
- [Major] Discussion potential: the target audience is the research community, and the paper makes a strong case for the importance of the research directions it outlines. As a result, I would expect the paper to inspire significant discussion within the community. 
- [Major] Communication quality: the paper is very well written, and the tables and figures are very informative. I thought the definitions in Section 2 were very clear, and I also appreciated Figures 2 and 3 and the examples given of each category.

### Weaknesses
- [Minor] Methodology: the paper should be more transparent about its methodology
    - Although the systematic review consisted of 411 papers, these 411 papers are not listed or cited anywhere (given that there are only 143 citations). I would highly recommend citing all reviewed papers, then adding a table listing all of them
    - Line 882 indicates that the systematic review "adher[es] to the the [sic] PRISMA guideline." PRISMA is a guideline for transparent _reporting_ of systematic literature reviews, but the paper does not actually follow PRISMA reporting guidelines. Highly suggest adding an appendix with the PRISMA checklist [1-2]
    - In particular, it would be useful to know: how the initial 34,213 papers were identified; what the inclusion/exclusion criteria were for filtering; how the codebook was developed; how coding was performed/how many coders did each paper/how conflicts were resolved, etc.
- [Minor] Context: lines 331-404 could use more citations—in particular, I would like to see citations to work from other disciplines or in non-AI contexts that are good examples of the type of work that you'd like to see (if such work exists)

[1] https://www.prisma-statement.org/

[2] https://prisma.shinyapps.io/checklist/

### Questions
- Lines 44-45: suggest rephrasing to active voice, i.e., "the research community should/must..."
- L95-100: consider moving this definition to the top of Section 2, which might make the definitions easier to follow
-L 411-12: how did you filter for ML, NLP, and HCI only? Can you list some examples of papers from other disciplines that are relevant?
- Framing: "align AI to humans" refers to aligning AI and human _values_, but "align humans to AI" refers to human "human cognitive and behavioral adaptation to AI advancement" (L105-6). Since these are different "axes" that are being aligned, I find the "align humans to AI" language a bit confusing since my instinct is to read that statement as "align human values to AI values" (which is incorrect). Suggest changing the language, maybe "align AI to human values" and "align humans to AI capabilities"?
- Captions of figures/tables: is "topology" meant to be "typology"?
- Consider adding citations to [3-4] and maybe the AI resilience literature [5-6]

[3] https://www.full-stack-alignment.ai/paper

[4] https://arxiv.org/abs/2405.10295

[5] https://cetas.turing.ac.uk/sites/default/files/2023-08/cetas-cltr_ai_risk_briefing_paper.pdf

[6] https://thefuturesociety.org/aicrisisexplainer/

### Presentation
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This position paper introduces a "Bidirectional Human-AI Alignment" framework that extends traditional AI alignment from a one-way process of aligning AI to humans into a reciprocal relationship where humans also adapt to AI systems. Through a systematic review of over 400 papers spanning HCI, NLP, and ML, the authors organize this framework around four research questions:  (RQ1) What relevant human values are studied for AI alignment, and how do humans specify these values? (RQ2) How can human values be integrated into the AI systems? (RQ3) How do humans learn to perceive, explain, and critique AI? (RQ4) How do individuals and society adapt their behaviours in response to AI advancements? The paper concludes with three progressive challenges: the "Specification Game" requiring better methods to capture human values through democratic processes; "Dynamic Co-evolution" necessitating continuous adaptation where AI systems and humans evolve together; and "Safeguarding Co-adaptation" demanding interpretable AI architectures with robust oversight to prevent harmful autonomous actions, ultimately arguing for alignment as an ongoing, mutual adaptation process.

### Strengths
* One area of strength lies in its successful unification of disparate research communities and perspectives under a coherent bidirectional framework. It excellently bridges the significant gap between ML/NLP and HCI communities, which have been working on different aspects of alignment in isolation - some focused on aligning AI to human values, others on human adaptation to AI systems. 
* The framework systematically integrates these previously siloed research streams while thoughtfully incorporating the critical but often overlooked temporal dimension of alignment, recognizing that both human values and AI capabilities evolve dynamically over time.
* The authors provide clear, standardized terminology that helps unify fragmented field vocabulary, supported by a robust systematic review of 400+ papers that lends empirical credibility to their gap identification and claims.
* Also, the paper demonstrates that alignment isn't merely a technical problem but requires a holistic approach considering human cognitive adaptation, behavioral changes, and broader societal impacts, effectively articulating current research gaps, underexplored dimensions, and potential future challenges.

### Weaknesses
* The paper suffers from some structural and evidential limitations that undermine its impact. A major flaw is the heavy reliance on appendix materials, where essential content, including comprehensive value taxonomies, definitional frameworks, and systematic methodology, is buried rather than integrated into the main narrative, creating a fragmented reading experience where the main text cannot stand alone.

* The paper lacks some real-world scenarios demonstrating the urgent risks of maintaining current unidirectional alignment approaches, without concrete examples of potential failures or misalignment consequences. 

* Despite reviewing 400+ papers systematically, the main text lacks sufficient quantitative analysis and relies too heavily on qualitative descriptions. The main text/body of the paper misses opportunities to provide statistical evidence through concrete metrics on research distributions, citation patterns, and temporal trends, particularly weakening claims about ML/NLP vs. HCI disparities that would benefit from numerical data rather than general assertions.

The content is valuable. I'd suggest restructuring the paper in the final version.

### Questions
* How would you mathematically formalize bidirectional optimization that simultaneously trains AI systems and adapts human behavior, rather than current single-direction loss functions? How would you make it even more dynamic to cover the evolution of values? 
* What algorithmic methods would validate that training data represents authentic human values before assuming it's a "gold standard"?
* When AI capability goals conflict with human agency preservation, what mathematical frameworks would resolve these trade-offs?
* What specific legal requirements would operationalize bidirectional alignment (e.g., mandatory human adaptation impact assessments)?
* How would you structure enforceable agreements between AI companies, users, and regulators across different jurisdictions?
* How would bidirectional optimization scale computationally for systems like ChatGPT or Claude serving millions of diverse users?
* With conflicting user values and adaptation needs, how would your framework handle this complexity while maintaining system safety?

### Presentation
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper reviews over 400 works across HCI, NLP, ML, and related areas to examine how “AI alignment” is defined and practiced. It proposes the Bidirectional Human-AI Alignment framework, which pairs aligning AI to human values with aligning humans to AI through cognitive, behavioral, and societal adaptation. The study identifies gaps in long-term interaction design, human value modeling, and mutual understanding. It also outlines three core challenges specification gaming, scalable oversight, and dynamic alignment and offers recommendations for more reciprocal and adaptive alignment approaches.

### Strengths
The paper clearly articulates its central position that alignment should be understood as a bidirectional, dynamic process, expanding beyond the traditional one-way perspective. 
It supports its argument with a large-scale systematic review of over 400 papers, giving its claims breadth and grounding in cross-disciplinary literature. 
The Bidirectional Human-AI Alignment framework is well-structured and effectively links conceptual ideas to practical dimensions, making the proposal tangible.

### Weaknesses
Although it identifies major research gaps, it offers few concrete methodologies or metrics for implementing and measuring “aligning humans to AI” in practice.

### Questions
How might the framework be stress-tested in real-world, high-stakes environments to ensure its applicability beyond academic or prototype settings?

Have you considered whether certain AI capabilities or domains (e.g., medical AI vs. creative AI) require different balance points between the two alignment directions?

### Presentation
2
