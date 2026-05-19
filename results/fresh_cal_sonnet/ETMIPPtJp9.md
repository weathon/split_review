Now let me run the calibration search to bracket the paper's score.**Round 1 bracket: 4.5–6.5**. KARPA (4.6) is most similar in structure (training-free KGQA) but FiDeLiS has more components (deductive verification, beam search, ablations), and SubgraphRAG (6.0, accepted) has a comparable level of contribution. Let me narrow with Round 2.Now I have enough information to write the final review. Let me compile everything.

---

## Summary

FiDeLiS proposes a training-free retrieval-augmented method for Knowledge Graph Question Answering (KGQA), consisting of two components: Path-RAG (keyword-enhanced vector retrieval over KG entities/relations) and DVBS (a deductive-verification-guided beam search). Evaluated on three benchmarks (WebQSP, CWQ, CR-LT), it outperforms the same-backbone baseline ToG consistently across all settings and surpasses fine-tuned baselines in the GPT-4-turbo configuration. A thorough ablation study isolates each component's contribution.

---

## Strengths

- **Keyword-enhanced retrieval (Path-RAG) concretely improves recall over vanilla retrievers.** Figures 3(a)–(b) show Path-RAG achieving substantially higher coverage ratios over ground-truth paths than the cosine-similarity baseline. Table 3 further confirms that Path-RAG with OpenAI embeddings (79.32 Hits@1 on WebQSP) outperforms a vanilla retriever with the same backbone (72.35), isolating the keyword enrichment contribution.

- **Deductive verification yields measurably more accurate stopping.** Table `tab:termination_singals` shows FiDeLiS path depths (2.4/2.8/4.6 across datasets) are much closer to ground-truth depths (2.3/3.2/4.7) than ToG (3.1/4.1/5.2), directly supporting the claim that the termination mechanism avoids over-extension. Ablation in Table 2 attributes a 5.19 Hits@1 drop to removing the deductive verifier on WebQSP.

- **Comprehensive, systematic ablation study.** Table 2 removes each component—vanilla retriever, ToG-style retrieval, planning, beam search, and deductive verifier—and reports drops on three datasets. The beam-search component has by far the largest contribution (−18.97 Hits@1 on WebQSP); deductive verification and planning are secondary but consistent across all three datasets. This correctly characterizes the method's internal structure.

- **Cleanest comparison (same-backbone) shows consistent, meaningful gains.** FiDeLiS vs. ToG using identical backbones (GPT-3.5: 79.32 vs. 75.13 on WebQSP; 63.12 vs. 57.59 on CWQ; 67.34 vs. 62.48 on CR-LT; GPT-4: 84.39 vs. 81.84 on WebQSP) provides a well-controlled test that isolates the method's contribution over baseline retrieval+reasoning.

- **Efficiency advantage over ToG-equivalent.** Table `tab:runtime` shows 43.83s and 2,452 tokens per question (WebQSP) versus 74.26s and 6,437 tokens for the ToG-retrieval variant, while achieving higher Hits@1. The comparison also includes faster models (GPT-4o, GPT-4o-mini) showing scalability.

- **Error analysis motivates the design from a concrete gap.** Figure 3(c) quantifies RoG's reasoning-step validity at 67%, providing a concrete empirical basis for the paper's stepwise KG-constrained design.

---

## Weaknesses

### Fatal
None.

### Major

- **Backbone confound in the headline "training-free beats fine-tuned" claim.** Table 1 presents FiDeLiS (GPT-4-turbo) outperforming RoG (83.15 → 84.39 on WebQSP Hits@1) and DeCAF as a central result. However, RoG, DeCAF, NSM, CBR-KBQA, and KD-CoT all use substantially smaller fine-tuned models. The abstract and introduction frame this as a demonstration that training-free methods can surpass fine-tuned ones, but the actual experiment cannot support this framing—the backbone advantage of GPT-4-turbo (which already reaches 72.11% with CoT alone, per Table 1) is uncontrolled. The paper should clarify that the "outperforms fine-tuned" comparison is backbone-inclusive, and should not present it as evidence for a methodological advantage over fine-tuned approaches. The fair controlled comparison (FiDeLiS vs. ToG with same backbone) does support real gains, but that is a narrower claim than what the introduction makes.

- **Deductive verification mechanism is underspecified in the main text.** The binary criterion $C(q', s^t, s^{1:t-1}) \in \{0,1\}$ in Equation 4 is the paper's most novel element, but $q'$ appears without definition—it differs from the query $q$ used throughout without explanation, and the definition in Eq. 3 uses $C(x, s^t, s^{1:t-1})$ with $x$, while Eq. 4 uses $q'$, creating a notation inconsistency alongside the semantic gap. No example is shown in the main text for what counts as "deducible." The ablation validates the component quantitatively, and the path-depth analysis in Table `tab:termination_singals` corroborates it indirectly, but a reader cannot understand or audit what the deductive verification actually checks from the main text alone.

### Minor

- **FiDeLiS's own faithfulness ratio is never reported.** The paper motivates its design by showing RoG achieves only 67% valid reasoning steps. By construction, FiDeLiS constrains every step to KG-retrieved candidates, so its validity ratio should approach 100%. Not reporting this leaves the paper's headline "faithful reasoning" claim asymmetric: the problem is demonstrated for the baseline but the proposed method's faithfulness is not directly quantified, only inferred.

- **CR-LT dataset is never introduced.** It appears in Tables 1, 2, 3, and 4 but is never described: its source KG, size, question type, and reasoning depth distribution are unknown to the reader. For WebQSP and CWQ, existing literature provides context; for CR-LT there is none. This affects how much weight to assign to CR-LT results.

- **Notation inconsistency: Top$_k$ vs Top$_B$.** Equation 2 (beam search) uses Top$_k$ while Equation 3 (overall DVBS objective) uses Top$_B$, with no explanation of the switch. The text states $k=4$ as the default. This creates unnecessary confusion about whether the beam width is $k$ or $B$.

### Trivial

- **Redundant definitions across Sections 2 and 3.** Definitions 1–3 in Section 2 (Preliminary) are repeated nearly verbatim as Definitions 1–4 in the Notation block at the start of Section 3 (Method), wasting space that could be used to better specify the method.

- **Hyperparameter $\alpha$ in Equation 3 is never analyzed.** The paper identifies $\alpha$ as governing the lookahead tradeoff but reports no default value, no sensitivity analysis, and no ablation of its effect. This is a separate design dimension from Path-RAG vs. vanilla retriever.

---

## Nice-to-Haves

- Report FiDeLiS's own validity ratio (expected ~100%) alongside RoG's 67% — this would directly close the faithfulness argument the paper builds.
- Provide a one-sentence description of CR-LT (source, size, reasoning complexity) so readers can interpret those results without prior knowledge.
- Show, even briefly, what kinds of questions benefit most from the deductive verifier (e.g., multi-hop vs. single-hop) using the average-depth data in Table `tab:termination_singals`.
- The $\alpha$ sensitivity analysis for Path-RAG's scoring function would be a useful short ablation.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "1.7x faster claim compares against an ablated variant, not ToG."** Table `tab:runtime` compares FiDeLiS (43.83s) to "w/o Path-RAG using ToG" (74.26s). The "w/o Path-RAG using ToG" variant uses ToG's retrieval in FiDeLiS's framework, which is functionally equivalent to ToG's retrieval method—this is a valid comparison even if the label is imprecise. *Removed because the comparison is legitimate; at worst it is a minor labeling issue*.

- **Harsh Critic: "Case study 'Iranian Rail' vs 'Iranian rial' mismatch."** The question in Table `tab:case` says "Iranian Rail" but the reasoning paths use "Iranian rial." This is likely a formatting/parser artifact in the extracted text (rail vs. rial), not an author error in the original submission. *Removed per the hard rule against parser artifacts.*

- **Strength Finder: "Training-free method outperforms fine-tuned baselines on three datasets"** listed as an unqualified strength. This conflicts with the backbone confound weakness above. *Removed as a standalone strength; the fair same-backbone comparison is retained as a genuine strength.*

- **Harsh Critic: "The error analysis that motivates the grounding approach is one-sided."** Partially retained as Minor weakness (missing FiDeLiS's own validity ratio), but the criticism that FiDeLiS "never reports" this is converted from Major to Minor since the construction of the method (KG-constrained steps) implicitly guarantees near-100% validity—the gap is presentation, not evidence of a hidden problem.

---

## Novel Insights

The paper's most interesting structural finding, surfaced clearly by the ablation, is that **beam search** is by far the dominant contributor to performance (−18.97 Hits@1 when removed on WebQSP), dwarfing the novel deductive verification (−5.19) and planning (−3.09). This suggests that iterative path exploration with beam search is substantially underused in KGQA systems that rely on single-pass retrieval or greedy reasoning, and that the primary bottleneck being solved here is the exploration strategy rather than the stopping criterion per se. The deductive verification serves as a precision refinement on top of an already high-performing beam search scaffold.

---

## Suggestions

1. **Reframe the backbone-conflated comparisons explicitly.** In Table 1, add a column or footnote clarifying that fine-tuned baselines use smaller models, and soften the "training-free beats fine-tuned" framing in the introduction to "outperforms fine-tuned baselines when paired with a sufficiently capable LLM backbone."
2. **Define $q'$ and resolve the $x$ vs. $q'$ notation inconsistency** in the deductive verification criterion (Equations 3–4).
3. **Add CR-LT description** (at minimum: source KG, dataset size, average reasoning depth distribution).
4. **Report FiDeLiS's validity ratio** alongside RoG's 67% in the faithfulness analysis section.

---

## Score and Decision

**Calibration Anchors Across All Rounds:**

| Path | Avg Score | Round | Comparison to FiDeLiS |
|---|---|---|---|
| `ds3Tcnrte8.md` (QAP, KG prompting for MCQA) | 3.00 | R1-weak | Much weaker — no novel retrieval mechanism, limited scope |
| `fMaEbeJGpp.md` (Multimodal RAG QA) | 2.50 | R1-weak | Much weaker — engineering benchmark |
| `a2rSx6t4EV.md` (EDU-RAG benchmark) | 2.33 | R1-weak | Much weaker — benchmark paper, no method contribution |
| `oqRe1KvD17.md` (Reward-RAG) | 3.00 | R1-weak | Weaker — training-based; limited experiments |
| `EVuANndPlX.md` (GNN-RAG) | 5.60 | R1-mid | Roughly comparable — similar scope (KGQA), similar backbone confound concerns, FiDeLiS has more thorough ablation |
| `JvkuZZ04O7.md` (SubgraphRAG) | 6.00 | R1-mid | Slightly above FiDeLiS — cleaner architecture and smaller models without fine-tuning, similar experiment coverage |
| `DOA1WSPZSi.md` (KG trustworthiness QA) | 4.75 | R1-mid | Below FiDeLiS — benchmark construction paper with no new method |
| `Hw1tOjCWBZ.md` (KARPA) | 4.60 | R1-mid | Below FiDeLiS — fewer components, less rigorous ablation, similar backbone issue |
| `GGlpykXDCa.md` (MMQA multi-table) | 8.00 | R1-strong | Much stronger — introduces a new benchmark with clean evaluation |
| `WbWtOYIzIK.md` (Knowledge Card) | 8.00 | R1-strong | Much stronger — novel modular plug-in architecture with broader scope |
| `07yvxWDSla.md` (Synthetic continued pretraining) | 8.00 | R1-strong | Much stronger — novel synthetic data pipeline with strong theoretical grounding |
| `Iyrtb9EJBp.md` (Grounded Attributions RAG) | 8.00 | R1-strong | Much stronger — introduces new metric and training method |
| `6embY8aclt.md` (GCR: faithful KG reasoning) | 4.75 | R2 | Most directly comparable — same "faithful KGQA" goal, similar KG-constrained reasoning; GCR is technically more novel (KG-Trie) but less comprehensive in experiments; FiDeLiS has better ablation and more datasets |
| `Vx3o2tUErQ.md` (REPANA) | 5.75 | R2 | Slightly above FiDeLiS — program induction approach, multiple datasets, cleaner formulation |
| `iSTMsye6SD.md` (knowledge-intensive benchmark) | 5.25 | R2 | Comparable — benchmark + evaluation paper |
| `oMFOKjwaRS.md` (KG-SFT) | 5.80 | R2 | Slightly above FiDeLiS — 15 domains, but fine-tuning paper, different task |
| `tqhAA26vXE.md` (ChatKBQA) | 5.67 | R2 | Roughly comparable — also KGQA, generate-then-retrieve framework |

**Round 1 bracket: 4.5–6.5**

**Round 2 narrowing:** The two most comparable anchors are GCR (4.75, rejected) and SubgraphRAG (6.0, accepted). FiDeLiS is better than GCR in experimental breadth (3 datasets vs. 2, more thorough ablation) but similar in the core faithfulness-on-KG framing. FiDeLiS is below SubgraphRAG in methodological clarity (SubgraphRAG has a lighter, cleaner architecture; FiDeLiS has the backbone confound and underspecification). KARPA (4.6, rejected) is the floor: FiDeLiS is clearly stronger due to more components and rigorous ablation. GNN-RAG (5.6, rejected) and ChatKBQA (5.67) represent a good mid-point. FiDeLiS's controlled comparison (same backbone vs. ToG) is solid, and the ablation is genuinely comprehensive. However, the backbone framing issue and deductive verification underspecification are real. 

Positioning: FiDeLiS sits between KARPA (4.6) and GNN-RAG/SubgraphRAG (5.6–6.0), closer to the GNN-RAG band. Score: **5.0**.

**Evaluation on key axes:**
- *Originality*: Moderate — combining keyword-enhanced retrieval, deductive verification, and beam search for KGQA is a reasonable contribution but the components individually build on existing work (ToG, CoT planning, standard beam search).
- *Importance of research question*: Good — faithful, grounded reasoning in KGQA is an active and important problem.
- *Claims vs. support*: Mixed — the same-backbone comparison is well-supported; the "beats fine-tuned" framing is overclaimed.
- *Soundness of experiments*: Good for ablation and robustness analysis; weak for the main headline comparison.
- *Clarity of writing*: Moderate — redundant definitions, underspecified key component.
- *Value to the community*: Moderate — the practical system is useful and the efficiency results are informative.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>