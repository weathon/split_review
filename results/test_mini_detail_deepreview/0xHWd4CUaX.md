Now I have sufficient calibration data. Let me write the final review.

**Calibration Analysis:**

**Round 1 Bracketing:** I searched broad bands. Weak anchors (avg <3.5): FALCON (3.00), AutoPR (3.50). Middle anchors (3.5-7.5): CoRNStack (6.25), ContraDiff (5.67), GEPCode (4.33), CodeDPO (4.25). Strong anchors (>7.5): Various 8.0 papers on different topics. Initial bracket: 2.5-4.5.

**Round 2 Narrowing:** Inside the bracket I read SWE-Search (4.00), CodeDPO (4.25), AutoPR (3.50), GEPCode (4.33). Comparing in detail:
- SWE-Search (4.00): Has writing issues and limited baselines but clear contribution. Our paper has worse writing plus the GraphRL-survey baseline issue. **Our paper is weaker.**
- AutoPR (3.50): Poor writing and evaluation concerns. Our paper has similar problems PLUS the more critical GraphRL-is-a-survey issue. **Our paper is slightly weaker.**
- CodeDPO (4.25): Some novelty concerns but better written. **Our paper is clearly weaker.**
- FALCON (3.00): Poor writing and questionable novelty. Our paper has a better-designed method but worse evaluation validity (GraphRL survey) and no code release. **Comparable to FALCON.**

**Final Score: 3.0**. The paper has a coherent framework idea but the evaluation is critically undermined by a key baseline (GraphRL) being a survey paper, not a concrete method. Combined with poor writing quality (obvious LLM artifacts), missing action space definition, no variance reporting, and unsupported claims about symbolic execution cost, the paper does not meet the bar for acceptance.

---

## Summary

This paper proposes a reinforcement learning framework for automated code refactoring that uses contrastive pre-trained code graph embeddings. The method combines a syntax-guided contrastive encoder, a composite reward function (traditional metrics + embedding dynamics + semantic preservation), and embedding-guided exploration. Experiments on refactoring datasets with ablation studies are reported.

## Strengths

- **Coherent framework design with clear modular components**: The method decomposes into three well-defined modules — contrastive pre-training of code graphs (Section 4.1), a composite reward function fusing three signals (Section 4.2), and embedding-guided exploration via Mahalanobis distance to prototype states (Section 4.3). Each component is formalized with explicit equations.

- **Ablation study shows each component contributes**: Table 2 systematically removes key components and reports the drop in SI, SP, and MG. The largest single drop comes from removing contrastive pre-training (−7.5% SI), and removing semantic tests drops SP by 8.6%. This provides empirical evidence that the design decisions matter beyond what a single metric would show.

- **Cross-language generalization experiment**: Table 3 evaluates the Java-pretrained model on Python and C++ without fine-tuning, outperforming language-specific rule-based tools (PyLint, Cppcheck). This demonstrates transferability that rule-based approaches do not achieve.

## Weaknesses

### Fatal
- **"GraphRL" baseline is a survey paper, not a concrete method**: The paper treats "GraphRL" (Darvari et al., 2024) as a state-of-the-art RL-based refactoring method ("GNN policy with expert demonstrations") and claims to outperform it (Table 1). However, the reference (lines 353–355) shows this is a survey: "Graph reinforcement learning for combinatorial optimization: A survey and unifying perspective" (arXiv:2404.06492). It is not a refactoring system with reported SI/SP/MG scores. The paper's central comparative claim — that the proposed method beats the best RL baseline — rests on comparing against a paper that contains no such method or results. This fundamentally undermines the evaluation in Table 1. The comparison against Code2Seq, Graph2Edit, RLRefactor, and NeuroRefactor is not sufficient to salvage this, since GraphRL is presented as the strongest RL baseline and the claimed margins over it (e.g., +5.9% SI) are unverifiable.

### Major
- **No variance or confidence intervals reported for any result**: Tables 1–3 report single numbers without standard deviations, confidence intervals, or number of seeds. RL agents are inherently noisy; results from a single run could be within the noise of the baselines. This is a standard expectation for RL papers that is not met here.

- **Action space is never defined**: The MDP formulation mentions an action space $A$ ("possible refactorings") but the paper never lists what specific refactoring operations the agent can perform (e.g., extract method, rename variable, reorder statements). Without this, the method is not reproducible and the reader cannot assess what transformations the agent is learning to apply.

- **Symbolic execution claimed to be "lightweight" with no supporting evidence**: Section 4.5 describes generating test cases via symbolic execution (Cadar & Sen, 2013) at each RL step and calls this "lightweight." Symbolic execution is NP-hard in general, and no runtime analysis, wall-clock measurements, or success rates are reported. In a setup requiring 1M environment steps, it is unclear whether this component is feasible at all, yet it is central (removing it drops SP by 8.6%).

- **PMD and Checkstyle as SI baselines are not explained**: Table 1 reports SI scores for PMD (62.1%) and Checkstyle (58.7%). SI is defined as "percentage reduction in code smells (PMD/Checkstyle violations)." How do static analysis-only tools (which detect but do not generate code transformations) achieve SI scores? The paper does not explain this, making the comparison uninterpretable.

### Minor
- **Writing quality reflects heavy LLM polish with residual artifacts**: The abstract and body contain phrases like "most often do last year," "lemon deep learning technologies," "excellently reduces the necessity," and "objecting to code quality." While Section 8 discloses LLM use for polishing, the result is sometimes unclear or non-sequitur. This does not affect technical content but harms readability.

- **Equation (7) has notation issues**: The attention computation writes $\mathbf{a}^\top [\mathbf{W}_h \|\mathbf{W}_q] \mathbf{h}_j$ which concatenates weight matrices $\mathbf{W}_h$ and $\mathbf{W}_q$ (both $\mathbb{R}^{d' \times d}$) before multiplying by $\mathbf{h}_j$. Standard GAT attention uses $\mathbf{a}^\top [\mathbf{W}\mathbf{h}_i \| \mathbf{W}\mathbf{h}_j]$ — the concatenation of transformed features, not weight matrices. The paper should clarify this.

- **BigCloneBench usage is unclear**: The paper lists BigCloneBench (6M Java fragments) as a refactoring dataset for "cross-project evaluation" but BigCloneBench is a clone detection benchmark. It is not explained how refactoring operations are applied to these fragments or what the evaluation protocol is.

### Trivial
- None beyond the writing artifacts noted above.

## Nice-to-Haves
- Reporting results over multiple random seeds (≥3) with standard deviations.
- A cleaner baseline that isolates the embedding contribution by fixing the policy architecture while swapping reward formulations.
- A runtime/scaling analysis of the symbolic execution component.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Criticism that "Marvellous et al., 2025" is not in the reference list**: Removed as factually wrong — the reference appears at line 389.
- **Claim that the embedding dynamics reward "could encourage needless transformations" with no evidence**: Removed — this is speculative. The ablation study shows removing this reward degrades SI, which is standard evidence for a component's contribution.
- **"Pure formatting/style nitpicks"**: Removed per instructions. Various minor presentation complaints.
- **Criticism about missing appendix content**: Removed — the parser strips those sections; they exist in the original submission.
- **Strength Finder's generic strengths about "addressing an important problem"**: Removed — these are superficial and not specific to this paper.
- **Strength Finder's claim about "faster convergence" as a separate strength**: Merged into other strengths; it's a supporting point, not a core one.

## Novel Insights

None beyond the paper's own contributions. The reviews surfaced the critical GraphRL-survey baseline issue that the paper's own framing obscures, but this is a flaw in the evaluation, not a novel insight about the subject matter.

## Suggestions

1. **Replace the GraphRL baseline** with a properly implemented RL-based code refactoring method whose results can be independently verified. Without this, Table 1 cannot support the central comparative claim.
2. **Define the action space explicitly** — enumerate at minimum the refactoring operations available to the agent.
3. **Run experiments over ≥3 random seeds** and report means with standard deviations.
4. **Either provide runtime measurements for the symbolic execution component** or replace the claim of "lightweight" with a realistic description of the implementation.
5. **Explain how PMD and Checkstyle are used to produce SI scores** — are they being used with auto-fix rules? If so, state this explicitly.
6. **Proofread carefully** to remove LLM artifacts like "lemon," "last year," and "excellently reduces."

## Score and Decision

**Anchors (all rounds):**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|--------------------------|
| N18Z2MkMEa (FALCON) | 3.00 | R1, R2 | Similar poor writing and methodological concerns. FALCON has code release; this paper has a clearer framework design but critically flawed evaluation. Comparable quality. |
| dsALpkd1OU (D2Coder) | 1.67 | R1 | Much weaker — barely coherent. Our paper is clearly better. |
| kNvwWXp6xD (Seeker) | 3.00 | R1 | Comparable score but different domain. |
| CscKx97jBi (CodeGen Feedback) | 3.00 | R1 | Comparable. |
| iyJOUELYir (CoRNStack) | 6.25 | R1, R2 | Much stronger — well-written, thorough evaluation, clear contribution. Our paper is far below this. |
| vfzRRjumpX (Code Rep at Scale) | 5.75 | R1 | Much stronger. |
| XMOaOigOQo (ContraDiff) | 5.67 | R1, R2 | Stronger — clear motivation, thorough experiments, though some theoretical concerns. Our paper has more severe evaluation flaws. |
| 6EadiKkfgR (Contrastive Learners) | 5.25 | R1 | Stronger theoretical contribution. |
| YrycTjllL0 (BigCodeBench) | 9.00 | R1 | Exceptional quality — not comparable. |
| KbetDM33YG (Online GNN) | 8.00 | R1 | Much stronger. |
| 6FNYXWHRbz (AutoPR) | 3.50 | R2 | Similar writing and evaluation issues. AutoPR has somewhat better presentation; this paper has the GraphRL-survey issue. This paper is slightly weaker overall. |
| G7sIFXugTX (SWE-Search) | 4.00 | R2 | Clearer contribution and better experiments. Our paper is notably weaker. |
| U5TebOVpfd (CodeDPO) | 4.25 | R2 | Stronger — better writing, more thorough evaluation despite some concerns. |
| DgGdQo3iIR (GEPCode) | 4.33 | R2 | Stronger — focused contribution with clear experiments. |

**Round 1 bracket:** 2.5–4.5. **Round 2 narrowing:** Compared to FALCON (3.00) and AutoPR (3.50), this paper has a more critical evaluation flaw (GraphRL is a survey) that prevents the main comparative claim from being supported. Compared to SWE-Search (4.00) and CodeDPO (4.25), this paper is clearly weaker due to writing quality and evaluation validity. The paper lands closest to FALCON (3.00) in terms of overall quality, making **3.0** the appropriate score.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>