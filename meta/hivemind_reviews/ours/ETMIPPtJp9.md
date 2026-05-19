Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes FiDeLiS, a training-free retrieval-augmented reasoning method for Knowledge Graph Question Answering (KGQA). It combines two components: (1) Path-RAG, a keyword-enhanced retrieval mechanism that retrieves entities and relations from a vector-based KG index to build candidate reasoning steps, and (2) Deductive-Verification Beam Search (DVBS), which uses LLM-based deductive reasoning (rather than logit-based scoring) as a termination criterion during beam search over these candidates. Experiments on WebQSP, CWQ, and CR-LT show competitive or state-of-the-art results against both fine-tuned and prompting-based baselines, and the method is shown to be more efficient than the comparable training-free baseline ToG.

## Strengths

- **Training-free method achieves competitive or superior results against fine-tuned baselines.** Table 1 shows FiDeLiS with gpt-4-turbo achieves 84.39 Hits@1 on WebQSP (vs. RoG's 83.15 and DeCAF's 82.1) and 71.47 on CWQ (vs. RoG's 61.39). That a prompting-based method with no training on the answer distribution can match or exceed fine-tuned methods is a significant result, and the table cleanly separates "Prompting" and "Finetuning" families with explicit section headers.

- **Consistent and substantial efficiency gains over the primary training-free baseline (ToG).** Table 4 shows FiDeLiS reduces average runtime by ~40% on WebQSP (43.83s vs. 74.26s) and ~44% on CWQ (74.59s vs. 132.59s) relative to ToG, while also achieving higher Hits@1. This directly supports the claim of reduced computational cost.

- **Ablation study cleanly quantifies the contribution of each component.** Table 2 shows that removing beam-search drops Hits@1 by 18.97% on WebQSP (60.35 vs. 79.32), removing Path-RAG via a vanilla retriever drops 6.97%, and removing the deductive verifier drops 5.19%. These are substantial and consistent across datasets, providing direct evidence that both modules matter.

- **Path-RAG's retrieval improvement is validated across multiple embedding backbones.** The table comparing Vanilla Retriever vs. Path-RAG across BM25, SentenceBert, E5, and OpenAI embeddings shows Path-RAG outperforms the vanilla retriever in every configuration (e.g., 79.32 vs. 72.35 on WebQSP with OpenAI embeddings), demonstrating that the benefit is not tied to a single embedding model.

## Weaknesses

### Fatal

None.

### Major

- **The core claim of "faithful reasoning" (in the title and throughout) is not directly measured for FiDeLiS itself; only a baseline error is reported.** Section 4.2 ("Error analysis regarding whole path generation") defines the validity ratio (VR) metric and reports that RoG's reasoning paths are only 67% valid. This is used to motivate FiDeLiS's design, but the paper never reports FiDeLiS's own validity ratio. Since the method is *designed* to ensure every step is KG-grounded (retrieval from the KG + deductive verification), one would expect near-100% VR, but this is asserted rather than demonstrated. The paper even says "To verify the faithfulness of our stepwise method" (line 354) and then only analyzes RoG. This is a direct evidential gap for the paper's central framing. The authors could fill this gap straightforwardly by running the same VR analysis on FiDeLiS's own paths.

### Minor

- **The deductive verification component's benefit is shown through plausible but indirect evidence.** The primary evidence is (a) ablation results showing a 5.19% (WebQSP) / 5.89% (CWQ) drop when removing the verifier, and (b) average reasoning depths closer to ground-truth than ToG's. However, the paper does not compare against simpler termination heuristics (e.g., fixed depth limit, confidence threshold), nor does it provide a qualitative analysis of cases where the verifier prevented an incorrect path. The claim that deductive verification "avoids misleading reasoning chains and reduces unnecessary computational demand" would be materially stronger with such controls. This does not invalidate the contribution but weakens the evidence for one of its signature components.

- **Key hyperparameter α (Eq. 3) is described functionally but not given a default value.** Line 118 explains that α balances short-term and long-term scoring, but the paper does not specify what value was used in the experiments or show a sensitivity analysis. Similarly, the top-*m* retrieval count (Eq. 2, line 105) and the number of generated keywords are not specified. These affect reproducibility.

- **"Ground-truth reasoning paths" are not clearly defined.** The coverage ratio analysis (Figures 2a–b) depends on comparing retrieved paths to "ground-truth reasoning paths," but the paper does not explain how these ground-truth paths are determined. In KGQA, the ground truth is answer entities, not paths — so are these shortest paths? All possible paths? A definition is needed for the metric to be interpretable.

### Trivial

- The Notation section (Section 3, lines 71–74) partially repeats content from the Preliminary section (Section 2, lines 54–58). Redundant but harmless.

## Nice-to-Haves

- **Prompt templates used throughout** (keyword generation, deductive verification, planning) are not provided in the main text. The paper promises code release, but including the prompts (even in a supplementary) would aid reproducibility.
- **Run-to-run variance or statistical significance** would strengthen confidence in the reported margins, particularly for close comparisons (e.g., 84.39 vs. 83.15 on WebQSP). However, single-run evaluation with expensive API calls is the norm in this area.
- **A failure case analysis** (what types of questions does FiDeLiS struggle with?) would round out the evaluation, which currently focuses on successes.

## Removed Points

These points were raised by reviewers but are removed as per the filtering rules. Treat with caution:

1. **"Comparison with fine-tuned baselines conflates two fundamentally different settings"** — REMOVED. The paper's Table 1 explicitly separates methods into "Prompting - LLM Only," "Finetuning - LLM + KG," and "Prompting - LLM + KG" with clear section headers. The abstract and text note that FiDeLiS is "training-free." The paper is transparent about the comparison landscape; the numbers are simply presented as reported.

2. **"The case study appears cherry-picked"** — REMOVED. This is speculative and not grounded in specific evidence about the distribution of cases. Case studies are illustrative by nature.

3. **"The green shading in ablation table is arbitrary"** — REMOVED. This is a presentation nitpick. The table also reports Δ values numerically, so the shading is supplementary.

4. **"Notation section repeated from Preliminary"** — MOVED to Trivial. It is a minor redundancy but not a substantive weakness.

## Novel Insights

The two reviews independently notice the same core issue: the paper claims "faithful reasoning" prominently but provides no direct empirical measurement of its own method's faithfulness (validity ratio), only a negative result on a baseline. This is the single most impactful issue to address because it sits at the intersection of the paper's main claim and its weakest evidence. Neither reviewer noticed that the paper could trivially compute this metric since every step is KG-retrieved — the gap is in reporting, not design.

## Suggestions

1. **Report FiDeLiS's own validity ratio** using the same VR metric defined for RoG in Section 4.2. This directly operationalizes the paper's faithfulness claim and would be the single most impactful addition.
2. **Disclose the default value of α** (Eq. 3) and, ideally, include a brief sensitivity analysis (α ∈ {0, 0.5, 1.0, 2.0}) to show robustness.
3. **Clarify how "ground-truth reasoning paths" are constructed** in the coverage ratio analysis (e.g., shortest paths between topic and answer entities? all possible valid paths?).
4. **Consider adding a simple baseline** for the deductive verification component's termination criterion (e.g., a fixed depth limit) to better isolate its benefit.

## Score and Decision

The paper presents a well-motivated, training-free KGQA method with strong experimental results and clear efficiency gains over comparable approaches. The primary weakness is an evidential gap: the central "faithful reasoning" claim lacks direct measurement for the proposed method itself. This is not fatal (the gap is easily closed by reporting a metric the paper already defines and the method is designed to satisfy by construction), but it prevents the paper from being a top-tier contribution as currently presented. The remaining issues are minor.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>