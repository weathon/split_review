Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper introduces Dig-DEC, a new model-free Decision-Estimation Coefficient that removes the optimism principle used in prior work (optimistic DEC [FGQ+23]) and drives exploration purely through information gain. The authors provide a unified algorithmic framework that generalizes prior AIR-based approaches, and apply it to both stochastic and hybrid MDPs. Key results include: (i) Dig-DEC is always no larger than optimistic DEC and can be much smaller, (ii) the first model-free regret bounds for hybrid MDPs with bandit feedback (resolving an open problem from [LWZ25]), and (iii) improved regret rates for Bellman-complete MDPs ($\sqrt{T}$, matching optimism-based SOTA).

## Strengths

1. **First model-free regret bounds for hybrid MDPs with bandit feedback.** The paper obtains sublinear regret for hybrid bilinear classes and coverable MDPs with linear reward and bandit feedback, resolving the main open problem stated in [LWZ25] (abstract, Section 5.2, Table 2). This is a well-motivated and technically significant advance.

2. **Principled removal of optimism.** Dig-DEC removes the optimism mechanism and replaces it with pure information-gain-driven exploration. This is conceptually cleaner and enables handling adversarial rewards without explicit reward estimators — something the optimism-based approach could not do (Section 4, Theorem 13, Section 6). Theorem 13 shows Dig-DEC ≤ optimistic DEC + η, so nothing is lost and potentially much is gained.

3. **$\sqrt{T}$ regret for Bellman-complete MDPs.** The paper improves the squared-estimation-error procedure from the $T^{5/6}$ bound of [FGQ+23] to $\sqrt{T}$ for Bellman-complete MDPs (Table 1, Theorem 11), matching the performance of optimism-based approaches for the first time in a DEC-based method.

4. **Unified analysis framework.** Algorithm 1 with the general divergence $D^\pi$ in Eq. (7) recovers prior AIR-based results cleanly and connects to standard mirror-descent analysis, without relying on the "constructive minimax theorem" of [XZ23]. The analysis is more flexible and addresses all canonical MDP classes (bilinear, Bellman-eluder, coverable) under a single framework.

## Weaknesses

### Fatal
None.

### Major

1. **Inconsistency between advertised and tabulated regret exponents.** The abstract claims: "improving their regret bounds from $T^{\frac{3}{4}}$ to $T^{\frac{3}{5}}$ (on-policy) and from $T^{\frac{5}{6}}$ to $T^{\frac{7}{8}}$ (off-policy)" for average estimation error minimization. However, Table 1 reports regret of $T^{2/3}$ for **all** entries using average estimation error ($\overline{D}_{\text{av}}$) — both on-policy and off-policy bilinear classes, and both Q-type and V-type BE. Neither $T^{3/5}$ nor $T^{7/8}$ appears anywhere in the table. The squared-error improvement to $\sqrt{T}$ is correctly reflected in Table 1 for several Bellman-complete settings, but the average-error claims in the abstract do not align with the stated results. This is not a minor formatting issue — it directly affects how readers understand the paper's contribution. The authors must reconcile these numbers or clarify which setting the abstract refers to.

### Minor

2. **Scope limitation of Assumption 3 is underplayed in the introduction.** The paper claims (abstract, line 38) to resolve "the main open problem left by [LWZ25]" regarding model-free hybrid MDPs with bandit feedback. However, Section 3.2 (lines 121-122) acknowledges that Assumption 3 (unique reward-to-value mapping) does not capture all learnable hybrid MDPs — e.g., when reward features are unknown, the $\log|\Phi|$ term scales polynomially, while a prior work [LMWZ24] handles this case with only logarithmic dependence. The authors also require Assumption 4 (known linear reward feature). The introduction's framing somewhat overstates the generality of the resolution. The paper is honest about this in the technical section, but a reader skimming the abstract and intro could get an inflated impression.

3. **Theorem 14 (constant regret in 3-armed bandit) would benefit from main-text intuition.** The claim that Dig-DEC achieves constant regret ($\max_a \mathbb{E}[\text{Reg}(a)] \leq 1$) in a constructed 3-armed bandit instance where optimistic DEC suffers $\Omega(\sqrt{T})$ is striking, and the proof is relegated to Appendix J. While deferring proofs to appendices is standard practice for theory papers, a short intuitive explanation of *why* constant regret is possible (e.g., what structural property the example exploits) would help the reader assess the result without needing to reconstruct the appendix argument.

### Trivial

4. **Parsing artifacts in the introduction.** The introduction (line 39) contains clearly corrupted fractions such as "$T^{\frac{3}{2}}/T^{\frac{5}{8}}$" and "$T^{\frac{3}{2}}$" as claimed [FGQ+23] regret bounds — $T^{3/2}$ is superlinear and cannot be a valid regret bound. This is a PDF extraction artifact from the original submission, but the authors should ensure the camera-ready version has clean typesetting.

## Nice-to-Haves

- A brief example or illustration of the $\Phi$ partition structure (Figure 1, referenced in Appendix B) would aid understanding of Assumptions 2-3, which are dense and central to the hybrid setting.
- A discussion of whether the algorithm's computational complexity is polynomial/practical or purely existential would help contextualize the contribution.

## Removed Points

- **Theorem 14 "extraordinary claim without justification" (Harsh Critic Issue 2):** REMOVED. The proof is in Appendix J of the original submission. Per policy, missing appendix content is not a valid criticism — the parser strips these sections from all papers. The main text provides the theorem statement and explains its purpose (showing strict improvement over optimistic DEC in a toy setting). A minor weakness remains (see Weakness 3 above) about the lack of intuition in the main text, but the core criticism is invalid.
- **POSTERIORITYUPDATE insufficiently specified (Harsh Critic Issue 3):** REMOVED as a standalone weakness. The main text provides high-level descriptions for both the average estimation error case (unbiased estimator via sample splitting, Section 4.2.1) and the squared error case (two-timescale procedure, Section 4.2.2). Deferring algorithmic pseudocode to the appendix is standard practice for theoretical papers at top venues.
- **Introduction's $T^{3/2}$ fractions "fatal inconsistency" (part of Harsh Critic Issue 1):** REMOVED. These are clearly PDF parsing artifacts — no paper would claim $T^{1.5}$ regret. The genuine inconsistency between abstract and Table 1 (retained as Major Weakness 1) is what matters.
- **Strength Finder's generic strengths** (e.g., "addressed an important problem", "comprehensive coverage"): REMOVED. Only concrete, evidence-grounded strengths are retained.
- **Criticism about Assumption 3 not capturing all cases as an "understated" limitation:** WEAKENED to Minor. The paper explicitly acknowledges this limitation (lines 121-122) and notes that [LWZ25] has the same limitation. The issue is that the abstract and introduction frame the contribution more ambitiously than the full nuance would warrant.
- **"Evaluation lacks rigor" / "could be measuring a proxy" type speculative criticisms:** REMOVED. None present in the actual reviews.

## Novel Insights

None beyond the paper's own contributions. The reviews do not uncover a fundamentally new interpretation of the work — they surface a presentational inconsistency (abstract vs. Table 1) and note limitations the paper itself acknowledges.

## Suggestions

1. **Fix the abstract/Table 1 inconsistency.** Either correct the abstract's claimed regret exponents ($T^{3/5}$, $T^{7/8}$) to match the $T^{2/3}$ in Table 1, or, if the abstract refers to a different setting not captured in Table 1, clarify this explicitly and add the corresponding row to the table.
2. **Add a short intuition for Theorem 14** in the main text explaining how the 3-armed bandit instance is constructed to make constant regret achievable.
3. **Tone down the "resolving the open problem" framing** to match the Assumptions 3-4 limitations, or explicitly state the scope (known linear reward features, unique reward-to-value mapping).

## Score and Decision

**Calibration anchors** (all from the human-reviewed corpus):

| Anchor | Avg Score | Comparison to this paper |
|--------|-----------|--------------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/txD9llAYn9.md` (Model-based RL, horizon-free) | 7.0 | Stronger — cleaner presentation, no inconsistencies, well-received results |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/aPNwsJgnZJ.md` (Horizon-free adversarial linear mixture MDPs) | 6.0 | Comparable — both have solid theory contributions; the current paper has a broader scope but a presentation flaw |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/w8Zo7jACq7.md` (Model-free CMDPs) | 5.2 | Comparable — both have genuine contributions and some weaknesses; the current paper has stronger novelty |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/2h3m61LFWL.md` (Value-biased MLE for linear MDPs) | 4.25 | Weaker — had novelty concerns relative to prior work; current paper has clearer novelty |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/en3NwykrHW.md` (Minimax optimal RL with trajectory feedback) | 5.5 | Similar quality — solid theory with meaningful contributions and some presentation concerns |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/i3KSorBQxF.md` (No-regret learning in adversarial MDPs) | 4.0 | Weaker — had significant technical concerns; current paper is technically stronger |

The paper makes genuine contributions: a new model-free DEC formulation, the first model-free bounds for hybrid MDPs with bandit feedback, and improved rates for Bellman-complete MDPs. The main weakness is an inconsistency between abstract claims and Table 1 that must be resolved. This is not a fatal flaw — the core technical results are likely sound — but it requires correction before publication. Relative to the calibration anchors, the paper sits comfortably above papers with novelty/technical concerns (score 4-5) and is comparable to well-regarded theory papers (score 6), pulled down slightly by the presentation issue.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>