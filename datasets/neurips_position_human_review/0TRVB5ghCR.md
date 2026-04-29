# Position: Why is plausibility surprisingly problematic as an XAI criterion?

- Decision: Reject
- Scores: 1, 7, 7

## Abstract
Explainable artificial intelligence (XAI) is motivated by the problem of making AI predictions understandable, transparent, and responsible, as AI becomes increasingly impactful in society and high-stakes domains. The evaluation and optimization criteria of XAI are gatekeepers for XAI algorithms to achieve their expected goals and should withstand rigorous inspection. To improve the scientific rigor of XAI, we conduct a critical examination of a common XAI criterion: plausibility. Plausibility assesses how convincing the AI explanation is to humans, and is usually quantified by metrics of feature localization or feature correlation. Our examination shows that plausibility is invalid to measure explainability, and human explanations are not the ground truth for XAI, because doing so ignores the necessary assumptions underpinning an explanation. Our examination further reveals the consequences of using plausibility as an XAI criterion, including increasing misleading explanations that manipulate users, deteriorating users' trust in the AI system, undermining human autonomy, being unable to achieve complementary human-AI task performance, and abandoning other possible approaches of enhancing understandability. Due to the invalidity of measurements and the unethical issues, this position paper argues that the community should stop using plausibility as a criterion for the evaluation and optimization of XAI algorithms. We also delineate new research approaches to improve XAI in trustworthiness, understandability, and utility to users, including complementary human-AI task performance.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This position paper argues that plausibility (i.e., how convincing AI explanations appear to humans) should not be used as a primary criterion for evaluating explainable AI (XAI) algorithms. The authors demonstrate that optimizing for plausibility increases "misleading explanations" (convincing explanations for incorrect predictions), which manipulate users, erode trust, and prevent effective human-AI collaboration. Instead, they propose using plausibility as an intermediate measure to assess XAI's specific intended purposes rather than as an end goal, emphasizing that human explanations should not serve as ground truth for XAI evaluation.

### Strengths
I apologise in advance but this paper has modified the latex template and hence I feel it should not progress to the reviewing stage. To treat it otherwise would be unfair to the other submissions.

The section headings (e.g., the Introduction) have not enough white space above them, this happens a lot throughout the paper.

Anyone who compares Page 1 to any other submission will see what I mean, it is quite obvious. 


### Nevertheless, here are the paper's strenghts in my view:
The paper argues addresses an important topic, and argue against the use of plausibility as a primary evaluation criterion. The position is articulated clearly, supported by theoretical analysis, illustrative examples, and references to prior literature. The authors also propose constructive alternatives, such as using plausibility as an intermediate measure tied to specific user-oriented purposes, and provide mathematical conditions for complementary human–AI performance, which could guide future research.

### Weaknesses
The core argument that plausible explanations are not necessarily correct may be viewed as intuitive, and not that interesting of a position. 

Plausibility is after all badly defined.

### Questions
How do you explain the formatting issues?

### Presentation
2

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The paper considers plausibility for XAI, and argues strongly against and suggests elimination entirely.  This includes discussion, referencing examples, theory, and experiments.

### Strengths
Provides specific position(s) on use of plausibility for XAI, and argues forcefully in various ways for this, considering examples from literature, theory, and experiment.

Paper provides in depth discussions and is well referenced.  

Relates plausibility to other XAI criteria such as transparency.

Extensive appendix includes Theorem proofs, experiments, and more.  

Figure 1 encapsulates much of the papers arguments in a well conceived and clear way.

### Weaknesses
Seems to boil down to the fact that a plausible explanation is not necessarily a correct one.  To the reviewer this seems pretty obvious (although the paper presents a lot of evidence that this is apparently not true across the ML community!).  

For a position paper, perhaps much of the appendix is better in a 'technical' paper track (??).  

Section 3.3.1:  It seems there may be some tradeoffs in XAI performance and overall AI performance, e.g., AI architecture.  

Theorem 1: should say in body of paper what is the model and key assumptions and conjecture 1 (which is a strong questionable assumption).

Conclusion: call on the community to stop using plausibility as **the** XAI criterion. Nevertheless, with sufficiently defined metrics, and sufficiently educated users, it might be used as one of several ways to understand an AI output.  But clearly plausibility alone is insufficient. 

Paper doesn’t consider advanced uses of AI as an assistant, and focuses on one-time binary decision problems.  However, AI is becoming an interactive tool, able to provide multiple possible solutions, enable iteration with a user including querying, provide for ‘insufficient evidence’ type conclusions, and provide confidence and error metrics.

### Questions
Why is the title a question and not a position? (Yes, the reviewer is answering a question with a question in a moment of lightheartedness.)

Is eqtn (1) the only way to define plausibility in the AI context?

Perhaps instead we should ask 'why is that plausible' in an interactive-adaptive context?  

Is much of this down to different definitions of plausible, and especially different engineering-quantifiable measures versus semantic-verbal definitions?

Theorem 1, conjecture.  How does a human only judge plausibility without also judging probability of correctness (or at least biased by this)?

### Presentation
3

---

## Human Reviewer 3

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The paper argues that plausibility (defined by how similar an AI explanation is to a human explanation) should not be used to optimize and evaluate XAI algorithms. The main reasons are: 1) Human explanations are not the ground truth for XAI, so plausibility is invalid to measure explanability. 2) Using plausibility as an XAI criterion destroys trust, manipulates users, and cannot achieve complementary human-AI performance. 3) Plausible features are a sufficient but not necessary condition of understandability, so focusing on plausibility ignores other possibilities of enhancing understandability. The authors then suggest that instead of using plausibility as an end, researchers should use it as a means for other purposes, such as decision verification and bias detection.

### Strengths
The paper addresses an important topic that is very relevant to the XAI community. Evaluation criteria guide the future direction of the XAI field, so this topic is worthy of discussion at the conference.

The paper's arguments are well-supported by proofs and evidence, including the comprehensive appendices. The opposing opinions are thoroughly addressed and refuted. The presentation is clear. The examples and figures help illustrate the idea, and the authors provide the necessary definitions and background information, making the paper accessible to a wider audience.

### Weaknesses
In the paragraph starting on line 85, Reason 5, 7, and 8 of the alternative view do not have citations. I am wondering whether there are papers that advocate for those reasons.

### Questions
In the abstract, the authors explain plausibility as "how convincing the AI explanation is to humans." Then, the formal definition given in section 2 is $P = \text{similarity}(E^\text{human}, E^\text{AI})$. I am wondering whether the similarity between an AI explanation and a human explanation is the only factor affecting how convincing the AI explanation is to humans.

### Presentation
4
