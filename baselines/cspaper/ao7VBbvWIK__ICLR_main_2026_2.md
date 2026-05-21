---
job_id: e042d80a-08ab-4bf3-b463-9fa8c15553a7
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ao7VBbvWIK.pdf
paper: HASTE: Hybrid AST-Guided Selection With Token-Bounded Extraction
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is about retrieval and context compression for LLM-based code generation/editing, which fits ICLR’s scope through language models, representation/retrieval for code, and ML infrastructure for long-context reasoning.

## Minimum Quality
Pass ✅. The submission contains the basic components of a research paper, including abstract, introduction, related work, methodology, experiments/results, and conclusion. Although the empirical support and methodological precision are weak, these issues are better handled in full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, suspicious reviewer-targeting text, or other prompt-injection style manipulations in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes HASTE, a pipeline for retrieving code context for LLM-based software engineering tasks under token-budget constraints. The method combines AST-aware chunking, hybrid lexical and semantic retrieval, call-graph expansion, and budgeted extraction, with the stated goal of balancing semantic relevance and structural coherence. The paper evaluates HASTE on a small curated set of six Python files and on a subset of SWE-PolyBench using LLM-as-a-judge scores, reporting high compression and generally strong judged edit quality.

## Strengths
The paper tackles a practical and important problem. Context selection for code LLMs under limited token budgets is genuinely relevant, and the paper frames the structure-versus-relevance trade-off in a way that is easy to understand and motivated by real failure modes in code generation.

The overall system design is intuitive. In particular, the combination of retrieval signals with structure-aware expansion is a sensible engineering direction. **Figure 1** gives a useful high-level picture of the intended modular flow, from ingestion and indexing to retrieval and observability. Even though the figure is not sufficient for reproducibility, it does make the paper’s intended decomposition clear.

The paper also makes an effort to study compression-quality trade-offs rather than reporting only a single operating point. **Figure 2(b)** and **Figure 2(c,d)** at least attempt to connect token reduction with downstream quality, which is more informative than a single average score.

The writing is readable at a high level. A reader can follow the motivation and the claimed contributions without much difficulty, and the main pipeline components are described in an accessible way.

## Weaknesses
1. **The empirical validation is far too weak for the paper’s central claims.**  
   The main curated evaluation in **Section 4.1.1** and **Table 1** uses only six Python files, several of which are quite small, for example `test1.py` with 52 LOC and `test6.py` with 144 LOC. That is simply not enough to support claims about “reliable and scalable AI-assisted software development” from the abstract and conclusion. With only six curated instances, the paper is effectively a small case study, not a convincing benchmark-driven evaluation. This matters because the claimed contribution is not just that the pipeline can work in a few examples, but that it meaningfully resolves a general retrieval/compression trade-off.

2. **The baseline comparison promised in the methodology is missing from the results.**  
   In **Section 4.1.3**, the paper lists three baselines: IR-only retrieval, AST-only retrieval, and naive truncation. However, **Table 2**, **Figure 2**, and the discussion in **Section 5.1-5.3** do not report comparative results against any of these baselines. This is a major problem. Without side-by-side numbers, there is no evidence that HASTE outperforms simpler alternatives, and the central claim that the hybrid structure-aware design resolves the trade-off better than structure-only or relevance-only approaches remains unsubstantiated. Right now, the paper mostly shows that HASTE can produce decent outputs on some examples, not that HASTE is better than the baselines it names.

3. **Several evaluation metrics are introduced but then not actually reported.**  
   In **Section 4.2**, the paper defines three metrics: LLM-as-Judge score, AST Fidelity, and Hallucination Rate. But the presented results only include judge scores and compression ratios. I could not find quantitative AST Fidelity results or hallucination-rate results in **Table 2**, **Figure 2**, or **Figure 3**. This is not a minor omission. The paper repeatedly argues that AST guidance preserves structural integrity and reduces hallucination; if so, those two metrics should be central evidence, not dropped after being introduced. The current evidence does not actually demonstrate the claimed structural fidelity or hallucination reduction.

4. **The method is underspecified at the algorithmic level, especially the core AST-guided selection step.**  
   The paper describes HASTE in broad modules, but the critical mechanism is not defined precisely enough to reproduce or evaluate scientifically. For example, in **Section 3.3**, after retrieval, “the expanded set is then filtered under a strict token budget,” but the paper never specifies the actual optimization or heuristic used for this filtering. Is the selection greedy by fused score? Is there subtree-level packing? Are ancestors forced in when descendants are selected? What happens when a node partially fits the budget? How are imports, class headers, decorators, and enclosing scopes handled? These details are exactly where AST-aware selection either succeeds or quietly breaks.  
   Similarly, **Equation (RRF)** only defines the rank fusion score,
   \[
   \mathrm{RRF}(d)=\sum_{s\in S}\frac{1}{k+\mathrm{rank}_s(d)},
   \]
   but the rest of the pipeline is mathematically or algorithmically unspecified. The paper claims “AST-bounded pruning” and token-bounded extraction, yet there is no formal objective such as
   \[
   \max_{A \subseteq \mathcal{N}} \sum_{n\in A} w_n \quad \text{s.t.} \quad \sum_{n\in A} \mathrm{tokens}(n) \le B,
   \]
   together with closure constraints over the AST or call graph. Without such a definition, the paper’s core contribution remains too vague.

5. **Important implementation choices that strongly affect results are omitted.**  
   The embedding model is not specified in **Section 3.2**. The chunking granularity is described only qualitatively. The semantic index type is given as examples such as FAISS/Annoy/HNSW rather than the actual one used. The top-\(n\) value, call-graph traversal depth, token budget, retrieval candidate count, and the exact prompt format for the editor LLM and judge LLM are not fully documented in the main paper. These are not cosmetic details, they directly affect retrieval quality, context size, and edit performance. Because of this, the work reads more like a system sketch than a sufficiently pinned-down scientific method.

6. **The curated results are not statistically meaningful, and the correlation analysis is overinterpreted.**  
   In **Figure 2(c)** and **Figure 2(d)**, the paper highlights Pearson correlations \(r=-0.97\) and \(r=-0.81\) between compression and judge score. But this is based on only six points, one of which (`test3.py`) is a clear leverage point with unusually high compression in **Figure 2(b)** and the lowest score in **Figure 2(a)**. With \(n=6\), these correlations are not robust evidence for a general trade-off, especially with such a narrow score range. The paper presents these figures as if they establish a meaningful frontier, but in reality they mostly visualize that one case is more compressed and slightly worse. This matters because a key contribution claimed in the abstract and introduction is understanding the compression-quality frontier.

7. **The SWE-PolyBench evaluation is weakly framed and potentially biased by task selection and exclusions.**  
   In **Section 5.3**, the paper states that the analysis “excludes instances that resulted in processing errors.” That exclusion could materially change conclusions, but the paper does not tell the reader how many instances were excluded, why they failed, or whether failures were due to HASTE itself. Also, **Figure 3** shows that many high scores come from “POLYBENCH-NOOP” tasks, which are explicitly trivial non-functional edits. The paper itself admits this. That sharply limits what can be concluded from the benchmark results. If most successes are no-op tasks, then the evidence for meaningful code reasoning and localization is much weaker than the headline presentation suggests.

8. **The paper relies heavily on LLM-as-a-judge without adequate validation.**  
   **Section 4.2.1** says a general-purpose LLM scores correctness, readability, and instruction alignment, but there is no calibration against execution-based correctness, unit tests, or human annotations. For code editing, judge models are especially risky because syntactic plausibility and verbal alignment can mask semantic errors. The use of a single editor model and a judging model, both without robust external validation, reduces confidence in the conclusions. Given that the paper claims improved success rate and reduced hallucinations, stronger objective evaluation should be expected.

9. **The paper makes strong claims about structural coherence and executability without showing executable evidence.**  
   Repeated language throughout the abstract, **Section 2.2**, and **Section 5** suggests that HASTE produces “structurally coherent and executable” context. But no compilation/pass-rate metric, parsing success rate, or execution-based benchmark is shown. Even AST fidelity is not reported, despite being defined. This is a gap between claim and evidence. In code tasks, “looks coherent” is not the same as “compiles/runs/solves the task.”

10. **Novelty and positioning relative to prior work are not convincing enough.**  
   The high-level recipe, hybrid lexical+semantic retrieval plus structural expansion/pruning under a token budget, feels incremental. The paper argues novelty from the combination, but the positioning is not sharp enough to establish what is substantially new beyond assembling familiar components. The related work also misses some important code-retrieval/context-compression literature, including retrieval-augmented code generation frameworks such as **ReACC** and long-context code compression work such as **LongCodeZip**. This matters because the current framing risks overstating originality while under-discussing closely adjacent systems.

11. **The presentation is clear at the narrative level, but the figures and tables also expose the limits of the evidence.**  
   **Table 2** reports only HASTE’s judge score and compression ratio, with no baseline columns, no variance, and no AST-fidelity/hallucination metrics. That table is therefore not strong enough to support comparative or mechanistic claims.  
   **Figure 1** is useful as an architecture diagram, but it also reveals how broad and pipeline-oriented the paper is relative to the amount of concrete technical detail actually provided. The figure contains many modules, yet the paper never drills down into the exact selection algorithm that is supposed to be the scientific core.  
   **Figure 3** is also somewhat self-undermining: it visually confirms that the benchmark evidence is dominated by perfect scores on trivial tasks, with a tail of severe failures. That pattern suggests the method may be acceptable for easy prompt-localization cases, but the paper is not yet showing robust gains on demanding code editing.

12. **There are some troubling signals around citation and framing precision.**  
   A few references appear futuristic or placeholder-like, for example the **Zhang et al., 2025** citation is explicitly marked “Placeholder citation for illustrative purposes” on **Page 10**. That is not appropriate in a polished conference submission. It makes the literature review feel less reliable and raises concern that the positioning was not assembled carefully enough.

## Questions
1. The most important issue is the missing baseline comparison. Can the authors provide a table, on both the curated set and SWE-PolyBench, directly comparing HASTE against the three baselines listed in **Section 4.1.3**: IR-only, AST-only, and naive truncation? Ideally this should include judge score, AST fidelity, hallucination rate, and some variance estimate across runs.

2. What is the exact algorithm for token-bounded AST-guided extraction after retrieval and call-graph expansion? Please define it precisely. For example, what units are selected, how is budget enforced, and what closure constraints are required so that extracted code remains structurally valid? A pseudo-code algorithm or formal objective would significantly increase confidence.

3. Can the authors report the metrics that are currently defined but missing from the results, specifically AST Fidelity and Hallucination Rate from **Sections 4.2.2-4.2.3**? If these metrics did not support the narrative, that would itself be important to know.

4. On SWE-PolyBench, how many total instances were attempted, how many were excluded due to processing errors, and what were the causes of those errors? Were these errors due to retrieval, parsing, prompting, or downstream generation? This matters for practical robustness.

5. What embedding model, vector index, chunking policy, top-\(n\), call-graph depth, and token budget were actually used? The main paper currently leaves these underdetermined. A concrete configuration table would help a lot.

6. Did the authors evaluate any execution-based or parser-based correctness metric, for example parse success, unit-test pass rate, or exact patch correctness, to validate the LLM judge? If not, can they provide evidence that judge scores correlate with actual code correctness on this task?

7. The correlation analysis in **Figure 2(c,d)** is based on only six examples. Can the authors either expand this study substantially or tone down the interpretation? As written, the claims about the compression-quality frontier feel stronger than the evidence.

8. The paper claims structural coherence and executability. Can the authors provide direct evidence, such as compilation/parse rates of retrieved contexts or edited outputs, and compare this against structure-agnostic retrieval/truncation?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond standard considerations for using open-source code datasets and LLM evaluation. The paper does not raise a clear ethics issue that requires escalation based on the main text alone.

## Soundness Rating
2: fair. The core idea is plausible, but the technical claims are only partially supported because key baselines are missing, core metrics are unreported, and the method is underspecified.

## Presentation Rating
2: fair. The paper is readable and the high-level motivation is clear, but the scientific presentation is incomplete. Important algorithmic details, configuration choices, and comparative evidence are missing.

## Contribution Rating
2: fair. The problem is relevant and the system combination is sensible, but the current paper does not convincingly establish a contribution at ICLR level in either methodological novelty or empirical substantiation.

## Overall Rating
2: Reject, not good enough. The paper addresses a useful problem and has a reasonable systems intuition, but the current submission does not provide the evidence needed to support its main claims. The absence of baseline comparisons, missing reported metrics, very small curated evaluation, and underspecified core algorithm leave the work substantially below the bar for acceptance.

## Reviewer Confidence
4: confident. I am confident in this assessment. The paper is easy enough to follow at a high level, and the main concerns come from explicit gaps between the claims, the stated methodology, and the actual reported evidence.