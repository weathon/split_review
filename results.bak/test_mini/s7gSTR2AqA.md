Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper investigates whether LLMs exhibit a human-like inductive bias toward Information Bottleneck (IB) efficiency in semantic categorization. Using color naming as a testbed, the authors first benchmark 39 LLMs on English color naming and find that only larger instruction-tuned models approach human-level alignment. They then introduce Iterated In-Context Language Learning (IICLL) — a method that simulates cultural transmission of category systems through iterative in-context learning — and show that LLMs restructure randomly initialized pseudo-term systems toward greater IB-efficiency. Notably, only Gemini 2.0 recapitulates the full range of near-optimal tradeoffs observed across human languages. A rotation analysis and convergence from random initializations rule out mere training-data mimicry. The paper also provides preliminary evidence for domain generality via Shepard circles. The work combines the IB theoretical framework with iterated learning to make a theory-driven empirical contribution at the intersection of cognitive science and LLM evaluation.

## Strengths

- **Novel paradigm (IICLL) with direct human comparison.** The IICLL method adapts iterated learning to LLMs via in-context learning, enabling direct quantitative comparison between LLM cultural evolution dynamics and human behavioral data from Xu et al. (2013). This is a well-motivated methodological contribution that goes beyond prior I-ICL work by targeting semantic category structure rather than factual knowledge elicitation (Section 2.3, Figure 1c).

- **Convergence to near-optimal IB solutions is compelling and multi-evidenced.** Figure 3 shows that Gemini's IICLL trajectories converge to the same range of complexity-accuracy tradeoffs as human languages (WCS) and human iterated learning data. This is quantitatively reinforced by Figure 4 (efficiency loss, IB-alignment, WCS-alignment over generations, all with 95% CIs) and by a rotation analysis (Appendix H) that shows rotating the color-label mapping along hue significantly degrades efficiency and alignment — ruling out the possibility that the observed structure is an artifact of the color space rather than a genuine inductive bias (Section 4.2, line 153).

- **Broad and systematic model evaluation.** The paper tests 39 models across 6 families (Gemini, Gemma, Llama, Qwen, Olmo, GPT-2), varying size, instruction-tuning, and modality. This allows identification of clear trends (size + instruction-tuning → better alignment) while also surfacing surprising findings (e.g., some models produce systems resembling low-resource WCS languages rather than English). The Olmo checkpoint analysis further isolates when during training these categories emerge (Section 3, Figure 2c, Appendix F).

- **Rotation analysis and random-initialization controls are strong evidence against mimicry.** The IICLL experiments start from randomly-initialized pseudo-term systems, with pseudo-terms and no indication that stimuli are colors (only "features"). The rotation analysis shows that the emergent structure is causally tied to the specific color-label mapping. Together these rule out the trivial explanation that the model is simply reproducing memorized patterns from training data (Section 4.2, Appendix H).

- **Theoretical grounding in the Information Bottleneck framework.** The use of IB theory grounds the analysis in a well-established framework with proven empirical support across human languages. Metrics like efficiency loss and NID-based alignment are precisely defined and allow quantitative comparison to optimal systems and human data (Section 2.2).

## Weaknesses

### Fatal
None.

### Major

1. **The Shepard circles experiment does not quantitatively support the paper's central IB-efficiency thesis.** The analysis is purely qualitative — visual inspection of category maps showing partitions becoming more compact. No IB complexity-accuracy computation is performed for this domain, no alignment to human data is reported, and there is no comparison baseline (random chains or clustering baseline). The paper itself labels this a "preliminary investigation" and states that testing whether this structure supports IB-efficiency is "an important direction for future work." This is honest, but it means the experiment contributes no evidence for the paper's core claim about IB-efficiency as a domain-general principle — it only shows that LLMs can develop *some* structured categories in a non-color domain. The paper would be stronger either by removing this section or by providing a quantitative IB analysis (which would require constructing a perceptual similarity metric and computing the IB bound for the Shepard stimulus space).

2. **The claim that IICLL "replicates as closely as possible the experimental conditions of ILL studies" is overstated.** In Xu et al. (2013), human participants learn from a small training set through memorization and generalization, while IICLL provides all examples in a single prompt for in-context pattern matching. This representational difference means the mechanism driving regularization is different: humans compress through memory limitations, while LLMs compress through whatever inductive biases govern in-context generalization from limited examples. The paper acknowledges this distinction implicitly by calling it a new paradigm (IICLL), but the phrase "replicates as closely as possible" (Section 2.3) invites a stronger analogy than the evidence supports. The paper would benefit from explicitly discussing how this difference might affect the results — e.g., does reducing the number of in-context examples increase regularization pressure toward simpler systems (as it would for humans)?

### Minor

3. **The rotation analysis reports "significant decrease" for Gemini without providing numerical statistics (p-values, effect sizes, or confidence intervals) in the main text.** Figure 11 is in the appendix (stripped from the submission), and the main text only states the qualitative finding. While 95% confidence intervals are shown in Figure 4 for the main IICLL trajectories, the rotation analysis lacks comparable statistical reporting. The claim that "Gemini's efficiency and alignment over generations are higher than the human IL trajectories" is also made without precise comparison — it is ambiguous whether this means the *average trajectory* is higher or the *final states* exceed the human data, and the paper should clarify what is being compared.

4. **The CIELAB coordinate finding may reflect a training data confound rather than a perceptual difference.** The paper reports that using CIELAB (which better captures human perceptual similarity) hurts all models' color naming performance, and frames this as a "key difference between how LLMs represent color and how humans do." However, CIELAB coordinates are far rarer in web text than sRGB coordinates (the standard for digital displays), so the degradation may simply reflect distributional mismatch in training data rather than a fundamental limitation in how LLMs represent color. The paper should acknowledge this confound explicitly.

### Trivial

None.

## Nice-to-Haves

- A systematic ablation varying the number of IICLL in-context examples per category (e.g., 1, 3, 5, 10) would help characterize the strength of the inductive bias and clarify the analogy to human iterated learning, where training set size directly affects regularization.
- For the Shepard circles experiment, computing an IB bound using feature-space distances (raw radius and angle) and plotting IICLL trajectories on that information plane would connect the experiment to the paper's central claim.

## Removed Points

**These points are flagged to be removed; treat them with caution.**

- *Underspecified IICLL sampling strategy (Critical Issue 2 from Harsh Critic):* The critic notes that the number of examples per category and the sampling procedure are not fully specified in the main text. The paper states "see Appendix G for more details" (Section 4.2, line 133), and the code is publicly released at the provided URL. Since the appendix content is stripped by the PDF parser and the code repository is referenced, this is not a verifiable gap in the submission as written. The information is likely present in the full submission.

- *Strength about "Generalization beyond color to Shepard circles" (from Strength Finder):* This strength claims that the Shepard circles experiment "directly supports the claim that the bias toward non-arbitrary semantic organization may be domain-general." The paper is appropriately cautious about this ("potentially have a domain-general bias," "preliminary investigation"), and the experiment provides only qualitative evidence that LLMs can develop structured categories in another domain — it does not demonstrate IB-efficiency or human-alignment in that domain. Since this conflicts with verified weakness #1, it is removed.

- *Several generic strengths from the Strength Finder:* The strength about "Systematic evaluation across 39 models" and "Introduction of IICLL" are retained as specific and evidence-backed. The strength about "Use of the IB framework for quantitative evaluation" merges into the retained strengths above.

- *The critic's suggestion about varying IICLL example count* is moved to Nice-to-Haves rather than listed as a weakness.

- *The critic's point about the analogy between IICLL and human IL being weakened* has been retained in Major (point 2) but reframed from a "Critical Issue" to "Major" since the paper's core claims do not depend on perfect replication of the human protocol — the IICLL results stand on their own as demonstrations of IB-efficiency emerging through cultural transmission in LLMs.

## Novel Insights

The most striking finding is not just that LLMs can produce IB-efficient systems (this could be explained by training data patterns), but the *asymmetry* between models revealed by the IICLL paradigm: Gemini 2.0 recapitulates the full typological range of human IB tradeoffs, while other frontier models (Gemma 3 27B, Llama 3.3 70B, Qwen 2.5 32B) converge to low-complexity solutions despite performing comparably on the static English naming task. This differential behavior in cultural evolution — where the static naming benchmark does not predict the IICLL outcome — is itself a novel empirical finding that suggests IICLL probes a different dimension of model competence than static benchmarks. The fact that many trajectories initially *climb* in complexity before descending along the IB bound (Section 4.2, line 151) is another interesting dynamical signature that bears further investigation.

## Suggestions

1. Provide quantitative IB analysis for the Shepard circles experiment, or remove the section. The current qualitative evidence does not strengthen the paper's core claims.
2. Add statistical details (p-values, effect sizes) for the rotation analysis to the main text.
3. Clarify the comparison when stating Gemini's efficiency/alignment is "higher than the human IL trajectories" — specify whether this refers to trajectory-level averages, final generations, or specific tradeoff points.
4. Acknowledge the CIELAB training-data confound explicitly.
5. Add a brief discussion of how the IICLL-vs-human-IL representational difference (in-context vs. memorization) might affect the interpretation of the results.

## Score and Decision

**Round 1 — Bracketing:** I queried for similar papers across three bands: weak (score < 3.5), middle (3.5–7.5), and strong (> 7.5). Weak anchors included *Color Names in VLMs* (2.00) and *Beyond Natural Language* (3.00), which are substantially shallower in both theoretical depth and experimental scope. Middle anchors included *From Tokens to Thoughts* (6.00), *Language and Experience* (6.40), *On the Relationship Between Representation and ICL* (5.00), and *LLMs Develop Novel Social Biases* (4.67). Strong anchors (*Mixing Mechanisms* 8.00, *LLMs Get Lost In Multi-Turn* 8.00) are topically distant. **Initial bracket: 5.0–7.5.**

**Round 2 — Narrowing:** I targeted the 4.5–6.5 and 5.5–8.0 ranges with topic-specific queries. The closest comparator is *From Tokens to Thoughts* (6.00, Accept Poster), which similarly applies IB theory to compare LLMs and humans on categorization. The paper under review is stronger on several dimensions: (a) IICLL is a more causally informative paradigm than embedding extraction; (b) the cultural-evolution design with random initializations and rotation controls provides stronger evidence for inductive bias than static embedding comparisons; (c) the direct parallel to human iterated learning data (Xu et al. 2013) grounds the results in established cognitive-science findings. However, the paper is held back from the 7+ range by the qualitative-only Shepard circles analysis and the somewhat overstated IICLL-replication claim. Compared to the other anchors in this range — *Language and Experience* (6.40) and *On the Relationship Between Representation and ICL* (5.00) — this paper is clearly above the latter in novelty and impact and comparable to the former in quality. The paper sits at the upper end of the 6.0–6.5 range: stronger than a typical 6.0 paper due to its novel paradigm and comprehensive evaluation, but not reaching 7.0 due to the weaknesses noted above.

**Final Score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>