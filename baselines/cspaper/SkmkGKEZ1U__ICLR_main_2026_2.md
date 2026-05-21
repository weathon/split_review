---
job_id: ae4164b6-b6eb-459d-9c67-63d8ce6b9472
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: SkmkGKEZ1U.pdf
paper: O-FORGE: An LLM + Computer Algebra Framework for Asymptotic Analysis
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper fits ICLR through neurosymbolic and hybrid AI systems, specifically the use of an LLM coupled with a symbolic verifier/CAS for mathematical reasoning.

## Minimum Quality
Pass ✅. The paper contains the core components expected of a research submission, including abstract, introduction, methodology/framework, empirical evaluation, related work, and conclusion. While the empirical evidence and technical specificity are weak, these issues do not rise to the level of an automatic desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, concealed instructions to reviewers, or other manipulative content in the provided manuscript text or figure content.

# Expected Review Outcome:
## Summary
This paper presents O-Forge, a framework that combines a frontier LLM with Mathematica's `Resolve` function to prove asymptotic inequalities and series bounds by first proposing a domain decomposition and then verifying each regime symbolically. The paper focuses on two case studies, one inequality involving \(xy \ll x\log x + e^y\), and one series estimate attributed to Tao, and also reports brief experience on a small collection of easier problems. The main claim is that LLM-guided decomposition plus CAS verification can serve as a practical research assistant for asymptotic analysis.

## Strengths
The paper targets an interesting and underexplored use case for hybrid AI systems, namely helping mathematicians with asymptotic estimates rather than contest-style one-shot proof generation. That is a relevant direction for ICLR's neurosymbolic audience, and the framing around decomposition as the "creative" step is intuitive and potentially useful.

I appreciated the high-level workflow in **Figure 1**. It clearly communicates the intended division of labor between the user, the LLM, and the CAS, and it supports the paper's central message that the LLM is used for proposing regimes while the verifier handles rigor. As a conceptual diagram, it is simple but effective.

The two worked examples are easy to follow and make the intended use case concrete. In particular, the inequality example on **Page 4**, centered around Equation **(1)**, does show why regime splitting can turn a hard-looking global claim into easy local checks. Even though the example itself is mathematically elementary, it succeeds as a pedagogical illustration of the pipeline.

The paper is also commendably explicit about one important limitation: Mathematica does not emit independently checkable proof objects. This caveat appears in Sections 1, 6, and 7, and it is good that the authors do not oversell formal verification in the proof-assistant sense.

There is some practical value in the user-facing tooling. A CLI and website interface may lower the barrier for non-programmer users, and for systems papers or tool papers that kind of accessibility can matter.

## Weaknesses
1. **The empirical evidence is far too thin for the strength of the claims.**  
   The paper repeatedly claims that O-Forge is effective for "research-level mathematics today" and can prove estimates that would take mathematicians "several hours" or even be inaccessible to "almost no theorem prover, human or machine" without the right decomposition, see **Pages 2, 3, 5, and 8-9**. But the actual evidence in the main paper consists of two handpicked case studies and a vague statement in **Section 5** that the tool was tested on "around 40-50 easier problems." There is no benchmark table, no dataset specification, no per-problem outcomes, no failure analysis, no comparison across models, and no quantitative success rate. This matters a lot because the paper's central contribution is empirical: the value of the method hinges on whether the LLM reliably proposes useful decompositions and whether the full pipeline works beyond cherry-picked examples. Right now, the reader is asked to trust broad claims on the basis of anecdotal evidence.

2. **The absence of results tables is a serious presentation and evaluation gap.**  
   Since the paper has an empirical section, I expected at least one table listing the problem suite, categories, number of variables, decomposition size \(k\), whether the LLM suggestion was accepted, whether `Resolve` succeeded, and possibly runtime. Instead, **Section 5** contains only qualitative bullet points. Because there is no **Table 1** or equivalent results summary anywhere in the paper, it is impossible to assess coverage, robustness, or reproducibility from the main text. This is not a cosmetic issue. Without a results table, the paper does not substantiate its own claims about "robustness" or "wide variety of asymptotic inequalities" on **Page 7**.

3. **The method is underspecified at exactly the point where the paper claims the main novelty: how decompositions are generated.**  
   The decomposition proposal is the core creative component, but **Section 2, Step 2** only states that the LLM proposes a finite cover \(D=\bigcup_{i=1}^k D_i\) guided by "dominant terms and monotonic regimes." That is too vague. What is the actual prompt structure? What constraints are imposed on candidate decompositions? How are malformed, overlapping, redundant, or incomplete regime proposals handled? Is there one LLM call or multiple rounds? Is there any self-correction? On **Pages 6-7**, the prompt block is effectively empty:
   ```
   <guiding_principles>
   -
   </guiding_principles>
   ...
   ```
   This is surprisingly incomplete for a paper whose claimed contribution depends on prompt-mediated decomposition quality. The omission makes it difficult to understand what is actually being evaluated and whether the system can be reproduced from the main paper.

4. **The mathematical verification procedure is underspecified and, as written, weaker than the rhetoric suggests.**  
   In **Section 2, Step 4** on **Page 3**, the method checks
   \[
   \forall x \in D_i:\ f(x)\le C g(x),
   \]
   while "searching \(C\) over a finite grid (e.g. \(1\) to \(10^4\))." This means the system is not proving an asymptotic statement in any symbolic sense; it is searching over a finite set of constants and declaring success if one works. For the stated use case this may be acceptable as a practical procedure, but the paper should be much more precise about what is and is not guaranteed. In particular:
   - Why is a finite grid search over integer constants sufficient for the examples considered?
   - Is \(C\) searched before or after simplification, and does the same \(C\) need to hold across all subdomains?
   - If the true optimal constant is not in the grid, the method may produce a false negative. How common is that?
   - For asymptotic notation, one usually quantifies existence of some \(C>0\), often together with domain conditions; the paper never formalizes how the user-specified domain restrictions are normalized before calling `Resolve`.

   This matters because the manuscript often uses language like "rigorously verify" and "proof verified," but the operational semantics in the method are a finite search procedure wrapped around a trusted backend, not a fully specified theorem-proving pipeline.

5. **There are mathematical shortcuts and informal proof steps that are not carefully written, even in the flagship examples.**  
   The proof sketch for Equation **(1)** on **Page 4** contains the line
   \[
   y > 2\log x \Rightarrow x\log x + e^y \ge e^{y/2} e^{y/2} \ge xy.
   \]
   The intended idea is presumably that \(e^{y/2} > x\), hence \(e^y = e^{y/2}e^{y/2} \ge x e^{y/2}\), and then one needs \(e^{y/2}\ge y\) or some variant to conclude \(e^y \ge xy\). But that intermediate justification is omitted. For a human mathematician this gap is easy to repair, but in a paper about automated rigorous verification, such shorthand is not ideal. Similarly, in **Case Study 2** the phrase "the summand can be approximated as" \(\frac{d+1}{h^2}\), \(\frac{1}{d}\), or \(\frac{h^4m^4}{d^5}\) on **Page 5** is informal. If these are upper bounds needed for proof, the paper should state them as precise inequalities, with the conditions under which they hold. The distinction between approximation, asymptotic equivalence, and valid dominating bound matters here.

6. **The series case is especially underexplained, and the claimed simplification rule is not formally justified in the main paper.**  
   On **Page 5**, the authors state that "if the numerator and denominator are a sum of finite numbers of terms, then the summand \(\ll\) ratio of these leading order terms." That heuristic is not valid without assumptions such as positivity, monotonicity, and control over cancellations. **Section 2, Step 3** does mention "enforcing positivity where required" and guarding against singular regions, but the actual rule used by the implementation is never formalized. For example, if
   \[
   \frac{\sum_i a_i(d)}{\sum_j b_j(d)}
   \]
   is replaced by a ratio of selected leading terms, one needs explicit conditions ensuring
   \[
   \frac{\sum_i a_i(d)}{\sum_j b_j(d)} \le C \frac{\tilde a(d)}{\tilde b(d)}
   \]
   on the given regime. The main paper does not state these conditions. This is not a request for deep theory for theory's sake, it is about whether the core simplification step is mathematically valid beyond the showcased example.

7. **The paper makes broad novelty and significance claims without adequately differentiating itself from prior work.**  
   Statements such as "No existing AI tools are able to complete and symbolically verify proofs of this kind" on **Page 3**, or "This is one of the first AI-powered tools that is useful for research-level mathematics today" on **Page 8**, are much stronger than what the evidence supports. The related work section is short and selective. It compares mainly against AlphaGeometry, some Lean tactics, and autoformalization, but does not sufficiently situate the paper within the broader landscape of interactive mathematical reasoning, tool-augmented LLMs, or formal-math evaluation. Even within the paper's own framing, it is not clear whether the contribution is mainly a new algorithm, a system integration, or a case study around Mathematica's existing quantifier elimination capabilities. The current positioning overclaims relative to the demonstrated evidence.

8. **The implementation section reads more like a prototype note than a scientific method description.**  
   **Section 4** on **Pages 6-7** is unusually thin. The prompt is omitted, the Mathematica code snippet is truncated and syntactically unclear, and there is no algorithm box or pseudocode for the end-to-end loop. The CLI commands are mentioned, but the actual system behavior, fallback cases, parsing assumptions, and error handling are absent. This hurts both reproducibility and scientific clarity. A conference paper can of course present a system, but then the system must be described with enough fidelity that one can understand how inputs are transformed into verified outputs.

9. **The paper's main examples are illustrative but too simple to establish "research-level" capability.**  
   Equation **(1)**, \(xy \ll x\log x + e^y\), is a nice toy example for regime splitting, but it is not itself a strong stress test. The series example is somewhat better, but even there the main paper provides only a verbal decomposition argument rather than the actual mechanically verified subgoals. If the claim is that the tool helps on estimates that consume serious researcher time, the examples need to show more complexity, or the evaluation section needs to provide a broader and better documented suite.

10. **There are several writing and formatting issues that reduce credibility.**  
   The paper has multiple informal or unfinished passages, for example "(** describe the structure of the prompt**)" on **Page 2**, the empty prompt skeleton in **Section 4**, malformed closing tags and code formatting on **Pages 6-7**, and some grammatical issues. The references also contain placeholders like "Commit version as of <insert-hash-or-date>" on **Page 10**. These are not fatal on their own, but they reinforce the impression that the manuscript is not yet polished enough for a top conference.

11. **The trust model is weaker than suggested by the paper's language.**  
   The manuscript does acknowledge that Mathematica is closed source and does not emit proof objects, see **Sections 1 and 7**, which is good. However, many parts of the paper still use wording like "rigorously verified" and "the mathematician may be assured that the estimate is indeed true" on **Page 5**. That language should be toned down. What the system provides is trusted symbolic validation by a proprietary CAS backend, not independently checkable formal certification. For some users that is perfectly useful, but the distinction matters scientifically and philosophically, especially in a paper centered on verification.

## Questions
1. Please provide a concrete quantitative evaluation in the rebuttal. At minimum, I would like a table over the claimed 40-50 easier problems containing: problem category, number of variables, decomposition proposed, whether the decomposition covered the full domain, whether `Resolve` succeeded on each piece, overall success/failure, runtime, and which LLM was used. If the success rate is strong on a nontrivial suite, that would materially improve my assessment.

2. What exactly is the decomposition-generation protocol? Is it a single prompt to one model, multiple samples with selection, or an iterative loop? What model(s) were used, with what prompting, temperature, and stopping criteria? Right now the method section is too underspecified to judge whether the decomposition component is robust or just a prompt-engineering artifact.

3. Can you formalize the simplification rule used in the series case? In particular, under what conditions is replacing a summand by a bound derived from "leading order terms" guaranteed to be sound? A precise proposition or even a clearly stated heuristic condition would help.

4. In **Section 2, Step 4**, why is searching \(C\in\{1,\dots,10^4\}\) the right formulation? Did any examples fail only because the required constant lay outside the search grid? Also, is \(C\) shared across all subdomains or can each subdomain use its own constant before taking a global maximum?

5. For the two case studies, could you show the exact subdomain formulas passed to `Resolve` and the exact returned truth values? This would make the examples much more convincing than the current verbal description.

6. Have you compared the LLM-proposed decomposition against simple handcrafted heuristics, such as thresholding by dominant term equalities, dyadic splits, or exhaustive small families of candidate splits? Without such baselines, it is hard to know how much value the LLM actually adds.

7. The paper states that `Resolve` is superior to alternatives like Z3, CVC5, MetiTarski, Lean tactics, Maple, and Sage for this use case. Can you provide a more systematic comparison, even on a small benchmark? At present these comparisons are anecdotal.

## Flag For Ethics Review
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)  
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The paper relies on proprietary components, specifically frontier LLM APIs and Mathematica, and promotes a public website interface, see **Pages 2, 6, and 9**. This raises practical questions about terms of use, data handling, and reproducibility for user-submitted mathematical content, even if the risk level is not high. I am not flagging this as a major ethical violation, but I do think the paper should more clearly state what user inputs are sent to third-party services, what is stored, and what reproducibility guarantees exist for a system whose core components are closed and paid.

There is also a responsible research practice issue in that the paper's framing around "rigorous verification" can be misunderstood by readers as formal proof certification, whereas the backend is a trusted but closed-source CAS without proof objects. This is discussed by the authors, but the terminology should be more careful throughout the manuscript.

## Soundness Rating
2: fair. The overall idea is plausible and the showcased examples are believable, but the core method is underspecified and the empirical support is too limited to fully substantiate the broader claims.

## Presentation Rating
2: fair. The high-level story is understandable and **Figure 1** helps, but the paper has several incomplete passages, missing methodological detail, and no quantitative results table in the main paper.

## Contribution Rating
2: fair. The application direction is interesting and potentially useful, but the current submission does not yet demonstrate enough rigor, breadth, or differentiation to justify a stronger contribution score.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The problem setting is interesting and the hybrid AI angle is relevant, but the current paper is too anecdotal and underspecified for ICLR. The biggest issue is not that the idea is bad, it is that the paper asks the reader to infer generality and robustness from two examples and a vague claim about 40-50 easy problems, without the tables, ablations, baselines, or formalization needed to support that leap.

## Reviewer Confidence
4: confident. I am confident in the overall assessment, though not absolutely certain. The mathematical examples are easy to follow, and the main weaknesses are visible from the paper itself: underspecified methodology, missing quantitative evidence, and overextended claims.