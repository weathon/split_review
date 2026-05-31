## Summary

This paper investigates whether LLMs can develop human-aligned semantic category systems guided by the Information Bottleneck (IB) principle—specifically whether IB-efficiency, which underlies cross-linguistic universals in human color naming, can emerge in LLMs without explicit training for that objective. The authors conduct two main experiments with 39 LLMs: (1) an English color naming study benchmarked against human data via IB complexity-accuracy analysis, and (2) a novel "Iterated In-Context Language Learning" (IICLL) paradigm that simulates cultural transmission of pseudo color-naming systems to elicit LLMs' inductive learning biases. Results show that larger instruction-tuned models better align with English color naming, and that over IICLL generations, all tested models evolve random color-naming systems toward greater IB-efficiency and human alignment—with Gemini 2.0 uniquely covering the full range of human typological diversity.

---

## Strengths

- **Rigorous, theory-driven evaluation framework.** Using the IB principle from Zaslavsky et al. (2018) as the analytical lens is well-grounded, offers precise quantitative predictions, and has strong prior empirical support across human languages. The use of efficiency loss, NID-based alignment (English, WCS, IB), and the rotation analysis (Regier et al., 2007) provides a multi-angle evaluation that goes well beyond superficial accuracy metrics.

- **Large-scale, systematic model comparison.** Testing 39 models across 6 families, varying size, instruction-tuning, modality, and (for OLMo) training checkpoints is unusually thorough. This enables principled conclusions about which factors (model size, instruction-tuning) drive IB alignment, rather than relying on a single cherry-picked model.

- **Novel IICLL paradigm with direct human-experiment replication.** Extending I-ICL to iterated *language* learning and closely replicating the experimental conditions of Xu et al. (2013) is a genuine methodological contribution. Using pseudo-labels and presenting stimuli without revealing that they encode color provides a reasonable design to disentangle emergent inductive biases from surface-level imitation of training data.

- **Convergence across qualitatively different models.** The finding that all four large instruction-tuned models evolve random systems toward near-optimal IB solutions—despite differences in architecture, training, and coverage—is notable evidence for a robust emergent behavior, not an idiosyncrasy of one model.

- **Honest reporting of differential results.** The authors transparently report that only Gemini 2.0 replicates the full *range* of human IB diversity, while others converge to low-complexity solutions, and they propose an interpretable mechanism (in-context learning capacity) for this asymmetry. This is preferable to overstating uniformity across models.

---

## Weaknesses

### Fatal
None.

### Major

1. **Training data contamination in the IICLL paradigm is only partially addressed.** The use of pseudo-labels and omission of the word "color" is a reasonable mitigation, but frontier LLMs such as Gemini 2.0 have almost certainly encountered substantial text about IB theory, color naming universals, and iterated learning experiments during training. The claim that the emergent IB-efficiency reflects an "inductive bias" rather than recalled knowledge of the normative literature is the central empirical claim of the paper, yet the evidence against the contamination alternative is indirect. A stronger control would be to compare against a domain with no known literature encoded in LLM training data (Shepard circles are offered, but without IB quantification—see below). The rotation analysis (Appendix H) helps but only shows that random rotations degrade efficiency, not that the model is generalizing from first principles rather than stored knowledge.

2. **The Shepard circles extension is too preliminary to support the domain-generality claim.** Section 4.3 presents only a qualitative visual inspection of four chain samples, with no IB efficiency analysis, no alignment metric, no statistical test, and no comparison to human data. Yet the abstract and discussion repeatedly invoke domain generality as a contribution. Without IB quantification for Shepard circles, the claim that "LLMs have a domain-general bias to organize features into… increasingly regular, semantic categories" is not demonstrated by the paper's own evidence.

3. **Heavy reliance on Gemini 2.0 for the headline findings.** The full-range IB coverage result—the strongest claim of human-like diversity—is demonstrated by only one proprietary, closed-weight model. Because its training details are unknown, it is impossible to rule out targeted data contamination, fine-tuning on categorization tasks, or other confounds specific to Gemini. The finding does not transfer to open-weight models at the same level, limiting interpretability and reproducibility of the most prominent result.

### Minor

- The finding that image input does not improve (and can harm) larger models' color naming alignment is interesting and counterintuitive, but is discussed only briefly without a mechanistic hypothesis. This has practical implications for multimodal grounding research.

- The OLMo training checkpoint analysis is mentioned in the main text but deferred entirely to the appendix; even a single summarizing sentence about the shape of the learning curve would strengthen the narrative about instruction-tuning's role.

### Trivial

- Figure captions are reproduced multiple times in the text (likely a parser artifact).

---

## Nice-to-Haves

- A direct test of whether models that have *not* been exposed to IB/color-naming literature in training (e.g., models trained from scratch on controlled corpora) still converge to IB-efficient systems would greatly strengthen the inductive-bias interpretation.
- Quantitative IB analysis for the Shepard circles domain (even approximate) would make the domain-generality argument empirical rather than suggestive.
- Reporting per-condition (k=2,3,4,5,6) IICLL trajectories in the main text would clarify how much of the aggregate improvement is driven by low-k chains that trivially converge to IB-efficient solutions.

---

## Novel Insights

The IICLL paradigm is a concrete and reusable methodological bridge between cognitive-science iterated learning and LLM evaluation, going beyond prior I-ICL work by enabling direct experimental comparison to human ILL studies. The finding that cultural transmission pressure alone—without communication or explicit IB optimization—is sufficient to drive LLMs toward near-optimal IB-efficient category systems is a genuinely new and theoretically interesting result. It suggests that certain structural pressures known to drive human language universals (compressibility, generalization from limited data) may be absorbed by LLMs from their training distribution even without explicit grounding, and that the IB efficiency observed at the level of language populations may partly reflect individual learning biases that transfer across substrates.

---

## Suggestions

- Quantify IB efficiency and alignment for the Shepard circles chains or remove the domain-generality claim from the abstract/discussion until this is done.
- Add a discussion or ablation specifically addressing the training-data contamination hypothesis for Gemini: e.g., does Gemini converge to IB-efficient solutions in IICLL even when the pseudo-labels are entirely novel (e.g., assigned randomly anew for each chain), or does performance degrade in ways suggesting reliance on memorized associations?
- Provide per-condition (per-k) IICLL curves at least in the appendix to allow readers to assess whether complexity-diversity in Gemini arises from multi-condition averaging or genuine within-condition diversity.

---

## Score and Decision

The paper makes a solid, well-motivated contribution to understanding LLM cognition through a principled cognitive-science framework. The IICLL paradigm is novel and reusable, the evaluation is thorough and systematic, and the findings are honestly reported. The major concerns—training data contamination, the preliminary Shepard circles analysis, and the reliance on one proprietary model for the strongest result—are real but do not invalidate the core findings; they bound their interpretation. The paper advances knowledge at the intersection of cognitive science, information theory, and LLM behavior in ways that will interest a broad ICLR audience.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>