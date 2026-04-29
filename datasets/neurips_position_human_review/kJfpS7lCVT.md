# Position: Meaning Is Not A Metric: Using LLMs to make cultural context legible at scale

- Decision: Reject
- Scores: 10, 8, 3

## Abstract
This position paper argues that large language models (LLMs) can make cultural context, and therefore human meaning, legible at an unprecedented scale in AI-based sociotechnical systems. We argue that such systems have previously been unable to represent human meaning because they rely on thin descriptions: numerical representations that enforce standardization and therefore strip human activity of the cultural context that gives it meaning. By contrast, scholars in the humanities and qualitative social sciences have developed frameworks for representing meaning through thick description: verbal representations that accommodate heterogeneity and retain contextual information needed to represent human meaning. While these methods can effectively codify meaning, they are difficult to deploy at scale. However, the verbal capabilities of LLMs now provide a means of (at least partially) automating the generation and processing of thick descriptions, potentially overcoming this bottleneck. We argue that the problem of rendering human meaning legible is not just about selecting better metrics, but about developing new representational formats (based on thick description). We frame this as a crucial direction for the application of generative AI and identify five key challenges: preserving context, maintaining interpretive pluralism, integrating perspectives based on lived experience and critical distance, distinguishing qualitative content from quantitative magnitude, and acknowledging meaning as dynamic rather than static. Furthermore, we suggest that thick description has the potential to serve as a unifying framework to address a number of emerging concerns about the difficulties of representing culture in (or using) LLMs. In addressing these challenges, we present a pathway to developing systems that can better represent and support meaningful human experiences across domains including healthcare, education, and sustainability.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The paper is concerned about making human meaning  legible at scale in sociothecnical sytems.

-Human meaning is defined in section 2.1 as made of 2 components: CULTURAL (symbols significant in a community, e.g. Olympics rings) and EXPERIENTIAL (experience of events that matter, e.g. coming to age ceremonies).

-Representation of Meaning is in section 3, it is based on Clifford Geertz’s classification of thin and thick descriptions. Thin description is intended as a quantitative representation that "strip[s] human activity of the cultural context that gives it meaning".

Thick description means  "verbal representations that accommodate heterogeneity and retain contextual information needed to represent human meaning."

-Legibility is in section 2, but I had to use Claude to get a meningful definition "[Scott's] legibility is the state's process of simplifying and standardizing complex social realities into formats that can be easily measured, monitored, and administered by bureaucratic institutions."

-Sociotechnical systems are states, social media platforms, institutions for healtcare, education, etc.

The positon of the paper is that LLMs can make thick descriptions legible at scale.

### Strengths
The paper provides a well presented description of several concepts related to the analysis of meaning. 
In the thin/thick descriptions framework, authors explain their choice of representing Meaning via thick descriptions to fully, or, at least, better describe "what really matters" moving away from the tyranny of quantitative proxies (thin descriptions). 

To make thick descriptions available/legible at scale would require the intervention of content-related scholars at levels not possible. 

Their claim is that "LLMs can help solve the problem of scaling thick description. [...] this approach would seek to reproduce a form of analysis that has typically required deep, situated human judgment.", and, in this critical task of scaling thick descriptions, they identify (and discuss) 5 critical challenges for LLMs.
-Meaning Only Exists in Context
-There Is No Single Source Of Truth for Meaning
-Both Lived Experience and Critical Distance Are Crucial
-What $\neq$ How Much [Quantitative vs Qualitative]
-Meaning Is Made, Not Found

Contrasting views are discussed and addressed at a general level.

The paper provides an interesting and growing approach to AI models that entails deeper questions about cultural and social meaning.

### Weaknesses
As I had to navigate through concepts and definitions far from my technical background, I appreciated the clarity of many of those concepts in the paper, and the care, by the authors, to make readers like me comfortable in this environment. 

The only concept that I found hard to grasp is legibility, and I would suggest the author to revisit that definition. Besides that I think the authors did a good job at addressing the core position.   

There are no specific actions suggested in the paper, but this is consistent with the speculative  approach of the paper.

### Questions
I'd like to challenge the authors on how they would get started on a project like this. How would you design the implementation of a pilot project?

### Presentation
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This position paper argues that LLMs can make human meaning legible at unprecedented scale by enabling "thick description" rather than relying on "thin" numerical metrics. Drawing on anthropological theory (Geertz) and political science (Scott), the authors contend that current sociotechnical systems strip away cultural context essential for representing human meaning through standardized metrics. They propose using LLMs to automate generation and processing of thick descriptions that preserve contextual information. The paper identifies five key challenges: preserving context, maintaining interpretive pluralism, integrating lived experience with critical distance, distinguishing qualitative content from quantitative magnitude, and acknowledging meaning as dynamic. Examples span healthcare, education, and sustainability domains.

### Strengths
The paper is exceptionally well-written and shows strong theoretical depth. It tackles a fundamental problem in representing human meaning in computational systems, offering a novel integration of ideas from anthropology and political science. Examples from multiple domains clearly illustrate the limitations of thin metrics. The five challenges are well defined and paired with thoughtful responses. Alternative perspectives and potential risks are addressed thoroughly. The interdisciplinary approach provides valuable insights for the ML community, and the position is clearly stated and persuasively argued.

### Weaknesses
- Lacks empirical examples or case studies demonstrating the practical utility of SMF in actual ML/NLP system design.
- The critique of computationalist approaches sometimes relies on strawman formulations, missing more nuanced defenses from recent literature.
- Limited engagement with cognitive science work that bridges symbolic/statistical models and embodied/situated perspectives.
- Practical implementation pathways for SMF are vague, leaving unclear how designers and engineers should operationalize these ideas.
- Evaluation criteria for “meaning alignment” remain abstract and not reproducible across domains.
- The argument is ambitious but risks alienating practitioners due to its heavy reliance on theoretical framing without actionable guidance.

### Questions
How would you empirically validate that LLMs can produce thick descriptions that accurately capture cultural meaning comparable to human experts? What would concrete pilot implementations look like across the domains you discuss, and what metrics would demonstrate their effectiveness without falling into the same traps as thin descriptions? How do you reconcile the need for interpretive pluralism with the practical requirements of actionable representations in computational systems?

### Presentation
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors contrast thin and thick descriptions, and then argue that LLMs can be used to make thick descriptions legible at scale. Crucially, legible is a term of art -- it was introduced by Scott (1998) to initially describe the what kinds of information can be processed by a political state.

### Strengths
Clearly written, well explained. The paper introduces the concept of thick descriptions to an audience that is likely not familiar with thick vs thin descriptions. Several examples are given and key issues are raised.

### Weaknesses
The paper does not address the key issue raised by the "legibility of meaning", in the sense of legibility as a property of how information is aggregated within a state. Namely, for information to be legible, it must be aggregated -- hence why thin descriptions are commonly used. 

The authors devote a whole section (section 4) to the difficulties in aggregating thick descriptions (meaning only exists in context, no single source of meaning, lived experience and critical distance are crucial, and what $\neq$ how much) but do not argue why or how LLMs are the appropriate tool to enable the aggregation of thick descriptions. Instead, the authors point out a few general uses for LLMs that are similar to the issues the authors rightly raise. For example, in 4.2 the authors state "Systems for representing meaning should maintain this plurality rather than collapsing diverse interpretations into singular representations" but only point towards recent work on using LLMs to identify dog whistles (a discriminative task) as a possible first step in supporting interpretative pluralism (an aggregation task).

### Questions
1. If the key problem with the legibility of thick descriptions is their aggregation so that they can be processed by a sociotechnical system (e.g. a political state), why do you believe that LLMs can aggregate thick descriptions? 
2. Related to Question 1, throughout the paper LLMs are referenced, but not described. What description of an LLM leads you to believe that what is argued is possible? As the paper currently reads, LLMs are treated as magic, not a tool to be used to solve a problem raised. 
3. More generally, chatbots and the LLMs that support them have been described as "mansplaining as a service". This is anathema to lived experience and critical distance. Why do you believe these tools could work for thick descriptions?

### Presentation
3
