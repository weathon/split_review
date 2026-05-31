## Human Reviewer 1

### Summary
This work presents an adaptive tutoring framework consisting of two stages, integrating collaborative cognitive diagnosis with dynamic instructional adaptation. The first stage aims to model the student’s cognitive state through collaborative cognitive diagnosis. The teacher utilizes a successor-first method to efficiently generate diagnostic questions, ensuring their accuracy through an expert-assistant-verifier pipeline. In the second stage, based on the estimated cognitive state, the teacher uses slow-thinking-based methods to select teaching strategies from a strategy pool to guide the student in solving problems.

### Strengths
1. The entire framework is meaningfully designed and the authors present the prompt design clearly. 
 
2. The authors present a systematic evaluation by comparing with baselines in cognitive diagnosis and adaptive tutoring, with ablation studies in different modules and backbones. 

3. Several case studies and deeper analysis regarding the effectiveness of this framework in specific education scenarios.

4. The related work presents necessary background for readers to understand the context.

### Weaknesses
1. Unclear model design rationale. It is unclear what the unique strength of this proposed model is and why it should be, compared with prior models. The introduction and related work sections briefly stated that prior work can not do something, but the detailed research gap and how this work addressed such gap are unclear.

2. The current framework is meaningful, but there is no fundamental breakthrough or unique insights in algorithms or model side. It is more like a manually crafted application system in education with prompt-engineering.

3. Dataset Scale. There is only one dataset with only 184 questions. 

4. The main experiment used simulated students for evaluation, which does not seem to be convincing. It is also unclear how many simulated students were generated, the differences among the simulated students, and rationales for such design. Without such details about student settings in the experiment, it is hard to evaluate the rigor and effectiveness of this work.

5. Lack of statistical tests (such as t tests) for most tables to show the significance.

6. Main Experiment: The experimental measurements may not really support the claimed contribution in line 107: "stimulating critical thinking". Which metrics measure how the tutoring system improves the critical thinking of students in either simulation or real student study?

7. Real Student Experiment: 

The real student experiment is unclear and does not look like a formal study. Is it a between-subject design or within-subject design or a mixed study design? 

For this statement: "one of six tutoring methods is randomly selected (with equal probability) to tutor the student", does it mean that each student only receives one tutoring method (between-subject design) or each student receives different tutoring method for different questions? If so, how do you control so many human factors like different students in different questions with different tutoring methods? If one question is delivered to different students in different tutoring methods, how do you know the result difference is due to student subject difference or due to the tutoring method difference? 

Participant scale and limited samples: So many human factors usually need larger-scale user study rather than N = 67. The authors can report the power via power analysis to show the statistical significance with the current participant number. Moreover, for this statement "The student who selected the most questions chose 12, while the student who selected the
fewest chose 2", does it mean that each student only tested 12 questions at most? This limited sample size is probably not convincing to show its effectiveness.


Study design and metrics: Another concern is that the current study design and metrics may not really support the claim of enhancing tutoring performance. Most metrics are subjective (e.g., Appropriateness, Sentiment, Inspiration) and do not provide a very objective measurement. The success rate may be better quantified and more convincing, but Pelican's success rate (87%) is lower than simple step-wise methods (87.3%).


Minor Issues:

There are some typos.

### Questions
Please check my concerns and questions in Weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper proposes an adaptive tutoring framework called PELICAN, which is designed to address the limitations of existing LLMs in personalized education. It achieves student-centered teaching through a two-stage process: collaborative cognitive diagnosis and dynamic instructional adaptation. Specifically, it first organizes knowledge points into a hierarchical dependency structure and then conduct CD to get student's cognitive state. Then, the teaching strategies are dynamically selected from "fast thinking" and "slow thinking" modes based on the diagnostic results. Experiments conducted on GAOKAO bench demonstrate the effectiveness of the proposed framework.

### Strengths
1. The proposed 2-stage personalize education framework is well-defined and reasonable, and the introduction of dual system in stage-2 is convincing and fitting the problem well.
2. The experiments on GAOKAO Bench is comprehensive, effectively demonstrates the superiority of the proposed PELICAN.
3. The writing and structure of this paper are clear and easy to understand.

### Weaknesses
1. In my understanding, the construction of knowledge tree may heavily relies on manual work, which may hurts the scalability of the proposed framework. For example, scaling to full K12 education or vocational education would lead to a sharp increase in manual costs.
2. The evaluation limits to only 1 benchmark (GAOKAO Bench), it will be more convincing if authors validate PELICAN framework on more benchmarks.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
6

### Confidence
2

---

## Human Reviewer 3

### Summary
The authors introduce PELICAN: a way to personalize education utilizing both LLMs and cognitive diagnosing. The LLM utilizes cognitive diagnosis to identify appropriate responses tailored to the student's cognitive level and understanding. Each problem has different knowledge components that the student must master and these are organized into a hierarchical structure. Based on this knowledge state, the adaptive tutoring will select an appropriate response to solve problem p with the student via dialogue. If the number of dialogue rounds with a student exceeds a threshold M, it is assumed that they are facing persistent cognitive obstacles, and slow-thinking is enabled to focus on smaller subproblems. The authors tested their method on the public Gaokao dataset, as well as a real-world study involving high schoolers.

### Strengths
The paper is well-motivated, with a clear introduction, and is overall easy to follow. I also think the figures are well-made and help aid the explanation of the ideas and methodologies. The appendix is thorough.

### Weaknesses
Overall, the paper lacks deep substance and novelty. It is more of an applied research paper, but it lacks statistical rigor (e.g., ANOVA tests, effect sizes, p-values). It could become more interesting and impactful with greater care and attention to detail for deeper results, analysis, and presentation, etc. However, I also don't find it to be a great fit for ICLR and don't think the audience of ICLR would be interested in this topic. This paper appears to be more closely aligned with AI applications in education venues, such as AIED, EDM, and EAAI, among others, once it has been improved. I have little to specifically point to in a critique of it, other than that it is a limited-scope paper that utilizes GPT models for teaching. This also raises concerns about the future reproducibility of the reported results. It is very time-specific and niche.

Abstract:
* Have LLMs really generated attention in education because of their extensive knowledge base and reasoning capabilities?
* Extra space between "at" and "here" for code reference.

Introduction:
* Change "I Don't understand" to "I don't understand" in Figure 1
* Add spacing: "OK,I get it!" between "OK," and "I" in Figure 1
* First two paragraphs need citations to support their various claims
* Parentheses around citations are needed. In-text citation references are likely not the style for ICLR.
* Line 80: random word "Planning." appears
* Figure 3: Why does "Explanation" lead to "Explanation" in the slow-thinking? Why does "Decomposition" have a crown?
* Line 148: random word "Planning." appears

3.2: "introduce a successor-first strategy, in which the teacher prioritizes assessing leaf nodes or nodes whose successors have already been evaluated," I thought line 175 said "a student can only master a child node after mastering its parent"?

3.3: "dual system theory" citation? lines 215, 246

Line 264: Is this what you are proposing? Simulated teaching tree? Or is that something that already exists in the literature?

Line 270: Does m = |S| (i.e., the length of the strategy pool)? If not, why?

Section 3: The formulas seem overly high-level to the point of being complete black boxes with no reproducibility

Section 4: Reporting overhead in cost of dollars? Maybe should use something more concrete, like token usage.

Section 4: Why not cite baseline methods?

How are suitability, logicality, informativeness, reliability, and overall quality calculated in the results?

The real-world experiment sounds limited. What is the average and standard deviation for the problems that the students voluntarily selected to be tutored? And what was the distribution like amongst the 6 conditions? Why no ANOVA test results?

Line 1314 in Appendix L.4.: "FIANL" should be "FINAL"

### Questions
* Have LLMs really generated attention in education because of their extensive knowledge base and reasoning capabilities?

* Figure 3: Why does "Explanation" lead to "Explanation" in the slow-thinking? Why does "Decomposition" have a crown?

3.2: "introduce a successor-first strategy, in which the teacher prioritizes assessing leaf nodes or nodes whose successors have already been evaluated," I thought line 175 said "a student can only master a child node after mastering its parent"?

3.3: "dual system theory" citation? lines 215, 246

Line 264: Is this what you are proposing? Simulated teaching tree? Or is that something that already exists in the literature?

Line 270: Does m = |S| (i.e., the length of the strategy pool)? If not, why?

Section 4: Why not cite baseline methods?

How are suitability, logicality, informativeness, reliability, and overall quality calculated in the results?

The real-world experiment sounds limited. What is the average and standard deviation for the problems that the students voluntarily selected to be tutored? And what was the distribution like amongst the 6 conditions? Why no ANOVA test results?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
The authors introduce PELICAN, a large language model–based tutoring framework to deliver personalized education. It is designed to give adaptive feedback to students. It has two primary components: cognitive diagnosis and adaptive tutoring. The cognitive diagnosis uses a hierarchy of concept knowledge graph and uses an expert–assistant–verifier to generate diagnostic questions. Adaptive tutoring creates explanations and strategies based on the diagnosed cognitive state. It uses a dual-system strategy: fast and slow thinking to tailor based on the necessity of student. By extensive experiments across synthetic and real students, the authors show that PELICAN can be highly effective for LLM-driven personalized tutoring that mirrors human pedagogical behavior.

### Strengths
The primary strength of the paper lies in the clarity of its presentation. The authors take an intuitive idea to adapt LLMs to humans and show such system can work in practice. The two major components in PELICAN have been clearly written and motivated. The authors explain the importance of each and every component in the training pipeline. For example, the cognitive modeling component uses a hierarchical knowledge tree, with a well-defined curriculum that traverses from the leaf to the root. In order to ensure robust question quality during diagnosis, Expert–Assistant–Verifier Pipeline. Finally, the authors explain the importance of both short and fast thinking in adaptive tutoring and how they are decided based on the diagnosed cognitive state. By clearly showing improvements on both synthetic and real world students, the authors show the efficacy of their proposed tutoring sysem.

### Weaknesses
As such, I don't have many concerns with the paper. Please find some of my questions regarding the experiment setup.

a) How fine-grained are the knowledge concepts in the hierarchy? Furthermore, does the system allow more granularity in the concepts, depending on the student?

b) The expert-assistant-verifier pipeline depends on the accuracy of the two LLMs involved. Do the authors conduct ablations on what fraction of the diagnostic questions are noisy? And how much is the performance of PELICAN affected by the noise?


Furthermore, the authors should discuss on the diversity of the students involved in the human study. More than just performing well, did the students also report favorable experiences when interacting with LLMs? For example, a hyperparameter that can be controlled is M, which controls the number of times the LLM switches from fast to slow thinking. Is M decided based on whether the student progresses in the problem?

### Questions
Please see above for my questions.

### Soundness
4

### Presentation
4

### Contribution
4

### Rating
8

### Confidence
4