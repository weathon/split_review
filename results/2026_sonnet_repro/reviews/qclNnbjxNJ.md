Now let me do the calibration searches to anchor the score.**Round 1 bracket: 6–8.** The paper under review is clearly above the weak papers (3–4) and comparable to strong work like xByvdb3DCm (score 8, CDIS, which is actually cited as a baseline). Let me narrow the range.Now I have sufficient calibration data to write the review. Let me synthesize.

---

## Summary

This paper tackles the underexplored problem of **post-treatment selection** in interventional causal discovery with latent confounders — the selective inclusion of samples *after* interventions (e.g., cells that pass quality control in gene perturbation studies). The authors show that existing frameworks cannot distinguish this selection from genuine causal responses because both produce the same CI signature (variant marginal, invariant conditional distributions). They introduce a new causal formulation with an augmented DAG that explicitly includes a selection variable S, characterize the resulting *FI*-Markov equivalence class, propose a new graphical representation (*F*-PAG) with novel edge marks, and develop the F-FCI algorithm — proved sound and complete (with a qualification on Type II inducing nodes). Experiments on synthetic graphs (10–25 nodes) and real single-cell perturbation data (Norman et al.) support the claims.

---

## Strengths

- **Clear non-identifiability motivation (Figure 1, Section 2.2):** The paper concretely shows that existing frameworks conflate Figures 1(a) and 1(b) (selection-via-latent-confounder vs. direct causation) and 1(c) and 1(d) (direct selection vs. latent-confounded link), establishing an undeniable gap in prior art.

- **Principled causal formulation (Definition 1, Eq. 1):** The augmented DAG $\text{Augz}(\mathcal{G})$ unifies observational and interventional data under selection bias via a selection variable S and intervention indicators ψ, with a clean joint factorization. The extension of the standard Markov properties to this setting (Theorem 1) is rigorous and non-trivial.

- **Novel FI-Markov equivalence and F-PAG (Definitions 2, 5; Theorem 2):** The paper defines a strictly finer equivalence class than PAG, characterized by four mark types (tail, arrowhead, square, circle) and eight edge types. The graphical criteria in Theorem 2 and Lemmas 2–4 directly connect d-separation in the augmented DAG to the observable CI signatures, providing a clean theoretical foundation.

- **Soundness and completeness (Theorems 3–4):** F-FCI is proved sound (Theorem 3) and complete (Theorem 4), meaning it exactly recovers the FI-Markov equivalence class under oracle CIs. Adding completeness on top of soundness is a meaningful advance over the closely related CDIS (Dai et al., 2025), which proves soundness only.

- **Type I inducing node disambiguation mechanism (Definition 6, Step 2.3):** The use of hard interventions on intermediate Type I inducing nodes (nodes $X_n$ with $\dashv\square$ pattern) to resolve $\circ\to$ ambiguity is the paper's most original algorithmic contribution. The mechanism — testing $\psi_n \perp\!\!\!\perp X_i$ to detect whether an inducing path carries a real causal link — is elegant and is grounded in Theorem 1's characterization.

- **Empirical validation at scale (Figure 6, Section 5.2):** Comparison on synthetic graphs with 10–25 nodes and 2–3 selection/latent-confounder variables, plus real-world Norman scRNA-seq perturbation data evaluated via Enrichr, shows consistent improvements in DAG Precision and SHD over six baselines. Confidence intervals over 10 graphs are provided.

---

## Weaknesses

### Fatal
None.

### Major

- **Completeness claim in Theorem 4 is stated more broadly than the result supports.** Section 6 acknowledges: *"The identification of direct causal links and selection structures depends critically on the presence of Type I inducing nodes. One future direction is how to identify the causal structure along inducing paths composed solely of Type II inducing nodes."* This means the algorithm cannot handle graphs where all inducing paths between two variables contain only Type II nodes (adjacent square–square configurations). Theorem 4's statement — *"Each type of substructures represented by tail, arrowhead, square, ▲, and ▼ … can be identified by different types of CI patterns"* — does not explicitly state this side condition. Since the abstract and introduction both claim the algorithm is "provably sound and complete," readers will assume unconditional completeness. Theorem 4 should be stated with explicit side conditions, or a forward reference to the limitation should appear immediately after the theorem, not just in the conclusion section.

- **Experimental evaluation does not directly demonstrate the disambiguation mechanism.** All six baselines (GIES, IGSP, UT-IGSP, JCI-GSP, FCI-interven, CDIS) are explicitly not designed to handle post-treatment selection; data is generated with selection. This makes F-FCI's advantage over them partially by construction. The evaluation would be more informative with: (a) a condition with no selection bias to confirm F-FCI does not degrade relative to baselines in that regime; (b) an ablation removing Step 2.3 (Type I inducing node disambiguation) to isolate this novel component's contribution. Table 1 (selection identification performance), mentioned briefly in Section 5.1 as being in the appendix, is actually the most direct test of the central claim and deserves a place in the main paper.

### Minor

- **DAG Precision metric may systematically favor conservative predictors.** F-FCI, by correctly attributing some dependencies to selection rather than causation, will naturally output fewer edges than baselines that cannot make this distinction, boosting its precision score. F1-score and recall are deferred to Figure 10 in the appendix and SHD is also shown, which partially mitigates this concern, but the main paper should acknowledge this dynamics explicitly.

- **Step 2.2 orientation rules lack explicit CI-pattern matching conditions in the main text.** The six orientation rules in Algorithm 1 are each supposed to correspond to a distinct CI-pattern tuple; Figure 4(i) provides the mapping, but the pseudocode as written should cross-reference Figure 4 explicitly for each case. The connection between the table in Figure 4 and each "Orient" line in Step 2.2 is left to the reader to reconstruct.

- **Requirement that selection operates on at least two observed variables is stated in passing (Section 3.1) but never fully justified.** The sentence "we assume selection works on at least two observed variables" is critical for the symmetric-CI detection logic in Step 2.2, but there is no explanation of what failure modes arise when selection operates on only a single variable, or how the algorithm degrades. A brief justification would clarify the model's boundary conditions.

### Trivial

- The notation for edge marks in Definition 5 (▲ vs. ▼ used for different inducing path types) is introduced tersely; Definition 6 and Figure 5 together clarify the distinction, but a one-line plain-English summary immediately following Definition 5 would ease parsing.

---

## Nice-to-Haves

- A focused synthetic experiment directly constructing pairs of graphs that alternate between "direct causation" (Figure 1(b)) and "selection-mediated dependence" (Figure 1(a)) as ground truth, showing F-FCI correctly identifies which is which case-by-case, would be a decisive demonstration of the core claim.

- Step 2.3 and Type I inducing node disambiguation are the most novel algorithmic components. Statistics on how frequently Type I inducing paths arise in the random graphs tested, and how often Step 2.3 actually fires and resolves an ambiguity, would ground the theoretical contribution in observed empirical behavior.

- For the Norman real-world study, an explicit example of an identified selection pattern (a dependency correctly flagged as arising from quality-control selection rather than biological causation) with its biological interpretation would strengthen Section 5.2 considerably.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

**From the harsh critic:**
- *Algorithm Step 2.2 rendering problem*: Removed. The conditions in Step 2.2 all appear as `(⊥,⊥,⊥,⊥)` in the extracted text because `⊥` and `⊥̸` (not-independent) are indistinguishable in the parser output. This is a confirmed PDF-parsing artifact, not an error in the submission. Per hard rules, such formatting/symbol artifacts must be removed.

- *Functions f and f_s proportions unspecified*: Removed. This is a reproducibility nitpick about trivial implementation details not expected in a submission.

- *Noise distribution Unif([0,2]∪[2,4]) motivation unspecified*: Removed as a pure presentation nitpick that does not affect any result. The choice is unusual but not erroneous.

- *Proof of Theorem 2 in stripped appendix*: Removed. The rules explicitly exclude criticisms about missing appendix content, which the parser strips from all papers.

- *"Marks" doing significant work in Theorem 2*: Removed as too minor a notational concern to retain.

**From the strength finder:**
- All eight strengths listed are concrete, specific, and well-grounded in the paper. All are retained.

---

## Novel Insights

The paper's most structurally interesting observation — that post-treatment selection and direct causation produce *identical* CI signatures (variant marginal, invariant conditional) in the standard augmented-DAG framework, yet can be disambiguated by exploiting the *differential responses* of selection vs. causation under additional hard interventions on intermediate nodes — is a clean and genuinely surprising result. The key insight is that a selection-mediated inducing path (Figure 4(b)) can be unmasked by intervening on a Type I inducing node $X_n$: if $\psi_n \perp\!\!\!\perp X_i$, the path is selection-mediated; if not, it reflects real causal propagation. This "third intervention for disambiguation" logic elegantly extends the standard FCI/augmented-MAG machinery without requiring parametric assumptions. It also establishes a clear and testable relationship between graph structure (Type I vs. Type II inducing nodes) and the limits of identifiability — a relationship that the authors honestly acknowledge as incomplete in the Type II case.

---

## Suggestions

1. Move Table 1 (selection identification performance) to the main body of Section 5.1 — it is the most direct test of the paper's central claim and should not be relegated to an appendix.
2. Add a no-selection-bias experimental condition to confirm F-FCI's performance does not degrade in the absence of the problem it was designed for.
3. Add an ablation removing Step 2.3 to quantify the specific contribution of Type I inducing node disambiguation.
4. Revise Theorem 4 to include explicit side conditions (or immediately forward-reference the limitation), so that "completeness" is not read as unconditional.
5. In Section 5.1, state the proportion of linear/square/sin/tanh functions used in f and f_s to aid reproducibility.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| xByvdb3DCm (When Selection meets Intervention / CDIS) | 8.00 | R1/R2 | Directly comparable: pre-treatment selection in interventional causal discovery. Proves soundness only. Paper under review adds completeness (with qualification) and harder post-treatment setting. Similar or slightly stronger contribution. |
| u63OVngeSp (Deriving Causal Order from Single-Variable Interventions) | 7.00 | R2 | Comparable rigor, theoretical guarantees, clean experiments. The paper under review has a harder setting and richer theory, but also more caveats in completeness. |
| BZYIEw4mcY (Efficient Causal Discovery with Latent Variables) | 6.00 | R1/R2 | Accepted, strong theory but presentation issues and limited experiments. Paper under review is stronger on both theory and experiments. |
| fGhr39bqZa (Recovery of Causal Graph via Homologous Surrogates) | 6.00 | R1/R2 | Accepted, comparable theory scope. Paper under review is similarly rigorous but targets a harder problem setting. |
| nHkMm0ywWm (Structural Estimation of Partially Observed LiNGAM) | 6.50 | R2 | Similar profile. Paper under review is stronger in experimental scale and addresses a more widely applicable problem. |
| G5KbDVAlI6 (GISL: GRN Inference under Selection and Latent Confounders) | 4.00 | R1 | Closely related but rejected. Much smaller scale (5–9 nodes), weaker theory, limited baselines. Paper under review is clearly stronger. |
| ZXs3pkmrRG (Test-Time Learning for Causal Structure) | 5.50 | R1 | Comparable broad area but different technical approach. Paper under review is more formally rigorous. |

**Round 1 bracket:** 6–8.

**Round 2 narrowing:** The paper under review is clearly above the 6.0 anchors (BZYIEw4mcY, fGhr39bqZa), which have presentation/experimental limitations not present here. It is comparable to u63OVngeSp (7.0) in rigor and experimental quality. Most importantly, the closest topical comparator is xByvdb3DCm (CDIS, score 8.0): the paper under review solves the harder post-treatment selection problem (CDIS is its baseline), proves completeness in addition to soundness (CDIS does not), and adds a more expressive graphical representation. The two weaknesses — an unqualified completeness claim in the theorem statement and missing ablation/no-selection baseline — are real but do not undermine the contribution's core validity. The paper is somewhat better than u63OVngeSp (7.0) and roughly comparable to xByvdb3DCm (8.0) minus the completeness caveat.

**Final score: 7.5** — positioned above the 7.0 anchor (paper is more rigorous and addresses a harder problem), and slightly below the 8.0 anchor (xByvdb3DCm has cleaner experimental framing and an unconditional soundness claim; the paper under review has a stronger but qualified completeness claim and evaluation design gaps that need addressing).

**Decision: Accept** — The paper makes a genuine, well-motivated, and formally grounded contribution to interventional causal discovery under a condition (post-treatment selection) that existing frameworks cannot handle. The theoretical machinery is sound, the empirical evaluation is credible, and the identified limitations are acknowledged honestly. The major weaknesses — unqualified completeness claim and missing ablation — are addressable in a revision.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>