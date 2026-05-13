# Strategic Filtering for Content Moderation: Free Speech or Free of Distortion?

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
User-generated content (UGC) on social media platforms is vulnerable to incitements and manipulations, necessitating effective regulations. To address these challenges, those platforms often deploy automated content moderators tasked with evaluating the harmfulness of UGC and filtering out content that violates established guidelines. However, such moderation inevitably gives rise to strategic responses from users, who strive to express themselves within the confines of guidelines. Such phenomenons call for a careful balance between: 1. ensuring freedom of speech --- by minimizing the restriction of expression; and 2. reducing social distortion --- measured by the total amount of content manipulation. We tackle the problem of optimizing this balance through the lens of mechanism design, aiming at optimizing the trade-off between minimizing social distortion and maximizing free speech. Although  determining the optimal trade-off is NP-hard, we propose practical methods to approximate the optimal solution. Additionally, we provide generalization guarantees that determine the amount of finite offline data required to effectively approximate the optimal moderator.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work studies the problem of social media regulation, where the platform would like to design guidelines in order to minimize users' engagement with harmful social trends, but also minimizing suppressing freedom of speech that would result from unnecessary content removal. This is done by the designer committing to a content moderator, which the users observe. Specifically, this work models this as a constrained optimization problem where the designer has the goal of minimizing social distortion, which they define as the average distance between the users' original content and the manipulated content. The authors provide sample complexity and hardness results: They show that for a sufficiently large set of samples, we will obtain consistent estimates for average social distortion for any filter class. Furthermore, they show that even for a class of linear filters, finding a filter that minimizes average social distortion while filtering out at most k content is NP-hard. They present an empirical approach to approximately compute the optimal filter by relaxing the freedom of speech violation constraint. ,

### Strengths
* This paper is well-written and easy to follow. 
* Social media regulation is a timely and well-motivated problem. 
* The technical formulation of such a problem is interesting and one that would be great to see studied more by the ICLR community.

### Weaknesses
It's difficult to see where the main strength of this paper is, and I would encourage the authors to bring this out more. If the novelty is how the social media regulation problem is motivated, then it would help if the authors contrasted this with other such technical papers and highlight either (1) the new practical insights that arise from this paper or (2) the new technical insights. From looking through the related works discussion on strategic classification and constrained optimization, it is not clear that the latter is the main strength of the work. Could the authors address this concern? 

Relatedly, I was not clear on the experimental results section. The level of relaxation the authors suggest may be impractical. Could the authors include more discussion on why this is not the case if so?

### Questions
See weakness section above.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
* The paper proposes a strategic classification model aimed at reducing harmful social trends.
* In the model, users interact with a content moderation system, and strategically adjust their created content in response to moderation policies. Each user is characterized by a feature vector $x$ and a manipulation cost parameter $c$. The system applies a “harmfulness score” function $f(x,w)$, and content is flagged as benign when $f(x,w)\\le 0$. In response to $f$ and in face of a social trend represented by a vector $e$, the user reports a manipulated feature vector $z^*=\\mathrm{argmax}_z \ \\mathbb{I}[f(z)\\le 0] \\cdot z^T e - c|z-x|^2$. The decision boundary induced by the content moderation rule $f$ is assumed to be convex with respect to benign content.
* The goal of the system designer is to find an acceptable tradeoff between “social distortion”, which is defined as the distance $|x-z^*|^2$ for feature vectors $x$ which were originally considered as benign (Definition 1), and “freedom of speech”, defined as the proportion of feature vectors considered by the system as benign. 
* Theorem 1 presents a learnability result for distortion-minimizing classifiers under freedom of speech constraints. These sample complexity upper bounds are shown to hold for natural hypothesis classes (Proposition 3). The hardness of finding optimal linear classifiers is established by Theorem 2. Section 6 presents a differentiable relaxation of the optimization objective, and analyzes performance on a synthetic dataset.

### Strengths
* The paper is addressing a problem of high social significance.
* Learnability and hardness results are interesting, and helpful intuition is provided.
* The differentiable relaxation of the optimization problem has potential to facilitate more practical applications.

### Weaknesses
* The problem setting relies on assumptions which may not hold in practice, however the paper does not explicitly discuss or address these limitations. In particular:
  * Definition 1 appears to suggest that the system could label all content as benign. However, in practice platforms often face legal or policy constraints requiring the removal of certain content (e.g., the EU Digital Services Act, or the YouTube Community Guidelines). In such cases, full freedom of speech may not be feasible, which could undermine assumptions such as the convexity of the decision boundary induced by the score function $f$, the feasibility of the trivial moderator $\\perp$, and the relevance of the optimization objectives.
  * Assuming that the social trend can be identified and quantified, and assuming that there is a single social trend.
  * Additionally, the choice of strategic manipulation in Equation (1) and the definition of social distortion lack sufficient justification—particularly in the use of the $L_2$ norm and the inner product with the trend vector. Clarifying the practical or technical motivations for these choices would be valuable.
* Experiments are only performed on synthetic datasets.
* Formatting problems:
  * Text in Figure 3 is too small to read.
  * Equation (14) overflows beyond the text area boundaries.
  * Notations in Figure 1 (Right) are unclear.
  * Confusing notation - If I understand correctly, in Section 6.1, $\\mathbf{c}_i$ seems to indicate Gaussian mixture centroids, and $c_i$ indicates the cost coefficient?
  * Real numbers are denoted by $R$ in L132, but denoted as $\\mathbb{R}$ in L146
  * “Subsection-style” formatting in L141 vs “paragraph-style” formatting in L152
  * $f$ is defined as a function of $x,w$ in L146, but defined as a function of $z$ only in L157.

### Questions
* What are the implications of the platform having obligations to remove certain types of content?
* How does the model handle multiple social trends occurring simultaneously?
* In Section 6.1, is it possible to estimate the difference between the globally optimal classifier, and the classifier obtained using the differentiable relaxation?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper considers a model of a social media platform where users modify their content to align with trends on the platform. For those trends that are harmful, the platform would like to adopt a content moderation policy that disincentivizes user modification of content to conform to trends while also maintaining user participation on the platform. The paper considers both the computational complexity of designing such policies, and also the sample complexity required to do so from finite data.

### Strengths
The design of content moderation policies is a topic of central concern for online platforms, and it is very sensible to take users' strategic behavior into account when designing these policies, particularly the way in which users will modify their content to align with ongoing trends.

### Weaknesses
It seems useful to highlight four sources of concern. 

- First, while the results make sense in the context of the model that has been presented, the paper never really returns from the formal model back to the high-level issues that motivated the paper. At a high level, beyond the specifics of the model, what did we learn about content moderation in the face of strategic behavior and harmful trends? Were there qualitative insights that a content moderation group at a large platform could take away from the results? 

- Related to this, the paper provides a discussion of the literature on strategic classification, but it would also be important to discuss how the current model captures key features of online content creation and content moderation as a particular domain, rather than just the problem of strategic classification in general. As written, it's not clear why the model couldn't be cast much more generally as being about an arbitrary instance of strategic classification (e.g. students writing college applications, or job applicants submitting resumes) rather than about the creation of online content specifically. Of course, if there are new contributions being made more generally to strategic classification as a whole, that would be a good argument for the paper to make, but either way, it should make clear what about the model is specific to content creation and content moderation. 

- In contrast to the survey of strategic classification, the paper does not really discuss the earlier literature on adversarial information retrieval, which is directly concerned with content creators who strategically modify their content, and with the responses of platforms to this strategic behavior. It would be important to explain the relationship to this earlier literature; see for example the survey by Castillo and Davidson: Castillo, Carlos, and Brian D. Davison. "Adversarial web search." Foundations and trends in information retrieval 4, no. 5 (2011): 377-486. 

- Finally, there's something a bit unusual about the way the authors invoke the concept of "freedom of speech": it appears from the exposition that the paper views a violation of free speech to have occurred when (a) a user leaves the platform, but not when (b) a user produces speech different from what they would optimally like to say due to platform policies. But the law tends to view scenario (b), in which a policy compels you to say things differently from how you'd like to say them, as also being a violation of free speech. Of course, the platform is not the government, and so in all these cases we're talking about restrictions on speech imposed by a private actor, which are always evaluated differently than restrictions imposed by the government; some would argue that "freedom of speech" should only be used when referring to restrictions that carry the force of law as imposed by a government. For all these reasons, the paper may want to use different terminology that would run into fewer of these definitional problems; for example, part (a) above could arguably be said to be more about participation.

### Questions
It would be helpful if the authors could address the weaknesses listed above.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper addresses content moderation on online platforms, focusing on how users may adapt their posts to align with harmful trends in pursuit of virality, even if this means compromising their genuine beliefs. The platform aims to implement a content moderation filter that blocks harmful content while minimizing the "distortion" between users' true beliefs and the content they share publicly. This filtering is constrained to ensure that only a limited fraction of users are banned, keeping within a target threshold.

### Strengths
1) I appreciate that the paper tackles the problem from both a "sample" and "time" complexity perspective, alongside experimental results. This makes the paper well-rounded. 
2) I believe it is an important and timely topic. The paper took a principled approach in studying it.

### Weaknesses
Unfortunately, I think that the paper made some overly-stylized decisions when studying the problem that were not properly motivated. My main concern is the following: 
In the definition of social distortion (Defition 1) on the paper, the distortion is zero if the deployed content moderator would qualify the original content x as non-benign. So, unlike in the strategic classifying literature, there is no notion of "true label", instead the "true label" is in some way defined by what the chosen classifer/content moderator would decide. 
The authors try to motivate this decision, but for me this is quite problematic. Let me give an exampe as to why: 
The distribution of true content x is a point mass distribution at (0,0), and the trend e is at (1,0). The cost c is such that z' = x + e / 2c is somwhere in the [0,1] x-axis. 
The estimator that qualifies all points as benign would have the maximum possible social distortion, as stated in proposition 2. 
Now, consider the estimator that quantifies the point (0,0) as non-benign, and has the decision boundary in (0 + \epsion, 0). 
This estimator induces exactly the same "movement" by the users, but it has a social distortion of 0, which is the best possible.

Thus, this means that the estimator can "minimize" the objective function of your problem not by "reducing distance" from original labels, but by "gaming the system" around the labels it assigns to the "original points x" 

If the authors address this remark, I would change my score on the paper. 


Minor concerns: 
1) "We focus on moderators f that induce convex benign regions. This assumption is motivated by the natural property that if two pieces of content are benign, their linear combination should also be benign in the feature space."
Is this actually true? It is not obvious to me that either for text or image embeddings this is true. I would either provide citations for it, or weeken the statement.

### Questions
1) I would try to better motivate your choice of objective. I think the approach that the paper took is very good, but I have serious concerns with respect to the given definition of social distortion. Was there a specific reason for which you opted to define SD = 0 if the current estimator defines the true content as benign, as opposed to "if the current content is objectively benign"?
2) What would change in the analysis of the paper if you made that change? 
3 If I understand correctly, theorem 1 is a union bound over 2 unlikely events: Pollard's theorem for the sample complexity of classifiers and the standard VC generalization result. Given how standard these results are, I would frame it as a lemma, not a theorem.

### Soundness
2

### Presentation
3

### Contribution
2
