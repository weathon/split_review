Now I have all the evidence I need. Let me write the consolidated review.

## Summary

This paper introduces GOT-D, a data selection method for "pre-fine-tuning" LLMs (warming up fine-tuning on unlabeled data before task-specific fine-tuning). The core insight is that when selecting warm-up data for a pre-trained model, one should prioritize samples that shift the pre-training distribution *toward* the target task distribution, rather than samples that merely match the target. This contrasts with prior distribution-matching approaches. The method computes the gradient of the Optimal Transport (OT) distance between a candidate set (proxy for pre-training distribution) and the target data, then selects samples with the most negative gradients. The paper evaluates GOT-D on detoxification (GPT-2), domain-specific NLU (BERT), and GLUE benchmarks, reporting consistent improvements over baselines like DSIR, DAPT, and RTP.

## Strengths

1. **Novel and well-motivated conceptual framing.** The paper identifies a genuine limitation of distribution-matching for data selection in fine-tuning: since the model is already pre-trained on D_P, samples already well-represented in D_P contribute little. The cat/dog example (Fig. 3) provides excellent intuition for why one should select data that fills gaps in the pre-training distribution relative to the target, rather than data that matches the target distribution alone. This is a genuinely useful conceptual contribution.

2. **Broad evaluation across diverse tasks and models.** The paper evaluates on three substantially different settings — NLG (toxicity reduction with GPT-2), domain-specific NLU (8 tasks across Biomed/CS/News/Reviews with BERT), and general NLU (GLUE benchmark) — and includes zero-shot experiments with models up to 2.7B. The detoxification experiment (Table 1) shows particularly strong results: GOT-D_clean with 20K samples achieves toxicity probability of 0.28 on toxic prompts vs. GPT-2 base at 0.67, substantially outperforming RTP (0.44).

3. **Computational efficiency.** The method requires solving a single OT problem and ranking gradients, which is O(N log N) in practice and can be parallelized on GPU. The paper claims selection completes in minutes for millions of samples, which — if verified — would be a meaningful practical advantage over gradient-retraining methods.

4. **Effective in low-resource regimes.** The GLUE experiments with 5K labeled target data (Table 4, lower half) and the resource-constrained domain adaptation (Table 3, 50K selected + 5K labeled) show that GOT-D maintains advantages precisely where data is scarcest — the setting most relevant for practical "emerging task" scenarios.

## Weaknesses

### Major

1. **The theoretical foundation (Lemma 1, Theorem 1) is not rigorous and overclaims formal optimality.** 
   
   Lemma 1 claims that light fine-tuning on D_U "equates to" minimizing loss on the weighted combination λ·D_U + (1-λ)·D_P. This is presented as a formal lemma with proof in Appendix B.1, but the only supporting reference in the main text is to scaling-laws "effective datasize" (Hernandez et al., 2021), which is a *descriptive heuristic* about how performance scales with data, not a *prescriptive equivalence* about the optimization objective. Fine-tuning solves min_θ L(D_U; θ) starting from pre-trained weights; it does not solve min_θ [λL(D_U; θ) + (1-λ)L(D_P; θ)], and the paper provides no argument that these two problems produce the same solution. Since Theorem 1's derivation depends on Lemma 1 (the effective data distribution D_M is central to the bound), the theoretical claims of optimality are not well supported. 

   Furthermore, Theorem 1 claims the optimal selection is given by ∂OT(D_S, D_R)/∂D_S. Remark 1 invokes a first-order Taylor expansion along the "update D_U," but the derivation connects a continuous derivative (with respect to probability mass in D_S) to a discrete subset selection (choosing N_0 specific samples from D_S). The gap between continuous OT gradient and discrete data selection is not addressed.

   **Impact:** The paper's claimed theoretical contribution ("optimality under certain conditions") is overstated. The core intuition (shift distribution, don't just match it) can stand on its own as a heuristic motivation, but the formal framing as Lemma 1 and Theorem 1 invites scrutiny the paper cannot currently withstand.

2. **Internal incoherence between the theoretical assumption and key experiments.** The theoretical development assumes D_S is proximate to D_P (OT(D_P, D_S) ≤ ε). The paper then applies GOT-D to domain adaptation tasks (Section 3.2) using BERT (pre-trained on Wikipedia + BooksCorpus) with candidate data from biomedical (PubMed) and CS (ACL) domains. For these domains, the assumption that D_S ≈ D_P is almost certainly violated. The paper acknowledges this indirectly as a "limitation" (line 117: "not intended for tasks requiring domain knowledge very different from the scope of pre-training data") but proceeds with the experiments anyway. The positive results under assumption violation suggest either (a) the theory is unnecessary, or (b) the method works for reasons unrelated to the theoretical framing. Either way, the paper does not reconcile this tension, which weakens the overall narrative.

### Minor

3. **Empirical margins are often small and statistical significance is not assessed.** While the detoxification results are large, the domain adaptation gains (Table 2) are often under 1% (e.g., GOT-D 83.83 avg vs. DSIR 82.98 — a 0.85% improvement), and many comparisons are within 1 standard deviation (e.g., RCT: 87.21±0.15 vs. 87.14±0.13). The GLUE results (Table 4) show similarly small margins over DSIR and TAPT/c (e.g., 78.43 vs. 78.32 for the 5K setting). The paper claims GOT-D "consistently surpasses" baselines but does not report significance tests or discuss effect sizes. This makes it hard to judge whether the improvements are robust.

4. **The DAPT baseline comparison lacks sufficient methodological detail.** DAPT (Gururangan et al., 2020) was designed for large-scale continued pre-training on the full domain corpus. The paper constrains DAPT to the same 150K selection budget as GOT-D but does not describe *how* the 150K samples were selected for DAPT (random? first-N? frequency-based?). Since DAPT is not inherently a selection method, forcing a budget constraint without specifying the selection mechanism makes the comparison difficult to interpret.

5. **The feature representation for OT computation is not specified.** The paper defines the OT cost as L1-norm but does not state how text samples are featurized (e.g., sentence embeddings from a frozen model, bag-of-words, n-gram frequencies). OT distance quality depends heavily on the feature space, and this omission hinders reproducibility.

6. **The "30% toxicity reduction" claim in the abstract is ambiguous.** The paper states "reducing the toxicity level of GPT-2 by 30% with 10K samples" without specifying which of the four toxicity metrics in Table 1 this refers to, nor from which baseline. No entry in Table 1 corresponds precisely to a 30% relative reduction from the GPT-2 base.

7. **Computational efficiency is claimed but not quantified in the main text.** The abstract claims "scaling to millions of samples within a single GPU hour" and the text says "takes a few minutes for millions of samples," but no wall-clock runtime numbers or comparisons to baseline selection methods are presented in the main paper. Since efficiency is a stated goal (G3), this should be supported with measurements.

### Trivial

- None that survived filtering.

## Nice-to-Haves
- Include runtime comparison (wall-clock time for selection on, say, 1M candidates) for GOT-D vs. DSIR vs. random in the main paper.
- Report statistical significance (e.g., paired bootstrap or Wilcoxon signed-rank across tasks) to quantify confidence in improvements.
- Ablate the sensitivity to the choice of text features/embeddings used in the OT cost function.
- Add an ablation study varying λ or selection budget more finely to verify that the gradient-based selection consistently outperforms distribution-matching.

## Removed Points
- **"DAPT comparison is staged to favor GOT-D"** (speculative claim not supported by paper content).
- **"RTP outperformance is suspicious"** (speculative; no concrete evidence of a confound; the paper reports consistent results across two toxicity APIs).
- **"Missing appendix/proof"** (parser artifact — appendices exist in the original submission).
- **"Missing related works"** (cannot verify external knowledge of missing works).
- **"Formatting/typo nitpicks"** (parser artifacts, not author errors).
- **"Reproducibility: undisclosed hyperparameters/trivial details"** (these are standard for the field and/or deferred to appendix).

## Novel Insights
None beyond the paper's own contributions. The key insight — that pre-fine-tuning selection should aim to shift the pre-training distribution toward the target rather than match the target — is the paper's main contribution and is well-articulated. No novel synthesis emerges from the reviews that the paper itself does not convey.

## Suggestions
1. **Reframe the theory as a principled heuristic, not a theorem.** The core intuition is valuable and can motivate the method without claiming formal optimality. Replace Lemma 1 and Theorem 1 with a clear development of the idea that, under light fine-tuning, the model's effective distribution is influenced by both D_U and D_P (citing scaling laws), and that the gradient of OT(D_S, D_R) provides a sensible criterion for selecting samples that reduce OT distance to the target. This would be honest about the approximation and avoid overclaiming.

2. **Specify the text representation used for OT computation** (e.g., document embeddings from a frozen sentence encoder, or n-gram features). This is essential for reproducibility.

3. **Address the assumption-theory gap explicitly.** Either justify why GOT-D works even when D_S is not proximate to D_P, or limit experiments to settings where the assumption plausibly holds.

4. **Run significance tests** (e.g., paired bootstrap across tasks/seeds) and report which improvements are statistically robust.

5. **Include a runtime table in the main paper** comparing GOT-D to DSIR on wall-clock time for fixed dataset sizes.

## Score and Decision

### Calibration

**Round 1 — Bracketing:**
- Weak anchors (avg < 3.5): KpC3dPumJj (3.25), EOPLy80bBm (3.0), OdoS6cH8MP (2.0), z4Ho599uOL (3.0), EVZnnhtMNX (3.0) — these are withdrawn/reject papers well below the paper under review.
- Middle anchors (3.5–7.5): Fty0wTcemV/DELIFT (6.0, Accept Poster), qUJsX3XMBH/Rethinking (4.4, Reject), FAfxvdv1Dy/STAFF (6.5, Accept Poster), huuKoVQnB0/PPL-Corr (6.0, Accept Poster), 3NnfJnbJT2/GIO (7.0, Accept Spotlight).
- Strong anchors (>7.5): dhAL5fy8wS/PDS (8.0, Oral), tPNHOoZFl9/LearningDynamics (8.0, Oral), f4gF6AIHRy/DiSF (8.0, Oral) — these are clearly above the paper's quality.

**Round 1 bracket:** [4.5, 6.5]

**Round 2 — Narrowing:**
- (4.5, 6.0) band: 1fwZJzGdKj/Multi-Agent (5.5, Reject), 6M5G5hNiAU/HowAbilities (4.67, Withdrawn), 8EM1A6qfX5/Unearthing (5.0, Reject), 79ZkWgY2FI/Small-to-Large (5.25, Accept Poster), E7ecidOeCE/GATEAU (5.0, Withdrawn).
- (6.0, 7.5) band: 3NnfJnbJT2/GIO (7.0, Spotlight), FAfxvdv1Dy/STAFF (6.5, Poster), bAFVlpFQvT/CoLM (6.75, Poster).

The paper is closer to the 5.0–5.5 anchors than to the 6.0+ ones. Compared to DELIFT (6.0, Poster): GOT-D has a more novel conceptual framing (shift vs. match) but weaker execution — DELIFT's theory is clean and its empirical results are stronger (70% data reduction without loss vs. ~1% improvements). Compared to "Multi-Agent" (5.5, Reject): GOT-D has a cleaner, more focused contribution. Compared to "Unearthing" (5.0, Reject): GOT-D has a more principled approach but similar issues of overclaim and modest results. The paper sits comfortably above the 4.5 band but does not reach the 6+ band due to the theoretical overreach and modest empirical margins.

**Final score:** 5.5 — The paper presents a genuinely useful conceptual contribution and broad empirical evaluation, but the theoretical overclaim is a significant weakness, and the margins are often small. The paper would benefit from reframing the theory as a heuristic.

**Decision rationale:** The core idea is interesting and the method is simple and fast. However, the formal theoretical claims (Lemma 1, Theorem 1) are not adequately supported and invite valid skepticism. Combined with modest empirical margins and unresolved tension between theory and experimental design, the paper in its current form does not meet the bar for a top venue.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>