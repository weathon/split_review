Now I have enough calibration data. Let me write the consolidated review.

## Summary

This paper identifies an overlooked problem in VLM attribute-based few-shot learning: the "black sheep" phenomenon where a tiny fraction (<7%) of spuriously correlated attributes (e.g., "grass" for park bench, "sea" for fireboat) disproportionately influence VLM predictions and harm out-of-distribution generalization. The authors propose two complementary solutions: (1) Spurious Attribute Probing (SAP), which uses MLLMs + CBMs to automatically identify and filter spurious attributes from the attribute pool, and (2) Spurious Attribute Shielding (SAS), a plug-and-play module that constructs pseudo-categories from spurious attributes and adds an auxiliary classification loss to reduce reliance on them. SAS is shown to consistently improve multiple PEFT baselines across 11 datasets and 3 generalization tasks by ~2% on average, with a counter-group evaluation demonstrating that gains are concentrated on samples where spurious cues are absent.

## Strengths

1. **Well-motivated problem discovery with manual validation.** Section 3.2 and Table 1 show that manually removing <7% of spurious attributes boosts new-class accuracy by ~2.4% (CPL: 65.30→67.66; ArGue: 66.07→67.69) without harming base accuracy. This cleanly quantifies the phenomenon and grounds the paper's motivation in a concrete, reproducible observation.

2. **Comprehensive and consistent empirical results across multiple paradigms.** Figure 3 shows that SAS improves OOD accuracy across 11 datasets × 3 tasks for *multiple* PEFT approaches (CoCoOp, PromptSRC, CPL, MaPLe, TCP, etc.), with average gains >2%. The counter-group evaluation (Table 2) provides particularly compelling evidence: SAS nearly doubles the accuracy improvement on samples deliberately stripped of spurious attributes (e.g., PromptSRC on ImageNet: +5.49% on counter group vs +1.36% on full test set), demonstrating genuine robustness enhancement rather than mere in-distribution overfitting.

3. **Plug-and-play design with practical efficiency consideration.** SAS integrates into existing methods without architectural changes, using only an auxiliary loss. Table 5 shows a selective optimization trick (optimizing only 10% of categories) recovers most of the gain while reducing training overhead substantially (CoCoOp: 6h18m→4h51m), addressing a practical deployment concern.

4. **Ablation studies validate design choices.** Table 4 (γ threshold) confirms that the spurious attribute selection quality matters—too few (γ=0.8→HM 79.09) or too many false positives (γ=0.0→HM 79.44) both hurt, and the adaptive strategy outperforms all fixed thresholds (80.38). Table 3 shows that more diverse SD prompts improve results, validating the construction approach.

## Weaknesses

### Fatal
None.

### Major

1. **Missing direct validation that SAP recovers the same spurious attributes as manual identification.** The motivating study (Table 1) manually identifies spurious attributes and shows removing them helps. SAP is proposed as an automatic replacement, but the paper never compares SAP's output against these manual labels on the same datasets (e.g., precision/recall). The paper would be substantially strengthened by showing that SAP recovers the same attributes removed in the manual study, or at least that SAP-identified attributes overlap significantly with human-identified ones. Without this, it is unclear whether SAP is actually finding spurious attributes or simply filtering something else that also benefits OOD accuracy. The CBM+MLLM pipeline is plausible, but the chain-of-thought prompts used with GPT-4V are untested for this specific task.

2. **The effect of adding extra data (pseudo-categories) is not fully disentangled from the effect of specifically targeting spurious attributes.** SAS adds training images for pseudo-categories alongside real categories. While the γ ablation (Table 4) provides *indirect* evidence that the specific choice of spurious attributes matters (performance drops when γ is too high or low), a cleaner control would compare SAS against a variant using *random* or *core-attribute-based* pseudo-categories with the same number of additional images. Without this, the argument that gains come from spurious-attribute mitigation rather than the general benefit of more training data, additional regularization, or increased image diversity remains partially circumstantial.

### Minor

1. **Key numerical results (HM, Base, New) for the "new state-of-the-art" claim are presented only as scatter plots in the main paper.** The paper defers detailed numerical tables to Supp. Mat. E (removed by the parser). While figures give an overview, a main-paper table with at least the top combinations and key baselines would allow readers to directly inspect the evidence for the SOTA claim without consulting supplementary material.

2. **The similarity metric used for top-k image selection in pseudo-category construction is not specified.** The paper states "selecting top-k images that are most similar to the corresponding spurious attribute" (Section 3.4) but does not state whether this is CLIP cosine similarity or another metric. This is a reproducibility-relevant detail.

3. **No variance/error bars reported on main results.** The paper states results are averaged over three runs but does not report standard deviations or confidence intervals, making it difficult to assess the statistical significance of the ~1-2% improvements.

### Trivial

- The adaptive γ selection heuristic is described but its connection to the core-attribute weight distribution could be stated more precisely.

## Nice-to-Haves

- A control experiment using pseudo-categories constructed from non-spurious (core) attributes or random concepts would cleanly isolate whether the benefit is specific to spurious-attribute targeting versus additional data.
- A direct comparison of SAP's identified attributes against the Table 1 manual labels on 2-3 datasets would ground the probing method's accuracy.
- The paper relies on GPT-4V and Stable Diffusion, which are not deterministic. A brief discussion of reproducibility with these components and potential open-source alternatives would be useful.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"SAS is not controlling for data augmentation" framed as fatal.** The paper partially addresses this with the γ ablation (Table 4), showing that performance degrades when the spurious attribute selection quality is poor. Downgraded from fatal to major with a more precise framing.
- **"Zero prompts baseline missing in Table 3."** The baseline without SAS is already shown in Figure 3 (each plotted point is a baseline method; +SAS is the improvement). Requesting #p=0 in Table 3 would just recover the baseline, which is already compared.
- **"Counter-group evaluation is circular"** as presented in the critic. The counter group is defined using SAP-identified spurious attributes, and SAS is then evaluated on it. While this has a whiff of circularity, it is still informative: if SAS merely added noise, it wouldn't systematically help on this specific subset. The critic's own characterization ("somewhat circular, but still informative") is reasonable, so this is not a genuine weakness.
- **"Comparison to related spurious correlation methods in appendix"** is criticism about missing appendix content, which was stripped by the parser.
- **Pure presentation/style nitpicks** about formatting that are parser artifacts.
- **"Missing related work"** — I cannot confirm these claims.

## Novel Insights

The harsh critic's concern about the missing data augmentation control (random vs. spurious pseudo-categories) and the strength finder's overclaiming about causal evidence together reveal a deeper issue: the paper's empirical strategy relies on *indirect* evidence (γ ablation, counter-group evaluation) to argue that the benefit comes from targeting spurious attributes specifically. While these experiments are consistent with the causal claim, none of them cleanly rule out the hypothesis that *any* auxiliary classification task with extra data could produce similar gains. The counter-group experiment comes closest to causal identification but is itself defined using the same SAP attributes. A reviewer genuinely interested in the paper's core thesis would push hardest on this evidential gap. That said, the paper's strength—the manual study establishing the phenomenon independently of any method—is a genuinely nice empirical sanity check that many papers in this area lack.

## Suggestions

1. Run a control experiment: replace spurious-attribute pseudo-categories with (a) random-word pseudo-categories and (b) core-attribute pseudo-categories, keeping the number of additional images constant. Show that only spurious-attribute-based pseudo-categories yield the improvement.
2. On 2-3 datasets from Table 1, run SAP and report precision/recall against the manual spurious attribute labels. This directly validates the probing method.
3. Add a main-paper table (even a concise one) showing HM, Base, New for the top-5 baselines and their +SAP/+SAS variants, along with standard deviations over 3 runs.

## Score and Decision

**Calibration Report:**

*Round 1 (bracketing):* Weak anchors (<3.5): avg 2.50-3.00 (e.g., "Emergent Corpus Pretraining," "Ask Your Distribution Shift"). Middle anchors (3.5-7.5): avg 4.00-5.00 for topically-similar (SFR, LogicAI-PT, Unclipping CLIP's Wings). Strong anchors (>7.5): avg 8.00 (oral-level, e.g., "Two Effects, One Trigger"). Initial bracket: [4.0, 7.0].

*Round 2 (narrowing, 5.5-7.5):* AttrVR (avg 6.00, Accept Poster) — similarly about attributes+CLIP, comparable empirical scope, similar LLM-reliance weakness. CoPrompt (avg 5.75, Accept Poster) — similar 11-dataset evaluation, comparable contribution level but less novelty in the core idea. The paper under review sits between these two anchors but is slightly stronger than CoPrompt due to clearer motivation and a more novel problem framing. Compared to AttrVR, the scope is broader (3 tasks vs 1) but the missing-validation weakness is more salient.

*Final placement:* The paper is comparable to accepted poster-level work (5.75-6.00) in the VLM adaptation space. It identifies a genuinely overlooked problem, validates it with a clean manual study, and proposes two complementary solutions with extensive experiments. The two major weaknesses (SAP not validated against ground-truth labels; SAS data augmentation effect not fully disentangled) are real but addressable, and they do not invalidate the core contribution. The paper is stronger than the rejected spurious-correlation papers (SFR at 4.00, LogicAI-PT at 5.00) which had more fundamental issues. It is not at the oral level (8.00) where papers demonstrate exceptional depth or surprising insights beyond their own contributions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>