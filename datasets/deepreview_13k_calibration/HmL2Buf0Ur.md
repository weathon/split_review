# Can Copyright be Reduced to Privacy?

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3

## Abstract
There is a growing concern that generative AI models will generate outputs  closely resembling the copyrighted materials for which they are trained.  This worry has intensified as the quality and complexity of generative models have immensely improved, and the availability of extensive datasets containing copyrighted material has expanded. Researchers are actively exploring strategies to mitigate the risk of generating infringing samples, with a recent line of work suggesting to employ techniques such as differential privacy and other forms of algorithmic stability to provide guarantees on the lack of infringing copying.
In this work, we examine whether such algorithmic stability techniques are suitable to ensure the responsible use of generative models without inadvertently violating copyright laws. We argue that while these techniques aim to verify the presence of identifiable information in datasets, thus being privacy-oriented, copyright law aims to promote the use of original works for the benefit of society as a whole, provided that no unlicensed use of protected expression occurred. These fundamental differences between privacy and copyright must not be overlooked. In particular, we demonstrate that while algorithmic stability may be perceived as a practical tool to detect copying, such copying does not necessarily constitute  copyright infringement. Therefore, if adopted as a standard for detecting an establishing copyright infringement, algorithmic stability may undermine the intended objectives of copyright law.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This article contends that it's crucial to recognize the distinctions between privacy and copyright. While algorithmic stability might seem like a useful method for identifying copying, it doesn't automatically ensure copyright protection. The authors pinpoint several discrepancies between algorithmic stability strategies and copyright regulations, illustrating why the implementation of such strategies might not fully consider fundamental copyright principles. Consequently, the paper suggests that if algorithmic stability techniques become the standard for addressing copyright infringement, they could undermine the original objectives of copyright law. The authors emphasize the necessity for any copyright concept to establish a clear distinction between protected expressions and unprotected ideas, highlighting a challenge that algorithmic stability concepts such as DP might not effectively address in certain cases. They provide instances where several elements of copyright law complicate the simplification of the copyright issue to a matter of privacy:
 - Copyright protections have a time limit, allowing works to enter the public domain after the expiration of protection. This implies that DP might be excessively stringent as a privacy notion. 
 - Copyright law excludes certain subject matter from protection as they serve as raw material for cultural expression, a factor not readily addressed by privacy considerations. 
 - Privacy protects content rather than expression, which differs from the scope of copyright law. 
 - Copyright law promotes the use of copyrighted materials through specific transformative uses, including quotations and parodies, a dimension not fully encapsulated by privacy concerns.

In summary, the paper prompts critical thinking on why DP and NAF fail to effectively address the copyright problem. However, it lacks a comprehensive proposal for a practical resolution.

### Strengths
- The work provides an in-depth discussion on the relationship between DP, NAF and copyright law. 
- The work studies a timely problem.

### Weaknesses
 **No constructive copyright notion**. Authors look at special cases when DP or NAF would be too strict of a copyright notion and a relaxed notion could yield more benefit. While these special use cases make sense (e.g., Copyright is limited in time; copyright law encourages the use of copyrighted materials for transformative use cases) the authors merely identify these use cases without providing a technical copyright notion that would help make a step towards a more realistic copyright notion. In my view, both DP and NAF already do a good job at ensuring copyright law is upheld. As the authors note, to claim that the output of a generative model infringes copyright, a plaintiff must: 
 1. prove that the model had access to her copyrighted work; and
 2. prove that the alleged copy is substantially similar to her original work.

Therefore, it is my understanding that any reasonable algorithm to ensure copyright, must either make sure that the model behaves as if it had no access to the copyrighted work or that the model makes sure that the generated output is dissimilar to the original work. In my understanding, (1) is guaranteed by DP and in doing that DP is quite conservative, e.g., copyright law does allow the output to be influenced by the original work if it is sufficiently dissimilar from the original work which DP prohibits. Another strategy can lie in simply making sure that the generated output is dissimilar to the original work. This is what NAF aims to achieve targeting point (2). To summarize, the work does not offer a constructive solution that helps solve these problems.

**Unclear theoretical results.** The theoretical results do not seem self-contained – e.g., to properly understand the paper, you must have read the work by Vyas et al (2023). Below are more concrete examples that are unclear: 
  - “The premise in the above theorem is identical to that in Theorem 3.1 in Vyas et al. (2023)”: Does this mean that the full premise is stated in Proposition 1 or should the reader look at Theorem 3.1 of Vyas et al (2023) to understand the full premise of Proposition 1?
  - Some terms are not properly introduced: e.g., what is a “sharded-safety setting”?
  - Proposition 2 is presented in section 2; but the discussion on its implications is provided in Section 4.
  - In Proposition 1, eta is not defined. What is eta?

### Questions
See above.

Authors should consider using \citep instead of \citet (most of the time).

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors examine two proposed computational measures, viz. differential privacy and Near Access Freeness, that have recently been proposed as measures that can be used to assess whether the generated content of a model counts as copyrighted content. The authors argue that neither of the measures constitute an adequate test of copyright infringement when considered within the context of U.S. legislation.

### Strengths
If correct, the authors conclusion significantly contributes to current research on assessing the copyright status of the generated content of a model. It shows that two recently proposed measures for this do not cohere with copyright as it is found in U.S. legislation. The comparison between the two disciplines is essential in developing computational measures that allow this assessment and, if correct, the discussion of the authors constitutes an original and important step in relation to this aim.

### Weaknesses
(1) The discussion is not sufficiently informed by the definition of copyright within U.S. legislation. It appeals to the goals of copyright legislation and to examples of what does and does not count as copyright according to the legislation, but not to the definition of copyright itself. The paper would benefit from a more precise engagement with the statutory language, specifically 17 U.S.C. § 102, which outlines the criteria for copyrightability. A deeper analysis of how the concepts of 'originality' and 'fixation' are interpreted in legal contexts would strengthen the arguments presented. The current discussion lacks a clear articulation of how these legal concepts relate to the proposed computational measures.
(2) In a few places, there is an inconsistency between claims. For example, on page two, the authors state that they will focus on challenges to providing a definition of copyright, while in Section 2, the focus is on algorithmic stability as a surrogate for copyright. These two are not the same, and will involve different implications and challenges. The paper should clarify whether it aims to address the definitional challenges of copyright directly or to evaluate the suitability of algorithmic stability as a proxy. The current framing creates ambiguity about the core objective of the work. The shift from a broad definitional discussion to a specific focus on algorithmic stability needs to be better motivated and contextualized.
(3) In many places, there are grammatical errors. For example, on page two, discussion is of Alice 'had she never saw' (vs seen) B. There are numerous instances of similar errors throughout the text, which detract from the clarity and professionalism of the paper. These errors make it difficult to follow the arguments at times and suggest a need for careful proofreading.
(4) Unless an unfamiliar referencing convention is being used, the format for citation and referencing needs to be corrected throughout.

### Questions
(1) How does the definition of copyright as it is found within U.S. legislation relate to your discussion?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper analyzes whether differential privacy (DP) and near access freeness (NAF) are sufficient to implement copyright law in ML models. DP is drawn from the privacy literature, and NAF is a recent copyright-inspired proposal that draws ideas from copyright to implement a kind of deliberate ignorance of specific training examples. The paper argues that some key notions in copyright, such as fair use and parody, are not adequately captured by DP/NAF.

### Strengths
The paper is legally informed and does a very good job applying legal doctrines. It includes a helpful discusison of recent caselaw and copyright scholarship, and the point made in section 4 about the limits of the NAF approach is very well-taken. The analysis in section 3 is particularly helpful in showing the ways in which these approaches can be both over and under-inclusive.

### Weaknesses
The writing is confusing. I had a hard time keeping straight over-inclusiveness, over-exclusiveness, under-exhaustiveness, stability, and safety. The paper could benefit from a careful pass to use consistent terminology.

I also think that the paper is discussing at least three kinds of issues: (1) whether there was copying in fact from a source work, (2) the quantitative degree of similiarity between an output and a source work, and (3) whether the use of a source work is justified in light of some approved legal purpose, such as parodic fair use or criticism. It is conceptually very difficult to separate (1) and (2), and the paper makes some attempts to clarify this line using DP/NAF, but I am not sure that it succeeds. On the other hand, (3) is very different and I am not sure that it is fair to critique NAF for excessive caution in saying that such examples have been copied. They have, and we currently lack computational tools to analyze whether the copying is justified.

### Questions
none

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper discusses the challenges and misfits of applying algorithmic stability approaches, such as differential privacy and near-access-freeness (NAF), to copyright disputes, with an emphasizes that while computer science methodologies, including algorithmic stability approaches, can assist policymakers in making more informed decisions, they may not be suitable for converting legal standards into rigid rules.

### Strengths
Strength:
1.	Discusses in details on the subtle differences between privacy and copyright 
2.	provides a thorough and comprehensive analysis of the challenges and misfits associated with applying algorithmic stability approaches to copyright disputes. 
3.	Critically evaluates the limitations and potential pitfalls of algorithmic stability approaches, such as differential privacy and near-access-freeness (NAF), in the context of copyright law.

### Weaknesses
Weakness:
1.	Overall, the technical contributions of this paper may seem weak. While I admit that the paper made contribution in capturing the differences between using existing algorithmic stability methods to determine copyright infringement and applying copyright law, the technical contributions is not significant and do not help to address the problems. The main theoretical result is Proposition 1, which most people would likely anticipate. From my opinion, the most valuable part is Section 3, but this part does not contain any technical discussion.

2.	Another issue with this paper is that critique of NAF and DP does not lead to new quantifiable algorithmic stability approach immediately, not does it shed light on how to modify these notions to better resonate with the essence of copyright law.

3.  The paper lacks empirical or experimental results that would solidly substantiate its technical claims. For instance, 1) DP does not allow high influence under a satisfactory 'copyright definition', 2) NAF can allow models that may memorize completely the training set as long as a content they output does not provide a proof for such memorization.
 
4. There is contradiction between the legal and technical discussions. For example, the authors initially assert that a satisfactory "copyright definition" must allow algorithms to be highly influenced. However, in discussing the 'overly exclusive' of algorithmic stability, they claim that protection is confined to concrete 'expressions' and does not encompass abstract "ideas".

5. While the paper conceptually identifies the problem, it does not propose a practical solution or methodology to prevent copyright infringement, nor does it provide any discussions towards that end.

### Questions
Questions:
1.	On page 2, the authors mentioned “We further propose a different approach to using quantified measures in copyright disputes, to better serve and reconcile copyright trade-offs.” However, I was not able to identify where in the paper this different approach is proposed. 

2.	The title "Can copyright be reduced to privacy?" seems to be incoherent with the main subject matter and body of this paper. The entire discourse in Section 3 orbits around the disparity between practical application and algorithmic stability methods. These methods are not exclusively confined to Differential Privacy (DP), but are more associated with the more versatile concept of NAF. The main purpose of NAF is to provide a measurement of a model's copyright protection, rather than privacy protection. However, this discussion strays from the main theme of whether privacy can reduce to copyright. From my perspective, this paper is more centered on the incongruity between NAF and copyright protection in practice.

3. please provide some experimental results to further support your claims on the limitation of DP and the flexibility of NAF.

4.  clarify the contradictions between the legal and technical discussions, and provide empirical evidence if necessary.
5. discuss the potential solutions


3.	On page 9, I am still uncertain about the distinction between "convert murky standards into rigid rules" and "make legal standards less murky" in the context of computer science methodology. If we intend to incorporate CS methodology into the legal profession to clarify legal standards, rigid rules are inevitable. Could the authors further elaborate on this?

4.	The writing in some parts can be further improved. For example, what does \eta mean in Proposition 1.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
