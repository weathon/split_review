Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes the Fast and Slow Effect (FSE) framework and Class Representation Index (CRI) metric to evaluate whether LLM-generated concept annotations for XAI are sufficient for accurate concept-class mapping. The framework progressively refines concepts across five stages, comparing a "fast mode" (direct visual classification) to a "slow mode" (textual concept-based classification). Experiments across six LLMs and five datasets reveal a striking finding: the slow mode underperforms fast mode by 25%+ on fine-grained datasets, and the utility-as-proxy assumption commonly used in prior work does not reliably reflect annotation sufficiency.

## Strengths

- **Novel and principled framework design**: The FSE framework is a genuinely creative contribution. The fast/slow mode contrast (inspired by dual-process theory) provides a structured way to probe the gap between what LLMs can do implicitly (visual recognition) and what they can externalize as textual concepts. The five-stage refinement process—background, superclass, salient features, detailed features, auxiliary features—is thoughtfully designed and grounded in prior hierarchical extraction literature.

- **Comprehensive and rigorous empirical evaluation**: The paper evaluates six models from three families (GPT, Llama, Qwen) at two scales each, across three fine-grained and two general datasets, in both post-hoc and visual-grounded settings. The findings that slow mode consistently underperforms fast mode on fine-grained data (average CRI-Gap of −25% to −27%, Table 2) while the pattern reverses on general datasets (Table 3) are robust and well-supported. Three runs with negligible standard deviations confirm consistency.

- **Utility-as-proxy assumption empirically refuted**: The fused-mode experiment (Table 4) provides direct evidence that high downstream performance (~90% CRI in fused mode) can coexist with insufficient textual annotations (~50-60% in slow mode alone). This is an important cautionary result for the concept-based XAI community, where utility-as-proxy has been a widespread validation practice.

- **Autonomous evaluation without human supervision**: The framework requires no human annotation or domain expertise for validation, addressing a genuine bottleneck in the field. The semantically related distractor strategy (validated in a preliminary contradiction test, Table 1) ensures the candidate set presents a realistic challenge.

## Weaknesses

### Major

- **The CRI metric conflates annotation sufficiency with the LLM's reasoning ability, and the paper's central claim over-interprets the evidence.** Definition 3.1 defines sufficient annotations as those enabling "accurate inference of the corresponding class." The CRI operationalizes this by having the *same* LLM that generated the concepts reason from them. If the LLM fails (low CRI), this could indicate either (a) the concepts are genuinely insufficient, or (b) the LLM cannot reliably reason from its own textual descriptions—a well-documented limitation. The paper acknowledges this tension in the abstract ("it remains challenging for them to conceptualize this knowledge in the slow mode") and elsewhere, but the core claim—that "current annotation methods fail to provide sufficient semantic coverage" (abstract, conclusion)—overstates what the evidence supports. The result is more precisely described as a **self-consistency gap**: LLMs can recognize objects from images but cannot reliably re-identify them from their own textual concepts. This is still a valuable empirical finding, but the framing should be adjusted to avoid overclaiming about annotation quality independent of the model's reasoning capability. The limitation section (Section 8) does not discuss this confound at all, focusing instead on societal impacts.

### Minor

- **Equation (2) contains a clear typo in the CRI formula.** The equation reads $\frac{1}{t} \sum_{i=1}^t \mathbb{1}[y_i^t = y_i]$, where $i$ indexes test cases $1,\dots,l$ (from the definition of $\mathcal{D}_{\text{test}}$). The sum should be over $i=1$ to $l$, and the divisor should be $l$, not $t$. The surrounding text correctly describes it as "the proportion of correctly predicted labels," so this is a typo in the manuscript rather than a fundamental error, but it needs correction.

- **Distractor selection description is somewhat underspecified.** The Semantic Similarity Dictionary (SSD) construction (Section 5.3) states: "For each class, we record the top four predicted classes (excluding the ground-truth class itself) for each data sample." It is unclear whether this produces per-class aggregated distractors or per-sample distractors, and how they are applied in the main FSE evaluation (where distractor sets are needed per test case). The methodology is understandable in broad strokes, but full pseudocode or a clearer description would aid reproducibility.

### Trivial

- None beyond the above.

## Nice-to-Haves

- The paper would benefit from an additional experiment separating concept quality from reasoning ability, e.g., using a stronger reasoner (GPT-4o) to classify from concepts generated by a weaker model (Llama-3.2-11b). If low CRI persists across reasoners, the concepts themselves are the bottleneck; if not, the reasoning gap is the dominant factor.

- Including formal statistical significance tests (e.g., paired permutation tests) for the CRI-Gap comparisons would strengthen the results, though the reported small error bars suggest the trends are reliable.

- The "Slow Mode Superiority" hypothesis would benefit from clearer framing as a diagnostic sanity check derived from dual-process theory, rather than a claim about what the XAI community expects.

## Removed Points

The following points from the input reviews were removed per the filtering rules:

- **"Slow Mode Superiority is a straw-man framing"** — Removed. The paper motivates this hypothesis from dual-process theory (Kahneman, 2011), which is a legitimate scientific framework. Testing a hypothesis and finding it does not hold is how science works; this is not a straw man.
- **"CRI confound is structural and cannot be fixed"** — Demoted from Fatal to Major. The confound is real but the paper acknowledges it partially; the finding remains valuable as a self-consistency measure. The issue is framing, not structural invalidity.
- **"The motivating example is over-interpreted"** — Removed. The example (Figure 1) is a clear and appropriate illustration of the inconsistency problem the paper addresses.
- **Various section-by-section opinions** (e.g., "the paper should be more explicit about this," "the framing draws attention from the more interesting result") — Removed as personal takes rather than concrete weaknesses.
- **"Missing related works"** — Removed per hard rules.
- **"Formatting/style nitpicks"** — Removed per hard rules.
- **Strength Finder's generic strengths** (e.g., "important problem," "principled definition") — Removed or demoted when they conflicted with verified weaknesses.

## Novel Insights

The most valuable insight from this reviewer synthesis is that the paper's findings are stronger when reframed around **self-consistency** rather than annotation insufficiency. The observation that the fused mode (visual + textual) achieves ~90% CRI while the slow (text-only) mode achieves only ~50-60% tells us something important about how these models use (or fail to use) their own generated concepts. This is not merely a limitation of the annotation pipeline—it reveals a fundamental property of LLMs: their visual knowledge is not easily ported into the textual reasoning channel, even when the textual descriptions are generated by the same model. The reversal on general datasets (CIFAR-100, Caltech-101) further suggests this gap is task-dependent: LLMs can externalize knowledge for coarse-grained categories but struggle with fine-grained distinctions. These findings could inform the design of better prompting strategies or training objectives for concept-based XAI.

## Suggestions

1. **Reframe the central claim** around self-consistency: the paper shows that LLMs struggle to re-identify classes from their own textual concepts, revealing a modality gap in how knowledge is represented and accessed.
2. **Fix the CRI formula typo** in Equation (2): change $\frac{1}{t}\sum_{i=1}^t$ to $\frac{1}{l}\sum_{i=1}^l$.
3. **Add a cross-model experiment**: use one LLM to generate concepts and a different (stronger) LLM to classify from them, to disentangle concept quality from reasoning ability.
4. **Expand the limitation section** to explicitly discuss the CRI-reasoning confound.
5. **Clarify the distractor selection** by specifying whether distractors are aggregated per-class or selected per-sample, and how the SSD is queried during main evaluation.

## Score and Decision

**Calibration procedure**: Three rounds of calibration_search were conducted.

### Round 1 — Bracketing
Three queries on topics similar to the paper (automated concept annotation evaluation, LLM self-consistency in XAI, concept bottleneck evaluation benchmarks):

| Query Band | Anchor | Avg Score | Comparison |
|---|---|---|---|
| Low (< 3.5) | kTjEPEy96Q (Framework for unsupervised CBMs) | 3.00 | Weaker: limited novelty, small experiments |
| Low (< 3.5) | KLUDshUx2V (Automating concept banks with LLMs) | 3.40 | Weaker: thin evaluation, limited scope |
| Middle (3.5–7.5) | RC5FPYVQaH (CB-LLM) | 5.75 | Comparable novelty, accepted; similar interpretive concerns |
| Middle (3.5–7.5) | lHbLpwbEyt (Enhancing cognition with self-synthesized data) | 6.00 | Stronger: clearer contribution, accepted |
| Middle (3.5–7.5) | kJgi5ykK3t (Logical consistency in LLMs) | 5.60 | Mixed (8,5,6,6,3); similar "framework + empirical study" structure |
| High (> 7.5) | uAFHCZRmXk (Modality gap in VLMs) | 8.00 | Much stronger: deeper analysis, clearer claims |

**Round-1 bracket**: 4.5–6.5. The paper is clearly above the 3.0-level papers (more novel framework, broader experiments) but below the 8.0-level papers (which have cleaner contributions and fewer interpretive issues).

### Round 2 — Narrowing within bracket
Two queries targeting topics close to the paper inside (4.5, 6.5):

| Anchor | Avg Score | Comparison |
|---|---|---|
| kJgi5ykK3t (Logical consistency) | 5.60 | Similar: proposes evaluation framework with empirical study; has some interpretive overclaims |
| wk77w7DG1N (Generation consistency) | 4.67 | Weaker: narrower scope, less novel |
| kFALGqLp46 (Sanitizing LLMs) | 5.33 | Similar: proposes a metric and empirical study |
| xrgXaOV6dK (Annotation quality for LLM-as-judge) | 5.50 | Similar topic area |
| zp88xOXAfS (Linear interpretable CEM) | 4.80 | Weaker: incremental method |
| tZk3LnvVtK (LLM uncertainty with concepts) | 5.60 | Similar: proposes metric with concept-based evaluation |

**Final calibration**: The paper is most comparable to papers in the 5.0–5.75 range. It has a genuinely novel framework and more comprehensive experiments than many papers at this level. However, the interpretive confound in the CRI metric (reasoning ability vs. concept quality) is a real concern that tempers the central claim. The paper is above reject-range papers (3.0–3.5) but not as clean as strong-accept papers (6.0+). At 5.0, the paper makes a solid contribution that can be strengthened with adjustments to framing and a few clarifications.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>