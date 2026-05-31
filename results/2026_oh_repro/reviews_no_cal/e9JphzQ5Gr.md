## Summary
The paper proposes **CaPT (CLIP as a Prior Teacher)**, an asymmetric co-training framework for semi-supervised image classification that combines (i) a fully fine-tuned unimodal SSL model and (ii) a parameter-efficiently tuned CLIP branch. The two branches exchange information via a **co-pseudo label** fusion scheme and report very large gains in extreme low-label regimes, especially **1 label per class** (e.g., CIFAR-100: 82.51 vs ~61 in Table 3).

## Strengths
- **Very strong results in extreme low-label SSL, including 1-shot.** Table 3 reports large improvements over FreeMatch/RegMixMatch, e.g., **CIFAR-100 1-shot: 82.51 (CaPT) vs 61.13/60.49**, and **EuroSAT 1-shot: 96.33 vs 92.28/90.12** (Table 3, lines 236–241).
- **Consistent gains across multiple standard SSL benchmarks and label budgets.** Under the USB-style settings, CaPT is best across the shown settings (Table 1 is referenced in text; the paper emphasizes “consistently achieves state-of-the-art performance across multiple SSL benchmarks” in Abstract, line 9).
- **Ablation support for key components (bidirectionality / CLIP-PEFT / design choices).** The paper includes component analyses (Table 6 is discussed in the text) indicating the full asymmetric co-training is better than “only UPM” or “only MPM” variants (as described in the paper’s ablation discussion).
- **Efficiency tradeoff is at least partially quantified.** Table 4 reports per-iteration time/memory vs FreeMatch/RegMixMatch on CIFAR-100 (2 labels/class), with CaPT being closer to FreeMatch than RegMixMatch in compute while improving accuracy (Table 4, lines 242–248).

## Weaknesses

### Fatal
None.

### Major
- **Core algorithm specification is internally inconsistent around the co-pseudo label math (argmax vs distribution), making Eq. (13)–(15) ill-defined as written.**  
  The paper defines hard pseudo labels as indices: “\(\hat{q}^a = \arg \max(q^{w,a})\), \(\hat{q}^b = \arg \max(q^{w,b})\)” (Eq. 10, line 149). It then forms a *weighted sum* “\(\tilde{q}^c = \Gamma^a \hat{q}^a + \Gamma^b \hat{q}^b\)” (Eq. 13, line 161) and uses cross-entropy “\(CE(\tilde{q}_j^c, q_j^{s,a})\)” (Eq. 15, line 171), which requires \(\tilde{q}^c\) to be a (possibly soft) target *vector*, not a class index.  
  This is not a small notation nit: the **co-pseudo label fusion is the central novelty**, and as written a reader cannot unambiguously infer whether the targets are (one-hot) vectors, normalized mixtures, or something else (especially given the paper also discusses replacing low-confidence pseudo labels with all-zeros elsewhere). Clarifying the exact target representation and loss computation is necessary to evaluate soundness and to reproduce the method.

- **The paper’s strongest claimed regime (1 label/class) lacks basic robustness reporting (variance / multiple draws), despite the method’s own motivation emphasizing sensitivity to label choice/quality.**  
  Table 3 presents single-point accuracies for 1-shot CIFAR-10/100/EuroSAT (lines 236–241) with no “±” deviations, while the introduction explicitly argues performance depends strongly on *which* labeled example is chosen (Figure 1 discussion: prototypicality-ordered sets; lines 13–20). Because the main headline is a **very large discontinuity** at 1-shot (e.g., CIFAR-100: +21.38 over second best claimed in text, line 218–223), readers need evidence the result is stable over seeds and over labeled-set draws. As written in the main paper text, that key robustness evidence is not shown.

### Minor
- **Central framing claim (“breaking inherent label dependency”) is stronger than what the experiments alone establish, given the method explicitly injects substantial external prior via CLIP.**  
  The abstract states SSL is “inherently label-dependent” and CaPT “breaks” that dependency (Abstract, line 9). However, the empirical evidence primarily demonstrates “SSL + CLIP prior teacher > SSL alone” in low-label regimes (e.g., Table 3, Table 4). That is an important and valid contribution, but the stronger causal/structural claim about SSL itself is not directly isolated by the experiments presented in the main text.

### Trivial
None.

## Nice-to-Haves
- Report **mean ± std** (or confidence intervals) for Table 2 and especially Table 3, and explicitly specify the **1-shot labeled-set sampling protocol** (random seed strategy, number of draws, whether class exemplars are fixed), ideally aligning it with the paper’s own “label quality/prototypicality” motivation in Section 1.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **“Comparisons may be unfair due to CLIP preprocessing/prompting differences or unmatched training budgets.”** The paper does not provide enough concrete, on-page evidence of a specific mismatch (e.g., a stated different backbone capacity, different unlabeled set, different training steps) to keep this as a grounded criticism rather than speculation.  
- **“Theorem/appendix connection is missing.”** Any claim hinging on missing appendix/proof details is unreliable here due to extraction limitations; moreover, the review cannot verify whether the appendix clarifies this.

## Novel Insights
The paper’s most impressive empirical gains occur exactly where its own introduction argues SSL is highly sensitive to *which* labeled samples are chosen (prototypicality vs anti-prototypicality). That makes the absence of variance-over-draws in the 1-shot tables not just a generic “add error bars” request, but a direct tension with the paper’s motivating diagnosis—resolving it (by reporting robustness across labeled draws and perhaps stratifying by prototypicality) would substantially strengthen the causal story that CaPT reduces label dependence rather than merely being lucky on a particular 1-shot split.

## Suggestions
- **Fix the method specification:** explicitly define whether \(\hat{q}\) is an index, a one-hot vector, or a soft distribution; define whether \(\tilde{q}^c\) is normalized; and define the exact cross-entropy used when targets are weighted mixtures or can be all-zero.
- **Harden the 1-shot evidence:** re-run Table 3 over multiple labeled-set draws/seeds and report mean±std; explicitly state the labeled selection procedure; optionally include a prototypical vs anti-prototypical 1-shot slice to directly validate the Section 1 motivation.
- **Recalibrate claims:** present “breaking label dependency” as an empirical effect under a “CLIP prior teacher” assumption, and more clearly scope when/why it should or should not help.

## Score and Decision
**Originality:** High—an asymmetric SSL/CLIP co-training with co-pseudo labels is a concrete, nontrivial method design.  
**Importance:** High—robust SSL under extreme label scarcity is valuable, and the reported gains (if robust) are potentially impactful.  
**Support for claims:** Mixed—benchmark improvements are strong, but (i) the 1-shot headline lacks robustness reporting in the main text, and (ii) the core label-fusion math is ambiguous/inconsistent as written.  
**Experimental soundness:** Generally strong breadth, but the most central regime needs stronger statistical/protocol evidence.  
**Clarity:** Good overall, but the PFM equations around pseudo labels are currently a major clarity/soundness gap.  
**Community value:** Potentially high if the method spec and 1-shot robustness are clarified.

MY FINAL SCORE: <score>6.0</score>  
MY FINAL DECISION: <decision>Reject</decision>