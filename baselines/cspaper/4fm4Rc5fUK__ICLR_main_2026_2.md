---
job_id: 3ba8064d-b1ee-45de-9247-089d65c4634c
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 4fm4Rc5fUK.pdf
paper: Autoformalizer with Tool Feedback
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically neurosymbolic and hybrid AI systems, tool-integrated reasoning, datasets/benchmarks, and machine learning for formal reasoning.

## Minimum Quality
Pass ✅. The paper includes all expected core sections, namely Abstract, Introduction, Related Work, Methodology, Experiments, Results/Ablations/Analysis, and Conclusion, and it presents a complete empirical study with quantitative tables and figures. While I have substantial concerns about evaluation design and some claims, these are review-level weaknesses rather than desk-rejection issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions or manipulative content targeting automated reviewers; the prompts included in the appendix are part of the described method and dataset construction rather than attempts to influence peer review.

# Expected Review Outcome:
## Summary
This paper studies autoformalization for Lean 4 and proposes ATF, a formalizer trained to iteratively use two external tools during generation, a syntax checker based on Lean 4 compiler feedback and a semantic consistency checker based on an ensemble of LLM judges. The training pipeline combines cold-start synthetic tool-use trajectories, expert iteration, and a DPO stage that prefers shorter successful revision paths. Experiments on FormalMath-Lite, ProverBench, and CombiBench show large gains over several recent formalizer baselines, and the paper also introduces a 750K synthetic dataset, Numina-ATF.

## Strengths
The paper targets a real bottleneck in autoformalization, namely that syntax-validity and semantic faithfulness are both brittle in existing systems. This is not a cosmetic issue, and the motivation is well conveyed in **Figure 1**, which concretely illustrates two failure modes, compiler failure and subtle semantic drift. Even though the figure is stylized, it helps anchor the central claim that “formalization quality” is not captured by syntax alone.

The proposed pipeline is reasonably coherent. The decomposition into cold start, expert iteration, and DPO in **Figure 2** is easy to follow, and the three-stage design is aligned with the intended behavior, first learning tool-use format, then improving formalization quality, then reducing wasteful revisions. I also appreciated that the paper did not simply stop at “we use compiler feedback,” but explicitly added a second tool for semantic checking.

The empirical gains reported in **Table 3** are large and consistent across datasets, especially on CombiBench. If the evaluation protocol is reliable, the result that ATF-32B improves Pass@1 consistency on CombiBench from 36.25 to 65.38 over Goedel-V2-Formalizer-32B is substantial, and the human evaluation row shows the same direction of improvement. The out-of-distribution behavior on CombiBench is one of the more compelling parts of the paper.

The ablation in **Table 4** is useful and supports the high-level claim that tool feedback matters. In particular, the gap between “NO TOOLS” and “SYNTAX CHECK + CONSISTENCY CHECK” is large on all three datasets, and the comparison between “SYNTAX CHECK ONLY” and the full system suggests that the semantic checker contributes beyond mere compiler repair. This is better than many papers that only compare the final system to baselines and leave the mechanism underspecified.

The paper includes some analysis beyond benchmark numbers. **Figure 4** suggests that the model benefits from both more revisions and larger sampling budgets, and **Figure 5** gives some visibility into how often the tools are being used. The grouped Lean execution design in **Figure 3** is also a practical systems contribution, and the appendix timing table indicates a meaningful efficiency gain for large-scale syntax checking.

Presentation is mostly solid. The main paper is generally readable, and the core method can be understood without depending on the appendix.

## Weaknesses
1. **The central semantic evaluation tool is still too weakly validated for the weight the paper places on it.**  
   This is the biggest issue for me. The paper repeatedly frames semantic consistency as a key criterion and attributes a large part of the gains to the consistency-check tool, but the evidence in **Section 3.1.2** and **Table 1** is not strong enough to establish that this tool is a trustworthy evaluator, especially when it is also used inside the training loop. On the benchmark of 800 positives plus perturbations, the ensemble vote reduces FPR, but at the cost of recall dropping to 0.5967. That is a very large false-negative rate, 0.4033, which means a substantial fraction of actually consistent formalizations are judged inconsistent. The paper acknowledges this tradeoff but underplays its implications. It matters because this tool is not just a noisy side metric, it governs data filtering, successful trajectories, and the training signal in expert iteration. A conservative judge may improve “precision of acceptance,” but it can also distort what the model learns to produce, potentially favoring formulations that please the judge rather than faithfully formalize the problem.

2. **There is a concerning circularity between training and evaluation, especially for semantic consistency.**  
   The same family of judge-based criteria appears in tool construction, training-time filtering, and main evaluation. Even if the exact prompts or models differ in small details, the paper’s main success metric, CC in **Table 3** and **Table 4**, is fundamentally tied to the proposed consistency checker. This makes it hard to disentangle whether ATF is truly better at formalization or better at satisfying the preferences of the judge used throughout the pipeline. The human evaluation helps, but it is limited to 100 examples per benchmark and only for 32B models. Moreover, Appendix C states that annotators were provided with “the results from the consistency check execution” and were allowed to refer to the tool explanation or ask Claude 4 for help. That setup is not a clean blind gold-standard evaluation. Showing the tool outputs to annotators risks anchoring them toward the paper’s own judge. This is exactly the place where independence matters most.

3. **The benchmark for validating the consistency checker is narrow and may not reflect the real failure modes of autoformalization.**  
   In **Section 3.1.2**, negatives are constructed by perturbing valid statements with Gemini-2.5-Pro, filtered by high character-level similarity and human verification. This creates a useful stress test for near-miss examples, but it is still a synthetic distribution. Real autoformalization mistakes are often messier: omitted assumptions, wrong type choices, quantifier scope shifts entangled with library artifacts, underspecified domains, and theorem statements that are syntactically polished but mathematically underconstrained. A judge that performs well on perturbation-based negatives may still fail on naturally generated model errors. This matters because the paper uses the benchmark in **Table 1** as the justification for calling the tool “more accurate” and then relies on it extensively for training and evaluation.

4. **The fairness of the baseline comparison is not fully convincing because ATF is allowed iterative tool use while the baselines are treated as static generators.**  
   The paper notes in **Section 4.1** that ATF uses up to 4 revision attempts at inference, while the output length is said to be “roughly equivalent” to Goedel-V2-Formalizer-32B. That is not the same as equal inference budget. ATF has access to external verification and iterative correction; the baselines apparently do not receive analogous test-time assistance. This makes **Table 3** harder to interpret as a pure model comparison. It may still be a fair system-level comparison, but then the claim should be phrased more carefully as “ATF system with tools” versus “standalone formalizer baselines,” not as a straightforward model superiority result. I would have liked to see at least one stronger baseline equipped with a syntax-repair or self-correction loop under comparable inference compute.

5. **The mathematical specification of the training objective is underspecified relative to the actual training data structure.**  
   **Equation (1)** gives a DPO-style loss with an additional NLL term,
   \[
   \mathcal{L}=-\mathbb{E}\left[\log\sigma\left(\beta\log\frac{\pi_{\theta}(y_w|x)}{\pi_{\text{ref}}(y_w|x)}-\beta\log\frac{\pi_{\theta}(y_l|x)}{\pi_{\text{ref}}(y_l|x)}\right)\right]-\alpha\mathbb{E}\left[\log\pi_{\theta}(y_w|x)\right].
   \]
   But the paper also says that tool-result tokens are masked, and for DPO, tool-invocation-related tokens are masked as well. This raises an important question: what exactly is the sequence probability \(\pi_\theta(y\mid x)\) over in the loss? Is it the full trajectory probability with some token losses masked, or the probability of only the natural-language and code-edit portions? DPO is sensitive to how log-probabilities are computed. If masked tokens are excluded, the effective objective is not the same as standard DPO over complete trajectories, and this should be stated explicitly. Otherwise, it is hard to reason about what preference is actually being optimized. Relatedly, the chosen/rejected pair construction is based solely on revision count difference \(\ge 3\), which is a fairly blunt proxy for quality. Fewer revisions does not always imply a better formalization policy unless success probability and correctness are controlled very carefully.

6. **The evaluation protocol for Pass@k is not fully transparent once iterative revisions enter the picture.**  
   In **Section 4.1**, the paper says it samples 16 times with temperature 0.6 and reports unbiased Pass@1/8/16, while also allowing ATF multiple revision attempts per sample. It is not fully clear what constitutes one “sample” for Pass@k, a complete trajectory that may contain up to 4 revisions, or a single initial formalization before revision. This matters for interpreting the very high Pass@16 numbers in **Table 3**, especially the near-saturated results for ATF. If each of the \(k\) samples internally performs several tool-guided revisions, then the effective search budget is much larger than a standard \(k\)-sample decoding baseline.

7. **Some of the strongest claims are broader than what the evidence supports.**  
   For instance, the abstract and introduction claim that the syntax tool “allows adjustments tailored to different language versions” and addresses version generalizability, but all experiments are in Lean 4 v4.15. There is no cross-version evaluation, no Lean 3 transfer experiment, and no ablation showing robustness to compiler-version changes. That part reads as aspiration rather than demonstrated result. Similarly, the paper says the developed tools provide “accurate measurements” of syntax and semantic consistency, but the consistency side is only partially validated and remains noisy by the authors’ own numbers.

8. **The analysis figures are suggestive but a bit too thin to support the paper’s broader interpretive claims.**  
   In **Figure 4(b)**, the curve on CombiBench reaches essentially 100% by Pass@32, which looks impressive, but without cost reporting the result is incomplete. The paper argues that this demonstrates favorable inference-time scaling, yet there is no analysis of total tool calls, wall-clock time, or compute-normalized comparison to baselines. Likewise, **Figure 5** is helpful descriptively, but the interpretation is sometimes too confident. For example, the claim on **Page 9** that decreasing consistency success with more revision attempts means the model is exhausting its confident strategies is plausible, but not uniquely supported by the figure. It could also reflect selection bias, because harder examples naturally survive to later attempts.

9. **The human evaluation is useful but not rigorous enough to fully validate the semantic claims.**  
   The human study in **Table 3** improves confidence somewhat, but the design leaves room for concern. First, only 100 instances per benchmark are used. Second, only 32B models are evaluated. Third, the evaluators are provided the tool outputs, which can bias judgment. Fourth, no inter-annotator agreement is reported. Fifth, the reported Pearson correlation of 0.746 on **Page 8** is hard to interpret without confidence intervals and without clarifying the unit of correlation, model-level, benchmark-level, or per-instance. This is not fatal, but for a paper whose main novelty is a semantic validation tool, the human validation should be stronger.

10. **The related-work positioning is somewhat incomplete around compiler/type-check feedback for autoformalization.**  
   The paper cites several recent formalizer systems, but the positioning around prior work that also uses type checking, compiler feedback, or iterative correction in Lean-focused formalization feels thinner than it should be. Given that the core idea here is not merely “use a model for autoformalization,” but “close the loop with formal-system feedback,” the paper should more sharply distinguish what is genuinely new relative to prior syntax/type-check-guided pipelines and process-oriented formalization setups. As written, the novelty story is a bit blurred between engineering integration, data synthesis, and evaluation-tool design.

11. **There are some signs of presentation sloppiness that become problematic in a paper about formal languages.**  
   The main text is mostly readable, but there are small issues that chip away at confidence: inconsistent capitalization and dataset naming, a few grammatical glitches, and some overly compressed descriptions of the tool logic. More importantly, the appendix case study on **Pages 14 to 17** is visibly corrupted with malformed symbols and garbled quantifiers. I am not using the appendix to downgrade soundness directly, but it does suggest insufficient proofreading around the exact formal objects the paper is centered on.

## Questions
1. The most important question is about independence of semantic evaluation. Could the authors provide a stronger human-only analysis where annotators do **not** see the consistency-check output or explanations, and report inter-annotator agreement? If that evaluation still shows a similar margin on CombiBench and the in-distribution sets, my confidence would increase materially.

2. In **Equation (1)**, how exactly are \(\log \pi_\theta(y\mid x)\) and \(\log \pi_{\mathrm{ref}}(y\mid x)\) computed when tool-result tokens and, in DPO, tool-invocation tokens are masked? Please specify whether the trajectory probability is restricted to a subset of tokens, and if so, which subset. This is important for understanding what preference signal DPO is actually optimizing.

3. For **Table 3**, what is the exact inference budget per benchmarked sample for ATF versus the baselines? In particular, for Pass@\(k\), does each of the \(k\) attempts include up to 4 internal revisions with tool calls? A compute-normalized comparison, total model tokens plus total tool invocations, would make the results much easier to interpret.

4. Could the authors provide at least one competitive baseline augmented with a simple iterative syntax-repair loop or compiler-guided self-correction, using the same max revision budget? This would help isolate whether the gains come from the ATF training pipeline specifically, or from giving any reasonably strong model access to the same test-time feedback channel.

5. The consistency-check benchmark in **Section 3.1.2** uses perturbation-generated negatives. Can the authors quantify judge performance on naturally occurring model outputs instead, for example by sampling errors from baseline formalizers and manually labeling them? That would better reflect the distribution encountered during expert iteration and final evaluation.

6. The paper claims adaptability across language versions in the introduction. Do the authors have any evidence for this, even a small transfer experiment across Lean versions or library settings? If not, I suggest softening that claim.

7. In Appendix C, annotators were allowed to consult Claude 4 and were shown tool outputs. Please clarify the exact annotation protocol and whether the model/tool assistance could have biased judgments toward the paper’s own consistency-check criterion.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the main paper. The work focuses on autoformalization benchmarks, tool integration, and synthetic dataset construction for Lean 4 theorem statements. I do encourage the authors to clearly document licensing, provenance, and intended use restrictions for the released Numina-ATF dataset in the final version, but this does not rise to the level of an ethics flag based on the current submission.

## Soundness Rating
2: fair. The empirical results are promising and the paper is methodologically organized, but the central semantic-evaluation component is not validated strongly enough, and there is nontrivial circularity between training, filtering, and evaluation.

## Presentation Rating
3: good. The paper is generally readable and the high-level method is clearly structured, with helpful figures and tables, though some claims overreach the evidence and a few details are underspecified.

## Contribution Rating
2: fair. The tool-feedback framing and strong benchmark gains make this worth attention, but the scientific contribution is weakened by evaluation dependence on the paper’s own judge and by incomplete isolation of where the gains actually come from.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is clearly tackling an important problem and reports strong numbers, but the evidence for semantic correctness, which is the core claim, is not yet rigorous enough for me to recommend acceptance with confidence.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I carefully checked the main method, tables, figures, and the stated objective, and I am familiar with the area, but some uncertainty remains because the strongest concerns hinge on evaluation design rather than an outright technical flaw.