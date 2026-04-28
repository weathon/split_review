# Procedural Fairness Through Addressing Social Determinants of Opportunity

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5

## Abstract
_Social determinants of opportunity_ are variables that, while not directly pertaining to any specific individual, capture key aspects of contexts and environments that have direct causal influences on certain attributes of an individual, e.g., environmental pollution in an area affects individual's health condition, and educational resources in an neighborhood influence individual's academic preparedness. Previous algorithmic fairness literature often overlooks _social determinants of opportunity_, leading to implications for procedural fairness and structural justice that are incomplete and potentially even inaccurate. We propose a modeling framework that explicitly incorporates _social determinants of opportunity_ and their causal influences on individual-level attributes of interest. To demonstrate theoretical perspectives and practical applicability of our framework, we consider college admissions as a running example. Specifically, for three mainstream admission procedures that have historically been implemented or are still in use today, we distinguish and draw connections between the outcome of admission decision-making and the underlying distribution of academic preparedness in the applicant population. Our findings suggest that mitigation strategies centering solely around protected features may introduce new procedural unfairness when addressing existing discrimination. Considering both individual-level attributes and _social determinants of opportunity_ facilitates a more comprehensive explication of benefits and burdens experienced by individuals from diverse demographic backgrounds as well as contextual environments, which is essential for understanding and achieving procedural fairness effectively and transparently.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper discusses the consideration of "social determinants of opportunity" such as geographical locations for algorithmic fairness.

### Strengths
The discussion of the actual effects of different approaches to achieve "fairness" is discussed, which is often not considered enough in our field.

### Weaknesses
First of all, I am not sure if this conference is a good fit for this paper/topic since it is from my perspective hardly at all concerned with "learning representation". It is more a general societal consideration about how fairness could be achieved.

While the claim of the paper is to discuss the "social determinants of opportunity" in general, the discussion focusses very much on a single use case, i.e., university admissions.

The paper is written in a very US-centric way, specifically considering the legal situation.

The case considerations in Section 4 often (e.g., Section 4.3.) come to conclusions that are quite trivial. E.g., that taking the top-x % per region increases the share of "weaker" regions was literally my first thought. The accompanying formulas appear to just make a trivial insight more sophisticated.

The authors should more critically reflect on their approach. For example,
(i) even if "academic preparedness" is caused by certain external factors, isn't academic preparedness still a key factor to a succesful university curriculum? If someone is not well prepared for university, they should not be admitted - that should be at the core of all admission procedures
(ii) the legal implications of adjusting for "social determinants of opportunity" should be considered, specifically if this correlates with sensitive attributes such as race. 
(iii) trying to form groups again beyond sensitive attributes - again - introduces new sources of unfairness. For example "poor" students growing up in "rich" regions. Also, if this kind of admission procedure would gain traction, it would also be possible to trick procedures, e.g. for "rich" people renting temporarily to appear to be from a "poor" region.

The assumptions in the paper appear to be somewhat arbitrary. E.g., why assume the gamma parameterization in 4.3., and how is this justified?

The writing of the paper should also be improved. For example, what is the purpose of Section 2.1. For the contents of the paper?

### Questions
What are the authors thoughts of the critical reflection of the approach (see weaknesses)?
Why is this paper a good fit for specifically ICLR?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper develops a model of the interactions between ethnicity, academic preparedness, and "social determinants of opportunity", which capture socio-geographic influences on academic preparedness. The model is used to study different college admissions policies both in theory, and applied to a dataset of UC Berkeley admissions.

### Strengths
The paper is clearly arranged and easy to follow. This paper is also laudable for trying to raise the salience of geographic and community influences on opportunity over a reductive focus on ethnicity.

### Weaknesses
Ultimately, the theoretical results in this paper do not provide novel insight, and the empirical results aren't very interesting or plausible. The model is used to show that:

1. Quota-based affirmative action harms disadvantaged members of majority groups.
2. "Plus factors" for being from an underrepresented group benefit advantaged members of that group more than disadvantaged members.
3. "Top-percent" policies that are blind to ethnicity reallocate opportunity to regions with less of it.

All three of these findings are well-known, and have been part of the debate around these policies for decades. The model doesn't provide extra insights into these policies. 

When the model is deployed on real data, it also doesn't provide insights. It seems as though the admissions data from Berkeley is too censored to study the impacts of social determinants of opportunity, since it doesn't include anything about an applicant's geography beyond whether they are in-state. The regions inferred by the model don’t make a lot of sense given what we know about California’s ethnic geography (eg they don't show any signs of the racial segregation induced by California's restrictive housing policies).

### Questions
Are the regions in the experiment latent? Region 1 and 3 are almost identical, calling into question the identifiability of the model. Also, if regions don’t correspond to geographies or social networks then how can they capture social determinants of opportunity? 

Notes:

> “Specifically, by definition of causality, this edge asserts that there is a difference in the distribution of education status, when we “intervene” on individual’s race while keeping all other things unchanged”

“all other things” meaning every other variable in their causal graph, not literally every other possible thing. Since these graphs typically only use a handful of features, I don’t think this edge is an endorsement of racial essentialism - it just summarizes dozens of effects that the model is too coarse to model explicitly.

>“If a certain edge or path in the causal model does not reflect an actual real-world causal process, subsequent causal fairness analyses based on causal effects may not provide informative conclusions.”

This is certainly true, but to my knowledge not a single causal graph in history has ever actually described a real-world causal process where humans were involved. It’s extremely difficult to establish single treatment effects, let alone a network of them.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work explores incoporating the concept of social determinants of opportunity, variables that relate to an individual's academic success causally and potentially implicitly. The authors deviate from past work by modeling implicit relationships between these variables rather than simplified relationships and futher explore adding previously omitted variables. Then, framing academic preparedness as an optimization problem, the authors find a correlation between race and social determinants of opportunity, using GPA as an estimation of academic preparedness and analyzing data from the University of California's admissions data. As an analysis of existing data, this work proposes modeling protected characteristics and studying the influence of contexts and environments on the individual for fairness analysis.

### Strengths
The authors seek to model fairness in college admissions by disentangling variables that implicitly model each other, which provides an interesting framework for considering the intersectionality of factors that influence an individual. When applied to college admissions and academic preparedness, the authors provide a convincing argument for abstracting out social determinants of opportunity and studying the underlying framework and its impact on the individual. Further, the authors demonstrate various applications of their framework in Section 4 in studying historical admissions systems.

### Weaknesses
While there are limitations in studying observational data, this paper could have benefitted from a further analysis of the University of California dataset; the authors do acknowledge the limitations of summary statistics but further discussion of the dataset and analysis on other datasets could have provided more support to the experimental section of this paper. The authors briefly discuss their experimental findings but the three separate graphs in Figure 3 could have benefitted from further discussion, particularly in relation to each other and how the correlation between race and social discriminators of opportunity correlates with understanding academic preparedness in a region. Potentially interleaving the methods and providing experimental results for the modeling of past admissions systems could have provided more tractable examples of how this framework compares to prior work.

### Questions
How does modeling University of California admissions data via the presented framework differ experimentally from past methods? What are possible extensions of this framework in developing more holistic admissions systems? A theoretical analysis of what this kind of admissions system could look like could provide further insight into the extensions of this model.

### Soundness
3

### Presentation
3

### Contribution
2
