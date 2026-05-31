## Human Reviewer 1

### Summary
The paper introduces **O-Forge**, a workflow that couples a frontier LLM with a computer algebra system (CAS), specifically Mathematica’s Resolve, to prove asymptotic inequalities by (i) asking the LLM to propose a domain (or index) decomposition and (ii) using Resolve to verify each piece via first-order quantifier elimination. A toy inequality and a series bound from Tao are used as case studies; the paper claims the approach “moves beyond contest math” by offloading the creative split to the LLM and the verification to CAS. The system exposes a CLI and a website front-end; evaluation is described as ~40–50 “easier problems,” with qualitative takeaways about typical numbers of subdomains and the usefulness of leading-term simplifications.

### Strengths
N.A.

### Weaknesses
There are too many drawbacks in this paper. In general, this submission is more like a blog post instead of a rigorous paper as it lacks of enough and solid experiments and evaluations to demonstrate its claims. Some of the weaknesses are as follows.
- **Lack of Novelty:** LLM + CAS could be viewed as part of Tool-use LLM research. The proposed idea is not novel.
- **Insufficient rigor and experimental substance:** The “evaluation” consists of two main case studies plus ~“40–50 easier problems,” but there are no well-defined benchmarks, success metrics, or failure analyses (rates of correct/incorrect splits, wall-clock, query counts, sensitivity to prompts, comparisons to baselines like hand-crafted heuristics or SMT-based pipelines, etc.). As is, this reads more like a prototype report/blogpost than an ICLR-level empirical study.
- **Underspecified method details:** Key pieces are missing or skeletal. For example, the “structured prompt” is left with placeholders (“describe the structure of the prompt”), and the code snippet for Resolve is fragmentary; the search over constants C is a coarse grid without justification or sensitivity analysis. This makes the approach hard to reproduce or evaluate scientifically.
- **Heavy reliance on closed-source Mathematica without proof objects:** While Resolve is powerful, the paper acknowledges there is no proof term and asks the reader to trust a closed system; this undermines the claim of “rigorous verification,” especially for research-level math. No attempt is made to cross-check with open tools (e.g. SageMath) on a subset, or to export certificates.
- **Reproducibility & accessibility concerns:** Running the system requires Mathematica and a frontier LLM API, making reproduction costly; even the authors’ ethics section notes access costs. There is a website, but that can’t substitute for open artifacts or independent verification.
- **Scope creep vs. precise problem definition:** The paper oscillates between “asymptotic inequalities” and the specific case study. I could feel the motivation of this paper: making a true AI4Math tool or project to better help professional mathematicians instead of some fuzzy LLMs that could only do math questions. But there is no crisp task definition, no sanity check for the motivation, and no quantitative experiments to show the helpfulness and effectiveness. This vagueness makes it hard to judge whether this is something scientifically helpful or just some course project.

### Questions
- Please use \citep for non-subject/object citations.

### Soundness
1

### Presentation
1

### Contribution
1

### Rating
0

### Confidence
5

---

## Human Reviewer 2

### Summary
Following Terry Tao’s proposed algorithm, a system for asymptotic analysis is implemented. It combines an LLM for the creative part of sub-domain choice, and uses Mathematica for the rest of the steps - notably “Resolve” for proofs in specific sub-domains.

2 non-trivial asymptotic bounds were proven via this system.

### Strengths
If works well, applicable to a broad range of scientific endeavors.

Final results are grounded via a reliable CAS system.

Shown proof of concept for useful mathematical results.

### Weaknesses
Line 86: “(** describe the structure of the prompt**)”...
This is unprofessional at best.

Line 91: All the mentioned solvers need citations, as well as the Mathematica Resolve function - due to its central role in your system.

Line 100: Fig.1 is mentioned initially on page 2 but appears on page 4. Why?

Line 101 (and multiple others): “o-forge.com”.
At the top right corner of the front page of this website it clearly states:

Created by

Vijay Ganesh

Ayush Khaitan

Violating the ICLR guidelines regarding anonymity. 


Regarding the website itself, while I liked the UI and readily available examples, it sometimes returns weird results.
For example, Example Series 1 returns a summary that contains a single word: “The”. I ran it a few times to make sure it’s not some random LLM aberration.
Other times the output shows a Python error stack trace (“Execution Failed”).
Seems underbaked and the code is unstable.

Line 109,113,119 (and others): Citations. You’re mentioning Prof. Tao many, many times - but he is a prolific mathematician. Point to the specific works you use.

Line 123: While I personally agree with this claim on (most) interesting series bounds, it needs to be quantified (benchmark vs. other methods), or at least supported by multiple examples from the literature.

Line 127: The novelty claim is unclear to me. It seems like an engineering project - implementing a (good) idea by Prof. Tao. While I agree that such an online tool can be useful for mathematicians around the world - and would like to encourage you to improve it and fix the bugs - the system does not constitute *scientific* innovation done by you.

The generate (via LLM) -> verify (via CAS) approach was done in multiple projects (though not specifically in your use case) - so the core approach is also not novel on its own.

If the strongest results are the proof of the specific use-case (which to my understanding is indeed novel, but I don’t know enough to say how impactful this singular result is), then perhaps consider submitting to a mathematical / experimental math journal?

Line 295: I’m a supporter of readable papers and not-too-formal language, but this is too much. 
The paper is not your blogpost.

Line 348: What do you mean “around 40-50”??

Section 5: You need concrete statistics for all the claims here. Currently it’s anecdotal.

Section 6: There are multiple other works in AI for Math that apply combinations of CAS/code generation + LLMs. The current overview is quite limited.

### Questions
Line 256: This “elaborate Mathematica code’ seems like an important part of the system - perhaps ~50% of its power?

Line 270: Once in the entire process? If I’m reading the outputs on your website correctly, there are recursive attempts to re-define the sub-domain partition, until you get “True” on all of them?

Line 328: How is the output passed to Mathematica? Is there a specific format that you force it to use in its output? Do you parse the output text and translate it to Mathematica code? If so, how?

Line 359: How do you count decompositions? Number of separate domains or number of boundaries?

Line 367: Any ideas why this happens? 
How do you do this replacement?

### Soundness
1

### Presentation
1

### Contribution
2

### Rating
0

### Confidence
4

---

## Human Reviewer 3

### Summary
he paper presents O-Forge, a system that integrates a large language model (LLM) with a computer algebra system (CAS) to aid in the verification of asymptotic inequalities. This is an instance of classical synthesis paradigms such as oracle guided inductive synthesis combining an inductive LLM with deductive reasoning system to generate formal artifacts. The paper describes this as an “In-Context Symbolic Feedback Loop”.  The LLM proposes domain decompositions (i.e., how to split a problem into manageable subdomains). The CAS (via Mathematica’s Resolve function) then verifies whether each subdomain satisfies the proposed inequality using first-order logic and quantifier elimination.

### Strengths
The authors claim their tool can handle research-level asymptotic inequalities, going beyond standard competition-style problem solving by combining LLM creativity with CAS rigor. This is left to some subjective interpretation. 
Two case studies: an asymptotic AM-GM inequality and a series decomposition, are used to demonstrate the concept.

### Weaknesses
The paper reads more like a concept demo or blog post than a rigorous scientific study, lacking detailed quantitative and ablation studies with proper baselines. Testing on self-curated  "suite of around 40-50 easier problems" and a few case studies falls far short of the evaluation expected of a research paper. 

Hybrid symbolic–neural approaches (e.g., Lean+LLM, AlphaProof, Autoformalization pipelines; see https://arxiv.org/abs/2310.17807, https://ieeexplore.ieee.org/document/10356332) have already explored the same broader paradigm with planning, code generation, formal proof verification, not just heuristic checking. The authors present O-Forge as “revolutionary,” yet it is essentially prompting an LLM for suggestions and sending them to a formal tool - Mathematica. 

Crucial implementation details are omitted. How exactly is the LLM prompted? How is the “in-context feedback” loop structured? How is the decomposition quality evaluated or improved iteratively? Are there failure modes where the LLM produces incorrect decompositions, and how are these handled?

### Questions
Can you expand experimental evaluation and share quantitative metrics (success rate, runtime, size of inequalities handled) over larger benchmark suite to substantiate performance?

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
The paper introduces a CAS + LLM system for proving asymptotic expressions. The primary thrust of the system is to use a LLM to propose decompositions and then use a CAS to test their correctness.

### Strengths
Due to the very unusual nature of the weaknesses, I don't have any strengths to comment on.

### Weaknesses
This paper does not appear to contrain any evidence as to its effectiveness. Section 5 begins "In addition to the above-mentioned case study of hard problems, we tested our tools on an extensive suite of around 40-50 easier problems, in order to study how well it performs on a diverse set of inequalities," but there is no mention of these "hard problems" anywhere in the paper. Additionally, for these easy problems, the paper presents three high level takeaways but no actual evidence.

### Questions
Did I misunderstand something? Does this paper present evidence of its correctness?

### Soundness
1

### Presentation
1

### Contribution
1

### Rating
0

### Confidence
4