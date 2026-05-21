Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes the **Fast and Slow Effect (FSE)** framework, an automatic evaluation method for assessing whether LLM/VLM-generated concept annotations are semantically sufficient to discriminate target classes. The framework progressively refines textual concepts from coarse to fine (5 stages), compares classification from raw visual input ("fast mode") against classification from accumulated textual concepts ("slow mode"), and introduces the **Class Representation Index (CRI)** to quantify annotation sufficiency. Experiments across 6 models (GPT-4o, Qwen2-VL, Llama3.2 families) and 5 datasets show that: (1) slow mode underperforms fast mode by ~25% on fine-grained datasets, (2) LLMs perform well on coarse-grained datasets, and (3) high downstream accuracy does not imply annotation sufficiency (the "utility-as-proxy" assumption is invalid).

## Strengths

1. **Systematic empirical evidence of annotation insufficiency**: Table 2 reports negative CRI-Gap values averaging -25% to -27% across three fine-grained datasets and six LLMs. Figure 3 shows that even with five-step concept chains, CRI scores on fine-grained datasets remain below 70% (post-hoc) and below 60% (visual-grounded). This breadth of evidence (3 model families × 2 sizes each) makes the finding robust.

2. **Critical debunking of the utility-as-proxy assumption**: Table 4 shows fused mode (fast + slow) achieves ~90% CRI while slow mode alone achieves only ~50-60%. This empirically demonstrates that strong end-to-end performance does not imply annotation sufficiency — a central methodological claim of the paper that challenges a common practice in the field.

3. **Fully autonomous, scalable evaluation framework**: The FSE framework requires no human supervision for either annotation generation or evaluation. Given the well-documented cost and subjectivity of human evaluation for concept annotations, this addresses a genuine scalability bottleneck.

4. **Empirically grounded distractor selection**: The preliminary experiment (Table 1) shows semantically related distractors yield 34-45% contradiction rates vs. 14-20% for random selection, justifying the more challenging evaluation setup. This methodological care prevents the evaluation from being artificially easy.

5. **Principled definition grounding the framework**: Definition 3.1 formally defines annotation sufficiency ("concepts alone enable accurate inference"), providing a clear, reusable foundation that future work can build upon.

## Weaknesses

### Major

1. **CRI conflates concept annotation quality with the LLM's reasoning ability**: Definition 3.1 frames sufficiency as a property of the concepts themselves — whether they are "expressive, clear, and precise enough to enable accurate inference." The CRI operationalizes this by testing whether *the same LLM* can classify from its own textual concepts ($y_i^t = \mathcal{F}(c_i^t; \Theta)$). This conflates two distinct phenomena: (a) whether the concepts are semantically precise, and (b) whether the LLM can reliably reason from its own textual outputs. A low CRI could mean the concepts are genuinely insufficient, or it could mean the LLM generates decent concepts but cannot consistently reason from them (a self-consistency failure). The paper acknowledges this partially in the abstract ("it remains challenging for them to conceptualize this knowledge in the slow mode") and results section, but the framing throughout — "CRI quantifies how sufficiently the accumulated concepts support accurate concept-class mapping" (Section 4.2) — presents it as a pure measure of annotation quality rather than a joint measure. This does *not* invalidate the paper's findings (the practical observation that concepts don't support reliable inference is meaningful regardless of root cause), but it weakens the specific claim about measuring "annotation sufficiency" as an intrinsic property of the concepts.

### Minor

2. **CRI-Gap compares fundamentally different information modalities**: The fast mode (t=0) uses rich pixel-level visual information, while the slow mode (t>0) uses only textual descriptions. A negative CRI-Gap could simply reflect that visual information is inherently richer for fine-grained visual classification than any textual description, independent of annotation quality. The paper interprets the gap as revealing insufficient "semantic coverage," but this conclusion would need an alternative baseline — e.g., having a human expert write the best possible textual description and testing whether the LLM can classify from *that*. Without such a control, it is unclear how much of the gap is due to poor annotation vs. the inherent poverty of the textual modality for this task.

3. **Utility-as-proxy debunking relies on only 2 models from a single family**: The main experiments cover 6 models across 3 families, but the important Table 4 (debunking the utility-as-proxy assumption) only tests GPT-4o and GPT-4o-mini. Given that this is one of the paper's headline findings, testing on additional model families (QwenVL2, Llama-3.2-vision) would substantially strengthen the claim.

4. **The "Slow Mode Superiority" hypothesis is questionable**: The paper hypothesizes that slow mode should outperform fast mode, citing dual-process theory (Kahneman, 2011). But expecting textual descriptions of fine-grained visual features to outperform direct visual recognition is a strong — and arguably counterintuitive — assumption. Information theory predicts information loss in the visual→textual transformation. The fact that the hypothesis fails is interesting, but the hypothesis itself seems set up to fail. The paper would be stronger by framing the comparison more neutrally from the start.

### Trivial

5. **Missing reproducibility link**: Line 327 states "We have provided the code and data at here" without an actual URL. This needs to be added for the camera-ready version.

## Nice-to-Haves

- Extend the "fused mode" experiment (Table 4) to at least the QwenVL2-72b and Llama-3.2-vision-90b models to test whether the utility-as-proxy finding generalizes beyond GPT.
- Include a human-written concept baseline for a subset of classes to quantify how much of the slow-mode gap is due to annotation quality vs. modality differences.
- Report sample-level results or per-class analyses to show whether insufficiency is uniform or concentrated on certain class types.

## Removed Points

- **Harsh critic's claim that the CRI issue "invalidates" the paper's core claims**: I verified the paper content. The paper defines sufficiency in Definition 3.1 and operationalizes it via CRI. The confound is real but the paper acknowledges the alternative interpretation (e.g., abstract: "it remains challenging for them to conceptualize this knowledge"). The finding is practically meaningful regardless of root cause. Demoted from "fatal" to "Major."

- **Harsh critic's claim that the paper should be reframed around "Do LLMs rely on their own concepts consistently?"**: The paper's framing around annotation sufficiency is legitimate given the practical context (these concepts are intended for use in concept-based XAI pipelines). The confound is a limitation to disclose, not a reason to overhaul the paper's framing. Removed as overreach.

- **Strength Finder's generic strengths about "important problem" and "timely topic"**: These are generic and not specific to the paper's evidence. Removed per filtering rules.

- **Strength Finder's claim about CRI having "clear interpretation" without caveat**: The CRI's interpretation as a pure measure of annotation sufficiency is the very thing weakened by Weakness #1. Modified to note the caveat.

## Novel Insights

Beyond the paper's own contributions, the most striking cross-cutting insight emerges from comparing the FSE framework with concurrent work on LLM self-evaluation (SelfReflect, Sage). These papers independently find that LLMs are poor at self-assessing their own outputs — SelfReflect shows LLMs cannot faithfully express their internal answer distributions, Sage shows LLMs are inconsistent judges. The current paper adds a new dimension: even when generating concepts that *should* support classification, the LLM cannot reliably use those concepts to make correct inferences. The pattern across all three works suggests a general limitation: LLMs have a gap between what they "know" (as evidenced by direct performance) and what they can articulate, summarize, or reason about in textual form. This paper's contribution is distinctive in showing that this gap specifically undermines the reliability of automated concept annotation for XAI — a finding that has direct practical implications for how the field should validate explanations.

## Suggestions

- **Address the reasoning-vs-annotation confound**: Add a brief experiment or discussion where you test whether a different LLM (or a human reading the concepts) can classify correctly from the generated concepts. If model B or a human can classify from model A's concepts but model A cannot, this would isolate the reasoning failure. If no agent can classify from them, this would confirm annotation insufficiency.
- **Add a human-written concept control**: For a subset of fine-grained classes (e.g., 10 CUB bird species), have a domain expert write the best textual descriptions, then compute CRI. This would bound how much of the gap is due to the modality (text vs. vision) vs. annotation quality.
- **Extend Table 4 to QwenVL2 and Llama-3.2-vision families** to test generality of the utility-as-proxy finding.
- **Add sample qualitative analysis** showing concrete examples of insufficient vs. sufficient concept sets, to illustrate what the CRI numbers mean in practice.

## Score and Decision

**Calibration**: 

Round 1 bracketing placed this paper between the weak band (< 3.5) and the strong band (> 7.5), in the middle band (3.5-7.5). The most topically similar anchors were M-CBM (5.50, Poster), Chat-CBM (4.00, Reject), and Probing Boundaries of Concepts (4.50, Reject).

Round 2 narrowing retrieved additional anchors within the bracket: Sage (5.00, Reject), SelfReflect (5.50, Poster), Adaptive Concept Discovery (5.20, Poster), and DeepTRACE (6.00, Poster). Reading the full reviews of the most comparable papers:

- **M-CBM (5.50, Poster)**: Closest in topic (CBM + concept annotation). Had leakage concerns similar in severity to this paper's confound issue. Accepted as Poster. The current paper has cleaner methodology and more extensive model coverage. Slightly stronger.
- **SelfReflect (5.50, Poster)**: Similar structure — proposes metric + uses self-evaluation + reports negative finding. Also had a confound concern (judge LLM vs. measured LLM were different). Accepted as Poster. Comparable quality.
- **Adaptive Concept Discovery / StructCBM (5.20, Poster)**: Concept-based method paper. Accepted as Poster. The current paper is stronger in experimental breadth.
- **Sage (5.00, Reject)**: Evaluation framework for LLM-as-a-Judge. Rejected due to proxy validity concerns. The current paper has a tighter connection between its metric and its construct.

The paper is clearly stronger than the weak band (1-3) papers and sits comfortably in the 5-6 range. Comparing against the most directly comparable accepted posters (M-CBM at 5.50, SelfReflect at 5.50), this paper is of similar quality with perhaps slightly stronger empirical breadth. The main methodological concern (Major Weakness #1) is real but does not invalidate the core finding, and is comparable in severity to the leakage concerns in M-CBM, which was accepted.

The paper is **better than** Sage (5.00, Reject), **comparable to** M-CBM (5.50, Poster) and SelfReflect (5.50, Poster), and **comparable to slightly stronger than** Adaptive Concept Discovery (5.20, Poster).

| Anchor Path | Avg Score | Round | Comparison |
|---|---|---|---|
| ETe03Iyluy.md | 3.00 | 1 | Much weaker — unclear contribution, limited evaluation |
| PxYlYQ6orQ.md | 2.00 | 1 | Much weaker — text annotation framework without clear XAI connection |
| mqNKv0brqk.md | 1.00 | 1 | Much weaker — sparse interpretability benchmark |
| gdEWoxhb70.md (M-CBM) | 5.50 | 1,2 | Comparable — similar type of contribution concern (leakage vs. confound), similar empirical effort |
| Ylgds6UMxf.md (Chat-CBM) | 4.00 | 1 | Weaker — criticized as prompt engineering, less novel contribution |
| BQ0jaVCZRK.md | 4.50 | 1 | Weaker — narrower scope, fewer experiments |
| Qtq5YjnIlB.md | 4.67 | 2 | Different topic (reasoning self-evaluation) — lower empirical breadth |
| JFTSZa2stt.md (Sage) | 5.00 | 2 | Weaker — proxy validity concerns, narrower evaluation |
| hOErnDsehG.md (SelfReflect) | 5.50 | 2 | Comparable — similar structure (metric + negative finding + confound issue) |
| UZBQ7iZzYz.md (StructCBM) | 5.20 | 2 | Comparable — slightly narrower scope |

Final score: **5.5** — a solid paper with a clear contribution, extensive evaluation, and one significant but not fatal methodological limitation that should be addressed.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>